# 尖点层与常数项函子

- id：`raskin_glc/concept/cuspidal-sheaf`
- 类型：concept　轨道：B　状态：dev
- 一句话：用 Hecke 对应 $\operatorname{Bun}_{\mathrm{PGL}_2}\xleftarrow{p}\operatorname{Bun}_B\xrightarrow{q}\operatorname{Bun}_{\mathbb{G}_m}$ 定义常数项 $\mathrm{CT}_*:=q_*p^!$；$\mathrm{CT}_*\mathcal{F}\simeq 0$ 即 $\mathcal{F}$ 为尖点层。

**问题**：为什么常数项用 $p^!$ 而不是 $p_*$，以及为什么「对所有 $d$ 消没」等价于「$\mathrm{CT}_*\simeq 0$」？

## 定义

设 $G=\mathrm{PGL}_2$，$B\subset G$ 为 Borel 子群。考虑对应 $\operatorname{Bun}_G\xleftarrow{p}\operatorname{Bun}_B\xrightarrow{q}\operatorname{Bun}_{\mathbb{G}_m}$，其中 $p$ 记 $(0\to L\to\mathcal{E}\to\mathcal{O}\to 0)\mapsto\mathcal{E}$，$q$ 记 $\mapsto L$。定义常数项函子 $\mathrm{CT}_*:=q_*p^!:\operatorname{Shv}(\operatorname{Bun}_G)\to\operatorname{Shv}(\operatorname{Bun}_{\mathbb{G}_m})$，并按次数分解为 $\mathrm{CT}^d_*$。称 $\mathcal{F}\in\operatorname{Shv}(\operatorname{Bun}_G)$ 为尖点层，若 $\mathrm{CT}_*\mathcal{F}\simeq 0$；等价地，对所有 $d$ 有 $\mathrm{CT}^d_*\mathcal{F}\simeq 0$。一般约化群用所有真抛物子群及其 Levi 商重复此定义。

记号：$\operatorname{Bun}^d_B$ 为 $\deg L=d$ 的连通分支；$\mathrm{CT}^d_*$ 为 $\mathrm{CT}_*$ 限制到该分支；$\operatorname{Shv}$ 为可构造层的有界导出范畴。

## 要点

- 常数项是「沿抛物子群的纤维做紧支集积分」的层论版本：$p^!$ 先把 $\mathcal{F}$ 拉回到 $\operatorname{Bun}_B$，再用 $q_*$ 沿 $\operatorname{Bun}_B\to\operatorname{Bun}_{\mathbb{G}_m}$ 推前。
- $p^!$ 而非 $p_*$ 的选择使 $\mathrm{CT}_*$ 与 Verdier 对偶交换：$\mathrm{CT}_*\simeq D\,\mathrm{CT}^!\,D$，其中 $\mathrm{CT}^!:=q_!p^*$。
- 对 $\mathrm{PGL}_2$，$\operatorname{Bun}_B$ 按 $\deg L$ 分解，因此 $\mathrm{CT}_*\simeq 0$ 等价于每个 $\mathrm{CT}^d_*\simeq 0$；一般 $G$ 要对所有真抛物子群及 Levi 商同时消没。
- 尖点性在 Verdier 对偶下保持（Cor 2.1.9），并且在 $d>2g-2$ 时给出到 $\operatorname{Bun}^d_B$ 的 $!$-与 $*$-限制的消没（Cor 2.1.10）。
- 存在只依赖 $g$ 的开子叠 $U_n$，任意尖点层都从 $U_n$ 同时以 $!$ 与 $*$ 延拓（Cor 2.1.11）；这是后面「先用 $U_n$ 上的限制控制 $\mathcal{F}$」的起点。

## 公式

$$ \mathrm{CT}_*:=q_*p^! $$

$$ \mathrm{CT}^!:=q_!p^* $$

$$ \mathrm{CT}_*\simeq D\,\mathrm{CT}^!\,D $$

$$ \mathrm{CT}_*\mathcal{F}\simeq 0\iff \forall d,\ \mathrm{CT}^d_*\mathcal{F}\simeq 0 $$

## 定理与证明状态

### 命题 2.1.5

若 $\mathcal{F}$ 为尖点层，则对 $d>2g-2$，$\mathcal{F}$ 到 $\operatorname{Bun}^d_B$ 的 $!$-限制为零。

- 证明状态：`sketch`
- 说明：原文正文写 $B H^1(X,L)$ 并称 $H^1$ 可缩，与 $d>2g-2$ 时 $H^1=0$、$H^0\neq0$ 矛盾；脚注给出 $R\Gamma(X,L)[1]$。正确写法是 $B H^0(X,L)$，见勘误卡。
- 出处：§2.1，原文 p.6

### 推论 2.1.9–2.1.11

(a) $\mathcal{F}$ 可构造且尖点，则 $D\mathcal{F}$ 尖点；(b) 尖点 $\mathcal{F}$ 对 $d>2g-2$ 到 $\operatorname{Bun}^d_B$ 的 $*$-限制为零；(c) 存在开子叠 $U_n$，任意尖点层从 $U_n$ 同时以 $!$ 与 $*$ 延拓。

- 证明状态：`cited`
- 说明：讲义把 (a)(b) 归于 Verdier 对偶与第二伴随，(c) 归于 $\mathrm{CT}$ 的消没；证明细节见 Drinfeld–Gaitsgory, Selecta Math. 22 (2016)。
- 出处：§2.1，原文 p.6–7

## 易错点

- 常数项不是 $q_*p_*$：$p^!$ 与 $p_*$ 在非光滑、非固有情形差别很大；用错会破坏与 Verdier 对偶的交换性。
- 「尖点」是对所有真抛物子群及其 Levi 商同时消没；对 $\mathrm{PGL}_2$ 只有标准 Borel，所以只看 $\mathrm{CT}_*$ 就够。
- 对 $d>2g-2$ 的消没是 $!$-限制的消没，不是 $*$-限制；后者是推论，不是定义。
- 原文 p.6 的 $B H^1(X,L)$ 与「$H^1$ 可缩」两句话不能同时成立；应以 $B H^0(X,L)$ 或 $B R\Gamma(X,L)[1]$ 理解。

## 出处

- Sam Raskin 讲授、Lin Chen 笔记《Notes for "Geometric Langlands for Projective Curves"》（2025-07-07/11，18 页），§2.1 尖点性，pp. 6, 7；`源码/sections/s02-cusp.tex:L21-L70（Definition 2.1.1/2.1.2 与 Prop 2.1.5）`
  > Definition 2.1.2. ... We say that F is cuspidal if CT_* F ≃ 0.

## 相关卡

- `raskin_glc/derivation/cuspidal-vanishing`
- `raskin_glc/concept/coefficient-functor`
- `raskin_glc/concept/pgl2-geometric-langlands`

## 核验（partial，2026-11-27）

- nLab / perverse sheaf：`partial` — 反常层是可构造有界导出范畴的 abelian 子范畴；这支撑卡中「$\mathcal{F}$ 为可构造层」与尖点性在 $\operatorname{Shv}$ 中讨论的框架，但不涉及常数项定义。

常数项函子的定义与第二伴随以原文和 Drinfeld–Gaitsgory 为准；nLab 只提供反常层框架。
