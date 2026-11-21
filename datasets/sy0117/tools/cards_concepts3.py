# -*- coding: utf-8 -*-
"""sy0117 概念卡补编：第三轮校定新增的术语解释（阿米巴、环簇与扇、gentle 代数、crepant 消解）。"""
from cards_concepts import concept

CONCEPTS_3 = [
    concept(
        "amoeba", "第8章", "阿米巴（amoeba）",
        ["amoeba", "阿米巴", "Log 映射", "热带化"],
        "复环面中超曲面在逐坐标对数映射下的像；它把复几何对象压成 $\\mathbb R^n$ 里一只带腿的“变形虫”，其缩放极限就是热带超曲面。",
        "为什么把超曲面取对数后得到的图形，能帮我们读出它的热带化？",
        r"""设 $V\subset(\mathbb C^*)^n$ 是超曲面，逐坐标对数映射为
$\operatorname{Log}(z_1,\dots,z_n)=(\log|z_1|,\dots,\log|z_n|)\in\mathbb R^n$。
集合 $A(V)=\operatorname{Log}(V)$ 称为 $V$ 的**阿米巴**（amoeba，希腊语“变形虫”）：它通常是一块带若干“腿”的厚实区域，补集由有限个凸区域拼成。令 $t\to\infty$，把 $A(V)$ 按 $1/\log t$ 缩放，其极限（按 Hausdorff 距离）就是 $V$ 的热带化 $\operatorname{Trop}(V)$。""",
        r"""$\operatorname{Log}\colon(\mathbb C^*)^n\to\mathbb R^n$；$A(V)=\operatorname{Log}(V)$；$\operatorname{Trop}(V)=\lim_{t\to\infty}\frac1{\log t}\operatorname{Log}(V)$。""",
        [
            r"阿米巴只记录 $|z_i|$，丢掉全部辐角，因此是实 $n$ 维集合而非复对象。",
            r"补集的分量对应 Newton 多面体的面：这是 Forsberg–Passare–Tsikh 的定理。",
            r"缩放极限给出热带化，边的重数等于对应相交数；这正是“热带几何是阿米巴的骨架”的精确含义。",
        ],
        [r"A(V)=\{\operatorname{Log}(z):z\in V\}", r"\operatorname{Trop}(V)=\lim_{t\to\infty}\tfrac1{\log t}A(V)"],
        [
            r"把 $\operatorname{Log}$ 当成复对数；这里的像落在 $\mathbb R^n$，没有“多值”问题。",
            r"把阿米巴当成代数簇来算维数：它是带边界的实集合，边界来自 $|z_i|\to0$ 或 $\infty$。",
        ],
        [
            ("易错预警", "Log 不是全纯映射", r"""$\operatorname{Log}$ 逐坐标取模再取对数，连续但非全纯；因此 $A(V)$ 的“边界”没有复解析意义，不能用除子理论直接算。"""),
            ("背景直觉", "为什么叫变形虫", r"""$n=2$ 时 $A(V)$ 是平面区域，中央一团、伸出若干条腿（tentacle），形似变形虫；腿的数目与 Newton 多边形的边数有关。"""),
        ],
        ["toric-variety", "dimer"],
        "§8.2", "ch08.tex:440-470",
    ),
    concept(
        "toric-variety", "第8章", "环簇与扇",
        ["toric variety", "fan", "环簇", "扇"],
        "环簇是以代数环面为稠密开子集的代数簇，完全由扇（整锥的集合）这组组合数据决定。",
        "为什么一组锥（扇）就能唯一确定一个代数簇？",
        r"""设 $N\cong\mathbb Z^n$，$M=\operatorname{Hom}(N,\mathbb Z)$。$N_{\mathbb R}$ 中的**整锥**是 $\sigma=\{\sum a_i v_i:a_i\ge0\}$（$v_i\in N$ 有限个）且 $\sigma\cap(-\sigma)=\{0\}$。**扇** $\Delta$ 是整锥的集合：每个锥的面仍在 $\Delta$ 中，任两锥之交是公共面。对每个 $\sigma$ 取 $R_\sigma=\mathbb C[\sigma^\vee\cap M]$、$U_\sigma=\operatorname{Spec}R_\sigma$；若 $\tau$ 是 $\sigma$ 的面，则 $U_\tau\subset U_\sigma$ 是开子集。沿这些包含关系粘合，得到**环簇** $X_\Delta=\bigcup_\sigma U_\sigma$。""",
        r"""$\sigma^\vee=\{m\in M_{\mathbb R}:\langle m,v\rangle\ge0\ \forall v\in\sigma\}$；$X_\Delta$ 含环面 $T=N\otimes\mathbb C^*$ 作为稠密开子集。""",
        [
            r"$\Delta$ 的 $k$ 维锥对应 $X_\Delta$ 中余维 $k$ 的轨道闭包。",
            r"射影空间 $\mathbb P^n$ 对应以 $\mathbb R^{n+1}$ 中标准基向量张成的锥及其面组成的扇。",
            r"环簇的除子、线丛、上同调都可由扇的组合数据读出；这是环簇几何“组合化”的核心。",
        ],
        [r"X_\Delta=\bigcup_{\sigma\in\Delta}U_\sigma", r"R_\sigma=\mathbb C[\sigma^\vee\cap M]"],
        [
            r"把“扇”理解成一组孤立的锥：必须封闭于取面，且两两相交于公共面。",
            r"忘记整性：锥的生成元要落在格 $N$ 里，否则粘出来的不是簇而是栈。",
        ],
        [
            ("含糊点拨", "扇为什么够用", r"""每个 $U_\sigma$ 是仿射簇，$U_\tau\to U_\sigma$ 是局部化给出的开浸入；扇的公理恰好保证这些开浸入能无矛盾地粘合。"""),
            ("背景直觉", "环簇是“带组合骨架的射影空间”", r"""$\mathbb P^n$ 的扇由 $n+1$ 个射线锥组成；把扇细分（加射线）对应环簇的双有理修改，例如爆破。"""),
        ],
        ["amoeba", "dimer"],
        "§8.1", "ch08.tex:180-230",
    ),
    concept(
        "crepant-resolution", "第8章", "crepant 消解",
        ["crepant resolution", "crepant 消解", "典范类"],
        r"保持典范类的奇点消解：$K_{\widetilde X}=\pi^*K_X$，即消解不改变“扭曲程度”。",
        "为什么三维 Gorenstein 奇点总能找到 crepant 消解，而高维不一定？",
        r"""设 $\pi\colon\widetilde X\to X$ 是奇点消解。若 $K_{\widetilde X}=\pi^*K_X$（等价地，例外除子的典范类贡献为零），则称 $\pi$ 为 **crepant 消解**。它是最“经济”的消解：不引入额外的典范类扭曲。三维 Gorenstein 奇点必有 crepant 消解（Bridgeland–King–Reid，用 $G$-Hilbert 概形给出）；四维及以上可以不存在。""",
        r"""$K_{\widetilde X}=\pi^*K_X$；例外除子 $E_i$ 满足 $\sum a_iE_i$ 中 $a_i=0$。""",
        [
            r"crepant 是法语词，意为“响亮、干脆”；数学上取“不引入额外典范类”之意，中文文献多保留英文。",
            r"$\mathbb A^3/\mathbb Z_5$ 的 crepant 消解给出五次 Calabi–Yau 的镜像构造。",
            r"crepant 消解在派生等价下与矩阵分解、LG 模型相连（BKR 猜想/定理）。",
        ],
        [r"\pi\colon\widetilde X\to X,\quad K_{\widetilde X}=\pi^*K_X"],
        [
            r"把“crepant”当成“任意消解”：普通的奇点消解一般会改变典范类。",
            r"在维数 $\ge4$ 时默认存在性；这是三维 Gorenstein 的特权。",
        ],
        [
            ("易错预警", "crepant ≠ 极小", r"""极小消解要求例外除子没有负的自相交，crepant 要求典范类不变；两者在三维 Gorenstein 情形常同时成立，但不是同一定义。"""),
            ("背景直觉", "为什么镜像对称需要它", r"""B 侧的矩阵分解与 A 侧的消失圈只有在 crepant 消解上才匹配；非 crepant 消解会多出不属于 LG 模型的例外除子。"""),
        ],
        ["orbifold", "lg-model"],
        "§8.3", "ch08.tex:570-600",
    ),
    concept(
        "gentle-algebra", "第9章", "gentle 代数",
        ["gentle algebra", "gentle 代数", "温和代数"],
        "由箭图与单项式关系给出的一类特殊代数：每顶点至多两入两出、每箭至多属一个关系、无长度 $\\ge3$ 的既约圈。",
        "为什么“每顶点两入两出”这种组合条件，能让模范畴变得可以完全分类？",
        r"""设 $A=kQ/I$，$I$ 由长度 $2$ 的路径生成。若
(i) 每个顶点至多有两条入箭、两条出箭；
(ii) 每条箭至多出现在一个关系里；
(iii) 每个关系是两条长度 $2$ 的路径；
(iv) 不存在长度 $\ge3$ 的既约圈，
则称 $A$ 为 **gentle 代数**。它的不可分解对象由弦（string，不带圈的路径）与带（band，环状路径连同 $\lambda\in k^*$）完全分类。""",
        r"""$A=kQ/I$；弦对象 $S(i,w)$，带对象 $B(\lambda,n)$；关系 $I$ 由长度 $2$ 的路径生成。""",
        [
            r"gentle 代数必为双列代数（biserial），反之不然。",
            r"有限维 gentle 代数对应无内部标记点的带标记曲面；曲面上的弧给出弦模。",
            r"曲面的多边形剖分给出 gentle 代数，其 $A_\infty$ 结构的高阶乘积由曲面上的多边形计数给出。",
        ],
        [r"A=kQ/I", r"\text{每顶点至多 }2\text{ 入 }2\text{ 出}"],
        [
            r"与“温和（tame）表示型”混淆：gentle 是组合条件，tame 是表示型分类，二者不同。",
            r"漏掉“每条箭至多属一个关系”，会把一般双列代数误当成 gentle。",
        ],
        [
            ("易错预警", "gentle ≠ tame", r"""旧译“温和代数”容易与 tame（温和型）混为一谈；中文文献多保留 gentle，本译本从之。"""),
            ("背景直觉", "为什么曲面能造代数", r"""把曲面三角剖分，顶点给箭图、三角形给关系；曲面上弧的相交数就是 Ext 的维数，于是表示论变成曲面拓扑。"""),
        ],
        ["graded-surface", "quiver-representation"],
        "§9.1", "ch09.tex:4-70",
    ),
]
