#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lint encyclopedia entries.

Usage:
  python entry_lint.py <entries_dir> [--trans <plain_translation.txt>] [--index]
Checks structure, required fields, page ranges, proof completeness, and
12-character overlap against a plain-text translation corpus.
Exit code 1 if any ERROR.
"""
import json, os, re, sys, glob

CATEGORIES = {"topology", "geometry", "algebra", "qft", "susy", "condensed", "math-phys"}
ID_RE = re.compile(r"^[a-z-]+/[a-z0-9-]+$")
MAX_SUMMARY = 160
MAX_ENTRY_CHARS = 20000
PAGE_MIN, PAGE_MAX = 1, 207


def cjk_len(s):
    return len(re.findall(r"[\u4e00-\u9fff]", s or ""))


def walk_text(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from walk_text(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_text(v)


def shingles(text, n=12):
    s = re.sub(r"[^\u4e00-\u9fff]+", "|", text or "")
    out = set()
    for seg in s.split("|"):
        out |= {seg[i:i + n] for i in range(max(0, len(seg) - n + 1))}
    return out


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "entries"
    trans_path = None
    if "--trans" in sys.argv:
        trans_path = sys.argv[sys.argv.index("--trans") + 1]
    trans_sh = set()
    if trans_path and os.path.exists(trans_path):
        trans_sh = shingles(open(trans_path, encoding="utf-8", errors="replace").read())

    files = sorted(glob.glob(os.path.join(d, "**", "*.json"), recursive=True))
    errs, warns, ids = [], [], {}
    index = []
    for f in files:
        rel = os.path.relpath(f, d).replace("\\", "/")
        try:
            e = json.load(open(f, encoding="utf-8"))
        except Exception as ex:
            errs.append(f"{rel}: JSON 解析失败: {ex}")
            continue
        eid = e.get("id", "")
        if not ID_RE.match(eid):
            errs.append(f"{rel}: id 格式不对: {eid!r}")
        elif rel[:-5] != eid:
            warns.append(f"{rel}: 路径与 id 不一致（id={eid}）")
        if eid in ids:
            errs.append(f"{rel}: id 重复（另见 {ids[eid]}）")
        ids[eid] = rel
        cat = e.get("category", "")
        if cat not in CATEGORIES:
            errs.append(f"{rel}: category 非法: {cat!r}")
        if not e.get("title"):
            errs.append(f"{rel}: 缺 title")
        if cjk_len(e.get("summary", "")) > MAX_SUMMARY:
            errs.append(f"{rel}: summary 过长")
        if not e.get("definition") and len(e.get("theorems", [])) < 2:
            errs.append(f"{rel}: 既无 definition 又少于 2 条定理")
        for i, t in enumerate(e.get("theorems", [])):
            if not t.get("statement"):
                errs.append(f"{rel}: theorem[{i}] 缺 statement")
            p = t.get("proof") or {}
            if p.get("status") == "complete" and len(p.get("steps", [])) < 2:
                errs.append(f"{rel}: theorem[{i}] 标 complete 但 steps < 2")
            if p.get("status") == "sketch" and not p.get("gap_note"):
                warns.append(f"{rel}: theorem[{i}] 标 sketch 但没写 gap_note")
            for s in p.get("steps", []):
                if not s.get("text") or not s.get("why"):
                    errs.append(f"{rel}: theorem[{i}] 有步骤缺 text/why")
        for j, ex in enumerate(e.get("examples", [])):
            if not ex.get("result"):
                errs.append(f"{rel}: example[{j}] 缺 result")
            if not ex.get("computation"):
                warns.append(f"{rel}: example[{j}] 没有计算步骤")
        for k, src in enumerate(e.get("sources", []) + [s for t in e.get("theorems", []) for s in t.get("sources", [])]):
            if "section" not in src and "pages" not in src:
                continue  # top-level bibliography entry
            pg = src.get("pages")
            if not (isinstance(pg, list) and len(pg) == 2 and all(isinstance(x, int) for x in pg)):
                errs.append(f"{rel}: source[{k}] pages 不是两个整数: {pg}")
            else:
                a, b = pg
                if not (PAGE_MIN <= a <= b <= PAGE_MAX):
                    errs.append(f"{rel}: source[{k}] 页码越界/顺序错: {pg}")
        total = sum(len(x) for x in walk_text(e))
        if total > MAX_ENTRY_CHARS:
            warns.append(f"{rel}: 词条过长（{total} 字符）")
        if trans_sh:
            overlaps = set()
            for txt in walk_text(e):
                for sh in shingles(txt) & trans_sh:
                    overlaps.add(sh)
            if overlaps:
                sample = "、".join(sorted(overlaps)[:3])
                warns.append(f"{rel}: 与译稿有 {len(overlaps)} 处 12 字重合（如「{sample}」），需人工确认是否引用")
        index.append({"id": eid, "title": e.get("title", ""), "category": cat, "summary": e.get("summary", "")})

    for w in warns:
        print("WARN ", w)
    for err in errs:
        print("ERROR", err)
    print(f"\n{len(files)} entries, {len(errs)} errors, {len(warns)} warnings")
    if "--index" in sys.argv:
        out = os.path.join(d, "..", "index.jsonl")
        with open(out, "w", encoding="utf-8") as fh:
            for row in sorted(index, key=lambda r: r["id"]):
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        print("wrote", os.path.abspath(out))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
