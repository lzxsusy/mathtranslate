# -*- coding: utf-8 -*-
"""Find section starts & headers; page map."""
import pymupdf, re, collections, os
ROOT = r"<本地路径>"
doc = pymupdf.open(os.path.join(ROOT, "src.pdf"))

# header = first non-empty line of page for body pages
heads = []
for i, p in enumerate(doc):
    t = p.get_text()
    lines = [l.strip() for l in t.split("\n") if l.strip()]
    heads.append(lines[0] if lines else "")

print("=== candidate section starts (line contains § and x.y) ===")
starts = []
for i, h in enumerate(heads):
    m = re.search(r"§\s*([0-9]{1,2})\s*[\.．]\s*([0-9]{1,2})", h)
    if m:
        tag = f"{int(m.group(1))}.{int(m.group(2))}"
        starts.append((tag, i + 1, h[:60]))
prev = None
for s in starts:
    if s[0] != prev:
        print(s)
        prev = s[0]

print("\n=== page headers sample 18..30 ===")
for i in range(17, 30):
    print(i + 1, "|", heads[i][:70])

print("\n=== pages whose header starts with 第N章 ===")
for i, h in enumerate(heads):
    m = re.match(r"^第\s*([0-9]+)\s*章", h)
    if m:
        print(i + 1, "|", h[:70])

print("\n=== back matter headers ===")
for i in range(140, 168):
    print(i + 1, "|", heads[i][:70])
