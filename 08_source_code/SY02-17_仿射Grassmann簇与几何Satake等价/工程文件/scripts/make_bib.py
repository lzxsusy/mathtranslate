# -*- coding: utf-8 -*-
r"""把原文 amsrefs 的 \bib{key}{type}{...} 条目转成 thebibliography 的 \bibitem。

用法： python make_bib.py   （路径由 __file__ 推导，避免中文命令行参数乱码）

规则：
- 只输出不在 \quash{...} 内的条目（原文靠 \quash 关闭未引用的示例条目）；
- 条目按原文出现次序排列，编号即 thebibliography 的序号。
"""
import io
import os
import re


def match_brace(s, start):
    """s[start] == '{'，返回配对 '}' 的下标。"""
    d = 0
    i = start
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            d += 1
        elif c == "}":
            d -= 1
            if d == 0:
                return i
        i += 1
    return -1


def quash_spans(s):
    spans = []
    for m in re.finditer(r"\\quash\{", s):
        st = m.end() - 1
        en = match_brace(s, st)
        if en > 0:
            spans.append((st, en))
    return spans


def inside(pos, spans):
    return any(a <= pos <= b for a, b in spans)


def parse_bibs(s, spans):
    out = []
    for m in re.finditer(r"\\bib\{([^}]*)\}\s*\{([a-zA-Z]+)\}\s*\{", s):
        if inside(m.start(), spans):
            continue
        key, typ = m.group(1), m.group(2)
        st = m.end() - 1
        en = match_brace(s, st)
        if en < 0:
            continue
        out.append((key, typ, s[st + 1:en]))
    return out


def fields(body):
    out = {}
    for m in re.finditer(r"([A-Za-z]+)\s*=\s*\{", body):
        name = m.group(1).lower()
        st = m.end() - 1
        en = match_brace(body, st)
        if en < 0:
            continue
        val = re.sub(r"\s+", " ", body[st + 1:en]).strip()
        out.setdefault(name, []).append(val)
    return out


def render(key, typ, body):
    f = fields(body)
    auth = f.get("author", [])
    def flip(n):
        if "," not in n:
            return n.strip()
        last, first = n.split(",", 1)
        return ("%s %s" % (first.strip(), last.strip())).strip()

    names = [flip(x) for x in auth]
    if len(names) == 1:
        a = names[0]
    elif len(names) > 1:
        a = ", ".join(names[:-1]) + " and " + names[-1]
    else:
        a = ""
    title = f.get("title", [""])[0]
    parts = []
    if a:
        parts.append(a + ",")
    if title:
        parts.append("\\emph{%s}," % title.replace("\n", " "))
    if typ == "article":
        seg = f.get("journal", [""])[0]
        vol = f.get("volume", [""])[0]
        num = f.get("number", [""])[0]
        date = f.get("date", [""])[0]
        pages = f.get("pages", [""])[0]
        s2 = seg
        if vol:
            s2 += " \\textbf{%s}" % vol
        if date:
            s2 += " (%s)" % date
        if num:
            s2 += ", no. %s" % num
        if pages:
            s2 += ", %s" % pages
        if s2.strip():
            parts.append(s2 + ".")
        else:
            link = f.get("eprint", [""])[0] or f.get("url", [""])[0]
            if link:
                parts.append("available at %s." % link)
    elif typ == "book":
        ed = f.get("edition", [""])[0]
        pub = f.get("publisher", [""])[0]
        addr = f.get("address", [""])[0]
        date = f.get("date", [""])[0]
        if ed:
            parts.append("%s ed.," % ed)
        if pub:
            parts.append(pub + ",")
        if addr:
            parts.append(addr + ",")
        if date:
            parts.append(date + ".")
    else:
        book = f.get("booktitle", [""])[0]
        series = f.get("series", [""])[0]
        pub = f.get("publisher", [""])[0]
        addr = f.get("address", [""])[0]
        date = f.get("date", [""])[0]
        pages = f.get("pages", [""])[0]
        if book:
            parts.append("in %s," % book)
        if series:
            parts.append(series + ",")
        if pub:
            parts.append(pub + ",")
        if addr:
            parts.append(addr + ",")
        if date:
            parts.append(date + ",")
        if pages:
            parts.append("pp. %s." % pages)
    txt = " ".join(x for x in parts if x)
    return "\\bibitem{%s} %s" % (key, txt)


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(root, "work", "原文", "main.tex")
    out = os.path.join(os.path.dirname(root), "源码", "chunks", "ch08.tex")
    s = io.open(src, encoding="utf-8", errors="replace").read()
    spans = quash_spans(s)
    ents = parse_bibs(s, spans)
    lines = ["\\begin{thebibliography}{99}", ""]
    for key, typ, body in ents:
        lines.append(render(key, typ, body))
        lines.append("")
    lines.append("\\end{thebibliography}")
    io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print("quash spans", len(spans), "entries", len(ents), "->", out)


if __name__ == "__main__":
    main()
