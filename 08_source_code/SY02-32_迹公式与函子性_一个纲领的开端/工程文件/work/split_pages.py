#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 work/fulltext.txt 拆成 work/src/pNNN.txt，供 verify_quotes.py 逐字核查引文。"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(HERE, "fulltext.txt")
out = os.path.join(HERE, "src")
os.makedirs(out, exist_ok=True)

text = open(src, encoding="utf-8").read()
parts = re.split(r"^===== BOOK PAGE (\d+) \(PDF (\d+)\) =====\s*$", text, flags=re.M)
# parts: [pre, n, pdf, body, n, pdf, body, ...]
assert len(parts) >= 4, "找不到页标记"
count = 0
for i in range(1, len(parts), 3):
    n = int(parts[i])
    body = parts[i + 2]
    with open(os.path.join(out, "p%03d.txt" % n), "w", encoding="utf-8") as f:
        f.write(body)
    count += 1
print("wrote", count, "pages")
