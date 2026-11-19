# ℤ_N 由 1 生成，加法阶为 N

- 卡号：`leanstmt/witten2015-s02`　轨道：W　scope：`discrete-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）2.6.6，印刷页 14–16
- 锚点：§2.6.6

## 原文陈述

> ℤ_N 是 N 阶循环群：元素 1 的加法阶恰为 N，即 N 次重复的 't Hooft 磁通为零。

英文：ℤ_N is cyclic of order N; the additive order of 1 is N.

## Lean 陈述

```lean
theorem orderOf_one_zmod (N : ℕ) : addOrderOf (1 : ZMod N) = N
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.orderOf_one_zmod`；imports：`Mathlib.Data.ZMod.Basic`

## 依赖

- `ZMod.addOrderOf_one`（mathlib，`Mathlib.Data.ZMod.Basic`）

## 假设

- 无（N = 0 时两边都是 0）

## 盲验回译

> 对任意自然数 N，元素 1 在 ℤ/N 中的加法阶等于 N。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

ℤ_N 的循环性给出磁通的「N 次为零」量化；与 S03 的 n-挠陈述互为表里。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

