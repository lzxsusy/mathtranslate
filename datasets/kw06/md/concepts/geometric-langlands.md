# 几何 Langlands 对应

> `kw/concept/geometric-langlands` · 轨道 E · Langlands 与翻译器 · 状态 dev

> **先自测**：几何 Langlands 对应断言什么，本文的物理推导还缺哪一环？

## 一句话

曲线 $C$ 上的几何对应：$^L G$ 的局部系统对应 $\mathrm{Bun}_G$ 上的 Hecke 特征 D-模；本文用扭化 $\mathcal N=4$ 的膜范畴给它一个物理来源。

## 定义

几何 Langlands 对应断言：$C$ 上 $^L G$ 的局部系统（等价地 $\mathrm{Bun}_{{}^LG}$ 上的 D-模）与 $\mathrm{Bun}_G$ 上的 Hecke 特征层（holonomic D-模）之间存在自然对应。本文用扭化 $\mathcal N=4$ 理论的 S-对偶与膜范畴给出它的物理来源，但只处理非分歧情形。

**记号**：$^L G$：Langlands 对偶群；$\mathrm{Bun}_G$：$G$-丛的模栈；$\vartheta$：$\pi_1(C)\to{}^LG_{\mathbb C}$ 的同态。

## 要点（为什么需要它）

1. 它是全文的靶心：§1 列为第四个主要想法，§8–§11 逐步搭物理实现。
2. 它把规范理论翻译成表示论：$^L G$ 局部系统对应 $\mathrm{Bun}_G$ 上的 Hecke 特征层。
3. 本文的贡献是把 Hecke 特征层实现为磁特征膜（type F），但 type F 住在 $M_H(G,C)$、D-模住在 $M(G,C)$，还缺一环。
4. 严格陈述与证明属于几何 Langlands 文献；本文给的是物理动机与一致性检验。

## 核心公式

$$
$\vartheta:\pi_1(C)\to{}^LG_{\mathbb C}\ \longleftrightarrow\ \mathcal F_\vartheta\in \mathrm{D}\text{-}\mathrm{mod}(\mathrm{Bun}_G)$$\mathbb H_x^V(\mathcal F_\vartheta)\cong V\otimes\mathcal F_\vartheta$
$$

$$
$\mathbb H_x^V(\mathcal F_\vartheta)\cong V\otimes\mathcal F_\vartheta$
$$

## 定理与证明（或缺口）

### 几何 Langlands 的物理实现（主断言）

对每个半稳定的同态 $\vartheta:\pi_1(C)\to{}^LG_{\mathbb C}$，存在 $M(G,C)$ 上一个非零层，它同时是 Hecke 特征层与 holonomic D-模。

> 证明状态：**gap**。原文 p.122 把它称为 program 的 main claim，并预告 §9–§11 解释 type F 膜为何有正确性质；本文未给证明，作者自承只看到“a glimmering”。

出处：`B p.122`

## 常见误解

- 把几何 Langlands 当成本文已证明的定理；本文只给物理推导，严格证明在数学文献里。
- 把 $\mathrm{Bun}_G$（所有 $G$-丛的栈）与 $M(G,C)$（稳定 Higgs 丛）混同。
- 把两端弄反：$^L G$ 局部系统对应 $\mathrm{Bun}_G$ 上的 Hecke 特征层，而非 $\mathrm{Bun}_{{}^LG}$ 上。

## 相关卡

[Hecke 特征层](../concepts/hecke-eigensheaf.md) · [Hecke 算子](../concepts/hecke-operator.md) · [D-模](../concepts/d-module.md) · [从 GNO 对偶群到 Langlands 对偶群](../derivations/gno-to-langlands.md)

## 出处（印刷页）

- B p.4–5（B p.4–5）
- B p.122（B p.122）
- B p.184（B p.184）

> 说明：A=原文 p.122 的主断言与 p.4–5 的定位；B=把 $M_H$ 上的 type F 膜与 $\mathrm{Bun}_G$ 上的层对应；C=“还缺一环”的判断来自 p.184 的自述。
