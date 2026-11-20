# -*- coding: utf-8 -*-
"""按相对坐标裁剪手写页，用于辨认难读处。
用法: python crop.py t1-01 0.03 0.28 0.80 0.35
参数: 页名(不带.png) x0 y0 x1 y1（均为 0..1 相对坐标）
输出: 工程文件/tools/_crops/<页名>_<x0>-<y0>.png
"""
import sys, os
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.normpath(os.path.join(ROOT, '..', '..', '源码', 'original', 'pages'))
OUT = os.path.join(ROOT, '_crops')
os.makedirs(OUT, exist_ok=True)

name = sys.argv[1]
x0, y0, x1, y1 = [float(a) for a in sys.argv[2:6]]
scale = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0

im = Image.open(os.path.join(PAGES, name + '.png'))
W, H = im.size
box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
crop = im.crop(box)
if scale != 1.0:
    crop = crop.resize((int(crop.width * scale), int(crop.height * scale)), Image.LANCZOS)
dst = os.path.join(OUT, '%s_%03d_%03d.png' % (name, int(x0 * 100), int(y0 * 100)))
crop.save(dst)
print(dst, crop.size)
