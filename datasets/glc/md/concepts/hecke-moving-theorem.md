---
id: glc/concept/hecke-moving-theorem
type: concept
track: H
---

# Hecke 移动定理

> 若奇异支撑不落在 $\mathrm{Nilp}_{\mathrm{irreg}}$ 内，则存在有效除子 $D$，使 Hecke 平移后 $\mathrm{Nilp}_{\mathrm{Kos}}$ 成为奇异支撑的不可约分支。

**问题**：Hecke 移动定理的假设与结论各用哪个锥／分支表述，它如何把非消失性移到 Kostant 分支上？

## 定义

剩余的几何输入是 [FR25] 中的 Hecke 移动定理。其中 $D=\sum_i\check\lambda_i x_i$ 是 $X$ 上取值于 $\check\Lambda^+$ 的有效除子，$V^D\in\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 是它对应的对象（点互异处为各点 $V^{\check\lambda_i}$ 的张量积，Ran 空间上为因子化延拓），$\star$ 为 Hecke 作用。该定理通过仿射 Springer 纤维的局部计算，以及一个全局铺展论证证明；非正式地说，Hecke 修改可以将任意一般位置正则的幂零奇异方向移动到 Kostant 分支。

*记号*：$\operatorname{SS}$ 为奇异支撑；$\mathrm{Nilp}_{\mathrm{irreg}}$ 为一般位置正则轨迹的闭补集；$\mathrm{Nilp}_{\mathrm{Kos}}$ 为 Kostant 分支；$\check\Lambda^+$ 为优势权半群。

## 要点

- 假设是 $\operatorname{SS}(\mathcal F)\not\subset\mathrm{Nilp}_{\mathrm{irreg}}$，即奇异支撑有一部分落在一般位置正则幂零轨迹内。
- 结论是存在 $D$，使 $\mathrm{Nilp}_{\mathrm{Kos}}$ 作为 $\operatorname{SS}(V^D\star\mathcal F)$ 的分支出现。
- 证明通过仿射 Springer 纤维的局部计算，以及一个全局铺展论证。
- 非正式地说，Hecke 修改可以将任意一般位置正则的幂零奇异方向移动到 Kostant 分支。

## 关键公式

- $\operatorname{SS}(\mathcal F)\not\subset\mathrm{Nilp}_{\mathrm{irreg}}\ \Longrightarrow\ \exists D$，使 $\mathrm{Nilp}_{\mathrm{Kos}}$ 作为 $\operatorname{SS}(V^D\star\mathcal F)$ 的分支出现

## 定理与证明

### Hecke 移动定理（要点（有缺口））

若 $\operatorname{SS}(\mathcal F)\not\subset\mathrm{Nilp}_{\mathrm{irreg}}$，则存在 $D$，使 $\mathrm{Nilp}_{\mathrm{Kos}}$ 作为 $\operatorname{SS}(V^D\star\mathcal F)$ 的分支出现。

1. 对仿射 Springer 纤维做局部计算。  
   *为什么*：把一般位置正则的幂零奇异方向在局部移到 Kostant 方向。
2. 用全局铺展（spread-out）论证把局部结论搬到 $X$ 上。  
   *为什么*：局部构造需在 $X$ 上整体化，这一步由铺展论证完成。

> 缺口：讲义只述不证：§13.6 只说「该定理通过仿射 Springer 纤维的局部计算，以及一个全局铺展论证证明」，完整证明见 [FR25]。

*出处*：§13.6 定理（讲义未编号）/ 原书 p.67


## 易错点

- 结论是「存在 $D$」而不是「对某个给定的 $D$」；$D$ 依赖 $\mathcal F$ 的奇异支撑方向。
- 当 $\operatorname{SS}(\mathcal F)\subset\mathrm{Nilp}_{\mathrm{irreg}}$ 时定理不适用——这正是保守性证明中反证的那一步。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§13.6 其他 Whittaker 系数与 Hecke 平移，p.67（PDF p.67），`源码/chapters/ch13.tex:128-132（Hecke 移动定理）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FR25：https://arxiv.org/abs/2207.02955 — 「Suppose F∈Shv_Nilp(Bun_G) … SS(F)⊄Nilp_irreg. Then there exists D … such that Nilp_Kos⊆SS(V^D⋆F)」——卡定理逐字对应（存在量词，非对给定 D）
- FR25：https://arxiv.org/abs/2207.02955 — 要么 F 反温和，要么存在这样的 D——支持卡 pitfall「存在 D，不对给定 D」
- FR25：https://arxiv.org/abs/2207.02955 — 证明从「a purely local result concerning Hecke modifications and affine Springer fibers」开始（affine Springer fiber Spr_ξ、discrepancy）——支持卡 proof 的「仿射 Springer 纤维局部计算 + 全局铺展」

## 关联

- `glc/concept/microlocal-index-theorem`
- `glc/concept/geometric-casselman-shalika`
- `glc/concept/global-nilpotent-cone`
- `glc/concept/whittaker-conservativity`
