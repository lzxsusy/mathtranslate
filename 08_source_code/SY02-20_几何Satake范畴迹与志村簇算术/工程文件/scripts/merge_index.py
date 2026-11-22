# -*- coding: utf-8 -*-
r"""合并条款索引（编号/类别/译本页）与原文页，输出 markdown 表与核对报告。"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORK = os.path.join(ROOT, "work")
A = os.path.join(WORK, "条款索引数据.tsv")
B = os.path.join(WORK, "原文页.tsv")
OUT = os.path.join(WORK, "条款索引合并.tsv")

a = [l.rstrip("\n").split("\t") for l in open(A, encoding="utf-8") if l.strip()]
b = [l.rstrip("\n").split("\t") for l in open(B, encoding="utf-8") if l.strip()]
assert len(a) == len(b), (len(a), len(b))

rows = []
bad = 0
for x, y in zip(a, b):
    num, kind, page, key = x
    if (num, kind) != (y[0], kind):
        bad += 1
    rows.append([num, kind, page, y[2], key])

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write("\t".join(r) + "\n")
print("rows", len(rows), "mismatch", bad)
