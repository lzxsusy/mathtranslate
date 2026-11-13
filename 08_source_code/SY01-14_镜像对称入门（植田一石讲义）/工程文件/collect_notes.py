# -*- coding: utf-8 -*-
"""collect_notes.py —— 从 src/chunks/*.tex 收集 % [Tutor Note: ...] 批注，生成 审校批注汇总.md。"""
import io, os, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, "src", "chunks")
OUT = os.path.join(ROOT, "审校批注汇总.md")

names = {
    "c00": "卷首 + §1 开篇（p1–p2）", "c01": "§1（p2–p5）", "c02": "§2–§3（p6–p8）",
    "c03": "§3 末–§7（p9–p13）", "c04": "§8（p14–p15）", "c05": "§9 前半（p16–p21）",
    "c06": "§9 末 + §10（p22–p26）", "c07": "§11 + §12 前半（p27–p30）",
    "c08": "§12 末 + §13（p31–p35）", "c09": "§14（p36）", "c10": "参考文献（p37–p40）",
}

rows = []
for f in sorted(os.listdir(CH)):
    if not re.fullmatch(r"c\d\d\.tex", f):
        continue
    key = f[:-4]
    text = open(os.path.join(CH, f), encoding="utf-8").read()
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if "[Tutor Note:" in lines[i]:
            block = [lines[i]]
            j = i + 1
            # 后续以 % 开头的行并入（多行批注）
            while j < len(lines) and lines[j].strip().startswith("%") and "[Tutor Note:" not in lines[j]:
                block.append(lines[j]); j += 1
            rows.append((key, i + 1, block))
            i = j
        else:
            i += 1

with open(OUT, "w", encoding="utf-8", newline="\n") as fo:
    fo.write("# JP02《镜像对称入门》审校批注汇总\n\n")
    fo.write("> 由 `collect_notes.py` 从 `src/chunks/*.tex` 自动生成；改动批注后请重新运行。\n")
    fo.write("> 共 **%d** 条。每条只记录「原文如此 / 疑似笔误 / 记号冲突」，正文一律照原文翻译，未擅自改动。\n\n" % len(rows))
    cur_key = None
    n = 0
    for key, ln, block in rows:
        if key != cur_key:
            fo.write(f"\n## {key} —— {names.get(key, '')}\n\n")
            cur_key = key
        n += 1
        body = " ".join(re.sub(r"^%\s*(\[Tutor Note:\s*)?", "", s).rstrip("]").strip()
                        for s in block)
        body = body.replace("|", "\\|")
        fo.write(f"{n}. （`{key}.tex` 第 {ln} 行）{body}\n")
print("notes:", len(rows), "->", OUT)
