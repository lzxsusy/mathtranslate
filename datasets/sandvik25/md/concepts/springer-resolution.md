# Springer 解消 $\widetilde{\mathcal N}$ 与线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$

> `sandvik25/concept/springer-resolution` · 轨道 B · Springer 侧与三造函子 · 状态 dev

> **先自测**：Springer 解消的线丛为什么按 $X^\vee$ 编号，哪些对象生成了它的等变凝聚层范畴？

## 一句话

$\widetilde{\mathcal N}=G^\vee\times_{B^\vee}\mathfrak n^\vee$ 是 $G^\vee$-等变的 Springer 解消，其上的线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 与 $V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 生成 $\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$。

## 定义

设 $\mathcal N$ 为 $G^\vee$ 的幂零锥，$\widetilde{\mathcal N}:=G^\vee\times_{B^\vee}\mathfrak n^\vee$，带矩映射 $\mu\colon\widetilde{\mathcal N}\to\mathcal N$ 与投影 $\widetilde{\mathcal N}\to G^\vee/B^\vee$；后者使 $\widetilde{\mathcal N}$ 成为 $G^\vee/B^\vee$ 上的向量丛，且是 $\mathfrak g^\vee\times G^\vee/B^\vee$ 的子向量丛。对 $\lambda\in X^\vee$ 记 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 为 $\mathcal O_{G^\vee/B^\vee}(\lambda)$ 的拉回。

**记号**：$\mathfrak n^\vee\subset\mathfrak g^\vee$ 为幂零根，$B^\vee\subset G^\vee$ 为 Borel；$X^\vee$ 为余根格（$G^\vee$ 的权格）。

## 要点（为什么需要它）

1. $\lambda$ 的编号来自 $G^\vee/B^\vee$ 上的特征线丛：$\lambda\in X^\vee=X_*(T^\vee)$，所以 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 是「$T^\vee$ 权」的几何化。
2. 引理 3.1.1 的第 (1) 类与第 (2) 类并不对称：前者 $\lambda$ 任意、后者 $\lambda$ 须支配（$\lambda\in X^\vee_+$）。支配性是「$V\otimes$」能张成剩余部分的原因。
3. Springer 解消同时是从 $\widetilde{\mathcal N}$ 到 $\mathcal N$ 的紧合映射与到旗簇的向量丛：两个结构各用一次，前者给紧合性，后者给线丛与 $T^\vee$ 作用。
4. 此范畴的 $K$ 群正是反球模 $M^{\mathrm{asph}}$（式 (2)），所以这一节在几何侧重现了 §2 的模论骨架。

## 核心公式

$$
$\widetilde{\mathcal N}=G^\vee\times_{B^\vee}\mathfrak n^\vee$$\mu\colon\widetilde{\mathcal N}\to\mathcal N,\qquad \widetilde{\mathcal N}\to G^\vee/B^\vee$（向量丛）
$$

$$
$\mu\colon\widetilde{\mathcal N}\to\mathcal N,\qquad \widetilde{\mathcal N}\to G^\vee/B^\vee$（向量丛）
$$

## 定理与证明（或缺口）

### 引理 3.1.1（生成元）

$\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$ 由 (1) 线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$（$\lambda\in X^\vee$）与 (2) $V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)$（$V\in\mathrm{Rep}(G^\vee)$、$\lambda\in X^\vee_+$）共同生成。

> 证明状态：**gap**。原文只陈述，不证；这是 Springer 解消上等变凝聚层的标准生成性结果。

出处：`A p.6`

## 常见误解

- 把 $\widetilde{\mathcal N}$ 与其矩映射的像 $\mathcal N$ 搞混：前者光滑、是向量丛，后者才是奇异的幂零锥；所有「凝聚层」都活在前者上。
- 线丛编号用 $X^\vee$，而 Wakimoto 层与 IW 标准层的编号也用 $X^\vee$——三处编号必须是同一套，否则定理 5.0.1 的对象对应会错位。

## 相关卡

[反球模 $M^{\mathrm{asph}}$](../concepts/antispherical-module.md) · [无穷小稳定化子 $\widehat{\mathcal N}$ 与 $\widehat{\mathcal N}_X$](../concepts/hat-n-x.md) · [函子 III：$F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b\mathcal P_I$](../concepts/functor-f3.md)

## 出处（印刷页）

- A p.6（A p.6）

> 说明：定义与引理 3.1.1 均在 p.6；$\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 的编号沿用 §2.5 的 $X^\vee$。
