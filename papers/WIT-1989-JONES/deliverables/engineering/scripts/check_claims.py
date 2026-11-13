#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 claims.jsonl / questions.jsonl 的结构与锚点格式。

用法：
    python check_claims.py <project_root> [--verbose]

检查项：
  1. JSONL 可解析（逐行）；
  2. 必填字段齐全（claims: id/session/claim/type/anchors/source/confidence/status；
     questions: id/session/question/target/why_open/attempts/status）；
  3. 枚举值合法；
  4. id 唯一；
  5. 非 open 类型 claim 至少有一个锚点；
  6. anchors 里的 [src p.N] 落在 351–399（CMP 印刷页范围）。
退出码：0 全部通过；1 有错误。
"""
import json
import re
import sys
from pathlib import Path

CLAIM_FIELDS = ["id", "session", "claim", "type", "anchors", "source", "confidence", "status"]
Q_FIELDS = ["id", "session", "question", "target", "why_open", "attempts", "status"]
CLAIM_TYPES = {"definition", "conjecture", "evidence", "interpretation", "open"}
SOURCES = {"witten", "reconstruction", "post-1990", "textbook"}
CONFIDENCE = {"high", "medium", "low"}
CLAIM_STATUS = {"active", "accepted", "confirmed", "downgraded", "provisional", "contested", "retired"}
Q_STATUS = {"open", "answered", "closed", "superseded"}
PAGE_RE = re.compile(r"p\.\s*(\d{1,3})")

errors = []
warnings = []


def check_page_range(anchor, where):
    m = PAGE_RE.search(anchor)
    if m:
        n = int(m.group(1))
        if not (351 <= n <= 399):
            errors.append(f"{where}: 页码 {n} 不在 351–399（anchor={anchor!r}）")


def check_claims(path, verbose):
    seen = set()
    n = 0
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        n += 1
        where = f"{path.name}:{lineno}"
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"{where}: JSON 解析失败：{e}")
            continue
        missing = [f for f in CLAIM_FIELDS if f not in obj]
        if missing:
            errors.append(f"{where}: 缺字段 {missing}")
            continue
        if obj["id"] in seen:
            errors.append(f"{where}: id 重复 {obj['id']}")
        seen.add(obj["id"])
        if obj["type"] not in CLAIM_TYPES:
            errors.append(f"{where}: type={obj['type']!r} 不合法")
        if obj["source"] not in SOURCES:
            errors.append(f"{where}: source={obj['source']!r} 不合法")
        if obj["confidence"] not in CONFIDENCE:
            errors.append(f"{where}: confidence={obj['confidence']!r} 不合法")
        if obj["status"] not in CLAIM_STATUS:
            warnings.append(f"{where}: status={obj['status']!r} 不在建议集合 {sorted(CLAIM_STATUS)}")
        if obj["type"] != "open" and not obj["anchors"]:
            errors.append(f"{where}: 非 open 的 claim 必须至少有一个锚点")
        for a in obj["anchors"]:
            # 只对 Witten 原刊页锚点检查 351–399；教材页锚点（河野/Moore/李思）不受此限
            if "[src" in a or "[原文" in a:
                check_page_range(a, where)
        if verbose:
            print(f"  ok {obj['id']} [{obj['type']}/{obj['status']}]")
    return n


def check_questions(path, verbose):
    seen = set()
    n = 0
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        n += 1
        where = f"{path.name}:{lineno}"
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"{where}: JSON 解析失败：{e}")
            continue
        missing = [f for f in Q_FIELDS if f not in obj]
        if missing:
            errors.append(f"{where}: 缺字段 {missing}")
            continue
        if obj["id"] in seen:
            errors.append(f"{where}: id 重复 {obj['id']}")
        seen.add(obj["id"])
        if obj["status"] not in Q_STATUS:
            warnings.append(f"{where}: question status={obj['status']!r}")
        if verbose:
            print(f"  ok {obj['id']} [{obj['status']}]")
    return n


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verbose = "--verbose" in sys.argv
    root = Path(args[0]) if args else Path(".")
    sessions = root / "sessions"
    total_c = total_q = 0
    for claims in sorted(sessions.glob("s*/claims.jsonl")):
        print(f"[claims] {claims.relative_to(root)}")
        total_c += check_claims(claims, verbose)
    for qs in sorted(sessions.glob("s*/questions.jsonl")):
        print(f"[questions] {qs.relative_to(root)}")
        total_q += check_questions(qs, verbose)

    print(f"\n统计：claims {total_c} 条，questions {total_q} 条")
    for w in warnings:
        print(f"WARN {w}")
    if errors:
        for e in errors:
            print(f"ERROR {e}")
        print(f"\n失败：{len(errors)} 个错误")
        return 1
    print("通过：0 个错误")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
