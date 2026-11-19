# 缺口（本文主定理）：Hitchin 纤维化上的镜像对称

- 卡号：`leanstmt/witten2008-g06`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）3，印刷页 4–5
- 锚点：§3（主定理：mirror symmetry between Hitchin fibrations）

## 原文陈述

> M_H(^LG, C) 在复结构 J 下的 B-模型，镜像于 M_H(G, C) 配 ω = ω_K 的 A-模型；经 SYZ，对偶纤维化就是对偶群的 Hitchin 纤维化（纤维上作 T-对偶）。

英文：The B-model of M_H(^LG,C) in complex structure J is mirror to the A-model of M_H(G,C) with ω_K.

## Lean 陈述

```lean
theorem mirror_symmetry (G C : Type*) :
    Nonempty (bModelData (higgsBundleModuli (langlandsDual G) C) ≃
      aModelData (higgsBundleModuli G C))
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.mirror_symmetry`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- `bModelData`/`aModelData`/`higgsBundleModuli`/`langlandsDual` 均为占位定义

## 盲验回译

> （缺口占位）对偶群 Higgs 模空间的 B-模型与群 G 的 Higgs 模空间的 A-模型等价。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：同 G05；另缺 SYZ/T-对偶与镜像对称本身。这是全文主定理，恰好是 mathlib 缺口最深的一条。

- 缺口：同 G05；另缺 SYZ/T-对偶与镜像对称本身。这是全文主定理，恰好是 mathlib 缺口最深的一条。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

