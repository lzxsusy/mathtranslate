#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cards_b.py —— B 轨 5 张 + B 轨推导 1 张。"""
from gen_cards import CARDS, card, src, write_cards

B = {}

B["concepts/modular-form-classical"] = card(
    "concepts", "modular-form-classical",
    title="经典模形式",
    aliases=["modular form", "模形式", "尖点形式", "$\\SL(2,\\bbZ)$"],
    track="B",
    summary="$\\SL(2,\\bbZ)$ 的权 $k$ 模形式是上半平面上的全纯函数，在 $\\SL(2,\\bbZ)$ 作用下按 $k$ 次自守因子变换；尖点形式是其中在尖点处取零的那些。",
    question="模形式与猜想右侧有什么关系，为什么偏偏是 $\\SL(2,\\bbZ)$ 的权 $k$ 形式？",
    definition={
        "text": "设 $f\\colon\\he\\to\\bbC$ 全纯，$\\gamma=\\binom{a\\ b}{c\\ d}\\in\\SL(2,\\bbZ)$。称 $f$ 为权 $k$ 模形式，若 $f\\bigl(\\frac{az+b}{cz+d}\\bigr)=(cz+d)^k f(z)$ 对一切 $\\gamma$ 成立，且在尖点处具有适当的增长条件（$f$ 的 Fourier 展开只有非负指数项）。若进一步在尖点处取零（只有正指数项），称 $f$ 为尖点形式；尖点形式构成空间 $S_k$。",
        "notation": "$\\he=\\{z:\\Im z>0\\}$ 上半平面；$q=e^{2\\pi iz}$；$f=\\sum_{n\\ge0}a_nq^n$ 为 Fourier 展开。",
    },
    key_points=[
        "自守因子 $(cz+d)^k$ 的作用是让 $f(z)(dz)^{k/2}$ 在 $\\SL(2,\\bbZ)$ 下不变；这是几何上「权」的来源，不是随手加的。",
        "「在尖点处取零」这个条件正是「尖点」一词的来源，也是右端要求 cuspidal 的古典原型。",
        "模形式空间 $M_k$ 有限维；$\\dim S_k$ 由 Riemann–Roch 给出，这使「Hecke 特征值」成为一族离散的数据。",
        "$q$ 展开把一个函数变成一串系数 $(a_1,a_2,\\dots)$，Hecke 算子作用在这串系数上——这就是右侧「数据」的具体形态。",
    ],
    formulas=[
        "$f\\bigl(\\tfrac{az+b}{cz+d}\\bigr)=(cz+d)^k f(z)$，$\\binom{a\\ b}{c\\ d}\\in\\SL(2,\\bbZ)$",
        "$f(z)=\\sum_{n\\ge 0}a_nq^n$，$q=e^{2\\pi iz}$；$f\\in S_k\\iff a_0=0$",
    ],
    theorems=[
        {
            "name": "有限维性（古典）",
            "statement": "$M_k(\\SL(2,\\bbZ))$ 有限维，$S_k$ 是其子空间；当 $k<0$ 或 $k$ 为奇数时 $M_k=0$。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "把模形式看成 $\\SL(2,\\bbZ)\\backslash\\he$ 上加性条件的截面。", "why": "这把它变成紧化曲线上的截面问题。"},
                    {"no": 2, "text": "用 Riemann–Roch 数截面的维数。", "why": "有限维性由此而来。"},
                ],
                "gap_note": "原文没有证明，只说「众所周知」；完整证明见 [Sh1] 或 [K]。",
            },
            "source": "A p.8",
        },
    ],
    pitfalls=[
        "权 $k$ 与自守因子指数必须统一：有的书写 $f(\\gamma z)=(cz+d)^kf(z)$，有的书把 $k$ 换成 $2k$，对照文献时要先确认约定。",
        "模形式与自守形式不是同义词：前者是 $\\SL(2,\\bbZ)$ 的古典对象，后者是平代环上的对象；两者通过 (6.1.1) 等同，但不是定义上相同。",
    ],
    related=["goresky04/concept/hecke-operator", "goresky04/deriv/adelic-equivalence", "goresky04/concept/eichler-shimura-theorem"],
    sources=[src([7, 9], "A p.8", "§5.1–§5.3")],
    provenance_note="对应原文 §5.1–§5.2；有限维性一条原文只作背景提了一句，本卡按 [Sh1][K] 的通行说法补齐。",
)

B["concepts/hecke-operator"] = card(
    "concepts", "hecke-operator",
    title="Hecke 对应与 Hecke 算子",
    aliases=["Hecke operator", "Hecke 算子", "Hecke 对应", "$T_g$"],
    track="B",
    summary="每个 $g\\in\\GL(2,\\bbQ)$ 给出一个双陪集 $\\Gamma g\\Gamma$，它定义模曲线之间的对应，作用在函数上就是 Hecke 算子 $T_g=s_*t^*$。",
    question="Hecke 算子是怎么从「一个矩阵」变成一个「作用在模形式上的算子」的？",
    definition={
        "text": "记 $\\Gamma=\\SL(2,\\bbZ)$，$g\\in\\GL(2,\\bbQ)$，$\\Gamma'=\\Gamma\\cap g\\Gamma g^{-1}$。有两个自然映射 $s\\colon\\Gamma'\\backslash\\he\\to(g\\Gamma g^{-1})\\backslash\\he$ 与 $t\\colon\\Gamma'\\backslash\\he\\to\\Gamma\\backslash\\he$，它们都是有限覆叠和谐同态，于是 $X'\\to X\\times X$ 给出一个对应。这个对应只依赖双陪集 $\\Gamma g\\Gamma$。它作用在函数上为 $T_g(f)=s_*t^*f$；在模曲线上则是「把 $X'$ 的像推回去」，是多值映射的像。",
        "notation": "$T_g$ 记 Hecke 算子；对 $g=\\mathrm{diag}(p,1)$ 记 $T_p$；$s_*$ 为沿 $s$ 的推前（对覆叠取迹）。",
    },
    key_points=[
        "Hecke 算子不是「函数的线性变换」这么简单：它由对应给出，$s_*$ 里带着「有限覆叠的迹」，这一步是它成为自伴算子的原因。",
        "对应只依赖双陪集：同一个双陪集里的不同 $g$ 给出同一个算子，这就是为什么 Hecke 代数以双陪集为基。",
        "$T_p$ 的几何含义是「$p$ 阶子群」：在模曲线分类椭圆曲线的意味下，$T_p$ 是把 $E$ 送到它的 $p$ 个 $p$ 阶子商的对应。",
    ],
    formulas=[
        "$T_g(f)=s_*t^*f$  (5.4.1)",
        "$\\Gamma'=\\Gamma\\cap g\\Gamma g^{-1}$，$[\\Gamma:\\Gamma']<\\infty$",
    ],
    theorems=[
        {
            "name": "$T_g$ 的函子性",
            "statement": "$T_g$ 只依赖双陪集 $\\Gamma g\\Gamma$；当 $g,h$ 的阶互素时 $T_gT_h=T_{gh}$。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "若 $g'=\\gamma_1g\\gamma_2$，用 $\\gamma_1,\\gamma_2\\in\\Gamma$ 的不变性把 $X'$ 与 $s,t$ 重写。", "why": "说明对应只看到双陪集。"},
                    {"no": 2, "text": "两个对应复合，得到 $\\Gamma'\\backslash\\he\\to X\\times X$ 的三重纤维积。", "why": "复合对应即纤维积。"},
                    {"no": 3, "text": "在 $g,h$ 阶互素时纤维积退化为单个双陪集，故乘积等于 $T_{gh}$。", "why": "得到 Hecke 代数的乘法表。"},
                ],
                "gap_note": "原文给出定义与「只依赖双陪集」一句，乘法表没有展开；本卡步 2–3 是译者按通行证明补的。",
            },
            "source": "A p.8",
        },
    ],
    pitfalls=[
        "推前 $s_*$ 在覆叠次数不为 1 时不是「直接前推」，要按纤维求和；漏掉这一点会把 $T_p$ 算错。",
        "$T_g$ 与 $T_{g^{-1}}$ 一般不相等，尽管它们是伴随；「自伴」只在配上 Petersson 内积之后成立。",
    ],
    related=["goresky04/concept/modular-form-classical", "goresky04/concept/hecke-eigenform", "goresky04/concept/satake-parameter"],
    sources=[src([8, 9], "A p.8", "§5.4")],
    provenance_note="对应原文 §5.4 的 (5.4.1) 与对应图；乘法表一条原文未证，按通行说法补齐。",
)

B["concepts/hecke-eigenform"] = card(
    "concepts", "hecke-eigenform",
    title="Hecke 特征形式与 Fourier 系数",
    aliases=["Hecke eigenform", "Hecke 特征形式", "特征值", "$\\lambda_p$"],
    track="B",
    summary="若一个尖点形式是所有 $T_p$ 的共同特征向量，则它的 Fourier 系数 $a_n$ 与特征值 $\\lambda_n$ 满足 $a_n=\\lambda_n a_1$；于是「Hecke 特征值」就成了一串可比较的数。",
    question="为什么 Hecke 特征值可以等同于 Fourier 系数，这一步在猜想里起什么作用？",
    definition={
        "text": "设 $f=\\sum a_nq^n\\in S_k$ 满足 $T_pf=\\lambda_pf$ 对一切素数 $p$ 成立（这样的 $f$ 称 Hecke 特征形式）。由 $T_p$ 在 $q$ 展开上的显式作用可以算出 $a_p=\\lambda_pa_1$；归一化 $a_1=1$ 后得 $a_p=\\lambda_p$。更一般地 $a_n=\\lambda_n$，其中 $\\lambda_n$ 是复合算子 $T_n$ 的特征值。Hecke 代数 $\\bbT$ 由这些 $T_n$ 生成，特征形式给出 $\\bbT\\to\\bbC$ 的特征。",
        "notation": "$\\lambda_p$ 记 $T_p$ 的特征值；$\\bbT$ 记 Hecke 代数；归一化特征形式指 $a_1=1$ 的那一个。",
    },
    key_points=[
        "「$a_p=\\lambda_p$」是整篇文章的枢纽：它把分析侧（算子的特征值）翻译成算术侧（一串整数或代数数），才有资格与 Frobenius 的特征值比较。",
        "Hecke 算子互相交换（$T_pT_q=T_qT_p$，$p\\neq q$），所以可以同时对角化；这是「存在特征形式基」的原因。",
        "归一化 $a_1=1$ 排除了数乘的自由度；没有这一步，特征值是「差一个常数」的，无法与 Galois 侧对齐。",
      ],
    formulas=[
        "$T_pf=\\lambda_pf$，$f=\\sum a_nq^n$ $\\Rightarrow$ $a_p=\\lambda_pa_1$",
        "$L(f,s)=\\sum a_nn^{-s}=\\prod_p(1-\\lambda_pp^{-s}+p^{k-1-2s})^{-1}$（归一化后）",
    ],
    theorems=[
        {
            "name": "特征形式的存在性与唯一性",
            "statement": "$S_k$ 有一组由 Hecke 特征形式构成的基；每个特征形式归一化后由它的特征值系统 $(\\lambda_p)_p$ 唯一确定。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "Hecke 算子两两交换且关于 Petersson 内积自伴。", "why": "自伴交换算子族可以同时正交对角化。"},
                    {"no": 2, "text": "在 $S_k$ 上同时对角化，得到特征形式基。", "why": "得到存在性。"},
                    {"no": 3, "text": "由 $q$ 展开的系数比较，特征值系统决定全部 $a_n$。", "why": "得到唯一性。"},
                ],
                "gap_note": "原文只用了结论，没有证明；完整证明见 [Sh1][K]。",
            },
            "source": "A p.9",
        },
    ],
    pitfalls=[
        "特征形式未必是整系数的：$a_n$ 一般是代数数，落在某个数域里；原文说「整数」只在特定情形（如 $\\SL(2,\\bbZ)$ 的 Hecke 特征形式）成立。",
        "$L(f,s)$ 的局部因子有 $p^{k-1-2s}$ 项，与 Galois 侧的 $2$ 维表示对应时要用到 $k$ 与权的匹配；丢掉这一项就对不上。",
    ],
    related=["goresky04/concept/hecke-operator", "goresky04/concept/satake-parameter", "goresky04/deriv/hecke-to-frobenius"],
    sources=[src([9, 9], "A p.9", "§5.5–§5.6")],
    provenance_note="对应原文 §5.5–§5.6；存在性定理按 [Sh1][K] 补，原文只写「可以同时对角化」。",
)

B["concepts/adele-ring"] = card(
    "concepts", "adele-ring",
    title="平代环与限制直积",
    aliases=["adele ring", "平代环", "A_Q", "限制直积"],
    track="B",
    summary="平代环 $\\bbA_\\bbQ=\\bbR\\times\\prod_p'\\bbQ_p$ 是把所有完备化一次收进来的环；它使「对所有素数同时成立」的陈述可以写成一个整体对象上的陈述。",
    question="为什么要把所有 $\\bbQ_p$ 乘起来，限制直积这个条件又在限制什么？",
    definition={
        "text": "平代环 $\\bbA_\\bbQ$ 的元素是序列 $(g_\\infty,g_2,g_3,\\dots)$，其中 $g_\\infty\\in\\bbR$，$g_p\\in\\bbQ_p$，并要求对几乎所有 $p$ 有 $g_p\\in\\bbZ_p$。这个条件叫限制直积。$\\bbQ$ 通过对角嵌入成为 $\\bbA_\\bbQ$ 的离散子环，商 $\\bbQ\\backslash\\bbA_\\bbQ$ 紧。有限平代 $\\bbA_{\\mathrm f}=\\prod_p'\\bbQ_p$ 是其中去掉 $\\bbR$ 的部分。",
        "notation": "$\\bbA=\\bbA_\\bbQ$；$\\bbA_{\\mathrm f}$ 有限平代；$\\hat{\\bbZ}=\\prod_p\\bbZ_p$ 是 $\\bbA_{\\mathrm f}$ 的紧开子环。",
    },
    key_points=[
        "限制直积不是技术细节：没有它，$\\prod_p\\bbQ_p$ 太大，$\\bbQ$ 的嵌入不离散，商空间没有好性质。",
        "平代环把「每个素数处给一个局部对象」打包成一个整体对象；朗兰兹猜想的两侧都是整体对象，所以必须用平代环。",
        "$\\bbQ\\backslash\\bbA$ 紧（加上 $\\bbR$ 后要除以正实数）是「整体紧性」的来源，它让 $L^2$ 空间的分解成为可能。",
    ],
    formulas=[
        "$\\bbA_\\bbQ=\\bbR\\times\\prod_p{}'\\bbQ_p$，$\\prod'$ 表示限制直积",
        "$\\bbQ\\backslash\\bbA_\\bbQ/\\bbR_{>0}$ 紧",
    ],
    theorems=[
        {
            "name": "紧性",
            "statement": "$\\bbQ$ 在 $\\bbA_\\bbQ$ 中离散，且 $\\bbQ\\backslash\\bbA_\\bbQ/\\bbR_{>0}$ 紧。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "取 $\\bbA$ 中使 $|x|\\le1$（所有局部绝对值）的基本域。", "why": "这是 $\\bbQ$ 的基本域候选。"},
                    {"no": 2, "text": "证明每个平代元模 $\\bbQ$ 都有唯一的代表元落在该基本域中。", "why": "离散性与基本域的存在性由此而来。"},
                    {"no": 3, "text": "基本域在 $\\bbA/\\bbR_{>0}$ 中的像紧。", "why": "得到商的紧性。"},
                ],
                "gap_note": "原文只陈述紧性，不证；这是 Tate 论文与 [G1] 的标准结果。",
            },
            "source": "A p.11",
        },
    ],
    pitfalls=[
        "平代环是环不是域：$2$ 在 $\\bbA$ 中没有逆（在 $2$ 进分量上不可逆），但它有逆当且仅当每个局部分量都可逆。",
        "$\\bbA_{\\mathrm f}$ 与 $\\hat{\\bbZ}$ 常被混用：前者是环，后者是它的紧开子环；$\\GL(2,\\bbA_{\\mathrm f})$ 的紧开子群是 $\\prod_p\\GL(2,\\bbZ_p)$，不是 $\\hat{\\bbZ}$ 本身。",
    ],
    related=["goresky04/concept/global-and-local-fields", "goresky04/deriv/adelic-equivalence", "goresky04/concept/automorphic-representation"],
    sources=[src([11, 11], "A p.11", "§6.1")],
    provenance_note="对应原文 §6.1 的定义段与 (6.1.1) 前的铺垫；紧性一条原文只引用，未证。",
)

B["concepts/automorphic-representation"] = card(
    "concepts", "automorphic-representation",
    title="自守形式与自守表示",
    aliases=["automorphic form", "自守形式", "自守表示", "$L^2_0$"],
    track="B",
    summary="自守形式是 $\\GL(n,\\bbQ)Z(\\bbA)\\backslash\\GL(n,\\bbA)$ 上满足增长与 $K$-有限条件的函数；自守表示是它在 $\\GL(n,\\bbA)$ 右正则作用下的不可约成分，尖点条件对应 $L^2_0$ 部分。",
    question="从模形式到自守表示这一步换掉了什么，为什么非换不可？",
    definition={
        "text": "自守形式 $f$ 是 $\\GL(n,\\bbQ)Z(\\bbA)\\backslash\\GL(n,\\bbA)$ 上的函数，满足：(1) $K_\\infty$ 有限、(2) 在 $\\mathfrak z$ 上按中心特征作用、(3) 中等增长。尖点自守形式还要求在抛物子群上的积分取零。自守表示是这些函数张成的空间在右正则作用下的不可约成分；尖点自守表示对应 $L^2_0$ 中的成分。对每个素数 $p$，自守表示在 $p$ 处的局部成分 $\\pi_p$ 决定 Hecke 特征值。",
        "notation": "$Z(\\bbA)$ 平代环的中心；$K_\\infty\\subset\\GL(n,\\bbR)$ 极大紧子群（$\\sO(n)$）；$\\pi=\\bigotimes_p'\\pi_p$ 为限制张量积。",
    },
    key_points=[
        "换掉的是「函数」这个载体：模形式是具体的函数，自守表示是整个表示，函数只是其中的向量。这样换之后才能对每个 $p$ 谈局部成分 $\\pi_p$。",
        "尖点条件（$L^2_0$）排除了 Eisenstein 级数，剩下的才是猜想里「漂亮」的那一部分。",
        "自守表示是**限制张量积**：整体表示由每个素数的局部表示拼成，这正是 (2.0.2) 逐素数比较的结构基础。",
    ],
    formulas=[
        "$L^2_0(\\GL(n,\\bbQ)Z(\\bbA)\\backslash\\GL(n,\\bbA))=\\bigoplus_\\pi m(\\pi)\\,\\pi$（离散谱分解）",
        "$\\pi=\\bigotimes_p{}'\\pi_p$，$\\pi_p$ 为 $p$ 处的局部成分",
    ],
    theorems=[
        {
            "name": "自守表示的局部–整体分解",
            "statement": "尖点自守表示分解为局部表示的限制张量积 $\\pi=\\bigotimes'_p\\pi_p$，且除有限个 $p$ 外 $\\pi_p$ 非分歧、由它的 Satake 参数唯一确定。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "把 $\\pi$ 在 $K=\\prod_pK_p$ 下的有限向量张成 $\\bigotimes\\pi_p$。", "why": "$K$-有限性给出张量积结构。"},
                    {"no": 2, "text": "证明除有限个 $p$ 外 $\\pi_p$ 有 $K_p$-不动向量。", "why": "这就是非分歧的定义。"},
                    {"no": 3, "text": "在非分歧处，$\\pi_p$ 由球 Hecke 代数的特征唯一确定。", "why": "Satake 同构给出参数。"},
                ],
                "gap_note": "原文没有证明，只把结论用作 §6.4 的前提；完整证明属 [G1] 的范畴。",
            },
            "source": "A p.12",
        },
    ],
    pitfalls=[
        "自守表示不等于模形式：一个自守表示可以含有一族模形式（同一个特征值系统的所有向量），模形式只是其中 $K$-有限向量的具体实现。",
        "$\\GL(1)$ 情形下自守表示就是 Hecke 特征（类域论），所以 §7.3 说「$\\GL(1)$ 又如何」时答案是类域论，不是平凡的。",
    ],
    related=["goresky04/concept/adele-ring", "goresky04/concept/satake-parameter", "goresky04/deriv/adelic-equivalence"],
    sources=[src([12, 14], "A p.12", "§6.2–§6.3")],
    provenance_note="对应原文 §6.2–§6.3 的 (6.2.1)(6.2.2)(6.3.1)–(6.3.3)；局部–整体分解按 [G1] 的通行陈述补齐。",
)

D = {}

D["derivations/adelic-equivalence"] = card(
    "derivations", "adelic-equivalence",
    title="从模形式到平代环上的自守形式（(6.1.1)）",
    aliases=["(6.1.1)", "平代等价", "adelic equivalence"],
    track="B",
    summary="把 $\\SL(2,\\bbZ)\\backslash\\he$ 写成 $\\GL(2,\\bbQ)Z(\\bbA)\\backslash\\GL(2,\\bbA)/\\sO(2)K_{\\mathrm f}$，模形式就变成平代环上的函数；这一步把古典对象交给整体表示论处理。",
    question="为什么 $\\SL(2,\\bbZ)\\backslash\\he$ 与平代环的商是同一个空间？",
    goal="证明 $X=\\SL(2,\\bbZ)\\backslash\\he\\cong\\GL(2,\\bbQ)Z(\\bbA)\\backslash\\GL(2,\\bbA)/\\sO(2)K_{\\mathrm f}$，并说明模形式的自守条件在这个等同下怎么读。",
    setup=[
        "$\\GL(2,\\bbA)=\\GL(2,\\bbR)\\times\\prod_p'\\GL(2,\\bbQ_p)$，$K_{\\mathrm f}=\\prod_p\\GL(2,\\bbZ_p)$。",
        "$\\bbA$ 上的强逼近定理：$\\GL(2,\\bbQ)$ 在 $\\GL(2,\\bbA)$ 中的双陪集代表元可以取成有限平代部分。",
        "$\\GL(2,\\bbR)$ 的 Iwasawa 分解 $\\GL(2,\\bbR)=\\sO(2)\\cdot\\bbR_{>0}\\cdot N$，$\\he\\cong\\GL(2,\\bbR)/(\\sO(2)\\cdot\\bbR_{>0})$。",
    ],
    steps=[
        {"no": 1, "text": "先看实分量：$\\he\\cong\\GL(2,\\bbR)/(\\sO(2)\\cdot\\bbR_{>0})$，左乘 $\\GL(2,\\bbR)$ 即 $\\SL(2,\\bbR)$ 在上半平面上的分式线性作用。", "why": "这给出「模形式定义在上半平面」的群论解释。", "locator": "A p.11", "provenance": "A"},
        {"no": 2, "text": "加上有限平代分量：$\\GL(2,\\bbQ)$ 在 $\\GL(2,\\bbA)$ 中离散，$K_{\\mathrm f}$ 是紧开子群，故 $\\GL(2,\\bbQ)\\backslash\\GL(2,\\bbA)/K_{\\mathrm f}$ 的连通成分对应到 $\\SL(2,\\bbZ)\\backslash\\he$ 的各个「层」。", "why": "有限素数的信息被 $K_{\\mathrm f}$ 的固定向量吸收。", "locator": "A p.11", "provenance": "A"},
        {"no": 3, "text": "取 $K_{\\mathrm f}$-不变函数，等价于只依赖 $\\GL(2,\\bbR)$ 分量，即上半平面上的函数。", "why": "这一步把「整体对象」压回「古典对象」。", "locator": "A p.11", "provenance": "A"},
        {"no": 4, "text": "再商掉中心 $Z(\\bbA)$ 与 $\\sO(2)$，得到 (6.1.1) 的等同。", "why": "中心与极大紧子群的作用不改变模形式的值。", "locator": "A p.11", "provenance": "B"},
        {"no": 5, "text": "在这个等同下，$\\SL(2,\\bbZ)$ 的自守因子对应到 $\\sO(2)$ 的权作用，Hecke 算子 $T_p$ 对应到 $\\GL(2,\\bbQ_p)$ 上的双陪集算子。", "why": "说明等同不只保空间，还保算子。", "locator": "A p.12", "provenance": "B"},
    ],
    result="古典模形式与 $\\GL(2,\\bbA)$ 上的 $K_{\\mathrm f}$-不变自守形式是同一批对象；Hecke 算子在两边对应，因此「特征值」这个概念在两边是同一个。",
    gaps=["强逼近定理原文没有陈述，只在 (6.1.1) 前说「有一个自然的（虽然并不完全显然的）等同」；步 2 的离散性依赖它。"],
    pitfalls=[
        "等同只在 $\\GL(2)$ 上成立，$n\\ge3$ 时 $\\SL(n,\\bbZ)\\backslash\\he_n$ 与平代商的对应仍成立，但缺少 Shimura 簇这个几何载体（见 §7.2）。",
        "中心 $Z(\\bbA)$ 不能随便去掉：不商掉它，$\\GL(2,\\bbQ)\\backslash\\GL(2,\\bbA)$ 上的函数会多一个连续参数（中心特征）。",
    ],
    related=["goresky04/concept/adele-ring", "goresky04/concept/modular-form-classical", "goresky04/concept/automorphic-representation"],
    sources=[src([11, 12], "A p.11", "§6.1")],
    provenance_note="步 1–3 对应原文 (6.1.1) 前的论述；步 4–5 的算子对应是译者按，原文只说「这个等同诱导同构」。",
)


if __name__ == "__main__":
    CARDS.update(B)
    CARDS.update(D)
    print("wrote", write_cards({**B, **D}))
