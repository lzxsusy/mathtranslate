#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""生成 taxonomy.md：按轨道分组的卡片总表。"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NAMES = {
    "O": "O · 总览：主陈述、两侧理论、证明地图",
    "A": "A · TQFT 语言与算术–拓扑字典（§1–§3）",
    "B": "B · 边界条件、raviolo、Hecke 与 Satake（§4、§7）",
    "C": "C · 球簇、对偶群、小 Weyl 群、超球（§8–§10）",
    "D": "D · Plancherel 与局部范畴化猜想（§8、§11）",
    "E": "E · 周期层、L-层、整体猜想、L-函数与例子（§5、§12–§15）",
}


def main():
    cards = []
    for kind in ("concepts", "derivations"):
        for p in glob.glob(os.path.join(ROOT, "cards", kind, "*.json")):
            with io.open(p, encoding="utf-8") as f:
                cards.append(json.load(f))
    lines = ["# lawrge24 · 卡片总表", "",
             "底本：LAWRGE 2024 NOTES, *Relative Langlands Duality*（2024-12-03，73 页）。"
             "页码为原文 PDF 页；`§N` 对应 `chNN.txt`。", ""]
    for t in "OABCDE":
        sub = sorted([c for c in cards if c["track"] == t], key=lambda c: c["id"])
        if not sub:
            continue
        lines.append("## " + NAMES[t])
        lines.append("")
        lines.append("| id | 标题 | 类型 | 摘要 |")
        lines.append("|---|---|---|---|")
        for c in sub:
            typ = "推导" if c["type"] == "derivation" else "概念"
            lines.append("| `%s` | %s | %s | %s |" %
                         (c["id"], c["title"].replace("|", "\\|"), typ,
                          c["summary"].replace("|", "\\|")))
        lines.append("")
    out = os.path.join(ROOT, "taxonomy.md")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print("taxonomy.md: %d cards" % len(cards))


if __name__ == "__main__":
    main()
