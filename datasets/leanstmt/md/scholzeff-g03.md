# 缺口：几何 Satake 的 Tannaka 形式

- 卡号：`leanstmt/scholzeff-g03`　轨道：FF21　scope：`gap`　验证：**gap**
- 来源：Scholze, Geometrization of the Local Langlands Correspondence（Berkeley 课程讲稿，Tony Feng 记录）（Lecture notes, UC Berkeley, 2021-10-30 至 2022-01/02）§21，印刷页 117–117
- 锚点：Theorem 21.17，原文 p.117

## 原文陈述

> 对约化群 G 与其对偶群 Ĝ，(Sat_G(Λ), ⋆) 自然升级为对称幺半范畴，且 ⨁_i H^i(Gr_{G,Spa η}, −): Sat_G(Λ) → Rep_{W_E}(Λ) 是纤维函子，其 Tannaka 群为 Ĝ。

英文：Theorem 21.17: (Sat_G(Λ), ⋆) upgrades to a symmetric monoidal category such that ⊕_i H^i(Gr_{G,Spa η}, −) is a fiber functor with Tannaka group Ĝ.

## Lean 陈述

```lean
theorem geometric_satake_tannaka (G : Type u) (hG : reductiveGroup G) (Λ : Type v) :
    ∃ F : SatakeCategory G Λ → RepresentationCategory (DualGroup G) Λ,
      Nonempty (TannakaGroup G ≃ DualGroup G)
```

文件 `lean/ShuyiFormal/ScholzeFF/Gaps.lean`，声明名 `ScholzeFF.Gaps.geometric_satake_tannaka`；imports：`Mathlib.AlgebraicGeometry.Scheme`、`Mathlib.CategoryTheory.Monoidal.Braided.Basic`、`Mathlib.RingTheory.PicardGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- G 是约化群（占位谓词）
- Λ 是环，底层取 ℤ_ℓ 之类的系数

## 盲验回译

> 对任意类型 G、Λ，在占位假设 reductiveGroup G 下，存在一个函数 F : SatakeCategory G Λ → RepresentationCategory (DualGroup G) Λ，且存在等价 TannakaGroup G ≃ DualGroup G；涉及的四个类型均为占位，F 未被要求具有函子性或相容性。

方法：blind-backtranslation；验卡人：subagent r01（盲回译：只读 Lean 语句与占位定义，未读中文陈述与原文）。

## 备注与缺口

缺口：几何 Satake 的陈述依赖一整层 $\infty$-范畴机器；此卡把对称幺半结构、纤维函子与 Tannaka 群压缩成一个占位三元组。原文印刷页 117（第 21 讲末页）。

- 缺口：需要菱形的 étale 上同调、完备化 Grassmann 簇、ULA 层的六函子形式化与幺半 $\infty$-范畴的 Tannaka 重建；mathlib 均无（有 Condensed 模块但没有这类应用）。（blocked_by: mathlib 缺 étale 上同调与六函子形式化）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-27，`sorry` 数 1。

