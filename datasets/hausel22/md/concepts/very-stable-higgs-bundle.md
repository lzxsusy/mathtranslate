# 非常稳定 Higgs 丛

> `hausel22/concept/very-stable-higgs-bundle` · 轨道 D · 幂零锥上的等变重数 · 状态 dev

> **先自测**：「非常稳定」这个名字与「稳定」是什么关系？

## 一句话

非常稳定指上行流与芯只交于自身；等价地上行流是闭的，且 Hitchin 映射在其上 proper、有限。

## 定义

在 BB 框架下：当 $W^+_\alpha\cap\calC=\{\alpha\}$ 时，称 $\alpha\in(X^s)^\T$ 与 $W^+_\alpha$ 非常稳定。等价地，$\alpha$ 非常稳定当且仅当 $W^+_\alpha\cap W^-_\beta\neq\emptyset$ 蕴含 $\beta=\alpha$。更一般地，当 $W^+_\alpha\cap W^-_\beta\neq\emptyset$ 时规定 $\alpha\le\beta$，这给出偏序，而非常稳定恰是它关于此序的极大元。

**记号**：$W^+_\alpha$；$\calC$；$\le$（BB 序）；$\M^{s\T}$。

## 要点（为什么需要它）

1. 非常稳定是「极大性」：没有任何别的下行流与它相交，所以它「最靠上」。
2. 定理 3.2：非常稳定 ⟺ 上行流 $W^+_\alpha\subset X$ 是闭的。
3. 定理 3.3：对 $\calE\in\M^{s\T}$，非常稳定 ⟺ $h^{-1}(0)\cap W^+_\calE=\{\calE\}$ ⟺ $h_\calE:W^+_\calE\to\calA$ proper ⟺ $h_\calE$ 有限。
4. 非常稳定与 wobbly 互补：§3.3 猜想的对象 $\calE_{\delta^\mu_c}$ 在 $\mu=(d+1)\omega_k$ 时是 wobbly（不非常稳定），其拉格朗日闭包才是镜像的对象。

## 核心公式

$$
$$\alpha\text{ very stable}\iff W^+_\alpha\cap\calC=\{\alpha\}\iff W^+_\alpha\subset X\text{ closed}$$$$\calE\text{ very stable}\iff h^{-1}(0)\cap W^+_\calE=\{\calE\}\iff h_\calE\text{ proper}\iff h_\calE\text{ finite}$$
$$

$$
$$\calE\text{ very stable}\iff h^{-1}(0)\cap W^+_\calE=\{\calE\}\iff h_\calE\text{ proper}\iff h_\calE\text{ finite}$$
$$

## 定理与证明（或缺口）

### 非常稳定的闭性（定理 3.2）

$\alpha\in(X^s)^\T$ 非常稳定，当且仅当 $W^+_\alpha\subset X$ 是闭的。

> 证明状态：**sketch**。原文引用 [HH, Prop 2.14]，未给证明。

出处：`A p.2237`

### 非常稳定与 proper 性的等价（定理 3.3）

设 $\calE\in\M^{s\T}$。则 $\calE$ 非常稳定 ⟺ $h^{-1}(0)\cap W^+_\calE=\{\calE\}$ ⟺ $h_\calE:W^+_\calE\to\calA$ 是 proper 的 ⟺ $h_\calE$ 是有限映射。

> 证明状态：**sketch**。原文引用 [HH]，未给证明。

出处：`A p.2238`

## 常见误解

- 本文的「非常稳定」用 BB 序刻画（定理 3.2）；文献中另有 Drinfeld 的原始定义（不存在非零幂零 Higgs 场使 $(E,\Phi)$ 半稳定）。HH 的主要结果正是把两者联系起来，引用时要说明用的是哪一种。
- 把「稳定」与「非常稳定」混为一谈：稳定是 GIT 条件，非常稳定是流/层的条件，后者强得多。
- 定理 3.3 的四个等价是连等的，但只在 $\calE\in\M^{s\T}$（光滑轨迹上的不动点）时成立，不能对任意 Higgs 丛套用。
- $h_\calE$ proper 说的是限制映射 $W^+_\calE\to\calA$，不是整个 $h:\M\to\calA$ 的 proper 性（后者对一切 $\M$ 都成立）。

## 相关卡

[Białynicki–Birula 分解与上行流](../concepts/bialynicki-birula-attraction.md) · [等变重数 $m_\calE(t)$](../concepts/equivariant-multiplicity.md) · [局部重数代数 $Q_\calE$](../concepts/local-multiplicity-algebra.md) · [非常稳定的四重等价链](../derivations/very-stable-chain.md)

## 出处（印刷页）

- A p.2237（A p.2237）
- A p.2238（A p.2238）

> 说明：A=原文 §3.1.1 的定义与定理 3.2、§3.1.2 的定理 3.3；B=把定理 3.3 的四个等价串成一条链；C=「非常稳定与 wobbly 互补」是按 §3.3 的用法归纳。最没把握处：Drinfeld 定义与 BB 定义的一致性，原文未在本文中说明，只引 HH。
