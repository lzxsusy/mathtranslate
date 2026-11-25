#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate taxonomy.md and MAP.md from cards/concepts/*.json."""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

TRACKS = {
    "O": "总览：主定理与证明地图",
    "A": "谱定理、Fourier 与 Mellin（Abel 玩具模型）",
    "B": "Bun_G、Hecke 与几何 Satake",
    "C": "谱侧、Hitchin 与谱作用",
    "D": "因子化、相对 Langlands 与证明架构",
    "E": "分歧、局部/函数域与物理",
}


def load():
    cards = []
    for p in sorted(glob.glob(os.path.join(ROOT, "cards", "concepts", "*.json"))):
        with io.open(p, encoding="utf-8") as f:
            cards.append(json.load(f))
    return cards


def main():
    cards = load()
    by_track = {k: [c for c in cards if c["track"] == k] for k in TRACKS}

    lines = ["# benzvi_glc 卡片总表（taxonomy）", ""]
    lines.append("底本：David Ben-Zvi, *What is the Geometric Langlands Correspondence about?* "
                 "(arXiv:2605.23167v1, 2026-05-22, 34 pp., CC BY 4.0)。")
    lines.append("")
    lines.append("共 **%d** 张概念卡；全部 `reviewed` + `source-only`，"
                 "尚未做 nLab / Stacks Project 的外部逐条核验。" % len(cards))
    lines.append("")
    lines.append("## 轨道分布")
    lines.append("")
    lines.append("| 轨道 | 名称 | 数量 |")
    lines.append("| --- | --- | ---: |")
    for k in TRACKS:
        lines.append("| %s | %s | %d |" % (k, TRACKS[k], len(by_track[k])))
    lines.append("")
    for k in TRACKS:
        lines.append("## %s · %s" % (k, TRACKS[k]))
        lines.append("")
        lines.append("| id | 标题 | 摘要 |")
        lines.append("| --- | --- | --- |")
        for c in by_track[k]:
            lines.append("| `%s` | %s | %s |" % (
                c["id"], c["title"].replace("|", r"\|"), c["summary"].replace("|", r"\|")))
        lines.append("")

    with io.open(os.path.join(ROOT, "taxonomy.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    slugs = {c["id"].split("/")[-1]: c for c in cards}
    nid = {s: s.replace("-", "_") for s in slugs}
    m = ["# benzvi_glc 卡片依赖图（MAP）", "",
         "节点为卡 id 的 slug；边 `A --- B` 表示 A 的 `related` 指向 B。", "",
         "```mermaid", "flowchart LR"]
    for c in cards:
        s = c["id"].split("/")[-1]
        label = c["title"].replace('"', "'").replace("[", "(").replace("]", ")")
        m.append('  %s["%s"]' % (nid[s], label))
    seen = set()
    for c in cards:
        a = c["id"].split("/")[-1]
        for r in c.get("related", []):
            b = r.split("/")[-1]
            if b not in slugs:
                continue
            key = tuple(sorted((a, b)))
            if key in seen:
                continue
            seen.add(key)
            m.append("  %s --- %s" % (nid[a], nid[b]))
    m.append("```")
    with io.open(os.path.join(ROOT, "MAP.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(m) + "\n")

    print("taxonomy.md / MAP.md: %d cards" % len(cards))


if __name__ == "__main__":
    main()
