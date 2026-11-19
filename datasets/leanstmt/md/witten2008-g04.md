# 缺口：Hitchin 解 ↔ 复平坦联络 ↔ 半稳定希格斯丛

- 卡号：`leanstmt/witten2008-g04`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）2，印刷页 3–3
- 锚点：§2（A+iφ 平坦 ↔ 希格斯丛；M_H 的超凯勒结构 Ω_I = ω_J + iω_K）

## 原文陈述

> Hitchin 方程的解有两种解释：A + iφ 是复平坦联络（给出 Y 的点）；(E,φ) 是半稳定希格斯丛，φ ∈ H⁰(C, K⊗ad E)（给出 M_H 在复结构 I 下的点）；M_H 超凯勒，Ω_I = ω_J + iω_K。

英文：Solutions of Hitchin's equations correspond both to flat G_ℂ-connections and to semistable Higgs bundles (E,φ).

## Lean 陈述

```lean
theorem flat_iff_higgs (G C : Type*) :
    Nonempty (flatConnModuli G C ≃ higgsBundleModuli G C)
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.flat_iff_higgs`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- `flatConnModuli`/`higgsBundleModuli` 为占位定义

## 盲验回译

> （缺口占位）平坦丛模空间与希格斯丛模空间之间存在等价。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：同 G03；另缺希格斯丛、稳定性（GIT）与超凯勒商 Ω_I = ω_J + iω_K。

- 缺口：同 G03；另缺希格斯丛、稳定性（GIT）与超凯勒商 Ω_I = ω_J + iω_K。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

