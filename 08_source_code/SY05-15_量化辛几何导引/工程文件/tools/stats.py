#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计全书指标：页数、图数、公式编号、Tutor Note、定理环境、章节数。"""
import re
from pathlib import Path

QSG = Path(__file__).resolve().parent.parent
TEX = QSG / "tex"


def main():
    files = sorted(TEX.glob("*.tex"))
    text = "\n".join(f.read_text(encoding="utf-8") for f in files)
    body = re.sub(r"(?m)^\s*%.*$", "", text)  # 去注释行
    tags = re.findall(r"\\tag\*?\{([^}]+)\}", text)
    notes = len(re.findall(r"%\s*\[Tutor Note", text))
    chapters = len(re.findall(r"\\chapter\{", body))
    sections = len(re.findall(r"\\section\{", body))
    takes = len(re.findall(r"\\begin\{keytakeaways\}", body))
    envs = len(re.findall(r"\\begin\{w(?:defn|thm|prop|lem|cor|conj|exam|exer|rem|not|clm|prob|que|fact)\}", body))
    figs = len(re.findall(r"\\begin\{figure\}", body))
    figfiles = len(list((QSG / "figures").glob("*.png")))
    # 公式编号按章统计
    per = {}
    for t in tags:
        ch = t.split(".")[0]
        per.setdefault(ch, []).append(t)
    print(f"tex 片段: {len(files)}")
    print(f"章: {chapters}  节: {sections}  本节重点盒: {takes}")
    print(f"定理类环境: {envs}")
    print(f"公式编号: {len(tags)}")
    print(f"图（figure 环境）: {figs}   裁剪图文件: {figfiles}")
    print(f"Tutor Note: {notes}")
    for ch in sorted(per, key=lambda x: (len(x), x)):
        print(f"  ch{ch}: {len(per[ch])} 个编号")


if __name__ == "__main__":
    main()
