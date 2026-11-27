# Abel–Jacobi 纤维被写成 $\Gamma(X,L)\setminus\{0\}$

- id：`raskin_glc/correction/abel-jacobi-fiber`
- 类型：correction　轨道：B　状态：dev
- 一句话：原文说 $\mathrm{AJ}_d$ 在 $L$ 处的纤维是 $\Gamma(X,L)\setminus\{0\}$；正确者应为射影空间 $\mathbb{P}\Gamma(X,L)$。否则纤维维数多一维，且去掉原点的仿射空间不紧、讨论单连通性时结论不同。

**问题**：为什么差一个 $\mathbb{P}$ 会同时破坏维数公式与单连通性论证？

## 位置

§1.2，原文 p.4（Deligne 构造的下降步骤）

## 原文

> The fiber of this map at $L$ is $\Gamma(X,L)\setminus 0$.

## 应为

> The fiber of this map at $L$ is $\mathbb{P}\Gamma(X,L)$.

## 理由

当 $d>2g-2$ 时 $H^1(X,L)=0$，故 $h^0(L)=d+1-g$。$\Gamma(X,L)\setminus\{0\}$ 的维数是 $d+1-g$，而 $\mathbb{P}\Gamma(X,L)$ 的维数是 $d-g$；后者才与 $\operatorname{Sym}^d X\to\operatorname{Jac}(X)$ 的纤维维数 $d-g$ 相符。此外 $\Gamma(X,L)\setminus\{0\}$ 是仿射空间去掉原点，不是紧的，也不是射影空间；讲义随后要用「纤维单连通」做下降，射影空间 $\mathbb{P}^{d-g}$ 单连通，而 $\mathbb{A}^{d+1-g}\setminus\{0\}$ 在 $d-g\ge 1$ 时同伦 $S^{2(d-g)-1}$，并不单连通。

## 说明

此笔误不影响构造 1.2.4 的最终结论（下降仍可沿射影化纤维进行），但正文的「纤维」与「单连通」两句话必须按 $\mathbb{P}\Gamma$ 理解；译文正文照录原文并加译注。

## 出处

- Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》（2025-07-07/11，18 页），§1.2，构造 1.2.4，pp. 4；`源码/sections/s01-intro.tex:L145-L150（原文照录与译注）`
  > The fiber of this map at L is Γ(X,L) ∖ 0.

## 相关卡

- `raskin_glc/concept/deligne-gl1-construction`

## 核验（partial，2026-11-27）

- nLab / local system：`not_applicable` — 页面确认局部系统与平坦联络的对应，但不涉及 Abel–Jacobi 纤维的维数；本卡的更正依据是原文自身的维数计算与 $\mathbb{P}\Gamma$ 的标准事实。

更正依据：$\dim\mathbb{P}\Gamma(X,L)=d-g$ 与 $\operatorname{Sym}^d X\to\operatorname{Jac}$ 的纤维维数一致；$\mathbb{P}^N$ 单连通。
