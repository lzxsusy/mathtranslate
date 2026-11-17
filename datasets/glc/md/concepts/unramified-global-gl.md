---
id: glc/concept/unramified-global-gl
type: concept
track: O
---

# 非分歧整体几何 Langlands 对应（猜想）

> 对每个几何不可约的 $\check{G}$-局部系统 $\sigma$，$\operatorname{Bun}_G$ 上应存在唯一以 $\sigma$ 为特征值的 Hecke 特征层 $\operatorname{Aut}_\sigma$。

**问题**：非分歧整体几何 Langlands 猜想对 $\sigma$ 附加了什么条件，$\operatorname{GL}_n$ 情形的存在性已知到什么程度？

## 定义

设定：$X$ 是完美域 $k$ 上光滑、完备、几何连通的曲线，$K=K(X)$ 是其函数域；$G$ 是 $k$ 上的分裂约化群，$\check{G}$ 是它的 Langlands 对偶群；固定一种合理的层理论，其系数域 $e$ 代数闭（Betti 情形用复拓扑下的反常层，$\ell$-进情形用反常 $\ell$-进 Weil 层，de Rham 情形用凝聚右 $D$ 模）。称 $\sigma$ 几何不可约，是指基变换到 $\bar k$ 后，相应的 $\check{G}$-局部系统不存在到 $\check{G}$ 的真抛物子群的平坦约化；对 $G=\operatorname{GL}_n$，这就是秩 $n$ 局部系统通常意义下的不可约性。猜想断言：对每个几何不可约的 $\check{G}$-局部系统 $\sigma$，在 $\operatorname{Bun}_G$ 上都存在本质唯一的 Hecke 特征层 $\operatorname{Aut}_\sigma$，其特征值为 $\sigma$（Hecke 特征层的一般定义见 §2.6 定义 2.6.1）。

*记号*：$\operatorname{Bun}_G$：$X$ 上 $G$ 丛的模叠；$\check{G}$：Langlands 对偶群；$\operatorname{LocSys}_{\check{G}}(X)$：$X$ 上 $\check{G}$-局部系统的模对象；$e$：层理论的系数域；$\operatorname{Shv}_c(\operatorname{Bun}_G)$：$\operatorname{Bun}_G$ 上相应层理论的（导出）范畴，$\operatorname{Shv}_c(\operatorname{Bun}_G)^\heartsuit$ 为其 $t$-结构的心。

## 要点

- 猜想的对象是 $\check{G}$-局部系统而不是 $G$-局部系统：对于与 $G$ 相联系的自守层，实际特征值是系数域 $e$ 上 Langlands 对偶群 $\check{G}$ 的局部系统。
- 「几何不可约」比不可约更强：基变换到 $\bar k$ 后不存在到 $\check{G}$ 的真抛物子群的平坦约化；对 $G=\operatorname{GL}_n$ 它退化为秩 $n$ 局部系统的通常不可约性。
- 若 $\sigma$ 可约，预期得到的是 $\operatorname{Shv}_c(\operatorname{Bun}_G)$ 中的 Hecke 特征对象，而不是心中的特征层，且本质唯一性不再成立。
- 对 $G=\operatorname{GL}_n$ 存在性定理已成立：$n=1$ 由 Deligne、$n=2$ 由 Drinfeld、一般情形由 Frenkel–Gaitsgory–Vilonen 证明 [FGKV98]。
- $\ell$-进情形对 $\operatorname{Aut}_\sigma$ 取 Frobenius 迹得到自守函数；由 $\operatorname{Aut}_\sigma$ 得到的函数是尖点函数。

## 关键公式

- $\{\text{几何不可约的}\ \check{G}\text{-局部系统}\ \sigma\}\ \longmapsto\ \operatorname{Aut}_\sigma\in\operatorname{Shv}_c(\operatorname{Bun}_G)^\heartsuit$
- $\operatorname{Bun}_G(k)\simeq G(K)\backslash G(\mathbb{A}_K)/G(\mathcal{O}_K)$
- $G(K)\backslash G(\mathbb{A}_K)/G(\mathcal{O}_K)\ \longleftrightarrow\ \{X\ \text{上主}\ G\ \text{丛的同构类}\}$

## 定理与证明

### 猜想 1.2.3（非分歧整体几何 Langlands）（要点（有缺口））

对 $X$ 上每个几何不可约的 $\check{G}$-局部系统 $\sigma$，在 $\operatorname{Bun}_G$ 上都存在本质唯一的 Hecke 特征层 $\operatorname{Aut}_\sigma$，其特征值为 $\sigma$。


> 缺口：这是猜想：讲义未证明。$\operatorname{GL}_n$ 情形 $n=1$ 为 Deligne、$n=2$ 为 Drinfeld、一般情形为 [FGKV98]，讲义均未给出证明。

*出处*：猜想 1.2.3 / 原书 p.8


## 易错点

- 几何不可约不是「不可约」的重复：它要求基变换到 $\bar k$ 后没有到真抛物子群的平坦约化；可约情形预期的是 $\operatorname{Shv}_c(\operatorname{Bun}_G)$ 中的特征对象，而不是心中的层。
- 特征值是 $\check{G}$-局部系统，不是 $G$-局部系统；$\check{G}$ 的出现是因为 Hecke 函子取值于 $\operatorname{Rep}(\check{G})$，由 $V$ 与 $\sigma$ 造出 $X$ 上的局部系统 $V_\sigma$。
- 本质唯一性在 $\sigma$ 可约时失效；不要把它读成对所有 $\sigma$ 都成立的唯一性断言。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§1.2 非分歧整体几何 Langlands 对应，p.8（PDF p.8），`源码/chapters/ch01.tex:171-173（猜想 1.2.3）；可约情形的说明见 175 行`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/geometric+Langlands+correspondence — 页面给出原初 BD 猜想 DMod(Bun_G(Σ))≃QCoh(Loc_{^L G}(Σ))，并说典范等价把左端摩天层送到 Hecke 特征层；abelian case 已证，一般情形对 SL_2、P^1 为假，需 Arinkin–Gaitsgory 的幂零支撑修正。这支持猜想的总体形状，但没有「几何不可约 σ ⇒ 本质唯一 Aut_σ」的逐字陈述。

## 关联

- `glc/concept/hecke-eigensheaf-general`
- `glc/concept/bun-g-artin-stack`
- `glc/concept/cuspidal-de-rham`
