---
id: csw/concept/holomorphic-sections
type: concept
track: C
---

# 全纯截面空间作为量子 Hilbert 空间

> CS 的量子 Hilbert 空间是 $\cH_\Sigma=H^0(\cM_J,\cL^{\otimes k})$：模空间上的全纯截面空间，有限维。

**问题**：$H^0(\cM_J,\cL^{\otimes k})$ 的维数由什么决定？为什么它随 $J$ 变而物理上不该变？

## 定义

取 $M=\Sigma\times\mathbb{R}$，相空间 $\cM_J$ 是复结构 $J$ 下的稳定丛模空间，预量子化线丛 $\cL^{\otimes k}$。则量子 Hilbert 空间 $\cH_\Sigma=H^0(\cM_J,\cL^{\otimes k})$，即全纯截面空间。大 $k$（半经典）时 $\dim\cH_\Sigma\sim\frac{\operatorname{Vol}(\cM)}{(2\pi)^n n!}k^n$（Weyl 律）。

*记号*：$\cM_J$ 与 $J$ 有关；$\cH_\Sigma$ 严格说是一个射影平坦丛的纤维，随 $J$ 变动。

## 要点

- 全纯截面空间有限维：$\cM_J$ 紧、$\cL$ 正，$H^0$ 是椭圆复形的核。
- 维数由 Riemann–Roch（指标定理）给出；对 $S^2$ 带三个标记点，$\dim=N_{ijk}$（Verlinde 公式）。
- 随 $J$ 变，$H^0(\cM_J,\cL^{\otimes k})$ 构成 Teichmüller 空间上的向量丛，只带射影平坦联络。
- 半形式修正把 $\cL^{\otimes k}$ 换成 $\cL^{\otimes k}\otimes K^{1/2}$，维数从 $k$ 变成 $k+1$（$SU(2)$、环面）。
- 这就是“量子化后的模空间”与“WZW 共形块”能比较的公共语言：两边都是全纯截面。

## 关键公式

- $\cH_\Sigma=H^0(\cM_J,\cL^{\otimes k})$
- $\dim\cH_\Sigma\sim\frac{\operatorname{Vol}(\cM_J)}{(2\pi)^n n!}k^n\ (k\to\infty)$
- $S^2,\ 3\text{ 个标记点}:\ \dim=N_{ijk}$

## 有限维性

$\cM_J$ 紧致且 $\cL$ 正时，$H^0(\cM_J,\cL^{\otimes k})$ 是有限维复向量空间。

**证明要点**（sketch）：

1. 全纯截面满足椭圆方程 $\bar\partial s=0$。 *（$\bar\partial$ 的主符号在 Kähler 流形上是椭圆复形。）*
2. 紧流形上椭圆复形的核有限维（Hodge 理论）。 *（这是标准结果，不需要额外的分析。）*
3. 故 $\dim H^0<\infty$。 *（结论直接。）*

> **缺口**：紧致性在可约联络奇点处失效；本文用“紧化/相交上同调”回避，未展开。

## 陷阱

- 不要忘记 $k$：$H^0(\cM_J,\cL)$ 与 $H^0(\cM_J,\cL^{\otimes k})$ 是不同空间，后者才对应 level $k$。
- 维数不是常数函数：它是 $J$ 的（射影）平坦丛的纤维维数，局部常数但整体有单值性。
- 大 $k$ 的 Weyl 律只给首项，不能用来算有限 $k$ 的整数维数。

## 相关卡片

- [polarization](../concepts/polarization.md)
- [prequantization-determinant-line](../concepts/prequantization-determinant-line.md)
- [projective-flat-connection](../concepts/projective-flat-connection.md)
- [verlinde-formula](../concepts/verlinde-formula.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.1–3.2 全纯截面与射影平坦丛，印刷页 [368, 370] / PDF 页 [18, 20]（witten1989/sections/s04-canonical.tex（§3.1–3.2））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
