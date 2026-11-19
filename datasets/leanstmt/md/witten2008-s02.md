# 有限对偶环面的影子：Hom(ℤ_N, U(1)) 有 N 个元素

- 卡号：`leanstmt/witten2008-s02`　轨道：W08　scope：`discrete-core`　验证：**certified**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）3，印刷页 2–4
- 锚点：§2（GNO/Langlands 对偶群）与 §3（special Lagrangian 纤维上的 T-对偶）

## 原文陈述

> 对偶环面是原环面的字符群；其有限群影子为 Hom(ℤ_N, U(1)) ≅ ℤ_N，因此「环面与对偶环面同秩」在 ℤ_N 层面表现为字符个数仍为 N。

英文：The dual torus is the character group; at the finite level Hom(ℤ_N, U(1)) ≅ ℤ_N, so the character count is still N.

## Lean 陈述

```lean
theorem card_dual_zmod (n : ℕ) [NeZero n] :
    Fintype.card (AddChar (ZMod n) ℂ) = n
```

文件 `lean/ShuyiFormal/Witten2008/Statements.lean`，声明名 `Witten2008.card_dual_zmod`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.Dimension.Constructions`、`Mathlib.LinearAlgebra.SpecialLinearGroup`、`Mathlib.Logic.Equiv.Prod`

## 依赖

- `AddChar.card_eq`（mathlib，`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`）
- `ZMod.card`（mathlib，`Mathlib.Data.ZMod.Basic`）

## 假设

- n ≥ 1（`NeZero n`；n = 0 时 ZMod 0 ≅ ℤ，其对偶不是有限群）

## 盲验回译

> 对任意正整数 n，从 ℤ/n 到复数乘法群的加法字符恰有 n 个。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

对偶环面 T∨ = Hom(X_*(T), U(1)) 的有限影子。原文 §3 的 T-对偶在 special Lagrangian 纤维上进行，此卡只形式化其群论骨架；环面/复几何部分见 G06。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

