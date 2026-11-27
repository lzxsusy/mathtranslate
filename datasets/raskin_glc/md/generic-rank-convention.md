# 通用秩公式中的指数 $d_i$

- id：`raskin_glc/remark/generic-rank-convention`
- 类型：remark　轨道：D　状态：dev
- 一句话：原文写通用秩为 $\prod_i d_i^{(2d_i-1)(g-1)}$，称 $d_i$ 为 $G$ 的指数。按此约定，$\mathrm{GL}_2$ 的指数为 $1,2$，公式给 $2^{3g-3}$；$\mathrm{PGL}_2$ 的指数为 $1$，公式给 $1$，都与各自已知的通用秩一致。

**问题**：$d_i$ 应如何代入：按 $G$ 的指数，还是按不变多项式的次数？

## 陈述

对 $g>1$，定理 4.3.2 中 $\mathcal{F}_\sigma$ 的通用秩为 $\prod_i d_i^{(2d_i-1)(g-1)}$，其中 $d_i$ 为 $G$ 的指数。

## 缘由

对 $G=\mathrm{GL}_2$，指数为 $1,2$，故 $\prod_i d_i^{(2d_i-1)(g-1)}=1^1\cdot 2^{3(g-1)}=2^{3g-3}$，与已知的 $\mathrm{GL}_2$ Hecke 特征层通用秩一致；对 $G=\mathrm{PGL}_2$，指数为 $1$，公式给 $1$，也与其通用秩一致。若把 $d_i$ 读成不变多项式的次数（$\mathrm{GL}_2$ 为 $2,3$），会得到不同数值，那不是原文的约定。

## 说明

译文按「$G$ 的指数」解释并加脚注，不改原公式；读者不要把 $d_i$ 读成不变多项式次数。

## 出处

- Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》（2025-07-07/11，18 页），§4.3，定理 4.3.2 后的通用秩公式，pp. 15；`源码/sections/s04-hecke.tex 定理 4.3.2 后的通用秩公式与脚注 20`
  > For g > 1, the generic rank of F_σ is ∏_i d_i^{(2d_i−1)(g−1)}, where d_i's are the exponents of G.

## 相关卡

- `raskin_glc/concept/hecke-eigensheaf`
- `raskin_glc/concept/pgl2-geometric-langlands`

## 核验（source-only，2026-11-27）

- 无外部逐条核验；见上方说明。

据原文与译文脚注；未逐篇核外部文献对该公式的陈述，故只记原文约定与两个自洽校验。
