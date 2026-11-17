---
id: glc/concept/restricted-spectral-stack
type: concept
track: G
---

# 受限谱叠 $\operatorname{LocSys}^{\mathrm{restr}}_{\check G}$

> 由带右 $t$-正合条件的幺半函子给出的点函子所定义的谱叠，是可构造与 $\ell$-进情形中正确的谱对象。

**问题**：$\operatorname{LocSys}^{\mathrm{restr}}_{\check G}$ 的定义里，为什么必须加右 $t$-正合条件？

## 定义

在可构造情形，范畴 $\operatorname{LocSys}(X(\mathbb C))$ 过大，正确的替代是 $\operatorname{QLisse}(X):=\operatorname{Shv}_0(X)$，其中下标表示零奇异支撑。按以下点函子规则定义受限变体：
$$\operatorname{LocSys}^{\mathrm{restr}}_{\check G}(S):=\operatorname{Fun}^{\otimes,\mathrm{r.t.ex.}}\bigl(\operatorname{Rep}(\check G),\operatorname{QLisse}(S\times X)\bigr).$$

*记号*：$\operatorname{QLisse}(S\times X)$ 为 §11.3–11.4 的拟光滑层范畴；$\operatorname{Fun}^{\otimes,\mathrm{r.t.ex.}}$ 表示保持张量积且右 $t$-正合的函子；$\mathrm{Shv}_0$ 为零奇异支撑层。

## 要点

- 在 AGKRRV 的构造 [AGK20a] 中，$\operatorname{QLisse}(X)$ 更准确地说是 $\operatorname{Ind}(\operatorname{Lisse}(X))$ 的左完备化，其中 $\operatorname{Lisse}(X)$ 表示所选层理论中的有限秩局部系统。
- 因此这种限制并非「只允许有限秩」：它保留拟光滑部分，而移除具有非零微局部支撑的层。
- 记号 $\mathrm{r.t.ex.}$ 意为右 $t$-正合；它是普通 Betti 叠中张量函子右正合条件的可构造对应版本。
- 对仿射测试概形，目标常被启发性地写为 $\operatorname{QCoh}(S)\otimes\operatorname{QLisse}(X)$；要点是这个族只允许沿 $X$ 在零奇异支撑方向（光滑方向）变动。

## 关键公式

- $$\operatorname{LocSys}^{\mathrm{restr}}_{\check G}(S):=\operatorname{Fun}^{\otimes,\mathrm{r.t.ex.}}\bigl(\operatorname{Rep}(\check G),\operatorname{QLisse}(S\times X)\bigr)$$
- $$\operatorname{QLisse}(X):=\operatorname{Shv}_0(X)$$
- $$\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{restr}}_{\check G})\curvearrowright\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$$

## 定理与证明

### 受限谱叠的作用（要点（有缺口））

在任何定义了 $\operatorname{Shv}_{\mathrm{Nilp}}$ 的可构造或 $\ell$-进情形中，局部到整体定理给出作用 $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{restr}}_{\check G})\curvearrowright\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$。

1. 把 Betti 局部到整体定理中的 $\operatorname{Rep}(\check G)$-作用限制到拟光滑方向。  
   *为什么*：受限变体的点函子正是带右 $t$-正合条件的幺半函子。
2. 对可构造/ℓ-进层理论重复同一构造。  
   *为什么*：定理在这些层论背景下有相应版本（§12.5 所列）。

> 缺口：讲义只述该作用由局部到整体定理给出（p.62），未在此证明；具体验证见 [AGK20a]。

*出处*：定义与命题（§12.5，讲义无编号） / 原书 p.62


## 易错点

- 右 $t$-正合条件不能省：它是 §12.5 定义的一部分（讲义用 $\mathrm{r.t.ex.}$ 明确标注）；去掉它，点函子就不再是受限变体的点函子。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§12.5 其他层理论与受限变体，p.62（PDF p.62），`源码/chapters/ch12.tex:80-101（QLisse 与受限变体的定义，§12.5）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — Lisse(X)=有限秩局部系统；QLisse(X)=IndLisse(X) 的左完备化（P^1 处 IndLisse≠QLisse）；S-点为右 t-正合对称幺半函子 Rep(Ĝ)→A-mod⊗QLisse(X)。
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — QLisse(X)=Shv_{0}(X)，即零奇异支撑层。
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — QCoh(LocSys^restr) 作用在 Shv_Nilp(Bun_G) 上，且 Rep(Ĝ)⊗QCoh(LocSys^restr)→QLisse(X)。

## 关联

- `glc/concept/hecke-lisse-sheaves`
- `glc/concept/restricted-categorical-langlands`
- `glc/concept/quasi-lisse-sheaves`
