# ℤ_N 中每个元素都是 N-挠的

- 卡号：`leanstmt/witten2015-s03`　轨道：W15　scope：`discrete-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）2.6.6，印刷页 14–16
- 锚点：§2.6.6

## 原文陈述

> 磁通的任何取值 ξ 都满足 N·ξ = 0：'t Hooft 磁通是 N 挠的。

英文：Every element of ℤ_N is N-torsion: N·x = 0.

## Lean 陈述

```lean
theorem nsmul_zmod (N : ℕ) (x : ZMod N) : N • x = 0
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.nsmul_zmod`；imports：`Mathlib.Data.ZMod.Basic`

## 依赖

- `ZMod.natCast_self`（mathlib，`Mathlib.Data.ZMod.Basic`）
- `nsmul_eq_mul`（mathlib，`Mathlib.Algebra.Group.Defs`）

## 假设

- 无

## 盲验回译

> 对任意自然数 N 与 ℤ/N 中任意元素 x，N 倍 x 等于 0。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

PSU(N) 丛的障碍类落在 N-挠子群，这一条是其离散内核。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

