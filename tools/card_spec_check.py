#!/usr/bin/env python3
"""资料卡规范校验器（04_playbook/23_资料卡制作规范_v1.md v1.0）。

用法：
  python tools/card_spec_check.py --all
  python tools/card_spec_check.py --set glc
  python tools/card_spec_check.py --paths list.txt        # 每行一个 json 路径
  python tools/card_spec_check.py --all --json _meta/card_spec_report.json
  python tools/card_spec_check.py --all --warn-as-error

硬错误（hard）→ 退出码 1；警告（warn）不影响退出码，除非 --warn-as-error。
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS = os.path.join(REPO, "datasets")

TYPES = {"concept", "derivation", "correction", "example", "statement", "remark", "conjecture"}
STATUS = {"draft", "dev", "reviewed", "published"}
RIGHTS = {"rewritten", "self", "arxiv", "book"}
PROOF = {"complete", "sketch", "cited", "none"}
# 历史形态（legacy）：默认只报 warn；--strict 下才算 hard。
LEGACY_PROOF = {"gap", "reference", "full", "sketched", "略证", "略证（标准结果）", None}
ID_ALIASES = {
    "bzg": "benzvi_glc",
    "kw": "kw06",
    "lawrge": "lawrge24",
    "pi": "pathintegral",
    "sy29": "sy02-29",
    "sy32": "sy02-32",
    "sy38": "sy0238",
}


def card_paths(args):
    if args.paths:
        out = []
        with open(args.paths, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                p = line if os.path.isabs(line) else os.path.join(REPO, line)
                out.append(p)
        return out
    if args.set:
        root = os.path.join(DATASETS, args.set, "cards")
    elif args.all:
        root = os.path.join(DATASETS, "*", "cards")
    else:
        print("需要 --all / --set <name> / --paths <file>", file=sys.stderr)
        sys.exit(2)
    files = []
    for p in glob.glob(os.path.join(root, "**", "*.json"), recursive=True):
        if os.path.basename(p) in ("index.json", "work.json"):
            continue
        files.append(p)
    return sorted(files)


def is_int_list(v):
    return isinstance(v, list) and all(isinstance(x, int) and not isinstance(x, bool) for x in v)


def check_card(path, ids, strict=False):
    errs, warns = [], []
    rel = os.path.relpath(path, REPO).replace("\\", "/")
    parts = rel.split("/")
    set_name = parts[1] if len(parts) > 2 and parts[0] == "datasets" else None
    slug = os.path.splitext(os.path.basename(path))[0]

    def hard(code, msg):
        errs.append({"code": code, "msg": msg})

    def warn(code, msg):
        warns.append({"code": code, "msg": msg})

    def legacy(code, msg):
        if strict:
            hard(code, msg)
        else:
            warns.append({"code": "legacy_" + code, "msg": msg})

    try:
        raw = open(path, encoding="utf-8").read()
        d = json.loads(raw)
    except Exception as e:  # noqa: BLE001
        hard("json_parse", f"{type(e).__name__}: {e}")
        return rel, errs, warns

    if not isinstance(d, dict):
        hard("json_not_object", f"顶层是 {type(d).__name__}")
        return rel, errs, warns

    # 控制字符
    for i, ch in enumerate(raw):
        if ord(ch) < 0x20 and ch not in "\n\t":
            hard("control_char", f"偏移 {i} 出现 U+{ord(ch):04X}")
            break

    for k in ("id", "type", "track", "title", "rights", "status"):
        if not d.get(k):
            hard("required", f"缺通用字段 {k}")

    t = d.get("type")
    if t not in TYPES:
        hard("type_enum", f"type={t!r} 不在 {sorted(TYPES)}")

    st = d.get("status")
    if st not in STATUS:
        hard("status_enum", f"status={st!r} 不在 {sorted(STATUS)}")
    rt = d.get("rights")
    if rt not in RIGHTS:
        hard("rights_enum", f"rights={rt!r} 不在 {sorted(RIGHTS)}")

    cid = d.get("id") or ""
    if set_name and cid and not cid.startswith(set_name + "/"):
        prefix = cid.split("/")[0]
        if ID_ALIASES.get(prefix) == set_name:
            legacy("id_set", f"id 前缀 {prefix!r} 是指定别名（规范集名 {set_name!r}）")
        else:
            hard("id_set", f"id={cid!r} 不以集名 {set_name!r} 开头")
    if cid and cid.rsplit("/", 1)[-1] != slug:
        warn("id_slug", f"id 末段 {cid.rsplit('/', 1)[-1]!r} != 文件名 {slug!r}")

    # 分 type 必填
    def need(*fields):
        for f in fields:
            v = d
            for seg in f.split("."):
                if isinstance(v, dict) and seg in v:
                    v = v[seg]
                else:
                    v = None
                    break
            if v is None or (isinstance(v, (str, list, dict)) and len(v) == 0):
                hard("type_required", f"{t} 缺 {f}")

    if t in ("concept", "conjecture"):
        need("summary", "question", "definition.text", "key_points", "related", "sources")
        if isinstance(d.get("key_points"), list) and len(d["key_points"]) < 3:
            hard("key_points_min", f"key_points 只有 {len(d['key_points'])} 条（需 ≥3）")
    elif t == "derivation":
        need("summary", "question", "goal", "setup", "steps", "result", "gaps", "sources", "related")
        if isinstance(d.get("steps"), list) and len(d["steps"]) < 2:
            hard("steps_min", f"steps 只有 {len(d['steps'])} 步（需 ≥2）")
    elif t == "correction":
        need("summary", "question", "location", "original", "corrected", "why", "note", "sources", "related")
    elif t == "example":
        need("summary", "question", "setup", "computation", "result", "check", "concept_refs", "sources", "related")
    elif t == "statement":
        need("source", "natural_language.zh", "natural_language.en", "lean.file", "lean.name", "lean.statement")
    elif t == "remark":
        need("summary", "question", "statement", "why", "sources", "related")

    # sources
    src = d.get("sources")
    if t != "statement":
        if not isinstance(src, list) or not src:
            hard("sources_empty", "sources 缺失或为空")
        else:
            for i, s in enumerate(src):
                if not isinstance(s, dict):
                    hard("source_type", f"sources[{i}] 不是对象")
                    continue
                if not s.get("section"):
                    if s.get("section") == "":
                        legacy("source_section", f"sources[{i}].section 为空字符串")
                    else:
                        hard("source_section", f"sources[{i}] 缺 section")
                pg = s.get("pages")
                if isinstance(pg, list) and pg and all(isinstance(x, str) for x in pg):
                    legacy("source_pages", f"sources[{i}].pages 是文本区间 {pg!r}（规范为整数列表）")
                elif isinstance(pg, int):
                    legacy("source_pages", f"sources[{i}].pages 是整数 {pg!r}（规范为列表）")
                elif isinstance(pg, list) and pg and all(isinstance(x, str) for x in pg):
                    legacy("source_pages", f"sources[{i}].pages 是文本区间 {pg!r}（规范为整数列表）")
                elif (s.get("pages_zh") or s.get("pages_en")) and not pg:
                    legacy("source_pages", f"sources[{i}] 用 pages_zh/pages_en 双语页（规范为 pages）")
                elif not is_int_list(pg):
                    hard("source_pages", f"sources[{i}].pages 不是整数列表")
                if s.get("pages") and s.get("pdf_pages") and s.get("pages") != s.get("pdf_pages") and not s.get("page_note"):
                    warn("pages_offset_no_note", f"sources[{i}] pages≠pdf_pages 但无 page_note")
                if not s.get("quote"):
                    warn("source_no_quote", f"sources[{i}] 缺逐字 quote")
                if not s.get("anchor"):
                    warn("source_no_anchor", f"sources[{i}] 缺 anchor")

    # related
    rel_list = d.get("related")
    if isinstance(rel_list, list):
        for r in rel_list:
            if not isinstance(r, str) or "/" not in r:
                hard("related_format", f"related 项 {r!r} 不是完整 id")
            elif r not in ids:
                hard("related_broken", f"related 指向不存在的 id {r}")
        if len(rel_list) > 8:
            warn("related_many", f"related 有 {len(rel_list)} 条（建议 ≤8）")

    # theorems
    ths = d.get("theorems")
    if isinstance(ths, list):
        for i, th in enumerate(ths):
            if not isinstance(th, dict):
                legacy("theorem_type", f"theorems[{i}] 是 {type(th).__name__}，不是对象")
                continue
            if not th.get("name"):
                warn("theorem_no_name", f"theorems[{i}] 缺 name")
            if not th.get("statement"):
                hard("theorem_no_statement", f"theorems[{i}] 缺 statement")
            pr = th.get("proof")
            if isinstance(pr, dict):
                ps = pr.get("status")
                if ps not in PROOF:
                    if ps in LEGACY_PROOF:
                        legacy("proof_status_enum", f"theorems[{i}].proof.status={ps!r} 是历史取值（规范 {sorted(PROOF)}）")
                    else:
                        hard("proof_status_enum", f"theorems[{i}].proof.status={ps!r} 不在 {sorted(PROOF)}")
                if ps == "sketch" and not pr.get("gap_note"):
                    hard("proof_sketch_gap", f"theorems[{i}] sketch 无 gap_note")
            if not th.get("source"):
                warn("theorem_no_source", f"theorems[{i}] 缺 source")

    # formulas
    fs = d.get("formulas")
    if isinstance(fs, list):
        for i, f in enumerate(fs):
            if not isinstance(f, str):
                hard("formula_type", f"formulas[{i}] 不是字符串")
                continue
            if f.count("$") % 2:
                warn("formula_dollar", f"formulas[{i}] $ 数为奇数")
            if f.count("{") != f.count("}"):
                warn("formula_brace", f"formulas[{i}] 花括号不配对")
            if len(f) > 800:
                warn("formula_long", f"formulas[{i}] 长度 {len(f)}（建议 ≤800）")

    if not d.get("provenance_note"):
        warn("no_provenance", "缺 provenance_note")
    if not d.get("aliases"):
        warn("no_aliases", "缺 aliases")
    if len(raw.encode("utf-8")) > 12 * 1024:
        warn("card_large", f"{len(raw.encode('utf-8'))} bytes（建议 ≤12 KB）")

    return rel, errs, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--set")
    ap.add_argument("--paths")
    ap.add_argument("--json")
    ap.add_argument("--warn-as-error", action="store_true")
    ap.add_argument("--strict", action="store_true", help="历史形态也按 hard 计（新卡/返工必须过）")
    ap.add_argument("--limit-print", type=int, default=40)
    args = ap.parse_args()

    paths = card_paths(args)
    ids = set()
    for p in paths:
        try:
            d = json.load(open(p, encoding="utf-8"))
            if isinstance(d, dict) and d.get("id"):
                ids.add(d["id"])
        except Exception:  # noqa: BLE001
            pass

    hard_codes, warn_codes = Counter(), Counter()
    by_set = defaultdict(lambda: [0, 0, 0])  # cards, hard, warn
    results = []
    printed = 0
    for p in paths:
        rel, errs, warns = check_card(p, ids, strict=args.strict)
        results.append({"path": rel, "hard": errs, "warn": warns})
        set_name = rel.split("/")[1] if rel.startswith("datasets/") else "?"
        by_set[set_name][0] += 1
        by_set[set_name][1] += len(errs)
        by_set[set_name][2] += len(warns)
        for e in errs:
            hard_codes[e["code"]] += 1
        for w in warns:
            warn_codes[w["code"]] += 1
        if errs and printed < args.limit_print:
            printed += 1
            print(f"\n[hard] {rel}")
            for e in errs[:8]:
                print(f"   - {e['code']}: {e['msg']}")

    n = len(paths)
    nh = sum(1 for r in results if r["hard"])
    nw = sum(1 for r in results if r["warn"])
    print("\n=== summary ===")
    print(f"cards={n} hard_cards={nh} warn_cards={nw} strict={args.strict}")
    print("hard by code:", dict(hard_codes) or "{}")
    print("warn by code:", dict(warn_codes) or "{}")
    print("by set (cards/hard/warn):")
    for s, v in sorted(by_set.items(), key=lambda kv: (-kv[1][1], kv[0])):
        if v[1] or v[2]:
            print(f"  {s:14s} {v[0]:4d}/{v[1]:4d}/{v[2]:4d}")

    if args.json:
        out = os.path.join(REPO, args.json) if not os.path.isabs(args.json) else args.json
        os.makedirs(os.path.dirname(out), exist_ok=True)
        json.dump(
            {
                "spec": "04_playbook/23_资料卡制作规范_v1.md",
                "spec_version": "1.0",
                "cards": n,
                "hard_cards": nh,
                "warn_cards": nw,
                "hard_by_code": dict(hard_codes),
                "warn_by_code": dict(warn_codes),
                "by_set": {k: {"cards": v[0], "hard": v[1], "warn": v[2]} for k, v in by_set.items()},
                "results": results,
            },
            open(out, "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=1,
        )
        print("wrote", out)

    if nh or (args.warn_as_error and nw):
        sys.exit(1)


if __name__ == "__main__":
    main()
