# -*- coding: utf-8 -*-
"""修复被引号转换破坏的 tikz 标签：\\arrow[...] / \\node[...] 内的「」还原为 ""。"""
import io
import os
import re

SRC = r"<本地路径>"
fixed = 0
for i in range(15):
    p = os.path.join(SRC, "ch%02d.tex" % i)
    if not os.path.isfile(p):
        continue
    lines = io.open(p, encoding="utf-8").read().splitlines()
    out = []
    for line in lines:
        if ("\\arrow" in line or "\\node" in line) and ("\u300c" in line or "\u300d" in line):
            line = line.replace("\u300c", '"').replace("\u300d", '"')
            fixed += 1
        out.append(line)
    io.open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("lines fixed:", fixed)
