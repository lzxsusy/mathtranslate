# Prym 的维数 = (N²−1)(g−1)

- 卡号：`leanstmt/witten2015-s09`　轨道：W　scope：`arithmetic-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）2.6.2，印刷页 11–13
- 锚点：§2.6.2（阿贝尔化与 Prym）

## 原文陈述

> 谱曲线亏格 g_D = N²(g−1)+1 时，阿贝尔化的余核（Prym）维数 g_D − g = (N²−1)(g−1)。

英文：If the spectral curve has genus N²(g−1)+1, the Prym has dimension (N²−1)(g−1).

## Lean 陈述

```lean
theorem prym_dim (N g : ℤ) : (N ^ 2 * (g - 1) + 1) - g = (N ^ 2 - 1) * (g - 1)
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.prym_dim`；imports：`Mathlib.Data.ZMod.Basic`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- N, g 为整数

## 盲验回译

> 对任意整数 N、g，若谱曲线亏格为 N²(g−1)+1，则它与底曲线的亏格差等于 (N²−1)(g−1)。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

几何前提 g_D = N²(g−1)+1 本身没有形式化（缺口 G01），本卡只固化其维数推论，避免把前提当已证。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

