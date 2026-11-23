#!/usr/bin/env bash
# 整书编译：xelatex 三遍 → 复制成品到 工程文件/deliverable/
set -u
cd "$(dirname "$0")/../源码" || exit 1     # 到 源码/
ROOT=".."
NAME="无穷范畴讲义_中译注本"

xelatex -interaction=nonstopmode main.tex > /tmp/build1.log 2>&1
xelatex -interaction=nonstopmode main.tex > /tmp/build2.log 2>&1
xelatex -interaction=nonstopmode main.tex > /tmp/build3.log 2>&1
rc=$?

echo "== xelatex exit: $rc"
echo "== errors:"
grep -n "^!" /tmp/build3.log | head -20
echo "== undefined refs:"
grep -c "undefined" main.log
echo "== missing chars:"
grep -c "Missing character" main.log

if [ -f main.pdf ]; then
  mkdir -p "$ROOT/工程文件/deliverable"
  cp main.pdf "$ROOT/工程文件/deliverable/${NAME}.pdf"
  echo "== pages: $(python -c "import pymupdf;print(len(pymupdf.open('main.pdf')))" 2>/dev/null)"
  echo "== output: $ROOT/工程文件/deliverable/${NAME}.pdf"
fi

rm -f main.aux main.log main.out main.toc main.thm
