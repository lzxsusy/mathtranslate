# 非单连通群的 n_g 修正与 Table 1

> `kw/deriv/table1-and-ng` · 轨道 A · 四维物理与对偶 · 状态 dev · 4 步

> **要回答的问题**：Table 1 的对偶群里，为什么 $\mathrm{Sp}(k)\leftrightarrow\mathrm{Spin}(2k+1)$ 需要 $n_g=2$ 的修正，而 $G_2$、$E_8$ 不需要？

## 一句话

从 Table 1 的七行对偶出发，说明 $n_g$ 只在 $\mathrm{Sp}(k)\leftrightarrow\mathrm{Spin}(2k+1)$ 这类李代数不同构的群对上出现，并由 $\tau$ 的归一化定出 $n_g=2$（$F_4$）与 $n_g=3$（$G_2$）。

## 目标

解释 Table 1 各行的来源，并说明 $n_g$ 何时出现、取何值。

## 前提

- GNO：电荷取权格、磁荷取对偶群权格，见 `B p.2`。
- Table 1 的七行对偶群表，见 `B p.3`。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 逐行读出 Table 1：$\mathrm{U}(N)\leftrightarrow\mathrm{U}(N)$、$\mathrm{SU}(N)\leftrightarrow\mathrm{PSU}(N)$、$\mathrm{Spin}(2n)\leftrightarrow\mathrm{SO}(2n)/\mathbb Z_2$、$\mathrm{Sp}(n)\leftrightarrow\mathrm{SO}(2n+1)$、$\mathrm{Spin}(2n+1)\leftrightarrow\mathrm{Sp}(n)/\mathbb Z_2$、$G_2$ 与 $E_8$ 自对偶。这些群对的根格与余根格互换，是 GNO 荷格规则的逐群实现。 | 先把表读全，才能看出哪些行两边李代数同构、哪些不同构；后者才是 $n_g$ 的来源。 | `B p.3` | A·原文明确写了 |
| 2 | $n_g$ 只在李代数不同构的群对上出现：$\mathrm{Sp}(k)$ 与 $\mathrm{Spin}(2k+1)$ 是唯二这样的单群对，因为 YM 作用量与 $\tau$ 只依赖李代数，所以必须分别设 $\tau$ 与 $\tau'$ 再比较。 | 若两边李代数同构，可直接用同一个 $\tau$；不同构时直接比较会把归一化因子误当成物理效应。 | `B p.12` | A·原文明确写了 |
| 3 | 归一化使 $T$ 为 $\tau\to\tau+1$、$\tau'\to\tau'+1$，则 $S$ 作用为 $\tau=-1/(2\tau')$、$\tau'=-1/(2\tau)$，与 $F_4$ 的 $n_g=2$ 同型。换成 $\tilde\tau=2\tau$ 可消去因子，但此时 $T:\tilde\tau\to\tilde\tau+2$。 | 这一步说明 $n_g$ 不是物理常数，而是 $S$ 与 $T$ 的相对归一化；换归一化会把它移到 $T$ 上。 | `B p.12` | A·原文明确写了 |
| 4 | $n_g$ 的完整取值：单边（单连通）为 $1$，$F_4$ 为 $2$，$G_2$ 为 $3$；后两者的对偶群不是 $\mathrm{SL}(2,\mathbb Z)$ 而是 Hecke 群。 | 若不区分单边与非单边，就会把 $S:\tau\mapsto-1/\tau$ 错用到所有群上，导致 Table 1 中 $G_2$、$F_4$ 两行无法自洽。 | `B p.12` | A·原文明确写了 |

## 结论

Table 1 的每一行都由 GNO 荷格配对给出；$n_g$ 修正只在李代数不同构的群对上出现，归一化后统一为 $n_g=2$（含 $F_4$），$G_2$ 为 $3$。基本几何 Langlands 对偶只用 $\Psi=0$ 与 $\Psi=\infty$，$n_g$ 在其中不起作用；但 §11 的精确对偶群需要它。

## 缺口

- 原文明说非单连通情形的完整故事还要特征类 $\xi\in H^2(M,\pi_1(G))$，本文不做，留给 §7。

## 最容易讲错的地方

- 把 $n_g$ 当成群的中心阶数：对 $G_2$、$F_4$ 它来自对偶群的 Hecke 结构，而不是有限中心。
- 在 $\mathrm{Sp}(k)$ 与 $\mathrm{Spin}(2k+1)$ 之间直接比较 $\tau$ 而不重新归一化，会把因子 $2$ 误当成物理效应。

## 相关卡

[GNO 对偶群](../concepts/gno-dual-group.md) · [Langlands 对偶群](../concepts/langlands-dual-group.md) · [从 GNO 对偶群到 Langlands 对偶群](../derivations/gno-to-langlands.md) · [S-对偶生成元、SL(2,Z) 与超荷的双覆盖](../derivations/sdual-sl2z.md)

## 出处（印刷页）

- B p.3–12（B p.12）

> 说明：A4：Table 1、$\mathrm{Sp}/\mathrm{Spin}$ 的特殊性、$n_g=2$ 的归一化论证与取值均在 `B p.3–12` 明写；最没把握处是「$n_g=2$ 同时覆盖 $\mathrm{Sp}/\mathrm{Spin}$ 与 $F_4$」的表述边界。
