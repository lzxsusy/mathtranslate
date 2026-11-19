# -*- coding: utf-8 -*-
"""Generate the two appendices from the four part files.

* appendix_notes.tex     -- all \\transnote{...} regrouped by section (reading order)
* appendix_glossary.tex  -- bilingual glossary from \\index{english@中文} entries
* 校对记录/译注清单.tsv  -- flat ledger of notes (id / section / file / line / text)

Run:  python 工程文件/tools/gen_appendix.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "源码")
OUTDIR = os.path.join(ROOT, "校对记录")
PARTS = ["part1_zh.tex", "part2_zh.tex", "part3_zh.tex", "part4_zh.tex"]

SECTION_RE = re.compile(r"\\(section|subsection|subsubsection)\*?\s*\{")
LABEL_RE = re.compile(r"\\label\{([^}]*)\}")
INDEX_RE = re.compile(r"\\index\s*\{")
TRANSNOTE_RE = re.compile(r"\\transnote\s*\{")


def balanced(text, open_pos):
    """Return (content, end_pos) for the brace group starting at open_pos (text[open_pos]=='{')."""
    depth = 0
    i = open_pos
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
                return text[open_pos + 1 : i], i + 1
        i += 1
    raise ValueError("unbalanced braces at %d" % open_pos)


def strip_comments(text):
    out = []
    for line in text.split("\n"):
        i = 0
        kept = []
        while i < len(line):
            if line[i] == "\\" and i + 1 < len(line):
                kept.append(line[i : i + 2])
                i += 2
                continue
            if line[i] == "%":
                break
            kept.append(line[i])
            i += 1
        out.append("".join(kept))
    return "\n".join(out)


def scan(path, start=(0, 0, 0)):
    """Walk one part file, tracking section counters; return notes, glossary hits and counters."""
    raw = open(path, encoding="utf-8").read()
    text = strip_comments(raw)
    notes = []
    glossary = []  # (cn, en, section)
    sec, sub, subsub = start
    cur = (sec, sub, subsub)
    sec_title = ""
    sub_title = ""
    i = 0
    while i < len(text):
        m = SECTION_RE.search(text, i)
        n = TRANSNOTE_RE.search(text, i)
        idx = INDEX_RE.search(text, i)
        nxt = min([x.start() for x in (m, n, idx) if x is not None] + [len(text)])
        if nxt == len(text):
            break
        if m is not None and m.start() == nxt:
            content, end = balanced(text, m.end() - 1)
            level = m.group(1)
            if level == "section":
                sec += 1
                sub = subsub = 0
                sec_title = content
                sub_title = ""
            elif level == "subsection":
                sub += 1
                subsub = 0
                sub_title = content
            else:
                subsub += 1
            cur = (sec, sub, subsub)
            i = end
            continue
        if n is not None and n.start() == nxt:
            content, end = balanced(text, n.end() - 1)
            line = text[: n.start()].count("\n") + 1
            notes.append(
                {
                    "content": content,
                    "section": cur,
                    "sec_title": sec_title if cur[1] == 0 else sub_title,
                    "file": os.path.basename(path),
                    "line": line,
                }
            )
            i = end
            continue
        if idx is not None and idx.start() == nxt:
            content, end = balanced(text, idx.end() - 1)
            if "@" in content and "!" not in content and "|" not in content:
                en, cn = content.split("@", 1)
                glossary.append((cn.strip(), en.strip(), cur))
            i = end
            continue
        i = nxt + 1
    return notes, glossary, (sec, sub, subsub)


def sec_label(sec_tuple):
    s, b, c = sec_tuple
    if b == 0:
        return "%d" % s
    if c == 0:
        return "%d.%d" % (s, b)
    return "%d.%d.%d" % (s, b, c)


def latex_escape_tsv(t):
    return t.replace("\t", " ").replace("\n", " ")


def main():
    all_notes = []
    glossary = {}
    counters = (0, 0, 0)
    for fn in PARTS:
        notes, gl, counters = scan(os.path.join(SRC, fn), counters)
        all_notes.extend(notes)
        for cn, en, sec in gl:
            if cn not in glossary:
                glossary[cn] = (en, sec)

    # ---------------- appendix A ----------------
    lines = []
    lines.append("% 自动生成文件：由 工程文件/tools/gen_appendix.py 生成，请勿手工编辑")
    lines.append("\\section{译注汇总}")
    lines.append("\\label{app:notes}")
    lines.append(
        "\\noindent 本附录按节重列正文中的全部译者注，共 \\textbf{%d} 条"
        "（与正文脚注一一对应）. 编号「节号-序号」只用于本附录检索；来源等级与访问日期见各条末尾括注."
        % len(all_notes)
    )
    lines.append("\\begingroup\\small")
    counter = {}
    grouped = []
    for note in all_notes:
        key = sec_label(note["section"])
        title = note["sec_title"]
        counter[key] = counter.get(key, 0) + 1
        nid = "%s-%d" % (key, counter[key])
        grouped.append((key, title, nid, note["content"], note["file"], note["line"]))
    cur_key = None
    for key, title, nid, content, _f, _l in grouped:
        if key != cur_key:
            lines.append("\\medskip\\noindent\\textbf{第 %s 节\\quad %s}\\par\\nopagebreak" % (key, title))
            lines.append("\\begin{description}[leftmargin=5.8em,labelwidth=5em,labelsep=0.6em,itemsep=0.15ex,topsep=0.2ex]")
            cur_key = key
        lines.append("\\item[%s] %s" % (nid, content))
        # close description when the next item starts a new section
    # rebuild grouping properly: close before new heading
    lines = []
    lines.append("% 自动生成文件：由 工程文件/tools/gen_appendix.py 生成，请勿手工编辑")
    lines.append("\\section{译注汇总}")
    lines.append("\\label{app:notes}")
    lines.append(
        "\\noindent 本附录按节重列正文中的全部译者注，共 \\textbf{%d} 条"
        "（与正文脚注一一对应）. 编号「节号-序号」只用于本附录检索；来源等级与访问日期见各条末尾括注."
        % len(all_notes)
    )
    lines.append("\\begingroup\\small")
    cur_key = None
    for key, title, nid, content, _f, _l in grouped:
        if cur_key is not None and key != cur_key:
            lines.append("\\end{description}")
        if key != cur_key:
            lines.append("\\medskip\\noindent\\textbf{第 %s 节\\quad %s}\\par\\nopagebreak" % (key, title))
            lines.append("\\begin{description}[leftmargin=5.8em,labelwidth=5em,labelsep=0.6em,itemsep=0.15ex,topsep=0.2ex]")
            cur_key = key
        lines.append("\\item[%s] %s" % (nid, content))
    if cur_key is not None:
        lines.append("\\end{description}")
    lines.append("\\endgroup")
    with open(os.path.join(SRC, "appendix_notes.tex"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    # ---------------- appendix B ----------------
    rows = []
    for cn, (en, sec) in glossary.items():
        rows.append((cn, en, sec_label(sec)))
    def _sk(where):
        return tuple(int(x) for x in where.split(".")) + (0,) * (3 - where.count(".") - 1)

    rows.sort(key=lambda r: (_sk(r[2]), r[1].lower()))
    gl = []
    gl.append("% 自动生成文件：由 工程文件/tools/gen_appendix.py 生成，请勿手工编辑")
    gl.append("\\section{术语对照表}")
    gl.append("\\label{app:glossary}")
    gl.append(
        "\\noindent 下表由译文索引条目生成：中文术语、英文原文与首次出现的小节. "
        "「首见」只记到小节，精确页码见文末中文术语索引."
    )
    gl.append("\\begin{longtable}{p{0.36\\textwidth}p{0.40\\textwidth}c}")
    gl.append("\\toprule")
    gl.append("中文 & 英文 & 首见\\\\")
    gl.append("\\midrule")
    gl.append("\\endfirsthead")
    gl.append("\\toprule")
    gl.append("中文 & 英文 & 首见\\\\")
    gl.append("\\midrule")
    gl.append("\\endhead")
    gl.append("\\bottomrule")
    gl.append("\\endfoot")
    for cn, en, where in rows:
        gl.append("%s & %s & %s\\\\" % (cn.replace("&", "\\&"), en.replace("&", "\\&"), where))
    gl.append("\\end{longtable}")
    with open(os.path.join(SRC, "appendix_glossary.tex"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(gl) + "\n")

    # ---------------- TSV ledger ----------------
    ledger = os.path.join(OUTDIR, "译注清单.tsv")
    with open(ledger, "w", encoding="utf-8", newline="\n") as f:
        f.write("id\tsection\tfile\tline\tnote\n")
        for key, title, nid, content, nfile, nline in grouped:
            f.write("%s\t%s\t%s\t%d\t%s\n" % (nid, key, nfile, nline, latex_escape_tsv(content)))

    print("notes=%d  glossary=%d" % (len(all_notes), len(rows)))
    print("wrote appendix_notes.tex, appendix_glossary.tex, 校对记录/译注清单.tsv")


if __name__ == "__main__":
    sys.exit(main())
