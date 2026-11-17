---
id: csw/concept/wilson-line
type: concept
track: A
---

# Wilson 线

> 沿闭曲线 $C$ 取联络的路径序指数再取迹：不需要度规，只依赖曲线的同伦类与表示，是三维理论的“可观测量”。

**问题**：Wilson 线为什么是 CS 理论里最自然的观测量？它的期望值为什么给纽结不变量？

## 定义

设 $C\subset M$ 是闭曲线，$R$ 是 $G$ 的表示。Wilson 线定义为 $W_R(C)=\operatorname{Tr}_R\,\mathrm{P}\exp\oint_C A$，其中 $\mathrm{P}$ 表示沿 $C$ 的路径序。链环配分函数为 $Z(M;C_i,R_i)=\int\mathcal{D}A\,e^{iL}\prod_iW_{R_i}(C_i)$。

*记号*：$\mathrm{P}\exp$ 是路径序指数；$\operatorname{Tr}_R$ 在表示 $R$ 的空间上取迹。

## 要点

- 路径序指数是沿曲线的平行移动，取迹后与起点无关，因此只依赖同伦类与表示。
- 它不需要度规：曲线、联络、表示都是拓扑/微分几何数据。
- 在 CS 理论里，Wilson 线的期望值是三维流形中链环的不变量；$S^3$ 上取 $G=SU(N)$、定义表示，得到 Jones 多项式的两变量推广。
- 标架进入相位：带扭转的 Wilson 线乘 $e^{2\pi i t h_R}$，这是标架反常的物理来源。
- 在正则量子化里，Wilson 线变成穿刺点上的算符，对应表示 $R$ 的插入。

## 关键公式

- $W_R(C)=\operatorname{Tr}_R\,\mathrm{P}\exp\oint_CA$
- $Z(M;C_i,R_i)=\int\mathcal{D}A\,e^{iL}\prod_iW_{R_i}(C_i)$
- $W_R(C\text{ 带扭转 }t)=e^{2\pi ith_R}W_R(C)$

## 规范不变性

设 $g:M\to G$ 是规范变换，则 $W_R(C)$ 在 $A\mapsto A^g$ 下不变（对闭曲线）。

**证明**：

1. 沿 $C$ 的平行移动在规范变换下共轭：$U_C(A^g)=g(x_0)^{-1}U_C(A)g(x_0)$，$x_0$ 是起点。 *（路径序指数是平行移动的合成，规范变换逐点共轭作用。）*
2. 取迹后共轭消失：$\operatorname{Tr}_R(g^{-1}Ug)=\operatorname{Tr}_R(U)$。 *（迹对共轭不变。）*
3. 闭曲线起点可以取同一点，因此 $W_R(C)$ 规范不变。 *（对开曲线，两端点处的共轭不抵消，Wilson 线变成两端点表示空间的张量。）*

## 陷阱

- 开曲线的 Wilson 线不是规范不变的，它带两个端点的表示指标。
- 路径序在非阿贝尔情形不可省；把 $\exp\oint A$ 当成普通指数会漏掉沿曲线的排序。
- $\operatorname{Tr}$ 取哪个表示（定义表示还是伴随表示）决定它对应哪个不变量：$SU(N)$ 定义表示 ↔ Jones，$SO(N)$ ↔ Kauffman。

## 相关卡片

- [cs-action](../concepts/cs-action.md)
- [puncture-gauss-law](../concepts/puncture-gauss-law.md)
- [jones-from-cs](../concepts/jones-from-cs.md)
- [borel-weil-bott](../concepts/borel-weil-bott.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§1 Wilson 线与配分函数，印刷页 [355, 355] / PDF 页 [5, 5]（witten1989/sections/s01-cs-action.tex（式 1.5–1.6））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
