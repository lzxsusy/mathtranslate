#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_md.py —— 把资料卡 JSON 渲染成可读 Markdown（供人读、打印、导入 Anki）。

用法：python tools/render_md.py
输出：md/concepts/<slug>.md、md/examples/<slug>.md
（md/INDEX.md 由 build_index.py 生成，本脚本不碰。）
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
MD = ROOT / "md"

TRACK_NAMES = {
    "A": "跨章基础",
    "1": "Hitchin 联络与 TQFT",
    "2": "Koszul 上同调",
    "3": "Reider 与 Thaddeus 再探",
    "4": "奇异模空间的相交配对",
    "5": "BD Grassmannian 与辛纽结同调",
    "6": "曲线上层的算术",
    "7": "α-稳定凝聚系",
    "8": "阿贝尔簇上的正则性",
    "9": "可约曲线上的向量丛",
}


def load_all():
    cards = {}
    for kind in ("concepts", "examples"):
        for p in sorted((CARDS / kind).glob("*.json")):
            c = json.loads(p.read_text(encoding="utf-8"))
            c["_kind"] = kind
            c["_slug"] = p.stem
            cards[c["id"]] = c
    return cards


def link(cards, cid, prefix="../"):
    c = cards.get(cid)
    if not c:
        return f"`{cid}`"
    return f"[{c['title']}]({prefix}{c['_kind']}/{c['_slug']}.md)"


def fmt_formula(f):
    ff = f.strip()
    if ff.startswith("$$") and ff.endswith("$$"):
        ff = ff[2:-2].strip()
    elif ff.startswith("$") and ff.endswith("$"):
        ff = ff[1:-1].strip()
    return ff


def src_line(s):
    return (f"- {s.get('section', '')}；中译 p.{s.get('pages_zh', '?')}"
            f"（英文 PDF p.{s.get('pages_en', '?')}），源码 `{s.get('anchor', '')}`")


def head(c):
    L = [f"# {c['title']}\n"]
    L.append(f"> `{c['id']}` · 轨道 {c['track']} · {TRACK_NAMES.get(c['track'], c['track'])} · 状态 {c.get('status', 'draft')}\n")
    return L


def render_concept(c, cards):
    L = head(c)
    L.append("> **先自测**：" + c.get("question", "") + "\n")
    L.append("## 一句话\n")
    L.append(c["summary"] + "\n")
    d = c.get("definition", {})
    L.append("## 定义\n")
    L.append(d.get("text", "") + "\n")
    if d.get("notation"):
        L.append("**记号约定**：" + d["notation"] + "\n")
    L.append("## 要点（为什么需要它）\n")
    for x in c.get("key_points", []):
        L.append(f"- {x}")
    L.append("")
    if c.get("formulas"):
        L.append("## 关键公式\n")
        for f in c["formulas"]:
            L.append(f"$$\n{fmt_formula(f)}\n$$\n")
    L.append("## 定理与证明（或缺口）\n")
    for th in c.get("theorems", []):
        L.append(f"### {th['name']}\n")
        L.append(th["statement"] + "\n")
        pr = th.get("proof", {})
        st = pr.get("status")
        if st == "complete":
            L.append("**证明状态：完整**\n")
            for i, s in enumerate(pr.get("steps", []), 1):
                L.append(f"{i}. {s['text']}")
                L.append(f"   - *为什么*：{s['why']}")
            L.append("")
        elif st == "sketch":
            L.append("**证明状态：提纲（有缺口）**\n")
            for i, s in enumerate(pr.get("steps", []), 1):
                L.append(f"{i}. {s['text']}")
                L.append(f"   - *为什么*：{s['why']}")
            if pr.get("gap_note"):
                L.append(f"\n> **缺口**：{pr['gap_note']}\n")
        else:
            L.append("**证明状态：只引出处，原书不重证**\n")
            if pr.get("gap_note"):
                L.append(f"\n> {pr['gap_note']}\n")
        L.append(f"\n出处：{th.get('source', '')}\n")
    L.append("## 易错点\n")
    for x in c.get("pitfalls", []):
        L.append(f"- {x}")
    L.append("")
    L.append("## 相关卡\n")
    for r in c.get("related", []):
        L.append(f"- {link(cards, r)}")
    L.append("")
    L.append("## 出处\n")
    for s in c.get("sources", []):
        L.append(src_line(s))
    L.append("")
    return "\n".join(L)


def render_example(c, cards):
    L = head(c)
    L.append("> **这张卡练什么**：" + c.get("question", "") + "\n")
    L.append("## 一句话\n")
    L.append(c["summary"] + "\n")
    d = c.get("definition", {})
    if d.get("text"):
        L.append("## 背景定义\n")
        L.append(d["text"] + "\n")
    L.append("## 设定\n")
    L.append(c.get("setup", "") + "\n")
    L.append("## 计算\n")
    L.append(c.get("computation", "") + "\n")
    if c.get("key_points"):
        L.append("## 要点\n")
        for x in c["key_points"]:
            L.append(f"- {x}")
        L.append("")
    if c.get("formulas"):
        L.append("## 关键公式\n")
        for f in c["formulas"]:
            L.append(f"$$\n{fmt_formula(f)}\n$$\n")
    if c.get("theorems"):
        L.append("## 相关定理\n")
        for th in c["theorems"]:
            L.append(f"- **{th['name']}**：{th['statement']}")
        L.append("")
    L.append("## 易错点\n")
    for x in c.get("pitfalls", []):
        L.append(f"- {x}")
    L.append("")
    if c.get("concept_refs"):
        L.append("## 用到哪些概念\n")
        for r in c["concept_refs"]:
            L.append(f"- {link(cards, r)}")
        L.append("")
    L.append("## 相关卡\n")
    for r in c.get("related", []):
        L.append(f"- {link(cards, r)}")
    L.append("")
    L.append("## 出处\n")
    for s in c.get("sources", []):
        L.append(src_line(s))
    L.append("")
    return "\n".join(L)


def main():
    cards = load_all()
    (MD / "concepts").mkdir(parents=True, exist_ok=True)
    (MD / "examples").mkdir(parents=True, exist_ok=True)
    n = 0
    for cid, c in cards.items():
        if c["type"] == "concept":
            text = render_concept(c, cards)
            out = MD / "concepts" / f"{c['_slug']}.md"
        else:
            text = render_example(c, cards)
            out = MD / "examples" / f"{c['_slug']}.md"
        out.write_text(text, encoding="utf-8", newline="\n")
        n += 1
    print(f"rendered {n} cards -> {MD}")


if __name__ == "__main__":
    main()
