#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成「数语规范」表：TERMS.tsv / SYMBOLS.tsv / CONFLICTS.tsv / MACROS.tsv / INDEX.md

用法：
  python tools/build_norm.py            # 重新生成全部表
  python tools/build_norm.py --check    # 只比对，不写盘；与已提交的表不一致则 exit 1

数据源（只读）：
  01_corpus_zh/termbase.jsonl            术语基
  01_corpus_zh/terms_frozen_*.tsv        工程冻结术语表（英文/中文/等级/依据/首次出现/备注）
  01_corpus_zh/symbols_frozen_*.tsv      工程冻结记号表（记号/LaTeX 源码/读法·中文名/含义/首次出现/依据）
  08_source_code/**/*.tex                宏声明（\\newcommand / \\renewcommand / \\providecommand /
                                         \\DeclareMathOperator / \\def），用于发现「同名异义」的记法冲突

输出（写入 01_corpus_zh/数语规范/）：
  TERMS.tsv      合并后的统一术语表（一条译名一行，标等级与来源）
  SYMBOLS.tsv    合并后的统一记号表
  CONFLICTS.tsv  译名层冲突（一外多中 / 一中多外 / 空格与连字符 / 等级不一致 / 命名不合规）
  MACROS.tsv     LaTeX 宏跨工程比对，含「真冲突 / 写法差异」判定
  INDEX.md       汇总与优先处理清单

口径说明见 01_corpus_zh/数语规范/README.md。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "01_corpus_zh")
OUT = os.path.join(CORPUS, "数语规范")
SRC = os.path.join(ROOT, "08_source_code")
OUT_REL = os.path.join("01_corpus_zh", "数语规范")

LEVEL_RANK = {"A": 0, "B": 1, "I": 2, "D": 3}
LEVEL_DESC = {
    "A": "原文页码/式号锚定",
    "B": "外部权威（nLab 等）",
    "I": "本库定案",
    "D": "未标级（待考）",
}
SEVERITY = {"高": 0, "中": 1, "低": 2}

# LaTeX 内部寄存器：各工程按版面自行调值，不属于术语层面的记法冲突
MACRO_BLACKLIST = {
    "headrulewidth", "footrulewidth", "arraystretch", "baselineskip", "fboxrule", "fboxsep",
    "parindent", "parskip", "columnsep", "tabcolsep", "linespread", "topmargin", "oddsidemargin",
    "evensidemargin", "textwidth", "textheight", "hoffset", "voffset", "emergencystretch",
}


def nk(s: str) -> str:
    """外文规范化键：压缩空白、统一连接号、拉丁部分小写。"""
    s = (s or "").strip()
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = re.sub(r"\s+", " ", s)
    return s.casefold()


def nz(s: str) -> str:
    """中文名规范化键：去掉全部空白、统一连接号与全角括号，用于判断「只是写法不同」。"""
    s = (s or "").strip()
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = s.replace("（", "(").replace("）", ")")
    s = re.sub(r"\s+", "", s)
    return s


def clean(s) -> str:
    return re.sub(r"[\t\r\n]+", " ", str(s or "")).strip()


def read_jsonl(path: str) -> list[dict]:
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def read_tsv(path: str) -> list[list[str]]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig") as fh:
        return [ln.rstrip("\n").split("\t") for ln in fh if ln.strip()]


def pkg_of(filename: str) -> str:
    m = re.match(r"(?:terms|symbols)_frozen_(.+)\.tsv$", os.path.basename(filename))
    return m.group(1) if m else os.path.basename(filename)


def frozen_files(prefix: str) -> list[str]:
    return sorted(os.path.join(CORPUS, f) for f in os.listdir(CORPUS) if f.startswith(prefix))


# ---------------------------------------------------------------------------
# 1. 术语与记号
# ---------------------------------------------------------------------------
def load_terms() -> list[dict]:
    rows: list[dict] = []
    for rec in read_jsonl(os.path.join(CORPUS, "termbase.jsonl")):
        rows.append(
            {
                "foreign": clean(rec.get("foreign")),
                "lang": clean(rec.get("lang")) or "en",
                "zh": clean(rec.get("zh")),
                "level": clean(rec.get("level")).upper() or "D",
                "status": clean(rec.get("status")) or "candidate",
                "evidence": clean(rec.get("source")),
                "where": clean(rec.get("lecture")) or "—",
                "pkg": clean(rec.get("pkg")) or "—",
                "frozen": False,
            }
        )
    for path in frozen_files("terms_frozen_"):
        pkg = pkg_of(path)
        for cells in read_tsv(path)[1:]:
            cells = cells + [""] * (6 - len(cells))
            foreign, zh, level, evidence, where, note = cells[:6]
            if not foreign.strip() or foreign.lstrip().startswith("#"):
                continue
            rows.append(
                {
                    "foreign": clean(foreign),
                    "lang": "en",
                    "zh": clean(zh),
                    "level": clean(level).upper() or "D",
                    "status": "frozen",
                    "evidence": clean(evidence),
                    "where": clean(where) or "—",
                    "pkg": pkg,
                    "frozen": True,
                    "note": clean(note),
                }
            )
    return [r for r in rows if r["foreign"] and r["zh"]]


def merge_terms(rows: list[dict]) -> list[dict]:
    """同一 (外文, 语种, 译名, 工程) 只留一条；等级高者、有依据者、冻结表优先。"""
    best: dict[tuple, dict] = {}
    for r in rows:
        key = (nk(r["foreign"]), r["lang"], r["zh"], r["pkg"])
        cur = best.get(key)
        if cur is None:
            best[key] = dict(r)
            continue
        cand = (LEVEL_RANK.get(r["level"], 3), 0 if r["evidence"] else 1, 0 if r["frozen"] else 1)
        prev = (LEVEL_RANK.get(cur["level"], 3), 0 if cur["evidence"] else 1, 0 if cur["frozen"] else 1)
        if cand < prev:
            best[key] = dict(r)
        else:
            if not cur.get("evidence") and r.get("evidence"):
                cur["evidence"] = r["evidence"]
            if cur["level"] == "D" and r["level"] != "D":
                cur["level"] = r["level"]
    out = sorted(best.values(), key=lambda r: (r["lang"], nk(r["foreign"]), nz(r["zh"]), r["pkg"]))
    for i, r in enumerate(out, 1):
        r["id"] = f"T{i:04d}"
    return out


def load_symbols() -> list[dict]:
    rows: list[dict] = []
    for path in frozen_files("symbols_frozen_"):
        pkg = pkg_of(path)
        group = ""
        for cells in read_tsv(path)[1:]:
            if len(cells) == 1 and cells[0].lstrip().startswith("##"):
                group = cells[0].lstrip("#").strip()
                continue
            cells = cells + [""] * (6 - len(cells))
            tok, latex, read, meaning, where, evidence = cells[:6]
            if not tok.strip():
                continue
            rows.append(
                {
                    "token": clean(tok),
                    "latex": clean(latex),
                    "read": clean(read),
                    "meaning": clean(meaning),
                    "where": clean(where) or "—",
                    "evidence": clean(evidence),
                    "pkg": pkg,
                    "group": group,
                }
            )
    for i, r in enumerate(rows, 1):
        r["id"] = f"S{i:04d}"
    return rows


# ---------------------------------------------------------------------------
# 2. 冲突
# ---------------------------------------------------------------------------
def zh_naming_issues(zh: str) -> list[tuple[str, str]]:
    """只报机械可判、且确实不该出现在术语表里的写法。

    刻意不检查：含拉丁字母（人名/算子名是常规写法）、半角括号与数学符号（如 `(A∞,2)-范畴`）、
    长度（`Cauchy–Riemann 方程` 这类长名合法）、以「的」结尾（`半稳定的` 是合法的形容词条目）。
    """
    out = []
    if re.search(r"[，。、；：？！]", zh):
        out.append(("含句读", "术语名里出现句子标点，说明是从正文抽句时切下的残片"))
    if re.match(r"^(的|其|此|该|这|那|所|若|故|则)", zh):
        out.append(("以虚词开头", "抽句切分残留，术语表里只收名词/形容词性条目"))
    return out


def build_conflicts(terms: list[dict]) -> list[dict]:
    rows: list[dict] = []

    # 2.1 同一外文 → 多个中文（按 norm 判：真不同 vs 只是空格/连字符写法）
    by_foreign: dict[tuple, list[dict]] = defaultdict(list)
    for r in terms:
        by_foreign[(nk(r["foreign"]), r["lang"])].append(r)
    for (_fk, lang), group in sorted(by_foreign.items()):
        variants: dict[str, list[dict]] = defaultdict(list)
        raw: dict[str, str] = {}
        for r in group:
            variants[nz(r["zh"])].append(r)
            raw.setdefault(nz(r["zh"]), r["zh"])
        if len(variants) == 1:
            keys = {r["zh"] for r in group}
            if len(keys) > 1:
                all_levels = sorted({r["level"] for r in group})
                rows.append(
                    {
                        "类型": "空格/连字符不一致",
                        "键": group[0]["foreign"],
                        "候选": " ｜ ".join(f"「{k}」" for k in sorted(keys)),
                        "来源": "/".join(sorted({r["pkg"] for r in group})),
                        "建议": "同一译名的排版写法；统一后改源表，中文与拉丁名之间留一个空格、与专名连写不加空格",
                        "严重度": "低",
                    }
                )
            continue
        # 排序：冻结表优先 > 等级高 > 用例多。
        # 「冻结」是本库的显式裁决，必须压过别的工程在 A/B 级里留下的自用译名——
        # 否则一个工程把 stack 译作「栈」并标 A（原文页码），就会把全库裁决「叠」挤下去。
        def vkey(kv: tuple[str, list[dict]]) -> tuple[int, int, int]:
            items = kv[1]
            is_frozen = 0 if any(r.get("frozen") for r in items) else 1
            return (is_frozen, min(LEVEL_RANK.get(r["level"], 3) for r in items), -len(items))

        ranked = sorted(variants.items(), key=vkey)
        best_key, best_rows = ranked[0]
        best_frozen = any(r.get("frozen") for r in best_rows)
        best_level = min(LEVEL_RANK.get(r["level"], 3) for r in best_rows)
        cands = " ｜ ".join(
            f"{raw[k]}（{'冻结' if any(r.get('frozen') for r in rs) else ''}"
            f"{'/'.join(sorted({r['level'] for r in rs}))}，{len(rs)} 处）"
            for k, rs in ranked
        )
        decidable = all(vkey((k, rs)) > vkey((best_key, best_rows)) for k, rs in ranked[1:])
        why = "本库冻结" if best_frozen else "等级更高"
        rows.append(
            {
                "类型": "一外多中",
                "键": group[0]["foreign"],
                "候选": cands,
                "来源": "/".join(sorted({r["pkg"] for r in group})),
                "建议": f"取「{raw[best_key]}」（{why}）" if decidable else f"建议「{raw[best_key]}」，需仓主裁决",
                "严重度": "高" if decidable else "中",
            }
        )

    # 2.2 同一中文 → 多个外文：同语种才算撞车，跨语种是同一概念的英/日底本对照
    by_zh: dict[str, list[dict]] = defaultdict(list)
    for r in terms:
        by_zh[nz(r["zh"])].append(r)
    for _z, group in sorted(by_zh.items()):
        for lang in sorted({r["lang"] for r in group}):
            same_lang = [r for r in group if r["lang"] == lang]
            outs = {nk(r["foreign"]): r for r in same_lang}
            if len(outs) < 2:
                continue
            rows.append(
                {
                    "类型": "一中多外",
                    "键": group[0]["zh"],
                    "候选": " ｜ ".join(f"{r['foreign']}（{r['pkg']}）" for r in outs.values()),
                    "来源": "/".join(sorted({r["pkg"] for r in same_lang})),
                    "建议": "确认是多义词还是译名撞车；撞车则给其中一条改名，多义则在术语表加「歧义」标记",
                    "严重度": "中" if lang == "en" else "低",
                }
            )

    # 2.3 同一 (外文, 译名) 等级不一致
    by_pair: dict[tuple, list[dict]] = defaultdict(list)
    for r in terms:
        by_pair[(nk(r["foreign"]), nz(r["zh"]))].append(r)
    for _k, group in sorted(by_pair.items()):
        levels = sorted({r["level"] for r in group})
        if len(levels) < 2:
            continue
        rows.append(
            {
                "类型": "等级不一致",
                "键": f"{group[0]['foreign']} → {group[0]['zh']}",
                "候选": " ｜ ".join(
                    f"{lv}（{'/'.join(sorted({r['pkg'] for r in group if r['level'] == lv}))}）" for lv in levels
                ),
                "来源": "/".join(sorted({r["pkg"] for r in group})),
                "建议": f"统一按 {levels[0]} 级登记（就高不就低），并把依据补进「依据」列",
                "严重度": "低",
            }
        )

    # 2.4 命名不合规（同一译名只报一次）
    seen: set[str] = set()
    for r in terms:
        if nz(r["zh"]) in seen:
            continue
        seen.add(nz(r["zh"]))
        for rule, why in zh_naming_issues(r["zh"]):
            rows.append(
                {
                    "类型": "命名不合规",
                    "键": r["zh"],
                    "候选": f"规则：{rule}",
                    "来源": r["pkg"],
                    "建议": why,
                    "严重度": "低",
                }
            )

    rows.sort(key=lambda r: (SEVERITY.get(r["严重度"], 9), r["类型"], r["键"]))
    return rows


def build_symbol_conflicts(symbols: list[dict]) -> list[dict]:
    rows: list[dict] = []
    by_token: dict[str, list[dict]] = defaultdict(list)
    for r in symbols:
        by_token[r["token"]].append(r)
    for tok, group in sorted(by_token.items()):
        reads = {r["read"] for r in group if r["read"]}
        lat = {r["latex"] for r in group if r["latex"]}
        if len(reads) > 1 or len(lat) > 1:
            rows.append(
                {
                    "类型": "一符多义",
                    "键": tok,
                    "候选": " ｜ ".join(sorted({f"{r['read']} [{r['latex']}]" for r in group})),
                    "来源": "/".join(sorted({r["pkg"] for r in group})),
                    "建议": "同一记号在同一译本内必须唯一；跨工程差异进 MACROS.tsv",
                    "严重度": "高",
                }
            )
    by_read: dict[str, list[dict]] = defaultdict(list)
    for r in symbols:
        if r["read"]:
            by_read[r["read"]].append(r)
    for read, group in sorted(by_read.items()):
        toks = {r["token"] for r in group}
        if len(toks) > 1:
            rows.append(
                {
                    "类型": "同名异符",
                    "键": read,
                    "候选": " ｜ ".join(sorted(toks)),
                    "来源": "/".join(sorted({r["pkg"] for r in group})),
                    "建议": "同一读法对应多个记号；形式化前统一到一个符号",
                    "严重度": "中",
                }
            )
    return rows


# ---------------------------------------------------------------------------
# 3. 宏扫描
# ---------------------------------------------------------------------------
MACRO_DECL = re.compile(
    r"\\(newcommand|renewcommand|providecommand|DeclareMathOperator|def)\*?\s*"
    r"(?:\{\s*\\([A-Za-z@]+)\s*\}|\\([A-Za-z@]+))"
)


def capture_braced(text: str, start: int) -> tuple[str, int]:
    if start >= len(text) or text[start] != "{":
        return "", start
    depth = 0
    i = start
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1 : i], i + 1
        i += 1
    return "", start


def strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        res = []
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "\\" and i + 1 < len(line):
                res.append(line[i : i + 2])
                i += 2
                continue
            if ch == "%":
                break
            res.append(ch)
            i += 1
        out.append("".join(res))
    return "\n".join(out)


def norm_def(body: str) -> str:
    """把同一含义的常见写法折成同一串：去括号/空白，\\Bbb→\\mathbb，\\operatorname{X}/\\text{X}/{\\rm X}→\\mathrm{X}。"""
    s = body
    s = s.replace("\\Bbb", "\\mathbb")
    s = re.sub(r"\\operatorname\*?\{([^{}]*)\}", r"\\mathrm{\1}", s)
    s = re.sub(r"\\text\{([^{}]*)\}", r"\\mathrm{\1}", s)
    s = re.sub(r"\\mathrm\s*\{([^{}]*)\}", r"\\mathrm{\1}", s)
    s = s.replace("\\rm", "\\mathrm")
    s = s.replace("\\left", "").replace("\\right", "")
    s = re.sub(r"[\s{}]", "", s)
    return s


def tracked_tex() -> list[str]:
    """只扫 git 跟踪的 .tex：站点与统计都按「仓库里真实存在的东西」算，
    这里同口径，避免未提交的草稿把宏表带偏。"""
    try:
        out = subprocess.run(
            ["git", "ls-files", "-z", "08_source_code"],
            cwd=ROOT, capture_output=True, check=True,
        ).stdout
        files = [f for f in out.decode("utf-8", "replace").split("\0") if f.endswith(".tex")]
    except (OSError, subprocess.CalledProcessError):
        files = []
        for dirpath, dirnames, filenames in os.walk(SRC):
            dirnames[:] = [d for d in dirnames if d not in {"work", "pages", "figures", "build"}]
            for fn in filenames:
                if fn.endswith(".tex"):
                    files.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    return sorted(files)


def scan_macros() -> list[dict]:
    decls: dict[str, list[dict]] = defaultdict(list)
    for rel in tracked_tex():
        if any(seg in {"work", "pages", "figures", "build"} for seg in rel.split("/")):
            continue
        path = os.path.join(ROOT, rel)
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = strip_comments(fh.read())
        except OSError:
            continue
        if "newcommand" not in text and "DeclareMathOperator" not in text and "\\def" not in text:
            continue
        pkg = os.path.relpath(path, SRC).split(os.sep)[0]
        for m in MACRO_DECL.finditer(text):
            kind = m.group(1)
            name = m.group(2) or m.group(3)
            if not name or name in MACRO_BLACKLIST:
                continue
            pos = m.end()
            while pos < len(text) and text[pos] in " \t":
                pos += 1
            while pos < len(text) and text[pos] == "[":
                close = text.find("]", pos)
                if close < 0:
                    break
                pos = close + 1
                while pos < len(text) and text[pos] in " \t\n":
                    pos += 1
            body, _ = capture_braced(text, pos)
            if not body:
                continue
            # 图内局部临时宏（tikz 里 \def\R{2} 这类单个数字/单词）不算记法冲突
            if kind == "def" and "\\" not in body and len(body) <= 3:
                continue
            decls[name].append(
                {
                    "kind": kind,
                    "body": body.strip(),
                    "norm": norm_def(body),
                    "pkg": pkg,
                    "file": os.path.relpath(path, ROOT).replace(os.sep, "/"),
                }
            )

    out = []
    for name, items in sorted(decls.items()):
        by_norm: dict[str, dict] = {}
        spellings = set()
        for it in items:
            spellings.add(it["norm"])
            g = by_norm.setdefault(it["norm"], {"body": it["body"], "pkgs": set(), "files": set()})
            g["pkgs"].add(it["pkg"])
            g["files"].add(it["file"])
        if len(spellings) < 2:
            continue
        pkgs = sorted({p for g in by_norm.values() for p in g["pkgs"]})
        bodies = sorted({g["body"] for g in by_norm.values()})
        out.append(
            {
                "name": name,
                "kind": items[0]["kind"],
                "decls": len(items),
                "variants": len(spellings),
                "pkgs": pkgs,
                "bodies": bodies,
                "verdict": "真冲突",
                "example": sorted({f for g in by_norm.values() for f in g["files"]})[0],
            }
        )
    out.sort(key=lambda m: (-len(m["pkgs"]), -m["variants"], m["name"]))
    return out


# ---------------------------------------------------------------------------
# 4. 输出
# ---------------------------------------------------------------------------
TERMS_HEADER = ["术语ID", "外文", "语种", "中文", "等级", "状态", "依据", "出处", "来源"]
SYMBOLS_HEADER = ["记号ID", "记号", "LaTeX", "读法·中文名", "含义", "出处", "依据", "来源", "分组"]
CONFLICTS_HEADER = ["类型", "键", "候选", "来源", "建议", "严重度"]
MACROS_HEADER = ["宏", "声明方式", "声明数", "不同含义数", "出现工程数", "判定", "含义变体（前 4）", "出现工程", "样例文件"]


def to_tsv(header: list[str], rows: list[list]) -> str:
    lines = ["\t".join(header)]
    for r in rows:
        lines.append("\t".join(clean(c) for c in r))
    return "\n".join(lines) + "\n"


def render(terms, symbols, conflicts, macros) -> dict[str, str]:
    terms_tsv = to_tsv(
        TERMS_HEADER,
        [
            [r["id"], r["foreign"], r["lang"], r["zh"], r["level"], r["status"], r["evidence"], r["where"], r["pkg"]]
            for r in terms
        ],
    )
    symbols_tsv = to_tsv(
        SYMBOLS_HEADER,
        [
            [r["id"], r["token"], r["latex"], r["read"], r["meaning"], r["where"], r["evidence"], r["pkg"], r["group"]]
            for r in symbols
        ],
    )
    conflicts_tsv = to_tsv(
        CONFLICTS_HEADER,
        [[r["类型"], r["键"], r["候选"], r["来源"], r["建议"], r["严重度"]] for r in conflicts],
    )
    macros_tsv = to_tsv(
        MACROS_HEADER,
        [
            [
                m["name"],
                m["kind"],
                m["decls"],
                m["variants"],
                len(m["pkgs"]),
                m["verdict"],
                " ｜ ".join(m["bodies"][:4]),
                "/".join(m["pkgs"]),
                m["example"],
            ]
            for m in macros
        ],
    )

    by_level = Counter(r["level"] for r in terms)
    by_lang = Counter(r["lang"] for r in terms)
    by_status = Counter(r["status"] for r in terms)
    by_ctype = Counter(r["类型"] for r in conflicts)
    by_sev = Counter(r["严重度"] for r in conflicts)
    frozen_n = sum(1 for r in terms if r["status"] == "frozen")
    macro_pkgs = Counter(len(m["pkgs"]) for m in macros)
    macro_top = macros[:8]
    top = [c for c in conflicts if c["严重度"] == "高"]

    lines = [
        "# 数语规范 · 汇总",
        "",
        "> 本文件与同目录 `TERMS.tsv` / `SYMBOLS.tsv` / `CONFLICTS.tsv` / `MACROS.tsv` 由 `tools/build_norm.py` 生成，",
        "> **不要手改**。要改数据，改 `01_corpus_zh/termbase.jsonl`、`terms_frozen_*.tsv`、`symbols_frozen_*.tsv` 后重跑。",
        "",
        "## 一、表规模",
        "",
        "| 表 | 行数 | 覆盖 |",
        "|---|---|---|",
        f"| 术语（TERMS.tsv） | {len(terms)} | {len({r['pkg'] for r in terms})} 个工程；去重键＝外文＋语种＋译名＋工程 |",
        f"| 记号（SYMBOLS.tsv） | {len(symbols)} | {len({r['pkg'] for r in symbols})} 个工程（仅 FUNCTORIALITY 有冻结记号表） |",
        f"| 冲突（CONFLICTS.tsv） | {len(conflicts)} | 高 {by_sev.get('高', 0)} / 中 {by_sev.get('中', 0)} / 低 {by_sev.get('低', 0)} |",
        f"| 宏（MACROS.tsv） | {len(macros)} | 跨工程同名不同含义；其中出现在 ≥5 个工程的 {sum(v for k, v in macro_pkgs.items() if k >= 5)} 个 |",
        "",
        "## 二、术语分级",
        "",
        "| 等级 | 条数 | 含义 |",
        "|---|---|---|",
    ]
    for lv in ["A", "B", "I", "D"]:
        lines.append(f"| {lv} | {by_level.get(lv, 0)} | {LEVEL_DESC[lv]} |")
    lines += [
        "",
        f"语种：en {by_lang.get('en', 0)} / ja {by_lang.get('ja', 0)} / other {by_lang.get('other', 0)}。"
        f"状态：frozen {frozen_n} / confirmed {by_status.get('confirmed', 0)} / candidate {by_status.get('candidate', 0)}。",
        "",
        "## 三、冲突分类",
        "",
        "| 类型 | 条数 | 含义 |",
        "|---|---|---|",
    ]
    meaning = {
        "一外多中": "同一外文有两个以上真正不同的译名——最需要裁决的一类",
        "一中多外": "同一译名对应多个外文（同语种才算撞车）",
        "空格与连字符": "只是写法不同（空格、连字符），不影响理解但影响检索与形式化映射",
        "等级不一致": "同一译名在不同工程里标了不同等级",
        "命名不合规": "机械可判的命名毛病（句读、残片、过长）",
        "一符多义": "同一记号读法或含义不唯一",
        "同名异符": "同一读法对应多个记号",
    }
    for k, v in meaning.items():
        if by_ctype.get(k, 0):
            lines.append(f"| {k} | {by_ctype.get(k, 0)} | {v} |")
    lines += [
        "",
        "## 四、优先处理（高严重度）",
        "",
    ]
    if top:
        lines += ["| 类型 | 键 | 候选 | 建议 |", "|---|---|---|---|"]
        for c in top[:20]:
            lines.append(f"| {c['类型']} | `{c['键']}` | {c['候选']} | {c['建议']} |")
        if len(top) > 20:
            lines.append(f"| … | 其余 {len(top) - 20} 条见 `CONFLICTS.tsv` | | |")
    else:
        lines.append("（当前没有高严重度冲突。）")
    lines += [
        "",
        "## 五、宏：形式化之前必须先对齐的部分",
        "",
        "同一个宏名在不同工程的 `preamble.tex` 里被定义成不同含义，换算子文本时最容易出错。按出现工程数排序的前 8 个：",
        "",
        "| 宏 | 出现工程数 | 不同含义数 | 含义变体 |",
        "|---|---|---|---|",
    ]
    for m in macro_top:
        lines.append(f"| `\\{m['name']}` | {len(m['pkgs'])} | {m['variants']} | {' ｜ '.join(m['bodies'][:3])} |")
    lines += [
        "",
        "完整清单见 `MACROS.tsv`。注意：`\\R` 这类「同一含义的多种写法」已在判定时折算（`\\Bbb`→`\\mathbb`、`\\operatorname{}`/`\\text{}`/`{\\rm }`→`\\mathrm{}`），",
        "剩下的 `真冲突` 才是语义不同。",
        "",
        "## 六、怎么用",
        "",
        "1. 写译文前先查 `TERMS.tsv`：有登记就照用，不新造；查不到按 `STYLE_NL.md` §术语 处理并登记回源表。",
        "2. 公式里的记号先查 `SYMBOLS.tsv` 与 `工程文件/preamble.tex`；不在表内的记号登记后再用。",
        "3. `CONFLICTS.tsv` 的「建议」列是机械推断，**裁定权在仓主**；裁定后改源表，不要改生成物。",
        "4. 改完跑 `python tools/build_norm.py --check`；表与源数据不一致会让闸门失败，确认无误再重建。",
        "",
        f"本表由 `tools/build_norm.py` 生成于 2026-11-21（术语 {len(terms)} / 记号 {len(symbols)} / 冲突 {len(conflicts)} / 宏 {len(macros)}）。",
        "",
    ]
    return {
        "TERMS.tsv": terms_tsv,
        "SYMBOLS.tsv": symbols_tsv,
        "CONFLICTS.tsv": conflicts_tsv,
        "MACROS.tsv": macros_tsv,
        "INDEX.md": "\n".join(lines),
    }


def diff(old: str, new: str) -> str:
    a = old.splitlines()
    b = new.splitlines()
    if a == b:
        return ""
    out = []
    shown = 0
    for i in range(max(len(a), len(b))):
        x = a[i] if i < len(a) else "<缺行>"
        y = b[i] if i < len(b) else "<缺行>"
        if x != y:
            shown += 1
            out.append(f"  行 {i + 1}\n    旧: {x[:180]}\n    新: {y[:180]}")
        if shown >= 12:
            out.append("  …")
            break
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只比对，不写盘")
    args = ap.parse_args()

    terms = merge_terms(load_terms())
    symbols = load_symbols()
    conflicts = build_conflicts(terms) + build_symbol_conflicts(symbols)
    conflicts.sort(key=lambda r: (SEVERITY.get(r["严重度"], 9), r["类型"], r["键"]))
    macros = scan_macros()
    files = render(terms, symbols, conflicts, macros)

    os.makedirs(OUT, exist_ok=True)
    problems = 0
    for name, content in files.items():
        path = os.path.join(OUT, name)
        old = ""
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                old = fh.read()
        if args.check:
            if old != content:
                problems += 1
                print(f"[不一致] {os.path.join(OUT_REL, name)}")
                print(diff(old, content))
        else:
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(content)
            print(f"[写入] {os.path.join(OUT_REL, name)}  {len(content.splitlines())} 行")

    print(f"术语 {len(terms)} / 记号 {len(symbols)} / 冲突 {len(conflicts)} / 宏 {len(macros)}")
    if args.check:
        if problems:
            print(f"数语规范表与源数据不一致：{problems} 个文件。跑 `python tools/build_norm.py` 重建。")
            return 1
        print("数语规范表与源数据一致。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
