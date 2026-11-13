# -*- coding: utf-8 -*-
"""底本尽调：深谷賢治《シンプレクティック幾何学》"""
import pymupdf, os, json, re

SRC = r"<本地路径> (深谷賢治 Kenji Fukaya) (z-library.sk  1lib.sk  z-lib.sk).pdf"

doc = pymupdf.open(SRC)
print("pages:", doc.page_count)
print("metadata:", json.dumps(doc.metadata, ensure_ascii=False, indent=1))

n = doc.page_count
# per page: text length, image count, drawings count
textlen = []
imgcnt = []
drawcnt = []
for i in range(n):
    p = doc[i]
    t = p.get_text("text")
    textlen.append(len(t.strip()))
    imgcnt.append(len(p.get_images(full=True)))
    drawcnt.append(len(p.get_drawings()))

tot_text = sum(textlen)
print("total extracted chars:", tot_text)
print("pages with <20 chars text:", sum(1 for x in textlen if x < 20))
print("pages with 0 images:", sum(1 for x in imgcnt if x == 0))
print("total images (refs):", sum(imgcnt))
print("total drawings:", sum(drawcnt))

# first 15 pages text sample
for i in range(min(15, n)):
    t = doc[i].get_text("text").strip()
    print(f"===== PDF p{i+1} len={len(t)} imgs={imgcnt[i]} =====")
    print(t[:600])

# fonts on a middle page
print("\n--- fonts page 50 ---")
for f in doc[49].get_fonts(full=True):
    print(f)

# page size
print("page rect:", doc[10].rect)

doc.close()
