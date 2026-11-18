---
id: dmod/concept/characteristic-variety
type: concept
track: B
---

# 特征簇（$D(n)$-模，第 I 章）

> 对有限生成 $D(n)$-模，用次数滤过下分次模零化子的根在 $k^{2n}=T^*k^n$ 中截出闭锥 $\operatorname{Ch}(M)$；它是模的几何不变量，维数等于 Bernstein 维数。

**问题**：特征簇是怎样由分次模的零化子定义的，它为什么与好滤过的选取无关，又为什么其维数等于 Bernstein 维数？

## 定义

设 $M$ 是有限生成 $D(n)$-模，$F M$ 是它关于微分算子次数滤过 $F D(n)$ 的好滤过。则 $\operatorname{Gr}M$ 是分次环 $\operatorname{Gr}D(n)=k[X_1,\dots,X_n,\xi_1,\dots,\xi_n]$ 上的有限生成分次模（$\xi_i$ 是 $\partial_i$ 的象征）。设 $I$ 是 $\operatorname{Gr}M$ 在 $\operatorname{Gr}D(n)$ 中的零化子，它是分次理想，其根 $r(I)$ 也是分次理想且与好滤过的选取无关（引理 7.2），称为 $M$ 的\emph{特征理想} $J(M)$。$M$ 的\emph{特征簇}定义为 $k^{2n}$ 中的闭代数集 $$\operatorname{Ch}(M)=V(J(M))\subset k^{2n}.$$ 由于 $J(M)$ 关于 $\xi_1,\dots,\xi_n$ 齐次，$\operatorname{Ch}(M)$ 是锥。

*记号*：$k^{2n}$ 的坐标记作 $(x,\xi)=(x_1,\dots,x_n,\xi_1,\dots,\xi_n)$，与 $T^*k^n$ 的余切坐标等同；$V(I)$ 是理想 $I$ 的零点集；$\pi:k^{2n}\to k^n$，$\pi(x,\xi)=x$；$d(M)$ 是 Bernstein 维数；$\operatorname{supp}(M)$ 是 $M$ 作为 $k[X_1,\dots,X_n]$-模的支集。

## 要点

- 若 $(x,\xi)\in\operatorname{Ch}(M)$，则对任意 $\lambda\in k$ 有 $(x,\lambda\xi)\in\operatorname{Ch}(M)$：特征簇是余切丛中的锥（引理 7.3）。
- 对有限生成 $D(n)$-模的短正合列 $0\to M'\to M\to M''\to 0$ 有 $\operatorname{Ch}(M)=\operatorname{Ch}(M')\cup\operatorname{Ch}(M'')$（命题 7.4）。
- 支集是特征簇在 $\pi$ 下的像：$\operatorname{supp}(M)=\pi(\operatorname{Ch}(M))$（命题 7.5）。
- 维数等于 Bernstein 维数：$\dim\operatorname{Ch}(M)=d(M)$（定理 7.7）；特别地，$M\neq0$ 时 $\dim\operatorname{Ch}(M)\ge n$（定理 7.13）。
- 两个基本例子：$\operatorname{Ch}(\mathcal O_n)=k^n\times\{0\}$ 而 $\operatorname{Ch}(\Delta_n)=\{0\}\times k^n$（例 8.2、8.3）。
- 在光滑簇 $X$ 上，凝聚 $\mathcal D_X$-模的特征簇是 $T^*(X)$ 的闭子簇，构造逐仿射开集粘合（第 III 章 §3）。

## 关键公式

- $\operatorname{Ch}(M)=V(J(M))\subset k^{2n}$
- $\dim\operatorname{Ch}(M)=d(M)$
- $\operatorname{Ch}(M)=\operatorname{Ch}(M')\cup\operatorname{Ch}(M'')$
- $\operatorname{supp}(M)=\pi(\operatorname{Ch}(M))$
- $(x,\xi)\in\operatorname{Ch}(M),\ \lambda\in k\ \Longrightarrow\ (x,\lambda\xi)\in\operatorname{Ch}(M)$

## 定理与证明

### 定理 7.7（特征簇的维数等于 Bernstein 维数）（完整）

设 $M$ 是有限生成 $D(n)$-模，则 $$\dim\operatorname{Ch}(M)=d(M).$$

1. 先设 $M=D(n)/L$，$L$ 为左理想。对 $D(n)$ 取次数滤过、对 $L$ 与 $M$ 取诱导滤过，得 $\operatorname{Gr}M=\operatorname{Gr}D(n)/\operatorname{Gr}L$，故 $\operatorname{Ch}(M)=V(\operatorname{Gr}L)$，只需证 $\dim V(\operatorname{Gr}L)=d(D(n)/L)$。  
   *为什么*：分次化保持正合，且 $\operatorname{Gr}M$ 的零化子恰为 $\operatorname{Gr}L$，故其特征簇就是 $V(\operatorname{Gr}L)$。
2. 引入加权滤过 $F^{(s)}$（$|I|+s|J|\le m$）。由引理 7.8、7.9 的双向维数比较得 $d(D(n)/L)=d(A/\operatorname{Gr}^{(s)}L)$，其中 $A=k[X,\xi]$；再由引理 7.10 得 $d(D(n)/L)=\dim V(\operatorname{Gr}^{(s)}L)$。  
   *为什么*：两个 Hilbert 型函数被双向不等式夹住，故其多项式次数相同；而 $\operatorname{Gr}^{(s)}L$ 是 $A/\operatorname{Gr}^{(s)}L$ 的零化子，由 §4 的维数—零点集对应得第二条等式。
3. 由引理 7.12，对 $L$ 的有限个生成元可取充分大的 $s$ 使 $\sigma^{(s)}(D_i)=\sigma(\operatorname{Symb}(D_i))$；于是 $\operatorname{Gr}(\operatorname{Gr}L)\subset\operatorname{Gr}^{(s)}L$，从而 $\dim V(\operatorname{Gr}L)\ge\dim V(\operatorname{Gr}^{(s)}L)=d(D(n)/L)$。  
   *为什么*：理想包含反转零点集的包含，取维数后不等号方向不变；这是所需的一个方向。
4. 反向不等式：$T\in F^{(1)}_p(L)$ 的次数 $\le p$，故 $\dim_k F^{(1)}_p(L)\le\dim_k F_p(\operatorname{Gr}L)$；逐 $p$ 相减得 $\dim_k F_p(A/\operatorname{Gr}L)\le\dim_k F^{(1)}_p(D(n)/L)$，取多项式次数得 $\dim V(\operatorname{Gr}L)\le d(D(n)/L)$。  
   *为什么*：$F^{(1)}_p(L)$ 到其次数分次片的映射是单射，维数不等式逐项成立，再对 $p$ 取次数。
5. 一般情形对 $M$ 的生成元个数归纳：取 $M'$ 由 $q-1$ 个生成元生成、$M''$ 循环，用 $d(M)=\max(d(M'),d(M''))$（3.9）与 $\operatorname{Ch}(M)=\operatorname{Ch}(M')\cup\operatorname{Ch}(M'')$ 归结到已证的循环情形。  
   *为什么*：并集的维数等于各自维数的最大值，而 §3 的维数对短正合列也取最大值，两边同时归纳。

*出处*：定理 7.7 / 原书 p.27–31

### 定理 7.13（非零模的特征簇维数下界）（完整）

设 $M$ 是有限生成 $D(n)$-模，$M\neq0$，则 $$\dim\operatorname{Ch}(M)\ge n.$$

1. 非零有限生成模的 Bernstein 维数满足 $d(M)\ge n$（定理 6.3）。  
   *为什么*：这是 §6 的 Bernstein 定理：由 $D_p(n)$ 到 $\operatorname{Hom}_k(F_pM,F_{2p}M)$ 的单射比较多项式次数，得 $2n\le2d(M)$。
2. 由定理 7.7，$\dim\operatorname{Ch}(M)=d(M)$。  
   *为什么*：特征簇的维数与 Bernstein 维数相等，已在定理 7.7 证明。
3. 合并两步即得 $\dim\operatorname{Ch}(M)=d(M)\ge n$。  
   *为什么*：两个等式/不等式直接复合。

*出处*：定理 7.13 / 原书 p.31


## 易错点

- 特征簇用的是**次数滤过**的分次环，而不是 Bernstein 滤过的分次环；两者虽都同构于多项式环，但变量的加权不同，混用会把 $J(M)$ 算错。
- 特征簇不是支集：$\operatorname{Ch}(M)\subset k^{2n}$ 而 $\operatorname{supp}(M)=\pi(\operatorname{Ch}(M))\subset k^n$；$\operatorname{Ch}(\mathcal O_n)=k^n\times\{0\}$ 时支集仍是整个 $k^n$。
- 零化子本身依赖好滤过，只有它的根（特征理想）不依赖；把 $J(M)$ 写成「$\operatorname{Gr}M$ 的零化子」是错的。
- $\dim\operatorname{Ch}(M)$ 是在 $k^{2n}$（实维数 $2n$ 的仿射空间）中取的，不是纤维方向或底空间方向的维数；在一般光滑簇上要用逐纤维的 $\dim_{p_X^{-1}(x)}$，不能照搬整体维数。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），§7 特征簇，p.25-26-27-28-29-30-31（PDF p.31-32-33-34-35-36-37），`源码/chapters/chap1.tex:936-1159（定理 7.7、7.13）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译校订批注本，150 页），III §3 特征簇，p.83-84-85（PDF p.89-90-91），`源码/chapters/chap3.tex:211-330（III §3 特征簇）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/characteristic-ideal`
- `dmod/concept/bernstein-dimension`
- `dmod/concept/holonomic-module`
- `dmod/concept/singular-support`
- `dmod/concept/characteristic-variety-sheaf`
