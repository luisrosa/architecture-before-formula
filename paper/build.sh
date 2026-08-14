#!/usr/bin/env bash
set -euo pipefail

LATEXMK=${LATEXMK:-latexmk}
JMLR_STYLE_COMMIT="f413f638b407af76074813f8f88a82a7a5a81e9d"
JMLR_STYLE_URL="https://raw.githubusercontent.com/JmlrOrg/jmlr-style-file/${JMLR_STYLE_COMMIT}/jmlr2e.sty"

if [[ ! -f jmlr2e.sty ]]; then
  command -v curl >/dev/null 2>&1 || { echo "Missing curl for pinned JMLR style retrieval." >&2; exit 1; }
  curl --fail --location --silent --show-error "$JMLR_STYLE_URL" --output jmlr2e.sty
fi
if ! grep -q "Document Style .*jmlr" jmlr2e.sty; then
  echo "jmlr2e.sty does not look like the official JMLR style file." >&2
  exit 1
fi
BIBTEX_RULE=()
if ! command -v bibtex >/dev/null 2>&1; then
  if command -v bibtex8 >/dev/null 2>&1; then
    BIBTEX_RULE=(-e '$bibtex = "bibtex8 %O %B";')
  else
    echo "Missing required command: bibtex or bibtex8" >&2
    exit 1
  fi
fi
"$LATEXMK" -pdf -interaction=nonstopmode -halt-on-error "${BIBTEX_RULE[@]}" main.tex
