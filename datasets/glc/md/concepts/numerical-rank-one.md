---
id: glc/concept/numerical-rank-one
type: concept
track: H
---

# 归约到数值秩 $n=1$

> 伴随型、$g_X>1$ 时 $\mathcal A_{G,\mathrm{irr}}\simeq\mathcal O^{\oplus n}$，由 $\operatorname{End}(W_i)=k$ 得 $n=1$。

**问题**：为什么只需计算 $\operatorname{End}(W_i)$？

## 定义

限制到证明中使用的标准良好情形：$G$ 为伴随型，且 $g_X>1$；小的例外情形 $g_X=2$ 且 $\check G=\operatorname{SL}_2$ 通过单独的归约处理。在这一情形中，$\operatorname{LocSys}^{\mathrm{irr}}_{\check G}$ 在这里所需的意义下没有非平凡的有限 étale 覆盖，因此它上面的任意有限 étale 代数都是常值的：
$$\mathcal A_{G,\mathrm{irr}}\simeq\mathcal O^{\oplus n}_{\operatorname{LocSys}^{\mathrm{irr}}_{\check G}},$$
其中 $n\ge1$ 为整数。

*记号*：$g_X$ 为曲线 $X$ 的亏格；$r(G)=\operatorname{rank}_{\mathrm{ss}}(G)$ 为半单秩；$W_i$ 为基本 Whittaker 对象；$\chi_{\mathrm{glob}}$ 为简单根 Whittaker 特征标之积；$U_i$ 为幺幂群。

## 要点

- 要证明 $n=1$，只需证明全局截面上的映射 $\Gamma(\operatorname{LocSys}^{\mathrm{irr}}_{\check G},\mathcal O)\to\Gamma(\operatorname{LocSys}^{\mathrm{irr}}_{\check G},\mathcal A_{G,\mathrm{irr}})$ 是同构。
- 在良好情形中，不可约轨迹的补集余维至少为二，而且局部系统叠是 Cohen–Macaulay 的；因此将 $\mathcal A_{G,\mathrm{irr}}$ 延拓为整个 $\operatorname{LocSys}_{\check G}$ 上的全局代数 $\mathcal A_G$ 后，可以检验同一个问题，只需 $\Gamma(\operatorname{LocSys}_{\check G},\mathcal O)\xrightarrow{\sim}\Gamma(\operatorname{LocSys}_{\check G},\mathcal A_G)$。
- 全局函数方面的输入给出 $\Gamma(\operatorname{LocSys}_{\check G},\mathcal O)=k$；由全局 Poincaré 真空核的定义，右端是基本 Whittaker 对象 $W_i$ 的自同态代数：$\Gamma(\operatorname{LocSys}_{\check G},\mathcal A_G)\simeq\operatorname{End}(W_i)$。
- 最后需计算 $\operatorname{End}(W_i)=k$：Whittaker 图卡是通常 Drinfeld 紧化中的开分层；对充分负的次数数据 $i$ 有局部闭图，其中 $\chi_{\mathrm{glob}}$ 是简单根 Whittaker 特征标的乘积，相关极小层形如 $\mathring{\mathcal A}_{\min}\simeq\mathbb G_m^{r(G)}\times BU_i$。
- 对洁净 Whittaker 对象，$BU_i$ 因子只贡献单位对象；因此相关自同态计算归约为 $\operatorname{End}_{\operatorname{DMod}(\mathring{\mathcal A}_{\min})}(W_i|_{\mathring{\mathcal A}_{\min}})\simeq\operatorname{End}_{\operatorname{DMod}(\mathbb G_m^{r(G)})}(\mathcal E^{\boxtimes r(G)})$。
- $W_i$ 在这一图卡上限制为洁净指数对象 $\chi_{\mathrm{glob}}^!\mathcal E$；因此计算就是 $\mathbb G_m^{r(G)}$ 上 $\mathcal E^{\boxtimes r(G)}$ 的初等计算，并且 $\operatorname{End}(W_i)=k$。
- 所以 $n=1$，$\mathcal A_{G,\mathrm{irr}}\simeq\mathcal O$；单子 $\mathbb L_{G,\mathrm{cusp}}\mathbb L^L_{G,\mathrm{cusp}}$ 是恒等单子。由于 $\mathbb L_{G,\mathrm{cusp}}$ 是保守的且具有所需的伴随，它是一个等价。
- 再与可约部分的 Eisenstein 等价 (16.5) 结合，便证明了整体几何 Langlands 等价。

## 关键公式

- $\mathcal A_{G,\mathrm{irr}}\simeq\mathcal O^{\oplus n}_{\operatorname{LocSys}^{\mathrm{irr}}_{\check G}},\qquad n\ge1$
- $\Gamma(\operatorname{LocSys}_{\check G},\mathcal A_G)\simeq\operatorname{End}(W_i),\qquad \operatorname{End}(W_i)=k$
- $\mathring{\mathcal A}_{\min}\simeq\mathbb G_m^{r(G)}\times BU_i,\qquad \operatorname{End}_{\operatorname{DMod}(\mathbb G_m^{r(G)})}(\mathcal E^{\boxtimes r(G)})=k$

## 定理与证明

### 尖点等价（§16.10）（要点（有缺口））

$\mathbb L_{G,\mathrm{cusp}}:\operatorname{DMod}(\operatorname{Bun}_G)_{\mathrm{cusp}}\xrightarrow{\sim}\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G})$；与 (16.5) 结合即得整体几何 Langlands 等价。

1. 在良好情形把有限 étale 代数写成 $\mathcal A_{G,\mathrm{irr}}\simeq\mathcal O^{\oplus n}$，并把 $n=1$ 化为 $\Gamma(\mathcal O)\to\Gamma(\mathcal A_{G,\mathrm{irr}})$ 是同构。  
   *为什么*：常值有限 étale 代数由它的全局截面决定；不可约轨迹补集余维 $\ge2$ 且叠 Cohen–Macaulay，故可延拓到 $\operatorname{LocSys}_{\check G}$ 上检验。
2. 用 $\Gamma(\operatorname{LocSys}_{\check G},\mathcal O)=k$ 与全局 Poincaré 真空核的定义，把问题化为 $\operatorname{End}(W_i)=k$。  
   *为什么*：全局 Poincaré 真空核把 $\Gamma(\operatorname{LocSys}_{\check G},\mathcal A_G)$ 识别为 $W_i$ 的自同态代数。
3. 在 Drinfeld 紧化的开分层上计算 $\operatorname{End}(W_i)$：极小层 $\mathring{\mathcal A}_{\min}\simeq\mathbb G_m^{r(G)}\times BU_i$，洁净对象使 $BU_i$ 只贡献单位，计算归约为 $\mathbb G_m^{r(G)}$ 上 $\mathcal E^{\boxtimes r(G)}$。  
   *为什么*：$W_i$ 在该图卡上限制为 $\chi_{\mathrm{glob}}^!\mathcal E$，故自同态就是指数对象在环面上的自同态。
4. 得 $\operatorname{End}(W_i)=k$，故 $n=1$、$\mathcal A_{G,\mathrm{irr}}\simeq\mathcal O$，单子为恒等；保守性给出 $\mathbb L_{G,\mathrm{cusp}}$ 是等价。  
   *为什么*：保守 + 单子恒等 = 等价；再与 (16.5) 合并即得整体定理。

> 缺口：讲义给出完整证明链，但 $\Gamma(\operatorname{LocSys}_{\check G},\mathcal O)=k$、局部系统叠的 Cohen–Macaulay 性、Drinfeld 紧化图卡与 $\operatorname{End}(W_i)=k$ 的计算细节均以引用或断言形式给出；细节见 [GR24b]。

*出处*：§16.10 / 原书 p.82-83


## 易错点

- 良好情形 $G$ 为伴随型、$g_X>1$ 是证明的技术假设，$g_X=2$ 且 $\check G=\operatorname{SL}_2$ 单独处理；引用结论时不能去掉这些假设。
- $\mathcal A_{G,\mathrm{irr}}\simeq\mathcal O^{\oplus n}$ 是常值有限 étale 代数，$n$ 是覆盖的度数；把它写成 $\mathcal O^n$ 会丢掉「étale 局部化后常值」这一来源。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§16.10 归约到一个数值秩，p.82-83（PDF p.82-83），`源码/chapters/ch16.tex:212-235（$n=1$、$\operatorname{End}(W_i)=k$ 与尖点等价）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv:2409.09856 (GR24b)：https://arxiv.org/abs/2409.09856 — 原文：「…a multiplicity one theorem: we need to show that cuspidal objects of Dmod(Bun_G) can be (uniquely) reconstructed from their Whittaker coefficients」，且每个不可约 σ 存在「unique (up to tensoring with a vector space) Hecke eigensheaf」——支持卡的结论（n=1、End(W_i)=k 的等价形式）。
- arXiv:2409.09856 (GR24b)：https://arxiv.org/abs/2409.09856 — 卡中 Å_min ≅ G_m^{r(G)}×BU_i、χ_glob^!E、End(W_i)=k 的逐步计算未见逐字对应（原文证明路线不同）。

## 关联

- `glc/concept/generic-oper-coalgebra`
- `glc/concept/cuspidal-conservativity`
- `glc/concept/global-langlands-functor`
