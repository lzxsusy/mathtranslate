#!/usr/bin/env bash
# 干净目录重建校订批注本 PDF。
#   bash build.sh <源码目录> [输出PDF路径]
# 依赖：MiKTeX（xelatex / pdfinfo）。在 MSYS Bash 下运行。
set -euo pipefail

SRC="${1:?用法: bash build.sh <源码目录> [输出PDF]}"
OUT="${2:-}"
MIX="${MIXTEX:-/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64}"
XELATEX="$MIX/xelatex.exe"
PDFINFO="$MIX/pdfinfo.exe"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
cp -r "$SRC"/. "$WORK"/
rm -f "$WORK"/*.aux "$WORK"/*.toc "$WORK"/*.log "$WORK"/*.out "$WORK"/*.pdf

cd "$WORK"
for i in 1 2 3; do
  "$XELATEX" -interaction=nonstopmode -halt-on-error main.tex > "pass$i.txt" 2>&1 || {
    echo "!! xelatex 第 $i 遍失败，错误如下："
    grep -n -A5 -E "^! |^l\.[0-9]+" main.log | head -60
    exit 1
  }
done

echo "--- 页数 ---"
"$PDFINFO" main.pdf | grep -E "^Pages|^Page size"
echo "--- 警告统计 ---"
grep -c "Overfull" main.log || true
grep -E "^! |LaTeX Warning: Reference|undefined" main.log | head -20 || true

if [ -n "$OUT" ]; then
  mkdir -p "$(dirname "$OUT")"
  cp main.pdf "$OUT"
  echo "已输出：$OUT"
fi
