# -*- coding: utf-8 -*-
"""抽检：把编译后 PDF 的某页与原文对应页并排成一张图，供人眼比对。

用法：
  python sample_pages.py            # 每节取 1 页（默认抽样表），输出到 工程文件/work/抽检/
  python sample_pages.py 12 26 47   # 指定原文页码（印刷页）

映射方式：编译稿每页页边有 \\srcpage 打的 `1252–NN` 边注，用 pdftotext 抽出全文，
按页找该记号即可把「原文页 NN」映射到「编译稿第 k 页」。
"""
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image

BASE = Path(__file__).resolve().parent.parent.parent
PDF = BASE / "源码" / "main.pdf"
PAGES = BASE / "工程文件" / "work" / "pages"
OUTDIR = BASE / "工程文件" / "work" / "抽检"
DPI = 130

# 每节抽 1 页（原文印刷页）
DEFAULT = [3, 12, 21, 24, 26, 34, 36, 39, 42, 47, 50, 53]


def page_map():
    txt = subprocess.run(
        ["pdftotext", "-layout", str(PDF), "-"], capture_output=True
    ).stdout.decode("utf-8", "replace")
    pages = txt.split("\f")
    m = {}
    for i, p in enumerate(pages, 1):
        for nn in re.findall(r"1252[-–—]{1,2}\s*(\d{1,2})", p):
            m.setdefault(int(nn), i)
    return m


def render(pdf_page, out):
    subprocess.run(
        ["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", str(DPI), "-png", "-singlefile", str(PDF), str(out)],
        check=True,
    )
    return Path(str(out) + ".png")


def main():
    src_pages = [int(x) for x in sys.argv[1:]] or DEFAULT
    if not PDF.exists():
        sys.exit(f"缺少 {PDF}，请先编译 main.tex")
    OUTDIR.mkdir(parents=True, exist_ok=True)
    m = page_map()
    print(f"映射到 {len(m)} 个原文页")
    rows = []
    for nn in src_pages:
        if nn not in m:
            print(f"!! 原文 p{nn} 在编译稿中找不到页锚")
            continue
        k = m[nn]
        zh = render(k, OUTDIR / f"_zh_p{nn:03d}")
        orig = PAGES / f"p{nn:03d}.png"
        a = Image.open(zh).convert("RGB")
        b = Image.open(orig).convert("RGB")
        h = max(a.height, b.height)
        canvas = Image.new("RGB", (a.width + b.width + 16, h), "white")
        canvas.paste(b, (0, 0))
        canvas.paste(a, (b.width + 16, 0))
        dst = OUTDIR / f"p{nn:03d}.png"
        canvas.save(dst)
        rows.append(f"原文 p{nn} ↔ 编译稿第 {k} 页 → {dst.name}（左原文，右译文）")
        print(rows[-1])
    (OUTDIR / "对照表.txt").write_text("\n".join(rows) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
