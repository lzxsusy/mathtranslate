#!/usr/bin/env python3
"""G0 闸门：开工前必须读过当前版本的 MEMORANDUM-01。

用法：
    python tools/check_memo_gate.py --role r01
    python tools/check_memo_gate.py --role r01 --record      # 读完后登记回执
    python tools/check_memo_gate.py --role r01 --max-age-days 7

退出码：0 = 通过；1 = 不通过（按提示补回执后重试）。
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MEMO = ROOT / "MEMORANDUM_01_论证精读与语料生产.md"
RECEIPTS = ROOT / "_meta" / "read_receipts.jsonl"


def sha16(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def load_receipts() -> list:
    if not RECEIPTS.exists():
        return []
    out = []
    for line in RECEIPTS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def record(role: str, memo_sha: str, memo_path: Path) -> None:
    RECEIPTS.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "role": role,
        "date": now_iso(),
        "memo": memo_path.name,
        "memo_sha256_16": memo_sha,
    }
    with RECEIPTS.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print("OK  receipt recorded: " + json.dumps(row, ensure_ascii=True))


def main() -> int:
    ap = argparse.ArgumentParser(description="MEMORANDUM-01 开工闸门")
    ap.add_argument("--role", required=True, help="角色 id，如 r01 / teacher / student-a")
    ap.add_argument("--memo", default=str(DEFAULT_MEMO))
    ap.add_argument("--max-age-days", type=float, default=7.0,
                    help="回执有效期（天），默认 7")
    ap.add_argument("--record", action="store_true",
                    help="读完并确认后登记一条回执（不会自动通过本闸门）")
    args = ap.parse_args()

    memo = Path(args.memo)
    if not memo.exists():
        print("FAIL memo not found: " + str(memo))
        return 1
    cur = sha16(memo)

    if args.record:
        record(args.role, cur, memo)
        if RECEIPTS.exists():
            print("NOTE: a receipt only records that you claim to have read it.")
        return 0

    receipts = [r for r in load_receipts() if r.get("role") == args.role]
    if not receipts:
        print("FAIL no read receipt for role " + args.role)
        print("  1) read the memo: " + str(memo))
        print("  2) then run: python tools/check_memo_gate.py --role " + args.role + " --record")
        return 1

    stale_sha = [r for r in receipts if r.get("memo_sha256_16") != cur]
    fresh = [r for r in receipts
             if r.get("memo_sha256_16") == cur and r.get("date")]
    if not fresh:
        print("FAIL memo changed; old receipts are void. Re-read the current version.")
        print("  current sha16 = " + cur)
        if stale_sha:
            print("  last stale receipt: " + str(stale_sha[-1].get("date")) + " sha16=" + str(stale_sha[-1].get("memo_sha256_16")))
        print("  then run: python tools/check_memo_gate.py --role " + args.role + " --record")
        return 1

    newest = max(fresh, key=lambda r: r.get("date", ""))
    try:
        ts = datetime.fromisoformat(newest["date"])
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        age_days = (datetime.now(timezone.utc) - ts.astimezone(timezone.utc)).total_seconds() / 86400
    except ValueError:
        age_days = float("inf")

    if age_days > args.max_age_days:
        print("FAIL receipt expired: %.1f days > %g days." % (age_days, args.max_age_days))
        print("  then run: python tools/check_memo_gate.py --role " + args.role + " --record")
        return 1

    print("OK  role=%s receipt=%s (%.1f days ago) sha16=%s" % (args.role, newest["date"], age_days, cur))
    print("  read: " + memo.name + " ; keep following its section 8 red lines.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
