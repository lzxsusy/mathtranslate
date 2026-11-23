# -*- coding: utf-8 -*-
"""GLOSSARY.md -> work/glossary.tsv (english, zh, grade, basis/note)."""
import os, re

HERE = os.path.dirname(__file__)
SRC = os.path.join(HERE, "..", "GLOSSARY.md")
OUT = os.path.join(HERE, "glossary.tsv")

section = ""
rows = []
with open(SRC, encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        m = re.match(r"^##\s+([A-F])\.\s*(.*)$", line)
        if m:
            section = m.group(1) + ". " + m.group(2).strip()
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        if cells[0] in ("英文", "English") or set(cells[0]) <= set("-: "):
            continue
        en, zh = cells[0], cells[1]
        note = cells[2] if len(cells) > 2 else ""
        en = en.replace("\\\\", "\\")
        zh = zh.replace("\\\\", "\\")
        note = note.replace("\\\\", "\\")
        grade = "I"
        basis = "本库:SY01-07 GLOSSARY"
        if section.startswith("B."):
            basis = "人名：保留拉丁字母，不译"
        elif section.startswith("D."):
            basis = "记号约定：见 GLOSSARY §D"
        elif section.startswith("F."):
            basis = "终稿记号裁定：见 GLOSSARY §F"
        elif "原书" in note:
            basis = "原书用语；" + ("备注：" + note if note else "")
        rows.append((en, zh, grade, basis + ("；" + note if note and "原书" not in note else ""), section))

seen = set()
with open(OUT, "w", encoding="utf-8", newline="") as f:
    f.write("english\t中文\t等级\t依据/备注\t节\n")
    for r in rows:
        if r[0] in seen:
            continue
        seen.add(r[0])
        f.write("\t".join(r) + "\n")
print("rows:", len(seen), "->", OUT)
