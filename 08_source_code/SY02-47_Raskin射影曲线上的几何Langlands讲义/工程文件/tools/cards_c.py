# -*- coding: utf-8 -*-
"""Raskin 讲义资料卡：第三组（范畴化、勘误、约定说明）。"""

SRC = "Sam Raskin 讲授、Lin Chen 笔记《Notes for \"Geometric Langlands for Projective Curves\"》（2025-07-07/11，18 页）"

CARDS = []

CARDS.append({
    "id": "raskin_glc/concept/categorical-geometric-langlands",
    "type": "concept",
    "track": "E",
    "title": "范畴化几何 Langlands",
    "aliases": ["categorical geometric Langlands", "LG functor", "IndCohNilp"],
    "summary": "$\\mathrm{LG}:\\operatorname{DMod}(\\operatorname{Bun}_G)\\to\\operatorname{IndCoh}_{\\mathrm{Nilp}}(\\operatorname{LS}_{\\check G})$ 是等价；粗版 $\\operatorname{QCoh}$ 陈述只在尖点子范畴成立，全局需 Arinkin–Gaitsgory 的幂零修正。",
    "question": "为什么粗版 $\\mathrm{LG}_{\\mathrm{coarse}}$ 不可能是等价？",
    "definition": {
        "text": "设 $\\operatorname{LS}_{\\check G}=\\operatorname{LS}^{\\mathrm{dR}}_{\\check G}$ 为 de Rham $\\check G$-局部系统的模叠。粗版函子 $\\mathrm{LG}_{\\mathrm{coarse}}:\\operatorname{DMod}(\\operatorname{Bun}_G)\\to\\operatorname{QCoh}(\\operatorname{LS}_{\\check G})$ 由「把常层送到零」之外的 Hecke 作用刻画。Arinkin–Gaitsgory 的修正把目标换成 $\\operatorname{IndCoh}_{\\mathrm{Nilp}}(\\operatorname{LS}_{\\check G})$：由所有抛物 $\\check G_P$ 及其 Levi 商 $\\check G_M$ 的 $\\operatorname{Perf}(\\operatorname{LS}_{\\check G_M})\\to\\operatorname{Coh}(\\operatorname{LS}_{\\check G})$ 的像生成。定理 5.2.9 断言存在唯一函子 $\\mathrm{LG}:\\operatorname{DMod}(\\operatorname{Bun}_G)\\to\\operatorname{IndCoh}_{\\mathrm{Nilp}}(\\operatorname{LS}_{\\check G})$ 与 $\\mathrm{LG}_{\\mathrm{coarse}}$ 相容，且它是等价。",
        "notation": "$\\operatorname{DMod}$ 为 D-模范畴；$\\operatorname{IndCoh}_{\\mathrm{Nilp}}$ 为幂零奇异支撑的归纳凝聚层；$\\operatorname{LS}^{\\mathrm{dR}}_{\\check G}$ 为 de Rham 局部系统模叠；$\\operatorname{LS}^{\\mathrm{irred}}_{\\check G}\\subset\\operatorname{LS}_{\\check G}$ 为不可约轨迹。"
    },
    "key_points": [
        "粗版不可能是等价：对非交换 $G$，$\\mathrm{LG}_{\\mathrm{coarse}}$ 把常层送到零，而 $\\operatorname{QCoh}(\\operatorname{LS}_{\\check G})$ 中零对象只有零；故它必有非平凡核。",
        "尖点版本（定理 5.2.5）是第一个正确陈述：$\\mathrm{LG}_{\\mathrm{coarse}}$ 诱导 $\\operatorname{DMod}(\\operatorname{Bun}_G)_{\\mathrm{cusp}}\\simeq\\operatorname{QCoh}(\\operatorname{LS}^{\\mathrm{irred}}_{\\check G})$。",
        "全局版本必须把 $\\operatorname{QCoh}$ 换成 $\\operatorname{IndCoh}_{\\mathrm{Nilp}}$：$\\operatorname{Perf}\\subset\\operatorname{Coh}$ 在 $\\operatorname{LS}_{\\check G}$ 有奇点时不相等，$\\operatorname{QCoh}=\\operatorname{Ind}(\\operatorname{Perf})$ 会丢掉幂零方向的信息。",
        "$\\operatorname{Coh}_{\\mathrm{Nilp}}$ 可由「所有抛物诱导的完美复形的像」生成，也可用凝聚层的奇异支撑内蕴定义（Remark 5.2.7）；两种定义给出同一子范畴。",
        "主定理 5.2.9 的证明用 de Rham 特殊性（如临界水平 Kac–Moody 局部化），并依赖 2024 年「具体」定理 4.3.2 的全部范畴断言；Betti 与 ℓ-进版本可经 Riemann–Hilbert 得到。"
    ],
    "formulas": [
        "\\mathrm{LG}:\\operatorname{DMod}(\\operatorname{Bun}_G)\\to\\operatorname{IndCoh}_{\\mathrm{Nilp}}(\\operatorname{LS}_{\\check G})",
        "\\operatorname{DMod}(\\operatorname{Bun}_G)_{\\mathrm{cusp}}\\simeq\\operatorname{QCoh}(\\operatorname{LS}^{\\mathrm{irred}}_{\\check G})",
        "\\operatorname{QCoh}(Y)\\simeq\\operatorname{Ind}(\\operatorname{Perf}(Y)),\\qquad\\operatorname{IndCoh}(Y):=\\operatorname{Ind}(\\operatorname{Coh}(Y))"
    ],
    "theorems": [
        {
            "name": "定理 5.2.2 / 5.2.3（Lurie, Gaitsgory–Rozenblyum; Drinfeld–Gaitsgory）",
            "statement": "(5.2.2) $\\operatorname{Loc}:\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}\\to\\operatorname{QCoh}(\\operatorname{LS}_{\\check G})$ 有全忠实右伴随；(5.2.3) $\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}$ 在 $\\operatorname{DMod}(\\operatorname{Bun}_G)$ 上的作用经 $\\operatorname{Loc}$ 分解。",
            "proof": {"status": "cited", "gap_note": "引自 Lurie 与 Gaitsgory–Rozenblyum；讲义只引结论。"},
            "source": "§5.2，原文 p.17"
        },
        {
            "name": "主定理 5.2.5（尖点范畴化几何 Langlands）",
            "statement": "$\\mathrm{LG}_{\\mathrm{coarse}}$ 诱导 $\\operatorname{DMod}(\\operatorname{Bun}_G)_{\\mathrm{cusp}}\\simeq\\operatorname{QCoh}(\\operatorname{LS}^{\\mathrm{irred}}_{\\check G})$。",
            "proof": {"status": "cited", "gap_note": "2024 年证明的一部分；讲义只述结论。"},
            "source": "§5.2，原文 p.17"
        },
        {
            "name": "定理 5.2.8 与主定理 5.2.9",
            "statement": "存在唯一函子 $\\mathrm{LG}:\\operatorname{DMod}(\\operatorname{Bun}_G)\\to\\operatorname{IndCoh}_{\\mathrm{Nilp}}(\\operatorname{LS}_{\\check G})$，与 $\\mathrm{LG}_{\\mathrm{coarse}}$ 相容（经 $\\Psi:\\operatorname{IndCoh}_{\\mathrm{Nilp}}\\to\\operatorname{QCoh}$），且 $\\mathrm{LG}$ 是等价。",
            "proof": {
                "status": "cited",
                "gap_note": "2024–2025 年几何 Langlands 证明的最终形式；证明用 de Rham 特殊性与 Kac–Moody 局部化，讲义不展开。"
            },
            "source": "§5.2，原文 p.18"
        }
    ],
    "pitfalls": [
        "$\\operatorname{QCoh}$ 与 $\\operatorname{IndCoh}$ 不能混：$\\operatorname{QCoh}=\\operatorname{Ind}(\\operatorname{Perf})$，$\\operatorname{IndCoh}=\\operatorname{Ind}(\\operatorname{Coh})$；在奇点处 $\\operatorname{Perf}\\subsetneq\\operatorname{Coh}$。",
        "粗版 $\\mathrm{LG}_{\\mathrm{coarse}}$ 在尖点子范畴上才是等价；全局必须加 Nilp 修正，否则常层会落到零。",
        "$\\operatorname{LS}^{\\mathrm{irred}}_{\\check G}$ 是不可约局部系统的轨迹，不是整个 $\\operatorname{LS}_{\\check G}$；把尖点版本误写成全局版本会丢掉可约 $\\sigma$ 的贡献。",
        "主定理要求 char $k=0$ 且 de Rham 系数；Betti/ℓ-进版本需要额外的 Riemann–Hilbert 论证。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§5.2 de Rham 范畴化",
            "pages": [17, 18],
            "anchor": "源码/sections/s05-whittaker.tex:L192-L320（Theorem 5.2.8 与 Main Theorem 5.2.9）",
            "quote": "Main Theorem 5.2.9. ... LG is an equivalence."
        }
    ],
    "related": [
        "raskin_glc/concept/whittaker-coefficient",
        "raskin_glc/concept/hecke-eigensheaf"
    ],
    "rights": "rewritten",
    "status": "dev",
    "verification": {
        "status": "partial",
        "checked_on": "2026-11-27",
        "checks": [
            {
                "source": "nLab",
                "entry": "geometric Langlands correspondence",
                "url": "https://ncatlab.org/nlab/show/geometric+Langlands+correspondence",
                "last_revised": "",
                "asserts": "Idea 段明确写出粗版 $\\mathcal{O}Mod(Loc_{{}^L G}(\\Sigma))\\simeq\\mathcal{D}Mod(\\operatorname{Bun}_G(\\Sigma))$，并提到 Arinkin–Gaitsgory 的 Nilp 修正与 2025 年 Gaitsgory 等的证明；这直接支撑卡中「粗版需修正」的叙述。",
                "verdict": "supports"
            }
        ],
        "note": "nLab 页面支持粗版与 Nilp 修正的存在；主定理的精确陈述以原文与 GLC 系列为准。"
    }
})

CARDS.append({
    "id": "raskin_glc/correction/abel-jacobi-fiber",
    "type": "correction",
    "track": "B",
    "title": "Abel–Jacobi 纤维被写成 $\\Gamma(X,L)\\setminus\\{0\\}$",
    "aliases": ["AJ fiber erratum", "PΓ(X,L)"],
    "summary": "原文说 $\\mathrm{AJ}_d$ 在 $L$ 处的纤维是 $\\Gamma(X,L)\\setminus\\{0\\}$；正确者应为射影空间 $\\mathbb{P}\\Gamma(X,L)$。否则纤维维数多一维，且去掉原点的仿射空间不紧、讨论单连通性时结论不同。",
    "question": "为什么差一个 $\\mathbb{P}$ 会同时破坏维数公式与单连通性论证？",
    "location": "§1.2，原文 p.4（Deligne 构造的下降步骤）",
    "original": "The fiber of this map at $L$ is $\\Gamma(X,L)\\setminus 0$.",
    "corrected": "The fiber of this map at $L$ is $\\mathbb{P}\\Gamma(X,L)$.",
    "why": "当 $d>2g-2$ 时 $H^1(X,L)=0$，故 $h^0(L)=d+1-g$。$\\Gamma(X,L)\\setminus\\{0\\}$ 的维数是 $d+1-g$，而 $\\mathbb{P}\\Gamma(X,L)$ 的维数是 $d-g$；后者才与 $\\operatorname{Sym}^d X\\to\\operatorname{Jac}(X)$ 的纤维维数 $d-g$ 相符。此外 $\\Gamma(X,L)\\setminus\\{0\\}$ 是仿射空间去掉原点，不是紧的，也不是射影空间；讲义随后要用「纤维单连通」做下降，射影空间 $\\mathbb{P}^{d-g}$ 单连通，而 $\\mathbb{A}^{d+1-g}\\setminus\\{0\\}$ 在 $d-g\\ge 1$ 时同伦 $S^{2(d-g)-1}$，并不单连通。",
    "note": "此笔误不影响构造 1.2.4 的最终结论（下降仍可沿射影化纤维进行），但正文的「纤维」与「单连通」两句话必须按 $\\mathbb{P}\\Gamma$ 理解；译文正文照录原文并加译注。",
    "sources": [
        {
            "book": SRC,
            "section": "§1.2，构造 1.2.4",
            "pages": [4],
            "anchor": "源码/sections/s01-intro.tex:L145-L150（原文照录与译注）",
            "quote": "The fiber of this map at L is Γ(X,L) ∖ 0."
        }
    ],
    "related": [
        "raskin_glc/concept/deligne-gl1-construction"
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
                "asserts": "页面确认局部系统与平坦联络的对应，但不涉及 Abel–Jacobi 纤维的维数；本卡的更正依据是原文自身的维数计算与 $\\mathbb{P}\\Gamma$ 的标准事实。",
                "verdict": "not_applicable"
            }
        ],
        "note": "更正依据：$\\dim\\mathbb{P}\\Gamma(X,L)=d-g$ 与 $\\operatorname{Sym}^d X\\to\\operatorname{Jac}$ 的纤维维数一致；$\\mathbb{P}^N$ 单连通。"
    }
})

CARDS.append({
    "id": "raskin_glc/correction/perverse-lisse-swap",
    "type": "correction",
    "track": "B",
    "title": "$\\sigma^{(d)}$ 与 $\\mathcal{F}_\\sigma$ 的 perverse/lisse 性质被互换",
    "aliases": ["perverse-lisse erratum", "σ^(d) is perverse but not lisse"],
    "summary": "原文说 $\\sigma^{(d)}$ 是 perverse 但非 lisse；实际上 $\\sigma^{(d)}$ 是 $\\operatorname{Sym}^d X$ 上的秩 $1$ 局部系统，因而是 lisse；真正 perverse 但非 lisse 的是 $\\mathcal{F}_\\sigma$。",
    "question": "为什么把「perverse」与「lisse」对调会误导读者对目标 3.1.2 的理解？",
    "location": "§3.1，原文 p.9（$\\operatorname{coeff}_d$ 的升级段落）",
    "original": "However, $\\sigma^{(d)}$ is perverse but not lisse.",
    "corrected": "$\\sigma^{(d)}$ is lisse; $\\mathcal{F}_\\sigma$ is perverse but not lisse.",
    "why": "$\\sigma^{(d)}=(\\mathrm{add}_{d,*}\\sigma^{\\boxtimes d})^{S_d}$ 是 $\\operatorname{Sym}^d X$ 上的局部系统：$\\mathrm{add}_{d,*}$ 把局部系统推前为局部系统，取 $S_d$-不变量仍是局部系统，故 lisse。$\\mathcal{F}_\\sigma$ 是 $\\operatorname{Bun}_{\\mathrm{PGL}_2}$ 上的反常层，支撑在整个叠上（包括非半稳定部分），其奇异支撑非零，故 perverse 而非 lisse。",
    "note": "此句位于「$\\operatorname{coeff}_d(\\mathcal{F}_\\sigma)\\cong\\sigma^{(d)}$」之后，读者容易误以为 $\\operatorname{coeff}_d(\\mathcal{F}_\\sigma)$ 是 perverse 的；实际上它是 $\\operatorname{Sym}^d X$ 上的 lisse 层。译文照录原文并加译注。",
    "sources": [
        {
            "book": SRC,
            "section": "§3.1，$\\operatorname{coeff}_d$ 的升级",
            "pages": [9],
            "anchor": "源码/sections/s03-coeff.tex:L95-L110（原文照录与译注）",
            "quote": "However, σ^(d) is perverse but not lisse."
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
        "note": "更正依据是局部系统的定义与原文自身对 $\\mathcal{F}_\\sigma$ 的描述；无需外部页面。"
    }
})

CARDS.append({
    "id": "raskin_glc/remark/generic-rank-convention",
    "type": "remark",
    "track": "D",
    "title": "通用秩公式中的指数 $d_i$",
    "aliases": ["generic rank", "exponents of G", "∏ d_i^{(2d_i−1)(g−1)}"],
    "summary": "原文写通用秩为 $\\prod_i d_i^{(2d_i-1)(g-1)}$，称 $d_i$ 为 $G$ 的指数。按此约定，$\\mathrm{GL}_2$ 的指数为 $1,2$，公式给 $2^{3g-3}$；$\\mathrm{PGL}_2$ 的指数为 $1$，公式给 $1$，都与各自已知的通用秩一致。",
    "question": "$d_i$ 应如何代入：按 $G$ 的指数，还是按不变多项式的次数？",
    "statement": "对 $g>1$，定理 4.3.2 中 $\\mathcal{F}_\\sigma$ 的通用秩为 $\\prod_i d_i^{(2d_i-1)(g-1)}$，其中 $d_i$ 为 $G$ 的指数。",
    "why": "对 $G=\\mathrm{GL}_2$，指数为 $1,2$，故 $\\prod_i d_i^{(2d_i-1)(g-1)}=1^1\\cdot 2^{3(g-1)}=2^{3g-3}$，与已知的 $\\mathrm{GL}_2$ Hecke 特征层通用秩一致；对 $G=\\mathrm{PGL}_2$，指数为 $1$，公式给 $1$，也与其通用秩一致。若把 $d_i$ 读成不变多项式的次数（$\\mathrm{GL}_2$ 为 $2,3$），会得到不同数值，那不是原文的约定。",
    "note": "译文按「$G$ 的指数」解释并加脚注，不改原公式；读者不要把 $d_i$ 读成不变多项式次数。",
    "sources": [
        {
            "book": SRC,
            "section": "§4.3，定理 4.3.2 后的通用秩公式",
            "pages": [15],
            "anchor": "源码/sections/s04-hecke.tex 定理 4.3.2 后的通用秩公式与脚注 20",
            "quote": "For g > 1, the generic rank of F_σ is ∏_i d_i^{(2d_i−1)(g−1)}, where d_i's are the exponents of G."
        }
    ],
    "related": [
        "raskin_glc/concept/hecke-eigensheaf",
        "raskin_glc/concept/pgl2-geometric-langlands"
    ],
    "rights": "rewritten",
    "status": "dev",
    "verification": {
        "status": "source-only",
        "checked_on": "2026-11-27",
        "checks": [],
        "note": "据原文与译文脚注；未逐篇核外部文献对该公式的陈述，故只记原文约定与两个自洽校验。"
    }
})
