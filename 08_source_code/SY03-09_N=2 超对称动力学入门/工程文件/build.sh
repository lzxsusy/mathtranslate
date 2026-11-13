#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
for command in xelatex makeindex; do
  if ! command -v "$command" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$command" >&2
    exit 1
  fi
done
# First populate cross-references, then generate the concept index.
xelatex -interaction=nonstopmode -halt-on-error main.tex
makeindex -s index.ist main.idx
# Resolve the table of contents, bibliography back-links, and index pagination.
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
printf '\nGenerated: %s/main.pdf\n' "$PWD"
