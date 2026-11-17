---
id: glc/concept/restricted-variant-formal-model
type: concept
track: G
---

# 受限变体的形式局部模型

> 在 $\mathbb C$ 上，受限变体以半单化处的形式完备化 $(\pi^{-1}(\bar\sigma))^\wedge$ 为局部模型；这只是形式局部描述，不是代数同构。

**问题**：为什么 $\operatorname{LocSys}^{\mathrm{restr}}_{\check G}$ 不能理解成 $\operatorname{LocSys}^{\mathrm{dR}}_{\check G}$ 的字面代数对应物？

## 定义

在 $\mathbb C$ 上，受限变体最好被看作 Betti 叠的形式细化，通过 Riemann–Hilbert 对应可以在解析意义下与 de Rham 图景比较。有自然映射
$$\operatorname{LocSys}^{\mathrm{restr}}_{\check G}\longrightarrow\operatorname{LocSys}^{\mathrm{Betti}}_{\check G}.$$
粗略地说，若 $\pi:\operatorname{LocSys}^{\mathrm{Betti}}_{\check G}\to\operatorname{LocSys}^{\mathrm{coarse}}_{\check G}$ 表示到半单局部系统的 GIT 粗模空间的映射，则在一个半单化 $\bar\sigma$ 的局部，受限变体以形式完备化 $(\pi^{-1}(\bar\sigma))^\wedge$ 为模型。

*记号*：$\operatorname{LocSys}^{\mathrm{coarse}}_{\check G}$ 为半单局部系统的 GIT 粗模空间；$\bar\sigma$ 为一个半单化参数；$({-})^\wedge$ 表示形式完备化；$\pi^{-1}(\bar\sigma)$ 为纤维。

## 要点

- 存在自然映射 $\operatorname{LocSys}^{\mathrm{restr}}_{\check G}\to\operatorname{LocSys}^{\mathrm{Betti}}_{\check G}$。
- 在半单化 $\bar\sigma$ 的局部，受限变体以形式完备化 $(\pi^{-1}(\bar\sigma))^\wedge$ 为模型。
- 这是一个形式局部描述，并非所有这类完备化的普通不交并。
- 在该描述中 $\pi(\sigma_1)=\pi(\sigma_2)$ 当且仅当 $\sigma_1$ 与 $\sigma_2$ 具有相同的半单化。
- de Rham 对应物只有经过解析 Riemann–Hilbert 比较才能得到，因此不应将它理解为字面上的代数映射 $\operatorname{LocSys}^{\mathrm{restr}}\to\operatorname{LocSys}^{\mathrm{dR}}$。

## 关键公式

- $$\operatorname{LocSys}^{\mathrm{restr}}_{\check G}\longrightarrow\operatorname{LocSys}^{\mathrm{Betti}}_{\check G}$$
- $$\operatorname{LocSys}^{\mathrm{restr}}_{\check G}\ \text{局部模型}\ (\pi^{-1}(\bar\sigma))^\wedge$$

## 定理与证明

### 受限变体的形式局部刻画（要点（有缺口））

若 $\pi:\operatorname{LocSys}^{\mathrm{Betti}}_{\check G}\to\operatorname{LocSys}^{\mathrm{coarse}}_{\check G}$ 为到半单局部系统 GIT 粗模空间的映射，则在半单化 $\bar\sigma$ 的局部，$\operatorname{LocSys}^{\mathrm{restr}}_{\check G}$ 以 $(\pi^{-1}(\bar\sigma))^\wedge$ 为模型。

1. 把 Betti 叠按半单化分层，取半单局部系统粗模空间的 GIT 商。  
   *为什么*：半单化是模叠上由 Jordan 型决定的等价关系。
2. 在每层上取纤维的形式完备化，作为受限变体的局部模型。  
   *为什么*：受限变体只保留沿零奇异支撑方向的形变。

> 缺口：讲义只给「粗略地说」的形式局部描述（p.62），未给证明；并明确声明它不是所有完备化的普通不交并。

*出处*：注（§12.5，讲义无编号） / 原书 p.62


## 易错点

- 不要把这句话反过来用：受限变体不是「所有 $(\pi^{-1}(\bar\sigma))^\wedge$ 的不交并」，也不是字面上的代数映射 $\operatorname{LocSys}^{\mathrm{restr}}\to\operatorname{LocSys}^{\mathrm{dR}}$——后者只经解析 Riemann–Hilbert 比较才存在。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§12.5 其他层理论与受限变体，p.62（PDF p.62），`源码/chapters/ch12.tex:103-108（形式局部模型，§12.5）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — LocSys^restr→LocSys 在 de Rham/Betti 两边都等同于按固定半单化取形式完备化的不交并；Betti 情形这些闭子叠正是 r:LocSys→LocSys^coarse 的纤维。
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — LocSys^restr 有粗模空间，其连通分支是形式仿射概形。

## 关联

- `glc/concept/restricted-spectral-stack`
- `glc/concept/betti-local-systems`
