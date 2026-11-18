# 小哈密顿形变不改变对象的拟同构类

`kshms/concept/prp-04-fukaya-hamiltonian-deformation-quasi-iso` · track C（Fukaya 与退化） · 原文 命题 4

**问题**　拉格朗日子流形不横截时，能否用小哈密顿形变把它挪到横截位置，而不改变它在范畴中的类？

**摘要**　由 $\mathcal{F}(V)$ 的对象 $(L,\rho)$ 经小哈密顿形变得到的 $(L_t,\rho_t)$，与 $(L,\rho)$ 拟同构；这条延拓性质让横截序列可以补足缺失的对象。

**别名**　small Hamiltonian deformation；小哈密顿形变；Fukaya 范畴的形变不变性

## 陈述

设 $(L_t,\rho_t)$ 是由 $\mathcal{F}(V)$ 的对象 $(L,\rho)$ 作小哈密顿形变得到的对象。则 $(L_t,\rho_t)$ 与 $(L,\rho)$ 是拟同构的。

## 记号

$(L,\rho)$：$\mathcal{F}(V)$ 的对象（定义 16）；$(L_t,\rho_t)$：$L$ 的小哈密顿形变，$t$ 在 $0$ 的邻域内；拟同构：定义 9 意义下非幺 $A_\infty$-预范畴的态射；$\mathcal{F}(V)=\mathcal{F}(V,\omega,J,\Omega)$。

## 要点

- 结论是拟同构而非同构：非幺 $A_\infty$-预范畴没有单位态射，只能用拟同构说「同一个对象」。
- 形变必须小：哈密顿量取得足够小，保证 $L_t$ 与 $L$ 横截相交、相应的 Floer 模空间随 $t$ 连续形变。
- 用途是延拓：单个对象组成的序列可延拓为横截序列 $\bigl((L_{t_1},\rho_{t_1}),(L,\rho)\bigr)$，任意有限个横截序列也可继续延拓。
- 这是命题 5 的前置：先在横截序列上把 $m_k$ 定义出来，才谈得上 $\eta\to0$ 的极限。

## 公式

$$\bigl((L_{t_1},\rho_{t_1}),(L,\rho)\bigr)$$

$$(L_t,\rho_t)\ \text{quasi-isomorphic}\ (L,\rho)$$

## 证明（sketch）

1. 取 $L$ 的小哈密顿形变 $L_t$，并把局部系 $\rho$ 沿哈密顿同痕搬运为 $\rho_t$。

   *为什么*：哈密顿同痕给出 $L$ 与 $L_t$ 之间保持定向的微分同胚，局部系可沿同痕拉回，故 $(L_t,\rho_t)$ 仍是 $\mathcal{F}(V)$ 的对象。

2. 在横截条件下比较两边的 Floer 复形，引用 Fukaya 的延拓定理得到拟同构。

   *为什么*：小形变使模空间与 Fredholm 指标连续形变，$m_1$-上同调不变，故左乘与右乘 $m_2$ 都是复形的拟同构。

> 缺口：原文未给证明，把依据写在命题之前：「延拓性质的证明基于 Fukaya 的如下结果（见 [Fu2]、[Se]）」（p31）。本文只陈述该结果并给出延拓的例子，Fukaya 的论证未复述，细节在其原文。

## 易错点

- 「小」不能去掉：大哈密顿形变可以改变 $L$ 的 Hamiltonian 同痕类，此时未必还有拟同构。
- 拟同构不是同构，不要写成 $(L_t,\rho_t)\cong(L,\rho)$；非幺框架里没有单位态射可比。
- 命题只保证经小形变后序列可延拓，不保证任意给定的两个拉格朗日子流形横截。

## 相关卡

- `kshms/concept/dfn-16-fukaya-objects`
- `kshms/concept/dfn-09-quasi-isomorphism`
- `kshms/concept/prp-05-fukaya-oh-limit-equivalence`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §5.1（原文 p.31）；锚点 `源码/chunks/ch05.tex:96-98（命题 4）`

> 原文 p31 §5.1；译文见 ch05.tex:94-100，原文把证明归于 [Fu2]、[Se]，并在同页给出横截序列延拓的例子。
