# -*- coding: utf-8 -*-
"""Deck check for arXiv:2307.07547v2 (Lectures on Generalized Symmetries)."""
import sys, re, io, os, json
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz
from collections import Counter, defaultdict

ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "2307.07547v2.pdf")
PROBE = os.path.join(ROOT, "work", "probe")
os.makedirs(PROBE, exist_ok=True)

doc = fitz.open(PDF)
out = []
def P(s=""):
    out.append(str(s)); print(s)

P("=== METADATA ===")
for k, v in (doc.metadata or {}).items():
    P(f"{k}: {v!r}")
P(f"pages: {len(doc)}")
P(f"page size: {doc[0].rect}")

P("\n=== EMBEDDED TOC ===")
toc = doc.get_toc()
P(f"toc entries: {len(toc)}")
for lvl, title, pg in toc[:80]:
    P(f"  L{lvl} p{pg}: {title}")

P("\n=== PAGE 1 TEXT ===")
P(doc[0].get_text())

P("\n=== FIGURE / TABLE CENSUS (text layer) ===")
full_pages = [p.get_text() for p in doc]
full = "\n".join(full_pages)
figs = sorted(set(int(m.group(1)) for m in re.finditer(r"Figure\s+(\d+)\s*[:.]", full)))
tabs = sorted(set(int(m.group(1)) for m in re.finditer(r"Table\s+(\d+)\s*[:.]", full)))
P(f"Figure captions found (max sets): {figs}")
P(f"Table captions found: {tabs}")
for i, t in enumerate(full_pages):
    for m in re.finditer(r"(Figure|Table)\s+(\d+)\s*[:.]", t):
        P(f"  p{i+1}: {m.group(0)}  ctx={t[max(0,m.start()-40):m.start()+60].replace(chr(10),' ')!r}")

P("\n=== IMAGE / DRAWING STATS ===")
tot_img = 0; tot_draw = 0
for i, p in enumerate(doc):
    ni = len(p.get_images(full=True)); nd = len(p.get_drawings())
    tot_img += ni; tot_draw += nd
    if ni:
        P(f"  p{i+1}: raster images={ni} drawings={nd}")
P(f"TOTAL raster images={tot_img} drawings={tot_draw} (drawings include fraction bars)")

P("\n=== EQUATION TAGS (span algorithm) ===")
tagpat = re.compile(r"^\(\s*(\d+\.\d+)\s*\)$")
tags = []
for i, p in enumerate(doc):
    W = p.rect.width
    d = p.get_text("dict")
    cand = []
    for b in d["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"]).strip()
            x1 = max((s["bbox"][2] for s in l["spans"]), default=0)
            m = tagpat.match(txt)
            if m and x1 > W * 0.78:
                cand.append((m.group(1), round(x1, 1)))
    seen = []
    for tg, x in cand:
        if not seen or seen[-1][0] != tg:
            seen.append((tg, x))
    for tg, x in seen:
        tags.append((tg, i + 1))
P(f"tags found: {len(tags)}  unique: {len(set(t for t,_ in tags))}")
bysect = defaultdict(list)
for tg, pg in tags:
    a, b = tg.split(".")
    bysect[a].append((int(b), pg))
for a, lst in sorted(bysect.items(), key=lambda kv: int(kv[0])):
    nums = [b for b, _ in lst]
    dups = [x for x in set(nums) if nums.count(x) > 1]
    missing = sorted(set(range(1, max(nums) + 1)) - set(nums)) if nums else []
    P(f"section {a}: n={len(nums)} max={max(nums) if nums else 0} dups={dups} missing={missing}")
with io.open(os.path.join(PROBE, "tags_raw.txt"), "w", encoding="utf-8", newline="\n") as fh:
    for tg, pg in tags:
        fh.write(f"{tg}\tp{pg}\n")

P("\n=== KEYWORDS ===")
for kw in ["Appendix", "References", "Bibliography", "Acknowledg", "Contents", "Exercise", "Summary", "Part"]:
    P(f"{kw}: {len(re.findall(kw, full))} occurrences")

P("\n=== FONTS ===")
fonts = set()
for i in range(min(len(doc), 12)):
    for f in doc[i].get_fonts(full=True):
        fonts.add((f[3], f[4]))
for f in sorted(fonts):
    P(f"  {f}")

P("\n=== PER PAGE SUMMARY ===")
for i, p in enumerate(doc):
    lines = [l.strip() for l in p.get_text().splitlines() if l.strip()]
    first = lines[0][:60] if lines else ""
    last = lines[-1][:60] if lines else ""
    P(f"p{i+1:03d} chars={len(p.get_text()):5d} FIRST={first!r} LAST={last!r}")

with io.open(os.path.join(PROBE, "probe.md"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write("```\n" + "\n".join(out) + "\n```\n")
print("\nwritten probe/probe.md")
