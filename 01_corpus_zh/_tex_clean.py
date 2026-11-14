# -*- coding: utf-8 -*-
r"""LaTeX 片段清洗：把正文里的自定义宏展开成纯文本，保留数学。

只用在本工程的取语料脚本里（`_append_pkg.py`）。设计目标：
- `\BookCite{ref393,ref461}` → `[393, 461]`
- `\BookEqRef{eq:2.1}{2.1}` → `(2.1)`
- `\BookSectionRef{sec:3.1}{3.1}` → `第 3.1 节`
- `\BookChapterRef{2}` → `第 2 章`
- `\BookRef{fig:2.3}{图3}` → `图3`
- `\footnote{…}` → `（…备注…）`（递归展开内部宏）
- `\emph/\textbf/\textit/text…` → 只留内容，不留花括号
- `\BookStatementNumber{1}`、`\label{…}`、`\SourceParagraph{…}{…}` 等 → 删除
- 其余未知命令原样保留（数学宏如 `\mathbb`、`\frac` 不能动）
"""
from __future__ import annotations

import re

UNWRAP = {"emph", "textbf", "textit", "textrm", "textsf", "texttt", "text",
          "underline", "mbox", "mathrm", "operatorname", "hbox"}
DROP = {"BookStatementNumber", "label", "SourceParagraph", "SourceAnchor",
        "BookImage", "BookIndexPage", "index", "addcontentsline", "nocite",
        "BookNumberOnlyCaption", "caption", "vspace", "hspace", "centering",
        "noindent", "indent", "par", "smallskip", "medskip", "bigskip",
        "setcounter", "clearpage", "newpage", "protect", "relax", "ignorespaces",
        "unskip", "quad", "qquad", "hfill", "null", "phantomsection", "BookQED"}


def _read_group(s: str, i: int, open_ch: str = "{", close_ch: str = "}") -> tuple[str, int]:
    """s[i] == open_ch；返回 (组内文本, 组后下标)。花括号平衡，考虑转义。"""
    if i >= len(s) or s[i] != open_ch:
        return "", i
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


def _arg(s: str, i: int) -> tuple[str, int]:
    """跳过空格后读一个 {…} 实参；读不到就返回空串、下标不动。"""
    j = i
    while j < len(s) and s[j] in " \t":
        j += 1
    if j < len(s) and s[j] == "{":
        return _read_group(s, j)
    return "", i


def _read_opt(s: str, i: int) -> tuple[str, int]:
    j = i
    while j < len(s) and s[j] in " \t":
        j += 1
    if j < len(s) and s[j] == "[":
        return _read_group(s, j, "[", "]")
    return "", i


def expand(s: str) -> str:
    out = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c != "\\":
            out.append(c)
            i += 1
            continue
        m = re.match(r"\\([A-Za-z@]+\*?|.)", s[i:])
        if not m:
            out.append(c)
            i += 1
            continue
        name = m.group(1)
        j = i + len(m.group(0))
        star = name.endswith("*")
        base = name[:-1] if star else name

        if base == "BookCite":
            arg, j = _arg(s, j)
            keys = []
            for k in arg.split(","):
                k = k.strip()
                k2 = re.sub(r"^ref0*", "", k)
                keys.append(k2 if k2 else k)
            out.append("[%s]" % ", ".join(k for k in keys if k))
            i = j
            continue

        if base == "BookBibText":
            _lab, j = _arg(s, j)
            disp, j = _arg(s, j)
            if disp:
                out.append(disp)
            i = j
            continue

        if base in ("BookRef", "BookEqRef", "BookSectionRef"):
            _lab, j = _arg(s, j)
            disp, j2 = _arg(s, j)
            if disp:
                j = j2
            if base == "BookEqRef":
                out.append("(%s)" % disp)
            elif base == "BookSectionRef":
                out.append("第 %s 节" % disp)
            else:
                out.append(disp)
            i = j
            continue

        if base == "BookChapterRef":
            lab, j = _arg(s, j)
            disp, j2 = _arg(s, j)
            if disp:
                out.append(disp)
                j = j2
            else:
                out.append("第 %s 章" % lab)
            i = j
            continue

        if base == "BookTableRef":
            _lab, j = _arg(s, j)
            disp, j = _arg(s, j)
            if disp:
                out.append(disp)
            i = j
            continue

        if base == "footnote":
            arg, j = _arg(s, j)
            inner = expand(arg).strip()
            out.append("（%s）" % inner if inner else "")
            i = j
            continue

        if base in UNWRAP:
            _opt, j = _read_opt(s, j)
            arg, j2 = _arg(s, j)
            if j2 != j:
                j = j2
            out.append(expand(arg))
            i = j
            continue

        if base in DROP:
            jj = j
            while True:
                _x, j2 = _read_opt(s, jj)
                if j2 != jj:
                    jj = j2
                    continue
                _y, j2 = _arg(s, jj)
                if j2 != jj:
                    jj = j2
                    continue
                break
            i = jj
            continue

        out.append("\\" + name)
        i = j
    return "".join(out)


def strip_unbalanced_braces(t: str) -> str:
    """删掉不配平的孤立花括号（多由宏展开产生），配平的对保留（数学要用）。"""
    depth = 0
    out = []
    for ch in t:
        if ch == "{":
            depth += 1
            out.append(ch)
        elif ch == "}":
            if depth > 0:
                depth -= 1
                out.append(ch)
        else:
            out.append(ch)
    if depth > 0:
        s = "".join(out)
        k = depth
        res = []
        for ch in reversed(s):
            if ch == "{" and k > 0:
                k -= 1
                continue
            res.append(ch)
        out = list(reversed(res))
    return "".join(out)
