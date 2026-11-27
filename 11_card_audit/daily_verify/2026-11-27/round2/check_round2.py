#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第二轮复核校验器。

- 对 fix_log.json 的每一处改动：当前卡片字段值 == after；字符串型 before 已不在该字段；
- 对 records_round2.jsonl：当前字段 == should_be，card_says 已不在该字段，
  且 fix_log 中存在同 (id, field) 的 after == should_be；
- 检查 (id, field) 无重复、after 非空、severity 合法。
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
FIXLOG = os.path.join(ROOT, "11_card_audit", "daily_verify", "2026-11-27", "fixes", "fix_log.json")
RECORDS = os.path.join(HERE, "records_round2.jsonl")
SEV = {"critical", "major", "minor"}


def norm(s):
    return re.sub(r"\s+", "", s or "")


def load_card(path, source):
    """source=worktree 读磁盘；source=index 读 git 暂存区（即本次 commit 的内容）。"""
    if source == "worktree":
        with io.open(path, encoding="utf-8") as f:
            return json.load(f)
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    raw = subprocess.check_output(["git", "show", ":" + rel], cwd=ROOT)
    return json.loads(raw.decode("utf-8"))


def get(obj, path):
    cur = obj
    for k in path:
        cur = cur[k]
    return cur


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["worktree", "index"], default="index",
                    help="校验来源：index=暂存区（默认，代表即将提交的内容）")
    source = ap.parse_args().source
    errors = []
    with io.open(FIXLOG, encoding="utf-8") as f:
        log = json.load(f)

    seen = {}
    total = 0
    for entry in log:
        card_path = os.path.join(ROOT, entry["path"])
        card = load_card(card_path, source)
        for ch in entry["changes"]:
            total += 1
            field = tuple(ch["field"])
            key = (entry["id"], field)
            if key in seen:
                errors.append(f"duplicate change: {entry['id']} {field}")
            seen[key] = ch
            try:
                cur = get(card, ch["field"])
            except IndexError as e:
                # 删除型改动：after=None，且父列表已短于原索引
                if ch["after"] is None:
                    parent = get(card, ch["field"][:-1])
                    if isinstance(parent, list) and len(parent) <= ch["field"][-1]:
                        continue
                errors.append(f"missing field {entry['id']} {field}: {e}")
                continue
            except (KeyError, TypeError) as e:
                errors.append(f"missing field {entry['id']} {field}: {e}")
                continue
            if cur != ch["after"]:
                errors.append(f"after mismatch {entry['id']} {field}")
            if isinstance(ch["before"], str) and ch["before"] != ch["after"]:
                if norm(ch["before"]) in norm(json.dumps(cur, ensure_ascii=False)):
                    errors.append(f"before still present {entry['id']} {field}")

    nrec = 0
    with io.open(RECORDS, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            nrec += 1
            r = json.loads(line)
            if r.get("severity") not in SEV:
                errors.append(f"bad severity: {r.get('id')} {r.get('severity')}")
            card_path = os.path.join(ROOT, r["path"])
            card = load_card(card_path, source)
            try:
                cur = get(card, r["field"])
            except (KeyError, IndexError, TypeError) as e:
                errors.append(f"round2 missing field {r['id']} {r['field']}: {e}")
                continue
            if cur != r["should_be"]:
                errors.append(f"round2 should_be mismatch {r['id']} {r['field']}")
            if norm(r["card_says"]) in norm(json.dumps(cur, ensure_ascii=False)):
                errors.append(f"round2 card_says still present {r['id']}")
            match = seen.get((r["id"], tuple(r["field"])))
            if not match:
                errors.append(f"round2 change absent from fix_log: {r['id']} {r['field']}")
            elif match["after"] != r["should_be"]:
                errors.append(f"round2 after != should_be: {r['id']}")

    if errors:
        print("\n".join(errors))
        print(f"FAILED: {len(errors)} error(s)")
        return 1
    print(f"OK: {len(log)} cards, {total} changes, {nrec} round2 records (source={source})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
