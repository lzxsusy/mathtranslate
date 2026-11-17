---
id: csw/concept/wzw-action
type: concept
track: E
---

# Wess–Zumino–Witten 作用量与 level

> $S_{WZW}=S_\sigma+k\Gamma$：动能项 $S_\sigma$ 与拓扑项 $\Gamma$（Wess–Zumino 项）；$e^{iS}$ 单值要求 $k\in\mathbb{Z}$。

**问题**：WZ 项为什么只有在 $k$ 整数时才有定义？它为什么是拓扑项？

## 定义

设 $g:\Sigma\to G$ 是场。$S_{WZW}[g]=S_\sigma[g]+k\Gamma[g]$，其中 $S_\sigma=\frac1{8\pi}\int_\Sigma\operatorname{Tr}(g^{-1}\partial_ig\,g^{-1}\partial^ig)$，$\Gamma=\frac1{24\pi^2}\int_B\operatorname{Tr}(g^{-1}dg)^3$（$B$ 是 $\Sigma$ 的三维延拓）。$\Gamma$ 在 $g$ 的延拓改变时平移 $2\pi i\mathbb{Z}$ 的整数倍，故 $e^{iS}$ 单值要求 $k\in\mathbb{Z}$。

*记号*：$g$ 取值于紧单群 $G$；$\Gamma$ 是 WZ 项；$k$ 是 level（整数）。

## 要点

- $\Gamma$ 是三维的，虽然理论是二维的：它只依赖 $g$ 在三维延拓上的值（拓扑项）。
- 延拓不唯一，但改变延拓只改变 $\Gamma$ 的 $2\pi i$ 整数倍，因此 $e^{ik\Gamma}$ 只需 $k\in\mathbb{Z}$。
- 这与 CS 的 $k\in\mathbb{Z}$ 是同一件事的两面：三维拓扑项的边界就是二维的 WZ 项。
- WZW 是“有质量”的二维理论，但有共形对称性；其中心荷 $c=k\dim G/(k+h^\vee)$。
- CS 与 WZW 的关系不只是“边界”：CS 在 $\Sigma\times\mathbb{R}$ 上的态空间就是 WZW 的共形块空间。

## 关键公式

- $S_{WZW}=S_\sigma+k\Gamma$
- $\Gamma=\frac1{24\pi^2}\int_B\operatorname{Tr}(g^{-1}dg)^3$
- $c=\frac{k\dim G}{k+h^\vee}$

## WZ 项的整性

$\Gamma$ 在两个延拓上的差为 $2\pi i$ 的整数倍；因此 $e^{ik\Gamma}$ 逐点定义当且仅当 $k\in\mathbb{Z}$。

**证明要点**（sketch）：

1. 两个三维延拓 $B_1,B_2$ 拼成闭三维流形，$\int_{B_1}-\int_{B_2}$ 是整周期。 *（$(g^{-1}dg)^3$ 是闭形式，其周期整。）*
2. 周期为 $2\pi i\mathbb{Z}$ 倍（归一化后）。 *（这是 Wess–Zumino 项的标准计算。）*
3. 故 $e^{ik\Gamma}$ 单值 iff $k\in\mathbb{Z}$。 *（$k$ 整数才能吸收相位。）*

> **缺口**：本文把 WZ 项当作已知背景；推导在 Witten 1984 与河野 §1.3。

## 陷阱

- 不要把 $S_\sigma$ 与 $\Gamma$ 的归一化混用：不同书的 $k$ 归一化差因子 2，比较前先对齐。
- WZW 的 level $k$ 与 CS 的 level $k$ 相等，但 $SU(2)$ 的有效 level 是 $k+2$（半形式修正）。
- $\Gamma$ 不是“边界项”，它是三维延拓上的积分；二维理论里它只是记号。

## 相关卡片

- [cs-action](../concepts/cs-action.md)
- [level-quantization](../concepts/level-quantization.md)
- [affine-lie-algebra](../concepts/affine-lie-algebra.md)
- [sugawara-construction](../concepts/sugawara-construction.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§1（WZ 项与 k 整性）、§3–4，印刷页 [354, 396] / PDF 页 [4, 46]（witten1989/sections/s01-cs-action.tex（(1.4)））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
