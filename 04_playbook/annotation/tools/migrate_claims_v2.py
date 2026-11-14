# -*- coding: utf-8 -*-
"""Migrate WIT-1989-JONES v1 claims.jsonl to claim v2.

只做加法：v1 字段原样保留，补 premises / mode / warrant / role / difficulty /
concept_hints / provenance / review。不删、不改 claim 正文与 anchors。

用法：
  python migrate_claims_v2.py <repo_root> [--out claims/wit_claims_v2.jsonl]
"""
import argparse
import glob
import json
import os
import sys

PAPER_ID = "WIT-1989-JONES"
SOURCE_MAP = {
    "witten": "paper",
    "reconstruction": "reconstruction",
    "post-1990": "external",
    "textbook": "external",
}


def migrate(rec):
    anchors = [a for a in (rec.get("anchors") or []) if str(a).strip()]
    legacy_source = rec.get("source", "")
    out = {
        "id": rec["id"],
        "paper_id": PAPER_ID,
        "session": rec.get("session", ""),
        "claim": rec["claim"],
        "type": rec.get("type", "evidence"),
        "anchors": anchors,
        "provenance": {
            "source": SOURCE_MAP.get(legacy_source, "external"),
            "doc": PAPER_ID,
            "locator": anchors[0] if anchors else "",
        },
        "legacy_source": legacy_source,
        "premises": [],
        "mode": None,
        "warrant": None,
        "role": None,
        "difficulty": None,
        "concept_hints": [],
        "confidence": rec.get("confidence", "medium"),
        "status": rec.get("status", "active"),
        "counterpoints": rec.get("counterpoints", []),
        "review": {
            "status": "accepted" if rec.get("status") == "accepted" else "proposed",
            "reviewers": [],
            "note": "v1→v2 迁移；premises/warrant/role 待人工或 LLM 补",
        },
    }
    if not anchors:
        out["review"]["status"] = "needs_review"
        out["review"]["note"] += "；无锚点，必须降级"
    if rec.get("status") == "contested":
        out["review"]["status"] = "needs_review"
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo_root")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    root = os.path.abspath(args.repo_root)
    pattern = os.path.join(root, "papers", PAPER_ID, "sessions", "s*", "claims.jsonl")
    files = sorted(glob.glob(pattern))
    if not files:
        print(f"no claims.jsonl under {pattern}")
        return 2

    out_path = args.out or os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "claims", "wit_claims_v2.jsonl")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    rows, ids, no_anchor = [], set(), 0
    for f in files:
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if rec["id"] in ids:
                raise SystemExit(f"duplicate id {rec['id']} in {f}")
            ids.add(rec["id"])
            row = migrate(rec)
            rows.append(row)
            if not row["anchors"]:
                no_anchor += 1

    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(json.dumps({
        "input_files": len(files),
        "claims": len(rows),
        "with_anchors": len(rows) - no_anchor,
        "no_anchor": no_anchor,
        "out": out_path,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
