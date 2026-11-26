# 缺口：GL_n 超尖表示与 n 维 Weil 表示的双射

- 卡号：`leanstmt/scholzeff-g02`　轨道：FF21　scope：`gap`　验证：**gap**
- 来源：Scholze, Geometrization of the Local Langlands Correspondence（Berkeley 课程讲稿，Tony Feng 记录）（Lecture notes, UC Berkeley, 2021-10-30 至 2022-01/02）§1.4.2，印刷页 3–3
- 锚点：Theorem 1.9（Laumon–Rapoport–Stuhler、Harris–Taylor、Henniart），原文 p.3

## 原文陈述

> 对非阿基米德局部域 E 与 n ≥ 1，GL_n(E) 的超尖表示与 Weil 群 W_E 的不可约 n 维复表示之间存在自然的双射（Laumon–Rapoport–Stuhler、Harris–Taylor、Henniart）。

英文：Theorem 1.9: there is a natural bijection between supercuspidal representations of GL_n(E) and irreducible n-dimensional representations W_E → GL_n(C).

## Lean 陈述

```lean
theorem lrs_bijection (E : Type u) (hE : localField E) (n : ℕ) :
    Nonempty (SupercuspidalRep E ≃ RepresentationCategory (WeilGroup E) (Fin n))
```

文件 `lean/ShuyiFormal/ScholzeFF/Gaps.lean`，声明名 `ScholzeFF.Gaps.lrs_bijection`；imports：`Mathlib.AlgebraicGeometry.Scheme`、`Mathlib.CategoryTheory.Monoidal.Braided.Basic`、`Mathlib.RingTheory.PicardGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- E 是非阿基米德局部域（占位谓词）
- n ≥ 1

## 盲验回译

> 对任意类型 E 与自然数 n，在占位假设 localField E 下，存在一个等价 SupercuspidalRep E ≃ RepresentationCategory (WeilGroup E) (Fin n)；两侧都是占位类型，命题只断言二者等价。

方法：blind-backtranslation；验卡人：subagent r01（盲回译：只读 Lean 语句与占位定义，未读中文陈述与原文）。

## 备注与缺口

缺口：超尖表示需要模空间/诱导理论；此卡只保留双射的形（两条消息都是占位类型）。原文印刷页 3。

- 缺口：mathlib 没有 $p$ 进局部域上的超尖表示概念，也没有 Weil 群的表示范畴（只有一般群的表示与有限群的对偶理论）。（blocked_by: mathlib 缺局部域表示论基础设施）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-27，`sorry` 数 1。

