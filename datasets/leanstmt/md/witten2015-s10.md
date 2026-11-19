# 分歧除子的次数 = 2N(N−1)(g−1)

- 卡号：`leanstmt/witten2015-s10`　轨道：W15　scope：`arithmetic-core`　验证：**certified**
- 来源：Witten, More On Gauge Theory And Geometric Langlands（arXiv:1506.04293v3）2.6.1，印刷页 10–12
- 锚点：§2.6.1（谱曲线的 Riemann–Hurwitz 计算）

## 原文陈述

> 由 Riemann–Hurwitz 公式反解，N 层谱覆盖 D → C 的分歧除子次数为 2N(N−1)(g−1)。

英文：Riemann–Hurwitz gives deg R = 2N(N−1)(g−1) for an N-sheeted spectral cover.

## Lean 陈述

```lean
theorem ramification_degree (N g : ℤ) :
    2 * (N ^ 2 * (g - 1) + 1) - 2 - N * (2 * g - 2) = 2 * N * (N - 1) * (g - 1)
```

文件 `lean/ShuyiFormal/Witten2015/Statements.lean`，声明名 `Witten2015.ramification_degree`；imports：`Mathlib.Data.ZMod.Basic`

## 依赖

- 仅用核心库/基础算术，无额外依赖

## 假设

- N, g 为整数

## 盲验回译

> 对任意整数 N、g，把 g_D = N²(g−1)+1 代入 2g_D−2 = N(2g−2)+deg R 解出的 deg R 等于 2N(N−1)(g−1)。

方法：blind-backtranslation；验卡人：subagent（未见本卡中文陈述，仅据 Lean 语句回译）。

## 备注与缺口

与 S09 同族：Riemann–Hurwitz 本身未形式化，本卡固化代数恒等式；原文式 (2.19) 附近。


验证环境：leanprover/lean4:v4.36.0，mathlib `d33c49ca43873d3746194325da62640cc893c9d9`，检查日期 2026-11-19，`sorry` 数 0。

