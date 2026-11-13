# -*- coding: utf-8 -*-
"""从 chunks 提取 % [Tutor Note: ...]（跨文件继承章/节）→ 书末附录 tex + 译注汇总.md"""
import os, re, collections

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
MAIN = os.path.join(ROOT, "src", "main.tex")
OUT_TEX = os.path.join(CH, "index_notes.tex")
OUT_MD = os.path.join(ROOT, "work", "译注汇总.md")

CH_MAP = {
    "fm": "序与理论的概要与展望",
    "ch01a": "共形场理论的几何", "ch01b": "共形场理论的几何",
    "ch01c": "共形场理论的几何", "ch01d": "共形场理论的几何",
    "ch02a": "Jones--Witten 理论", "ch02b": "Jones--Witten 理论",
    "ch02c": "Jones--Witten 理论", "ch02d": "Jones--Witten 理论",
    "ch02e": "Jones--Witten 理论",
    "ch03a": "Chern--Simons 微扰理论", "ch03b": "Chern--Simons 微扰理论",
    "ch03c": "Chern--Simons 微扰理论",
    "future": "今后的方向与课题", "references": "参考文献",
}

NOTE_RE = re.compile(r'% \[Tutor Note:\s*(.*?)\]\s*$')
PAGE_RE = re.compile(r'% \[原文 p\.(\w+)\]')
SEC_RE = re.compile(r'<本地路径>]*)\}')
CHAP_RE = re.compile(r'<本地路径>]*)\}')


def chunk_order():
    names = []
    for line in open(MAIN, encoding="utf-8"):
        m = re.search(r'<本地路径>]+)\}', line)
        if m:
            names.append(m.group(1))
    return names


def main():
    order = chunk_order()
    notes = []
    for name in order:
        f = os.path.join(CH, name + ".tex")
        if not os.path.exists(f):
            continue
        chapter, section, page = CH_MAP.get(name, ""), "", ""
        chapter = CH_MAP.get(name, chapter)
        for line in open(f, encoding="utf-8"):
            s = line.strip()
            if not s.startswith("%"):
                m = CHAP_RE.search(s)
                if m:
                    chapter = m.group(1); section = ""
                m = SEC_RE.search(s)
                if m:
                    section = m.group(1)
            m = PAGE_RE.search(s)
            if m:
                page = m.group(1)
            m = NOTE_RE.search(s)
            if m:
                txt = m.group(1).strip()
                txt = txt.replace("∘", r"$\circ$").replace("■", r"$\blacksquare$")
                txt = txt.replace("∞", r"$\infty$").replace("−", "-")
                txt = txt.replace("·", r"$\cdot$")
                notes.append([name, chapter, section, page, txt])
    print("notes:", len(notes))

    lines = ["% 自动生成，勿手改（gen_notes.py）", "\\chapter{译校批注}", "",
             "本附录汇集正文中以源码注释形式给出的译校批注，按章节顺序排列。每条注明所在原文页码，便于对照原书。批注只写三类内容：易错预警、省略论证的点拨、背景直觉。<本地路径>", ""]
    cur_ch = None
    for (chunk, ch, sec, pg, txt) in notes:
        if ch != cur_ch:
            cur_ch = ch
            lines.append(f"\\section*{{{ch}}}" if ch else "\\section*{前置与书末}")
            lines.append("")
        ref = f"\\textbf{{（原书 p.{pg}）}}\\ " if pg else ""
        lines.append(f"\\noindent {ref}{txt}<本地路径>")
        lines.append("")
    with open(OUT_TEX, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    md = ["# 译校批注汇总", "", f"共 {len(notes)} 条。", "",
          "| # | 文件 | 章 | 节 | 原书页 | 批注 |", "|---|---|---|---|---|---|"]
    for i, (chunk, ch, sec, pg, txt) in enumerate(notes, 1):
        t = txt.replace("|", "\\|")
        md.append(f"| {i} | {chunk} | {ch or '-'} | {sec or '-'} | {pg} | {t} |")
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("written:", OUT_TEX)
    print("written:", OUT_MD)
    bych = collections.Counter(n[1] or "（未标）" for n in notes)
    print("by chapter:", dict(bych))


if __name__ == "__main__":
    main()
