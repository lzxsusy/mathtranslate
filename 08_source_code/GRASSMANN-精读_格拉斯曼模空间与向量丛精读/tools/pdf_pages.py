# -*- coding: utf-8 -*-
"""格拉斯曼精读项目工具：取页文本 / 渲染页面 PNG / 打印章节页表。

用法（Python 路径见 任务书.md）：
  python tools/pdf_pages.py map
  python tools/pdf_pages.py text zh 7-12            # 输出到 stdout（UTF-8）
  python tools/pdf_pages.py text en 10-13 -o /tmp/x.txt
  python tools/pdf_pages.py png zh 12 --dpi 140 --out 产出/_pages
"""
import sys, os, io, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = {"zh": os.path.join(ROOT, "zh-译文.pdf"),
       "en": os.path.join(ROOT, "original", "en-原书.pdf")}

# 章节页表：章 -> (中文 PDF 页起止, 英文 PDF 页起止, 原书印刷页, 源文件)
CH = [
    ("前言/引言", (1, 6), (1, 9), "i–viii", "chapters/frontmatter.tex"),
    ("ch1 Hitchin 联络/Toeplitz", (7, 29), (10, 33), "1–24", "chapters/ch01.tex"),
    ("ch2 Koszul 上同调", (30, 54), (34, 59), "25–50", "chapters/ch02.tex"),
    ("ch3 Reider/Thaddeus", (55, 71), (60, 77), "51–68", "chapters/ch03.tex"),
    ("ch4 奇异模空间相交配对", (72, 81), (78, 89), "69–80", "chapters/ch04.tex"),
    ("ch5 Beilinson–Drinfeld 格拉斯曼", (82, 93), (90, 103), "81–94", "chapters/ch05.tex"),
    ("ch6 曲线上层模空间的算术", (94, 115), (104, 129), "95–120", "chapters/ch06.tex"),
    ("ch7 α-稳定凝聚系存在性", (116, 134), (130, 149), "121–140", "chapters/ch07.tex"),
    ("ch8 阿贝尔簇上的正则性 III", (135, 159), (150, 177), "141–168", "chapters/ch08.tex"),
    ("ch9 可约曲线上的向量丛", (160, 170), (178, 190), "169–179", "chapters/ch09.tex"),
]


def parse_pages(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        elif part:
            out.append(int(part))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["map", "text", "png", "outline"])
    ap.add_argument("which", nargs="?", default="zh", choices=["zh", "en"])
    ap.add_argument("pages", nargs="?", default="1")
    ap.add_argument("--dpi", type=int, default=140)
    ap.add_argument("--out", default="")
    ap.add_argument("-o", dest="ofile", default="")
    a = ap.parse_args()

    if a.cmd == "map":
        print(f"{'章':38s} {'中文PDF':>10s} {'英文PDF':>10s} {'原书页':>10s}  源文件")
        for name, z, e, op, f in CH:
            print(f"{name:38s} {z[0]:>4}-{z[1]:<5} {e[0]:>4}-{e[1]:<5} {op:>10s}  {f}")
        return

    import pymupdf
    doc = pymupdf.open(PDF[a.which])

    if a.cmd == "outline":
        for lvl, title, pg in doc.get_toc():
            print(f"{'  ' * (lvl - 1)}[{pg}] {title}")
        return

    pages = parse_pages(a.pages)
    if a.cmd == "text":
        buf = io.StringIO()
        for p in pages:
            if 1 <= p <= doc.page_count:
                buf.write(f"\n===== {a.which.upper()} PDF p{p} =====\n")
                buf.write(doc[p - 1].get_text())
        s = buf.getvalue()
        if a.ofile:
            io.open(a.ofile, "w", encoding="utf-8").write(s)
            print(f"wrote {a.ofile} ({len(s)} chars)")
        else:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stdout.write(s)
    elif a.cmd == "png":
        outdir = a.out or os.path.join(ROOT, "产出", "_pages")
        os.makedirs(outdir, exist_ok=True)
        for p in pages:
            pix = doc[p - 1].get_pixmap(dpi=a.dpi)
            fp = os.path.join(outdir, f"{a.which}-p{p:03d}.png")
            pix.save(fp)
            print(fp)


if __name__ == "__main__":
    main()
