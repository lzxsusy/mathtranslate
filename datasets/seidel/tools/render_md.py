#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_md.py —— 把 cards/ 渲染成 md/。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
MD = ROOT / "md"


def esc(s):
    return str(s)


def render_concept(c):
    out = [f"# {c['title']}", "",
           f"> `{c['id']}` ｜ track {c['track']} ｜ {c['status']}", "",
           f"**一句话**：{c['summary']}", "",
           f"**自测**：{c['question']}", "",
           "## 定义", "", c["definition"]["text"], ""]
    if c["definition"].get("notation"):
        out += [f"记号：{c['definition']['notation']}", ""]
    out += ["## 要点", ""] + [f"- {x}" for x in c["key_points"]] + [""]
    if c.get("formulas"):
        out += ["## 公式", ""] + [x for x in c["formulas"]] + [""]
    out += ["## 定理与证明", ""]
    for t in c.get("theorems", []):
        out += [f"### {t['name']}", "", t["statement"], "",
                f"（{t['proof'].get('status')}；来源：{t['source']}）", ""]
        for st in t["proof"].get("steps") or []:
            out += [f"{st['no']}. {st['text']}  ",
                    f"   为什么：{st['why']}"]
        if t["proof"].get("gap_note"):
            out += ["", f"缺口：{t['proof']['gap_note']}"]
        out += [""]
    out += ["## 易错点", ""] + [f"- {x}" for x in c["pitfalls"]] + [""]
    out += refs(c)
    return "\n".join(out)


def render_deriv(c):
    out = [f"# {c['title']}", "",
           f"> `{c['id']}` ｜ track {c['track']} ｜ {c['status']}", "",
           f"**目标**：{c['goal']}", "",
           f"**自测**：{c['question']}", "",
           "## 前提", ""] + [f"- {x}" for x in c["setup"]] + ["", "## 步骤", ""]
    for st in c["steps"]:
        out += [f"{st['no']}. **{st['text']}**  ",
                f"   为什么：{st['why']}  ",
                f"   锚点：{st['locator']}（证据 {st['provenance']}）", ""]
    out += ["## 结果", "", c["result"], "", "## 缺口", ""] + [f"- {x}" for x in c["gaps"]] + [""]
    out += ["## 易错点", ""] + [f"- {x}" for x in c["pitfalls"]] + [""]
    out += refs(c)
    return "\n".join(out)


def render_correction(c):
    out = [f"# {c['title']}", "",
           f"> `{c['id']}` ｜ 原书 p.{c['page']} ｜ {c['status']}", "",
           f"**一句话**：{c['summary']}", "",
           f"**自测**：{c['question']}", "",
           "## 初版", "", f"```\n{c['original']}\n```", "",
           "## 改后", "", f"```\n{c['corrected']}\n```", "",
           "## 为什么改", "", c["why"], ""]
    if c.get("note"):
        out += ["## 补注", "", c["note"], ""]
    if c.get("pitfalls"):
        out += ["## 易错点", ""] + [f"- {x}" for x in c["pitfalls"]] + [""]
    out += refs(c)
    return "\n".join(out)


def refs(c):
    out = ["## 参考与关联", ""]
    for s in c.get("sources", []):
        out.append(f"- {s['book']}，{s.get('section','')}，p.{s['pages'][0]}–{s['pages'][1]}（{s['anchor']}）")
    out += ["", "关联：" + "、".join(f"`{r}`" for r in c.get("related", [])), "",
            f"来源说明：{c.get('provenance_note','')}", ""]
    return out


SUBDIR = {"concept": "concepts", "derivation": "derivations", "correction": "corrections"}


def main():
    MD.mkdir(exist_ok=True)
    for d in SUBDIR.values():
        (MD / d).mkdir(exist_ok=True)
    rows = []
    for p in sorted(CARDS.glob("**/*.json")):
        c = json.loads(p.read_text(encoding="utf-8"))
        if c["type"] == "concept":
            body = render_concept(c)
        elif c["type"] == "derivation":
            body = render_deriv(c)
        else:
            body = render_correction(c)
        sub = SUBDIR[c["type"]]
        (MD / sub / f"{p.stem}.md").write_text(body, encoding="utf-8", newline="\n")
        rows.append(c)
    rows.sort(key=lambda c: ({"concept": 0, "derivation": 1, "correction": 2}[c["type"]], c["track"], c["id"]))
    idx = ["# Seidel 资料卡索引", "",
           f"共 {len(rows)} 张：概念 {sum(1 for c in rows if c['type']=='concept')}　"
           f"推导 {sum(1 for c in rows if c['type']=='derivation')}　"
           f"勘误 {sum(1 for c in rows if c['type']=='correction')}", "",
           "| id | 标题 | track | 一句话 |", "|---|---|---|---|"]
    for c in rows:
        idx.append(f"| [`{c['id']}`]({SUBDIR[c['type']]}/{c['id'].split('/')[-1]}.md) | {c['title']} | {c['track']} | {c['summary']} |")
    (MD / "index.md").write_text("\n".join(idx) + "\n", encoding="utf-8", newline="\n")
    print(f"md/：{len(rows)} 张卡 + index.md")


if __name__ == "__main__":
    main()
