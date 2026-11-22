# -*- coding: utf-8 -*-
"""抓原文中重复词、常见笔误，作为疑点清单/勘误的候选。输出到标准输出。"""
import re
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "work", "原文", "samplez.tex")
lines = open(SRC, encoding="utf-8", errors="replace").read().splitlines()

DUP = re.compile(r"\b([A-Za-z]{2,})\s+\1\b")
WORDY = [
    "thory", "recieve", "seperate", "occured", "the the", "of of", "to to",
    "is is", "and and", "that that", "we we", "a a", "in in", "for for",
    "on on", "be be", "it it", "as as", "with with", "which which",
    "hypersepcial", "represetation", "representaion", "cohomlogy",
    "isomorphism isomorphism", "canonical canonical", "functor functor",
]
for i, line in enumerate(lines, 1):
    if i < 297:
        continue
    m = DUP.search(line)
    if m:
        print("DUP L%d: %s" % (i, line.strip()[:160]))
    low = line.lower()
    for w in WORDY:
        if w in low:
            print("WORD L%d [%s]: %s" % (i, w, line.strip()[:160]))
