---
id: csw/concept/cs-action
type: concept
track: A
---

# Chern–Simons 作用量

> 在三维流形上积一个 3-形式 $\operatorname{Tr}(A\wedge dA+\frac23A^3)$：只依赖定向、不依赖度规，变分给出 $F=0$。

**问题**：为什么不能直接用 Yang–Mills 作用量？CS 作用量对联络的变分为什么是 $\int\operatorname{Tr}(\delta A\wedge F)$？

## 定义

设 $M$ 是紧致定向三维流形，$A$ 是 $G$-联络（Lie 代数值 1-形式），$F=dA+A\wedge A$。Chern–Simons 作用量定义为 $L=\frac{k}{4\pi}\int_M\operatorname{Tr}\left(A\wedge dA+\frac{2}{3}A\wedge A\wedge A\right)$，其中 $\operatorname{Tr}$ 取 $G$ 的某个表示上的迹，$k$ 是耦合常数。

*记号*：$\operatorname{Tr}$ 的归一化必须固定：本文取基本表示、长根平方 $=2$，此时 $k\in\mathbb{Z}$；换表示或换 Killing 型，$k$ 要跟着换算。

## 要点

- Yang–Mills 作用量 $\int\sqrt g\,g^{ik}g^{jl}\operatorname{Tr}(F_{ij}F_{kl})$ 有两处度规依赖：体积元 $\sqrt g\,d^3x$ 与指标缩并 $g^{ik}g^{jl}$；前者可以靠“不积分体积”绕过，后者绕不过。
- CS 项是 3-形式在 3-流形上的积分，只需要定向，因此天然是“拓扑场论”的作用量。
- 变分时 $\delta(A\wedge dA)=\delta A\wedge dA+A\wedge d\delta A$，第二项分部积分并用 $dA=-\frac12[A,A]$ 变成 $A\wedge[\delta A,A]$，三段合并为 $2\operatorname{Tr}(\delta A\wedge F)$。
- 驻点条件 $F=0$：三维 CS 理论的经典解是平坦联络，这正是相空间是平坦联络模空间的来源。
- 三维 CS 不是“有质量矢量”的理论：它没有局域自由度，只有拓扑自由度；这才使 Hilbert 空间有限维。

## 关键公式

- $L=\frac{k}{4\pi}\int_M\operatorname{Tr}(A\wedge dA+\tfrac23A\wedge A\wedge A)$
- $F=dA+A\wedge A$
- $\delta L=\frac{k}{2\pi}\int_M\operatorname{Tr}(\delta A\wedge F)$
- $F=0\iff A$ 平坦

## 变分公式

对任意变分 $\delta A$（在边界上为零），$\delta L=\frac{k}{2\pi}\int_M\operatorname{Tr}(\delta A\wedge F)$。

**证明**：

1. 展开 $\delta L=\frac{k}{4\pi}\int\operatorname{Tr}(\delta A\wedge dA+A\wedge d\delta A+2\delta A\wedge A\wedge A)$。 *（把 $\delta(A\wedge A\wedge A)$ 的三项都写出来，再合并。）*
2. 对第二项分部积分：$\int\operatorname{Tr}(A\wedge d\delta A)=-\int\operatorname{Tr}(dA\wedge\delta A)$，边界项因 $\delta A|_{\partial M}=0$ 消失。 *（分部积分给出的负号被 $\delta A$ 与 $A$ 的交换子吸收。）*
3. 用 $dA=F-A\wedge A$，把 $-\operatorname{Tr}(dA\wedge\delta A)+2\operatorname{Tr}(\delta A\wedge A\wedge A)$ 合并成 $2\operatorname{Tr}(\delta A\wedge F)$，再乘 $\frac{k}{4\pi}$ 得 $\frac{k}{2\pi}\int\operatorname{Tr}(\delta A\wedge F)$。 *（关键是 $\operatorname{Tr}(A\wedge A\wedge\delta A)$ 与 $\operatorname{Tr}(\delta A\wedge A\wedge A)$ 只差循环置换，正好补上 $-\operatorname{Tr}(A\wedge A\wedge\delta A)$。）*

## 陷阱

- 系数 $1/4\pi$ 与 $\frac23$ 依赖 $\operatorname{Tr}$ 的归一化；河野书用 $\frac{1}{8\pi^2}\int\operatorname{Tr}(A\wedge dA+\frac23A^3)$，与本文差一个常数因子 $2\pi k$。
- 不要给 CS 作用量补一个 $\sqrt g$：那会破坏拓扑不变性。
- $\int A\wedge dA$ 在规范变换下变一个边界项，这是下一张卡（level-quantization）的入口。

## 相关卡片

- [level-quantization](../concepts/level-quantization.md)
- [gauss-law-constraint](../concepts/gauss-law-constraint.md)
- [wilson-line](../concepts/wilson-line.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§1 The Chern–Simons Action，印刷页 [353, 354] / PDF 页 [3, 4]（witten1989/sections/s01-cs-action.tex §1）

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
