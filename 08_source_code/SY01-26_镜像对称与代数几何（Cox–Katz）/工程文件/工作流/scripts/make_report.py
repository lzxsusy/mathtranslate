#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the review deliverables (校订记录 / 译注 / 统计) from review/*.json + review_applied.json.

usage: python make_report.py OUTDIR
"""
import glob, json, os, sys, collections

os.chdir(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else "report"
os.makedirs(OUT, exist_ok=True)

manifest = {m["unit"]: m for m in json.load(open("units/manifest.json", encoding="utf-8"))}
applied = json.load(open("review_applied.json", encoding="utf-8")) if os.path.exists("review_applied.json") else []

# ---- statistics ----
by_type = collections.Counter(a["type"] for a in applied)
by_conf = collections.Counter(a["conf"] for a in applied)
by_file = collections.Counter(a["file"].split("/")[-1] for a in applied)

notes = []
skipped = []
for jf in sorted(glob.glob("review/u*.json")):
    d = json.load(open(jf, encoding="utf-8"))
    for n in d.get("notes", []):
        n["unit"] = d.get("unit")
        notes.append(n)
    for s in d.get("skipped", []):
        s["unit"] = d.get("unit")
        skipped.append(s)

# ---- 校订记录 ----
lines = ["# 校订记录 · SY01-26《镜像对称与代数几何》(Cox–Katz)", "",
         f"- 逐单元对照原文（RapidOCR 300 dpi，`ocr2/pNNN.txt`）后机械套用；共 **{len(applied)}** 条改动。",
         "- 页码 `PDF` 为原扫描件物理页（= 译本 `\\SourcePage{N}`），`书 p` 为原书印刷页码（PDF − 23）。", "",
         "| # | 章 | PDF | 书 p | 类型 | 置信 | 原文（译本） | 订正 | 依据 |", "|---|---|---|---|---|---|---|---|---|"]
for i, a in enumerate(applied, 1):
    pg = a.get("page") or ""
    book = (str(int(pg) - 23) if str(pg).isdigit() else "")
    q = a["quote"].replace("|", "\\|")
    nw = a["new"].replace("|", "\\|")
    pr = (a.get("problem") or "").replace("|", "\\|").replace("\n", " ")
    chap = a["file"].split("/")[-1].replace("chapter", "第").replace(".tex", " 章").replace("appendix", "附录 ")
    lines.append(f"| {i} | {chap} | {pg} | {book} | {a['type']} | {a['conf']} | {q} | {nw} | {pr} |")
open(os.path.join(OUT, "校订记录.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

# ---- 译注 ----
nl = ["# 译注 · SY01-26《镜像对称与代数几何》", "",
      "补作者未讲清处 / 术语歧义 / 跳步说明；正文中以脚注或括注形式给出。", ""]
for n in notes:
    u = n.get("unit")
    m = manifest.get(u, {})
    nl += [f"## {u} · PDF p{n.get('line') and ''}{m.get('p0','?')}–{m.get('p1','?')}", "",
           f"> 原文：{n.get('quote','')}", "", f"{n.get('note','')}", ""]
open(os.path.join(OUT, "译注.md"), "w", encoding="utf-8").write("\n".join(nl) + "\n")

# ---- 统计 ----
stat = {"applied": len(applied), "by_type": dict(by_type), "by_conf": dict(by_conf),
        "by_file": dict(by_file), "notes": len(notes), "skipped": len(skipped),
        "units_done": len({a["unit"] for a in applied})}
json.dump(stat, open(os.path.join(OUT, "统计.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(stat, ensure_ascii=False))
