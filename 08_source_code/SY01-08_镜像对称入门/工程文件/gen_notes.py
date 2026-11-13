# -*- coding: utf-8 -*-
"""从 chunks 提取 % [Tutor Note: ...] → src/chunks/appendix_notes.tex + 译注汇总.md

JPB07 版要点（与原《辛几何》工程的区别）：
  * 页标记格式不同：本工程逐页写 `% ===== PDF p.024 (原书 p.16) =====`，
    页码取括号里的「原书 p.N」，既可能是阿拉伯数字也可能是罗马数字（前置页）。
  * 节标题多为无编号形式（\\section* / \\subsection*），因此三种都要认。
  * 译注汇总.md 写到工程根目录（交付七件套之一）。
"""
import os, re, collections

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
MAIN = os.path.join(ROOT, "src", "main.tex")
OUT_TEX = os.path.join(CH, "appendix_notes.tex")
OUT_MD = os.path.join(ROOT, "译注汇总.md")

NOTE_RE = re.compile(r"%\s*\[Tutor Note:\s*(.*?)\]\s*$")
PAGE_RE = re.compile(r"%\s*=+\s*PDF\s*p\.?\s*\d+\s*\(\s*原书\s*p\.?\s*([0-9]+|[ivxlc]+)\s*\)")
SEC_RE = re.compile(r"\\(?:sub)*section\*?\{([^}]*)\}")
CHAP_RE = re.compile(r"<本地路径>")


def chunk_order():
    names = []
    for line in open(MAIN, encoding="utf-8"):
        m = re.search(r"<本地路径>]+)\}", line)
        if m:
            names.append(m.group(1))
    return names


SYM = {
    "ψ": r"\psi", "φ": r"\phi", "ϕ": r"\phi", "η": r"\eta", "δ": r"\delta",
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "λ": r"\lambda", "μ": r"\mu",
    "ν": r"\nu", "π": r"\pi", "ρ": r"\rho", "σ": r"\sigma", "τ": r"\tau",
    "χ": r"\chi", "ω": r"\omega", "κ": r"\kappa", "θ": r"\theta", "ξ": r"\xi",
    "ζ": r"\zeta", "Λ": r"\Lambda", "Σ": r"\Sigma", "Ω": r"\Omega", "Φ": r"\Phi",
    "Ψ": r"\Psi", "Γ": r"\Gamma", "Δ": r"\Delta", "Θ": r"\Theta",
    "∞": r"\infty", "∩": r"\cap", "∪": r"\cup", "⊂": r"\subset", "⊃": r"\supset",
    "∈": r"\in", "∉": r"\notin", "→": r"\to", "←": r"\leftarrow", "⇒": r"\Rightarrow",
    "⇔": r"\Leftrightarrow", "×": r"\times", "⊗": r"\otimes", "⊕": r"\oplus",
    "≤": r"\le", "≥": r"\ge", "≠": r"\ne", "≅": r"\cong", "≈": r"\approx",
    "∼": r"\sim", "∓": r"\mp", "±": r"\pm", "∂": r"\partial", "∇": r"\nabla",
    "∑": r"\sum", "∏": r"\prod", "√": r"\surd", "∘": r"\circ", "■": r"\blacksquare",
    "□": r"\square", "·": r"\cdot", "◦": r"\circ", "′": r"'", "−": "-",
    "ℤ": r"\mathbb{Z}", "ℝ": r"\mathbb{R}", "ℂ": r"\mathbb{C}", "ℚ": r"\mathbb{Q}",
    "ℙ": r"\mathbb{P}", "ℤ": r"\mathbb{Z}",
}
MATH_OK = set("$")


def latexify(txt):
    """把批注文本转成能在附录正文安全排版的 LaTeX：
    逐段处理 $...$ 之外的字符——转义 # & _ % 等 LaTeX 特殊字符，
    把裸 Unicode 数学符号包进 $...$。"""
    out, buf, in_math = [], [], False
    i = 0
    while i < len(txt):
        ch = txt[i]
        if ch == "$" and (i == 0 or txt[i - 1] != "\\"):
            out.append("".join(buf))
            buf = []
            in_math = not in_math
            out.append("$")
            i += 1
            continue
        if in_math:
            out.append(ch)
        else:
            buf.append(ch)
        i += 1
    out.append("".join(buf))
    seg = "".join(out)
    # 重新按 $ 切分：偶数段（数学外）转义 + 符号替换
    parts = seg.split("$")
    for k in range(0, len(parts), 2):
        s = parts[k]
        s = s.replace("#", r"\#").replace("&", r"\&").replace("%", r"\%")
        s = s.replace("_", r"\_").replace("^", r"\^{}")
        # 裸 Unicode 数学符号
        res = []
        for ch in s:
            if ch in SYM:
                res.append("$" + SYM[ch] + "$")
            else:
                res.append(ch)
        parts[k] = "".join(res)
    return "$".join(parts)
    return seg


def main():
    order = chunk_order()
    notes = []   # [chunk, chapter, section, page, text]
    chapter = section = ""
    for name in order:
        f = os.path.join(CH, name + ".tex")
        if not os.path.exists(f):
            continue
        for line in open(f, encoding="utf-8"):
            s = line.strip()
            if not s.startswith("%"):
                m = CHAP_RE.search(s)
                if m:
                    chapter, section = m.group(1), ""
                m = SEC_RE.search(s)
                if m:
                    section = m.group(1)
            m = PAGE_RE.search(s)
            if m:
                page = m.group(1)
            m = NOTE_RE.search(s)
            if m:
                txt = m.group(1).strip()
                txt = (txt.replace("・", "·").replace("∘", r"$\circ$")
                          .replace("■", r"$\blacksquare$").replace("∞", r"$\infty$")
                          .replace("−", "-"))
                notes.append([name, chapter, section, page, txt])
    # 重新扫一遍，给每条批注补上它前面最近的页标记
    idx = 0
    chapter = section = page = ""
    for name in order:
        f = os.path.join(CH, name + ".tex")
        if not os.path.exists(f):
            continue
        # 分块文件（ch08b / ch12b 等）没有 \chapter，沿用上一块的章名；
        # 否则这些批注在附录里会落到「前置与书末」节。2026-11-09 tr2 终校。
        for line in open(f, encoding="utf-8"):
            s = line.strip()
            if not s.startswith("%"):
                m = CHAP_RE.search(s)
                if m:
                    chapter, section = m.group(1), ""
                m = SEC_RE.search(s)
                if m:
                    section = m.group(1)
            m = PAGE_RE.search(s)
            if m:
                page = m.group(1)
            m = NOTE_RE.search(s)
            if m:
                if idx < len(notes):
                    notes[idx][1] = chapter
                    notes[idx][2] = section
                    notes[idx][3] = page
                idx += 1
    print("notes:", len(notes))

    # ---- 附录 tex ----
    lines = ["% 自动生成，勿手改（gen_notes.py）", "\\chapter{译校批注}", "",
             "本附录汇集正文中以源码注释形式给出的译校批注，按章节顺序排列。每条注明所在原书页码，便于对照原书。"
             "批注只写三类内容：易错预警（符号、指标、约定）、作者省略论证的点拨、背景直觉。"
             "原书疑似笔误一律照原样排，仅在批注中指出。<本地路径>", ""]
    cur = None
    for (chunk, ch, sec, pg, txt) in notes:
        if ch != cur:
            cur = ch
            num = re.match(r"ch(\d\d)", os.path.basename(chunk))
            if ch and num:
                lines.append("\\section*{第 %d 章\\quad %s}" % (int(num.group(1)), ch))
            else:
                lines.append("\\section*{%s}" % (ch if ch else "前置与书末"))
            lines.append("")
        head = "（原书 p.%s）" % pg if pg else ""
        if sec:
            head = (head + "\\ " if head else "") + "\\textbf{§ %s}\\ " % sec
        lines.append("\\noindent %s%s<本地路径>" % (head, latexify(txt)))
        lines.append("")
    os.makedirs(os.path.dirname(OUT_TEX), exist_ok=True)
    open(OUT_TEX, "w", encoding="utf-8").write("\n".join(lines))

    # ---- markdown 汇总 ----
    md = ["# 译校批注汇总", "", "共 %d 条。" % len(notes), "",
          "| # | 文件 | 章 | 节 | 原书页 | 批注 |", "|---|---|---|---|---|---|"]
    for i, (chunk, ch, sec, pg, txt) in enumerate(notes, 1):
        t = txt.replace("|", "\\|")
        md.append("| %d | %s | %s | %s | %s | %s |" % (i, chunk, ch or "-", sec or "-", pg or "-", t))
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(md))
    print("written:", OUT_TEX)
    print("written:", OUT_MD)
    print("by chapter:", dict(collections.Counter(n[1] or "（未标）" for n in notes)))


if __name__ == "__main__":
    main()
