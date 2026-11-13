# -*- coding: utf-8 -*-
import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf as fitz

PDF = r"<本地路径>"
doc = fitz.open(PDF)
for i, p in enumerate(doc):
    t = p.get_text()
    if "处于相 II" in t or "在 $q" in t or "q≪1" in t:
        print(f"--- page {i+1} ---")
        for ln in t.splitlines():
            if ("且" in ln) or ("q" in ln and ("处于相" in ln or "≪" in ln)):
                print(repr(ln[:160]))
# also dump blocks around the junction
for i, p in enumerate(doc):
    t = p.get_text("blocks")
    for b in t:
        s = b[4]
        if "对于具有" in s or "且 $q" in s:
            print(f"=== block p{i+1} ===")
            print(s[:400])
