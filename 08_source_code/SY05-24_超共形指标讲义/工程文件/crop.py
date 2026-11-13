# -*- coding: utf-8 -*-
r"""crop.py — 把底本某页的局部放大裁出来看公式（公式的唯一真值来源）。

页码用 **PDF 页序**（1–32）；印刷页码 = PDF 页 − 1。

用法（在 工程文件\ 目录下跑）：
  python crop.py PAGE y0 y1 OUTFILE            # 整宽，纵向 y0..y1（0..1 比例）
  python crop.py PAGE x0 y0 x1 y1 OUTFILE      # 任意矩形，比例坐标
  python crop.py PAGE y0 y1 OUTFILE --dpi 600  # 指定分辨率（默认 500）

例：
  python crop.py 10 0.10 0.75 d10_tab.png       # 第 10 页的 Table 1
  python crop.py 10 0.10 0.75 0.20 0.60 d10_t1.png
然后用 read_image 工具看图（不要用 read 读 PNG）。
"""
import sys, os
import pymupdf

ROOT = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(ROOT, "底本_arXiv-2006.13630.pdf")


def main():
    a = sys.argv[1:]
    dpi = 500
    if "--dpi" in a:
        i = a.index("--dpi")
        dpi = float(a[i + 1])
        del a[i:i + 2]
    page = int(a[0])
    nums = [float(x) for x in a[1:-1]]
    out = a[-1]
    if len(nums) == 2:
        x0, y0, x1, y1 = 0.0, nums[0], 1.0, nums[1]
    elif len(nums) == 4:
        x0, y0, x1, y1 = nums
    else:
        print("bad args"); sys.exit(2)
    doc = pymupdf.open(PDF)
    p = doc[page - 1]
    r = p.rect
    clip = pymupdf.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height,
                        r.x0 + x1 * r.width, r.y0 + y1 * r.height)
    zoom = dpi / 72.0
    pix = p.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), clip=clip, alpha=False)
    if not os.path.isabs(out):
        out = os.path.join(ROOT, out)
    pix.save(out)
    print("saved %s (%dx%d)" % (out, pix.width, pix.height))


if __name__ == "__main__":
    main()
