# -*- coding: utf-8 -*-
r"""从 src/chunks/*.tex 抽取全部 % [Tutor Note: ...] 批注，生成 译注汇总.md
用法：python tools/gen_notes.py
"""
import sys, io, os, glob, re
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
OUT = os.path.join(ROOT, "译注汇总.md")

CHUNK_CN = {
    "c01": "第 1 章 引言与概述", "ch02": "第 2 章 四维规范理论的对偶",
    "ch03": "第 3 章 Vafa–Witten 理论作为带规范场的 4d A-模型",
    "ch04": "第 4 章 拓扑场论、范畴与 2-范畴", "ch05": "第 5 章 在圆上紧化",
    "ch06a": "第 6 章 4d TFT 的面算子（上）", "ch06b": "第 6 章 4d TFT 的面算子（下）",
    "ch07": "第 7 章 修正 A-模型", "ch08": "第 8 章 Vafa–Witten 理论在 g≥2 黎曼面上的紧化",
    "ch09": "第 9 章 二维 σ-模型的缺陷", "appA": "附录 A 2d TFT", "appB": "附录 B 3d TFT",
    "appC": "附录 C 相伴纤维丛与等变上同调", "appD": "附录 D 第 9 章命题的证明",
}

def chunk_of(name):
    m = re.match(r"([a-z0-9]+?)(?:-\d+)?\.tex$", name)
    if not m:
        return name
    base = m.group(1)
    if base.startswith("ch06a"):
        return "ch06a"
    if base.startswith("ch06b"):
        return "ch06b"
    return base

files = []
for base in CHUNK_CN:
    files += sorted(glob.glob(os.path.join(CH, f"{base}-*.tex")))
files = [f for f in files if os.path.basename(f) != "_order.tex"]

items = []
for f in files:
    txt = io.open(f, encoding="utf-8", errors="replace").read()
    # 记录当前原文页码
    page = "?"
    for i, ln in enumerate(txt.splitlines(), 1):
        m = re.search(r"%\s*\[原文 p\.(\d+)\]", ln)
        if m:
            page = m.group(1)
        m2 = re.match(r"\s*%\s*\[Tutor Note:(.*)$", ln)
        if m2:
            body = m2.group(1)
            j = i
            lines = txt.splitlines()
            # 跨行批注：后续以 % 开头的行并入
            while j < len(lines) and re.match(r"^\s*%", lines[j]) and "[Tutor Note" not in lines[j]:
                body += "\n" + re.sub(r"^\s*%\s?", "", lines[j])
                j += 1
            body = body.strip()
            body = re.sub(r"\]\s*$", "", body).strip()
            items.append((os.path.basename(f), page, body))

with io.open(OUT, "w", encoding="utf-8", newline="\n") as fo:
    fo.write("# 译注汇总（Tutor Notes）\n\n")
    fo.write("本文件由 `tools/gen_notes.py` 从 LaTeX 源码中的 `% [Tutor Note: ...]` 注释自动生成，\n")
    fo.write("与源码保持同步。批注是译者所加，不进入排版；每条都尽量给出可核对的依据。\n\n")
    fo.write(f"共 **{len(items)}** 条。\n\n")
    cur = None
    for fn, page, body in items:
        base = chunk_of(fn)
        if base != cur:
            cur = base
            fo.write(f"\n## {CHUNK_CN.get(base, base)}\n\n")
        fo.write(f"- **原文 p.{page}**（`{fn}`）：{body}\n")
print("notes:", len(items), "->", OUT)
