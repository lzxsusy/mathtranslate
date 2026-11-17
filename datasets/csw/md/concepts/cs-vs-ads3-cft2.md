---
id: csw/concept/cs-vs-ads3-cft2
type: concept
track: H
---

# CS/WZW 与 AdS₃/CFT₂：两码事

> CS/WZW 是“态空间等同”（拓扑理论，无引力子）；AdS₃/CFT₂ 是“动力学等价”（体引力 + 边界 CFT + 全息字典）。两者不是同一种对偶。

**问题**：为什么不能说“CS/WZW 就是全息”？它们的接触点在哪里、边界在哪里？

## 定义

CS/WZW：三维 CS 在 $\Sigma\times\mathbb{R}$ 上的态空间 = 二维 WZW 的共形块空间；三维理论无度规、无局域自由度，配分函数是拓扑不变量。AdS₃/CFT₂：三维量子引力（含度规，渐近 AdS₃）与边界二维 CFT 的动力学等价，有引力子、BTZ 黑洞、全息字典（体场↔边界算子）。

*记号*：$c_{CS}=k\dim G/(k+h^\vee)$ 由 $k$ 离散决定；$c_{AdS}=3l/2G$ 连续。

## 要点

- 维度相同（3d/2d），结构完全不同：一个是拓扑态空间，一个是动力学对偶。
- CS 无引力子（无度规自由度）；AdS₃ 有引力子与 BTZ 黑洞。
- 中心荷来源不同：CS 的 $c$ 由 level $k$（整数）给出；AdS₃ 的 $c$ 由 $l/G$（连续）给出。
- 唯一接触点：三维引力可写成 CS（非紧群 $ISO(2,1)$ 或 $SL(2,\mathbb{R})\times SL(2,\mathbb{R})$），但这是经典相空间层面的改写，不是本文的结论。
- 原文没有 AdS、没有“全息”字样；AdS/CFT 是 1997 年后的事。

## 关键公式

- $c_{CS}=\frac{k\dim G}{k+h^\vee}$
- $c_{AdS}=\frac{3l}{2G}$
- $Z_{CS}(X\times S^1)=\dim\mathcal{H}_X$

## 两者的区别（判据）

CS/WZW 的等同是态空间层面的对象等同，不涉及体引力；AdS₃/CFT₂ 是含引力的动力学对偶。二者不能互相推出。

**证明要点**（sketch）：

1. CS 作用量不含度规，理论无引力子；AdS₃ 的体理论含度规与引力子。 *（这是定义层面的差别。）*
2. CS 的中心荷由离散 level 给出；AdS₃ 的中心荷连续。 *（$c_{CS}=k\dim G/(k+h^\vee)$ vs $c=3l/2G$。）*
3. CS 的“边界”只是态空间的载体，没有边界动力学；AdS 的边界有完整的 CFT 动力学。 *（全息字典要求体场与边界算子对应。）*

> **缺口**：“3d 引力=CS”的精确层级（经典/量子、渐进边界条件）需要额外讨论，超出本文。

## 陷阱

- 不要写“Witten 1989 预言了全息”：原文无此内容，1988 年也没有 AdS/CFT。
- 不要把 $c_{CS}$ 与 $c_{AdS}$ 的数值相等当成对偶证据：它们来源不同。
- “3d 引力 = CS”只在特定群与边界条件下成立，不是普遍等同。

## 相关卡片

- [cs-wzw-duality](../concepts/cs-wzw-duality.md)
- [conformal-blocks](../concepts/conformal-blocks.md)
- [mapping-class-group](../concepts/mapping-class-group.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§5 Applications to Physics（p.396–397），印刷页 [396, 397] / PDF 页 [46, 47]（witten1989/sections/s09-applications.tex（§5））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
