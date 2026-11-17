---
id: glc/concept/cuspidal-de-rham
type: concept
track: O
---

# 尖点 de Rham 形式（猜想）

> de Rham 侧应在 $\operatorname{DMod}_{\mathrm{coh}}(\operatorname{Bun}_G)$ 尖点部分与 $\operatorname{Coh}$ 的不可约局部系统侧间有 $t$-正合等价。

**问题**：尖点 de Rham 猜想中的等价为什么必须是 $t$-正合的，$\mathbb{L}_G^{-1}$ 把摩天层送到什么？

## 定义

设定：$k$ 是特征 $0$ 的代数闭域，层理论取 de Rham 情形（凝聚右 $D$ 模），$\operatorname{Bun}_G$ 是 $X$ 上 $G$ 丛的模叠；$\operatorname{LocSys}_{\check{G}}^{\mathrm{irred}}$ 是分类 $X$ 上几何不可约 $\check{G}$-局部系统族的代数几何对象，在 de Rham 情形它是光滑 Artin 叠。猜想断言：存在典范的 $t$-正合等价 $\mathbb{L}_G:\operatorname{DMod}_{\mathrm{coh}}(\operatorname{Bun}_G)_{\mathrm{cusp}}\simeq\operatorname{Coh}(\operatorname{LocSys}_{\check{G}}^{\mathrm{irred}})$，使 $\mathbb{L}_G^{-1}$ 将不可约 $\check{G}$-局部系统 $\sigma$ 处的摩天层映为以 $\sigma$ 为特征值的 Hecke 特征层 $\operatorname{Aut}_\sigma$。

*记号*：$\operatorname{DMod}_{\mathrm{coh}}$：凝聚右 $D$ 模；下标 $\mathrm{cusp}$：尖点部分；$\operatorname{Coh}$：凝聚层范畴；$\delta_\sigma$：$\sigma$ 处的摩天层；$t$-正合：把 $t$-结构的心送到心。

## 要点

- 这是猜想 1.2.3 的范畴形式：不再逐点赋层，而是要求从整个谱模对象出发的函子，并从理念上预期它与 $\operatorname{Shv}_c(\operatorname{Bun}_G)^\heartsuit$ 的尖点部分等价。
- 等价 $\mathbb{L}_G$ 是 $t$-正合的，这是「尖点」形式的标志。
- $\mathbb{L}_G^{-1}$ 把不可约 $\check{G}$-局部系统 $\sigma$ 处的摩天层送到 $\operatorname{Aut}_\sigma$，即逐点层面回到猜想 1.2.3 的对应。
- de Rham 情形 $\operatorname{LocSys}_{\check{G}}^{\mathrm{irred}}$ 是光滑 Artin 叠，因此谱侧可以取 $\operatorname{Coh}$。

## 关键公式

- $\mathbb{L}_G:\operatorname{DMod}_{\mathrm{coh}}(\operatorname{Bun}_G)_{\mathrm{cusp}}\simeq\operatorname{Coh}(\operatorname{LocSys}_{\check{G}}^{\mathrm{irred}})$
- $\mathbb{L}_G^{-1}(\delta_\sigma)\simeq\operatorname{Aut}_\sigma$
- $\operatorname{Coh}(\operatorname{LocSys}_{\check{G}}^{\mathrm{irred}})^\heartsuit\longrightarrow\operatorname{Shv}_c(\operatorname{Bun}_G)^\heartsuit,\qquad\delta_\sigma\longmapsto\operatorname{Aut}_\sigma$

## 定理与证明

### 猜想 1.3.1（尖点 de Rham 形式）（要点（有缺口））

存在典范的 $t$-正合等价
$$\mathbb{L}_G:\operatorname{DMod}_{\mathrm{coh}}(\operatorname{Bun}_G)_{\mathrm{cusp}}\simeq\operatorname{Coh}(\operatorname{LocSys}_{\check{G}}^{\mathrm{irred}}),$$
使 $\mathbb{L}_G^{-1}$ 将不可约 $\check{G}$-局部系统 $\sigma$ 处的摩天层映为以 $\sigma$ 为特征值的 Hecke 特征层 $\operatorname{Aut}_\sigma$。


> 缺口：这是猜想：讲义未证明，§1.3 只陈述它并说明它与朴素整体形式（定理 1.3.2）的差别。

*出处*：猜想 1.3.1 / 原书 p.8


## 易错点

- $t$-正合性是这条猜想的要害：若把可约局部系统也包括进来，就必须放弃 $t$-正合性、在范畴层面工作，那就是定理 1.3.2 的朴素整体形式。
- 左边的下标 $\mathrm{cusp}$ 不能省：等价的是 $\operatorname{Bun}_G$ 上凝聚 $D$ 模的尖点部分，不是整个 $\operatorname{DMod}_{\mathrm{coh}}(\operatorname{Bun}_G)$。
- 谱侧是心层面的 $\operatorname{Coh}(\operatorname{LocSys}_{\check{G}}^{\mathrm{irred}})$；非尖点的精确陈述要把这一侧换成带幂零奇异支撑的重整化范畴，例如 $\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check{G}})$。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§1.3 非分歧整体几何 Langlands 等价，p.8（PDF p.8），`源码/chapters/ch01.tex:186-190（猜想 1.3.1）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/geometric+Langlands+correspondence — 页面说典范等价把左端（DMod(Bun_G)）的摩天层送到右端（QCoh(LocSys)）的 Hecke 特征层，支持卡里 L_G^{-1}(δ_σ)≅Aut_σ 的方向；并记原初版本在一般情形为假、Arinkin–Gaitsgory 以幂零支撑的 ind-凝聚层替换 QCoh，支持卡的 IndCoh_Nilp 备注；但未陈述尖点部分的 t-正合等价 Coh(LocSys^irred)≃DMod_coh(Bun_G)_cusp。

## 关联

- `glc/concept/unramified-global-gl`
- `glc/concept/local-gl-schematic`
- `glc/concept/hecke-eigensheaf-general`
