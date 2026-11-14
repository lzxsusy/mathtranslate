#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 main.tex：按 front -> 各章文件 -> 文献/索引 的顺序拼装。

同时在每章第一片段前写入 \\setcounter{chapter}{N-1}，
保证即使只编译部分章节，章号也与原书一致（第 2 章就是第 2 章）。
"""
import re
from pathlib import Path

QSG = Path(__file__).resolve().parent.parent
TEX = QSG / "tex"

HEAD = r"""\documentclass[UTF8,11pt,fontset=fandol,openany,oneside,a4paper]{ctexbook}
\usepackage[a4paper,margin=2.6cm]{geometry}
\input{preamble}
\begin{document}
\frontmatter
"""


def chapter_no(name: str):
    m = re.match(r"ch(\d+)", name)
    return int(m.group(1)) if m else None


def natural(p: Path):
    m = re.match(r"ch(\d+)([a-z]?)", p.stem)
    if m:
        return (int(m.group(1)), m.group(2), p.name)
    return (999, "", p.name)


def build_lines(with_front=True):
    lines = []
    if with_front:
        lines.append(r"\input{tex/00-front.tex}")
        lines.append(r"\mainmatter")
    current = None
    files = sorted(TEX.glob("ch*.tex"), key=natural)
    for f in files:
        no = chapter_no(f.name)
        if no is not None and no != current:
            lines.append(r"\setcounter{chapter}{%d}" % (no - 1))
            current = no
        lines.append(r"\input{tex/%s}" % f.name)
    for name in ("90-bib.tex", "91-index.tex"):
        if (TEX / name).exists():
            lines.append(r"\input{tex/%s}" % name)
    return lines, files


def main():
    front = TEX / "00-front.tex"
    lines, files = build_lines(front.exists())
    (QSG / "main.tex").write_text(HEAD + "\n".join(lines) + "\n\\end{document}\n",
                                  encoding="utf-8")
    print(f"main.tex: {len(files)} 个章节片段")
    for f in files:
        print("  ", f.name)


if __name__ == "__main__":
    main()
