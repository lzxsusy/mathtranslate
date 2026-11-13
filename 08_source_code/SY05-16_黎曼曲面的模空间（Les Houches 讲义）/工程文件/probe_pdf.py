# -*- coding: utf-8 -*-
import pymupdf, re, json, os, sys

PDF = r"<本地路径>"
doc = pymupdf.open(PDF)
out = []
out.append("FILE: %s" % PDF)
out.append("SIZE: %d bytes" % os.path.getsize(PDF))
out.append("METADATA: %r" % (doc.metadata,))
out.append("PAGES: %d" % len(doc))
out.append("PAGE SIZE (p0): %s" % (doc[0].rect,))

# images / drawings per page
tot_img = 0
tot_draw = 0
img_pages = []
for i, p in enumerate(doc):
    ni = len(p.get_images(full=True))
    nd = len(p.get_drawings())
    tot_img += ni
    tot_draw += nd
    if ni > 0:
        img_pages.append((i + 1, ni))
out.append("TOTAL RASTER IMAGES: %d  on pages: %s" % (tot_img, img_pages[:50]))
out.append("TOTAL DRAWINGS: %d" % tot_draw)

# text per page
texts = []
for i, p in enumerate(doc):
    texts.append(p.get_text())
full = "\n".join(texts)
out.append("TOTAL TEXT CHARS: %d" % len(full))

# first page text
out.append("=== PAGE 1 TEXT ===")
out.append(texts[0][:3000])
out.append("=== PAGE 2 TEXT ===")
out.append(texts[1][:1500])

# equation tags
tags = []
for i, t in enumerate(texts):
    for m in re.finditer(r"\((\d+\.\d+)\)", t):
        tags.append((i + 1, m.group(1)))
out.append("RAW (x.y) matches: %d" % len(tags))
uniq = sorted(set(t[1] for t in tags), key=lambda s: (int(s.split('.')[0]), int(s.split('.')[1])))
out.append("UNIQUE tags: %d" % len(uniq))
out.append("FIRST 20: %s" % uniq[:20])
out.append("LAST 20: %s" % uniq[-20:])

# section / appendix / references search
for kw in ["Appendix", "References", "Bibliography", "Acknowledg", "Contents"]:
    hits = [i + 1 for i, t in enumerate(texts) if kw in t]
    out.append("KW %-12s -> pages %s" % (kw, hits[:20]))

with open(r"<本地路径>", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
with open(r"<本地路径>", "w", encoding="utf-8") as f:
    for pno, tg in tags:
        f.write("%d\t%s\n" % (pno, tg))
print("\n".join(out[:20]))
print("...written")
