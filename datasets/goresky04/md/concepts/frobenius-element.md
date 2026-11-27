# Frobenius 元素与局部因子

> `goresky04/concept/frobenius-element` · 轨道 A · 域与 Galois 侧 · 状态 dev

> **先自测**：$\Fr_p$ 是怎么被定义出来的，为什么它只在非分歧处良定义？

## 一句话

在非分歧素数 $p$ 处，Galois 表示经过 $\Gal(\overline{\bbF}_p/\bbF_p)$ 分解，后者的生成元在表示中的像就是 $\Fr_p$；它的特征多项式定义了局部因子。

## 定义

设 $\rho\colon\Gal(\Qbar/\bbQ)\to\GL(H)$，$p\neq\ell$。称 $\rho$ 在 $p$ 处非分歧，若 $\rho$ 在分解群 $\Gal(\overline{\bbQ}_p/\bbQ_p)$ 上的限制经过商 $\Gal(\overline{\bbF}_p/\bbF_p)$ 分解。此时 $\Gal(\overline{\bbF}_p/\bbF_p)\cong\hat{\bbZ}$ 有典则生成元（几何 Frobenius 的逆），取它在 $\rho$ 下的像即 $\Fr_p=\rho_p(\sigma_p)$。局部因子 $\zeta_p(\rho,t)=1/\det(I-t\Fr_p)$。

**记号**：$\sigma_p$ 是原文对 $\Fr_p$ 的记号；$\mathrm{Gal}(\overline{\bbF}_p/\bbF_p)\cong\hat{\bbZ}=\prod_{q}\bbZ_q$。

## 要点（为什么需要它）

1. 非分歧条件的作用是保证 $\rho$ 在惯性群 $I_p$ 上平凡，于是 $\Fr_p$ 的选取只差一个共轭——因此在 $\GL(H)$ 中共轭类良定义，特征多项式良定义。
2. 分歧处的局部因子更复杂，要引入 $\varepsilon$ 因子与导子；本文只处理非分歧处，因为「几乎所有 $p$ 都非分歧」对几何来源的表示成立。
3. $\Fr_p$ 不是唯一的元素，同一个共轭类里的任何元素给出的特征多项式相同，所以 $\zeta_p$ 是良定义的。

## 核心公式

$$
$\rho_p\colon\Gal(\overline{\bbF}_p/\bbF_p)\to\GL(H)$，$\Fr_p=\rho_p(\sigma_p)$$\zeta_p(\rho,t)=\dfrac{1}{\det(I-t\Fr_p)}$
$$

$$
$\zeta_p(\rho,t)=\dfrac{1}{\det(I-t\Fr_p)}$
$$

## 定理与证明（或缺口）

### 良定义性

若 $\rho$ 在 $p$ 处非分歧，则 $\Fr_p$ 的共轭类与 $\zeta_p(\rho,t)$ 都不依赖分解群的选取。

> 证明状态：**sketch**。原文只说「不难看出」，没有写出这三步；本卡的三步是译者按。

出处：`A p.7`

## 常见误解

- 原文在 $\Fr_p$ 与 $\sigma_p$ 之间混用记号（$\Fr_p=\rho_p(\sigma_p)$ 中 $\sigma_p$ 是抽象生成元，$\Fr_p$ 是它在表示里的像）；读的时候要分清「Galois 群里的元素」与「矩阵」。
- 几何 Frobenius 与算术 Frobenius 互为逆，取哪一个只影响 $t$ 与 $t^{-1}$，不影响 $\zeta$ 的有理性；本文不作区分。
- 非分歧的定义要求 $\rho$ 在惯性群上平凡，而不是只要求「$\rho$ 在 $I_p$ 上有有限像」；后者是一般情形，要用导子处理。

## 相关卡

[平展上同调与 Galois 作用](../concepts/etale-cohomology.md) · [从 Frobenius 特征值造出局部因子与欧拉乘积](../derivations/local-zeta-factor.md) · [Satake 参数：非分歧局部表示的指纹](../concepts/satake-parameter.md)

## 出处（印刷页）

- A p.7（A p.7）

> 说明：对应原文 §4.4；「共轭类良定义」的证明是译者补的三步，原文只说「不难看出」。
