# -*- coding: utf-8 -*-
r"""把底本 PDF 逐页拆成 文本 + PNG（供译手回图核对公式）。"""
import os, subprocess, sys

PDF = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\Kontsevich_Soibelman_HMS_TorusFibrations.pdf"
ROOT = r"C:\Users\admin\Desktop\数译发布\shuyi\translations\SY01-25"
WORK = os.path.join(ROOT, "工程文件", "work")
PAGES = os.path.join(WORK, "pages")
os.makedirs(PAGES, exist_ok=True)

# 总页数
out = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
n = 66
for line in out.splitlines():
    if line.startswith("Pages:"):
        n = int(line.split()[1])
print("pages:", n)

for i in range(1, n + 1):
    txt = os.path.join(PAGES, "p%03d.txt" % i)
    subprocess.run(["pdftotext", "-layout", "-f", str(i), "-l", str(i), PDF, txt], check=True)
print("text done")

for i in range(1, n + 1):
    png = os.path.join(PAGES, "p%03d" % i)   # pdftoppm 自动补 -1.png/.png
    if os.path.exists(png + ".png") or os.path.exists(png + "-%02d.png" % i):
        continue
    subprocess.run(["pdftoppm", "-r", "160", "-png", "-f", str(i), "-l", str(i), "-singlefile", PDF, png], check=True)
print("png done")
