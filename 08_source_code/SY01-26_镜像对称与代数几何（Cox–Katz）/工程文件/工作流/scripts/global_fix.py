#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Global terminology substitutions across the translation (chapters/*.tex + README.md).

Run AFTER the per-unit review issues have been applied, so that agent quotes still match.
usage: python global_fix.py [--dry]
"""
import glob, os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry" in sys.argv

# ordered: longer/more specific first is not needed here, patterns are disjoint
MAP = [
    ("单值化", "单值性"),      # monodromy mistranslated as uniformization
    ("虚基本类", "虚拟基本类"),  # virtual fundamental class (repo majority form)
    ("通用族", "万有族"),      # universal family
    ("线性束", "线性系"),      # pencil
]

targets = sorted(glob.glob("chapters/*.tex")) + ["README.md"]
total = {}
for pat, rep in MAP:
    n = 0
    hits = []
    for f in targets:
        t = open(f, encoding="utf-8").read()
        c = t.count(pat)
        if c:
            hits.append((f, c))
            n += c
            if not DRY:
                open(f, "w", encoding="utf-8", newline="\n").write(t.replace(pat, rep))
    total[(pat, rep)] = (n, hits)
    print(f"{pat} -> {rep}: {n}  {hits}", flush=True)
print("dry" if DRY else "written")
