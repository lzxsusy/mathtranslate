#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cards_cd.py —— C 轨 4 张 + 推导 2 张 + D 轨 3 张。"""
from gen_cards import CARDS, card, src, write_cards

C = {}

C["concepts/satake-parameter"] = card(
    "concepts", "satake-parameter",
    title="Satake 参数：非分歧局部表示的指纹",
    aliases=["Satake parameter", "Satake 同构", "球 Hecke 代数", "$\\lambda_p$"],
    track="C",
    summary="非分歧局部表示 $\\pi_p$ 由球 Hecke 代数 $H_p$ 的一个特征（即 $n$ 个数的无序组 $\\alpha_1,\\dots,\\alpha_n$）唯一确定；这组数就是 Satake 参数，也等于 $T_p$ 的特征值。",
    question="为什么一个非分歧局部表示可以被「$n$ 个数」完全决定？",
    definition={
        "text": "固定素数 $p$，$G_p=\\GL(n,\\bbQ_p)$，$K_p=\\GL(n,\\bbZ_p)$。球 Hecke 代数 $H_p$ 是 $K_p$-双不变紧支函数的卷积代数，以双陪集 $K_pgK_p$ 为基。Satake 同构说 $H_p\\cong\\bbC[X_*(T)]^{W}$，其中 $T$ 是极大环面、$W$ 是 Weyl 群。于是 $H_p$ 的特征由 $T$ 上的一个点（模 $W$）给出，即一个无序的 $n$ 元组 $(\\alpha_1,\\dots,\\alpha_n)\\in(\\bbC^\\times)^n/W$。这个 $n$ 元组就是 $\\pi_p$ 的 Satake 参数。",
        "notation": "$T\\subset\\GL(n)$ 对角环面；$X_*(T)=\\bbZ^n$；$W=S_n$；$\\alpha_i$ 记 Satake 参数；$H_p$ 的生成元是 $T_{p,i}$（$i=0,\\dots,n$）。",
    },
    key_points=[
        "Satake 参数是「非分歧」的等价物：一个局部表示非分歧，当且仅当它有 $K_p$-固定向量，当且仅当它是 $H_p$ 的特征。",
        "参数是无序组（模 $W$）而不是有序组：这正是为什么它只能与「Frobenius 的共轭类」比较，不能与单个矩阵比较。",
        "参数与 $L$ 因子直接相关：$L_p(\\pi,s)=\\prod_{i}(1-\\alpha_ip^{-s})^{-1}$，所以「Satake 参数相等」就是「局部因子相等」。",
        "对 $\\GL(2)$，参数是两个数 $\\alpha,\\beta$；模形式情形下它们由 $\\lambda_p$ 与 $p^{k-1}$ 决定，即 $\\alpha+\\beta=\\lambda_p$，$\\alpha\\beta=p^{k-1}$。",
    ],
    formulas=[
        "$H_p=K_p\\backslash G_p/K_p$ 为基的卷积代数，$H_p\\cong\\bbC[X_*(T)]^{W}$",
        "$L_p(\\pi,s)=\\prod_{i=1}^{n}(1-\\alpha_ip^{-s})^{-1}$",
    ],
    theorems=[
        {
            "name": "Satake 同构",
            "statement": "$H_p\\cong\\bbC[X_*(T)]^{W}$ 是环同构；因此 $H_p$ 的特征与 $(\\bbC^\\times)^n/W$ 一一对应。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只在注 25 里引用这个同构，没有证明；它属于 $p$ 进群的表示论（Macdonald 公式、球函数）。",
            },
            "source": "A p.18",
        },
    ],
    pitfalls=[
        "参数是 $(\\alpha_1,\\dots,\\alpha_n)$ 模置换，不是有序组；写 $\\{\\alpha_i\\}$ 时要用花括号或「无序组」。",
        "Satake 参数依赖归一化：把 $\\pi_p$ 乘上一个未分歧特征，参数会整体乘一个数；比较两侧时必须固定同一个归一化（通常要求中心特征与 $|\\cdot|^?$ 匹配）。",
        "非分歧是必要前提：分歧表示的局部因子更复杂，没有这种「$n$ 个数」的干净描述。",
    ],
    related=["goresky04/concept/automorphic-representation", "goresky04/concept/hecke-eigenform", "goresky04/deriv/hecke-to-frobenius"],
    sources=[src([13, 13], "A p.13", "§6.4"), src([18, 18], "A p.18", "注 25")],
    provenance_note="对应原文 §6.4 与注 25；同构的证明属 Macdonald 公式，原文未给。",
)

C["concepts/eichler-shimura-theorem"] = card(
    "concepts", "eichler-shimura-theorem",
    title="Eichler–Shimura：$n=2$ 情形猜想的证明",
    aliases=["Eichler–Shimura", "Eichler-Shimura 定理", "$n=2$"],
    track="C",
    summary="模曲线 $X$ 的平展上同调 $H^1_{\\et}(X,\\Ql)$ 分解为 Eisenstein 部分与尖点部分，尖点部分正好给出与 Hecke 特征形式对应的 $2$ 维 Galois 表示——这就是 $n=2$ 的朗兰兹对应。",
    question="为什么 $n=2$ 时猜想可以被证明，证明用的是哪条上同调？",
    definition={
        "text": "取 $X=\\GL(2,\\bbQ)Z(\\bbA)\\backslash\\GL(2,\\bbA)/\\sO(2)K_{\\mathrm f}$（模曲线）。Eichler 与 Shimura 证明：$X$ 上存在局部系数系 $E_k$（由权 $k$ 决定），使得 $H^1_P(X,E_k;\\bbQ)\\otimes\\bbC\\cong S_k\\oplus\\overline{S_k}$。于是每个归一化 Hecke 特征形式 $f\\in S_k$ 对应 $H^1_{\\et}(X,\\Ql)$ 中的一个 $2$ 维 Galois 表示 $\\rho_f$，并且 $L(\\rho_f,s)=L(f,s)$。",
        "notation": "$H^1_P$ 记抛物上同调（parabolic cohomology）；$E_k$ 是权 $k$ 的局部系数系；$\\overline{S_k}$ 是复共轭。",
    },
    key_points=[
        "关键的几何事实：模曲线是**代数曲线**，所以它有平展上同调，上同调上带 Galois 作用。$n\\ge3$ 时缺的正是这个几何对象。",
        "上同调分解成 Eisenstein 部分与尖点部分，尖点部分才对应自守表示；Eisenstein 部分对应的是诱导表示，不属于「漂亮」的那一类。",
        "证明是「构造性」的：它不只说存在对应，而是把对应具体写成「取上同调中的一个成分」，所以能逐素数验证 $L$ 函数相等。",
    ],
    formulas=[
        "$H^1_P(X,E_k;\\bbQ)\\otimes_{\\bbQ}\\bbC\\cong S_k\\oplus\\overline{S_k}$  (7.1.1)",
        "$L(\\rho_f,s)=L(f,s)=\\prod_p(1-\\lambda_pp^{-s}+p^{k-1-2s})^{-1}$",
    ],
    theorems=[
        {
            "name": "Eichler–Shimura（$n=2$）",
            "statement": "对每个归一化 Hecke 特征形式 $f\\in S_k$，存在 $2$ 维 Galois 表示 $\\rho_f\\colon\\Gal(\\Qbar/\\bbQ)\\to\\GL(2,\\Ql)$，使 $L(\\rho_f,s)=L(f,s)$；反之 $H^1_{\\et}$ 的每个尖点成分都这样来。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "在模曲线上取局部系数系 $E_k$，算抛物上同调。", "why": "上同调是 Galois 表示的来源。"},
                    {"no": 2, "text": "用 Hecke 算子作用在上同调上，同时对角化，得到特征形式与上同调成分的对应。", "why": "这一步把 Hecke 特征值与上同调成分绑在一起。"},
                    {"no": 3, "text": "对每个成分取 $2$ 维 Galois 表示（模曲线是曲线，$H^1$ 是 $2$ 维）。", "why": "$n=2$ 的特殊性：$H^1$ 的秩正好是 $2$。"},
                    {"no": 4, "text": "逐素数比较 $\\Fr_p$ 与 $T_p$ 的特征多项式，得 $L$ 函数相等。", "why": "完成 (2.0.2)。"},
                ],
                "gap_note": "原文只给出 (7.1.1) 与结论，不提证明细节；完整证明见 [Sh1][K][M]。",
            },
            "source": "A p.14",
        },
    ],
    pitfalls=[
        "不要把 $H^1_{\\et}(X,\\Ql)$ 直接等同于 $S_k$：中间要乘 $\\overline{S_k}$（复共轭），且要取抛物上同调（去掉 Eisenstein 部分）。",
        "$n=2$ 的成功依赖「模曲线是一维的」：$H^1$ 的秩 $2$ 与群 $\\GL(2)$ 的维数 $2$ 恰好对上；对 $\\GL(n)$ 需要 $n-1$ 维的簇，那是 Shimura 簇，只在少数情形存在。",
    ],
    related=["goresky04/concept/shimura-variety", "goresky04/deriv/eichler-shimura-decomposition", "goresky04/concept/obstruction-n-ge-3"],
    sources=[src([14, 14], "A p.14", "§7.1")],
    provenance_note="对应原文 §7.1 的 (7.1.1) 与文字说明；证明四步是译者按 [Sh1][K] 的通行证明概括，原文未展开。",
)

C["concepts/shimura-variety"] = card(
    "concepts", "shimura-variety",
    title="Shimura 簇：$n=2$ 的几何载体",
    aliases=["Shimura variety", "Shimura 簇", "模曲线", "模空间"],
    track="C",
    summary="Shimura 簇是带水平结构的阿贝尔簇的模空间；对 $n=2$ 它就是一维的模曲线，所以有上同调可用；$n\\ge3$ 时对应的空间不再是簇。",
    question="Shimura 簇到底是什么，为什么它只在部分情形存在？",
    definition={
        "text": "$\\GL(2)$ 情形：$X=\\GL(2,\\bbQ)Z(\\bbA)\\backslash\\GL(2,\\bbA)/\\sO(2)K_{\\mathrm f}$ 分类带水平结构的椭圆曲线，是一维代数曲线（模曲线）。一般地，Shimura 簇是某个约化群 $G$ 的对称空间上的商，分类带水平结构的阿贝尔簇（或更一般的 motive）。它存在的前提是 $G$ 的对称空间是 Hermitian 对称空间，这要求 $G$ 的类型属于特定几族。",
        "notation": "$\\sO(2)$ 是 $\\GL(2,\\bbR)$ 的极大紧子群；$K_{\\mathrm f}=\\prod_p K_p$ 水平结构；$X_\\Gamma=\\Gamma\\backslash X$。",
    },
    key_points=[
        "Shimura 簇的存在性是**群论条件**：等价于 $G$ 的对称空间是 Hermitian 的；$\\GL(n)$ 只有在 $n=2$ 时满足（此时对称空间是 $\\he$）。",
        "$n=2$ 时它是曲线（一维），$H^1$ 的秩恰是 $2$；$n=3$ 时对称空间是 $\\GL(3,\\bbR)/(\\sO(3)\\cdot\\bbR_{>0})$，维数 $5$，不是 Hermitian 对称空间。",
        "没有 Shimura 簇不等于没有自守侧：自守形式仍定义在 $\\GL(n,\\bbQ)\\backslash\\GL(n,\\bbA)$ 上，缺的是「能取上同调的几何对象」。",
    ],
    formulas=[
        "$X=\\GL(2,\\bbQ)Z(\\bbA)\\backslash\\GL(2,\\bbA)/\\sO(2)K_{\\mathrm f}$ 为一维模曲线",
        "$\\dim\\,\\GL(n,\\bbR)/(\\sO(n)\\cdot\\bbR_{>0})=\\frac{n(n-1)}{2}$",
    ],
    theorems=[
        {
            "name": "模曲线的代数性",
            "statement": "$X$ 作为带水平结构的椭圆曲线模空间，具有定义在 $\\bbQ$ 上的代数曲线结构，故可用平展上同调。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文直接使用这个结论（「模空间」），没有证明；这是模形式几何理论的标准结果。",
            },
            "source": "A p.14",
        },
    ],
    pitfalls=[
        "Shimura 簇不是「所有 $G$ 的对称空间」：一般 $G$ 的对称空间只是 Riemann 对称空间，没有复结构，取不了代数簇的上同调。",
        "「模曲线是一维的」与「$\\GL(2)$ 是二维群」容易混淆：维数说的是簇的维数 $1$，不是群的维数 $2$。",
    ],
    related=["goresky04/concept/eichler-shimura-theorem", "goresky04/concept/obstruction-n-ge-3", "goresky04/concept/geometric-langlands"],
    sources=[src([14, 15], "A p.14", "§7.1–§7.2")],
    provenance_note="对应原文 §7.1 对模曲线的引用与 §7.2 对 $n\\ge3$ 的对照；Hermitian 对称空间一条是把原文「所需的 Shimura 簇不存在」讲开，属译者按。",
)

C["concepts/obstruction-n-ge-3"] = card(
    "concepts", "obstruction-n-ge-3",
    title="$n\\ge3$ 的障碍：Shimura 簇不存在",
    aliases=["障碍", "obstruction", "$n\\ge3$", "五维流形"],
    track="C",
    summary="对 $n\\ge3$，对应的 Shimura 簇不存在，模空间那一侧整个失效；原文说「这是本领域最大的谜团之一」。",
    question="为什么把 $n=2$ 的证明照搬到 $n\\ge3$ 会失效？",
    definition={
        "text": "原文对 $n=3$ 写出类似的对象 $\\GL(3,\\bbQ)Z(\\bbA)\\backslash\\GL(3,\\bbA)/\\sO(3)K_{\\mathrm f}$，并指出它「根本不是代数簇，事实上它是一个（实）五维流形」。原因是：$\\GL(3,\\bbR)/(\\sO(3)\\cdot\\bbR_{>0})$ 的维数是 $3\\cdot2/2=3$，加上中心与紧子群后得到的商空间没有复结构。没有代数簇就没有平展上同调，Eichler–Shimura 的整条路线断掉。",
        "notation": "$\\sO(3)$ 为 $\\GL(3,\\bbR)$ 的极大紧子群；$K_{\\mathrm f}=\\prod_p\\GL(3,\\bbZ_p)$。",
    },
    key_points=[
        "缺的不是「信心」而是**几何对象**：$n=2$ 的证明是从模曲线的上同调读出 Galois 表示，$n\\ge3$ 没有这个曲线。",
        "这不是技术困难，是结构性障碍：$\\GL(n,\\bbR)$ 的对称空间是 Hermitian 的当且仅当 $n=2$（对 $\\GL(n)$ 而言）。",
        "几何朗兰兹的动机之一就是绕开这个障碍：不找 Shimura 簇，改在 $\\Bun_G$ 上做几何（见 D 轨）。",
    ],
    formulas=[
        "$\\GL(3,\\bbQ)Z(\\bbA)\\backslash\\GL(3,\\bbA)/\\sO(3)K_{\\mathrm f}$：实五维流形，非代数簇",
        "$\\dim\\,\\GL(3,\\bbR)/(\\sO(3)\\cdot\\bbR_{>0})=3$，加上中心与水平结构后总维数 $5$",
    ],
    theorems=[
        {
            "name": "障碍（原文的观察）",
            "statement": "对 $n\\ge3$，$\\GL(n)$ 的对称空间不是 Hermitian 对称空间，因此不存在与 $n=2$ 同类型的 Shimura 簇；Eichler–Shimura 路线不能直接推广。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "算对称空间维数 $\\dim\\GL(n,\\bbR)/(\\sO(n)\\cdot\\bbR_{>0})=n(n-1)/2$。", "why": "维数是判断是否 Hermitian 的第一步。"},
                    {"no": 2, "text": "Hermitian 对称空间的复维数等于实维数的一半，且要求存在复结构。", "why": "这是 Hermitian 的定义。"},
                    {"no": 3, "text": "$n\\ge3$ 时该空间不是 Hermitian 的（$\\GL(n)$ 的类型不属于 Hermitian 族），故没有 Shimura 簇。", "why": "得到障碍。"},
                ],
                "gap_note": "原文只写「根本不存在所需的 Shimura 簇」并称其为谜团；本卡按对称空间理论补出原因，原文没有展开。",
            },
            "source": "A p.14",
        },
    ],
    pitfalls=[
        "「$n\\ge3$ 没有 Shimura 簇」不等于「$n\\ge3$ 没有自守表示」：自守侧完全存在，缺的只是几何载体。",
        "不要以为换个群就能绕开：原文 §8 说换群、换域、换范畴，但这已经离开「$\\GL(n)$ 的原始猜想」，进入函子性与几何朗兰兹。",
    ],
    related=["goresky04/concept/shimura-variety", "goresky04/concept/eichler-shimura-theorem", "goresky04/concept/geometric-langlands"],
    sources=[src([14, 15], "A p.14", "§7.2")],
    provenance_note="对应原文 §7.2 全节；维数计算与 Hermitian 判据是译者按标准对称空间理论补的，原文只说结论。",
)

D = {}

D["derivations/hecke-to-frobenius"] = card(
    "derivations", "hecke-to-frobenius",
    title="把 Hecke 特征值对上 Frobenius 特征值",
    aliases=["特征值对应", "L 函数相等", "逐素数比较"],
    track="C",
    summary="在非分歧素数 $p$ 处，自守侧的 Satake 参数 $\\alpha_1,\\dots,\\alpha_n$ 与 Galois 侧 $\\Fr_p$ 的特征值 $\\beta_1,\\dots,\\beta_n$ 逐一相等，于是两个局部因子相等、两个 $L$ 函数相等。",
    question="「Frobenius 特征值 = Hecke 特征值」这句话在技术上到底是怎么落实的？",
    goal="把 $L(\\rho,s)=L(\\pi,s)$ 归结为每个非分歧 $p$ 处两组特征值的相等。",
    setup=[
        "$\\rho$ 在 $p$ 处非分歧，$\\Fr_p$ 有特征值 $\\beta_1,\\dots,\\beta_n$，$L_p(\\rho,s)=\\prod_i(1-\\beta_ip^{-s})^{-1}$。",
        "$\\pi$ 在 $p$ 处非分歧，有 Satake 参数 $\\alpha_1,\\dots,\\alpha_n$，$L_p(\\pi,s)=\\prod_i(1-\\alpha_ip^{-s})^{-1}$。",
        "$\\zeta_p(\\rho,t)=1/\\det(I-t\\Fr_p)$，$t=p^{-s}$。",
    ],
    steps=[
        {"no": 1, "text": "写出 Galois 侧局部因子 $L_p(\\rho,s)=\\det(I-p^{-s}\\Fr_p)^{-1}$。", "why": "这是 (4.4.1) 的直接改写。", "locator": "A p.7", "provenance": "A"},
        {"no": 2, "text": "写出自守侧局部因子 $L_p(\\pi,s)=\\prod_i(1-\\alpha_ip^{-s})^{-1}$。", "why": "Satake 参数的定义就是让这个乘积成立。", "locator": "A p.13", "provenance": "A"},
        {"no": 3, "text": "断言两组特征值作为无序组相等：$\\{\\beta_i\\}=\\{\\alpha_i\\}$。", "why": "这是 (2.0.2) 的精确含义，也是猜想的核心内容。", "locator": "A p.1", "provenance": "A"},
        {"no": 4, "text": "于是对所有非分歧 $p$，局部因子相等；由欧拉乘积的唯一性，整体 $L$ 函数相等。", "why": "完成 (2.0.2) 到 $L(\\rho,s)=L(\\pi,s)$ 的过渡。", "locator": "A p.7", "provenance": "B"},
        {"no": 5, "text": "分歧处需要另加导子与 $\\varepsilon$ 因子，两侧的导子也要相等；本文不处理这一层。", "why": "说明「相等」在有限个素数处要单独规定。", "locator": "A p.7", "provenance": "B"},
    ],
    result="猜想的算术内容是：逐素数地，$\\Fr_p$ 与 $T_p$ 的特征多项式相等。这个等式一旦成立，$L$ 函数相等就是形式推论。",
    gaps=["步 3 是猜想本身，不是可证的步骤；本卡只是把它拆成可检验的形式。"],
    pitfalls=[
        "特征值是**无序组**：$\\Fr_p$ 的共轭类只给出无序特征值组，Satake 参数也模 $W$，两边都无序才对得上。",
        "整体 $L$ 函数相等**不能**推出逐素数相等（可能相差有限个因子）；本文的猜想是逐素数陈述，更强。",
    ],
    related=["goresky04/concept/satake-parameter", "goresky04/concept/frobenius-element", "goresky04/deriv/local-zeta-factor"],
    sources=[src([1, 1], "A p.1", "§2"), src([13, 13], "A p.13", "§6.4")],
    provenance_note="步 1–3 对应原文 (2.0.2) 与 §6.4；步 4–5 的「欧拉乘积唯一性」与「分歧处另设」是译者按，原文未写。",
)

D["derivations/eichler-shimura-decomposition"] = card(
    "derivations", "eichler-shimura-decomposition",
    title="$n=2$：上同调分解给出 Galois 表示（(7.1.1)）",
    aliases=["(7.1.1)", "上同调分解", "Eichler–Shimura 分解"],
    track="C",
    summary="抛物上同调 $H^1_P(X,E_k;\\bbQ)\\otimes\\bbC$ 分解为 $S_k\\oplus\\overline{S_k}$，每个尖点特征形式贡献一个 $2$ 维 Galois 表示，这就是 $n=2$ 的对应。",
    question="从模形式到 Galois 表示，具体走的是哪条上同调、哪一步给出 $2$ 维？",
    goal="说明 (7.1.1) 如何把每个 Hecke 特征形式变成一个 $2$ 维 Galois 表示，并使 $L$ 函数相等。",
    setup=[
        "$X$ 为模曲线 $\\GL(2,\\bbQ)Z(\\bbA)\\backslash\\GL(2,\\bbA)/\\sO(2)K_{\\mathrm f}$。",
        "$E_k$ 为 $X$ 上权 $k$ 的局部系数系（来自对称幂）。",
        "$H^1_P$ 为抛物上同调，即 $H^1$ 商掉 Eisenstein 部分。",
    ],
    steps=[
        {"no": 1, "text": "在 $X$ 上取局部系数系 $E_k$，算 $H^1_P(X,E_k;\\bbQ)\\otimes\\bbC$。", "why": "上同调的系数要带上权，才能看到 $S_k$。", "locator": "A p.14", "provenance": "A"},
        {"no": 2, "text": "证明它同构于 $S_k\\oplus\\overline{S_k}$：每个特征形式 $f$ 贡献一个复共轭对。", "why": "这是 (7.1.1) 的内容，把分析对象放进上同调。", "locator": "A p.14", "provenance": "A"},
        {"no": 3, "text": "Hecke 算子作用在上同调上并与 Galois 作用交换，故可同时分解。", "why": "分解出的每个成分既是 Hecke 特征空间，又是 Galois 不变子空间。", "locator": "A p.14", "provenance": "B"},
        {"no": 4, "text": "每个成分是 $2$ 维的（曲线 $H^1$ 的秩），于是在其上得到 $2$ 维 Galois 表示 $\\rho_f$。", "why": "$n=2$ 的关键：$2$ 维恰好对上 $\\GL(2)$。", "locator": "A p.14", "provenance": "A"},
        {"no": 5, "text": "逐素数比较 $\\Fr_p$ 与 $T_p$ 的特征多项式，得 $L(\\rho_f,s)=L(f,s)$。", "why": "完成 (2.0.2) 的验证。", "locator": "A p.14", "provenance": "B"},
    ],
    result="$n=2$ 的朗兰兹对应被实现为「模曲线上同调的尖点成分」，对应是构造性的，$L$ 函数相等可以逐素数核对。",
    gaps=["步 1–2 的证明（比较定理与上同调分解）原文没有给出，只写结论 (7.1.1)。"],
    pitfalls=[
        "必须用抛物上同调：完整的 $H^1$ 含 Eisenstein 部分，那部分对应诱导表示，不属于尖点自守表示。",
        "复共轭对 $\\overline{S_k}$ 不能省：$H^1$ 是 $\\bbQ$ 系数，复化后自然带共轭结构，$f$ 与 $\\bar f$ 成对出现。",
    ],
    related=["goresky04/concept/eichler-shimura-theorem", "goresky04/concept/shimura-variety", "goresky04/deriv/hecke-to-frobenius"],
    sources=[src([14, 14], "A p.14", "§7.1")],
    provenance_note="步 1–2、4 对应原文 (7.1.1) 与说明；步 3、5 是把原文「Eichler 与 Shimura 证明了」展开成可读的推理，标 B 级。",
)

F = {}

F["concepts/geometric-langlands"] = card(
    "concepts", "geometric-langlands",
    title="几何朗兰兹：把猜想搬到曲线上",
    aliases=["geometric Langlands", "几何朗兰兹", "$\\Bun_G$", "Hecke 特征层"],
    track="D",
    summary="把 $\\bbQ$ 换成曲线 $C$ 的函数域，把「Galois 表示」换成 $C$ 上的 $G$-丛与局部系统，把「自守表示」换成 $\\Bun_G$ 上的层，得到几何版的对应。",
    question="几何朗兰兹换掉的是哪几样东西，为什么这样换能绕开 $n\\ge3$ 的障碍？",
    definition={
        "text": "设 $C$ 为 $\\bbF_q$ 上的光滑射影曲线，$G$ 为约化群。几何朗兰兹猜测：$C$ 上 $G^\\vee$-局部系统与 $\\Bun_G$（$G$-丛的模栈）上满足 Hecke 特征条件的 $\\Ql$-层（Hecke 特征层）之间存在对应，使每个局部系统 $E$ 对应一个层 $\\mathcal F_E$，且 $\\mathcal F_E$ 是每个 Hecke 算子 $\\mathbb H_V$ 的特征层，特征值为 $E$ 的相应数据。",
        "notation": "$\\Bun_G$ 为 $G$-丛模栈；$G^\\vee$ 为对偶群；$\\mathbb H_V$ 为沿 $\\mathrm{Gr}_{G,V}$ 的 Hecke 算子；$\\mathcal F_E$ 为 Hecke 特征层。",
    },
    key_points=[
        "换的三样：底域（$\\bbQ$ → 曲线函数域）、左侧（Galois 表示 → 局部系统）、右侧（$\\GL(n)$ 的自守表示 → $\\Bun_G$ 上的层）。",
        "绕开障碍的机制：不再需要 Shimura 簇。$\\Bun_G$ 对任意 $G$ 都存在，是无穷维栈，直接在它上面做层论。",
        "$n=2$ 的经典对应是几何对应的「$\\bbQ$ 影子」：模曲线上的 Hecke 特征层可以看成 $\\Bun_{\\GL(2)}$ 上的层在有限域上的痕迹。",
        "本文 §8.5 只有标题、正文为空；作者在引言里说「几个月后再来看空节有没有补上」，但这一节直到本文定稿仍是空的。",
    ],
    formulas=[
        "$\\mathbb H_V\\colon \\mathcal D(\\Bun_G)\\to\\mathcal D(\\Bun_G\\times C)$，$\\mathcal F_E\\mapsto E\\boxtimes\\mathcal F_E$",
        "$\\mathcal F_E$ 是 Hecke 特征层：$\\mathbb H_V(\\mathcal F_E)\\cong E_V\\boxtimes\\mathcal F_E$",
    ],
    theorems=[
        {
            "name": "几何朗兰兹猜想（本文未陈述）",
            "statement": "$C$ 上 $G^\\vee$-局部系统与 $\\Bun_G$ 上的 Hecke 特征层之间存在对应；在 $G=\\GL(n)$ 且 $C$ 为椭圆曲线时，这与经典对应一致。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文 §8.5 正文为空，只留标题；本卡的陈述按标题与 §8.1 的一般形式补出，属译者按（B 级），不是原文内容。",
            },
            "source": "B p.15",
        },
    ],
    pitfalls=[
        "几何朗兰兹不是「把朗兰兹翻译成几何语言」：它改变的是底域（数域 → 函数域），因此它是**另一个猜想**，不是同一个猜想的重述。",
        "不要把它与「$p$ 进朗兰兹」「局部朗兰兹」混为一谈：那些仍在数域上，几何朗兰兹在曲线上。",
        "本文没有给出几何朗兰兹的任何内容：§8.5 是空的。读到这里应当把它当成「作者指了一个方向」，而不是「作者讲了这个方向」。",
    ],
    related=["goresky04/concept/obstruction-n-ge-3", "goresky04/concept/dual-group", "goresky04/concept/functoriality"],
    sources=[src([15, 16], "B p.15", "§8.5（原文正文空缺）"), src([1, 1], "A p.1", "§1")],
    provenance_note="原文 §8.5 只有标题。本卡的定义与陈述按标题、§8.1 的一般形式、以及库内已译的 SY02-40/SY02-38/SY99-04 补出，属 B 级译者按；不冒充原文。",
)

F["concepts/functoriality"] = card(
    "concepts", "functoriality",
    title="函子性：换群的那条路",
    aliases=["functoriality", "函子性", "Langlands 函子性"],
    track="D",
    summary="若两个群的对偶群之间有同态 ${}^{L}H\\to{}^{L}G$，则 $H$ 的自守表示应当「转移」为 $G$ 的自守表示；这是朗兰兹猜想的主干推广。",
    question="函子性为什么被称为「主干推广」，它与原猜想是什么关系？",
    definition={
        "text": "设 $H,G$ 为约化群，${}^{L}H\\to{}^{L}G$ 为 $L$-群之间的同态。函子性猜测：对 $H$ 的每个自守表示 $\\pi$，存在 $G$ 的自守表示 $\\Pi$（称为 $\\pi$ 的转移），使两者的 $L$ 函数满足 $L(\\Pi,s)=L(\\pi,\\rho\\circ\\varphi,s)$，其中 $\\varphi$ 是 $L$-群同态、$\\rho$ 是 $G$ 的有限维表示。当 $H=\\GL(n)$、$G=\\GL(m)$ 时，这给出对称幂与张量积的 $L$ 函数。",
        "notation": "${}^{L}G=G^\\vee\\rtimes\\Gal(\\Qbar/\\bbQ)$ 为 $L$-群；$\\varphi\\colon{}^{L}H\\to{}^{L}G$；$\\Pi$ 记转移。",
    },
    key_points=[
        "原猜想是函子性在 $H=\\GL(1)$（或 $H$ 平凡）、$G=\\GL(n)$ 时的特例；函子性把「一个群」的对应推广成「群之间」的对应。",
        "函子性给出 $L$ 函数的**运算**：对称幂、张量积、外幂都可以通过选不同的 $L$-群同态得到。",
        "它比原猜想更难，也更值钱：很多具体 $L$ 函数的解析性质（如对称平方的整纯性）靠它。",
        "本文 §8.6 只有标题；作者在引言里把函子性列为「其它群」的一部分，但没有展开。",
    ],
    formulas=[
        "$\\varphi\\colon{}^{L}H\\to{}^{L}G$ 诱导 $\\pi\\mapsto\\Pi$，$L(\\Pi,s)=L(\\pi,\\rho\\circ\\varphi,s)$",
        "$H=\\GL(n),\\ G=\\GL(\\mathrm{Sym}^2)$ 时给出对称平方 $L$ 函数",
    ],
    theorems=[
        {
            "name": "函子性猜想（本文未陈述）",
            "statement": "每个 $L$-群同态 ${}^{L}H\\to{}^{L}G$ 应当诱导自守表示的转移，并使相应的 $L$ 函数相等。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文 §8.6 正文为空；本卡按标题与 [Ar][F] 的通行陈述补出，属 B 级译者按。",
            },
            "source": "B p.15",
        },
    ],
    pitfalls=[
        "函子性不是「群同态诱导表示」这么简单：自守表示不是有限群的表示，转移的存在性是猜想。",
        "不是每个 $L$-群同态都有转移：需要同态来自代数群的同态（或至少是「好的」同态），否则陈述不成立。",
    ],
    related=["goresky04/concept/dual-group", "goresky04/concept/geometric-langlands", "goresky04/concept/langlands-conjecture-statement"],
    sources=[src([15, 16], "B p.15", "§8.6（原文正文空缺）")],
    provenance_note="原文 §8.6 只有标题；陈述按 [Ar][F] 补，属 B 级译者按。",
)

F["concepts/dual-group"] = card(
    "concepts", "dual-group",
    title="对偶群与 $L$-群",
    aliases=["dual group", "对偶群", "L-group", "${}^{L}G$"],
    track="D",
    summary="对偶群 $G^\\vee$ 由 $G$ 的根数据（把根与余根互换）决定；加上 Galois 作用得到 $L$-群 ${}^{L}G$，它是朗兰兹对应里「左侧」的群。",
    question="对偶群是怎么从 $G$ 造出来的，为什么它出现在猜想的左侧？",
    definition={
        "text": "设 $G$ 为约化群，取极大环面 $T$ 与根系 $\\Phi\\subset X^*(T)$、余根系 $\\Phi^\\vee\\subset X_*(T)$。把这两组数据互换（$X^*\\leftrightarrow X_*$，$\\Phi\\leftrightarrow\\Phi^\\vee$），得到一个新的根数据，它对应的复约化群就是 $G^\\vee$。例如 $\\GL(n)^\\vee=\\GL(n)$，$\\SL(n)^\\vee=\\PGL(n)$，$\\mathrm{Sp}(2n)^\\vee=\\SO(2n+1)$。再加上 Galois 群在根数据上的作用，得到 $L$-群 ${}^{L}G=G^\\vee\\rtimes\\Gal(\\Qbar/\\bbQ)$。",
        "notation": "$X^*(T)$ 特征标格；$X_*(T)$ 余特征标格；$W$ 外尔群；${}^{L}G$ 记 $L$-群。",
    },
    key_points=[
        "对偶群的构造是**纯组合**的：只用到根数据，与 $G$ 的具体实现无关；这解释了为什么它可以出现在纯算术的猜想里。",
        "自对偶的例子（$\\GL(n)$、$\\SO(2n)$、$\\mathrm{Sp}(2n)$ 的某些形式）让 $\\GL(n)$ 的情形看起来「两边是同一个群」，但一般情形两边不同。",
        "对偶群把「群」与「表示」对偶起来：$G^\\vee$ 的有限维表示正是构造 $L$ 函数所需的原料。",
        "$L$-群里的半直积（$\\rtimes$）不能省：Galois 作用编码了分歧与扭曲，去掉它就只能处理「无扭曲」的对应。",
    ],
    formulas=[
        "$\\Phi\\subset X^*(T)$ 与 $\\Phi^\\vee\\subset X_*(T)$ 互换，得到 $G^\\vee$ 的根数据",
        "${}^{L}G=G^\\vee\\rtimes\\Gal(\\Qbar/\\bbQ)$",
    ],
    theorems=[
        {
            "name": "对偶群的组合构造（本文未陈述）",
            "statement": "根数据的对偶仍是一个根数据，故对应一个复约化群 $G^\\vee$；$G$ 与 $G^\\vee$ 的根系互为对偶。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文 §8.2 只有标题；本卡按根数据的标准理论补出，属 B 级译者按。",
            },
            "source": "B p.15",
        },
    ],
    pitfalls=[
        "$\\GL(n)^\\vee=\\GL(n)$ 会让人误以为对偶群总是自己：$\\SL(n)^\\vee=\\PGL(n)$ 才是常态。",
        "对偶群不是「Pontryagin 对偶」：这里是根数据的对偶，与局部紧群的字符群无关（名字撞车而已）。",
    ],
    related=["goresky04/concept/functoriality", "goresky04/concept/geometric-langlands", "goresky04/concept/langlands-conjecture-statement"],
    sources=[src([15, 16], "B p.15", "§8.2（原文正文空缺）")],
    provenance_note="原文 §8.2 只有标题；构造与例子按标准根数据理论补，属 B 级译者按。",
)


if __name__ == "__main__":
    CARDS.update(C)
    CARDS.update(D)
    CARDS.update(F)
    print("wrote", write_cards({**C, **D, **F}))
