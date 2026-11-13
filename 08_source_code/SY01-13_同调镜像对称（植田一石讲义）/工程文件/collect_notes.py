# -*- coding: utf-8 -*-
"""生成 审校批注汇总.md：从各 chunk 抽出 Tutor Note。"""
import io, os, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, "src", "chunks")
OUT = os.path.join(ROOT, "审校批注汇总.md")

PAGE = {
    "c00": "p001–p005", "c01": "p006–p009", "c02": "p010–p013", "c03": "p014–p015",
    "c04": "p016–p018", "c05": "p019–p021", "c06": "p022–p023", "c07": "p024–p028",
    "c08": "p029–p032", "c09": "p033–p036", "c10": "p037–p042", "c11": "p043–p049",
    "c12": "p050–p064",
}

lines = ["# 审校批注汇总（Tutor Notes）", "",
         "> 全部来自译者对原文存疑处的标注；译本正文一律照录原文，不改写、不补写。",
         "> 供后续审校逐条裁定。", ""]
n = 0
for name in sorted(PAGE):
    p = os.path.join(CH, name + ".tex")
    if not os.path.exists(p):
        continue
    t = open(p, encoding="utf-8").read()
    notes = re.findall(r"%\s*\[Tutor Note:\s*(.*?)\]", t, re.S)
    if not notes:
        continue
    lines.append(f"## {name}（{PAGE[name]}）")
    lines.append("")
    for k, note in enumerate(notes, 1):
        note = " ".join(note.split())
        lines.append(f"{k}. {note}")
        n += 1
    lines.append("")
lines.append(f"---\n\n共 {n} 条。")
open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print(f"已写 {OUT}，共 {n} 条批注")
