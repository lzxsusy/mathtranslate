# -*- coding: utf-8 -*-
"""Deck check for the source PDF."""
import re, sys, io, json, os
import pymupdf as fitz

PDF = r"<本地路径>"
OUT = r"<本地路径>"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
n = len(doc)
lines = []
def p(s=""):
    lines.append(s)

p("=== METADATA ===")
p(json.dumps(doc.metadata, ensure_ascii=False, indent=1))
p(f"pages={n}")
p()
p("=== PAGE SIZE ===")
r = doc[0].rect
p(f"page0 rect={r}  w={r.width:.1f} h={r.height:.1f}")

# per-page stats
rows = []
total_imgs = 0
total_draw = 0
for i, page in enumerate(doc):
    t = page.get_text()
    imgs = len(page.get_images(full=True))
    draws = len(page.get_drawings())
    total_imgs += imgs
    total_draw += draws
    lines_ = [l.strip() for l in t.split("\n") if l.strip()]
    head = lines_[0][:60] if lines_ else ""
    tail = lines_[-1][:60] if lines_ else ""
    rows.append((i+1, len(t), imgs, draws, head, tail))
p()
p("=== PER PAGE (pdfpage chars imgs draws | head ... tail) ===")
for r_ in rows:
    p(f"p{r_[0]:03d} ch={r_[1]:5d} img={r_[2]} dr={r_[3]:3d} | {r_[4]!r} ... {r_[5]!r}")
p()
p(f"TOTAL bitmaps={total_imgs} drawings={total_draw}")

# section headings
p()
p("=== SECTION-LIKE LINES ===")
secpat = re.compile(r"^\s*((\d+(\.\d+)*)\s+[A-Z][^\n]{2,80})$")
for i, page in enumerate(doc):
    for ln in page.get_text().split("\n"):
        s = ln.strip()
        if secpat.match(s) and len(s) < 90:
            p(f"p{i+1}: {s}")

# equation tags
p()
p("=== EQUATION TAGS BY PAGE ===")
tagpat = re.compile(r"\((\d+\.\d+|[A-Z]\.\d+)\)")
alltags = []
for i, page in enumerate(doc):
    t = page.get_text()
    found = tagpat.findall(t)
    # filter plausible: digits like 1.1..9.99
    f2 = [x for x in found if re.fullmatch(r"\d{1,2}\.\d{1,3}", x)]
    if f2:
        p(f"p{i+1}: {f2}")
    alltags += f2
p(f"TAG COUNT(raw, may include refs) = {len(alltags)}")
p(f"UNIQUE = {len(set(alltags))}")
p("SORTED UNIQUE: " + ", ".join(sorted(set(alltags), key=lambda s: (int(s.split('.')[0]), int(s.split('.')[1])))))

# keyword scan
p()
p("=== KEYWORDS ===")
full = "\n".join(page.get_text() for page in doc)
for kw in ["Appendix", "References", "Bibliography", "Acknowledg", "Contents", "Introduction"]:
    p(f"{kw}: {full.count(kw)}")

open(os.path.join(OUT, "deck_check.txt"), "w", encoding="utf-8").write("\n".join(lines))
print("wrote deck_check.txt, lines:", len(lines))
print("pages", n, "tags", len(alltags))
