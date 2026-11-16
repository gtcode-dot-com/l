#!/bin/sh
set -eu
cd "$(dirname "$0")"
if command -v bibtex >/dev/null 2>&1; then BIBTEX=bibtex
elif command -v bibtex8 >/dev/null 2>&1; then BIBTEX=bibtex8
else echo 'Missing BibTeX or bibtex8 executable' >&2; exit 1
fi
latexmk -lualatex -e "\$bibtex = '$BIBTEX %O %B';" \
  -interaction=nonstopmode -halt-on-error -file-line-error main.tex
printf '\nBuilt %s/main.pdf\n' "$(pwd)"
