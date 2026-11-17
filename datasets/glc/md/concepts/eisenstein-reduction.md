---
id: glc/concept/eisenstein-reduction
type: concept
track: H
---

# Eisenstein 生成的子范畴与尖点归约

> 设真 Levi 的 Langlands 等价已成立，则 $\mathbb L_G$ 在 Eisenstein 直和因子上是等价 (16.5)，整体问题归约到尖点部分。

**问题**：(16.5) 的等价是无条件的吗？

## 定义

令 $\operatorname{DMod}(\operatorname{Bun}_G)_{\mathrm{Eis}}$ 为由真抛物子群 $P$ 对应的 $\operatorname{Eis}_P(\operatorname{DMod}(\operatorname{Bun}_M))$ 生成的子范畴，令 $\operatorname{LocSys}^{\mathrm{red}}_{\check G}\subset\operatorname{LocSys}_{\check G}$ 为可约轨迹，即所有真抛物子群 $\check P$ 对应的 $\operatorname{LocSys}_{\check P}\to\operatorname{LocSys}_{\check G}$ 的像的并。等价地，这些局部系统容许真抛物约化；其补集是不可约轨迹 $\operatorname{LocSys}^{\mathrm{irr}}_{\check G}$。

*记号*：$\mathbb L^L_G$、$\mathbb L^R_G$ 分别为 $\mathbb L_G$ 在相关直和因子上限制后的左、右伴随；$\operatorname{QCoh}^!(\operatorname{LocSys}_{\check G})_{\mathrm{red}}$ 为可约轨迹上的重整化谱目标。

## 要点

- 需要证明粗函子 $\mathbb L_G^0$ 有左伴随；要点是只需在生成对象上构造左伴随。
- 在谱侧，生成对象来自 $\operatorname{Eis}^{\mathrm{spec}}_{\check P}(\operatorname{QCoh}(\operatorname{LocSys}_{\check M}))$，而 Eisenstein 相容性通过从 $M$ 输运伴随，给出所需的自守函子。
- 等价地，转到 Ran 作用描述后，粗函子已经有左伴随：$\operatorname{Rep}(\check M)_{\mathrm{Ran}}$ 作用于自守侧，而商 $\operatorname{Rep}(\check M)_{\mathrm{Ran}}\to\operatorname{QCoh}(\operatorname{LocSys}_{\check M})$ 识别谱作用。
- 假设每个真 Levi 子群 $M$ 的 Langlands 等价已经成立，则 $\mathbb L_G$ 在 Eisenstein 直和因子上诱导等价 (16.5)：$\mathbb L_G:\operatorname{DMod}(\operatorname{Bun}_G)_{\mathrm{Eis}}\xrightarrow{\sim}\operatorname{QCoh}^!(\operatorname{LocSys}_{\check G})_{\mathrm{red}}$。
- 于是整体猜想被归约到尖点部分，剩余陈述为 $\mathbb L_{G,\mathrm{cusp}}:\operatorname{DMod}(\operatorname{Bun}_G)_{\mathrm{cusp}}\xrightarrow{\sim}\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G})$。
- $\operatorname{LocSys}^{\mathrm{irr}}_{\check G}$ 是不可约局部系统的开子叠，即不容许约化到真抛物子群 $\check P\subsetneq\check G$ 的局部系统。

## 关键公式

- $\mathbb L_G:\operatorname{DMod}(\operatorname{Bun}_G)_{\mathrm{Eis}}\xrightarrow{\sim}\operatorname{QCoh}^!(\operatorname{LocSys}_{\check G})_{\mathrm{red}}$（式 (16.5)）
- $\mathbb L_{G,\mathrm{cusp}}:\operatorname{DMod}(\operatorname{Bun}_G)_{\mathrm{cusp}}\xrightarrow{\sim}\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G})$
- $\operatorname{Rep}(\check M)_{\mathrm{Ran}}\longrightarrow\operatorname{QCoh}(\operatorname{LocSys}_{\check M})$

## 定理与证明

### 式 (16.5)：Eisenstein 直和因子上的等价（要点（有缺口））

假设每个真 Levi 子群 $M$ 的 Langlands 等价已经成立，则 $\mathbb L_G:\operatorname{DMod}(\operatorname{Bun}_G)_{\mathrm{Eis}}\xrightarrow{\sim}\operatorname{QCoh}^!(\operatorname{LocSys}_{\check G})_{\mathrm{red}}$。

1. 在生成对象 $\operatorname{Eis}^{\mathrm{spec}}_{\check P}(\operatorname{QCoh}(\operatorname{LocSys}_{\check M}))$ 上构造 $\mathbb L_G^0$ 的左伴随。  
   *为什么*：左伴随只需在生成对象上给出；谱侧生成对象的结构已知，Eisenstein 相容性把 $M$ 侧的伴随输运到 $G$ 侧。
2. 用归纳假设（每个真 Levi 的 Langlands 等价）识别这些生成对象上的函子。  
   *为什么*：$M$ 是 $G$ 的真 Levi，归纳假设适用；逐因子比较即得 (16.5)。

> 缺口：讲义只述 (16.5) 依赖 (16.1)、(16.2) 与对真 Levi 的归纳，未展开细节；见 [CCF24]。

*出处*：§16.6 式 (16.5) / 原书 p.80


## 易错点

- (16.5) 是有条件的：假设每个真 Levi 子群 $M$ 的 Langlands 等价已经成立；把它当成无条件定理会构成循环论证。
- $\operatorname{LocSys}^{\mathrm{red}}_{\check G}$ 是可约轨迹，它的补集 $\operatorname{LocSys}^{\mathrm{irr}}_{\check G}$ 才是尖点等价的目标；不要把 $\operatorname{QCoh}^!(\operatorname{LocSys}_{\check G})_{\mathrm{red}}$ 与整个 $\operatorname{QCoh}^!(\operatorname{LocSys}_{\check G})$ 混淆。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§16.6 伴随与 Eisenstein 生成的部分，p.80-81（PDF p.80-81），`源码/chapters/ch16.tex:137-157（Eisenstein 生成子范畴、式 16.5 与尖点归约）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv:2409.07051 (CCF24)：https://arxiv.org/abs/2409.07051 — 原文：「Let us assume that GLC is valid for Levi subgroups of all proper parabolics of G. Then the adjoint functors 𝕃_G: Dmod_{1/2}(Bun_G)_Eis ⇄ IndCoh_Nilp(LS_Ĝ)_red: 𝕃_G^L are mutually inverse equivalences.」——与卡 (16.5) 及同一假设逐字对应。
- arXiv:2409.07051 (CCF24)：https://arxiv.org/abs/2409.07051 — 原文把 𝕃_G 与左伴随 𝕃_G^L 作为一对互逆函子陈述，支持卡对 𝕃_G^L、𝕃_G^R 的限制描述。

## 关联

- `glc/concept/eisenstein-compatibility`
- `glc/concept/cuspidal-conservativity`
- `glc/concept/global-langlands-functor`
