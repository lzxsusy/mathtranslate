---
id: glc/concept/fiber-calculation-surjective
type: concept
track: D
---

# 满射情形的纤维计算

> 满射情形：纤维是普通修改叠，所需 !-推前为 Av_E^d 的茎，度数估计给出 d>nk(2g−2)，故为零。

**问题**：满射情形中，d 与 ℓ 的关系是怎样算出来的？

## 定义

使用紧化 Whittaker 公式
\[
F_k\simeq\pi_!(p_1^*\mathcal{L}_E\otimes p_2^*\mathcal{L}_{\psi})[\text{移位}](\text{扭曲})|_{C'_k},
\]
其中 $p_1$ 记录挠商，$p_2$ 是 Whittaker 特征标。基变换后，取定一点 $(s_{\mathcal{T}}:\Omega_X^{k-1}\to\mathcal{T},\mathring{M})\in\widetilde{Z}$。相关纤维由 Whittaker 旗以及固定扩张
\[
0\longrightarrow\mathring{M}\longrightarrow M\longrightarrow\mathcal{T}\longrightarrow0
\]
之上的映射 $M_k\to M$ 组成，使复合 $\Omega_X^{k-1}=M_1\to M_k\to M\to\mathcal{T}$ 为固定映射 $s_{\mathcal{T}}$；诱导映射 $M_k\to\mathcal{T}$ 未必为满射。

*记号*：$d=\operatorname{length}(M/M_k)$ 是本次修改的长度；$\mathring{\deg}$ 为归一化次数。

## 要点

- 满射时 $\mathring{M}_k:=\ker(M_k\to\mathcal{T})$，且 $\mathring{M}/\mathring{M}_k\simeq M/M_k$，故纤维是普通修改叠。
- 所需的 $!$-推前是平均函子 $\operatorname{Av}^d_E$ 的一个茎。
- 归一化次数下 $M_k$ 的度为零、$\mathring{M}_k$ 的度为 $-\ell$。
- 条件 （2） 给出 $\mathring{\deg}\mathring{M}>nk(2g-2)$，于是 $d>nk(2g-2)+\ell$，消失定理适用。

## 关键公式

- $\{\mathring{M}_k\to\mathring{M}\mid\mathring{M}/\mathring{M}_k\in\operatorname{Tor}^d\}$
- $d=\mathring{\deg}\mathring{M}-\mathring{\deg}\mathring{M}_k>nk(2g-2)+\ell$

## 定理与证明

### 满射情形的纤维计算（要点（有缺口））

若 $M_k\to\mathcal{T}$ 为满射，令 $\mathring{M}_k:=\ker(M_k\to\mathcal{T})$，则纤维等价于普通修改叠
\[
\{\mathring{M}_k\to\mathring{M}\mid\mathring{M}/\mathring{M}_k\in\operatorname{Tor}^d\}.
\]
因此所需的 $!$-推前是 $\operatorname{Av}^d_E$ 的一个茎。在归一化次数下，Whittaker 旗的终点 $M_k$ 满足 $\mathring{\deg}M_k=0$，故 $\mathring{\deg}\mathring{M}_k=-\ell$；由于 $\mathring{M}\oplus\mathcal{T}\in C_k$，条件 （2） 给出 $\mathring{\deg}\mathring{M}>nk(2g-2)$。于是
\[
d=\mathring{\deg}\mathring{M}-\mathring{\deg}\mathring{M}_k>nk(2g-2)+\ell,
\]
所以 $d>nk(2g-2)$，消失定理给出 $\operatorname{Av}^d_E=0$，即该纤维的 $!$-推前为零。

1. 取定 $\widetilde{Z}$ 中一点，把相关纤维写成满足固定复合条件的 Whittaker 旗与映射 $M_k\to M$。  
   *为什么*：这是基变换后纤维的定义。
2. 满射时用蛇引理比较 $0\to\mathring{M}_k\to M_k\to\mathcal{T}\to0$ 与 $0\to\mathring{M}\to M\to\mathcal{T}\to0$，得 $\mathring{M}/\mathring{M}_k\simeq M/M_k$。  
   *为什么*：两个满射到同一个 $\mathcal{T}$，核的商同构于中间项的商。
3. 故纤维是修改叠 $\{\mathring{M}_k\to\mathring{M}\mid\mathring{M}/\mathring{M}_k\in\operatorname{Tor}^d\}$，所需 $!$-推前是 $\operatorname{Av}^d_E$ 的茎。  
   *为什么*：这正是平均函子的定义。
4. 用 $\mathring{\deg}M_k=0$、$\mathring{\deg}\mathring{M}_k=-\ell$ 与条件 （2） 得 $d>nk(2g-2)+\ell$，故 $d>nk(2g-2)$，由定理 5.7.2 消失。  
   *为什么*：$\ell\ge0$，且归纳层级满足 $k<n$。

> 缺口：这是定理 6.2.1 的满射情形（讲义 §6.5）；计算在讲义中给出，但结论依赖定理 5.7.2（只引用 [Gai04]、[Gai16b] 未证明）。

*出处*：§6.5 纤维计算与满射情形（定理 6.2.1 证明的一部分，原文未单独编号）/ 原书 p.38–39


## 易错点

- 归一化次数下 $M_k$ 的度为零、$\mathring{M}_k$ 的度为 $-\ell$，这两个度数是把 $d$ 与 $nk(2g-2)$ 比较的关键，不能漏。
- 满射性是对诱导映射 $M_k\to\mathcal{T}$ 说的，不是对 $M_k\to M$ 说的。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§6.5 纤维计算与满射情形，p.38-39（PDF p.38-39），`源码/chapters/ch06.tex:97-114（§6.5 纤维计算与满射情形）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv：https://arxiv.org/abs/math/0204081 — 摘要确认 Av_E^d 的消失定理由该文建立，即 gap_note 所称『定理 5.7.2 只引用 [Gai04]、[Gai16b] 未证明』的出处属实；但摘要不含 k<n、d>nk(2g−2) 的界，也不含归一化次数 deg(M_k)=0、deg(Ṁ_k)=−ℓ 与 d=deg(Ṁ)−deg(Ṁ_k) 的度数记账。

## 关联

- `glc/concept/induction-step-base-change`
- `glc/concept/vanishing-theorem`
- `glc/concept/non-surjective-reduction`
