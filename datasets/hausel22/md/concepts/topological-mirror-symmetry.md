# 拓扑镜像对称

> `hausel22/concept/topological-mirror-symmetry` · 轨道 B · 拓扑镜像对称与 Hodge 数 · 状态 dev

> **先自测**：为什么镜像一侧必须用「弦性」Hodge 数，而不能直接用普通 Hodge 数？

## 一句话

拓扑镜像对称断言 Langlands 对偶的 Hitchin 模空间之间 Hodge 数相等，镜像一侧用弦性 Hodge 数并带 gerbe 扭转。

## 定义

取 $\G=\SL_n$、$\G^\vee=\PGL_n$。设 $\M=\M_\Dol$ 为 $\SL_n$ 稳定 Hitchin 对的模空间（$\det$ 固定、次数 $1$、$\Phi\in H^0(C;\End_0(E)\otimes K)$），$\Gamma:=\Jac_C[n]$ 作用其上，$\M^\vee:=\M/\Gamma$ 是轨形，并带 gerbe $\alpha\in H^2(\M^\vee,\U(1))\cong H^2(\M,\U(1))^\Gamma$。猜想 2.1：$h^{p,q}(\M)=h^{p,q}_{st,\alpha}(\M^\vee)$。

**记号**：$\M,\M^\vee$；$\Gamma=\Jac_C[n]$；$\alpha$；$h^{p,q}$；$h^{p,q}_{st,\alpha}$。

## 要点（为什么需要它）

1. 镜像一侧是轨形（orbifold），Hodge 数必须换成弦性 Hodge 数，否则两侧维数都对不上。
2. 弦性 Hodge 数带 $\alpha$-扭转：对每个 $\gamma\in\Gamma$ 取不动点集 $\M^\gamma$ 上的 $L_\alpha$-扭上同调，再作 $\Gamma$-不变部分。
3. 移位量 $F(\gamma)$ 是费米子移位，由 $\gamma$ 在某个不动点处切空间上的作用决定。
4. $\M_\Dol$ 与 $\M_\DR$ 的 Hodge 数相同（Hausel–Thaddeus），所以猜想同时也是关于 SYZ 镜像对 $\M_\DR,\M^\vee_\DR$ 的拓扑镜像对称。

## 核心公式

$$
$$h^{p,q}(\M)=h^{p,q}\big(H^{p+q}_c(\M)\big)$$$$h_{st,\alpha}^{p,q}(\M^\vee):=\sum_{\gamma\in\Gamma}h^{p-F(\gamma);q-F(\gamma)}\big(H^{p+q-2F(\gamma)}(\M^\gamma;L_\alpha)^\Gamma\big)$$
$$

$$
$$h_{st,\alpha}^{p,q}(\M^\vee):=\sum_{\gamma\in\Gamma}h^{p-F(\gamma);q-F(\gamma)}\big(H^{p+q-2F(\gamma)}(\M^\gamma;L_\alpha)^\Gamma\big)$$
$$

## 定理与证明（或缺口）

### 拓扑镜像对称猜想（Hausel–Thaddeus）

$h^{p,q}(\M)=h_{st,\alpha}^{p,q}(\M^\vee)$，即 $\SL_n$ 侧混合 Hodge 数等于 $\PGL_n$ 侧 $\alpha$-扭弦性 Hodge 数。

> 证明状态：**sketch**。原文只综述，不展开证明；三个证明路径都在综述层面，细节须查原文引文。

出处：`A p.2233`

## 常见误解

- 镜像一侧是轨形 $\M/\Gamma$，不能直接对它用普通 Hodge 理论；必须用弦性 Hodge 数。
- 弦性 Hodge 数不是「$\M^\gamma$ 的 Hodge 数之和」：还要作 $F(\gamma)$ 的移位、取 $\Gamma$-不变部分、并扭上 $L_\alpha$。
- 猜想说的是 $\M$（$\SL_n$）与 $\M^\vee$（$\PGL_n$）之间的 Hodge 数相等，方向写反会把 $\alpha$-扭转挪到错误的一侧。
- $\M^\vee=\M/\Gamma$ 里 $\Gamma=\Jac_C[n]$，不是整个 $\Jac_C$；$n$ 是 $\SL_n$ 的秩。

## 相关卡

[弦性 Hodge 数（$\alpha$-扭）](../concepts/stringy-hodge-numbers.md) · [镜像对称（三个方面）](../concepts/mirror-symmetry.md) · [Hitchin 系统](../concepts/hitchin-system.md) · [从混合 Hodge 数到 $\alpha$-扭弦性 Hodge 数](../derivations/stringy-hodge-shift.md)

## 出处（印刷页）

- A p.2232–2233（A p.2233）
- A p.2233（A p.2233 eq (2.4)）

> 说明：A=原文 §2.4 的定义与猜想陈述；B=把三个证明路径（HT、GWZ、Maulik–Shen）并列；C=「维数对不上」的解释是我们按弦性 Hodge 数的定义补的。最没把握处：费米子移位 $F(\gamma)$ 的符号约定，原文只给出「由作用定义」而未写公式。
