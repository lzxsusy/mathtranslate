#!/usr/bin/env bash
# 整书编译：两遍 xelatex，然后把成品复制到 交付\
set -e
cd "$(dirname "$0")/../源码"
export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"
xelatex -interaction=nonstopmode main.tex > /dev/null 2>&1 || true
xelatex -interaction=nonstopmode main.tex > build.log 2>&1
echo "errors: $(grep -cE '^! ' build.log)"
echo "overfull: $(grep -c 'Overfull' build.log)"
grep -o "Output written.*" build.log
cp main.pdf "../交付/陈麟_代数几何1_2025秋_课程讲义_中译注本.pdf"
echo "copied to 交付"
