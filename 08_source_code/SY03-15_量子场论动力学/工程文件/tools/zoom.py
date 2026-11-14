# -*- coding: utf-8 -*-
"""Zoom into a region of a page PNG for close reading.

Usage: python zoom.py --page 4 --box 0.10,0.14,0.60,0.20 --scale 2.5 --out tmp/zoom.png
Box fractions of width/height, origin top-left.
"""
import argparse
import os

from PIL import Image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", type=int, required=True)
    ap.add_argument("--box", required=True)
    ap.add_argument("--scale", type=float, default=2.0)
    ap.add_argument("--out", default="tmp/zoom.png")
    args = ap.parse_args()

    src = os.path.join("witten_qft", "pages", "p%03d.png" % args.page)
    im = Image.open(src).convert("L")
    W, H = im.size
    x0, y0, x1, y1 = [float(v) for v in args.box.split(",")]
    box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    im = im.crop(box)
    im = im.resize((int(im.width * args.scale), int(im.height * args.scale)), Image.LANCZOS)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    im.save(args.out)
    print("saved", args.out, im.size)


if __name__ == "__main__":
    main()
