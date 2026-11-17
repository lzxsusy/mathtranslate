---
id: glc/concept/hecke-eigensheaf-oper
type: concept
track: G
---

# Beilinson–Drinfeld 定理：$\operatorname{Aut}_\sigma$ 是 Hecke 特征层

> 对每个 $V\in\operatorname{Rep}(\check G)$，$H_{V,x}$ 在 $\operatorname{Aut}_\sigma$ 上等于张量 $V_{\sigma,x}$，故它是 Hecke 特征层。

**问题**：定理 14.5.1 的 Hecke 特征性质写成哪个等式，证明里 Beilinson–Drinfeld 局部化起什么作用？

## 定义

定理 14.5.1（Beilinson–Drinfeld [BD91]）：$\operatorname{Aut}_\sigma$ 是特征值为 $\sigma$ 的 Hecke 特征层。等价地，对每个 $x\in X$ 及每个 $V\in\operatorname{Rep}(\check G)$，$H_{V,x}(\operatorname{Aut}_\sigma)\simeq V_{\sigma,x}\otimes\operatorname{Aut}_\sigma$，其中 $H_{V,x}$ 是对应于 $V$ 的 Hecke 函子，而 $V_{\sigma,x}$ 是由 $V$ 和 $\sigma$ 关联的局部系统在 $x$ 处的纤维。

*记号*：$H_{V,x}$ 为对应 $V\in\operatorname{Rep}(\check G)$ 的 Hecke 函子；$V_{\sigma,x}$ 为相应局部系统在 $x$ 处的纤维；$\operatorname{Aut}_\sigma=\mathcal D_{\mathrm{crit}}\otimes_{A,\sigma}k_\sigma$；$\operatorname{Sat}_x(V)$ 为 $V$ 在 $x$ 处的几何 Satake 对象。

## 要点

- 特征性质对每个 $x\in X$ 与每个 $V\in\operatorname{Rep}(\check G)$ 断言。
- $V_{\sigma,x}$ 是相应局部系统在 $x$ 处的纤维，随 $x$ 变动。
- 证明用 Beilinson–Drinfeld 局部化 $\operatorname{Loc}_x:\widehat{\mathfrak g}_{\mathrm{crit},x}\text{-}\mathrm{Mod}^{G[[t]]}\to\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$，满足 $\operatorname{Loc}_x(\mathbb V_{\mathrm{crit},x})\simeq\mathcal D_{\mathrm{crit}}$。
- Hecke 作用与局部化相容：$\operatorname{Sat}_x(V)\star\mathcal D_{\mathrm{crit}}\simeq\operatorname{Loc}_x(\operatorname{Sat}_x(V)\star\mathbb V_{\mathrm{crit},x})\simeq\operatorname{Loc}_x\bigl(F_{D_x}(V)\otimes_{\mathfrak z_{\mathrm{crit}}(D_x)}\mathbb V_{\mathrm{crit},x}\bigr)$。
- 把 $F_{D_x}$ 认成 $\operatorname{Op}_{\check G}(X)$ 上普遍挠子的限制，再沿 $k_\sigma$ 作张量，即得 Hecke 特征性质。

## 关键公式

- $H_{V,x}(\operatorname{Aut}_\sigma)\simeq V_{\sigma,x}\otimes\operatorname{Aut}_\sigma$
- $\operatorname{Loc}_x:\widehat{\mathfrak g}_{\mathrm{crit},x}\text{-}\mathrm{Mod}^{G[[t]]}\longrightarrow\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G),\qquad \operatorname{Loc}_x(\mathbb V_{\mathrm{crit},x})\simeq\mathcal D_{\mathrm{crit}}$
- $\operatorname{Sat}_x(V)\star\mathcal D_{\mathrm{crit}}\simeq V_{\mathcal F,x}\otimes_A\mathcal D_{\mathrm{crit}},\qquad \operatorname{Sat}_x(V)\star\operatorname{Aut}_\sigma\simeq V_{\sigma,x}\otimes\operatorname{Aut}_\sigma$

## 定理与证明

### 定理 14.5.1（Beilinson–Drinfeld）（完整）

$\operatorname{Aut}_\sigma$ 是特征值为 $\sigma$ 的 Hecke 特征层：对每个 $x\in X$ 及每个 $V\in\operatorname{Rep}(\check G)$，$H_{V,x}(\operatorname{Aut}_\sigma)\simeq V_{\sigma,x}\otimes\operatorname{Aut}_\sigma$。

1. 用 Beilinson–Drinfeld 局部化 $\operatorname{Loc}_x$，它满足 $\operatorname{Loc}_x(\mathbb V_{\mathrm{crit},x})\simeq\mathcal D_{\mathrm{crit}}$。  
   *为什么*：真空模在局部化下的像就是临界扭转微分算子层。
2. 对 $V\in\operatorname{Rep}(\check G)$，Hecke 作用与局部化相容：$\operatorname{Sat}_x(V)\star\mathcal D_{\mathrm{crit}}\simeq\operatorname{Loc}_x(\operatorname{Sat}_x(V)\star\mathbb V_{\mathrm{crit},x})$，再由几何 Satake 与 Feigin–Frenkel 识别化为 $\operatorname{Loc}_x\bigl(F_{D_x}(V)\otimes_{\mathfrak z_{\mathrm{crit}}(D_x)}\mathbb V_{\mathrm{crit},x}\bigr)$。  
   *为什么*：Hecke 算子是局部化的（$\operatorname{Loc}_x$ 是范畴等价的一侧），而 $\operatorname{Sat}_x(V)\star\mathbb V_{\mathrm{crit},x}$ 已由定理 14.3.1 的函子 $F_{D_x}$ 描述。
3. 令 $\mathcal F$ 为 $\operatorname{Op}_{\check G}(X)$ 上的普遍 $\check G$-挠子（等价地普遍 oper 局部系统），则 $F_{D_x}$ 是它在形式圆盘上的限制，上式变为 $\operatorname{Sat}_x(V)\star\mathcal D_{\mathrm{crit}}\simeq V_{\mathcal F,x}\otimes_A\mathcal D_{\mathrm{crit}}$。  
   *为什么*：$F_{D_x}$ 只依赖 $x$ 处的纤维，而该纤维来自 $\operatorname{Op}_{\check G}(X)$ 上的普遍对象。
4. 在 $A$ 上与 $k_\sigma$ 作张量积，得到 $\operatorname{Sat}_x(V)\star\operatorname{Aut}_\sigma\simeq V_{\sigma,x}\otimes\operatorname{Aut}_\sigma$，这正是 Hecke 特征性质。  
   *为什么*：$\operatorname{Aut}_\sigma=\mathcal D_{\mathrm{crit}}\otimes_{A,\sigma}k_\sigma$，张量积与 $\star$ 相容。

*出处*：定理 14.5.1 / 原书 p.70-71


## 易错点

- $H_{V,x}$ 是 Hecke 函子，不是与 $V$ 作张量；等式右边的 $V_{\sigma,x}\otimes\operatorname{Aut}_\sigma$ 才是 $\mathcal D$-模的张量。
- 证明中把 $F_{D_x}$ 认成普遍挠子在形式圆盘上的限制，这一步依赖定理 14.3.1 的 $\operatorname{Spec}\mathfrak z_{\mathrm{crit}}\simeq\operatorname{Op}^D_{\check G}$。
- 定理 14.5.1 的编号在英文正文 §14.4 被误引（那里用它指量子 Hitchin 同构），读原文时注意区分。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§14.5 oper 对应的自守模，p.70-71（PDF p.70-71），`源码/chapters/ch14.tex:124-147（定理 14.5.1 与证明）`

## 核验

状态：`external-confirmed`（2026-11-18）
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — “Tχi MF = 0 for i≠0 and there is a canonical isomorphism … (255) Tχ0 MF ≅ MF⊠V_Fχ … All this means that MF is a Hecke eigen-D-module of eigenvalue F”——逐字支持定理 14.5.1 的 H_{V,x}(Aut_σ)≅V_{σ,x}⊗Aut_σ 形式。
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — “Main theorem: MF is a Hecke eigensheaf with eigenvalue F … In other words MF corresponds to the local system F in the Langlands sense”——支持“Aut_σ 是特征值 σ 的 Hecke 特征层”。
- Frenkel05：https://arxiv.org/abs/hep-th/0512172 — “A marvelous result of A. Beilinson and V. Drinfeld [15] is that the D-module corresponding to a LG-oper E is nothing but the sought-after Hecke eigensheaf with 'eigenvalue' E!”——外部综述逐字支持。
- nLab: Hecke eigensheaf：https://ncatlab.org/nlab/show/Hecke+eigensheaf — “A Hecke eigensheaf is an object that is taken to a tensor-multiple of itself under the integral transform induced by a Hecke correspondence.”——只支持“Hecke 特征层”的一般定义，未给 Aut_σ 或 V_{σ,x} 公式。

## 关联

- `glc/concept/aut-sigma-module`
- `glc/concept/feigin-frenkel-center`
- `glc/concept/quantum-hitchin-map`
- `glc/concept/fundamental-local-equivalence`
