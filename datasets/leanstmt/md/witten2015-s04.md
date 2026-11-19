# N 次单位根的刻画

- 卡号：`leanstmt/witten2015-s04`　轨道：W15　scope：`discrete-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）7.1，印刷页 66–67
- 锚点：§7.1（'t Hooft 算符本征值的讨论）

## 原文陈述

> 复数 z 是 N 次单位根，当且仅当 z^N = 1；'t Hooft 算符的本征值必满足此方程。

英文：z is an N-th root of unity iff z^N = 1.

## Lean 陈述

```lean
theorem mem_rootsOfUnity_iff (n : ℕ) (z : ℂˣ) : z ∈ rootsOfUnity n ℂ ↔ (z : ℂ) ^ n = 1
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.mem_rootsOfUnity_iff`；imports：`Mathlib.RingTheory.RootsOfUnity.Complex`

## 依赖

- `mem_rootsOfUnity'`（mathlib，`Mathlib.RingTheory.RootsOfUnity.Basic`）

## 假设

- 无（用单位群 ℂˣ 表达非零性，避免零元的平凡解）

## 盲验回译

> 对任意自然数 n 与任意非零复数 z，z 属于 n 次单位根群当且仅当 z 的 n 次方等于 1。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

用 ℂˣ 而非 ℂ 是为了排除 z = 0（0^n = 0 ≠ 1 时该方程无解，用单位群更贴近「本征值」的非零语境）。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

