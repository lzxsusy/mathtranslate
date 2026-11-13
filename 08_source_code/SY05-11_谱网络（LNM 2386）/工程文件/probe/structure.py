# -*- coding: utf-8 -*-
"""Structural analysis: chapter page ranges, figures, equations, page offset."""
import re, os, json
import pymupdf as fitz

PDF = r"<本地路径>"
OUT = r"<本地路径>"
doc = fitz.open(PDF)
n = len(doc)
L = []
def p(s=""): L.append(s)

full_pages = []
for i, page in enumerate(doc):
    full_pages.append(page.get_text())

# chapter starts: page whose text begins with "Chapter N" near top / or contains heading
chap = {}
for i, t in enumerate(full_pages):
    m = re.match(r"\s*Chapter\s+(\d+)\s*\n([^\n]+)", t)
    if m:
        chap.setdefault(int(m.group(1)), (i+1, m.group(2).strip()))
# also appendices
p("=== CHAPTER STARTS (pdf page, title) ===")
for k in sorted(chap):
    p(f"Ch{k}: pdf p{chap[k][0]}  {chap[k][1]}")

# parts
p()
p("=== PART STARTS ===")
for i, t in enumerate(full_pages):
    m = re.match(r"\s*(Part\s+[IVX]+)\s*\n([^\n]+)", t)
    if m:
        p(f"{m.group(1)}: pdf p{i+1}  {m.group(2).strip()}")
p("Appendix: " + str([i+1 for i,t in enumerate(full_pages) if re.match(r"\s*Appendix\s*\n?", t)][:6]))
p("Bibliography start: " + str([i+1 for i,t in enumerate(full_pages) if "Bibliography" in t[:120]][:4]))
p("Index start: " + str([i+1 for i,t in enumerate(full_pages) if re.match(r"\s*Index\s*\n", t)][:3]))

# printed page footer offset: scan bottom lines numerically
p()
p("=== PRINTED PAGE OFFSET SAMPLE ===")
offs = []
for i in range(43, 100):
    t = full_pages[i]
    lines = [x.strip() for x in t.split("\n") if x.strip()]
    if lines:
        try:
            q = int(lines[-1])
            offs.append((i+1, q, i+1-q))
        except Exception:
            pass
p(str(offs[:12]))

# figure captions
p()
p("=== FIGURE CAPTIONS ===")
figpat = re.compile(r"^\s*Fig\.\s*(\d+\.\d+)\s*(.*)$")
figs = []
for i, t in enumerate(full_pages):
    for ln in t.split("\n"):
        m = figpat.match(ln.strip())
        if m:
            figs.append((i+1, m.group(1), m.group(2)[:70]))
p(f"count={len(figs)}")
for f_ in figs:
    p(f"pdf p{f_[0]}: Fig {f_[1]}  {f_[2]}")
open(os.path.join(OUT, "structure.txt"), "w", encoding="utf-8").write("\n".join(L))
print("figure captions:", len(figs), "chapters:", len(chap))
