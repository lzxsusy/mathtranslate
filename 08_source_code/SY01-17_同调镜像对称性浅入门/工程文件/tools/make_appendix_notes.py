# -*- coding: utf-8 -*-
"""Collect  % [Tutor Note: ...]  comments from the chapters and emit

  * appendix_notes.tex   (typeset appendix, included by main.tex)
  * reports/notes_index.md    (markdown index of all notes)

Usage: python tools/make_appendix_notes.py
"""
import io, os, re, glob

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = WS
REPORTS = os.path.join(WS, "reports")
CH_TITLES = {
    1: "范畴", 2: "上同调", 3: "高阶积", 4: "箭图", 5: "来自物理的动机",
    6: "A 侧", 7: "B 侧", 8: "镜像对称", 9: "粘合", 10: "分次",
    11: "稳定化", 12: "变形",
}
NOTE_RE = re.compile(r"^%\s*\[Tutor Note:\s*(.*?)\]\s*$")
SEC_RE = re.compile(r"^\\section\{")
SEC_READ = re.compile(r"^\\section\*?\{")
SUB_RE = re.compile(r"^\\subsection\{")


def title_of(line):
    i = line.find("{")
    depth, j = 0, i
    while j < len(line):
        if line[j] == "{":
            depth += 1
        elif line[j] == "}":
            depth -= 1
            if depth == 0:
                return line[i + 1:j]
        j += 1
    return ""


def esc(s):
    out, math, i = [], False, 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            out.append(s[i:i + 2])
            i += 2
            continue
        if c == "$":
            math = not math
            out.append(c)
            i += 1
            continue
        if not math:
            c = {"#": r"\#", "&": r"\&", "%": r"\%", "_": r"\_"}.get(c, c)
        out.append(c)
        i += 1
    return "".join(out)


def collect():
    chapters = []
    for n in range(1, 13):
        f = os.path.join(BOOK, "chapters", "ch%02d.tex" % n)
        lines = io.open(f, encoding="utf-8").read().splitlines()
        sec, sub, notes = "", "", []
        seccount = 0
        for k, line in enumerate(lines):
            if SUB_RE.match(line):
                sub = title_of(line)
            elif SEC_RE.match(line):
                seccount += 1
                sec = "%d.%d" % (n, seccount)
                sub = ""
            m = NOTE_RE.match(line.strip())
            if m:
                notes.append((n, sec, sub, m.group(1).strip(), k + 1))
        chapters.append((n, notes))
    return chapters


def main():
    chapters = collect()
    os.makedirs(REPORTS, exist_ok=True)
    tex = []
    md = ["# 校订批注索引", "",
          "共 %d 条批注，按章、节顺序排列；批注在 PDF 中见“附录：校订批注”，在源码中为 `%% [Tutor Note: ...]` 注释。" % sum(len(x[1]) for x in chapters),
          ""]
    for n, notes in chapters:
        if not notes:
            continue
        tex.append(r"\section*{第 %d 章\quad %s}" % (n, CH_TITLES[n]))
        md.append("## 第 %d 章 %s" % (n, CH_TITLES[n]))
        md.append("")
        md.append("| 节 | 行 | 批注 |")
        md.append("|---|---|---|")
        cur = None
        for (_, sec, sub, text, line) in notes:
            label = ("§%s" % sec) if sec else ""
            tex.append(r"\noindent\textbf{%s}\quad %s\par\medskip" % (label, esc(text)))
            md.append("| %s | %s | %s |" % (label, line, text.replace("|", r"\|")))
        md.append("")
    io.open(os.path.join(BOOK, "appendix_notes.tex"), "w", encoding="utf-8", newline="\n").write(
        "% 由 tools/make_appendix_notes.py 自动生成，勿手改\n" + "\n".join(tex) + "\n")
    io.open(os.path.join(REPORTS, "notes_index.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(md) + "\n")
    print("notes:", sum(len(x[1]) for x in chapters))


if __name__ == "__main__":
    main()
