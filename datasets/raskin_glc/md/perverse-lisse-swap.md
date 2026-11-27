# $\sigma^{(d)}$ 与 $\mathcal{F}_\sigma$ 的 perverse/lisse 性质被互换

- id：`raskin_glc/correction/perverse-lisse-swap`
- 类型：correction　轨道：B　状态：dev
- 一句话：原文说 $\sigma^{(d)}$ 是 perverse 但非 lisse；实际上 $\sigma^{(d)}$ 是 $\operatorname{Sym}^d X$ 上的秩 $1$ 局部系统，因而是 lisse；真正 perverse 但非 lisse 的是 $\mathcal{F}_\sigma$。

**问题**：为什么把「perverse」与「lisse」对调会误导读者对目标 3.1.2 的理解？

## 位置

§3.1，原文 p.9（$\operatorname{coeff}_d$ 的升级段落）

## 原文

> However, $\sigma^{(d)}$ is perverse but not lisse.

## 应为

> $\sigma^{(d)}$ is lisse; $\mathcal{F}_\sigma$ is perverse but not lisse.

## 理由

$\sigma^{(d)}=(\mathrm{add}_{d,*}\sigma^{\boxtimes d})^{S_d}$ 是 $\operatorname{Sym}^d X$ 上的局部系统：$\mathrm{add}_{d,*}$ 把局部系统推前为局部系统，取 $S_d$-不变量仍是局部系统，故 lisse。$\mathcal{F}_\sigma$ 是 $\operatorname{Bun}_{\mathrm{PGL}_2}$ 上的反常层，支撑在整个叠上（包括非半稳定部分），其奇异支撑非零，故 perverse 而非 lisse。

## 说明

此句位于「$\operatorname{coeff}_d(\mathcal{F}_\sigma)\cong\sigma^{(d)}$」之后，读者容易误以为 $\operatorname{coeff}_d(\mathcal{F}_\sigma)$ 是 perverse 的；实际上它是 $\operatorname{Sym}^d X$ 上的 lisse 层。译文照录原文并加译注。

## 出处

- Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》（2025-07-07/11，18 页），§3.1，$\operatorname{coeff}_d$ 的升级，pp. 9；`源码/sections/s03-coeff.tex:L95-L110（原文照录与译注）`
  > However, σ^(d) is perverse but not lisse.

## 相关卡

- `raskin_glc/concept/coefficient-functor`
- `raskin_glc/concept/pgl2-geometric-langlands`

## 核验（source-only，2026-11-27）

- 无外部逐条核验；见上方说明。

更正依据是局部系统的定义与原文自身对 $\mathcal{F}_\sigma$ 的描述；无需外部页面。
