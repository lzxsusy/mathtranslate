#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lint_cards.py —— GGL 资料卡质检（gtgl15/kw06 规则的参数化版）。

用法：
    python tools/lint_cards.py out/03_ggl03/cards
    python tools/lint_cards.py out/03_ggl03/cards --max-pages 90 --allow-missing --strict

前缀自动取包目录名（`03_ggl03` → `ggl03`，`ggl03` → `ggl03`）。
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TRACKS = {"A", "B", "C", "D", "E", "O"}
STATUS = {"draft", "dev"}
DOCS = {"A", "B", "C", "D"}
ANCHOR_RE = re.compile(r"^[A-D] p\.\d+(\s*[–-]\s*\d+)?(.*)$")
ABS_RE = re.compile(r"(?:[A-Za-z]:[\\/]+(?:Users|admin|Downloads|Desktop)|/c/Users|file:///)")


def text_len(s):
    s = re.sub(r"\$[^$]*\$", "", s or "")
    return len(re.sub(r"\s+", "", s))


def check_card(path: Path, card: dict, ids: set, prefix: str, max_pages: int, allow_missing: bool):
    e = []
    kind = "concepts" if "concepts" in path.parts else "derivations"
    cid = card.get("id", "")
    m = re.match(rf"^{re.escape(prefix)}/(concept|deriv)/([a-z0-9]+(?:-[a-z0-9]+)*)$", cid)
    if not m:
        e.append(f"id 格式错：{cid}")
    else:
        if m.group(1) != ("concept" if kind == "concepts" else "deriv"):
            e.append("id 类型与目录不符")
        if m.group(2) != path.stem:
            e.append(f"slug 与文件名不符：{m.group(2)} vs {path.stem}")
    if card.get("type") != ("concept" if kind == "concepts" else "derivation"):
        e.append("type 与目录不符")
    if card.get("track") not in TRACKS:
        e.append(f"track 非法：{card.get('track')}")
    for k in ("title", "summary", "question", "pitfalls", "related", "sources",
              "rights", "status", "provenance_note", "aliases"):
        if k not in card:
            e.append(f"缺字段 {k}")
    if not card.get("aliases"):
        e.append("aliases 至少 1 条")
    if text_len(card.get("summary", "")) > 120:
        e.append(f"summary 过长：{text_len(card.get('summary',''))}")
    if not card.get("question", "").rstrip().endswith(("？", "?")):
        e.append("question 未以问号结尾")
    if card.get("rights") != "rewritten":
        e.append("rights 必须是 rewritten")
    if card.get("status") not in STATUS:
        e.append(f"status 非法：{card.get('status')}")
    if not isinstance(card.get("pitfalls"), list) or len(card.get("pitfalls", [])) < 2:
        e.append("pitfalls 至少 2 条")
    rel = card.get("related", [])
    if not isinstance(rel, list) or not rel:
        e.append("related 至少 1 条")
    for r in rel:
        if r not in ids and not allow_missing:
            e.append(f"related 指向不存在的卡：{r}")

    srcs = card.get("sources", [])
    if not isinstance(srcs, list) or not srcs:
        e.append("sources 必须非空")
    for i, s in enumerate(srcs):
        if s.get("text") not in DOCS:
            e.append(f"sources[{i}].text 非法")
        pages = s.get("pages")
        if not (isinstance(pages, list) and len(pages) == 2 and all(isinstance(x, int) for x in pages)):
            e.append(f"sources[{i}].pages 必须是两整数")
        elif not (1 <= pages[0] <= pages[1] <= max_pages):
            e.append(f"sources[{i}].pages 越界：{pages}（上限 {max_pages}）")
        if not ANCHOR_RE.match(s.get("anchor", "")):
            e.append(f"sources[{i}].anchor 格式错：{s.get('anchor')}")
        q = (s.get("quote") or "").strip()
        if s.get("text") == "A":
            if not (12 <= len(q) <= 120):
                e.append(f"sources[{i}].quote 需 12–120 字符的英文原句（现 {len(q)}）")
            elif re.search(r"[\u4e00-\u9fff]", q):
                e.append(f"sources[{i}].quote 应为英文原文")

    if kind == "concepts":
        d = card.get("definition")
        if not isinstance(d, dict) or not d.get("text"):
            e.append("definition.text 必填")
        if len(card.get("key_points", [])) < 3:
            e.append("key_points 至少 3 条")
        if len(card.get("formulas", [])) < 1:
            e.append("formulas 至少 1 条")
        for j, t in enumerate(card.get("theorems", [])):
            pr = (t or {}).get("proof") or {}
            st = pr.get("status")
            if st not in {"complete", "sketch", "gap"}:
                e.append(f"theorems[{j}].proof.status 非法")
            steps = pr.get("steps") or []
            if st == "complete":
                if len(steps) < 2:
                    e.append(f"theorems[{j}] complete 需 ≥2 步")
                for k, stp in enumerate(steps):
                    if not stp.get("text") or not stp.get("why"):
                        e.append(f"theorems[{j}].steps[{k}] 缺 text/why")
            elif not pr.get("gap_note"):
                e.append(f"theorems[{j}] {st} 必须有 gap_note")
    else:
        if not card.get("goal"):
            e.append("goal 必填")
        if len(card.get("setup", [])) < 1:
            e.append("setup 至少 1 条")
        steps = card.get("steps", [])
        if len(steps) < 3:
            e.append(f"steps 至少 3 条（现 {len(steps)}）")
        for k, stp in enumerate(steps):
            for f in ("text", "why", "locator", "provenance"):
                if not stp.get(f):
                    e.append(f"steps[{k}] 缺 {f}")
            if stp.get("provenance") not in {"A", "B", "C"}:
                e.append(f"steps[{k}].provenance 非法")
            if not ANCHOR_RE.match(stp.get("locator", "")):
                e.append(f"steps[{k}].locator 格式错：{stp.get('locator')}")
        if not card.get("result"):
            e.append("result 必填")

    if ABS_RE.search(json.dumps(card, ensure_ascii=False)):
        e.append("含本机绝对路径")
    return e


def check_pkg(pkg: Path):
    """包级质检：笔记的核对节 + errata.tsv + 卡片 corrections 一致性。"""
    e = []
    notes = pkg / "notes.md"
    if not notes.exists():
        e.append("缺 notes.md")
        txt = ""
    else:
        txt = notes.read_text(encoding="utf-8")
    if not re.search(r"^##\s*(?:\d+[.、]\s*)?核对与勘误", txt, re.M):
        e.append("notes.md 缺「核对与勘误」节（外部校正必须留痕）")
    else:
        seg = re.split(r"^##\s*(?:\d+[.、]\s*)?核对与勘误.*$", txt, maxsplit=1, flags=re.M)[1]
        seg = seg.split("\n## ", 1)[0]
        srcpart = seg.split("### 勘误", 1)[0]
        nsrc = len(re.findall(r"^\|\s*[^|\n]+\|\s*[^|\n]+\|\s*[^|\n]+", srcpart, re.M))
        if nsrc < 4:
            e.append(f"核对节的「外部来源」不足 3 条（现 {max(0, nsrc - 1)} 条，表头不算）")
        if "勘误" not in seg:
            e.append("核对节里缺「勘误」小节")
    er = pkg / "errata.tsv"
    ids = set()
    rows = []
    if not er.exists():
        e.append("缺 errata.tsv（无笔误也要有表头）")
    else:
        lines = [l for l in er.read_text(encoding="utf-8").splitlines() if l.strip()]
        if not lines or "位置" not in lines[0]:
            e.append("errata.tsv 缺表头（序/位置/原写法/订正/依据1/依据2/置信度/影响卡片/状态）")
        else:
            for i, l in enumerate(lines[1:], 1):
                p = l.split("\t")
                if len(p) < 9:
                    e.append(f"errata.tsv 第 {i} 行字段不足（{len(p)}/9，用制表符分隔）")
                    continue
                rows.append(p)
                ids.add(p[0])
                if p[6] not in {"high", "medium", "low"}:
                    e.append(f"errata.tsv 第 {i} 行置信度非法：{p[6]}")
                if p[8] not in {"open", "fixed", "wontfix"}:
                    e.append(f"errata.tsv 第 {i} 行状态非法：{p[8]}")
                if not p[4] or p[4] == "-":
                    e.append(f"errata.tsv 第 {i} 行缺依据1（必须写出处）")
                if p[6] == "high" and (not p[5] or p[5] == "-"):
                    e.append(f"errata.tsv 第 {i} 行判 high 但缺依据2（high 需两处独立出处）")
                if not p[1] or p[1] == "-":
                    e.append(f"errata.tsv 第 {i} 行缺位置（页码/式号）")
    return e, ids, rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default="cards")
    ap.add_argument("--prefix", default="")
    ap.add_argument("--max-pages", type=int, default=400)
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--no-pkg", action="store_true", help="跳过包级检查（只查卡片）")
    a = ap.parse_args()

    base = Path(a.target)
    if not base.is_absolute():
        base = Path.cwd() / base
    pkg_checks = None
    if not a.no_pkg and (base / "cards").is_dir():
        pkg_checks = base
        base = base / "cards"
    prefix = a.prefix or re.sub(r"^\d+_", "", base.parent.name if pkg_checks else base.parent.name)

    files = sorted(base.glob("*/*.json"))
    if not files:
        print(f"[error] {base} 下没有卡片")
        return 1
    cards, ids = [], set()
    for f in files:
        try:
            c = json.loads(f.read_text(encoding="utf-8"))
        except Exception as ex:
            print(f"[FAIL] {f.name}: JSON 解析失败 {ex}")
            return 1
        cards.append((f, c))
        ids.add(c.get("id"))

    nerr = 0
    for f, c in cards:
        errs = check_card(f, c, ids, prefix, a.max_pages, a.allow_missing)
        if errs:
            nerr += len(errs)
            print(f"[FAIL] {f.parent.name}/{f.name}")
            for e in errs:
                print(f"   - {e}")
    dup = len(cards) - len(ids)
    if dup:
        print(f"[warn] id 重复 {dup} 处")
    n_c = sum(1 for f, _ in cards if "concepts" in f.parts)
    n_d = len(cards) - n_c

    if pkg_checks:
        perrs, eids, erows = check_pkg(pkg_checks)
        # 卡片 corrections 与 errata.tsv 互相对照
        cardids = {c.get("id"): c for _, c in cards}
        for cid, c in cardids.items():
            for j, cor in enumerate(c.get("corrections") or []):
                if not isinstance(cor, dict) or not cor.get("id") or not cor.get("note"):
                    perrs.append(f"{cid}.corrections[{j}] 需 {{id,note}}")
                    continue
                if eids and cor["id"] not in eids:
                    perrs.append(f"{cid}.corrections[{j}].id={cor['id']} 在 errata.tsv 里不存在")
        for p in erows:
            hits = [x for x in (p[7] or "").split(",") if x.strip()]
            for h in hits:
                if h.strip() and h.strip() not in cardids:
                    perrs.append(f"errata {p[0]} 的影响卡片 {h.strip()} 不存在")
        if perrs:
            nerr += len(perrs)
            print(f"[FAIL] 包级检查 {pkg_checks.name}")
            for e in perrs:
                print(f"   - {e}")
        else:
            print(f"[ok] 包级检查：核对节 + errata {len(erows)} 条")

    print(f"[done] 卡 {len(cards)} 张（概念 {n_c} / 推导 {n_d}），错误 {nerr}")
    return 1 if (nerr and a.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
