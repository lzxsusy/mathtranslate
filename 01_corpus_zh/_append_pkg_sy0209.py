# -*- coding: utf-8 -*-
r"""把 SY02-09《Langlands 纲领导论》增量追加进 01_corpus_zh。

与 _append_pkg.py 的差异（本工程 TeX 用 `\sourcepage{原书页}` 做页锚点，没有段落 id 锚点）：
  * ANCHOR 改为 `\sourcepage{(\d+)}`，`\sourcepage` 之后到下一个 `\sourcepage` 之间的文字归该原书页；
  * 术语从 `terminology.tsv`（两列：English<TAB>中文）读；
  * tier = B。

用法：
    python _append_pkg_sy0209.py --dry-run
    python _append_pkg_sy0209.py
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

REPO = r"<本地路径>"
CORPUS = os.path.join(REPO, "01_corpus_zh", "zh_paragraphs.jsonl")
STATS = os.path.join(REPO, "01_corpus_zh", "zh_paragraphs_stats.json")
TERMBASE = os.path.join(REPO, "01_corpus_zh", "termbase.jsonl")
PKG_ROOT = os.path.join(REPO, "08_source_code", "SY02-09_Langlands纲领导论", "源码")
PKG = "SY02-09"
TIER = "B"
ZH = re.compile(r"[\u4e00-\u9fff]")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tex_clean import expand as _expand, strip_unbalanced_braces as _strip_braces
from _tex_clean_sy0209 import preclean as _preclean

TEX_EXPAND = lambda s: _strip_braces(_expand(_preclean(s)))
ENV_MARKER = re.compile(
    r"\\(?:begin|end)\{(?:document|definition|theorem|proposition|lemma|corollary|"
    r"example|remark|proof|conjecture|exercise|solution|letteraxiom|lettertheorem|"
    r"center|itemize|enumerate|quote|minipage|tabular|figure|table)\}"
)

ANCHOR = re.compile(r"\\sourcepage\{(\d+)\}")
FIG_ENV = re.compile(r"\\begin\{figure\}.*?\\end\{figure\}", re.S)
TABLE_ENV = re.compile(r"\\begin\{(table|longtable)\}.*?\\end\{\1\}", re.S)
SECTION_LINE = re.compile(r"^\s*\\(?:chapter|section|subsection|subsubsection|paragraph|part)\*?\{")
JUNK_TAIL = re.compile(r"[\s\d.ptemex]{6,}$", re.I)


def clean_text(t: str) -> str:
    t = re.sub(r"(?<!\\)%.*$", "", t, flags=re.M)
    t = FIG_ENV.sub("", t)
    t = TABLE_ENV.sub("", t)
    t = TEX_EXPAND(t)
    t = ENV_MARKER.sub("", t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = t.strip()
    t = JUNK_TAIL.sub("", t).strip()
    return t


def is_content(t: str) -> bool:
    if not t:
        return False
    plain = re.sub(r"\$[^$]*\$", "", t)
    if len(ZH.findall(plain)) >= 6:
        return True
    if "\\begin{" in t or "$$" in t or "\\[" in t:
        return True
    return False


def doc_env(chunk: str) -> str:
    for e in re.findall(r"\\begin\{([A-Za-z*]+)\}", chunk):
        if e not in ("document", "figure", "table", "tabular", "minipage", "center",
                     "itemize", "enumerate", "quote"):
            return {"theorem": "theorem", "proposition": "theorem", "lemma": "theorem",
                    "corollary": "theorem", "definition": "definition", "example": "example",
                    "remark": "remark", "conjecture": "theorem", "exercise": "example",
                    "proof": "proof"}.get(e, "text")
    if re.search(r"\\begin\{proof\}", chunk):
        return "proof"
    return "text"


def paragraphs_of_segment(seg: str):
    out = []
    for chunk in re.split(r"\n\s*\n", seg):
        if not chunk.strip():
            continue
        if SECTION_LINE.match(chunk.strip()) and "\\begin{" not in chunk:
            continue
        env = doc_env(chunk)
        t = clean_text(chunk)
        if not is_content(t):
            continue
        out.append((t, env))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    seen = {}
    total_existing = 0
    with io.open(CORPUS, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            total_existing += 1
            seen.setdefault(d["text"].strip(), d["para_id"])
    print("existing paragraphs:", total_existing, "unique texts:", len(seen))

    chapters = os.path.join(PKG_ROOT, "chapters")
    files = sorted(os.path.join(chapters, x) for x in os.listdir(chapters) if x.endswith(".tex"))
    rows = []
    n_page = 0
    for fp in files:
        rel = PKG + "/chapters/" + os.path.basename(fp)
        src = io.open(fp, encoding="utf-8").read()
        parts = ANCHOR.split(src)     # [pre, page1, text1, page2, text2, ...]
        segs = []
        if parts[0].strip():
            segs.append((None, parts[0]))
        for i in range(1, len(parts), 2):
            segs.append((int(parts[i]), parts[i + 1]))
        paras = []
        for page, seg in segs:
            for t, env in paragraphs_of_segment(seg):
                paras.append({"page": page, "env": env, "text": t})
        for idx, p in enumerate(paras, 1):
            pid = hashlib.sha1(p["text"].encode("utf-8")).hexdigest()[:16]
            rec = {"pkg": PKG, "file": rel, "para": idx, "para_id": pid,
                   "page_orig": p["page"], "env": p["env"], "tier": TIER,
                   "text": p["text"], "zh_chars": len(ZH.findall(p["text"]))}
            prev = seen.get(p["text"])
            if prev:
                rec["dup_of"] = prev
            rows.append(rec)
            if p["page"] is not None:
                n_page += 1
        print("%-42s %4d paragraphs" % (rel, len(paras)))

    math = sum(1 for r in rows if "$" in r["text"] or "\\begin{" in r["text"])
    dup = sum(1 for r in rows if r.get("dup_of"))
    leftover = [r for r in rows if re.search(r"\\(?:sourcepage|eref|lref|idx|znote|znoteplain|originalnumber|refitem|bref)", r["text"])]
    print("\nnew rows:", len(rows), "| with_math:", math, "| page_orig:", n_page,
          "| exact_dup:", dup, "| leftover_macro:", len(leftover))
    for r in leftover[:3]:
        print("LEFT:", r["text"][:200])

    if args.dry_run:
        print("\n[dry-run] 未写盘")
        return

    stamp = time.strftime("%Y%m%d-%H%M%S")
    bak = os.path.join(REPO, "_backup_corpus_%s" % stamp)
    os.makedirs(bak, exist_ok=True)
    for p in (CORPUS, STATS, TERMBASE):
        shutil.copy2(p, os.path.join(bak, os.path.basename(p)))
    print("backup ->", bak)

    with io.open(CORPUS, "a", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # 术语：terminology.tsv（English \t 中文）
    added = 0
    existing_terms = set()
    with io.open(TERMBASE, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                d = json.loads(line)
                existing_terms.add((d.get("foreign"), d.get("zh")))
    tsv = os.path.join(PKG_ROOT, "terminology.tsv")
    with io.open(TERMBASE, "a", encoding="utf-8", newline="\n") as f:
        for ln in io.open(tsv, encoding="utf-8").read().splitlines()[1:]:
            c = ln.split("\t")
            if len(c) < 2:
                continue
            en, zh = c[0].strip(), c[1].strip()
            if not en or not zh or (en, zh) in existing_terms:
                continue
            existing_terms.add((en, zh))
            f.write(json.dumps({"foreign": en, "lang": "en", "zh": zh, "status": "candidate",
                                "pkg": PKG, "src_format": "tsv"}, ensure_ascii=False) + "\n")
            added += 1
    print("terms added:", added)

    tot = math2 = pages = zhsum = dup2 = near = 0
    pkgs = set()
    ids = set()
    with io.open(CORPUS, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            d = json.loads(line)
            tot += 1
            if "$" in d["text"] or "\\begin{" in d["text"]:
                math2 += 1
            if d.get("page_orig") is not None:
                pages += 1
            if d.get("dup_of"):
                dup2 += 1
            if d.get("near_dup_of"):
                near += 1
            zhsum += int(d.get("zh_chars") or 0)
            pkgs.add(d["pkg"])
            ids.add(d["para_id"])
    old = json.load(io.open(STATS, encoding="utf-8"))
    st = {"total": tot, "dropped_junk": old.get("dropped_junk", 0),
          "junk_trimmed": old.get("junk_trimmed", 0),
          "with_math": math2, "with_math_pct": round(100.0 * math2 / tot, 2),
          "exact_dup_flagged": dup2, "near_dup_flagged": near,
          "placeholder_in_math_fixed": old.get("placeholder_in_math_fixed", 0),
          "unbalanced_math_fixed": old.get("unbalanced_math_fixed", 0),
          "unique_para_id": len(ids), "packages": len(pkgs),
          "with_page_orig": pages, "zh_chars_total": zhsum}
    io.open(STATS, "w", encoding="utf-8", newline="\n").write(
        json.dumps(st, ensure_ascii=False, indent=1))
    print(json.dumps(st, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
