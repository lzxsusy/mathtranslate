# -*- coding: utf-8 -*-
"""gen_notes.py — 从 SY05-24 源码抽取 % [Tutor Note: ...] 批注，生成 工程文件\\译注汇总.md"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "源码")

BLOCKS = [
    ("c01", ["abstract.tex", "sec0.tex"], "摘要 + §0 讲义提纲（原文 p1–2）"),
    ("c02", ["sec1a.tex"], "§1 Witten 指标 + §1.1 超对称谐振子（原文 p3–5）"),
    ("c03", ["sec1b.tex"], "§1.2 整体对称性（原文 p6–7）"),
    ("c04", ["sec2a.tex"], "§2 超共形指标 + §2.1 手征多重态（原文 p8–12）"),
    ("c05", ["sec2b.tex"], "§2.2 规范理论的指标、§2.3 重组不变性、§2.4 插叙（原文 p13–18）"),
    ("c06", ["sec3a.tex"], "§3 $\\sN=2$ 理论 + §3.1 超对称极限（原文 p19–22）"),
    ("c07", ["sec3b.tex"], "§3.2 S 对偶、§3.3 Class S 与 TQFT（原文 p23–25）"),
    ("c08", ["sec4.tex"], "§4 大 $N$ 极限 + §4.1 黑洞呢？（原文 p26–30）"),
    ("c09", ["refs.tex"], "参考文献（原文 p31–32）"),
]

NOTE_RE = re.compile(r"^%\s*\[Tutor Note:\s*(.+?)\]\s*$")
PAGE_RE = re.compile(r"^%\s*\[原文 p\.(\d+)\]")


def main():
    rows = []
    sections = []
    total = 0
    for blk, files, title in BLOCKS:
        notes = []
        for f in files:
            p = os.path.join(SRC, f)
            if not os.path.isfile(p):
                continue
            page = "?"
            for ln in io.open(p, encoding="utf-8"):
                m = PAGE_RE.match(ln.strip())
                if m:
                    page = m.group(1)
                    continue
                m = NOTE_RE.match(ln.strip())
                if m:
                    notes.append((page, m.group(1).strip()))
        rows.append((blk, "`" + "` + `".join(files) + "`", len(notes)))
        sections.append((blk, title, notes))
        total += len(notes)

    out = ["# 译注汇总 — SY05-24", "",
           "> 本文件由 `工程文件\\gen_notes.py` 从源码自动抽取，与源码中的 `% [Tutor Note: ...]` 批注逐条对应，条数一致。",
           "> 批注不进排版成品，只随源码交付。", "",
           "| 块 | 文件 | Tutor Note |", "|---|---|---|"]
    for blk, fs, n in rows:
        out.append("| %s | %s | %d |" % (blk, fs, n))
    out.append("| **合计** | | **%d** |" % total)
    out.append("")
    out.append("---")
    out.append("")
    for blk, title, notes in sections:
        out.append("## %s %s" % (blk, title))
        out.append("")
        if not notes:
            out.append("（本块无批注）")
        for i, (page, text) in enumerate(notes, 1):
            out.append("%d. （原文 p.%s）%s" % (i, page, text))
        out.append("")

    dst = os.path.join(HERE, "译注汇总.md")
    io.open(dst, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print("blocks=%d notes=%d -> %s" % (len(rows), total, dst))


if __name__ == "__main__":
    main()
