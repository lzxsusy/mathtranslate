# 缺口：A-模型与 B-模型的数据

- 卡号：`leanstmt/witten2008-g02`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）1，印刷页 1–2
- 锚点：§1（A-模型与 B-模型的定义）

## 原文陈述

> 同一复辛流形 Y 上：B-模型 = (Y, 复结构, 平凡典范丛)；A-模型 = (Y, ω = Im Ω)。镜像对称把 (^LG 的) B-模型与 (G 的) A-模型配对。

英文：B-model: (Y, complex structure, trivial canonical bundle); A-model: (Y, ω = Im Ω).

## Lean 陈述

```lean
theorem a_b_model (G C : Type*) :
    Nonempty (aModelData (flatConnModuli G C) ≃ bModelData (flatConnModuli G C))
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.a_b_model`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- `aModelData`/`bModelData`/`flatConnModuli` 均为占位定义

## 盲验回译

> （缺口占位）同一个底流形上的 A-模型数据与 B-模型数据之间存在等价。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：mathlib 无超凯勒/复辛流形、无二维拓扑场论（A/B 模型）与镜像对称本身。

- 缺口：mathlib 无超凯勒/复辛流形、无二维拓扑场论（A/B 模型）与镜像对称本身。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

