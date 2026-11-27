# -*- coding: utf-8 -*-
"""cards_data.py — sy0246 十四张资料卡的数据（make_cards.py 调用）。

每张卡的法文引文都由 make_cards.quote / qj 从底本文本层现取现拼，取不到即 assert。
anchor 由 make_cards.anchor / line_anchor 扫译稿源码行号生成。
"""


def build(m):
    card = m.card
    src = m.src
    qj = m.qj
    anchor = m.anchor
    line_anchor = m.line_anchor
    e1 = m.e1
    vcheck = m.vcheck

    ID = {
        "intro": "sy0246/concept/drinfeld-langlands-correspondence",
        "betti": "sy0246/concept/betti-setting",
        "fourier": "sy0246/concept/homogeneous-fourier",
        "proper": "sy0246/concept/proper-perverse",
        "gl1": "sy0246/concept/gl1-aut-e",
        "hecke": "sy0246/concept/hecke-operator",
        "mainthm": "sy0246/concept/main-theorem-fgv",
        "ldE": "sy0246/concept/perverse-LdE",
        "autp": "sy0246/concept/aut-prime-E",
        "unstable": "sy0246/concept/very-unstable",
        "diag": "sy0246/concept/fundamental-diagram",
        "vanish": "sy0246/concept/vanishing-theorem",
        "descent": "sy0246/concept/descent",
    }
    TRACK = "几何 Langlands"
    TEX = "https://arxiv.org/e-print/math/0207078"
    FGV = "https://arxiv.org/pdf/math/0012255v3"
    GAI = "https://arxiv.org/pdf/math/0204081v2"
    BG = "https://arxiv.org/pdf/math/9912097v2"
    LAU3 = "https://arxiv.org/abs/math/0207129"

    C = []

    # 1 ------------------------------------------------------------------
    C.append(card(
        ID["intro"], TRACK,
        "Drinfeld–Langlands 对应（几何 Langlands 对应）",
        ["几何 Langlands 对应", "correspondance de Drinfeld-Langlands",
         "geometric Langlands correspondence"],
        "全篇总纲：X 上 G-丛模空间的自守侧对象应与 X 上 Ĝ-局部系统对应；"
        "G=GL(1) 是几何类域论，G=GL(n) 的主定理由 FGV 给出。",
        "几何 Langlands 对应断言什么？Laumon 在报告中把讨论限制在什么范围？",
        {"text": "设 $k$ 为域，$X$ 为 $k$ 上光滑拟射影曲线，$F=k(X)$，$G$ 为 $F$ 上分裂约化群，"
                 "$\\hat G$ 为其 Langlands 对偶。Drinfeld–Langlands 对应预测：$X$ 上 $G$-丛模空间"
                 "（配以 Hecke 对应）的系数化导出范畴中的 Hecke 特征层，与 $X$ 上 $\\hat G$-局部系统的"
                 "模空间之间存在对应。严格陈述须先选定上同调理论；本篇取 Betti 三元组。",
         "notation": "$X$, $F=k(X)$, $G$, $\\hat G$, $\\Fib_n(X)$, $\\Aut_E$"},
        ["$G=\\GL(1)$ 时即 Rosenlicht–Lang 几何类域论，自守侧对象由定理 1.2 的 $\\Aut_E$ 给出。",
         "$G=\\GL(2)$ 的几何对应由 Drinfeld [Dr 2][Dr 3] 处理；（整体的）Langlands 对应则在函数域上由 Drinfeld [Dr 1]（$n=2$）与 Lafforgue [La]（任意 $n$）证明，数域情形仍是重大未决问题。",
         "本篇只讨论 $X$ 射影（处处非分歧）、$G=\\GL(n)$ 的情形，主定理为定理 2.2。",
         "$\\hat G$ 是复约化群，其根为 $G$ 的余根；$\\GL(n)$ 的对偶为 $\\GL(n,\\C)$。"],
        ["$\\Bun_G(X)\\;\\leftrightarrow\\;\\LocSys_{\\hat G}(X)$"],
        [],
        ["把「处处非分歧」误解为对群 $G$ 的限制；它限制的是所论的 $X$（射影曲线）与对象。",
         "把自守侧对象当成函数或自守表示；在几何 Langlands 中它是反常层。"],
        [ID["betti"], ID["gl1"], ID["mainthm"]],
        [src(1, "引言（原文 p1）",
             "La correspondance de Drinfeld-Langlands, dite aussi de Langlands géométrique",
             "où k est un corps arbitraire.",
             line_anchor("s00-intro.tex", "Drinfeld–Langlands 对应，又称几何 Langlands 对应"))],
        [e1(1, "原文第 1 页给出对应的一般陈述，并说明本篇只处理 $X$ 射影、$G=\\GL(n)$、FGV 的工作。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "解压所得 Bourbaki2002.tex 与 PDF 第 1 页逐句对应，为措辞的最终校对件。", "supports"),
         vcheck("FGV, arXiv:math/0012255v3 第 4 页", FGV + "#page=4",
                "以 Conjecture 1.3 陈述同一对应（一般 $n$），与本卡 definition 一致。", "partial"),
         vcheck("本工程译稿 引言", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s00-intro.tex:L12-L16",
                "中译与上引法文逐句对应，未增补原文所无论证。", "supports")]))

    # 2 ------------------------------------------------------------------
    C.append(card(
        ID["betti"], TRACK,
        "Betti 三元组与 $D^b_c$ 的工作框架",
        ["Betti 上同调理论", "Betti 三元组", "constructible derived category"],
        "本篇的技术底座：底域 $k=\\C$、系数域 $C$ 特征 $0$ 代数闭，用解析叠上的可构造导出范畴"
        "$\\Dbc(\\cS)$，从而绕开 $\\ell$-进情形对 $\\operatorname{char} k>0$ 的额外要求。",
        "Laumon 报告在哪种上同调理论中工作？这个选择带来什么方便与什么代价？",
        {"text": "取 (Betti) 三元组：$k=\\C$，$C$ 为特征 $0$ 的代数闭域；对 $\\C$ 上局部有限型代数叠 "
                 "$\\cS$，$\\Dbc(\\cS)$ 记相伴解析叠上具有有界可构造上同调的 $C$-向量空间层复形的导出范畴。"
                 "当 $\\cS=[S/G]$ 时，它就是 Bernstein–Lunts 的 $D^b_{G(\\C)^{\\mathrm{an}}}(S(\\C)^{\\mathrm{an}})$。",
         "notation": "$k=\\C$, $C$, $\\Dbc(\\cS)$, $\\Perv(\\cS)$"},
        ["对可表态射，六函子 $f_*,f_!,f^*,f^!$ 齐备；中间反常 $t$-结构的心 $\\Perv$ 阿贝尔、Noether、Artin、自对偶（两者见原文 p3）。",
         "模空间一律按代数叠处理，采用 [L-M] 的叠语言。",
         "FGV 原文用 $\\ell$-进三元组，并为几何 Fourier 变换额外假设 $\\operatorname{char} k=p>0$；本篇指出这一限制并不必要。",
         "原文同时指出：Betti 情形下解析叠的一般理论尚待写出。"],
        [],
        [],
        ["把系数域 $C$ 与底域 $k$ 混同：Betti 情形 $k=\\C$，而斜体 $C$ 始终指系数域。",
         "以为任意代数叠上六函子形式体系都已建立；原文明确说它「尚未得到系统的建立」。"],
        [ID["intro"], ID["fourier"]],
        [src(2, "0. 预备（原文 p2）",
             "Dans le cas partout non ramifié",
             "théorie cohomologique à coefficients dans C",
             line_anchor("s01-prelim.tex", "本文讨论处处非分歧的情形"))],
        [e1(2, "原文第 2 页列出三种三元组，并声明本文采用 Betti 三元组，底域 $k=\\C$。"),
         e1(3, "原文第 3 页给出六函子、反常 $t$-结构，以及 $\\Perv$ 的阿贝尔性、Noether 性、Artin 性与自对偶性。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 中三种三元组的条目与 PDF 完全一致。", "supports"),
         vcheck("Bernstein–Lunts, LNM 1578", "https://doi.org/10.1007/BFb0073549",
                "DOI 页确认该书为 LNM 1578、1994 年出版；只核书目，不构成对正文「范畴等价」的证明。", "partial"),
         vcheck("本工程译稿 第 0 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s01-prelim.tex:L10-L19",
                "中译保留三种三元组与 Betti 选择的说明，译注标明 $C$ 与 $k$ 的区别。", "supports")]))

    # 3 ------------------------------------------------------------------
    C.append(card(
        ID["fourier"], TRACK,
        "齐次 Fourier 变换 $\\Four_{V/S}$",
        ["齐次 Fourier 变换", "几何 Fourier 变换", "homogeneous Fourier transform"],
        "$\\Gm$-等变复形上的 Fourier 变换：由公式 (0.1) 定义，是导出范畴的等价、与对偶交换、"
        "关于反常 $t$-结构 $t$-正合；它是 §5 构造 $\\Aut'_E$ 的主要工具（还要配合 $j_!$、$(j^\\vee)^*$、$(\\iota_i)_*$ 与 $\\sL^d_E$）。",
        "齐次 Fourier 变换如何定义？它有哪些函子性质？",
        {"text": "设 $\\pi:\\cV\\to\\cS$ 为秩 $r$ 的向量丛，$\\overline{\\cV}=[\\cV/\\Gm]$ 为按数乘取商所得的叠，$\\overline{\\cV}{}^\\vee$ 为对偶丛。"
                 "齐次 Fourier 变换 $\\Four_{\\cV/\\cS}:\\Dbc(\\overline{\\cV})\\to\\Dbc(\\overline{\\cV}{}^\\vee)$ 由 (0.1) 定义；"
                 "它是导出范畴的等价，逆变换为 $\\Four_{\\overline{\\cV}^\\vee/\\cS}$，与 Verdier 对偶交换，"
                 "并且关于反常 $t$-结构 $t$-正合。",
         "notation": "$\\cV$, $\\cV^\\vee$, $r$, $\\Psi$, $\\mu:\\cV\\times_\\cS\\cV^\\vee\\to\\cA$"},
        ["$\\Psi=\\beta_*\\C$，其中 $\\beta:[\\Gm/\\Gm]=\\mathrm{pt}\\hookrightarrow\\cA=[\\A^1/\\Gm]$；$H^0(\\Psi)=\\C$，$H^1(\\Psi)=\\alpha_*\\C$。",
         "$p,p^\\vee$ 不可表，$(p^\\vee)_!$ 不保持 $\\Dbc$；原文强调须验证有界性。",
         "$\\Gm$ 按数乘作用在 $\\cV$ 上，取商后 (0.1) 才是 $\\cS$ 上的公式。"],
        ["$\\Four_{\\cV/\\cS}(K)=(p^\\vee)_!\\,\\bigl(p^*K\\otimes\\mu^*\\Psi\\bigr)[r-1]$"],
        [],
        ["把 $\\Psi$ 当成常数层：$H^0(\\Psi)=\\C$，但 $H^1(\\Psi)=\\alpha_*\\C\\neq 0$。",
         "漏掉平移 $[r-1]$。"],
        [ID["proper"], ID["diag"]],
        [src(3, "0. 预备（原文 p3）",
             "On a une transformation de Fourier géométrique",
             "associée au fibré vectoriel V/S (cf. [Lau 3]).",
             line_anchor("s01-prelim.tex", "齐次 Fourier 变换（参 [Lau 3]）"))],
        [e1(3, "原文第 3 页给出齐次 Fourier 变换的等价性、逆与 $t$-正合性；(0.1) 的显式公式在下一页（p4）。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 中 (0.1) 的系数与平移 $[r-1]$ 与 PDF 一致。", "supports"),
         vcheck("Laumon, arXiv:math/0207129（[Lau 3]）", LAU3,
                "该文经 arXiv/Crossref 核验存在（Bull. SMF 131 (2003) 527–551）；原文把齐次 Fourier 变换归于它，内容未逐条比对。", "partial"),
         vcheck("本工程译稿 第 0 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s01-prelim.tex:L29-L45",
                "中译保留 (0.1) 的配对 $\\mu$、投影与平移，未改写公式。", "supports")]))

    # 4 ------------------------------------------------------------------
    C.append(card(
        ID["proper"], TRACK,
        "proper 反常层与 Radon 变换",
        ["proper 反常层", "propre", "Radon 变换"],
        "$P(\\cV)$ 上反常层「proper」的定义 (0.2)、判据 (0.3)，以及 (0.4)：proper 性使 "
        "$\\Four(j_!L)$ 仍 proper，且在 $P(\\cV^\\vee)$ 上化为 Radon 变换。",
        "proper 反常层是什么？它与 Radon 变换、Fourier 变换如何相容？",
        {"text": "$P(\\cV)$ 上的反常层 $L$ 称为 proper，若遗忘支撑的态射 $j_!L\\to j_*L$ 是同构；"
                 "此时 $j_!L\\cong j_*L$，且这个公共对象正是 $L$ 的中间延拓 $j_{!*}L$。判据 (0.3)：$L$ proper 当且仅当 "
                 "$(\\pi^\\circ)_!L=0$。Radon 变换定义为 $\\Rad_{P(\\cV)/\\cS}(L)=(q^\\vee)_!q^*L[r-1]$。",
         "notation": "$P(\\cV)$, $j:P(\\cV)\\hookrightarrow\\overline{\\cV}$, $\\pi^\\circ$, $\\Rad$, $\\Four$"},
        ["(0.4)：若 $L$ proper，则 $\\Four_{\\cV/\\cS}(j_!L)$ proper，且它在 $P(\\cV^\\vee)$ 上的限制等于 $\\Rad_{P(\\cV)/\\cS}(L)$。",
         "关联叠 $H\\subset P(\\cV^\\vee)\\times_\\cS P(\\cV)$ 是 Radon 变换的对应。",
         "proper 性刻画的是层的支撑不向无穷远处逃逸。"],
        ["$L$ proper $\\iff$ $(\\pi^\\circ)_!L=0$"],
        [],
        ["把 proper 误作态射的紧合性；此处是反常层的一个性质（支撑条件）。",
         "把 (0.4) 的结论方向写反：是 $\\Four$ 的限制等于 Radon 变换，而非 Radon 变换等于 $\\Four$。"],
        [ID["fourier"], ID["vanish"]],
        [src(4, "0. 预备（原文 p4）",
             "Un faisceau pervers L sur P(V) est dit propre",
             "est un isomorphisme.",
             anchor("s01-prelim.tex", "definitionZ", 0, "定义 (0.2)：proper 反常层"))],
        [e1(4, "原文第 4 页给出定义 (0.2) 与判据 (0.3)、(0.4)。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 中 (0.2)(0.3)(0.4) 的陈述与 PDF 一致。", "supports"),
         vcheck("本工程译稿 第 0 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s01-prelim.tex:L47-L65",
                "中译保留「proper」不译，并在译注中说明它不是紧合性。", "supports")]))

    # 5 ------------------------------------------------------------------
    C.append(card(
        ID["gl1"], TRACK,
        "GL(1) 情形：几何类域论与 $\\Aut_E$",
        ["Abel–Jacobi 定理", "Aut_E", "几何类域论"],
        "$G=\\GL(1)$ 的 Drinfeld–Langlands：Abel–Jacobi 定理 1.1 与定理 1.2。秩 $1$ 局部系统 $E$ "
        "在 $\\Pic^0(X)$ 上有唯一自守对应 $\\Aut_E$，且 $\\phi^*\\Aut_E=E$。",
        "GL(1) 的几何 Langlands 对应如何陈述与证明？",
        {"text": "设 $X$ 为连通射影光滑曲线，亏格 $g$，基点 $x_0$。Abel–Jacobi：$J(X)=\\C^g/\\Lambda$，"
                 "且 $\\phi:X\\to J(X)\\cong\\Pic^0(X)$，$x\\mapsto\\cO_X([x]-[x_0])$。"
                 "定理 1.2：对任意秩 $1$ 局部系统 $E$，存在唯一（在原点刚性化）的秩 $1$ 局部系统 "
                 "$\\Aut_E$ 于 $\\Pic^0(X)$，使 $\\phi^*\\Aut_E=E$，且 $m^*\\Aut_E\\cong\\Aut_E\\boxtimes\\Aut_E$。",
         "notation": "$J(X)$, $\\Pic^0(X)$, $\\phi$, $E$, $\\Aut_E$, $X^{(d)}$"},
        ["代数证明：对称积 $X^{(d)}=X^d/S_d$，$\\phi^{(d)}:X^{(d)}\\to\\Pic^0(X)$，$D\\mapsto\\cO_X(D-d[x_0])$；$d\\ge 2g-1$ 时它是射影丛，纤维单连通。",
         "$E^{(d)}=(r_*E^{\\boxtimes d})^{S_d}$，纤维公式 (1.3)：$(E^{(d)})_D=\\bigotimes_x \\Sym^{d_x}E_x$。",
         "秩 $1$ 时 $E^{(d)}$ 沿 $\\phi^{(d)}$ 的纤维常值，故下降为 $\\Pic^0(X)$ 上的 $\\Aut_E$；这正是处处非分歧的 GL(1) Drinfeld–Langlands。"],
        ["$(E^{(d)})_D=\\bigotimes_{x\\in X}\\Sym^{d_x}E_x$"],
        [{"name": "定理 1.1（Abel–Jacobi）", "kind": "定理",
          "statement": "$J(X)$ 是 $\\Pic^0(X)$ 的底层复环面；解析态射 $\\phi:X\\to J(X)\\cong\\Pic^0(X)$ 正是把 $x$ 送到 $\\cO_X([x]-[x_0])$ 的同构类的代数态射。",
          "proof": {"status": "cited", "steps": [],
                    "gap_note": ""},
          "source": anchor("s02-classfield.tex", "theorem", 0, "定理 1.1")},
         {"name": "定理 1.2（$\\Aut_E$ 的存在唯一性）", "kind": "定理",
          "statement": "秩 $1$ 局部系统 $E$ 在 $\\Pic^0(X)$ 上有唯一（原点刚性化）秩 $1$ 局部系统 $\\Aut_E$，"
                       "使 $\\phi^*\\Aut_E=E$ 且 $m^*\\Aut_E\\cong\\Aut_E\\boxtimes\\Aut_E$。",
          "proof": {"status": "sketch", "steps": [
              {"no": 1, "text": "用对称积与 Abel–Jacobi 态射 $\\phi^{(d)}$ 把问题化为沿射影丛纤维的下降。",
               "why": "$d\\ge 2g-1$ 时 $\\phi^{(d)}$ 是射影丛，纤维单连通。"},
              {"no": 2, "text": "构造 $S_d$-不变局部系统 $E^{(d)}=(r_*E^{\\boxtimes d})^{S_d}$，用 (1.3) 算纤维。",
               "why": "纤维公式给出 $E^{(d)}$ 沿 $\\phi^{(d)}$ 的常数性。"},
              {"no": 3, "text": "由单连通纤维上的下降得到 $\\Pic^0(X)$ 上的 $\\Aut_E$。",
               "why": "常值纤维的局部系统沿单连通纤维下降。"}],
              "gap_note": "卡内只记证明骨架；下降与射影丛纤维单连通性依赖 [B-L]/[L-M] 的标准事实，未在卡内展开。"},
          "source": anchor("s02-classfield.tex", "theorem", 1, "定理 1.2")}],
        ["「唯一」是在原点刚性化意义下；忘记刚性化会差一个平移。",
         "把 $\\Aut_E$ 与 $E$ 混同：$\\Aut_E$ 在 $\\Pic^0(X)$ 上，$E$ 在 $X$ 上。"],
        [ID["intro"], ID["mainthm"]],
        [src(5, "1. 几何类域论（原文 p5）",
             "Pour tout système local E de rang 1 sur X, il existe un unique",
             "AutE = E.",
             anchor("s02-classfield.tex", "theorem", 1, "定理 1.2"))],
        [e1(5, "原文第 5 页陈述定理 1.1 与定理 1.2；代数证明自第 6 页（p6）起。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 的定理 1.2 与 (1.3) 与 PDF 一致。", "supports"),
         vcheck("底本 TeX 源码中的 (1.3)", TEX,
                "源码含纤维公式 (1.3) 的完整排版，与 PDF 第 6 页公式一致。", "supports"),
         vcheck("本工程译稿 第 1 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s02-classfield.tex:L29-L82",
                "中译保留定理 1.1/1.2 的层级与原编号，(1.3) 逐字保留。", "supports")]))

    # 6 ------------------------------------------------------------------
    C.append(card(
        ID["hecke"], TRACK,
        "Hecke 叠、Hecke 算子与 Hecke 性质",
        ["Hecke 算子", "Hecke 叠", "Hecke 特征层", "Hecke eigensheaf"],
        "Hecke 对应 $\\Hck_n(X)\\to X\\times\\Fib_n(X)$ 给出算子 $H(K)=(q,p')_*p^*K[n-1]$；"
        "定义 2.1 用 $H(K)\\cong E\\boxtimes K$ 及 $H\\circ H$ 的 $S_2$-等变性定义 Hecke 性质。",
        "Hecke 算子如何定义？「相对 E 有 Hecke 性质」是什么意思？",
        {"text": "Hecke 叠 $\\Hck_n(X)$ 参数化三元组 $(x,\\cL,\\cL'\\subset\\cL)$，其中 $\\cL'$ 是 $\\cL$ 在 $x$ 处的"
                 "初等下修改（$\\cL/\\cL'$ 为集中于 $x$ 的长度 $1$ 摩天层，$\\deg\\cL'=\\deg\\cL-1$）。"
                 "投影 $(q,p'):\\Hck_n\\to X\\times\\Fib_n$ 与 $p:\\Hck_n\\to\\Fib_n$ 可表、射影、光滑，"
                 "相对维数分别为 $n-1$ 与 $n$。",
         "notation": "$\\Hck_n(X)$, $H(K)$, $S_2$-等变, $\\Fib_n^d(X)$"},
        ["$H(K)=(q,p')_*p^*K[n-1]\\in\\Dbc(X\\times\\Fib_n(X))$。",
         "$H\\circ H$ 在 $(X\\times X-\\Delta_X)\\times\\Fib_n(X)$ 上是 $S_2$-等变的（$S_2$ 交换两个 $X$ 因子）。",
         "定义 2.1 要求 $E$ 是秩 $n$ 的不可约局部系统、$K$ 是不可约反常层；Hecke 性质由 $H(K)\\cong E\\boxtimes K$ 与 $H\\circ H$ 的 $S_2$-等变性共同刻画。"],
        ["$H(K)=(q,p')_*p^*K[n-1]$"],
        [],
        ["把 Hecke 性质写成 $H(K)\\cong K\\boxtimes E$：$E$ 在 $X$ 因子上，$K$ 在 $\\Fib_n$ 因子上，次序不可换。",
         "忽略 $n-1$ 的平移；它是相对维数 $n-1$ 的 Poincaré–Verdier 对偶带来的。"],
        [ID["mainthm"], ID["vanish"]],
        [src(7, "2. 主定理（原文 p7）",
             "Le champ de Hecke est le champ modulaire Hecken (X) des triplets",
             "(x, L, L′ ⊂ L)",
             line_anchor("s03-main.tex", "Hecke 叠是三元组"))],
        [e1(7, "原文第 7 页给出 Hecke 叠、投影的相对维数与算子 $H(K)$ 的定义。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 的 Hecke 算子公式与 $[n-1]$ 平移与 PDF 一致。", "supports"),
         vcheck("FGV, arXiv:math/0012255v3 第 4 页", FGV + "#page=4",
                "FGV §1.1 的 Hecke 特征层定义 (1.3) 为 $H^1_n(K)\\simeq E\\boxtimes K$，与本卡方向一致。", "supports"),
         vcheck("本工程译稿 第 2 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s03-main.tex:L16-L40",
                "中译保留初等下修改与两个投影的相对维数。", "supports")]))

    # 7 ------------------------------------------------------------------
    C.append(card(
        ID["mainthm"], TRACK,
        "主定理（FGV）：$\\Aut_E$ 的存在性",
        ["定理 2.2", "Frenkel–Gaitsgory–Vilonen", "Hecke 特征反常层"],
        "定理 2.2：任意秩 $n$ 不可约局部系统 $E$ 都有 $\\Fib_n(X)$ 上的反常层 $\\Aut_E$，"
        "在各连通分支上不可约，且相对 $E$ 有 Hecke 性质。证明分「构造 $\\Aut'_E$」与「下降」两步。",
        "FGV 的主定理陈述什么？证明的两个步骤各是什么？",
        {"text": "定理 2.2（$n=2$ 为 Drinfeld [Dr 2]；一般情形为 FGV [F-G-V 2] 与 [Ga]）："
                 "对任意 $X$ 上秩 $n$ 的不可约局部系统 $E$，存在 $\\Fib_n(X)$ 上的反常层 $\\Aut_E$，"
                 "使其在每个连通分支 $\\Fib_n^d(X)$ 上的限制不可约，且相对 $E$ 有 Hecke 性质。",
         "notation": "$\\Fib_n(X)$, $\\Fib_n^d(X)$, $\\Aut_E$, $\\Fib'_n(X)$"},
        ["第一步：在 $\\Fib'_n(X)$（$(\\cL,s)$，$s:(\\Omega^1_X)^{\\otimes(n-1)}\\hookrightarrow\\cL$，模数乘）上构造 $\\Aut'_E$。",
         "灵感来自 $\\GL(n)$ 尖点自守形式的 Fourier 展开与 Shintani 公式（Grothendieck 函数–层字典），但不是简单移植。",
         "第二步：在大开集上证明 $\\Aut'_E$ 是反常层，并沿遗忘 $s$ 的态射 $\\Fib'_n\\to\\Fib_n$ 下降；难点在这一步。",
         "核对 FGV 原文可见：其主陈述是猜想（Conjecture 1.3），消没部分由 Gaitsgory 的定理补足。"],
        [],
        [{"name": "定理 2.2", "kind": "定理",
          "statement": "对任意秩 $n$ 不可约局部系统 $E$，存在 $\\Fib_n(X)$ 上反常层 $\\Aut_E$，"
                       "在每个连通分支上不可约，且相对 $E$ 有 Hecke 性质。",
          "proof": {"status": "cited", "steps": [],
                    "gap_note": ""},
          "source": anchor("s03-main.tex", "theorem", 0, "定理 2.2")}],
        ["把 Laumon 的「定理 2.2」直接当成 FGV 论文中的定理：FGV 原文陈述为猜想 1.3，"
         "其消没部分由 Gaitsgory（arXiv:math/0204081）证明；Laumon 报告把两者合并陈述为定理。",
         "忽略「在每个连通分支上不可约」这一条，只记住 Hecke 性质。"],
        [ID["intro"], ID["hecke"], ID["autp"], ID["descent"]],
        [src(8, "2. 主定理（原文 p8）",
             "Pour tout système local irréductible E de rang n sur X, il existe",
             "qui a la propriété de Hecke relativement à E.",
             anchor("s03-main.tex", "theorem", 0, "定理 2.2"))],
        [e1(8, "原文第 8 页陈述定理 2.2，并说明证明分两步、难点在第二步。"),
         vcheck("FGV, arXiv:math/0012255v3 第 4 页", FGV + "#page=4",
                "FGV 的主陈述编为 Conjecture 1.3（非定理），内容与本卡定理 2.2 相同。", "partial"),
         vcheck("Gaitsgory, arXiv:math/0204081v2 第 5 页", GAI + "#page=5",
                "Gaitsgory 的 Conjecture 1.3（消没）即 Laumon 定理 6.1 的来源；两者合起来才给出定理 2.2。", "partial"),
         vcheck("本工程译稿 第 2 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s03-main.tex:L61-L75",
                "中译保留「在每个连通分支上不可约」与 Hecke 性质两项结论。", "supports")]))

    # 8 ------------------------------------------------------------------
    C.append(card(
        ID["ldE"], TRACK,
        "反常层 $\\sL^d_E$ 与中间延拓",
        ["L^d_E", "中间延拓", "Coh^d_0(X)"],
        "在秩 $0$ 长 $d$ 凝聚层叠 $\\Coh^d_0(X)$ 上，由 $\\sL^d_{E,rss}=\\det^*E^{(d)}$ 出发作中间延拓，"
        "得到 $\\sL^d_E$；引理 3.1 说明 $E^{(d)}[d]$ 也是同一类中间延拓。",
        "$\\sL^d_E$ 如何定义？为什么必须用中间延拓而不是零延拓？",
        {"text": "$\\Coh^d_0(X)$ 是 $X$ 上秩 $0$（有限支撑）长 $d$ 凝聚层的叠。"
                 "$\\sL^d_{E,rss}=\\det^*E^{(d)}|\\Coh^d_{0,rss}(X)$ 是稠密开集上的秩 $n^d$ 局部系统。"
                 "定义 3.2：$\\sL^d_E$ 是 $\\sL^d_{E,rss}$ 到整个 $\\Coh^d_0(X)$ 的中间延拓。",
         "notation": "$\\Coh^d_0(X)$, $\\Coh^d_{0,rss}$, $\\det$, $E^{(d)}$, $\\sL^d_E$"},
        ["$\\Coh^d_0(\\A^1)=[\\mathfrak{gl}(d)/\\GL(d)]$；光滑曲线 étale 局部同构于 $\\A^1$，故一般情形 étale 局部如此。",
         "$X^{(d)}\\to\\Coh^d_0$，$D\\mapsto\\cO_{X,D}=\\cO_X/\\cO_X(-D)$，光滑、相对维 $d$。",
         "引理 3.1：$E^{(d)}[d]$（把 $E^{(d)}$ 放在次数 $-d$）是反常层，且是到 $X^{(d)}_{rss}$ 限制的中间延拓；$E$ 不可约（半单）则同。"],
        ["$\\sL^d_{E,rss}=\\det{}^*E^{(d)}|\\Coh^d_{0,rss}(X)$",
         "$X^{(d)}\\to\\Coh^d_0(X),\\ D\\mapsto\\cO_X/\\cO_X(-D)$"],
        [{"name": "引理 3.1", "kind": "引理",
          "statement": "$E^{(d)}[d]$ 是反常层，且为到 $X^{(d)}_{rss}$ 的限制的中间延拓；$E$ 不可约（半单）时同。",
          "proof": {"status": "cited", "steps": [], "gap_note": ""},
          "source": anchor("s04-perverse.tex", "lemma", 0, "引理 3.1")}],
        ["把 $E^{(d)}[d]$ 理解为把 $E^{(d)}$ 放在次数 $+d$；原文放在 $-d$。",
         "把 $\\sL^d_E$ 写成零延拓 $j_!$；那样会丢掉 $\\Coh^d_0\\setminus\\Coh^d_{0,rss}$ 上的支撑信息。"],
        [ID["autp"], ID["vanish"]],
        [src(9, "3. 反常层 $\\sL^d_E$（原文 p9）",
             "Pour chaque entier d ≥ 0, le faisceau pervers LdE",
             "à Cohd0 (X) tout entier.",
             anchor("s04-perverse.tex", "definition", 0, "定义 3.2"))],
        [e1(9, "原文第 9 页给出引理 3.1 与定义 3.2，并说明 $E^{(d)}[d]$ 的平移方向。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 中 $-d$ 的平移与中间延拓的措辞与 PDF 一致。", "supports"),
         vcheck("本工程译稿 第 3 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s04-perverse.tex:L30-L55",
                "中译保留「放在次数 $-d$」与中间延拓。", "supports")]))

    # 9 ------------------------------------------------------------------
    C.append(card(
        ID["autp"], TRACK,
        "复形 $\\Aut'_E$ 的定义",
        ["Aut'_E", "Fib'_n(X)", "M'^d_{n,E}"],
        "在 $\\Fib'_n(X)$（带 $s:(\\Omega^1_X)^{\\otimes(n-1)}\\hookrightarrow\\cL$ 的向量丛）上，"
        "定义 4.1 用函子 $M'^d_{n,E}$ 逐分支定义复形 $\\Aut'_E$，它是定理 2.2 证明第一阶段的产物。",
        "$\\Aut'_E$ 如何定义？为什么先要在 $\\Fib'_n(X)$ 上构造它？",
        {"text": "$\\Fib'_n(X)$ 参数化 $(\\cL,s)$，$s:(\\Omega^1_X)^{\\otimes(n-1)}\\to\\cL$ 模数乘。"
                 "定义 4.1：$\\Aut'_E$ 在分支 $\\Fib'^{\\,n(n-1)(g-1)+d}_n(X)$ 上为 $M'^d_{n,E}(L_n)$（$d\\ge 0$），"
                 "在 $d<0$ 时为 $0$。其中 $L_n=(\\bar f_n)_!(\\bar g_n)^*\\Psi[\\dim\\bar\\cU_n]$。",
         "notation": "$\\Fib'_n(X)$, $\\cU_n$, $\\overline{\\cU}_n$, $L_n$, $M'^d_{n,E}$"},
        ["$\\cU_n$ 参数化完全旗 $(\\cL,\\cL_\\bullet,s_\\bullet)$；$f_n:\\cU_n\\to\\Fib'_n$，$g_n:\\cU_n\\to\\A^1$ 取各扩张类之和。",
         "$\\Gm$ 作用 $t\\cdot(\\cL,\\cL_\\bullet,s_\\bullet)=(\\cL,\\cL_\\bullet,t\\cdot s_\\bullet)$，$t\\cdot s_\\bullet=(t^{n-j}s_j)$；取商得 $\\overline{\\cU}_n=\\cU_n/\\Gm$。",
         "$M'^d_{n,E}(K)=p_*p'{}^*(K\\otimes q^*\\sL^d_E)[nd]$。",
         "本节起恒设 $g\\ge 2$（$g=0,1$ 无秩 $\\ge 2$ 的不可约局部系统）。"],
        ["$L_n=(\\bar f_n)_!(\\bar g_n)^*\\Psi[\\dim\\bar\\cU_n]$",
         "$M'^d_{n,E}(K)=p_*p'{}^*(K\\otimes q^*\\sL^d_E)[nd]$"],
        [{"name": "定义 4.1", "kind": "定义",
          "statement": "$\\Aut'_E$ 在 $\\Fib'^{\\,n(n-1)(g-1)+d}_n(X)$ 上为 $M'^d_{n,E}(L_n)$（$d\\ge0$），$d<0$ 为 $0$。",
          "proof": {"status": "none", "steps": [], "gap_note": ""},
          "source": anchor("s05-autprime.tex", "definition", 0, "定义 4.1")}],
        ["混淆 $\\cU_n=Y^{0\\circ}_n/\\Gm$ 与 $\\overline{\\cU}_n=Y^{0\\circ}_n/\\Gm^2$：两者相差一个 $\\Gm$。",
         "把 $L_n$（复形）与 $\\sL$（向量丛）混同；原文用花体与斜体区分。"],
        [ID["mainthm"], ID["diag"]],
        [src(11, "4. 复形 $\\Aut'_E$（原文 p11）",
             "Si E est un système local sur X, on définit le complexe Aut′E",
             "si d < 0.",
             anchor("s05-autprime.tex", "definition", 0, "定义 4.1"))],
        [e1(11, "原文第 11 页给出定义 4.1 与 $M'^d_{n,E}$ 的公式。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 的定义 4.1 与 PDF 一致，含 $d<0$ 时为 $0$ 的分支。", "supports"),
         vcheck("本工程译稿 第 4 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s05-autprime.tex:L96-L110",
                "中译区分 $\\cU_n$ 与 $\\overline{\\cU}_n$，并保留 $[nd]$。", "supports")]))

    # 10 -----------------------------------------------------------------
    C.append(card(
        ID["unstable"], TRACK,
        "非常不稳定的向量丛（引理 5.1）",
        ["非常不稳定", "très instable", "引理 5.1"],
        "引理 5.1：当次数足够大且 $\\Hom(\\cL,(\\Omega^1_X)^{\\otimes n+1})\\neq 0$ 时，$\\cL$ 有非平凡直和分解 "
        "$\\cL=\\cL_1\\oplus\\cL_2$ 使 $\\Ext^1(\\cL_1,\\cL_2)=0$。它保证 $\\cC_i$ 上的 Serre 对偶消没。",
        "引理 5.1 说的「非常不稳定」是什么意思？它在构造中起什么作用？",
        {"text": "$\\cL$ 称非常不稳定，若存在非平凡的直和分解 $\\cL=\\cL_1\\oplus\\cL_2$ 使 "
                 "$\\Ext^1_{\\cO_X}(\\cL_1,\\cL_2)=0$。引理 5.1：存在常数 $c(g,n)$，使对任意 $d\\ge c(g,n)$ 与任意 "
                 "$\\cL\\in\\Fib^d_n(X)$，只要 $\\Hom_{\\cO_X}(\\cL,(\\Omega^1_X)^{\\otimes n+1})\\neq(0)$，$\\cL$ 就非常不稳定。",
         "notation": "$c(g,n)$, $\\cC_i$, $\\Ext^1$, $\\Hom$"},
        ["作用：在 $\\cC_i$ 上同时消没 $\\Hom(\\cM_i,(\\Omega^1)^{\\otimes i})$ 与 $\\Ext^1((\\Omega^1)^{\\otimes i-1},\\cM_i)$，"
         "从而 $\\cV_i$ 与 $\\cV_i^\\vee$ 成为对偶向量丛，Fourier 变换可用。",
         "$\\cC_i$ 是次数 $\\ge c(n,g)+i(i-1)(g-1)$ 且 $\\Hom(\\cM_i,(\\Omega^1)^{\\otimes n+1})=0$ 的开集。",
         "常数 $c(g,n)$ 只保证「次数足够大」，其具体值不出现在本篇的任何计算中。"],
        ["$\\cL=\\cL_1\\oplus\\cL_2,\\quad \\Ext^1_{\\cO_X}(\\cL_1,\\cL_2)=0$"],
        [{"name": "引理 5.1", "kind": "引理",
          "statement": "存在 $c(g,n)$：$d\\ge c(g,n)$ 且 $\\Hom(\\cL,(\\Omega^1)^{\\otimes n+1})\\neq 0$ 时 $\\cL$ 非常不稳定。",
          "proof": {"status": "cited", "steps": [], "gap_note": ""},
          "source": anchor("s06-fourier.tex", "lemma", 0, "引理 5.1")}],
        ["把「非常不稳定」当成通常斜率稳定性的否定；它是存在直和分解使 $\\Ext^1$ 消没，比不稳定的含义更强、更具体。",
         "忽略常数在原文中一处作 $c(g,n)$、另一处作 $c(n,g)$；这是原文的不一致，照录不改。"],
        [ID["diag"], ID["fourier"]],
        [src(12, "5. 用 Fourier 变换构造（原文 p12）",
             "Il existe une constante c(g, n) qui a la propriété suivante",
             "pour laquelle Ext1OX (L1 , L2 ) = (0).",
             anchor("s06-fourier.tex", "lemma", 0, "引理 5.1"))],
        [e1(12, "原文第 12 页陈述引理 5.1，并随即用它定义 $\\cC_i$。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 第 1676 行作 $c(g,n)$、第 1689 行作 $c(n,g)$，两处不一致为原文所有。", "supports"),
         vcheck("本工程译稿 第 5 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s06-fourier.tex:L10-L30",
                "中译照录两处常数写法，未擅自统一。", "supports")]))

    # 11 -----------------------------------------------------------------
    C.append(card(
        ID["diag"], TRACK,
        "基本图与引理 5.2",
        ["基本图", "diagramme fondamental", "K_{E,i}", "引理 5.2"],
        "对 $i=0,\\dots,n$ 的向量丛 $\\cV_i,\\cV_i^\\vee$ 与开集 $\\cV_i^\\circ,\\cV_i^{\\vee\\circ}$ 经 $\\Gm$ 取商后构成基本图，"
        "并用 Fourier 变换递推定义 $K_{E,i}\\in\\Dbc(\\bar\\cV_i^\\circ)$；引理 5.2 把它与 $M'^d_{i,E}(L_i)$ 对齐。",
        "基本图由哪些对象组成？$K_{E,i}$ 如何递推定义？引理 5.2 给出什么？",
        {"text": "$\\cV_i$ 参数化 $(\\cM_i,s_i)$，$\\cV_i^\\vee$ 参数化扩张 $0\\to(\\Omega^1_X)^{\\otimes i}\\to\\cM_{i+1}\\to\\cM_i\\to0$；"
                 "$\\pi_i,\\pi_i^\\vee$ 为对偶向量丛；开集 $\\cV_i^\\circ=\\{s_i$ 单射$\\}$，"
                 "$\\cV_i^{\\vee\\circ}=\\{\\cM_{i+1}\\in\\cC_{i+1}\\}$，并有典范同构 $\\cV_i^{\\vee\\circ}\\cong\\cV_{i+1}^\\circ$。对 $\\Gm$ 取商得 $\\bar\\cV_i=[\\cV_i/\\Gm]$，$K_{E,i}\\in\\Dbc(\\bar\\cV_i^\\circ)$。",
         "notation": "$\\cV_i$, $\\cV_i^\\vee$, $\\cV_i^\\circ$, $\\cV_i^{\\vee\\circ}$, $K_{E,i}$"},
        ["$K_{E,i}\\in\\Dbc(\\bar\\cV_i^\\circ)$；$K_{E,1}=(\\iota_0)_*(\\bar\\pi^{\\vee\\circ}_0)^*L_E$，其中 $L_E$ 在 $\\cC^d_0$ 上是 $\\sL^d_E$ 平移 $d-1$。",
         "$K_{E,i+1}=(\\iota_i)_*(j_i^\\vee)^*\\Four_{\\bar\\cV_i/\\cC_i}\\bigl((j_i)_!K_{E,i}\\bigr)$，$i=1,\\dots,n-1$。",
         "引理 5.2：$K_{E,i}$ 在 $\\bar\\cV_i^\\circ\\cap\\Fib'^{\\,i(i-1)(g-1)+d}_i(X)$ 上的限制等于 $M'^d_{i,E}(L_i)$；特别 $K_{E,n}$ 与 $\\Aut'_E$ 在该开集上一致。"],
        ["$K_{E,i+1}=(\\iota_i)_*(j_i^\\vee)^*\\Four_{\\bar\\cV_i/\\cC_i}\\bigl((j_i)_!K_{E,i}\\bigr)$"],
        [{"name": "引理 5.2", "kind": "引理",
          "statement": "对每个 $i=1,\\dots,n$ 与每个整数 $d\\ge0$，$K_{E,i}$ 在 $\\bar\\cV_i^\\circ\\cap\\Fib'^{\\,i(i-1)(g-1)+d}_i$ 上的限制为 $M'^d_{i,E}(L_i)$。",
          "proof": {"status": "cited", "steps": [], "gap_note": ""},
          "source": anchor("s06-fourier.tex", "lemma", 1, "引理 5.2")}],
        ["把图中的斜箭头（投影 $\\pi_i,\\pi^\\vee_i$）与水平箭头（开浸入 $j_i,j_i^\\vee$ 与同构 $\\iota_i$）混为一谈。",
         "把 $L_E$ 直接当成 $\\sL^d_E$；它其实是 $\\sL^d_E$ 平移 $d-1$。"],
        [ID["autp"], ID["vanish"], ID["unstable"]],
        [src(13, "5. 用 Fourier 变换构造（原文 p13）",
             "Pour tout système local E de rang n sur X on définit alors les complexes",
             "définie dans la section 0.",
             "08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s06-fourier.tex:L105-L117（$K_{E,i}$ 的定义，引文止于引理 5.2 前）")],
        [e1(13, "原文第 13 页给出 $K_{E,1}$ 与递推式，并陈述引理 5.2。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 中递推式的下标与 $[d-1]$ 平移与 PDF 一致。", "supports"),
         vcheck("本工程译稿 第 5 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s06-fourier.tex:L80-L125",
                "中译的基本图为 tikz-cd 重画，箭头方向已逐条对照底本。", "supports")]))

    # 12 -----------------------------------------------------------------
    C.append(card(
        ID["vanish"], TRACK,
        "消没定理（定理 6.1）",
        ["消没定理", "théorème d'annulation", "Gaitsgory", "M^d_{i,E}"],
        "定理 6.1（Gaitsgory）：$E$ 秩 $n$ 不可约时，对 $i=1,\\dots,n-1$ 与 $d>in(2g-2)$，"
        "函子 $M^d_{i,E}$ 恒为零。它是定理 2.2 证明的核心输入；命题 6.3 与推论 6.4 是其推论。",
        "消没定理的条件与结论是什么？它如何推出 $\\Aut'_E$ 的 proper 性与不可约性？",
        {"text": "$M^d_{i,E}(K)=p_*p'{}^*(K\\otimes q^*\\sL^d_E)[id]$，定义在 $\\Mod^d_i(X)$（$(\\cL,\\cL'\\subset\\cL)$，"
                 "$\\cL'$ 为下修改、余长 $d$）的对应上。定理 6.1：$E$ 为秩 $n$ 不可约局部系统，则对 $i=1,\\dots,n-1$ "
                 "与任意整数 $d>in(2g-2)$，$M^d_{i,E}$ 恒为零。",
         "notation": "$M^d_{i,E}$, $\\Mod^d_i(X)$, $\\sL^d_E$, $in(2g-2)$"},
        ["注 6.2：证明长且技术性强，超出报告范围；$i=1$ 时即 Deligne 结果（cf. [Dr 2]）的改写。",
         "命题 6.3：$(j_i)_!K_{E,i}\\to(j_i)_*K_{E,i}$ 是同构；证明化归 $(\\overline\\pi^\\circ_i)_!K_{E,i}=0$，由引理 5.2 逐分支等于 $M^d_{i,E}(\\pi'_*L_i)$，再用定理 6.1。",
         "推论 6.4：$K_{E,n}$ 在 $\\overline{\\cV}^\\circ_n$ 的各连通分支上不可约。"],
        ["$M^d_{i,E}(K)=p_*p'{}^*(K\\otimes q^*\\sL^d_E)[id]$"],
        [{"name": "定理 6.1", "kind": "定理",
          "statement": "$E$ 秩 $n$ 不可约，$i=1,\\dots,n-1$，$d>in(2g-2)$ $\\Rightarrow$ $M^d_{i,E}=0$。",
          "proof": {"status": "cited", "steps": [], "gap_note": ""},
          "source": anchor("s07-vanishing.tex", "theorem", 0, "定理 6.1")}],
        ["把条件 $d>in(2g-2)$ 中的 $in$ 当成排版错误改为 $n(2g-2)$；注 6.2 确实用 $n(2g-2)$，但定理陈述是逐 $i$ 的 $i\\,n$，照录不改。",
         "把定理 6.1 当成已完全证明：原文明说证明超出报告范围，只给出 $i=1$ 的 Deligne 特例说明。"],
        [ID["autp"], ID["descent"], ID["proper"]],
        [src(14, "6. 消没定理（原文 p14）",
             "Soit E un système local irréductible de rang n.",
             "identiquement nul.",
             anchor("s07-vanishing.tex", "theorem", 0, "定理 6.1"),
             qt=qj(14, "Soit E un système local irréductible de rang n.",
                   "Alors, pour tout i = 1, . . . , n − 1 et tout entier d > in(2g − 2), le foncteur Mi,E",
                   "identiquement nul."))],
        [e1(14, "原文第 14 页陈述定理 6.1，条件逐字为 $d>in(2g-2)$。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 第 1872 行逐字作 `$d>in(2g-2)$`，证明该写法为原文所有。", "supports"),
         vcheck("Gaitsgory, arXiv:math/0204081v2 第 5 页", GAI + "#page=5",
                "Gaitsgory 的消没陈述条件为 $d>(2g-2)\\,n\\,\\mathrm{rk}(E)$，与定理 6.1（$i=n$ 时 $in(2g-2)$）相容。", "partial"),
         vcheck("本工程译稿 第 6 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s07-vanishing.tex:L21-L30",
                "中译照录 $in(2g-2)$ 并加译注说明 $i\\,n$ 是乘积。", "supports")]))

    # 13 -----------------------------------------------------------------
    C.append(card(
        ID["descent"], TRACK,
        "下降：由 $\\Aut'_E$ 得到 $\\Aut_E$",
        ["下降", "Euler–Poincaré 示性函数", "命题 7.3", "引理 7.4"],
        "§7 用 Euler–Poincaré 示性函数 $\\chi$ 完成下降：引理 7.1（Deligne）说明 $\\chi$ 在紧合前推下不变，"
        "命题 7.3 给出可表紧合态射 $\\tilde f$，引理 7.4 把 $\\Aut'_E$ 写成 $\\tilde f_*N^d_{n,E}(\\Phi)$，"
        "从而 $\\chi_{\\Aut'_E}$ 不依赖 $E$，再由引理 7.2 得 $\\Aut_E$。",
        "如何从 $\\Fib'_n(X)$ 上的 $\\Aut'_E$ 下降到 $\\Fib_n(X)$ 上的 $\\Aut_E$？",
        {"text": "对 $K\\in\\Dbc$，$\\chi_K(s)=\\sum_i(-1)^i\\dim_\\C H^i(K_s)$。引理 7.1（Deligne, [Il] 推论 2.10）："
                 "$f:Y\\to Z$ 紧合，$K,K'$ 局部同构，则 $\\chi_{f_*K}=\\chi_{f_*K'}$。"
                 "引理 7.2：$\\pi:P(\\cV)\\to\\cS$ 为射影丛、$K$ 不可约反常层，则 存在 $S$ 上的（必然不可约）反常层 $L$，使 $K\\cong\\pi^*(L)[r-1]$，当且仅当 "
                 "$\\chi_K$ 沿 $\\pi$ 的纤维常值。",
         "notation": "$\\chi_K$, $\\tilde f:\\widetilde Y^d_n\\to\\Fib'^{\\,n(n-1)(g-1)+d}_n$, $N^d_{n,E}$, $\\Phi$"},
        ["命题 7.3（[B-G] 命题 1.2.2 的同类技术事实）：$\\tilde f:\\widetilde Y^d_n=[Y^d_n/\\Gm^n]\\to\\Fib'^{\\,n(n-1)(g-1)+d}_n$ 可表且紧合。",
         "引理 7.4：$\\Aut'_E$ 在 $\\Fib'^{\\,n(n-1)(g-1)+d}_n$ 上的限制等于 $\\tilde f_*N^d_{n,E}(\\Phi)$。",
         "末段：由 7.1、7.3 与 7.4，$\\chi_{\\Aut'_E}$ 不依赖 $E$；对平凡 $E$ 算出 $\\chi$，再用 7.2 得 $\\Aut_E$，从而完成定理 2.2 的证明。"],
        ["$\\chi_K(s)=\\sum_i(-1)^i\\dim_\\C H^i(K_s)$"],
        [{"name": "引理 7.1（Deligne）", "kind": "引理",
          "statement": "设 $f:Y\\to Z$ 为概形（或代数叠的可表）紧合态射，$K,K'\\in\\Dbc(Y)$ 在 $Y$ 上局部同构，则 $\\chi_{f_*K}=\\chi_{f_*K'}$。",
          "proof": {"status": "cited", "steps": [], "gap_note": ""},
          "source": anchor("s08-descente.tex", "lemma", 0, "引理 7.1")},
         {"name": "引理 7.2", "kind": "引理",
          "statement": "存在 $S$ 上的（必然不可约）反常层 $L$，使 $K\\cong\\pi^*(L)[r-1]$，当且仅当 $\\chi_K$ 沿 $\\pi$ 的纤维常值。",
          "proof": {"status": "sketch", "steps": [
              {"no": 1, "text": "用反常层的结构定理写 $K\\cong i_*j_{!*}E[\\dim Q]$。",
               "why": "不可约反常层由其支撑 $Q$ 与开集上的局部系统决定。"},
              {"no": 2, "text": "由 $\\chi_K$ 沿纤维常值证明 $Q=\\pi^{-1}(T)$，再取 $Q^\\circ=\\pi^{-1}(T^\\circ)$。",
               "why": "纤维上的常值性迫使支撑是 $\\pi$ 的饱和集。"},
              {"no": 3, "text": "$E$ 来自 $T^\\circ$ 上的局部系统 $F$（纤维单连通），取 $L=F[\\dim T]$ 的中间延拓再零延拓。",
               "why": "单连通纤维上局部系统必为常值。"}],
              "gap_note": "卡内只记三步骨架；结构定理与 $\\pi$ 的饱和性细节见原文与 [B-L]。"},
          "source": anchor("s08-descente.tex", "lemma", 1, "引理 7.2")}],
        ["把命题 7.3 说成「就是 [B-G] 命题 1.2.2」；BG 的命题讲的是 $\\Bun_B\\to\\Bun_G$ 的可表紧合性，"
         "对象与目标都不同，只能说同类技术事实。",
         "忽略 $\\Phi$ 是把 $(\\overline g_n)^*\\Psi$ 沿 $[Y^{0\\circ}_n/\\Gm^2]\\to[Y^{0\\circ}_n/\\Gm^n]$ 作紧支撑前推得到的。"],
        [ID["mainthm"], ID["vanish"], ID["diag"]],
        [src(15, "7. 下降（原文 p15）",
             "Soit S un schéma, voire un champ algébrique, soit V → S un fibré",
             "constante le long des fibres de π.",
             anchor("s08-descente.tex", "lemma", 1, "引理 7.2"))],
        [e1(15, "原文第 15 页陈述引理 7.1、7.2 及它们的证明。"),
         vcheck("底本 TeX 源码（arXiv e-print）", TEX,
                "Bourbaki2002.tex 中引理 7.1 归引 [Il] 推论 2.10，与 PDF 一致。", "supports"),
         vcheck("Braverman–Gaitsgory, arXiv:math/9912097v2 第 12 页", BG + "#page=12",
                "BG 命题 1.2.2 讲 $\\Bun_B\\to\\Bun_G$ 可表紧合，与命题 7.3 同类但对象不同。", "partial"),
         vcheck("本工程译稿 第 7 节", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s08-descente.tex:L13-L40",
                "中译保留引理 7.1 的 [Il] 出处与 7.2 的「当且仅当」。", "supports")]))

    # 14 correction ------------------------------------------------------
    C.append({
        "id": "sy0246/correction/b-l-year",
        "type": "correction",
        "track": TRACK,
        "title": "参考文献 [B-L] 的出版年：1974 应为 1994",
        "aliases": ["[B-L] 年份勘误", "Bernstein–Lunts LNM 1578"],
        "summary": "原文参考文献 [B-L] 把 LNM 1578 的出版年写成 1974；该书实为 1994 年出版。译文照录原文，此处登记勘误。",
        "question": "[B-L]（Bernstein–Lunts, Equivariant Sheaves and Functors）的出版年是 1974 还是 1994？",
        "location": "参考文献 [B-L]（原文 p18，译文 s09-refs.tex）",
        "original": "J. BERNSTEIN, V. LUNTS – Equivariant Sheaves and Functors, Lecture Notes in Mathematics 1578, Springer-verlag (1974).",
        "corrected": "J. Bernstein, V. Lunts – Equivariant Sheaves and Functors, Lecture Notes in Mathematics 1578, Springer-Verlag (1994).",
        "why": "LNM 1578 的出版年为 1994：Springer 官方页与 DOI 10.1007/BFb0073549 均记 1994，zbMATH 605663 同。原文的 1974 应为笔误。",
        "note": "按本工程体例，译文照录原文「(1974)」，不改动参考文献；勘误只登记在本卡与《04-术语文献勘误》。",
        "provenance_note": "法文引文由 make_cards.py 从底本 p18 文本层逐字截取；出版年以 Springer DOI 页与 zbMATH 记录为准。",
        "related": [ID["betti"], ID["mainthm"]],
        "sources": [src(18, "参考文献（原文 p18）",
                       "J. BERNSTEIN, V. LUNTS – Equivariant Sheaves and Functors",
                       "Springer-verlag (1974).",
                       "08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s09-refs.tex:L11-L12（参考文献 [B-L]）")],
        "rights": "rewritten",
        "status": "reviewed",
        "verification": {"status": "checked", "checked_on": m.CHECKED, "checks": [
            e1(18, "原文第 18 页 [B-L] 条目末尾作「Springer-verlag (1974)」。"),
            vcheck("Springer, LNM 1578", "https://doi.org/10.1007/BFb0073549",
                   "DOI 页记该书出版年为 1994。", "contradicts"),
            vcheck("zbMATH Open 605663", "https://zbmath.org/?q=an%3A605663",
                   "zbMATH 记录 Bernstein–Lunts, LNM 1578, 1994。", "contradicts"),
            vcheck("本工程译稿 参考文献", "repo:08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/源码/sections/s09-refs.tex:L11-L12",
                   "译文照录 (1974)，未擅自改动。", "supports")]},
    })

    return C
