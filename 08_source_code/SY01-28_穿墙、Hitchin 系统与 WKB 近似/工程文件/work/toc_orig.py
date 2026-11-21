import pymupdf
d = pymupdf.open(r"C:\Users\admin\Desktop\GMN系列\00_原文\GMN2_0907.3987\0907.3987v2.pdf")
out = []
for i in range(min(6, d.page_count)):
    out.append("=== page %d ===" % (i + 1))
    out.append(d[i].get_text())
open(r"C:\Users\admin\Desktop\GMN系列\01_翻译\GMN2_0907.3987\工程文件\work\orig_toc.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok", d.page_count)
