#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""lint_cards.py —— kshms 资料卡质检（字段、编号、anchor、related 解析）。

用法（在 datasets/kshms/ 下）：
    python tools/lint_cards.py cards
    python tools/lint_cards.py cards --strict     # 有 error 时退出码 1
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRCROOT = os.path.dirname(os.path.dirname(ROOT))          # 仓库根
ID_RE = re.compile(r"^kshms/(concept|remark|correction)/([a-z0-9]+(?:-[a-z0-9]+)*)$")
ANCHOR_RE = re.compile(r"^(?:[^:]+):(\d+)-(\d+)")
KINDS = {"定义", "定理", "命题", "引理", "推论", "猜想"}
TRACKS = set("OABCDEFG")

errors = []
warnings = []


def han_count(s):
    s = re.sub(r"\$[^$]*\$", "", s)
    return len(re.findall(r"[\u4e00-\u9fff]", s))


def need(card, key, kind="error"):
    if key not in card or card[key] in ("", [], None):
        (errors if kind == "error" else warnings).append(f"{card.get('id','?')}: 缺 {key}")


def check_anchor(card, anchor):
    m = ANCHOR_RE.match(anchor)
    if not m:
        errors.append(f"{card['id']}: anchor 格式应为「路径:起始行-结束行（…）」：{anchor}")
        return
    path = anchor.split(":")[0]
    full = os.path.join(SRCROOT, "08_source_code",
                        "SY01-25_同调镜像对称与环面纤维化", path)
    if not os.path.exists(full):
        errors.append(f"{card['id']}: anchor 文件不存在 {path}")
        return
    n = sum(1 for _ in open(full, encoding="utf-8", errors="ignore"))
    a, b = int(m.group(1)), int(m.group(2))
    if not (1 <= a <= b <= n):
        errors.append(f"{card['id']}: anchor 行区间越界 {a}-{b}（文件共 {n} 行）")


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "cards"
    strict = "--strict" in sys.argv
    base = os.path.join(ROOT, target)
    files = []
    for dirpath, _, names in os.walk(base):
        for nm in sorted(names):
            if nm.endswith(".json"):
                files.append(os.path.join(dirpath, nm))

    ids = {}
    cards = []
    for f in files:
        try:
            card = json.load(open(f, encoding="utf-8"))
        except Exception as e:                                    # noqa: BLE001
            errors.append(f"{f}: JSON 解析失败 {e}")
            continue
        cards.append(card)
        cid = card.get("id", "")
        if not ID_RE.match(cid):
            errors.append(f"{f}: id 不合规 {cid}")
        if cid in ids:
            errors.append(f"{cid}: id 重复（{f} 与 {ids[cid]}）")
        ids[cid] = f
        if os.path.basename(f)[:-5] != cid.split("/")[-1]:
            errors.append(f"{f}: 文件名应等于 id 最后一段 {cid.split('/')[-1]}")

        typ = card.get("type")
        if typ not in ("concept", "remark", "correction"):
            errors.append(f"{cid}: type 非法 {typ}")
        if card.get("track") not in TRACKS:
            errors.append(f"{cid}: track 非法 {card.get('track')}")
        if card.get("rights") != "rewritten":
            errors.append(f"{cid}: rights 必须为 rewritten")
        if card.get("status") not in ("draft", "reviewed", "published"):
            errors.append(f"{cid}: status 非法")
        common = ("title", "summary", "question", "aliases", "pitfalls",
                  "sources", "provenance_note")
        for k in (common if typ == "correction" else common + ("related",)):
            need(card, k)
        if card.get("question") and not card["question"].rstrip().endswith("？"):
            errors.append(f"{cid}: question 必须以中文问号结尾")
        if card.get("summary") and han_count(card["summary"]) > 120:
            errors.append(f"{cid}: summary 超过 120 汉字（{han_count(card['summary'])}）")
        if len(card.get("aliases", [])) < 2:
            errors.append(f"{cid}: aliases 至少 2 条")
        if len(card.get("pitfalls", [])) < 1:
            errors.append(f"{cid}: pitfalls 至少 1 条")
        if typ != "correction" and len(card.get("related", [])) < 1:
            errors.append(f"{cid}: related 至少 1 条")

        if typ == "concept":
            for k in ("kind", "statement", "notation", "key_points", "formulas", "proof"):
                need(card, k, "warn")
            if card.get("kind") and card["kind"] not in KINDS:
                errors.append(f"{cid}: kind 非法 {card['kind']}")
            if not isinstance(card.get("kind_no"), int):
                errors.append(f"{cid}: kind_no 必须是整数")
            if len(card.get("key_points", [])) < 2:
                errors.append(f"{cid}: key_points 至少 2 条")
            pr = card.get("proof") or {}
            st = pr.get("status")
            if st not in ("complete", "sketch", "none"):
                errors.append(f"{cid}: proof.status 非法 {st}")
            if st == "complete" and len(pr.get("steps", [])) < 2:
                errors.append(f"{cid}: proof.complete 要求 ≥2 步")
            if st == "sketch" and not pr.get("gap_note"):
                errors.append(f"{cid}: proof.sketch 必须给 gap_note")
            if st == "none" and pr.get("steps"):
                errors.append(f"{cid}: proof.none 不应有 steps")
            if card.get("kind") == "猜想" and st != "none":
                errors.append(f"{cid}: 猜想卡 proof.status 必须是 none")
        if typ == "remark":
            for k in ("statement", "why", "kind_no"):
                need(card, k)

        for s in card.get("sources", []):
            if not isinstance(s, dict) or "anchor" not in s:
                errors.append(f"{cid}: sources 条目缺 anchor")
                continue
            if not s.get("pages"):
                errors.append(f"{cid}: sources 缺 pages（原文印刷页码）")
            check_anchor(card, s["anchor"])

        # 公式里不得出现译注本自定义宏
        bad = re.findall(r"\\(Ainf|eps|lam|dbar|vol|Cmer|Ceps|Yan|TYZ|Tstar|Symp|Hom|Spec|Ber|A|B|C|R|Z|N|Q|F|G|M|X|Y)\b",
                         json.dumps(card, ensure_ascii=False))
        if bad:
            warnings.append(f"{cid}: 出现自定义宏 {sorted(set(bad))}（应展开为 \\mathcal/\\mathbb 形式）")

    for c in cards:
        for r in c.get("related", []):
            if r not in ids:
                warnings.append(f"{c['id']}: related 未解析 {r}")

    print(f"cards: {len(cards)} | errors: {len(errors)} | warnings: {len(warnings)}")
    for e in errors:
        print("ERROR", e)
    for w in warnings[:40]:
        print("WARN ", w)
    if strict and errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
