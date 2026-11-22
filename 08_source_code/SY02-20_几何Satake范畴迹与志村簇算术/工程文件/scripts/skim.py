# -*- coding: utf-8 -*-
r"""生成「速读版」原文：删注释、把展示公式环境压成一行标记，便于通读建图。

用法： python skim.py
输出： 工程文件/work/原文/skim.txt
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "work", "原文", "main.tex")
OUT = os.path.join(ROOT, "work", "原文", "skim.txt")

DISPLAY = ("equation", "equation*", "align", "align*", "gather", "gather*",
           "multline", "multline*", "CD", "tikzpicture", "xy", "tiny")

lines = open(SRC, encoding="utf-8").read().split("\n")
out = []
skip = None
for i, line in enumerate(lines, 1):
    s = line
    if skip:
        if ("\\end{%s}" % skip) in s:
            skip = None
            out.append("%%%% [展示公式/图 %d 行 略]" % i)
        continue
    m = re.search(r"\\begin\{(%s)\}" % "|".join(re.escape(x) for x in DISPLAY), s)
    if m:
        skip = m.group(1)
        pre = s[:m.start()].strip()
        if pre:
            out.append("%5d| %s" % (i, pre))
        continue
    # 去行内注释（保留 \%）
    t = re.sub(r"(?<!\\)%.*$", "", s).rstrip()
    if not t.strip():
        continue
    out.append("%5d| %s" % (i, t))

open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("skim lines", len(out), "bytes", os.path.getsize(OUT))
