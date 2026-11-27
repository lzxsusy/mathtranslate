# Shimura 簇：$n=2$ 的几何载体

> `goresky04/concept/shimura-variety` · 轨道 C · 对应与障碍 · 状态 dev

> **先自测**：Shimura 簇到底是什么，为什么它只在部分情形存在？

## 一句话

Shimura 簇是带水平结构的阿贝尔簇的模空间；对 $n=2$ 它就是一维的模曲线，所以有上同调可用；$n\ge3$ 时对应的空间不再是簇。

## 定义

$\GL(2)$ 情形：$X=\GL(2,\bbQ)Z(\bbA)\backslash\GL(2,\bbA)/\sO(2)K_{\mathrm f}$ 分类带水平结构的椭圆曲线，是一维代数曲线（模曲线）。一般地，Shimura 簇是某个约化群 $G$ 的对称空间上的商，分类带水平结构的阿贝尔簇（或更一般的 motive）。它存在的前提是 $G$ 的对称空间是 Hermitian 对称空间，这要求 $G$ 的类型属于特定几族。

**记号**：$\sO(2)$ 是 $\GL(2,\bbR)$ 的极大紧子群；$K_{\mathrm f}=\prod_p K_p$ 水平结构；$X_\Gamma=\Gamma\backslash X$。

## 要点（为什么需要它）

1. Shimura 簇的存在性是**群论条件**：等价于 $G$ 的对称空间是 Hermitian 的；$\GL(n)$ 只有在 $n=2$ 时满足（此时对称空间是 $\he$）。
2. $n=2$ 时它是曲线（一维），$H^1$ 的秩恰是 $2$；$n=3$ 时对称空间是 $\GL(3,\bbR)/(\sO(3)\cdot\bbR_{>0})$，维数 $5$，不是 Hermitian 对称空间。
3. 没有 Shimura 簇不等于没有自守侧：自守形式仍定义在 $\GL(n,\bbQ)\backslash\GL(n,\bbA)$ 上，缺的是「能取上同调的几何对象」。

## 核心公式

$$
$X=\GL(2,\bbQ)Z(\bbA)\backslash\GL(2,\bbA)/\sO(2)K_{\mathrm f}$ 为一维模曲线$\dim\,\GL(n,\bbR)/(\sO(n)\cdot\bbR_{>0})=\frac{n(n-1)}{2}$
$$

$$
$\dim\,\GL(n,\bbR)/(\sO(n)\cdot\bbR_{>0})=\frac{n(n-1)}{2}$
$$

## 定理与证明（或缺口）

### 模曲线的代数性

$X$ 作为带水平结构的椭圆曲线模空间，具有定义在 $\bbQ$ 上的代数曲线结构，故可用平展上同调。

> 证明状态：**gap**。原文直接使用这个结论（「模空间」），没有证明；这是模形式几何理论的标准结果。

出处：`A p.14`

## 常见误解

- Shimura 簇不是「所有 $G$ 的对称空间」：一般 $G$ 的对称空间只是 Riemann 对称空间，没有复结构，取不了代数簇的上同调。
- 「模曲线是一维的」与「$\GL(2)$ 是二维群」容易混淆：维数说的是簇的维数 $1$，不是群的维数 $2$。

## 相关卡

[Eichler–Shimura：$n=2$ 情形猜想的证明](../concepts/eichler-shimura-theorem.md) · [$n\ge3$ 的障碍：Shimura 簇不存在](../concepts/obstruction-n-ge-3.md) · [几何朗兰兹：把猜想搬到曲线上](../concepts/geometric-langlands.md)

## 出处（印刷页）

- A p.14–15（A p.14）

> 说明：对应原文 §7.1 对模曲线的引用与 §7.2 对 $n\ge3$ 的对照；Hermitian 对称空间一条是把原文「所需的 Shimura 簇不存在」讲开，属译者按。
