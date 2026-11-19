# 膜、$A$-膜与 $B$-膜

> `gtgl15/concept/branes-ab` · 轨道 C · 膜、线算符与本征膜 · 状态 dev

> **先自测**：在同一个超凯勒靶空间上，$A$-膜与 $B$-膜到底差在哪里，为什么它们会对应不同的几何对象？

## 一句话

$\MH$ 上的边界条件由膜描述：$B$-膜是复子流形加全纯 sheaf，$A$-膜是 Lagrangian 子流形加平坦 $U(1)$ 联络；超凯勒三个复结构给出 $(B,B,B)$、$(B,A,A)$ 等不同类型。

## 定义

2d $\sigma$-模型的边界条件＝$\MH$ 上的膜。对复结构 $I$：$B$-膜是 $I$-全纯子流形（或更一般 coherent sheaf）配全纯结构；对辛形式 $\omega_K$：$A$-膜是 $\omega_K$-Lagrangian 子流形配平坦 $U(1)$ 线丛（Chan–Paton）。若 $\MH$ 有复结构 $I,J,K$ 与相应辛形式 $\omega_I,\omega_J,\omega_K$，则膜按保持哪些超荷分成类型 $(B,B,B)$、$(B,A,A)$、$(A,B,A)$ 等。本文关心的磁本征膜是 $(B,A,A)$ 型：对 $I$ 是 $B$-膜，对 $J,K$ 是 $A$-膜。

**记号**：$(B,B,B)$ 等类型；$I,J,K$；$\omega_I,\omega_J,\omega_K$；Chan–Paton 丛。

## 要点（为什么需要它）

1. $B$-膜依赖复结构（全纯对象），$A$-膜依赖辛结构（Lagrangian + 平坦线丛）：两者不是同一类几何对象。
2. 超凯勒流形上同一条膜可以同时对不同复结构是 $A$-膜或 $B$-膜，于是有类型 $(B,A,A)$ 等。
3. 零维膜（摩天楼层）是最简单的 $B$-膜：对三个复结构都是 $(B,B,B)$。
4. $F$ 型膜是 Hitchin 纤维上的秩 1 $A$-膜配平坦 Chan–Paton 线丛：对 $I$ 是 $B$-膜（纤维复子流形），对 $J,K$ 是 $A$-膜。
5. 几何 Langlands 对偶把 $\MH(G)$ 的 $\omega_K$-A-膜与 $\MH({}^LG)$ 的 $J$-B-膜对应起来。

## 核心公式

$$
$$B\text{-膜}:\ (X,\mathcal F),\ \ \bar\partial_{\mathcal F}=0;\qquad A\text{-膜}:\ (L,\nabla),\ \ \omega|_L=0,\ F_\nabla=0$$$$\text{类型 }(B,A,A):\ \text{对 }I\ \text{全纯，对 }J,K\ \text{Lagrangian}$$
$$

$$
$$\text{类型 }(B,A,A):\ \text{对 }I\ \text{全纯，对 }J,K\ \text{Lagrangian}$$
$$

## 定理与证明（或缺口）

### 膜类型的超荷刻画

膜的 $(A/B)$ 类型由它保持哪些超荷决定；同一膜对不同复结构可有不同类型。

> 证明状态：**sketch**。原文 §4 只按需要引用这些标准事实，未给系统证明。

出处：`A p.34`

## 常见误解

- $A$-膜不是“反全纯的 $B$-膜”：它由辛形式定义，与复结构无关（但需要选一个）。
- 平坦 Chan–Paton 线丛要求 $c_1=0$；有曲率的线丛不是 $A$-膜。
- $(B,A,A)$ 型膜对 $I$ 是全纯的，对 $J,K$ 是 Lagrangian 的：三个结构不能混为一谈。
- 零维膜是 $(B,B,B)$，不是 $(B,A,A)$；S-对偶后才变成 $(B,A,A)$ 型磁本征膜。

## 相关卡

[二维 $\sigma$-模型与靶空间 $\MH$](../concepts/sigma-model-mh.md) · [本征膜](../concepts/eigenbranes.md) · [$\mathbf F$ 型膜](../concepts/type-f-brane.md) · [摩天楼层（零维膜）](../concepts/skyscraper-zero-brane.md) · [超凯勒商与复结构 I、J、K](../concepts/hyperkahler-quotient.md)

## 出处（印刷页）

- A p.34–37（A p.35）
- A p.37–38（A p.38 eq (4.7)）
- A p.54–55（A p.54）

> 说明：A=原文 §4.1 的膜与 sheaf 描述、$\S4.2$ 的 $(B,B,B)\to(B,A,A)$、$\S5.1$ 的 F 型膜；B=把 A/B 型的几何判据整理成两步；C=超荷判据按标准 2d $\sigma$-模型背景补。最没把握处：类型记号在原文散见于 §4–§5，未集中定义。
