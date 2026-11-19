# -*- coding: utf-8 -*-
"""从 workflow/cards_plan.tsv 与 cards/ 生成 MAP.md（书骨架 + 卡的位置）。

用法：python tools/gen_map.py
"""
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(ROOT, "workflow", "cards_plan.tsv")
CARDS = os.path.join(ROOT, "cards")
OUT = os.path.join(ROOT, "MAP.md")

CHAPTERS = {
    "chapter1": ("1", "引言"),
    "chapter2": ("2", "Floer 上同调、Fukaya A∞-范畴与操作子原理"),
    "chapter3": ("3", "拼接 Floer 理论与拉格朗日对应函子"),
    "chapter4": ("4", "辛 (A∞,2)-范畴 Symp"),
    "chapter5": ("5", "应用"),
}
TRACKS = {"A": "第 1–2 章：辛流形、Floer、Fukaya、操作子",
          "B": "第 3 章：拼接 Floer 与函子",
          "C": "第 4 章：辛 $(A_\\infty,2)$-范畴",
          "D": "第 5 章：应用",
          "O": "术语总览"}


def load_plan():
    rows = []
    with io.open(PLAN, encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            cells = line.split("\t")
            row = dict(zip(head, cells))
            rows.append(row)
    return rows


def card_path(kind, slug):
    sub = {"concept": "concepts", "deriv": "derivations", "correction": "corrections"}[kind]
    return os.path.join(CARDS, sub, slug + ".json")


def read_json(path):
    if not os.path.exists(path):
        return None
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def sec_key(section):
    nums = re.findall(r"\d+", section)
    return [int(x) for x in nums] or [0]


def short_id(card_id):
    return card_id.rsplit("/", 1)[1]


def main():
    plan = load_plan()
    groups = {}
    for row in plan:
        groups.setdefault((row["chapter"], row["section"]), []).append(row)

    # corrections grouped by chapter too
    corr_by_chapter = {}
    corr_dir = os.path.join(CARDS, "corrections")
    for fn in sorted(os.listdir(corr_dir)):
        if not fn.endswith(".json"):
            continue
        c = read_json(os.path.join(corr_dir, fn))
        if not c:
            continue
        page = c.get("page", 0)
        ch = "chapter1"
        if page >= 53:
            ch = "chapter5"
        elif page >= 39:
            ch = "chapter4"
        elif page >= 19:
            ch = "chapter3"
        elif page >= 4:
            ch = "chapter2"
        corr_by_chapter.setdefault(ch, []).append(c)

    lines = []
    lines.append("# MAP ——《范畴辛几何中的函子性》资料卡在全书的分布\n")
    lines.append("底本：Abouzaid & Bottman, *Functoriality in categorical symplectic geometry*（arXiv:2210.11159v1，68 页）。")
    lines.append("锚点 `原书 p.N` 指英文原文的印刷页（PDF 页 = 印刷页）。")
    lines.append("卡分三种：**概念**（`concept`）、**推导**（`deriv`）、**勘误**（`correction`）；每张卡一个 JSON，渲染版在 `md/`。\n")

    lines.append("## 一、书骨架（按章）\n")
    lines.append("```mermaid")
    lines.append("flowchart TB")
    lines.append("  B[\"Abouzaid–Bottman（2022）：范畴辛几何中的函子性\"]")
    for ch, (num, title) in CHAPTERS.items():
        node = "C" + num
        clean = re.sub(r"[$\\{}]", "", title)
        lines.append("  %s[\"§%s %s\"]" % (node, num, clean))
        lines.append("  B --> %s" % node)
        for (chapter, section), rows in sorted(groups.items(), key=lambda kv: sec_key(kv[0][1])):
            if chapter != ch:
                continue
            sec_clean = section.replace("§", "")
            snode = "S%s_%s" % (num, sec_clean.replace(".", "_"))
            lines.append("  %s[\"%s · %d 张\"]" % (snode, section, len(rows)))
            lines.append("  %s --> %s" % (node, snode))
    lines.append("```\n")

    lines.append("## 二、卡的位置\n")
    for ch, (num, title) in CHAPTERS.items():
        lines.append("### §%s %s\n" % (num, title))
        for (chapter, section), rows in sorted(groups.items(), key=lambda kv: sec_key(kv[0][1])):
            if chapter != ch:
                continue
            lines.append("**%s**（原书 p.%s）" % (section, rows[0]["pages"].replace(" ", "–")))
            lines.append("")
            lines.append("| 卡 id | 类型 | 标题 | 原书页 |")
            lines.append("|---|---|---|---|")
            for row in rows:
                kind = row["type"]
                path = card_path(kind, row["slug"])
                has = "✅" if os.path.exists(path) else "—"
                lines.append("| `functoriality/%s/%s` %s | %s | %s | p.%s |" % (
                    kind, row["slug"], has, kind, row["title"], row["pages"].replace(" ", "–")))
            lines.append("")
        corrs = corr_by_chapter.get(ch, [])
        if corrs:
            lines.append("**本章勘误卡**")
            lines.append("")
            lines.append("| 卡 id | 页 | 一句话 |")
            lines.append("|---|---|---|")
            for c in sorted(corrs, key=lambda x: x["page"]):
                lines.append("| `%s` | p.%d | %s |" % (c["id"], c["page"], c["title"]))
            lines.append("")

    lines.append("## 三、轨道一览\n")
    lines.append("| 轨道 | 主题 |")
    lines.append("|---|---|")
    for k in ("A", "B", "C", "D", "O"):
        n = sum(1 for r in plan if r["track"] == k)
        lines.append("| %s（%d 张计划） | %s |" % (k, n, TRACKS[k]))
    lines.append("")

    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote", OUT, "lines", len(lines))


if __name__ == "__main__":
    main()
