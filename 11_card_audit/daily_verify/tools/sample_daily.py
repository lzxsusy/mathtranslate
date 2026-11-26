#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日核验抽样器：确定性地从全库资料卡中抽 n 张。

用法:
  python 11_card_audit/daily_verify/tools/sample_daily.py --n 20
  python 11_card_audit/daily_verify/tools/sample_daily.py --date 2026-11-27 --set glc --set benzvi_glc

规则:
  - 只收 datasets/*/cards/**/*.json 中同时有 id 与 type 的对象，排除 work.json；
  - 365 天内已核过的 id 优先排除；候选不足时按「最久未核」补足；
  - 同一天、同一参数重跑结果一致（seed = 日期）。
输出:
  11_card_audit/daily_verify/<date>/sample.json
"""
import argparse
import datetime as dt
import glob
import hashlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DAILY = os.path.join(ROOT, "11_card_audit", "daily_verify")
LEDGER = os.path.join(DAILY, "ledger.jsonl")
RECENT_DAYS = 365


def read_ledger(path):
    last = {}
    if not os.path.exists(path):
        return last
    with io.open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except Exception:
                continue
            cid, d = row.get("id"), row.get("date")
            if cid and d:
                if cid not in last or d > last[cid]:
                    last[cid] = d
    return last


def discover(sets):
    out = []
    pattern = os.path.join(ROOT, "datasets", "*", "cards", "**", "*.json")
    for p in glob.glob(pattern, recursive=True):
        name = os.path.basename(p)
        if name in ("work.json", "index.json"):
            continue
        try:
            with io.open(p, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            continue
        if not isinstance(d, dict) or "id" not in d or "type" not in d:
            continue
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        setname = rel.split("/")[1]
        if sets and setname not in sets:
            continue
        srcs = d.get("sources") or []
        out.append({
            "id": d["id"],
            "path": rel,
            "set": setname,
            "type": d.get("type"),
            "status": d.get("status"),
            "title": d.get("title"),
            "n_sources": len(srcs) if isinstance(srcs, list) else 0,
            "sources": [
                {k: s.get(k) for k in ("text", "book", "section", "pages", "pdf_pages", "anchor", "quote") if k in s}
                for s in (srcs if isinstance(srcs, list) else [])
            ],
        })
    return out


def h(date, cid):
    return hashlib.sha256((date + "|" + cid).encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--set", action="append", default=None)
    ap.add_argument("--include-recent", action="store_true")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    cards = discover(set(args.set) if args.set else None)
    if not cards:
        print("ERROR: no cards found", file=sys.stderr)
        return 2

    last = read_ledger(LEDGER)
    try:
        today = dt.date.fromisoformat(args.date)
    except ValueError:
        print("ERROR: --date must be YYYY-MM-DD", file=sys.stderr)
        return 2
    cutoff = (today - dt.timedelta(days=RECENT_DAYS)).isoformat()

    def is_recent(c):
        d = last.get(c["id"])
        return bool(d and d >= cutoff)

    pool = [c for c in cards if args.include_recent or not is_recent(c)]
    pool.sort(key=lambda c: h(args.date, c["id"]))
    picked = pool[: args.n]
    if len(picked) < args.n:
        rest = [c for c in cards if is_recent(c) and c not in picked]
        rest.sort(key=lambda c: (last.get(c["id"], ""), h(args.date, c["id"])))
        picked += rest[: args.n - len(picked)]

    # 排序：先有 sources 的卡（更可核），同组内保持确定性顺序
    picked.sort(key=lambda c: (0 if c["n_sources"] else 1, h(args.date, c["id"])))

    out_dir = args.out_dir or os.path.join(DAILY, args.date)
    os.makedirs(out_dir, exist_ok=True)
    payload = {
        "date": args.date,
        "seed": args.date,
        "n": len(picked),
        "library_total": len(cards),
        "ledger_ids": len(last),
        "recent_cutoff": cutoff,
        "sets": {},
        "items": picked,
    }
    for c in picked:
        payload["sets"][c["set"]] = payload["sets"].get(c["set"], 0) + 1
    out = os.path.join(out_dir, "sample.json")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    print("date=%s n=%d pool=%d library=%d ledger=%d" % (args.date, len(picked), len(pool), len(cards), len(last)))
    print("sets:", json.dumps(payload["sets"], ensure_ascii=False))
    for c in picked:
        print("%-42s %-14s src=%d %s" % (c["id"], c["set"], c["n_sources"], c["path"]))
    print("WROTE", os.path.relpath(out, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
