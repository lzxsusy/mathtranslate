# -*- coding: utf-8 -*-
r"""make_train_subset.py —— 从 zh_paragraphs.jsonl 生成"可直接进训练"的干净子集。

用途：测评报告（2026-11-20）P1-2 指出，原始语料里含 `empty_ref`、`orphan_number`
等标注段落，"训练前应过滤"。本脚本把这条建议固化成一条命令，避免每个人各写一版
过滤逻辑、过滤口径还不一致。

口径（默认，可按需覆盖）：
  - 丢弃 flags 命中 DROP_FLAGS 的段落（公式引用残缺、编号孤立、版式残渣等）；
  - 丢弃汉字段过短的段落（< 8 字，多为标题碎片）；
  - 按 `para_id` 去重（保留首次出现）；
  - 只保留非空 `text`。

注意：**不**删除 `near_dup_of` 段落（近重复仍可用于蒸馏，只是别重复计数）；
需要更严的口径就自己加 `--drop-flag near_dup_of`。

用法：
    python tools/make_train_subset.py                      # 写 01_corpus_zh/zh_train.jsonl.gz
    python tools/make_train_subset.py --stats              # 只报数，不写文件
    python tools/make_train_subset.py --drop-flag overlong # 额外丢某类
    python tools/make_train_subset.py -o /tmp/train.jsonl.gz

产物默认被 .gitignore 忽略（体积大，按需生成，不随仓发布）。
"""
from __future__ import annotations

import argparse
import collections
import gzip
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "01_corpus_zh", "zh_paragraphs.jsonl")
DEFAULT_OUT = os.path.join(REPO, "01_corpus_zh", "zh_train.jsonl.gz")

# 这些 flags 表示"这一段拿出来单独训练会教坏模型"：缺公式引用、编号无主、版式残渣。
DROP_FLAGS = {"empty_ref", "orphan_number", "layout_residue", "junk_trimmed",
              "meta_block", "unbalanced_math", "placeholder_in_math"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default=DEFAULT_OUT)
    ap.add_argument("--min-chars", type=int, default=8)
    ap.add_argument("--drop-flag", action="append", default=[],
                    help="额外要丢弃的 flag，可重复")
    ap.add_argument("--keep-flag", action="append", default=[],
                    help="从默认丢弃集合里豁免某个 flag，可重复")
    ap.add_argument("--stats", action="store_true", help="只统计，不写文件")
    a = ap.parse_args()

    drop = (DROP_FLAGS | set(a.drop_flag)) - set(a.keep_flag)
    total = kept = 0
    dropped = collections.Counter()
    seen = set()
    kept_rows = []

    with io.open(SRC, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            r = json.loads(line)
            text = (r.get("text") or "").strip()
            if not text:
                dropped["empty_text"] += 1
                continue
            bad = [fl for fl in (r.get("flags") or []) if fl in drop]
            if bad:
                dropped[bad[0]] += 1
                continue
            if int(r.get("zh_chars") or 0) < a.min_chars:
                dropped["too_short"] += 1
                continue
            pid = r.get("para_id") or ""
            if pid and pid in seen:
                dropped["dup_para_id"] += 1
                continue
            if pid:
                seen.add(pid)
            kept_rows.append(r)
            kept += 1

    zh = sum(int(r.get("zh_chars") or 0) for r in kept_rows)
    fml = sum(1 for r in kept_rows if "$" in r["text"] or "\\begin{" in r["text"])
    print("源段落 %s 段 → 训练子集 %s 段（丢弃 %s 段）"
          % ("{:,}".format(total), "{:,}".format(kept), "{:,}".format(total - kept)))
    for k, v in dropped.most_common():
        print("  - %-18s %s 段" % (k, "{:,}".format(v)))
    print("子集汉字 %s，含公式 %s 段（%.0f%%）"
          % ("{:,}".format(zh), "{:,}".format(fml),
             100.0 * fml / max(1, kept)))

    if a.stats:
        return 0
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with gzip.open(a.out, "wt", encoding="utf-8", compresslevel=6) as g:
        for r in kept_rows:
            g.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("已写出 %s（%.1f MB）" % (a.out, os.path.getsize(a.out) / 1048576.0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
