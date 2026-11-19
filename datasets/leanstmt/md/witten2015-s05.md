# ℂ 中 N 次单位根恰有 N 个

- 卡号：`leanstmt/witten2015-s05`　轨道：W　scope：`discrete-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）4.1，印刷页 18–20
- 锚点：§4.1（本征膜与 't Hooft 算符的本征值）

## 原文陈述

> 复数域中 N 次单位根恰有 N 个（N ≥ 1），故 't Hooft 算符的本征值只能从这 N 个数中取。

英文：There are exactly N N-th roots of unity in ℂ.

## Lean 陈述

```lean
theorem card_rootsOfUnity_complex (n : ℕ) [NeZero n] : Nat.card (rootsOfUnity n ℂ) = n
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.card_rootsOfUnity_complex`；imports：`Mathlib.RingTheory.RootsOfUnity.Complex`

## 依赖

- `card_rootsOfUnity_eq_iff_exists_isPrimitiveRoot`（mathlib，`Mathlib.RingTheory.RootsOfUnity.PrimitiveRoots`）
- `Complex.isPrimitiveRoot_exp_of_coprime`（mathlib，`Mathlib.RingTheory.RootsOfUnity.Complex`）

## 假设

- n ≥ 1（`NeZero n`）

## 盲验回译

> 对任意正整数 n，复数域中 n 次单位根构成的集合恰有 n 个元素。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

证明通过给出本原根 exp(2πi/n) 完成；这是 π、exp 与单位根三条 API 的接口，也是本批唯一用到复分析的陈述。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

