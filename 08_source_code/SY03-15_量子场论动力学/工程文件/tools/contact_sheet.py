# -*- coding: utf-8 -*-
"""Build a contact sheet of all cropped figures for visual QC.

Usage: python contact_sheet.py [out.png]
"""
import glob
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "figs")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "meta", "contact_sheet.png")

files = sorted(glob.glob(os.path.join(FIG, "fig_p*.png")))
if not files:
    raise SystemExit("no figures")

COLS, THUMB_W, PAD, LABEL_H = 4, 360, 10, 22
font = ImageFont.load_default()
cells = []
for f in files:
    im = Image.open(f).convert("L")
    w, h = im.size
    th = int(h * THUMB_W / w)
    th = min(th, 520)
    im = im.resize((THUMB_W, th), Image.LANCZOS)
    cells.append((os.path.basename(f), im, th))

rows = (len(cells) + COLS - 1) // COLS
row_h = [0] * rows
for i, (_, im, th) in enumerate(cells):
    row_h[i // COLS] = max(row_h[i // COLS], th)
W = COLS * (THUMB_W + PAD) + PAD
H = sum(r + LABEL_H + PAD for r in row_h) + PAD
sheet = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(sheet)
y = PAD
for r in range(rows):
    x = PAD
    for c in range(COLS):
        i = r * COLS + c
        if i >= len(cells):
            break
        name, im, th = cells[i]
        sheet.paste(im, (x, y + LABEL_H))
        d.text((x + 2, y + 4), name.replace("fig_", "").replace(".png", ""), fill=0, font=font)
        x += THUMB_W + PAD
    y += row_h[r] + LABEL_H + PAD
sheet.save(OUT)
print("saved", OUT, sheet.size, f"({len(cells)} figures)")
