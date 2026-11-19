# 典范丛次数为偶数，自旋结构存在

- 卡号：`leanstmt/witten2015-s08`　轨道：W15　scope：`arithmetic-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）2.6.5，印刷页 16–18
- 锚点：§2.6.5（酉群的谱覆盖与 K^{1/2} 的选择）

## 原文陈述

> 亏格 g 曲面上典范丛的次数 2g−2 是偶数，因此 K^{1/2}（自旋结构）总存在。

英文：deg K = 2g−2 is even, hence a spin structure exists.

## Lean 陈述

```lean
theorem even_deg_canonical (g : ℤ) : Even (2 * g - 2)
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.even_deg_canonical`；imports：`Mathlib.Data.ZMod.Basic`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- g 为整数（亏格）

## 盲验回译

> 对任意整数 g，整数 2g−2 是偶数。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

本卡只形式化「偶性」这一步；「K 的次数 = 2g−2」与「偶次数线丛有平方根」两条留在缺口清单（G01/G03）。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

