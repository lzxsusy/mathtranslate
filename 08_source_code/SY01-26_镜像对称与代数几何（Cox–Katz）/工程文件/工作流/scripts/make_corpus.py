#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""导出「校订语料」：把 153 个单元的 issue 与最终是否采纳，导出成 JSONL。

用途：这是「看似正确的自然语料里被核实过的错误」的机器可读记录——对训练/评测
大模型识别译文缺陷有用（错误混在通顺文本里最难发现）。

字段：
  unit      单元号（u01..u153）
  file      译本源文件
  line      单元内行号（uXX.tex）
  page      PDF 物理页（印刷页 = page − 23）
  type      错译/漏译/增译/术语/记号/数学/病句/指代
  conf      high/medium/low
  quote     原文片段（逐字，来自译本）
  new       订正
  problem   问题说明
  applied   是否最终采纳
  reason    未采纳原因（low/术语统一/手工豁免/未命中）
"""
import io
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REV = os.path.join(BASE, "review")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "校订语料.jsonl")


def load_applied():
    p = os.path.join(BASE, "review_applied.json")
    if not os.path.exists(p):
        return set()
    data = json.load(io.open(p, encoding="utf-8"))
    return {(d.get("quote"), d.get("new")) for d in data}


def load_skip():
    p = os.path.join(BASE, "manual_skip.json")
    if not os.path.exists(p):
        return set()
    return {(d.get("quote"),) for d in json.load(io.open(p, encoding="utf-8"))}


def main():
    applied = load_applied()
    skipped = load_skip()
    rows = []
    for name in sorted(os.listdir(REV)):
        if not name.endswith(".json") or name.startswith("_"):
            continue
        path = os.path.join(REV, name)
        try:
            d = json.load(io.open(path, encoding="utf-8"))
        except Exception as e:
            print("skip", name, e, file=sys.stderr)
            continue
        unit = d.get("unit") or name[:-5]
        for it in d.get("issues", []):
            key = (it.get("quote"), it.get("new"))
            ok = key in applied
            reason = ""
            if not ok:
                if str(it.get("conf", "")).lower() == "low":
                    reason = "low"
                elif "单值化" in (it.get("quote") or ""):
                    reason = "术语统一（global_fix 处理）"
                elif (it.get("quote"),) in skipped:
                    reason = "手工豁免"
                else:
                    reason = "未命中/未采纳"
            rows.append({
                "unit": unit,
                "file": it.get("file"),
                "line": it.get("line"),
                "page": it.get("page"),
                "type": it.get("type"),
                "conf": it.get("conf"),
                "quote": it.get("quote"),
                "new": it.get("new"),
                "problem": it.get("problem"),
                "applied": ok,
                "reason": reason,
            })
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    n_ok = sum(1 for r in rows if r["applied"])
    print(f"wrote {len(rows)} rows ({n_ok} applied) -> {OUT}")


if __name__ == "__main__":
    main()
