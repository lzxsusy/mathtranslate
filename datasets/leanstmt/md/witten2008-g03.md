# 缺口：Hitchin 方程 (2.1)

- 卡号：`leanstmt/witten2008-g03`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）2，印刷页 2–2
- 锚点：§2 式 (2.1)

## 原文陈述

> Hitchin 方程：F − φ∧φ = 0、Dφ = D⋆φ = 0，其中 φ 是 C 上取值于 ad(E) 的 1-形式，⋆ 由 C 的复结构决定。

英文：Hitchin's equations: F − φ∧φ = 0 and Dφ = D⋆φ = 0.

## Lean 陈述

```lean
theorem hitchin_equations (F phi : Type*) :
    isHitchinSolution F phi
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.hitchin_equations`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- `isHitchinSolution` 为占位定义（恒真）

## 盲验回译

> （缺口占位）给定联络曲率与希格斯场，(F, φ) 满足 Hitchin 方程。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：mathlib 无黎曼面联络、Hodge 星、ad(E) 值 1-形式；连「方程」这一层的对象都不存在。

- 缺口：mathlib 无黎曼面联络、Hodge 星、ad(E) 值 1-形式；连「方程」这一层的对象都不存在。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

