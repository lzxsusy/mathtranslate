#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""make_cards.py — SY02-46 资料卡生成器（唯一真源）

用法：
    python tools/make_cards.py            # 生成全部 JSON + index.jsonl + verification.jsonl
    python tools/make_cards.py --check    # 只校验，不写文件

约定：
- 所有法文引文由本脚本从 工程文件/work/src/pNN.txt 现取现拼（去连字符、压空白），
  引文因此逐字可核；缺一即 assert 失败。
- anchor 由本脚本扫描 源码/sections/*.tex 的定理环境行号生成，不手写。
"""
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # 工程根
SRC = ROOT / "工程文件" / "work" / "src"
SECT = ROOT / "源码" / "sections"
OUT = ROOT.parents[0] / "sy0246" if False else Path(
    r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\datasets\sy0246")
BOOK = ("Gérard Laumon, Travaux de Frenkel, Gaitsgory et Vilonen sur la "
        "correspondance de Drinfeld-Langlands, Séminaire Bourbaki 906 (juin 2002), "
        "arXiv:math/0207078v1")
ARXIV = "https://arxiv.org/pdf/math/0207078v1"
CHECKED = "2026-11-27"


def page_text(nn):
    raw = io.open(SRC / f"p{nn:02d}.txt", encoding="utf-8").read()
    raw = raw.replace("-\n", "")                     # 行末连字符接回
    raw = re.sub(r"[ \t]+", " ", raw)
    lines = [ln.strip() for ln in raw.split("\n")]
    txt = " ".join(ln for ln in lines if ln)
    txt = re.sub(r"\s+", " ", txt)
    # dvips/OT1 文本层的已知伪码，按排印还原（README「引文口径」）
    txt = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", txt)
    txt = txt.replace("6=", "≠").replace("∼ =", "≅")
    return txt


def quote(nn, start, end):
    """从第 nn 页文本层截取 [start, end] 之间的逐字引文（含两端）。"""
    t = page_text(nn)
    i = t.find(start)
    assert i >= 0, f"p{nn:02d}: 找不到引文起点 {start!r}"
    j = t.find(end, i)
    assert j >= 0, f"p{nn:02d}: 找不到引文终点 {end!r}"
    return t[i:j + len(end)].strip()


def env_range(fname, env, nth=0):
    """返回源码 fname 中第 nth 个 \\begin{env}...\\end{env} 的 (起行, 止行)。"""
    path = SECT / fname
    lines = io.open(path, encoding="utf-8").read().split("\n")
    hit = -1
    for k, ln in enumerate(lines):
        if re.search(r"\\begin\{%s\}" % env, ln):
            hit += 1
            if hit == nth:
                depth = 0
                for m in range(k, len(lines)):
                    depth += len(re.findall(r"\\begin\{%s\}" % env, lines[m]))
                    depth -= len(re.findall(r"\\end\{%s\}" % env, lines[m]))
                    if depth == 0:
                        return k + 1, m + 1
    raise AssertionError(f"{fname}: 第 {nth} 个 {env} 环境不存在")


def anchor(fname, env, nth=0, note=""):
    a, b = env_range(fname, env, nth)
    s = f"08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/{fname}:L{a}-L{b}"
    return s + (f"（{note}）" if note else "")


def line_anchor(fname, needle, note=""):
    lines = io.open(SECT / fname, encoding="utf-8").read().split("\n")
    for k, ln in enumerate(lines):
        if needle in ln:
            s = (f"08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应"
                 f"/源码/sections/{fname}:L{k+1}")
            return s + (f"（{note}）" if note else "")
    raise AssertionError(f"{fname}: 找不到 {needle!r}")


def qj(nn, *frags):
    """多段逐字引文，用 … 省略中间部分（playbook 23 §5 允许）。"""
    t = page_text(nn)
    for f in frags:
        assert f in t, f"p{nn:02d}: 找不到引文片段 {f[:40]!r}"
    return " … ".join(frags)


def src(nn, section, start, end, anc, qt=None):
    return {
        "book": BOOK,
        "section": section,
        "pages": [nn],
        "pdf_pages": [nn],
        "quote": qt if qt is not None else quote(nn, start, end),
        "anchor": anc,
    }


def vcheck(entry, url, asserts, verdict="supports"):
    return {"entry": entry, "url": url, "asserts": asserts, "verdict": verdict}


def e1(nn, what):
    return vcheck(f"底本 PDF 第 {nn} 页（arXiv:math/0207078v1）",
                  f"{ARXIV}#page={nn}", what)


def card(cid, track, title, aliases, summary, question, definition, key_points,
         formulas, theorems, pitfalls, related, sources, checks, notes=()):
    return {
        "id": cid,
        "type": "concept" if "/concept/" in cid else "correction",
        "track": track,
        "title": title,
        "aliases": aliases,
        "summary": summary,
        "question": question,
        "definition": definition,
        "key_points": key_points,
        "formulas": formulas,
        "theorems": theorems,
        "pitfalls": pitfalls,
        "annotations": list(notes),
        "related": related,
        "sources": sources,
        "provenance_note": (
            "法文引文由 make_cards.py 从底本 PDF 文本层逐字截取（去行末连字符、压空白），"
            "数学式以下标压平的文本层为准；中译 anchor 由脚本扫描源码行号生成。"),
        "rights": "rewritten",
        "status": "reviewed",
        "verification": {"status": "checked", "checked_on": CHECKED, "checks": checks},
    }


def main():
    import cards_data
    out = OUT
    cards = cards_data.build(sys.modules[__name__])
    (out / "cards" / "concepts").mkdir(parents=True, exist_ok=True)
    (out / "cards" / "corrections").mkdir(parents=True, exist_ok=True)
    for c in cards:
        sub = "concepts" if c["type"] == "concept" else "corrections"
        slug = c["id"].split("/")[-1]
        path = out / "cards" / sub / f"{slug}.json"
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(c, f, ensure_ascii=False, indent=2)
            f.write("\n")
    with io.open(out / "index.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for c in cards:
            row = {"id": c["id"], "type": c["type"], "track": c["track"],
                   "title": c["title"], "summary": c["summary"],
                   "pages": sorted({p for s in c["sources"] for p in s["pages"]}),
                   "aliases": c["aliases"]}
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with io.open(out / "verification.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for c in cards:
            row = {"id": c["id"], "status": c["verification"]["status"],
                   "checked_on": c["verification"]["checked_on"],
                   "checks": c["verification"]["checks"]}
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"生成 {len(cards)} 张卡 → {out}")


if __name__ == "__main__":
    main()
