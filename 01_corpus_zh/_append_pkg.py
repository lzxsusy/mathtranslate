# -*- coding: utf-8 -*-
r"""Incrementally append one package (SY01-23) to 01_corpus_zh.

比 v3 多一件事：本工程的 TeX 用 `\SourceParagraph{id}{原书PDF页号}` 做段落锚点，
所以这里**按锚点切段**，每段都能带上 page_orig（原书 PDF 页号），比全库平均覆盖率高得多。

用法：
    python _append_pkg.py --dry-run       # 只统计、抽样打印，不写盘
    python _append_pkg.py                 # 追加并刷新 stats
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

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(REPO, "01_corpus_zh", "zh_paragraphs.jsonl")
STATS = os.path.join(REPO, "01_corpus_zh", "zh_paragraphs_stats.json")
TERMBASE = os.path.join(REPO, "01_corpus_zh", "termbase.jsonl")
PKG_ROOT = os.path.join(REPO, "08_source_code", "SY01-23_Dirichlet 膜与镜像对称（Clay 专著）", "源码")
PKG = "SY01-23"
TIER = "A"
ZH = re.compile(r"[\u4e00-\u9fff]")

from _tex_clean import expand as _expand, strip_unbalanced_braces as _strip_braces

TEX_EXPAND = lambda s: _strip_braces(_expand(s))
ENV_MARKER = re.compile(
    r"\\(?:begin|end)\{(?:document|definition|theorem|proposition|lemma|corollary|"
    r"example|remark|proof|conjecture|exercise|solution|letteraxiom|lettertheorem|"
    r"center|itemize|enumerate|quote|minipage|tabular|figure|table)\}"
)

ANCHOR = re.compile(r"\\SourceParagraph\{([^}]*)\}\{(\d+)\}")
FIG_ENV = re.compile(r"\\begin\{figure\}.*?\\end\{figure\}", re.S)
TABLE_ENV = re.compile(r"\\begin\{(table|longtable)\}.*?\\end\{\1\}", re.S)
CMD_DROP = re.compile(
    r"\\(?:cite|citep|citet|ref|eqref|label|index|nocite|pageref)\{[^}]*\}"
)
MACRO_TWO = re.compile(
    r"\\(BookRef|BookEqRef|BookSectionRef|BookChapterRef|BookTableRef)\{([^}]*)\}\{([^}]*)\}"
)
OTHER_REF = re.compile(r"\\BookChapterRef\{([^}]*)\}")


def ref_to_text(m: re.Match) -> str:
    kind, _label, disp = m.group(1), m.group(2), m.group(3)
    if kind == "BookEqRef":
        return "(%s)" % disp
    if kind == "BookSectionRef":
        return "第 %s 节" % disp
    if kind in ("BookChapterRef", "BookTableRef"):
        return "第 %s 章" % disp
    return disp
MACRO_ONE_DROP = re.compile(
    r"\\(?:BookImage|BookIndex|SourceParagraph|addcontentsline|index)\b(?:\{[^}]*\})*"
)
BOOKCITE = re.compile(r"\\BookCite\{ref0*(\d+)\}")
UNWRAP = re.compile(r"\\(?:emph|textbf|textit|textrm|textsf|texttt|text|underline|mbox)\{")
ENV_BEGIN = re.compile(r"^\s*\\begin\{([A-Za-z*]+)\}")
SECTION_LINE = re.compile(
    r"^\s*\\(?:chapter|section|subsection|subsubsection|paragraph|part)\*?\{"
)
PURE_CMD = re.compile(
    r"^\s*\\(?:chapter|section|subsection|subsubsection|part|label|SourceParagraph|"
    r"addcontentsline|setcounter|clearpage|newpage|noindent|indent|vspace|hspace|"
    r"input|include|tableofcontents|maketitle|frontmatter|mainmatter|backmatter|"
    r"nocite|printbibliography|addbibresource|documentclass|usepackage|title|author|"
    r"date|cover|BookImage|centering|small|footnotesize|normalsize|Large|large|"
    r"begin|end|caption|BookNumberOnlyCaption|item|par|medskip|bigskip|"
    r"chaptermark|markboth|thispagestyle|pagenumbering|appendix|def|newcommand)"
)
JUNK_TAIL = re.compile(r"[\s\d.ptemex]{6,}$", re.I)


def unwrap_all(s: str) -> str:
    r"""下行兼容用。旧实现用 `UNWRAP.sub("", s)` 直接删 `\cmd{`，
    会把 `\mathrm{e}^{2\pi i}` 剥成 `e}^{2\pi i}`（闭合括号留在外面），
    这里是不可配平的坏公式来源之一，已改为走 _tex_clean 的配平展开。"""
    return _expand(s)


def clean_text(t: str) -> str:
    t = re.sub(r"(?<!\\)%.*$", "", t, flags=re.M)          # 注释
    t = FIG_ENV.sub("", t)
    t = TABLE_ENV.sub("", t)
    t = TEX_EXPAND(t)                                       # 宏展开（_tex_clean）
    t = ENV_MARKER.sub("", t)                               # 删 \begin{...}/\end{...} 标记
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = t.strip()
    t = JUNK_TAIL.sub("", t).strip()
    return t


def is_content(t: str) -> bool:
    if not t:
        return False
    plain = re.sub(r"\$[^$]*\$", "", t)
    nzh = len(ZH.findall(plain))
    if nzh >= 6:
        return True
    if "\\begin{" in t or "$$" in t or "\\[" in t:
        return True
    return False


def doc_env(chunk: str) -> str:
    envs = re.findall(r"\\begin\{([A-Za-z*]+)\}", chunk)
    for e in envs:
        if e not in ("document", "figure", "table", "tabular", "minipage", "center", "itemize", "enumerate", "quote"):
            return {"theorem": "theorem", "proposition": "theorem", "lemma": "theorem",
                    "corollary": "theorem", "definition": "definition", "example": "example",
                    "remark": "remark", "conjecture": "theorem", "exercise": "example",
                    "proof": "proof"}.get(e, "text")
    if re.search(r"\\begin\{proof\}", chunk):
        return "proof"
    return "text"


def paragraphs_of_segment(seg: str):
    """把一段文本按空行切成段落；返回 [(text, env)]。"""
    out = []
    for chunk in re.split(r"\n\s*\n", seg):
        if not chunk.strip():
            continue
        head = chunk.strip()
        # 纯标题行 / 纯命令块：不算正文段落
        if SECTION_LINE.match(head) and "\\begin{" not in head:
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

    # 已有 corpus 的 text -> para_id（精确重复判定）
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
    files = sorted([os.path.join(chapters, x) for x in os.listdir(chapters) if x.endswith(".tex")])
    rows = []
    n_page = 0
    for fp in files:
        rel = PKG + "/" + os.path.relpath(fp, os.path.dirname(PKG_ROOT)).replace("\\", "/")
        src = io.open(fp, encoding="utf-8").read()
        parts = ANCHOR.split(src)   # [pre, id1, page1, text1, id2, page2, ...]
        pre = parts[0]
        segs = []
        if pre.strip():
            segs.append((None, pre))
        for i in range(1, len(parts), 3):
            pid, page, txt = parts[i], int(parts[i + 1]), parts[i + 2]
            segs.append((page, txt))
        paras = []
        for page, seg in segs:
            for t, env in paragraphs_of_segment(seg):
                paras.append({"page": page, "env": env, "text": t})
        for idx, p in enumerate(paras, 1):
            pid = hashlib.sha1(p["text"].encode("utf-8")).hexdigest()[:16]
            rec = {
                "pkg": PKG,
                "file": rel,
                "para": idx,
                "para_id": pid,
                "page_orig": p["page"],
                "env": p["env"],
                "tier": TIER,
                "text": p["text"],
                "zh_chars": len(ZH.findall(p["text"])),
            }
            prev = seen.get(p["text"])
            if prev and prev != pid:
                rec["dup_of"] = prev
            elif prev == pid:
                rec["dup_of"] = prev   # 内容哈希相同即同段，标为重复更安全
            rows.append(rec)
            if p["page"] is not None:
                n_page += 1
        print("%-46s %4d paragraphs" % (rel, len(paras)))

    math = sum(1 for r in rows if "$" in r["text"] or "\\begin{" in r["text"])
    dup = sum(1 for r in rows if r.get("dup_of"))
    leftover = [r for r in rows if re.search(r"\\(?:Book|SourceParagraph|cite|ref|label|BookImage|BookCite)", r["text"])]
    print("\nnew rows:", len(rows), "| with_math:", math, "| page_orig:", n_page, "| exact_dup:", dup,
          "| leftover_macro:", len(leftover))
    for r in leftover[:3]:
        print("LEFT:", r["text"][:200])
    for r in rows[:3]:
        print(json.dumps(r, ensure_ascii=False)[:300])

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

    # 术语表：glossary.csv -> termbase（en）
    added_terms = 0
    existing_terms = set()
    with io.open(TERMBASE, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                d = json.loads(line)
                existing_terms.add((d.get("foreign"), d.get("zh")))
    gcsv = os.path.join(PKG_ROOT, "glossary.csv")
    with io.open(TERMBASE, "a", encoding="utf-8", newline="\n") as f:
        import csv
        with io.open(gcsv, encoding="utf-8", newline="") as g:
            rd = csv.DictReader(g)
            for row in rd:
                en = (row.get("english") or "").strip()
                zh = (row.get("chinese") or "").strip()
                if not en or not zh or (en, zh) in existing_terms:
                    continue
                existing_terms.add((en, zh))
                rec = {"foreign": en, "lang": "en", "zh": zh, "status": "candidate",
                       "pkg": PKG, "src_format": "csv"}
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                added_terms += 1
    print("terms added:", added_terms)

    # 重算 stats
    tot = math2 = uniq = pages = zhsum = dup2 = near = 0
    pkgs = set()
    with io.open(CORPUS, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
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
            uniq += 1  # placeholder
    ids = set()
    with io.open(CORPUS, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                ids.add(json.loads(line)["para_id"])
    old = json.load(io.open(STATS, encoding="utf-8"))
    st = {
        "total": tot,
        "dropped_junk": old.get("dropped_junk", 0),
        "junk_trimmed": old.get("junk_trimmed", 0),
        "with_math": math2,
        "with_math_pct": round(100.0 * math2 / tot, 2),
        "exact_dup_flagged": dup2,
        "near_dup_flagged": near,
        "placeholder_in_math_fixed": old.get("placeholder_in_math_fixed", 0),
        "unbalanced_math_fixed": old.get("unbalanced_math_fixed", 0),
        "unique_para_id": len(ids),
        "packages": len(pkgs),
        "with_page_orig": pages,
        "zh_chars_total": zhsum,
    }
    io.open(STATS, "w", encoding="utf-8", newline="\n").write(
        json.dumps(st, ensure_ascii=False, indent=1))
    print(json.dumps(st, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
