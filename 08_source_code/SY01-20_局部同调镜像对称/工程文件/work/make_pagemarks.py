import io
import json
import os
import re

ROOT = r"<本地路径>"
pages = json.load(io.open(os.path.join(ROOT, "work", "page_start.json"), encoding="utf-8"))
pages = {int(k): v for k, v in pages.items()}
src = io.open(os.path.join(ROOT, "..", "_work", "arxiv_src", "main.tex"), encoding="utf-8").read().splitlines()

chunks = [
    ("ch00", 171, 214), ("ch01", 215, 364), ("ch02", 365, 515), ("ch03", 516, 810),
    ("ch04", 811, 1054), ("ch05", 1055, 1300), ("ch06", 1301, 1478), ("ch07", 1805, 2169),
    ("ch08", 2170, 2670), ("ch09", 2671, 3290), ("ch10", 3291, 3657), ("ch11", 3658, 4215),
    ("ch12", 4216, 4655), ("ch13", 4656, 5023), ("ch14", 5024, 5545),
]


def excerpt(line_no):
    i = line_no - 1
    while i < len(src) and not src[i].strip():
        i += 1
    s = src[i].strip()
    s = re.sub(r"\s+", " ", s)
    return s[:90]


outdir = os.path.join(ROOT, "work", "pagemarks")
if not os.path.isdir(outdir):
    os.makedirs(outdir)
for ch, a, b in chunks:
    rows = []
    for p in sorted(pages):
        L = pages[p]
        if a < L <= b:
            rows.append("%d\t%d\t%s" % (p, L, excerpt(L)))
    path = os.path.join(outdir, ch + ".txt")
    io.open(path, "w", encoding="utf-8").write("\n".join(rows) + "\n")
    print(ch, len(rows))
