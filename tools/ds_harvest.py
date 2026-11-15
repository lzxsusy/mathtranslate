# -*- coding: utf-8 -*-
"""ds_harvest.py — 从存量语料里挑「余料」候选，生成标注队列。

用法：
    python tools/ds_harvest.py                 # 写 datasets/candidates/harvest_queue.jsonl
    python tools/ds_harvest.py --limit 300     # 只取前 300 条
    python tools/ds_harvest.py --dry-run       # 只统计，不写文件

不调用任何模型；只做确定性打分。打分理由写进 reasons，供人工/模型复核。
"""
import io
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "01_corpus_zh", "zh_paragraphs.jsonl")
TERMS = os.path.join(ROOT, "01_corpus_zh", "termbase.jsonl")
DEEPREAD_DIR = os.path.join(ROOT, "datasets", "deepread")
OUT_DIR = os.path.join(ROOT, "datasets", "candidates")
OUT = os.path.join(OUT_DIR, "harvest_queue.jsonl")

MACRO_RE = re.compile(r"\\(R|C|Z|Hom|dd|mathrm|ref|cite|eqref|begin|end)\b")
PATH_RE = re.compile(r"C:[\\/]+Users|/Users/|<本地路径>|<path>", re.I)
FLAG_WEIGHT = {"meta_block": 4, "orphan_number": 3, "empty_paren": 2,
               "template": 4, "size_residue": 2, "near_dup_of": 1}


def norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()


def score_para(rec, deepread_pkgs):
    reasons = []
    score = 0
    flags = rec.get("flags") or []
    for f in flags:
        w = FLAG_WEIGHT.get(f, 1)
        score += w
        reasons.append("flags=%s" % f)
    n = int(rec.get("zh_chars") or 0)
    if n < 30:
        score += 1
        reasons.append("碎片段(%d字)" % n)
    elif n > 1500:
        score += 2
        reasons.append("超长段(%d字)" % n)
    text = str(rec.get("text") or "")
    hits = sorted(set(MACRO_RE.findall(text)))
    if hits:
        score += min(2 * len(hits), 6)
        reasons.append("未展开宏:" + ",".join(hits[:6]))
    if "??" in text:
        score += 2
        reasons.append("未解析引用")
    if PATH_RE.search(text):
        score += 4
        reasons.append("本机路径残留")
    pkg = str(rec.get("pkg") or "")
    if pkg and pkg not in deepread_pkgs:
        score += 2
        reasons.append("工程尚无精读卡")
    if rec.get("env") in ("proof", "theorem"):
        score += 1
        reasons.append("命题/证明段")
    return score, reasons


def main():
    limit = 500
    dry = "--dry-run" in sys.argv
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    deepread_pkgs = set()
    if os.path.isdir(DEEPREAD_DIR):
        for name in os.listdir(DEEPREAD_DIR):
            if name.endswith(".jsonl"):
                deepread_pkgs.add(name.split(".")[0])

    if not os.path.isfile(CORPUS):
        print("找不到语料：%s" % CORPUS)
        return 2

    rows, reason_count = [], Counter()
    per_pkg = Counter()
    seen = set()
    ignored = 0
    with io.open(CORPUS, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            text = norm(rec.get("text"))
            if not text:
                ignored += 1
                continue
            score, reasons = score_para(rec, deepread_pkgs)
            if score <= 0:
                continue
            pid = str(rec.get("para_id") or "")
            if pid in seen:
                continue
            seen.add(pid)
            pkg = str(rec.get("pkg") or "?")
            if per_pkg[pkg] >= 25:
                continue
            per_pkg[pkg] += 1
            for r in reasons:
                reason_count[r.split("(")[0].split(":")[0]] += 1
            rows.append({
                "id": pid or "%s.para%s" % (pkg, rec.get("para")),
                "type": "paragraph",
                "pkg": pkg,
                "env": rec.get("env"),
                "zh_chars": rec.get("zh_chars"),
                "flags": rec.get("flags") or [],
                "score": score,
                "reasons": reasons,
                "suggested_action": suggest(reasons),
                "snippet": text[:180],
            })

    # 术语候选：status=candidate，单列，权重低一档
    term_rows = []
    if os.path.isfile(TERMS):
        with io.open(TERMS, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                t = json.loads(line)
                if t.get("status") != "candidate":
                    continue
                foreign = norm(t.get("foreign"))
                if not foreign:
                    continue
                term_rows.append({
                    "id": "TERM:%s" % foreign,
                    "type": "term",
                    "pkg": str(t.get("pkg") or "?"),
                    "score": 3,
                    "reasons": ["术语待裁决(candidate)"],
                    "suggested_action": "L1 术语裁决：定译名、给理由与反例，回写 termbase",
                    "snippet": "%s → %s" % (foreign, norm(t.get("zh"))),
                })

    rows.sort(key=lambda r: (-r["score"], r["id"]))
    term_rows.sort(key=lambda r: r["id"])
    out = rows[:limit] + term_rows[:200]

    print("paragraph candidates: %d (selected %d, ignored empty %d)" %
          (len(rows), min(limit, len(rows)), ignored))
    print("term candidates: %d (appended %d)" % (len(term_rows), min(200, len(term_rows))))
    print("by reason:", ", ".join("%s=%d" % kv for kv in reason_count.most_common(8)))
    print("top pkg:", ", ".join("%s=%d" % kv for kv in per_pkg.most_common(8)))
    for r in out[:5]:
        print("  [%d] %s %s" % (r["score"], r["id"], "; ".join(r["reasons"])[:80]))

    if dry:
        return 0
    if not os.path.isdir(OUT_DIR):
        os.makedirs(OUT_DIR)
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("wrote %s (%d records)" % (os.path.relpath(OUT, ROOT).replace("\\", "/"), len(out)))
    return 0


def suggest(reasons):
    joined = " ".join(reasons)
    if "本机路径" in joined:
        return "L0 修正：删路径、补回公式"
    if "未展开宏" in joined:
        return "L0 修正：展开宏为具体符号/命令"
    if "flags=meta_block" in joined or "flags=template" in joined:
        return "L0 修正：判为元数据/模板，移出语料或标 excluded"
    if "碎片段" in joined:
        return "L0 修正：与相邻段合并或删"
    if "超长段" in joined:
        return "L0 修正：按句群拆分"
    if "未解析引用" in joined:
        return "L0 修正：解析 \\ref 目标"
    if "尚无精读卡" in joined:
        return "L2 精读：为工程补第一张精读卡"
    return "L2 精读：判断是否值得做命题卡"


if __name__ == "__main__":
    sys.exit(main())
