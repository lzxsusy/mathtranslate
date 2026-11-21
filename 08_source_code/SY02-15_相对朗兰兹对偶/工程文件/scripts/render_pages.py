# -*- coding: utf-8 -*-
"""Render every PDF page to PNG for symbol-by-symbol formula checking.

Usage:  python render_pages.py [dpi]
Output: 工程文件/work/pages/pNNN.png  (1-based page numbers, zero padded)
"""
import os
import sys

import fitz  # pymupdf

PDF = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\20-BenZvi_LAWRG2024_lectures.pdf"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "work", "pages"))


def main() -> None:
    dpi = int(sys.argv[1]) if len(sys.argv) > 1 else 170
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF)
    print("pages:", doc.page_count, "dpi:", dpi)
    for i, page in enumerate(doc, start=1):
        path = os.path.join(OUT, "p%03d.png" % i)
        if os.path.exists(path):
            continue
        pix = page.get_pixmap(dpi=dpi)
        pix.save(path)
    print("done ->", OUT)


if __name__ == "__main__":
    main()
