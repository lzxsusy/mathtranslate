# 缺口：wild ramification 与辫群 B(G) ≅ B(^LG)

- 卡号：`leanstmt/witten2008-g08`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）5，印刷页 8–10
- 锚点：§5（Stokes 矩阵、等单值变形、辫群 B(G) ≅ B(^LG)）

## 原文陈述

> 非正则奇点的扩展单值 = 普通单值 ⊕ Stokes 矩阵；Y(G,C;T_1,…,T_n) 复辛且与 T_2,…,T_n 无关；辫群 B(G) = π₁(𝔱^reg) 与 B(^LG) 自然同构，镜像对称与辫群作用交换。

英文：Extended monodromy = monodromy + Stokes matrices; the braid groups B(G) and B(^LG) are naturally isomorphic.

## Lean 陈述

```lean
theorem braid_dual (G : Type*) :
    Nonempty (braidGroup G ≃ braidGroup (langlandsDual G))
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.braid_dual`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- `braidGroup`/`langlandsDual` 为占位定义

## 盲验回译

> （缺口占位）G 与对偶群的辫群之间存在等价。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：缺 Stokes 现象、等单值变形（Jimbo–Miwa–Ueno 1981）、辫群 π₁(𝔱^reg) 与其对偶同构。

- 缺口：缺 Stokes 现象、等单值变形（Jimbo–Miwa–Ueno 1981）、辫群 π₁(𝔱^reg) 与其对偶同构。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

