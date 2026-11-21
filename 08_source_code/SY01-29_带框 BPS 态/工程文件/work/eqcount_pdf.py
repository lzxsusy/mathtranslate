#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GMN3 每块编号公式数：从原文 PDF 实测。

判据：编号出现在行末右侧栏边（x0 > 页宽 − 86pt），排除正文里的式号引用。
输出可直接粘贴进 BRIEF 分块表的「式数」列。
"""
import re
import sys
from collections import defaultdict

import pymupdf

PDF = r"C:\Users\admin\Desktop\GMN系列\00_原文\GMN3_1006.0146\1006.0146v2.pdf"
CHUNKS = [
    ("ch01", 4, 6), ("ch02", 7, 13), ("ch03", 14, 21), ("ch04", 22, 27),
    ("ch05", 28, 38), ("ch06", 39, 47), ("ch07", 48, 56), ("ch08", 57, 66),
    ("ch09", 67, 72), ("ch10", 73, 78), ("ch11", 79, 85), ("ch12", 86, 92),
    ("ch13", 93, 98), ("ch14", 99, 106), ("ch15", 107, 114), ("ch16", 115, 124),
]
PAT = re.compile(r"^\(\s*(\d+|[A-G])\s*\.\s*(\d+)\s*\)$")


def scan():
    doc = pymupdf.open(PDF)
    per_page = defaultdict(set)
    for pno, page in enumerate(doc, 1):
        right = page.rect.width - 112
        for w in page.get_text("words"):
            if w[2] >= page.rect.width - 90 and PAT.match(w[4]):
                m = PAT.match(w[4])
                per_page[pno].add((m.group(1), int(m.group(2))))
    return per_page


def main():
    per_page = scan()
    total = 0
    for name, a, b in CHUNKS:
        s = set()
        for p in range(a, b + 1):
            s |= per_page.get(p, set())
        total += len(s)
        print("%s  PDF %3d-%3d  式 %2d" % (name, a, b, len(s)))
    print("合计 %d" % total)
    sec = defaultdict(int)
    for p, s in per_page.items():
        pass
    allpairs = set()
    for s in per_page.values():
        allpairs |= s
    for k in sorted({k for k, _ in allpairs}, key=lambda x: (len(x), x)):
        sec[k] = len({n for kk, n in allpairs if kk == k})
    print("逐节：", dict(sec), "总", sum(sec.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
