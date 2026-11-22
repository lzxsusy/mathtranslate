# -*- coding: utf-8 -*-
"""定位 \bib{Laf} 在原文中的位置，判断是否落在 \quash 跨度内。"""
import io
import os
import re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(root, "work", "原文", "main.tex")
s = io.open(src, encoding="utf-8", errors="replace").read()


def match_brace(s, start):
    d = 0
    i = start
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            d += 1
        elif c == "}":
            d -= 1
            if d == 0:
                return i
        i += 1
    return -1


for m in re.finditer(r"\\bib\{Laf\}", s):
    print("bib{Laf} at", m.start())
    st = s.find("\\quash{")
    while st >= 0:
        en = match_brace(s, st + 6)
        print("  quash span", st, en, "inside:", st <= m.start() <= en)
        st = s.find("\\quash{", st + 1)
    print("  context:", repr(s[m.start():m.start() + 200]))
