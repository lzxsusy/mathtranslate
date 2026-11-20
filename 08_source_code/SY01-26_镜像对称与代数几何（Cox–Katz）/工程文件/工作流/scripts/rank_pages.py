#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rank pages that are math-heavy and whose OCR is short (likely formula errors).

A page is suspicious when it has many $ / equation environments but the OCR text
for it is short (formulas became garbage), i.e. the translator had to guess.
"""
import glob, json, os, re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
per = []
for f in sorted(glob.glob("chapters/*.tex")):
    cur, buf = None, []
    for line in open(f, encoding="utf-8"):
        for m in re.finditer(r"\\SourcePage\{(\d+)\}", line):
            if cur is not None:
                per.append((cur, f, "".join(buf)))
            cur, buf = int(m.group(1)), []
        if cur is not None:
            buf.append(line)
    if cur is not None:
        per.append((cur, f, "".join(buf)))

rows = []
for page, f, text in per:
    maths = text.count("$") // 2 + 3 * len(re.findall(r"\\begin\{(equation|align|eqnarray|split)\}", text))
    ocr = f"ocr2/p{page:03d}.txt"
    olen = len(open(ocr, encoding="utf-8", errors="ignore").read()) if os.path.exists(ocr) else 0
    ratio = maths / max(olen, 1) * 1000
    rows.append((round(ratio, 2), maths, olen, page, os.path.basename(f)))
rows.sort(reverse=True)
for r in rows[:30]:
    print(f"score={r[0]:6.2f} math={r[1]:3d} ocrlen={r[2]:4d} p{r[3]} {r[4]}")
