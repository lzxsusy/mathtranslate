---
id: dmod/concept/local-system
type: concept
track: G
---

# 局部系（局部常值层）

> 解析簇上局部同构于常值层 $\underline{k}^{\oplus q}$ 的层；它等价于配平坦联络的 $\mathcal O_X$-模，是 Riemann–Hilbert 对应的一端。

**问题**：局部系的层论定义是什么，它为什么可以作为平坦联络那一侧的对应物出现在 Riemann–Hilbert 对应中？

## 定义

设 $X$ 是 $k$ 上的代数簇，$X^{an}$ 是其解析化。$X^{an}$ 上的局部系指一个层 $\mathcal L$，使每点有开邻域 $U$ 与整数 $q\ge0$ 及同构 $\mathcal L|_U\cong\underline{k}^{\oplus q}$；等价地，$\mathcal L$ 是局部常值层。在连通分支上 $q$ 为常数，称为 $\mathcal L$ 的秩。讲义 §2 的批注把配平坦联络 $\nabla$ 的 $\mathcal O_X$-模与局部系等同（经典 Riemann–Hilbert 情形），并在 §4 的批注里指出：$\dim X=1$ 的正则奇点情形，$D_{rh}(X)$ 的每个对象都来自局部系。

*记号*：$X^{an}$：$X$ 的解析化；$\underline{k}$：常值层；$q$：秩；$D_{rh}(X)$：正则奇点（正则完整）模构成的范畴，见 $\dim X=1$ 的批注。

## 要点

- 局部系是 $X^{an}$ 上的层，每点局部同构于常值层 $\underline{k}^{\oplus q}$；等价说法是「局部常值层」，秩在连通分支上是常数。
- 局部系与配平坦联络的 $\mathcal O_X$-模等价，这就是 Riemann–Hilbert 对应的经典情形（§2 批注）。
- 取 de Rham 复形把局部系送到 $\mathcal D_X$-模一侧，批注给出 $\mathrm{dR}:D^b_{rh}(X)\cong D^b_c(X^{an},\mathbb C)$，并注明归 Mebkhout–Kashiwara–Beilinson–Bernstein。
- $\dim X=1$ 的正则奇点情形，局部单值化给出 Deligne 的结论：$D_{rh}(X)$ 的每个对象都来自局部系（§4 批注）。
- 局部系不是 $\mathcal D_X$-模：它是解析簇上的层，只有经 de Rham 函子（或等价地经平坦联络的水平截面）才与模联系起来。

## 关键公式

- $\mathcal L|_U\cong\underline{k}^{\oplus q}$
- $\mathrm{dR}:D^b_{rh}(X)\ \cong\ D^b_c(X^{an},\mathbb C)$
- $\operatorname{rank}\mathcal L=q\quad(\text{在连通分支上})$

## 定理与证明

### 定理 5.2.1（联络的零截面刻画）（完整）

设 $X$ 是连通光滑代数簇，$\mathcal V$ 是非零凝聚 $\mathcal D_X$-模。则 $\mathcal V$ 是联络，当且仅当 $\operatorname{Ch}(\mathcal V)$ 含于余切丛的零截面，当且仅当 $\operatorname{Ch}(\mathcal V)$ 就是零截面，当且仅当 $\mathcal V$ 是有限秩局部自由 $\mathcal O_X$-模。

1. (ii)$\Rightarrow$(i)：仿射化，取好滤过 $F\mathcal V$，把 $\operatorname{Ch}(\mathcal V)$ 含于零截面翻译成 $\operatorname{Gr}\mathcal V$ 的零化子包含 $(D_1,\dots,D_n)$ 的某个幂，于是 $\operatorname{Gr}_p\mathcal V=0$（$p\gg0$），$\mathcal V$ 作为 $\mathcal O_X$-模凝聚。  
   *为什么*：Hilbert 零点定理把零点集包含关系翻译成理想的根包含关系，好滤过保证分次模有限生成。
2. (i)$\Rightarrow$(iv)：在仿射局部取 $s_1,\dots,s_q$ 使像构成 $T_x(\mathcal V)$ 的基，得 $\mathcal O_X^q\to\mathcal V$ 满射；再证 $\sum g_is_i=0$ 迫使 $g_i\in\mathfrak m_x^p$ 对一切 $p$，故 $s_i$ 局部自由。  
   *为什么*：Nakayama 引理给出满射，对 $p$ 的归纳用向量场作用与 II.2.15。
3. (iv)$\Rightarrow$(iii)$\Rightarrow$(ii) 与 (iii)$\Rightarrow$(ii) 直接：有限秩局部自由时取平凡滤过，特征簇含于零截面；零截面又投射到 $\operatorname{supp}(\mathcal V)=X$ 上，故等于零截面。  
   *为什么*：$X$ 连通时秩非零且局部常值，支集为 $X$。

*出处*：定理 5.2.1 / 原书 V §2, p.135–136


## 易错点

- 局部系是解析簇 $X^{an}$ 上的层，不是 $X$ 上的 $\mathcal O_X$-模，也不是 $\mathcal D_X$-模；三者只有通过平坦联络与 de Rham 函子才对应起来。
- 「局部常值」是对层的局部性质：它不意味着整体常值，整体信息正是单值表示（$\pi_1$ 的作用）所记录的内容。
- 讲义只在批注里陈述「平坦联络 $\Leftrightarrow$ 局部系」与 de Rham 等价，没有给出证明；不要把它当作讲义正文已证的定理。
- 秩的定义要求连通分支：在非连通簇上各分支的 $q$ 可以不同，写成一个整数只在连通情形成立。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §2 联络（Connections），批注，p.136（PDF p.142），`源码/chapters/chap5.tex:132-134（批注：局部系与 de Rham 对应）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §4 不可约完整模的分类，批注，p.140（PDF p.146），`源码/chapters/chap5.tex:274-276（批注：Deligne 与局部单值化）`

## 核验

状态：`external-confirmed`（2026-11-19）
- nLab：https://ncatlab.org/nlab/show/local+system — 条目断言局部系统就是局部常值层；与卡中「每点局部同构于常值层」的定义一致。
- nLab：https://ncatlab.org/nlab/show/Riemann-Hilbert+correspondence — 条目给出 $\mathrm{dR}:D^b_{rh}(X)\cong D^b_c(X^{an},\mathbb C)$，即局部系一侧经 de Rham 函子对应到正则完整模一侧。

## 关联

- `dmod/concept/flat-connection`
- `dmod/concept/riemann-hilbert-correspondence`
- `dmod/concept/deligne-regular-singular`
