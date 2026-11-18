#!/usr/bin/env bash
# 整书编译（XeLaTeX → Biber → XeLaTeX×2 → makeindex → XeLaTeX），成品复制到 成品/
set -e
cd "$(dirname "$0")/../源码"
export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"

xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null 2>&1
biber main > /dev/null 2>&1
xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null 2>&1
xelatex -interaction=nonstopmode -halt-on-error main.tex > build.log 2>&1
[ -f main.idx ] && makeindex main.idx -o main.ind > /dev/null 2>&1 || true
xelatex -interaction=nonstopmode -halt-on-error main.tex > build.log 2>&1

echo "errors:   $(grep -cE '^! ' build.log)"
echo "overfull: $(grep -c 'Overfull' build.log)"
echo "index:    $(grep -c '\\item' main.ind 2>/dev/null || echo 0) 条"
grep -o "Output written.*" build.log
cp main.pdf "../成品/Siebert_镜像对称_2019秋_课程讲义_中译注本.pdf"
echo "copied to 成品/"
