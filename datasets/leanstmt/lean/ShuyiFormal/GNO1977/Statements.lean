/-
GNO 1977（Goddard–Nuyts–Olive, "Gauge Theories and Magnetic Charge",
Nucl. Phys. B125 (1977) 1–28）陈述层转写：可落在 mathlib 上的离散/代数部分。

对应语料卡：datasets/leanstmt/cards/statements/gno1977-s01 .. s06。

注意：本文件只做"陈述层"（L1），不含证明工作量的创造性内容；
结构性缺口见 Gaps.lean。
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality

set_option maxHeartbeats 800000

namespace GNO1977

/-!
### S01 整数权（式 (1.3) 的 U(1) 特例 / 权格的整数性）

GNO 的磁权 $p_i$ 在归一化后落在权格上；对 $U(1)$ 而言，"权"就是整数：
$\exp(2\pi i z) = 1 \iff z \in \mathbb{Z}$。
-/
theorem weight_integrality (z : ℂ) :
    Complex.exp (2 * (Real.pi : ℂ) * Complex.I * z) = 1 ↔ ∃ n : ℤ, z = (n : ℂ) := by
  rw [Complex.exp_eq_one_iff]
  constructor
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have hne : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
      simp [Real.pi_ne_zero]
    have h : (2 * (Real.pi : ℂ) * Complex.I) * z = (2 * (Real.pi : ℂ) * Complex.I) * (n : ℂ) := by
      rw [hn]; ring
    exact mul_left_cancel₀ hne h
  · rintro ⟨n, rfl⟩
    exact ⟨n, by ring⟩

/-!
### S02 狄拉克量子化条件（式 (1.3) 的 $U(1)$ 情形）

$\exp(4\pi i z) = 1 \iff 2z \in \mathbb{Z}$，即电荷与磁荷乘积取半整数，
这正是 GNO 式 (1.3) $\exp(4\pi i eG) = 1$ 在 $U(1)$ 上的形式。
-/
theorem dirac_quantization (z : ℂ) :
    Complex.exp (4 * (Real.pi : ℂ) * Complex.I * z) = 1 ↔ ∃ n : ℤ, 2 * z = (n : ℂ) := by
  rw [Complex.exp_eq_one_iff]
  constructor
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have hne : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
      simp [Real.pi_ne_zero]
    have h : (2 * (Real.pi : ℂ) * Complex.I) * (2 * z) =
        (2 * (Real.pi : ℂ) * Complex.I) * (n : ℂ) := by
      have h1 : (2 * (Real.pi : ℂ) * Complex.I) * (2 * z) =
          4 * (Real.pi : ℂ) * Complex.I * z := by ring
      rw [h1, hn]
      ring
    exact mul_left_cancel₀ hne h
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    rw [← hn]
    ring

/-!
### S03 $SU(N)$ 中心元（磁权和的模 $N$ 条件）

若 $k \in \mathbb{Z}$，则 $\zeta = \exp(2\pi i k/N)$ 满足 $\zeta^N = 1$：
这是 $SU(N)$ 的权格中 $\sum_i p_i \equiv 0 \pmod N$ 的单变量原型。
-/
theorem center_element_pow (N : ℕ) (hN : N ≠ 0) (k : ℤ) :
    (Complex.exp (2 * (Real.pi : ℂ) * Complex.I * (k : ℂ) / N)) ^ N = 1 := by
  rw [← Complex.exp_natCast_mul]
  have h : (N : ℂ) * (2 * (Real.pi : ℂ) * Complex.I * (k : ℂ) / N) =
      2 * (Real.pi : ℂ) * Complex.I * (k : ℂ) := by
    field_simp
  rw [h]
  simpa [mul_assoc, mul_comm, mul_left_comm] using Complex.exp_int_mul_two_pi_mul_I k

/-!
### S04 对偶群与原群同阶

磁对偶群 $H^\vee = \operatorname{Hom}(H, U(1))$ 与原群同阶（GNO §4–5 的有限群情形）。
-/
theorem dual_card {α : Type*} [AddCommGroup α] [Fintype α] :
    Fintype.card (AddChar α ℂ) = Fintype.card α :=
  AddChar.card_eq

/-!
### S05 双对偶 $(H^\vee)^\vee \cong H$（式 (1.6) 的有限阿贝尔情形）

GNO 式 (1.6)：$(H^\vee)^\vee = H$。对有限阿贝尔群由 Pontryagin 双对偶给出。
-/
theorem double_dual (n : ℕ) [NeZero n] :
    Nonempty (ZMod n ≃+ AddChar (AddChar (ZMod n) ℂ) ℂ) :=
  ⟨AddChar.doubleDualEquiv⟩

/-!
### S06 Weyl 反射 $p \mapsto -p$ 保持量子化条件

秩 1 情形 Weyl 群 $S_2$ 把磁权 $p$ 送到 $-p$；量子化条件
$\exp(4\pi i z) = 1$ 在这个反射下不变。
-/
theorem magnetic_weight_neg (z : ℂ) :
    Complex.exp (4 * (Real.pi : ℂ) * Complex.I * z) = 1 ↔
      Complex.exp (4 * (Real.pi : ℂ) * Complex.I * (-z)) = 1 := by
  have hneg : 4 * (Real.pi : ℂ) * Complex.I * (-z) = -(4 * (Real.pi : ℂ) * Complex.I * z) := by
    ring
  rw [hneg, Complex.exp_neg, inv_eq_one]

end GNO1977
