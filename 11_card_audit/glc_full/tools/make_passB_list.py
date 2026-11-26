#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build the blind Pass B list from Pass A results.

Rules (user spec):
  * every card A marked `issue`  -> must be re-audited in Pass B
  * a random 20% sample of cards A marked `pass` -> also re-audited (seeded, reproducible)
  * B reviewers get ONLY the card paths, never A's verdict.

Outputs:
  passB_list.json          machine record (seed, counts, per-card origin)
  passB/groups/B<n>.txt    one path per line, shuffled, fixed order = JSONL n order
  passB/manifest.json      group -> [ {n,id,path,origin} ]
"""
import argparse
import json
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
REPO = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))


def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20261126)
    ap.add_argument("--frac", type=float, default=0.2)
    ap.add_argument("--per-group", type=int, default=20)
    args = ap.parse_args()

    a_dir = os.path.join(ROOT, "passA")
    rows = []
    for fn in sorted(os.listdir(a_dir)):
        if fn.endswith(".jsonl"):
            rows.extend(load_jsonl(os.path.join(a_dir, fn)))
    by_id = {}
    for r in rows:
        by_id.setdefault(r["id"], []).append(r)
    dup = {k: len(v) for k, v in by_id.items() if len(v) > 1}
    if dup:
        raise SystemExit("duplicate ids across passA: %r" % dup)

    issues = [r for r in rows if r.get("verdict") == "issue"]
    passes = [r for r in rows if r.get("verdict") == "pass"]
    unver = [r for r in rows if r.get("verdict") not in ("issue", "pass")]
    if unver:
        print("WARN: %d rows with verdict outside {issue,pass}: %s"
              % (len(unver), [r["id"] for r in unver]))

    # deterministic sample of A-pass cards
    pool = sorted(r["id"] for r in passes)
    rng = random.Random(args.seed)
    k = int(round(args.frac * len(pool)))
    sampled = sorted(rng.sample(pool, k))

    origin = {}
    for r in issues:
        origin[r["id"]] = "a_issue"
    for cid in sampled:
        origin[cid] = "a_pass_sample"

    path_of = {r["id"]: r["path"] for r in rows}
    cards = sorted(origin.items())
    rng2 = random.Random(args.seed + 1)
    rng2.shuffle(cards)

    ngroups = max(1, int(math.ceil(len(cards) / float(args.per_group))))
    groups = [[] for _ in range(ngroups)]
    for i, (cid, org) in enumerate(cards):
        groups[i % ngroups].append((cid, org))

    out_dir = os.path.join(ROOT, "passB")
    grp_dir = os.path.join(out_dir, "groups")
    os.makedirs(grp_dir, exist_ok=True)
    manifest = {}
    for gi, g in enumerate(groups, 1):
        gname = "B%d" % gi
        with open(os.path.join(grp_dir, gname + ".txt"), "w", encoding="utf-8") as f:
            for cid, _ in g:
                f.write(path_of[cid] + "\n")
        manifest[gname] = [
            {"n": i + 1, "id": cid, "path": path_of[cid], "origin": org}
            for i, (cid, org) in enumerate(g)
        ]

    summary = {
        "seed": args.seed,
        "frac": args.frac,
        "passA_rows": len(rows),
        "passA_issue": len(issues),
        "passA_pass": len(passes),
        "passA_other": len(unver),
        "sample_size": k,
        "total_b_cards": len(cards),
        "groups": {g: len(v) for g, v in manifest.items()},
        "origin_counts": {
            "a_issue": len(issues),
            "a_pass_sample": k,
        },
        "note": "B reviewers must NOT see A verdicts; they get only passB/groups/B<n>.txt",
    }
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "groups": manifest}, f,
                  ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(ROOT, "passB_list.json"), "w", encoding="utf-8") as f:
        json.dump({
            "summary": summary,
            "a_issue_ids": sorted(r["id"] for r in issues),
            "a_pass_sampled_ids": sampled,
            "a_unverifiable_ids": sorted(r["id"] for r in unver),
        }, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
