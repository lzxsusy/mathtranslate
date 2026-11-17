# -*- coding: utf-8 -*-
"""把 cards.json 组装成《定义与定理资料卡》LaTeX 源，并跑 xelatex 两遍。"""
import io, json, os, re, subprocess

BASE = r"C:\Users\admin\Downloads\陈麟_代数几何1_译注工程\资料卡"
SRC = r"C:\Users\admin\Downloads\陈麟_代数几何1_译注工程\源码"
TEX = os.path.join(BASE, "代数几何资料卡.tex")
CORE = {"definition", "theorem", "proposition", "lemma", "corollary", "claim",
        "predefinition", "propdef"}

cards = json.load(io.open(os.path.join(BASE, "cards.json"), encoding="utf-8"))
secs = json.load(io.open(os.path.join(BASE, "sections.json"), encoding="utf-8"))
core = [c for c in cards if c["env"] in CORE]

MACROS = r"""
% ---- 书本宏（与译注本 preamble 一致）----
\newcommand{\Z}{\mathbb{Z}}\newcommand{\Q}{\mathbb{Q}}\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}\newcommand{\N}{\mathbb{N}}\newcommand{\F}{\mathbb{F}}
\newcommand{\A}{\mathbb{A}}\newcommand{\PP}{\mathbb{P}}\newcommand{\GG}{\mathbb{G}}
\newcommand{\bbk}{\mathbb{k}}
\newcommand{\cA}{\mathcal{A}}\newcommand{\cB}{\mathcal{B}}\newcommand{\cC}{\mathcal{C}}
\newcommand{\cD}{\mathcal{D}}\newcommand{\cE}{\mathcal{E}}\newcommand{\cF}{\mathcal{F}}
\newcommand{\cG}{\mathcal{G}}\newcommand{\cI}{\mathcal{I}}\newcommand{\cJ}{\mathcal{J}}
\newcommand{\cK}{\mathcal{K}}\newcommand{\cL}{\mathcal{L}}\newcommand{\cM}{\mathcal{M}}
\newcommand{\cN}{\mathcal{N}}\newcommand{\cO}{\mathcal{O}}\newcommand{\cP}{\mathcal{P}}
\newcommand{\cQ}{\mathcal{Q}}\newcommand{\cR}{\mathcal{R}}\newcommand{\cS}{\mathcal{S}}
\newcommand{\cT}{\mathcal{T}}\newcommand{\cU}{\mathcal{U}}\newcommand{\cV}{\mathcal{V}}
\newcommand{\cW}{\mathcal{W}}\newcommand{\cX}{\mathcal{X}}\newcommand{\cY}{\mathcal{Y}}
\newcommand{\cZ}{\mathcal{Z}}
\newcommand{\Spec}{\operatorname{Spec}}\newcommand{\Spm}{\operatorname{Spm}}
\newcommand{\Proj}{\operatorname{Proj}}\newcommand{\Spv}{\operatorname{Spv}}
\newcommand{\Hom}{\operatorname{Hom}}\newcommand{\uHom}{\underline{\mathrm{Hom}}}
\newcommand{\End}{\operatorname{End}}\newcommand{\Aut}{\operatorname{Aut}}
\newcommand{\Isom}{\operatorname{Isom}}\newcommand{\id}{\operatorname{id}}
\newcommand{\coker}{\operatorname{coker}}\newcommand{\im}{\operatorname{im}}
\newcommand{\Ker}{\operatorname{Ker}}\newcommand{\Ob}{\operatorname{Ob}}
\newcommand{\Mor}{\operatorname{Mor}}\newcommand{\Frac}{\operatorname{Frac}}
\newcommand{\Pic}{\operatorname{Pic}}\newcommand{\Supp}{\operatorname{Supp}}
\newcommand{\cHom}{\underline{\mathcal{H}om}}
\newcommand{\Ext}{\operatorname{Ext}}\newcommand{\Tor}{\operatorname{Tor}}
\newcommand{\coim}{\operatorname{coim}}
\newcommand{\colim}{\operatorname*{colim}}
\newcommand{\CRing}{\mathsf{CRing}}\newcommand{\Ring}{\mathsf{Ring}}
\newcommand{\Set}{\mathsf{Set}}\newcommand{\Ab}{\mathsf{Ab}}
\newcommand{\Grp}{\mathsf{Grp}}\newcommand{\Top}{\mathsf{Top}}
\newcommand{\Sch}{\mathsf{Sch}}\newcommand{\PShv}{\mathsf{PShv}}
\newcommand{\Shv}{\mathsf{Shv}}\newcommand{\Mod}{\mathsf{Mod}}
\newcommand{\Vect}{\mathsf{Vect}}\newcommand{\QCoh}{\mathsf{QCoh}}
\newcommand{\Coh}{\mathsf{Coh}}\newcommand{\Sym}{\operatorname{Sym}}
\newcommand{\op}{\mathrm{op}}
\newcommand{\smallcat}[1]{\mathsf{#1}}
\newcommand{\omod}{\cO_X\text{-}\mathsf{mod}}
\newcommand{\omodP}{\cO_X\text{-}\mathsf{mod}^{\PShv}}
\newcommand{\lto}{\longrightarrow}\newcommand{\into}{\hookrightarrow}
\newcommand{\longmapsfrom}{\mathrel{\rotatebox[origin=c]{180}{$\longmapsto$}}}
\newcommand{\mapsfrom}{\mathrel{\reflectbox{$\mapsto$}}}
\newcommand{\Zc}{\Z}\newcommand{\PPc}{\PP}
"""

PREAMBLE = r"""\documentclass[UTF8,10pt,fontset=windows]{ctexart}
\usepackage[a4paper,top=18mm,bottom=17mm,left=16mm,right=16mm,headsep=5mm]{geometry}
\usepackage{xcolor}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{tikz-cd}
\usepackage{enumitem}
\usepackage{booktabs,longtable,array}
\usepackage[most]{tcolorbox}
\usepackage{needspace}
\usepackage{fancyhdr}
\usepackage[hidelinks,bookmarksnumbered]{hyperref}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont{Latin Modern Mono}
\setCJKmainfont{SimSun}[BoldFont=SimHei,ItalicFont=KaiTi,BoldItalicFont=SimHei]
\setCJKsansfont{Microsoft YaHei}[BoldFont=Microsoft YaHei]
\setCJKmonofont{SimSun}
\linespread{1.30}
\emergencystretch=2.5em
\parindent=0pt
\parskip=2.4pt

\definecolor{ink}{HTML}{1F3A5F}
\definecolor{accent}{HTML}{B06A2C}
\definecolor{cardbg}{HTML}{FCFAF5}
\definecolor{yzbg}{HTML}{F4F1E8}
\definecolor{rulegray}{HTML}{D8D2C4}
\definecolor{metagray}{HTML}{8A8272}

\newcommand{\yizhu}[1]{\par\vspace{1.6pt}%
  {\color{accent}\vrule width 1.2pt}\hspace{3pt}%
  \begin{minipage}[t]{\dimexpr\linewidth-4pt\relax}\sloppy%
  {\color{ink}\sffamily\bfseries\scriptsize 译注}\hspace{2pt}{\small #1}%
  \end{minipage}\par\vspace{1pt}}

\newtcolorbox{card}[2]{enhanced,breakable,colback=cardbg,colframe=rulegray,
  boxrule=0.4pt,arc=1.5pt,left=3.6mm,right=3.2mm,top=2.0mm,bottom=2.4mm,
  fonttitle=\sffamily\bfseries\small,coltitle=white,colbacktitle=ink,
  title={#1\hfill{\mdseries\scriptsize\color{white!85!ink}#2}},
  title after break={\sffamily\bfseries\small #1\hfill{\mdseries\scriptsize\color{white!85!ink}#2（续）}},
  before skip=4pt,after skip=5pt,toprule at break=0pt}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\kaishu\small 代数几何讲义 I\,·\,定义与定理资料卡}
\fancyhead[R]{\kaishu\small\leftmark}
\renewcommand{\headrulewidth}{0.4pt}
\fancyfoot[C]{\small\thepage}

\newcommand{\cardssec}[2]{%
  \needspace{6\baselineskip}\par\addvspace{6mm}%
  \phantomsection\addcontentsline{toc}{section}{#1\quad #2}%
  \noindent{\sffamily\bfseries\large #1\quad #2}\par\vspace{1.4mm}%
  {\color{accent}\rule{\linewidth}{0.9pt}}\par\vspace{3.4mm}%
  \markboth{#1\ #2}{#1\ #2}}

"""


MATH_ENVS = {"equation", "equation*", "align", "align*", "gather", "gather*",
             "multline", "multline*", "aligned", "split", "matrix", "pmatrix",
             "bmatrix", "vmatrix", "array", "cases", "tikzcd"}


def clean(body):
    out, stack = [], []
    for line in body.split("\n"):
        opens = re.findall(r"\\begin\{([^}]+)\}", line)
        closes = re.findall(r"\\end\{([^}]+)\}", line)
        if line.strip() == "" and stack:
            continue
        out.append(line)
        for o in opens:
            stack.append(o)
        for c in closes:
            if c in stack:
                stack.remove(c)
    return "\n".join(out)


def esc_short(s, n):
    s = s.replace("\\", "")
    return s if len(s) <= n else s[:n] + "…"


LOCAL = []
_seen = set()
for f in sorted([x for x in os.listdir(SRC) if re.match(r"sec\d\d\.tex$", x)]) + ["appendixA.tex"]:
    for line in io.open(os.path.join(SRC, f), encoding="utf-8").read().splitlines():
        m = re.match(r"\\(?:providecommand|newcommand|DeclareMathOperator)\*?\{(\\[A-Za-z]+)\}", line.strip())
        if m and m.group(1) not in _seen:
            _seen.add(m.group(1)); LOCAL.append(line.strip())
print("local macros:", len(LOCAL))

out = io.StringIO()
w = out.write
w(PREAMBLE)
w(MACROS + "\n".join(LOCAL) + "\n")
w(r"""
\begin{document}
\begin{titlepage}
\centering
\vspace*{34mm}
{\sffamily\bfseries\fontsize{30}{38}\selectfont 代数几何讲义 I\par}
\vspace{5mm}
{\sffamily\fontsize{17}{22}\selectfont 定义与定理资料卡\par}
\vspace{12mm}
{\color{accent}\rule{0.55\linewidth}{1.1pt}\par}
\vspace{10mm}
{\large 预层与层\,·\,概形\,·\,凝聚层\,·\,射影态射\par}
\vspace{26mm}
\begin{minipage}{0.72\linewidth}\centering\small
本册把《代数几何讲义 I（中译注本）》中的定义、定理、命题、引理、推论与断言逐条裁出，
每条一张卡片，按原书节次排列，并注明所属小节与原书页码。\\
卡片正文与译注均取自译注本，公式、记号、编号一律与原书对应。
\end{minipage}
\vfill
{\small 底本：Lin Chen, \emph{Notes for Algebraic Geometry 1}（2025 年秋，171 页）\par}
\vspace{4mm}
{\small 二〇二六年十一月\par}
\end{titlepage}

\thispagestyle{empty}
{\small\makeatletter\renewcommand{\addvspace}[1]{\vspace{0.42em}}\makeatother\tableofcontents}
\clearpage
""")

serial = 0
for s in secs:
    no, title = s["no"], s["title"]
    group = [c for c in core if c["section"] == no]
    if not group:
        continue
    w("\\cardssec{%s}{%s}\n" % (no, title))
    for c in group:
        serial += 1
        meta_bits = []
        parts = c["num"].rsplit(".", 1)
        if len(parts) == 2:
            meta_bits.append("§" + parts[0])
        if c["page"]:
            meta_bits.append("p.%d" % c["page"])
        meta = " · ".join(meta_bits)
        head = "%s %s" % (c["cn"], c["num"])
        w("\\begin{card}{%s}{%s}\n" % (head, meta))
        w(clean(c["body"].strip()) + "\n")
        if c["yizhu"].strip():
            w("\\yizhu{%s}\n" % clean(c["yizhu"].strip()))
        w("\\end{card}\n")
    w("\n")

w(r"""
\clearpage
\cardssec{}{条目索引}
\noindent{\small 下表列出全部 366 条卡片；「原书页」一栏是条目在原书（译注本）中的页码。}\par\vspace{2mm}
\renewcommand{\arraystretch}{1.18}
{\small\begin{longtable}{@{}p{0.355\linewidth}p{0.085\linewidth}p{0.355\linewidth}p{0.085\linewidth}@{}}
\toprule
\textbf{条目} & \textbf{原书页} & \textbf{条目} & \textbf{原书页} \\
\midrule
\endfirsthead
\toprule
\textbf{条目} & \textbf{原书页} & \textbf{条目} & \textbf{原书页} \\
\midrule
\endhead
""")
idx = [( "%s %s" % (c["cn"], c["num"]), c["page"] or 0) for c in core]
half = (len(idx) + 1) // 2
for i in range(half):
    l = idx[i]
    r = idx[i + half] if i + half < len(idx) else ("", "")
    w("%s & %s & %s & %s \\\\\n" % (l[0], l[1] or "", r[0], r[1] or ""))
w(r"""\bottomrule
\end{longtable}}
\end{document}
""")

io.open(TEX, "w", encoding="utf-8").write(out.getvalue())
print("cards:", len(core), "sections:", len([s for s in secs if any(c['section'] == s['no'] for c in core)]))
print("tex bytes:", os.path.getsize(TEX))

env = dict(os.environ, PATH=r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64;" + os.environ["PATH"])
for i in (1, 2):
    p = subprocess.run(["xelatex", "-interaction=nonstopmode", "代数几何资料卡.tex"],
                       cwd=BASE, env=env, capture_output=True)
    log = io.open(os.path.join(BASE, "代数几何资料卡.log"), encoding="utf-8", errors="replace").read()
    errs = [l for l in log.splitlines() if l.startswith("!")]
    print("pass", i, "rc", p.returncode, "errors", len(errs))
    if errs:
        print("\n".join(errs[:6]))
        break
