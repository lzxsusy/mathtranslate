"""Build 附录C 译注汇编 from review/*.json notes.

Each note: {unit, page, text}. Group by chapter (from manifest unit->file).
Escape fallback when math/braces are unbalanced.
"""
import glob
import io
import json
import os
import re

WORK = os.path.dirname(os.path.abspath(__file__))
MANIFEST = {m["unit"]: m for m in json.load(io.open(os.path.join(WORK, "units", "manifest.json"), encoding="utf-8"))}

CHAP_NAMES = {
    "preface.tex": "前言",
    "notation.tex": "符号表",
    "appendixA.tex": "附录 A",
    "appendixB.tex": "附录 B",
}


def chapter_label(fname):
    fname = fname.split("/")[-1]
    if fname in CHAP_NAMES:
        return CHAP_NAMES[fname]
    m = re.match(r"chapter(\d+)\.tex", fname)
    if m:
        return "第 %d 章" % int(m.group(1))
    return fname


def balanced(s):
    if s.count("$") % 2:
        return False
    depth = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0:
                return False
        i += 1
    return depth == 0


SPECIAL = {"%": r"\%", "&": r"\&", "#": r"\#", "_": r"\_"}


def plain_escape(s):
    out = []
    for c in s:
        if c == "\\":
            out.append(r"\textbackslash{}")
        elif c in SPECIAL:
            out.append(SPECIAL[c])
        elif c == "{":
            out.append(r"\{")
        elif c == "}":
            out.append(r"\}")
        elif c == "$":
            out.append(r"\$")
        elif c == "^":
            out.append(r"\^{}")
        elif c == "~":
            out.append(r"\~{}")
        else:
            out.append(c)
    return "".join(out)


def math_escape(s):
    """Keep $...$ but escape text specials outside math."""
    parts = s.split("$")
    out = []
    for k, seg in enumerate(parts):
        if k % 2 == 1:
            out.append("$" + seg + "$")
            continue
        for c in seg:
            if c == "\\":
                out.append(r"\textbackslash{}")
            elif c in SPECIAL:
                out.append(SPECIAL[c])
            elif c == "{":
                out.append(r"\{")
            elif c == "}":
                out.append(r"\}")
            elif c == "^":
                out.append(r"\^{}")
            elif c == "~":
                out.append(r"\~{}")
            else:
                out.append(c)
        pass
    return "".join(out)


notes = []
for jf in sorted(glob.glob(os.path.join(WORK, "review", "u*.json"))):
    d = json.load(io.open(jf, encoding="utf-8"))
    unit = d.get("unit")
    fname = MANIFEST.get(unit, {}).get("file", "")
    for n in d.get("notes", []):
        text = (n.get("text") or "").strip()
        if not text:
            continue
        notes.append({
            "unit": unit,
            "chapter": chapter_label(fname) if fname else "",
            "page": n.get("page"),
            "text": text,
        })

notes.sort(key=lambda x: (str(x["page"]).zfill(4), x["unit"]))

lines = [
    r"\chapter*{附录 C\quad 译注汇编}",
    r"\addcontentsline{toc}{chapter}{附录 C\quad 译注汇编}",
    r"\markboth{附录 C\quad 译注汇编}{附录 C\quad 译注汇编}",
    "",
    r"本汇编收录逐页对照原书英文扫描件时写下的译注，共 %d 条，按原书 PDF 物理页排序"
    r"（与原书印刷页相差 23）。内容分三类：原文笔误与 OCR 不可辨处的处理、术语与记号的歧义、"
    r"作者未展开的跳步说明。正文未插入脚注，以免影响版面与原书页码对位；读者可据页号回查。" % len(notes),
    "",
]

cur = None
for n in notes:
    if n["chapter"] != cur:
        cur = n["chapter"]
        lines += ["", r"\subsection*{%s}" % cur, ""]
    body = math_escape(n["text"]) if balanced(n["text"]) else plain_escape(n["text"])
    pg = n["page"] if n["page"] is not None else "?"
    lines.append(r"\noindent\textbf{\footnotesize p%s}\quad %s" % (pg, body))
    lines.append("")

out = os.path.join(WORK, "chapters", "appendixC.tex")
io.open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote", out, len(notes), "notes")
