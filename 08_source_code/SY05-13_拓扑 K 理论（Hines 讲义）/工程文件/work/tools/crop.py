# -*- coding: utf-8 -*-
r"""裁剪并放大原 PDF 的任意区域，用于核对公式（本项目 = Hines, Topological K-theory, 10 页）。

用法（PowerShell；python 用绝对路径）：
  $py="<本地路径>"
  & $py "<本地路径>" <页号> <x0> <y0> <x1> <y1> <输出png> [dpi]

坐标单位为 PDF 点（1/72 英寸）；**本底本整页 612 x 792**（Letter）。
例：裁第 6 页上半部分（输出放 work\tmp\）：
  & $py "...\crop.py" 6 60 80 560 420 "<本地路径>" 600
默认 dpi=600。
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>"
args = sys.argv[1:]
if len(args) < 6:
    print(__doc__)
    sys.exit(1)
pg = int(args[0])
x0, y0, x1, y1 = (float(v) for v in args[1:5])
out = args[5]
dpi = int(args[6]) if len(args) > 6 else 600
doc = fitz.open(PDF)
page = doc[pg - 1]
pix = page.get_pixmap(dpi=dpi, clip=fitz.Rect(x0, y0, x1, y1))
pix.save(out)
print("saved {} ({}x{})".format(out, pix.width, pix.height))
