# 缺口：tame ramification 的单值 exp(−2π(α−iγ))

- 卡号：`leanstmt/witten2008-g07`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）4，印刷页 7–7
- 锚点：§4 式 (4.3) 与 Remark 4.1

## 原文陈述

> 正则奇点（tame ramification）的留数 (α,γ) 决定绕 punctures 的单值 U = exp(−2π(α−iγ))；镜像侧参数按 (α,η) = (^Lη, −^Lα) 对应（Gukov–Witten）。

英文：Around a regular singularity the monodromy is U = exp(−2π(α−iγ)); the mirror parameter map is (α,η) = (^Lη, −^Lα).

## Lean 陈述

```lean
theorem tame_monodromy (α γ : ℝ) :
    monodromyExp α γ = Complex.exp (-(2 * Real.pi) * (α - γ * Complex.I))
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.tame_monodromy`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- α, γ 为实数；`monodromyExp` 为占位定义

## 盲验回译

> （缺口占位）留数 (α,γ) 给出的单值等于 exp(−2π(α − iγ))。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：缺 𝔤 值留数、ad-作用下的矩阵指数与单值理论（mathlib 只有 `NormedSpace.exp` 的标量/赋范情形），缺 Gukov–Witten 的参数对偶。

- 缺口：缺 𝔤 值留数、ad-作用下的矩阵指数与单值理论（mathlib 只有 `NormedSpace.exp` 的标量/赋范情形），缺 Gukov–Witten 的参数对偶。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

