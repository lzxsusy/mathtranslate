# -*- coding: utf-8 -*-
"""生成 gaits04 资料卡：JSON、索引、核验台账、Markdown 渲染、taxonomy 与 MAP。

用法：
    python make_cards.py            # 生成并报告
    python make_cards.py --check    # 只校验，不写文件
"""
import io
import json
import os
import re
import sys

from cards_1 import CARDS_1
from cards_2 import CARDS_2

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CARDS = CARDS_1 + CARDS_2

TRACKS = [
    ("O", "总览", "全章地图与阅读路线"),
    ("A", "阿代尔与球表示", "函数域、阿代尔环、Hecke 代数、Satake 参数"),
    ("B", "尖点与 Langlands 对应", "尖点性、多重度一、无分歧对应、Lafforgue 定理"),
    ("C", "向量丛与 Hecke", "双商与向量丛、Hecke 对应、算子、常项"),
    ("D", "层化与猜想", "模叠、Hecke 函子、本征层、几何 Langlands 猜想"),
    ("E", "附录：层-函数对应", "Grothendieck 层-函数对应与特征层"),
]
TRACK_NAMES = {t[0]: t[1] for t in TRACKS}
ANN_TYPES = {"易错预警", "含糊点拨", "背景直觉"}
STATUSES = {"draft", "reviewed", "published"}
VERIF = {"external-confirmed", "source-only", "rejected"}

errors = []
warnings = []


def err(cid, msg):
    errors.append("[%s] %s" % (cid, msg))


def warn(cid, msg):
    warnings.append("[%s] %s" % (cid, msg))


def strip_math(s):
    return re.sub(r"\$[^$]*\$", "　", s)


def validate(cards):
    ids = [c["id"] for c in cards]
    if len(ids) != len(set(ids)):
        err("-", "id 重复")
    idset = set(ids)
    for c in cards:
        cid = c["id"]
        slug = cid.split("/")[-1]
        if not cid.startswith("gaits04/concept/"):
            err(cid, "id 前缀不对")
        for f in ("id", "type", "track", "title", "aliases", "summary", "question",
                  "definition", "key_points", "formulas", "theorems", "pitfalls",
                  "annotations", "related", "sources", "rights", "status", "verification"):
            if f not in c or c[f] in (None, "", []):
                if f in ("theorems",):
                    continue
                err(cid, "缺字段 " + f)
        if c["track"] not in TRACK_NAMES:
            err(cid, "track 非法：%s" % c["track"])
        if not c["question"].endswith(("？", "?")):
            err(cid, "question 未以问号结尾")
        if len(c["aliases"]) < 1:
            err(cid, "aliases 为空")
        if len(c["key_points"]) < 3:
            err(cid, "key_points < 3")
        if len(c["formulas"]) < 1:
            err(cid, "formulas 为空")
        if len(c["pitfalls"]) < 1:
            err(cid, "pitfalls 为空")
        if len(c["related"]) < 2:
            err(cid, "related < 2")
        for r in c["related"]:
            if r not in idset:
                err(cid, "related 无法解析：%s" % r)
            if r == cid:
                err(cid, "related 指向自身")
        if not c.get("annotations"):
            err(cid, "annotations 为空（本数据集要求卡片携带批注）")
        for a in c.get("annotations", []):
            if a.get("type") not in ANN_TYPES:
                err(cid, "批注类型非法：%s" % a.get("type"))
            if not a.get("title") or not a.get("text"):
                err(cid, "批注缺 title/text")
        if c["rights"] != "rewritten":
            err(cid, "rights 必须是 rewritten")
        if c["status"] not in STATUSES:
            err(cid, "status 非法")
        v = c["verification"]
        if v.get("status") not in VERIF:
            err(cid, "verification.status 非法")
        if c["status"] == "published" and v.get("status") != "external-confirmed":
            err(cid, "source-only 不得标 published")
        if not c["sources"]:
            err(cid, "sources 为空")
        for s in c["sources"]:
            if s["pdf_pages"] != [p + 2 for p in s["pages"]]:
                err(cid, "pages/pdf_pages 不对齐：%s" % s["pages"])
            if not s.get("anchor") or "ch12_sec" not in s.get("anchor", ""):
                err(cid, "anchor 缺失或不合格式")
        n = len(strip_math(c["summary"]))
        if n > 120:
            warn(cid, "summary 汉字数 %d > 120" % n)

    # 每轨至少一张
    for t, _, _ in TRACKS:
        if not any(c["track"] == t for c in cards):
            warn("-", "轨道 %s 无卡片" % t)


def write_json(cards, check):
    out = os.path.join(ROOT, "cards", "concepts")
    if check:
        return
    if not os.path.isdir(out):
        os.makedirs(out)
    for c in cards:
        p = os.path.join(out, c["id"].split("/")[-1] + ".json")
        with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(c, fh, ensure_ascii=False, indent=2)
            fh.write("\n")


def write_index(cards, check):
    if check:
        return
    with io.open(os.path.join(ROOT, "index.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for c in cards:
            row = {
                "id": c["id"],
                "track": c["track"],
                "title": c["title"],
                "aliases": c["aliases"],
                "summary": c["summary"],
                "question": c["question"],
                "status": c["status"],
                "verification": c["verification"]["status"],
                "path": "cards/concepts/%s.json" % c["id"].split("/")[-1],
            }
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_verification(cards, check):
    if check:
        return
    with io.open(os.path.join(ROOT, "verification.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for c in cards:
            row = {
                "id": c["id"],
                "status": c["verification"]["status"],
                "checked_on": c["verification"]["checked_on"],
                "checks": c["verification"]["checks"],
                "basis": "译文与原书页逐条对照；未逐条做外部独立核验",
            }
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def md_card(c):
    L = []
    L.append("# %s" % c["title"])
    L.append("")
    L.append("> `%s` · 轨 %s %s · 状态 %s · 核验 %s" % (
        c["id"], c["track"], TRACK_NAMES[c["track"]], c["status"],
        c["verification"]["status"]))
    L.append("")
    L.append("**问题：** %s" % c["question"])
    L.append("")
    L.append("**一句话：** %s" % c["summary"])
    L.append("")
    if c["aliases"]:
        L.append("**别名：** " + "、".join("`%s`" % a for a in c["aliases"]))
        L.append("")
    L.append("## 定义")
    L.append("")
    L.append(c["definition"]["text"])
    L.append("")
    if c["definition"].get("notation"):
        L.append("**记号：** %s" % c["definition"]["notation"])
        L.append("")
    L.append("## 要点")
    L.append("")
    for k in c["key_points"]:
        L.append("- " + k)
    L.append("")
    L.append("## 公式")
    L.append("")
    for f in c["formulas"]:
        L.append("$$")
        L.append(f)
        L.append("$$")
        L.append("")
    if c["theorems"]:
        L.append("## 定理与证明")
        L.append("")
        for t in c["theorems"]:
            L.append("**%s**　%s" % (t["name"], t["statement"]))
            L.append("")
            p = t.get("proof", {})
            if p.get("steps"):
                for s in p["steps"]:
                    L.append("1. " + s)
                L.append("")
            if p.get("gap_note"):
                L.append("> 跳步说明：%s" % p["gap_note"])
                L.append("")
            if t.get("source"):
                L.append("*出处：%s*" % t["source"])
                L.append("")
    L.append("## 易错点")
    L.append("")
    for p in c["pitfalls"]:
        L.append("- " + p)
    L.append("")
    L.append("## 批注")
    L.append("")
    for a in c["annotations"]:
        L.append("**〔%s〕%s**　%s" % (a["type"], a["title"], a["text"]))
        L.append("")
    L.append("## 相关")
    L.append("")
    L.append("、".join("[[%s]]" % r.split("/")[-1] for r in c["related"]))
    L.append("")
    L.append("## 来源")
    L.append("")
    for s in c["sources"]:
        L.append("- %s，%s，原书 pp. %s（PDF pp. %s）" % (
            s["book"], s["section"],
            "–".join(str(p) for p in s["pages"]),
            "–".join(str(p) for p in s["pdf_pages"])))
        L.append("  - 锚点：`%s`" % s["anchor"])
    L.append("")
    return "\n".join(L)


def write_md(cards, check):
    out = os.path.join(ROOT, "md")
    if check:
        return
    if not os.path.isdir(out):
        os.makedirs(out)
    for c in cards:
        p = os.path.join(out, c["id"].split("/")[-1] + ".md")
        with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(md_card(c))


def write_taxonomy(cards, check):
    if check:
        return
    L = ["# gaits04 分类体系", "", "六轨共 %d 张概念卡。" % len(cards), ""]
    for t, name, desc in TRACKS:
        sel = [c for c in cards if c["track"] == t]
        L.append("## %s %s（%d 张）" % (t, name, len(sel)))
        L.append("")
        L.append(desc + "。")
        L.append("")
        for c in sel:
            L.append("- `%s`　%s" % (c["id"].split("/")[-1], c["title"]))
        L.append("")
    with io.open(os.path.join(ROOT, "taxonomy.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L))


def write_map(cards, check):
    if check:
        return
    L = ["# gaits04 卡片地图", "",
         "| 轨 | 卡片 | 原书页 | 一句话 |", "| --- | --- | --- | --- |"]
    for c in sorted(cards, key=lambda x: (x["track"], x["id"])):
        pages = sorted({p for s in c["sources"] for p in s["pages"]})
        pr = "%d–%d" % (min(pages), max(pages)) if len(pages) > 1 else str(pages[0])
        L.append("| %s | `%s` %s | %s | %s |" % (
            c["track"], c["id"].split("/")[-1], c["title"], pr,
            strip_math(c["summary"]).replace("　", "").strip()[:40]))
    L.append("")
    with io.open(os.path.join(ROOT, "MAP.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L))


def main():
    check = "--check" in sys.argv
    validate(CARDS)
    if errors:
        print("校验失败：%d 条" % len(errors))
        for e in errors:
            print("  " + e)
        return 1
    write_json(CARDS, check)
    write_index(CARDS, check)
    write_verification(CARDS, check)
    write_md(CARDS, check)
    write_taxonomy(CARDS, check)
    write_map(CARDS, check)
    print("卡片总数：%d%s" % (len(CARDS), "（仅校验，未写文件）" if check else ""))
    for t, name, _ in TRACKS:
        n = sum(1 for c in CARDS if c["track"] == t)
        print("  %s %s：%d" % (t, name, n))
    notes = sum(len(c["annotations"]) for c in CARDS)
    print("批注总数：%d（%d 张卡携带）" % (notes, sum(1 for c in CARDS if c["annotations"])))
    print("警告：%d 条" % len(warnings))
    for w in warnings:
        print("  " + w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
