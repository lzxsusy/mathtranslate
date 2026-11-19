/-
Witten 2015 陈述层形式化的**缺口卡**（status: gap）。

这些陈述在原文中是核心命题，但当前 mathlib（commit 见 `lake-manifest.json`）
没有对应的数学基础设施，因此只能写下"应该被证明的命题"：把待实现的几何对象
声明成占位（`specCurveGenus` / `hitchinFiberDim`），把原文的断言写成关于它们的
命题，再用 `sorry` 占位。缺口本身是语料的交付内容之一：每条都写明缺什么。
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.LinearAlgebra.Dual.Lemmas

namespace Witten2015.Gaps

/-- 占位：谱曲线 `D → C` 的亏格（mathlib 尚无曲线亏格，见 G01 备注）。 -/
def specCurveGenus (N g : ℕ) : ℕ := 0

/-- 占位：一般 Hitchin 纤维的复维数（mathlib 尚无 Hitchin 模空间，见 G02 备注）。 -/
def hitchinFiberDim (g dimG : ℕ) : ℕ := 0

/-- 缺口卡 G01（原文 §2.6.1–§2.6.2）：N 层谱曲线 `D → C` 的亏格为 `N²(g−1)+1`。

缺口：mathlib 没有紧黎曼面/代数曲线的亏格、分歧除子与 Riemann–Hurwitz 公式；
`AlgebraicGeometry` 里的 scheme 层没有曲线亏格与除子次数的一般理论。
需要的基础设施：曲线（`Smooth` + `Proper` + `GeometricallyConnected`）的 `genus`、
有限态射的分歧除子、Riemann–Hurwitz。
-/
theorem spectral_curve_genus (N g : ℕ) (hN : 2 ≤ N) (hg : 2 ≤ g) :
    specCurveGenus N g = N ^ 2 * (g - 1) + 1 := by
  sorry

/-- 缺口卡 G02（原文 §2.4–§2.6）：Hitchin 纤维化的一般纤维是 `½ dim M_H = (g−1)·dim G`
维紧复环面。

缺口：mathlib 没有 Hitchin 模空间、稳定丛模空间（`Bun_G`）、稳定性判据，
也没有黎曼面上主丛模空间的余切丛与辛结构。
-/
theorem hitchin_fiber_dimension (g dimG : ℕ) (hg : 2 ≤ g) :
    hitchinFiberDim g dimG = (g - 1) * dimG := by
  sorry

end Witten2015.Gaps
