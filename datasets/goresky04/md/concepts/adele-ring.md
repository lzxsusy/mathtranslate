# 平代环与限制直积

> `goresky04/concept/adele-ring` · 轨道 B · 自守侧 · 状态 dev

> **先自测**：为什么要把所有 $\bbQ_p$ 乘起来，限制直积这个条件又在限制什么？

## 一句话

平代环 $\bbA_\bbQ=\bbR\times\prod_p'\bbQ_p$ 是把所有完备化一次收进来的环；它使「对所有素数同时成立」的陈述可以写成一个整体对象上的陈述。

## 定义

平代环 $\bbA_\bbQ$ 的元素是序列 $(g_\infty,g_2,g_3,\dots)$，其中 $g_\infty\in\bbR$，$g_p\in\bbQ_p$，并要求对几乎所有 $p$ 有 $g_p\in\bbZ_p$。这个条件叫限制直积。$\bbQ$ 通过对角嵌入成为 $\bbA_\bbQ$ 的离散子环，商 $\bbQ\backslash\bbA_\bbQ$ 紧。有限平代 $\bbA_{\mathrm f}=\prod_p'\bbQ_p$ 是其中去掉 $\bbR$ 的部分。

**记号**：$\bbA=\bbA_\bbQ$；$\bbA_{\mathrm f}$ 有限平代；$\hat{\bbZ}=\prod_p\bbZ_p$ 是 $\bbA_{\mathrm f}$ 的紧开子环。

## 要点（为什么需要它）

1. 限制直积不是技术细节：没有它，$\prod_p\bbQ_p$ 太大，$\bbQ$ 的嵌入不离散，商空间没有好性质。
2. 平代环把「每个素数处给一个局部对象」打包成一个整体对象；朗兰兹猜想的两侧都是整体对象，所以必须用平代环。
3. $\bbQ\backslash\bbA$ 紧（加上 $\bbR$ 后要除以正实数）是「整体紧性」的来源，它让 $L^2$ 空间的分解成为可能。

## 核心公式

$$
$\bbA_\bbQ=\bbR\times\prod_p{}'\bbQ_p$，$\prod'$ 表示限制直积$\bbQ\backslash\bbA_\bbQ/\bbR_{>0}$ 紧
$$

$$
$\bbQ\backslash\bbA_\bbQ/\bbR_{>0}$ 紧
$$

## 定理与证明（或缺口）

### 紧性

$\bbQ$ 在 $\bbA_\bbQ$ 中离散，且 $\bbQ\backslash\bbA_\bbQ/\bbR_{>0}$ 紧。

> 证明状态：**sketch**。原文只陈述紧性，不证；这是 Tate 论文与 [G1] 的标准结果。

出处：`A p.11`

## 常见误解

- 平代环是环不是域：$2$ 在 $\bbA$ 中没有逆（在 $2$ 进分量上不可逆），但它有逆当且仅当每个局部分量都可逆。
- $\bbA_{\mathrm f}$ 与 $\hat{\bbZ}$ 常被混用：前者是环，后者是它的紧开子环；$\GL(2,\bbA_{\mathrm f})$ 的紧开子群是 $\prod_p\GL(2,\bbZ_p)$，不是 $\hat{\bbZ}$ 本身。

## 相关卡

[域的分类：数域、$p$ 进域、函数域](../concepts/global-and-local-fields.md) · [从模形式到平代环上的自守形式（(6.1.1)）](../derivations/adelic-equivalence.md) · [自守形式与自守表示](../concepts/automorphic-representation.md)

## 出处（印刷页）

- A p.11（A p.11）

> 说明：对应原文 §6.1 的定义段与 (6.1.1) 前的铺垫；紧性一条原文只引用，未证。
