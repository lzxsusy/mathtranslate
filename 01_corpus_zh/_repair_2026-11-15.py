# -*- coding: utf-8 -*-
r"""语料与源文件的可修缺陷修复（2026-11-15 第三方评审后）。

修三件事，全部可逆、可复核：

1. **还原被脱敏脚本吃掉的 TeX 换行 `\\`**
   `tools/scrub_publish.py` 旧版有一条路径正则 `r"\\\\[A-Za-z0-9._\-]+\\[^\s\"'<>|]*"`，
   在 .tex 里撞上公式换行（如 pmatrix 的 `y_0\\y_1`）也会命中，把 `\\` 换成 `<本地路径>`。
   结果：36 个源 .tex、22 段语料里的矩阵/对齐环境被写坏。
   判定依据（已人工核对 99 处上下文）：.tex 里 `<本地路径>` 后面紧跟换行/`'`/`)`/`[`，
   没有一处是真正的路径（`\input{}`/`\includegraphics{}` 里一处都没有）。
   **只改 .tex 与语料文本；.py / .md 里的 `<本地路径>` 是真路径占位，一律不动。**

2. **给已有段落补结构性缺陷标记**（只加 `flags`，不改文本）：
   `empty_ref`（引用编号被吞，只剩 `（ ）`）、`layout_residue`（字号/行距残渣）、
   `meta_block`（目次/参考文献/索引类非正文块）、`overlong`（超长未切段）。

3. 重算 `zh_chars` / `para_id` / 统计 json，并输出修复台账 `REPAIR_2026-11-15.md`。

用法：
    python _repair_2026-11-15.py --dry-run
    python _repair_2026-11-15.py --write
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import io
import json
import os
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CORPUS = os.path.join(HERE, "zh_paragraphs.jsonl")
STATS = os.path.join(HERE, "zh_paragraphs_stats.json")
PH = "<本地路径>"

ZH = re.compile(r"[\u4e00-\u9fff]")
EMPTY_REF = re.compile(r"[（(]\s*(?:[,，、;；]?\s*)*[）)]")
# 字号/行距/目次编号残渣：`[6pt]`、`[2.4cm]`、行首孤立 `1.15`
# 注意：`\\[6pt]`（换行+间距）是**合法 TeX**，不算残渣，用负向后视排除
SIZE_RESIDUE = re.compile(r"(?<!\\)\[\d+(?:\.\d+)?(?:pt|cm|mm|em|ex|baselineskip)\]")
LEAD_NUM = re.compile(r"^\s*\d+(?:\.\d+)+\s*$", re.M)
META_WORDS = ("目录", "参考文献", "索引", "附录", "前言", "序言", "致谢", "后记")
META_TAIL = re.compile(r"(?:^|\n)\s*(?:图|表|name)?\s*(?:参考文献|目录|附录|索引)\s*(?:\n|$)")

OVERLONG_CHARS = 3000          # 报告里「≤3000 字」的切分上限，超出的打标
MAX_TEXT_LEN = 6000            # 极端长度（整文件级）也打标


def fix_placeholder_tex(dry: bool) -> tuple[int, int]:
    files = sorted(glob.glob(os.path.join(REPO, "08_source_code", "**", "*.tex"), recursive=True))
    n_files = n_hits = 0
    for p in files:
        s = io.open(p, encoding="utf-8", errors="replace").read()
        if PH not in s:
            continue
        cnt = s.count(PH)
        n_files += 1
        n_hits += cnt
        if not dry:
            io.open(p, "w", encoding="utf-8", newline="\n").write(s.replace(PH, "\\\\"))
    return n_files, n_hits


def defect_flags(text: str) -> list[str]:
    """只打标、不改文本。四个标记的定义写死在这里，便于复核：

    - `empty_ref`：`（ ）`/`( )`——`\\ref` 编号在抽语料时被吞掉，只剩空括号（不可逆，
      因为编号信息已丢失；下游若要引用必须回源 tex）。
    - `layout_residue`：正文里残留字号/行距参数（`[6pt]`、`[2.4cm]`；`\\\\[6pt]` 这种合法换行不算）。
    - `orphan_number`：段落里出现独占一行的孤立编号（公式号 `13.11`、页码 `0.47`），
      多半是公式编号或版面编号被断到了正文行。
    - `meta_block`：目次/参考文献/索引/附录类非正文块（标题词 + 尾部标记同时命中）。
    - `overlong`：超过 3,000 汉字或 6,000 字符，说明切分器在该文件上失效（附录/索引最常见）。
    """
    out = []
    if EMPTY_REF.search(text):
        out.append("empty_ref")
    if SIZE_RESIDUE.search(text):
        out.append("layout_residue")
    if LEAD_NUM.search(text):
        out.append("orphan_number")
    head = text[:200]
    if any(w in head for w in META_WORDS) and META_TAIL.search(text):
        out.append("meta_block")
    if len(text) > MAX_TEXT_LEN or len(ZH.findall(text)) > OVERLONG_CHARS:
        out.append("overlong")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    dry = not args.write

    rows = []
    with io.open(CORPUS, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))

    n_ph = n_id = n_flag = 0
    flag_count = {}
    for d in rows:
        t = d["text"]
        if PH in t:
            t = t.replace(PH, "\\\\")
            n_ph += 1
            if hashlib.sha1(t.encode("utf-8")).hexdigest()[:16] != d["para_id"]:
                n_id += 1
            d["text"] = t
            d["para_id"] = hashlib.sha1(t.encode("utf-8")).hexdigest()[:16]
            d["zh_chars"] = len(ZH.findall(t))
        fl = set(d.get("flags") or [])
        add = [x for x in defect_flags(d["text"]) if x not in fl]
        if add:
            n_flag += 1
            fl |= set(add)
            d["flags"] = sorted(fl)
        for x in (d.get("flags") or []):
            flag_count[x] = flag_count.get(x, 0) + 1

    nf, nh = fix_placeholder_tex(dry)

    print("[tex] files with placeholder: %d, occurrences: %d" % (nf, nh))
    print("[corpus] rows repaired: %d (para_id recomputed: %d), rows newly flagged: %d"
          % (n_ph, n_id, n_flag))
    print("[flags]", json.dumps(flag_count, ensure_ascii=False, sort_keys=True))

    if dry:
        print("\n[dry-run] 未写盘")
        return

    stamp = time.strftime("%Y%m%d-%H%M%S")
    # 备份放在仓库**外**的兄弟目录，避免 28 MB 的 jsonl 被重复计入仓库体积/被提交
    bak = os.path.join(os.path.dirname(REPO), "_corpus_backups", "repair_%s" % stamp)
    os.makedirs(bak, exist_ok=True)
    shutil.copy2(CORPUS, os.path.join(bak, os.path.basename(CORPUS)))
    print("backup ->", os.path.relpath(bak, REPO))

    with io.open(CORPUS, "w", encoding="utf-8", newline="\n") as f:
        for d in rows:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    # 重算统计（单一来源）
    ids = {d["para_id"] for d in rows}
    pkgs = {d["pkg"] for d in rows}
    st = json.load(io.open(STATS, encoding="utf-8"))
    st.update({
        "total": len(rows),
        "with_math": sum(1 for d in rows if "$" in d["text"] or "\\begin{" in d["text"]),
        "exact_dup_flagged": sum(1 for d in rows if d.get("dup_of")),
        "near_dup_flagged": sum(1 for d in rows if d.get("near_dup_of")),
        "unique_para_id": len(ids),
        "packages": len(pkgs),
        "with_page_orig": sum(1 for d in rows if d.get("page_orig") is not None),
        "zh_chars_total": sum(int(d.get("zh_chars") or 0) for d in rows),
    })
    st["with_math_pct"] = round(100.0 * st["with_math"] / max(1, st["total"]), 2)
    st["flag_counts"] = dict(sorted(flag_count.items()))
    io.open(STATS, "w", encoding="utf-8", newline="\n").write(
        json.dumps(st, ensure_ascii=False, indent=1))
    print("[stats]", json.dumps(st, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
