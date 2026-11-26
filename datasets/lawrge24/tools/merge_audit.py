#!/usr/bin/env python3
"""Merge audit/track-*.jsonl verdicts into verification.jsonl.

Each audit row carries card_id (e.g. concepts/shearing), claim, verdict,
severity, sources[]. We keep the original source-alignment check and append
one check per audited claim, then set status "audited" for cards with rows.
Idempotent: previous audit-* checks are removed before merging.
"""
import glob, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = os.path.join(ROOT, "verification.jsonl")
AUDIT = os.path.join(ROOT, "audit")

rows = []
with open(VER, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))
by_id = {r["id"]: r for r in rows}

# strip previous audit checks
for r in rows:
    r["checks"] = [c for c in r.get("checks", []) if not c.get("kind") == "audit"]

counts = {}
for path in sorted(glob.glob(os.path.join(AUDIT, "track-*.jsonl"))):
    track = os.path.basename(path)[6:-6]
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            a = json.loads(line)
            cid = a["card_id"]
            if cid.startswith("lawrge/"):
                rid = cid.replace("lawrge/concepts/", "lawrge/concept/").replace(
                    "lawrge/derivations/", "lawrge/deriv/")
            else:
                typ, slug = cid.split("/", 1)
                typ = {"concepts": "concept", "derivations": "deriv"}.get(typ, typ)
                rid = f"lawrge/{typ}/{slug}"
            r = by_id.get(rid)
            if r is None:
                raise SystemExit(f"unknown card id in audit: {rid}")
            srcs = "; ".join(
                f'{s.get("name","?")} {s.get("locator","")}'.strip()
                for s in a.get("sources", [])
            )
            r.setdefault("checks", []).append({
                "kind": "audit",
                "track": track.upper(),
                "entry": f"{a.get('severity','?')} / {cid}",
                "asserts": a.get("claim", ""),
                "verdict": a.get("verdict", "unverifiable"),
                "sources": srcs,
                "last_revised": "2024-12-03",
            })
            counts.setdefault(rid, []).append(a.get("verdict", "unverifiable"))

AUDITED_STATUS = "audited"
for rid, verdicts in counts.items():
    r = by_id[rid]
    r["status"] = AUDITED_STATUS
    r["note"] = (
        f"原文对齐 + 外部核验：{len(verdicts)} 条断言，"
        f"supported {verdicts.count('supported')} / partially-supported {verdicts.count('partially-supported')}"
        f" / unverifiable {verdicts.count('unverifiable')} / conflict {verdicts.count('conflict')}。"
    )

with open(VER, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"verification.jsonl: {len(rows)} cards, {len(counts)} audited, "
      f"{sum(len(v) for v in counts.values())} claims")
