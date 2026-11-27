import Lake
open Lake DSL

/-
  数译形式化陈述层（leanstmt 的 Lean 侧）。

  只放两类东西：
    * 定义：把论文里用到的数学对象写成真的 `def` / `structure`，不用占位；
    * 陈述：定理陈述可编译，证明一律 `sorry`，并由卡片的 `verification.status`
      标成 gap 记进缺口台账（`datasets/leanstmt/gaps/`）。

  版本钉死：Lean 见 `lean-toolchain`，mathlib 见下面的 rev——
  换 rev 必须同步改 `lake-manifest.json` 与各卡的 `verification.mathlib_rev`。
-/

package «shuyi-leanstmt» where
  description := "数译形式化陈述层：定义与定理陈述（证明以 sorry 占位并登记 gap）"
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "d33c49ca43873d3746194325da62640cc893c9d9"

@[default_target]
lean_lib «ShuyiFormal» where
  globs := #[.submodules `ShuyiFormal]
