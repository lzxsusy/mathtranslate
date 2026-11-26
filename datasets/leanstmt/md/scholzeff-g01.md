# 缺口：FF 曲线的线丛分类 Pic ≅ ℤ

- 卡号：`leanstmt/scholzeff-g01`　轨道：FF21　scope：`gap`　验证：**gap**
- 来源：Scholze, Geometrization of the Local Langlands Correspondence（Berkeley 课程讲稿，Tony Feng 记录）（Lecture notes, UC Berkeley, 2021-10-30 至 2022-01/02）§4.4，印刷页 20–21
- 锚点：Corollary 4.14（原文 p.20–21）

## 原文陈述

> 对任何非阿基米德局部域 E 与完备代数闭剩余域 C，Fargues–Fontaine 曲线 X_{C,E} 的 Picard 群同构于 ℤ，且线丛 O(D) 只依赖次数 deg D：Pic(X_{C,E}) ≅ ℤ。

英文：Corollary 4.14: O(D) ≅ O(deg D) and Pic(X_{C,E}) ≅ ℤ, normalized so that O(1) ↦ 1.

## Lean 陈述

```lean
theorem pic_ff_curve_is_int (E : Type u) (hE : localField E) :
    Nonempty (PicardGroup E ≃ ℤ)
```

文件 `lean/ShuyiFormal/ScholzeFF/Gaps.lean`，声明名 `ScholzeFF.Gaps.pic_ff_curve_is_int`；imports：`Mathlib.AlgebraicGeometry.Scheme`、`Mathlib.CategoryTheory.Monoidal.Braided.Basic`、`Mathlib.RingTheory.PicardGroup`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- E 是非阿基米德局部域（占位谓词）
- C 完备代数闭（卡内省略，见 notes）

## 盲验回译

> 对任意类型 E，在占位假设 localField E 下，存在一个等价 PicardGroup E ≃ ℤ（形式为 Nonempty (PicardGroup E ≃ ℤ)）；PicardGroup E 是占位类型，命题只断言它与 ℤ 之间存在等价。

方法：blind-backtranslation；验卡人：subagent r01（盲回译：只读 Lean 语句与占位定义，未读中文陈述与原文）。

## 备注与缺口

缺口：FF 曲线的构造（$\mathbb D^*_C/arphi_C^{\mathbb Z}$ 的 adic 空间商）本身无法在 mathlib 里陈述；此卡的 Lean 语句只保留「Pic ≅ ℤ」的形状。原文印刷页 20–21（PDF 页相同）。

- 缺口：mathlib 没有 Fargues–Fontaine 曲线、等晶体与 perfectoid 空间这一层；Picard 群只有概形的 PicardGroup，没有 $\mathbb D^*_C/arphi^{\mathbb Z}$ 上的线丛分类。（blocked_by: mathlib 缺 $p$ 进几何基础设施）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-27，`sorry` 数 1。

