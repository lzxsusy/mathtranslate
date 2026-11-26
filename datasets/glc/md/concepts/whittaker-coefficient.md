---
id: glc/concept/whittaker-coefficient
type: concept
track: H
---

# 第一个 Whittaker 系数

> 把 $\mathcal F$ 拉回到 $N$-丛叠、以指数层扭转、再取紧支撑 de Rham 上同调得到的标量不变量，是 Whittaker 一侧全部构造的出发点。

**问题**：第一个 Whittaker 系数 $\operatorname{coeff}(\mathcal F)$ 由哪三步复合而成，取值落在哪个范畴？

## 定义

固定 Borel 子群 $B=TN$ 以及非退化加性特征标 $\psi:N\to\mathbb G_a$。令 $\operatorname{Bun}_N^\Omega$ 为通常的 $\Omega$-扭转 $N$-丛叠，它带有投影 $p:\operatorname{Bun}_N^\Omega\to\operatorname{Bun}_G$ 和 Whittaker 特征标 $\psi:\operatorname{Bun}_N^\Omega\to\mathbb A^1$。忽略标准的上同调归一化，第一个 Whittaker 系数是紧支撑 de Rham 上同调 $\operatorname{coeff}(\mathcal F):=C_{\mathrm{dR},c}\bigl(\operatorname{Bun}_N^\Omega,\,p^!(\mathcal F)\otimes\psi^!(\exp)\bigr)\in\operatorname{Vect}$。等价地，它是将 $\mathcal F$ 拉回到 Whittaker 叠后，以指数层扭转，再 $!$-推前到一点；移位的选择与 Verdier 对偶和下文的微局部指标公式相容。

*记号*：$C_{\mathrm{dR},c}$ 为紧支撑 de Rham 上同调；$p^!$ 为反常拉回；$\psi^!(\exp)$ 为指数层沿 Whittaker 特征标的 $!$-拉回；$\operatorname{Vect}$ 为（DG）向量空间范畴；$\Omega$ 为 $X$ 上的扭转参数。

## 要点

- 系数取值于 $\operatorname{Vect}$，即它是标量值泛函；取值于 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 的版本是重整化系数。
- 等价描述是三步复合：拉回到 Whittaker 叠、以指数层扭转、$!$-推前到一点。
- 讲义忽略了标准的上同调归一化，但移位并不随意：它要与 Verdier 对偶、与微局部指标公式相容。
- $\operatorname{coeff}:\operatorname{DMod}(\operatorname{Bun}_G)\to\operatorname{Vect}$ 经由到温和商的投影分解（讲义 §13.1 用作证明的第一个基本事实）。

## 关键公式

- $\operatorname{coeff}(\mathcal F):=C_{\mathrm{dR},c}\bigl(\operatorname{Bun}_N^\Omega,\,p^!(\mathcal F)\otimes\psi^!(\exp)\bigr)\in\operatorname{Vect}$
- $\operatorname{coeff}:\operatorname{DMod}(\operatorname{Bun}_G)\longrightarrow\operatorname{Vect}$，且经由到温和商的投影分解

## 定理与证明

### 系数经由温和商分解（要点（有缺口））

$\operatorname{coeff}:\operatorname{DMod}(\operatorname{Bun}_G)\to\operatorname{Vect}$ 经由到温和商的投影分解。

1. 讲义把它列为证明保守性所用的两个基本事实之一，没有给出论证。  
   *为什么*：该分解属于所要引用的 Whittaker 理论框架，本章不重新证明。

> 缺口：讲义只述不证：§13.1 把「$\operatorname{coeff}$ 经由到温和商的投影分解」作为第一个基本事实直接引用，未作说明。

*出处*：§13.1（讲义未编号的正文陈述）/ 原书 p.65


## 易错点

- $\psi$ 在讲义里同时表示 $N\to\mathbb G_a$ 的加性特征标和 $\operatorname{Bun}_N^\Omega\to\mathbb A^1$ 的 Whittaker 特征标，读公式时须按出现的位置区分。
- $\operatorname{coeff}$ 是 $\operatorname{Vect}$ 值的；把它当成 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 值，就会与 §13.1 的重整化版本混淆。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§13.1 普通系数函子与重整化系数函子，p.64（PDF p.64），`源码/chapters/ch13.tex:22-26（第一个 Whittaker 系数）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FR25：https://arxiv.org/abs/2207.02955 — 定义 coeff(F):=C_dR(Bun_N^Ω, p^!(F)^!⊗ψ^!(exp))[−dim Bun_N^Ω]；Remark 5.2.1.1 明说该移位含在定义里；5.2.1.2 称其为 the first Whittaker coefficient——支持卡的公式与「第一个 Whittaker 系数」
- FR25：https://arxiv.org/abs/2207.02955 — 「the functor coeff ≃ Hom(Poinc^!,−) factors through the projection to D(Bun_G)^temp」——支持卡 key_point「coeff 经由到温和商的投影分解」
- FR25：https://arxiv.org/abs/2207.02955 — 「coeff[dim Bun_G] … is t-exact and commutes with Verdier duality」，且 Euler 特征等于特征圈在 Nilp_Kos 的重数——支持卡「移位的选择与 Verdier 对偶和微局部指标公式相容」
- NT25：https://arxiv.org/abs/2206.09216 — 「The shifted Whittaker functional … calculates (shifted) microstalk … In particular (3.40) is exact and commutes with Verdier duality」——外部逐字支持移位与 Verdier 对偶相容

## 关联

- `glc/concept/renormalized-whittaker-coefficient`
- `glc/concept/whittaker-conservativity`
- `glc/concept/geometric-casselman-shalika`
