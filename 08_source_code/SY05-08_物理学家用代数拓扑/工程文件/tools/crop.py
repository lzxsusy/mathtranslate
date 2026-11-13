#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""crop.py —— 从底本 PDF 裁出插图（底本插图是手绘位图，直接渲染对应区域最清晰）

用法（在工程根目录执行）：
  # 查看某页内嵌图片的位置（PDF 点坐标 + 160dpi 像素坐标）
  python tools\\crop.py --page 12 --list

  # 自动裁该页所有内嵌图片的并集（最常见用法）
  python tools\\crop.py --page 12 --auto --out src<本地路径>

  # 只裁第 k 张（k 从 0 起）
  python tools\\crop.py --page 12 --index 0 --out src<本地路径>

  # 手工指定区域（--box 用 PDF 点；--pxbox 用 160dpi 页图上的像素，可省换算）
  python tools\\crop.py --page 12 --pxbox 300,200,900,600 --out src<本地路径>

  # 加白边（点）与提高分辨率
  python tools\\crop.py --page 12 --auto --pad 6 --dpi 400 --out src<本地路径>
"""
import argparse
import os
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_PDF = os.path.join(ROOT, "00_原文", "notes.pdf")
PX_PER_POINT = 160.0 / 72.0  # 页图按 160 dpi 生成


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=DEFAULT_PDF)
    ap.add_argument("--page", type=int, required=True, help="PDF 页码（= 原书页）")
    ap.add_argument("--list", action="store_true", help="只列出该页内嵌图片位置")
    ap.add_argument("--auto", action="store_true", help="裁所有内嵌图片的并集")
    ap.add_argument("--index", type=int, default=None, help="只裁第 k 张图（0 起）")
    ap.add_argument("--box", default=None, help="x0,y0,x1,y1（PDF 点）")
    ap.add_argument("--pxbox", default=None, help="x0,y0,x1,y1（160dpi 像素）")
    ap.add_argument("--pad", type=float, default=4.0, help="四周留白（点），默认 4")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    doc = pymupdf.open(args.pdf)
    page = doc[args.page - 1]
    infos = page.get_image_info(xrefs=True)
    boxes = [pymupdf.Rect(info["bbox"]) for info in infos]

    if args.list:
        print(f"page {args.page}: {len(boxes)} embedded image(s)")
        for i, r in enumerate(boxes):
            px = [round(v * PX_PER_POINT) for v in (r.x0, r.y0, r.x1, r.y1)]
            print(f"  [{i}] points x0={r.x0:.1f} y0={r.y0:.1f} x1={r.x1:.1f} y1={r.y1:.1f}"
                  f"   px(160dpi) {px[0]},{px[1]},{px[2]},{px[3]}"
                  f"   size {r.width:.1f}x{r.height:.1f}pt")
        return 0

    if args.pxbox:
        nums = [float(v) for v in args.pxbox.split(",")]
        rect = pymupdf.Rect(*[v / PX_PER_POINT for v in nums])
    elif args.box:
        rect = pymupdf.Rect(*[float(v) for v in args.box.split(",")])
    elif args.index is not None:
        if not boxes:
            print(f"page {args.page}: no embedded image", file=sys.stderr)
            return 2
        rect = boxes[args.index]
    elif args.auto:
        if not boxes:
            print(f"page {args.page}: no embedded image", file=sys.stderr)
            return 2
        rect = boxes[0]
        for r in boxes[1:]:
            rect |= r
    else:
        ap.error("需要 --list / --auto / --index / --box / --pxbox 之一")

    rect = pymupdf.Rect(rect.x0 - args.pad, rect.y0 - args.pad,
                        rect.x1 + args.pad, rect.y1 + args.pad)
    rect = rect & page.rect
    if args.out is None:
        ap.error("裁图必须给 --out")
    out = args.out if os.path.isabs(args.out) else os.path.join(ROOT, args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pix = page.get_pixmap(dpi=args.dpi, clip=rect)
    pix.save(out)
    print(f"saved {out}  ({pix.width}x{pix.height}px, {args.dpi}dpi, "
          f"box {rect.x0:.1f},{rect.y0:.1f},{rect.x1:.1f},{rect.y1:.1f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
