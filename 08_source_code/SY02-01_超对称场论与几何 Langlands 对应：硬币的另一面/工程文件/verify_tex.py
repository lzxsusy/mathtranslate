#!/usr/bin/env python
# -*- coding: utf-8 -*-\nimport io\nsys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
"""
LaTeX 源码静态检查脚本（无需 TeX 引擎即可运行）。

用法：
    python verify_tex.py                 # 检查 build/sections/*.tex 与 build/*.tex
    python verify_tex.py <file.tex> ...  # 检查指定文件

检查项：
  1. 文件编码与 BOM
  2. 左右文档类命令（分节文件不应含 \documentclass/\begin{document}）
  3. 花括号配平（剔除 \% 与注释后计数）
  4. \begin / \end 环境配对（栈式，跨行）
  5. 未定义宏（对照 preamble.tex 中的 \newcommand/\DeclareMathOperator 与 LaTeX 标准命令）
  6. \cite key 是否都在 references.tex 中
  7. \ref / \eqref 是否有对应 \label
  8. 数学模式内的中文标点（全角）
  9. 批注数量统计（% [Tutor Note:）
 10. keytakeaways 是否存在
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

# 标准/常用命令白名单（非穷尽，覆盖本文实际可能用到的）
STD_CMDS = set("""
documentclass usepackage begin end section subsection subsubsection paragraph label ref eqref cite
item itemize enumerate textbf textit emph textrm texttt textsc mathrm mathbf mathcal mathbb mathsf
mathit mathfrak mathop operatorname frac dfrac tfrac sqrt sum prod int oint partial nabla infty
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi
pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
left right big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr middle
cdot cdots ldots dots vdots ddots times otimes oplus ominus leq geq neq approx sim simeq
simeq cong equiv propto ll gg subset supset subseteq supseteq in notin ni cup cap setminus
forall exists neg wedge vee leftrightarrow Leftrightarrow rightarrow Rightarrow leftarrow Leftarrow
mapsto longrightarrow longleftrightarrow Longrightarrow
langle rangle lfloor rfloor lceil rceil
hat bar tilde vec dot ddot widehat widetilde overline underline overbrace underbrace
stackrel overset underset substack stackrel
boxed fbox hbox mbox text mbox
small skip medskip bigskip noindent newline linebreak pagebreak newpage clearpage
hspace vspace hfill vfill quad qquad enspace thinspace negthinspace
center quote quotation flushleft flushright minipage parbox rule color colorbox textcolor
footnote thanks caption includegraphics resizebox scalebox rotatebox
table tabular array multirow multicolumn hline cline toprule midrule bottomrule
thebibliography bibitem newblock
appendix tableofcontents addcontentsline
verb verbatim
S P dag dagger hbar ell imath jmath Re Im wp
textstyle scriptstyle scriptscriptstyle displaystyle
frac sqrt
newcommand renewcommand providecommand def let
DeclareMathOperator newtheorem theoremstyle
setlength addtolength linespread sloppy flushbottom
label eqref tag notag nonumber
exp log ln sin cos tan det dim ker coker pr
to gets mapsto
mathbf mathbb mathsf mathit mathnormal
displaystyle
limits nolimits
bmod pmod mod
quad
And micro
dag S pilcrow
Biggl Biggr biggl biggr
mathopen mathclose mathbin mathrel mathord mathpunct mathinner
textwidth textheight linewidth columnwidth baselineskip bigskipamount medskipamount smallskipamount
rm bf it sf tt sc em
check sharp flat natural emptyemptyset
lim max min sup inf
emptyset varnothing pm mp sharp cosh sinh tanh log ln exp det dim ker coker pr
qquad
""".split())

# 特殊符号字符命令：\LaTeX \TeX \% \$ \& \# \_ \{ \} \, \; \: \! \\ \ 等
CHAR_CMDS = set(["LaTeX", "TeX", "%", "$", "&", "#", "_", "{", "}", ",", ";", ":", "!", "\\", " ", "\n"])


def strip_comments(text):
    """去掉未转义的 % 之后的内容（保留换行）。"""
    out = []
    for line in text.split("\n"):
        idx = -1
        i = 0
        while i < len(line):
            if line[i] == "\\":
                i += 2
                continue
            if line[i] == "%":
                idx = i
                break
            i += 1
        out.append(line if idx < 0 else line[:idx])
    return "\n".join(out)


def brace_balance(text):
    # 先去掉 \% 与 \{
    t = text.replace("\\%", "").replace("\\{", "").replace("\\}", "")
    t = strip_comments(t)
    depth = 0
    line_no = 1
    problems = []
    for ch in t:
        if ch == "\n":
            line_no += 1
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                problems.append(("brace", line_no, "多余的 }"))
                depth = 0
    if depth != 0:
        problems.append(("brace", 0, "未闭合的 { × %d" % depth))
    return problems


def env_pairs(text):
    t = strip_comments(text)
    stack = []
    problems = []
    for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", t):
        kind, name = m.group(1), m.group(2).strip()
        line_no = t[: m.start()].count("\n") + 1
        if kind == "begin":
            stack.append((name, line_no))
        else:
            if not stack:
                problems.append(("env", line_no, "\\end{%s} 无对应 \\begin" % name))
            else:
                open_name, open_line = stack.pop()
                if open_name != name:
                    problems.append(
                        ("env", line_no, "\\begin{%s}(第%d行) 与 \\end{%s} 不配对" % (open_name, open_line, name))
                    )
    for name, line_no in stack:
        problems.append(("env", line_no, "\\begin{%s} 未闭合" % name))
    return problems


def defined_macros(preamble_path):
    macros = set()
    if not os.path.exists(preamble_path):
        return macros
    text = open(preamble_path, encoding="utf-8", errors="replace").read()
    text = strip_comments(text)
    for m in re.finditer(r"\\(?:new|renew|provide)command\*?\{?\\([A-Za-z@]+)\}?", text):
        macros.add(m.group(1))
    for m in re.finditer(r"\\DeclareMathOperator\*?\{\\([A-Za-z@]+)\}", text):
        macros.add(m.group(1))
    for m in re.finditer(r"\\newtheorem\{([A-Za-z]+)\}", text):
        macros.add("begin{" + m.group(1) + "}")
        macros.add("end{" + m.group(1) + "}")
    for m in re.finditer(r"\\newenvironment\{([A-Za-z]+)\}", text):
        macros.add("begin{" + m.group(1) + "}")
        macros.add("end{" + m.group(1) + "}")
    return macros


def used_macros(text):
    t = strip_comments(text)
    found = {}
    for m in re.finditer(r"\\([A-Za-z@]+)", t):
        name = m.group(1)
        found.setdefault(name, t[: m.start()].count("\n") + 1)
    return found


def main(paths):
    preamble = os.path.join(BASE, "preamble.tex")
    known = defined_macros(preamble) | STD_CMDS | CHAR_CMDS

    refs_text = ""
    refs_path = os.path.join(BASE, "references.tex")
    if os.path.exists(refs_path):
        refs_text = open(refs_path, encoding="utf-8", errors="replace").read()
    bibkeys = set(re.findall(r"\\bibitem\{([^}]*)\}", refs_text))

    all_text = ""
    for p in paths:
        all_text += open(p, encoding="utf-8", errors="replace").read() + "\n"
    all_labels = set(re.findall(r"\\label\{([^}]*)\}", all_text))

    total_notes = 0
    fail = 0
    for p in paths:
        raw = open(p, "rb").read()
        bom = raw.startswith(b"\xef\xbb\xbf")
        text = raw.decode("utf-8", errors="replace")
        clean = strip_comments(text)
        issues = []

        if bom:
            issues.append(("enc", 1, "文件带 UTF-8 BOM"))
        if "\\documentclass" in clean or "\\begin{document}" in clean:
            issues.append(("doc", 1, "分节文件不应包含 \\documentclass 或 \\begin{document}"))

        issues += brace_balance(text)
        issues += env_pairs(text)

        for name, line_no in used_macros(text).items():
            if name in known:
                continue
            if name in ("begin", "end"):
                continue
            issues.append(("macro", line_no, "未定义或未登记的命令 \\%s" % name))

        for m in re.finditer(r"\\cite\{([^}]*)\}", clean):
            for key in m.group(1).split(","):
                key = key.strip()
                if key and refs_text and key not in bibkeys:
                    issues.append(("cite", 1, "\\cite{%s} 在 references.tex 中无对应 \\bibitem" % key))

        for m in re.finditer(r"\\(?:eq)?ref\{([^}]*)\}", clean):
            if m.group(1) not in all_labels:
                issues.append(("ref", 1, "\\ref{%s} 无对应 \\label" % m.group(1)))

        # 数学模式中的全角标点：逐行按未转义 $ 配对扫描（跳过 \$ 与 \%）
        t_disp = re.sub(
            r"\\begin\{(?:equation|align|gather|multline|subequations|eqnarray)\*?\}.*?"
            r"\\end\{(?:equation|align|gather|multline|subequations|eqnarray)\*?\}",
            "", clean, flags=re.S)
        for line in t_disp.split("\n"):
            in_math = False
            j = 0
            while j < len(line):
                ch = line[j]
                if ch == "\\":
                    j += 2
                    continue
                if ch == "$":
                    in_math = not in_math
                elif in_math and ("\u3000" <= ch <= "\u303f" or "\uff00" <= ch <= "\uffef"):
                    issues.append(("punct", 1, "数学模式内出现全角标点：%s" % line[max(0, j - 12):j + 12]))
                j += 1

        notes = len(re.findall(r"^\s*%\s*\[Tutor Note:", text, re.M))
        total_notes += notes
        has_kr = "keytakeaways" in text

        rel = os.path.relpath(p, BASE)
        print("=" * 78)
        print("文件：%s   行数：%d   批注：%d   keytakeaways：%s"
              % (rel, text.count("\n") + 1, notes, "有" if has_kr else "缺"))
        if not has_kr:
            issues.append(("struct", 1, "缺少 keytakeaways 环境"))
        if issues:
            fail += 1
            for kind, line_no, msg in issues:
                loc = ("第%d行 " % line_no) if line_no else ""
                print("  [%s] %s%s" % (kind, loc, msg))
        else:
            print("  OK：未发现问题")

    print("=" * 78)
    print("合计：%d 个文件，%d 个有问题，批注总数 %d，bibitem 总数 %d"
          % (len(paths), fail, total_notes, len(bibkeys)))
    return 1 if fail else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        files = []
        secdir = os.path.join(BASE, "sections")
        if os.path.isdir(secdir):
            files += [os.path.join(secdir, f) for f in sorted(os.listdir(secdir)) if f.endswith(".tex")]
        files += [os.path.join(BASE, "main.tex"), os.path.join(BASE, "glossary.tex")]
        args = [f for f in files if os.path.exists(f)]
    print("待检查：%d 个文件" % len(args))
    sys.exit(main(args))
