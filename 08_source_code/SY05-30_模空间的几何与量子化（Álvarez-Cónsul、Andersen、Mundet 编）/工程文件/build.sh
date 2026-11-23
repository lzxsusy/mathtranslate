#!/usr/bin/env bash
# 编译 SY05-30 并给出验收报告。用法：bash 工程文件/build.sh
set -u
cd "$(dirname "$0")/../源码" || exit 1

XELATEX="${XELATEX:-xelatex}"
for i in 1 2 3; do
  "$XELATEX" -interaction=nonstopmode main.tex > /tmp/sy0530_build.log 2>&1
  errs=$(grep -c '^!' /tmp/sy0530_build.log)
  echo "pass $i: errors=$errs"
  [ "$errs" -eq 0 ] || { echo "--- 前 20 条错误 ---"; grep -A3 '^!' /tmp/sy0530_build.log | head -20; break; }
done

echo "Overfull : $(grep -c 'Overfull' /tmp/sy0530_build.log)"
echo "Underfull: $(grep -c 'Underfull' /tmp/sy0530_build.log)"
echo "Undefined: $(grep -c 'undefined' /tmp/sy0530_build.log)"
if [ -f main.pdf ]; then
  echo "页数     : $(grep -o 'Output written on main.pdf ([0-9]* pages' /tmp/sy0530_build.log | grep -o '[0-9]*' | head -1)"
fi
