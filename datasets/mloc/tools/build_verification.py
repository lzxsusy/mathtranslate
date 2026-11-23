#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""cards/*.json → verification.jsonl（一行一卡：核验状态 + 原文对齐结果）。

用法（在 datasets/mloc 下）：
    python tools/build_verification.py [源码 chapters 目录]

原文对齐闸：卡片 sources[].anchor 形如 `源码/chapters/ch02a.tex:88-96（引理 1.2）`，
脚本回查该 tex 的行号是否存在、区间是否合法，据此给出 alignment：
    match    全部 anchor 都能在源码里落到合法行区间
    broken   至少一个 anchor 落空（区间越界或文件不存在）
没有任何 anchor 的卡记 `no-anchor`，由人复核。

另做一条本库特有的检查：`pdf_pages - pages == 4`（底本 PDF 页 = 印刷页 + 4）。
"""
import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_SRC = os.path.join(
    ROOT, "..", "..", "08_source_code",
    "SY07-11_局部化与约化李群的表示论（Miličić）", "源码", "chapters")
SRC = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC

# `源码/chapters/ch02a.tex:88-96（…）` 或裸写 `ch02a.tex:88-96`
ANCHOR = re.compile(r'(ch[0-9]{2}[a-z]?\.tex):(\d+)(?:\s*[-–]\s*(\d+))?')


def tex_lines(name):
    p = os.path.join(SRC, name)
    if not os.path.exists(p):
        return None
    return len(io.open(p, encoding="utf-8").read().splitlines())


def page_gap_bad(d):
    bad = []
    for s in d.get("sources", []):
        pg, pp = s.get("pages"), s.get("pdf_pages")
        if not isinstance(pg, list):
            pg = [pg]
        if not isinstance(pp, list):
            pp = [pp]
        if len(pg) != len(pp):
            bad.append("pages/pdf_pages 长度不一致：%s vs %s" % (pg, pp))
            continue
        for a, b in zip(pg, pp):
            if a is None or b is None:
                bad.append("pages 或 pdf_pages 为空")
            elif b - a != 4:
                bad.append("pdf_pages(%s) - pages(%s) != 4" % (b, a))
    return bad


def main():
    cache = {}
    rows, n_match, n_broken, n_na, n_gap = [], 0, 0, 0, 0
    for p in sorted(glob.glob(os.path.join(ROOT, "cards", "*", "*.json"))):
        d = json.load(io.open(p, encoding="utf-8"))
        v = d.get("verification", {})
        verdicts, bad = [], []
        for s in d.get("sources", []):
            a = s.get("anchor", "")
            m = ANCHOR.search(a)
            if not m:
                continue
            name, start, end = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
            if name not in cache:
                cache[name] = tex_lines(name)
            n = cache[name]
            if n is None:
                bad.append("%s（文件缺失）" % a)
            elif not (1 <= start <= end <= n):
                bad.append("%s（越界，该文件共 %d 行）" % (a, n))
            else:
                verdicts.append(a)
        gaps = page_gap_bad(d)
        if gaps:
            n_gap += 1
        if not verdicts and not bad:
            align = "no-anchor"
            n_na += 1
        elif bad:
            align = "broken"
            n_broken += 1
        else:
            align = "match"
            n_match += 1
        rows.append({
            "id": d["id"],
            "status": v.get("status", "source-only"),
            "alignment": align,
            "checked_on": v.get("checked_on", ""),
            "checks": v.get("checks", []),
            "anchors": verdicts,
            "broken_anchors": bad,
            "page_gaps": gaps,
            "note": (v.get("note") or ""),
        })
    out = os.path.join(ROOT, "verification.jsonl")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    ext = sum(1 for r in rows if r["status"] == "external-confirmed")
    print("verification.jsonl: %d cards | external-confirmed %d | source-only %d | rejected %d"
          % (len(rows), ext, sum(1 for r in rows if r["status"] == "source-only"),
             sum(1 for r in rows if r["status"] == "rejected")))
    print("alignment: match %d | broken %d | no-anchor %d" % (n_match, n_broken, n_na))
    print("page gap(≠4) cards: %d" % n_gap)
    for r in rows:
        if r["broken_anchors"]:
            print("BROKEN", r["id"], r["broken_anchors"])
        if r["page_gaps"]:
            print("PAGE", r["id"], r["page_gaps"])


if __name__ == "__main__":
    main()
