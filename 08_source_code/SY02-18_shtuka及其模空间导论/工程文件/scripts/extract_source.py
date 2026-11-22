# -*- coding: utf-8 -*-
"""SY02-16 原文抽取：PDF 文本层按页导出 + 逐页位图（公式核对用）。
用法： python extract_source.py
输入： 工程文件/work/pdf/src.pdf（原 PDF 工作副本）
输出： 工程文件/work/原文/full.txt（===== PDF PAGE n ===== 分页标记）
       工程文件/work/pages/pNNN.png（170 dpi）
"""
import os
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "work", "pdf", "src.pdf")
OUT_TXT = os.path.join(ROOT, "work", "原文", "full.txt")
OUT_IMG = os.path.join(ROOT, "work", "pages")


def main() -> None:
    os.makedirs(os.path.dirname(OUT_TXT), exist_ok=True)
    os.makedirs(OUT_IMG, exist_ok=True)
    doc = pymupdf.open(PDF)
    chunks = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text()
        chunks.append("===== PDF PAGE %d =====" % i)
        chunks.append(text.rstrip())
        pix = page.get_pixmap(dpi=170)
        pix.save(os.path.join(OUT_IMG, "p%03d.png" % i))
    with open(OUT_TXT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(chunks) + "\n")
    print("pages:", doc.page_count)
    print("text bytes:", os.path.getsize(OUT_TXT))
    print("images:", len([f for f in os.listdir(OUT_IMG) if f.endswith(".png")]))


if __name__ == "__main__":
    sys.exit(main())
