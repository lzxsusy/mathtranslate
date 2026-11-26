#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate one Pass A / Pass B / tiebreak JSONL file for the glc full audit.

Usage:
  python check_audit.py --file passA/A1_groupA1.jsonl --group A1 --reviewer A1
  python check_audit.py --file passB/B1.jsonl --list passB/B1.list --reviewer B1

Checks: JSONL syntax, required fields, n continuity against the group list,
path membership, verdict/issues consistency, checks>=3 with the three required
aspect families, issue evidence completeness, `card_says` really present in the
card, control characters inside decoded strings.
"""
import argparse
import json
import os
import re
import sys

ROOT = r"C:/Users/admin/Desktop/数译发布/gitee_shuyi"
AUD = os.path.join(ROOT, "datasets/_audit/glc_full_2026-11-26")

VERDICTS = {"pass", "issue", "unverifiable"}
CONFIDENCES = {"high", "medium", "low"}
SEVERITIES = {"critical", "major", "minor"}
CHECK_VERDICTS = {"ok", "issue", "na", "concern"}
REQUIRED = ["n", "group", "reviewer", "pass", "set", "id", "path", "verdict",
            "confidence", "checks", "issues", "unverifiable_aspects", "notes"]


def load_group(name):
    p = os.path.join(AUD, "groups", name + ".txt")
    with open(p, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]


def load_list(p):
    with open(p, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]


def card_json(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return json.load(f)


def norm(s):
    return re.sub(r"\s+", "", s or "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--group", required=True)
    ap.add_argument("--reviewer", required=True)
    ap.add_argument("--list", default=None, help="explicit path list (passB/tiebreak)")
    ap.add_argument("--expect", type=int, default=None)
    ap.add_argument("--allow-subset", action="store_true")
    args = ap.parse_args()

    expected = load_list(args.list) if args.list else load_group(args.group)
    if args.expect is not None and len(expected) != args.expect:
        expected = expected[: args.expect]

    errors, warns = [], []
    rows = []
    with open(args.file, encoding="utf-8") as f:
        for i, ln in enumerate(f, 1):
            ln = ln.strip()
            if not ln:
                continue
            try:
                rows.append((i, json.loads(ln)))
            except Exception as e:  # noqa: BLE001
                errors.append("line %d: bad JSON: %s" % (i, e))

    if not rows:
        print("EMPTY FILE: %s" % args.file)
        return 1

    seen = set()
    for i, r in rows:
        tag = "line %d (%s)" % (i, r.get("id", "?"))
        for k in REQUIRED:
            if k not in r:
                errors.append("%s: missing field %r" % (tag, k))
        if r.get("reviewer") != args.reviewer:
            errors.append("%s: reviewer %r != %r" % (tag, r.get("reviewer"), args.reviewer))
        if r.get("pass") not in {"A", "B", "arbiter"}:
            errors.append("%s: bad pass %r" % (tag, r.get("pass")))
        if r.get("set") != "glc":
            errors.append("%s: set %r != 'glc'" % (tag, r.get("set")))
        v = r.get("verdict")
        if v not in VERDICTS:
            errors.append("%s: bad verdict %r" % (tag, v))
        if r.get("confidence") not in CONFIDENCES:
            errors.append("%s: bad confidence %r" % (tag, r.get("confidence")))
        checks = r.get("checks") or []
        if len(checks) < 3:
            errors.append("%s: only %d checks (need >=3)" % (tag, len(checks)))
        aspects = " ".join((c.get("aspect", "") if isinstance(c, dict) else str(c)) for c in checks)
        for family, pats in (("math", ("defin", "theor", "math", "formula", "statement")),
                             ("sources", ("source", "anchor", "page", "citat", "quote")),
                             ("internal", ("internal", "consist", "summary", "related", "pitfall", "term"))):
            if not any(p in aspects.lower() for p in pats):
                errors.append("%s: checks miss the %r family" % (tag, family))
        for c in checks:
            if isinstance(c, dict):
                if c.get("verdict") not in CHECK_VERDICTS:
                    errors.append("%s: check verdict %r" % (tag, c.get("verdict")))
                if not (c.get("note") or "").strip():
                    errors.append("%s: check without note" % (tag,))
            elif not str(c).strip():
                errors.append("%s: empty check" % (tag,))
        issues = r.get("issues") or []
        if v == "issue" and not issues:
            errors.append("%s: verdict=issue but issues empty" % (tag,))
        if v != "issue" and issues:
            errors.append("%s: verdict=%s but issues non-empty" % (tag, v))
        if v == "unverifiable" and not (r.get("unverifiable_aspects") or []):
            errors.append("%s: verdict=unverifiable without unverifiable_aspects" % (tag,))
        if v == "unverifiable" and not (r.get("notes") or "").strip():
            errors.append("%s: verdict=unverifiable without notes" % (tag,))
        for j, iss in enumerate(issues):
            for k in ("severity", "aspect", "field", "card_says", "problem", "should_be", "evidence"):
                if k not in iss or (k != "evidence" and not str(iss.get(k) or "").strip()):
                    errors.append("%s: issue[%d] missing %r" % (tag, j, k))
            if iss.get("severity") not in SEVERITIES:
                errors.append("%s: issue[%d] bad severity %r" % (tag, j, iss.get("severity")))
            ev = iss.get("evidence") or []
            if not ev:
                errors.append("%s: issue[%d] has no evidence" % (tag, j))
            for k, e in enumerate(ev):
                if not isinstance(e, dict):
                    errors.append("%s: issue[%d].evidence[%d] not an object" % (tag, j, k))
                    continue
                if not (e.get("ref") or "").strip():
                    errors.append("%s: issue[%d].evidence[%d] missing ref" % (tag, j, k))
        if r.get("path") not in expected:
            errors.append("%s: path not in group %s: %r" % (tag, args.group, r.get("path")))
        if r.get("path") in seen:
            errors.append("%s: duplicate path" % (tag,))
        seen.add(r.get("path"))

    if not args.allow_subset and len(rows) != len(expected):
        errors.append("row count %d != group size %d" % (len(rows), len(expected)))
    if not args.allow_subset:
        for idx, (i, r) in enumerate(rows, 1):
            if r.get("n") != idx:
                errors.append("line %d: n=%r, expected %d (file order must follow the group list)"
                              % (i, r.get("n"), idx))
            if r.get("path") != expected[idx - 1]:
                errors.append("line %d: path %r != group list position %d %r"
                              % (i, r.get("path"), idx, expected[idx - 1]))

    # card_says must really occur in the card (guards against invented quotes)
    cache = {}
    for i, r in rows:
        if r.get("verdict") != "issue":
            continue
        try:
            cj = cache.setdefault(r["path"], card_json(r["path"]))
        except Exception as e:  # noqa: BLE001
            errors.append("line %d: cannot load card: %s" % (i, e))
            continue
        blob = norm(json.dumps(cj, ensure_ascii=False))
        for j, iss in enumerate(r.get("issues") or []):
            cs = norm(iss.get("card_says", ""))
            if not cs:
                continue
            parts = [p for p in cs.split("…") if p.strip()]
            if not all(p in blob for p in parts):
                warns.append("line %d: issue[%d].card_says not found verbatim in card: %r"
                             % (i, j, iss["card_says"][:80]))

    for w in warns:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    print("== %s: %d rows, %d errors, %d warnings ==" % (args.file, len(rows), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
