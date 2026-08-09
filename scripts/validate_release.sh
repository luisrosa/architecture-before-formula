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
    qpdf --check "$pdf" >/dev/null
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

validate_pdf() {
  local pdf="$1"
  local label="$2"
  local check_placeholders="${3:-yes}"
  local pages rendered

  test -s "$pdf"
  check_pdf_structure "$pdf"

  pages="$(pdfinfo "$pdf" | awk '/^Pages:/ {print $2}')"
  test -n "$pages"
  test "$pages" -gt 0

  pdftotext "$pdf" "$BUILD_DIR/${label}.txt"
  test -s "$BUILD_DIR/${label}.txt"
  if [ "$check_placeholders" = "yes" ] && grep -Eiq 'TODO|FIXME|TBD|\?\?\?' "$BUILD_DIR/${label}.txt"; then
    echo "Draft placeholder found in ${label}.pdf" >&2
    exit 1
  fi

  while IFS= read -r embedded; do
    test "$embedded" = "yes"
  done < <(pdffonts "$pdf" | awk 'NR>2 {print $(NF-4)}')

  mkdir -p "$BUILD_DIR/${label}-pages"
  pdftoppm -png -r 110 "$pdf" "$BUILD_DIR/${label}-pages/page" >/dev/null 2>&1
  rendered="$(find "$BUILD_DIR/${label}-pages" -name 'page-*.png' -type f -size +5k | wc -l)"
  test "$rendered" -eq "$pages"
}

# Validate a fresh build from the current source tree under the CI toolchain.
validate_pdf "$ROOT/paper/main.pdf" main
validate_pdf "$ROOT/paper/supplement.pdf" supplement

main_release="$RELEASE_DIR/Architecture_Before_the_Formula_v1.0.pdf"
supp_release="$RELEASE_DIR/Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf"

# The committed v1.0 files are immutable release artifacts. Verify their
# identity against the committed manifest, then validate the PDFs independently.
(
  cd "$RELEASE_DIR"
  sha256sum -c SHA256SUMS.txt
)

validate_pdf "$main_release" release-main
validate_pdf "$supp_release" release-supplement

python "$ROOT/scripts/package_source.py" \
  --root "$ROOT" \
  --output "$ARTIFACT_DIR/Architecture_Before_the_Formula_v1.0_Source.zip"

cp "$ROOT/paper/main.pdf" "$ARTIFACT_DIR/Architecture_Before_the_Formula_v1.0.pdf"
cp "$ROOT/paper/supplement.pdf" "$ARTIFACT_DIR/Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf"
(
  cd "$ARTIFACT_DIR"
  sha256sum \
    Architecture_Before_the_Formula_v1.0.pdf \
    Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf \
    Architecture_Before_the_Formula_v1.0_Source.zip \
    > SHA256SUMS.txt
)
