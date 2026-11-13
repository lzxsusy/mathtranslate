# -*- coding: utf-8 -*-
"""在 tikzcd / tikzpicture 环境内把「」还原为 ASCII 双引号（引号事故的彻底修复）。"""
import io
import os

SRC = r"<本地路径>"
total = 0
for i in range(15):
    p = os.path.join(SRC, "ch%02d.tex" % i)
    if not os.path.isfile(p):
        continue
    lines = io.open(p, encoding="utf-8").read().splitlines()
    depth = 0
    changed = 0
    out = []
    for line in lines:
        if "\\begin{tikzcd}" in line or "\\begin{tikzpicture}" in line:
            depth += 1
        if depth > 0 and ("\u300c" in line or "\u300d" in line):
            line = line.replace("\u300c", '"').replace("\u300d", '"')
            changed += 1
        if "\\end{tikzcd}" in line or "\\end{tikzpicture}" in line:
            depth = max(0, depth - 1)
        out.append(line)
    if changed:
        io.open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")
        print("ch%02d fixed lines: %d" % (i, changed))
        total += changed
print("TOTAL", total)
