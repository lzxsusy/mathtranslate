#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lint_cards.py —— raskin_lcft 资料卡质检。

用法：
    python tools/lint_cards.py cards
    python tools/lint_cards.py cards --allow-missing
    python tools/lint_cards.py cards --strict

检查：JSON 可解析；字段/类型/长度；id 与目录、文件名一致；track 合法；question 以问号结尾；
summary ≤120 汉字；related 可解析；sources 页码与 anchor 格式；三类卡各自的必填结构；
禁本机绝对路径；status 合法；id 唯一。
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKS = {"A", "B", "C", "D", "E", "F", "O"}
STATUS = {"draft", "reviewed", "published"}
ID_RE = re.compile(r"^raskin_lcft/(concept|deriv|correction)/([a-z0-9]+(?:-[a-z0-9]+)*)$")
ANCHOR_RE = re.compile(r"^原书 p\.\d+")
ABS_RE = re.compile(r"(?:[A-Za-z]:\\+Users|[A-Za-z]:/Users|/c/Users|file:///|C:\\\\Users)")
BOOK = "Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)"
PAGE_MIN, PAGE_MAX = 1, 115  # 讲义原 PDF 的印刷页 1–115


def text_len(s: str) -> int:
    s = re.sub(r"\$[^$]*\$", "", s or "")
    s = re.sub(r"\s+", "", s)
    return len(s)


def check_common(card, path, ids, allow_missing):
    e = []
    cid = card.get("id", "")
    m = ID_RE.match(cid)
    kind = {"concepts": "concept", "derivations": "deriv", "corrections": "correction"}.get(path.parent.name)
    if not m:
        e.append(f"id 格式错：{cid}")
    else:
        if m.group(1) != kind:
            e.append("id 的类型段与目录不符")
        if m.group(2) != path.stem:
            e.append(f"slug 与文件名不符：{m.group(2)} vs {path.stem}")
    if card.get("type") != {"concept": "concept", "deriv": "derivation", "correction": "correction"}[kind]:
        e.append("type 与目录不符")
    if card.get("track") not in TRACKS:
        e.append(f"track 非法：{card.get('track')}")
    for k in ("title", "aliases", "summary", "question", "pitfalls", "related", "sources",
              "rights", "status", "provenance_note"):
        if k not in card:
            e.append(f"缺字段 {k}")
    if text_len(card.get("summary", "")) > 120:
        e.append(f"summary 过长：{text_len(card.get('summary',''))}")
    if not str(card.get("question", "")).rstrip().endswith(("？", "?")):
        e.append("question 未以问号结尾")
    if card.get("rights") != "rewritten":
        e.append("rights 必须是 rewritten")
    if card.get("status") not in STATUS:
        e.append(f"status 非法：{card.get('status')}")
    if not isinstance(card.get("aliases"), list) or not card.get("aliases"):
        e.append("aliases 必须是非空数组")
    if not isinstance(card.get("related"), list) or len(card.get("related", [])) < 2:
        e.append("related 至少 2 条")
    else:
        for r in card["related"]:
            if not allow_missing and r not in ids:
                e.append(f"related 悬空：{r}")
    srcs = card.get("sources")
    if not isinstance(srcs, list) or not srcs:
        e.append("sources 至少 1 条")
    else:
        for s in srcs:
            if s.get("book") != BOOK:
                e.append("sources.book 与数据集约定不符")
            pg = s.get("pages")
            if not (isinstance(pg, list) and len(pg) == 2 and all(isinstance(x, int) for x in pg)
                    and PAGE_MIN <= pg[0] <= pg[1] <= PAGE_MAX):
                e.append(f"sources.pages 非法：{pg}")
            if not ANCHOR_RE.match(s.get("anchor", "")):
                e.append(f"sources.anchor 非法：{s.get('anchor')}")
    if ABS_RE.search(json.dumps(card, ensure_ascii=False)):
        e.append("出现本机绝对路径")
    return e


def check_concept(card):
    e = []
    for k in ("definition", "key_points", "formulas", "theorems"):
        if k not in card:
            e.append(f"概念卡缺字段 {k}")
    d = card.get("definition", {})
    if not isinstance(d, dict) or not d.get("text"):
        e.append("definition.text 为空")
    if not isinstance(card.get("key_points"), list) or len(card.get("key_points", [])) < 3:
        e.append("key_points 至少 3 条")
    if not isinstance(card.get("formulas"), list) or len(card.get("formulas", [])) < 1:
        e.append("formulas 至少 1 条")
    for t in card.get("theorems", []):
        for k in ("name", "statement", "proof", "source"):
            if k not in t:
                e.append(f"theorem 缺 {k}")
        pr = t.get("proof", {})
        if pr.get("status") not in {"complete", "sketch", "none"}:
            e.append(f"proof.status 非法：{pr.get('status')}")
        if pr.get("status") == "complete" and not pr.get("steps"):
            e.append("proof 标 complete 但没有 steps")
    return e


def check_deriv(card):
    e = []
    for k in ("goal", "setup", "steps", "result", "gaps"):
        if k not in card:
            e.append(f"推导卡缺字段 {k}")
    if not isinstance(card.get("setup"), list) or len(card.get("setup", [])) < 1:
        e.append("setup 至少 1 条")
    if not isinstance(card.get("steps"), list) or len(card.get("steps", [])) < 3:
        e.append("steps 至少 3 步")
    for st in card.get("steps", []):
        for k in ("no", "text", "why", "locator", "provenance"):
            if k not in st:
                e.append(f"step 缺 {k}")
        if st.get("provenance") not in {"A", "B", "C"}:
            e.append(f"step.provenance 非法：{st.get('provenance')}")
        if not str(st.get("locator", "")).startswith("原书 p."):
            e.append(f"step.locator 必须以「原书 p.」开头：{st.get('locator')}")
    if not isinstance(card.get("gaps"), list) or not card.get("gaps"):
        e.append("gaps 至少 1 条")
    return e


def check_correction(card):
    e = []
    for k in ("page", "original", "corrected", "why", "note"):
        if k not in card:
            e.append(f"勘误卡缺字段 {k}")
    if not isinstance(card.get("page"), int) or not (PAGE_MIN <= card["page"] <= PAGE_MAX):
        e.append(f"page 非法：{card.get('page')}")
    for k in ("original", "corrected", "why"):
        if not str(card.get(k, "")).strip():
            e.append(f"{k} 为空")
    return e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cards", nargs="?", default="cards")
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    base = ROOT / args.cards
    files = sorted(base.glob("**/*.json"))
    if not base.is_dir():
        print(f"卡片目录不存在：{base}")
        return 1
    if not files:
        # 空数据集是合法状态：脚手架阶段 cards/ 下还没有卡。
        print("卡片 0 张（空数据集）")
        print("OK：0 error，0 warn")
        return 0

    cards, parse_errs = {}, []
    for p in files:
        try:
            cards[p] = json.loads(p.read_text(encoding="utf-8"))
        except Exception as ex:
            parse_errs.append(f"{p.relative_to(ROOT)}: JSON 解析失败：{ex}")

    ids = {c.get("id") for c in cards.values() if isinstance(c, dict)}
    errors, warns = list(parse_errs), []
    seen = {}
    for c in cards.values():
        if isinstance(c, dict):
            cid = c.get("id", "")
            seen[cid] = seen.get(cid, 0) + 1
    for cid, n in seen.items():
        if n > 1:
            errors.append(f"id 重复 {cid}（{n} 次）")
    for p, c in cards.items():
        if not isinstance(c, dict):
            errors.append(f"{p.relative_to(ROOT)}: 根不是对象")
            continue
        rel = p.relative_to(ROOT)
        e = check_common(c, p, ids, args.allow_missing)
        if p.parent.name == "concepts":
            e += check_concept(c)
        elif p.parent.name == "derivations":
            e += check_deriv(c)
        elif p.parent.name == "corrections":
            e += check_correction(c)
        if len(c.get("key_points", []) if isinstance(c.get("key_points"), list) else []) > 6:
            warns.append(f"{rel}: key_points 超过 6 条")
        for msg in e:
            errors.append(f"{rel}: {msg}")

    print(f"卡片 {len(cards)} 张（概念 {sum(1 for p in cards if p.parent.name=='concepts')}，"
          f"推导 {sum(1 for p in cards if p.parent.name=='derivations')}，"
          f"勘误 {sum(1 for p in cards if p.parent.name=='corrections')}）")
    for w in warns:
        print("WARN", w)
    for e in errors:
        print("ERROR", e)
    print(f"{'FAIL' if errors else 'OK'}：{len(errors)} error，{len(warns)} warn")
    if args.strict and errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
