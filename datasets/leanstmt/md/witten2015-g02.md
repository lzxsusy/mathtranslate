# 缺口：Hitchin 纤维维数 (g−1)·dim G

- 卡号：`leanstmt/witten2015-g02`　轨道：W　scope：`gap`　验证：**gap**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）2.4，印刷页 8–10
- 锚点：§2.4–§2.6

## 原文陈述

> Hitchin 纤维化的一般纤维是 ½ dim M_H = (g−1)·dim G 维紧复环面（原文 §2.4、§2.6）。

英文：A generic Hitchin fiber is a compact complex torus of dimension (g−1)·dim G.

## Lean 陈述

```lean
theorem hitchin_fiber_dimension (g dimG : ℕ) (hg : 2 ≤ g) :
    hitchinFiberDim g dimG = (g - 1) * dimG
```

文件 `lean/ShuyiFormal/Witten2015/Gaps.lean`，声明名 `Witten2015.Gaps.hitchin_fiber_dimension`；imports：`Mathlib.Data.ZMod.Basic`

## 依赖

- Mathlib 无 Hitchin 模空间：本卡用占位 `hitchinFiberDim` 承载命题

## 假设

- g ≥ 2
- `hitchinFiberDim` 为待实现占位（def 值 0），因此本卡 status=gap

## 盲验回译

> （缺口占位）一般 Hitchin 纤维是复维数 (g−1)·dim G 的紧复环面。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：mathlib 无 Hitchin 模空间、`Bun_G`、稳定性判据、余切丛的辛结构。需要黎曼面上主丛的模空间（栈）与 Hitchin 系统的基础设施。

- 缺口：mathlib 无 Hitchin 模空间、`Bun_G`、稳定性判据、余切丛的辛结构。需要黎曼面上主丛的模空间（栈）与 Hitchin 系统的基础设施。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

