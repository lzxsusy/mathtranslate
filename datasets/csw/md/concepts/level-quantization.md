---
id: csw/concept/level-quantization
type: concept
track: A
---

# $k$ 的整性：大规范变换

> 绕数为 $m$ 的大规范变换把作用量平移 $2\pi km$；量子理论要求 $e^{iL}$ 单值，于是 $k$ 必须是整数。

**问题**：为什么 CS 的耦合常数必须量子化？充分性为什么原文只说一句？

## 定义

设 $g:M\to G$ 是规范变换，$A\mapsto A^g=g^{-1}Ag+g^{-1}dg$。当 $\pi_3(G)\cong\mathbb{Z}$ 时，$g$ 有绕数 $m=\frac{1}{24\pi^2}\int_M\operatorname{Tr}(g^{-1}dg)^3\in\mathbb{Z}$。作用量在 $A^g$ 下的平移为 $L(A^g)=L(A)+2\pi k\,m$。

*记号*：$m$ 也叫 $g$ 的度数；对 $SU(N)$，$m$ 就是映射 $M\to SU(N)$ 的拓扑度数。

## 要点

- 小规范变换（可连续形变到恒等）让作用量不变；大规范变换（不同同伦类）让它平移。
- 平移量正比于 $k$ 与绕数 $m$，比例系数 $2\pi$ 来自 Wess–Zumino 项的归一化，不是约定。
- 量子配分函数是 $\int\mathcal{D}A\,e^{iL}$，被积函数必须规范不变，因此 $e^{2\pi ikm}=1$ 对一切 $m$ 成立，即 $k\in\mathbb{Z}$。
- 必要性是严格论证；充分性（$k$ 整数就够）原文只用一句带过，严格说还需要测度与相位的整体定义。
- 同一量子化也出现在仿射 Lie 代数的中心荷上：$k$ 就是 level。

## 关键公式

- $L(A^g)=L(A)+2\pi k\,m$
- $m=\frac{1}{24\pi^2}\int_M\operatorname{Tr}(g^{-1}dg)^3\in\mathbb{Z}$
- $e^{2\pi ikm}=1\ \forall m\ \Longrightarrow\ k\in\mathbb{Z}$

## 必要性：$k\in\mathbb{Z}$

若 $\pi_3(G)\cong\mathbb{Z}$ 且 $e^{iL}$ 在规范变换下不变，则 $k$ 为整数。

**证明**：

1. 取绕数 $m=1$ 的大规范变换 $g$，作用量平移 $\Delta L=2\pi k$。 *（绕数 $m$ 的平移由 Wess–Zumino 项的拓扑性质给出。）*
2. 量子理论要求 $e^{iL}$ 规范不变，即 $e^{i\Delta L}=e^{2\pi ik}=1$。 *（$e^{iL}$ 是路径积分的权重，相位不可是新物理。）*
3. 于是 $k\in\mathbb{Z}$；对任意 $m$ 同理。 *（取 $m=1$ 已足够，其他绕数给出的是同一个条件。）*

## 陷阱

- $k$ 的整性依赖 $\operatorname{Tr}$ 的归一化；若把长根平方取为 2 的倍数，整性条件会变成别的格。
- 在带边流形上，大规范变换还会在边界上产生一个 WZW 项，$k$ 的整性条件与边界 CFT 的 level 是同一件事。
- 不要把它和“规范群的中心荷”混淆：中心荷是 $c=k\dim G/(k+h^\vee)$，与 $k$ 的单位不同。

## 相关卡片

- [cs-action](../concepts/cs-action.md)
- [wzw-action](../concepts/wzw-action.md)
- [affine-lie-algebra](../concepts/affine-lie-algebra.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§1 大规范变换与 $k$ 的整性，印刷页 [354, 355] / PDF 页 [4, 5]（witten1989/sections/s01-cs-action.tex（式 1.4））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
