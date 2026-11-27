# -*- coding: utf-8 -*-
r"""从源码 sections/*.tex 抽取编号条目，生成 资料卡/03-条款索引.md。

用法：
  python 工程文件/tools/gen_index.py

编号 = LaTeX 自动排的「讲次.序号」（15 类环境共用一个计数器，按正文出现顺序）；
页码按出现顺序取 工程文件/work/条目总表.tsv 的同讲第 k 行（源文手写编号与
译本自动编号会因原文编号跳号而错位，故不能按编号字符串匹配）。

摘录保留数学符号（Γ、π₁、QC、D 模等）：旧版 plain() 直接删掉反斜杠命令，
把 \Gamma、\pi、\QCoh 一并吞掉，导致 03 的 78 行数学残缺；本版改为先做
符号/宏替换，再清理残余命令。
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEC = os.path.join(ROOT, "源码", "sections")
TOC = os.path.join(ROOT, "lectures", "toc.json")
TABLE = os.path.join(ROOT, "工程文件", "work", "条目总表.tsv")
OUT = os.path.join(ROOT, "资料卡", "03-条款索引.md")

ENVS = ["definition", "theorem", "proposition", "lemma", "corollary", "remark",
        "example", "warning", "question", "conjecture", "notation", "fact",
        "exercise", "construction", "hope"]

ZH = {"definition": "定义", "theorem": "定理", "proposition": "命题", "lemma": "引理",
      "corollary": "推论", "remark": "注", "example": "例", "warning": "警告",
      "question": "问题", "conjecture": "猜想", "notation": "记号", "fact": "事实",
      "exercise": "练习", "construction": "构造", "hope": "期望"}

# 单符号命令 → Unicode / 可读写法
SYMBOLS = {
    "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ",
    "Pi": "Π", "Sigma": "Σ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω",
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε",
    "varepsilon": "ε", "zeta": "ζ", "eta": "η", "theta": "θ", "iota": "ι",
    "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ",
    "pi": "π", "rho": "ρ", "sigma": "σ", "tau": "τ", "upsilon": "υ",
    "phi": "φ", "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
    "infty": "∞", "to": "→", "rightarrow": "→", "longrightarrow": "⟶",
    "gets": "←", "leftarrow": "←", "mapsto": "↦", "longmapsto": "⟼",
    "Rightarrow": "⇒", "Leftarrow": "⇐", "Leftrightarrow": "⇔",
    "hookrightarrow": "↪", "hookleftarrow": "↩", "uparrow": "↑",
    "downarrow": "↓", "simeq": "≃", "cong": "≅", "approx": "≈",
    "sim": "∼", "equiv": "≡", "neq": "≠", "le": "≤", "leq": "≤",
    "ge": "≥", "geq": "≥", "ll": "≪", "gg": "≫", "pm": "±", "mp": "∓",
    "otimes": "⊗", "oplus": "⊕", "ominus": "⊖", "odot": "⊙",
    "boxtimes": "⊠", "times": "×", "cdot": "·", "cdots": "⋯",
    "ldots": "…", "dots": "…", "vdots": "⋮", "ddots": "⋱",
    "subset": "⊂", "supset": "⊃", "subseteq": "⊆", "supseteq": "⊇",
    "in": "∈", "notin": "∉", "ni": "∋", "cup": "∪", "cap": "∩",
    "sqcup": "⊔", "setminus": "∖", "emptyset": "∅", "varnothing": "∅",
    "wedge": "∧", "vee": "∨", "neg": "¬", "forall": "∀", "exists": "∃",
    "sum": "Σ", "prod": "∏", "coprod": "∐", "int": "∫", "oint": "∮",
    "partial": "∂", "nabla": "∇", "hbar": "ℏ", "ell": "ℓ",
    "langle": "⟨", "rangle": "⟩", "vert": "|", "mid": "|",
    "colon": ":", "quad": " ", "qquad": "  ", " ": " ",
    "backslash": "∖", "star": "⋆", "ast": "∗", "circ": "∘",
    "bullet": "•", "sharp": "♯", "flat": "♭", "natural": "♮",
    "dagger": "†", "angle": "∠", "perp": "⊥", "parallel": "∥",
    "aleph": "ℵ", "Re": "Re", "Im": "Im", "prime": "′",
}
# 无参数、无实义的排版命令
DROP = {"left", "right", "big", "Big", "bigg", "Bigg", "bigl", "bigr",
        "Bigl", "Bigr", "displaystyle", "textstyle", "scriptstyle",
        "scriptscriptstyle", "limits", "nolimits", "mathstrut", "strut",
        "hfill", "vfill", "noindent", "indent", "centering",
        "smallskip", "medskip", "bigskip", "par", "newline", "linebreak",
        "protect", "relax", "the", "expandafter", "csname", "endcsname"}
# 带参数、只保留内容的命令
KEEP_ONE = {"emph", "textbf", "textit", "textsf", "texttt", "textsc",
            "underline", "ul", "mathrm", "mathbf", "mathsf", "mathtt",
            "mathcal", "mathbb", "mathfrak", "operatorname", "text",
            "textrm", "textup", "mbox", "hbox", "overline", "underline",
            "widehat", "widetilde", "hat", "tilde", "bar", "vec", "dot",
            "ddot", "check", "breve", "acute", "grave", "mathop", "mathbin",
            "mathrel", "mathord", "mathopen", "mathclose", "mathpunct",
            "mathinner", "mathnormal", "boldsymbol", "bm", "substack",
            "ol", "wt"}
# 领域宏（含本工程 preamble 里的单字母黑板体与简写）
DOMAIN = {
    "Bun": "Bun", "Rep": "Rep", "Loc": "Loc", "LocSys": "LocSys",
    "Pic": "Pic", "Gr": "Gr", "Sph": "Sph", "Vect": "Vect",
    "Spec": "Spec", "QCoh": "QCoh", "IndCoh": "IndCoh", "Coh": "Coh",
    "Hom": "Hom", "End": "End", "Aut": "Aut", "Map": "Map", "Sym": "Sym",
    "Perv": "Perv", "Shv": "Shv", "Sh": "Sh", "Mod": "Mod", "Fun": "Fun",
    "Set": "Set", "Spaces": "Spaces", "Ring": "Ring", "Alg": "Alg",
    "F": "F", "C": "C", "Q": "Q", "Z": "Z", "A": "A", "G": "G",
    "R": "R", "P": "P", "Fp": "F_p", "Fq": "F_q", "Fl": "F_ℓ",
    "Qp": "Q_p", "Zp": "Z_p", "Ql": "Q̄_ℓ", "Zl": "Z_ℓ", "Lam": "Λ",
    "et": "ét", "Dmod": "D-mod", "Spa": "Spa", "Div": "Div",
    "Hck": "Hecke", "breveE": "E", "BdR": "B_dR", "Bcris": "B_cris",
    "Bst": "B_st", "BHT": "B_HT", "Ainf": "A_inf", "BunG": "Bun_G",
    "Perf": "Perf", "Fil": "Fil", "trdeg": "trdeg", "oo": "O", "id": "id", "Tr": "Tr",
}

_CAL = {"cA": "A", "cB": "B", "cC": "C", "cD": "D", "cE": "E", "cF": "F",
        "cG": "G", "cH": "H", "cI": "I", "cJ": "J", "cK": "K", "cL": "L",
        "cM": "M", "cN": "N", "cO": "O", "cP": "P", "cQ": "Q", "cR": "R",
        "cS": "S", "cT": "T", "cU": "U", "cV": "V", "cW": "W", "cX": "X",
        "cY": "Y", "cZ": "Z", "ul": "", "wt": ""}


def _match_brace(s: str, i: int) -> int:
    """s[i] == '{'；返回匹配的 '}' 下标（找不到返回 len(s)）。"""
    depth = 0
    while i < len(s):
        if s[i] == "{" and (i == 0 or s[i - 1] != "\\"):
            depth += 1
        elif s[i] == "}" and (i == 0 or s[i - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return len(s)


def _drop_arg(s: str, name: str, nargs: int = 1) -> str:
    """删除 \\name{...}（可带 nargs 个参数）。"""
    out = []
    i = 0
    while i < len(s):
        m = re.match(r"\\" + name + r"\*?(?![a-zA-Z])", s[i:])
        if m:
            j = i + m.end()
            ok = True
            for _ in range(nargs):
                while j < len(s) and s[j] == " ":
                    j += 1
                if j < len(s) and s[j] == "{":
                    j = _match_brace(s, j) + 1
                else:
                    ok = False
                    break
            if ok:
                i = j
                continue
        out.append(s[i])
        i += 1
    return "".join(out)


def _keep_arg(s: str, names: list[str]) -> str:
    """\\name{...} → 内容；只处理一个参数。"""
    pat = re.compile(r"\\(" + "|".join(names) + r")\*?(?![a-zA-Z])")
    out = []
    i = 0
    while i < len(s):
        m = pat.match(s, i)
        if m:
            j = m.end()
            while j < len(s) and s[j] == " ":
                j += 1
            if j < len(s) and s[j] == "{":
                k = _match_brace(s, j)
                out.append(s[j + 1:k])
                i = k + 1
                continue
        out.append(s[i])
        i += 1
    return "".join(out)


def _frac(s: str) -> str:
    """\\frac{a}{b} → a/b（递归处理内容）。"""
    pat = re.compile(r"\\(?:d?frac|tfrac)\s*")
    out = []
    i = 0
    while i < len(s):
        m = pat.match(s, i)
        if m:
            j = m.end()
            if j < len(s) and s[j] == "{":
                k = _match_brace(s, j)
                a = s[j + 1:k]
                j = k + 1
                while j < len(s) and s[j] == " ":
                    j += 1
                if j < len(s) and s[j] == "{":
                    k2 = _match_brace(s, j)
                    b = s[j + 1:k2]
                    out.append("(%s)/(%s)" % (a.strip(), b.strip()))
                    i = k2 + 1
                    continue
        out.append(s[i])
        i += 1
    return "".join(out)


def plain(body: str, cap: int = 110) -> str:
    s = body
    # 先删掉注、译注、标签等整块
    s = _drop_arg(s, "footnote")
    s = _drop_arg(s, "yizhu", 2)
    s = _drop_arg(s, "label")
    s = _drop_arg(s, "index")
    s = _drop_arg(s, "srcpage")
    s = _drop_arg(s, "srcpageinl")
    s = _drop_arg(s, "lecture")
    s = _drop_arg(s, "ref")
    s = _drop_arg(s, "cite")
    # 行间/行内公式定界符
    s = s.replace("\\[", " ").replace("\\]", " ")
    s = s.replace("\\(", " ").replace("\\)", " ")
    s = s.replace("$$", " ").replace("$", "")
    # 环境与排版
    s = re.sub(r"\\begin\{[^{}]*\}|\\end\{[^{}]*\}", " ", s)
    s = s.replace("\\\\", " ")
    s = re.sub(r"&", " ", s)
    s = s.replace("~", " ")
    s = _frac(s)
    s = re.sub(r"\\sqrt\s*\{([^{}]*)\}", r"√(\1)", s)
    # 单符号先做（否则 \cC 换成 C 后会与前面的 \in 粘成 \inC 而被当作未知命令删掉）
    for k, v in sorted(SYMBOLS.items(), key=lambda kv: -len(kv[0])):
        s = re.sub(r"\\" + re.escape(k) + r"(?![a-zA-Z])", v, s)
    # 领域宏（长名优先，避免 \F 抢先吃掉 \Fq）
    for k, v in sorted(DOMAIN.items(), key=lambda kv: -len(kv[0])):
        s = re.sub(r"\\" + k + r"(?![a-zA-Z])", v, s)
    for k, v in _CAL.items():
        s = re.sub(r"\\" + k + r"(?![a-zA-Z])", v, s)
    # 保留参数内容的命令
    s = _keep_arg(s, sorted(KEEP_ONE, key=len, reverse=True))
    # 去排版命令
    s = re.sub(r"\\([a-zA-Z]+)\*?(?![a-zA-Z])",
               lambda m: " " if m.group(1) in DROP else "", s)
    # 上下标 → 可读括号
    s = re.sub(r"\^\{([^{}]*)\}", r"^(\1)", s)
    s = re.sub(r"_\{([^{}]*)\}", r"_(\1)", s)
    s = s.replace("^()", "").replace("_()", "")
    s = s.replace("^(′)", "'")
    s = s.replace("\\#", "#").replace("\\%", "%").replace("\\&", "&")
    s = s.replace("\\_", "_")
    s = s.replace("\\{", "").replace("\\}", "")
    s = s.replace("---", "—").replace("--", "–")
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"\s+", " ", s).strip()
    s = s.strip("：:，,。;； ")
    s = s.replace("|", "\\|")
    # 摘录：取不超过 cap 的最后一个句末，至少凑够 45 字；过长则在 cap 处截断
    s = s.strip()
    if len(s) > cap:
        ends = [m.end() for m in re.finditer(r"[。！？]", s)]
        cand = [e for e in ends if e <= cap]
        cut = cand[-1] if cand else 0
        if cut < 45:
            cut = cap
        s = (s[:cut] + ("…" if cut >= cap else "")).strip()
    return s


def main() -> int:
    toc = json.load(io.open(TOC, encoding="utf-8"))
    pages: dict[int, list[str]] = {}
    with io.open(TABLE, encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 5:
                pages.setdefault(int(parts[0]), []).append(parts[3])

    rows = []
    warn = 0
    for entry in toc:
        n = entry["n"]
        files = [fn for fn in sorted(os.listdir(SEC)) if fn.startswith("s%02d-" % n)]
        if not files:
            continue
        text = io.open(os.path.join(SEC, files[0]), encoding="utf-8").read()
        found = []
        for env in ENVS:
            for m in re.finditer(r"\\begin\{%s\}(.*?)\\end\{%s\}" % (env, env), text, re.S):
                found.append((m.start(), env, m.group(1)))
        found.sort()
        plist = pages.get(n, [])
        if len(found) != len(plist):
            print("WARN lecture %d: tex=%d table=%d" % (n, len(found), len(plist)))
            warn += 1
        for k, (_pos, env, body) in enumerate(found, 1):
            page = plist[k - 1] if k - 1 < len(plist) else "—"
            rows.append((n, "%d.%d" % (n, k), ZH[env], page, plain(body)))

    lines = ["# 资料卡 03 · 条款索引", "",
             "共 %d 条编号条目。编号由 LaTeX 自动生成（`讲次.序号`），页码为原文印刷页（= PDF 页）。" % len(rows),
             "", "| 讲 | 编号 | 类型 | 原文页 | 内容（首句节选） |", "| --- | --- | --- | --- | --- |"]
    for n, num, kind, page, body in rows:
        lines.append("| %d | %s | %s | %s | %s |" % (n, num, kind, page, body))
    io.open(OUT, "w", encoding="utf-8", newline="").write("\n".join(lines) + "\n")
    print("wrote", OUT, len(rows), "rows; warnings:", warn)
    return 0


if __name__ == "__main__":
    sys.exit(main())
