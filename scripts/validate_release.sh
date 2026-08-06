#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$ROOT/.build/ci"
ARTIFACT_DIR="$ROOT/.build/artifacts"
RELEASE_DIR="$ROOT/releases/v1.0"

rm -rf "$BUILD_DIR" "$ARTIFACT_DIR"
mkdir -p "$BUILD_DIR" "$ARTIFACT_DIR"

check_pdf_structure() {
  local pdf="$1"
  if command -v qpdf >/dev/null 2>&1; then
    check_pdf_structure "$pdf"
  else
    python - "$pdf" <<'PY_FITZ'
import sys
import fitz
path = sys.argv[1]
doc = fitz.open(path)
assert doc.page_count > 0
for page in doc:
    page.get_text("text")
doc.close()
PY_FITZ
  fi
}

for stem in main supplement; do
  generated="$ROOT/paper/${stem}.pdf"
  test -s "$generated"
  check_pdf_structure "$generated"
  pages="$(pdfinfo "$generated" | awk '/^Pages:/ {print $2}')"
  test -n "$pages"
  test "$pages" -gt 0

  pdftotext "$generated" "$BUILD_DIR/${stem}.txt"
  test -s "$BUILD_DIR/${stem}.txt"
  if grep -Eiq 'TODO|FIXME|TBD|\?\?\?' "$BUILD_DIR/${stem}.txt"; then
    echo "Draft placeholder found in ${stem}.pdf" >&2
    exit 1
  fi

  while IFS= read -r embedded; do
    test "$embedded" = "yes"
  done < <(pdffonts "$generated" | awk 'NR>2 {print $(NF-4)}')

  mkdir -p "$BUILD_DIR/${stem}-pages"
  pdftoppm -png -r 110 "$generated" "$BUILD_DIR/${stem}-pages/page" >/dev/null 2>&1
  rendered="$(find "$BUILD_DIR/${stem}-pages" -name 'page-*.png' -type f -size +5k | wc -l)"
  test "$rendered" -eq "$pages"
done

main_release="$RELEASE_DIR/Architecture_Before_the_Formula_v1.0.pdf"
supp_release="$RELEASE_DIR/Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf"

for pdf in "$main_release" "$supp_release"; do
  test -s "$pdf"
  check_pdf_structure "$pdf"
done

normalize_text() {
  pdftotext "$1" - | tr '\n\r\t' '   ' | tr -s '[:space:]' ' '
}

diff -u <(normalize_text "$ROOT/paper/main.pdf") <(normalize_text "$main_release")
diff -u <(normalize_text "$ROOT/paper/supplement.pdf") <(normalize_text "$supp_release")

python "$ROOT/scripts/package_source.py" \
  --root "$ROOT" \
  --output "$ARTIFACT_DIR/Architecture_Before_the_Formula_v1.0_Source.zip"

cp "$ROOT/paper/main.pdf" "$ARTIFACT_DIR/Architecture_Before_the_Formula_v1.0.pdf"
cp "$ROOT/paper/supplement.pdf" "$ARTIFACT_DIR/Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf"
sha256sum "$ARTIFACT_DIR"/* > "$ARTIFACT_DIR/SHA256SUMS.txt"
