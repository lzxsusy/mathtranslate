# -*- coding: utf-8 -*-
"""Locate vector-drawing clusters per PDF page and (optionally) export them as
single-page PDFs whose CropBox is the cluster, so LaTeX keeps them as vector art.

Usage:
  python crop_figs.py                 # list clusters for every page -> work/fig_clusters.tsv
  python crop_figs.py export N x0 y0 x1 y1 name   # export one region -> 源码/figures/name.pdf
"""
import os
import sys

import pymupdf

PDF = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\20-BenZvi_LAWRG2024_lectures.pdf"
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.normpath(os.path.join(HERE, "..", "work"))
FIGS = os.path.normpath(os.path.join(HERE, "..", "..", "源码", "figures"))
GAP = 18.0      # pt: vertical gap that separates two clusters
PAD = 6.0       # pt: padding around a cluster


def clusters(page):
    rects = []
    for d in page.get_drawings():
        r = d["rect"]
        if r.is_empty or r.width < 0.5 and r.height < 0.5:
            continue
        rects.append(r)
    if not rects:
        return []
    rects.sort(key=lambda r: (r.y0, r.x0))
    groups = [[rects[0]]]
    cur_y1 = rects[0].y1
    for r in rects[1:]:
        if r.y0 > cur_y1 + GAP:
            groups.append([r])
        else:
            groups[-1].append(r)
        cur_y1 = max(cur_y1, r.y1)
    out = []
    for g in groups:
        x0 = min(r.x0 for r in g) - PAD
        y0 = min(r.y0 for r in g) - PAD
        x1 = max(r.x1 for r in g) + PAD
        y1 = max(r.y1 for r in g) + PAD
        if (x1 - x0) < 12 or (y1 - y0) < 8 or len(g) < 3:
            continue
        out.append((x0, y0, x1, y1, len(g)))
    return out


def export(page_no, box, name):
    doc = pymupdf.open(PDF)
    page = doc[page_no - 1]
    rect = pymupdf.Rect(*box)
    new = pymupdf.open()
    new.insert_pdf(doc, from_page=page_no - 1, to_page=page_no - 1)
    p = new[0]
    p.set_cropbox(rect)
    p.set_mediabox(rect)     # some includegraphics paths only read MediaBox
    out = os.path.join(FIGS, name + ".pdf")
    new.save(out, garbage=3, deflate=True, clean=True)
    print("saved", out, box)


def main() -> None:
    if len(sys.argv) > 2 and sys.argv[1] == "export":
        page_no = int(sys.argv[2])
        box = [float(x) for x in sys.argv[3:7]]
        export(page_no, box, sys.argv[7])
        return
    doc = pymupdf.open(PDF)
    os.makedirs(WORK, exist_ok=True)
    lines = ["page\tx0\ty0\tx1\ty1\tpaths"]
    for i, page in enumerate(doc, start=1):
        for c in clusters(page):
            lines.append("%d\t%.1f\t%.1f\t%.1f\t%.1f\t%d" % ((i,) + c))
    with open(os.path.join(WORK, "fig_clusters.tsv"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("clusters written:", len(lines) - 1)


if __name__ == "__main__":
    main()
