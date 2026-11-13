# -*- coding: utf-8 -*-
"""底本尽职调查：元数据 / 页数 / 图 / 表 / 编号公式 / 参考文献 / 字体 / 页码偏移。"""
import re, json, collections
import pymupdf

PDF = r"<本地路径>"
PDF = r"<本地路径>).pdf"
OUT = r"<本地路径>"

doc = pymupdf.open(PDF)
lines = []
def p(*a):
    s = " ".join(str(x) for x in a)
    lines.append(s)
    print(s)

p("== META ==")
p(doc.metadata)
p("pages =", doc.page_count)
pw = doc[0].rect
p("page size pt =", pw.width, pw.height)

# --- tag scan: right-aligned (x.y) ---
tag_pat = re.compile(r"^\((\d{1,2}\.\d{1,2})\)$")
tags = collections.defaultdict(list)
tag_pages = collections.defaultdict(list)
for i, page in enumerate(doc):
    W = page.rect.width
    d = page.get_text("dict")
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for ln in b["lines"]:
            txt = "".join(s["text"] for s in ln["spans"]).strip()
            m = tag_pat.match(txt)
            if m:
                x1 = max(s["bbox"][2] for s in ln["spans"])
                if x1 > 0.74 * W:
                    tag_pages[i + 1].append(m.group(1))
p("== TAGS ==")
p("tag pages count =", len(tag_pages))
for pg in sorted(tag_pages):
    p(pg, tag_pages[pg])

# --- structure keywords ---
p("== STRUCTURE ==")
for kw in ["Contents", "References", "Bibliography", "Appendix", "Lecture 1", "Lecture 18", "Introduction"]:
    hits = []
    for i, page in enumerate(doc):
        t = page.get_text("text")
        if kw in t:
            hits.append(i + 1)
    p(kw, "->", hits[:12], "(%d)" % len(hits))

# --- figures / images / drawings ---
p("== FIGURES/TABLES ==")
img_pages = []
drw_pages = []
for i, page in enumerate(doc):
    if page.get_images():
        img_pages.append((i + 1, len(page.get_images())))
    n = len(page.get_drawings())
    if n > 40:
        drw_pages.append((i + 1, n))
p("pages with raster images:", img_pages)
p("pages with >40 drawings:", drw_pages)
fig_hits = []
tab_hits = []
for i, page in enumerate(doc):
    t = page.get_text("text")
    for m in re.finditer(r"(Figure|Fig\.)\s*(\d+)", t):
        fig_hits.append((i + 1, m.group(0)))
    for m in re.finditer(r"Table\s*(\d+)", t):
        tab_hits.append((i + 1, m.group(0)))
p("Figure occurrences:", fig_hits[:40], "count", len(fig_hits))
p("Table occurrences:", tab_hits[:40], "count", len(tab_hits))

# --- fonts ---
p("== FONTS ==")
fonts = collections.Counter()
for i, page in enumerate(doc):
    for f in page.get_fonts(full=True):
        fonts[(f[3], f[4])] += 1
for k, v in fonts.most_common(30):
    p(k, v)

# --- first 6 pages text ---
p("== TEXT p1-p6 ==")
for i in range(min(6, doc.page_count)):
    p("--------- page", i + 1, "---------")
    p(doc[i].get_text("text"))

open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("written", OUT)
