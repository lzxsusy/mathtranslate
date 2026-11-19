#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lint_cards.py —— cdm14 资料卡质检。

用法：
    python tools/lint_cards.py cards                 # 全量质检
    python tools/lint_cards.py cards --allow-missing # 起草阶段（related 可暂时悬空）
    python tools/lint_cards.py cards --strict        # 有 error 时退出码 1

检查：JSON 可解析、字段/类型/长度、id 与文件名一致、track 合法、question 以问号结尾、
summary ≤120 汉字、related 可解析、sources 的 pages 范围与 anchor 格式、
推导卡 steps ≥3 且每步四字段齐全、概念卡 proof 规则、禁本机路径、status 合法、id 唯一。
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKS = {"A", "B", "C", "D", "E", "F", "G", "O"}
STATUS = {"draft", "dev"}
ID_RE = re.compile(r"^cdm14/(concept|deriv)/([a-z0-9]+(?:-[a-z0-9]+)*)$")
ANCHOR_RE = re.compile(r"^(A|B|C|D) p\.\d+(\s*[–-]\s*\d+)?(\s+eq\s+\(?[\w.\-]+\)?)?$")
ABS_RE = re.compile(r"(?:[A-Za-z]:\\+(?:Users|admin|Desktop|dsh|Program|Windows)|C:/Users|/c/Users|file:///)")


def text_len(s: str) -> int:
    s = re.sub(r"\$[^$]*\$", "", s or "")
    s = re.sub(r"\s+", "", s)
    return len(s)


def check_card(path: Path, card: dict, ids: set):
    e = []
    kind = "concepts" if "concepts" in path.parts else "derivations"
    cid = card.get("id", "")
    m = ID_RE.match(cid)
    if not m:
        e.append(f"id 格式错：{cid}")
    else:
        if m.group(1) != ("concept" if kind == "concepts" else "deriv"):
            e.append("id 类型与目录不符")
        if m.group(2) != path.stem:
            e.append(f"slug 与文件名不符：{m.group(2)} vs {path.stem}")
    if card.get("type") != ("concept" if kind == "concepts" else "derivation"):
        e.append("type 与目录不符")
    if card.get("track") not in TRACKS:
        e.append(f"track 非法：{card.get('track')}")
    for k in ("title", "summary", "question", "pitfalls", "related", "sources", "rights", "status", "provenance_note"):
        if k not in card:
            e.append(f"缺字段 {k}")
    if text_len(card.get("summary", "")) > 120:
        e.append(f"summary 过长：{text_len(card.get('summary',''))}")
    q = card.get("question", "")
    if not q.rstrip().endswith(("？", "?")):
        e.append("question 未以问号结尾")
    if card.get("rights") != "rewritten":
        e.append("rights 必须是 rewritten")
    if card.get("status") not in STATUS:
        e.append(f"status 非法：{card.get('status')}")
    if not isinstance(card.get("pitfalls"), list) or len(card.get("pitfalls", [])) < 2:
        e.append("pitfalls 至少 2 条")
    rel = card.get("related", [])
    if not isinstance(rel, list) or len(rel) < 1:
        e.append("related 至少 1 条")
    for r in rel:
        if r not in ids:
            e.append(f"related 指向不存在的卡：{r}")

    srcs = card.get("sources", [])
    if not isinstance(srcs, list) or not srcs:
        e.append("sources 必须非空")
    for i, s in enumerate(srcs):
        if s.get("text") not in {"A", "B", "C", "D"}:
            e.append(f"sources[{i}].text 非法")
        pages = s.get("pages")
        if not (isinstance(pages, list) and len(pages) == 2 and all(isinstance(x, int) for x in pages)):
            e.append(f"sources[{i}].pages 必须是两整数")
        elif not (1 <= pages[0] <= pages[1] <= 65):
            e.append(f"sources[{i}].pages 越界：{pages}")
        if not ANCHOR_RE.match(s.get("anchor", "")):
            e.append(f"sources[{i}].anchor 格式错：{s.get('anchor')}")

    if kind == "concepts":
        d = card.get("definition")
        if not isinstance(d, dict) or not d.get("text"):
            e.append("definition.text 必填")
        if len(card.get("key_points", [])) < 3:
            e.append("key_points 至少 3 条")
        if len(card.get("formulas", [])) < 1:
            e.append("formulas 至少 1 条")
        for j, t in enumerate(card.get("theorems", [])):
            pr = (t or {}).get("proof") or {}
            st = pr.get("status")
            if st not in {"complete", "sketch", "gap"}:
                e.append(f"theorems[{j}].proof.status 非法")
            steps = pr.get("steps") or []
            if st == "complete":
                if len(steps) < 2:
                    e.append(f"theorems[{j}] complete 需 ≥2 步")
                for k, stp in enumerate(steps):
                    if not stp.get("text") or not stp.get("why"):
                        e.append(f"theorems[{j}].steps[{k}] 缺 text/why")
            elif not pr.get("gap_note"):
                e.append(f"theorems[{j}] {st} 必须有 gap_note")
    else:
        if not card.get("goal"):
            e.append("goal 必填")
        if len(card.get("setup", [])) < 1:
            e.append("setup 至少 1 条")
        steps = card.get("steps", [])
        if len(steps) < 3:
            e.append(f"steps 至少 3 条（现 {len(steps)}）")
        for k, stp in enumerate(steps):
            for f in ("text", "why", "locator", "provenance"):
                if not stp.get(f):
                    e.append(f"steps[{k}] 缺 {f}")
            if stp.get("provenance") not in {"A", "B", "C"}:
                e.append(f"steps[{k}].provenance 非法")
            if not ANCHOR_RE.match(stp.get("locator", "")):
                e.append(f"steps[{k}].locator 格式错：{stp.get('locator')}")
        if not card.get("result"):
            e.append("result 必填")

    raw = json.dumps(card, ensure_ascii=False)
    if ABS_RE.search(raw):
        e.append("含本机绝对路径")
    return e


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default="cards")
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    base = ROOT / args.target if not Path(args.target).is_absolute() else Path(args.target)

    cards = {}
    for kind in ("concepts", "derivations"):
        for p in sorted((base / kind).glob("*.json")):
            try:
                cards[p] = json.loads(p.read_text(encoding="utf-8"))
            except Exception as ex:  # noqa: BLE001
                print(f"[JSON ERROR] {p.name}: {ex}")
                cards[p] = None
    ids = {c["id"] for c in cards.values() if c}
    dup = len(cards) - len(ids)
    total_err = 0
    by_track = {}
    for p, c in cards.items():
        if c is None:
            total_err += 1
            continue
        errs = check_card(p, c, ids)
        if args.allow_missing:
            errs = [x for x in errs if "related 指向不存在" not in x]
        by_track[c.get("track", "?")] = by_track.get(c.get("track", "?"), 0) + 1
        if errs:
            total_err += len(errs)
            print(f"{p.name}:")
            for x in errs:
                print(f"  - {x}")
    print("-" * 60)
    print(f"cards={len(cards)} ids={len(ids)} dup={dup} tracks={by_track} errors={total_err}")
    if total_err == 0:
        print("OK: 0 error")
    if args.strict and (total_err or dup):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
