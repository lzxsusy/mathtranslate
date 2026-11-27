#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-27 第二轮（独立复核）修卡。

在 apply_fixes.py 的 23 处字段编辑之外，本轮复核又确认两处：
  1. sy0238 key_points[1]：Weil 猜想的完成者写成「Lai–Künnemann」，史实错误；
  2. ggl09 steps[4].locator：边界讨论实际在 p.17，locator 只写到 p.16。

复用 apply_fixes.py 的无损格式与 before 断言；写盘后把改动追加进 fix_log.json。
"""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_fixes import DELETED, LOG, ROOT, fmt, get, load, put  # noqa: E402

EDITS = [
    dict(
        path="datasets/sy0238/cards/concepts/tamagawa-number.json",
        field=["key_points", 1],
        before="$\\tau(\\mathrm{SL}_n)=1$ 属于 Weil 猜想的一类情形（Langlands 证 $\\mathrm{SL}_2$，一般情形后来由 Lai–Kunnemann 等完成）；原文只引 [Col11, Appendix B] 与 [Lur, Lecture 1]。",
        after="$\\tau(\\mathrm{SL}_n)=1$ 是 Weil 猜想（单连通半单群的 Tamagawa 数=1）的特例：Langlands 证分裂情形，Rapoport 与 Lai 推广到拟分裂情形，Kottwitz（1988）用 Arthur 迹公式完成数域一般情形；原文只引 [Col11, Appendix B] 与 [Lur, Lecture 1]。",
        why="史实归属错误：Weil 猜想数域情形由 Langlands（分裂）→ Rapoport/Lai（拟分裂）→ Kottwitz 1988（一般）完成，没有「Lai–Künnemann」这一完成链。",
    ),
    dict(
        path="datasets/ggl09/cards/derivations/descent-to-xi.json",
        field=["steps", 4, "locator"],
        before="A p.16 eq (2.10)",
        after="A p.16–17 eq (2.10)",
        why="该步后半（左/右边界、同调于小 S²）在 p.17；locator 只到 p.16，与已改写的 step text 不匹配。",
    ),
]


def main() -> int:
    by_file: dict[str, list[dict]] = {}
    for e in EDITS:
        by_file.setdefault(e["path"], []).append(e)

    pending = []
    for rel, items in by_file.items():
        path = ROOT / rel
        raw, data = load(path)
        assert fmt(raw, data) == raw, f"格式无法无损往返：{rel}"
        changes = []
        for e in items:
            cur = get(data, e["field"])
            assert cur == e["before"], f"before 不匹配：{rel} {e['field']}\n  got={cur!r}"
            put(data, e["field"], e["after"])
            changes.append({"field": e["field"], "before": e["before"], "after": e["after"], "why": e["why"]})
        pending.append((rel, path, fmt(raw, data), items, changes, data["id"]))

    if "--dry-run" in sys.argv:
        print(f"DRY-RUN OK: {len(pending)} files, {len(EDITS)} changes")
        return 0

    for rel, path, out, items, changes, _id in pending:
        io.open(path, "w", encoding="utf-8", newline="").write(out)
        _, again = load(path)
        for e in items:
            assert get(again, e["field"]) == e["after"], f"after 回读失败：{rel} {e['field']}"

    log = json.loads(io.open(LOG, encoding="utf-8").read())
    by_path = {e["path"]: e for e in log}
    for rel, _path, _out, _items, changes, cid in pending:
        if rel in by_path:
            have = {tuple(c["field"]): c for c in by_path[rel]["changes"]}
            for c in changes:
                have[tuple(c["field"])] = c
            by_path[rel]["changes"] = list(have.values())
        else:
            log.append({"id": cid, "path": rel, "changes": changes})
    order = {p: i for i, p in enumerate(dict.fromkeys([e["path"] for e in json.loads(io.open(LOG, encoding="utf-8").read())] + [p[0] for p in pending]))}
    log.sort(key=lambda e: order[e["path"]])
    io.open(LOG, "w", encoding="utf-8", newline="\n").write(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
    print(f"OK: {len(pending)} files, {len(EDITS)} changes; fix_log 现 {len(log)} 张卡 / {sum(len(e['changes']) for e in log)} 处")
    return 0


if __name__ == "__main__":
    sys.exit(main())
