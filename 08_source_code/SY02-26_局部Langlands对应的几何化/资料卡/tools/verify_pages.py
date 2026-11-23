#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_pages.py —— 把卡片里的「出处」拿回原文逐条核对。

原理：每张卡的每条 `sources` 都带一段 `quote`（≤120 字符的英文原句）。本工具在
`txt/<NN>/p*.txt` 里搜这段引文，回报它**实际**出现在第几页，与卡片写的 `pages` 对照。

用法：
    python tools/verify_pages.py out/19_ggl19                 # 只报告
    python tools/verify_pages.py out/19_ggl19 --strict        # 有错就退出 1
    python tools/verify_pages.py out/19_ggl19 --write         # 把错页直接改对（保守：只改 pages）

为什么必须做：页码/式号写错，卡片在语料里就变成了「查不到出处」的断言；
推理再对也没法追溯。这件事人眼容易漏，机器一搜就现形。
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DATA = Path(__file__).resolve().parent.parent

LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi",
       "\ufb04": "ffl", "\ufb05": "ft", "\ufb06": "st"}


def norm(s: str) -> str:
    s = "".join(LIG.get(c, c) for c in s).lower()
    return re.sub(r"[^a-z0-9]+", "", s)


def load_pages(txtdir: Path):
    pages = {}
    for p in sorted(txtdir.glob("p*.txt")):
        m = re.search(r"p(\d+)", p.stem)
        if m:
            pages[int(m.group(1))] = norm(p.read_text(encoding="utf-8", errors="replace"))
    return pages


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pkg")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--max-pages", type=int, default=0)
    a = ap.parse_args()

    pkg = Path(a.pkg)
    if not pkg.is_absolute():
        pkg = Path.cwd() / pkg
    no = int(pkg.name.split("_")[0])
    txtdir = DATA / "txt" / f"{no:02d}"
    if not txtdir.is_dir():
        print(f"[error] 缺 {txtdir}，先跑 tools/extract.py {no}")
        return 1
    pages = load_pages(txtdir)
    files = sorted((pkg / "cards").glob("*/*.json"))
    if not files:
        print("[error] 没有卡片")
        return 1

    bad = 0
    nchk = nskip = 0
    rows = []
    for f in files:
        card = json.loads(f.read_text(encoding="utf-8"))
        changed = False
        for i, s in enumerate(card.get("sources") or []):
            if s.get("text") != "A":
                nskip += 1
                continue
            q = (s.get("quote") or "").strip()
            if len(q) < 12:
                rows.append((f.name, i, "缺 quote", "", ""))
                bad += 1
                continue
            if len(q) > 120:
                rows.append((f.name, i, f"quote 超 120 字符（{len(q)}）", "", ""))
                bad += 1
            nq = norm(q)
            hits = [p for p, t in pages.items() if nq and nq in t]
            nchk += 1
            pages_s = s.get("pages") or [0, 0]
            lo, hi = int(pages_s[0]), int(pages_s[1])
            if not hits:
                rows.append((f.name, i, "原文里搜不到这段 quote", f"{lo}–{hi}", "—"))
                bad += 1
            elif any(lo <= h <= hi for h in hits):
                continue  # 对上了
            else:
                real = hits[0]
                rows.append((f.name, i, "页码不符", f"{lo}–{hi}", f"实际 p.{real}"))
                bad += 1
                if a.write:
                    s["pages"] = [real, real]
                    an = s.get("anchor", "")
                    s["anchor"] = re.sub(r"\bp\.\d+", f"p.{real}", an)
                    changed = True
        if changed:
            f.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for name, i, kind, claimed, real in rows:
        print(f"[FAIL] {name} sources[{i}] {kind}：卡片写 {claimed}　{real}")
    print(f"[done] 核对 {nchk} 条（跳过非 A 来源 {nskip} 条），问题 {bad} 条")
    return 1 if (bad and a.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
