#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cards_b.py —— 轨道 B：Springer 侧与三造函子（§3）。"""
from gen_cards import CARDS, card, src, PKG, write_cards

B = {}

B["concepts/springer-resolution"] = card(
    "concepts", "springer-resolution",
    title="Springer 解消 $\\widetilde{\\mathcal N}$ 与线丛 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$",
    aliases=["Springer resolution", "Ñ", "Springer 解消上的凝聚层"],
    track="B",
    summary="$\\widetilde{\\mathcal N}=G^\\vee\\times_{B^\\vee}\\mathfrak n^\\vee$ 是 $G^\\vee$-等变的 Springer 解消，其上的线丛 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 与 $V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 生成 $\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$。",
    question="Springer 解消的线丛为什么按 $X^\\vee$ 编号，哪些对象生成了它的等变凝聚层范畴？",
    definition={
        "text": "设 $\\mathcal N$ 为 $G^\\vee$ 的幂零锥，$\\widetilde{\\mathcal N}:=G^\\vee\\times_{B^\\vee}\\mathfrak n^\\vee$，带矩映射 $\\mu\\colon\\widetilde{\\mathcal N}\\to\\mathcal N$ 与投影 $\\widetilde{\\mathcal N}\\to G^\\vee/B^\\vee$；后者使 $\\widetilde{\\mathcal N}$ 成为 $G^\\vee/B^\\vee$ 上的向量丛，且是 $\\mathfrak g^\\vee\\times G^\\vee/B^\\vee$ 的子向量丛。对 $\\lambda\\in X^\\vee$ 记 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 为 $\\mathcal O_{G^\\vee/B^\\vee}(\\lambda)$ 的拉回。",
        "notation": "$\\mathfrak n^\\vee\\subset\\mathfrak g^\\vee$ 为幂零根，$B^\\vee\\subset G^\\vee$ 为 Borel；$X^\\vee$ 为余根格（$G^\\vee$ 的权格）。",
    },
    key_points=[
        "$\\lambda$ 的编号来自 $G^\\vee/B^\\vee$ 上的特征线丛：$\\lambda\\in X^\\vee=X_*(T^\\vee)$，所以 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 是「$T^\\vee$ 权」的几何化。",
        "引理 3.1.1 的第 (1) 类与第 (2) 类并不对称：前者 $\\lambda$ 任意、后者 $\\lambda$ 须支配（$\\lambda\\in X^\\vee_+$）。支配性是「$V\\otimes$」能张成剩余部分的原因。",
        "Springer 解消同时是从 $\\widetilde{\\mathcal N}$ 到 $\\mathcal N$ 的紧合映射与到旗簇的向量丛：两个结构各用一次，前者给紧合性，后者给线丛与 $T^\\vee$ 作用。",
        "此范畴的 $K$ 群正是反球模 $M^{\\mathrm{asph}}$（式 (2)），所以这一节在几何侧重现了 §2 的模论骨架。",
    ],
    formulas=[
        "$\\widetilde{\\mathcal N}=G^\\vee\\times_{B^\\vee}\\mathfrak n^\\vee$",
        "$\\mu\\colon\\widetilde{\\mathcal N}\\to\\mathcal N,\\qquad \\widetilde{\\mathcal N}\\to G^\\vee/B^\\vee$（向量丛）",
    ],
    theorems=[
        {
            "name": "引理 3.1.1（生成元）",
            "statement": "$\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$ 由 (1) 线丛 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$（$\\lambda\\in X^\\vee$）与 (2) $V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$（$V\\in\\mathrm{Rep}(G^\\vee)$、$\\lambda\\in X^\\vee_+$）共同生成。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文只陈述，不证；这是 Springer 解消上等变凝聚层的标准生成性结果。",
            },
            "source": "A p.6",
        }
    ],
    pitfalls=[
        "把 $\\widetilde{\\mathcal N}$ 与其矩映射的像 $\\mathcal N$ 搞混：前者光滑、是向量丛，后者才是奇异的幂零锥；所有「凝聚层」都活在前者上。",
        "线丛编号用 $X^\\vee$，而 Wakimoto 层与 IW 标准层的编号也用 $X^\\vee$——三处编号必须是同一套，否则定理 5.0.1 的对象对应会错位。",
    ],
    related=[
        f"{PKG}/concept/antispherical-module",
        f"{PKG}/concept/hat-n-x",
        f"{PKG}/concept/functor-f3",
    ],
    sources=[src([6, 6], "A p.6", "§3.1")],
    provenance_note="定义与引理 3.1.1 均在 p.6；$\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 的编号沿用 §2.5 的 $X^\\vee$。",
)

B["concepts/hat-n-x"] = card(
    "concepts", "hat-n-x",
    title="无穷小稳定化子 $\\widehat{\\mathcal N}$ 与 $\\widehat{\\mathcal N}_X$",
    aliases=["infinitesimal stabilizer", "N̂_X", "仿射完备化 X"],
    track="B",
    summary="把 $G^\\vee/U^\\vee$ 仿射完备化为 $X=\\mathrm{Spec}\\,\\mathcal O(G^\\vee/U^\\vee)$，其无穷小万有稳定化子是 $\\widehat{\\mathcal N}_X$；$\\widehat{\\mathcal N}\\subset\\widehat{\\mathcal N}_X$ 是开子簇，且 $\\widehat{\\mathcal N}$ 是 $\\widetilde{\\mathcal N}$ 上的 $T^\\vee$-torsor。",
    question="$\\widehat{\\mathcal N}_X$ 是怎么从 $\\widetilde{\\mathcal N}$ 造出来的，图 (4) 中三种映射各自负责什么？",
    definition={
        "text": "记 $\\widehat{\\mathcal N}$ 为 $\\widetilde{\\mathcal N}$ 在 $\\mathfrak g^\\vee\\times_{G^\\vee/U^\\vee}\\to G^\\vee/B^\\vee$ 下的原像；$X:=\\mathrm{Spec}(\\mathcal O(G^\\vee/U^\\vee))$ 为 $G^\\vee/U^\\vee$ 的仿射完备化，$G^\\vee/U^\\vee\\subset X$ 开，$\\partial X:=X\\setminus G^\\vee/U^\\vee$。$G^\\vee$ 在 $G^\\vee/U^\\vee$ 上作用的无穷小万有稳定化子即 $\\widehat{\\mathcal N}$；在 $X$ 上作用的无穷小万有稳定化子记为 $\\widehat{\\mathcal N}_X$，它是 $\\mathfrak g^\\vee\\times X$ 的闭子概形，含 $\\widehat{\\mathcal N}$ 为开子簇。",
        "notation": "$\\mathrm{Coh}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)$ 为形如 $V\\otimes\\mathcal O_{\\widehat{\\mathcal N}_X}$（$V\\in\\mathrm{Rep}(G^\\vee\\times T^\\vee)$）的自由对象构成的全加法子范畴。",
    },
    key_points=[
        "图 (4) 的三条边各有分工：$\\widehat{\\mathcal N}\\to\\widetilde{\\mathcal N}$ 是 $T^\\vee$-torsor（提供 $T^\\vee$ 作用与权分解），$\\widehat{\\mathcal N}\\hookrightarrow\\widehat{\\mathcal N}_X$ 是开浸入（提供可去掉的边界），三个竖直箭头都是闭浸入（提供支撑条件）。",
        "为什么要完备化：$G^\\vee/U^\\vee$ 本身不是仿射的，凝聚层没有足够好的整体截面；换成 $X$ 才能把 $\\mathcal O(\\widehat{\\mathcal N}_X)$ 当交换代数用（§3.3 的 Tannakian 构造就靠它）。",
        "$\\partial X$ 是「被丢掉的部分」：命题 3.1.2 的商恰好按 $\\partial X$ 上的支撑作零化，这就是等价能成立的关键。",
        "$\\mathrm{Coh}_{\\mathrm{free}}$ 的下标 free 不是装饰：只有自由的 $V\\otimes\\mathcal O$ 才与表示范畴对应，一般凝聚层不在 Tannakian 像里。",
    ],
    formulas=[
        "$X=\\mathrm{Spec}(\\mathcal O(G^\\vee/U^\\vee)),\\qquad \\partial X=X\\setminus G^\\vee/U^\\vee$",
        "$\\widehat{\\mathcal N}\\to\\widetilde{\\mathcal N}$ 为 $T^\\vee$-torsor，$\\widehat{\\mathcal N}\\hookrightarrow\\widehat{\\mathcal N}_X$ 为开浸入",
    ],
    theorems=[
        {
            "name": "命题 3.1.2（去边界得等价）",
            "statement": "有函子 $K^b\\mathrm{Coh}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)\\to\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$，它唯一地穿过三角范畴的等价 $K^b\\mathrm{Coh}^{\\dots}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)/K^b\\mathrm{Coh}^{\\dots}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)_{\\partial X}\\xrightarrow{\\sim}\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "函子由两段拼成：沿 $\\widehat{\\mathcal N}_X\\leftarrow\\widehat{\\mathcal N}$ 拉回，再用 $\\mathcal D^b\\mathrm{Coh}_{G^\\vee\\times T^\\vee}(\\widehat{\\mathcal N})\\cong\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$。", "why": "后一个等价本质是栈同构 $\\widehat{\\mathcal N}/(G^\\vee\\times T^\\vee)\\cong\\widetilde{\\mathcal N}/G^\\vee$（脚注 8）。"},
                    {"no": 2, "text": "验证它是等价：「基本上是同调代数与代数群表示论的练习」（原文语），未展开。", "why": "原文明确说省略，故本卡只记骨架。"},
                ],
                "gap_note": "第 2 步原文不写细节；$\\partial X$-支撑的商与 $\\widehat{\\mathcal N}\\subset\\widehat{\\mathcal N}_X$ 的开性互补，是这一步的实质内容。",
            },
            "source": "A p.6",
        }
    ],
    pitfalls=[
        "$\\widehat{\\mathcal N}$ 与 $\\widehat{\\mathcal N}_X$ 只差一个边界，但范畴层面差别很大：前者只带 $T^\\vee$ 的 torsor 结构，后者才是仿射的、可取其函数环。",
        "「自由」是范畴层面的条件（对象形如 $V\\otimes\\mathcal O$），不是几何上的局部自由性；不要按字面理解成向量丛。",
    ],
    related=[
        f"{PKG}/concept/springer-resolution",
        f"{PKG}/concept/functor-f2",
    ],
    sources=[src([6, 7], "A p.6", "§3.1")],
    provenance_note="对象定义、图 (4) 与命题 3.1.2 在 p.6，证明开头与脚注 8 在 p.7。",
)

B["concepts/functor-f1"] = card(
    "concepts", "functor-f1",
    title="函子 I：$F_1\\colon\\mathrm{Rep}(G^\\vee\\times T^\\vee)\\to\\mathcal P_I^{\\mathrm{Wak}}$",
    aliases=["F1", "functor I", "第一个范畴化"],
    track="B",
    summary="在表示范畴上直接定义 $V\\otimes k_{T^\\vee}(\\lambda)\\mapsto Z(\\mathrm{Sat}(V))\\star_I\\mathbb W_\\lambda$；定理 2.5.3 保证值域落在有 Wakimoto 滤链的中心层里，且它是幺半的。",
    question="函子 I 为什么能定义在表示范畴上，幺半性由什么保证？",
    definition={
        "text": "定义 $F_1\\colon\\mathrm{Rep}(G^\\vee\\times T^\\vee)\\to\\mathcal P_I^{\\mathrm{Wak}}$，$V\\otimes k_{T^\\vee}(\\lambda)\\mapsto Z(\\mathrm{Sat}(V))\\star_I\\mathbb W_\\lambda$，其中 $V\\in\\mathrm{Rep}(G^\\vee)$、$\\lambda\\in X^\\vee$。",
        "notation": "$\\mathrm{Sat}\\colon\\mathrm{Rep}(G^\\vee)\\xrightarrow{\\sim}\\mathrm{Perv}(L^+G\\backslash\\mathrm{Gr}_G)$ 为几何 Satake 等价；$\\mathcal P_I^{\\mathrm{Wak}}\\subset\\mathcal P_I$ 为允许 Wakimoto 滤链的反常层。",
    },
    key_points=[
        "$F_1$ 的良定义靠两条：定理 2.5.3 保证 $Z(\\mathrm{Sat}(V))$ 有 Wakimoto 滤链，引理 2.5.4 保证 $\\mathcal P_I^{\\mathrm{Wak}}$ 对 $\\star_I$ 封闭。",
        "幺半性（引理 3.2.1）来自两处：定理 2.4.1(3) 的「$Z$ 落在中心」给出 $Z(\\mathcal F)\\star_I Z(\\mathcal G)\\cong Z(\\mathcal F\\star\\mathcal G)$，命题 2.5.2(3) 给出 $\\mathbb W_\\lambda\\star_I\\mathbb W_\\mu\\cong\\mathbb W_{\\lambda+\\mu}$。",
        "定义域是 $\\mathrm{Rep}(G^\\vee\\times T^\\vee)$ 而非 $\\mathrm{Coh}(\\widehat{\\mathcal N}_X)$：这一步只用到「自由对象」这一小片，后面的函子 II 才把它扩张到整个自由凝聚层范畴。",
        "原文脚注 9 提醒：$k_{T^\\vee}(\\lambda)\\mapsto\\mathbb W_\\lambda$ 单独是函子（$\\mathrm{Rep}(T^\\vee)\\to\\mathcal P_I$），但 Functoriality 仍需说明——所以 $F_1$ 的良定义不是自动的。",
    ],
    formulas=[
        "$F_1\\colon\\mathrm{Rep}(G^\\vee\\times T^\\vee)\\to\\mathcal P_I^{\\mathrm{Wak}},\\quad V\\otimes k_{T^\\vee}(\\lambda)\\mapsto Z(\\mathrm{Sat}(V))\\star_I\\mathbb W_\\lambda$",
    ],
    theorems=[
        {
            "name": "引理 3.2.1（幺半性）",
            "statement": "$F_1$ 是幺半函子。",
            "proof": {
                "status": "sketch",
                "steps": [
                    {"no": 1, "text": "把两边各写成一个 $\\mathrm{Sat}(V)$ 的中心层与一个 Wakimoto 层的卷积，分别用定理 2.4.1(3)（中心性）与命题 2.5.2(3)（$\\mathbb W_{\\lambda+\\mu}$）交换与合并。", "why": "这是两个「乘法交换律」的拼接，原文称「容易的推论」。"},
                ],
                "gap_note": "原文只写「easy consequence」，未逐项核对约束（尤其是 $\\mathbb W$ 的下标加法与 $V$ 的张量同时发生时）。",
            },
            "source": "A p.7",
        }
    ],
    pitfalls=[
        "把 $F_1$ 当成 $K$ 群层面的同构：$F_1$ 只是范畴层面的幺半函子，它到定理 5.0.1 之前都不是等价。",
        "$k_{T^\\vee}(\\lambda)$ 中的 $\\lambda$ 与 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)$ 中的 $\\lambda$ 必须同号；若在 $T^\\vee$ 与 $T$ 之间对偶时翻符号，$F_1$ 与 $F$ 就对不上。",
    ],
    related=[
        f"{PKG}/concept/wakimoto-filtration",
        f"{PKG}/concept/functor-f2",
        f"{PKG}/deriv/f1-monoidal",
    ],
    sources=[src([7, 7], "A p.7", "§3.2")],
    provenance_note="定义与引理 3.2.1 均在 p.7；脚注 9 关于 functoriality 的提醒同页。",
)

B["concepts/functor-f2"] = card(
    "concepts", "functor-f2",
    title="函子 II：经 Tannakian 重构把 $F_1$ 扩到 $\\mathrm{Coh}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)$",
    aliases=["F2", "functor II", "Tannakian 重构"],
    track="B",
    summary="把 $\\mathcal P_I^{\\mathrm{Wak}}$ 换成一个对称幺半的非全子范畴 $\\mathcal C$，用 Tannakian 形式得 $H\\colon\\mathcal C\\xrightarrow{\\sim}A\\text{-}\\mathrm{mod}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}$，于是扩张 $F_1$ 等价于造一个等变代数映射 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$。",
    question="为什么要绕道 Tannakian 重构，$\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$ 这个映射又从哪里来？",
    definition={
        "text": "取对称幺半的非全子范畴 $\\mathcal C\\subset\\mathcal P_I^{\\mathrm{Wak}}$ 使 $F_1$ 穿过它（脚注 10 指出：$\\mathrm{Coh}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)$ 对称幺半而 $\\mathcal P_I^{\\mathrm{Wak}}$ 不是）。由 Tannakian 形式得等价 $H\\colon\\mathcal C\\to A\\text{-}\\mathrm{mod}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}$，其中 $A$ 带 $G^\\vee\\times T^\\vee$ 作用；$F'_1$ 在 $H$ 下成为 $V\\mapsto V\\otimes A$。扩张 $F'_1$ 到 $\\mathrm{Coh}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)$ 等价于给一个 $G^\\vee\\times T^\\vee$-等变代数映射 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$。",
        "notation": "$A\\text{-}\\mathrm{mod}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}$ 为自由 $A$-模构成的等变范畴。",
    },
    key_points=[
        "这一步的动机是「对称幺半」：要借用交换代数的语言（$\\mathcal O(\\widehat{\\mathcal N}_X)$ 是交换环），必须先把非对称的目标范畴换成对称的 $\\mathcal C$。",
        "Tannakian 重构在此是黑箱：$A$ 是 $\\mathcal C$ 的「函数环」，$V\\otimes A$ 是 $\\mathcal C$ 中自由对象的统一写法；原文不给构造。",
        "两个分量映射各有出处：$\\mathcal O(\\mathfrak g^\\vee)\\to A$ 是附近循环单值自同构的对数，$\\mathcal O(X)\\to A$ 由定理 2.5.3 的 Wakimoto 滤链决定。",
        "合成 $\\mathcal O(\\mathfrak g^\\vee)\\otimes\\mathcal O(X)\\to A$ 唯一分解出 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$：因为 $\\mathcal O(\\widehat{\\mathcal N}_X)$ 是 $\\mathcal O(\\mathfrak g^\\vee)\\otimes\\mathcal O(X)$ 的商。",
        "得到 $F_2$ 的公式 $M\\mapsto M\\otimes_{\\mathcal O(\\widehat{\\mathcal N}_X)}A$：这是标准的「沿环映射换基」，说明 $F_2$ 本质是一个张量积函子。",
    ],
    formulas=[
        "$H\\colon\\mathcal C\\xrightarrow{\\sim}A\\text{-}\\mathrm{mod}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}},\\quad V\\otimes k_{T^\\vee}(\\lambda)\\mapsto V\\otimes k_{T^\\vee}(\\lambda)\\otimes A$",
        "$F_2\\colon\\mathrm{Coh}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)\\to A\\text{-}\\mathrm{mod}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}\\cong\\mathcal C\\hookrightarrow\\mathcal P_I^{\\mathrm{Wak}},\\quad M\\mapsto M\\otimes_{\\mathcal O(\\widehat{\\mathcal N}_X)}A$",
    ],
    theorems=[],
    pitfalls=[
        "Tannakian 重构要求 $\\mathcal C$ 对称幺半且「足够小」；若直接对 $\\mathcal P_I^{\\mathrm{Wak}}$ 做，会因它非对称幺半而失败。",
        "$A$ 不是 $\\mathcal O(\\widehat{\\mathcal N}_X)$：前者是 $\\mathcal C$ 的端环，后者是几何环；两者的映射 $\\mathcal O(\\widehat{\\mathcal N}_X)\\to A$ 才是全部内容，方向不能反。",
    ],
    related=[
        f"{PKG}/concept/functor-f1",
        f"{PKG}/concept/hat-n-x",
        f"{PKG}/deriv/tannakian-algebra",
    ],
    sources=[src([7, 8], "A p.7", "§3.3")],
    provenance_note="构造在 p.7，两个分量映射的说明与 $F_2$ 的公式在 p.8。",
)

B["concepts/functor-f3"] = card(
    "concepts", "functor-f3",
    title="函子 III：$F\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b\\mathcal P_I$",
    aliases=["F", "functor III", "几何侧到 Iwahori 侧"],
    track="B",
    summary="先验证 $K^bF_2$ 把 $\\partial X$-支撑的复形打成零，于是 $F_2$ 下降为 $F$：$V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}\\mapsto Z(\\mathrm{Sat}(V))$、$\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)\\mapsto\\mathbb W_\\lambda$；复合实现函子后仍**不是**等价。",
    question="为什么 $F_2$ 能下降成 $\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})$ 上的函子，而 $F$ 本身还不是等价？",
    definition={
        "text": "由命题 3.1.2，$\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\cong K^b\\mathrm{Coh}^{G^\\vee\\times T^\\vee}_{\\mathrm{free}}(\\widehat{\\mathcal N}_X)/K^b_{\\partial X}$。若 $K^bF_2$ 把 $K^b_{\\partial X}$ 打到 $K^b\\mathcal P_I^{\\mathrm{Wak}}$ 的零调复形，则 $F_2$ 下降为 $F\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b\\mathcal P_I^{\\mathrm{Wak}}\\hookrightarrow\\mathcal D^b\\mathcal P_I$，$V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}\\mapsto Z(\\mathrm{Sat}(V))$、$\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)\\mapsto\\mathbb W_\\lambda$。",
        "notation": "实现函子 $\\mathcal D^b\\mathcal P_I\\to\\mathcal D^b(I\\backslash\\mathrm{Fl}_G)$ 把反常层复形送到通常的导出等变范畴；它在 Iwahori 情形**不是**等价。",
    },
    key_points=[
        "下降（descend）的关键是 $\\partial X$ 上的零化，而这一步原文说「可以相当显式地验证，略去」——这是全文最明显的一处省略。",
        "两个对象对应是整篇文章的主线：$V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}\\mapsto Z(\\mathrm{Sat}(V))$ 与 $\\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)\\mapsto\\mathbb W_\\lambda$；§5 的等价正是把这两个对应升级为定理。",
        "「实现函子不是等价」是原文的明确警告（p.8 末）：Iwahori 情形反常层与通常导出范畴之间的差异真实存在，所以 $F$ 只能在反常层里取值域。",
        "与 $F_1$ 的关系：$F$ 在自由对象上就是 $F_1$ 的公式；$F$ 多做的是把这些对象装进 $\\mathcal D^b\\mathcal P_I$，从而可以取卷积、做三角运算。",
    ],
    formulas=[
        "$F\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b\\mathcal P_I,\\quad V\\otimes\\mathcal O_{\\widetilde{\\mathcal N}}\\mapsto Z(\\mathrm{Sat}(V)),\\quad \\mathcal O_{\\widetilde{\\mathcal N}}(\\lambda)\\mapsto\\mathbb W_\\lambda$",
    ],
    theorems=[
        {
            "name": "函子 III 的存在性（§3.4）",
            "statement": "$K^bF_2$ 把 $\\partial X$-支撑复形打到零调复形，故 $F_2$ 下降为 $F\\colon\\mathcal D^b\\mathrm{Coh}_{G^\\vee}(\\widetilde{\\mathcal N})\\to\\mathcal D^b\\mathcal P_I$。",
            "proof": {
                "status": "gap",
                "steps": [],
                "gap_note": "原文：「This can be checked rather explicitly, and is omitted.」这是本译本标注的主要空白之一。",
            },
            "source": "A p.8",
        }
    ],
    pitfalls=[
        "把 $F$ 与「$F$ 复合实现函子」混为一谈：后者落在 $\\mathcal D^b(I\\backslash\\mathrm{Fl}_G)$，且因实现函子非等价而丢掉信息。",
        "下降用的商是 $K^b_{\\partial X}$（$\\partial X$ 上的集合论支撑），不是「$X$ 上的支撑」；边界差一个开浸入，这两种支撑不同。",
    ],
    related=[
        f"{PKG}/concept/functor-f2",
        f"{PKG}/concept/springer-resolution",
        f"{PKG}/concept/functor-fiw",
    ],
    sources=[src([8, 8], "A p.8", "§3.4")],
    provenance_note="下降论证与两个对象对应在 p.8；「实现函子非等价」的警告同页末。",
)

if __name__ == "__main__":
    CARDS.update(B)
    print("wrote", write_cards(B))
