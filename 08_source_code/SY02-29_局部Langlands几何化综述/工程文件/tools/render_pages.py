# -*- coding: utf-8 -*-
"""render_pages.py —— 把底本某几页渲染成 PNG（公式核对用）

用法：
    python 工程文件/tools/render_pages.py 3 4 5            # 渲染 p.3–p.5
    python 工程文件/tools/render_pages.py 3-10 --dpi 170   # 渲染 p.3–p.10
输出到 工程文件/work/pages/pNNN.png（已存在则跳过）。
"""
import sys, os, re
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 工程文件/
PROJ = os.path.dirname(ROOT)
PDF = os.path.join(os.environ.get("FG16_SRC", r"C:\Users\admin\Documents\deepseek-harness\default-workspace\fargues_ov"),
                   "Fargues_Geometrization_overview.pdf")
OUT = os.path.join(ROOT, "work", "pages")


def pages_from_args(args):
    out = []
    if "--dpi" in args:
        i = args.index("--dpi")
        args = args[:i] + args[i + 2:]
    for a in args:
        if not a.startswith("-"):
            if "-" in a:
                lo, hi = a.split("-")
                out.extend(range(int(lo), int(hi) + 1))
            else:
                out.append(int(a))
    return out


def main():
    args = sys.argv[1:]
    dpi = 150
    if "--dpi" in args:
        dpi = int(args[args.index("--dpi") + 1])
    nums = pages_from_args(args)
    if not nums:
        print(__doc__)
        return 1
    os.makedirs(OUT, exist_ok=True)
    doc = pymupdf.open(PDF)
    for n in nums:
        path = os.path.join(OUT, "p%03d.png" % n)
        if os.path.exists(path):
            print("skip", path)
            continue
        page = doc[n - 1]
        pix = page.get_pixmap(dpi=dpi)
        pix.save(path)
        print("saved", path, pix.width, "x", pix.height)
    return 0


if __name__ == "__main__":
    sys.exit(main())
