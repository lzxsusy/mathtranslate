# 缺口：四维提升与 Bun_G 无有限维整体商

- 卡号：`leanstmt/witten2008-g09`　轨道：W08　scope：`gap`　验证：**gap**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）6，印刷页 12–13
- 锚点：§6（四维提升）与 §6.1（Bun_G 无有限维整体商）

## 原文陈述

> M = Σ×C 上四维扭转 N=4 规范理论低能给出二维 sigma 模型 Φ: Σ → M_H(G,C)；规范变换群为 Maps(Σ×C, G)。Bun_G(C) 不能写成有限维整体商 (Y, W_C)，故奇点处必须回到四维。

英文：The 4d twisted theory reduces to a 2d sigma model on M_H; Bun_G(C) admits no finite-dimensional global quotient.

## Lean 陈述

```lean
theorem four_dimensional_lift (Sig C G : Type*) :
    Nonempty (sigmaModelOn Sig C G ≃ fourDimGaugeTheory Sig C G)
```

文件 `lean/ShuyiFormal/Witten2008/Gaps.lean`，声明名 `Witten2008.Gaps.four_dimensional_lift`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.SpecialLinearGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- `sigmaModelOn`/`fourDimGaugeTheory` 为占位定义

## 盲验回译

> （缺口占位）Σ×C 上的四维规范理论与 Σ 上取值的二维 sigma 模型给出同一物理。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：无四维规范理论/二维 sigma 模型的物理层形式化；Atiyah–Bott 1982 的「Bun_G 无整体商」亦缺。

- 缺口：无四维规范理论/二维 sigma 模型的物理层形式化；Atiyah–Bott 1982 的「Bun_G 无整体商」亦缺。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

