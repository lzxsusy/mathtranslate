---
id: glc/concept/hecke-lisse-sheaves
type: concept
track: G
---

# Hecke 光滑层与幂零奇异支撑

> 所有迭代 Hecke 变换都沿曲线方向局部常值的层；在 Betti 情形，这与幂零奇异支撑等价。

**问题**：「Hecke 光滑」说的是层 $\mathcal F$ 本身局部常值，还是它的 Hecke 变换沿曲线方向局部常值？

## 定义

令 $X$ 为曲线，并取 $\mathcal F\in\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)$。整体 Hecke 对应为每个 $V\in\operatorname{Rep}(\check G)$ 给出函子
$$H(V,{-}):\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)\longrightarrow\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G\times X).$$
称 $\mathcal F$ 是 Hecke 光滑的，若对每个有限集合 $I$ 及每个 $V_I\in\operatorname{Rep}(\check G)^{\otimes I}$，迭代 Hecke 变换都位于沿曲线方向光滑的子范畴中，即
$$H_I(V_I,\mathcal F)\in\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)\otimes\operatorname{LocSys}(X(\mathbb C)^I)\subset\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G\times X^I).$$
等价地，所有 Hecke 变换都沿 $X^I$ 方向局部常值。

*记号*：$H(V,{-})$ 为整体 Hecke 对应给出的函子；$H_I(V_I,{-})$ 为迭代 Hecke 变换；$\operatorname{LocSys}(X(\mathbb C)^I)$ 为 $X(\mathbb C)^I$ 上的局部系统范畴，作为沿曲线方向局部常值的模型。

## 要点

- 整体 Hecke 对应对每个 $V\in\operatorname{Rep}(\check G)$ 给出 $H(V,{-}):\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)\to\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G\times X)$。
- Hecke 光滑要求对每个有限集 $I$ 与每个 $V_I\in\operatorname{Rep}(\check G)^{\otimes I}$，迭代变换落在 $\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)\otimes\operatorname{LocSys}(X(\mathbb C)^I)$ 中。
- 等价地，所有 Hecke 变换都沿 $X^I$ 方向局部常值。
- Betti 局部到整体定理说明幂零支撑蕴涵 Hecke 光滑 [NY19]，AGKRRV 使用的形式把这一结论加强为等价 [AGK20a]：$\operatorname{Shv}^{\mathrm{all}}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\simeq\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)_{\mathrm{Hecke}\text{-}\mathrm{lisse}}$。
- 因此 Hecke 作用满足局部到整体定理的假设，得到谱作用 $\operatorname{Perf}(\operatorname{LocSys}^{\mathrm{Betti}}_{\check G})\curvearrowright\operatorname{Shv}^{\mathrm{all}}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$；可呈示完备化后得到相应的 $\operatorname{QCoh}$ 作用。

## 关键公式

- $$H(V,{-}):\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)\longrightarrow\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G\times X)$$
- $$H_I(V_I,\mathcal F)\in\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)\otimes\operatorname{LocSys}(X(\mathbb C)^I)\subset\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G\times X^I)$$
- $$\operatorname{Shv}^{\mathrm{all}}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\simeq\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)_{\mathrm{Hecke}\text{-}\mathrm{lisse}}$$
- $$\operatorname{Perf}(\operatorname{LocSys}^{\mathrm{Betti}}_{\check G})\curvearrowright\operatorname{Shv}^{\mathrm{all}}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$$

## 定理与证明

### 幂零支撑 $\Longleftrightarrow$ Hecke 光滑（要点（有缺口））

在 Betti 情形有等价 $\operatorname{Shv}^{\mathrm{all}}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\simeq\operatorname{Shv}^{\mathrm{all}}(\operatorname{Bun}_G)_{\mathrm{Hecke}\text{-}\mathrm{lisse}}$，即幂零奇异支撑与 Hecke 光滑性互为等价。

1. 由 Nadler–Yun，具有幂零奇异支撑的层其 Hecke 函子在 $X$ 的点参数上局部常值 [NY19]，得到「幂零支撑 $\Rightarrow$ Hecke 光滑」。  
   *为什么*：Hecke 光滑正是所有迭代变换沿 $X^I$ 局部常值。
2. 用 AGKRRV 中的逆命题与推广 [AGK20a] 反向，得到等价。  
   *为什么*：该逆命题断言 Hecke 光滑性强制奇异支撑落于 $\mathrm{Nilp}_{\mathrm{glob}}$。

> 缺口：讲义只述该等价（p.61–62），未给证明；正向见 [NY19]，逆向见 [AGK20a]。

*出处*：命题（§12.4，讲义无编号） / 原书 p.61–62


## 易错点

- Hecke 光滑不是 $\mathcal F$ 在 $\operatorname{Bun}_G$ 上局部常值：局部常值性是对 $H_I(V_I,\mathcal F)$ 沿 $X^I$ 方向而言的。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§12.4 Hecke 光滑层与幂零奇异支撑，p.61-62（PDF p.61-62），`源码/chapters/ch12.tex:61-78（Hecke 光滑的定义与等价，§12.4，跨 p.61–62）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — Shv(Bun_G)^{Hecke-lisse} 定义为所有 V∈Rep(Ĝ) 使 H(V,F)∈Shv(Bun_G)⊗QLisse(X)；Main Theorem 14.4.3：包含 Shv_Nilp(Bun_G)⊂Shv^{Hecke-lisse} 是等号。
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — H(V,-):Shv_Nilp(Bun_G)→Shv_Nilp(Bun_G)⊗QLisse(X^I)；且 Shv_Nilp(Bun_G)⊗QLisse(X)^{⊗I}⊂Shv(Bun_G×X^I)。

## 关联

- `glc/concept/betti-local-to-global`
- `glc/concept/restricted-spectral-stack`
- `glc/concept/betti-nilpotent-conjecture`
