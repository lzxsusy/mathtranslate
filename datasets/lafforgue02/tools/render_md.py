#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_md.py —— 把 lafforgue02 资料卡 JSON 渲染成可读 Markdown（供人读、打印、导入 Anki）。

用法：python tools/render_md.py
输出：md/concepts/<slug>.md、md/derivations/<slug>.md、md/index.md
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
MD = ROOT / "md"
TRACK_NAMES = {
    "A": "A · 镜像对称与几何 Langlands",
    "B": "B · 拓扑镜像对称与 Hodge 数",
    "C": "C · 增强镜像对称与膜",
    "D": "D · 幂零锥上的等变重数",
    "E": "E · 仿射 Grassmannian 与重数代数",
    "O": "总览",
}
PROV = {"A": "原文明确写了", "B": "原文暗示、我们补的中间步", "C": "我们的判断"}


def load_all():
    cards = {}
    for kind in ("concepts", "derivations"):
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


def src_lines(c):
    out = []
    for s in c.get("sources", []):
        pages = s.get("pages", [])
        pr = f"p.{pages[0]}" if pages and pages[0] == pages[-1] else (f"p.{pages[0]}–{pages[-1]}" if pages else "")
        out.append(f"- {s.get('text', '?')} {pr}（{s.get('anchor', '')}）")
    return out


def render_concept(c, cards):
    L = [f"# {c['title']}\n",
         f"> `{c['id']}` · 轨道 {TRACK_NAMES.get(c['track'], c['track'])} · 状态 {c.get('status')}\n",
         "> **先自测**：" + c.get("question", "") + "\n",
         "## 一句话\n", c.get("summary", "") + "\n",
         "## 定义\n", c.get("definition", {}).get("text", "") + "\n"]
    if c.get("definition", {}).get("notation"):
        L += ["**记号**：" + c["definition"]["notation"] + "\n"]
    L += ["## 要点（为什么需要它）\n"]
    L += [f"{i}. {x}" for i, x in enumerate(c.get("key_points", []), 1)]
    L.append("")
    if c.get("formulas"):
        L += ["## 核心公式\n", "$$"]
        L += ["".join(c["formulas"])]
        L += ["$$\n"]
        for f in c["formulas"][1:]:
            L += ["$$", f, "$$\n"]
    if c.get("theorems"):
        L += ["## 定理与证明（或缺口）\n"]
        for t in c["theorems"]:
            L += [f"### {t.get('name', '命题')}\n", t.get("statement", "") + "\n"]
            pr = t.get("proof", {}) or {}
            st = pr.get("status")
            if st == "complete":
                for s in pr.get("steps", []):
                    L.append(f"{s.get('no')}. {s.get('text', '')}")
                    L.append(f"   - *为什么*：{s.get('why', '')}")
                L.append("")
            else:
                L += [f"> 证明状态：**{st}**。" + (pr.get("gap_note") or "") + "\n"]
            if t.get("source"):
                L.append(f"出处：`{t['source']}`\n")
    if c.get("pitfalls"):
        L += ["## 常见误解\n"]
        L += [f"- {x}" for x in c["pitfalls"]]
        L.append("")
    if c.get("related"):
        L += ["## 相关卡\n", " · ".join(link(cards, r) for r in c["related"]) + "\n"]
    L += ["## 出处（印刷页）\n"] + src_lines(c) + [""]
    if c.get("provenance_note"):
        L += ["> 说明：" + c["provenance_note"] + "\n"]
    return "\n".join(L)


def render_deriv(c, cards):
    L = [f"# {c['title']}\n",
         f"> `{c['id']}` · 轨道 {TRACK_NAMES.get(c['track'], c['track'])} · 状态 {c.get('status')} · {len(c.get('steps', []))} 步\n",
         "> **要回答的问题**：" + c.get("question", "") + "\n",
         "## 一句话\n", c.get("summary", "") + "\n",
         "## 目标\n", c.get("goal", "") + "\n",
         "## 前提\n"]
    L += [f"- {x}" for x in c.get("setup", [])]
    L += ["", "## 推导链\n", "| # | 步骤 | 为什么 | 出处 | 可信度 |", "|---|---|---|---|---|"]
    for s in c.get("steps", []):
        txt = s.get("text", "").replace("|", "\\|")
        why = s.get("why", "").replace("|", "\\|")
        L.append(f"| {s.get('no')} | {txt} | {why} | `{s.get('locator')}` | {s.get('provenance')}·{PROV.get(s.get('provenance'), '')} |")
    L += ["", "## 结论\n", c.get("result", "") + "\n"]
    if c.get("gaps"):
        L += ["## 缺口\n"] + [f"- {x}" for x in c["gaps"]] + [""]
    if c.get("pitfalls"):
        L += ["## 最容易讲错的地方\n"] + [f"- {x}" for x in c["pitfalls"]] + [""]
    if c.get("related"):
        L += ["## 相关卡\n", " · ".join(link(cards, r) for r in c["related"]) + "\n"]
    L += ["## 出处（印刷页）\n"] + src_lines(c) + [""]
    if c.get("provenance_note"):
        L += ["> 说明：" + c["provenance_note"] + "\n"]
    return "\n".join(L)


def main():
    cards = load_all()
    (MD / "concepts").mkdir(parents=True, exist_ok=True)
    (MD / "derivations").mkdir(parents=True, exist_ok=True)
    for cid, c in cards.items():
        if c["_kind"] == "concepts":
            text = render_concept(c, cards)
        else:
            text = render_deriv(c, cards)
        (MD / c["_kind"] / f"{c['_slug']}.md").write_text(text, encoding="utf-8", newline="\n")

    # index.md
    L = ["# Hausel ICM 2022（lafforgue02）资料卡索引\n",
         f"共 {len(cards)} 张：概念卡 {sum(1 for x in cards.values() if x['_kind']=='concepts')} 张、"
         f"推导卡 {sum(1 for x in cards.values() if x['_kind']=='derivations')} 张。\n"]
    for tr in ["A", "B", "C", "D", "E", "O"]:
        sub = [c for c in cards.values() if c["track"] == tr]
        if not sub:
            continue
        L += [f"\n## 轨道 {TRACK_NAMES.get(tr, tr)}\n"]
        for kind, label in (("concepts", "概念卡"), ("derivations", "推导卡")):
            got = sorted([c for c in sub if c["_kind"] == kind], key=lambda x: x["id"])
            if not got:
                continue
            L.append(f"\n**{label}**\n")
            for c in got:
                L.append(f"- [{c['title']}]({kind}/{c['_slug']}.md) —— {c['summary']}")
    (MD / "index.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"rendered {len(cards)} cards -> {MD}")


if __name__ == "__main__":
    main()
