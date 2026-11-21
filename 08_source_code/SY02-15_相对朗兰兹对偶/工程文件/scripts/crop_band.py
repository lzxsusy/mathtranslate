# -*- coding: utf-8 -*-
"""Export a figure from a PDF page as a standalone vector PDF.

The figure is selected by a vertical band (fractions of page height): all vector
paths whose centre falls in the band are taken, then any text span whose centre
lies inside the resulting box is added (that pulls in labels such as Σ^n, ∂_in),
then the box is padded.

Usage:
  python crop_band.py PAGE YTOP YBOT NAME [PAD]
    PAGE  1-based page number
    YTOP  top of band as fraction of page height (0 = top)
    YBOT  bottom of band
    NAME  output stem -> 源码/figures/NAME.pdf (plus NAME_preview.png)
    PAD   extra points around the box (default 3)
"""
import os
import sys

import pymupdf

PDF = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\20-BenZvi_LAWRG2024_lectures.pdf"
HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.normpath(os.path.join(HERE, "..", "..", "源码", "figures"))


def _union(rects):
    x0 = min(r.x0 for r in rects)
    y0 = min(r.y0 for r in rects)
    x1 = max(r.x1 for r in rects)
    y1 = max(r.y1 for r in rects)
    return pymupdf.Rect(x0, y0, x1, y1)


def fig_bbox(page, ytop, ybot, pad):
    H = page.rect.height
    y0, y1 = ytop * H, ybot * H
    sel = [d["rect"] for d in page.get_drawings()
           if (d["rect"].width > 1 or d["rect"].height > 1)
           and y0 <= (d["rect"].y0 + d["rect"].y1) / 2 <= y1]
    if not sel:
        raise SystemExit("no drawing paths in this band")
    box = _union(sel)
    spans = []
    for blk in page.get_text("dict")["blocks"]:
        if blk["type"] != 0:
            continue
        for line in blk["lines"]:
            for sp in line["spans"]:
                if sp["text"].strip():
                    spans.append(pymupdf.Rect(sp["bbox"]))
    grown = pymupdf.Rect(box.x0 - 14, box.y0 - 14, box.x1 + 14, box.y1 + 14)
    inside = [s for s in spans if grown.contains(s)]
    if inside:
        box = _union([box] + inside)
    return pymupdf.Rect(box.x0 - pad, box.y0 - pad, box.x1 + pad, box.y1 + pad)


def main() -> None:
    page_no = int(sys.argv[1])
    ytop, ybot = float(sys.argv[2]), float(sys.argv[3])
    name = sys.argv[4]
    pad = float(sys.argv[5]) if len(sys.argv) > 5 else 3.0
    doc = pymupdf.open(PDF)
    page = doc[page_no - 1]
    box = fig_bbox(page, ytop, ybot, pad)
    os.makedirs(FIGS, exist_ok=True)
    w, h = box.width, box.height
    new = pymupdf.open()
    page_out = new.new_page(width=w, height=h)
    page_out.show_pdf_page(pymupdf.Rect(0, 0, w, h), doc, page_no - 1, clip=box)
    out = os.path.join(FIGS, name + ".pdf")
    new.save(out, garbage=3, deflate=True, clean=True)
    prev = page_out.get_pixmap(dpi=200)
    prev.save(os.path.join(FIGS, name + "_preview.png"))
    print("%s  box=(%.1f, %.1f, %.1f, %.1f)  size=%.1fx%.1f pt"
          % (name, box.x0, box.y0, box.x1, box.y1, w, h))


if __name__ == "__main__":
    main()
