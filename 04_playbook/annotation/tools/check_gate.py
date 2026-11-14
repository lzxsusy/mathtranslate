# -*- coding: utf-8 -*-
"""G2.5 论证精读闸门（确定性检查，零 LLM）。

判据（可调常量见下）：
  1. validate_annotations.py 对 examples/ 返回 PASS
  2. units >= 5（同一篇）
  3. 带 evidence.quote 的 inferences >= 3
  4. chain >= 1
  5. claims >= 50，且每条 anchors 非空、id 唯一

用法：python check_gate.py [annotation_dir]
退出码 0 = PASS，1 = FAIL。
"""
import glob
import json
import os
import subprocess
import sys

MIN_UNITS = 5
MIN_EVIDENCED_INFERENCES = 3
MIN_CHAINS = 1
MIN_CLAIMS = 50
ALLOWED_CLAIM_TYPES = {"evidence", "interpretation", "definition", "open",
                       "conjecture", "method", "result"}
ALLOWED_REVIEW = {"proposed", "accepted", "rejected", "needs_review", "unresolved"}


def load_jsonl(path):
    out = []
    if not os.path.exists(path):
        return out
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except Exception as e:
                out.append({"_parse_error": f"{os.path.basename(path)}:{i} {e}"})
    return out


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1
                           else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    ex = os.path.join(root, "examples")
    problems = []

    # 1) schema / cross-reference validator
    vpath = os.path.join(root, "tools", "validate_annotations.py")
    proc = subprocess.run([sys.executable, vpath, ex], capture_output=True, text=True, encoding="utf-8")
    print(proc.stdout.strip())
    if proc.returncode != 0:
        problems.append(f"validate_annotations FAIL (rc={proc.returncode})")

    units = [u for u in load_jsonl(os.path.join(ex, "units.jsonl")) if "_parse_error" not in u]
    infs = [x for x in load_jsonl(os.path.join(ex, "inferences.jsonl")) if "_parse_error" not in x]
    chain_path = os.path.join(ex, "chain.json")
    chains = []
    if os.path.exists(chain_path):
        try:
            chains = [json.load(open(chain_path, encoding="utf-8"))]
        except Exception as e:
            problems.append(f"chain.json invalid: {e}")
    concepts = [k for k in load_jsonl(os.path.join(ex, "concepts.jsonl")) if "_parse_error" not in k]
    evidenced = [x for x in infs if len((x.get("evidence") or {}).get("quote", "")) >= 8]

    if len(units) < MIN_UNITS:
        problems.append(f"units {len(units)} < {MIN_UNITS}")
    if len(evidenced) < MIN_EVIDENCED_INFERENCES:
        problems.append(f"evidenced inferences {len(evidenced)} < {MIN_EVIDENCED_INFERENCES}")
    if len(chains) < MIN_CHAINS:
        problems.append(f"chains {len(chains)} < {MIN_CHAINS}")

    claim_rows, claim_ids, bad_claims = 0, set(), []
    claim_files = sorted(glob.glob(os.path.join(root, "claims", "*.jsonl")))
    for f in claim_files:
        for i, c in enumerate(load_jsonl(f), 1):
            claim_rows += 1
            cid = c.get("id")
            if not cid or cid in claim_ids:
                bad_claims.append(f"{os.path.basename(f)}:{i} bad/duplicate id")
            claim_ids.add(cid)
            if not c.get("anchors"):
                bad_claims.append(f"{cid} no anchors")
            if c.get("type") not in ALLOWED_CLAIM_TYPES:
                bad_claims.append(f"{cid} bad type {c.get('type')}")
            if (c.get("review") or {}).get("status") not in ALLOWED_REVIEW:
                bad_claims.append(f"{cid} bad review.status")
    if claim_rows < MIN_CLAIMS:
        problems.append(f"claims {claim_rows} < {MIN_CLAIMS}")
    problems.extend(bad_claims)

    print()
    print("G2.5 闸门")
    print(f"  units                    {len(units):>4}  (>= {MIN_UNITS})")
    print(f"  inferences w/ evidence   {len(evidenced):>4}  (>= {MIN_EVIDENCED_INFERENCES})")
    print(f"  chains                   {len(chains):>4}  (>= {MIN_CHAINS})")
    print(f"  concepts                 {len(concepts):>4}")
    print(f"  claims                   {claim_rows:>4}  (>= {MIN_CLAIMS}), files {len(claim_files)}")
    if problems:
        print("\nFAIL")
        for p in problems[:20]:
            print("  -", p)
        return 1
    print("\nPASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
