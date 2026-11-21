# Kapustin–Witten 的 $S$ 对偶纲领

> `hausel22/concept/kapustin-witten-duality` · 轨道 C · 增强镜像对称与膜 · 状态 dev

> **先自测**：$S$ 对偶为什么能推出几何 Langlands 对应？

## 一句话

Kapustin–Witten 用四维 $N=4$ 理论的 $S$ 对偶约化到二维，把几何 Langlands 对应解释成一种增强镜像对称。

## 定义

2007 年 Kapustin–Witten 论证：四维 $\calN=4$ 超对称 Yang–Mills 理论中研究充分的 $S$ 对偶（又称电磁对偶或 Montonen–Olive 对偶），约化到二维后给出一种增强镜像对称，而后者又蕴含 Beilinson–Drinfeld 所表述的几何 Langlands 对应。约化后 $S$ 对偶成为两个 $\sigma$ 模型之间的等价：一个以 $C$ 上平坦 $\G$-联络模空间 $\M_\DR$ 为目标（$B$ 型），另一个以平坦 $\G^\vee$-联络模空间 $\M^\vee_\DR$ 为目标（$A$ 型）。

**记号**：$S$ 对偶；$\M_\DR,\M^\vee_\DR$；$B$ 型/$A$ 型 $\sigma$ 模型；Montonen–Olive。

## 要点（为什么需要它）

1. 链条是：四维 $S$ 对偶 → 二维 $\sigma$ 模型等价 → 增强镜像对称 → 几何 Langlands。三步都有独立内容，不能只引用最后一步。
2. 两个 $\sigma$ 模型的目标分别是 $\M_\DR$（$B$ 型）与 $\M^\vee_\DR$（$A$ 型），类型不对称是关键。
3. $S$ 对偶交换 Wilson 算子与 't Hooft 算子，这一步正是式 (3.12) 的物理来源。
4. 四维来源还给出「超 Kähler 膜匹配」这一额外结构，它超出普通 HMS，因此叫「增强」。

## 核心公式

$$
$$\mathscr{S}:D^b(\M_\DR)\simeq Fuk(\M^\vee_\DR)$$
$$

## 定理与证明（或缺口）

### $S$ 对偶 ⇒ 增强镜像对称 ⇒ 几何 Langlands

四维 $\calN=4$ 理论的 $S$ 对偶约化到二维给出 $\M_\DR$ 与 $\M^\vee_\DR$ 之间的增强镜像对称；后者蕴含几何 Langlands 对应（从 $\M_\DR$ 中的平坦联络出发，构造 $Fuk(\M^\vee_\DR)$ 中的元素，并解释为 $\G^\vee$-丛模空间上的 $D$-模）。

> 证明状态：**sketch**。整个推导是物理的；原文只综述，没有数学证明。

出处：`A p.2234`

## 常见误解

- $S$ 对偶不是「把群换成对偶群再重做一遍」：它同时交换电磁荷、把强耦合与弱耦合互换。
- 约化后的两个理论目标空间是 $\M_\DR$ 与 $\M^\vee_\DR$（$J$ 结构），不是 $\M_\Dol$；后者属于经典极限。
- 「增强」体现在两处额外结构（超 Kähler 膜匹配、Wilson–Hecke 交换），不是「更强的同调镜像对称」这种空话。
- Kapustin–Witten 的结论依赖 $N=4$ 超对称；把它推广到 $N=2$ 或纯 Yang–Mills 需要额外论证。

## 相关卡

[增强镜像对称](../concepts/enhanced-mirror-symmetry.md) · [超 Kähler 膜的四类型](../concepts/hyperkahler-branes.md) · [几何 Langlands 对应](../concepts/geometric-langlands-correspondence.md) · [经典极限 $\mathscr{S}$ 与算子的交换](../derivations/s-intertwines-operators.md)

## 出处（印刷页）

- A p.2234（A p.2234）

> 说明：A=原文 §2.5 首两段的综述；B=把「四维 → 二维 → Langlands」三步拆开；C=「依赖 $N=4$」的提醒是我们补的。最没把握处：原文说「约化到二维」，但未写清是在 $C\times\R^2$ 上紧化还是别的几何，此处的严格设定需要查 KW 原文。
