#!/usr/bin/env bash
# SY99-04 上同调类域论（Raskin 讲义）· 复现成品 PDF
# 用法：bash 工程文件/build.sh
set -euo pipefail
cd "$(dirname "$0")/../源码"
for i in 1 2 3; do
  echo "== pass $i =="
  xelatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
done
grep -E "Output written" main.log | tail -1
echo "成品在 源码/main.pdf"
