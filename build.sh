#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_ROOT="${BUILD_ROOT:-$ROOT/.build}"
SOURCE_COPY="$BUILD_ROOT/paper"
OUTPUT_DIR="$BUILD_ROOT/output"

rm -rf "$SOURCE_COPY" "$OUTPUT_DIR"
mkdir -p "$SOURCE_COPY" "$OUTPUT_DIR"
cp -R "$ROOT/paper/." "$SOURCE_COPY/"

(
  cd "$SOURCE_COPY"
  bash ./build.sh
)

cp "$SOURCE_COPY/main.pdf" \
  "$OUTPUT_DIR/Architecture_Before_the_Formula_v1.0.pdf"
cp "$SOURCE_COPY/supplement.pdf" \
  "$OUTPUT_DIR/Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf"

printf 'Built %s\n' "$OUTPUT_DIR/Architecture_Before_the_Formula_v1.0.pdf"
printf 'Built %s\n' "$OUTPUT_DIR/Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf"
