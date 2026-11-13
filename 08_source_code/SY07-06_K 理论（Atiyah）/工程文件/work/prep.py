# -*- coding: utf-8 -*-
"""Atiyah K-Theory (Japanese trans.) —— 预处理：渲染页面图像 + 提取文字层。"""
import pymupdf, os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

SRC = r"<本地路径> (M.F.アティヤ Michael Francis Atiyah) (z-library.sk  1lib.sk  z-lib.sk).pdf"
ROOT = r"<本地路径>"
PAGES = os.path.join(ROOT, "work", "pages")
SPLIT = os.path.join(ROOT, "work", "split")
for d in (PAGES, SPLIT):
    os.makedirs(d, exist_ok=True)

doc = pymupdf.open(SRC)
print("pages:", doc.page_count, flush=True)

full = []
stats = []
for i in range(doc.page_count):
    page = doc[i]
    n = f"p{i+1:03d}"
    img = os.path.join(PAGES, n + ".png")
    if not os.path.exists(img):
        pix = page.get_pixmap(dpi=150)
        pix.save(img)
    t = page.get_text("text")
    with open(os.path.join(SPLIT, n + ".txt"), "w", encoding="utf-8") as f:
        f.write(t)
    full.append(f"===== PDF PAGE {i+1} =====\n{t}")
    stats.append({"pdf": i + 1, "textlen": len(t), "imgs": len(page.get_images()),
                  "w": round(page.rect.width), "h": round(page.rect.height)})

with open(os.path.join(ROOT, "work", "full.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(full))
with open(os.path.join(ROOT, "work", "page_stats.json"), "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=0)
with open(os.path.join(ROOT, "work", "toc.json"), "w", encoding="utf-8") as f:
    json.dump(doc.get_toc(), f, ensure_ascii=False)
print("done. blank/short pages:", [s["pdf"] for s in stats if s["textlen"] < 50], flush=True)
