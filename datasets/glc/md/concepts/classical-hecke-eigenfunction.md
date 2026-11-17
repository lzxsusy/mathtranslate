---
id: glc/concept/classical-hecke-eigenfunction
type: concept
track: C
---

# 经典 Hecke 特征函数

> 有限域上 GL_n 的球面自守函数在未归一化局部 Hecke 算子下按 ∧^d σ(Fr_x) 数乘本征，等价于按归一化 Satake 参数 γ_x 本征。

**问题**：球面自守函数 f 关于局部系统 σ 的第 d 个 Hecke 特征性质写成什么算子等式？

## 定义

设 $k$ 有限，$F=k(X)$，$\mathbb{A}$ 为 $F$ 的阿代尔环，$G=\operatorname{GL}_n$。设 $\sigma:\operatorname{Gal}(\overline F/F)\to\operatorname{GL}_n(\mathbb{Q}_\ell)$ 处处非分歧，等价地，它是 $X$ 上秩 $n$ 的局部系统。球面自守函数是定义在 $\operatorname{GL}_n(F)\backslash\operatorname{GL}_n(\mathbb{A})/\operatorname{GL}_n(\mathcal{O})$ 上的函数。对闭点 $x\in|X|$，记 $K_x$ 为局部域，$\mathcal{O}_x$ 为其整数环，$q_x=\#k(x)$，取素元 $t_x$，置 $M_n^d(\mathcal{O}_x):=\operatorname{GL}_n(\mathcal{O}_x)t_x^{(1^d,0^{n-d})}\operatorname{GL}_n(\mathcal{O}_x)\subset\operatorname{GL}_n(K_x)\subset\operatorname{GL}_n(\mathbb{A})$。未归一化局部 Hecke 算子为 $T_x^df(g)=\int_{M_n^d(\mathcal{O}_x)}f(gh)\,dh$。若对每个 $x\in|X|$ 都有 $T_x^df=q_x^{d(n-d)/2}\operatorname{Tr}\bigl(\bigwedge^d\sigma(\operatorname{Fr}_x)\bigr)f$，则称 $f$ 满足关于 $\sigma$ 的第 $d$ 个 Hecke 特征性质。

*记号*：$|X|$ 为闭点集；$\operatorname{Fr}_x$ 为 $x$ 处 Frobenius；$dh$ 为 $M_n^d(\mathcal{O}_x)$ 上的 Haar 测度（讲义未再指定归一化）；$t_x^{(1^d,0^{n-d})}$ 表示前 $d$ 个对角元为 $t_x$、其余为 $1$ 的对角元。归一化 Satake 参数 $\gamma_x\in\operatorname{GL}_n(\mathbb{Q}_\ell)$ 由 $\operatorname{Tr}\bigl(\bigwedge^d\gamma_x\bigr)=q_x^{d(n-1)/2}\operatorname{Tr}\bigl(\bigwedge^d\sigma(\operatorname{Fr}_x)\bigr)$（$0\le d\le n$）刻画。

## 要点

- 两种写法给出同一特征值：写成 $\sigma(\operatorname{Fr}_x)$ 时是 $q_x^{d(n-d)/2}\operatorname{Tr}\bigl(\bigwedge^d\sigma(\operatorname{Fr}_x)\bigr)$，写成归一化 Satake 参数 $\gamma_x$ 时是 $q_x^{-d(d-1)/2}\operatorname{Tr}\bigl(\bigwedge^d\gamma_x\bigr)$。
- $\gamma_x$ 由 $0\le d\le n$ 的 $n+1$ 个迹刻画；这些迹给出 $\gamma_x$ 的 $n$ 个特征值的全部初等对称函数，因而唯一确定半单元素 $\gamma_x$（译本译注）。
- Tate 扭转约定下记 $\gamma_x=\sigma((n-1)/2)(\operatorname{Fr}_x)$：$\gamma_x$ 与 $\sigma(\operatorname{Fr}_x)$ 只差标量 $q_x^{(n-1)/2}$，而 $(n-1)/2$ 正是半和正根 $\rho$ 在基本余权 $\varpi_1$ 上取的值（译本译注）。
- 尖点性在此是函数论条件：对幺幂根基为 $U$ 的抛物子群 $P\subsetneq\operatorname{GL}_n$，若 $\int_{U(F)\backslash U(\mathbb{A})}f(ug)\,du=0$ 对所有 $g\in\operatorname{GL}_n(\mathbb{A})$ 成立，则球面自守函数 $f$ 称为尖点函数。
- Lafforgue 定理（采用通常的有限阶行列式归一化）把这样的不可约 $\sigma$ 对应到具有上述非分歧特征值的尖点自守表示；球面向量在相差一个标量意义下唯一，Whittaker 归一化确定这个标量。

## 关键公式

- $T_x^df(g)=\int_{M_n^d(\mathcal{O}_x)}f(gh)\,dh$
- $T_x^df=q_x^{d(n-d)/2}\operatorname{Tr}\bigl(\bigwedge^d\sigma(\operatorname{Fr}_x)\bigr)f$
- $\operatorname{Tr}\bigl(\bigwedge^d\gamma_x\bigr)=q_x^{d(n-1)/2}\operatorname{Tr}\bigl(\bigwedge^d\sigma(\operatorname{Fr}_x)\bigr),\qquad 0\le d\le n$
- $\int_{U(F)\backslash U(\mathbb{A})}f(ug)\,du=0$

## 定理与证明

### Lafforgue 对应（讲义引述）（要点（有缺口））

采用通常的有限阶行列式归一化，Lafforgue 定理将具有上述非分歧特征值的尖点自守表示赋给这样的不可约 $\sigma$；球面向量在相差一个标量的意义下唯一，Whittaker 归一化确定这个标量。

1. 对处处非分歧的 $\sigma$ 取对应的尖点自守表示。  
   *为什么*：Lafforgue 定理（讲义引 [Laf18]）提供该对应。
2. 指出球面向量相差一个标量、由 Whittaker 归一化定标。  
   *为什么*：讲义只作此断言，未展开。

> 缺口：讲义只述不证，作为 [Laf18] 的结果引用；本卡不重复其证明。

*出处*：§3.2（原书 p.20）


## 易错点

- 常数因子不要混用：用 $\sigma(\operatorname{Fr}_x)$ 时是 $q_x^{d(n-d)/2}$，用 $\gamma_x$ 时是 $q_x^{-d(d-1)/2}$；两者相差的正是 $\gamma_x$ 与 $\sigma(\operatorname{Fr}_x)$ 之间的 $\rho$-移位。
- 「处处非分歧的 $\sigma$」与「$X$ 上秩 $n$ 的局部系统」在此被当作同一件事，这是讲义的前提约定，不是对任意表示成立。
- $T_x^d$ 是未归一化算子（积分未除体积），归一化只出现在特征值的幂次上；不要在 $T_x^d$ 的定义里额外乘 $q_x$ 的因子。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§3.2 经典 Hecke 特征函数，p.20（PDF p.20），`源码/chapters/ch03.tex:24-49（§3.2）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Tate+twist — Tate 扭转约定：卡中 γ_x=σ((n-1)/2)(Fr_x)，即 σ 扭 q_x^{(n-1)/2}
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — T_x^d f=q_x^{d(n-d)/2}Tr(∧^dσ(Fr_x))f，以及归一化 Satake 参数 γ_x 的刻画
- Lafforgue (Laf18)：https://arxiv.org/abs/1209.5352 — 尖点性：对每个真抛物 P，∫_{U(F)\U(A)}f(ug)du=0；Lafforgue 对应到尖点自守表示

## 关联

- `glc/concept/whittaker-character`
- `glc/concept/local-whittaker-eigenfunction`
