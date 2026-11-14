#!/usr/bin/env python
"""Detect and crop inline diagrams (small vector pictures embedded in formulas).

Outputs figures/inline/pNN-k.png at 400 dpi plus an index JSON.
Excludes the 14 display figures already cropped.
"""
import json
import os
import sys

import pymupdf

PDF = (r"<本地路径>"
       r"\2026-10\2204.01914v2(1).pdf")
OUT = r"<本地路径>"

FIG_BOXES = {   # page -> list of figure rects to exclude
    7: [(248, 88, 361, 190)],
    24: [(236, 276, 381, 402)],
    25: [(155, 88, 442, 214), (241, 264, 353, 389)],
    26: [(260, 89, 333, 189)],
    31: [(131, 88, 484, 216)],
    33: [(146, 88, 447, 222)],
    38: [(197, 88, 401, 242)],
    43: [(117, 356, 479, 563)],
    47: [(232, 454, 363, 572)],
    50: [(140, 96, 455, 217), (183, 452, 412, 618)],
    51: [(112, 93, 481, 215)],
    54: [(206, 87, 389, 270)],
}


def main():
    doc = pymupdf.open(PDF)
    os.makedirs(OUT, exist_ok=True)
    index = []
    for pno, page in enumerate(doc, 1):
        segs = []
        for d in page.get_drawings():
            r = pymupdf.Rect(d["rect"])
            if r.y1 < 78 or r.y0 > 675:
                continue                       # header / footnote rules
            if r.width > 430:
                continue                       # full-width rules
            if r.height < 0.5 and r.width > 120:
                continue                       # long table rules
            segs.append(r)
        if not segs:
            continue
        # union-find clustering on proximity (2 pt)
        parent = list(range(len(segs)))

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for i in range(len(segs)):
            for j in range(i + 1, len(segs)):
                a, b = segs[i], segs[j]
                if (a.x0 < b.x1 + 2 and b.x0 < a.x1 + 2 and
                        a.y0 < b.y1 + 2 and b.y0 < a.y1 + 2):
                    parent[find(i)] = find(j)
        groups = {}
        for i in range(len(segs)):
            groups.setdefault(find(i), []).append(segs[i])
        k = 0
        for g in groups.values():
            box = pymupdf.Rect(g[0])
            for r in g[1:]:
                box |= r
            if len(g) < 2 or box.height < 5 or box.width < 5:
                continue
            if box.height > 160 or box.width > 430:
                continue
            skip = False
            for fx0, fy0, fx1, fy1 in FIG_BOXES.get(pno, []):
                fb = pymupdf.Rect(fx0, fy0, fx1, fy1)
                if (box & fb).get_area() > 0.5 * box.get_area():
                    skip = True
            if skip:
                continue
            k += 1
            clip = pymupdf.Rect(box.x0 - 2, box.y0 - 2, box.x1 + 2, box.y1 + 2) & page.rect
            name = f"p{pno:02d}-{k:02d}.png"
            pix = page.get_pixmap(clip=clip, dpi=400)
            pix.save(os.path.join(OUT, name))
            index.append({"file": name, "page": pno,
                          "rect": [round(v, 1) for v in (clip.x0, clip.y0, clip.x1, clip.y1)],
                          "w": round(clip.width, 1), "h": round(clip.height, 1),
                          "n": len(g)})
    json.dump(index, open(os.path.join(OUT, "index.json"), "w"), indent=1)
    print("total", len(index))
    for e in index:
        print(e)
    return 0


if __name__ == "__main__":
    sys.exit(main())
