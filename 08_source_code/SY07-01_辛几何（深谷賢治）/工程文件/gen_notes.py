# -*- coding: utf-8 -*-
"""从 chunks 提取 % [Tutor Note: ...]（跨文件继承章/节）→ 附录 tex + 译注汇总.md"""
import os, re, collections

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
MAIN = os.path.join(ROOT, "src", "main.tex")
OUT_TEX = os.path.join(CH, "appendix_notes.tex")
OUT_MD = os.path.join(ROOT, "work", "译注汇总.md")

NOTE_RE = re.compile(r'% \[Tutor Note:\s*(.*?)\]\s*$')
PAGE_RE = re.compile(r'% \[原文 p\.(\d+)\]')
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
    notes = []   # (chunk, chapter, section, page, text)
    chapter, section = "", ""
    for name in order:
        f = os.path.join(CH, name + ".tex")
        if not os.path.exists(f):
            continue
        for line in open(f, encoding="utf-8"):
            s = line.strip()
            m = CHAP_RE.search(s)
            if m and not s.startswith("%"):
                chapter = m.group(1)
                section = ""
            m = SEC_RE.search(s)
            if m and not s.startswith("%"):
                section = m.group(1)
            m = PAGE_RE.search(s)
            if m:
                page = m.group(1)
            m = NOTE_RE.search(s)
            if m:
                pg = ""
                txt = m.group(1).strip()
                # 特殊字符转为数学模式（附录正文渲染需要）
                txt = txt.replace("∘", r"$\circ$").replace("■", r"$\blacksquare$")
                txt = txt.replace("∞", r"$\infty$").replace("−", "-")
                notes.append([name, chapter, section, pg, txt])
    # 补页码：逐文件重新扫描，记录每个 note 之前最近的 % [原文 p.N]
    idx = 0
    chapter = section = ""
    for name in order:
        f = os.path.join(CH, name + ".tex")
        if not os.path.exists(f):
            continue
        page = ""
        for line in open(f, encoding="utf-8"):
            s = line.strip()
            m = CHAP_RE.search(s)
            if m and not s.startswith("%"):
                chapter = m.group(1)
                section = ""
            m = SEC_RE.search(s)
            if m and not s.startswith("%"):
                section = m.group(1)
            m = PAGE_RE.search(s)
            if m:
                page = m.group(1)
            m = NOTE_RE.search(s)
            if m:
                notes[idx][3] = page
                idx += 1
    print("notes:", len(notes))

    # ---- 附录 tex ----
    lines = ["% 自动生成，勿手改（gen_notes.py）", "\\chapter{译校批注}", "",
             "本附录汇集正文中以源码注释形式给出的译校批注，按章节顺序排列。每条注明所在原文页码，便于对照原书。批注只写三类内容：易错预警、省略论证的点拨、背景直觉。<本地路径>", ""]
    cur_ch = None
    for (chunk, ch, sec, pg, txt) in notes:
        if ch != cur_ch:
            cur_ch = ch
            if ch:
                lines.append(f"\\section*{{{ch}}}")
            else:
                lines.append("\\section*{前置与书末}")
            lines.append("")
        ref = f"\\textbf{{（原书 p.{pg}）}}\\ " if pg else ""
        lines.append(f"\\noindent {ref}{txt}<本地路径>")
        lines.append("")
    os.makedirs(os.path.dirname(OUT_TEX), exist_ok=True)
    open(OUT_TEX, "w", encoding="utf-8").write("\n".join(lines))

    # ---- markdown 汇总 ----
    md = ["# 译校批注汇总", "", f"共 {len(notes)} 条。", "",
          "| # | 文件 | 章 | 节 | 原书页 | 批注 |", "|---|---|---|---|---|---|"]
    for i, (chunk, ch, sec, pg, txt) in enumerate(notes, 1):
        t = txt.replace("|", "\\|")
        md.append(f"| {i} | {chunk} | {ch or '-'} | {sec or '-'} | {pg} | {t} |")
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(md))
    print("written:", OUT_TEX)
    print("written:", OUT_MD)
    bych = collections.Counter(n[1] or "（未标）" for n in notes)
    print("by chapter:", dict(bych))

if __name__ == "__main__":
    main()
