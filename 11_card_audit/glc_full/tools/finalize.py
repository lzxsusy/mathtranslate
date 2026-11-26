# -*- coding: utf-8 -*-
"""Consolidate the campaign into issues.jsonl + stats.json.

Reads compare.json (pass A/B classification), tiebreak/*.jsonl (arbiter rows)
and fix_log.json (what was actually repaired).  Writes
  datasets/_audit/glc_full_2026-11-26/issues.jsonl
  datasets/_audit/glc_full_2026-11-26/tmp/stats.json

Status vocabulary per issue item:
  confirmed_fixed      two independent judgments agree (or arbiter breaks a tie)
                       and the edit is in fix_log.json
  confirmed_not_fixed  confirmed but the lead judged it out of scope (should be 0)
  single_sided         one reviewer only, arbiter passed -> recorded, not fixed
  unverifiable         reviewer could not verify against E1/E2
"""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def jload(name):
    p = os.path.join(ROOT, name)
    if not os.path.isfile(p):
        return None
    with io.open(p, encoding="utf-8") as fh:
        return json.load(fh)


def jsonl_dir(d):
    rows = []
    p = os.path.join(ROOT, d)
    if not os.path.isdir(p):
        return rows
    for fn in sorted(os.listdir(p)):
        if fn.endswith(".jsonl"):
            with io.open(os.path.join(p, fn), encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        rows.append(json.loads(line))
    return rows


def field_tokens(items):
    """Field paths mentioned in issue items, normalised for cross-reviewer
    comparison: 'sources[0].pages', 'key_points[3]＋pitfalls[0]' and
    'theorems[0].source＋gap_note' all yield plain paths; the index-stripped
    form is added too so 'sources.pages' matches 'sources[0].pages'."""
    out = set()
    pat = re.compile(r"[A-Za-z_]+(?:\[\d+\])?(?:\.[A-Za-z_]+(?:\[\d+\])?)*")
    for it in items or []:
        txt = str(it.get("field") or "")
        for tok in pat.findall(txt):
            out.add(tok)
            out.add(re.sub(r"\[\d+\]", "", tok))
    return out


def main():
    compare = jload("compare.json")
    fixes = jload("fix_log.json")
    inv = jload("sample_inventory.json")
    assert compare and inv, "run compare.py first"
    A = {r["id"]: r for r in jsonl_dir("passA")}
    B = {r["id"]: r for r in jsonl_dir("passB")}
    T = {r["id"]: r for r in jsonl_dir("tiebreak")}
    F = {fx["id"]: fx for fx in (fixes or {}).get("fixes", [])}
    title = {c["id"]: c["title"] for c in inv["cards"]}

    issues = []
    for card in compare["cards"]:
        cid = card["id"]
        cls = card["class"]
        if cls == "both_issue":
            chain = "A+B"
            status = "confirmed_fixed" if cid in F else "confirmed_not_fixed"
            src = list(card["a_issues"]) + [i for i in card["b_issues"]
                                            if i.get("field") not in
                                            {x.get("field") for x in card["a_issues"]}]
            confirm = {"a": card["a_reviewer"], "b": card["b_reviewer"]}
        elif cls in ("a_issue_only", "b_issue_only"):
            t = T.get(cid)
            src = (card["a_issues"] if cls == "a_issue_only" else card["b_issues"])
            side_fields = field_tokens(src)
            arb_fields = field_tokens((t or {}).get("issues", []))
            same_field = bool(t) and t.get("verdict") == "issue" and bool(side_fields & arb_fields)
            if same_field:
                chain = cls.split("_")[0].upper() + "+arbiter"
                status = "confirmed_fixed" if cid in F else "confirmed_not_fixed"
            else:
                chain = cls.split("_")[0].upper() + "+arbiter(pass)"
                status = "single_sided"
            confirm = {"a": card["a_reviewer"], "b": card["b_reviewer"],
                       "arbiter": (t or {}).get("reviewer"),
                       "arbiter_verdict": (t or {}).get("verdict"),
                       "arbiter_other_fields": sorted(arb_fields - side_fields)}
        elif cls == "both_pass":
            continue
        elif cls == "unverifiable":
            issues.append({
                "id": cid, "path": card["path"], "title": title.get(cid),
                "status": "unverifiable", "chain": "A/B",
                "a_verdict": card["a_verdict"], "b_verdict": card["b_verdict"],
                "a_unverifiable": card.get("a_unverifiable", []),
                "b_unverifiable": card.get("b_unverifiable", []),
            })
            continue
        else:
            continue
        for it in src:
            issues.append({
                "id": cid, "path": card["path"], "title": title.get(cid),
                "status": status, "chain": chain,
                "field": it.get("field"), "aspect": it.get("aspect"),
                "severity": it.get("severity"),
                "card_says": it.get("card_says"),
                "problem": it.get("problem"),
                "should_be": it.get("should_be"),
                "evidence": it.get("evidence"),
                "confirmed_by": confirm,
                "fixed_in_fix_log": cid in F,
            })

    with io.open(os.path.join(ROOT, "issues.jsonl"), "w",
                 encoding="utf-8", newline="\n") as fh:
        for it in issues:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    # ---- stats -------------------------------------------------------------
    def cnt(rows, key):
        d = {}
        for r in rows:
            d[r.get(key)] = d.get(r.get(key), 0) + 1
        return d

    a_rows = jsonl_dir("passA")
    b_rows = jsonl_dir("passB")
    t_rows = jsonl_dir("tiebreak")
    sev = {}
    for it in issues:
        if it["status"] in ("confirmed_fixed", "confirmed_not_fixed"):
            sev[it.get("severity")] = sev.get(it.get("severity"), 0) + 1
    stats = {
        "passA": {"rows": len(a_rows), "verdicts": cnt(a_rows, "verdict"),
                  "groups": cnt(a_rows, "group")},
        "passB": {"rows": len(b_rows), "verdicts": cnt(b_rows, "verdict"),
                  "groups": cnt(b_rows, "group")},
        "tiebreak": {"rows": len(t_rows), "verdicts": cnt(t_rows, "verdict"),
                     "groups": cnt(t_rows, "group")},
        "compare_counts": compare["counts"],
        "both_issue_field_agree": compare.get("both_issue_field_agree"),
        "both_issue_field_disagree": compare.get("both_issue_field_disagree"),
        "issues": {"rows": len(issues), "status": cnt(issues, "status"),
                   "severity": sev, "cards": len({i["id"] for i in issues})},
        "fixes": ({"cards": fixes.get("n_cards"), "edits": fixes.get("n_edits")}
                  if fixes else None),
        "a_issue_cards": sorted({r["id"] for r in a_rows if r.get("verdict") == "issue"}),
        "b_issue_cards": sorted({r["id"] for r in b_rows if r.get("verdict") == "issue"}),
    }
    with io.open(os.path.join(ROOT, "tmp", "stats.json"), "w",
                 encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(stats, ensure_ascii=False, indent=2) + "\n")

    # ---- append the arbiter / confirmation appendix to compare.md ----------
    cmp_md = os.path.join(ROOT, "compare.md")
    with io.open(cmp_md, encoding="utf-8") as fh:
        base = fh.read()
    marker = "\n## 第三名盲审仲裁（arbiter）\n"
    base = base.split(marker)[0].rstrip() + "\n"
    lines = [marker,
             "",
             "单方判 issue 的卡（%d 张）交第三名 arbiter 盲审；arbiter 同字段判 issue 才确认，"
             "判 pass 或只发现其它字段问题的保留为单方发现。\n" % len(t_rows),
             "| id | arbiter | 结论 | arbiter 认定字段 | A/B 认定字段 | 处理 |",
             "|---|---|---|---|---|---|"]
    cls = {c["id"]: c for c in compare["cards"]}
    for r in sorted(t_rows, key=lambda x: x["id"]):
        c = cls.get(r["id"], {})
        side_fields = "、".join(sorted({(i.get("field") or "") for i in
                                        (c.get("a_issues") or c.get("b_issues") or [])}))
        arb_fields = "、".join(sorted({(i.get("field") or "") for i in r.get("issues", [])}))
        handled = "确认并修复" if r["id"] in F and r.get("verdict") == "issue" \
            else ("单方未修" if r.get("verdict") != "issue" else "确认但未修")
        if r.get("verdict") == "issue" and r["id"] not in F:
            handled = "单方未修（arbiter 发现的是另一字段，A 的断言未被第二人认可）"
        lines.append("| `%s` | %s | %s | %s | %s | %s |"
                     % (r["id"].split("/")[-1], r.get("reviewer"), r.get("verdict"),
                        arb_fields or "—", side_fields or "—", handled))
    lines += ["",
              "## 最终确认\n",
              "| 状态 | 卡数 | 说明 |", "|---|---|---|",
              "| confirmed_fixed | %d | A+B 或 单方+arbiter 同字段确认，已按 fix_log 修复 |"
              % len({i["id"] for i in issues if i["status"] == "confirmed_fixed"}),
              "| single_sided | %d | 仅一方判 issue，另一判断未认可，不修 |"
              % len({i["id"] for i in issues if i["status"] == "single_sided"}),
              "| unverifiable | %d | 未能对 E1 来源核验 |"
              % len({i["id"] for i in issues if i["status"] == "unverifiable"}),
              ""]
    with io.open(cmp_md, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(base + "\n".join(lines))

    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
