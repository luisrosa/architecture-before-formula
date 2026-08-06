#!/usr/bin/env bash
set -euo pipefail

LATEXMK=${LATEXMK:-latexmk}
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
"$LATEXMK" -pdf -interaction=nonstopmode -halt-on-error "${BIBTEX_RULE[@]}" supplement.tex
