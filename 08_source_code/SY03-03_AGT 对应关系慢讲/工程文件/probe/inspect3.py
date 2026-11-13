# -*- coding: utf-8 -*-
import sys, re, io
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz
PDF = r"<本地路径>).pdf"
doc = fitz.open(PDF)
print("=== FULL TOC ===")
for lvl, title, pg in doc.get_toc():
    print(f"L{lvl} p{pg}: {title}")
print("\n=== PAGE 2 (contents) ===")
print(doc[1].get_text())
print("\n=== p105 tail ===")
print(doc[104].get_text()[-1500:])
print("\n=== p106 full ===")
print(doc[105].get_text())
print("\n=== p107 head ===")
print(doc[106].get_text()[:800])
print("\n=== 'Table' captions ===")
for i,p in enumerate(doc):
    t=p.get_text()
    for m in re.finditer(r"Table\s+(\d+):", t):
        print(f"p{i+1}: {t[max(0,m.start()-10):m.start()+120]}".replace("\n"," | "))
