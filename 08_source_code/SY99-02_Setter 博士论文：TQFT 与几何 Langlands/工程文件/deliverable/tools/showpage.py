import sys, re
sys.stdout.reconfigure(encoding="utf-8")
import pymupdf
d = pymupdf.open(r"<本地路径>")
pno = int(sys.argv[1]) if len(sys.argv) > 1 else 21
t = d[pno - 1].get_text()
sys.stdout.write(f"===== PDF p.{pno} =====\n" + t)
