# $\mathbf F$ 型膜

> `gtgl15/concept/type-f-brane` · 轨道 C · 膜、线算符与本征膜 · 状态 dev

> **先自测**：为什么把“秩 1 $A$-膜 + 平坦 Chan–Paton 线丛”支撑在整条 Hitchin 纤维上，就足以承载 't Hooft 算符的全部信息？

## 一句话

$F$ 型膜 = Hitchin 纤维上的秩 1 $A$-膜 + 平坦 Chan–Paton 线丛（flat Spin$^c$ 结构编码它在对偶纤维中的位置），是 §4–§7 中磁本征膜的具体形态。

## 定义

$F$ 型膜指：支撑在 Hitchin 纤维 $F$（复环面）上的秩 1 $A$-膜，配上一条平坦 Chan–Paton 线丛。因为 $F$ 复 Lagrangian 且 $c_1(\mathcal L)=0$，它同时是 $I$ 的 $B$-膜与 $J,K$ 的 $A$-膜。平坦 Chan–Paton 线丛等价于一个 flat Spin$^c$ 结构（$\S2.6.4$ 的 K-理论讨论：$C\subset T^*C$ 上的秩 1 $A$-膜其 Chan–Paton 为平坦 Spin$^c$，度 $g-1$）。在 S-对偶下，${}^LG$ 侧的零维膜（摩天楼层）变成 $G$ 侧的 $F$ 型膜；平坦 Spin$^c$ 结构编码该点在 ${}^L F$ 中的位置。

**记号**：$F$；flat Spin$^c$；Chan–Paton 线丛；${}^LF$；$(B,A,A)$。

## 要点（为什么需要它）

1. 三要素：支撑在整条 Hitchin 纤维上、秩 1、Chan–Paton 线丛平坦（$c_1=0$）。
2. $F$ 型膜是 $(B,A,A)$ 型：对 $I$ 全纯（纤维），对 $J,K$ Lagrangian。
3. 平坦 Chan–Paton 线丛 = flat Spin$^c$ 结构；它记录对偶环面中的平移类，是“位置”的几何编码。
4. 它是零维膜在 S-对偶下的像：点（0 维，电本征）↔ 纤维上的 $A$-膜（磁本征）。
5. $\S5.4$ 的 eq (5.8) 说明它确实是磁本征膜，本征值在 §7 算出。

## 核心公式

$$
$$\text{F 型膜}:\ \left(F,\ \mathcal L\right),\quad \mathrm{rank}\,\mathcal L=1,\quad c_1(\mathcal L)=0,\quad \nabla\ \text{平坦}$$$$\text{零维膜（}{}^LG\text{）}\ \xrightarrow{\ S\text{-对偶}\ }\ \text{F 型膜（}G\text{）}$$
$$

$$
$$\text{零维膜（}{}^LG\text{）}\ \xrightarrow{\ S\text{-对偶}\ }\ \text{F 型膜（}G\text{）}$$
$$

## 定理与证明（或缺口）

### $F$ 型膜是 $(B,A,A)$ 型

复 Lagrangian 纤维上的秩 1 平坦线丛给出对 $I$ 的 $B$-膜与对 $J,K$ 的 $A$-膜。

1. $F$ 是复子流形，故对 $I$ 是 $B$-膜；$\mathcal L$ 全纯且平坦，是合法的 Chan–Paton。
   - *为什么*：$B$-膜只需全纯子流形与全纯 sheaf。
2. $F$ 对 $\omega_J,\omega_K$ 是 Lagrangian（$\S2.5$ 推论），$\mathcal L$ 平坦使 $A$-膜条件成立。
   - *为什么*：A$-膜需要 Lagrangian 子流形 + 平坦线丛。

出处：`A p.55`

## 常见误解

- Chan–Paton 线丛必须在 $F$ 上平坦（$c_1=0$）；有第一陈类的线丛不是 $A$-膜。
- 平坦 Spin$^c$ 结构不是“额外的选择”：它是 $A$-膜存在的数据之一，与 K-理论异常相关。
- $F$ 型膜的支撑是整条纤维，不是某一点；这与零维膜（电本征）形成对偶对比。
- 不要把它写成“Hitchin 纤维上的 $B$-膜”：对 $K$ 它是 $A$-膜，这正是它成为磁本征膜的原因。

## 相关卡

[磁本征膜](../concepts/magnetic-eigenbranes.md) · [对偶环面纤维化与 T-对偶](../concepts/dual-torus-fibration.md) · [摩天楼层（零维膜）](../concepts/skyscraper-zero-brane.md) · [万有丛、万有希格斯丛与陈–帕顿丛](../concepts/universal-bundles.md) · [膜、$A$-膜与 $B$-膜](../concepts/branes-ab.md)

## 出处（印刷页）

- A p.54–55（A p.55）
- A p.59（A p.59 eq (5.8)）
- A p.16（A p.16 eq (2.36)）

> 说明：A=原文 $\S5.1$ 的 F 型膜定义与 $\S5.4$ 的 eq (5.8)，$K$-理论支撑见 $\S2.6.4$；B=把 $(B,A,A)$ 型的两步验证补全；C=flat Spin$^c$ 与 K-理论异常的对应按原文 $\S2.6.4$ 与 $\S4.2$ 综合。最没把握处：flat Spin$^c$ 编码位置的精确方式原文写得简略。
