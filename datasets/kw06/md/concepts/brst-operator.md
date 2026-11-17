# BRST 算子

> `kw/concept/brst-operator` · 轨道 B · 扭化与拓扑 · 状态 dev

> **先自测**：BRST 算子是什么，它在整条论证链里起什么作用？

## 一句话

扭化后得到的幂零标量超荷 $Q$（$Q^2=0$），作用像 BRST 微分：物理量取 $Q$-上同调，$Q$-恰当项视为零；本文的 $Q$ 来自扭化而非规范固定。

## 定义

本文语境中 BRST 算子指扭化后保留下来的幂零标量超荷 $Q$；仿照 BRST 的惯例，物理态与算子按 $Q$-闭模 $Q$-恰当分类，任何 $Q$-恰当的项在物理上视为零。

**记号**：$Q$；$\{Q,\cdot\}$；$H_Q=\ker Q/\operatorname{im}Q$；$t=v/u$。

## 要点（为什么需要它）

1. 它把『拓扑』变成代数操作：$Q$-恰当项可丢弃，度规依赖与 $t$ 依赖都被自动抹掉。
2. 与通常的规范固定 BRST 不同：这里的 $Q$ 是扭化选出的超荷，其 $Q$-上同调就是物理谱本身。
3. Wilson 线与 't Hooft 线必须保持同一个 $Q$ 才能在 $Q$-上同调中比较，这给出线算子的分类。
4. 当 $Q$ 是标量超对称生成元时 $Q^2=0$ 才成立；这正是拓扑扭化与非拓扑超对称的差别。

## 核心公式

$$
$$Q^2=0,\qquad T_{\mu\nu}=\{Q,b_{\mu\nu}\}$$$$\delta_{\text{度规}}I=\{Q,\cdots\}\ \Longrightarrow\ Z\ \text{与度规无关}$$
$$

$$
$$\delta_{\text{度规}}I=\{Q,\cdots\}\ \Longrightarrow\ Z\ \text{与度规无关}$$
$$

## 定理与证明（或缺口）

### $Q$ 幂零

扭化后存在 $\mathrm{Spin}'(4)$-不变的标量超荷 $Q$，满足 $Q^2=0$。

1. $Q$ 取为不变旋量对应的超荷，故 $Q^2=\frac12\{Q,Q\}$ 与 $\mathrm{Spin}'(4)$ 对易。
   - *为什么*：$Q$ 由不变旋量生成，$\mathrm{Spin}'(4)$ 作用在 $Q^2$ 上平凡。
2. 而 (2.15) 的右端没有 $\mathrm{Spin}'(4)$-不变算符，所以 $Q^2$ 只能为零。
   - *为什么*：右端是平移生成元的组合，$P_\mu$ 在 $\mathrm{Spin}'(4)$ 下变换非平凡，不存在不变组合。

出处：`B p.18`

### 度规变化在 BRST 上同调中平凡

沿曲面 $C$ 移动算符插入点（一种度规改变）使作用量改变 BRST-平凡项 $\{Q,\cdot\}$，故 $Q$-上同调类不变，并在 $C$ 上给出平坦联络。

> 证明状态：**gap**。原文 p.97 在讨论 7-单值性时断言『this changes the underlying action by a BRST-trivial term {Q, ·}』，p.171 在 OPE 处重申，均未给证明。

出处：`B p.97`

## 常见误解

- 把这里的 $Q$ 与规范固定的 BRST 算子混为一谈：它来自拓扑扭化，是超荷，不是 Faddeev–Popov 微分。
- 以为 $Q$-闭就够了：只有 $Q$-闭模去 $Q$-恰当后的类才有物理意义。
- 忽略 $Q$ 依赖 $t$：不同扭化参数下选出的 $Q$ 不同，其上的上同调也随之变化。

## 相关卡

[上同调](../concepts/cohomology.md) · [拓扑量子场论](../concepts/topological-qft.md) · [超荷](../concepts/supercharge.md) · [拓扑扭化](../concepts/topological-twist.md)

## 出处（印刷页）

- B p.18（B p.18）
- B p.97（B p.97）
- B p.171（B p.171）

> 说明：A=原文：$Q^2=0$ 的论证 (p.18)、『BRST-trivial term』(p.97)、BRST 上同调 (p.171)；C=整理：把原文的 BRST 术语解释为扭化标量超荷，并写 summary、key_points、pitfalls（原文未给 BRST 的定义）。
