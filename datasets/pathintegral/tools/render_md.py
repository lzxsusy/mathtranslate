#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_md.py —— 把资料卡 JSON 渲染成可读的 Markdown（供人读、打印、导入 Anki）。

用法：python tools/render_md.py
输出：
  md/concepts/<slug>.md
  md/examples/<slug>.md
  md/index.md
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
MD = ROOT / "md"
TRACK_NAMES = {"A": "A · 基础与时间切片", "B": "B · 高斯路径积分与谐振子", "C": "C · 渐近方法与半经典", "D": "D · 格林函数与 WKB", "E": "E · 微扰与代数结构", "O": "总览"}


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
    kind = c["_kind"]
    return f"[{c['title']}]({prefix}{kind}/{c['_slug']}.md)"


def src_line(s):
    pages = s.get("pages", [])
    pdf = s.get("pdf_pages", [])
    pr = f"p.{pages[0]}–{pages[1]}" if pages and pages[0] != pages[1] else (f"p.{pages[0]}" if pages else "")
    pd = f"PDF p.{pdf[0]}–{pdf[1]}" if pdf and pdf[0] != pdf[1] else (f"PDF p.{pdf[0]}" if pdf else "")
    return f"- {s.get('section', '')}，{pr}（{pd}），源码 `{s.get('anchor', '')}`"


def render_concept(c, cards):
    L = []
    L.append(f"# {c['title']}\n")
    L.append(f"> `{c['id']}` · 轨道 {TRACK_NAMES.get(c['track'], c['track'])} · 状态 {c.get('status', 'draft')}\n")
    L.append("> **先自测**：" + c.get("question", "") + "\n")
    L.append("## 一句话\n")
    L.append(c["summary"] + "\n")
    d = c.get("definition", {})
    L.append("## 定义\n")
    L.append(d.get("text", "") + "\n")
    if d.get("notation"):
        L.append("**记号约定**：" + d["notation"] + "\n")
    L.append("## 要点\n")
    for x in c.get("key_points", []):
        L.append(f"- {x}")
    L.append("")
    if c.get("formulas"):
        L.append("## 关键公式\n")
        for f in c["formulas"]:
            ff = f.strip()
            if ff.startswith("$$") and ff.endswith("$$"):
                ff = ff[2:-2].strip()
            elif ff.startswith("$") and ff.endswith("$"):
                ff = ff[1:-1].strip()
            L.append(f"$$\n{ff}\n$$\n")
    L.append("## 定理与证明\n")
    for th in c.get("theorems", []):
        L.append(f"### {th['name']}\n")
        L.append(th["statement"] + "\n")
        pr = th.get("proof", {})
        status = "完整证明" if pr.get("status") == "complete" else "证明提纲"
        L.append(f"**{status}**\n")
        for st in pr.get("steps", []):
            L.append(f"{st['no']}. {st['text']}")
            L.append(f"   - *为什么*：{st['why']}")
        if pr.get("gap_note"):
            L.append(f"\n> **缺口**：{pr['gap_note']}\n")
        L.append(f"\n来源：{th.get('source', '')}\n")
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
    L = []
    L.append(f"# {c['title']}\n")
    L.append(f"> `{c['id']}` · 轨道 {TRACK_NAMES.get(c['track'], c['track'])} · 状态 {c.get('status', 'draft')}\n")
    L.append("> **这张卡练什么**：" + c.get("question", "") + "\n")
    L.append("## 一句话\n")
    L.append(c["summary"] + "\n")
    L.append("## 设定\n")
    L.append(c["setup"] + "\n")
    L.append("## 计算\n")
    for st in c.get("computation", []):
        L.append(f"**第 {st['no']} 步**：{st['text']}\n")
        L.append(f"> 为什么：{st['why']}\n")
    L.append("## 结果\n")
    L.append(c["result"] + "\n")
    L.append("## 复核\n")
    L.append(c["check"] + "\n")
    L.append("## 易错点\n")
    for x in c.get("pitfalls", []):
        L.append(f"- {x}")
    L.append("")
    L.append("## 用到哪些概念\n")
    for r in c.get("concept_refs", []):
        L.append(f"- {link(cards, r)}")
    L.append("")
    L.append("## 相关卡\n")
    seen = set(c.get("concept_refs", []))
    for r in c.get("related", []):
        if r in seen:
            continue
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
    for cid, c in cards.items():
        if c["type"] == "concept":
            text = render_concept(c, cards)
            out = MD / "concepts" / f"{c['_slug']}.md"
        else:
            text = render_example(c, cards)
            out = MD / "examples" / f"{c['_slug']}.md"
        out.write_text(text, encoding="utf-8", newline="\n")

    # 索引页
    L = ["# 路径积分资料卡 · 索引\n", "共 %d 张卡。\n" % len(cards)]
    for track in ("O", "A", "B", "C", "D"):
        group = [c for c in cards.values() if c["track"] == track]
        if not group:
            continue
        L.append(f"## {TRACK_NAMES.get(track, track)}\n")
        for c in sorted(group, key=lambda x: (x["type"], x["id"])):
            badge = "概念" if c["type"] == "concept" else "例子"
            L.append(f"- [{badge}] {link(cards, c['id'], prefix='')} —— {c['summary']}")
        L.append("")
    (MD / "index.md").write_text("\n".join(L), encoding="utf-8", newline="\n")
    print(f"rendered {len(cards)} cards -> {MD}")


if __name__ == "__main__":
    main()
