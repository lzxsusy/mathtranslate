# -*- coding: utf-8 -*-
"""把 src/figures/dg_*.png 拼成一张校对用总览图（contact sheet）。

用法：python tools/contact.py [out.png] [--cols 5] [--w 260]
每个格子左上角标注文件名，方便对照 \figdiag 与裁图是否一致。
"""
import os, sys, glob
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, 'src', 'figures')

cols = 5
W = 260
args = sys.argv[1:]
if '--cols' in args:
    cols = int(args[args.index('--cols') + 1])
if '--w' in args:
    W = int(args[args.index('--w') + 1])
pos = [a for a in args if not a.startswith('--') and not a.isdigit()]
out = pos[0] if pos else os.path.join(ROOT, 'work', 'contact.png')

files = sorted(glob.glob(os.path.join(FIG, 'dg_*.png')))
tiles = []
for f in files:
    im = Image.open(f).convert('L')
    k = W / im.width
    im = im.resize((W, max(1, int(im.height * k))), Image.LANCZOS)
    tiles.append((os.path.basename(f)[:-4], im))

rowh = max(t[1].height for t in tiles) + 18
rows = (len(tiles) + cols - 1) // cols
sheet = Image.new('L', (cols * (W + 12) + 12, rows * (rowh + 8) + 8), 255)
d = ImageDraw.Draw(sheet)
for i, (name, im) in enumerate(tiles):
    r, c = divmod(i, cols)
    x = 12 + c * (W + 12)
    y = 8 + r * (rowh + 8)
    sheet.paste(im, (x, y + 14))
    d.text((x, y), name, fill=0)
    d.rectangle([x - 2, y + 12, x + W + 1, y + 14 + im.height + 1], outline=180)
sheet.save(out)
print('wrote', out, sheet.size, len(tiles), 'tiles')
