---
id: csw/concept/flat-connection-moduli
type: concept
track: B
---

# 平坦联络模空间

> CS 的物理相空间是 $\Sigma$ 上平坦联络模去规范变换，即 $\operatorname{Hom}(\pi_1\Sigma,G)/G$；$g>1$ 时实维数 $(2g-2)d$。

**问题**：为什么相空间是“表示模共轭”而不是“联络空间本身”？维数公式怎么来的？

## 定义

设 $\Sigma$ 是亏格 $g$ 的紧致定向曲面。平坦 $G$-联络由和乐表示 $\rho:\pi_1\Sigma\to G$ 决定，模去规范变换即模去共轭，故 $M=\operatorname{Hom}(\pi_1\Sigma,G)/G$。选复结构 $J$ 后，$M$ 又是 $\Sigma$ 上 degree $0$ 稳定全纯 $G_{\mathbb{C}}$-丛的模空间 $M_J$。

*记号*：$d=\dim G$；$g$ 是 $\Sigma$ 的亏格；$M$ 常记为 $M_{\mathrm{flat}}$，带复结构时记 $M_J$。

## 要点

- 平坦联络的局部数据被 $\pi_1$ 的表示完全决定：沿每条闭链取和乐，得到群同态。
- 模去规范变换 = 模去共轭：换个起点或换规范，表示被共轭。
- 维数：$\dim\operatorname{Hom}(\pi_1\Sigma,G)=d+2g(d-\frac12 d)$ 减去 $\dim G$ 的共轭，得 $(2g-2)d$（$g>1$）。
- $g=1$ 时公式给 0，但模空间不是点：$SU(2)$ 时是枕头套 $T^2/\{\pm1\}$（实维 2）；公式只对 $g\ge2$ 的一般位置成立。
- 紧致但不光滑：可约联络处有奇点，商是轨形；辛形式在光滑部分非退化。

## 关键公式

- $M=\operatorname{Hom}(\pi_1\Sigma,G)/G$
- $\dim_{\mathbb{R}}M=(2g-2)d\quad(g\ge2)$
- $g=1,\ G=SU(2):\ M\cong T^2/\{\pm1\}$

## 维数公式

对 $g\ge2$ 与单连通紧单群 $G$，$M=\operatorname{Hom}(\pi_1\Sigma,G)/G$ 在光滑点的实维数为 $(2g-2)d$。

**证明要点**（sketch）：

1. $\pi_1\Sigma$ 有 $2g$ 个生成元与 1 个关系，$\operatorname{Hom}$ 是 $G^{2g}$ 中被一个方程截出的子簇。 *（表示由生成元的像决定，关系给一个矩阵方程。）*
2. 方程 $\prod[A_i,B_i]=1$ 的微分在光滑点满秩，故 $\dim=d(2g-1)$。 *（满秩性等价于表示不可约（稳定化子中心化子最小）。）*
3. 再模去 $G$ 的共轭作用（$\dim G=d$），得 $d(2g-1)-d=(2g-2)d$。 *（自由作用在不可约表示上成立。）*

> **缺口**：公式只在 $g\ge2$ 的一般位置成立；$g=1$ 的枕头套与 $g=0$ 的单点是例外，需单独算。

## 陷阱

- 不要把 $g=1$ 代入 $(2g-2)d$ 得 0 就以为模空间是点：$g=1$ 时方程 $[A,B]=1$ 的微分不满秩，公式失效。
- 模空间不是流形而是轨形，可约联络（如 $G$ 的中心）处有奇点；辛商要改用相交上同调。
- 复结构 $J$ 改变的是复结构，不改变辛形式（Kähler 形式随 $J$ 变，但上同调类不变）。

## 相关卡片

- [gauss-law-constraint](../concepts/gauss-law-constraint.md)
- [narasimhan-seshadri](../concepts/narasimhan-seshadri.md)
- [holomorphic-sections](../concepts/holomorphic-sections.md)
- [pillowcase-dimension](../examples/pillowcase-dimension.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3 相空间与模空间，印刷页 [366, 368] / PDF 页 [16, 18]（witten1989/sections/s04-canonical.tex §3.1）

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
