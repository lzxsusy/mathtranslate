---
id: page/geometric-langlands
title: 几何 Langlands 对应：从 Drinfeld 到 FGV
aliases:
  - Drinfeld–Langlands 对应
  - 几何 Langlands 纲领
  - geometric Langlands
kind: topic
status: draft
version: 0.3
reviewed_by: []
reviewed_on: 2026-11-27
related:
  - page/kapustin-witten
entries:
  - geometry/geometric-langlands
  - geometry/bun-n
  - geometry/local-system
  - geometry/hecke-eigensheaf
  - geometry/hecke-correspondence
  - geometry/perverse-sheaf
  - geometry/verdier-duality
  - geometry/geometric-satake
  - geometry/geometric-class-field-theory
  - geometry/picard-variety
  - geometry/abel-jacobi
  - geometry/affine-grassmannian
  - algebra/langlands-correspondence
  - algebra/hecke-operator
parents:
  - page/langlands-program
order: 20
note: 引文取自 arXiv PDF 文本层，上下标已压平；逐字核对以所附页面链接为准。物理侧细节见配套页 page/kapustin-witten。
compiled_from:
  - id: sy0246/concept/betti-setting
    hash: 3d1a8cc4be76b25d
  - id: sy0246/concept/hecke-operator
    hash: 5ba6ffe01acebf6f
  - id: sy0246/concept/gl1-aut-e
    hash: 07be6cd06dfe6f83
  - id: sy0246/concept/main-theorem-fgv
    hash: 58d9cf6b9e4cdb9a
  - id: sy0246/concept/perverse-LdE
    hash: b40f48942bb4372d
  - id: sy0246/concept/vanishing-theorem
    hash: 669ef560fb1352ae
---

# 几何 Langlands 对应：从 Drinfeld 到 FGV

> 这是一页导航，不是一份讲义。数学陈述尽量以引文块给出并附页码；本页自己的话只回答三件事：为什么这样读、几条路线怎么选、证明去哪看。

## 0 导言：两个模空间

几何 Langlands 对应（又叫 Drinfeld–Langlands 对应）说的是一对模空间之间的对应：

- 一边是曲线 $X$ 上 $G$-丛的模空间 $\operatorname{Bun}_G(X)$，$G=\operatorname{GL}(n)$ 时记 $\operatorname{Fib}_n(X)$；
- 另一边是 $X$ 上 $\hat G$-局部系统的模空间 $\operatorname{LocSys}_{\hat G}(X)$，$G=\operatorname{GL}(n)$ 时就是秩 $n$ 局部系统的模空间。

「几何」二字指自守侧不再是函数而是**层**：$\operatorname{Bun}_G(X)$ 上的反常层（或 $D$-模、$\ell$-进层，看系数设定），谱侧则是曲线上的局部系统。对应的内容是：每个不可约的 $\hat G$-局部系统 $E$ 应当给出 $\operatorname{Bun}_G(X)$ 上一个**Hecke 特征层** $\operatorname{Aut}_E$，它的 Hecke 特征值正是 $E$。

为什么值得把这件事单独讲？因为它是 Langlands 纲领里少数几个「几何侧能真的构造出对象」的地方。整体 Langlands 说自守表示对应 Galois 表示，但两边都是难缠的对象；几何版本把「自守表示」换成「$\operatorname{Bun}_G$ 上的反常层」，把「Galois 表示」换成「$X$ 上的局部系统」，两边都成了可以取上同调、可以做 Fourier 变换的几何对象，于是「构造」第一次有了落脚点。

读这一页之前要知道它**不是**什么：它不是整体 Langlands 纲领的推论，也不包含 $L$-参数那一层。整体 Langlands 里的「谱侧」是 $\operatorname{Gal}(\bar F/F)$ 的表示，几何情形里换成了曲线 $X$ 上的局部系统；两者是类比，不是特例（见 {{entry:algebra/langlands-correspondence}} 与 {{entry:geometry/geometric-langlands}}）。

还有一层「为什么换成层」。整体情形里，自守形式是函数，Hecke 算子是积分算子，特征值给出 Satake 参数；层比函数多两样东西：一是可以取上同调（于是有「不可约」「中间延拓」这些结构），二是可以逐点取纤维（于是「特征值」变成「$E$ 的张量因子」）。Grothendieck 的函数–层字典说的正是这件事：层的 Frobenius 迹给出函数，但层本身携带更多信息。几何 Langlands 的「几何」二字，落点就在这里。

一个粗略的对照表，帮助定位：

| 整体 Langlands（算术） | 几何 Langlands（本页） |
|---|---|
| 整体域 $F$，$G/F$ 约化 | 曲线 $X/k$，$G$ 分裂 |
| 自守表示：$G(\mathbb A_F)$ 的表示 | 自守侧：$\operatorname{Bun}_G(X)$ 上的反常层 |
| 谱侧：$L$-群 ${}^LG$ 的 Galois 表示 | 谱侧：$X$ 上 $\hat G$-局部系统 |
| 函数域 $\operatorname{GL}_n$：Drinfeld、Lafforgue | $\operatorname{GL}_n$：Drinfeld、FGV+Gaitsgory |

表中的「函数域」一行是整体 Langlands 的结果，不要与几何侧混为一谈：前者证的是自守表示与 Galois 表示的对应，后者证的是层与局部系统的对应。

最后要分清「对应」这个词的三种强度，混用是这一行最常见的误读来源。

- **弱形式（集合/双射）**：谱侧的对象与自守侧的「某种东西」之间存在自然双射，但不指定自守侧对象的结构。经典的类域论大体处在这一层；Drinfeld 的 $\operatorname{GL}(2)$ 工作已经构造出具体的特征层，属于下一层。
- **中形式（Hecke 特征层）**：给每个谱侧对象 $E$ 配一个具体的层 $K_E$，并要求 $K_E$ 是 Hecke 算子的特征层（$H(K_E)\cong E\boxtimes K_E$）。这是本页第 5 节定理 2.2 的强度，也是 Laumon 906 与 FGV 的表述。
- **强形式（等价）**：两侧的导出范畴整体等价，例如 $D(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{{}^LG})$。这是 Scholze 1252 所述 Gaitsgory–Raskin 工作的强度（特征 $0$），需要额外的「谱侧取 nilpotent 支撑」修正；正特征的情形要再换 $\operatorname{LocSys}'$。

三种强度不是同一条定理的不同说法，而是三个不同的定理；引用时必须说清在哪一层。

## 1 对应的陈述

### 1.1 三条约定：底域、系数域、上同调

Laumon 把「三元组」作为整个报告的出发点：底域 $k$、系数域 $C$、以及一个 $C$-系数上同调理论。三种标准选择是 Betti（$k=\mathbb C$，经典拓扑下的可构造层）、de Rham（$\operatorname{char}k=0$，$C=k$，holonomic $D$-模）、$\ell$-进（$C=\mathbb Q_\ell$，étale 层；Laumon 原文如此）。

> [!quote] Laumon 2002, p.2 — [arXiv:math/0207078v1, p.2](https://arxiv.org/pdf/math/0207078v1#page=2)
> Dans le cas partout non ramifié qui fait l’objet de cet exposé, on espère établir une correspondance de Drinfeld-Langlands pour chaque triplet formé d’un corps de base k, d’un corps des coefficients C et d’une théorie cohomologique à coefficients dans C …

这三条不是装饰：同一条「对应」在不同设定里是不同难度的定理，公式的归一化也不同。本页以 Betti 设定为主（Laumon 906 全篇如此），$\ell$-进设定在讲到 FGV 原文时单独标出。两套设定的公式不能直接互换：FGV 的 Hecke 函子带半 Tate 扭 $\mathbb Q_\ell(\frac{n-1}{2})$，Betti 版没有这一项（详见 §2.3）。

### 1.2 自守侧与谱侧

**自守侧。** $G=\operatorname{GL}(n)$ 时，$\operatorname{Fib}_n(X)$ 是秩 $n$ 向量丛的叠；它是代数的、光滑的，纯维数 $n^2(g-1)$，连通分支按次数 $d$ 分成 $\operatorname{Fib}_n^d(X)$（Laumon 中译 p6 = 原文 p6）。自守侧的物件是 $\operatorname{Fib}_n(X)$ 上的反常层——不是函数，不是表示，是层。

**谱侧。** $\hat G$-局部系统。$G=\operatorname{GL}(n)$ 时 $\hat G=\operatorname{GL}(n,\mathbb C)$，局部系统就是秩 $n$ 的局部系统 $E$；主定理要求 $E$ 不可约。局部系统等价于基本群的表示，这正是「处处非分歧」的含义：$E$ 沿整个 $X$ 都有定义，没有分歧点。

对应的精确形式由 Hecke 算子写出：先有 Hecke 对应，再要求 $H(K)\cong E\boxtimes K$。这两步见下面两节。

### 1.3 为什么是「处处非分歧」

Laumon 的报告只处理 $X$ 射影、$G$ 分裂、处处非分歧的情形：谱侧是 $X$ 上的局部系统（而不是带分歧的 Galois 表示），自守侧不取任何级结构。这不是对 $G$ 的限制，而是对「分歧」的限制；也正因如此，$X$ 可以取任意域上的射影曲线，而不必是函数域。

> 更一般的情形（允许分歧、允许 level）本页不展开；它是几何 Langlands 的另一半，记号与这里不同。

## 2 自守侧：Hecke 算子

### 2.1 从函数到层：Hecke 算子在做什么

在整体 Langlands 里，Hecke 算子是自守表示上的算子：对每个点 $x$ 与每个 $\operatorname{GL}(n)$ 的表示，有一个卷积算子，特征值给出 Satake 参数。几何版本把「函数」换成「层」、「算子」换成「对应」，于是 Hecke 算子成了导出范畴上的一个函子：

$$H:D^b_c(\operatorname{Fib}_n(X))\to D^b_c(X\times\operatorname{Fib}_n(X)).$$

多出来的 $X$ 因子不是累赘：它记住「在哪个点做了修改」。特征方程 $H(K)\cong E\boxtimes K$ 就是说：在 $X$ 方向，$H(K)$ 不过是 $K$ 乘上局部系统 $E$。

### 2.2 初等下修改与 Hecke 叠

设 $x\in X$。$X$ 上秩 $n$ 的向量丛 $L$ 在 $x$ 处的**初等下修改**，指子丛 $L'\subset L$，使商 $L/L'$ 是集中于 $x$、长度为 $1$ 的摩天层；此时 $\deg L'=\deg L-1$。这是「只在一个点、只改一格」的最小修改。

> [!quote] Laumon 2002, p.7 — [arXiv:math/0207078v1, p.7](https://arxiv.org/pdf/math/0207078v1#page=7)
> Le champ de Hecke est le champ modulaire Hecken (X) des triplets (x, L, L′ ⊂ L)

Hecke 叠 $\operatorname{Hck}_n(X)$ 参数化三元组 $(x,L,L'\subset L)$，其中 $L'\subset L$ 是 $x$ 处的初等下修改（Laumon 中译 p6 = 原文 p7）。它是一个对应，不是算子：两个投影分别记住「大丛」与「小丛」，算子由推拉复合得到。

### 2.3 Hecke 对应与算子

Hecke 对应是图

$$\operatorname{Hck}_n(X)\xrightarrow{\ p\ }\operatorname{Fib}_n(X),\qquad
\operatorname{Hck}_n(X)\xrightarrow{(q,p')}X\times\operatorname{Fib}_n(X),$$

其中 $(q,p')(x,L,L'\subset L)=(x,L')$，$p(x,L,L'\subset L)=L$。两个投影分别是相对维数 $n-1$ 与 $n$ 的可表、射影、光滑态射（Laumon 中译 p6 = 原文 p7）。

Hecke 算子是

$$H(K)=(q,p')_*p^*K[n-1]\in D^b_c(X\times\operatorname{Fib}_n(X)),\qquad K\in D^b_c(\operatorname{Fib}_n(X)).$$

读法：大丛 $L$ 走拉回，小丛 $L'$ 走推前；$[n-1]$ 来自推前方的相对维数，拉回方的 $n$ 不进移位。输出多一个 $X$ 因子——这就是「特征」二字的位置。

迭代 $H\circ H$ 后，它在对角线的余集 $(X\times X-\Delta_X)\times\operatorname{Fib}_n(X)$ 上关于交换两个 $X$ 副本的作用是 $S_2$-等变的（Laumon 中译 p6 = 原文 p7）。等变只在对角线外要求，这一点在第 3 节会再出现：对角线上是「同一点做两次修改」，两次修改有先后，没有可交换的对象。

### 2.4 与 FGV 的记号对照

FGV 用四元组 $(x,M,M',\beta:M'\hookrightarrow M)$，$M/M'$ 非典范同构于 $\mathcal O_X(x)/\mathcal O_X$，并定义

$$H^1_n(K)=(\operatorname{supp}\times h_\to)_!\,h_\leftarrow^*(K)\otimes\mathbb Q_\ell(\tfrac{n-1}{2})[n-1]$$

（FGV 原文 p4，式 (1.2)）。这与 Laumon 的 $H(K)$ 是同一个几何对象（都是 $x$ 处长度 $1$ 的摩天层、次数少 $1$），但公式差一个半 Tate 扭：$\ell$-进设定里有 $\mathbb Q_\ell(\frac{n-1}{2})$，Betti 设定里没有。合稿时按设定分别写，不可直接等同。

局部模型（几何 Satake）不属于本节：它给出整体 Hecke 函子的输入，见 {{entry:geometry/geometric-satake}} 与 {{entry:geometry/affine-grassmannian}}。一句话区分：几何 Satake 是局部的——$\mathrm{DMod}(\mathrm{Gr}_G)^{L^+G}\simeq\operatorname{Rep}({}^LG)$ 的幺半等价（取 Grothendieck 群即经典 Satake 同构：球面 Hecke 代数 $\simeq$ $\operatorname{Rep}(\hat G)$ 的多项式表示环）；本节的 $H$ 是整体的（$\operatorname{Bun}$ 上的对应）。

把 $H$ 与经典 Hecke 算子对照一下会更清楚：经典情形取双陪集 $G(\mathcal O)\backslash G(F_x)/G(\mathcal O)$，卷积作用在自守形式空间上；几何情形把双陪集换成 Hecke 叠、把卷积换成推拉，作用在层的导出范畴上。$H(K)$ 多出的 $X$ 因子，正对应经典情形里「在点 $x$ 处」这个信息；$S_2$-等变则对应「不同点的 Hecke 算子交换」这一事实在层层面的加强版。

### 2.5 为什么移位是 $[n-1]$

Hecke 函子写作 $H(K)=(q,p')_*p^*K[n-1]$，很多人第一次看会问：这个 $[n-1]$ 从哪来。两个理由。第一是几何的：Hecke 对应中 $(q,p')$ 相对维数是 $n-1$，紧支撑前推沿纤维积分一次，就把维数降 $n-1$；要让算子把反常层送回反常层，必须补回这个次数，否则每次作用都掉进负次数。第二是结构的：只有补上 $[n-1]$，$H(K)$ 才可能与 $E\boxtimes K$ 落在同一个 $t$-心；否则「$H(K)\cong E\boxtimes K$」这句话本身就没有意义（两边不同类）。FGV 的 $\ell$-进版本把同一件事写成 $[n-1]$ 再加半 Tate 扭 $\mathbb Q_\ell(\tfrac{n-1}{2})$，扭的来历是他们的六函子约定与我们不同；两套记号不能逐字互换（见 2.4）。

## 3 谱侧：Hecke 特征层

### 3.1 特征方程

Laumon 的定义（定义 2.1）：$E$ 是 $X$ 上秩 $n$ 的不可约局部系统；$\operatorname{Fib}_n(X)$ 上的不可约反常层 $K$ 称为相对 $E$ 具有 **Hecke 性质**，若存在同构

$$H(K)\cong E\boxtimes K,$$

使诱导同构 $(H\circ H)(K)\cong E\boxtimes E\boxtimes K$ 在开集 $(X\times X-\Delta_X)\times\operatorname{Fib}_n(X)$ 上的限制是 $S_2$-等变的（Laumon 中译 p6 = 原文 p7；中译 PDF 第 6 页边注为 906--7）。

满足此性质的 $K$ 就是 $E$ 的 Hecke 特征层；主定理断言 $\operatorname{Aut}_E$ 存在。名字里的「特征」来自函数情形：Hecke 算子作用在自守形式上有特征值，几何版本把「特征值」换成了「$E$ 的张量因子」。

### 3.2 两套不可约性约定

这是全页最容易写错的地方，必须分开写：

- **Laumon（定义 2.1）**：$K$ 一开始就要求不可约，然后才谈 $H(K)\cong E\boxtimes K$ 与 $S_2$-等变；不可约性是**假设**。
- **FGV（§1.1）**：只要求 $K\neq 0$ 且存在同构 $H^1_n(K)\simeq E\boxtimes K$，并满足 (1.4) 的 $S_2$-等变；不可约性是**结论**（「irreducible on each connected component」写在猜想 1.3 里）。

两者不等价：Laumon 的定义窄，FGV 的定义宽。FGV 的宽定义方便陈述「存在性」，代价是必须另证不可约性——那正是第 6 节里消没定理与 proper 性要做的事。写综述时若把两者当成同一句话，就会把「假设」与「结论」互换，这是最典型的一类错误。

### 3.3 为什么需要 $S_2$-等变

它不是修饰，而是定义的一半，而且是从 $i=1$ 的 Hecke 性推到所有 $i$ 的唯一通道：由 $H(K)\cong E\boxtimes K$ 用两次得到 $(H\circ H)(K)\cong E\boxtimes E\boxtimes K$，$S_2$-等变正是要求这个同构与交换两个 $X$ 副本相容。

只在对角线外要求，是因为对角线上长度 $2$ 的修改不能拆成两个有序的长度 $1$ 步骤。FGV 的 Prop 1.5 与 (1.5) 正是把这条「$i=1$ + 对称性」升成所有 $i$ 的机制；SY02-33 的讲法更直白：第一 Hecke 特征性质加上交换不同点时的对称性，就推出所有微小特征性质。

## 4 $G=\operatorname{GL}(1)$：几何类域论

$n=1$ 时对应是定理，不是猜想。它既是整个纲领的出发点，也是第 6 节所有技术（对称积、下降、中间延拓）的雏形。

### 4.1 阿贝尔–雅可比映射

设 $X$ 是 $\mathbb C$ 上连通、光滑、射影曲线，亏格 $g$，基点 $x_0$。周期格 $\Lambda\subset\mathbb C^g$ 给出 $J(X)=\mathbb C^g/\Lambda$，阿贝尔–雅可比映射把 $x$ 送到 $\mathcal O_X([x]-[x_0])\in\operatorname{Pic}^0(X)$（见 {{entry:geometry/abel-jacobi}}）。减 $[x_0]$ 是为了落在次数 $0$ 的分支上；这也解释了为什么「点」会变成「线丛」。

> [!quote] Laumon 2002, p.5 — [arXiv:math/0207078v1, p.5](https://arxiv.org/pdf/math/0207078v1#page=5)
> Pour tout système local E de rang 1 sur X, il existe un unique système local (rigidifié à l’origine) AutE de rang 1 sur Pic0 (X) tel que ϕ∗ AutE = E.

定理 1.2 的存在性有两路：解析路用 $\pi_1$ 交换化，代数路用对称积下降。前者一句话：局部系统是 $\pi_1$ 的表示，$\pi_1(X)\twoheadrightarrow\pi_1(\operatorname{Pic}^0)\cong\Lambda$ 是商映射，故每个特征标 $\chi$ 唯一分解为 $\operatorname{Aut}_\chi\circ\varphi_*$，$\operatorname{Aut}_\chi$ 就是 $E$ 对应的那个局部系统。

后者是第 6 节全部技术的雏形，值得单独看（Laumon 中译 p5 = 原文 p5–6）：

1. 对称积 $X^{(d)}=X^d/S_d$，映射 $\varphi^{(d)}:X^{(d)}\to\operatorname{Pic}^0(X)$，$D\mapsto\mathcal O_X(D-d[x_0])$；$d\ge 2g-1$ 时它是秩 $d-g$ 的射影丛，纤维单连通。
2. $E^{(d)}=(r_*E^{\boxtimes d})^{S_d}$，纤维为 $\bigotimes_x\operatorname{Sym}^{d_x}E_x$（式 (1.3)）。
3. 秩 $1$ 时 $E^{(d)}$ 沿 $\varphi^{(d)}$ 的纤维常值，因纤维单连通而下降为 $\operatorname{Pic}^0(X)$ 上的局部系统，即 $\operatorname{Aut}_E$。

三步里每一步都在第 6 节放大：对称积对应 Laumon 层，单连通纤维对应「下降」，中间延拓对应 proper 性。

### 4.2 「唯一」必须带原点刚性化

若只要求 $\varphi^*\operatorname{Aut}\cong E$，则 $\operatorname{Aut}$ 还可张量一个从 $\operatorname{Spec}\mathbb C$ 拉回的常值局部系统，$\varphi^*$ 看不见它；此时只有「本质唯一」。把 $0\in\operatorname{Pic}^0$ 处的纤维固定为 $\mathbb C$，才得到严格唯一。

群律同构 $m^*\operatorname{Aut}_E\cong\operatorname{Aut}_E\boxtimes\operatorname{Aut}_E$ 记录 $\operatorname{Aut}_E$ 与 $\operatorname{Pic}^0$ 群结构的相容性；秩 $1$ 时它就是「$\operatorname{Aut}_E$ 是乘法群同态」的几何说法。

这就是处处非分歧的 $\operatorname{GL}(1)$ 几何 Langlands；它是 {{entry:geometry/geometric-class-field-theory}} 的几何版本，而不是整体类域论的复述：整体类域论讲 $\operatorname{Gal}^{\mathrm{ab}}$ 与 idèle 类群，这里讲 $\pi_1(X)^{\mathrm{ab}}$ 与 $\operatorname{Pic}^0(X)$ 上的局部系统。

### 4.3 与经典类域论的对照

经典（数域或函数域上的）类域论说：$\operatorname{Gal}^{\mathrm{ab}}(\bar F/F)$ 同构于伊代尔类群 $A_F^\times/F^\times$（的函数域版本是 $\operatorname{Pic}$ 的相应商）。几何版本把这个同构换成一个几何对象：$\pi_1(C)^{\mathrm{ab}}=H_1(C,\mathbb Z)$ 对应 $\operatorname{Pic}^0(C)$，而对偶 $\mathbb C^\times$ 的角色对应 $\operatorname{Pic}^0$ 上的秩 $1$ 局部系统。定理 1.2 的「$\varphi^*\operatorname{Aut}_E=E$」正是这种一一对应的精确形式：左边是 $H_1$ 的角色（局部系统 $E$），右边是 $\operatorname{Pic}^0$ 上的对象（$\operatorname{Aut}_E$），$\varphi$ 就是互反映射。

差别的要害在于「系数」：经典类域论的对象是 $\mathbb C^\times$ 值或 $\overline{\mathbb Q}_\ell$ 值的**函数**，几何版本的对象是**层**，从而可以张量化、可以取上同调、可以谈 Hecke 特征值而不必先有自守表示。这不是把定理换个说法，而是把定理放进一个更大的范畴里：$\operatorname{GL}(1)$ 之后还能往上走，正是因为层能承载非交换的 Hecke 算子。

## 5 主定理（$G=\operatorname{GL}(n)$）

> [!quote] Laumon 2002, p.8 — [arXiv:math/0207078v1, p.8](https://arxiv.org/pdf/math/0207078v1#page=8)
> Pour tout système local irréductible E de rang n sur X, il existe un faisceau pervers AutE sur Fibn (X) dont la restriction à chaque composante connexe Fibdn (X) est irréductible et qui a la propriété de Hecke relativement à E.

定理 2.2 的归属需要写清楚，否则很容易变成一句不实的「FGV 证明了它」：

- $n=2$ 由 Drinfeld 证明（[Dr 2]；另见 [Ga]）。
- 一般 $n$：FGV 的原文把主陈述写成 **Conjecture 1.3**（FGV p4），并明确说「In this paper we reduce Conjecture 1.3 to the Vanishing Conjecture 2.3」（FGV p4）。也就是说，FGV 做的是**归约**：假定消没猜想，则主猜想成立。
- 消没猜想本身：$k=\mathbb F_q$ 时由 Lafforgue 的结果推出（FGV §10）；一般情形由 Gaitsgory 证明（[Ga]），但他自限系数：特征 $0$，或 $\mathbb F_\ell$ 且 $\ell>d$。
- Laumon 906 把 FGV 的构造与 Gaitsgory 的消没合并，陈述为定理 2.2。所以正确的说法是「FGV + Gaitsgory」，而不是「FGV 证明了定理 2.2」。

定理 2.2 的结论有两部分：存在性，以及「限制到每个连通分支 $\operatorname{Fib}_n^d(X)$ 上不可约」。后者正是第 3 节说的、FGV 宽定义所缺的那一块：宽定义只保证 $K\neq0$，不保证不可约，所以 FGV 必须回来补证。

一个容易忽略的条件：$E$ 要求不可约。若 $E$ 可约，特征层可以不存在或需要更复杂的陈述；本页不展开这种情形。

> $n=2$ 还有另一种写法：Raskin 讲义定理 3.3.1 用 $\operatorname{PGL}_2$ 的 $\operatorname{Bun}$ 与 $\operatorname{SL}_2$-局部系统陈述同一对应（Raskin 中译 p13 = 原文 p10）。两种写法差一个行列式平凡化，不可混用。

## 6 证明路线：五步

本节只给路线图；每一步的细节在 Laumon 906 的对应小节，公式以原文为准。五步的顺序是：造种子层 → 造 $\operatorname{Aut}'_E$ → 用 Fourier 递推把 $i$ 推到 $n$ → 用消没定理换 proper 性 → 下降。

### 6.1 第一步：Laumon 层

先在对称积上造层。$E^{(d)}$ 是可构造复形；它在正则半单轨迹 $X^{(d)}_{\mathrm{rss}}$ 上的限制才是秩 $n^d$ 的局部系统（式 (1.3) 给出的是该限制在 $D$ 处的纤维）。复形 $E^{(d)}[d]$（把 $E^{(d)}$ 放在次数 $-d$）是反常层，且是它到正则半单轨迹 $X^{(d)}_{\mathrm{rss}}$ 上限制的中间延拓（引理 3.1）。

> [!quote] Laumon 2002, p.9 — [arXiv:math/0207078v1, p.9](https://arxiv.org/pdf/math/0207078v1#page=9)
> Pour chaque entier d ≥ 0, le faisceau pervers LdE associé à un système local E sur X est le prolongement intermédiaire de LdE,rss à Cohd0 (X) tout entier.

这个 $\mathcal L^d_E$ 是整个构造的种子：它是 $\operatorname{Coh}^d_0(X)$（长度 $d$ 的挠层叠）上的反常层，沿 $X^{(d)}\to\operatorname{Coh}^d_0$ 的 $d$-平移拉回就是 $E^{(d)}[d]$。

为什么选 $\operatorname{Coh}^d_0$ 而不是 $\operatorname{Fib}_n$？因为 Hecke 修改是「商 $L/L'$ 为长度 $d$ 的挠层」，挠层本身就是修改的数据；Laumon 的洞察是先把 $E$ 的对称幂搬到挠层叠上（那里有现成的中间延拓理论），再用 Hecke 对应把它推回丛的叠。这条「先到挠层、再回丛」的路线，是整篇技术结构的骨架。注意 $[d]$ 是把层放在次数 $-d$，不是把层本身平移——这是最常被写错的一处。

### 6.2 第二步：在 $\operatorname{Fib}'_n$ 上造 $\operatorname{Aut}'_E$

$\operatorname{Fib}'_n(X)$ 的参数是 $(L,s)$，$s:(\Omega^1_X)^{\otimes(n-1)}\hookrightarrow L$（模数乘）。在三元组 $(L,L_\bullet,s_\bullet)$ 的叠 $U_n$ 上（完全旗 + 一族线丛同构 $s_j:(\Omega^1_X)^{\otimes j-1}\cong L_{n-j+1}/L_{n-j}$），有两个态射：

- $f_n:U_n\to\operatorname{Fib}'_n(X)$，取 $s_n$ 诱导的截面；
- $g_n:U_n\to\mathbb A^1$，取各扩张类 $0\to L_j/L_{j-1}\to L_{j+1}/L_{j-1}\to L_{j+1}/L_j\to 0$ 之和；这些类落在 $\operatorname{Ext}^1_{\mathcal O_X}(\mathcal O_X,\Omega^1_X)\cong\mathbb C$。

$\mathbb G_m$ 按 $t\cdot(L,L_\bullet,s_\bullet)=(L,L_\bullet,t\cdot s_\bullet)$ 作用，$g_n$ 等变，取商后

$$L_n=(f_n)_!\,(g_n)^*\Psi[\dim U_n],$$

其中 $\Psi=\beta_*\mathbb C$ 是第 0 节定义的复形。$\Psi$ 是「非零扩张」的层化：它把「扩张类非零」这件事编码成一个反常层，从而让 $g_n$ 的纤维上的积分变成有意义的推前。

这一段里两个计算值得记住：$\operatorname{Ext}^1_{\mathcal O_X}(\mathcal O_X,\Omega^1_X)\cong H^1(X,\Omega^1_X)\cong\mathbb C$ 是 Serre 对偶给出的「一维」，所以 $g_n$ 的每个扩张类就是一个数；$\Psi$ 的 $H^0=\mathbb C$、$H^1=\alpha_*\mathbb C$ 则说明它把「零扩张」与「非零扩张」分开，这正是 $g_n$ 的纤维上「取非零部分」的层论实现。$\operatorname{Aut}'_E$ 再由 Hecke 对应 $\operatorname{Mod}'^d_n(X)$ 作用在 $\mathcal L^d_E$ 上得到（定义 4.1）。

### 6.3 第三步：Fourier 变换把 $i$ 推到 $i+1$

基本图把 $\operatorname{Coh}_i$ 与 $\operatorname{Coh}_{i+1}$ 用一对对偶向量丛 $\mathcal V_i\to\mathcal C_i$、$\mathcal V_i^\vee\to\mathcal C_i$ 连起来：开集 $\mathcal C_i$ 上 $\operatorname{Ext}^1((\Omega^1)^{\otimes i-1},\mathcal M_i)=0$（Serre 对偶 + 引理 5.1 的「非常不稳定」），故扩张 $0\to(\Omega^1)^{\otimes i}\to\mathcal M_{i+1}\to\mathcal M_i\to 0$ 的叠就是向量丛 $\mathcal V_i$；$\mathcal V_i^{\vee\circ}\cong\mathcal V_{i+1}^\circ$。

从 $K_{E,1}=(\iota_0)_*(\pi_0^{\vee\circ})^*\mathcal L_E$ 出发，递推

$$K_{E,i+1}=(\iota_i)_*\,(j_i^\vee)^*\,\operatorname{Four}_{\mathcal V_i/\mathcal C_i}\big((j_i)_!K_{E,i}\big).$$

这是整篇最技术的一步，但逻辑很干净：$\mathcal L^d_E$ 只认识 $\operatorname{Coh}^d_0$（长度 $d$ 的挠层），要把它搬到 $\operatorname{Fib}'_n$（带截面 $s$ 的丛），中间必须经过「部分旗」$\operatorname{Coh}_i$；每走一步用一次 Fourier 变换，把「$i$ 级旗」推到「$i+1$ 级旗」。引理 5.2 保证这一路推下来，在 $\mathcal V_i^\circ\cap\operatorname{Fib}'_i$ 上的限制正是 $M'^d_{i,E}(L_i)$；特别地 $K_{E,n}$ 与 $\operatorname{Aut}'_E$ 在相应开集上一致。

### 6.4 第四步：消没定理

> [!quote] Laumon 2002, p.14 — [arXiv:math/0207078v1, p.14](https://arxiv.org/pdf/math/0207078v1#page=14)
> Soit E un système local irréductible de rang n. … Alors, pour tout i = 1, . . . , n − 1 et tout entier d > in(2g − 2), le foncteur Mi,E … identiquement nul.

消没定理在证明里只用在**一个**地方：证明 $K_{E,i}$ 是 proper 的（命题 6.3 说 $(j_i)_!K_{E,i}\to(j_i)_*K_{E,i}$ 是同构）。路线是：在 $\operatorname{Fib}_i\cap\mathcal C_i$ 上 $\mathcal V_i^\circ$ 是零截面的补集，由引理 (0.3)（$L$ proper $\Leftrightarrow(\bar\pi^\circ)_!L=0$）只需证 $(\bar\pi_i^\circ)_!K_{E,i}=0$；由引理 5.2 逐分支这等于 $M^d_{i,E}(\pi'_*L_i)$，再用定理 6.1 得零。

proper 性的收益是：$K_{E,i}$ 的零延拓、$*$-延拓、中间延拓三者合一，于是可以「忘记」支撑继续下降；推论 6.4 由此得到 $K_{E,n}$ 在各分支上不可约；由引理 5.2，$\operatorname{Aut}'_E$ 在相应开集上也同样。换句话说，消没定理买的不是「某个上同调为零」，而是「支撑可以忘掉」——这正是下降的前提。

条件 $d>in(2g-2)$ 也值得看一眼：$i$ 是旗的级数，$n$ 是秩，$(2g-2)$ 是曲线的「复杂度」；$d$ 足够大时挠层「足够分散」，$\operatorname{Ext}^1$ 被迫消失，$\operatorname{Hom}$ 也消失，于是 $L$ 非常不稳定（引理 5.1）。$i=1$ 的情形就是 Deligne 的经典消没（注 6.2），一般 $i$ 由 Gaitsgory 补上。

### 6.5 第五步：下降

最后要从 $\operatorname{Fib}'_n$ 下降回 $\operatorname{Fib}_n$。工具是 Euler–Poincaré 示性函数 $\chi_K(s)=\sum_i(-1)^i\dim H^i(K_s)$ 与两条引理：

- 引理 7.1（Deligne）：$f:Y\to Z$ 紧合（或可表紧合叠态射），$K,K'$ 局部同构 $\Rightarrow\chi_{f_*K}=\chi_{f_*K'}$；
- 引理 7.2：$V\to S$ 常秩 $r$ 向量丛，$K$ 不可约反常层，则 $K\cong\pi^*(L)[r-1]$（$L$ 在 $S$ 上）当且仅当 $\chi_K$ 沿 $\pi$ 的纤维常值。

具体做法：用引理 7.4 把 $\operatorname{Aut}'_E$ 写成紧合前推 $f_*N^d_{n,E}(\Phi)$，由 7.1 知 $\chi$ 与 $E$ 无关；对平凡 $E$ 算出 $\chi$；再由 7.2 把「$\chi$ 沿纤维常值」翻译成「$\operatorname{Aut}'_E$ 来自 $\operatorname{Fib}_n$ 上的层」，即得 $\operatorname{Aut}_E$。

为什么绕道 $\chi$ 而不直接下降？因为 $\operatorname{Aut}'_E$ 不是显然常值的；$\chi$ 是可算的不变量，且对紧合前推不变，正好充当「常值性」的判据。

### 6.6 另一条路线

Scholze 1252 用现代语言重述同一件事：谱投影子、Whittaker 范畴、以及「特征层 = 特征函子的像」；它对一般约化群陈述定理 2.11（char 0）与定理 2.12（char $p\gg0$，谱侧换成 $\operatorname{LocSys}'$）。两条路线的关系见 {{entry:geometry/geometric-langlands}}；本页不展开。

两条路线的差别值得记一句：Laumon/FGV 走「显式构造 + 消没」，Scholze 走「函子性 + 谱投影子」；前者适合看 $\operatorname{GL}_n$ 的每一步，后者适合看一般 $G$ 的结构。

## 7 现状与开放问题

**$\operatorname{GL}(n)$。** $n=2$ 由 Drinfeld；任意 $n$ 由 FGV 的构造加 Gaitsgory 的消没（有限域情形消没可由 Lafforgue 推出）。这就是本页第 5 节的主定理。注意「$\operatorname{GL}_n$ 已证」指的是这个几何对应，不是整体 Langlands：后者的函数域情形由 Drinfeld 与 Lafforgue 证明，数域情形仍是重大未决问题。

**一般约化群。** $k$ 的特征 $0$ 时已是定理（Scholze 1252 定理 2.11，Gaitsgory–Raskin 等人的工作）；正特征 $p\gg0$ 有定理 2.12，但谱侧须换成 $\operatorname{LocSys}'$，且 $p$ 的限制是实质的。

**仍未解决。** 函子性（generalized / miraculous duality 之外的对应），任意特征 $p$，以及形式化：本仓库的 `leanstmt/laumon906-g01` 只是 $\operatorname{GL}(1)$ 定理 1.2 的**语句骨架**（`scope: gap`、`sorry_count: 1`、未编译），不是形式化证明。

还有三类问题不在本页展开：局部几何 Langlands（把 $X$ 换成形式圆盘、把 $\operatorname{Bun}$ 换成 $\operatorname{Gr}$ 或仿射 Grassmann 的环路群版本）；metaplectic 与量子化（把 $\hat G$-局部系统换成带辛结构的对象）；以及「函子性」——给定群同态 $H\to G$，两边的特征层是否相容。它们各自有独立的文献，混进本页只会让主线失焦。

## 8 物理侧：Kapustin–Witten 的图像

数学侧的对应在 2006 年多了一条独立解释：Kapustin 与 Witten 把它读成四维 $\mathcal N=4$ 超杨–米尔斯理论电磁对偶的一个推论。这一节只讲那条链条的骨架；细节、逐条页码与 KW 原文引文在配套页 [`page/kapustin-witten`](kapustin-witten.md)。

### 8.1 对偶群：从 Montonen–Olive 到 ${}^LG$

$\mathcal N=4$ 理论的 Montonen–Olive 对偶断言：规范群 $G$ 与它的 GNO 对偶群 ${}^LG$ 描述同一个物理。在 $G=\operatorname{GL}(n)$ 时 ${}^LG=\operatorname{GL}(n,\mathbb C)$——正是几何 Langlands 谱侧的那个群。KW 的第一步就是把这件事认出来：**谱侧的 ${}^LG$-局部系统，就是规范理论的对偶群。**

### 8.2 扭化与紧化：Hitchin 模空间登场

$\mathcal N=4$ 理论有三种拓扑扭化。KW 用的是 GL 扭化：它保留一半超对称，把理论变成四维拓扑场论；沿曲线 $C$ 紧化后，剩下的二维理论是目标为 Hitchin 模空间 $M_H(G,C)$ 的 $\sigma$-模型。扭化后的整族二维理论实际只依赖一个参数 $\Psi\in\mathbb{CP}^1$：$\Psi=\infty$ 时是复结构 $J$ 下的 B-模型，$\Psi=0$ 时是复结构 $K$ 下的 A-模型。四维的 $S$-对偶把 $\Psi$ 送到 $-1/(n_g\Psi)$（$n_g$ 为 $S$-对偶的标度因子，非单边群时取 2 或 3），恰好交换这两个值，于是 $M_H(G,C)$ 与 $M_H({}^LG,C)$ 在复结构 $J$ 下互为镜像流形。

### 8.3 线算子、膜与特征性

四维理论里的 Wilson 与 't Hooft 线算子，紧化后成为作用在 $M_H$ 的膜上的算子。KW 定义：一个膜若在该算子作用下只被乘以一个数（特征值），就称**特征膜**。于是：

- **电特征膜** ↔ 同态 $\pi_1(C)\to{}^LG_{\mathbb C}$，即谱侧的局部系统；
- **磁特征膜** ↔ $\operatorname{Bun}_G$ 上的 Hecke 特征层；
- **'t Hooft 算子** ↔ Hecke 算子。

这一条是全页与数学侧最直接的接口：它把「Hecke 特征层」翻译成「磁特征膜」，把「特征值 $E$」翻译成「电特征膜」。

### 8.4 落到 $\operatorname{Bun}_G$ 上

磁特征膜本身还在 Hitchin 模空间上，不在 $\operatorname{Bun}_G$ 上。KW 用 c.c. 膜（$(A,B,A)$ 型）作桥梁：$M_H$ 上复结构 $K$ 的每个 A-膜自然给出 $M(G,C)$ 上的 D-模；c.c. 膜的开弦代数就是扭化微分算子层，$\Psi=h$（$h$ 为 $G$ 的对偶 Coxeter 数）时扭化为零，恰好是普通微分算子。$G=\mathrm{U}(1)$ 时这就是 $\operatorname{Jac}(C)$ 上的平坦 $\mathbb C^*$-联络，与第 4 节的几何类域论逐项对上。

### 8.5 这条推导证明了什么

KW 自己划了两条边界（原文 p.5）：只处理**非分歧**情形；没有说明二维共形场论对这个纲领的用处。更要紧的是性质：这是**物理图像与一致性论证**，不是数学证明。数学侧是另一条独立路线——$\operatorname{GL}(n)$ 的非分歧情形由 FGV 加 Gaitsgory 消没（本页第 5–6 节），一般约化群特征 $0$ 由 Gaitsgory–Raskin 等人（Scholze 1252 定理 2.11）。两条路线在「对应存在、由 ${}^LG$-局部系统标号」这一点上汇合；引用时应说「物理机制」而不是「物理证明」。

### 8.6 三种语言对照

| 算术侧 | 几何侧（本页） | 物理侧（KW） |
|---|---|---|
| Galois 表示 $\sigma:\operatorname{Gal}(\bar F/F)\to{}^LG$ | 局部系统 $E$（$\pi_1(C)\to{}^LG_{\mathbb C}$） | 电特征膜、$\mathcal N=4$ 的一个真空 |
| 自守表示 $\pi$ | Hecke 特征层（perverse sheaf / D-模） | 磁特征膜、边界条件 |
| Hecke 算子 $T_v$ | Hecke 函子 $H$（对应上的积分） | 't Hooft 线算子 |
| 特征值 $a_v(\pi)$ | 特征同构 $H(K)\cong E\boxtimes K$ | 膜上的特征值 |
| 互反律 | 主定理（$\operatorname{GL}_n$） | $S$-对偶 $\leftrightarrow$ 镜像对称 |

## 9 怎么读这一页

- 想先看「对应是什么」：第 0、1 节 + {{entry:geometry/hecke-eigensheaf}}。
- 想先看「为什么 $\operatorname{GL}(1)$ 是定理」：第 4 节 + {{entry:geometry/abel-jacobi}}。
- 想先看「主定理怎么证」：第 6 节的五步；细节按 6.1→6.5 的顺序读 Laumon 906 的 §3–§7。
- 想先看「现在到哪了」：第 7 节 + {{entry:geometry/geometric-langlands}}。

### 依赖图

```
            Laumon 层 L^d_E (§3)
                    │
   Aut'_E 的构造 (§4) ── Fourier 递推 (§5) ── 消没定理 (§6) ── proper/IC
                    │                                              │
                    └────────────── 下降 (§7) ────────────────────┘
                                        │
                                    Aut_E (定理 2.2)
```

### 本页尚未做完的事

- 正文 10 个 `{{entry:…}}` 链接指向的词条仍是 draft，逐字引文与锚点未补；
- 定理转引（`{{transclude:…}}`）尚未接上词条锚点，现以引文块代替；
- 第 7 节的「一般约化群 char 0」只给 Scholze 1252 的定理编号（定理 2.11、2.12），未展开 Gaitsgory–Raskin 五篇的分工。

## 10 常见误解

**「$\operatorname{GL}_n$ 已证」＝整体 Langlands 已证？** 不是。几何对应与整体 Langlands 是两套猜想：前者在 $\operatorname{GL}_n$ 的处处非分歧情形已由 Drinfeld、Lafforgue、FGV、Gaitsgory 证明；后者的数域情形仍是重大未决问题。函数域上整体 Langlands 由 Drinfeld（$n=2$）与 Lafforgue（任意 $n$）证明，也不能直接搬到几何侧。

**FGV 证明了一般情形？** 不是。FGV 原文（`arXiv:math/0012255`）一般情形的主陈述是 Conjecture 1.3；他们把它归约到消没猜想 2.3，消没由 Gaitsgory（`arXiv:math/0204081`）处理。Laumon 906 把两者合起来陈述为定理 2.2，所以「FGV 证明了定理 2.2」这种写法不准确，应写「FGV 的构造 + Gaitsgory 的消没」。

**proper 反常层＝紧合态射？** 不是。proper 在这里是定义在 $\mathbb P(V)$ 上反常层的一个性质：遗忘支撑的态射 $j_!L\to j_*L$ 是同构。它与「紧合态射（morphisme propre）」只共享词根。译名因此保留英文 proper，避免与拓扑/代数几何的「紧合」混淆。

**$E^{(d)}[d]$ 是把 $E^{(d)}$ 平移 $d$ 次？** 方向相反。这里是把可构造层 $E^{(d)}$ 放在次数 $-d$（复形只有这一项），记作 $E^{(d)}[d]$；它成为反常层，是 $E^{(d)}$ 从 $X^{(d)}_{\mathrm{rss}}$ 到 $X^{(d)}$ 的中间延拓（引理 3.1）；到 $\operatorname{Coh}^d_0$ 的中间延拓是另一个层 $\mathcal L^d_E=\det^*E^{(d)}$（定义 3.2）。把「放低次数」读成「平移」是把复形与层两个范畴混为一谈。

**Betti 版与 $\ell$-进版可以逐字互换？** 不能。FGV 的 Hecke 函子带半 Tate 扭 $\mathbb Q_\ell(\tfrac{n-1}{2})$，Laumon 的 Betti 版没有；两者的六函子约定、对偶、甚至「有界」的含义都不同。跨设定引用公式时，先确认当前设定。

**物理推导＝证明？** 不是。Kapustin–Witten 给的是物理图像与一致性论证（第 8 节），数学证明是另一条独立路线（FGV + Gaitsgory，或 Gaitsgory–Raskin）。说「物理推出了几何 Langlands」会把两类不同性质的证据混在一起。
