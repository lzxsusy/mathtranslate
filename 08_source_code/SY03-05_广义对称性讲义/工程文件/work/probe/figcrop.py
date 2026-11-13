# -*- coding: utf-8 -*-
"""Auto-crop the 28 original figures at 400 dpi + build a contact sheet for review."""
import sys, re, io, os
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz
from PIL import Image

ROOT = r"<本地路径>"
PDF = os.path.join(ROOT, "2307.07547v2.pdf")
FIGDIR = os.path.join(ROOT, "work", "figures")
TMP = os.path.join(ROOT, "work", "tmp")
os.makedirs(FIGDIR, exist_ok=True)
DPI = 400
PT = DPI / 72.0

doc = fitz.open(PDF)

# locate captions: figure number -> (page_index, caption line bbox)
figs = {}
for i, page in enumerate(doc):
    d = page.get_text("dict")
    for b in d["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"]).strip()
            m = re.match(r"^Figure\s+(\d+)\s*:", txt)
            if m:
                n = int(m.group(1))
                if n not in figs:
                    figs[n] = (i, l["bbox"])
print("figure captions found:", sorted(figs))

report = []
for n in sorted(figs):
    pi, cb = figs[n]
    page = doc[pi]
    # previous figure caption bottom on the same page (if any)
    prev_bottom = None
    for m2, (pj, cb2) in figs.items():
        if pj == pi and cb2[1] < cb[1] - 1:
            if prev_bottom is None or cb2[3] > prev_bottom:
                prev_bottom = cb2[3]
    top = cb[1] - 300 if prev_bottom is None else prev_bottom + 2
    top = max(top, 30)
    bot = cb[1] - 2
    if bot - top < 20:
        print(f"WARN fig{n}: region too small")
    clip = fitz.Rect(25, top, 587, bot)
    pix = page.get_pixmap(dpi=DPI, clip=clip)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    # trim white margins: find ink bbox with tolerance
    gray = img.convert("L")
    import numpy as np
    a = np.array(gray)
    mask = a < 245
    if not mask.any():
        print(f"WARN fig{n}: empty region")
        rows = np.where(mask.any(axis=1))[0]
        cols = np.where(mask.any(axis=0))[0]
        if len(rows) == 0:
            continue
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    m = int(6 * PT)
    y0 = max(0, rows[0] - m); y1 = min(img.height, rows[-1] + 1 + m)
    x0 = max(0, cols[0] - m); x1 = min(img.width, cols[-1] + 1 + m)
    out = os.path.join(FIGDIR, f"fig{n}.png")
    img.crop((x0, y0, x1, y1)).save(out)
    report.append((n, pi + 1, x0, y0, x1, y1, x1 - x0, y1 - y0, round(y0 / PT, 1), round(y1 / PT, 1)))
    print(f"fig{n:02d} p{pi+1:03d} bbox_px=({x0},{y0})-({x1},{y1}) size={x1-x0}x{y1-y0} y_pt={round(y0/PT,1)}..{round(y1/PT,1)}")

with io.open(os.path.join(TMP, "figcrop_report.txt"), "w", encoding="utf-8", newline="\n") as fh:
    for r in report:
        fh.write(str(r) + "\n")

# contact sheet: 4 cols
files = sorted([f for f in os.listdir(FIGDIR) if re.fullmatch(r"fig\d+\.png", f)],
               key=lambda s: int(re.search(r"\d+", s).group()))
cell_w = 420
thumbs = []
for f in files:
    im = Image.open(os.path.join(FIGDIR, f)).convert("RGB")
    r = cell_w / im.width
    im = im.resize((cell_w, max(1, int(im.height * r))), Image.LANCZOS)
    thumbs.append((f, im))
maxh = max(im.height for _, im in thumbs)
rows = (len(thumbs) + 3) // 4
sheet = Image.new("RGB", (4 * cell_w + 50, rows * (maxh + 20) + 20), "white")
from PIL import ImageDraw
dr = ImageDraw.Draw(sheet)
for k, (f, im) in enumerate(thumbs):
    r, c = divmod(k, 4)
    x = c * cell_w + 10
    y = r * (maxh + 20) + 10
    sheet.paste(im, (x, y))
    dr.text((x + 2, y + 2), f, fill="red")
out = os.path.join(TMP, "fig_contact.png")
sheet.save(out)
print("contact sheet:", out, sheet.size)
