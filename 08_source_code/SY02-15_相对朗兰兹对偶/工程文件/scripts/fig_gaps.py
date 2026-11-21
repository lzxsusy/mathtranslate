# -*- coding: utf-8 -*-
"""自动找「图带」：在每一页里，凡是两条等宽正文行之间的大空隙，就是一个图带。

用法：
    fig_gaps.py [PAGE ...]     # 不给页码则扫全书

对每个图带输出：页码、序号、y0/y1（pt）、高度、带内墨迹包围盒（pt 与分数）。
"""
import sys, os
import pymupdf

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PDF = os.path.join(ROOT, '工程文件', 'work', 'pdf', 'src.pdf')

MIN_GAP = 26.0   # pt，低于此不算图带
PROSE_W = 0.55   # 行宽超过页宽这个比例，才算「正文行」（标签行不会这么宽）


def prose_lines(page):
    out = []
    W = page.rect.width
    d = page.get_text('dict')
    for blk in d['blocks']:
        if blk['type'] != 0:
            continue
        for ln in blk['lines']:
            x0, y0, x1, y1 = ln['bbox']
            if (x1 - x0) > PROSE_W * W:
                out.append((y0, y1))
    out.sort()
    # 合并重叠
    merged = []
    for a, b in out:
        if merged and a <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    return merged


def ink_bbox(page, y0, y1, dpi=150):
    import numpy as np
    p = page.get_pixmap(dpi=dpi, clip=pymupdf.Rect(0, y0, page.rect.width, y1))
    arr = np.frombuffer(p.samples, dtype=np.uint8).reshape(p.height, p.width, p.n)[:, :, :3]
    ink = arr.min(axis=2) < 200
    ys, xs = np.where(ink)
    if len(xs) == 0:
        return None
    sx = page.rect.width / p.width
    sy = (y1 - y0) / p.height
    return (xs.min() * sx, y0 + ys.min() * sy, xs.max() * sx, y0 + ys.max() * sy)


def main():
    doc = pymupdf.open(PDF)
    pages = [int(a) for a in sys.argv[1:]] or range(1, doc.page_count + 1)
    for pno in pages:
        p = doc[pno - 1]
        W, H = p.rect.width, p.rect.height
        lines = prose_lines(p)
        edges = [(0.0, lines[0][0])] if lines else [(0.0, H)]
        for i in range(len(lines) - 1):
            edges.append((lines[i][1], lines[i + 1][0]))
        if lines:
            edges.append((lines[-1][1], H))
        k = 0
        for a, b in edges:
            if b - a < MIN_GAP:
                continue
            bbox = ink_bbox(p, a, b)
            if bbox is None:
                continue
            k += 1
            print('p%03d #%d  y=%.1f-%.1f (h=%.1f)  ink=(%.1f,%.1f,%.1f,%.1f) frac=(%.3f,%.3f,%.3f,%.3f)'
                  % (pno, k, a, b, b - a, bbox[0], bbox[1], bbox[2], bbox[3],
                     bbox[0] / W, bbox[1] / H, bbox[2] / W, bbox[3] / H))


if __name__ == '__main__':
    main()
