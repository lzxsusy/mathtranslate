# -*- coding: utf-8 -*-
"""Raskin 讲义资料卡：第一组（GL_1、尖点、系数、Fourier、PGL_2）。"""

SRC = "Sam Raskin 讲授、Lin Chen 笔记《Notes for \"Geometric Langlands for Projective Curves\"》（2025-07-07/11，18 页）"

CARDS = []

CARDS.append({
    "id": "raskin_glc/concept/deligne-gl1-construction",
    "type": "concept",
    "track": "A",
    "title": "Deligne 的 $\\mathbb{G}_m$ 几何类域论构造",
    "aliases": ["Deligne's construction", "Construction 1.2.4", "GL_1 几何类域论"],
    "summary": "给秩 $1$ 局部系统 $\\sigma$，先在 $\\operatorname{Sym}^d X$ 上造 $\\sigma^{(d)}$，再沿 Abel–Jacobi 映射的单连通纤维下降，得到 $\\operatorname{Bun}_{\\mathbb{G}_m}$ 上满足 Hecke 性质的 lisse 层 $\\chi_\\sigma$。",
    "question": "为什么只在 $L=\\mathcal{O}(D)$ 上规定 Hecke 性质就足以确定整个 $\\operatorname{Bun}_{\\mathbb{G}_m}$ 上的层，以及为什么必须取 $d>2g-2$？",
    "definition": {
        "text": "设 $X/k$ 为光滑射影曲线，$g=g(X)$，$\\sigma$ 为 $X$ 上秩 $1$ 局部系统。对 $d\\ge 0$，令 $\\mathrm{add}_d:X^d\\to\\operatorname{Sym}^d X$ 为商映射，定义 $\\operatorname{Sym}^d X$ 上的秩 $1$ 局部系统 $\\sigma^{(d)}:=(\\mathrm{add}_{d,*}\\sigma^{\\boxtimes d})^{S_d}$。对 $d>2g-2$，Abel–Jacobi 映射 $\\mathrm{AJ}_d:\\operatorname{Sym}^d X\\to\\operatorname{Bun}^d_{\\mathbb{G}_m}$ 的纤维同构于 $\\mathbb{P}\\Gamma(X,L)$，因而是单连通的；于是 $\\sigma^{(d)}$ 沿 $\\mathrm{AJ}_d$ 下降为 $\\operatorname{Bun}^d_{\\mathbb{G}_m}$ 上的 lisse 层。再用 Hecke 性质 $\\chi_\\sigma|_{L(x)}\\cong\\chi_\\sigma|_L\\otimes\\sigma_x$ 把它延拓到所有次数。",
        "notation": "$\\operatorname{Bun}_{\\mathbb{G}_m}\\cong\\operatorname{Jac}(X)\\times\\mathbb{Z}\\times B\\mathbb{G}_m$；$L(x):=L\\otimes\\mathcal{O}(x)$；$\\sigma_x$ 为 $\\sigma$ 在 $x$ 的纤维；$\\mathcal{O}(D)$ 为除子 $D$ 对应的线丛。"
    },
    "key_points": [
        "$\\operatorname{Bun}_{\\mathbb{G}_m}$ 的分类由三部分给出：次数 $d\\in\\mathbb{Z}$、$\\operatorname{Jac}(X)$ 中的次数 $0$ 部分、以及每根线丛的自同构 $\\mathbb{G}_m$；因此只需在 $L=\\mathcal{O}(D)$ 上规定 $\\chi_\\sigma$。",
        "Hecke 性质逐点读出 $\\chi_\\sigma$ 在 $L$ 与 $L(x)$ 两处的纤维之差：$\\chi_\\sigma|_{L(x)}\\cong\\chi_\\sigma|_L\\otimes\\sigma_x$。沿 $X$ 走一圈就把所有次数连起来，所以只需验证它与除子 $D$ 的选取无关。",
        "$\\mathrm{AJ}_d$ 在 $d>2g-2$ 时纤维为 $\\mathbb{P}\\Gamma(X,L)$：此时 $H^1(X,L)=0$，故 $\\Gamma(X,L)$ 的维数为 $d+1-g$，射影化后维数 $d-g$；去掉原点的仿射空间单连通，射影化也单连通。",
        "下降的合法性来自纤维单连通：局部系统沿单连通纤维的拉回是常值的，故 $\\sigma^{(d)}$ 在每根纤维上平凡，从而沿 $\\mathrm{AJ}_d$ 下降。",
        "下降只给出每个 $\\operatorname{Bun}^d_{\\mathbb{G}_m}$ 上的层；Hecke 性质把这些层粘成整个 $\\operatorname{Bun}_{\\mathbb{G}_m}$ 上的 lisse 层。",
        "归一化 $\\chi_\\sigma|_{\\mathcal{O}_X}\\cong\\underline{\\e}$ 固定了整体常数，否则可乘以任意 $\\e^\\times$ 中的标量。"
    ],
    "formulas": [
        "\\chi_\\sigma|_{L(x)}\\cong\\chi_\\sigma|_L\\otimes\\sigma_x",
        "\\sigma^{(d)}=(\\mathrm{add}_{d,*}\\sigma^{\\boxtimes d})^{S_d}",
        "\\chi_\\sigma|_{\\operatorname{Sym}^d X}\\cong\\sigma^{(d)}",
        "\\operatorname{Bun}_{\\mathbb{G}_m}\\cong\\operatorname{Jac}(X)\\times\\mathbb{Z}\\times B\\mathbb{G}_m"
    ],
    "theorems": [
        {
            "name": "构造 1.2.4（Deligne）",
            "statement": "设 $\\sigma$ 为 $X$ 上秩 $1$ 局部系统。存在 $\\operatorname{Bun}_{\\mathbb{G}_m}$ 上的 lisse 层 $\\chi_\\sigma$，使得对每一点 $x\\in X$ 与每根线丛 $L$ 有 $\\chi_\\sigma|_{L(x)}\\cong\\chi_\\sigma|_L\\otimes\\sigma_x$，且 $\\chi_\\sigma|_{\\mathcal{O}_X}\\cong\\underline{\\e}$。",
            "proof": {
                "status": "sketch",
                "steps": [
                    "在 $\\operatorname{Sym}^d X$ 上定义 $\\sigma^{(d)}$，并验证它在 $S_d$ 作用下不变。",
                    "对 $d>2g-2$，验证 $\\mathrm{AJ}_d$ 的纤维为 $\\mathbb{P}\\Gamma(X,L)$，故单连通。",
                    "沿 $\\mathrm{AJ}_d$ 下降，得到 $\\operatorname{Bun}^d_{\\mathbb{G}_m}$ 上的 lisse 层。",
                    "用 Hecke 性质把各次数的层粘成 $\\operatorname{Bun}_{\\mathbb{G}_m}$ 上的层。"
                ],
                "gap_note": "讲义只述构造梗概，未逐条验证下降的数据（等化与上循环）；完整论证见 Deligne, LNM 163 与 Feng 的几何类域论讲义。"
            },
            "source": "§1.2，原文 p.3–4"
        }
    ],
    "pitfalls": [
        "$\\mathrm{AJ}_d$ 的纤维是射影空间 $\\mathbb{P}\\Gamma(X,L)$，不是 $\\Gamma(X,L)\\setminus\\{0\\}$；原文 p.4 写错了，若照抄会得到维数 $d+1-g$（多一维）且不单连通。",
        "条件 $d>2g-2$ 不能省：$d\\le 2g-2$ 时 $H^1(X,L)\\neq 0$，纤维不再是射影空间，单连通性也失效。",
        "Hecke 性质是对所有 $x\\in X$ 的局部条件；只在一点验证不够。",
        "归一化是 $\\chi_\\sigma|_{\\mathcal{O}_X}\\cong\\underline{\\e}$，其中 $\\underline{\\e}$ 是常值层，不是 $\\mathcal{O}_X$ 本身。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§1.2 交换几何类域论",
            "pages": [3, 4],
            "anchor": "源码/sections/s01-intro.tex:L122-L160（Construction 1.2.4）",
            "quote": "Construction 1.2.4 (Deligne). ... The fiber of this map at L is Γ(X,L) ∖ 0. ... σ^(d) := add_{d,*}(σ ⊠ ... ⊠ σ)^{S_d}."
        }
    ],
    "related": [
        "raskin_glc/concept/hecke-eigensheaf",
        "raskin_glc/correction/abel-jacobi-fiber"
    ],
    "rights": "rewritten",
    "status": "dev",
    "verification": {
        "status": "partial",
        "checked_on": "2026-11-27",
        "checks": [
            {
                "source": "nLab",
                "entry": "local system",
                "url": "https://ncatlab.org/nlab/show/local+system",
                "last_revised": "2025-04-10",
                "asserts": "线性局部系统是有限维局部常值层，且与平坦联络、$\\pi_1$ 表示等价；这支持卡中「$\\sigma$ 是秩 $1$ 局部系统」的用法。",
                "verdict": "supports"
            },
            {
                "source": "nLab",
                "entry": "geometric Langlands correspondence",
                "url": "https://ncatlab.org/nlab/show/geometric+Langlands+correspondence",
                "last_revised": "",
                "asserts": "Abelian 情形是 Fourier–Mukai 型构造（Laumon 1985/1996，Rothstein 1996），与卡中「用 Abel–Jacobi 下降构造 $\\chi_\\sigma$」属同一类构造，但页面未逐条覆盖 $\\operatorname{Sym}^d$ 下降。",
                "verdict": "partial"
            }
        ],
        "note": "构造的整体正确性以原文与 Deligne LNM 163 为准；nLab 仅支撑术语与 Abelian 情形的构造类型。"
    }
})

CARDS.append({
    "id": "raskin_glc/concept/cuspidal-sheaf",
    "type": "concept",
    "track": "B",
    "title": "尖点层与常数项函子",
    "aliases": ["cuspidal sheaf", "constant term functor", "CT_*"],
    "summary": "用 Hecke 对应 $\\operatorname{Bun}_{\\mathrm{PGL}_2}\\xleftarrow{p}\\operatorname{Bun}_B\\xrightarrow{q}\\operatorname{Bun}_{\\mathbb{G}_m}$ 定义常数项 $\\mathrm{CT}_*:=q_*p^!$；$\\mathrm{CT}_*\\mathcal{F}\\simeq 0$ 即 $\\mathcal{F}$ 为尖点层。",
    "question": "为什么常数项用 $p^!$ 而不是 $p_*$，以及为什么「对所有 $d$ 消没」等价于「$\\mathrm{CT}_*\\simeq 0$」？",
    "definition": {
        "text": "设 $G=\\mathrm{PGL}_2$，$B\\subset G$ 为 Borel 子群。考虑对应 $\\operatorname{Bun}_G\\xleftarrow{p}\\operatorname{Bun}_B\\xrightarrow{q}\\operatorname{Bun}_{\\mathbb{G}_m}$，其中 $p$ 记 $(0\\to L\\to\\mathcal{E}\\to\\mathcal{O}\\to 0)\\mapsto\\mathcal{E}$，$q$ 记 $\\mapsto L$。定义常数项函子 $\\mathrm{CT}_*:=q_*p^!:\\operatorname{Shv}(\\operatorname{Bun}_G)\\to\\operatorname{Shv}(\\operatorname{Bun}_{\\mathbb{G}_m})$，并按次数分解为 $\\mathrm{CT}^d_*$。称 $\\mathcal{F}\\in\\operatorname{Shv}(\\operatorname{Bun}_G)$ 为尖点层，若 $\\mathrm{CT}_*\\mathcal{F}\\simeq 0$；等价地，对所有 $d$ 有 $\\mathrm{CT}^d_*\\mathcal{F}\\simeq 0$。一般约化群用所有真抛物子群及其 Levi 商重复此定义。",
        "notation": "$\\operatorname{Bun}^d_B$ 为 $\\deg L=d$ 的连通分支；$\\mathrm{CT}^d_*$ 为 $\\mathrm{CT}_*$ 限制到该分支；$\\operatorname{Shv}$ 为可构造层的有界导出范畴。"
    },
    "key_points": [
        "常数项是「沿抛物子群的纤维做紧支集积分」的层论版本：$p^!$ 先把 $\\mathcal{F}$ 拉回到 $\\operatorname{Bun}_B$，再用 $q_*$ 沿 $\\operatorname{Bun}_B\\to\\operatorname{Bun}_{\\mathbb{G}_m}$ 推前。",
        "$p^!$ 而非 $p_*$ 的选择使 $\\mathrm{CT}_*$ 与 Verdier 对偶交换：$\\mathrm{CT}_*\\simeq D\\,\\mathrm{CT}^!\\,D$，其中 $\\mathrm{CT}^!:=q_!p^*$。",
        "对 $\\mathrm{PGL}_2$，$\\operatorname{Bun}_B$ 按 $\\deg L$ 分解，因此 $\\mathrm{CT}_*\\simeq 0$ 等价于每个 $\\mathrm{CT}^d_*\\simeq 0$；一般 $G$ 要对所有真抛物子群及 Levi 商同时消没。",
        "尖点性在 Verdier 对偶下保持（Cor 2.1.9），并且在 $d>2g-2$ 时给出到 $\\operatorname{Bun}^d_B$ 的 $!$-与 $*$-限制的消没（Cor 2.1.10）。",
        "存在只依赖 $g$ 的开子叠 $U_n$，任意尖点层都从 $U_n$ 同时以 $!$ 与 $*$ 延拓（Cor 2.1.11）；这是后面「先用 $U_n$ 上的限制控制 $\\mathcal{F}$」的起点。"
    ],
    "formulas": [
        "\\mathrm{CT}_*:=q_*p^!",
        "\\mathrm{CT}^!:=q_!p^*",
        "\\mathrm{CT}_*\\simeq D\\,\\mathrm{CT}^!\\,D",
        "\\mathrm{CT}_*\\mathcal{F}\\simeq 0\\iff \\forall d,\\ \\mathrm{CT}^d_*\\mathcal{F}\\simeq 0"
    ],
    "theorems": [
        {
            "name": "命题 2.1.5",
            "statement": "若 $\\mathcal{F}$ 为尖点层，则对 $d>2g-2$，$\\mathcal{F}$ 到 $\\operatorname{Bun}^d_B$ 的 $!$-限制为零。",
            "proof": {
                "status": "sketch",
                "steps": [
                    "记 $q_d:\\operatorname{Bun}^d_B\\to\\operatorname{Bun}^d_{\\mathbb{G}_m}$。$d>2g-2$ 时扩张 $0\\to L\\to\\mathcal{E}\\to\\mathcal{O}\\to 0$ 分裂，故 $\\operatorname{Bun}^d_B\\to\\operatorname{Bun}^d_{\\mathbb{G}_m}$ 的纤维为 $B H^1(X,L)$（按脚注应写 $B\\,R\\Gamma(X,L)[1]$）。",
                    "此时 $H^1(X,L)=0$，$H^0(X,L)\\neq 0$，纤维实为 $B H^0(X,L)$。",
                    "对 $\\pi:B\\mathbb{G}_a\\to\\mathrm{pt}$，$\\pi^*:\\operatorname{Vect}\\leftrightarrow\\operatorname{Shv}(B\\mathbb{G}_a):\\pi_*$ 是等价（$\\mathbb{G}_a$ 可缩）。",
                    "因此 $q_{d,*}$ 是等价；由 $\\mathrm{CT}^d_*\\mathcal{F}=q_{d,*}p_d^!\\mathcal{F}\\simeq 0$ 得 $p_d^!\\mathcal{F}\\simeq 0$。"
                ],
                "gap_note": "原文正文写 $B H^1(X,L)$ 并称 $H^1$ 可缩，与 $d>2g-2$ 时 $H^1=0$、$H^0\\neq0$ 矛盾；脚注给出 $R\\Gamma(X,L)[1]$。正确写法是 $B H^0(X,L)$，见勘误卡。"
            },
            "source": "§2.1，原文 p.6"
        },
        {
            "name": "推论 2.1.9–2.1.11",
            "statement": "(a) $\\mathcal{F}$ 可构造且尖点，则 $D\\mathcal{F}$ 尖点；(b) 尖点 $\\mathcal{F}$ 对 $d>2g-2$ 到 $\\operatorname{Bun}^d_B$ 的 $*$-限制为零；(c) 存在开子叠 $U_n$，任意尖点层从 $U_n$ 同时以 $!$ 与 $*$ 延拓。",
            "proof": {
                "status": "cited",
                "gap_note": "讲义把 (a)(b) 归于 Verdier 对偶与第二伴随，(c) 归于 $\\mathrm{CT}$ 的消没；证明细节见 Drinfeld–Gaitsgory, Selecta Math. 22 (2016)。"
            },
            "source": "§2.1，原文 p.6–7"
        }
    ],
    "pitfalls": [
        "常数项不是 $q_*p_*$：$p^!$ 与 $p_*$ 在非光滑、非固有情形差别很大；用错会破坏与 Verdier 对偶的交换性。",
        "「尖点」是对所有真抛物子群及其 Levi 商同时消没；对 $\\mathrm{PGL}_2$ 只有标准 Borel，所以只看 $\\mathrm{CT}_*$ 就够。",
        "对 $d>2g-2$ 的消没是 $!$-限制的消没，不是 $*$-限制；后者是推论，不是定义。",
        "原文 p.6 的 $B H^1(X,L)$ 与「$H^1$ 可缩」两句话不能同时成立；应以 $B H^0(X,L)$ 或 $B R\\Gamma(X,L)[1]$ 理解。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§2.1 尖点性",
            "pages": [6, 7],
            "anchor": "源码/sections/s02-cusp.tex:L21-L70（Definition 2.1.1/2.1.2 与 Prop 2.1.5）",
            "quote": "Definition 2.1.2. ... We say that F is cuspidal if CT_* F ≃ 0."
        }
    ],
    "related": [
        "raskin_glc/derivation/cuspidal-vanishing",
        "raskin_glc/concept/coefficient-functor",
        "raskin_glc/concept/pgl2-geometric-langlands"
    ],
    "rights": "rewritten",
    "status": "dev",
    "verification": {
        "status": "partial",
        "checked_on": "2026-11-27",
        "checks": [
            {
                "source": "nLab",
                "entry": "perverse sheaf",
                "url": "https://ncatlab.org/nlab/show/perverse+sheaf",
                "last_revised": "2026-10-16",
                "asserts": "反常层是可构造有界导出范畴的 abelian 子范畴；这支撑卡中「$\\mathcal{F}$ 为可构造层」与尖点性在 $\\operatorname{Shv}$ 中讨论的框架，但不涉及常数项定义。",
                "verdict": "partial"
            }
        ],
        "note": "常数项函子的定义与第二伴随以原文和 Drinfeld–Gaitsgory 为准；nLab 只提供反常层框架。"
    }
})

CARDS.append({
    "id": "raskin_glc/derivation/cuspidal-vanishing",
    "type": "derivation",
    "track": "B",
    "title": "尖点层在 $d>2g-2$ 的 $!$-消没：命题 2.1.5 的拆解",
    "aliases": ["Prop 2.1.5 proof", "cuspidal vanishing"],
    "summary": "把命题 2.1.5 拆成四步：扩张分裂、纤维识别为 $B H^0$、$B\\mathbb{G}_a$ 的层范畴平凡、由 $q_{d,*}$ 等价推出 $p_d^!\\mathcal{F}=0$。",
    "question": "为什么「$\\mathrm{CT}^d_*\\mathcal{F}=0$」能反推出「$p_d^!\\mathcal{F}=0$」，而不是只得到 $q_{d,*}$ 的核？",
    "goal": "设 $\\mathcal{F}\\in\\operatorname{Shv}(\\operatorname{Bun}_{\\mathrm{PGL}_2})$ 为尖点层。证明：对 $d>2g-2$，$p_d^!\\mathcal{F}\\simeq 0$，其中 $p_d:\\operatorname{Bun}^d_B\\to\\operatorname{Bun}_{\\mathrm{PGL}_2}$。",
    "setup": "记 $q_d:\\operatorname{Bun}^d_B\\to\\operatorname{Bun}^d_{\\mathbb{G}_m}$。$\\operatorname{Bun}^d_B$ 分类正合列 $0\\to L\\to\\mathcal{E}\\to\\mathcal{O}\\to 0$，$\\deg L=d$。$\\mathrm{CT}^d_*:=q_{d,*}p_d^!$。",
    "steps": [
        {
            "n": 1,
            "claim": "$d>2g-2$ 时，上述正合列自动分裂，故 $\\operatorname{Bun}^d_B\\to\\operatorname{Bun}^d_{\\mathbb{G}_m}$ 的纤维是 $\\operatorname{Ext}^1(\\mathcal{O},L)=H^1(X,L)$ 的分类叠。",
            "justification": "$\\operatorname{Ext}^1(\\mathcal{O},L)\\cong H^1(X,L)$；$\\deg L=d>2g-2=\\deg\\Omega$，故 $\\deg(L^\\vee\\otimes\\Omega)<0$，$H^1(X,L)^\\vee\\cong H^0(X,L^\\vee\\otimes\\Omega)=0$，所有扩张分裂。"
        },
        {
            "n": 2,
            "claim": "该纤维作为叠同构于 $B H^0(X,L)$（或等价的 $B R\\Gamma(X,L)[1]$），而不是 $B H^1(X,L)$。",
            "justification": "扩张分裂后，自同构群为 $\\operatorname{Hom}(\\mathcal{O},L)=H^0(X,L)$；$H^1=0$ 使 $R\\Gamma(X,L)[1]$ 只在 $H^0$ 处有上同调。原文正文的 $B H^1$ 与脚注的 $R\\Gamma[1]$ 应统一为 $B H^0$。"
        },
        {
            "n": 3,
            "claim": "对 $\\pi:B\\mathbb{G}_a\\to\\mathrm{pt}$，$\\pi^*:\\operatorname{Vect}\\to\\operatorname{Shv}(B\\mathbb{G}_a)$ 与 $\\pi_*$ 互为等价。",
            "justification": "$\\mathbb{G}_a$ 作为 $k$ 上的群是可缩的（$k$ 代数闭、char $\\e=0$ 的层论中 $\\mathbb{G}_a$ 的 classifying stack 的层范畴平凡）；更一般地，$B\\mathbb{G}_a$ 上的层由其在点上的纤维决定。"
        },
        {
            "n": 4,
            "claim": "$q_{d,*}$ 是等价，故 $\\mathrm{CT}^d_*\\mathcal{F}=q_{d,*}p_d^!\\mathcal{F}\\simeq 0$ 蕴含 $p_d^!\\mathcal{F}\\simeq 0$。",
            "justification": "第 3 步逐纤维应用：$q_d$ 是 $B\\mathbb{G}_a$-gerbe，$q_{d,*}$ 与 $q_d^*$ 互为逆；$q_{d,*}$ 反映零对象。"
        }
    ],
    "result": "尖点性 $\\mathrm{CT}_*\\mathcal{F}=0$ 迫使 $\\mathcal{F}$ 在所有 $d>2g-2$ 的 $\\operatorname{Bun}^d_B$ 上 $!$-限制为零。",
    "gaps": [
        "原文正文写 $B H^1(X,L)$ 并说「$H^1(X,L)$ 可缩」，这与 $d>2g-2$ 时 $H^1=0$、$H^0\\neq0$ 直接矛盾；脚注的 $R\\Gamma(X,L)[1]$ 才是对的，但应展开为 $B H^0$。",
        "$q_{d,*}$ 为等价的论证依赖 $\\operatorname{Shv}(B\\mathbb{G}_a)\\simeq\\operatorname{Vect}$；这一步在 de Rham/ℓ-进/Betti 三种系数下都成立，但讲义未逐系数说明。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§2.1，命题 2.1.5 及其证明",
            "pages": [6],
            "anchor": "源码/sections/s02-cusp.tex:L54-L92（Prop 2.1.5 证明）",
            "quote": "Proof. ... the fiber of q_d is B H^1(X,L). ... because H^1(X,L) is contractible."
        }
    ],
    "related": [
        "raskin_glc/concept/cuspidal-sheaf",
        "raskin_glc/concept/coefficient-functor"
    ],
    "rights": "rewritten",
    "status": "dev",
    "verification": {
        "status": "partial",
        "checked_on": "2026-11-27",
        "checks": [
            {
                "source": "nLab",
                "entry": "perverse sheaf",
                "url": "https://ncatlab.org/nlab/show/perverse+sheaf",
                "last_revised": "2026-10-16",
                "asserts": "页面只给反常层的范畴框架，不涉及 $B\\mathbb{G}_a$ 的层范畴或 Ext 计算；本卡的技术步骤以原文与标准形变理论为准。",
                "verdict": "not_applicable"
            }
        ],
        "note": "拆解按原文证明逻辑重排；第 2 步的 $B H^0$ 修正是本卡的核心发现。"
    }
})

CARDS.append({
    "id": "raskin_glc/concept/coefficient-functor",
    "type": "concept",
    "track": "B",
    "title": "$\\operatorname{coeff}_D$：把层变成向量空间的系数函子",
    "aliases": ["coeff_D", "coefficient functor", "Whittaker coefficient prototype"],
    "summary": "在 $\\operatorname{Bun}^{\\Omega(-D)}_N$ 上取 $!$-拉回、与 $\\exp$ 层做 $\\otimes^!$、再取紧支集积分，得到向量空间 $\\operatorname{coeff}_D(\\mathcal{F})$；$D=0$ 对应模形式的常数项。",
    "question": "为什么 $D=0$ 的 $\\operatorname{coeff}_0$ 对应模形式的常数项 $a_0$，而一般除子 $D$ 对应 $a_n$？",
    "definition": {
        "text": "对有效除子 $D=\\sum_i n_i x_i$，令 $\\operatorname{Bun}^{\\Omega(-D)}_N:=\\operatorname{Bun}_B\\times_{\\operatorname{Bun}_{\\mathbb{G}_m}}\\{\\Omega(-D)\\}$，它分类正合列 $0\\to\\Omega(-D)\\to\\mathcal{E}\\to\\mathcal{O}\\to 0$。记 $p_{N,D}:\\operatorname{Bun}^{\\Omega(-D)}_N\\to\\operatorname{Bun}_G$，并令 $\\varphi_D$ 为复合 $\\operatorname{Bun}^{\\Omega(-D)}_N\\to H^1(X,\\Omega(-D))\\to H^1(X,\\Omega)\\cong\\mathbb{A}^1$（Serre 对偶）。定义 $\\operatorname{coeff}_D(\\mathcal{F}):=\\mathbb{C}\\cdot(\\operatorname{Bun}^{\\Omega(-D)}_N,p_{N,D}^!\\mathcal{F}\\otimes^!\\varphi_D^!\\exp)$，其中 $\\mathbb{C}\\cdot$ 表示紧支集积分（取整体截面）。",
        "notation": "$\\Omega=\\Omega^1_X$；$\\Omega(-D):=\\Omega\\otimes\\mathcal{O}(-D)$；$\\exp$ 为 $\\mathbb{A}^1$ 上的指数层（de Rham 情形 $(\\mathcal{O},\\nabla=d-dt)$）；$\\otimes^!$ 为 $!$-张量积。"
    },
    "key_points": [
        "$\\operatorname{Bun}^{\\Omega(-D)}_N$ 比 $\\operatorname{Bun}_B$ 多记录一条同构 $L\\cong\\Omega(-D)$，因此是 $\\operatorname{Bun}_{\\mathbb{G}_m}$ 上的纤维积；这使 $\\varphi_D$ 成为到 $\\mathbb{A}^1$ 的映射。",
        "Serre 对偶给出 $H^1(X,\\Omega(-D))\\cong H^0(X,\\mathcal{O}(D))^\\vee$，故 $D=0$ 时 $\\varphi_0$ 的目标是 $H^1(X,\\Omega)\\cong k$，这正是「常数项」的来源。",
        "$D=\\sum n_i x_i$ 时，$\\operatorname{coeff}_D$ 只依赖 $D$ 作为除子，不依赖把 $D$ 写成点之和的方式；它把 $\\operatorname{Bun}_G$ 上的层变成向量空间。",
        "对 $\\mathcal{F}=\\mathcal{F}_\\sigma$，期望 $\\operatorname{coeff}_D(\\mathcal{F}_\\sigma)\\cong\\bigotimes_i\\operatorname{Sym}^{n_i}(\\sigma_{x_i})$；这是 Goal 3.1.2 的 $D$-版本，也是模形式系数 $a_n$ 的层论类比。",
        "把 $D$ 变动得到函子 $\\operatorname{coeff}_d:\\operatorname{Shv}(\\operatorname{Bun}_G)\\to\\operatorname{Shv}(\\operatorname{Sym}^d X)$；在 $\\mathcal{F}_\\sigma$ 上它应等于 $\\sigma^{(d)}$。"
    ],
    "formulas": [
        "\\operatorname{coeff}_D(\\mathcal{F})=\\mathbb{C}\\cdot\\left(\\operatorname{Bun}^{\\Omega(-D)}_N,\\ p_{N,D}^!\\mathcal{F}\\otimes^!\\varphi_D^!\\exp\\right)",
        "\\operatorname{Bun}^{\\Omega(-D)}_N:=\\operatorname{Bun}_B\\times_{\\operatorname{Bun}_{\\mathbb{G}_m}}\\{\\Omega(-D)\\}",
        "\\operatorname{coeff}_D(\\mathcal{F}_\\sigma)\\cong\\bigotimes_i\\operatorname{Sym}^{n_i}(\\sigma_{x_i})",
        "\\operatorname{coeff}_d(\\mathcal{F}_\\sigma)\\cong\\sigma^{(d)}"
    ],
    "theorems": [
        {
            "name": "定义 3.1.1（$\\operatorname{coeff}_D$）",
            "statement": "对有效除子 $D$ 与 $\\mathcal{F}\\in\\operatorname{Shv}(\\operatorname{Bun}_G)$，$\\operatorname{coeff}_D(\\mathcal{F})$ 是上述紧支集积分得到的向量空间；它是 $\\mathcal{F}$ 的「第 $D$ 个 Fourier 系数」。",
            "proof": {"status": "none", "gap_note": "定义，无需证明。"},
            "source": "§3.1，原文 p.8"
        },
        {
            "name": "目标 3.1.2",
            "statement": "对不可约 $\\mathrm{SL}_2$ 局部系统 $\\sigma$，存在尖点反常层 $\\mathcal{F}_\\sigma$，在每个连通分支上不可约，且对所有 $D=\\sum n_i x_i$ 有 $\\operatorname{coeff}_D(\\mathcal{F}_\\sigma)\\cong\\bigotimes_i\\operatorname{Sym}^{n_i}(\\sigma_{x_i})$。",
            "proof": {
                "status": "cited",
                "gap_note": "这是第三讲的「目标」，其存在性在 §3.3 由 Drinfeld–Laumon–FGV 定理给出；系数计算是 Hecke 特征性质的推论。"
            },
            "source": "§3.1，原文 p.8"
        },
        {
            "name": "命题 3.1.4",
            "statement": "若 $\\mathcal{F}$ 为尖点反常层、在 $\\operatorname{Bun}^{\\mathrm{even}/\\mathrm{odd}}$ 上不可约且支撑稠密，则 $\\mathcal{F}$ 由 $\\operatorname{coeff}_d(\\mathcal{F})$ 与 $\\operatorname{coeff}_{d+1}(\\mathcal{F})$（任意 $d>N(g)$）唯一确定。",
            "proof": {
                "status": "sketch",
                "gap_note": "证明用 Fourier 变换与 $U_n$ 上的连通纤维；讲义只给梗概，并警告此断言仅对 $\\mathrm{PGL}_2$ 特殊。"
            },
            "source": "§3.1，原文 p.8–9"
        }
    ],
    "pitfalls": [
        "线丛是 $\\Omega(-D)$ 而不是 $\\mathcal{O}(-D)$：这里要用 Serre 对偶把 $H^1$ 变成 $H^0$ 的对偶，才能把 $\\varphi_D$ 落到 $\\mathbb{A}^1$。",
        "$\\mathbb{C}\\cdot(\\cdots)$ 是紧支集积分/整体截面的简写，不是「乘以常数层」；读公式时要按六函子理解。",
        "$D$ 是有效除子，$n_i\\ge 0$；$\\operatorname{coeff}_D$ 对 $D$ 的写法不变，但 $\\operatorname{Sym}^{n_i}$ 的次序按点排列。",
        "$\\operatorname{coeff}_D(\\mathcal{F})$ 是向量空间，不是 $X$ 上的层；只有把 $D$ 变动时才得到 $\\operatorname{Sym}^d X$ 上的层。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§3.1 系数函子",
            "pages": [8, 9],
            "anchor": "源码/sections/s03-coeff.tex:L29-L75（Definition 3.1.1 与 Goal 3.1.2）",
            "quote": "Definition 3.1.1. ... coeff_D(F) := C · (Bun^{Ω(−D)}_N, p^!_{N,D}(F) ⊗^! φ_D^! (exp))."
        }
    ],
    "related": [
        "raskin_glc/concept/cuspidal-sheaf",
        "raskin_glc/concept/fourier-deligne-transform",
        "raskin_glc/concept/whittaker-coefficient",
        "raskin_glc/concept/pgl2-geometric-langlands"
    ],
    "rights": "rewritten",
    "status": "dev",
    "verification": {
        "status": "partial",
        "checked_on": "2026-11-27",
        "checks": [
            {
                "source": "nLab",
                "entry": "perverse sheaf",
                "url": "https://ncatlab.org/nlab/show/perverse+sheaf",
                "last_revised": "2026-10-16",
                "asserts": "反常层框架支撑「$\\mathcal{F}_\\sigma$ 是尖点反常层」的表述；页面不涉及 $\\operatorname{coeff}_D$ 的构造。",
                "verdict": "partial"
            }
        ],
        "note": "系数函子的定义与 Goal 3.1.2 以原文为准；nLab 仅支撑层的类型。"
    }
})

CARDS.append({
    "id": "raskin_glc/concept/fourier-deligne-transform",
    "type": "concept",
    "track": "C",
    "title": "Fourier–Deligne 变换与 $\\operatorname{coeff}_d$ 的改写",
    "aliases": ["Fourier transform", "Fourier–Deligne", "Four(F)"],
    "summary": "在 $V\\times V^\\vee$ 上用 $\\exp$ 核做「$!$-拉回—$!$-张量—推前」，得到 Fourier 变换；它把 $\\operatorname{coeff}_d$ 改写成向量丛 $E_d^\\vee$ 上的限制，从而把命题 3.1.4 化到零截面的消没。",
    "question": "为什么 Fourier 变换能把「$\\operatorname{Bun}_B$ 上的 $!$-限制」换成「向量丛 $E_d^\\vee$ 上的限制」，零截面又为什么对应常数项？",
    "definition": {
        "text": "设 $V$ 为有限维 $k$-向量空间，$V^\\vee$ 为其对偶，$\\mathrm{ev}:V\\times V^\\vee\\to\\mathbb{A}^1$ 为配对。对 $\\mathcal{F}\\in\\operatorname{Shv}(V)$，定义 $\\mathrm{Four}(\\mathcal{F}):=\\mathrm{pr}_{2,*}(\\mathrm{pr}_1^!\\mathcal{F}\\otimes^!\\mathrm{ev}^!\\exp)$。同一公式对向量丛 $E\\to S$ 与 $E^\\vee\\to S$ 逐纤维成立，给出 $\\operatorname{Shv}(E)\\to\\operatorname{Shv}(E^\\vee)$ 的等价（Fourier 反演）。",
        "notation": "$\\mathrm{pr}_1:E\\times_S E^\\vee\\to E$，$\\mathrm{pr}_2:E\\times_S E^\\vee\\to E^\\vee$；$\\exp$ 为 $\\mathbb{A}^1$ 上的指数层；$\\otimes^!$ 为 $!$-张量积。"
    },
    "key_points": [
        "Fourier 变换是 $\\operatorname{Shv}(V)$ 到 $\\operatorname{Shv}(V^\\vee)$ 的等价，逆变换由同一构造（交换 $V$ 与 $V^\\vee$）给出；在 de Rham 与 ℓ-进情形都有对应版本，Betti 情形需用单值化替代。",
        "在 $\\operatorname{Bun}_B$ 的改写中，取 $q_{-d}:\\operatorname{Bun}^{-d}_B\\to\\operatorname{Bun}^{-d}_{\\mathbb{G}_m}$。对 $d>0$ 有 $H^0(X,L)=0$，故 $q_{-d}$ 是向量丛 $E_d$，其纤维为 $H^1(X,L)$。",
        "$E_d^\\vee$ 的纤维为 $H^1(X,L)^\\vee\\cong H^0(X,L^\\vee\\otimes\\Omega)$，故 $E_d^\\vee$ 分类「截面 $s:L\\to\\Omega$」；$\\operatorname{Sym}^{d+(2g-2)}X\\to E_d^\\vee\\setminus\\{0\\}$ 把 $D$ 送到 $\\Omega(-D)\\to\\Omega$。",
        "练习 3.2.2 断言 $\\operatorname{coeff}_{d+(2g-2)}=\\mathrm{restriction}\\circ\\mathrm{Four}\\circ p_{-d}^!$：先在 $\\operatorname{Bun}^{-d}_B$ 上 $!$-拉回，做 Fourier，再限制到 $E_d^\\vee\\setminus\\{0\\}$。",
        "零截面上的 $!$-限制对应 $\\mathrm{CT}^{-d}_*$；尖点性正给出该限制为零，于是 $\\mathrm{Four}(p_{-d}^!\\mathcal{F})$ 由非零部分完全决定，再由 Fact 3.2.3/3.2.4 的「拉回全忠实」恢复 $p_{-d}^!\\mathcal{F}$。"
    ],
    "formulas": [
        "\\mathrm{Four}(\\mathcal{F})=\\mathrm{pr}_{2,*}\\left(\\mathrm{pr}_1^!\\mathcal{F}\\otimes^!\\mathrm{ev}^!\\exp\\right)",
        "E_d^\\vee\\text{ 的纤维}=H^1(X,L)^\\vee\\cong H^0(X,L^\\vee\\otimes\\Omega)",
        "\\operatorname{coeff}_{d+(2g-2)}=\\mathrm{restriction}\\circ\\mathrm{Four}\\circ p_{-d}^!"
    ],
    "theorems": [
        {
            "name": "练习 3.2.2",
            "statement": "$\\operatorname{coeff}_{d+(2g-2)}=\\mathrm{restriction}\\circ\\mathrm{Four}\\circ p_{-d}^!$，其中 restriction 指限制到 $E_d^\\vee\\setminus\\{0\\}\\subset E_d^\\vee$。",
            "proof": {"status": "none", "gap_note": "讲义留作练习；证明按定义展开 $\\operatorname{coeff}$ 与 $\\mathrm{Four}$，并用 $\\operatorname{Sym}^{d+2g-2}X\\to E_d^\\vee$ 的识别。"},
            "source": "§3.2，原文 p.9–10"
        },
        {
            "name": "Fact 3.2.3 / 3.2.4",
            "statement": "若 $f:E\\to S$ 光滑且纤维连通（或空），则反常层沿 $f$ 的拉回全忠实；特别地，不可约、支撑稠密的层由其在 $E\\setminus\\{0\\}$ 上的限制决定。",
            "proof": {"status": "cited", "gap_note": "引自 Beilinson–Drinfeld / Gaitsgory 的一般事实；讲义未证。"},
            "source": "§3.2，原文 p.10"
        }
    ],
    "pitfalls": [
        "Fourier 变换的核是 $\\exp$，不是加性特征 $\\psi$ 本身；在 de Rham 情形 $\\exp=(\\mathcal{O},\\nabla=d-dt)$，在 ℓ-进情形要用 Artin–Schreier 构造。",
        "$E_d$ 与 $E_d^\\vee$ 不能混：$E_d$ 的纤维是 $H^1(X,L)$，$E_d^\\vee$ 的纤维才是 $H^0(X,L^\\vee\\otimes\\Omega)$；练习 3.2.2 的 restriction 落在 $E_d^\\vee\\setminus\\{0\\}$。",
        "Betti 系数下没有 $\\exp$ 层，Fourier 变换需换成别的技巧（讲义明确说「Betti 情形没有 $\\exp$」）。",
        "$\\operatorname{coeff}_{d+2g-2}$ 的下标是 $d+2g-2$，不是 $d$；这是由 $\\Omega$ 的次数 $2g-2$ 造成的平移。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§3.2 Fourier(–Deligne) 变换",
            "pages": [9, 10],
            "anchor": "源码/sections/s03-coeff.tex:L110-L175（Four 定义与练习 3.2.2）",
            "quote": "Four(F) := pr_{2,*}(pr_1^! F ⊗^! ev^! (exp))."
        }
    ],
    "related": [
        "raskin_glc/concept/coefficient-functor",
        "raskin_glc/concept/pgl2-geometric-langlands"
    ],
    "rights": "rewritten",
    "status": "dev",
    "verification": {
        "status": "source-only",
        "checked_on": "2026-11-27",
        "checks": [],
        "note": "未抓取到可直接引用的 nLab 条目逐字覆盖 $\\exp$ 层的 $!$-Fourier 变换，故不写外部核验；构造以原文 §3.2 与 Beilinson–Drinfeld 的框架为准。"
    }
})
