# -*- coding: utf-8 -*-
"""Re-crop fig16 (p.73) with a taller window so the top label L_{g1g2g3g4} is included."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz
from PIL import Image
import numpy as np

ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "2307.07547v2.pdf")
FIGDIR = os.path.join(ROOT, "work", "figures")
doc = fitz.open(PDF)
page = doc[72]  # p.73
DPI = 400
PT = DPI / 72.0
clip = fitz.Rect(35, 95, 580, 645)
pix = page.get_pixmap(dpi=DPI, clip=clip)
img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
g = np.array(img.convert("L"))
mask = g < 245
rows = np.where(mask.any(axis=1))[0]
cols = np.where(mask.any(axis=0))[0]
m = int(6 * PT)
y0 = max(0, rows[0] - m); y1 = min(img.height, rows[-1] + 1 + m)
x0 = max(0, cols[0] - m); x1 = min(img.width, cols[-1] + 1 + m)
out = os.path.join(FIGDIR, "fig16.png")
img.crop((x0, y0, x1, y1)).save(out)
print(f"fig16 saved: {x1-x0}x{y1-y0}px  content top = {95 + rows[0]/PT:.1f}pt (clip top 95)")
