# -*- coding: utf-8 -*-
import sys, re, io, json
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>).pdf"
doc = fitz.open(PDF)
lines_out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    lines_out.append(s); print(s)

full_pages = [p.get_text() for p in doc]

# figures via captions
P("=== FIG CAPTIONS ===")
for i, t in enumerate(full_pages):
    for m in re.finditer(r"(Figure|Fig\.)\s*(\d+)", t):
        P(f"p{i+1}: {m.group(0)}")

P("\n=== SECTION HEADINGS (regex on text) ===")
for i, t in enumerate(full_pages):
    for line in t.splitlines():
        if re.match(r"^(Part\s+[IVX]+|[IVX]+\.?\s+[A-Z]|\d+(\.\d+)?\s+[A-Z])", line.strip()) and len(line.strip()) < 70:
            P(f"p{i+1}: {line.strip()}")

P("\n=== PER PAGE SUMMARY ===")
for i, t in enumerate(full_pages):
    ls = [l.strip() for l in t.splitlines() if l.strip()]
    first = ls[0][:60] if ls else ""
    last = ls[-1][:60] if ls else ""
    imgs = len(doc[i].get_images(full=True)); dr = len(doc[i].get_drawings())
    P(f"p{i+1:03d} ch={len(t):4d} img={imgs} dr={dr:3d} | {first!r} ... {last!r}")

P("\n=== FONTS (all pages) ===")
fonts = set()
for p in doc:
    for f in p.get_fonts(full=True):
        fonts.add((f[3], f[4]))
for f in sorted(fonts):
    P(f"  {f}")

P("\n=== KEYWORD SCAN ===")
full = "\n".join(full_pages)
for kw in ["Appendix", "References", "Acknowledg", "Contents", "Bibliography"]:
    for m in re.finditer(kw, full):
        pass
    P(f"{kw}: {full.count(kw)}")

with io.open(r"<本地路径>", "w", encoding="utf-8") as fh:
    fh.write("```\n" + "\n".join(lines_out) + "\n```\n")

# save per page text as files later; save full text
with io.open(r"<本地路径>", "w", encoding="utf-8") as fh:
    fh.write(full)
print("done")
