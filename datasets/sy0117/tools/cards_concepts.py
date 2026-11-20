# -*- coding: utf-8 -*-
"""sy0117 概念卡数据（19 张，一章至少一张）。

所有文字为二轮校订时重写，不复制原书或译文长句；公式为 LaTeX 源码。
"""

BOOK = "Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版）"
P = "08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/"


def concept(slug, track, title, aliases, summary, question, definition, notation,
            key_points, formulas, pitfalls, annotations, related, section, anchor,
            theorems=None):
    aid = "sy0117/concept/" + slug
    return {
        "id": aid,
        "type": "concept",
        "track": track,
        "title": title,
        "aliases": aliases,
        "summary": summary,
        "question": question,
        "definition": {"text": definition, "notation": notation},
        "key_points": key_points,
        "formulas": formulas,
        "theorems": theorems or [],
        "pitfalls": pitfalls,
        "annotations": [
            {"type": t, "title": ti, "text": tx} for (t, ti, tx) in annotations
        ],
        "related": ["sy0117/concept/" + r for r in related],
        "sources": [{
            "book": BOOK,
            "section": section,
            "pages": [],
            "pdf_pages": [],
            "anchor": P + anchor,
            "page_note": "原书页码从略：本机无英文原书与页面图像，只以中译本节号与源码行号定位。",
        }],
        "rights": "rewritten",
        "status": "reviewed",
        "verification": {
            "status": "source-only",
            "checked_on": "2026-11-20",
            "checks": ["与中译定稿逐段对照", "公式与上下文记号核对", "未做英文原书逐页核验"],
        },
    }


CONCEPTS = [
    concept(
        "category", "第1章", "范畴与函子",
        ["category", "functor", "自然变换"],
        "把对象、态射、复合与单位公理化，用函子与自然变换比较不同数学结构。",
        "为什么范畴论先比较态射而不是比较对象？",
        r"""范畴 $\mathcal C$ 由对象类 $\operatorname{Ob}\mathcal C$、每对对象 $X,Y$ 的 Hom 集 $\mathcal C(X,Y)$、复合 $\circ$ 与单位 $1_X$ 组成；复合结合，单位左吸收与右吸收。函子同时给对象与态射，并保复合与单位；自然变换给两个函子之间的态射族。""",
        r"""$\mathcal C(X,Y)$ 也记 $\operatorname{Hom}_{\mathcal C}(X,Y)$；小范畴要求对象类与所有 Hom 集都是集合。""",
        [
            "态射携带的对象间关系比对象本身更多；只比较对象会丢掉复合信息。",
            r"相反范畴 $\mathcal C^{\mathrm{op}}$ 反转复合次序，Hom 集不变。",
            "范畴等价只需函子与自然同构，不要求对象一一对应。",
        ],
        [r"\mathcal C(X,Y)", r"1_Y\circ f=f=f\circ 1_X", r"F(g\circ f)=F(g)\circ F(f)"],
        [
            "把“对象同构”当成“对象相等”；或在验算函子时漏掉单位。",
            r"把 $\mathcal C^{\mathrm{op}}$ 的复合方向与 Hom 集方向同时反掉。",
        ],
        [
            ("易错预警", "Hom 的方向", r"""$\mathcal C^{\mathrm{op}}(X,Y)=\mathcal C(Y,X)$，但复合写成 $f\circ^{\mathrm{op}}g=g\circ f$；只反 Hom 不反复合，会把相反范畴算成原范畴。"""),
            ("背景直觉", "自然变换才是“自然”", r"""书里反复说“这个同构是自然的”，意思是对所有对象同时给出且与态射相容；单个人工同构不构成自然变换。"""),
        ],
        ["functor-natural", "additive-split"],
        "§1.1–1.3", "ch01.tex:4-217",
    ),
    concept(
        "functor-natural", "第1章", "函子与自然变换",
        ["functor", "natural transformation", "Yoneda"],
        "函子保结构，自然变换比较函子；Yoneda 引理把对象 X 与可表函子 C(-,X) 绑定。",
        "Yoneda 引理为什么说“对象由它收到的态射完全决定”？",
        r"""函子 $F\colon\mathcal C\to\mathcal D$ 给每个对象 $X$ 一个 $FX$、每个态射 $f$ 一个 $Ff$，并保单位与复合。自然变换 $\eta\colon F\to G$ 给每个 $X$ 一个 $\eta_X\colon FX\to GX$，使 $\eta_Y\circ Ff=Gf\circ\eta_X$。Yoneda 引理给出 $\operatorname{Nat}(\mathcal C(-,X),F)\cong F(X)$。""",
        r"""$\operatorname{Nat}(F,G)$ 记自然变换集；可表函子指 $\mathcal C(-,X)$ 或 $\mathcal C(X,-)$。""",
        [
            r"Yoneda 嵌入 $X\mapsto\mathcal C(-,X)$ 一般是全忠实的，但是否本质满取决于范畴。",
            "自然变换的方块交换图必须对每个态射成立，不能只对对象验证。",
            "反变函子等价于相反范畴上的共变函子，右模就是这种情形。",
        ],
        [r"\eta_Y\circ Ff=Gf\circ\eta_X", r"\operatorname{Nat}(\mathcal C(-,X),F)\cong F(X)"],
        [
            "把自然变换写成“每个对象给一个同构”，却漏掉与态射的交换性。",
            r"把 $\mathcal C(-,X)$ 与 $\mathcal C(X,-)$ 的可表方向弄反。",
        ],
        [
            ("易错预警", "可表方向", r"""本章的 Yoneda 嵌入用 $X\mapsto\mathcal C(-,X)$；若写成 $\mathcal C(X,-)$，得到的是反变版本，复合方向随之反转。"""),
            ("含糊点拨", "Yoneda 的证明", r"""沿恒等态射 $1_X\in\mathcal C(X,X)$ 追踪像：自然变换由 $\eta_X(1_X)\in F(X)$ 完全决定，这就是逆映射。"""),
        ],
        ["category", "morita"],
        "§1.2–1.3", "ch01.tex:44-217",
    ),
    concept(
        "additive-split", "第1章", "加法完备化与分裂完备化",
        ["additive completion", "Karoubi envelope", "Split"],
        "加法完备化补上有限直和，分裂完备化把幂等元的像补成对象；两者合起来才便于比较模范畴。",
        "为什么分裂完备化的对象要写成 (X,e)，而不是直接写像？",
        r"""加法完备化 $\operatorname{Add}\mathcal C$ 的形式有限直和再取直和项；分裂完备化 $\operatorname{Split}\mathcal C$ 的对象是 $(X,e)$，其中 $e\colon X\to X$ 满足 $e^2=e$，态射为 $e'\mathcal C(X,X')e$。Karoubi 完备化就是分裂完备化。""",
        r"""$e$ 是幂等元；$(X,e)$ 代表 $\operatorname{im}e$，但像在原来的范畴里未必存在，所以要把像正式补成对象。""",
        [
            r"$\operatorname{Split}(\operatorname{Add}\mathcal C)$ 与 $\operatorname{Add}(\operatorname{Split}\mathcal C)$ 等价，但不是字面相等。",
            r"幂等元分裂后，$\operatorname{im}e$ 与 $\operatorname{im}(1-e)$ 互补。",
            "Morita 等价在加法/分裂完备化后更容易陈述。",
        ],
        [r"\operatorname{Split}\mathcal C", r"e^2=e", r"\operatorname{Hom}((X,e),(X',e'))=e'\mathcal C(X,X')e"],
        [
            r"把 $\operatorname{SplitAdd}\mathcal C$ 的对象误写成 $X$；实际是 $(X,e)$。",
            r"忘记 $e'\circ f\circ e$ 的左右夹逼，导致复合不封闭。",
        ],
        [
            ("易错预警", "对象是 (X,e)", r"""只写 $X$ 会丢掉“取哪个直和项”的数据；不同幂等元给出同一 $X$ 的不同对象。"""),
            ("背景直觉", "为什么先加后裂", r"""先取有限直和，才有足够的直和项可裂；两种次序在等价意义下一致，但定义处要说明取哪一种。"""),
        ],
        ["category", "morita"],
        "§1.4–1.5", "ch01.tex:218-329",
    ),
    concept(
        "morita", "第1章", "Morita 等价",
        ["Morita equivalence", "双模", "模范畴等价"],
        "两个环的模范畴等价，就称它们 Morita 等价；等价由一对互为逆的双模给出。",
        "Morita 等价为什么不要求两个环同构？",
        r"""环 $A,B$ 的 Morita 等价由 $(A,B)$-双模 $M$ 与 $(B,A)$-双模 $N$ 给出，并有 $M\otimes_B N\cong A$、$N\otimes_A M\cong B$，从而 $\mathrm{Mod}\text{-}A\simeq\mathrm{Mod}\text{-}B$。""",
        r"""$M$ 同时是左 $A$-模与右 $B$-模，且两种作用相容；$N$ 的方向相反。""",
        [
            "Morita 等价保持模范畴的加法、Abel、导出结构，但不保持环同构。",
            "矩阵环 $M_n(A)$ 与 $A$ Morita 等价。",
            "等价双模的复合要与单位同构相容，不能只给对象级同构。",
        ],
        [r"M\otimes_B N\cong A", r"N\otimes_A M\cong B", r"\mathrm{Mod}\text{-}A\simeq\mathrm{Mod}\text{-}B"],
        [
            "把 Morita 等价当成环同构，进而误以为中心相同。",
            "只给 $M$ 不给 $N$，或忘记双模作用的相容性。",
        ],
        [
            ("含糊点拨", "双模的左右作用", r"""$M$ 的 $A$-左作用与 $B$-右作用必须满足 $(a m)b=a(mb)$；否则张量积不结合。"""),
            ("背景直觉", "表示论的“相同”", r"""Morita 等价把“同一个环的不同矩阵实现”视为同一表示论；这正是后来导出等价的原型。"""),
        ],
        ["category", "additive-split"],
        "§1.6", "ch01.tex:330-481",
    ),
    concept(
        "chain-complex", "第2章", "链复形与上同调",
        ["chain complex", "cochain complex", "homology"],
        "复形是带微分 d 的分次对象，d²=0 使同调成为复合的障碍；链映射与同伦给出范畴结构。",
        "为什么同调只看见 d²=0 的商，而同伦在同调上消失？",
        r"""复形 $(C^\bullet,d)$ 由分次对象与微分 $d^n\colon C^n\to C^{n+1}$ 组成，满足 $d^{n+1}d^n=0$。$n$ 次上同调为 $H^n(C)=\ker d^n/\operatorname{im}d^{n-1}$。链映射与 $d$ 交换；同伦 $h$ 满足 $f-g=dh+hd$。""",
        r"""上链复形 $d$ 升次，链复形 $d$ 降次；本书多数用上链，故 $d^n\colon C^n\to C^{n+1}$。""",
        [
            "同调是链映射的商，不是复形本身的商；同伦的链映射诱导同一映射。",
            "正合列的长上同调序列来自蛇引理，不是额外公理。",
            "复形的平移 $C[1]^n=C^{n+1}$，微分变号。",
        ],
        [r"d^{n+1}\circ d^n=0", r"H^n(C)=\ker d^n/\operatorname{im}d^{n-1}", r"f-g=dh+hd"],
        [
            "把上链复形的 $d$ 写成降次；或把 $H^n$ 的指标写成 $H_n$ 后忘记约定。",
            r"把同伦 $h$ 的次数写错：$h\colon C^n\to C^{n-1}$ 时 $dh+hd$ 才是 $n$ 次。",
        ],
        [
            ("易错预警", "d 的次数", r"""本书用上链复形，$d$ 升次；若按链复形降次验算，所有符号与指标都会反。"""),
            ("含糊点拨", "同伦的符号", r"""$f-g=dh+hd$ 的符号取决于 $d$ 与 $h$ 的放置；在分次情形还要加 Koszul 符号。"""),
        ],
        ["ext", "quiver-representation"],
        "§2.1", "ch02.tex:5-191",
    ),
    concept(
        "ext", "第2章", "Ext 群与扩张",
        ["Ext", "projective resolution", "Yoneda product"],
        "Ext 群用投射分解计算 Hom 的同调，分类扩张；Yoneda 积使其成为分次环。",
        "Ext 为什么不依赖投射分解的选取？",
        r"""取 $M$ 的投射分解 $P_\bullet\to M$，定义 $\operatorname{Ext}^n_A(M,N):=H^n(\operatorname{Hom}_A(P_\bullet,N))$。比较定理保证不同投射分解给出典范同构；$\operatorname{Ext}^1$ 分类短正合列 $0\to N\to E\to M\to0$。""",
        r"""$\operatorname{Ext}^0_A(M,N)=\operatorname{Hom}_A(M,N)$；Yoneda 积把 $\operatorname{Ext}^p(M,N)\otimes\operatorname{Ext}^q(N,L)\to\operatorname{Ext}^{p+q}(M,L)$。""",
        [
            "投射分解的比较映射在同伦意义下唯一，故 Ext 与分解选取无关。",
            r"Ext 的 Yoneda 积与合成一致，使 $\bigoplus_n\operatorname{Ext}^n(M,M)$ 成为分次环。",
            "Koszul 分解给出多项式环上模的显式 Ext。",
        ],
        [r"\operatorname{Ext}^n_A(M,N):=H^n(\operatorname{Hom}_A(P_\bullet,N))", r"\operatorname{Ext}^1_A(M,N)\leftrightarrow\{0\to N\to E\to M\to0\}"],
        [
            "用任意分解（非投射/自由）硬算 Ext，得到的结果依赖分解。",
            r"把 $\operatorname{Ext}^1$ 只当成扩张的集合，忘掉它的加法群结构。",
        ],
        [
            ("易错预警", "分解必须投射", r"""Ext 的定义要求 $P_i$ 投射（或自由）；用一般分解取 Hom 上同调不保持同构。"""),
            ("背景直觉", "Ext 是“高阶 Hom”", r"""$\operatorname{Ext}^n$ 衡量“先映射再修正”的障碍；在导出范畴里它只是 Hom 的平移分量。"""),
        ],
        ["chain-complex", "quiver-representation"],
        "§2.3", "ch02.tex:474-771",
    ),
    concept(
        "ainfty-algebra", "第3章", "A∞ 代数",
        ["A-infinity algebra", "Stasheff", "higher product"],
        "A∞ 代数把结合律松弛为无穷多个高阶乘积 μ_n，满足 Stasheff 关系；dg 代数是 μ≥3=0 的特例。",
        "为什么普通结合代数不够，非要引入 μ_3, μ_4, …？",
        r"""A∞ 代数 $A$ 带分次模与运算 $\mu_n\colon A^{\otimes n}\to A$（$n\ge1$），满足 Stasheff 关系；$\mu_1$ 是微分，$\mu_2$ 是乘法，$\mu_3$ 度量结合律的失败。""",
        r"""$\mu_n$ 的次数为 $2-n$；符号 $(-1)^{rs}$ 来自 Koszul 约定。""",
        [
            r"$\mu_1^2=0$ 是高阶关系的 $n=1$ 情形；结合律的失败由 $\mu_3$ 补偿。",
            "A∞ 态射是满足无穷多个交换关系的族 $f_n$，不是单个保乘映射。",
            r"极小模型把 A∞ 代数换成 $\mu_1=0$ 的同构代表。",
        ],
        [r"\sum_{r+s+t=n}(-1)^{rs}\mu_{r+1+t}(1^{\otimes r}\otimes\mu_s\otimes1^{\otimes t})=0", r"|\mu_n|=2-n"],
        [
            r"把 A∞ 代数当成“带高阶项的 dg 代数”却漏掉符号；符号错会使 $\mu_3$ 的关系不成立。",
            r"以为 $\mu_3$ 可以任意选取；它受 Stasheff 关系约束，只到同伦意义下唯一。",
        ],
        [
            ("易错预警", "Koszul 符号", r"""把 $\mu_s$ 移过 $r$ 个元素时要乘 $(-1)^{rs}$；漏掉它会让 $n=3$ 的关系差一个负号。"""),
            ("背景直觉", "结合律的“同伦修正”", r"""普通代数要求 $a(bc)=(ab)c$；A∞ 只说这个差被 $\mu_3$ 填上，而 $\mu_3$ 的差又被 $\mu_4$ 填上，如此无穷。"""),
        ],
        ["twisted-complex", "chain-complex"],
        "§3.1", "ch03.tex:7-369",
    ),
    concept(
        "twisted-complex", "第3章", "扭曲复形与预范畴",
        ["twisted complex", "pre-category", "Maurer-Cartan"],
        "扭曲复形在预范畴中用下三角矩阵 δ 编码高阶态射，δ 满足 Maurer–Cartan 方程才给出复形。",
        "预范畴没有恒等态射，怎样还能定义“复形”？",
        r"""预范畴不要求恒等态射，只给分次 Hom 空间与高阶乘积。扭曲复形是形式直和 $\bigoplus_i X_i$ 配上 $\delta=\sum_{i<j}\delta_{ij}$（下三角），满足 $\mu_1(\delta)+\mu_2(\delta,\delta)+\cdots=0$。""",
        r"""下三角条件使 $\delta_{ij}$ 只从低指标指向高指标，故 MC 的无穷和在每个矩阵元上有限。""",
        [
            "MC 方程是 $d^2=0$ 在 A∞ 情形的高阶推广。",
            r"扭曲复形的态射也要带高阶修正，不能只取 $\mu_1$-闭的矩阵。",
            "预范畴的“范畴化”通过形式添加直和与扭曲复形完成。",
        ],
        [r"\delta=\sum_{i<j}\delta_{ij}", r"\mu_1(\delta)+\mu_2(\delta,\delta)+\mu_3(\delta,\delta,\delta)+\cdots=0"],
        [
            r"把 δ 当普通微分，只验 $\mu_1(\delta)=0$；这会漏掉高阶项。",
            "去掉下三角条件后无穷和不收敛，MC 方程失去意义。",
        ],
        [
            ("易错预警", "下三角不是装饰", r"""没有下三角，$\delta^n$ 的矩阵元会出现无限多条路径；下三角保证每个矩阵元只有有限项。"""),
            ("含糊点拨", "MC 的符号", r"""$\mu_2(\delta,\delta)$ 的符号由 $\delta$ 的奇偶次数决定；把 δ 当偶元素会漏掉 Koszul 符号。"""),
        ],
        ["ainfty-algebra", "quiver-representation"],
        "§3.3", "ch03.tex:637-1286",
    ),
]
