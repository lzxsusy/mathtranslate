#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terminology audit over chapters/*.tex: counts + sample contexts.

usage: python audit2.py [--ctx 2]
"""
import glob, os, re, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
CTX = 1

PAIRS = [
    ("单值化", "单值性"),
    ("线性束", "线性系"),
    ("通用族", "万有族"),
    ("翻转", "翻越"),
    ("相变", "相"),
    ("轨形", "轨道流形"),
    ("丰沛", "充裕"),
    ("万有", "通用"),
    ("幂零", "幂零"),
]

TERMS = ["上同调", "同调", "层", "束", "模空间", "锥", "扇", "除子", "因子",
         "平坦", "平滑", "光滑", "正规", "正则", "整性", "本原", "本原集合"]

files = sorted(glob.glob("chapters/*.tex"))
text = {f: open(f, encoding="utf-8").read().split("\n") for f in files}

print("== pair counts ==")
for a, b in PAIRS:
    ca = sum(l.count(a) for f in files for l in text[f])
    cb = sum(l.count(b) for f in files for l in text[f])
    print(f"{a}: {ca}\t{b}: {cb}")

print("\n== term counts ==")
for t in TERMS:
    c = sum(l.count(t) for f in files for l in text[f])
    print(f"{t}: {c}")

print("\n== samples: 同调 lines that look like cohomology ==")
n = 0
for f in files:
    for i, l in enumerate(text[f], 1):
        if "同调" in l and "上同调" not in l:
            n += 1
            if n <= 25:
                print(f"{os.path.basename(f)}:{i}: {l[:110]}")
print("total 同调-without-上同调 lines:", n)
