# -*- coding: utf-8 -*-
"""列出手写页的文本行带（相对 y 坐标），用于精确定位裁剪区域。
用法: python lines.py t1-02
"""
import sys, os
import numpy as np
from PIL import Image

PAGES = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '..', '..', '源码', 'original', 'pages'))
name = sys.argv[1]
im = Image.open(os.path.join(PAGES, name + '.png')).convert('L')
a = np.asarray(im.resize((im.width // 4, im.height // 4)))
rows = (a < 128).sum(axis=1)
thr = max(3, rows.mean() * 0.35)
inside = False
start = 0
n = len(rows)
for i, v in enumerate(rows):
    if v > thr and not inside:
        inside = True
        start = i
    elif v <= thr and inside:
        inside = False
        if i - start > 6:
            print("%.3f-%.3f  h=%d" % (start / n, i / n, i - start))
if inside:
    print("%.3f-%.3f" % (start / n, 1.0))
