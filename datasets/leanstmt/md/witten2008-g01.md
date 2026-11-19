# 缺口：Y(G,C) 复辛、维数 2(g−1)dim G、典范丛平凡

- 卡号：`leanstmt/witten2008-g01`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）1，印刷页 1–1
- 锚点：§1 开头（Y(G,C) 的定义与复辛结构）

## 原文陈述

> Y(G,C) 是平坦 G_ℂ-丛的模空间（= Hom(π₁(C),G_ℂ)/G_ℂ），复辛、典范丛平凡，复维数 2(g−1)dim G。

英文：Y(G,C) = Hom(π₁(C),G_ℂ)/G_ℂ is complex symplectic with trivial canonical bundle, of complex dimension 2(g−1)dim G.

## Lean 陈述

```lean
theorem moduli_dim (g d : ℤ) (hg : 2 ≤ g) :
    moduliDim g d = 2 * (g - 1) * d
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.moduli_dim`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- g ≥ 2；`moduliDim` 为占位定义（值为 0）

## 盲验回译

> （缺口占位）亏格 g 曲面上平坦丛模空间的复维数是 2(g−1)dim G。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：mathlib 无 Hom(π₁(C),G_ℂ)/G_ℂ 模空间、无曲面基本群与表示簇；`moduliDim` 为占位 def。

- 缺口：mathlib 无 Hom(π₁(C),G_ℂ)/G_ℂ 模空间、无曲面基本群与表示簇；`moduliDim` 为占位 def。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

