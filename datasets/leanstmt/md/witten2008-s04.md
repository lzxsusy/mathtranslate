# 非正则奇点系数在 z = λw 下的伸缩律

- 卡号：`leanstmt/witten2008-s04`　轨道：W08　scope：`algebraic-core`　验证：**certified**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）5，印刷页 8–9
- 锚点：§5 式 (5.1) 及其后关于 T_1 与奇点阶数 n 为规范不变量的讨论

## 原文陈述

> 非正则奇点写成 A = dz·(T_n/z^n + … + T_1/z + …)。在重标度 z = λw（λ≠0）下，第 (m+1) 重极点的系数变为 T_{m+1}/λ^m：留数 T_1 不变，m ≥ 1 的项随 λ 伸缩。

英文：Under z = λw (λ≠0), the coefficient of z^{-(m+1)} scales as λ^{-m}; the residue T_1 is invariant.

## Lean 陈述

```lean
theorem coefficient_scaling (lam c : ℂ) (hlam : lam ≠ 0) (m : ℕ) :
    lam * (c / lam ^ (m + 1)) = c / lam ^ m
```

文件 `lean/ShuyiFormal/Witten2008/Statements.lean`，声明名 `Witten2008.coefficient_scaling`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.Dimension.Constructions`、`Mathlib.LinearAlgebra.SpecialLinearGroup`、`Mathlib.Logic.Equiv.Prod`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- λ ≠ 0

## 盲验回译

> 对任意非零复数 λ、复数 c 与自然数 m，λ 乘以 c 除以 λ 的 m+1 次幂，等于 c 除以 λ 的 m 次幂。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

把「重标度下第 (m+1) 个系数变成 λ^{1-(m+1)}T_{m+1}」这个算术内容固定下来；留数不变（m=0）是同文件 `residue_invariant`。真正的模空间不变量陈述见 G08。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

