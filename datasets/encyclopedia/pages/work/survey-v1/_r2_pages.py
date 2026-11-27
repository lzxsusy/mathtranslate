#!/usr/bin/env python3
# 按 PAGE 切分原文，定位定理号/章节起止页
import re, sys
from pathlib import Path
src = Path(sys.argv[1])
pat = sys.argv[2] if len(sys.argv) > 2 else None
lines = src.read_text(encoding="utf-8").splitlines()
pages = {}
cur = 0
for ln in lines:
    m = re.match(r"^===== PAGE (\d+) =====", ln)
    if m:
        cur = int(m.group(1)); pages[cur] = []
    elif cur:
        pages[cur].append(ln)

if pat:
    rx = re.compile(pat)
    for p in sorted(pages):
        for i, ln in enumerate(pages[p]):
            if rx.search(ln):
                ctx = " / ".join(x.strip() for x in pages[p][max(0,i-1):i+2] if x.strip())
                print(f"p{p}\t{ctx[:180]}")
else:
    for p in sorted(pages):
        txt = " ".join(x.strip() for x in pages[p] if x.strip())
        print(f"p{p}\t{txt[:140]}")
