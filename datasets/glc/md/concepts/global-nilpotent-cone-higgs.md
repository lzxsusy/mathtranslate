---
id: glc/concept/global-nilpotent-cone-higgs
type: concept
track: F
---

# 全局幂零锥

> Higgs 叠中每个点的 Higgs 场逐点取值于幂零锥的闭子叠，是通常幂零锥 $\mathcal N_{\mathfrak g^*}$ 的全局对应物。

**问题**：全局幂零锥的条件为什么必须逐点 $x\in X$ 陈述，而不能只要求 $\varphi$ 整体落在某个锥里？

## 定义

对 $G$-丛 $P$，记 $\mathfrak g_P=P\times^G\mathfrak g$。$\operatorname{Bun}_G$ 的经典余切叠是 Higgs 叠
$$T^*\operatorname{Bun}_G\simeq\operatorname{Higgs}_G,\qquad \operatorname{Higgs}_G(\mathbb C)=\{(P,\varphi)\mid\varphi\in H^0(X,\mathfrak g_P^*\otimes\Omega_X)\}.$$
全局幂零锥定义为
$$\mathrm{Nilp}_{\mathrm{glob}}:=\{(P,\varphi)\in T^*\operatorname{Bun}_G\mid\varphi_x\in\mathcal N_{\mathfrak g^*}\text{ 对每个 }x\in X\text{ 都成立}\}.$$
它是通常的幂零锥 $\mathcal N_{\mathfrak g^*}\subset\mathfrak g^*$ 的全局对应物。

*记号*：$\mathfrak g_P=P\times^G\mathfrak g$ 为伴随丛；$\mathfrak g_P^*$ 为其对偶；$\Omega_X$ 为 $X$ 的典范丛；$\varphi$ 称为 Higgs 场，取值于 $H^0(X,\mathfrak g_P^*\otimes\Omega_X)$；$\mathcal N_{\mathfrak g^*}\subset\mathfrak g^*$ 为幂零锥。

## 要点

- $\operatorname{Bun}_G$ 的经典余切叠与 Higgs 叠同构：$T^*\operatorname{Bun}_G\simeq\operatorname{Higgs}_G$。
- Higgs 叠的复点形如 $(P,\varphi)$，其中 $\varphi\in H^0(X,\mathfrak g_P^*\otimes\Omega_X)$。
- $\mathrm{Nilp}_{\mathrm{glob}}$ 的条件是逐点的：$\varphi_x\in\mathcal N_{\mathfrak g^*}$ 对每个 $x\in X$ 都成立。
- 它是通常幂零锥 $\mathcal N_{\mathfrak g^*}\subset\mathfrak g^*$ 的全局对应物。

## 关键公式

- $$T^*\operatorname{Bun}_G\simeq\operatorname{Higgs}_G,\qquad \operatorname{Higgs}_G(\mathbb C)=\{(P,\varphi)\mid\varphi\in H^0(X,\mathfrak g_P^*\otimes\Omega_X)\}$$
- $$\mathrm{Nilp}_{\mathrm{glob}}:=\{(P,\varphi)\in T^*\operatorname{Bun}_G\mid\varphi_x\in\mathcal N_{\mathfrak g^*}\text{ 对每个 }x\in X\text{ 都成立}\}$$

## 易错点

- 抄写时须保留对偶星号：讲义写作 $\mathfrak g_P^*\otimes\Omega_X$（$\mathfrak g_P^*$ 为对偶丛，$\Omega_X$ 为典范丛），别写成 $\mathfrak g_P\otimes\Omega_X$。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§11.5 全局幂零锥，p.59（PDF p.59），`源码/chapters/ch11.tex:91-99（Higgs 叠与全局幂零锥，§11.5）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv：https://arxiv.org/abs/1606.08523 — L925-926：『T^*_E Bun_G(X)≃H^0(X,g_E^*⊗ω_X)』（同文 L78 把 QCoh(T^*Bun_G(X)) 称作『quasi coherent Higgs sheaves』）——正是卡里 T^*Bun_G≃Higgs_G 与 Higgs_G(C)={(P,φ)|φ∈H^0(X,g_P^*⊗Ω_X)}。
- arXiv：https://arxiv.org/abs/1606.08523 — L933-934：『The global nilpotent cone, introduced by Laumon, is the zero-fiber 𝒩_{X,G}=Hitch^{-1}(0)⊂T^*Bun_G(X) parameterizing G-bundles and nilpotent Higgs fields. It is a conic Lagrangian substack』——支持卡里 Nilp_glob 的逐点幂零定义与『通常幂零锥 N_{g^*} 的全局对应物』。
- nLab：https://ncatlab.org/nlab/show/Hitchin+fibration — 『a canonical map from the cotangent bundle of the moduli space to the so-called Hitchin base, and the map is called the Hitchin fibration』——支持『余切丛→Hitchin 基』的整体框架。

## 关联

- `glc/concept/hitchin-fibration`
- `glc/concept/betti-nilpotent-conjecture`
- `glc/concept/shv-nilpotent-support`
