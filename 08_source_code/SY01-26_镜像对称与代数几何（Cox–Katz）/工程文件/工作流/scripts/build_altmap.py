#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Map printed page numbers of the two-up scan 镜对称与代数几何.pdf to (alt page, side).

For each page we OCR the top-left and top-right corners; the digits found there are the
printed page numbers.  Output: altmap.json  {printed: [alt_page, "L"|"R"]}
"""
import json, os, re, sys
import pymupdf
from rapidocr_onnxruntime import RapidOCR
from concurrent.futures import ProcessPoolExecutor

SRC = r"C:\Users\admin\Desktop\归档\08_教材与参考书\镜对称与代数几何.pdf"
OUT = "altmap.json"
_ocr = None


def ocr_digits(img):
    global _ocr
    if _ocr is None:
        _ocr = RapidOCR()
    res, _ = _ocr(img)
    if not res:
        return None
    txt = " ".join(r[1] for r in res)
    m = re.findall(r"\d{1,3}", txt)
    return m[0] if m else None


def work(i):
    doc = pymupdf.open(SRC)
    pg = doc[i]
    w, h = pg.rect.width, pg.rect.height
    z = 200 / 72.0
    out = []
    for x0, x1 in ((0, w * 0.18), (w * 0.82, w)):
        clip = pymupdf.Rect(x0, h * 0.03, x1, h * 0.12)
        pix = pg.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=clip)
        out.append(ocr_digits(pix.tobytes("png")))
    return i, out[0], out[1]


if __name__ == "__main__":
    n = pymupdf.open(SRC).page_count
    res = {}
    with ProcessPoolExecutor(max_workers=int(os.environ.get("W", "8"))) as ex:
        for i, l, r in ex.map(work, range(n)):
            res[i] = [l, r]
            if i % 20 == 0:
                print(i, l, r, flush=True)
    json.dump(res, open(OUT, "w"), indent=0)
    print("pages", n, "->", OUT)
