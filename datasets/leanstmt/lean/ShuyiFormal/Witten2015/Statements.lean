/-
Witten 2015（arXiv:1506.04293v3）陈述层形式化试点。
每条陈述对应 `datasets/leanstmt/cards/` 中的一张卡；本文件只做陈述层（L1），
证明尽量给出（凡 mathlib 已证者直接复用），缺口卡见 Gaps.lean。

约定：
* 不做证明层；mathlib 已有证明的引理，直接作为等价陈述给出。
* 每条的来源页/式锚写在注释里（印刷页 = PDF 页 − 1）。
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.LinearAlgebra.Dimension.Finrank

namespace Witten2015

set_option maxHeartbeats 800000

open Complex

/-! ## §2.6.6 PSU(N) 的 't Hooft 磁通取值于 ℤ_N -/

/-- 卡 S01：'t Hooft 磁通所在的群 `ℤ_N` 恰有 N 个元素。来源：原文 §2.6.6（印刷 p.14–16）。-/
theorem card_zmod (N : ℕ) [NeZero N] : Fintype.card (ZMod N) = N :=
  ZMod.card N

/-- 卡 S02：`ℤ_N` 由 1 生成，其加法阶为 N。来源：原文 §2.6.6。 -/
theorem orderOf_one_zmod (N : ℕ) : addOrderOf (1 : ZMod N) = N :=
  ZMod.addOrderOf_one N

/-- 卡 S03：`ℤ_N` 中每个元素都是 N-挠的（N·x = 0），即磁通量 N 次为零。来源：原文 §2.6.6。 -/
theorem nsmul_zmod (N : ℕ) (x : ZMod N) : N • x = 0 := by
  rw [nsmul_eq_mul, ZMod.natCast_self, zero_mul]

/-! ## §4.1/§7.1 't Hooft 算符的本征值是 N 次单位根 -/

/-- 卡 S04：`z` 是 N 次单位根当且仅当 `z^N = 1`。来源：原文 §7.1（印刷 p.66–67）。 -/
theorem mem_rootsOfUnity_iff (n : ℕ) (z : ℂˣ) : z ∈ rootsOfUnity n ℂ ↔ (z : ℂ) ^ n = 1 :=
  mem_rootsOfUnity' n z

/-- 卡 S05：ℂ 中 N 次单位根恰有 N 个（N ≥ 1）。来源：原文 §4.1、§7.1。 -/
theorem card_rootsOfUnity_complex (n : ℕ) [NeZero n] : Nat.card (rootsOfUnity n ℂ) = n :=
  card_rootsOfUnity_eq_iff_exists_isPrimitiveRoot.mpr
    ⟨_, Complex.isPrimitiveRoot_exp_of_coprime 1 n (NeZero.ne n) (by simp)⟩

/-! ## §3 GNO 对偶环面：电荷格的对偶再对偶 -/

/-- 卡 S06：有限自由模与其双对偶同构（Langlands 对偶的“双重对偶回到自身”）。来源：原文 §3.2、§3.3。 -/
theorem double_dual (K V : Type*) [Field K] [AddCommGroup V] [Module K V]
    [Module.Finite K V] [Module.Free K V] : Nonempty (V ≃ₗ[K] Module.Dual K (Module.Dual K V)) :=
  ⟨Module.evalEquiv K V⟩

/-- 卡 S07：对偶格与原格同秩（GNO 对偶环面与原环面维数相同）。来源：原文 §3.2。 -/
theorem dual_finrank (K V : Type*) [Field K] [AddCommGroup V] [Module K V]
    [Module.Finite K V] : Module.finrank K (Module.Dual K V) = Module.finrank K V :=
  Subspace.dual_finrank_eq

/-! ## §2.6.5 自旋结构：典范线丛的次数 2g−2 是偶数 -/

/-- 卡 S08：`2g − 2` 是偶数，故曲面上典范丛总有平方根（自旋结构）。来源：原文 §2.6.5。 -/
theorem even_deg_canonical (g : ℤ) : Even (2 * g - 2) :=
  ⟨g - 1, by ring⟩

/-! ## §2.6.2 阿贝尔化与 Prym：维数账 -/

/-- 卡 S09：谱曲线亏格 `g_D = N²(g−1)+1` 时，Prym 的维数 `g_D − g = (N²−1)(g−1)`。来源：原文 §2.6.2。 -/
theorem prym_dim (N g : ℤ) : (N ^ 2 * (g - 1) + 1) - g = (N ^ 2 - 1) * (g - 1) := by
  ring

/-- 卡 S10：由 Riemann–Hurwitz 反解，分歧除子的次数为 `2N(N−1)(g−1)`。来源：原文 §2.6.1。 -/
theorem ramification_degree (N g : ℤ) :
    2 * (N ^ 2 * (g - 1) + 1) - 2 - N * (2 * g - 2) = 2 * N * (N - 1) * (g - 1) := by
  ring

end Witten2015
