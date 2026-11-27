#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""make_items.py — 从分节原文抽出全部编号条目，生成 工程文件/work/条目总表.tsv

列：节 | 编号 | 类型 | 印刷页 | 原文首句（截 90 字符） | 中文标题（待主控填）
页数由该条目在 src-sNN.txt 中之前最近的 `1252–NN` 行决定；节首页另按 sections.json 的 pages[0]-1 处理。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "工程文件" / "work"
SRC = WORK / "src"

TYPES = ["Assumption", "Problem", "Theorem", "Conjecture", "Definition",
         "Proposition", "Corollary", "Lemma", "Example", "Remark"]
PAT = re.compile(r"^(" + "|".join(TYPES) + r")\s+(\d+\.\d+)\s*(\([^)]*\))?\s*\.?\s*—?\s*(.*)$")


def main():
    metas = {s["sec"]: s for s in json.loads((WORK / "sections.json").read_text(encoding="utf-8"))}
    rows = []
    seen = set()
    for sec in range(1, 14):
        f = SRC / f"src-s{sec:02d}.txt"
        if not f.exists():
            continue
        meta = metas[sec]
        start = (meta["pages"][0] - 1) if meta.get("pages") else 0
        page = start
        for ln in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^1252–(\d+)\s*$", ln.strip())
            if m:
                page = int(m.group(1))
                continue
            mm = PAT.match(ln.strip())
            if mm:
                typ, num, paren, first = mm.groups()
                if num.split(".")[0] != str(sec):
                    continue                      # 行首交叉引用（如 “Conjecture 1.5 would be…”）
                if (typ, num) in seen:
                    continue                      # 同一编号重复出现（续引），只取首见
                seen.add((typ, num))
                first = (first or "").strip()
                if len(first) > 90:
                    first = first[:90].rstrip() + "…"
                title = paren.strip("() ") if paren else ""
                rows.append((sec, num, typ, page, first, title))
    out = WORK / "条目总表.tsv"
    with out.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write("节\t编号\t类型\t印刷页\t原文首句\t条目名（原文括号）\n")
        for r in rows:
            fh.write("\t".join(str(x) for x in r) + "\n")
    print(f"条目总表：{len(rows)} 条 → {out}")
    from collections import Counter
    print(Counter(r[2] for r in rows))
    for sec in range(1, 14):
        n = sum(1 for r in rows if r[0] == sec)
        if n:
            print(f"  s{sec:02d}: {n} 条，页 {[r[3] for r in rows if r[0] == sec]}")


if __name__ == "__main__":
    main()
