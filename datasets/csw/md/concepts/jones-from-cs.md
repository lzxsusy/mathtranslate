---
id: csw/concept/jones-from-cs
type: concept
track: G
---

# Jones 多项式从 CS 来

> $S^3$ 上沿链环 $L$ 的 Wilson 线期望值 $\langle\prod W_{R_i}(K_i)\rangle$ 在 $G=SU(N)$ 定义表示时给出两变量 Jones 多项式（变量 $N$ 与 $k$）。

**问题**：为什么 CS 的 Wilson 线期望值等于 Jones 多项式？$q$ 是怎么从 $k$ 来的？

## 定义

取 $M=S^3$，链环 $L$ 的各分量取 $SU(N)$ 的定义表示，Wilson 线期望值 $Z(S^3;L)=\langle\prod_iW_{R_i}(K_i)\rangle$ 等于 Jones 多项式的两变量推广（变量为 $N$ 与 $q$，$q=e^{2\pi i/(N+k)}$）。取 $N=2$ 得经典 Jones 多项式。

*记号*：$q=e^{2\pi i/(N+k)}$（有效 level）；$R$ 为定义表示；$K_i$ 为链环分量。

## 要点

- 纽结不变量 = 拓扑量子场论的 Wilson 线期望值：这是本文的中心论断。
- $q$ 来自 $k$ 与 $N$：$q=e^{2\pi i/(N+k)}$；$q\to1$ 对应 $k\to\infty$（半经典）。
- 拆接关系与 Kauffman bracket 是同一结构的组合影子；CS 给了它三维解释。
- 推广到任意三维流形需要手术公式（不是每个流形都嵌入 $S^3$）。
- Kauffman 多项式对应 $SO(N)$ 与 $N$ 维表示。

## 关键公式

- $Z(S^3;L)=\langle\prod_iW_{R_i}(K_i)\rangle$
- $q=e^{2\pi i/(N+k)}$
- $V_L(t)=Z(S^3;L)|_{N=2,\ t=q}$

## CS 与 Jones

对 $SU(N)$ 与定义表示，CS 在 $S^3$ 上的 Wilson 线期望值是 Jones 多项式的两变量推广；$N=2$ 给出经典 Jones 多项式。

**证明要点**（sketch）：

1. 用正则量子化把 $S^3$ 上的链环期望值化为手术/共形块计算。 *（把 $S^3$ 看成 $S^2\times S^1$ 的手术或辫闭合。）*
2. 共形块的三点函数由 $S$ 矩阵给出（Verlinde）。 *（链环的每个交叉对应融合系数。）*
3. 整理得 $q=e^{2\pi i/(N+k)}$ 的 Jones 多项式。 *（$q$ 由有效 level 给出。）*

> **缺口**：本文给出的是物理推导与若干例子，未给完整的组合证明；严格化见 RT 与后续文献。

## 陷阱

- 不要把 $q$ 写成 $e^{2\pi i/k}$：$SU(N)$ 的分母是 $N+k$，$SU(2)$ 是 $k+2$。
- 不同文献的 Jones 变量 $t$ 与 $q$ 差符号/幂次，比较前对齐。
- Wilson 线要有标架（ribbon），否则链环不变量不完整。

## 相关卡片

- [wilson-line](../concepts/wilson-line.md)
- [s-matrix](../concepts/s-matrix.md)
- [surgery-formula](../concepts/surgery-formula.md)
- [trefoil-jones](../examples/trefoil-jones.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§1（(1.6)）与 §4.6（p.394），印刷页 [356, 394] / PDF 页 [6, 44]（witten1989/sections/s01-cs-action.tex（(1.6)））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
