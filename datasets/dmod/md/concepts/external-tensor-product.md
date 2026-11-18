---
id: dmod/concept/external-tensor-product
type: concept
track: D
---

# 外张量积 $M\boxtimes N$

> 把 $X$ 上与 $Y$ 上的模外张量成 $X\times Y$ 上的模：$\boxtimes$ 保持有限生成、使维数相加、使特征簇按换序映射变化，是复合直像与投影公式里的基本积。

**问题**：$\boxtimes$ 为什么把维数与特征簇都变成可加的量，换序映射 $q$ 又从哪里来？

## 定义

设 $M$ 是左 $\mathcal D_X$-模，$N$ 是左 $\mathcal D_Y$-模。定义 $$M\boxtimes N=M\otimes_kN,$$ 视为 $X\times Y$ 上的模，$\mathcal D_X\boxtimes\mathcal D_Y=\mathcal D_X\otimes_k\mathcal D_Y$ 通过 $(T\otimes S)(m\otimes n)=(Tm)\otimes(Sn)$ 作用，乘法为 $(T\otimes S)(T'\otimes S')=TT'\otimes SS'$。一般地，张量积取在两个 $k$-代数层上：$\mathcal D_X\boxtimes\mathcal D_Y=\mathcal D_X\otimes_k\mathcal D_Y$，且 $\mathcal D_X\boxtimes\mathcal D_Y=\mathcal D_{X\times Y}$（引理 9.1）。

*记号*：$M\in M_L(\mathcal D_X)$、$N\in M_L(\mathcal D_Y)$；$k$：基域；$F_pM$、$F_qN$：好滤过；$P(M,t)$：Poincaré 级数；$q$：交换 $x$ 与 $\xi$ 次序的映射 $T^*(X\times Y)\to T^*(X\times Y)$。

## 要点

- $\mathcal D_X\boxtimes\mathcal D_Y=\mathcal D_X\otimes_k\mathcal D_Y=\mathcal D_{X\times Y}$（引理 9.1），这是把两边的算子合并到乘积簇上的唯一自然方式。
- $M,N$ 有限生成 $\Rightarrow$ $M\boxtimes N$ 有限生成（引理 9.2）；维数可加 $d(M\boxtimes N)=d(M)+d(N)$（定理 9.3）；完整模的外张量积仍完整（推论 9.4）。
- 乘积滤过 $F_j(M\boxtimes N)=\sum_{p+q=j}F_pM\otimes_kF_qN$ 是好滤过，且 $\operatorname{Gr}_j(M\boxtimes N)\cong\bigoplus_{p+q=j}\operatorname{Gr}_pM\otimes_k\operatorname{Gr}_qN$（用引理 9.5、9.6），故 Poincaré 级数相乘。
- 特征簇按换序映射变化：$\operatorname{Ch}(M\boxtimes N)=q(\operatorname{Ch}(M)\times\operatorname{Ch}(N))$（定理 9.7）；支集相乘 $\operatorname{supp}(M\boxtimes N)=\operatorname{supp}(M)\times\operatorname{supp}(N)$（结论 9.8）。

## 关键公式

- $M\boxtimes N=M\otimes_kN,\qquad \mathcal D_X\boxtimes\mathcal D_Y=\mathcal D_{X\times Y}$
- $d(M\boxtimes N)=d(M)+d(N)$
- $\operatorname{Gr}_j(M\boxtimes N)\cong\bigoplus_{p+q=j}\operatorname{Gr}_pM\otimes_k\operatorname{Gr}_qN$
- $P(M\boxtimes N,t)=P(M,t)\,P(N,t)$
- $\operatorname{Ch}(M\boxtimes N)=q\bigl(\operatorname{Ch}(M)\times\operatorname{Ch}(N)\bigr)$

## 定理与证明

### 定理 9.3（外张量积的维数可加性）（完整）

设 $M$、$N$ 是有限生成模，则 $d(M\boxtimes N)=d(M)+d(N)$。

1. 取 $M$、$N$ 的好滤过，给 $M\boxtimes N$ 配乘积滤过 $F_j=\sum_{p+q=j}F_pM\otimes_kF_qN$，它是好滤过。  
   *为什么*：$\mathcal D_{X\times Y}=\mathcal D_X\otimes_k\mathcal D_Y$ 逐项作用，保持乘积滤过；有限生成性由引理 9.2 保证。
2. 逐次分量上，自然映射 $\bigoplus_{p+q=j}\operatorname{Gr}_pM\otimes_k\operatorname{Gr}_qN\to\operatorname{Gr}_j(M\boxtimes N)$ 是同构。  
   *为什么*：引理 9.5 把核写成交叉项之和 $\ker\otimes N+M\otimes\ker$，引理 9.6 的直和判定说明该核为零。
3. 于是 $P(M\boxtimes N,t)=P(M,t)P(N,t)$。  
   *为什么*：每个 $\operatorname{Gr}_pM$、$\operatorname{Gr}_qN$ 是 $k$-向量空间，长度对直和可加、对张量积可乘；按次数汇总即得级数相乘。
4. 按 $d$ 的定义（Poincaré 级数在 $t=1$ 处极点的阶，见定理 7.7）比较两边极点阶数，得 $d(M\boxtimes N)=d(M)+d(N)$。  
   *为什么*：极点阶数在级数相乘时相加，这正是 $d$ 的可加性。

*出处*：定理 9.3 / 原书 §9，p.37–39

### 定理 9.7（外张量积的特征簇）（要点（有缺口））

$M$、$N$ 有限生成时 $\operatorname{Ch}(M\boxtimes N)=q\bigl(\operatorname{Ch}(M)\times\operatorname{Ch}(N)\bigr)$，其中 $q$ 交换 $x$ 与 $\xi$ 的次序。


> 缺口：讲义只给出结论与「由 9.5、9.6 及乘积滤过的分次化」的提示，交换 $x$ 与 $\xi$ 次序的归约未逐步写出；完整论证见原书 §9 及 §7 关于特征簇在乘积下的行为。

*出处*：定理 9.7 / 原书 §9，p.39–40


## 易错点

- $\boxtimes$ 是 $\otimes_k$：它不是 $\otimes_{\mathcal O}$，也不是 $\otimes_{\mathcal D}$，$M\boxtimes N$ 一般不是某个有限生成模的「张量积」意义下的积。
- 特征簇公式中的 $q$ 交换 $x$ 与 $\xi$ 的次序，漏掉 $q$ 会把 $\operatorname{Ch}(M\boxtimes N)$ 与 $\operatorname{Ch}(M)\times\operatorname{Ch}(N)$ 当成同一集合。
- 分次化公式需要第 2 步的核为零；若只对两个滤过取张量积而不验证交叉项，分次模会多出 $\operatorname{Tor}$ 项。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§9 外张量积，p.36-37-38-39-40（PDF p.42-43-44-45-46），`源码/chapters/chap1.tex:1313-1436（定理 9.3、定理 9.7）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/good-filtration`
- `dmod/concept/characteristic-variety`
- `dmod/concept/direct-image-of-immersion`
