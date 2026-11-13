# -*- coding: utf-8 -*-
"""结构/图形普查：检测 drawings（矢量图）、标题行、tag 明细 → work/probe/struct.md"""
import os, re, json
import pymupdf

BASE = r"<本地路径>"
SRC = os.path.join(BASE, "01_surveys")
W = os.path.join(BASE, "work")
PAPERS = [
    ("p1", "Chan-2014_SYZ-conjecture-and-its-impact_arXiv1408.6062.pdf"),
    ("p2", "Glimpse-of-the-SYZ-conjecture-and-related-developments_ICCM2016.pdf"),
    ("p3", "Gross-2008_SYZ-conjecture_torus-fibrations-to-degenerations_arXiv0802.3407.pdf"),
    ("p4", "Gross-2013_Mirror-symmetry-and-SYZ-conjecture_arXiv1212.4220.pdf"),
    ("p5", "YangLi-2022_Survey-metric-SYZ-conjecture-non-archimedean-geometry_arXiv2204.11363.pdf"),
    ("p6", "Collins-Lin-2022_Recent-progress-SYZ-noncompact-CY-surfaces_arXiv2208.14485.pdf"),
]
census = json.load(open(os.path.join(W, "probe", "census.json"), encoding="utf-8"))

lines = ["# 结构/图形/编号公式 明细（实测）", ""]
for key, fn in PAPERS:
    doc = pymupdf.open(os.path.join(SRC, fn))
    c = census[key]
    body_end = c["body_end"]
    lines.append(f"## {key}  {fn[:50]}")
    # drawings per page (vector figure detection)
    drawinfo = []
    imgcount = []
    for i in range(body_end):
        p = doc[i]
        nd = len(p.get_drawings())
        ni = len(p.get_images(full=True))
        imgcount.append(ni)
        if nd > 40:
            drawinfo.append((i + 1, nd))
    lines.append(f"- 矢量线密集页(>40 drawings): {drawinfo}")
    lines.append(f"- 位图页: {[(i+1, x) for i, x in enumerate(imgcount) if x]}")
    # headings
    heads = []
    for i in range(body_end):
        t = doc[i].get_text("text")
        for line in t.splitlines():
            s = line.strip()
            if re.match(r"^\d{1,2}(\.\d{1,2}){0,2}\.?\s+[A-Z\u2013\u4e00-\u9fff]", s) and 3 < len(s) < 90:
                heads.append((i + 1, s))
    lines.append(f"- 标题行: {len(heads)}")
    for pg, s in heads:
        lines.append(f"  - p.{pg}: {s}")
    # tag detail
    tbp = {int(k): v for k, v in c["tags_by_page"].items()}
    lines.append(f"- 编号公式 {c['tags']} 条:")
    for pg in sorted(tbp):
        lines.append(f"  - p.{pg}: {tbp[pg]}")
    lines.append("")
    doc.close()

open(os.path.join(W, "probe", "struct.md"), "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("written")
