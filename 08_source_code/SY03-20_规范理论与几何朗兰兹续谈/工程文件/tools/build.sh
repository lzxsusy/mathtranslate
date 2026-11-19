#!/usr/bin/env bash
# 校订译注版构建脚本：xelatex ×3 + makeindex，审计 0 error / 0 undefined，产出成品 PDF 与预览图。
# 用法： bash 工程文件/tools/build.sh   （ROOT 由脚本位置推出，也可用 WITTEN_ROOT 覆盖）
set -uo pipefail

TOOLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${WITTEN_ROOT:-$(cd "$TOOLS_DIR/../.." && pwd)}"
SRC="$ROOT/源码"
OUT="$ROOT/成品"
NAME="Witten2015_规范理论与几何朗兰兹续谈_校订译注版"

cd "$SRC" || exit 1
rm -f main.aux main.idx main.ind main.out main.toc main.log

fail=0
run_pass () {
  local tag="$1"
  xelatex -interaction=nonstopmode -halt-on-error main.tex > "build_$tag.log" 2>&1
  local rc=$?
  if [ $rc -ne 0 ]; then
    echo "!! pass $tag 失败 (rc=$rc)"
    grep -n -m 20 -E "^!|^l\.[0-9]+" "build_$tag.log" || tail -30 "build_$tag.log"
    fail=1
  fi
  return $rc
}

run_pass 1 || exit 1
makeindex -q main.idx > makeindex.log 2>&1 || echo "!! makeindex 非零退出，见 makeindex.log"
run_pass 2 || true
run_pass 3 || true

LOG="build_3.log"
echo "== 审计 ($LOG) =="
echo "errors:      $(grep -c '^!' "$LOG" || true)"
echo "undefined:   $(grep -c 'undefined' "$LOG" || true)"
echo "overfull:    $(grep -c 'Overfull' "$LOG" || true)"
echo "warnings:    $(grep -c 'Warning' "$LOG" || true)"
grep -n -E "^!|Reference .* undefined|Citation .* undefined" "$LOG" | head -20

if [ -f main.pdf ]; then
  pages=$(pdfinfo main.pdf 2>/dev/null | awk '/^Pages:/{print $2}')
  echo "pages: $pages"
  mkdir -p "$OUT"
  cp -f main.pdf "$OUT/$NAME.pdf"
  # 预览图：第 1 页（封面/摘要）与第 3 页（目录）
  pdftoppm -f 1 -l 1 -r 100 -png main.pdf "$OUT/预览-封面" 2>/dev/null
  pdftoppm -f 3 -l 3 -r 100 -png main.pdf "$OUT/预览-正文" 2>/dev/null
  cd "$OUT"
  for f in 预览-*.png; do
    tgt=$(echo "$f" | sed 's/-0*[0-9]*\.png$/.png/')
    [ "$f" != "$tgt" ] && mv -f "$f" "$tgt"
  done
  cd "$SRC"
  ls -la "$OUT"
else
  echo "!! 没有生成 main.pdf"; fail=1
fi

exit $fail
