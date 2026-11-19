# SU(N) 的中心是 ℤ_N（对偶群 PSU(N) 的核）

- 卡号：`leanstmt/witten2008-s01`　轨道：W08　scope：`algebraic-core`　验证：**certified**
- 来源：Witten, Mirror Symmetry, Hitchin's Equations, and Langlands Duality（arXiv:0802.0999v1）2，印刷页 2–2
- 锚点：§2 开头（the dual of SU(N) is PSU(N) = SU(N)/Z_N）

## 原文陈述

> Langlands 对偶群的基本例子：SU(N) 的对偶群是 PSU(N) = SU(N)/ℤ_N，被商掉的是中心 ℤ(SU(N)) ≅ ℤ_N。中心元恰是标量矩阵 ζ·1（ζ 为 N 次单位根）；因 mathlib 无紧李群，这里用复化群 SL(N,ℂ) 陈述。

英文：The dual of SU(N) is PSU(N) = SU(N)/Z_N; the center of SU(N) consists of scalar matrices ζ·1 with ζ^N = 1.

## Lean 陈述

```lean
theorem center_sl (n : ℕ) (g : SpecialLinearGroup ℂ (Fin n → ℂ)) :
    g ∈ Subgroup.center (SpecialLinearGroup ℂ (Fin n → ℂ)) ↔
      ∃ r : ℂ, r ^ n = 1 ∧
        (g : (Fin n → ℂ) →ₗ[ℂ] (Fin n → ℂ)) = r • LinearMap.id
```

文件 `lean/ShuyiFormal/Witten2008/Statements.lean`，声明名 `Witten2008.center_sl`；imports：`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality`、`Mathlib.LinearAlgebra.Dimension.Constructions`、`Mathlib.LinearAlgebra.SpecialLinearGroup`、`Mathlib.Logic.Equiv.Prod`

## 依赖

- `SpecialLinearGroup.mem_center_iff`（mathlib，`Mathlib.LinearAlgebra.SpecialLinearGroup`）
- `Module.finrank_fintype_fun_eq_card`（mathlib，`Mathlib.LinearAlgebra.Dimension.Constructions`）

## 假设

- n 为自然数（n = 0 时 SL(0,ℂ) 平凡，陈述仍成立）

## 盲验回译

> 对任意自然数 n 与行列式为 1 的复矩阵 g，g 属于 SL(n,ℂ) 的中心当且仅当 g 是标量乘法、且该标量的 n 次幂为 1。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

原文只把 SU(N) 与 PSU(N) 作为对偶群的例子点名；此卡把「商掉的离散中心是 μ_N」这一内容固定下来。同文件另有恒等特例 `residue_invariant`（m = 0 的伸缩律）。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

