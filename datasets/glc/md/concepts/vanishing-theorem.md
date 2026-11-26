---
id: glc/concept/vanishing-theorem
type: concept
track: D
---

# Gaitsgory 消失定理

> E 几何不可约、秩 n、k<n 且 d>nk(2g−2) 时 Av_E^d=0；更一般地界为 d>(2g−2)k·rank(E)。

**问题**：消失定理的两个界如何统一理解，k=1 时它退化成什么？

## 定义

设 $E$ 为 $X$ 上秩 $n$ 的几何不可约局部系统，$k<n$，$\operatorname{Av}^d_E$ 为 $\operatorname{Bun}_k$ 上的平均函子（见另一张卡）。

*记号*：$g$ 为 $X$ 的亏格；$d$ 是 Hecke 修改的长度。

## 要点

- 界 $d>nk(2g-2)$ 中 $n=\operatorname{rank}(E)$，$k$ 是 $\operatorname{Bun}_k$ 的下标。
- 更一般的界把假设放宽为 $\operatorname{rank}(E)>k$，界为 $d>(2g-2)k\cdot\operatorname{rank}(E)$；两式是同一增长率的不同写法，不是两个独立条件。
- $k=1$ 时这是 Deligne 关于 Abel–Jacobi 的消失定理。
- 第 6 章用本定理证明洁净性定理。

## 关键公式

- $d>nk(2g-2)\ \Longrightarrow\ \operatorname{Av}^d_E=0$
- $\operatorname{rank}(E)>k$ 时，界为 $d>(2g-2)k\cdot\operatorname{rank}(E)$

## 定理与证明

### 消失定理（Gaitsgory）（要点（有缺口））

若 $E$ 几何不可约且秩为 $n$，$k<n$，并且 $d>nk(2g-2)$，则
\[
\operatorname{Av}^d_E=0.
\]
更一般地，当 $\operatorname{rank}(E)>k$ 时，消失定理适用于 $\operatorname{Bun}_k$ 上的平均函子，其界为 $d>(2g-2)k\cdot\operatorname{rank}(E)$。

1. 讲义只陈述该定理，未在书中展开证明。  
   *为什么*：它作为洁净性证明的输入被引用。

> 缺口：证明归因于 Gaitsgory 关于平均函子的消失定理 [Gai04]、[Gai16b]；讲义只引用不证明，书中没有展开。

*出处*：定理 5.7.2 / 原书 p.36


## 易错点

- 两个界要合起来读：$\operatorname{Av}^d_E$ 的核是 $\pi^*\mathcal{L}_E^d$，而 $\mathcal{L}_E^d$ 的「体积」随 $\operatorname{rank}(E)$ 与 $d$ 同时增长，两条界只是同一增长率的不同写法，不是两个独立条件。
- $k=1$ 的退化情形是 Deligne 的 Abel–Jacobi 消失定理，不要与一般 $k$ 的界混写。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§5.7 洁净性与平均消失，p.36（PDF p.36），`源码/chapters/ch05.tex:114-123（定理 5.7.2）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Gaitsgory 2002 (arXiv:math/0204081)：https://arxiv.org/abs/math/0204081 — Conjecture 1.3: 'Assume that E is irreducible, of rank > n. Then for d, which is greater than (2g−2)·n·rk(E), the functor Av_E^d is identically equal to zero.' The abstract says the paper establishes the vanishing. With book's k = paper's n, the bound and rank(E)>k condition match; the book's 'geometrically irreducible' implies the paper's 'irreducible', so the theorem applies. The k<n form is the special case rank(E)=n.

## 关联

- `glc/concept/averaging-functor`
- `glc/concept/cleanness-expected`
- `glc/concept/drinfeld-clean-extension-gl2`
- `glc/concept/fiber-calculation-surjective`
