#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 cards/*.json 生成读者版 taxonomy.md。

用法：python tools/build_taxonomy.py [--out taxonomy.md]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TRACKS = [
    ("O", "总览", "先看这一张，再决定读哪条轨道。"),
    ("A", "基础与时间切片", "费曼核、位置/动量表示、时间切片、路径积分定义、虚时间。"),
    ("B", "高斯路径积分与谐振子", "唯一能精确求和的两类模型；后面所有近似都要在它们身上退化。"),
    ("C", "渐近方法与半经典", "拉普拉斯、最速下降、莫尔斯流、斯托克斯、半经典核、雅可比场。"),
    ("D", "格林函数、WKB 与隧穿", "传播子的傅里叶变换，以及它在允许区/禁区的两种面孔。"),
    ("E", "微扰与代数结构", "威克定理、费曼图、Moyal 乘积、S¹ 关联、Hochschild 与量子 HKR。"),
]


def pages(card):
    s = card.get("sources") or [{}]
    p = s[0].get("pages") or [0, 0]
    return f"{p[0]}–{p[1]}" if p[0] != p[1] else str(p[0])


def anchor(card):
    return (card.get("sources") or [{}])[0].get("anchor", "")


def anchor_line(card):
    a = anchor(card)
    if ":" not in a:
        return 0
    try:
        return int(a.split(":")[1].split("-")[0])
    except ValueError:
        return 0


def slug(card):
    return card["id"].split("/")[-1]


def md_link(card):
    kind = "concepts" if card["type"] == "concept" else "examples"
    return f"[`{slug(card)}`](md/{kind}/{slug(card)}.md)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "taxonomy.md"))
    args = ap.parse_args()

    cards = []
    for p in sorted((ROOT / "cards").glob("*/*.json")):
        cards.append(json.loads(p.read_text(encoding="utf-8")))
    order = {"O": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
    cards.sort(key=lambda c: (order.get(c["track"], 9), anchor_line(c), c["id"]))

    concepts = [c for c in cards if c["type"] == "concept"]
    examples = [c for c in cards if c["type"] == "example"]

    L = []
    L.append("# 路径积分资料卡 · 总表\n")
    L.append("书名：李思《量子力学与几何》（中文译注本）第 2 章「路径积分形式」。\n")
    L.append(
        f"共 **{len(cards)} 张**：1 张总览 + {len([c for c in concepts if c['track'] != 'O'])} 张概念卡 + "
        f"{len(examples)} 张例子卡。页码为原书印刷页（80–160）；PDF 页 = 印刷页 + 1。\n"
    )
    L.append("## 阅读顺序\n")
    L.append("```text")
    L.append("O 总览 → A 定义与时间切片 → B 高斯/谐振子（精确答案）")
    L.append("        → C 驻定相位与半经典（近似机器）")
    L.append("        → D 格林函数/WKB/隧穿（物理输出）")
    L.append("        → E 威克/费曼图/Moyal/HKR（代数输出）")
    L.append("```\n")

    for track, name, blurb in TRACKS:
        sub = [c for c in concepts if c["track"] == track]
        if not sub:
            continue
        L.append(f"## {track} · {name}（{len(sub)} 张）\n")
        L.append(blurb + "\n")
        L.append("| 卡片 | 标题 | 印刷页 | 源码 |")
        L.append("|---|---|---|---|")
        for c in sub:
            L.append(f"| {md_link(c)} | {c['title']} | {pages(c)} | `{anchor(c)}` |")
        L.append("")

    L.append(f"## 例子卡（{len(examples)} 张）\n")
    L.append("每个编号例子一张卡；`对应概念` 指回它训练的那张概念卡。\n")
    L.append("| 卡片 | 标题 | 对应概念 | 印刷页 | 源码 |")
    L.append("|---|---|---|---|---|")
    for c in sorted(examples, key=lambda x: (anchor_line(x), x["id"])):
        refs = "、".join(f"`{r.split('/')[-1]}`" for r in c.get("concept_refs", []))
        L.append(f"| {md_link(c)} | {c['title']} | {refs} | {pages(c)} | `{anchor(c)}` |")
    L.append("")

    L.append("## 页码与出处\n")
    L.append("- `pages` 为原书印刷页；`pdf_pages = pages + 1`。")
    L.append("- `anchor` 指底本 `ch02a.tex`（§2.1–§2.5）、`ch02b.tex`（§2.6–§2.7）、`ch02c.tex`（§2.8）的行段；底本不随本目录发布。")
    L.append("- 每张卡的 `sources` 还带小节名，便于回书核对。")
    L.append("")

    Path(args.out).write_text("\n".join(L), encoding="utf-8")
    print(f"wrote {args.out}: {len(cards)} cards")


if __name__ == "__main__":
    main()
