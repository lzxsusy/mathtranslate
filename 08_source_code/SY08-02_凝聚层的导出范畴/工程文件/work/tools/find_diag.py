# -*- coding: utf-8 -*-
"""自动发现页内交换图（图版）的包围盒。

原书 PDF 的页面是整页位图 + 文字层，图没有可用的矢量结构，所以改用文字层的
排版统计：交换图的标签是**成串的窄块**，而正文段落是接近版心的宽块。于是

  1. 把每页的文字块分为「宽块」（宽 > 300pt，=正文/标题）与「窄块」（其余）；
  2. 在纵向扫描，凡是一段区间内没有宽块、却有 >= 3 个窄块，判为图版带；
  3. 取这些窄块的并集再加内边距，作为该图的包围盒。

用法：python tools/find_diag.py 544 545 557 ...
      python tools/find_diag.py --all 544-563
"""
import sys, glob, os, re
import pymupdf as fitz

PDF_DIR = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11"
PDF = [q for q in glob.glob(os.path.join(PDF_DIR, '*.pdf')) if 'rlov' in q][0]

WIDE = 300.0
PAD = 6.0


def bands(page):
    blocks = [b for b in page.get_text('blocks') if b[4].strip()]
    rects = [(fitz.Rect(b[0], b[1], b[2], b[3]), b[4].strip()) for b in blocks]
    wide = [r for r, t in rects if r.width > WIDE]
    narrow = [(r, t) for r, t in rects if r.width <= WIDE]
    narrow.sort(key=lambda x: x[0].y0)

    out, cur = [], []

    def flush():
        if len(cur) >= 3:
            b = fitz.Rect(cur[0].x0, cur[0].y0, cur[0].x1, cur[0].y1)
            for r in cur[1:]:
                b = b | r
            if b.height > 20:
                out.append(b)
        cur.clear()

    for r, t in narrow:
        if cur:
            gap = r.y0 - max(c.y1 for c in cur)
            blocked = any(w.intersects(fitz.Rect(r.x0, r.y0 - 2, r.x1, r.y1 + 2))
                          for w in wide)
            if gap > 18 or blocked:
                flush()
        cur.append(r)
    flush()
    res = []
    for b in out:
        res.append(fitz.Rect(b.x0 - PAD, b.y0 - PAD, b.x1 + PAD, b.y1 + PAD))
    return res


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] == '--all':
        a, b = args[1].split('-')
        pages = list(range(int(a), int(b) + 1))
    else:
        pages = [int(x) for x in args]
    doc = fitz.open(PDF)
    for book in pages:
        page = doc[book - 510 - 1]
        bs = bands(page)
        if not bs:
            continue
        print('== 原书 p.%d  (%d 处)' % (book, len(bs)))
        for i, b in enumerate(bs):
            print('   %s  x0=%6.1f y0=%6.1f x1=%6.1f y1=%6.1f  w=%5.1f h=%5.1f'
                  % (chr(ord('a') + i), b.x0, b.y0, b.x1, b.y1, b.width, b.height))


main()
