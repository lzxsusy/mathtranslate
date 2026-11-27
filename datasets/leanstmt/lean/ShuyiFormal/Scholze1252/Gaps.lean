/-
  Peter Scholze, "Geometric Langlands [after Gaitsgory, Raskin, …]",
  Séminaire Bourbaki, 78e année (2025–2026), n° 1252, Mars 2026 —— 陈述层形式化（缺口 GAP）。

  本文件只记录**猜想 2.10（几何 Langlands 猜想）的语句形状**：
  $$ \mathcal D(\mathrm{Bun}_G)\;\simeq\;\mathrm{IndCoh}_{\mathrm{Nilp}}(\mathrm{LocSys}_{\check G}), $$
  归一化使结构层送到 Whittaker 层。

  **这不是对猜想 2.10 的形式化。** `AutomorphicSide` / `SpectralSide` 是不透明占位类型；
  忠实的形式化需要：光滑射影曲线 $X$ 及其上的 $G$-丛叠 $\mathrm{Bun}_G$、
  $(\infty,1)$-范畴意义下的导出范畴 $\mathcal D(\mathrm{Bun}_G)$、
  局部系统叠 $\mathrm{LocSys}_{\check G}$（Betti / de Rham / étale 三种 setting）、
  幂零奇异支撑子范畴 $\mathrm{IndCoh}_{\mathrm{Nilp}}$ 与 Hecke 作用，
  这些在 Mathlib 中都没有（Mathlib 至今没有六函子形式化，也没有 $\mathrm{Bun}_G$）。

  文件末尾的 `sorry` 只用于让缺口陈述通过语法检查。
  纪律：本文件的声明只是占位签名，不构成“已形式化的命题”；卡片
  `verification.status` 必须为 `gap`，`gaps[].reason` 必须写清缺口。
-/
set_option autoImplicit false

namespace Scholze1252.Gaps

/-- 占位：自守侧范畴 $\mathcal D(\mathrm{Bun}_G)$。

真实定义需要 Bosonic 意义下的光滑射影曲线、约化群 $G$ 的 $\mathrm{Bun}_G$ 叠、
以及 $(\infty,1)$-范畴的六函子形式化；Mathlib 均无。 -/
opaque AutomorphicSide (k : Type) [Field k] : Type

/-- 占位：谱侧范畴 $\mathrm{IndCoh}_{\mathrm{Nilp}}(\mathrm{LocSys}_{\check G})$。

真实定义需要 Langlands 对偶群 $\check G$、$\check G$-局部系统叠（三种 setting 各自不同）、
以及 Arinkin–Gaitsgory 意义下的归纳凝聚层与幂零奇异支撑。 -/
opaque SpectralSide (k : Type) [Field k] : Type

/-- 猜想 2.10（几何 Langlands 猜想）的语句形状。

对代数闭域 $k$ 上的光滑射影曲线 $X$ 与约化群 $G$，存在范畴等价
$\mathcal D(\mathrm{Bun}_G)\simeq\mathrm{IndCoh}_{\mathrm{Nilp}}(\mathrm{LocSys}_{\check G})$，
其归一化把结构层送到 Whittaker 层（原文用 $\Theta$-特征与 Whittaker 层 $\mathcal W_\psi$ 固定唯一性）。

这里 `Nonempty (A ≃ B)` 只记录“存在等价”这一骨架，不记录等价的归一化条件，
也不记录特征 $p$ 时需换成开闭子叠 $\mathrm{LocSys}'_{\check G}$ 的修正。 -/
theorem glc_equivalence_shape (k : Type) [Field k] :
    Nonempty (AutomorphicSide k ≃ SpectralSide k) := by
  sorry

end Scholze1252.Gaps
