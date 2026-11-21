# 弦性 Hodge 数（$\alpha$-扭）

> `hausel22/concept/stringy-hodge-numbers` · 轨道 B · 拓扑镜像对称与 Hodge 数 · 状态 dev

> **先自测**：轨形上的 Hodge 数为什么要按不动点分别求和？

## 一句话

弦性 Hodge 数是轨形上按不动点分层、带费米子移位与 gerbe 扭转重新组合出的 Hodge 数，用来陈述拓扑镜像对称。

## 定义

对轨形 $\M^\vee=\M/\Gamma$ 与 gerbe $\alpha$，定义 $\alpha$-扭弦性 Hodge 数 $h_{st,\alpha}^{p,q}(\M^\vee):=\sum_{\gamma\in\Gamma}h^{p-F(\gamma);q-F(\gamma)}(H^{p+q-2F(\gamma)}(\M^\gamma;L_\alpha)^\Gamma)$，其中 $\M^\gamma$ 是 $\gamma$ 的不动点集，$L_\alpha$ 是 $\alpha$ 给出的扭层，$F(\gamma)$ 是费米子移位，由 $\gamma$ 在 $\M$ 的某个 $\gamma$-不动点处切空间上的作用定义。

**记号**：$\Gamma$；$\M^\gamma$；$F(\gamma)$；$L_\alpha$；$h^{p,q}_{st,\alpha}$。

## 要点（为什么需要它）

1. 轨形的「上同调」不是单个空间的上同调，而是各层不动点集上同调的组装；求和号正是这个组装。
2. $F(\gamma)$ 把上同调的次数平移 $2F(\gamma)$、把 Hodge 双次数同时平移 $F(\gamma)$，所以它不是普通的平移。
3. $\Gamma$-不变部分 $(-)^\Gamma$ 不能省：$\Gamma$ 作用在扭上同调上，只有不变部分才是轨形的贡献。
4. 普通（Chen–Ruan）弦性 Hodge 数对应 $\alpha$ 平凡的情形；这里的 $\alpha$ 是 $\PGL_n$ 侧真实存在的 gerbe，不能取平凡。

## 核心公式

$$
$$h_{st,\alpha}^{p,q}(\M^\vee):=\sum_{\gamma\in\Gamma}h^{p-F(\gamma);q-F(\gamma)}\big(H^{p+q-2F(\gamma)}(\M^\gamma;L_\alpha)^\Gamma\big)$$
$$

## 定理与证明（或缺口）

### 费米子移位的定义

设 $\gamma$ 在某个不动点处切空间上的特征值为 $e^{2\pi i\lambda_j}$，则 $F(\gamma)=\sum_j\lambda_j$ 为整数，称为费米子移位。

> 证明状态：**sketch**。原文只说「由 $\gamma$ 在某个不动点处切空间上的作用定义」，未写特征值公式，也未说明与不动点选取无关。

出处：`A p.2233`

## 常见误解

- 把 $F(\gamma)$ 当成「$\gamma$ 的阶」：它是特征值的相位和，与阶无关。
- 漏掉 $\Gamma$-不变上取：轨形的 Hodge 数取的是不变部分，不取会把 $\Gamma$ 的轨道重复计数。
- 弦性 Hodge 数与普通 Hodge 数的差别不只在移位，还在每个 $\gamma$ 层的扭层 $L_\alpha$。
- 把 $\alpha$ 取成平凡：$\PGL_n$ 侧的 gerbe 来自万有丛，非平凡是本质的，取平凡等于换了一个（错误的）猜想。

## 相关卡

[拓扑镜像对称](../concepts/topological-mirror-symmetry.md) · [从混合 Hodge 数到 $\alpha$-扭弦性 Hodge 数](../derivations/stringy-hodge-shift.md)

## 出处（印刷页）

- A p.2233（A p.2233）

> 说明：A=原文 §2.4 的定义式与费米子移位的定性说明；B=把「特征值相位和」这一展开补出来，并说明为什么是整数；C=与 Chen–Ruan 弦性 Hodge 数的对照是我们补的背景。最没把握处：原文未定义 $L_\alpha$ 的具体构造，只说「可以用 $\M$ 上的万有丛构造出来」。
