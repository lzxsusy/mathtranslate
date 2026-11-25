# -*- coding: utf-8 -*-
"""合并 9 份 errata 为 00-审校总表.tsv，并做结构与重复登记检查。

用法：
    python tools/merge_errata.py            # 生成总表 + 打印统计
    python tools/merge_errata.py --check    # 只检查，不写文件

检查项：
1. 表头是否与 BRIEF §8.3 完全一致；
2. 每行列数是否 11；type / severity 是否在枚举内；
3. loc_tex 是否形如 chapters/chNN.tex:行号；
4. 与 existing-notes.tsv 是否疑似重复（同章 + 同原书页 + 非 existing-note-wrong）。
"""
import os
import re
import sys
import io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HEADER = ["chapter", "loc_book", "loc_zh", "loc_tex", "type", "severity",
          "original", "problem", "suggestion", "evidence"]
TYPES = {"translation-error", "original-error", "term", "formula", "typo",
         "numbering", "existing-note-wrong"}
SEV = {"high", "medium", "low"}
SEV_RANK = {"high": 0, "medium": 1, "low": 2}


def load_errata(nn, problems):
    path = os.path.join(ROOT, "产出", "批注", f"ch{nn}-errata.tsv")
    if not os.path.exists(path):
        problems.append(f"ch{nn}: 文件不存在 {os.path.relpath(path, ROOT)}")
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    if not lines:
        problems.append(f"ch{nn}: 空文件")
        return []
    head = lines[0].split("\t")
    if [h.strip() for h in head] != HEADER:
        problems.append(f"ch{nn}: 表头不符 -> {head}")
    for i, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        fld = line.split("\t")
        if len(fld) != len(HEADER):
            problems.append(f"ch{nn}:{i}: 列数 {len(fld)} != {len(HEADER)}")
            continue
        ch, lb, lz, lt, typ, sev, orig, prob, sug, ev = fld
        if typ not in TYPES:
            problems.append(f"ch{nn}:{i}: type={typ} 不在枚举内")
        if sev not in SEV:
            problems.append(f"ch{nn}:{i}: severity={sev} 不在枚举内")
        # 行号写法归一：允许「524」「524,531」「chapters/ch01.tex:524」
        lt = lt.strip()
        if re.fullmatch(r"\d+", lt):
            lt = f"chapters/{ch or 'ch' + nn}.tex:{lt}"
        elif re.fullmatch(r"[\d,\s]+", lt):
            first = re.split(r"[,，\s]+", lt)[0]
            lt = f"chapters/{ch or 'ch' + nn}.tex:{first}"
        elif not lt.startswith("chapters/"):
            m2 = re.match(r"^(?:ch\d\d\.tex|chapters/ch\d\d\.tex)[:：](\d+)$", lt)
            if m2:
                lt = f"chapters/{ch or 'ch' + nn}.tex:{m2.group(1)}"
        if not re.match(r"^chapters/ch\d\d\.tex:\d+$", lt):
            problems.append(f"ch{nn}:{i}: loc_tex={lt} 格式不对")
        rows.append(dict(chapter=ch or f"ch{nn}", loc_book=lb, loc_zh=lz, loc_tex=lt,
                         type=typ, severity=sev, original=orig, problem=prob,
                         suggestion=sug, evidence=ev))
    return rows


def load_existing():
    path = os.path.join(ROOT, "产出", "汇总", "existing-notes.tsv")
    out = {}
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as f:
        for line in f.read().splitlines()[1:]:
            fld = line.split("\t")
            if len(fld) < 4:
                continue
            m = re.search(r"p\.?\s*(\d+)", fld[2])
            page = m.group(1) if m else ""
            out.setdefault(fld[0], set()).add(page)
    return out


def main():
    check_only = "--check" in sys.argv
    problems = []
    rows = []
    for nn in [f"{i:02d}" for i in range(1, 10)]:
        rows += load_errata(nn, problems)

    existing = load_existing()
    dup = []
    for r in rows:
        if r["type"] == "existing-note-wrong":
            continue
        m = re.search(r"p\.?\s*(\d+)", r["loc_book"])
        if m and m.group(1) in existing.get(r["chapter"], set()):
            dup.append(r)

    rows.sort(key=lambda r: (r["chapter"], SEV_RANK.get(r["severity"], 9),
                             r["type"], r["loc_tex"]))
    out_path = os.path.join(ROOT, "产出", "批注", "00-审校总表.tsv")
    if not check_only:
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\t".join(HEADER) + "\n")
            for r in rows:
                f.write("\t".join(r[k] for k in HEADER) + "\n")

    print(f"总条数: {len(rows)}")
    for key in ("type", "severity"):
        cnt = {}
        for r in rows:
            cnt[r[key]] = cnt.get(r[key], 0) + 1
        print(f"按 {key}: " + ", ".join(f"{k}={v}" for k, v in sorted(cnt.items())))
    per_ch = {}
    for r in rows:
        per_ch[r["chapter"]] = per_ch.get(r["chapter"], 0) + 1
    print("按章: " + ", ".join(f"{k}={v}" for k, v in sorted(per_ch.items())))
    print(f"结构问题: {len(problems)}")
    for p in problems:
        print("  ! " + p)
    print(f"疑似重复已有译注: {len(dup)}")
    for r in dup:
        print(f"  ? {r['chapter']} {r['loc_book']} | {r['original'][:40]}")
    print("写出:", os.path.relpath(out_path, ROOT) if not check_only else "(--check 未写)")


if __name__ == "__main__":
    main()
