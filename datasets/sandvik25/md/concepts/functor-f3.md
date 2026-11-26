# 函子 III：$F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b\mathcal P_I$

> `sandvik25/concept/functor-f3` · 轨道 B · Springer 侧与三造函子 · 状态 dev

> **先自测**：为什么 $F_2$ 能下降成 $\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$ 上的函子，而 $F$ 本身还不是等价？

## 一句话

先验证 $K^bF_2$ 把 $\partial X$-支撑的复形打成零，于是 $F_2$ 下降为 $F$：$V\otimes\mathcal O_{\widetilde{\mathcal N}}\mapsto Z(\mathrm{Sat}(V))$、$\mathcal O_{\widetilde{\mathcal N}}(\lambda)\mapsto\mathbb W_\lambda$；复合实现函子后仍**不是**等价。

## 定义

由命题 3.1.2，$\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\cong K^b\mathrm{Coh}^{G^\vee\times T^\vee}_{\mathrm{free}}(\widehat{\mathcal N}_X)/K^b_{\partial X}$。若 $K^bF_2$ 把 $K^b_{\partial X}$ 打到 $K^b\mathcal P_I^{\mathrm{Wak}}$ 的零调复形，则 $F_2$ 下降为 $F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b\mathcal P_I^{\mathrm{Wak}}\hookrightarrow\mathcal D^b\mathcal P_I$，$V\otimes\mathcal O_{\widetilde{\mathcal N}}\mapsto Z(\mathrm{Sat}(V))$、$\mathcal O_{\widetilde{\mathcal N}}(\lambda)\mapsto\mathbb W_\lambda$。

**记号**：实现函子 $\mathcal D^b\mathcal P_I\to\mathcal D^b(I\backslash\mathrm{Fl}_G)$ 把反常层复形送到通常的导出等变范畴；它在 Iwahori 情形**不是**等价。

## 要点（为什么需要它）

1. 下降（descend）的关键是 $\partial X$ 上的零化，而这一步原文说「可以相当显式地验证，略去」——这是全文最明显的一处省略。
2. 两个对象对应是整篇文章的主线：$V\otimes\mathcal O_{\widetilde{\mathcal N}}\mapsto Z(\mathrm{Sat}(V))$ 与 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)\mapsto\mathbb W_\lambda$；§5 的等价正是把这两个对应升级为定理。
3. 「实现函子不是等价」是原文的明确警告（p.8 末）：Iwahori 情形反常层与通常导出范畴之间的差异真实存在，所以 $F$ 只能在反常层里取值域。
4. 与 $F_1$ 的关系：$F$ 在自由对象上就是 $F_1$ 的公式；$F$ 多做的是把这些对象装进 $\mathcal D^b\mathcal P_I$，从而可以取卷积、做三角运算。

## 核心公式

$$
$F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b\mathcal P_I,\quad V\otimes\mathcal O_{\widetilde{\mathcal N}}\mapsto Z(\mathrm{Sat}(V)),\quad \mathcal O_{\widetilde{\mathcal N}}(\lambda)\mapsto\mathbb W_\lambda$
$$

## 定理与证明（或缺口）

### 函子 III 的存在性（§3.4）

$K^bF_2$ 把 $\partial X$-支撑复形打到零调复形，故 $F_2$ 下降为 $F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b\mathcal P_I$。

> 证明状态：**gap**。原文：「This can be checked rather explicitly, and is omitted.」这是本译本标注的主要空白之一。

出处：`A p.8`

## 常见误解

- 把 $F$ 与「$F$ 复合实现函子」混为一谈：后者落在 $\mathcal D^b(I\backslash\mathrm{Fl}_G)$，且因实现函子非等价而丢掉信息。
- 下降用的商是 $K^b_{\partial X}$（$\partial X$ 上的集合论支撑），不是「$X$ 上的支撑」；边界差一个开浸入，这两种支撑不同。

## 相关卡

[函子 II：经 Tannakian 重构把 $F_1$ 扩到 $\mathrm{Coh}_{\mathrm{free}}(\widehat{\mathcal N}_X)$](../concepts/functor-f2.md) · [Springer 解消 $\widetilde{\mathcal N}$ 与线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$](../concepts/springer-resolution.md) · [主函子 $F^{\mathrm{IW}}$ 与 Arkhipov–Bezrukavnikov 等价（定理 5.0.1）](../concepts/functor-fiw.md)

## 出处（印刷页）

- A p.8（A p.8）

> 说明：下降论证与两个对象对应在 p.8；「实现函子非等价」的警告同页末。
