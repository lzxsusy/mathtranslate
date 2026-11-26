#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日核验记录校验器。

用法:
  python 11_card_audit/daily_verify/tools/check_daily.py \
    --file 11_card_audit/daily_verify/<date>/records.jsonl \
    --sample 11_card_audit/daily_verify/<date>/sample.json [--append-ledger]

检查:
  - 一行一卡、n 连续、id 与 sample 一致（不重不漏）；
  - 必需字段齐全，verdict/confidence 取值合法；
  - 每卡 checks >= 3 且覆盖 A/B/C 三类；
  - verdict=issue <=> issues 非空；issue 必带 severity/field/card_says/problem/should_be/evidence；
  - card_says 去空白后必须是卡 JSON 的子串；
  - evidence 的 kind/ref/quote 非空。
退出码: 0 = 无 error；1 = 有 error。
"""
import argparse
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DAILY = os.path.join(ROOT, "11_card_audit", "daily_verify")
LEDGER = os.path.join(DAILY, "ledger.jsonl")

A_ASPECTS = {"definition", "theorem", "formula", "example", "math", "mathematical"}
B_ASPECTS = {"sources", "source", "anchor", "quotation"}
C_ASPECTS = {"internal", "consistency", "related"}
SEV = {"critical", "major", "minor"}
VERDICTS = {"pass", "issue", "unverifiable"}
CONF = {"high", "medium", "low"}
REQUIRED = ["n", "date", "set", "id", "path", "verdict", "confidence", "checks",
            "issues", "unverifiable_aspects", "notes"]


def norm(s):
    return re.sub(r"\s+", "", s or "")


def load_card(path):
    p = os.path.join(ROOT, path)
    try:
        with io.open(p, encoding="utf-8") as f:
            raw = f.read()
        return raw, norm(raw)
    except Exception:
        return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--sample", required=True)
    ap.add_argument("--append-ledger", action="store_true")
    args = ap.parse_args()

    errors, warns = [], []
    with io.open(args.sample, encoding="utf-8") as f:
        sample = json.load(f)
    items = sample.get("items", [])
    by_id = {c["id"]: c for c in items}
    order = [c["id"] for c in items]

    rows = []
    with io.open(args.file, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append((ln, json.loads(line)))
            except Exception as e:
                errors.append("line %d: bad JSON (%s)" % (ln, e))
    if len(rows) != len(items):
        errors.append("record count %d != sample count %d" % (len(rows), len(items)))

    seen = []
    for i, (ln, r) in enumerate(rows):
        where = "row %d%s" % (i + 1, " (line %d)" % ln)
        for k in REQUIRED:
            if k not in r:
                errors.append("%s: missing %s" % (where, k))
        if r.get("n") != i + 1:
            errors.append("%s: n=%r expected %d" % (where, r.get("n"), i + 1))
        cid = r.get("id")
        seen.append(cid)
        if i < len(order) and cid != order[i]:
            errors.append("%s: id %r != sample[%d] %r" % (where, cid, i, order[i]))
        if cid not in by_id:
            errors.append("%s: id %r not in sample" % (where, cid))
            continue
        if r.get("path") != by_id[cid].get("path"):
            errors.append("%s: path mismatch %r vs %r" % (where, r.get("path"), by_id[cid].get("path")))
        if r.get("verdict") not in VERDICTS:
            errors.append("%s: bad verdict %r" % (where, r.get("verdict")))
        if r.get("confidence") not in CONF:
            errors.append("%s: bad confidence %r" % (where, r.get("confidence")))

        checks = r.get("checks") or []
        if len(checks) < 3:
            errors.append("%s: checks=%d < 3" % (where, len(checks)))
        cats = set()
        for j, c in enumerate(checks):
            a = str(c.get("aspect", "")).lower()
            if a in A_ASPECTS:
                cats.add("A")
            elif a in B_ASPECTS:
                cats.add("B")
            elif a in C_ASPECTS:
                cats.add("C")
            else:
                warns.append("%s.check%d: unknown aspect %r" % (where, j + 1, a))
            if c.get("verdict") not in ("ok", "issue", "na", "concern"):
                errors.append("%s.check%d: bad check verdict %r" % (where, j + 1, c.get("verdict")))
            if not str(c.get("detail", "")).strip():
                warns.append("%s.check%d: empty detail" % (where, j + 1))
        for need, name in (("A", "math"), ("B", "sources"), ("C", "internal")):
            if need not in cats:
                errors.append("%s: checks do not cover %s" % (where, name))

        issues = r.get("issues") or []
        if r.get("verdict") == "issue" and not issues:
            errors.append("%s: verdict=issue but issues empty" % where)
        if r.get("verdict") != "issue" and issues:
            errors.append("%s: verdict=%r but issues non-empty" % (where, r.get("verdict")))
        raw, nr = load_card(r.get("path", ""))
        if raw is None:
            errors.append("%s: card not found %r" % (where, r.get("path")))
        for j, iss in enumerate(issues):
            w = "%s.issue%d" % (where, j + 1)
            for k in ("severity", "aspect", "field", "card_says", "problem", "should_be", "evidence"):
                if k not in iss:
                    errors.append("%s: missing %s" % (w, k))
            if iss.get("severity") not in SEV:
                errors.append("%s: bad severity %r" % (w, iss.get("severity")))
            if not str(iss.get("field", "")).strip():
                errors.append("%s: empty field" % w)
            ev = iss.get("evidence") or []
            if not ev:
                errors.append("%s: evidence empty" % w)
            for k, e in enumerate(ev):
                if not e.get("kind") or not e.get("ref") or not e.get("quote"):
                    errors.append("%s.evidence%d: kind/ref/quote required" % (w, k + 1))
            cs = norm(iss.get("card_says"))
            if cs and nr is not None and cs not in nr:
                errors.append("%s: card_says is not a substring of the card" % w)
            if not cs:
                errors.append("%s: empty card_says" % w)

        if r.get("verdict") == "unverifiable" and not (r.get("unverifiable_aspects") or []):
            warns.append("%s: unverifiable without unverifiable_aspects" % where)

    if [s for s in seen if s not in by_id]:
        errors.append("records contain ids outside sample")
    if len(set(seen)) != len(seen):
        errors.append("duplicate ids in records")

    print("checked %d row(s): %d error(s), %d warning(s)" % (len(rows), len(errors), len(warns)))
    for e in errors:
        print("ERROR:", e)
    for w in warns:
        print("WARN:", w)

    if args.append_ledger and not errors:
        os.makedirs(DAILY, exist_ok=True)
        existing = set()
        if os.path.exists(LEDGER):
            with io.open(LEDGER, encoding="utf-8") as f:
                for line in f:
                    try:
                        row = json.loads(line)
                    except Exception:
                        continue
                    existing.add((row.get("date"), row.get("id")))
        added = 0
        with io.open(LEDGER, "a", encoding="utf-8", newline="\n") as f:
            for _, r in rows:
                key = (r.get("date"), r.get("id"))
                if key in existing:
                    continue
                sev = [i.get("severity") for i in (r.get("issues") or [])]
                rank = {"critical": 3, "major": 2, "minor": 1}
                smax = max(sev, key=lambda s: rank.get(s, 0)) if sev else ""
                f.write(json.dumps({
                    "date": r.get("date"), "id": r.get("id"), "path": r.get("path"),
                    "verdict": r.get("verdict"), "confidence": r.get("confidence"),
                    "severity_max": smax, "n_issues": len(sev),
                }, ensure_ascii=False) + "\n")
                added += 1
        print("ledger appended: %d row(s) -> %s" % (added, os.path.relpath(LEDGER, ROOT)))
    elif args.append_ledger:
        print("ledger NOT appended: fix errors first")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
