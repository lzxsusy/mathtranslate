#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cards_deriv.py —— 推导卡（跨轨的「怎么算出来」）。"""
from gen_cards import CARDS, card, src, PKG, write_cards

R = {}

R["derivations/nearby-cycles-to-central"] = card(
    "derivations", "nearby-cycles-to-central",
    title="从附近循环造出中心函子，并证明它 $t$-正合",
    aliases=["Z 的构造", "why Z is t-exact", "中心函子推导"],
    track="A",
    summary="把 $Z(\\mathcal F)=\\Psi_f(\\mathcal F\\boxtimes k_{\\mathbb C^\\times}[1])$ 拆成「张量一个常层」与「附近循环」两步：前者显然 $t$-正合，后者由命题 2.2.2(2) 提供 $t$-正合性。",
    question="中心函子的 $t$-正合性，究竟由哪条性质、在哪一步用上？",
    goal="从 $\\Psi_f$ 的定义与五条性质，推出 $Z$ 是反常 $t$-正合的幺半函子。",
    setup=[
        "$\\mathrm{Gr}^{\\mathrm{cen}}_G$ 带正则映射 $f$，一般纤维 $\\mathrm{Gr}_G\\times\\mathbb C^\\times$、特殊纤维 $\\mathrm{Fl}_G$（§2.3）。",
        "$\\Psi_f\\colon\\mathcal D^b_c(X^\\times)\\to\\mathcal D^b_c(X^0)$，$\\mathcal F\\mapsto(i^*j_*\\exp_{X*}\\exp_X^*\\mathcal F)[-1]$（定义 2.2.1）。",
        "命题 2.2.2：(1) 保可构造；(2) perverse $t$-正合；(3) 光滑基变换；(4) 紧合基变换；(5) 投影的常层特殊化为原层。",
    ],
    steps=[
        {
            "no": 1,
            "text": "先看 $\\mathcal F\\mapsto\\mathcal F\\boxtimes k_{\\mathbb C^\\times}[1]$：它在 $\\mathrm{Gr}_G\\times\\mathbb C^\\times$ 上把反常层映到「反常层张量常层的一次平移」，是 $t$-正合的。",
            "why": "常层 $k_{\\mathbb C^\\times}[1]$ 是 perverse 的（$\\mathbb C^\\times$ 是 $1$ 维光滑，$[1]$ 恰把它摆到反常次数 $0$），与它作外积不改变反常 $t$-结构。",
            "locator": "A p.3",
            "provenance": "A",
        },
        {
            "no": 2,
            "text": "再取 $\\Psi_f$：由命题 2.2.2(2)，$\\Psi_f$ 本身 perverse $t$-正合，故两步复合仍 $t$-正合，得 $Z$ 的 (2)。",
            "why": "这是唯一需要「非平凡输入」的一步：$\\Psi_f$ 的 $t$-正合性不是自动的，正因为 $\\exp_X$ 不是代数映射（脚注 4），才要单独立命题。",
            "locator": "A p.3–4",
            "provenance": "A",
        },
        {
            "no": 3,
            "text": "幺半性：对 $\\mathcal F,\\mathcal G$ 用定义与 $\\Psi_f$ 的乘法性质，把 $Z(\\mathcal F)\\star_I Z(\\mathcal G)$ 与 $Z(\\mathcal F\\star\\mathcal G)$ 都化成对 $\\mathcal F\\boxtimes\\mathcal G$ 的一次附近循环，再用卷积的紧合基变换对齐。",
            "why": "原文把 (1) 归给「与 (5) 同法」，核心工具是命题 2.2.2(3)(4) 的两种基变换。",
            "locator": "A p.4",
            "provenance": "A",
        },
        {
            "no": 4,
            "text": "结论：$Z$ 是 $t$-正合幺半函子；「像落在中心」(3) 另需一句「卷积可交换」的直接验证，原文未展开。",
            "why": "(1)(2) 到这里就证完了；(3)(4) 是额外结构，本推导不覆盖。",
            "locator": "A p.4",
            "provenance": "A",
        },
    ],
    result="$Z$ 的 $t$-正合性 = 「张量常层」的显然 $t$-正合性 $\\circ$ 命题 2.2.2(2)；幺半性 = 两次基变换。",
    gaps=["(3) 落在中心、(4) 两次卷积仍反常，原文均只作断言；本推导只覆盖 (1)(2) 的链条。"],
    pitfalls=[
        "把 $[1]$ 平移漏掉：$k_{\\mathbb C^\\times}$ 不经 $[1]$ 不是 perverse 的，第一步就不再 $t$-正合。",
        "$\\Psi_f$ 的 $t$-正合性方向是「反常 → 反常」，不是「通常 $t$-结构 → 通常 $t$-结构」；两者不可混用。",
    ],
    related=[
        f"{PKG}/concept/nearby-cycles",
        f"{PKG}/concept/gaitsgory-central-functor",
        f"{PKG}/deriv/wakimoto-multiplicity",
    ],
    sources=[src([2, 4], "A p.4", "§2.2、§2.4")],
    provenance_note="$\\Psi_f$ 的性质在 p.2–3，$Z$ 的定义与定理 2.4.1 在 p.3–4；本推导把定理证明中分散的依据串成一条链。",
)

R["derivations/wakimoto-multiplicity"] = card(
    "derivations", "wakimoto-multiplicity",
    title="Wakimoto 滤链的重数如何变成 $\\dim V_\\lambda$",
    aliases=["重数公式", "multiplicity = dim V_λ", "2.5.3 到 4.5.1"],
    track="C",
    summary="定理 2.5.3 说 $Z(\\mathrm{Sat}(V))$ 的 Wakimoto 滤链里 $\\mathbb W_\\lambda$ 的重数是 $V$ 的 $\\lambda$-权维数；定理 4.5.1 说平均之后 $\\Delta^{\\mathrm{IW}}_\\lambda$ 与 $\\nabla^{\\mathrm{IW}}_\\lambda$ 的重数也是 $\\dim V_\\lambda$——中间差一个 $\\mathrm{Av}^{\\mathrm{IW}}$ 保持重数的论证。",
    question="两个重数公式长得一样，凭什么说后者是前者的推论？",
    goal="把 §2.5 的 Wakimoto 重数公式沿 $\\mathrm{Av}^{\\mathrm{IW}}$ 搬运到 §4.5 的 IW 标准/余标准重数公式。",
    setup=[
        "定理 2.5.3：$[Z(\\mathcal F):\\mathbb W_\\lambda]=\\dim(\\mathrm{Sat}^{-1}(\\mathcal F))_\\lambda$。",
        "定理 4.4.1 证明中的 (6)：$\\mathrm{Av}^{\\mathrm{IW}}(\\Delta_w)\\cong\\Delta^{\\mathrm{IW}}_\\lambda$、$\\mathrm{Av}^{\\mathrm{IW}}(\\nabla_w)\\cong\\nabla^{\\mathrm{IW}}_\\lambda$，$\\lambda$ 由 $W\\cdot w=W\\cdot w_\\lambda$ 定。",
        "定理 4.5.1 要证：$(Z^{\\mathrm{IW}}(V):\\Delta^{\\mathrm{IW}}_\\lambda)=(Z^{\\mathrm{IW}}(V):\\nabla^{\\mathrm{IW}}_\\lambda)=\\dim V_\\lambda$。",
    ],
    steps=[
        {
            "no": 1,
            "text": "取 $Z(\\mathrm{Sat}(V))$ 的一条 Wakimoto 滤链：每一层商是 $\\mathbb W_{\\lambda_i}$，出现次数由定理 2.5.3 给出 $=\\dim V_{\\lambda_i}$。",
            "why": "这是重数信息的出发点；滤链存在性由定理 2.5.3(1)。",
            "locator": "A p.5",
            "provenance": "A",
        },
        {
            "no": 2,
            "text": "把 $\\mathrm{Av}^{\\mathrm{IW}}$ 作用到整条滤链上：它是反常 $t$-正合的加法函子，故把 $0\\to\\mathcal F_{i-1}\\to\\mathcal F_i\\to\\mathbb W_{\\lambda_i}\\to0$ 送到 IW 中的短正合列，商为 $\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_{\\lambda_i})$。",
            "why": "$t$-正合性是定理 4.4.1(1)，正是它保证「滤链的商」在平均后仍是商。",
            "locator": "A p.10",
            "provenance": "A",
        },
        {
            "no": 3,
            "text": "由式 (6)，$\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_{\\lambda_i})$ 在 $K_0$ 中等于 $\\Delta^{\\mathrm{IW}}_{\\lambda_i}$（原文在 (7) 之后明说「$\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$ 与 $\\Delta^{\\mathrm{IW}}_\\lambda$ 不同构，但在 $K_0$ 中相等」）。",
            "why": "重数是 $K_0$ 层面的量，所以「不同构但同类」足够；若要倾斜性则需更强，那由定理 4.5.1 另证。",
            "locator": "A p.11–12",
            "provenance": "A",
        },
        {
            "no": 4,
            "text": "于是 $Z^{\\mathrm{IW}}(V)$ 的滤链商在 $K_0$ 中给出重数 $\\dim V_\\lambda$；再用 $\\nabla$ 侧同法（(6) 的第二式）得余标准重数相同，二者相等即得倾斜性所需的平衡。",
            "why": "标准重数 = 余标准重数是最高权范畴中倾斜的刻画。",
            "locator": "A p.11",
            "provenance": "A",
        },
    ],
    result="IW 侧重数公式 = 把 §2.5 的 Wakimoto 重数沿 $t$-正合的 $\\mathrm{Av}^{\\mathrm{IW}}$ 推到 $K_0$，再用式 (6) 把 $\\mathbb W_\\lambda$ 换成 $\\Delta^{\\mathrm{IW}}_\\lambda$。",
    gaps=[
        "「$\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$ 与 $\\Delta^{\\mathrm{IW}}_\\lambda$ 在 $K_0$ 中相等」原文只用一句带过，未给证明。",
        "定理 4.5.1 本身的证明（尤其拟极小情形）原文只给三步梗概，本推导用的是它的结论而非重证。",
    ],
    pitfalls=[
        "不能由 $K_0$ 中同类推出滤链商同构：滤链需要的是对象层面的短正合列，这正是为什么要先有 $t$-正合性。",
        "$\\lambda_i$ 是 Wakimoto 侧下标，$\\lambda$ 是 IW 侧下标，两者按同一个 $X^\\vee$ 对齐——若在 $T$ 与 $T^\\vee$ 之间取了对偶，重数会整体平移。",
    ],
    related=[
        f"{PKG}/concept/wakimoto-filtration",
        f"{PKG}/concept/central-tilting",
        f"{PKG}/concept/iw-averaging",
    ],
    sources=[src([5, 12], "A p.11", "§2.5、§4.5")],
    provenance_note="重数公式在 p.5（定理 2.5.3），$K_0$ 的说明在 p.12，平均函子的 $t$-正合性在 p.10。",
)

R["derivations/f1-monoidal"] = card(
    "derivations", "f1-monoidal",
    title="函子 I 为什么是幺半的",
    aliases=["F1 monoidal", "引理 3.2.1 推导"],
    track="B",
    summary="$F_1(V\\otimes k_{T^\\vee}(\\lambda))=Z(\\mathrm{Sat}(V))\\star_I\\mathbb W_\\lambda$ 的两条乘法来源：中心的交换性（定理 2.4.1(3)）与 Wakimoto 层的加法性（命题 2.5.2(3)）。",
    question="把 $V$ 的张量与 $\\lambda$ 的加法同时处理时，为什么两条乘法互不干扰？",
    goal="由定理 2.4.1(3) 与命题 2.5.2(3) 推出 $F_1(V\\otimes V'\\otimes k_{T^\\vee}(\\lambda+\\mu))\\cong F_1(V\\otimes k_{T^\\vee}(\\lambda))\\star_I F_1(V'\\otimes k_{T^\\vee}(\\mu))$。",
    setup=[
        "$\\mathrm{Sat}$ 是幺半等价：$\\mathrm{Sat}(V\\otimes V')\\cong\\mathrm{Sat}(V)\\star\\mathrm{Sat}(V')$。",
        "定理 2.4.1(3)：$Z(\\mathcal F)$ 与任意 $\\mathcal G\\in\\mathcal D^b_c(I\\backslash\\mathrm{Fl}_G)$ 在 $\\star_I$ 下交换。",
        "命题 2.5.2(3)：$\\mathbb W_\\lambda\\star_I\\mathbb W_\\mu\\cong\\mathbb W_{\\lambda+\\mu}$。",
    ],
    steps=[
        {
            "no": 1,
            "text": "左边：$F_1(V\\otimes V'\\otimes k_{T^\\vee}(\\lambda+\\mu))=Z(\\mathrm{Sat}(V\\otimes V'))\\star_I\\mathbb W_{\\lambda+\\mu}=Z(\\mathrm{Sat}(V)\\star\\mathrm{Sat}(V'))\\star_I\\mathbb W_{\\lambda+\\mu}$。",
            "why": "$\\mathrm{Sat}$ 幺半，$k_{T^\\vee}$ 的乘法是加法。",
            "locator": "A p.7",
            "provenance": "A",
        },
        {
            "no": 2,
            "text": "右边：$F_1(V\\otimes k(\\lambda))\\star_I F_1(V'\\otimes k(\\mu))=Z(\\mathrm{Sat}(V))\\star_I\\mathbb W_\\lambda\\star_I Z(\\mathrm{Sat}(V'))\\star_I\\mathbb W_\\mu$。",
            "why": "按定义展开。",
            "locator": "A p.7",
            "provenance": "A",
        },
        {
            "no": 3,
            "text": "用定理 2.4.1(3) 把 $\\mathbb W_\\lambda$ 与 $Z(\\mathrm{Sat}(V'))$ 交换，得 $Z(\\mathrm{Sat}(V))\\star_I Z(\\mathrm{Sat}(V'))\\star_I\\mathbb W_\\lambda\\star_I\\mathbb W_\\mu$。",
            "why": "中心性允许中心层穿过任意对象；$\\mathbb W_\\lambda$ 是 $I$-等变层，正在适用范围内。",
            "locator": "A p.7",
            "provenance": "A",
        },
        {
            "no": 4,
            "text": "再用 $Z$ 的幺半性（定理 2.4.1(1)）合并前两项，用命题 2.5.2(3) 合并后两项，得 $Z(\\mathrm{Sat}(V)\\star\\mathrm{Sat}(V'))\\star_I\\mathbb W_{\\lambda+\\mu}$，与第 1 步相同。",
            "why": "两次合并各用一条乘法，互不干扰；这就是「两条乘法可以正交使用」的含义。",
            "locator": "A p.7",
            "provenance": "A",
        },
    ],
    result="$F_1$ 的幺半性 = 中心性（把 $\\mathbb W$ 挪过去）+ $Z$ 幺半（合并）+ $\\mathbb W$ 加法（合并）。",
    gaps=["单位对象的兼容（$1\\mapsto\\mathcal O$ 型的自然同构）原文未提，本推导也未覆盖。"],
    pitfalls=[
        "交换的次序不能反：中心性说的是中心层可以穿过别的对象，而不是任意两个对象可交换。",
        "若把 $\\mathbb W_\\lambda$ 换成 $\\mathrm{Av}^{\\mathrm{IW}}(\\mathbb W_\\lambda)$ 再做同一推导，需要额外的 $t$-正合性输入，不能直接照搬。",
    ],
    related=[
        f"{PKG}/concept/functor-f1",
        f"{PKG}/concept/wakimoto-sheaves",
        f"{PKG}/concept/gaitsgory-central-functor",
    ],
    sources=[src([5, 7], "A p.7", "§3.2")],
    provenance_note="引理 3.2.1 在 p.7；所引的两条乘法分别在 p.4（定理 2.4.1(3)）与 p.5（命题 2.5.2(3)）。",
)

R["derivations/tannakian-algebra"] = card(
    "derivations", "tannakian-algebra",
    title="Tannakian 重构里的代数 $A$ 与 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$",
    aliases=["algebra A", "F2 的构造", "Tannakian formalism"],
    track="B",
    summary="先在对称幺半的非全子范畴 $\\mathcal C\\subset\\mathcal P_I^{\\mathrm{Wak}}$ 上取端环 $A$，得到 $H\\colon\\mathcal C\\cong A\\text{-}\\mathrm{mod}_{\\mathrm{free}}$；再把 $\\mathcal O(\\mathfrak g^\\vee)\\to A$（单值的对数）与 $\\mathcal O(X)\\to A$（Wakimoto 滤链）拼成 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$。",
    question="两个分量映射各自的数学来源是什么，为什么它们的合成会「唯一分解」出 $\\mathcal O(\\widehat{\\mathcal N}_X)$ 上的映射？",
    goal="说明 $F_1$ 的扩张为什么等价于造一个等变代数映射 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$，以及这个映射怎么造。",
    setup=[
        "脚注 10：$\\mathrm{Coh}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)$ 对称幺半，而 $\\mathcal P_I^{\\mathrm{Wak}}$ 不是；故需先换成对称幺半的非全子范畴 $\\mathcal C$。",
        "Tannakian 形式：存在 $H\\colon\\mathcal C\\xrightarrow{\\sim}A\\text{-}\\mathrm{mod}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}$，使 $F'_1$ 成为 $V\\mapsto V\\otimes A$。",
        "$\\mathcal O(\\widehat{\\mathcal N}_X)$ 是 $\\mathcal O(\\mathfrak g^\\vee)\\otimes\\mathcal O(X)$ 的商（因为 $\\widehat{\\mathcal N}_X\\subset\\mathfrak g^\\vee\\times X$ 是闭子概形）。",
    ],
    steps=[
        {
            "no": 1,
            "text": "取 $\\mathcal C$ 的端环 $A=\\mathrm{End}_{\\mathcal C}(\\mathbf 1)$ 型对象，用 Tannakian 形式把 $\\mathcal C$ 等同于自由 $A$-模范畴。",
            "why": "这是「张量范畴 ↔ 交换代数上的模范畴」的标准双向；$A$ 带 $G^\\vee\\times T^\\vee$ 作用来自 $\\mathcal C$ 的等变性。",
            "locator": "A p.7",
            "provenance": "A",
        },
        {
            "no": 2,
            "text": "造 $\\mathcal O(\\mathfrak g^\\vee)\\to A$：把它解释为附近循环的单值自同构的对数。",
            "why": "单值算子 $T$ 可写 $\\exp(N)$，$N$ 给出 $\\mathfrak g^\\vee$ 的作用；$Z$ 的构造本身就依赖 $\\Psi_f$，故这条映射在 $A$ 中有天然来源。",
            "locator": "A p.8",
            "provenance": "A",
        },
        {
            "no": 3,
            "text": "造 $\\mathcal O(X)\\to A$：由定理 2.5.3 的 Wakimoto 滤链给出——滤链的各级商 $\\mathbb W_\\lambda$ 在 $A$ 中给出坐标函数。",
            "why": "$X=\\mathrm{Spec}\\,\\mathcal O(G^\\vee/U^\\vee)$ 的函数环由权坐标生成，而 Wakimoto 滤链恰按 $\\lambda$ 分层。",
            "locator": "A p.8",
            "provenance": "A",
        },
        {
            "no": 4,
            "text": "把两者张量得 $\\mathcal O(\\mathfrak g^\\vee)\\otimes\\mathcal O(X)\\to A$，再用「$\\mathcal O(\\widehat{\\mathcal N}_X)$ 是该张量积的商」得唯一的分解 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$。",
            "why": "商上的映射由原环上「在关系上取零」的映射唯一决定；这正是原文「factors uniquely」的含义。",
            "locator": "A p.8",
            "provenance": "A",
        },
        {
            "no": 5,
            "text": "于是 $F_2(M)=M\\otimes_{\\mathcal O(\\widehat{\\mathcal N}_X)}A$，即沿环映射的换基。",
            "why": "换基函子自动是右正合、幺半的，故 $F_2$ 的幺半性不需要另证。",
            "locator": "A p.8",
            "provenance": "A",
        },
    ],
    result="$F_2$ = 沿 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$ 的换基；$A$ 由 $\\mathcal C$ 的 Tannakian 端环给出。",
    gaps=[
        "Tannakian 形式在此是黑箱：$\\mathcal C$ 具体取哪个子范畴、$A$ 的具体计算，原文都未给。",
        "「$\\mathcal O(\\mathfrak g^\\vee)\\to A$ 是单值的对数」「$\\mathcal O(X)\\to A$ 由 Wakimoto 滤链定」两句都只有一句解释，没有构造细节。",
    ],
    pitfalls=[
        "把 $A$ 与 $\\mathcal O(\\widehat{\\mathcal N}_X)$ 混同：前者是范畴的端环，后者是几何环，映射方向是几何 → 范畴。",
        "忽略「对称幺半」这个前提：$\\mathcal P_I^{\\mathrm{Wak}}$ 不对称，故必须先换到 $\\mathcal C$，否则 Tannakian 形式不适用。",
    ],
    related=[
        f"{PKG}/concept/functor-f2",
        f"{PKG}/concept/hat-n-x",
        f"{PKG}/concept/wakimoto-filtration",
    ],
    sources=[src([7, 8], "A p.8", "§3.3")],
    provenance_note="构造在 p.7，两条分量映射与「唯一分解」在 p.8，脚注 10 在 p.7。",
)

R["derivations/fully-faithful-hom"] = card(
    "derivations", "fully-faithful-hom",
    title="主定理的全忠实：$\\mathrm{Hom}$ 两边的显式计算",
    aliases=["Hom computation", "fully faithful proof", "式 (8)"],
    track="D",
    summary="把 (8) 用五引理化到生成元后，两边都算成同一个数：$n=0$ 时为 $\\dim V_{-\\lambda}$，否则为 $0$。",
    question="为什么只需验证 $\\mathcal F=\\mathcal O_{\\widetilde{\\mathcal N}}$ 与 $\\mathcal G=V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n]$ 这一种情形？",
    goal="由生成元情形推出 $F^{\\mathrm{IW}}$ 全忠实。",
    setup=[
        "引理 3.1.1：$\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$ 由 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 与 $V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$（$\\lambda\\in X^\\vee_+$）生成。",
        "引理 2.5.4：$\\mathcal P_I^{\\mathrm{Wak}}$ 对 $\\star_I$ 封闭。",
        "定理 4.5.1：$(Z^{\\mathrm{IW}}(V):\\Delta^{\\mathrm{IW}}_\\lambda)=\\dim V_\\lambda$。",
    ],
    steps=[
        {
            "no": 1,
            "text": "对 (8) 用五引理：只需对 $\\mathcal F,\\mathcal G$ 都是生成元的单项情形验证；由平移与 $\\oplus$ 的兼容，进一步归为 $\\mathcal F=\\mathcal O_{\\widetilde{\\mathcal N}}$、$\\mathcal G=V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n]$。",
            "why": "五引理把「任意两个对象的 $\\mathrm{Hom}$」化成「生成元的 $\\mathrm{Hom}$」，前提是知道 $F^{\\mathrm{IW}}$ 在短正合列上同调意义兼容。",
            "locator": "A p.12",
            "provenance": "A",
        },
        {
            "no": 2,
            "text": "左边：$\\mathrm{Hom}(\\mathcal O_{\\widetilde{\\mathcal N}},V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)[n])=\\Gamma(\\widetilde{\\mathcal N},V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda))[n]$，其维数在 $n=0$ 时是 $V$ 的 $-\\lambda$ 权空间、否则为 $0$。",
            "why": "$\\widetilde{\\mathcal N}$ 上整体截面即 $V$ 按权 $\\lambda$ 分解的部分（$\\lambda$ 支配故只取非负侧）。",
            "locator": "A p.12",
            "provenance": "A",
        },
        {
            "no": 3,
            "text": "右边：用 $F^{\\mathrm{IW}}(\\mathcal O_{\\widetilde{\\mathcal N}})=\\Delta^{\\mathrm{IW}}_0$、$F^{\\mathrm{IW}}(V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda))\\cong Z^{\\mathrm{IW}}(V)\\star_I\\mathbb W_\\lambda$ 代入，得 $\\mathrm{Hom}(\\Delta^{\\mathrm{IW}}_0,Z^{\\mathrm{IW}}(V)\\star_I\\mathbb W_\\lambda[n])$。",
            "why": "这两个像是式 (7) 的直接读出。",
            "locator": "A p.12",
            "provenance": "A",
        },
        {
            "no": 4,
            "text": "用伴随性把 $\\mathbb W_\\lambda$ 挪到左边：$\\cong\\mathrm{Hom}(\\Delta^{\\mathrm{IW}}_0\\star_I\\mathbb W_{-\\lambda},Z^{\\mathrm{IW}}(V)[n])$，再由命题 2.5.2 与式 (6) 化成 $\\mathrm{Hom}(\\Delta^{\\mathrm{IW}}_{-\\lambda},Z^{\\mathrm{IW}}(V)[n])$。",
            "why": "这一步是全篇最关键的两行代数操作：把「与 $\\mathbb W$ 作卷积」转成「标准层下标的平移」。",
            "locator": "A p.12",
            "provenance": "A",
        },
        {
            "no": 5,
            "text": "由定理 4.5.1，该 $\\mathrm{Hom}$ 的维数是 $Z^{\\mathrm{IW}}(V)$ 中 $\\Delta^{\\mathrm{IW}}_{-\\lambda}$ 的重数，即 $\\dim V_{-\\lambda}$（$n=0$）或 $0$。",
            "why": "重数公式在这里被当作「自由变量」使用：它把 IW 侧的重数直接读成表示侧的权维数。",
            "locator": "A p.12",
            "provenance": "A",
        },
        {
            "no": 6,
            "text": "两边数值相等，(8) 是全忠实；结合本质满射得定理 5.0.1。",
            "why": "全忠实 + 本质满射 = 等价。",
            "locator": "A p.12",
            "provenance": "A",
        },
    ],
    result="(8) 的左边 = $\\dim V_{-\\lambda}$（$n=0$）/ $0$；右边经伴随与式 (6) 化成同一重数，故 $F^{\\mathrm{IW}}$ 全忠实。",
    gaps=[
        "第 1 步的「五引理」需要 $F^{\\mathrm{IW}}$ 与三角结构的兼容性，原文只说「routine」；本推导未验证。",
        "第 2 步的截面计算原文说「not hard to check」，仅给结果。",
    ],
    pitfalls=[
        "式 (6) 的 $\\lambda$ 由 $W\\cdot w=W\\cdot w_\\lambda$ 定，而第 4 步用的是 $\\mathbb W_{-\\lambda}$ 的平移；符号一旦取反，重数就对到 $\\dim V_{\\lambda}$ 而不是 $\\dim V_{-\\lambda}$。",
        "「$n\\neq0$ 时为 0」靠的是 $\\widetilde{\\mathcal N}$ 上那些线丛只有 $0$ 阶截面；换成更高阶的 $[n]$ 就会与非零的 Ext 混淆。",
    ],
    related=[
        f"{PKG}/concept/functor-fiw",
        f"{PKG}/concept/central-tilting",
        f"{PKG}/concept/five-categories",
    ],
    sources=[src([12, 12], "A p.12", "§5")],
    provenance_note="式 (8) 与全部计算都在 p.12；本推导把原文四段压缩成六步并标出两处省略。",
)

if __name__ == "__main__":
    CARDS.update(R)
    print("wrote", write_cards(R))

R["derivations/iw-averaging-t-exact"] = card(
    "derivations", "iw-averaging-t-exact",
    title="平均函子为什么 $t$-正合：式 (5)(6) 的用法",
    aliases=["Av^IW t-exact", "定理 4.4.1 推导", "式 (5) 式 (6)"],
    track="C",
    summary="$\\mathrm{Av}^{\\mathrm{IW}}=\\Delta^{\\mathrm{IW}}_0\\star_I(-)$ 把标准层送到标准层、余标准层送到余标准层（式 (6)），并把非极小胞腔的单层打成零（式 (5)）；由反常 $t$-结构的「标准–余标准判别法」即得 $t$-正合性。",
    question="为什么「标准层到标准层」加上「一部分单层为零」就足以推出 $t$-正合，而不是只推出有界性？",
    goal="由式 (5)(6) 推出定理 4.4.1(1) 的 $t$-正合性与 (2) 的「穿过反球商」。",
    setup=[
        "反常 $t$-结构由标准层/余标准层刻画：一个复形属于 $\\mathcal D^{\\le0}$ 当且仅当其反常上同调层都满足某些「标准层判别」条件。",
        "式 (5)：$\\mathrm{Av}^{\\mathrm{IW}}(\\mathrm{IC}_w)=0$ 除非 $w\\in\\widetilde W_{\\mathrm{ext}}$。",
        "式 (6)：$\\mathrm{Av}^{\\mathrm{IW}}(\\Delta_w)\\cong\\Delta^{\\mathrm{IW}}_\\lambda$、$\\mathrm{Av}^{\\mathrm{IW}}(\\nabla_w)\\cong\\nabla^{\\mathrm{IW}}_\\lambda$（$\\lambda$ 由 $W\\cdot w=W\\cdot w_\\lambda$ 定）。",
    ],
    steps=[
        {
            "no": 1,
            "text": "注意 $\\mathrm{Av}^{\\mathrm{IW}}=\\Delta^{\\mathrm{IW}}_0\\star_I(-)$ 是右卷积，故它是正合（triangulated）函子；问题只在于它把反常 $t$-结构送到哪里。",
            "why": "卷积本身是三角函子，所以只需在反常层生成元上检验 $t$-级别的行为。",
            "locator": "A p.10",
            "provenance": "A",
        },
        {
            "no": 2,
            "text": "在标准层上：$\\Delta_w\\mapsto\\Delta^{\\mathrm{IW}}_\\lambda$，仍是反常层（次数 $0$）；在余标准层上同理仍是反常层。",
            "why": "这是式 (6)；它保证「反常层的像仍在反常层」，即 $\\mathrm{Av}^{\\mathrm{IW}}$ 把 $\\mathcal D^{\\le0}$ 送到 $\\mathcal D^{\\le0}$、$\\mathcal D^{\\ge0}$ 送到 $\\mathcal D^{\\ge0}$。",
            "locator": "A p.10",
            "provenance": "A",
        },
        {
            "no": 3,
            "text": "在单层上：$\\mathrm{IC}_w\\mapsto0$（$w\\notin\\widetilde W_{\\mathrm{ext}}$）或非零（$w\\in\\widetilde W_{\\mathrm{ext}}$），两种情形都不产生负/正次数污染。",
            "why": "式 (5) 处理了「单层被打成零」这一唯一可能破坏 $t$-正合的情形。",
            "locator": "A p.10",
            "provenance": "A",
        },
        {
            "no": 4,
            "text": "由「标准–余标准判别法」及反常层的生成性，上述三条合起来即 $\\mathrm{Av}^{\\mathrm{IW}}$ 反常 $t$-正合。",
            "why": "这正是原文「basic homological algebra allows one to deduce from 5 and 6」的具体含义。",
            "locator": "A p.10",
            "provenance": "A",
        },
        {
            "no": 5,
            "text": "再由式 (5)：被 $\\mathrm{Av}^{\\mathrm{IW}}$ 打成零的单层恰是 $w\\notin\\widetilde W_{\\mathrm{ext}}$ 那些，正是反球商 $\\mathcal P_I\\to\\mathcal P_I^{\\mathrm{asph}}$ 所商的 Serre 子范畴的生成元，故 $\\mathrm{Av}^{\\mathrm{IW}}$ 穿过反球商。",
            "why": "这是 (2) 的一半；另一半（全忠实）靠造截面，不在本推导范围内。",
            "locator": "A p.10",
            "provenance": "A",
        },
    ],
    result="$t$-正合性 = 式 (6) 保证「像仍是反常层」+ 式 (5) 保证「少数单层为零不破坏判别」；穿过反球商 = 式 (5) 杀掉的那批恰是商掉的 Serre 子范畴。",
    gaps=[
        "「标准–余标准判别法」原文未写出具体表述，只称「基础同调代数」。",
        "全忠实性（(2) 的另一半）另需构造截面，原文只给直观描述，本推导不覆盖。",
    ],
    pitfalls=[
        "式 (5) 只在 $w\\notin\\widetilde W_{\\mathrm{ext}}$ 时给零；$\\widetilde W_{\\mathrm{ext}}$ 上的单层像一般非零且非单层，不能推出「单层到单层」。",
        "把 $t$-正合性理解成「逐点正合」：这里的 $t$ 是反常 $t$-结构，不是通常的 $\\mathrm{Coh}$ 或 $\\mathbb Q_\\ell$-层 $t$-结构。",
    ],
    related=[
        f"{PKG}/concept/iw-averaging",
        f"{PKG}/concept/antispherical-quotient",
        f"{PKG}/concept/iw-highest-weight",
    ],
    sources=[src([10, 10], "A p.10", "§4.4")],
    provenance_note="式 (5)(6) 与证明梗概全在 p.10；本推导把「basic homological algebra」一句展开成五步。",
)

if __name__ == "__main__":
    CARDS.update(R)
    print("wrote", write_cards(R))
