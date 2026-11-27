#!/usr/bin/env python3
"""check_survey.py — 综述页链接/引文/卡片一致性检查（survey v1.0 专用）。

用法：
    python datasets/encyclopedia/pages/work/survey-v1/check_survey.py [页面.md]

检查项：
  1. 每个 `{{card:ID}}` 都能在 datasets/*/cards/**/*.json 中找到；
  2. 每个 `{{entry:ID}}` 都能在 datasets/encyclopedia/entries/ 中找到；
  3. 每个仓库内相对 Markdown 链接指向的文件真实存在（忽略 #锚点）；
  4. front-matter `compiled_from` 的 id 存在且 hash = sha256(文件) 前 16 位；
  5. 统计 `〔...〕` 出处标记数与 `{{card:}}` 数，报告覆盖密度。
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import urllib.parse
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]  # .../gitee_shuyi
PAGE = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "datasets/encyclopedia/pages/geometric-langlands.md"

CARD_RE = re.compile(r"\{\{card:([^}]+)\}\}")
ENTRY_RE = re.compile(r"\{\{entry:([^}]+)\}\}")
LINK_RE = re.compile(r"\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)\s*\)")
CITE_RE = re.compile(r"〔[^〕]+〕")


def card_paths() -> dict[str, Path]:
    idx: dict[str, Path] = {}
    for f in (REPO / "datasets").glob("*/cards/**/*.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        cid = d.get("id")
        if cid:
            idx[cid] = f
    return idx


def front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    raw = text[3:end]
    body = text[end + 4 :]
    # 只解析 compiled_from 需要的两项；不依赖 PyYAML。
    return {"raw": raw}, body


def parse_compiled(raw: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    cur = None
    for line in raw.splitlines():
        m = re.match(r"\s*-\s*id:\s*(.+?)\s*$", line)
        if m:
            cur = m.group(1)
            continue
        m = re.match(r"\s*hash:\s*([0-9a-f]+)\s*$", line)
        if m and cur:
            out.append((cur, m.group(1)))
            cur = None
    return out


def main() -> int:
    text = PAGE.read_text(encoding="utf-8")
    fm, body = front_matter(text)
    errors: list[str] = []

    cards = card_paths()
    used_cards = CARD_RE.findall(body)
    missing_cards = sorted({c for c in used_cards if c not in cards})
    for c in missing_cards:
        errors.append(f"missing card: {c}")

    entries_dir = REPO / "datasets/encyclopedia/entries"
    used_entries = ENTRY_RE.findall(body)
    missing_entries = sorted({e for e in used_entries if not (entries_dir / f"{e}.json").exists()})
    for e in missing_entries:
        errors.append(f"missing entry: {e}")

    checked_links = 0
    for m in LINK_RE.finditer(body):
        target = m.group(1)
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if re.match(r"^(https?:|mailto:|#|data:)", target):
            continue
        target = urllib.parse.unquote(target.split("#", 1)[0])
        if not target:
            continue
        p = (PAGE.parent / target).resolve()
        checked_links += 1
        if not p.exists():
            errors.append(f"dead link: {target} -> {p}")

    compiled = parse_compiled(fm.get("raw", ""))
    for cid, h in compiled:
        p = cards.get(cid)
        if not p:
            errors.append(f"compiled_from unknown card: {cid}")
            continue
        real = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        if real != h:
            errors.append(f"compiled_from hash mismatch: {cid} {h} != {real}")

    cites = len(CITE_RE.findall(body))
    print(f"page: {PAGE}")
    print(f"cards: {len(set(used_cards))} unique / {len(used_cards)} refs; missing {len(missing_cards)}")
    print(f"entries: {len(set(used_entries))} unique; missing {len(missing_entries)}")
    print(f"local links checked: {checked_links}; dead {sum(1 for e in errors if e.startswith('dead link'))}")
    print(f"citation markers 〔…〕: {cites}")
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(" -", e)
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
