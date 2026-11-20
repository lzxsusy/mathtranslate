#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render a printed page of Cox–Katz from the sharp two-up scan.

usage: python showpage.py 98 [--dpi 180] [--out pic.png] [--crop x0,y0,x1,y1]
prints the alt page/side used; writes PNG next to this script by default.
"""
import json, os, sys
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\Users\admin\Desktop\归档\08_教材与参考书\镜对称与代数几何.pdf"
PDF = r"C:\Users\admin\Desktop\归档\08_教材与参考书\Mirrorsymmetryandalgebraicgeometry(DavidA.Cox)(Z-Library).pdf"
ALT = None


def mapping():
    global ALT
    if ALT is None:
        m = json.load(open(os.path.join(HERE, "altmap.json")))
        rev = {}
        for i, (l, r) in m.items():
            i = int(i)
            if l:
                rev.setdefault(int(l), (i, "L"))
            if r:
                rev.setdefault(int(r), (i, "R"))
        ALT = rev
    return ALT


def main():
    p = int(sys.argv[1])
    if "--pdf" in sys.argv:
        p = p - 23  # PDF physical page -> printed page
    dpi = 200
    out = os.path.join(HERE, f"pv{p:03d}.png")
    crop = None
    a = sys.argv[2:]
    for k in range(0, len(a) - 1):
        if a[k] == "--dpi":
            dpi = int(a[k + 1])
        if a[k] == "--out":
            out = a[k + 1]
        if a[k] == "--crop":
            crop = [float(x) for x in a[k + 1].split(",")]
    rev = mapping()
    if p not in rev:
        # fallback: primary scan page = printed page + 23
        doc = pymupdf.open(PDF)
        pg = doc[p + 23 - 1]
        clip = pg.rect
        if crop:
            cw, dh = clip.width, clip.height
            clip = pymupdf.Rect(clip.x0 + crop[0] * cw, clip.y0 + crop[1] * dh,
                                clip.x0 + crop[2] * cw, clip.y0 + crop[3] * dh)
        z = dpi / 72.0
        pix = pg.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=clip)
        pix.save(out)
        n = 0
        print(f"printed p{p} (no alt map) -> primary pdf page {p + 23} -> {out} ({pix.width}x{pix.height})")
        return
    i, side = rev[p]
    doc = pymupdf.open(SRC)
    pg = doc[i]
    w, h = pg.rect.width, pg.rect.height
    left, right = (0, w / 2) if side == "L" else (w / 2, w)
    clip = pymupdf.Rect(left, 0, right, h)
    if crop:
        cw = clip.width
        ch = clip.height
        clip = pymupdf.Rect(clip.x0 + crop[0] * cw, clip.y0 + crop[1] * ch,
                            clip.x0 + crop[2] * cw, clip.y0 + crop[3] * ch)
    z = dpi / 72.0
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=clip)
    pix.save(out)
    print(f"printed p{p} -> alt pdf page {i + 1} side {side} -> {out} ({pix.width}x{pix.height})")


if __name__ == "__main__":
    main()
