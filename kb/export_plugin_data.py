#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 kb/cards + kb/cards5 合并去重，导出成插件自带的 data/cards/*.jsonl。

插件（dsh-kb）用的是纯 JS 引擎，直接吃 jsonl；这里保证：
  · 同一 id 只保留一份（优先 verified > checked > draft）
  · 按 work 分文件，方便增量比对
  · 输出 = 插件目录下 data/cards/

用法：
    python kb/export_plugin_data.py                 # 导出到 ../../dsh-kb/data/cards
    python kb/export_plugin_data.py --out <dir>
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

KB = Path(__file__).resolve().parent
REPO = KB.parent
DEFAULT_OUT = REPO.parent / "dsh-kb" / "data" / "cards"
RANK = {"verified": 3, "checked": 2, "disputed": 1, "draft": 0}


def load_all() -> dict[str, dict]:
    best: dict[str, dict] = {}
    for sub in ("cards", "cards5"):
        for p in sorted((KB / sub).glob("*.jsonl")):
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    c = json.loads(line)
                except json.JSONDecodeError:
                    continue
                cid = c.get("id")
                if not cid:
                    continue
                cur = best.get(cid)
                if cur is None or RANK.get(c.get("status"), 0) > RANK.get(cur.get("status"), 0):
                    best[cid] = c
    return best


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args()
    out = Path(a.out)
    cards = load_all()
    if not cards:
        raise SystemExit("kb/cards 与 kb/cards5 都是空的，先跑 ingest.py / ingest_gen2.py")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)
    by_work: dict[str, list[dict]] = {}
    for c in cards.values():
        by_work.setdefault(str(c.get("work") or "UNKNOWN"), []).append(c)
    for work, items in by_work.items():
        items.sort(key=lambda c: (c.get("kind", ""), c.get("id", "")))
        with (out / f"{work}.jsonl").open("w", encoding="utf-8") as fh:
            for c in items:
                fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    total = sum(len(v) for v in by_work.values())
    print(f"导出 {total} 张卡 / {len(by_work)} 个作品 → {out}")
    st: dict[str, int] = {}
    kd: dict[str, int] = {}
    for c in cards.values():
        st[c.get("status", "?")] = st.get(c.get("status", "?"), 0) + 1
        kd[c.get("kind", "?")] = kd.get(c.get("kind", "?"), 0) + 1
    print("  status:", ", ".join(f"{k} {v}" for k, v in sorted(st.items(), key=lambda x: -x[1])))
    print("  kind  :", ", ".join(f"{k} {v}" for k, v in sorted(kd.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
