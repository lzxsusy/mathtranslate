# -*- coding: utf-8 -*-
"""生成 datasets/raskin_glc 的 JSON 卡、索引、核验记录与 md 渲染。

用法（在仓库根目录）：
    python 08_source_code/SY02-47_.../工程文件/tools/gen_cards.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
REPO = HERE.parents[4]
SET = "raskin_glc"
OUT = REPO / "datasets" / SET

sys.path.insert(0, str(HERE.parent))
import cards_a  # noqa: E402
import cards_b  # noqa: E402
import cards_c  # noqa: E402
import cards_d  # noqa: E402

PLURAL = {
    "concept": "concepts",
    "derivation": "derivations",
    "correction": "corrections",
    "remark": "remarks",
    "example": "examples",
    "statement": "statements",
    "conjecture": "conjectures",
}


def all_cards():
    cards = cards_a.CARDS + cards_b.CARDS + cards_c.CARDS + cards_d.CARDS
    ids = [c["id"] for c in cards]
    if len(ids) != len(set(ids)):
        raise SystemExit("重复 id")
    idset = set(ids)
    for c in cards:
        for r in c.get("related", []):
            if r not in idset:
                raise SystemExit(f"{c['id']} 的 related 不存在：{r}")
        if not c["id"].startswith(SET + "/"):
            raise SystemExit(f"id 前缀错误：{c['id']}")
        slug = c["id"].rsplit("/", 1)[1]
        if not slug.replace("-", "").isalnum() or slug.lower() != slug:
            raise SystemExit(f"slug 不是 kebab-case：{slug}")
    return cards


def pages_of(card):
    ps = set()
    for s in card.get("sources", []):
        for p in s.get("pages", []):
            ps.add(int(p))
    return sorted(ps)


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def provenance(card) -> str:
    src = card["sources"][0]
    pages = ", ".join(str(p) for p in src.get("pages", []))
    return (
        f"据原文 {src['section']}（pp. {pages}）逐段中文重述；逐字引文见 sources.quote，"
        f"译文锚点见 sources.anchor；未复制原文成段文字。"
    )


def md_of(card) -> str:
    lines = []
    lines.append(f"# {card['title']}\n")
    lines.append(f"- id：`{card['id']}`")
    lines.append(f"- 类型：{card['type']}　轨道：{card['track']}　状态：{card['status']}")
    lines.append(f"- 一句话：{card['summary']}\n")
    if card.get("question"):
        lines.append(f"**问题**：{card['question']}\n")
    if card["type"] == "concept":
        d = card["definition"]
        lines.append("## 定义\n")
        lines.append(d["text"] + "\n")
        lines.append(f"记号：{d['notation']}\n")
        lines.append("## 要点\n")
        for k in card.get("key_points", []):
            lines.append(f"- {k}")
        lines.append("")
        if card.get("formulas"):
            lines.append("## 公式\n")
            for f in card["formulas"]:
                lines.append(f"$$ {f} $$\n")
        if card.get("theorems"):
            lines.append("## 定理与证明状态\n")
            for t in card["theorems"]:
                p = t.get("proof", {})
                lines.append(f"### {t['name']}\n")
                lines.append(t["statement"] + "\n")
                lines.append(f"- 证明状态：`{p.get('status')}`")
                if p.get("gap_note"):
                    lines.append(f"- 说明：{p['gap_note']}")
                lines.append(f"- 出处：{t.get('source','')}\n")
        if card.get("pitfalls"):
            lines.append("## 易错点\n")
            for p in card["pitfalls"]:
                lines.append(f"- {p}")
            lines.append("")
    elif card["type"] == "derivation":
        lines.append("## 问题\n")
        lines.append(card["goal"] + "\n")
        lines.append("## 设置\n")
        lines.append(card["setup"] + "\n")
        lines.append("## 步骤\n")
        for s in card["steps"]:
            lines.append(f"{s['n']}. **{s['claim']}**\n")
            lines.append(f"   依据：{s['justification']}\n")
        lines.append("## 结论\n")
        lines.append(card["result"] + "\n")
        if card.get("gaps"):
            lines.append("## 缺口/原文问题\n")
            for g in card["gaps"]:
                lines.append(f"- {g}")
            lines.append("")
    elif card["type"] == "correction":
        lines.append("## 位置\n")
        lines.append(card["location"] + "\n")
        lines.append("## 原文\n")
        lines.append(f"> {card['original']}\n")
        lines.append("## 应为\n")
        lines.append(f"> {card['corrected']}\n")
        lines.append("## 理由\n")
        lines.append(card["why"] + "\n")
        lines.append("## 说明\n")
        lines.append(card["note"] + "\n")
    elif card["type"] == "remark":
        lines.append("## 陈述\n")
        lines.append(card["statement"] + "\n")
        lines.append("## 缘由\n")
        lines.append(card["why"] + "\n")
        lines.append("## 说明\n")
        lines.append(card["note"] + "\n")
    lines.append("## 出处\n")
    for s in card.get("sources", []):
        pages = ", ".join(str(p) for p in s.get("pages", []))
        lines.append(f"- {s['book']}，{s['section']}，pp. {pages}；`{s['anchor']}`")
        if s.get("quote"):
            lines.append(f"  > {s['quote']}")
    lines.append("")
    lines.append("## 相关卡\n")
    for r in card.get("related", []):
        lines.append(f"- `{r}`")
    lines.append("")
    v = card.get("verification", {})
    lines.append(f"## 核验（{v.get('status','')}，{v.get('checked_on','')}）\n")
    if v.get("checks"):
        for c in v["checks"]:
            lines.append(f"- {c['source']} / {c['entry']}：`{c['verdict']}` — {c['asserts']}")
    else:
        lines.append("- 无外部逐条核验；见上方说明。")
    if v.get("note"):
        lines.append(f"\n{v['note']}")
    lines.append("")
    return "\n".join(lines)


def main():
    cards = all_cards()
    OUT.mkdir(parents=True, exist_ok=True)
    index = []
    ver = []
    for c in cards:
        c.setdefault("provenance_note", provenance(c))
        plural = PLURAL[c["type"]]
        slug = c["id"].rsplit("/", 1)[1]
        rel = f"cards/{plural}/{slug}.json"
        write_json(OUT / rel, c)
        md_dir = OUT / "md"
        md_dir.mkdir(exist_ok=True)
        (md_dir / f"{slug}.md").write_text(md_of(c), encoding="utf-8")
        index.append({
            "id": c["id"],
            "type": c["type"],
            "track": c["track"],
            "title": c["title"],
            "summary": c["summary"],
            "pages": pages_of(c),
            "path": rel,
            "status": c["status"],
        })
        v = c.get("verification", {})
        ver.append({
            "id": c["id"],
            "status": v.get("status", ""),
            "alignment": "match",
            "checked_on": v.get("checked_on", ""),
            "checks": v.get("checks", []),
            "note": v.get("note", ""),
        })
    (OUT / "index.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in index) + "\n", encoding="utf-8"
    )
    (OUT / "verification.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in ver) + "\n", encoding="utf-8"
    )
    readme = [
        "# raskin_glc：Raskin 射影曲线几何 Langlands 讲义资料卡",
        "",
        "来源：Sam Raskin 讲授、Lin Chen 笔记《Notes for \"Geometric Langlands for Projective Curves\"》，",
        "2025-07-07/11，18 页；底本与译注本见 `08_source_code/SY02-47_Raskin射影曲线上的几何Langlands讲义/`。",
        "",
        f"共 {len(cards)} 张卡。每张卡含原文页码、逐字引文、译注锚点与核验记录；",
        "`verification.status = partial` 的卡含逐条外部核验；`source-only` 的卡只据原文与经典文献。",
        "",
        "## 卡片",
        "",
        "| id | 类型 | 标题 | 页码 |",
        "| --- | --- | --- | --- |",
    ]
    for x in index:
        readme.append(f"| `{x['id']}` | {x['type']} | {x['title']} | {', '.join(map(str, x['pages']))} |")
    readme += [
        "",
        "## 校验",
        "",
        "```bash",
        "python tools/card_spec_check.py --set raskin_glc --strict",
        "```",
        "",
        "`related` 只指向本集内已存在的 id；`rights` 统一为 `rewritten`（中文重述，不复制原文）。",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(readme), encoding="utf-8")
    print(f"wrote {len(cards)} cards to {OUT}")


if __name__ == "__main__":
    main()
