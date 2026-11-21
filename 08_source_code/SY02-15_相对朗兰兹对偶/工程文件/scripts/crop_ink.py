# -*- coding: utf-8 -*-
"""按墨迹裁图，并自动剥离粘在上下边缘的正文行。

用法：
    crop_ink.py PAGE X0 X1 Y0 Y1 NAME [DPI=300] [PAD=6]

搜索区域给得宽松一点没关系：脚本先取墨迹包围盒，再把「紧贴上/下边、从左边缘起笔、
宽度超过一半」的行块当成正文行剥掉（原书里图常紧贴一段正文）。
输出：源码/figures/NAME.png
"""
import sys, os
import numpy as np
import pymupdf

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PDF = os.path.join('C:/Users/admin/Downloads/BenZvi_LD_work/assets/pdf', 'src.pdf')
OUTDIR = os.path.join(ROOT, '源码', 'figures')

GAP = 3          # px：行间白隙超过它就分段
PROSE_W = 2.0    # 段落行宽占比阈值（>1 表示不剥正文行）
EDGE_X = 0.03    # 起笔在图像左侧这个比例内，视为「从左边距起笔」


def row_clusters(ink, gap=GAP):
    rows = ink.any(axis=1)
    out, start = [], None
    blank = 0
    for i, v in enumerate(rows):
        if v:
            if start is None:
                start = i
            blank = 0
        else:
            if start is not None:
                blank += 1
                if blank > gap:
                    out.append((start, i - blank))
                    start, blank = None, 0
    if start is not None:
        out.append((start, len(rows) - 1 - blank))
    return out


def is_prose(cluster, ink, width):
    a, b = cluster
    seg = ink[a:b + 1]
    xs = np.where(seg.any(axis=0))[0]
    if len(xs) == 0:
        return False
    span = (xs.max() - xs.min()) / width
    return xs.min() < EDGE_X * width and span > PROSE_W


def main():
    page = int(sys.argv[1])
    x0, x1, y0, y1 = (float(v) for v in sys.argv[2:6])
    name = sys.argv[6]
    dpi = int(sys.argv[7]) if len(sys.argv) > 7 else 300
    pad = int(sys.argv[8]) if len(sys.argv) > 8 else 6

    doc = pymupdf.open(PDF)
    p = doc[page - 1]
    W, H = p.rect.width, p.rect.height
    clip = pymupdf.Rect(x0 * W, y0 * H, x1 * W, y1 * H)
    pix = p.get_pixmap(dpi=dpi, clip=clip)
    arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    ink = arr[:, :, :3].min(axis=2) < 200

    cl = row_clusters(ink)
    cl = [c for c in cl if ink[c[0]:c[1] + 1].any()]
    if not cl:
        sys.exit('no ink in region')
    # 从上、下两端剥掉正文行
    while len(cl) > 1 and is_prose(cl[0], ink, pix.width):
        cl.pop(0)
    while len(cl) > 1 and is_prose(cl[-1], ink, pix.width):
        cl.pop()
    a, b = cl[0][0], cl[-1][1]

    seg = ink[a:b + 1]
    xs = np.where(seg.any(axis=0))[0]
    bx0, bx1 = max(xs.min() - pad, 0), min(xs.max() + pad, pix.width - 1)
    by0, by1 = max(a - pad, 0), min(b + pad, pix.height - 1)

    sx = (clip.x1 - clip.x0) / pix.width
    sy = (clip.y1 - clip.y0) / pix.height
    tight = pymupdf.Rect(clip.x0 + bx0 * sx, clip.y0 + by0 * sy,
                         clip.x0 + bx1 * sx, clip.y0 + by1 * sy)
    out = os.path.join(OUTDIR, name + '.png')
    p.get_pixmap(dpi=dpi, clip=tight).save(out)
    print('%-18s %dx%d  tight=(%.1f,%.1f,%.1f,%.1f)  frac=(%.3f,%.3f,%.3f,%.3f)'
          % (name, bx1 - bx0, by1 - by0, tight.x0, tight.y0, tight.x1, tight.y1,
             tight.x0 / W, tight.y0 / H, tight.x1 / W, tight.y1 / H))


if __name__ == '__main__':
    main()
