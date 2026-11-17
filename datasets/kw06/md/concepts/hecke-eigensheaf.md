# Hecke 特征层

> `kw/concept/hecke-eigensheaf` · 轨道 E · Langlands 与翻译器 · 状态 dev

> **先自测**：Hecke 特征层的本征方程是什么，它为什么是几何 Langlands 的一端？

## 一句话

$\mathrm{Bun}_G$ 上的层 $\mathcal F$，被 Hecke 算子作用后满足 $\mathbb H_x^V(\mathcal F)\cong V\otimes\mathcal F$；它是几何 Langlands 中局部系统那一端的像。

## 定义

Hecke 特征层是 $\mathrm{Bun}_G$ 上的层 $\mathcal F$，使得对每个表示 $V$ 与点 $x\in C$，Hecke 算子作用后满足 $\mathbb H_x^V(\mathcal F)\cong V\otimes\mathcal F$。在几何 Langlands 中，$C$ 上 $^L G$ 的局部系统对应这样的层。

**记号**：$\mathbb H_x^V$：沿表示 $V$ 的 Hecke 算子；$x\in C$：Hecke 修改点；$\mathcal F$：$\mathrm{Bun}_G$ 上的层。

## 要点（为什么需要它）

1. 它是几何 Langlands 的右端，本征方程就是“Hecke 作用等于张量 $V$”。
2. 它不是任意 D-模：还要求 holonomic，即解空间有限维。
3. 本征值是表示 $V$ 而不是数，这解释了特征膜特征值为什么必须是向量空间。
4. 物理上它应来自磁特征膜（'t Hooft 算子的特征膜）。

## 核心公式

$$
$\mathbb H_x^V(\mathcal F)\cong V\otimes\mathcal F$$\mathcal F_\vartheta\in\mathrm{D}\text{-}\mathrm{mod}(\mathrm{Bun}_G),\qquad \mathbb H_x^V(\mathcal F_\vartheta)\cong V\otimes\mathcal F_\vartheta$
$$

$$
$\mathcal F_\vartheta\in\mathrm{D}\text{-}\mathrm{mod}(\mathrm{Bun}_G),\qquad \mathbb H_x^V(\mathcal F_\vartheta)\cong V\otimes\mathcal F_\vartheta$
$$

## 定理与证明（或缺口）

### Hecke 特征层取 holonomic D-模

几何 Langlands 中的 Hecke 特征层是 holonomic D-模，故其解空间有限维；本文预期 type F 膜给出这类层。

> 证明状态：**gap**。原文 p.122 只把 holonomic D-模列为对应的一端，未证明 type F 膜给出的层确实 holonomic；这正是 §9–§11 想解释、但未完成的部分。

出处：`B p.122`

## 常见误解

- 把 Hecke 特征层当成任意 D-模；特征方程只是一个条件，holonomic 性是另一个。
- 把本征值当成标量；它是 $G$ 的表示 $V$。
- 把 $\mathrm{Bun}_G$ 与 $M(G,C)$ 混同：Hecke 特征层住在 $\mathrm{Bun}_G$ 上。

## 相关卡

[Hecke 算子](../concepts/hecke-operator.md) · [几何 Langlands 对应](../concepts/geometric-langlands.md) · [D-模](../concepts/d-module.md) · [特征膜（eigenbrane）](../concepts/eigenbrane.md)

## 出处（印刷页）

- B p.122（B p.122）
- B p.149（B p.149）

> 说明：A=原文 p.122 的名称与主断言、p.149 的 Hecke 对应；B=把本征方程从 p.122 的叙述读出来；C=holonomic 与有限维解空间的等价属数学常识，非原文明说。
