#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compare Pass A and Pass B verdicts (blind double review).

Classifications per card:
  both_issue     A issue  & B issue   -> confirmed, goes to lead evidence review
  a_issue_only   A issue  & B pass    -> needs a third blind arbiter
  b_issue_only   A pass   & B issue   -> needs a third blind arbiter
  both_pass      A pass   & B pass
  unverifiable   either side could not verify (recorded, never auto-confirmed)
  missing_b      A-issue card the B list failed to cover  (hard error)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))


def load_jsonl_dirs(*dirs):
    rows = []
    for d in dirs:
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p):
            continue
        for fn in sorted(os.listdir(p)):
            if not fn.endswith(".jsonl"):
                continue
            with open(os.path.join(p, fn), "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        rows.append(json.loads(line))
    return rows


def classify(a, b):
    av = (a or {}).get("verdict")
    bv = (b or {}).get("verdict")
    if av == "issue" and bv == "issue":
        return "both_issue"
    if av == "issue" and bv == "pass":
        return "a_issue_only"
    if av == "pass" and bv == "issue":
        return "b_issue_only"
    if av == "pass" and bv == "pass":
        return "both_pass"
    if bv is None:
        # card outside the 20% blind sample: nothing to compare
        return "b_not_sampled"
    if av in (None, "unverifiable") or bv in (None, "unverifiable"):
        return "unverifiable"
    return "other:%s/%s" % (av, bv)


def sev_of(row, which):
    """heaviest severity among the side's issues"""
    order = {"critical": 3, "major": 2, "minor": 1}
    best = None
    for it in (row or {}).get("issues", []):
        s = it.get("severity")
        if best is None or order.get(s, 0) > order.get(best, 0):
            best = s
    return best


def main():
    a_rows = load_jsonl_dirs("passA")
    b_rows = load_jsonl_dirs("passB")
    if len(a_rows) != len({r["id"] for r in a_rows}):
        print("ERROR: duplicate ids in passA")
        sys.exit(1)
    A = {r["id"]: r for r in a_rows}
    B = {}
    for r in b_rows:
        if r["id"] in B:
            print("ERROR: duplicate id in passB: %s" % r["id"])
            sys.exit(1)
        B[r["id"]] = r

    out = []
    counts = {}
    for cid in sorted(set(A) | set(B)):
        a, b = A.get(cid), B.get(cid)
        cls = classify(a, b)
        if a and a.get("verdict") == "issue" and b is None:
            cls = "missing_b"
        counts[cls] = counts.get(cls, 0) + 1
        out.append({
            "id": cid,
            "path": (a or b)["path"],
            "a_group": (a or {}).get("group"),
            "a_reviewer": (a or {}).get("reviewer"),
            "a_verdict": (a or {}).get("verdict"),
            "a_confidence": (a or {}).get("confidence"),
            "a_severity": sev_of(a, "A"),
            "a_issues": (a or {}).get("issues", []),
            "a_unverifiable": (a or {}).get("unverifiable_aspects", []),
            "b_group": (b or {}).get("group"),
            "b_reviewer": (b or {}).get("reviewer"),
            "b_verdict": (b or {}).get("verdict"),
            "b_confidence": (b or {}).get("confidence"),
            "b_severity": sev_of(b, "B"),
            "b_issues": (b or {}).get("issues", []),
            "b_unverifiable": (b or {}).get("unverifiable_aspects", []),
            "class": cls,
        })

    # field-level agreement for both_issue cards
    for r in out:
        if r["class"] != "both_issue":
            continue
        fa = {i.get("field") for i in r["a_issues"]}
        fb = {i.get("field") for i in r["b_issues"]}
        r["field_overlap"] = sorted(fa & fb)
        r["field_a_only"] = sorted(fa - fb)
        r["field_b_only"] = sorted(fb - fa)

    with open(os.path.join(ROOT, "compare.json"), "w", encoding="utf-8") as f:
        json.dump({
            "counts": counts,
            "passA_rows": len(a_rows),
            "passB_rows": len(b_rows),
            "both_issue_field_agree": sum(1 for r in out if r.get("field_overlap")),
            "both_issue_field_disagree": sum(
                1 for r in out if r["class"] == "both_issue" and not r.get("field_overlap")),
            "cards": out,
        }, f, ensure_ascii=False, indent=2)
        f.write("\n")

    lines = ["# Pass A / Pass B 对照", ""]
    lines.append("A 记录 %d 行，B 记录 %d 行。" % (len(a_rows), len(b_rows)))
    lines.append("")
    lines.append("| 分类 | 卡数 |")
    lines.append("|---|---|")
    for k in sorted(counts):
        lines.append("| %s | %d |" % (k, counts[k]))
    lines.append("")
    lines.append("## both_issue（可进入确认）")
    lines.append("")
    lines.append("| id | A group | A sev | B group | B sev | 字段重叠 |")
    lines.append("|---|---|---|---|---|---|")
    for r in out:
        if r["class"] == "both_issue":
            lines.append("| %s | %s | %s | %s | %s | %s |" % (
                r["id"], r["a_group"], r["a_severity"], r["b_group"],
                r["b_severity"], ", ".join(r["field_overlap"]) or "—"))
    for cls in ("a_issue_only", "b_issue_only", "missing_b"):
        sub = [r for r in out if r["class"] == cls]
        if not sub:
            continue
        lines.append("")
        lines.append("## %s（需 arbiter 盲审）" % cls if cls != "missing_b"
                     else "## missing_b（B 漏审，必须补）")
        lines.append("")
        lines.append("| id | A verdict | B verdict | A sev | B sev |")
        lines.append("|---|---|---|---|---|")
        for r in sub:
            lines.append("| %s | %s | %s | %s | %s |" % (
                r["id"], r["a_verdict"], r["b_verdict"], r["a_severity"], r["b_severity"]))
    lines.append("")
    with open(os.path.join(ROOT, "compare.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(json.dumps(counts, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
