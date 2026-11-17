---
id: csw/concept/narasimhan-seshadri
type: concept
track: B
---

# Narasimhan–Seshadri：平坦联络与稳定全纯丛

> degree 0 的稳定全纯 $G_{\mathbb{C}}$-丛与不可约平坦酉联络一一对应；它把 $M$ 变成 Kähler 模空间，从而可以谈“全纯截面”。

**问题**：一个平坦联络为什么等价于一整个全纯结构？这个对应为什么是几何量子化能进行的前提？

## 定义

设 $E$ 是 $\Sigma$ 上 degree $0$ 的稳定全纯 $G_{\mathbb{C}}$-丛。Narasimhan–Seshadri 定理断言：$E$ 上存在唯一的与全纯结构相容的平坦酉联络，反之不可约平坦酉联络给出唯一的稳定全纯结构。于是 $M_{\mathrm{flat}}\cong M_{\mathrm{Dol}}$（稳定丛模空间），后者是复 Kähler 流形。

*记号*：$G_{\mathbb{C}}$ 是 $G$ 的复化；Dolbeault 模空间 $M_{\mathrm{Dol}}$ 与平坦联络模空间 $M_{\mathrm{dR}}$ 通过非阿贝尔 Hodge 对应等同。

## 要点

- 平坦联络 = 全纯结构 + 相容的平坦酉结构；前者是复几何数据，后者是度量数据。
- “稳定”是 GIT 意义下的稳定性，等价于联络不可约；可约联络对应不稳定/半稳定点。
- 因此 $M$ 上有两个身份：辛流形（平坦联络）与 Kähler 流形（稳定丛）；量子化用后者。
- Kähler 形式 $\omega$ 的上同调类与预量子化线丛的 $c_1$ 一致，这是“$k$ 出现在线丛次数上”的来源。
- 该定理是 Donaldson–Uhlenbeck–Yau 定理的二维情形；对 $G=U(N)$ 它就是说“平坦酉联络 ↔ 稳定全纯向量丛”。

## 关键公式

- $M_{\mathrm{flat}}\cong M_{\mathrm{Dol}}$
- $\omega_{\mathrm{Kähler}}\in H^{1,1}(M)$

## Narasimhan–Seshadri 对应

在亏格 $g\ge2$ 的紧 Riemann 面上，degree $0$ 稳定全纯 $G_{\mathbb{C}}$-丛的模空间与不可约平坦 $G$-联络的模空间典范同构，且前者是 Kähler 流形。

**证明要点**（sketch）：

1. 从平坦联络取 $(0,1)$-部分，得全纯结构；联络的平坦性保证 $\bar\partial^2=0$。 *（$D''=\bar\partial+A''$，$F=0$ 给出 $\bar\partial A''+A''\wedge A''=0$。）*
2. 联络的酉性给出 Hermite 度量，且该度量满足 Hermite–Yang–Mills 方程（$\Sigma$ 上自动成立）。 *（二维时 HYM 方程就是度量的相容条件，没有更高阶障碍。）*
3. 反过来，稳定丛上的 HYM 度量给出唯一平坦酉联络（Donaldson–Uhlenbeck–Yau 的二维情形）。 *（高维用 UY 定理，二维是经典结果。）*

> **缺口**：本文只引用不证明；可约（不稳定）情形的边界与抛物结构未展开。

## 陷阱

- 不要把它读成“平坦联络就是全纯丛”：还要 degree 0 与稳定性，且对应是模空间层面的。
- 模空间在可约点有奇点，对应不稳定丛；量子化时要取相交上同调或抛物丛。
- Kähler 形式随复结构变，但上同调类不变；这是“Hilbert 空间与 $J$ 无关”的几何基础。

## 相关卡片

- [flat-connection-moduli](../concepts/flat-connection-moduli.md)
- [holomorphic-sections](../concepts/holomorphic-sections.md)
- [prequantization-determinant-line](../concepts/prequantization-determinant-line.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.1–3.2 全纯观点与平坦丛，印刷页 [368, 369] / PDF 页 [18, 19]（witten1989/sections/s04-canonical.tex（§3.1 末–§3.2））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
