---
id: glc/concept/kostant-component
type: concept
track: H
---

# Kostant 分支

> Kostant 截面在 Hitchin 零点的值给出正则幂零轨迹 $\mathfrak f^{\mathrm{glob}}$，唯一不可约分支 $\mathrm{Nilp}_{\mathrm{Kos}}$ 控制首个 Whittaker 系数。

**问题**：$\mathrm{Nilp}_{\mathrm{Kos}}$ 由哪条特殊轨迹选出，它在微局部上对应什么？

## 定义

全局 Kostant 截面是 Chevalley 映射的 Kostant 截面 $\mathfrak g^*/\!/G\to\mathfrak g^{*,\mathrm{reg}}$ 的全局对应物，并在取 $G$ 的商后理解。进行通常的全局扭转选择后，它在 Hitchin 底空间零点上的值给出一个特殊的正则幂零轨迹，记作 $\mathfrak f^{\mathrm{glob}}\subset\mathrm{Nilp}$。令 $\mathrm{Nilp}_{\mathrm{Kos}}$ 为包含这个轨迹的唯一不可约分支。在微局部意义下，$\mathrm{Nilp}_{\mathrm{Kos}}$ 是指数 Whittaker 核的对应物：将 Lagrange 图像 $d\psi\subset T^*\operatorname{Bun}_N^\Omega$ 与从 $\operatorname{Bun}_N^\Omega$ 到 $\operatorname{Bun}_G$ 的 Lagrange 对应复合，就得到全局 Kostant 切片。

*记号*：$\mathfrak g^{*,\mathrm{reg}}$ 为 $\mathfrak g^*$ 的正则元；$\mathfrak g^*/\!/G$ 为 Chevalley 商；$d\psi$ 为 Whittaker 特征标 $\psi$ 的微分所给的 Lagrange 图像；$\operatorname{Bun}_N^\Omega$ 为 $\Omega$-扭转 $N$-丛叠。

## 要点

- 全局 Kostant 截面是 Chevalley 映射的 Kostant 截面的全局对应物，在取 $G$ 的商后理解。
- 它要在 Hitchin 底空间的零点上取值，才得到特殊正则幂零轨迹 $\mathfrak f^{\mathrm{glob}}\subset\mathrm{Nilp}$。
- $\mathrm{Nilp}_{\mathrm{Kos}}$ 是包含 $\mathfrak f^{\mathrm{glob}}$ 的唯一不可约分支。
- 微局部描述：$d\psi$ 的 Lagrange 图像与 $\operatorname{Bun}_N^\Omega\to\operatorname{Bun}_G$ 的 Lagrange 对应复合，得全局 Kostant 切片。

## 关键公式

- $\mathfrak f^{\mathrm{glob}}\subset\mathrm{Nilp},\qquad \mathrm{Nilp}_{\mathrm{Kos}}\ \text{为包含}\ \mathfrak f^{\mathrm{glob}}\ \text{的唯一不可约分支}$
- $d\psi\subset T^*\operatorname{Bun}_N^\Omega\ \text{与}\ \operatorname{Bun}_N^\Omega\to\operatorname{Bun}_G\ \text{的 Lagrange 对应复合}\ \rightsquigarrow\ \text{全局 Kostant 切片}$

## 易错点

- 讲义英文作 distinguished regular nilpotent **locus**，[FR25] 的措辞是 distinguished **point**：$\mathfrak f^{\mathrm{glob}}$ 实为一个点（Hitchin 零点处的取值），不是轨道。译文「轨迹」译自 locus，勿读成 $G$-轨道。
- 轨迹与分支不同：$\mathfrak f^{\mathrm{glob}}$ 是轨迹，$\mathrm{Nilp}_{\mathrm{Kos}}$ 是包含它的不可约分支。
- 必须先做「通常的全局扭转选择」，否则 Hitchin 零点处的值不是所要的特殊轨迹。
- $\mathrm{Nilp}_{\mathrm{Kos}}$ 的「唯一性」按讲义是断言（Kostant 截面的性质），本章未证。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§13.5 Kostant 分支与第一个系数，p.66（PDF p.66），`源码/chapters/ch13.tex:106-108（全局 Kostant 截面与 Nilp_Kos）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FR25：https://arxiv.org/abs/2207.02955 — Kostant 切片与 Nilp 交于 distinguished point f^glob，该点在 Nilp 光滑轨迹上，故存在唯一不可约分支 Nilp_Kos 包含它——支持卡「唯一不可约分支」
- FR25：https://arxiv.org/abs/2207.02955 — ˚Nilp_reg:=Maps(X,˚N/G) 开于 ˚Nilp；Kostant 切片给基点 f^glob∈˚Nilp_reg；Nilp_Kos⊂˚Nilp_reg 为对应连通分支，显式 Nilp_Kos=˚Nilp_{(2−2g)ρ̌}
- FR25：https://arxiv.org/abs/2207.02955 — dψ: Bun_N^Ω→T*Bun_N^Ω 与 T*Bun_N^Ω–T*Bun_G 的 Lagrange 对应复合，所得 Lagrange 恰为全局 Kostant 切片，并称其为 coeff 的 microlocal shadow——支持卡的微局部描述
- NT25：https://arxiv.org/abs/2206.09216 — shifted Whittaker functional 计算 Hitchin 模空间上 Kostant 截面与全局幂零锥交点处的微茎——支持「Nilp_Kos 是指数 Whittaker 核的对应物」

## 关联

- `glc/concept/global-nilpotent-cone`
- `glc/concept/microlocal-index-theorem`
- `glc/concept/hecke-moving-theorem`
