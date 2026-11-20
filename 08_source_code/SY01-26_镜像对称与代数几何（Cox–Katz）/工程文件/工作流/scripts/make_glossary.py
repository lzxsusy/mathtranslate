#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build glossary.tsv from the README term table (with corrections applied)."""
import os, re, csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
rows = []
in_tab = False
for line in open("README.md", encoding="utf-8"):
    if line.startswith("| English |"):
        in_tab = True
        continue
    if in_tab:
        if not line.startswith("|"):
            break
        if set(line.strip()) <= set("|- "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2:
            rows.append(cells)

# corrections: en-substring -> (zh override, banned note)
FIX = {
    "monodromy": ("单值性 / 最大幺幂", "单值化", "monodromy 为「单值性」，单值化专指 uniformization"),
    "pencil": ("结点 / 直纹曲面 / 线性系", "线性束", "pencil = 线性系（linear system of dimension 1）"),
}

out = []
for en, zh in rows:
    banned = ""
    note = ""
    for k, (new_zh, ban, nt) in FIX.items():
        if en.startswith(k):
            zh, banned, note = new_zh, ban, nt
    # split pairs on " / " and zip when counts match
    ens = [s.strip() for s in en.split(" / ")]
    zhs = [s.strip() for s in zh.split(" / ")]
    if len(ens) == len(zhs):
        for e, z in zip(ens, zhs):
            out.append([e, z, "frozen", "B", "", "", banned, note])
    else:
        out.append([en, zh, "frozen", "B", "", "", banned, note])

with open("glossary.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["en", "zh", "mode", "grade", "sense", "first", "banned", "note"])
    for r in out:
        w.writerow(r)
print(len(out), "terms")
