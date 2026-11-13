# -*- coding: utf-8 -*-
"""Deck check: metadata, pages, figures, equations, structure."""
import sys, re, json, io
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>).pdf"
ROOT = r"<本地路径>"
doc = fitz.open(PDF)

out = []
def P(s=""):
    out.append(s); print(s)

P("=== METADATA ===")
for k, v in (doc.metadata or {}).items():
    P(f"{k}: {v!r}")
P(f"pages: {len(doc)}")
P(f"page size: {doc[0].rect}")
P(f"toc entries: {len(doc.get_toc())}")
for lvl, title, pg in doc.get_toc()[:80]:
    P(f"  TOC L{lvl} p{pg}: {title}")

P("\n=== PAGE 1 TEXT ===")
P(doc[0].get_text())

P("\n=== FIGURE STATS ===")
tot_img = 0; tot_draw = 0
for i, p in enumerate(doc):
    ni = len(p.get_images(full=True)); nd = len(p.get_drawings())
    tot_img += ni; tot_draw += nd
    if ni or nd > 200:
        P(f"  p{i+1}: images={ni} drawings={nd}")
P(f"TOTAL images={tot_img} drawings={tot_draw}")

P("\n=== EQUATION TAGS ===")
tagre = re.compile(r"\((\d+\.\d+)\)")
from collections import Counter, defaultdict
per_page = {}
alltags = []
for i, p in enumerate(doc):
    t = p.get_text()
    for m in tagre.finditer(t):
        alltags.append((m.group(1), i + 1))
    per_page[i+1] = len(tagre.findall(t))
P(f"total numbered-looking tags: {len(alltags)}")
c = Counter(t[0] for t in alltags)
dup = [k for k, v in c.items() if v > 1]
P(f"duplicate tag numbers (text-layer artifacts): {len(dup)} e.g. {dup[:20]}")
dist = {p: n for p, n in per_page.items() if n}
P("per-page tag counts: " + json.dumps(dist))

P("\n=== KEYWORDS ===")
full = "\n".join(p.get_text() for p in doc)
for kw in ["Appendix", "References", "Bibliography", "Acknowledg", "Contents", "Table", "Figure"]:
    idxs = [m.start() for m in re.finditer(kw, full)]
    P(f"{kw}: {len(idxs)} occurrences")
P("\n=== TABLE / FIGURE CAPTIONS ===")
for m in re.finditer(r"(Table|Figure)\s+(\d+)\s*[:.]", full):
    P(f"  {m.group(0)}  @char {m.start()}")

P("\n=== FONTS ===")
fonts = set()
for i in range(len(doc)):
    for f in doc[i].get_fonts(full=True):
        fonts.add((f[3], f[4]))
for f in sorted(fonts):
    P(f"  {f}")

P("\n=== PER PAGE: first line, last line, char count ===")
for i, p in enumerate(doc):
    lines = [l.strip() for l in p.get_text().splitlines() if l.strip()]
    first = lines[0][:80] if lines else ""
    last = lines[-1][:80] if lines else ""
    P(f"p{i+1:03d} chars={len(p.get_text()):5d} nlines={len(lines):3d} FIRST={first!r} LAST={last!r}")

with io.open(ROOT + r"\probe\probe_raw.md", "w", encoding="utf-8") as fh:
    fh.write("```\n" + "\n".join(out) + "\n```\n")
with io.open(ROOT + r"\probe\tags_all.txt", "w", encoding="utf-8", newline="\n") as fh:
    for t, p in alltags:
        fh.write(f"{t}\tp{p}\n")
print("\nwritten probe_raw.md")
