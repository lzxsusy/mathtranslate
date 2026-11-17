---
id: csw/concept/puncture-gauss-law
type: concept
track: D
---

# 穿刺点上的高斯定律

> 在标记点 $P_s$ 处，高斯定律的右端多出算符值源 $T^a_{(s)}$：$(k/8\pi)\varepsilon^{ij}F^a_{ij}(x)=\sum_s\delta^2(x-P_s)T^a_{(s)}$。

**问题**：为什么这个约束不能像普通高斯定律那样“解出”经典联络？

## 定义

把 Wilson 线穿过 $\Sigma$ 的交点看成标记点 $P_s$。对沿 $\Sigma$ 的变分，作用量的边界项要求约束为 $(k/8\pi)\varepsilon^{ij}F^a_{ij}(x)=\sum_s\delta^2(x-P_s)T^a_{(s)}$，其中 $T^a_{(s)}$ 是表示 $R_s$ 的生成元，作用在 $P_s$ 处的态空间上。

*记号*：$T^a_{(s)}$ 是第 $s$ 个标记点上表示 $R_s$ 的生成元；$\varepsilon^{ij}F_{ij}$ 在二维只有一个独立分量。

## 要点

- 没有标记点时右端为零，约束就是 $F=0$；有标记点时右端是 $\delta$ 函数源，联络在 $P_s$ 处有奇点。
- 右端是算符值：$T^a_{(s)}$ 互相不对易，约束是量子约束而不是经典方程。
- 直接把它当经典方程解，得到的“联络”依赖表示的选取，不是普通联络。
- Witten 的替代方案：不“解”约束，而是把表示 $R_s$ 本身量子化（Borel–Weil–Bott），把相空间扩大。
- 这个约束与共形场论中“插入顶点算子”的 Ward 恒等式是同一件事。

## 关键公式

- $(k/8\pi)\varepsilon^{ij}F^a_{ij}(x)=\sum_s\delta^2(x-P_s)T^a_{(s)}$
- $F=0$（无标记点时）

## 约束的算符性

带标记点时的高斯定律右端是算符值分布，因此不能在经典层面解出联络；把它当作经典方程会得到依赖表示且非单值的“联络”。

**证明要点**（sketch）：

1. 对 $\Sigma$ 上的变分，作用量的边界项给出 $(k/8\pi)\varepsilon^{ij}F^a_{ij}=\sum_s\delta^2T^a_{(s)}$。 *（边界项来自 Wilson 线在交点处的变分。）*
2. $T^a_{(s)}$ 是表示 $R_s$ 的生成元，彼此不对易（非阿贝尔）。 *（右端是算符，不是 $c$-数。）*
3. 故约束是量子约束；经典解的尝试会得到“q-数联络”，即量子群的萌芽。 *（Witten 明确说这条路只给出量子群，不作构造。）*

> **缺口**：本文没有把“量子群”路线做完；Borel–Weil–Bott 是替代路线。

## 陷阱

- 不要把 $\delta^2$ 源当成普通点电荷：它的“荷”是算符，不是数。
- 约束的奇点意味着平坦性只在 $\Sigma\setminus\{P_s\}$ 上成立，模空间是“带奇点的平坦联络模空间”。
- 标记点位置不能随便移动：移动会改变约束的解空间（除非同时做规范变换）。

## 相关卡片

- [gauss-law-constraint](../concepts/gauss-law-constraint.md)
- [borel-weil-bott](../concepts/borel-weil-bott.md)
- [conformal-blocks](../concepts/conformal-blocks.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.3 Incorporation of Wilson Lines，印刷页 [371, 373] / PDF 页 [21, 23]（witten1989/sections/s05-hilbert.tex（§3.3））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
