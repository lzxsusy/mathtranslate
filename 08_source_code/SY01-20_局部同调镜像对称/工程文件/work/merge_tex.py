# -*- coding: utf-8 -*-
"""把 src/main.tex 的 \\input 递归展开成单文件，便于 08_source_code 交付。"""
import io
import os
import re

ROOT = r"<本地路径>"
OUT = r"<本地路径>"

see = set()


def expand(path, base, depth=0):
    s = io.open(path, encoding="utf-8").read()
    if path.endswith("refs.bib"):
        return s

    def rep(m):
        name = m.group(1).strip()
        cand = os.path.join(base, name)
        if not cand.endswith(".tex"):
            cand += ".tex"
        if os.path.exists(cand):
            return expand(cand, os.path.dirname(cand), depth + 1)
        return m.group(0)

    s = re.sub(r"<本地路径>]+)\}", rep, s)
    return s


s = expand(os.path.join(ROOT, "main.tex"), ROOT)
s = s.replace(r"\bibliography{refs}", r"\bibliography{2611.07202v1_zh}")
header = "% !TeX program = xelatex\n% 2611.07202v1 中文译注本（单文件版，由 src/ 递归展开生成）\n"
io.open(OUT, "w", encoding="utf-8").write(header + s)
print("lines", s.count("\n") + 1, "chars", len(s))
