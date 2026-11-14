# -*- coding: utf-8 -*-
"""Generate a Markdown index of all % [Tutor Note: ...] annotations.

Usage: python gen_notes_index.py
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEC = os.path.join(ROOT, "sections")

ORDER = ["intro"]
for n in range(1, 20):
    ORDER += [f"lec{n:02d}_p{1}"]
ORDER += ["exo_p1", "sol_p1", "sol_p2"]

# use actual files in page order instead
files = []
for f in glob.glob(os.path.join(SEC, "*.tex")):
    base = os.path.basename(f)
    m = re.match(r"lec(\d+)_p(\d+)", base)
    if m:
        files.append((int(m.group(1)), int(m.group(2)), f))
    elif base == "lec09.tex":
        files.append((9, 0, f))
    elif base.startswith("sol"):
        files.append((100, 0, f))
    elif base.startswith("exo"):
        files.append((99, 0, f))
files.sort()

out = ["# 审校批注索引（Tutor Notes）", "",
       "本索引由源文件中的 `% [Tutor Note: ...]` 注释自动提取；",
       "页号为 PDF 扫描页序（原书印刷页 = 扫描页 + 1118）。", ""]

count = 0
for lec, part, f in files:
    src = open(f, encoding="utf-8").read()
    cur_page = 0
    notes = []
    for line in src.splitlines():
        m = re.match(r"%\s*=====\s*原文\s*p\.(\d+)", line)
        if m:
            cur_page = int(m.group(1))
        if re.match(r"%\s*\[Tutor Note:", line):
            txt = re.sub(r"^%\s*\[Tutor Note:\s*", "", line)
            notes.append((cur_page, txt[:160]))
    if not notes:
        continue
    label = f"第 {lec} 讲" if lec <= 19 else ("习题" if lec == 99 else "解答")
    out.append(f"## {label}（{os.path.basename(f)}）")
    out.append("")
    for p, t in notes:
        out.append(f"- **p.{p}** — {t}")
        count += 1
    out.append("")

out.insert(4, f"共 **{count}** 条批注。")
path = os.path.join(ROOT, "审校批注索引.md")
open(path, "w", encoding="utf-8").write("\n".join(out))
print("wrote", path, "notes:", count)
