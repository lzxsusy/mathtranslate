---
id: glc/concept/normalized-degree
type: concept
track: D
---

# 归一化次数

> C_k 第二个条件所用的次数：减去 O_X⊕Ω_X⊕…⊕Ω_X^{k−1} 的次数，并要求大于 nk(2g−2)。

**问题**：归一化次数比普通次数多减去了什么，为什么条件 （2） 要用它？

## 定义

设 $M_k\in C_k\subset\operatorname{Coh}_k$，以 $M_k^{\mathrm{tf}}$ 表示它的无挠商。归一化次数定义为
\[
\mathring{\deg}(M_k^{\mathrm{tf}}):=\deg(M_k^{\mathrm{tf}})-\deg\!\bigl(\mathcal{O}_X\oplus\Omega_X\oplus\cdots\oplus\Omega_X^{k-1}\bigr).
\]
本节使用的第二个条件是归一化次数必须足够大：
\[
\mathring{\deg}(M_k^{\mathrm{tf}})>nk(2g-2).
\]
从这里起，即使省去上圈，所有次数也都指归一化次数 $\mathring{\deg}$。

*记号*：$g$ 为 $X$ 的亏格，$n$ 为局部系统 $E$ 的秩；$\deg$ 是凝聚层在曲线 $X$ 上的次数。

## 要点

- 归一化次数减去的是 $\mathcal{O}_X\oplus\Omega_X\oplus\cdots\oplus\Omega_X^{k-1}$ 的次数，而不是单个 $\mathcal{O}_X$ 的次数。
- 条件 $\mathring{\deg}(M_k^{\mathrm{tf}})>nk(2g-2)$ 是第 5 章两个所需条件中的第二个。
- 讲义在第 6 章 §6.1 的条件 (2) 中使用这一归一化次数形式。
- 省去上圈后，$\deg$ 一律指 $\mathring{\deg}$；这个约定在第 6 章的估计中反复使用。

## 关键公式

- $\mathring{\deg}(M_k^{\mathrm{tf}})=\deg(M_k^{\mathrm{tf}})-\deg(\mathcal{O}_X\oplus\Omega_X\oplus\cdots\oplus\Omega_X^{k-1})$
- $\mathring{\deg}(M_k^{\mathrm{tf}})>nk(2g-2)$

## 易错点

- 不要把 $\mathring{\deg}$ 与 $\deg$ 混用：讲义从 §5.6 起约定所有次数都指归一化次数，读后面的估计时要按 $\mathring{\deg}$ 理解（条件 （2） 用的正是这一形式）。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§5.6 开子叠 C_k 与两个所需条件，p.35（PDF p.35），`源码/chapters/ch05.tex:87-99（§5.6 两个条件与归一化次数）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/geometric+Langlands+correspondence — The page has no definition of the normalized degree ndeg.

## 关联

- `glc/concept/opens-c-k-conditions`
- `glc/concept/averaging-functor`
- `glc/concept/naive-fourier-iteration`
