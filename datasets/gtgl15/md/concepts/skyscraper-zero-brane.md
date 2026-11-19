# 摩天楼层（零维膜）

> `gtgl15/concept/skyscraper-zero-brane` · 轨道 C · 膜、线算符与本征膜 · 状态 dev

> **先自测**：为什么最“局部”的零维膜反而是电本征膜，而它的对偶居然支撑在整条 Hitchin 纤维上？

## 一句话

在 $\MH$ 的一点 $m$ 处的摩天楼层 sheaf 给出零维膜，它是最简单的电本征膜（$(B,B,B)$ 型）；S-对偶把它变成磁侧的 $F$ 型膜。

## 定义

对点 $m\in\MH$，取 sheaf $U=\mathcal O_m$（摩天楼层：只在 $m$ 处有非零纤维）作为 Chan–Paton 丛，得到零维膜 $B=\delta_m$。它对 $I,J,K$ 三个复结构都是 $B$-膜，即 $(B,B,B)$ 型。Wilson 线作用后 $B\otimes\mathcal E_{H,{}^LR}|_{p\times m}$ 只是张量一个固定向量空间，故零维膜是电本征膜（eq (4.5)(4.6)）。在 S-对偶下，它对应 $G$ 侧的 $F$ 型膜（支撑整条纤维、带平坦 Chan–Paton 线丛）；对偶不保持支撑的维数。

**记号**：$m\in\MH$；$\mathcal O_m$；$\delta_m$；$(B,B,B)$；S-对偶。

## 要点（为什么需要它）

1. 零维膜 = 摩天楼层 sheaf，支撑是一个点；这是最简单的 $B$-膜，对三个复结构都是 $B$-型。
2. 零维膜总是电本征膜：Wilson 作用只乘一个固定向量空间，不改变支撑。
3. S-对偶后变成 $F$ 型膜：支撑维数从 0 变成 $\dim F$，这是对偶的非平凡之处。
4. 零维膜的“位置” $m$ 在 S-对偶后编码为 $F$ 型膜的平坦 Chan–Paton 线丛（flat Spin$^c$ 结构）。
5. $\S4.2$ 末把零维膜作为几何 Langlands 对偶的出发点：$(B,B,B)\to(B,A,A)$。

## 核心公式

$$
$$B=\delta_m=\mathcal O_m,\qquad W({}^LR,p)B=B\otimes\mathcal E_{H,{}^LR}|_{p\times m}$$$$\delta_m\ (\text{电，}0\text{ 维})\ \xrightarrow{\ S\text{-对偶}\ }\ \text{F 型膜（磁，}\dim F\text{ 维）}$$
$$

$$
$$\delta_m\ (\text{电，}0\text{ 维})\ \xrightarrow{\ S\text{-对偶}\ }\ \text{F 型膜（磁，}\dim F\text{ 维）}$$
$$

## 定理与证明（或缺口）

### 零维膜在 S-对偶下的像

${}^LG$ 侧的零维膜对偶到 $G$ 侧支撑在 Hitchin 纤维上的 $F$ 型膜。

> 证明状态：**sketch**。原文以猜测加 $\S5$ 的验证给出；逐纤维的严格镜像陈述未完整证明。

出处：`A p.38`

## 常见误解

- 零维膜不是“什么都不带的膜”：它带一个固定 Chan–Paton 向量空间，正是这一点让它本征。
- 摩天楼层 sheaf 与“点上的函数”不同：它是 skyscraper，只有该点有纤维。
- S-对偶不保持支撑维数：0 维变整条纤维，别以为对偶是逐点对应的。
- 零维膜是 $(B,B,B)$ 不是 $(B,A,A)$；对偶之后才是 $(B,A,A)$。

## 相关卡

[电本征膜](../concepts/electric-eigenbranes.md) · [磁本征膜](../concepts/magnetic-eigenbranes.md) · [$\mathbf F$ 型膜](../concepts/type-f-brane.md) · [本征膜](../concepts/eigenbranes.md) · [膜、$A$-膜与 $B$-膜](../concepts/branes-ab.md)

## 出处（印刷页）

- A p.37–39（A p.38 eq (4.5)）
- A p.54–55（A p.54）

> 说明：A=原文 $\S4.2$ 的 eq (4.5)(4.6) 与 $(B,B,B)$ 型陈述、$\S5.1$ 的对偶猜测；B=把 S-对偶的像拆成两步；C=支撑维数变化的表述按 $\S4.2$ 末段补。最没把握处：S-对偶下零维膜逐纤维对应的严格陈述原文未给证明。
