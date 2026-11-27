#!/usr/bin/env python3
# 每页：页边 1252--N 标记 + 疑似节标题
import re, sys
from pathlib import Path
src = Path(sys.argv[1])
lines = src.read_text(encoding="utf-8").splitlines()
pages, cur = {}, None
for ln in lines:
    m = re.match(r"^===== PAGE (\d+) =====", ln)
    if m:
        cur = int(m.group(1)); pages[cur] = []
    elif cur is not None:
        pages[cur].append(ln)
for p in sorted(pages):
    body = [x.strip() for x in pages[p] if x.strip()]
    margins = [x for x in body if re.match(r"^\d{4}--\d+$", x)]
    heads = [x for x in body if re.match(r"^\d{1,2}\s+\S", x) or re.match(r"^\d{1,2}\s*$", x)]
    print(f"p{p}: margins={margins} heads={heads[:6]}")
    print(f"   first={body[0][:80] if body else ''}")
    print(f"   last ={body[-1][:80] if body else ''}")
