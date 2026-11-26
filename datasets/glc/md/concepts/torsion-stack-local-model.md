---
id: glc/concept/torsion-stack-local-model
type: concept
track: E
---

# $\operatorname{Tor}^d$ 的局部模型与抛物对应

> 在 $X=\mathbb A^1$ 上长度 $d$ 挠层即 $d$ 维向量空间带自同态，故 $\operatorname{Tor}^d\simeq\mathfrak{gl}_d/\operatorname{GL}_d$；分支化为抛物对应。

**问题**：$\mathbb A^1$ 上的 $\operatorname{Tor}^d$ 为什么是整块 $\mathfrak{gl}_d/\operatorname{GL}_d$，而不是幂零锥？

## 定义

取 $X=\mathbb A^1=\operatorname{Spec}k[x]$。$\mathbb A^1$ 上长度 $d$ 的挠层就是一个 $d$ 维 $k[x]$-模：$x$ 的作用给出一个 $d\times d$ 矩阵，模同构就是 $\operatorname{GL}_d$-共轭，于是 $\operatorname{Tor}^d\simeq\mathfrak{gl}_d/\operatorname{GL}_d$。对 $d=d_1+d_2$，叠 $\operatorname{Tor}^{\mathrm{ses},d_1,d_2}$（子对象长 $d_1$、商长 $d_2$ 的短正合列）是抛物对应 $\mathfrak g/G\longleftarrow\mathfrak p/P\longrightarrow\mathfrak m/M$，其中 $G=\operatorname{GL}_d$，$P=P_{d_1,d_2}=UM$，$M\simeq\operatorname{GL}_{d_1}\times\operatorname{GL}_{d_2}$，$\mathfrak p,\mathfrak m$ 为相应 Lie 代数。

*记号*：$\mathfrak{gl}_d$ 是 $d\times d$ 矩阵的 Lie 代数（伴随作用下的商叠 $\mathfrak{gl}_d/\operatorname{GL}_d$）；$P=P_{d_1,d_2}$ 是保 $d_1$ 维子空间的抛物子群，$U$ 为其幂幺根、$M$ 为 Levi；$\mathfrak p,\mathfrak m$ 为 $P,M$ 的 Lie 代数。

## 要点

- $\operatorname{Tor}^d\simeq\mathfrak{gl}_d/\operatorname{GL}_d$ 取的是整块 $\mathfrak{gl}_d$，不额外要求 $x$ 幂零。
- 幂零的那些点构成幂零锥 $\mathcal{N}_d$，只是 $\mathfrak{gl}_d/\operatorname{GL}_d$ 中 $0$ 附近的一部分（第四章局部模型看到的就是这一部分）。
- 短正合列 $0\to M_1\to M\to M_2\to0$ 对应抛物子群 $P$ 的齐性空间：$\mathfrak g/G$ 记全空间、$\mathfrak p/P$ 记『$M_1$ 的 Lie 代数』一层、$\mathfrak m/M$ 记两块对角部分。
- 这个局部模型把因子化的几何内容化为常系数 Springer 陈述。

## 关键公式

- $\operatorname{Tor}^d\simeq\mathfrak{gl}_d/\operatorname{GL}_d$
- $\mathfrak g/G\longleftarrow\mathfrak p/P\longrightarrow\mathfrak m/M$
- $P=P_{d_1,d_2}=UM,\qquad M\simeq\operatorname{GL}_{d_1}\times\operatorname{GL}_{d_2}$

## 定理与证明

### $\mathbb A^1$ 上挠层的矩阵模型（完整）

对 $X=\mathbb A^1$，长度 $d$ 的挠层等同于『$d$ 维向量空间 + 一个自同态』，模同构即 $\operatorname{GL}_d$-共轭，故 $\operatorname{Tor}^d\simeq\mathfrak{gl}_d/\operatorname{GL}_d$。

1. $\mathbb A^1=\operatorname{Spec}k[x]$ 上长度 $d$ 的挠层即 $d$ 维 $k[x]$-模，由 $x$ 的作用矩阵唯一决定，反之任一 $d\times d$ 矩阵给出一个 $k[x]$-模结构。  
   *为什么*：$k[x]$-模结构由 $x$ 的像唯一确定。
2. $k[x]$-模同构即与该矩阵共轭的 $\operatorname{GL}_d$-作用，故模叠是 $\mathfrak{gl}_d$ 对 $\operatorname{GL}_d$ 的商叠。  
   *为什么*：换基把矩阵变成 $gAg^{-1}$，反之共轭的矩阵给出同构的模。

*出处*：§7.4 证明 / 原书 p.42


## 易错点

- 把 $\operatorname{Tor}^d$ 误当成幂零锥 $\mathcal{N}_d$：讲义明确取整块 $\mathfrak{gl}_d$；$\mathcal{N}_d$ 只是其中 $x$ 幂零的部分。
- 抛物对应中的 $P=P_{d_1,d_2}$ 对应『先取子对象再取商』的次序；交换 $d_1,d_2$ 会得到另一个（共轭的）抛物，$\mathfrak m/M$ 的两个因子随之交换。
- 这里只是 $\mathbb A^1$ 上的局部模型；断言在 $X$ 上要靠 étale 局部化搬回去，不能直接对一般曲线使用。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§7.4 Laumon 层通过短正合列的因子化（证明），p.42-43（PDF p.42-43），`源码/chapters/ch07.tex:94-103（$X=\mathbb A^1$ 的模型与抛物对应）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/coherent+sheaf — 页面只给 O_X-模的一般框架（A^1 上即 k[x]-模），未给出「长度 d 的挠层 ↔ d 维 k[x]-模 ↔ gl_d/GL_d」的叠同构，也未提抛物对应；不支持卡中两条断言。

## 关联

- `glc/concept/laumon-factorization`
- `glc/concept/grothendieck-springer-parabolic-restriction`
