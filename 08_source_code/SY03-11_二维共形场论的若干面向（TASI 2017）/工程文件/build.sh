#!/usr/bin/env bash
# 编译脚本（需要 TeX Live / MiKTeX）
set -e
echo "==> 第 1 遍 xelatex"
xelatex -interaction=nonstopmode -halt-on-error main.tex
echo "==> 第 2 遍 xelatex（目录/交叉引用/文献编号）"
xelatex -interaction=nonstopmode -halt-on-error main.tex
echo "完成：main.pdf"
