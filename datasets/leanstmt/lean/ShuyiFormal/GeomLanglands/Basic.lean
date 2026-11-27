/-
几何 Langlands 定义层：B1 骨架四定义。

本文件只做定义，不声称任何定理。四个对象对应 adic 空间/perfectoid
这一层最靠前的类型：

* `HuberPair`：环 + 开子环（Huber 对），完备性/有界性先作为 `Prop` 字段；
* `Spa`：Huber 对的 adic 谱，先用 `PrimeSpectrum` 上满足 `A⁺` 条件的子类型；
* `Perfectoid`：显式 `p` 的 perfectoid 环，Frobenius 满射作为字段；
* `tilt`：`R^♭` 的骨架，先用 `ℕ → R` 上满足 Frobenius 兼容条件的子环实现；
  `R/p` 商环版本与完备化留到 B2（见 `tiltSubring` 的说明）。

硬约束：不用 `PUnit` 占位，不用 `axiom`；本文件不写 `sorry`。
-/
import Mathlib.Algebra.CharP.Lemmas
import Mathlib.Algebra.CharP.Pi
import Mathlib.Algebra.CharP.Subring
import Mathlib.Algebra.Ring.Subring.Basic
import Mathlib.RingTheory.Spectrum.Prime.Basic

set_option linter.unusedVariables false

universe u

namespace ShuyiFormal.GeomLanglands

/-- Huber 对：一个交换环 `A`，连带开子环 `A⁺`。

完备性与有界性暂时只作为 `Prop` 字段保留位置；等 adic 谱的赋值层建好后，
再把它们换成真正的 `IsComplete` / `IsBounded` 谓词。 -/
structure HuberPair where
  A : Type u
  [commRing : CommRing A]
  Aplus : Subring A
  isComplete : Prop
  isBounded : Prop

attribute [instance] HuberPair.commRing

/-- Huber 对的 adic 谱。

真正的 `Spa(A, A⁺)` 是 `A` 上连续赋值等价类的集合；这里先取
`PrimeSpectrum A` 中素理想落在 `A⁺` 里的点作为可陈述的骨架。
等赋值层建好后，把这个子类型替换成 `ValuationSpectrum`。 -/
def Spa (P : HuberPair.{u}) : Type u :=
  { p : PrimeSpectrum P.A // (p.asIdeal : Set P.A) ⊆ (P.Aplus : Set P.A) }

/-- 显式 `p` 的 perfectoid 环。

`p` 作为参数而不是 `Fact p.Prime` 的隐式实例，避免在每个引理里先造
`Fact`。`frobenius_surjective` 是 perfectoid 定义里的实质条件；
`Aplus` 的 Frobenius 满射等更细的条件留给后续结构。 -/
structure Perfectoid (p : ℕ) where
  A : Type u
  [commRing : CommRing A]
  [expChar : ExpChar A p]
  Aplus : Subring A
  isComplete : Prop
  isBounded : Prop
  frobenius_surjective : Function.Surjective (frobenius A p)

attribute [instance] Perfectoid.commRing Perfectoid.expChar

/-- `tilt` 的底层子环：`R^♭ = lim_{←Frob} R` 的序列模型。

元素是 `f : ℕ → R`，满足 `frobenius (f (n+1)) = f n`。
真正的 `R^♭` 是 `lim_{←Frob} R/p`；这里先用 `R` 上的 Frobenius
兼容序列，等 `R/p` 的商环与完备化接上后再收紧为 mod `p`。 -/
def tiltSubring (P : Perfectoid.{u} p) : Subring (ℕ → P.A) where
  carrier := { f | ∀ n, frobenius P.A p (f (n + 1)) = f n }
  zero_mem' := by
    intro n
    simp
  one_mem' := by
    intro n
    simp
  add_mem' := by
    intro f g hf hg n
    simp [hf n, hg n, map_add]
  mul_mem' := by
    intro f g hf hg n
    simp [hf n, hg n, map_mul]
  neg_mem' := by
    intro f hf n
    simp [hf n]

/-- `tilt` 的环结构，来自 `ℕ → R` 的子环。 -/
abbrev tiltRing (P : Perfectoid.{u} p) : Type u := tiltSubring P

instance (P : Perfectoid.{u} p) : CommRing (tiltRing P) := by
  dsimp [tiltRing]
  infer_instance

/-- `tilt` 的开子环：第 0 个分量落在 `P.Aplus` 里的序列。 -/
def tiltAplus (P : Perfectoid.{u} p) : Subring (tiltRing P) where
  carrier := { f | (f : ℕ → P.A) 0 ∈ P.Aplus }
  zero_mem' := by
    simp
  one_mem' := by
    simp
  add_mem' := by
    intro f g hf hg
    exact P.Aplus.add_mem hf hg
  mul_mem' := by
    intro f g hf hg
    exact P.Aplus.mul_mem hf hg
  neg_mem' := by
    intro f hf
    exact P.Aplus.neg_mem hf

/-- `R ↦ R^♭`：把 perfectoid 环送到它的 tilt。

Frobenius 满射的证明是“整体左移一位”：若 `x` 是兼容序列，
令 `y n = x (n+1)`，则 `y` 仍兼容，且 `y^p = x`。 -/
def tilt (P : Perfectoid.{u} p) : Perfectoid.{u} p where
  A := tiltRing P
  commRing := inferInstance
  expChar := inferInstance
  Aplus := tiltAplus P
  isComplete := True
  isBounded := True
  frobenius_surjective := by
    intro x
    refine ⟨⟨fun n => (x : ℕ → P.A) (n + 1), ?_⟩, ?_⟩
    · intro n
      exact x.property (n + 1)
    · ext n
      change (x : ℕ → P.A) (n + 1) ^ p = (x : ℕ → P.A) n
      exact x.property n

end ShuyiFormal.GeomLanglands
