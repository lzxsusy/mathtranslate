#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""cards/*.json → md/<slug>.md（人读版，供站内检索与 diff）。

用法（在 datasets/mloc 下）：
    python tools/render_md.py
"""
import glob
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "md")


def lst(v):
    if isinstance(v, str):
        return [v]
    return [x for x in (v or []) if isinstance(x, str)]


def render(c):
    L = []
    L.append("# %s" % c["title"])
    L.append("")
    L.append("> `%s` · type=%s · track=%s · status=%s · verification=%s"
             % (c["id"], c.get("type"), c.get("track"), c.get("status"),
                (c.get("verification") or {}).get("status")))
    L.append("")
    if c.get("aliases"):
        L.append("**别名**：" + "、".join(lst(c["aliases"])))
        L.append("")
    if c.get("summary"):
        L.append("## 摘要")
        L.append("")
        L.append(c["summary"])
        L.append("")
    if c.get("question"):
        L.append("## 问题")
        L.append("")
        L.append(c["question"])
        L.append("")
    d = c.get("definition") or {}
    if d:
        L.append("## 定义")
        L.append("")
        if d.get("text"):
            L.append(d["text"])
            L.append("")
        if d.get("notation"):
            L.append("记号：" + d["notation"])
            L.append("")
    if c.get("setup"):
        L.append("## 设定")
        L.append("")
        L.append(c["setup"])
        L.append("")
    if c.get("key_points"):
        L.append("## 要点")
        L.append("")
        for x in lst(c["key_points"]):
            L.append("- " + x)
        L.append("")
    if c.get("formulas"):
        L.append("## 公式")
        L.append("")
        for x in lst(c["formulas"]):
            L.append("$$" + x + "$$")
            L.append("")
    if c.get("theorems"):
        L.append("## 相关定理")
        L.append("")
        for t in c["theorems"]:
            L.append("### %s" % (t.get("name") or "定理"))
            L.append("")
            if t.get("statement"):
                L.append(t["statement"])
                L.append("")
            pr = t.get("proof") or {}
            st = pr.get("status")
            if st:
                L.append("证明状态：`%s`" % st)
                L.append("")
            for s in (pr.get("steps") or []):
                L.append("%s. %s" % (s.get("no"), s.get("text")))
                if s.get("why"):
                    L.append("   - 为什么：" + s["why"])
            if pr.get("gap_note"):
                L.append("")
                L.append("> 缺口：" + pr["gap_note"])
            L.append("")
    if c.get("computation"):
        L.append("## 计算")
        L.append("")
        L.append(c["computation"])
        L.append("")
    if c.get("result"):
        L.append("## 结果")
        L.append("")
        L.append(c["result"])
        L.append("")
    if c.get("pitfalls"):
        L.append("## 易错点")
        L.append("")
        for x in lst(c["pitfalls"]):
            L.append("- " + x)
        L.append("")
    if c.get("related"):
        L.append("## 相关卡")
        L.append("")
        for x in lst(c["related"]):
            L.append("- `%s`" % x)
        L.append("")
    if c.get("sources"):
        L.append("## 出处")
        L.append("")
        for s in c["sources"]:
            L.append("- %s · %s · p.%s（PDF %s） · `%s`"
                     % (s.get("book"), s.get("section"), s.get("pages"),
                        s.get("pdf_pages"), s.get("anchor")))
        L.append("")
    return "\n".join(L)


def main():
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for p in sorted(glob.glob(os.path.join(ROOT, "cards", "*", "*.json"))):
        c = json.load(io.open(p, encoding="utf-8"))
        slug = c["id"].split("/")[-1]
        sub = os.path.join(OUT, c["type"] + "s")
        os.makedirs(sub, exist_ok=True)
        with io.open(os.path.join(sub, slug + ".md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(render(c))
        n += 1
    print("md/: %d files" % n)


if __name__ == "__main__":
    main()
