# -*- coding: utf-8 -*-
"""从 chunks 提取 % [Tutor Note: ...]（跨文件继承章/节）→ 书末附录 tex + 译注汇总.md"""
import os, re, collections

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
MAIN = os.path.join(ROOT, "src", "main.tex")
OUT_TEX = os.path.join(CH, "index_notes.tex")
OUT_MD = os.path.join(ROOT, "work", "译注汇总.md")

NOTE_RE = re.compile(r'% \[Tutor Note:\s*(.*?)\]\s*$')
PAGE_RE = re.compile(r'% \[原文 p\.(\w+)\]')
SEC_RE = re.compile(r'\\(?:section|backsection)\{([^}]*)\}')
CHAP_RE = re.compile(r'<本地路径>')

REPL = [("∘", r"$\circ$"), ("■", r"$\blacksquare$"), ("∞", r"$\infty$"), ("−", "-"),
        ("·", r"$\cdot$"), ("→", r"$\to$"), ("⊗", r"$\otimes$"), ("⊕", r"$\oplus$"),
        ("≅", r"$\cong$"), ("≠", r"$\neq$"), ("≤", r"$\le$"), ("≥", r"$\ge$"),
        ("×", r"$\times$"), ("∈", r"$\in$"), ("φ", r"$\varphi$"), ("ψ", r"$\psi$"),
        ("α", r"$\alpha$"), ("β", r"$\beta$"), ("γ", r"$\gamma$"), ("λ", r"$\lambda$"),
        ("π", r"$\pi$"), ("σ", r"$\sigma$"), ("χ", r"$\chi$"), ("η", r"$\eta$"),
        ("ζ", r"$\zeta$"), ("ω", r"$\omega$"), ("Δ", r"$\Delta$"), ("ε", r"$\varepsilon$")]


def chunk_order():
    names = []
    for line in open(MAIN, encoding="utf-8"):
        m = re.search(r'<本地路径>]+)\}', line)
        if m and m.group(1) != "index_notes":
            names.append(m.group(1))
    return names


def main():
    order = chunk_order()
    notes = []
    chapter, section = "", ""
    for name in order:
        f = os.path.join(CH, name + ".tex")
        if not os.path.exists(f):
            continue
        page = ""
        for line in open(f, encoding="utf-8"):
            s = line.strip()
            if not s.startswith("%"):
                m = CHAP_RE.search(s)
                if m:
                    title = m.group(1) or m.group(2)
                    title = title.replace('\\footnotemark','').replace('\\protect','')
                    chapter, section = title.strip(), ""
                m = SEC_RE.search(s)
                if m and m.group(1):
                    section = m.group(1)
            m = PAGE_RE.search(s)
            if m:
                page = m.group(1)
            m = NOTE_RE.search(s)
            if m:
                txt = m.group(1).strip().replace(chr(92)*2, chr(92))
                for a, b in REPL:
                    txt = txt.replace(a, b)
                notes.append([name, chapter, section, page, txt])
    print("notes:", len(notes))

    lines = ["% 自动生成，勿手改（gen_notes.py）",
             "\\chapter*{译校批注}",
             "<本地路径>",
             "\\markboth{译校批注}{译校批注}",
             "",
             "本附录汇集正文中以源码注释形式给出的译校批注，按原书顺序排列。每条注明所在原书页码，便于对照原书。批注只写三类内容：易错预警、省略论证的点拨、背景直觉。<本地路径>", ""]
    cur_ch = None
    for (chunk, ch, sec, pg, txt) in notes:
        if ch != cur_ch:
            cur_ch = ch
            title = ch if ch else "卷首与书末"
            lines.append(f"\\section*{{{title}}}")
            lines.append(f"\\addcontentsline{{toc}}{{section}}{{{title}}}")
            lines.append("")
        ref = f"\\textbf{{（原书 p.{pg}）}}\\ " if pg else ""
        see = f" \\textit{{（{sec}）}}" if sec else ""
        lines.append(f"\\noindent {ref}{txt}{see}<本地路径>")
        lines.append("")
    with open(OUT_TEX, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    md = ["# 译校批注汇总", "", f"共 {len(notes)} 条。", "",
          "| # | 文件 | 章 | 节 | 原书页 | 批注 |", "|---|---|---|---|---|---|"]
    for i, (chunk, ch, sec, pg, txt) in enumerate(notes, 1):
        t = txt.replace("|", "\\|")
        md.append(f"| {i} | {chunk} | {ch or '-'} | {sec or '-'} | {pg} | {t} |")
    with open(OUT_MD, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(md))
    print("written:", OUT_TEX)
    bych = collections.Counter(n[1] or "（未标）" for n in notes)
    for k, v in bych.items():
        print("  ", k, v)


if __name__ == "__main__":
    main()
