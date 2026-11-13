# -*- coding: utf-8 -*-
"""Fix tags.txt: add manually detected tag 5.1 (p115) and re-sort by page."""
import io, os, re
ROOT = r"<本地路径>"
T = os.path.join(ROOT, "work", "tags.txt")
rows = []
for ln in io.open(T, encoding="utf-8"):
    ln = ln.strip()
    if not ln:
        continue
    tag, pg = ln.split("\t")
    rows.append((tag, int(pg.lstrip("p"))))
if not any(t == "5.1" for t, _ in rows):
    rows.append(("5.1", 115))
rows.sort(key=lambda x: (x[1], tuple(int(v) for v in x[0].split("."))))
with io.open(T, "w", encoding="utf-8", newline="\n") as fh:
    for tag, pg in rows:
        fh.write(f"{tag}\tp{pg}\n")
print("tags:", len(rows))
# rebuild tags_bypage
from collections import defaultdict
bp = defaultdict(list)
for tag, pg in rows:
    bp[pg].append(tag)
with io.open(os.path.join(ROOT, "work", "tags_bypage.txt"), "w", encoding="utf-8", newline="\n") as fh:
    for pg in sorted(bp):
        fh.write(f"p{pg:03d}: " + ", ".join(bp[pg]) + "\n")
print("pages with tags:", len(bp))
