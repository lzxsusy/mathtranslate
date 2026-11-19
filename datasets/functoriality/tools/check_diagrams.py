#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_diagrams.py —— 编译校验资料卡里的 TikZ 交换图，并渲染 PNG。

卡的 `diagrams[].tikz` 是自足的 LaTeX 片段（tikz-cd 命令 + 本脚本 preamble 预定义
的一小组记号宏）。每张图单独用 standalone 类编译：既验证能不能过 LaTeX，
又直接得到紧贴内容的页面，再转 PNG 供 md/ 与站点引用。

用法：
    python tools/check_diagrams.py cards                      # 只编译校验
    python tools/check_diagrams.py cards --png                # 校验 + 写 md/diagrams/*.png
    python tools/check_diagrams.py cards --png --verbose      # 逐图列出
    python tools/check_diagrams.py cards --only mww-composition,phi-sharp-induction
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MUTOOL_CANDIDATES = [
    shutil.which("mutool"),
    r"C:\Users\admin\AppData\Local\Microsoft\WinGet\Packages\ArtifexSoftware.mutool_Microsoft.Winget.Source_8wekyb3d8bbwe\mupdf-1.28.5-windows\mutool.exe",
    "/usr/bin/mutool",
]

PREAMBLE = r"""\documentclass[border=8pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{tikz}
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,calc,positioning}
\newcommand{\Fuk}{\operatorname{Fuk}}
\newcommand{\HF}{HF}
\newcommand{\SH}{SH}
\newcommand{\SC}{SC}
\newcommand{\HH}{HH}
\newcommand{\QC}{QC}
\newcommand{\QH}{QH}
\newcommand{\MC}{MC}
\newcommand{\Ainf}{A_\infty}
\newcommand{\wt}{\widetilde}
\newcommand{\ol}{\overline}
\newcommand{\pt}{\mathrm{pt}}
\newcommand{\op}{\mathrm{op}}
\newcommand{\bC}{\mathbb{C}}
\newcommand{\bR}{\mathbb{R}}
\newcommand{\bZ}{\mathbb{Z}}
\newcommand{\bP}{\mathbb{P}}
\newcommand{\CP}{\mathbb{C}\mathrm{P}}
\begin{document}
"""


def find_mutool():
    for c in MUTOOL_CANDIDATES:
        if c and Path(c).exists():
            return c
    return None


def collect(cards_dir, only=None):
    """返回 [(slug, index, title, tikz)]，按卡 id 排序。"""
    out = []
    for p in sorted(Path(cards_dir).glob("**/*.json")):
        if only and p.stem not in only:
            continue
        card = json.loads(p.read_text(encoding="utf-8"))
        for i, d in enumerate(card.get("diagrams") or [], start=1):
            out.append((p.stem, i, d.get("title", ""), d.get("tikz", "")))
    return out


def compile_one(tikz, workdir, stem):
    d = workdir / stem
    d.mkdir(exist_ok=True)
    tex = d / "one.tex"
    tex.write_text(PREAMBLE + tikz.strip() + "\n\\end{document}\n", encoding="utf-8")
    cmd = ["xelatex", "-interaction=nonstopmode", "-halt-on-error", tex.name]
    r = subprocess.run(cmd, cwd=str(d), capture_output=True, text=True,
                       errors="replace", timeout=300)
    log = d / "one.log"
    text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    errs = [m.group(1).strip() for m in re.finditer(r"^! (.*)$", text, re.M)]
    return r.returncode, (errs[0] if errs else ("编译失败（见 " + str(log) + "）" if r.returncode else "")), d / "one.pdf"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cards", nargs="?", default="cards")
    ap.add_argument("--png", action="store_true", help="渲染 md/diagrams/ 下的 PNG")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--only", default="", help="逗号分隔的卡 slug，只处理这些")
    args = ap.parse_args()

    only = {s.strip() for s in args.only.split(",") if s.strip()} or None
    diagrams = collect(ROOT / args.cards, only)
    if not diagrams:
        print("没有找到 diagrams 字段：0 张图")
        return 0

    mutool = find_mutool() if args.png else None
    if args.png and not mutool:
        print("WARN 未找到 mutool，跳过 PNG 渲染（只做编译校验）")

    out_dir = ROOT / "md" / "diagrams"
    if mutool:
        out_dir.mkdir(parents=True, exist_ok=True)

    bad, done = [], 0
    with tempfile.TemporaryDirectory(prefix="card_diagrams_") as td:
        workdir = Path(td)
        for slug, i, title, tikz in diagrams:
            code, err, pdf = compile_one(tikz, workdir, "%s_%d" % (slug, i))
            if code != 0:
                bad.append(("%s-%d" % (slug, i), err))
                continue
            done += 1
            if mutool and args.png:
                dst = out_dir / ("%s-%d.png" % (slug, i))
                subprocess.run([mutool, "draw", "-r", "220", "-o", str(dst), str(pdf)],
                               capture_output=True, text=True, errors="replace", timeout=120)
            if args.verbose:
                print("  OK  %s-%d  %s" % (slug, i, title))

    print("图 %d 张（%d 张卡）：编译通过 %d" % (len(diagrams), len({d[0] for d in diagrams}), done))
    for label, msg in bad:
        print("  ERROR", label, "—", msg)
    if mutool and args.png and done:
        print("PNG → md/diagrams/（%d 张）" % done)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
