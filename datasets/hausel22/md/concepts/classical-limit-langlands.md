# 几何 Langlands 的经典极限 $\mathscr{S}$

> `hausel22/concept/classical-limit-langlands` · 轨道 C · 增强镜像对称与膜 · 状态 dev

> **先自测**：为什么一阶近似反而更容易写清楚？

## 一句话

经典极限是把增强镜像对称沿 Hitchin 底作一阶近似，得到 $\M_\Dol$ 与 $\M^\vee_\Dol$ 导出范畴之间的等价。

## 定义

Donagi–Pantev 把 $I$ 结构下的 $B$ 型膜到 $B$ 型膜的匹配表述为同调镜像对称的经典极限，即 $\mathscr{S}:D^b(\M_\Dol)\simeq D^b(\M^\vee_\Dol)$（式 (2.5)）。他们先验证每个约化群 $\G$ 的一般 Hitchin 纤维确实是对偶阿贝尔簇；再验证相对 Hitchin 底的 Fourier–Mukai 变换给出这样的等价，并满足 Hecke–Wilson 交换关系。

**记号**：$\mathscr{S}$；$D^b(\M_\Dol)$；相对 Fourier–Mukai；$\calA$。

## 要点（为什么需要它）

1. 经典极限把 $\M_\DR$ 换成 $\M_\Dol$：$I$ 结构下 $B$ 型膜就是复子流形加全纯丛，比 $A$ 型膜好写。
2. 「相对 $\calA$ 的 Fourier–Mukai」：在底的一般点上，两侧都是对偶阿贝尔簇的扭转族，可以取 Poincaré 丛作核。
3. 它是「一阶近似」：预期延拓到模空间的奇点之上时必须作修改，修改方式原文未写。
4. 经典极限仍然满足 $\mathscr{W}^\mu\circ\mathscr{S}=\mathscr{S}\circ\mathscr{H}^\mu$，这正是 §3.4 讨论的出发点。

## 核心公式

$$
$$\mathscr{S}:D^b(\M_\Dol)\simeq D^b(\M^\vee_\Dol)$$
$$

## 定理与证明（或缺口）

### Donagi–Pantev 的经典极限构造

对每个约化群 $\G$，相对 $\calA$ 的 Fourier–Mukai 变换给出 $D^b(\M_\Dol)\simeq D^b(\M^\vee_\Dol)$ 的等价，在 $\calA$ 的一般点上；它满足 Hecke–Wilson 交换。

> 证明状态：**sketch**。原文只综述 Donagi–Pantev 的结果，未给证明；奇点处的修改未写出。

出处：`A p.2234 eq (2.5)`

## 常见误解

- 经典极限是 $\M_\Dol$ 之间的等价，不是 $\M_\DR$ 之间的；后者才是完整的 HMS。
- 把 $\mathscr{S}$ 当成整体定义的 Fourier–Mukai：它只在 $\calA$ 的一般点上是相对 FM，整体上要修改。
- 「一阶近似」不是「小参数展开」：这里指的是把 $A$ 型膜近似成 $B$ 型膜（先看 $I$ 结构），没有连续参数。
- 经典极限的交换关系里，Wilson 算子仍在 $\G$ 侧、Hecke 在 $\G^\vee$ 侧；方向与式 (3.12) 一致。

## 相关卡

[同调镜像对称](../concepts/homology-mirror-symmetry.md) · [增强镜像对称](../concepts/enhanced-mirror-symmetry.md) · [几何 Langlands 对应](../concepts/geometric-langlands-correspondence.md) · [经典极限 $\mathscr{S}$ 与算子的交换](../derivations/s-intertwines-operators.md)

## 出处（印刷页）

- A p.2234（A p.2234 eq (2.5)）

> 说明：A=原文 §2.5 对 Donagi–Pantev 的综述与式 (2.5)；B=把「相对 FM 需要一般点」的理由补出来；C=「没有连续参数」的澄清是我们按原文语境补的。最没把握处：奇点处的修改，原文只说「必须作修改」。
