# -*- coding: utf-8 -*-
"""Raskin 讲义资料卡：第二组（PGL_2、Whittaker、Hecke 特征层、几何 Satake）。"""

SRC = "Sam Raskin 讲授、Lin Chen 笔记《Notes for \"Geometric Langlands for Projective Curves\"》（2025-07-07/11，18 页）"

CARDS = []

CARDS.append({
    "id": "raskin_glc/concept/pgl2-geometric-langlands",
    "type": "concept",
    "track": "B",
    "title": "$\\mathrm{PGL}_2$ 的几何 Langlands 对应",
    "aliases": ["PGL_2 eigensheaf", "Theorem 3.3.1", "Drinfeld–Laumon–FGV"],
    "summary": "对不可约 $\\mathrm{SL}_2$ 局部系统 $\\sigma$，存在 $\\operatorname{Bun}_{\\mathrm{PGL}_2}$ 上 perverse、尖点、在每个连通分支上不可约的 Hecke 特征层 $\\mathcal{F}_\\sigma$，其所有系数为 $\\operatorname{Sym}^n(\\sigma_x)$ 的张量积。",
    "question": "为什么 $\\mathcal{F}_\\sigma$ 不能是 lisse 层，而只能是 perverse 层？",
    "definition": {
        "text": "设 $\\sigma$ 为 $X$ 上不可约 $\\mathrm{SL}_2$-局部系统（秩 $2$，且 $\\wedge^2\\sigma$ 平凡化）。几何 Langlands 对应断言：存在 $\\mathcal{F}_\\sigma\\in\\operatorname{Shv}(\\operatorname{Bun}_{\\mathrm{PGL}_2})$，使得 $\\mathcal{F}_\\sigma$ 是 perverse 的、尖点的、在 $\\operatorname{Bun}^{\\mathrm{even}}$ 与 $\\operatorname{Bun}^{\\mathrm{odd}}$ 上分别不可约，并且对每个 $d\\ge 0$ 有 $\\operatorname{coeff}_d(\\mathcal{F}_\\sigma)\\cong\\sigma^{(d)}$；此外 $\\mathcal{F}_\\sigma$ 是 Hecke 特征层，即 $\\mathrm{H}_{\\mathrm{std}}(\\mathcal{F}_\\sigma)\\cong\\mathcal{F}_\\sigma\\boxtimes\\sigma$。",
        "notation": "$\\operatorname{Bun}_{\\mathrm{PGL}_2}$ 为秩 $2$ 向量丛模张量线丛；$\\operatorname{coeff}_d$ 取值在 $\\operatorname{Sym}^d X$ 上的层；$\\mathrm{H}_{\\mathrm{std}}$ 为标准表示对应的 Hecke 函子。"
    },
    "key_points": [
        "$\\operatorname{Bun}_{\\mathrm{PGL}_2}$ 不连通：$\\deg$ 给出到 $\\mathbb{Z}/2$ 的映射，分为 even 与 odd 两个连通分支；$\\mathcal{F}_\\sigma$ 在每个分支上各有一个不可约分量。",
        "$\\mathcal{F}_\\sigma$ 不是 lisse：它的奇异支撑非零，且支撑在整个 $\\operatorname{Bun}_{\\mathrm{PGL}_2}$ 上（包括非半稳定部分）；lisse 层做不到「尖点」——尖点性要求沿 $\\operatorname{Bun}_B$ 的常数项为零。",
        "Hecke 特征性质 $\\mathrm{H}_{\\mathrm{std}}(\\mathcal{F}_\\sigma)\\cong\\mathcal{F}_\\sigma\\boxtimes\\sigma$ 是「本征值」的准确含义：本征值不是一个标量，而是 $X$ 上的局部系统 $\\sigma$。",
        "系数 $\\operatorname{coeff}_d(\\mathcal{F}_\\sigma)\\cong\\sigma^{(d)}$ 是 Hecke 性质的逐个除子版本；对 $D=\\sum n_i x_i$ 展开即得 $\\bigotimes_i\\operatorname{Sym}^{n_i}(\\sigma_{x_i})$。",
        "唯一性由命题 3.1.4 给出：尖点、不可约、稠密支撑的 perverse 层由两个相邻系数 $\\operatorname{coeff}_d,\\operatorname{coeff}_{d+1}$（$d>N(g)$）唯一确定；但该断言只对 $\\mathrm{PGL}_2$ 特殊，不能推广到一般 $G$。"
    ],
    "formulas": [
        "\\mathrm{H}_{\\mathrm{std}}(\\mathcal{F}_\\sigma)\\cong\\mathcal{F}_\\sigma\\boxtimes\\sigma",
        "\\operatorname{coeff}_d(\\mathcal{F}_\\sigma)\\cong\\sigma^{(d)}",
        "\\operatorname{coeff}_D(\\mathcal{F}_\\sigma)\\cong\\bigotimes_i\\operatorname{Sym}^{n_i}(\\sigma_{x_i})",
        "\\deg:\\operatorname{Bun}_{\\mathrm{PGL}_2}\\to\\mathbb{Z}/2"
    ],
    "theorems": [
        {
            "name": "定理 3.3.1（Drinfeld, Laumon, Frenkel–Gaitsgory–Vilonen）",
            "statement": "对任意不可约 $\\mathrm{SL}_2$ 局部系统 $\\sigma$，存在 $\\mathcal{F}_\\sigma\\in\\operatorname{Shv}(\\operatorname{Bun}_{\\mathrm{PGL}_2})$，perverse 且在每连通分支不可约，满足 $\\operatorname{coeff}_d(\\mathcal{F}_\\sigma)\\cong\\sigma^{(d)}$ 与 Hecke 特征性质。",
            "proof": {
                "status": "cited",
                "gap_note": "讲义只述定理与证明思路（Fourier 反演 + 命题 3.1.4），完整证明见 Drinfeld, Laumon, Frenkel–Gaitsgory–Vilonen 的原始文献；第四讲的 $\\mathrm{PGL}_2$ 情形是它的特例。"
            },
            "source": "§3.3，原文 p.10–11"
        },
        {
            "name": "命题 3.1.4（唯一性）",
            "statement": "若 $\\mathcal{F}$ 为尖点 perverse 层、在 $\\operatorname{Bun}^{\\mathrm{even}/\\mathrm{odd}}$ 上不可约且支撑稠密，则 $\\mathcal{F}$ 由 $\\operatorname{coeff}_d(\\mathcal{F})$ 与 $\\operatorname{coeff}_{d+1}(\\mathcal{F})$（任意 $d>N(g)$）唯一确定。",
            "proof": {
                "status": "sketch",
                "gap_note": "证明用 Fourier 变换把问题化到 $E_d^\\vee\\setminus\\{0\\}$ 上的限制，再用 Fact 3.2.3/3.2.4 的拉回全忠实；细节见 §3.2。"
            },
            "source": "§3.1，原文 p.8–9"
        }
    ],
    "pitfalls": [
        "$\\sigma$ 是不可约 $\\mathrm{SL}_2$-局部系统，不是 $\\mathrm{PGL}_2$-局部系统：$\\mathrm{SL}_2$ 是 $\\mathrm{PGL}_2$ 的对偶群，$\\sigma$ 是「本征值」所在的一侧。",
        "$\\mathcal{F}_\\sigma$ 是 perverse，不是 lisse；原文 p.9 的「$\\sigma^{(d)}$ is perverse but not lisse」把主宾颠倒了（见勘误卡）。",
        "「在每个连通分支上不可约」不等于「整体不可约」：even 与 odd 两个分量可以同时存在，整体是二者的直和。",
        "命题 3.1.4 的唯一性只对 $\\mathrm{PGL}_2$ 成立；对一般 $G$，两个系数不足以确定层，讲义明确警告这一点。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§3.3 定理 3.3.1 与 §3.1 命题 3.1.4",
            "pages": [8, 9, 10, 11],
            "anchor": "源码/sections/s03-coeff.tex:L180-L260（Theorem 3.3.1）",
            "quote": "Theorem 3.3.1. ... there exists F_σ ∈ Shv(Bun_{PGL_2}), perverse and irreducible on each connected component, with coeff_d(F_σ) ≃ σ^(d)."
        }
    ],
    "related": [
        "raskin_glc/concept/cuspidal-sheaf",
        "raskin_glc/concept/coefficient-functor",
        "raskin_glc/concept/hecke-eigensheaf",
        "raskin_glc/correction/perverse-lisse-swap"
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
                "asserts": "Idea 段给出 $\\mathcal{O}Mod(Loc_{{}^L G}(\\Sigma))\\simeq\\mathcal{D}Mod(\\operatorname{Bun}_G(\\Sigma))$ 的粗版，并提到 Arinkin–Gaitsgory 的 Nilp 修正；这支撑「特征层对应局部系统」的大框架，但页面不涉及 $\\mathrm{PGL}_2$ 的尖点性与 $\\operatorname{coeff}_d$。",
                "verdict": "partial"
            }
        ],
        "note": "定理本身以原文与 Drinfeld–Laumon–FGV 为准；nLab 只支撑大框架。"
    }
})

CARDS.append({
    "id": "raskin_glc/concept/whittaker-coefficient",
    "type": "concept",
    "track": "E",
    "title": "Whittaker 系数与几何 Casselman–Shalika",
    "aliases": ["Whittaker coefficient", "coeff_D for general G", "geometric Casselman–Shalika"],
    "summary": "用 $\\operatorname{Bun}^{\\Omega}_N\\to\\mathbb{A}^1$ 与 $\\exp$ 层定义 $\\operatorname{coeff}_D$；FGV 的几何 Casselman–Shalika 定理把它写成「先做 Hecke 作用、再取 $\\operatorname{coeff}_0$」。",
    "question": "为什么一般约化群的 Whittaker 系数必须经过 $\\check\\rho(\\Omega)$ 的扭化，而不能直接用在 $\\operatorname{Bun}_B$ 上？",
    "definition": {
        "text": "设 $G$ 为分裂约化群，$N\\subset G$ 为极大单幂子群，$T$ 为极大环面。令 $\\check\\rho(\\Omega):=2\\check\\rho(\\Omega^{1/2})$（固定 $\\Omega$ 的平方根），并定义 $\\operatorname{Bun}^{\\Omega}_N:=\\operatorname{Bun}_B\\times_{\\operatorname{Bun}_T}\\{\\check\\rho(\\Omega)\\}$。对每个正单根 $\\alpha_i$，$N\\to\\mathbb{G}_a$ 诱导 $\\varphi_i:\\operatorname{Bun}^{\\Omega}_N\\to\\operatorname{Bun}^{\\Omega}_{\\mathbb{G}_a}\\to H^1(X,\\Omega)\\cong\\mathbb{A}^1$，令 $\\varphi:=\\sum_i\\alpha_i\\varphi_i$。定义 $\\operatorname{coeff}_0(\\mathcal{F}):=\\mathbb{C}\\cdot(\\operatorname{Bun}^{\\Omega}_N,p_N^!\\mathcal{F}\\otimes^!\\varphi^!\\exp)$。对 $D=\\sum_i\\check\\lambda_i x_i$（$\\lambda_i\\in\\check\\Lambda^+$），把 $\\check\\rho(\\Omega)$ 换成 $\\check\\rho(\\Omega)(-D)$ 即得 $\\operatorname{coeff}_D$。",
        "notation": "$\\check\\Lambda^+$ 为支配权；$\\check\\rho$ 为 Weyl 向量；$\\Omega^{1/2}$ 为固定平方根；$p_N:\\operatorname{Bun}_B\\to\\operatorname{Bun}_G$。"
    },
    "key_points": [
        "$\\operatorname{Bun}^{\\Omega}_N$ 不是 $\\operatorname{Bun}_B$ 本身：它把 $T$-丛扭到 $\\check\\rho(\\Omega)$，使每个正单根方向的 $\\mathbb{G}_a$-扩张有正确的「中心荷」，从而 $\\varphi$ 是良定义的。",
        "对 $G=\\mathbb{G}_m$，$\\operatorname{Bun}^{\\Omega}_N$ 退化为一点，$\\operatorname{coeff}_D$ 就是线丛 $\\mathcal{O}(-D)$ 处的 $!$-纤维；这是「Whittaker 系数」最简单的例子。",
        "对 $G=\\mathrm{PGL}_2$，$\\check\\rho(\\Omega)=\\Omega$，$\\operatorname{Bun}^{\\Omega}_N=\\operatorname{Bun}^{\\Omega(-D)}_N$，于是回到第三讲的 $\\operatorname{coeff}_D$（例 5.1.3）。",
        "几何 Casselman–Shalika（定理 5.1.4）：$\\operatorname{coeff}_D(\\mathcal{F})\\cong\\operatorname{coeff}_0(\\mathrm{H}_{\\boxtimes V_{\\check\\lambda_i},x}(\\mathcal{F}))$；即「取第 $D$ 个 Whittaker 系数」等于「先沿 $D$ 做 Hecke 作用，再取常数项」。",
        "对 Hecke 特征层 $\\mathcal{F}_\\sigma$，$\\mathrm{H}_{\\boxtimes V_{\\check\\lambda_i},x}(\\mathcal{F}_\\sigma)\\cong\\mathcal{F}_\\sigma\\otimes\\bigotimes_i(V_{\\check\\lambda_i,\\sigma})_{x_i}$，故 $\\operatorname{coeff}_D(\\mathcal{F}_\\sigma)\\cong\\bigotimes_i(V_{\\check\\lambda_i,\\sigma})_{x_i}$，回到 Goal 3.1.2 的一般 $G$ 版本。"
    ],
    "formulas": [
        "\\operatorname{coeff}_0(\\mathcal{F})=\\mathbb{C}\\cdot\\left(\\operatorname{Bun}^{\\Omega}_N,p_N^!\\mathcal{F}\\otimes^!\\varphi^!\\exp\\right)",
        "\\operatorname{Bun}^{\\Omega}_N:=\\operatorname{Bun}_B\\times_{\\operatorname{Bun}_T}\\{\\check\\rho(\\Omega)\\}",
        "\\operatorname{coeff}_D(\\mathcal{F})\\cong\\operatorname{coeff}_0(\\mathrm{H}_{\\boxtimes V_{\\check\\lambda_i},x}(\\mathcal{F}))",
        "\\operatorname{coeff}_D(\\mathcal{F}_\\sigma)\\cong\\bigotimes_i(V_{\\check\\lambda_i,\\sigma})_{x_i}"
    ],
    "theorems": [
        {
            "name": "定义 5.1.1（Whittaker 系数函子）",
            "statement": "上述 $\\operatorname{coeff}_D:\\operatorname{Shv}(\\operatorname{Bun}_G)\\to\\operatorname{Vect}$ 对每个 $D=\\sum\\check\\lambda_i x_i$ 有定义，称为 Whittaker 系数函子。",
            "proof": {"status": "none", "gap_note": "定义。"},
            "source": "§5.1，原文 p.16"
        },
        {
            "name": "定理 5.1.4（Frenkel–Gaitsgory–Vilonen，几何 Casselman–Shalika）",
            "statement": "对 $D=\\sum\\check\\lambda_i x_i$（$\\lambda_i\\in\\check\\Lambda^+$）与 $\\mathcal{F}\\in\\operatorname{Shv}(\\operatorname{Bun}_G)$，有 $\\operatorname{coeff}_D(\\mathcal{F})\\cong\\operatorname{coeff}_0(\\mathrm{H}_{\\boxtimes_i V_{\\check\\lambda_i},x}(\\mathcal{F}))$。",
            "proof": {
                "status": "cited",
                "gap_note": "讲义只述定理；证明见 Frenkel–Gaitsgory–Vilonen 的原始论文与 Ngo–Polo 的几何 Casselman–Shalika 表述。"
            },
            "source": "§5.1，原文 p.16"
        },
        {
            "name": "定理 5.1.7（Beraldo, FGV）",
            "statement": "当 $G=\\mathrm{GL}_n$ 或 $\\mathrm{PGL}_n$ 时，$\\operatorname{coeff}^{\\mathrm{ult}}$ 在尖点子范畴 $\\operatorname{Shv}(\\operatorname{Bun}_G)_{\\mathrm{cusp}}$ 上全忠实。",
            "proof": {
                "status": "cited",
                "gap_note": "$\\mathrm{PGL}_2$ 的证明模仿 Fourier 反演，$\\mathrm{GL}_n$ 的证明模仿 Piatetski–Shapiro–Shalika；讲义未展开。"
            },
            "source": "§5.1，原文 p.17"
        }
    ],
    "pitfalls": [
        "$\\check\\rho(\\Omega)$ 不是 $\\Omega$：对 $\\mathrm{PGL}_2$ 恰好相等，但对一般 $G$ 差一个 Weyl 向量；写成 $\\Omega$ 会丢掉单根方向的权重。",
        "$\\Omega^{1/2}$ 必须预先固定；换一个平方根会把 $\\operatorname{coeff}_D$ 整体乘以一个符号/二次特征。",
        "$D$ 的系数 $\\check\\lambda_i$ 取在支配权 $\\check\\Lambda^+$ 中，不是任意整数；这对应「最高权表示」的 Hecke 作用。",
        "$\\operatorname{coeff}_D$ 的取值是向量空间；$\\operatorname{coeff}^{\\mathrm{ult}}$ 才是取值在 $\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}$ 中的「终极」版本。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§5.1 Whittaker 系数",
            "pages": [16, 17],
            "anchor": "源码/sections/s05-whittaker.tex:L38-L100（Definition 5.1.1 与 Theorem 5.1.4）",
            "quote": "Definition 5.1.1. ... coeff_D(F) := C · (Bun^Ω_N, p_N^!(F) ⊗^! φ^!(exp))."
        }
    ],
    "related": [
        "raskin_glc/concept/coefficient-functor",
        "raskin_glc/concept/hecke-eigensheaf",
        "raskin_glc/concept/categorical-geometric-langlands"
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
                "asserts": "页面提到几何 Langlands 的 Hecke 特征层框架，但未涉及 Whittaker 系数或几何 Casselman–Shalika；只能作为大背景。",
                "verdict": "partial"
            }
        ],
        "note": "Whittaker 系数的定义与 FGV 定理以原文为准；nLab 无对应条目。"
    }
})

CARDS.append({
    "id": "raskin_glc/concept/hecke-eigensheaf",
    "type": "concept",
    "track": "D",
    "title": "Hecke 特征层",
    "aliases": ["Hecke eigensheaf", "eigenvalue local system", "Definition 4.2.2"],
    "summary": "以 $\\sigma$ 为特征值的 Hecke 特征层是 $\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}$-线性函子 $\\operatorname{Vect}\\to\\operatorname{Shv}(\\operatorname{Bun}_G)$，等价于对所有 $V$ 有 $\\mathrm{H}_V(\\mathcal{F})\\cong\\mathcal{F}\\boxtimes V_\\sigma$；2024 年定理给出存在性、半单性与特征圈。",
    "question": "为什么「对所有 $V$ 的 Hecke 作用」比单个 $\\mathrm{H}_{\\mathrm{std}}$ 的等式更强？",
    "definition": {
        "text": "固定 $\\check G$-局部系统 $\\sigma$。定义求值函子 $\\mathrm{ev}_\\sigma:\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}\\to\\operatorname{Vect}$：在 $\\operatorname{Rep}(\\check G)^{\\otimes I}\\otimes\\operatorname{Shv}(X^I)$ 上，它把 $\\boxtimes_i V_i\\otimes\\delta_{x_i}$ 送到 $\\bigotimes_i (V_i)_\\sigma|_{x_i}$，再取整体截面。称 $\\mathcal{F}\\in\\operatorname{Shv}(\\operatorname{Bun}_G)$ 为以 $\\sigma$ 为特征值的 Hecke 特征层，若存在 $\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}$-线性函子 $\\Phi:\\operatorname{Vect}\\to\\operatorname{Shv}(\\operatorname{Bun}_G)$，$\\underline{\\e}\\mapsto\\mathcal{F}$，使 $\\Phi$ 与 $\\mathrm{ev}_\\sigma$ 相容；等价地，对所有 $V$ 有 $\\mathrm{H}_V(\\mathcal{F})\\cong\\mathcal{F}\\boxtimes V_\\sigma$。",
        "notation": "$\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}$ 为 Ran 空间上的 colimit 范畴；$\\mathrm{H}_V$ 为 Hecke 函子；$V_\\sigma$ 为 $\\sigma$ 诱导的 $X$ 上局部系统。"
    },
    "key_points": [
        "本征值不是标量而是局部系统：$\\mathrm{H}_V(\\mathcal{F})\\cong\\mathcal{F}\\boxtimes V_\\sigma$ 中的 $V_\\sigma$ 是 $X$ 上的 lisse 层，随 $V\\in\\operatorname{Rep}(\\check G)$ 函子性变化。",
        "$\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}$ 把「在所有点 $x\\in X$ 同时做 Hecke 作用」的相容数据粘成一个范畴；Hecke 特征层是这个范畴在 $\\operatorname{Shv}(\\operatorname{Bun}_G)$ 上的一个表示。",
        "等价性 $\\mathrm{H}_V(\\mathcal{F})\\cong\\mathcal{F}\\boxtimes V_\\sigma$（练习 4.2.4）说明：只要对所有 $V$ 验证，就得到整个 Ran 范畴的线性性。",
        "定理 4.3.2（2024，Arinkin–Beraldo–Campbell–Chen–Faergeman–Gaitsgory–Lin–Raskin–Rozenblyum）：对不可约 $\\sigma$（不来自真抛物），存在唯一 Hecke 特征层 $\\mathcal{F}_\\sigma$，且它 perverse、尖点、半单；其分量按 $\\operatorname{Aut}(\\sigma)$ 的不可约表示编号。",
        "特征圈为 $[\\mathrm{Nilp}]$：$\\mathcal{F}_\\sigma$ 的奇异支撑包含在整个幂零锥 $\\mathrm{Nilp}\\subset T^*\\operatorname{Bun}_G$ 中，这是 2024 年定理最精细的部分之一。"
    ],
    "formulas": [
        "\\mathrm{H}_V(\\mathcal{F})\\cong\\mathcal{F}\\boxtimes V_\\sigma",
        "\\mathcal{F}_\\sigma\\cong\\bigoplus_{\\rho\\in\\operatorname{Irr}\\operatorname{Aut}(\\sigma)}\\mathcal{F}_{\\sigma,\\rho}^{\\oplus\\dim\\rho}",
        "\\operatorname{coeff}_0(\\mathcal{F}_\\sigma)\\cong\\underline{\\e}"
    ],
    "theorems": [
        {
            "name": "定义 4.2.2（Hecke 特征层）",
            "statement": "上述 $\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}$-线性函子 $\\Phi$（或等价地，对所有 $V$ 的等式 $\\mathrm{H}_V(\\mathcal{F})\\cong\\mathcal{F}\\boxtimes V_\\sigma$）定义以 $\\sigma$ 为特征值的 Hecke 特征层。",
            "proof": {"status": "none", "gap_note": "定义；练习 4.2.3 说明 $\\sigma$ 由 $\\mathrm{ev}_\\sigma$ 唯一确定。"},
            "source": "§4.2，原文 p.14"
        },
        {
            "name": "练习 4.2.4",
            "statement": "$\\mathcal{F}$ 为以 $\\sigma$ 为特征值的 Hecke 特征层，当且仅当对所有 $V\\in\\operatorname{Rep}(\\check G)$ 有 $\\mathrm{H}_V(\\mathcal{F})\\cong\\mathcal{F}\\boxtimes V_\\sigma$。",
            "proof": {"status": "none", "gap_note": "练习；由 Ran 范畴的泛性质与 $\\mathrm{ev}_\\sigma$ 的定义展开。"},
            "source": "§4.2，原文 p.14"
        },
        {
            "name": "猜想 4.3.1",
            "statement": "若 $\\sigma$ 为不可约 $\\check G$-局部系统（不来自真抛物），则存在唯一 Hecke 特征层 $\\mathcal{F}_\\sigma$，且 $\\operatorname{coeff}_0(\\mathcal{F}_\\sigma)\\cong\\underline{\\e}$。",
            "proof": {"status": "none", "gap_note": "猜想；定理 4.3.2 在 char $k=0$ 时证明。"},
            "source": "§4.3，原文 p.14"
        },
        {
            "name": "定理 4.3.2（2024）",
            "statement": "设 char $k=0$，$\\sigma$ 不可约且不来自真抛物。则存在唯一 Hecke 特征层 $\\mathcal{F}_\\sigma$，它 perverse、尖点、半单；$\\mathcal{F}_\\sigma\\cong\\bigoplus_{\\rho}\\mathcal{F}_{\\sigma,\\rho}^{\\oplus\\dim\\rho}$，其中 $\\mathcal{F}_{\\sigma,\\rho}$ 为单 perverse 层；特征圈为 $[\\mathrm{Nilp}]$。",
            "proof": {
                "status": "cited",
                "gap_note": "2024 年几何 Langlands 证明的产物；讲义只列结论与作者名单，证明见 GLC I–V 系列（arXiv:2405.03599 等）。"
            },
            "source": "§4.3，原文 p.14–15"
        }
    ],
    "pitfalls": [
        "本征值是局部系统 $\\sigma$，不是标量；把 $V_\\sigma$ 写成 $\\dim V$ 会丢掉 $\\sigma$ 的全部信息。",
        "$\\operatorname{Rep}(\\check G)$ 不是 $\\operatorname{Rep}(G)$：原文 p.12 的 $\\operatorname{Rep}(G)\\to\\operatorname{Shv}(X)$ 是笔误，对偶群才作用在 Hecke 侧（见疑点 Q14）。",
        "$\\mathcal{F}_\\sigma$ 一般不是 lisse；它是 perverse，奇异支撑非零。",
        "归一化 $\\operatorname{coeff}_0(\\mathcal{F}_\\sigma)\\cong\\underline{\\e}$ 是猜想/定理的一部分；缺了它，$\\mathcal{F}_\\sigma$ 可乘以任意非零标量。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§4.2 Hecke 性质与 §4.3 定理",
            "pages": [14, 15],
            "anchor": "源码/sections/s04-hecke.tex:L203-L300（Definition 4.2.2 与 Theorem 4.3.2）",
            "quote": "Definition 4.2.2. ... a Hecke eigensheaf with eigenvalue σ is a Rep(Ĝ)_Ran-linear functor Vect → Shv(Bun_G)."
        }
    ],
    "related": [
        "raskin_glc/concept/geometric-satake",
        "raskin_glc/concept/pgl2-geometric-langlands",
        "raskin_glc/concept/categorical-geometric-langlands",
        "raskin_glc/remark/generic-rank-convention"
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
                "asserts": "页面给出粗版等价 $\\mathcal{O}Mod(Loc_{{}^L G})\\simeq\\mathcal{D}Mod(\\operatorname{Bun}_G)$ 与 2025 年证明的提及，支撑「存在 Hecke 特征层」的大方向；不涉及 $\\operatorname{Rep}(\\check G)_{\\mathrm{Ran}}$ 的精确定义。",
                "verdict": "partial"
            }
        ],
        "note": "定义与 2024 年定理的陈述以原文为准；nLab 只支撑背景。"
    }
})

CARDS.append({
    "id": "raskin_glc/concept/geometric-satake",
    "type": "concept",
    "track": "D",
    "title": "几何 Satake 等价",
    "aliases": ["geometric Satake", "Satake equivalence", "Theorem 4.1.2"],
    "summary": "局部 Hecke 叠 $L^+G\\backslash LG/L^+G$ 上的反常层范畴与 $\\operatorname{Rep}(\\check G)$ 等价，$V\\mapsto\\mathcal{S}_V$；整体 Hecke 函子 $\\mathrm{H}_V$ 用它定义。",
    "question": "为什么几何 Satake 的卷积积对应 $\\operatorname{Rep}(\\check G)$ 的张量积，而不是某种更大的结构？",
    "definition": {
        "text": "设 $x\\in X$，$L_xG=G(k((t_x)))$，$L^+_xG=G(k[[t_x]])$。局部 Hecke 叠为 $\\operatorname{Hecke}^{\\mathrm{loc}}_x:=L^+_xG\\backslash L_xG/L^+_xG$，它分类 $D_x=\\operatorname{Spec} k[[t_x]]$ 上两个 $G$-丛及其在 $D_x^\\circ$ 上的同构。几何 Satake 等价断言：存在典范幺半函子 $\\operatorname{Rep}(\\check G)\\to\\operatorname{Shv}(\\operatorname{Hecke}^{\\mathrm{loc}}_x)$，$V\\mapsto\\mathcal{S}_V$，它是范畴等价（到适当的反常层子范畴）。",
        "notation": "$L_xG$ 为圈群；$L^+_xG$ 为正圈群；$\\operatorname{Hecke}^{\\mathrm{loc}}_x$ 为局部 Hecke 叠；$\\mathcal{S}_V$ 为 $V$ 对应的 Satake 层。"
    },
    "key_points": [
        "几何 Satake 是「局部」陈述：只依赖 $x$ 处的形式圆盘 $D_x$，不依赖整体曲线 $X$；因此 $\\mathcal{S}_V$ 与 $t_x$ 的选取无关（原文 Remark）。",
        "整体 Hecke 函子 $\\mathrm{H}_{V,x}(\\mathcal{F}):=\\overrightarrow{h}_*(\\overleftarrow{h}^!\\mathcal{F}\\otimes^!\\pi^!\\mathcal{S}_V)$ 把局部 Satake 层 $\\mathcal{S}_V$ 沿整体 Hecke 对应拉回，得到 $\\operatorname{Bun}_G\\times X$ 上的层。",
        "卷积积对应张量积：$\\mathrm{H}_{V_1,x}\\circ\\mathrm{H}_{V_2,x}\\cong\\mathrm{H}_{V_1\\otimes V_2,x}$（练习 4.1.6），这正是 Satake 幺半性的整体体现。",
        "对 $G=\\mathrm{PGL}_2$，$\\check G=\\mathrm{SL}_2$，$V=\\mathrm{std}$ 时 $\\mathrm{H}_{\\mathrm{std}}$ 回到 §3.3 的 Hecke 作用（练习 4.1.5）。",
        "几何 Satake 的证明用仿射 Grassmann 簇的卷积与 perverse 层的 Beilinson–Drinfeld–Gaitsgory 分解；它不是本文的证明目标，而是作为黑箱引用。"
    ],
    "formulas": [
        "\\operatorname{Rep}(\\check G)\\simeq\\operatorname{Shv}(L^+_xG\\backslash L_xG/L^+_xG)",
        "\\mathrm{H}_{V,x}(\\mathcal{F}):=\\overrightarrow{h}_*\\left(\\overleftarrow{h}^!\\mathcal{F}\\otimes^!\\pi^!\\mathcal{S}_V\\right)",
        "\\mathrm{H}_{V_1,x}\\circ\\mathrm{H}_{V_2,x}\\cong\\mathrm{H}_{V_1\\otimes V_2,x}"
    ],
    "theorems": [
        {
            "name": "定理 4.1.2（几何 Satake）",
            "statement": "存在典范幺半函子 $\\operatorname{Rep}(\\check G)\\to\\operatorname{Shv}(\\operatorname{Hecke}^{\\mathrm{loc}}_x)$，$V\\mapsto\\mathcal{S}_V$，且它是范畴等价。",
            "proof": {
                "status": "cited",
                "gap_note": "归功于 Mirković–Vilonen（以及 Beilinson–Drinfeld 的框架）；讲义只引用，不证明。"
            },
            "source": "§4.1，原文 p.12"
        },
        {
            "name": "练习 4.1.5 / 4.1.6",
            "statement": "(4.1.5) 对 $G=\\mathrm{PGL}_2$、$\\check G=\\mathrm{SL}_2$、$V=\\mathrm{std}$，$\\mathrm{H}_{\\mathrm{std}}$ 与 §3.3 的 Hecke 作用一致；(4.1.6) $\\mathrm{H}_{V_1,x}\\circ\\mathrm{H}_{V_2,x}\\cong\\mathrm{H}_{V_1\\otimes V_2,x}$。",
            "proof": {"status": "none", "gap_note": "练习；按定义与 Satake 幺半性展开。"},
            "source": "§4.1，原文 p.13"
        }
    ],
    "pitfalls": [
        "局部 Hecke 叠 $L^+G\\backslash LG/L^+G$ 不是整体 $\\operatorname{Bun}_G$ 的 Hecke 叠；前者只记录一个点的形式数据，后者记录整条曲线上的修改。",
        "$\\mathcal{S}_V$ 是 Hecke 叠上的层，$V_\\sigma$ 是 $X$ 上的局部系统，二者不能混：前者是「核」，后者是「本征值」。",
        "$L^+_xG=G(k[[t_x]])$ 依赖 $x$ 的局部参数 $t_x$；Satake 层 $\\mathcal{S}_V$ 不依赖 $t_x$ 的选取，但 $H_{V,x}$ 的定义里出现了 $\\pi^!\\mathcal{S}_V$，需把 $\\mathcal{S}_V$ 沿 $\\pi$ 拉回。",
        "几何 Satake 是等价，不是仅仅「有函子」；忘记全忠实/本质满射会把 Hecke 特征层的分类问题看轻。"
    ],
    "sources": [
        {
            "book": SRC,
            "section": "§4.1 几何 Satake 与 Hecke 函子",
            "pages": [12, 13],
            "anchor": "源码/sections/s04-hecke.tex:L48-L110（Theorem 4.1.2 与 Definition 4.1.4）",
            "quote": "Theorem 4.1.2 (Geometric Satake). ... Rep(Ĝ) → Shv(L^+_xG \\ L_xG / L^+_xG), V ↦ S_V."
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
        "note": "未抓取 nLab 的 geometric Satake 条目正文，故不写外部核验；定理以原文 §4.1 与 Mirković–Vilonen 为准。"
    }
})
