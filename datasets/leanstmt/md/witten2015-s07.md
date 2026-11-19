# 对偶格与原格同秩

- 卡号：`leanstmt/witten2015-s07`　轨道：W15　scope：`algebraic-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）3.2，印刷页 20–22
- 锚点：§3.2

## 原文陈述

> 对偶格与原格有相同的秩：GNO 对偶环面与原环面维数相同。

英文：The dual lattice has the same rank; the GNO dual torus has the same dimension.

## Lean 陈述

```lean
theorem dual_finrank (K V : Type*) [Field K] [AddCommGroup V] [Module K V]
    [Module.Finite K V] : Module.finrank K (Module.Dual K V) = Module.finrank K V
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.dual_finrank`；imports：`Mathlib.LinearAlgebra.Dual.Lemmas`、`Mathlib.LinearAlgebra.Dimension.Finrank`

## 依赖

- `Subspace.dual_finrank_eq`（mathlib，`Mathlib.LinearAlgebra.Dual.Lemmas`）

## 假设

- K 是域
- V 有限维

## 盲验回译

> 对任意域 K 与有限维 K-向量空间 V，对偶空间的维数等于 V 的维数。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

把「对偶环面维数相同」落到对偶空间 finrank 相等；T-对偶保持底空间维数在物理上正是这一点。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

