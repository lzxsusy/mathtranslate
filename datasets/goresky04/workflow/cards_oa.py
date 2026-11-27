#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cards_oa.py —— O 轨 2 张 + A 轨 4 张 + A 轨推导 1 张。"""
from gen_cards import CARDS, card, src, write_cards

O = {}

O["concepts/langlands-conjecture-statement"] = card(
    "concepts", "langlands-conjecture-statement",
    title="朗兰兹猜想（$\\GL(n,\\bbQ)$ 版）的陈述",
    aliases=["朗兰兹对应", "Langlands correspondence", "猜想陈述"],
    track="O",
    summary="对每个 $n$，$\\Gal(\\Qbar/\\bbQ)$ 的「漂亮」$n$ 维表示与 $\\GL(n,\\bbA_\\bbQ)$ 的「漂亮」自守表示应当一一对应，且 Frobenius 特征值对上 Hecke 特征值。",
    question="这条猜想到底断言了什么对应，两边各自要满足什么条件才算「漂亮」？",
    definition={
        "text": "原文把猜想写成一张箭头：(2.0.1) 把「$\\Gal(\\Qbar/\\bbQ)$ 的漂亮不可约 $n$ 维表示」送到「$\\GL(n,\\bbA_\\bbQ)$ 的漂亮自守表示」；(2.0.2) 说这个对应把「Frobenius 的特征值」送到「Hecke 算子的特征值」。两个「漂亮」都是占位词：左侧要求表示在几乎所有素数处非分歧、并且来自几何（有限个素数处容许分歧），右侧要求是尖点的（cuspidal）。",
        "notation": "$\\rho\\colon\\Gal(\\Qbar/\\bbQ)\\to\\GL(n,\\bbC)$ 或 $\\GL(n,\\Ql)$；$\\pi$ 记 $\\GL(n,\\bbA_\\bbQ)$ 的自守表示；$\\Fr_p$ 是 $p$ 处 Frobenius 元素，$T_p$ 是 $p$ 处 Hecke 算子。",
    },
    key_points=[
        "猜想是一张**双向箭头**而不是等号：它断言两侧的对象可以被对应起来，并且对应保持各自的特征值数据。",
        "「漂亮」不是修辞：左侧要非分歧（除有限个素数外），右侧要尖点。去掉这两个词，对应就假了。",
        "(2.0.2) 才是猜想有数学内容的地方。(2.0.1) 只说「有对应」，(2.0.2) 说这个对应**怎么算**：逐素数比对特征值。",
        "本文之后的每一节只做一件事：把 (2.0.1)(2.0.2) 里的每个词拆开讲清楚。",
    ],
    formulas=[
        "$\\left\\{\\substack{\\text{漂亮的不可约 }n\\text{ 维}\\\\ \\Gal(\\Qbar/\\bbQ)\\text{ 表示}}\\right\\}\\longrightarrow\\left\\{\\substack{\\GL(n,\\bbA_\\bbQ)\\text{ 的}\\\\ \\text{漂亮自守表示}}\\right\\}$  (2.0.1)",
        "$\\{\\Fr_p\\text{ 的特征值}\\}\\longrightarrow\\{T_p\\text{ 的特征值}\\}$  (2.0.2)",
    ],
    theorems=[
        {
            "name": "猜想 2.0.1（朗兰兹，$\\GL(n)$ 版）",
            "statement": "存在一个从 $\\Gal(\\Qbar/\\bbQ)$ 的漂亮 $n$ 维不可约表示到 $\\GL(n,\\bbA_\\bbQ)$ 的漂亮自守表示的对应，使得在每个非分歧素数 $p$ 处，该表示中 $\\Fr_p$ 的特征值等于对应自守表示中 $T_p$ 的特征值。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只是陈述，没有（也不可能有）证明；$n=2$ 的情形由 Eichler–Shimura 给出（见 $n=2$ 卡），$n\\ge3$ 至今未解。",
            },
            "source": "A p.1",
        },
    ],
    pitfalls=[
        "不要把 (2.0.1) 读成一个双射：原文只写箭头 $\\to$，两侧的「漂亮」条件各自筛选过，不是把所有表示都算进来。",
        "Frobenius 特征值是**逐素数**的数据，不是整体不变量；丢掉「几乎所有 $p$」这个限定，两边就无从比较。",
        "$\\GL(n,\\bbC)$ 与 $\\GL(n,\\Ql)$ 两种系数在本文里混用：左侧用 $\\bbC$ 便于谈特征值，用 $\\Ql$ 便于谈平展上同调，原文明说了这一点。",
    ],
    related=["goresky04/concept/two-sides-map", "goresky04/concept/frobenius-element", "goresky04/concept/satake-parameter"],
    sources=[src([1, 1], "A p.1", "§2")],
    provenance_note="对应原文 p.1 的 (2.0.1)(2.0.2) 与紧接的两句话；「漂亮」的两个条件取自 §2 末句与 §5、§6 的用法。",
)

O["concepts/two-sides-map"] = card(
    "concepts", "two-sides-map",
    title="两侧的地图：Galois 侧与自守侧各有什么",
    aliases=["两侧", "Galois 侧", "自守侧", "全局图景"],
    track="O",
    summary="左侧是平展上同调给出的 Galois 表示（数据是 Frobenius 特征值），右侧是模形式与自守表示（数据是 Hecke 特征值）；本文按「域—左侧—右侧—对照—推广」五步搭桥。",
    question="这条猜想的左右两侧分别由哪些对象组成，本文用什么顺序把它们搭起来？",
    definition={
        "text": "左侧：取定义在 $\\bbF_p$ 上的代数簇 $Y$，平展上同调 $H^i_{\\et}(Y,\\Ql)$ 天然带 $\\Gal(\\Qbar/\\bbQ)$ 作用，于是在每个非分歧 $p$ 处可以读出 $\\Fr_p$ 的特征值。右侧：模形式（上半平面上的函数）经 Hecke 算子作用得到 Hecke 特征形式，其特征值 $\\lambda_p$ 就是自守侧的数据；用平代环改写后，这些特征值成为自守表示的 Satake 参数。",
        "notation": "$H^i_{\\et}(Y,\\Ql)$ 平展上同调；$\\zeta(Y,s)$ 代数簇的 $\\zeta$ 函数；$\\he$ 上半平面；$\\bbA$ 平代环；$T_p$ Hecke 算子。",
    },
    key_points=[
        "两侧的「数据」是同一类型的东西：一侧是 Frobenius 的特征值，另一侧是 Hecke 的特征值，都是一个数（或一组数）附在每个素数上。对应就是让这两组数逐素数相等。",
        "左侧天生带几何（上同调），右侧天生带分析（$L^2$ 空间上的算子）；本文花了 §3 铺域、§4 讲左侧、§5–§6 讲右侧，最后才有资格谈 §7 的对照。",
        "五步顺序（§2 陈述 → §3 域 → §4 左侧 → §5–§6 右侧 → §7–§8 对照与推广）就是本文的骨架，也是读这篇文章的唯一顺序。",
    ],
    formulas=[
        "$\\zeta(Y,s)=\\prod_p \\zeta_p(Y,p^{-s})$，$\\zeta_p$ 由 $\\Fr_p$ 在 $H^i_{\\et}(Y,\\Ql)$ 上的特征值决定",
        "$L(\\pi,s)=\\prod_p L_p(\\pi,s)$，$L_p$ 由 $T_p$ 的特征值决定",
    ],
    theorems=[
        {
            "name": "对照原理（本文的目标）",
            "statement": "存在一族几何对象，使它们的平展上同调所携带的 Galois 表示正好对应到一族自守表示，并且两个 $L$ 函数相等。$n=2$ 时这族对象是 Shimura 簇（模曲线），$n\\ge3$ 时不存在。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "把 $\\zeta(Y,s)$ 分解为逐素数的局部因子之积。", "why": "只有拆成逐素数，才能与自守侧的 $L_p$ 比较。"},
                    {"no": 2, "text": "把 $L(\\pi,s)$ 也拆成逐素数的局部因子之积。", "why": "同上，比较必须在同一个粒度上做。"},
                    {"no": 3, "text": "逐素数证明两个局部因子相等。", "why": "这就是 (2.0.2)：Frobenius 特征值 = Hecke 特征值。"},
                ],
                "gap_note": "原文只对 $n=2$ 给出证明（§7.1 的 Eichler–Shimura），一般 $n$ 至今未解；这里列的是本文的论证目标，不是已证的定理。",
            },
            "source": "A p.14",
        },
    ],
    pitfalls=[
        "两侧并不是「同一种东西的两种写法」：左侧是几何对象的上同调，右侧是函数空间上的算子，中间没有显然的函子。本文的贡献之一就是把「没有显然函子」这件事讲明白。",
        "不要指望在 §4、§5 各自内部看到对应；对应只在 §7 出现，且只对 $n=2$ 成立。",
    ],
    related=["goresky04/concept/langlands-conjecture-statement", "goresky04/concept/etale-cohomology", "goresky04/concept/hecke-eigenform", "goresky04/concept/obstruction-n-ge-3"],
    sources=[src([1, 1], "A p.1", "§1–§2"), src([14, 15], "A p.14", "§7")],
    provenance_note="综合原文 §1 的定位段、§2 的箭头、§7 的对照与 §8 的推广；「五步顺序」是对全文结构的概括，原文未逐条列出。",
)

A = {}

A["concepts/global-and-local-fields"] = card(
    "concepts", "global-and-local-fields",
    title="域的分类：数域、$p$ 进域、函数域",
    aliases=["域", "fields", "局部域", "整体域"],
    track="A",
    summary="猜想原本写在 $\\bbQ$ 上，但同一句话在数域、$p$ 进域、函数域上各有版本；本文先把「域」这一层列清楚，才谈得上推广。",
    question="为什么讲朗兰兹之前必须先讲域，整体域与局部域在猜想里各扮演什么角色？",
    definition={
        "text": "整体域有两类：数域（$\\bbQ$ 的有限扩张，如 $\\bbQ$）与整体函数域（$\\bbF_q$ 上曲线 $C$ 的函数域 $\\bbF_q(C)$）。局部域是整体域在一个素数处的完备化：$\\bbQ$ 在 $p$ 处完备化得 $p$ 进域 $\\bbQ_p$，在无穷处得 $\\bbR$；整体函数域在一点处完备化得局部函数域 $\\bbF_q((t))$。猜想在整体域上陈述（两侧的对象都是整体的），但每个素数的局部因子只在局部域上定义。",
        "notation": "$\\bbF_q$ 有限域；$\\bbQ_p$ $p$ 进域，$\\bbZ_p$ 为其整数环；$\\bbF_q((t))$ 局部函数域；$\\bbA_F$ 整体域 $F$ 的平代环。",
    },
    key_points=[
        "「整体」与「局部」不是两种猜想，而是同一猜想的两个粒度：整体对象有 $L$ 函数，局部对象给出 $L$ 函数的每个因子。",
        "函数域情形比数域情形**简单**：曲线有几何，$\\bbF_q(C)$ 上的猜想可以看成「曲线上的几何对象」，这正是几何朗兰兹的起点。",
        "本文 §3 列了六种域，但只对 $\\bbQ$ 与 $\\bbQ_p$ 展开细节；其余几种只给一句话，为的是让读者知道「同一个猜想可以搬到哪儿」。",
    ],
    formulas=[
        "$\\bbQ\\subset\\bbQ_p$，$\\bbZ_p=\\{x\\in\\bbQ_p: |x|_p\\le 1\\}$",
        "$\\bbA_\\bbQ=\\bbR\\times\\prod_p{}'\\bbQ_p$（限制直积：除有限个 $p$ 外分量落在 $\\bbZ_p$）",
    ],
    theorems=[
        {
            "name": "局部–整体原则（本文用法）",
            "statement": "整体域上的 $L$ 函数是局部域上局部因子之积；因此「两侧 $L$ 函数相等」可以逐素数拆成「局部因子相等」。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "把整体域 $F$ 在每处完备化，得到一族局部域。", "why": "完备化是取局部信息的标准手段。"},
                    {"no": 2, "text": "在每个局部域上定义局部因子。", "why": "局部因子只依赖该处的表示数据。"},
                    {"no": 3, "text": "对几乎所有处，局部因子由未分歧条件唯一确定，乘积收敛。", "why": "这是欧拉乘积有意义的必要条件。"},
                ],
                "gap_note": "原文没有给出收敛性证明，只说「对几乎所有处非分歧」；收敛域要用 Deligne 的权估计，超出 §3 的范围。",
            },
            "source": "A p.2",
        },
    ],
    pitfalls=[
        "不要把「局部域」理解成「小的整体域」：$\\bbQ_p$ 不是 $\\bbQ$ 的子域，完备化是有损的。",
        "函数域与数域的地位并不对称：函数域情形有 Frobenius 的几何解释（曲线上的对应），数域情形没有，这正是几何朗兰兹只在函数域上成立的原因。",
        "$\\bbF_q((t))$ 与 $\\bbQ_p$ 都是局部域，但前者是「$t$ 的幂级数」，后者是「$p$ 的幂级数」；本文把它们分开列，是因为函数域情形的几何更好用。",
    ],
    related=["goresky04/concept/adele-ring", "goresky04/concept/frobenius-element", "goresky04/concept/geometric-langlands"],
    sources=[src([1, 4], "A p.2", "§3.1–§3.7")],
    provenance_note="对应原文 §3.2–§3.7 的六小节；局部–整体原则的表述是对 §3.8 表格与 §4.4 的概括。",
)

A["concepts/etale-cohomology"] = card(
    "concepts", "etale-cohomology",
    title="平展上同调与 Galois 作用",
    aliases=["étale cohomology", "平展上同调", "上同调"],
    track="A",
    summary="对定义在 $\\bbF_p$ 上的簇 $Y$，$H^i_{\\et}(Y,\\Ql)$ 是有限维 $\\Ql$ 向量空间，带 $\\Gal(\\Qbar/\\bbQ)$ 的连续作用；于是几何给出 Galois 表示。",
    question="为什么必须用平展上同调而不是奇异上同调，它凭什么携带 Galois 作用？",
    definition={
        "text": "设 $Y$ 是定义在 $\\bbF_p$（或数域）上的代数簇，$\\ell\\neq p$ 为素数。平展上同调 $H^i_{\\et}(Y,\\Ql)$ 是有限维 $\\Ql$ 向量空间，它具有「取几何纤维」的函子性：把 $Y$ 基变换到 $\\Qbar$ 上再取上同调，得到的空间上自然有 $\\Gal(\\Qbar/\\bbF_p)$（或 $\\Gal(\\Qbar/\\bbQ)$）的作用，因为几何纤维的选取只差一个 Galois 自同构。",
        "notation": "$\\Ql$ 是 $\\ell$ 进数域；$\\ell\\neq p$ 保证系数域与底域的特征不同（否则上同调退化）；$H^i_{\\et}(Y,\\Ql)$ 常简写为 $H^i(Y)$。",
    },
    key_points=[
        "奇异上同调 $H^i(Y(\\bbC),\\bbQ)$ 没有 Galois 作用——它只看到复点。要看到算术，必须换系数（$\\Ql$）并换拓扑（平展）。",
        "「$\\ell\\neq p$」不是技术洁癖：$\\ell=p$ 时系数域与底域同特征，平展上同调会退化，必须换成晶体上同调之类的工具，本文不涉及。",
        "有限维性使特征值有意义：$\\Fr_p$ 作用在有限维空间上，特征多项式是良定义的，这才有 (4.4.1) 的局部因子。",
    ],
    formulas=[
        "$H^i_{\\et}(Y,\\Ql)$：有限维 $\\Ql$ 向量空间，带连续 $\\Gal(\\Qbar/\\bbF_p)$ 作用（$\\ell\\neq p$）",
        "$H^i_{\\et}(Y,\\Ql)\\otimes_{\\Ql}\\bbC$：取嵌入后得到复向量空间，谈特征值",
    ],
    theorems=[
        {
            "name": "平展上同调的基本性质（本文引用的版本）",
            "statement": "$Y$ 为定义在 $\\bbF_p$ 上的代数簇、$\\ell\\neq p$ 时，$H^i_{\\et}(Y,\\Ql)$ 有限维，且 $\\Gal(\\Qbar/\\bbF_p)$ 的作用连续（经过一个有限商分解）。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只做陈述并指向 [T]（Taylor 的 ICM 报告）与 [G1]；完整证明属 SGA 4½ 的内容，超出本文范围。",
            },
            "source": "A p.5",
        },
    ],
    pitfalls=[
        "上同调的次数 $i$ 与权的概念容易混：$\\Fr_p$ 在 $H^i$ 上的特征值的绝对值（在复嵌入下）满足 Deligne 的权限制，这是 §4.2 的内容，不是上同调本身的定义。",
        "$\\Ql$ 与 $\\bbC$ 之间的切换要用到一个嵌入 $\\Ql\\hookrightarrow\\bbC$，这个嵌入不是典则的；原文特意提醒「取定一个嵌入」才能把特征值当复数谈。",
        "平展上同调不是「用平展拓扑算奇异上同调」：在 $\\bbC$ 上两者一致，但在有限域上没有拓扑空间可算，只能靠平展景。",
    ],
    related=["goresky04/concept/zeta-function-of-variety", "goresky04/concept/frobenius-element", "goresky04/concept/global-and-local-fields"],
    sources=[src([5, 5], "A p.5", "§4.1")],
    provenance_note="对应原文 §4.1 全节；「$\\ell=p$ 会退化」一句是把原文的 $\\ell\\neq\\char(E)$ 条件讲开，属译者按。",
)

A["concepts/zeta-function-of-variety"] = card(
    "concepts", "zeta-function-of-variety",
    title="代数簇的 $\\zeta$ 函数与 Deligne 的四个结论",
    aliases=["zeta function", "ζ 函数", "Weil 猜想", "Deligne"],
    track="A",
    summary="$\\zeta(Y,s)$ 把每个素数处 Frobenius 在 $H^i_{\\et}$ 上的特征值打包成一个欧拉乘积；Deligne 证明它有理性、函数方程，且零点满足 Riemann 假设。",
    question="$\\zeta(Y,s)$ 是怎么由上同调定义的，Deligne 的四个结论各说了什么？",
    definition={
        "text": "设 $Y$ 定义在 $\\bbF_q$ 上。把 $\\Fr_p$ 在 $H^i_{\\et}(Y,\\Ql)$ 上的特征值记为 $\\alpha_{ij}$，则 $\\zeta(Y,s)$ 定义为这些特征值的欧拉乘积；等价地，$\\zeta(Y,s)$ 是 $\\#Y(\\bbF_{q^m})$ 的增长函数。Deligne 证明：(1) 有理性；(2) 函数方程；(3) 零点与极点的位置（Riemann 假设的类比）；(4) 与拓扑 Betti 数的关系。",
        "notation": "$\\zeta(Y,s)=\\prod_p\\zeta_p(Y,p^{-s})$；$t=q^{-s}$ 时常写作 $Z(Y,t)$；$\\alpha_{ij}$ 是 $\\Fr$ 在 $H^i_{\\et}(Y,\\Ql)$ 上的特征值。",
    },
    key_points=[
        "把 $\\zeta$ 与上同调挂钩，是 Weil 猜想的实质：$\\zeta$ 的解析性质被翻译成 $\\Fr$ 在有限维空间上的线性代数。",
        "「Riemann 假设」在这里不是比喻：它断言 $\\alpha_{ij}$ 的复绝对值为 $q^{i/2}$，这正是 $\\Re s=i/2$ 的类比。",
        "函数方程来自 Poincaré 对偶：$H^i$ 与 $H^{2d-i}$ 配对，特征值取倒数。",
    ],
    formulas=[
        "$\\zeta(Y,s)=\\prod_{i=0}^{2d}\\prod_j\\bigl(1-\\alpha_{ij}q^{-s}\\bigr)^{(-1)^{i+1}}$",
        "$\\zeta(Y,s)\\mapsto\\pm q^{d(1-s)}\\zeta(Y,1-s)$（函数方程）",
    ],
    theorems=[
        {
            "name": "Deligne 的四个结论（Weil 猜想）",
            "statement": "(1) $\\zeta(Y,s)$ 是有理函数；(2) 满足函数方程 $\\zeta(Y,s)=\\pm q^{d(1-s)}\\zeta(Y,1-s)$；(3) 每个 $\\alpha_{ij}$ 的复绝对值为 $q^{i/2}$；(4) 当 $Y$ 光滑投射时，$\\zeta$ 的「次数」与 Betti 数一致。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只列结论并注明是 Deligne 的定理（[Del]），没有证明；这是 20 世纪代数几何最深的结果之一。",
            },
            "source": "A p.6",
        },
    ],
    pitfalls=[
        "不要把它与 Dedekind $\\zeta$ 或 Riemann $\\zeta$ 混为一谈：这里是**代数簇**的 $\\zeta$，即使 $Y=\\mathrm{Spec}\\,\\bbZ$ 也只是形式上的类比。",
        "函数方程里的 $\\pm$ 号与 $d=\\dim Y$ 有关，原文没展开符号，读者不必在此纠缠。",
        "「Riemann 假设」部分（结论 3）只对光滑投射簇叙述，奇异簇要用相交上同调修正（见注 28）。",
    ],
    related=["goresky04/concept/etale-cohomology", "goresky04/deriv/local-zeta-factor", "goresky04/concept/frobenius-element"],
    sources=[src([6, 6], "A p.6", "§4.2")],
    provenance_note="对应原文 §4.2 的四个结论与 $\\zeta$ 函数定义；「Riemann 假设的类比」一段是把原文一句「与 $\\Re s=1/2$ 类比」讲开。",
)

A["concepts/frobenius-element"] = card(
    "concepts", "frobenius-element",
    title="Frobenius 元素与局部因子",
    aliases=["Frobenius", "Fr_p", "σ_p", "非分歧"],
    track="A",
    summary="在非分歧素数 $p$ 处，Galois 表示经过 $\\Gal(\\overline{\\bbF}_p/\\bbF_p)$ 分解，后者的生成元在表示中的像就是 $\\Fr_p$；它的特征多项式定义了局部因子。",
    question="$\\Fr_p$ 是怎么被定义出来的，为什么它只在非分歧处良定义？",
    definition={
        "text": "设 $\\rho\\colon\\Gal(\\Qbar/\\bbQ)\\to\\GL(H)$，$p\\neq\\ell$。称 $\\rho$ 在 $p$ 处非分歧，若 $\\rho$ 在分解群 $\\Gal(\\overline{\\bbQ}_p/\\bbQ_p)$ 上的限制经过商 $\\Gal(\\overline{\\bbF}_p/\\bbF_p)$ 分解。此时 $\\Gal(\\overline{\\bbF}_p/\\bbF_p)\\cong\\hat{\\bbZ}$ 有典则生成元（几何 Frobenius 的逆），取它在 $\\rho$ 下的像即 $\\Fr_p=\\rho_p(\\sigma_p)$。局部因子 $\\zeta_p(\\rho,t)=1/\\det(I-t\\Fr_p)$。",
        "notation": "$\\sigma_p$ 是原文对 $\\Fr_p$ 的记号；$\\mathrm{Gal}(\\overline{\\bbF}_p/\\bbF_p)\\cong\\hat{\\bbZ}=\\prod_{q}\\bbZ_q$。",
    },
    key_points=[
        "非分歧条件的作用是保证 $\\rho$ 在惯性群 $I_p$ 上平凡，于是 $\\Fr_p$ 的选取只差一个共轭——因此在 $\\GL(H)$ 中共轭类良定义，特征多项式良定义。",
        "分歧处的局部因子更复杂，要引入 $\\varepsilon$ 因子与导子；本文只处理非分歧处，因为「几乎所有 $p$ 都非分歧」对几何来源的表示成立。",
        "$\\Fr_p$ 不是唯一的元素，同一个共轭类里的任何元素给出的特征多项式相同，所以 $\\zeta_p$ 是良定义的。",
    ],
    formulas=[
        "$\\rho_p\\colon\\Gal(\\overline{\\bbF}_p/\\bbF_p)\\to\\GL(H)$，$\\Fr_p=\\rho_p(\\sigma_p)$",
        "$\\zeta_p(\\rho,t)=\\dfrac{1}{\\det(I-t\\Fr_p)}$",
    ],
    theorems=[
        {
            "name": "良定义性",
            "statement": "若 $\\rho$ 在 $p$ 处非分歧，则 $\\Fr_p$ 的共轭类与 $\\zeta_p(\\rho,t)$ 都不依赖分解群的选取。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "不同素数 $p$ 上的分解群互相共轭（取一个 $\\Gal(\\Qbar/\\bbQ)$ 元素搬运）。", "why": "这是局部–整体对应中「选不同嵌入」的唯一差别。"},
                    {"no": 2, "text": "共轭变换把 $\\Fr_p$ 变成共轭元素。", "why": "共轭元素有相同的特征多项式。"},
                    {"no": 3, "text": "故 $\\det(I-t\\Fr_p)$ 与选取无关。", "why": "行列式在共轭下不变。"},
                ],
                "gap_note": "原文只说「不难看出」，没有写出这三步；本卡的三步是译者按。",
            },
            "source": "A p.7",
        },
    ],
    pitfalls=[
        "原文在 $\\Fr_p$ 与 $\\sigma_p$ 之间混用记号（$\\Fr_p=\\rho_p(\\sigma_p)$ 中 $\\sigma_p$ 是抽象生成元，$\\Fr_p$ 是它在表示里的像）；读的时候要分清「Galois 群里的元素」与「矩阵」。",
        "几何 Frobenius 与算术 Frobenius 互为逆，取哪一个只影响 $t$ 与 $t^{-1}$，不影响 $\\zeta$ 的有理性；本文不作区分。",
        "非分歧的定义要求 $\\rho$ 在惯性群上平凡，而不是只要求「$\\rho$ 在 $I_p$ 上有有限像」；后者是一般情形，要用导子处理。",
    ],
    related=["goresky04/concept/etale-cohomology", "goresky04/deriv/local-zeta-factor", "goresky04/concept/satake-parameter"],
    sources=[src([7, 7], "A p.7", "§4.4")],
    provenance_note="对应原文 §4.4；「共轭类良定义」的证明是译者补的三步，原文只说「不难看出」。",
)

D = {}

D["derivations/local-zeta-factor"] = card(
    "derivations", "local-zeta-factor",
    title="从 Frobenius 特征值造出局部因子与欧拉乘积",
    aliases=["(4.4.1)", "局部因子", "欧拉乘积"],
    track="A",
    summary="把 $\\Fr_p$ 的特征多项式取倒数得到 $\\zeta_p(\\rho,t)$，再把各素数处的 $\\zeta_p(\\rho,p^{-s})$ 乘起来就得到 $L(\\rho,s)$；这一步是整篇文章「逐素数比较」的技术基础。",
    question="如何从「$\\Fr_p$ 的特征值」这个逐素数数据，造出整体 $L$ 函数？",
    goal="证明 $L(\\rho,s)=\\prod_p\\zeta_p(\\rho,p^{-s})$ 是良定义的（在收敛域内），并说明它为什么编码了 Frobenius 的特征值。",
    setup=[
        "$\\rho\\colon\\Gal(\\Qbar/\\bbQ)\\to\\GL(H)$ 在几乎所有 $p$ 处非分歧，$\\dim H=n<\\infty$。",
        "取定嵌入 $\\Ql\\hookrightarrow\\bbC$，把 $\\Fr_p$ 的特征值看成复数。",
        "$\\zeta_p(\\rho,t)=1/\\det(I-t\\Fr_p)$，其中 $\\Fr_p$ 是 $n\\times n$ 矩阵。",
    ],
    steps=[
        {"no": 1, "text": "把 $\\det(I-t\\Fr_p)$ 展开为 $\\prod_{j=1}^{n}(1-t\\alpha_j)$，$\\alpha_j$ 是 $\\Fr_p$ 的特征值。", "why": "行列式按特征值分解，这是唯一把「矩阵」翻译成「数」的一步。", "locator": "A p.7", "provenance": "A"},
        {"no": 2, "text": "于是 $\\zeta_p(\\rho,t)^{-1}=\\prod_j(1-t\\alpha_j)$，其系数是特征值的初等对称函数。", "why": "说明局部因子只依赖特征值，不依赖矩阵本身。", "locator": "A p.7", "provenance": "A"},
        {"no": 3, "text": "代入 $t=p^{-s}$，得 $\\zeta_p(\\rho,p^{-s})=\\prod_j(1-\\alpha_j p^{-s})^{-1}$。", "why": "这是把「几何的 $t$」与「解析的 $s$」对齐的换元。", "locator": "A p.7", "provenance": "A"},
        {"no": 4, "text": "对几乎所有 $p$ 取乘积：$L(\\rho,s)=\\prod_p\\zeta_p(\\rho,p^{-s})$。", "why": "逐素数的局部数据被组装成整体函数。", "locator": "A p.7", "provenance": "A"},
        {"no": 5, "text": "由 Deligne 的权估计 $|\\alpha_j|\\le q^{w/2}$（$w$ 为权），乘积在 $\\Re s>w/2+1$ 时绝对收敛。", "why": "保证欧拉乘积不是形式记号，而是一个解析函数。", "locator": "A p.6", "provenance": "B"},
    ],
    result="$L(\\rho,s)$ 在每个非分歧素数处的局部因子由 $\\Fr_p$ 的特征值唯一决定；两侧比较最终归结为「逐素数比特征值」。",
    gaps=["原文没有证明收敛性，只引 Deligne 的权估计；本文其余部分也不需要收敛域，只需要「逐素数局部因子有定义」。"],
    pitfalls=[
        "局部因子是 $\\det(I-t\\Fr_p)^{-1}$ 而不是 $\\det(I-t\\Fr_p)$：取倒数是为了让欧拉乘积与通常的 $L$ 函数写法一致。",
        "在分歧处 $\\Fr_p$ 不良定义，局部因子要另设；漏掉这一点会把 (4.4.1) 误读成对所有 $p$ 成立。",
    ],
    related=["goresky04/concept/frobenius-element", "goresky04/concept/zeta-function-of-variety", "goresky04/deriv/hecke-to-frobenius"],
    sources=[src([7, 7], "A p.7", "§4.4"), src([6, 6], "A p.6", "§4.2")],
    provenance_note="步 1–4 逐字对应原文 (4.4.1) 的推导；步 5 的收敛性原文未写，按 Deligne 的权估计补，标 B 级。",
)


if __name__ == "__main__":
    CARDS.update(O)
    CARDS.update(A)
    CARDS.update(D)
    print("wrote", write_cards({**O, **A, **D}))
