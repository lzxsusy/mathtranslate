#!/bin/bash
# 编译两遍并过滤日志。用法：bash build.sh
cd "$(dirname "$0")"
XE="C:/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe"
"$XE" -interaction=nonstopmode main.tex >/dev/null 2>&1
"$XE" -interaction=nonstopmode main.tex >/dev/null 2>&1
grep -E '^!|^l\.[0-9]+|Missing character|Overfull \\hbox|Underfull \\hbox|Output written' main.log | head -30
echo "--- 未定义 ref/cite 条数（参考文献译完后须为 0）："
grep -cE 'LaTeX Warning: (Reference|Citation)' main.log
