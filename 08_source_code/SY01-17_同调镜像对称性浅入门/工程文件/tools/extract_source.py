import pymupdf, re, sys, io
src = r"<本地路径>"
orig = r"<本地路径> Gentle Introduction to Homological Mirror Symmetry (London Mathematical Society Student Texts  Series Number 99) (Raf Bocklandt) (z-library.sk  1lib.sk  z-lib.sk)(1).pdf"
out = r"<本地路径>"
import os
os.makedirs(os.path.dirname(out), exist_ok=True)
d = pymupdf.open(orig)
print("pages", d.page_count)
buf=[]
for i in range(d.page_count):
    t = d[i].get_text("text")
    bp = i+1-12
    buf.append(f"\n===== BOOK PAGE {bp} (PDF {i+1}) =====\n")
    buf.append(t)
open(out,"w",encoding="utf-8").write("".join(buf))
print("written", os.path.getsize(out))
# quick sanity of sample page
print(d[30].get_text("text")[:600])
