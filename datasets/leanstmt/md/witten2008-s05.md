# 规范变换群的 currying

- 卡号：`leanstmt/witten2008-s05`　轨道：W08　scope：`discrete-core`　验证：**certified**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）6.1，印刷页 12–13
- 锚点：§6.1（Atiyah–Bott 1982 的无限维对 (Y, W_C)，W = Maps(C,G)）

## 原文陈述

> M = Σ×C 上的规范变换群是 Maps(Σ, Maps(C,G))，按定义即 Maps(Σ×C, G)；类型层面这只是 currying。原文用这一步把四维规范理论看成以 Σ 为底、取值于 Bun_G(C) 的二维 sigma 模型。

英文：Gauge transformations on M = Σ×C are Maps(Σ, Maps(C,G)) = Maps(Σ×C, G): a currying of function spaces.

## Lean 陈述

```lean
theorem gauge_maps_curry (Sig C G : Type*) :
    Nonempty (((Sig → C → G) ≃ (Sig × C → G)))
```

文件 `lean/ShuyiFormal/Witten2008/Statements.lean`，声明名 `Witten2008.gauge_maps_curry`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.Dimension.Constructions`、`Mathlib.LinearAlgebra.SpecialLinearGroup`、`Mathlib.Logic.Equiv.Prod`

## 依赖

- `Equiv.curry`（mathlib，`Mathlib.Logic.Equiv.Prod`）

## 假设

- 无

## 盲验回译

> 对任意类型 Σ、C、G，两变量的函数空间 Σ → (C → G) 与乘积定义域上的函数空间 (Σ×C) → G 之间存在等价。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

只形式化类型等价（`Equiv.curry`），群结构由逐点乘法给出、此处不重复构造。原文 §6 的四维/二维物理陈述见 G09。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

