# 极小合冲猜想

> `grassmann/concept/minimal-syzygy-conjecture` · 轨道 2 · Koszul 上同调 · 状态 draft

> **先自测**：为什么 $s=1$ 与 $p=0$ 两个极端分别就是 Green 猜想与极大秩除子？

## 一句话

在 $\rho=0$ 的临界 $(r,s)$ 下，预言一般曲线每个 $g^r_d$ 的 $K_{p,2}$ 在 $p\le\frac{r-2s}{s+1}$ 时消没；$s=1$ 退化为 Green 猜想，$p=0$ 退化为定理 5.3。

## 定义

固定整数 $r,s\ge1$，令 $d:=rs+r$、$g:=rs+s$，于是 $\rho(g,r,d)=0$。**极小合冲猜想**（猜想 5.8）断言：对一般曲线 $[C]\in\mathcal{M}_g$、每个满足 $0\le p\le\frac{r-2s}{s+1}$ 的整数 $p$，以及每个线性系 $L\in W^r_d(C)$，都有消没 $K_{p,2}(C,L)=0$。

**记号约定**：$W^r_d(C)=\{L\in\Pic^d(C):h^0(C,L)\ge r+1\}$；$\rho(g,r,d)=g-(r+1)(g-d+r)$。

## 要点（为什么需要它）

- 它在 Green 猜想（$s=1$：$g\ge2p+3$ 时 $K_{p,2}(C,K_C)=0$，Voisin 主定理）与极大秩（$p=0$：定理 5.3）之间插值，$s$ 越大要求越弱。
- $d=rs+r$、$g=rs+s$ 使 $\rho(g,r,d)=g-(r+1)s=0$，正是定理 3.5 的秩相等条件；代入 $r=2s+sp+p$ 才得到极限 $p=\frac{r-2s}{s+1}$。
- 在极限 $p=\frac{r-2s}{s+1}\in\mathbb{Z}$ 处，失效轨迹 $\mathcal{Z}_{g,p}:=\{[C]:\exists L\in W^r_d,\ K_{p,2}(C,L)\neq0\}$ 是 $\mathcal{M}_g$ 上的有效除子，其闭包违背斜率猜想——这是它与 §1 的直接联系。
- 已知：$s=2$ 且 $g\le22$ 由 Farkas 证明；一般 $s$ 仍开放。

## 关键公式

$$
d=rs+r,\qquad g=rs+s,\qquad \rho(g,r,d)=0
$$

$$
K_{p,2}(C,L)=0\quad\text{对 } 0\le p\le\frac{r-2s}{s+1},\ \forall L\in W^r_d(C)
$$

$$
\rho(g,r,d)=g-(r+1)(g-d+r)
$$

## 定理与证明（或缺口）

### 猜想 5.8（极小合冲猜想）

固定 $r,s\ge1$，$d=rs+r$、$g=rs+s$（故 $\rho=0$）。对一般曲线 $[C]\in\mathcal{M}_g$ 与每个整数 $0\le p\le\frac{r-2s}{s+1}$，以及对每个 $L\in W^r_d(C)$，有 $K_{p,2}(C,L)=0$。

**证明状态：只引出处，原书不重证**


出处：中译 p.52（猜想 5.8）

### 两个极端情形

$s=1$ 时 $d=2r$、$g=2r+1$，条件 $0\le p\le\frac{r-2}{3}$ 就是 $g\ge2p+3$，猜想化为一般曲线的 Green 猜想（Voisin 定理）；$p=0$ 时它化为定理 5.3 断言的 $\nu_2$ 极大秩。

**证明状态：只引出处，原书不重证**


出处：中译 p.52（猜想 5.8 的讨论）

## 易错点

- 量词按字面读会被超椭圆曲线打破：原文「对每个 $L\in W^r_d(C)$」若对任意 $[C]$ 都成立，$s=1$ 时超椭圆（$\mathrm{Cliff}=0$）是反例，故必须读作对一般曲线（笔记疑问 6）。
- 把 $p$ 的上界读成总是正：$r=2s$ 时上界为 $0$，猜想退化为 $K_{0,2}=0$（即定理 5.3）；$r<2s$ 时上界为负，断言为空。
- $d=rs+r$、$g=rs+s$ 不是随便的数值：它们让 $\rho=0$，而 $g=s(2s+sp+p+1)$（秩相等）只在极限 $p$ 处与 $g=rs+s$ 相容。
- 把 $\mathcal{Z}_{g,p}$ 与 $\mathcal{Z}_{g,0}$（§5.1 的极大秩除子）混为一谈：前者是 $K_{p,2}$ 的失效轨迹，后者是 $\nu_2$ 的失效轨迹，$p=0$ 时才重合。

## 相关卡

- [Koszul 闭链与退化轨迹](../concepts/koszul-cycle.md)
- [极大秩猜想](../concepts/maximal-rank-conjecture.md)
- [Green 猜想](../concepts/greens-conjecture.md)
- [有效除子的斜率](../concepts/slope-of-effective-divisor.md)

## 出处

- ch2 §5.2 极小合冲猜想；中译 p.52（英文 PDF p.56），源码 `chapters/ch02.tex:904`
- ch2 §5.2 退化情形；中译 p.52（英文 PDF p.56），源码 `chapters/ch02.tex:918`
