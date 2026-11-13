# -*- coding: utf-8 -*-
"""普查：公式编号 / 図 / 表 / 節見出し（OCR 文字层，仅供参考，真值以页图为准）"""
import pymupdf, re, sys, os, json, collections
sys.stdout.reconfigure(encoding='utf-8')
SRC = r"<本地路径> (M.F.アティヤ Michael Francis Atiyah) (z-library.sk  1lib.sk  z-lib.sk).pdf"
ROOT = r"<本地路径>"
doc = pymupdf.open(SRC)

# 公式编号形如 (1.1) (2.13) (B.1.2) (C.3.1)
tagre = re.compile(r'[（(]\s*([0-9A-C])\s*[.．]\s*(\d{1,2})\s*(?:[.．]\s*(\d{1,2}))?\s*[）)]\s*$')
figre = re.compile(r'図\s*([0-9A-C])\s*[.．]\s*(\d{1,2})')
tags = []
figs = []
for i in range(doc.page_count):
    t = doc[i].get_text("text")
    for line in t.split("\n"):
        s = line.strip()
        m = tagre.search(s)
        if m:
            a, b, c = m.group(1), m.group(2), m.group(3)
            tag = f"{a}.{b}" + (f".{c}" if c else "")
            tags.append((tag, i + 1))
        for fm in figre.finditer(s):
            figs.append((f"図{fm.group(1)}.{fm.group(2)}", i + 1, s[:60]))
c = collections.Counter(t for t, p in tags)
print("=== equation tags: total", len(tags), "unique", len(c))
for ch in ["1", "2", "3", "A", "B", "C"]:
    lst = [(int(t.split('.')[1]), t, p) for t, p in tags if t.split('.')[0] == ch]
    lst.sort()
    print(f"-- ch{ch}: {len(lst)}")
    print("   " + ", ".join(f"{t}(p{p-9})" for _, t, p in lst))
print()
print("=== figures ===")
seen = {}
for f, p, s in figs:
    seen.setdefault(f, []).append(p)
for f in sorted(seen):
    print(f, "pages", sorted(set(seen[f])), "count", len(seen[f]))
print()
print("=== duplicate tag lines ===")
for t, n in c.items():
    if n > 1:
        print(t, n, [p for tt, p in tags if tt == t])
