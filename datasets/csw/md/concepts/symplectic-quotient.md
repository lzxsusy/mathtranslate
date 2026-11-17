---
id: csw/concept/symplectic-quotient
type: concept
track: B
---

# 辛商（Marsden–Weinstein 约化）

> 相空间 $P$ 带第一类约束时，物理相空间是约束面 $\mu^{-1}(0)$ 模掉约束生成的群作用，辛形式自动下降。

**问题**：为什么“先限制到约束面再取商”能得到一个辛流形？辛形式为什么能下降？

## 定义

设 $(P,\omega)$ 是辛流形，紧 Lie 群 $K$ 通过辛作用作用于 $P$，矩映射 $\mu:P\to\mathfrak{k}^*$。若 $0$ 是正则值且 $K$ 在 $\mu^{-1}(0)$ 上自由作用，则辛商 $P/\!/K:=\mu^{-1}(0)/K$ 是辛流形，其辛形式 $\omega_{\mathrm{red}}$ 由 $\omega$ 拉回后在商上良定义。

*记号*：$\mu^{-1}(0)$ 是约束面；$K$ 是规范群；$\mathfrak{k}$ 是它的 Lie 代数。

## 要点

- 两步：先解约束（限制到 $\mu^{-1}(0)$），再按规范群取商；顺序不能反。
- 辛形式能下降，是因为 $\omega$ 在约束面上拉回后沿群轨道为零（矩映射的性质），而沿轨道方向的内积由 $d\mu$ 控制。
- 在 CS 里，$P$ 是 $\Sigma$ 上所有联络的空间，$K$ 是规范群，$\mu=0$ 就是 $F=0$ 的弱形式。
- 商空间可能有奇点：可约联络处稳定化子非平凡，商是轨形而非流形。
- 辛商与“先固定规范再解约束”给出同一个相空间，但辛商的构造是无歧义的。

## 关键公式

- $\mu:P\to\mathfrak{k}^*,\quad d\langle\mu,X\rangle=\iota_{X^\#}\omega$
- $P/\!/K=\mu^{-1}(0)/K$
- $\omega_{\mathrm{red}}=\iota^*\omega$ 的商下降

## 辛商定理（Marsden–Weinstein）

在 $K$ 自由作用、$0$ 为正则值的假设下，$\mu^{-1}(0)/K$ 是辛流形，$\iota^*\omega$ 下降到其上。

**证明要点**（sketch）：

1. $\mu^{-1}(0)$ 是余维 $\dim K$ 的子流形（$0$ 正则值）。 *（正则值定理。）*
2. 群轨道切于 $\mu^{-1}(0)$ 且在 $\omega$ 下迷向：$\iota^*\omega$ 沿轨道为零。 *（矩映射方程 $d\langle\mu,X\rangle=\iota_{X^\#}\omega$ 与 $\mu=0$ 一起给出。）*
3. 迷向且自由⇒轨道是 $\iota^*\omega$ 的核，商空间继承非退化 2-形式。 *（商流的辛形式良定义，且闭性继承。）*

> **缺口**：自由作用只在不可约联络上成立；可约联络的奇点处理（相交上同调/抛物丛）超出本文范围。

## 陷阱

- 不要先取商再解约束：商掉规范后 $F=0$ 变成非局部方程，反而更难。
- 矩映射是 $\mathfrak{k}^*$ 值；对非阿贝尔群，$\mu=0$ 是向量方程，分量个数是 $\dim G$。
- 商空间在可约联络处是轨形，维数公式 $(2g-2)d$ 在一般位置成立。

## 相关卡片

- [gauss-law-constraint](../concepts/gauss-law-constraint.md)
- [flat-connection-moduli](../concepts/flat-connection-moduli.md)
- [holomorphic-sections](../concepts/holomorphic-sections.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.1 辛商与相空间，印刷页 [367, 367] / PDF 页 [17, 17]（witten1989/sections/s04-canonical.tex（式 3.3 后一段））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
