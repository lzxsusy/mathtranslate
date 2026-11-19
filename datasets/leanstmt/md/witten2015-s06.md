# 电荷格的双对偶回到自身

- 卡号：`leanstmt/witten2015-s06`　轨道：W　scope：`algebraic-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）3.2，印刷页 20–24
- 锚点：§3.2–§3.3（对偶环面与 GNO 对偶）

## 原文陈述

> 有限自由模与其双对偶同构：Langlands/GNO 对偶环面取两次对偶回到原来的环面。

英文：A finite free module is isomorphic to its double dual; the dual torus' dual torus is the original torus.

## Lean 陈述

```lean
theorem double_dual (K V : Type*) [Field K] [AddCommGroup V] [Module K V]
    [Module.Finite K V] [Module.Free K V] : Nonempty (V ≃ₗ[K] Module.Dual K (Module.Dual K V))
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.double_dual`；imports：`Mathlib.LinearAlgebra.Dual.Lemmas`

## 依赖

- `Module.evalEquiv`（mathlib，`Mathlib.LinearAlgebra.Dual.Defs`）
- `Module.instIsReflexiveOfFiniteOfProjective`（mathlib，`Mathlib.LinearAlgebra.Dual.Defs`）

## 假设

- K 是域（特征任意）
- V 有限生成自由模

## 盲验回译

> 对任意域 K 与任意有限维 K-向量空间 V，存在 V 到其双对偶空间的线性同构。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

环面 T = Λ⊗ℝ/Λ 的对偶是 Hom(Λ,ℤ)⊗U(1)；在格（自由 ℤ-模）层面「双对偶 ≅ 自身」正是这条代数陈述。环面层面未形式化。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

