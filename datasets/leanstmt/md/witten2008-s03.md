# T-对偶的离散同构：ℤ_N ≅ Hom(ℤ_N, U(1))

- 卡号：`leanstmt/witten2008-s03`　轨道：W08　scope：`discrete-core`　验证：**certified**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）3，印刷页 3–4
- 锚点：§3（special Lagrangian 纤维上的 T-对偶）

## 原文陈述

> 有限阿贝尔群是 Pontryagin 自对偶的：ℤ_N ≅ Hom(ℤ_N, U(1))，且同构是典范的（不依赖生成元选择）。这是 SYZ 图像下纤维 T-对偶在有限群情形的对照。

英文：Finite abelian groups are Pontryagin self-dual: Z_N ≅ Hom(Z_N, U(1)) canonically.

## Lean 陈述

```lean
theorem dual_zmod_equiv (n : ℕ) [NeZero n] :
    Nonempty (ZMod n ≃+ AddChar (ZMod n) ℂ)
```

文件 `lean/ShuyiFormal/Witten2008/Statements.lean`，声明名 `Witten2008.dual_zmod_equiv`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.Dimension.Constructions`、`Mathlib.LinearAlgebra.SpecialLinearGroup`、`Mathlib.Logic.Equiv.Prod`

## 依赖

- `AddChar.zmodAddEquiv`（mathlib，`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`）

## 假设

- n ≥ 1（`NeZero n`）

## 盲验回译

> 对任意正整数 n，ℤ/n 与其加法字符群之间存在加法群同构。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

与 S02 同一节；S02 给基数、本卡给同构本身。对偶环面的连续版本（T ≅ Hom(X_*,U(1))）不在本卡范围。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

