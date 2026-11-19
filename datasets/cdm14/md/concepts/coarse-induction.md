# 粗糙归纳与 Gorenstein 条件

> `cdm14/concept/coarse-induction` · 轨道 D · 晶体上的 t-结构 · 状态 dev

> **先自测**：$\oblv^r$ 什么时候能看成 $\QCoh$ 上的遗忘函子？

## 一句话

把 $\IndCoh$ 先左完备化到 $\QCoh$，得到「粗糙」的归纳/遗忘函子；$\oblv^r$ 穿过 $\QCoh$ 当且仅当 $X$ 是 Gorenstein。

## 定义

$\Psi_X:\IndCoh(X)\to\QCoh(X)$ 是左完备化（[IndCoh, 命题 1.3.4]）。定义 $'\oblv^r_X:=\Psi_X\circ\oblv^r_X$，$'\ind^r_X$ 为其左伴随（当存在）。

**记号**：$\Xi_X$ 为 $\Psi_X$ 的右伴随；最终余连接时 $\Xi_X$ 全忠实。

## 要点（为什么需要它）

1. 命题 4.6.4：$'\oblv^r_X$ 有有限上同调幅度且保守——所以「粗糙」遗忘仍然够用。
2. 引理 4.6.12（Drinfeld）：$\oblv^r_X$ 穿过 $\Xi_X$ 的像，当且仅当 $X$ 是 Gorenstein。
3. Gorenstein 的定义：$\omega_X\in\Coh(X)$ 且为分次线丛，等价于 $\omega_X\in\QCoh(X)^{\mathrm{perf}}$。
4. 最终余连接时 $'\ind^r_X\simeq\ind^r_X\circ\Xi_X$（引理 4.6.8），于是粗糙与精细的归纳只差 $\Xi$。

## 核心公式

$$'\oblv^r_X:=\Psi_X\circ\oblv^r_X,\qquad \oblv^r_X\text{ 穿过 }\Xi_X\iff X\text{ Gorenstein}$$

## 定理与证明（或缺口）

### Gorenstein 判别（引理 4.6.12）

$\oblv^r_X$ 取值落在 $\Xi_X$ 的本质像中，当且仅当 $X$ 是 Gorenstein 的。

> 证明状态：**sketch**。第 1 步的交换图在原文中是 (4.6) 式，本文未复述其证明。

出处：`A p.39`

## 常见误解

- Gorenstein 不是「对偶化层存在」：存在是最终余连接就够；Gorenstein 要求它完美。
- $'\ind^r$ 与 $\ind^r$ 一般不同；只有最终余连接时才有引理 4.6.8 的关系。
- 注 4.6.10：非最终余连接时 $('\ind^r,'\oblv^r)$ 不再是伴随对。

## 相关卡

[右晶体的归纳函子 $\ind^r_X$](../concepts/induction-right.md) · [$\Crys^r(X)$ 的左完备性](../concepts/left-completeness.md) · [$\Crys^r(X)$ 是其心上的导出范畴](../concepts/abelian-heart.md)

## 出处（印刷页）

- A p.38–40（A p.38）

> 说明：A=§4.6 的命题 4.6.4 与引理 4.6.12；最没把握处：Gorenstein 判别中第 1 步的交换图。
