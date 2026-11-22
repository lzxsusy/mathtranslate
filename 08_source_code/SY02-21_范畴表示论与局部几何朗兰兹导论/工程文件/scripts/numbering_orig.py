# -*- coding: utf-8 -*-
r"""从原文 PDF 抽取「定理类 n.m.k」与「公式 (n.m)」序列，作为编号对账的基准。"""
import os
import re

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PDF = os.path.join(ROOT, "work", "pdf", "src.pdf")
OUT = os.path.join(ROOT, "work", "numbering_orig.txt")

NAMES = ("Theorem|Lemma|Proposition|Corollary|Conjecture|Definition|Remark|"
         "Example|Question|Fact|Ansatz|Construction")

doc = pymupdf.open(PDF)
text = "\n".join(p.get_text() for p in doc)

thm = re.findall(r"\b(%s)\s+(\d+\.\d+\.\d+)" % NAMES, text)
eq = re.findall(r"^\s*\((\d+\.\d+)\)", text, re.M)

seen_t, seen_e = [], []
for name, num in thm:
    tag = (num, name)
    if tag not in [(n, k) for n, k in seen_t]:
        seen_t.append((num, name))
for n in eq:
    if n not in seen_e:
        seen_e.append(n)

lines = []
for num, name in seen_t:
    lines.append("%s\t%s" % (num, name))
for n in seen_e:
    lines.append("%s\t公式" % n)
open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("pages", doc.page_count, "thm", len(seen_t), "eq", len(seen_e), "->", OUT)
