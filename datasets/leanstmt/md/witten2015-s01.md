# 't Hooft 磁通所在的群 ℤ_N 有 N 个元素

- 卡号：`leanstmt/witten2015-s01`　轨道：W　scope：`discrete-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）2.6.6，印刷页 14–16
- 锚点：§2.6.6 关于 PSU(N) 与 't Hooft flux 的段落

## 原文陈述

> PSU(N) 规范的 't Hooft 磁通 ξ 取值于 H²(C, ℤ_N)，因此磁通的可能取值构成一个恰有 N 个元素的有限群。

英文：The 't Hooft magnetic flux for PSU(N) gauge theory takes values in H²(C, ℤ_N).

## Lean 陈述

```lean
theorem card_zmod (N : ℕ) [NeZero N] : Fintype.card (ZMod N) = N
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.card_zmod`；imports：`Mathlib.Data.ZMod.Basic`

## 依赖

- `ZMod.card`（mathlib，`Mathlib.Data.ZMod.Basic`）

## 假设

- N ≥ 1（`NeZero N`）

## 盲验回译

> 对任意正整数 N，群 ℤ/N 的元素个数等于 N。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

把「磁通取值于 ℤ_N」这一步落到「ℤ_N 是有限群、阶为 N」；H²(C,ℤ_N) 本身的群结构未在 mathlib 中形式化（缺口见 README §4）。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

