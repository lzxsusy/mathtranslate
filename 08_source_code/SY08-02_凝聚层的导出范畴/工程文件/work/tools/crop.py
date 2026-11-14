# -*- coding: utf-8 -*-
"""crop.py —— 从底本 PDF 按“检索串/矩形/页内相对位置”裁切 200dpi 灰度图，供核对公式与交换图。

用法：
  # 1) 打印某页全部文本块及其 bbox（帮定位）
  python crop.py --book 514 --blocks
  # 2) 按检索串裁切（取包含该串的行，上下各留 padding）
  python crop.py --book 514 --search "ΦE" --out name.png
  # 3) 按绝对点坐标裁切（单位 pt，原点在页面左上）
  python crop.py --book 514 --rect x0 y0 x1 y1 --out name.png
  # 4) 按页内相对矩形裁切（0..1）
  python crop.py --book 514 --rel 0.1 0.2 0.9 0.6 --out name.png
"""
import argparse, glob, os, sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11"
OFFSET = 510
DPI = 200


def find_pdf():
    hits = [p for p in glob.glob(os.path.join(PDF_DIR, "*.pdf")) if "Orlov" in p or "orlov" in p]
    if not hits:
        sys.exit("找不到底本 PDF")
    return hits[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", type=int, required=True)
    ap.add_argument("--search", default=None)
    ap.add_argument("--rect", nargs=4, type=float, default=None)
    ap.add_argument("--rel", nargs=4, type=float, default=None)
    ap.add_argument("--pad", type=float, default=18.0)
    ap.add_argument("--blocks", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--dpi", type=int, default=DPI)
    a = ap.parse_args()

    doc = pymupdf.open(find_pdf())
    page = doc[a.book - OFFSET - 1]
    W, H = page.rect.width, page.rect.height

    if a.blocks:
        for b in page.get_text("blocks"):
            x0, y0, x1, y1, txt = b[0], b[1], b[2], b[3], b[4].replace("\n", " | ")
            print("[%6.1f %6.1f %6.1f %6.1f] %s" % (x0, y0, x1, y1, txt[:160]))
        print("page size: %.1f x %.1f" % (W, H))
        return

    if a.search:
        rects = page.search_for(a.search)
        if not rects:
            sys.exit("未找到检索串：%r" % a.search)
        r = rects[0]
        for rr in rects[1:]:
            r = r | rr
        clip = pymupdf.Rect(r.x0 - a.pad, r.y0 - a.pad, r.x1 + a.pad, r.y1 + a.pad)
    elif a.rect:
        clip = pymupdf.Rect(*a.rect)
    elif a.rel:
        x0, y0, x1, y1 = a.rel
        clip = pymupdf.Rect(x0 * W, y0 * H, x1 * W, y1 * H)
    else:
        clip = page.rect

    clip = clip & page.rect
    pix = page.get_pixmap(dpi=a.dpi, clip=clip, colorspace=pymupdf.csGRAY)
    out = a.out or os.path.join(ROOT, "work", "crop.png")
    if not os.path.isabs(out):
        out = os.path.join(ROOT, "work", out)
    pix.save(out)
    print("saved %s  (%.0fx%.0f pt -> %dx%d px, clip=%s)" % (out, clip.width, clip.height, pix.width, pix.height, clip))


if __name__ == "__main__":
    main()
