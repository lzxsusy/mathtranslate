/-
  Witten, "Mirror Symmetry, Hitchin's Equations, and Langlands Duality",
  arXiv:0802.0999v1 (2008) —— 陈述层形式化（certified 部分）。

  本文件只包含在现有 Mathlib 上真正可编译、且证明已给出（无 sorry）的陈述；
  每条陈述的原文定位见 `datasets/leanstmt` 中对应卡片。无法忠实陈述的条目
  一律进 `Gaps.lean`。

  风险提示（见 playbook/14）：Lean 语句「类型对、含义错」照样能编译，
  因此每条都配了人工盲验回译，见卡片 `backtranslation` 字段。
-/
import Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.SpecialLinearGroup
import Mathlib.Logic.Equiv.Prod

set_option maxHeartbeats 800000

namespace Witten2008

/-! ## S01：SU(N) 的中心（Langlands 对偶群 PSU(N) 的离散核）

原文 §2：Langlands 对偶群的基本例子是 `SU(N)` 的对偶为
`PSU(N) = SU(N)/Z_N`，其中 `Z_N` 是中心。这里把「中心 = 标量矩阵 ζ·1，
ζ^N = 1」这一离散事实形式化：`SL(N,ℂ)` 的中心恰为 `μ_N`。

对应 Mathlib：`SpecialLinearGroup.mem_center_iff`（中心元 ↔ 标量
`r • id` 且 `r ^ finrank = 1`）。-/
theorem center_sl (n : ℕ) (g : SpecialLinearGroup ℂ (Fin n → ℂ)) :
    g ∈ Subgroup.center (SpecialLinearGroup ℂ (Fin n → ℂ)) ↔
      ∃ r : ℂ, r ^ n = 1 ∧
        (g : (Fin n → ℂ) →ₗ[ℂ] (Fin n → ℂ)) = r • LinearMap.id := by
  have h : Module.finrank ℂ (Fin n → ℂ) = n := by
    rw [Module.finrank_fintype_fun_eq_card, Fintype.card_fin]
  rw [SpecialLinearGroup.mem_center_iff, h]

/-! ## S02：有限阿贝尔群是 Pontryagin 自对偶的（T-对偶的离散影子）

原文 §2–§3：GNO / Langlands 对偶把环面换成对偶环面；在 SYZ 图像下即
special Lagrangian 纤维上的 T-对偶。有限群层面的影子是
`Hom(ℤ_N, U(1)) ≅ ℤ_N`（对偶环面与原环面同秩）。

对应 Mathlib：`AddChar.card_eq`（`|Hom(A,ℂ^*)| = |A|`）、
`AddChar.zmodAddEquiv`（`ZMod n ≃+ AddChar (ZMod n) ℂ`）。-/
theorem card_dual_zmod (n : ℕ) [NeZero n] :
    Fintype.card (AddChar (ZMod n) ℂ) = n := by
  rw [AddChar.card_eq, ZMod.card]

/-- 同上，用显式加法群同构表述 `ℤ_N ≅ Hom(ℤ_N, U(1))`。 -/
theorem dual_zmod_equiv (n : ℕ) [NeZero n] :
    Nonempty (ZMod n ≃+ AddChar (ZMod n) ℂ) :=
  ⟨AddChar.zmodAddEquiv⟩

/-! ## S03：非正则奇点的系数在 `z ↦ λz` 下的伸缩律

原文 §5：`A = dz·(T_n/z^n + … + T_1/z + …)`。在重标度 `z = λw`（`λ ≠ 0`）
下，第 `m+1` 个系数变成 `λ^{1-(m+1)} T_{m+1} = T_{m+1}/λ^m`：

  `λ · (T_{m+1} / λ^{m+1}) = T_{m+1} / λ^m`，

即留数项 `T_1` 不变（`m = 0`），`m ≥ 1` 的项按 `λ^{-m}` 伸缩。
这正是原文说「只有 `T_1` 与奇点阶数 `n` 是规范不变量」的算术内容。-/
theorem coefficient_scaling (lam c : ℂ) (hlam : lam ≠ 0) (m : ℕ) :
    lam * (c / lam ^ (m + 1)) = c / lam ^ m := by
  rw [pow_succ']
  field_simp

/-- 特例 `m = 0`：留数（一次项系数）是重标度不变量。 -/
theorem residue_invariant (lam c : ℂ) (hlam : lam ≠ 0) :
    lam * (c / lam) = c := by
  field_simp

/-! ## S04：`Maps(Σ, Maps(C,G)) ≃ Maps(Σ × C, G)`（currying）

原文 §6.1：四维规范场在 `M = Σ × C` 上的规范变换群是
`Maps(Σ, W) = Maps(Σ × C, G)`——这一步只是「分层映射」的 currying。
这里形式化类型层面的等价（群结构逐点给出，见卡片说明）。-/
theorem gauge_maps_curry (Sig C G : Type*) :
    Nonempty (((Sig → C → G) ≃ (Sig × C → G))) :=
  ⟨(Equiv.curry Sig C G).symm⟩

end Witten2008
