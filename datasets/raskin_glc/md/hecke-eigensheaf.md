# Hecke 特征层

- id：`raskin_glc/concept/hecke-eigensheaf`
- 类型：concept　轨道：D　状态：dev
- 一句话：以 $\sigma$ 为特征值的 Hecke 特征层是 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$-线性函子 $\operatorname{Vect}\to\operatorname{Shv}(\operatorname{Bun}_G)$，等价于对所有 $V$ 有 $\mathrm{H}_V(\mathcal{F})\cong\mathcal{F}\boxtimes V_\sigma$；2024 年定理给出存在性、半单性与特征圈。

**问题**：为什么「对所有 $V$ 的 Hecke 作用」比单个 $\mathrm{H}_{\mathrm{std}}$ 的等式更强？

## 定义

固定 $\check G$-局部系统 $\sigma$。定义求值函子 $\mathrm{ev}_\sigma:\operatorname{Rep}(\check G)_{\mathrm{Ran}}\to\operatorname{Vect}$：在 $\operatorname{Rep}(\check G)^{\otimes I}\otimes\operatorname{Shv}(X^I)$ 上，它把 $\boxtimes_i V_i\otimes\delta_{x_i}$ 送到 $\bigotimes_i (V_i)_\sigma|_{x_i}$，再取整体截面。称 $\mathcal{F}\in\operatorname{Shv}(\operatorname{Bun}_G)$ 为以 $\sigma$ 为特征值的 Hecke 特征层，若存在 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$-线性函子 $\Phi:\operatorname{Vect}\to\operatorname{Shv}(\operatorname{Bun}_G)$，$\underline{\e}\mapsto\mathcal{F}$，使 $\Phi$ 与 $\mathrm{ev}_\sigma$ 相容；等价地，对所有 $V$ 有 $\mathrm{H}_V(\mathcal{F})\cong\mathcal{F}\boxtimes V_\sigma$。

记号：$\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 为 Ran 空间上的 colimit 范畴；$\mathrm{H}_V$ 为 Hecke 函子；$V_\sigma$ 为 $\sigma$ 诱导的 $X$ 上局部系统。

## 要点

- 本征值不是标量而是局部系统：$\mathrm{H}_V(\mathcal{F})\cong\mathcal{F}\boxtimes V_\sigma$ 中的 $V_\sigma$ 是 $X$ 上的 lisse 层，随 $V\in\operatorname{Rep}(\check G)$ 函子性变化。
- $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 把「在所有点 $x\in X$ 同时做 Hecke 作用」的相容数据粘成一个范畴；Hecke 特征层是这个范畴在 $\operatorname{Shv}(\operatorname{Bun}_G)$ 上的一个表示。
- 等价性 $\mathrm{H}_V(\mathcal{F})\cong\mathcal{F}\boxtimes V_\sigma$（练习 4.2.4）说明：只要对所有 $V$ 验证，就得到整个 Ran 范畴的线性性。
- 定理 4.3.2（2024，Arinkin–Beraldo–Campbell–Chen–Faergeman–Gaitsgory–Lin–Raskin–Rozenblyum）：对不可约 $\sigma$（不来自真抛物），存在唯一 Hecke 特征层 $\mathcal{F}_\sigma$，且它 perverse、尖点、半单；其分量按 $\operatorname{Aut}(\sigma)$ 的不可约表示编号。
- 特征圈为 $[\mathrm{Nilp}]$：$\mathcal{F}_\sigma$ 的奇异支撑包含在整个幂零锥 $\mathrm{Nilp}\subset T^*\operatorname{Bun}_G$ 中，这是 2024 年定理最精细的部分之一。

## 公式

$$ \mathrm{H}_V(\mathcal{F})\cong\mathcal{F}\boxtimes V_\sigma $$

$$ \mathcal{F}_\sigma\cong\bigoplus_{\rho\in\operatorname{Irr}\operatorname{Aut}(\sigma)}\mathcal{F}_{\sigma,\rho}^{\oplus\dim\rho} $$

$$ \operatorname{coeff}_0(\mathcal{F}_\sigma)\cong\underline{\e} $$

## 定理与证明状态

### 定义 4.2.2（Hecke 特征层）

上述 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$-线性函子 $\Phi$（或等价地，对所有 $V$ 的等式 $\mathrm{H}_V(\mathcal{F})\cong\mathcal{F}\boxtimes V_\sigma$）定义以 $\sigma$ 为特征值的 Hecke 特征层。

- 证明状态：`none`
- 说明：定义；练习 4.2.3 说明 $\sigma$ 由 $\mathrm{ev}_\sigma$ 唯一确定。
- 出处：§4.2，原文 p.14

### 练习 4.2.4

$\mathcal{F}$ 为以 $\sigma$ 为特征值的 Hecke 特征层，当且仅当对所有 $V\in\operatorname{Rep}(\check G)$ 有 $\mathrm{H}_V(\mathcal{F})\cong\mathcal{F}\boxtimes V_\sigma$。

- 证明状态：`none`
- 说明：练习；由 Ran 范畴的泛性质与 $\mathrm{ev}_\sigma$ 的定义展开。
- 出处：§4.2，原文 p.14

### 猜想 4.3.1

若 $\sigma$ 为不可约 $\check G$-局部系统（不来自真抛物），则存在唯一 Hecke 特征层 $\mathcal{F}_\sigma$，且 $\operatorname{coeff}_0(\mathcal{F}_\sigma)\cong\underline{\e}$。

- 证明状态：`none`
- 说明：猜想；定理 4.3.2 在 char $k=0$ 时证明。
- 出处：§4.3，原文 p.14

### 定理 4.3.2（2024）

设 char $k=0$，$\sigma$ 不可约且不来自真抛物。则存在唯一 Hecke 特征层 $\mathcal{F}_\sigma$，它 perverse、尖点、半单；$\mathcal{F}_\sigma\cong\bigoplus_{\rho}\mathcal{F}_{\sigma,\rho}^{\oplus\dim\rho}$，其中 $\mathcal{F}_{\sigma,\rho}$ 为单 perverse 层；特征圈为 $[\mathrm{Nilp}]$。

- 证明状态：`cited`
- 说明：2024 年几何 Langlands 证明的产物；讲义只列结论与作者名单，证明见 GLC I–V 系列（arXiv:2405.03599 等）。
- 出处：§4.3，原文 p.14–15

## 易错点

- 本征值是局部系统 $\sigma$，不是标量；把 $V_\sigma$ 写成 $\dim V$ 会丢掉 $\sigma$ 的全部信息。
- $\operatorname{Rep}(\check G)$ 不是 $\operatorname{Rep}(G)$：原文 p.12 的 $\operatorname{Rep}(G)\to\operatorname{Shv}(X)$ 是笔误，对偶群才作用在 Hecke 侧（见疑点 Q14）。
- $\mathcal{F}_\sigma$ 一般不是 lisse；它是 perverse，奇异支撑非零。
- 归一化 $\operatorname{coeff}_0(\mathcal{F}_\sigma)\cong\underline{\e}$ 是猜想/定理的一部分；缺了它，$\mathcal{F}_\sigma$ 可乘以任意非零标量。

## 出处

- Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》（2025-07-07/11，18 页），§4.2 Hecke 性质与 §4.3 定理，pp. 14, 15；`源码/sections/s04-hecke.tex:L203-L300（Definition 4.2.2 与 Theorem 4.3.2）`
  > Definition 4.2.2. ... a Hecke eigensheaf with eigenvalue σ is a Rep(Ĝ)_Ran-linear functor Vect → Shv(Bun_G).

## 相关卡

- `raskin_glc/concept/geometric-satake`
- `raskin_glc/concept/pgl2-geometric-langlands`
- `raskin_glc/concept/categorical-geometric-langlands`
- `raskin_glc/remark/generic-rank-convention`

## 核验（partial，2026-11-27）

- nLab / geometric Langlands correspondence：`partial` — 页面给出粗版等价 $\mathcal{O}Mod(Loc_{{}^L G})\simeq\mathcal{D}Mod(\operatorname{Bun}_G)$ 与 2025 年证明的提及，支撑「存在 Hecke 特征层」的大方向；不涉及 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 的精确定义。

定义与 2024 年定理的陈述以原文为准；nLab 只支撑背景。
