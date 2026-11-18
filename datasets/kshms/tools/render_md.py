#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""render_md.py —— 由 cards/ 生成 md/（一卡一 md + md/README.md 总表）。

公式保留 MathJax 语法（$...$ / $$...$$），GitHub / Gitee / AtomGit 直接可读。
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, "md")
TRACKS = {
    "O": "纲领与阅读", "A": "CFT 与几何退化", "B": "$A_\\infty$ 形式框架",
    "C": "Fukaya 与退化", "D": "Morse 机器", "E": "刚性解析与凝聚层",
    "F": "同调镜像猜想", "G": "复情形附录",
}


def render(card):
    L = [f"# {card['title']}", ""]
    meta = [f"`{card['id']}`", f"track {card['track']}（{TRACKS.get(card['track'], '')}）"]
    if card.get("kind"):
        meta.append(f"原文 {card['kind']} {card['kind_no']}")
    elif card.get("kind_no"):
        meta.append(f"原文 注 {card['kind_no']}")
    L += [" · ".join(meta), ""]
    L += [f"**问题**　{card['question']}", "", f"**摘要**　{card['summary']}", ""]
    if card.get("aliases"):
        L += ["**别名**　" + "；".join(card["aliases"]), ""]
    if card.get("statement"):
        L += ["## 陈述", "", card["statement"], ""]
    if card.get("notation"):
        L += ["## 记号", "", card["notation"], ""]
    if card.get("why"):
        L += ["## 这条注在全文中的作用", "", card["why"], ""]
    if card.get("key_points"):
        L += ["## 要点", ""] + [f"- {k}" for k in card["key_points"]] + [""]
    if card.get("formulas"):
        L += ["## 公式", ""]
        for f in card["formulas"]:
            L += ["$$" + f + "$$", ""]
    pr = card.get("proof") or {}
    if pr.get("status") in ("complete", "sketch"):
        L += [f"## 证明（{pr['status']}）", ""]
        for s in pr.get("steps", []):
            L += [f"{s['no']}. {s['text']}", "", f"   *为什么*：{s['why']}", ""]
        if pr.get("gap_note"):
            L += [f"> 缺口：{pr['gap_note']}", ""]
    if card.get("pitfalls"):
        L += ["## 易错点", ""] + [f"- {p}" for p in card["pitfalls"]] + [""]
    if card.get("related"):
        L += ["## 相关卡", ""] + [f"- `{r}`" for r in card["related"]] + [""]
    if card.get("sources"):
        L += ["## 出处", ""]
        for s in card["sources"]:
            pages = ",".join(str(p) for p in s.get("pages", []))
            L += [f"- {s.get('book','')} {s.get('section','')}（原文 p.{pages}）；锚点 `{s.get('anchor','')}`"]
        L += [""]
    if card.get("provenance_note"):
        L += [f"> {card['provenance_note']}", ""]
    return "\n".join(L)


def main():
    os.makedirs(MD, exist_ok=True)
    cards = []
    for dirpath, _, names in os.walk(os.path.join(ROOT, "cards")):
        for nm in sorted(names):
            if nm.endswith(".json"):
                cards.append(json.load(open(os.path.join(dirpath, nm), encoding="utf-8")))
    order = {"concept": 0, "remark": 1, "correction": 2}
    cards.sort(key=lambda c: (order.get(c.get("type"), 9), c.get("track", ""), c.get("kind_no", 0)))

    for c in cards:
        slug = c["id"].split("/")[-1]
        with open(os.path.join(MD, slug + ".md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(render(c))

    lines = ["# kshms 资料卡 · 总目录", "",
             "一卡一文件，按轨道（track）分组；点标题进单卡。", ""]
    for t, name in TRACKS.items():
        group = [c for c in cards if c.get("track") == t]
        if not group:
            continue
        lines += [f"## track {t} · {name}", "", "| 原文 | 标题 | 一句话 |", "| --- | --- | --- |"]
        for c in group:
            label = (f"{c['kind']} {c['kind_no']}" if c.get("kind") else f"注 {c['kind_no']}")
            lines.append(f"| {label} | [{c['title']}]({c['id'].split('/')[-1]}.md) | {c['summary']} |")
        lines.append("")
    with open(os.path.join(MD, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print(f"md/: {len(cards)} 张卡 + README.md")


if __name__ == "__main__":
    main()
