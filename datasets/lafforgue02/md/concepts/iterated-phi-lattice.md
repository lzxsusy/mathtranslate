# 迭代 $\varphi$-格

> `lafforgue02/concept/iterated-phi-lattice` · 轨道 B · 拓扑镜像对称与 Hodge 数 · 状态 dev

> **先自测**：为什么要在 $\varphi$-空间里数「迭代 $\varphi$-格」，它们与 chtouca 的退化是什么关系？

## 一句话

在 chtouca 的一般纤维的 $\varphi$-空间里，$\varphi$-格是满足 $\varphi(M)\subset M$ 的格；迭代 $\varphi$-格再叠上 HN 滤过与完整同态，用来把「退化」变成可数对象。

## 定义

设 $A_X$ 是 chtouca 一般纤维处的离散赋值环，$\varphi$ 是其上的 Frobenius。$\varphi$-空间指 $(A_X,\varphi)$ 上带 $\varphi$-半线性映射的模。$\varphi$-格是有限生成 $A_X$-模 $M$ 配 $\varphi(M)\subset M$ 且余核有限维。迭代 $\varphi$-格是 $M$ 连带其 HN 滤过与逐级完整同态 $(\mathcal L_s,\ell_s)$ 的数据，使每一段都对应低秩的 $\varphi$-格。

**记号**：$M$、$M'$；$\widehat M$ 为完备化；$\ul r_M^\pm$ 记录退化位置。

## 要点（为什么需要它）

1. 任务：证明「迭代 $\varphi$-格总有无穷多个，其中恰有一个满足所选截断多边形 $p$ 规定的性质」。
2. 「迭代」的含义是递归：第 $s$ 段本身又是一个低秩的 $\varphi$-格，于是归纳假设可以逐段使用。
3. 从一个迭代 $\varphi$-格过渡到另一个靠「初等变换」；退化子（dégénérateur）记录变换过程中出现的中间对象。
4. 第 VI 章用初等变换的序列**构造**出满足要求的迭代 $\varphi$-格（第 V 章只证明其存在性路线），并借此修正 [Lafforgue 1998] 末页的一处小错。

## 核心公式

$$
$\varphi(M)\subset M$，$[M:\\varphi(M)]<\infty$$M=\sum_{s\in\ul r^+}\widehat M_s$，$\mathrm{rg}_{V_s}M_s=s$，$s\in\ul r^-\cap\ul r^+$$u_s=\big(\prod_{t<s}\pi_A^{d_t(s-t)}\big)^{-(q-1)}\Lambda^s u$
$$

$$
$M=\sum_{s\in\ul r^+}\widehat M_s$，$\mathrm{rg}_{V_s}M_s=s$，$s\in\ul r^-\cap\ul r^+$
$$

$$
$u_s=\big(\prod_{t<s}\pi_A^{d_t(s-t)}\big)^{-(q-1)}\Lambda^s u$
$$

## 定理与证明（或缺口）

### 迭代 $\varphi$-格的存在与唯一（路线）

对给定的截断多边形 $p$ 与 chtouca 的一般纤维，迭代 $\varphi$-格有无穷多个，其中恰有一个满足 $p$ 规定的斜率条件；该格由初等变换的序列显式构造。

> 证明状态：**gap**。讲义第 V 章把存在性归约为赋值判据，第 VI 章给出构造；两章都只给路线与关键引理，完整论证在 [Lafforgue 1998]。本译本未补。

出处：`A p.34`

## 常见误解

- $\varphi$-格不是向量空间格：它活在 $A_X$ 上，$\varphi$ 是半线性的，不能按 $K_X$-向量空间的维数直觉处理。
- 「无穷多个」不是「连续多个」：这里数的是离散的迭代结构，条件 $p$ 恰好挑出唯一一个。

## 相关卡

[完整同态（homomorphisme complet）](../concepts/complete-homomorphism.md) · [退化子（dégénérateur）](../concepts/degenerator.md) · [用赋值判据把紧合性化归为构造一个 $\varphi$-格](../derivations/properness-by-valuative-criterion.md)

## 出处（印刷页）

- A p.34–45（A p.34）

> 说明：$\varphi$-空间与迭代 $\varphi$-格的定义取第 V 章 p.34–36；存在性与初等变换路线取 p.36–40 与第 VI 章 p.42–45。公式 $u_s$ 的归一化照讲义 p.42 原文。
