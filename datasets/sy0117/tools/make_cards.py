# -*- coding: utf-8 -*-
"""生成并校验 sy0117 资料卡：JSON、索引、核验台账、Markdown、taxonomy 与 MAP。

用法：
    python make_cards.py            # 校验并写文件
    python make_cards.py --check    # 只校验
"""
import io
import json
import os
import re
import sys

from cards_concepts import CONCEPTS
from cards_concepts2 import CONCEPTS_2
from cards_corrections import CORRECTIONS

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CARDS = CONCEPTS + CONCEPTS_2 + CORRECTIONS
ANN_TYPES = {"易错预警", "含糊点拨", "背景直觉"}
STATUSES = {"draft", "reviewed", "published"}
VERIF = {"external-confirmed", "source-only", "rejected"}
errors = []
warnings = []


def err(cid, msg):
    errors.append("[%s] %s" % (cid, msg))


def warn(cid, msg):
    warnings.append("[%s] %s" % (cid, msg))


def cjk_len(s):
    s = re.sub(r"\$[^$]*\$", "　", s)
    return sum(1 for ch in s if "\u4e00" <= ch <= "\u9fff")


def check_anchor(cid, anchor):
    m = re.match(r"^(.*?):(\d+)-(\d+)$", anchor)
    if not m:
        err(cid, "anchor 格式不对：%s" % anchor)
        return
    path, a, b = m.group(1), int(m.group(2)), int(m.group(3))
    full = os.path.join(REPO, path)
    if not os.path.exists(full):
        err(cid, "anchor 文件不存在：%s" % full)
        return
    n = sum(1 for _ in io.open(full, encoding="utf-8"))
    if not (1 <= a <= b <= n):
        err(cid, "anchor 行号越界：%s (%d-%d, file %d lines)" % (anchor, a, b, n))


def validate(cards):
    ids = [c["id"] for c in cards]
    if len(ids) != len(set(ids)):
        err("-", "id 重复")
    idset = set(ids)
    for c in cards:
        cid = c["id"]
        slug = cid.split("/")[-1]
        typ = c.get("type")
        if typ not in ("concept", "correction"):
            err(cid, "type 非法")
        if not cid.startswith("sy0117/%s/" % typ):
            err(cid, "id 前缀不对")
        base = ("id", "type", "track", "title", "summary", "question",
                "annotations", "related", "sources", "rights", "status", "verification")
        for f in base:
            if f not in c or c[f] in (None, "", []):
                err(cid, "缺字段 " + f)
        if typ == "concept":
            if not c["aliases"]:
                err(cid, "aliases 为空")
            for f in ("definition", "key_points", "formulas", "pitfalls"):
                if not c.get(f):
                    err(cid, "缺字段 " + f)
            if len(c["key_points"]) < 3:
                err(cid, "key_points < 3")
            if len(c["formulas"]) < 1:
                err(cid, "formulas 为空")
            if len(c["pitfalls"]) < 1:
                err(cid, "pitfalls 为空")
            if not c["definition"].get("text"):
                err(cid, "definition.text 为空")
        else:
            for f in ("location", "original", "corrected", "why", "note"):
                if not c.get(f):
                    err(cid, "缺字段 " + f)
        if not c["question"].endswith(("？", "?")):
            err(cid, "question 未以问号结尾")
        if cjk_len(c["summary"]) > 120:
            err(cid, "summary 汉字数 %d > 120" % cjk_len(c["summary"]))
        if len(c["related"]) < 2:
            err(cid, "related < 2")
        for r in c["related"]:
            if r not in idset:
                err(cid, "related 无法解析：%s" % r)
            if r == cid:
                err(cid, "related 指向自身")
        if not c["annotations"]:
            err(cid, "annotations 为空")
        for a in c["annotations"]:
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
            pages = s.get("pages") or []
            pdf = s.get("pdf_pages") or []
            if pages and pdf != [p + 12 for p in pages]:
                err(cid, "pages/pdf_pages 不对齐：%s" % pages)
            if not s.get("anchor"):
                err(cid, "anchor 缺失")
            else:
                check_anchor(cid, s["anchor"])
        if not re.match(r"^第\d+章$", c["track"]):
            err(cid, "track 应为“第N章”")


def dump(path, obj):
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def render_md(c):
    lines = ["# %s" % c["title"], ""]
    lines.append("- **id**：`%s`" % c["id"])
    lines.append("- **类型**：%s" % c["type"])
    lines.append("- **章**：%s" % c["track"])
    lines.append("- **问题**：%s" % c["question"])
    lines.append("")
    lines.append("> %s" % c["summary"])
    lines.append("")
    if c["type"] == "concept":
        lines += ["## 定义", "", c["definition"]["text"], ""]
        if c["definition"].get("notation"):
            lines += ["**记号**：" + c["definition"]["notation"], ""]
        lines += ["## 关键点", ""] + ["- " + x for x in c["key_points"]] + [""]
        lines += ["## 公式", ""] + ["```latex\n%s\n```" % x for x in c["formulas"]] + [""]
        if c.get("pitfalls"):
            lines += ["## 常见错误", ""] + ["- " + x for x in c["pitfalls"]] + [""]
    else:
        lines += ["## 位置", "", c["location"], ""]
        lines += ["## 原文片段", "", "```latex\n%s\n```" % c["original"], ""]
        lines += ["## 改为", "", "```latex\n%s\n```" % c["corrected"], ""]
        lines += ["## 依据", "", c["why"], ""]
        lines += ["## 说明", "", c["note"], ""]
    lines += ["## 批注", ""]
    for a in c["annotations"]:
        lines += ["### %s：%s" % (a["type"], a["title"]), "", a["text"], ""]
    lines += ["## 出处", ""]
    for s in c["sources"]:
        lines.append("- %s %s；锚点 `%s`" % (s["book"], s["section"], s["anchor"]))
        if s.get("page_note"):
            lines.append("- " + s["page_note"])
    lines += ["", "---", "", "权利：`rewritten`；核验：`%s`。" % c["verification"]["status"], ""]
    return "\n".join(lines)


def main(check):
    validate(CARDS)
    if errors:
        print("ERRORS %d" % len(errors))
        for e in errors:
            print("  " + e)
        for w in warnings:
            print("WARN " + w)
        return 1
    print("OK %d cards (%d concepts, %d corrections)" % (
        len(CARDS), len(CONCEPTS) + len(CONCEPTS_2), len(CORRECTIONS)))
    for w in warnings:
        print("WARN " + w)
    if check:
        return 0
    for sub in ("concepts", "corrections"):
        d = os.path.join(ROOT, "cards", sub)
        os.makedirs(d, exist_ok=True)
        for f in os.listdir(d):
            if f.endswith(".json"):
                os.remove(os.path.join(d, f))
    idx = []
    ver = []
    for c in CARDS:
        sub = "concepts" if c["type"] == "concept" else "corrections"
        dump(os.path.join(ROOT, "cards", sub, c["id"].split("/")[-1] + ".json"), c)
        with io.open(os.path.join(ROOT, "md", c["id"].split("/")[-1] + ".md"),
                     "w", encoding="utf-8", newline="\n") as f:
            f.write(render_md(c))
        src = c["sources"][0]
        idx.append({
            "id": c["id"], "type": c["type"], "track": c["track"],
            "title": c["title"], "summary": c["summary"],
            "section": src["section"], "anchor": src["anchor"],
        })
        ver.append({
            "id": c["id"], "status": c["verification"]["status"],
            "checked_on": c["verification"]["checked_on"],
            "checks": c["verification"]["checks"],
        })
    with io.open(os.path.join(ROOT, "index.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for x in idx:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    with io.open(os.path.join(ROOT, "verification.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for x in ver:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    tracks = {}
    for c in CARDS:
        tracks.setdefault(c["track"], []).append(c)
    lines = ["# sy0117 分类", "", "按章分组；每张卡至少一条批注。", ""]
    for t in sorted(tracks, key=lambda x: int(re.search(r"\d+", x).group())):
        lines += ["## %s" % t, ""]
        for c in tracks[t]:
            lines.append("- `%s` %s（%s）" % (c["id"], c["title"], c["type"]))
        lines.append("")
    with io.open(os.path.join(ROOT, "taxonomy.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    lines = ["# sy0117 卡片地图", "",
             "| 章 | 类型 | 标题 | 节 | 锚点 |", "|---|---|---|---|---|"]
    for c in CARDS:
        s = c["sources"][0]
        lines.append("| %s | %s | %s | %s | `%s` |" % (
            c["track"], c["type"], c["title"], s["section"], s["anchor"]))
    lines += ["", "共 %d 张：概念 %d、勘误 %d。" % (
        len(CARDS), len(CONCEPTS) + len(CONCEPTS_2), len(CORRECTIONS)), ""]
    with io.open(os.path.join(ROOT, "MAP.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
