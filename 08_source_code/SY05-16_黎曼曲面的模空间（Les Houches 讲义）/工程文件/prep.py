# -*- coding: utf-8 -*-
"""Prep: render pages, split text, tags, figure captions, per-page tag map."""
import pymupdf, re, os

ROOT = r"<本地路径>"
PDF = r"<本地路径>"
os.makedirs(os.path.join(ROOT, "pages"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "split"), exist_ok=True)

doc = pymupdf.open(PDF)
texts = [p.get_text() for p in doc]

# 1) render 200 dpi == zoom 200/72
zoom = 200 / 72
mat = pymupdf.Matrix(zoom, zoom)
for i, p in enumerate(doc):
    pix = p.get_pixmap(matrix=mat, alpha=False)
    pix.save(os.path.join(ROOT, "pages", "p%02d.png" % (i + 1)))
print("rendered", len(doc), "pages")

# 2) split text with header line
# detect footer number: last numeric line of page text
for i, t in enumerate(texts):
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    footer = ""
    for l in reversed(lines):
        if re.fullmatch(r"\d{1,3}", l):
            footer = l
            break
    secs = re.findall(r"^(\d+(?:\.\d+)?)\s*\.?\s*$", t, re.M)
    with open(os.path.join(ROOT, "split", "p%02d.txt" % (i + 1)), "w", encoding="utf-8") as f:
        f.write("PDF p.%d (footer: %s)\n" % (i + 1, footer))
        f.write(t)

with open(os.path.join(ROOT, "full.txt"), "w", encoding="utf-8") as f:
    for i, t in enumerate(texts):
        f.write("\n\n===== PDF PAGE %d =====\n" % (i + 1))
        f.write(t)

# 3) tags: only tags that appear as isolated equity numbers.
# heuristic: keep (a.b) where it is the last token on a line or preceded by whitespace and line ends there
tags = []
for i, t in enumerate(texts):
    for m in re.finditer(r"\((\d+\.\d+)\)", t):
        start, end = m.span()
        after = t[end:end + 2]
        before = t[max(0, start - 2):start]
        # equation number lines typically end the line (after is newline) 
        tags.append((i + 1, m.group(1), "EOL" if after.startswith("\n") else "inline"))
with open(os.path.join(ROOT, "tags_raw.txt"), "w", encoding="utf-8") as f:
    for pno, tg, kind in tags:
        f.write("%d\t%s\t%s\n" % (pno, tg, kind))

uniq = []
seen = set()
for pno, tg, kind in tags:
    if tg not in seen:
        seen.add(tg)
        uniq.append((pno, tg))
uniq.sort(key=lambda x: (int(x[1].split(".")[0]), int(x[1].split(".")[1])))
with open(os.path.join(ROOT, "tags.txt"), "w", encoding="utf-8") as f:
    for pno, tg in uniq:
        f.write("p%02d\t%s\n" % (pno, tg))

print("unique tags:", len(uniq))
# 4) distribution by section
from collections import Counter
c = Counter()
for pno, tg in uniq:
    c[tg.split(".")[0]] += 1
print("by section:", dict(c))
# 5) print per page tag list compact
lines = []
for pno, tg, kind in tags:
    lines.append("p%d:%s%s" % (pno, tg, "" if kind == "EOL" else "~"))
print(" ".join(lines))

# 6) figure/table captions
caps = re.findall(r"(Figure \d+[^\n]{0,160}|Table \d+[^\n]{0,120})", "\n".join(texts))
print("=== CAPTIONS ===")
for x in caps:
    print(x)
