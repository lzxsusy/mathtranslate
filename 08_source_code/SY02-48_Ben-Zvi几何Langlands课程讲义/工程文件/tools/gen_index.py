# -*- coding: utf-8 -*-
"""从源码 sections/*.tex 抽取编号条目，生成 资料卡/03-条款索引.md。

用法：
  python 工程文件/tools/gen_index.py

编号 = LaTeX 自动排的「讲次.序号」（15 类环境共用一个计数器，按正文出现顺序）；
页码按出现顺序取 工程文件/work/条目总表.tsv 的同讲第 k 行（源文手写编号与
译本自动编号会因原文编号跳号而错位，故不能按编号字符串匹配）。
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEC = os.path.join(ROOT, "源码", "sections")
TOC = os.path.join(ROOT, "lectures", "toc.json")
TABLE = os.path.join(ROOT, "工程文件", "work", "条目总表.tsv")
OUT = os.path.join(ROOT, "资料卡", "03-条款索引.md")

ENVS = ["definition", "theorem", "proposition", "lemma", "corollary", "remark",
        "example", "warning", "question", "conjecture", "notation", "fact",
        "exercise", "construction", "hope"]

ZH = {"definition": "定义", "theorem": "定理", "proposition": "命题", "lemma": "引理",
      "corollary": "推论", "remark": "注", "example": "例", "warning": "警告",
      "question": "问题", "conjecture": "猜想", "notation": "记号", "fact": "事实",
      "exercise": "练习", "construction": "构造", "hope": "期望"}

MACROS = {"infty": "∞", "to": "→", "simeq": "≃", "otimes": "⊗", "oplus": "⊕",
          "times": "×", "subset": "⊂", "hookrightarrow": "↪", "mapsto": "↦",
          "Bun": "Bun", "Rep": "Rep", "Loc": "Loc", "Pic": "Pic", "Gr": "Gr",
          "Hck": "Hck", "Spec": "Spec", "cO": "O", "cC": "C", "cM": "M",
          "cF": "F", "C": "C", "R": "R", "Z": "Z", "Q": "Q", "F": "F",
          "A": "A", "G": "G"}


def plain(s: str, cap: int = 60) -> str:
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"√(\1)", s)
    for k, v in MACROS.items():
        s = re.sub(r"\\" + k + r"(?![a-zA-Z])", v, s)
    s = re.sub(r"\\yizhu\{.*?\}\{[^{}]*\}", "", s, flags=re.S)
    s = re.sub(r"\\srcpage(inl)?\{[^{}]*\}", "", s)
    s = re.sub(r"\\begin\{[^{}]*\}|\\end\{[^{}]*\}", "", s)
    s = re.sub(r"\\(emph|textbf|textit|underline|text|mathrm)\{([^{}]*)\}", r"\2", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"\s+", " ", s).strip()
    s = s.strip("：:，,。;； ")
    s = s.replace("|", "／")
    return s[:cap] + ("…" if len(s) > cap else "")


def main() -> int:
    toc = json.load(io.open(TOC, encoding="utf-8"))
    pages: dict[int, list[str]] = {}
    with io.open(TABLE, encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 5:
                pages.setdefault(int(parts[0]), []).append(parts[3])

    rows = []
    warn = 0
    for entry in toc:
        n = entry["n"]
        files = [fn for fn in sorted(os.listdir(SEC)) if fn.startswith("s%02d-" % n)]
        if not files:
            continue
        text = io.open(os.path.join(SEC, files[0]), encoding="utf-8").read()
        found = []
        for env in ENVS:
            for m in re.finditer(r"\\begin\{%s\}(.*?)\\end\{%s\}" % (env, env), text, re.S):
                found.append((m.start(), env, m.group(1)))
        found.sort()
        plist = pages.get(n, [])
        if len(found) != len(plist):
            print("WARN lecture %d: tex=%d table=%d" % (n, len(found), len(plist)))
            warn += 1
        for k, (_pos, env, body) in enumerate(found, 1):
            page = plist[k - 1] if k - 1 < len(plist) else "—"
            rows.append((n, "%d.%d" % (n, k), ZH[env], page, plain(body)))

    lines = ["# 资料卡 03 · 条款索引", "",
             "共 %d 条编号条目。编号由 LaTeX 自动生成（`讲次.序号`），页码为原文印刷页（= PDF 页）。" % len(rows),
             "", "| 讲 | 编号 | 类型 | 原文页 | 内容（首句节选） |", "| --- | --- | --- | --- | --- |"]
    for n, num, kind, page, body in rows:
        lines.append("| %d | %s | %s | %s | %s |" % (n, num, kind, page, body))
    io.open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("wrote", OUT, len(rows), "rows; warnings:", warn)
    return 0


if __name__ == "__main__":
    sys.exit(main())
