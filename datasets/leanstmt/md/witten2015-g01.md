# 缺口：谱曲线的亏格 N²(g−1)+1

- 卡号：`leanstmt/witten2015-g01`　轨道：W15　scope：`gap`　验证：**gap**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）2.6.1，印刷页 10–13
- 锚点：§2.6.1–§2.6.2

## 原文陈述

> 谱曲线 D → C 是 N 层覆盖，其亏格为 N²(g−1)+1（原文 §2.6.1–2.6.2 的核心几何事实）。

英文：The spectral curve is an N-sheeted cover of C and has genus N²(g−1)+1.

## Lean 陈述

```lean
theorem spectral_curve_genus (N g : ℕ) (hN : 2 ≤ N) (hg : 2 ≤ g) :
    specCurveGenus N g = N ^ 2 * (g - 1) + 1
```

文件 `lean/ShuyiFormal/Witten2015/Gaps.lean`，声明名 `Witten2015.Gaps.spectral_curve_genus`；imports：`Mathlib.Data.ZMod.Basic`

## 依赖

- Mathlib 无曲线亏格：本卡用占位 `specCurveGenus` 承载命题

## 假设

- N ≥ 2（N 层谱覆盖）
- g ≥ 2（曲线非平凡）
- `specCurveGenus` 为待实现占位（def 值 0），因此本卡 status=gap

## 盲验回译

> （缺口占位）N 层覆盖的谱曲线亏格为 N²(g−1)+1。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

缺口：mathlib 无紧黎曼面/代数曲线的亏格、分歧除子、Riemann–Hurwitz。需要 `Curve` 上的 `genus`、有限态射分歧除子与 RH 公式；这是本批 12 条中阻塞最硬的一条。

- 缺口：mathlib 无紧黎曼面/代数曲线的亏格、分歧除子、Riemann–Hurwitz。需要 `Curve` 上的 `genus`、有限态射分歧除子与 RH 公式；这是本批 12 条中阻塞最硬的一条。（blocked_by: mathlib 基础设施缺失）

验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 1。

