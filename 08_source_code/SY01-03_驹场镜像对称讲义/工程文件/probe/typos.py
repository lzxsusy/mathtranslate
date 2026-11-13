# -*- coding: utf-8 -*-
"""核查原文笔误候选词的出现页（PDF 页 → 印刷页=PDF-1）。"""
import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')

t = io.open(r"<本地路径>", encoding="utf-8").read()
pages = re.split(r"===== PDF p\.(\d+) =====", t)
pmap = {}
for k in range(1, len(pages), 2):
    pmap[int(pages[k])] = pages[k + 1]

cands = ["empolyed", "obatin", "peridicity", "positon", "contrl", "naive", "exacly",
         "hyeprsurface", "negtative", "corrsponding", "negtaive", "choise", "one pont",
         "discriminat", "isomorophism", "intry", "genertated", "ture", "defomation",
         "Furtheremore", "diemsional", "repect", "constanits", "surprize",
         "make it certain", "Hubsch", "Jocobi", "RG low", "tranformation",
         "differnt", "Forthermore", "equaivalence", "topologival", "indentified",
         "supersymetry", "Lagragian", "traget", "excatly", "therefor", "wether",
         "emperical", "piont", "remeber", "recieve", "seperated", "occured"]
for w in cands:
    hits = [p for p, txt in pmap.items() if w in txt]
    if hits:
        print(f"{w!r:22s} PDF {hits}  -> 印刷 {[p-1 for p in hits]}")
