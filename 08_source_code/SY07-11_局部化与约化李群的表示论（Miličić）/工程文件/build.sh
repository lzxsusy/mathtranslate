#!/usr/bin/env bash
# SY07-11 一键编译 + 自检
# 用法：bash 工程文件/build.sh [--index]
#   --index  先跑 insert_index.py 重建术语索引（会改写 源码/chapters/*.tex）
set -u
export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
PY="C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe"

cd "$ROOT/源码" || exit 1

if [ "${1:-}" = "--index" ]; then
  echo "== 重建术语索引 =="
  PYTHONIOENCODING=utf-8 "$PY" "$HERE/tools/insert_index.py" || exit 1
fi

echo "== xelatex 第 1 遍 =="
xelatex -interaction=nonstopmode main.tex > /dev/null 2>&1
echo "== makeindex =="
makeindex main.idx > /dev/null 2>&1 || echo "（无 .idx 或 makeindex 跳过了）"
echo "== xelatex 第 2、3 遍 =="
xelatex -interaction=nonstopmode main.tex > /dev/null 2>&1
xelatex -interaction=nonstopmode main.tex > log.txt 2>&1

echo
echo "== 自检 =="
printf '错误(!)：        %s\n' "$(grep -c '^!' log.txt)"
printf 'Overfull：       %s\n' "$(grep -c 'Overfull' log.txt)"
printf 'Underfull：      %s\n' "$(grep -c 'Underfull' log.txt)"
printf 'Missing char：   %s\n' "$(grep -c 'Missing character' log.txt)"
printf '未定义引用：     %s\n' "$(grep -c 'undefined' log.txt)"
printf 'PDF：            %s\n' "$(grep -o 'Output written on main.pdf ([0-9]* pages)' log.txt | head -1)"
echo
grep -n '^!' log.txt | head -10
grep -n 'Overfull' log.txt | head -10
grep -n 'Missing character' log.txt | head -10
