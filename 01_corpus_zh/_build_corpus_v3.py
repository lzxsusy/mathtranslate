# -*- coding: utf-8 -*-
r"""语料 v3：在 v2（公式保真）基础上做质检与清洗。

做四件事：
1. 清掉排版残渣段（目次碎片、图注编号碎片、LaTeX 环境名表等）——它们不是数学内容；
2. 修掉「脱敏占位符落进公式内部」造成的坏公式（`$<本地路径>` 之类），并把公式定界符不配平的段标记出来；
3. 用 MinHash-LSH 找近重复段（Jaccard≥0.8），只标注 `near_dup_of`，不删除；
4. 给每段加 `zh_chars`（汉字数），并输出 `QA_REPORT.md` 与统计 json。

用法：
    python build_corpus_v3.py --out out_v3
"""
from __future__ import annotations

import argparse
import io
import json
import math
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

SRC = r"<本地路径>"
ZH = re.compile(r"[\u4e00-\u9fff]")

# 排版残渣特征：这些字符串出现在正文里说明抽到的是目录/表格/环境定义，不是内容
JUNK_SPLIT = re.compile(
    r"(tocsection|tocsubsection|tocchapter|tocpart"
    r"|figures?/[\w\-./]+\.(?:png|pdf|jpg|jpeg|eps)"
    r"|(?:theorem|proposition|lemma|definition|remark|corollary|conjecture|question|example)"
    r"(?:\*?)(?:定理|命题|引理|定义|注|推论|猜想|问题|例))",
    re.I,
)
# 纯环境名表（如 "plain theorem*定理 proposition*命题 lemma*引理 …"）
ENV_TABLE = re.compile(
    r"^(?:\s*(?:plain|theorem|proposition|lemma|corollary|definition|conjecture|question|remark|example)"
    r"\*?(?:定理|命题|引理|推论|定义|猜想|问题|注|例)?)+\s*$"
)
# 尾部尺寸/编号残渣，如 "0pt 3.2pt"、"105"、"3754"
TAIL_JUNK = re.compile(r"[\s\d.ptemex]{3,}$", re.I)
PLACEHOLDERS = ("<本地路径>", "[邮箱隐去]", "[已脱敏]")


def clean_junk(text: str) -> tuple[str, bool]:
    """切掉目录/图注残渣，返回 (清洗后文本, 是否被清洗)。"""
    m = JUNK_SPLIT.search(text)
    cleaned = False
    if m:
        text = text[:m.start()]
        cleaned = True
    # 去掉尾部尺寸/编号残渣
    new = TAIL_JUNK.sub("", text)
    if new != text:
        text = new
        cleaned = True
    return text.strip(), cleaned


def is_empty_after_clean(text: str) -> bool:
    if ENV_TABLE.match(text.strip()):
        return True
    plain = re.sub(r"\$[^$]*\$", "", text)
    if len(ZH.findall(plain)) < 8:
        return not ("\\begin{" in text)   # 有数学环境的短段保留
    return False


def repair_math(text: str) -> tuple[str, list[str]]:
    flags = []
    # 1) 占位符落进公式内部：把 $...$ 里的占位符换成 \text{[略]}
    def fix_seg(m):
        seg = m.group(0)
        for ph in PLACEHOLDERS:
            if ph in seg:
                seg = seg.replace(ph, r"\text{[略]}")
                flags.append("placeholder_in_math")
        return seg
    text = re.sub(r"\$[^$]*\$", fix_seg, text, flags=re.S)
    # 2) 仍有占位符（公式外的），保留（那是正常脱敏）
    if text.count("$") % 2 == 1:
        flags.append("unbalanced_math")
        # 去掉孤立的 $，避免下游解析器把整段当公式起点
        parts = text.split("$")
        text = "".join(p if i % 2 == 0 else p for i, p in enumerate(parts))
    return text, sorted(set(flags))


def shingles(text: str, k: int = 5) -> set[int]:
    t = re.sub(r"\s+", "", text)
    if len(t) < k:
        return set()
    return {hash(t[i:i + k]) for i in range(len(t) - k + 1)}


def minhash(sh: set[int], n: int = 8) -> tuple[int, ...]:
    sig = []
    for i in range(n):
        mn = min(((h * (i * 2 + 1) + i * 7919) % (2 ** 61 - 1)) for h in sh) if sh else 0
        sig.append(mn)
    return tuple(sig)


def jaccard(a: set[int], b: set[int]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    return inter / (len(a) + len(b) - inter)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out_v3")
    ap.add_argument("--src", default=SRC)
    ap.add_argument("--thresh", type=float, default=0.8)
    args = ap.parse_args()
    root = r"<本地路径>"
    out = os.path.join(root, args.out)
    os.makedirs(out, exist_ok=True)

    rows = []
    dropped = []
    n_placeholder = n_unbal = n_cleaned = 0
    for line in io.open(args.src, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        t = d["text"]
        t, cleaned = clean_junk(t)
        if cleaned:
            n_cleaned += 1
        t, flags = repair_math(t)
        if "placeholder_in_math" in flags:
            n_placeholder += 1
        if "unbalanced_math" in flags:
            n_unbal += 1
        if is_empty_after_clean(t):
            dropped.append({"pkg": d["pkg"], "file": d["file"], "para": d["para"], "text": t[:120]})
            continue
        if cleaned:
            flags = sorted(set(flags) | {"junk_trimmed"})
        d["text"] = t
        d["zh_chars"] = len(ZH.findall(t))
        if flags:
            d["flags"] = flags
        rows.append(d)

    # ---- 近重复：MinHash-LSH（band=4 × 2 行） ----
    buckets = defaultdict(list)
    sigs = []
    for i, d in enumerate(rows):
        sh = shingles(d["text"]) if len(d["text"]) >= 80 else set()
        sigs.append((sh, minhash(sh) if sh else None))
        if sigs[-1][1]:
            s = sigs[-1][1]
            for b in range(4):
                buckets[(b, s[b * 2], s[b * 2 + 1])].append(i)

    checked = set()
    near = 0
    for key, idxs in buckets.items():
        if len(idxs) < 2:
            continue
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                pair = (idxs[a], idxs[b])
                if pair in checked:
                    continue
                checked.add(pair)
                ia, ib = pair
                if jaccard(sigs[ia][0], sigs[ib][0]) >= args.thresh:
                    rows[ib].setdefault("near_dup_of", rows[ia]["para_id"])
    near = sum(1 for d in rows if d.get("near_dup_of"))
    print("近重复标注:", near, " 候选对:", len(checked))

    # ---- 写盘 ----
    dst = os.path.join(out, "zh_paragraphs.jsonl")
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        for d in rows:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    tot = len(rows)
    math = sum(1 for d in rows if "$" in d["text"] or "\\begin{" in d["text"])
    dup = sum(1 for d in rows if d.get("dup_of"))
    stats = {
        "total": tot,
        "dropped_junk": len(dropped),
        "junk_trimmed": n_cleaned,
        "with_math": math,
        "with_math_pct": round(100.0 * math / tot, 2),
        "exact_dup_flagged": dup,
        "near_dup_flagged": near,
        "placeholder_in_math_fixed": n_placeholder,
        "unbalanced_math_fixed": n_unbal,
        "unique_para_id": len({d["para_id"] for d in rows}),
        "packages": len({d["pkg"] for d in rows}),
        "with_page_orig": sum(1 for d in rows if d.get("page_orig") is not None),
        "zh_chars_total": sum(d["zh_chars"] for d in rows),
    }
    io.open(os.path.join(out, "zh_paragraphs_stats.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(stats, ensure_ascii=False, indent=1))
    print(json.dumps(stats, ensure_ascii=False, indent=1))

    # ---- QA 报告 ----
    rep = ["# 语料质检报告（v3）", "",
           "| 指标 | 数值 |", "|---|---|",
           "| 总段数 | %d |" % tot,
           "| 含公式 | %d（%.1f%%） |" % (math, 100.0 * math / tot),
           "| 唯一 para_id | %d |" % stats["unique_para_id"],
           "| 精确重复（保留 + 标 `dup_of`） | %d |" % dup,
           "| 近重复（Jaccard≥%.1f，保留 + 标 `near_dup_of`） | %d |" % (args.thresh, near),
           "| 汉字总数 | %d |" % stats["zh_chars_total"],
           "",
           "## 本次清掉的排版残渣（%d 段）" % len(dropped), "",
           "判定规则：出现 `tocsection`/`figures/*.png`/环境名表；或汉字 ≤6 且整段几乎是数字与点线；或整段无汉字。",
           "", "抽样（最多 20 条）：", ""]
    for d in dropped[:20]:
        rep.append("- `%s` p%d：%s" % (d["pkg"], d["para"], d["text"].replace("\n", " ")))
    rep += ["", "## 公式修复", "",
            "- 占位符落进公式内部（`$<本地路径>` 之类）：修复 **%d** 段，改用 `\\text{[略]}`" % n_placeholder,
            "- 公式定界符不配平：修复 **%d** 段（去掉孤立 `$`），并在段落上标 `flags:[\"unbalanced_math\"]`" % n_unbal,
            "",
            "## 字段变化（相对 v2）", "",
            "- 新增 `zh_chars`（汉字数，可用于按语言纯度过滤或配比采样）",
            "- 新增 `near_dup_of`（近重复指向首个出现，**不删除**）",
            "- 新增 `flags`（`placeholder_in_math` / `unbalanced_math`，仅在有修复时出现）",
            ]
    io.open(os.path.join(out, "QA_REPORT.md"), "w", encoding="utf-8", newline="\n").write("\n".join(rep) + "\n")
    print("written ->", dst)


if __name__ == "__main__":
    main()
