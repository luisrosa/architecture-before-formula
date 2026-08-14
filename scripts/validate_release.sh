#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$ROOT/.build"
ARTIFACTS="$BUILD/artifacts"
mkdir -p "$ARTIFACTS"
(cd "$ROOT/paper" && sha256sum -c "$ROOT/releases/v1.6/SOURCE_SHA256SUMS.txt")
(cd "$ROOT/releases/v1.0" && sha256sum -c SHA256SUMS.txt)
cd "$ROOT"
python scripts/package_source.py --output "$ARTIFACTS/architecture-before-formula-v1.6-public-source.zip"
FRESH="$ROOT/paper/main.pdf"
[[ -s "$FRESH" ]] || { echo 'No fresh-build PDF available.' >&2; exit 1; }
pdfinfo "$FRESH" >/dev/null
pdftotext "$FRESH" - >/dev/null
if pdffonts "$FRESH" | tail -n +3 | awk 'NF && $6 != "yes" {bad=1} END {exit bad}'; then :; else
  echo "Found a non-embedded font in $FRESH" >&2; pdffonts "$FRESH" >&2; exit 1
fi
rm -rf "$BUILD/render-fresh"; mkdir -p "$BUILD/render-fresh"
pdftoppm -png -r 72 "$FRESH" "$BUILD/render-fresh/page" >/dev/null 2>&1
[[ $(find "$BUILD/render-fresh" -name 'page-*.png' | wc -l) -eq 34 ]]
cp "$FRESH" "$ARTIFACTS/Architecture_Before_the_Formula_v1.6_fresh-build.pdf"
cp "$ROOT/releases/v1.6/SOURCE_SHA256SUMS.txt" "$ARTIFACTS/SOURCE_SHA256SUMS.txt"
python scripts/validate_repository.py --mode postbuild
echo 'PUBLIC V1.6 RELEASE VALIDATION PASSED'
