# -*- coding: utf-8 -*-
"""Crop figures v2: generous window above caption, cut at last body-text line, trim white."""
import sys, re, io, os
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz
from PIL import Image
import numpy as np

ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "2307.07547v2.pdf")
FIGDIR = os.path.join(ROOT, "work", "figures")
TMP = os.path.join(ROOT, "work", "tmp")
os.makedirs(FIGDIR, exist_ok=True)
DPI = 400
PT = DPI / 72.0

doc = fitz.open(PDF)

figs = {}  # n -> (page_idx, caption_line_bbox, caption_block_bbox)
for i, page in enumerate(doc):
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"]).strip()
            m = re.match(r"^Figure\s+(\d+)\s*:", txt)
            if m and int(m.group(1)) not in figs:
                figs[int(m.group(1))] = (i, l["bbox"], b["bbox"])


def body_bottom(page, y_top, y_bottom):
    low = y_top
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"]).strip()
            bb = l["bbox"]
            if bb[3] > y_bottom + 2 or bb[1] < y_top:
                continue
            words = txt.split()
            if len(txt) > 55 or (len(words) >= 9 and (bb[2] - bb[0]) > 330):
                low = max(low, bb[3])
    return low


report = []
for n in sorted(figs):
    pi, cb, cblock = figs[n]
    page = doc[pi]
    cap_top = cb[1]
    prev_bottom = None
    for m2, (pj, cb2, cblk2) in figs.items():
        if pj == pi and cb2[1] < cap_top - 1:
            prev_bottom = cblk2[3] if prev_bottom is None else max(prev_bottom, cblk2[3])
    top = max(60.0, cap_top - 520.0) if prev_bottom is None else prev_bottom + 3
    bb = body_bottom(page, top, cap_top - 4)
    if bb > top:
        top = bb + 3
    clip = fitz.Rect(35, top, 580, cap_top - 2)
    pix = page.get_pixmap(dpi=DPI, clip=clip)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    g = np.array(img.convert("L"))
    mask = g < 245
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    if len(rows) == 0:
        print(f"WARN fig{n}: empty")
        continue
    m = int(5 * PT)
    y0 = max(0, rows[0] - m); y1 = min(img.height, rows[-1] + 1 + m)
    x0 = max(0, cols[0] - m); x1 = min(img.width, cols[-1] + 1 + m)
    out = os.path.join(FIGDIR, f"fig{n}.png")
    img.crop((x0, y0, x1, y1)).save(out)
    flag = "TOP-CUT?" if rows[0] < 3 else ""
    print(f"fig{n:02d} p{pi+1:03d} clip=({top:.0f}..{cap_top-2:.0f}) content_pt=({(top+y0/PT):.0f}..{(top+y1/PT):.0f}) size={x1-x0}x{y1-y0} {flag}")
    report.append((n, pi + 1, round(top, 1), round(cap_top, 1), flag))

files = [f"fig{i}.png" for i in sorted(figs) if os.path.exists(os.path.join(FIGDIR, f"fig{i}.png"))]
cell_w = 400
thumbs = []
for f in files:
    im = Image.open(os.path.join(FIGDIR, f)).convert("RGB")
    r = cell_w / im.width
    im = im.resize((cell_w, max(1, int(im.height * r))), Image.LANCZOS)
    thumbs.append((f, im))
maxh = max(im.height for _, im in thumbs)
rows_n = (len(thumbs) + 1) // 2
sheet = Image.new("RGB", (2 * cell_w + 30, rows_n * (maxh + 22) + 20), "white")
from PIL import ImageDraw
dr = ImageDraw.Draw(sheet)
for k, (f, im) in enumerate(thumbs):
    r, c = divmod(k, 2)
    x = c * cell_w + 8; y = r * (maxh + 22) + 10
    sheet.paste(im, (x, y))
    dr.text((x + 2, y + max(0, im.height - 12)), f, fill="red")
sheet.save(os.path.join(TMP, "fig_contact2.png"))
print("contact:", os.path.join(TMP, "fig_contact2.png"), sheet.size)
