# 缺口：Hitchin 纤维化的底与一般纤维

- 卡号：`leanstmt/witten2008-g05`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）3，印刷页 3–4
- 锚点：§3（Hitchin 纤维化与一般纤维是 special Lagrangian）

## 原文陈述

> Hitchin 纤维化 π: M_H → B 把 (E,φ) 映到 φ 的特征多项式；dim_ℂ B = (g−1)dim G，一般纤维是复阿贝尔簇（或挠子）、对 Ω_I 拉格朗日，故 M_H 是完全可积系统。

英文：The Hitchin fibration π: M_H → B has dim_ℂ B = (g−1)dim G; a generic fiber is a complex abelian variety (or torsor), Lagrangian for Ω_I.

## Lean 陈述

```lean
theorem hitchin_base_dim (g d : ℤ) (hg : 2 ≤ g) :
    hitchinBaseDim g d = (g - 1) * d
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.hitchin_base_dim`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- g ≥ 2；`hitchinBaseDim` 为占位定义

## 盲验回译

> （缺口占位）Hitchin 底的复维数为 (g−1)dim G。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：无模空间、特征多项式映射、阿贝尔簇与 Lagrange 子流形。

- 缺口：无模空间、特征多项式映射、阿贝尔簇与 Lagrange 子流形。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

