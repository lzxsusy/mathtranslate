---
id: glc/concept/hitchin-fibration
type: concept
track: F
---

# Hitchin 纤维化与 Hitchin 基

> 把 Higgs 场按不变多项式取值，得到 $T^*\operatorname{Bun}_G\to\mathcal A_G$；全局幂零锥正是它的零纤维。

**问题**：Hitchin 映射的目标为什么是 $\bigoplus_i H^0(X,\Omega_X^{d_i})$，而不是 $H^0(X,(\mathfrak g^*\!/\!/G)\otimes\Omega_X)$？

## 定义

设 $p_i\in\mathbb C[\mathfrak g^*]^G$ 是次数为 $d_i$ 的齐次生成元，置
$$\mathcal A_G:=\bigoplus_i H^0(X,\Omega_X^{d_i}).$$
Hitchin 映射为
$$h:T^*\operatorname{Bun}_G\longrightarrow\mathcal A_G,\qquad(P,\varphi)\longmapsto(p_i(\varphi))_i.$$
于是 $\mathrm{Nilp}_{\mathrm{glob}}=h^{-1}(0)$。用不变记号表示，这就是映射
$$\Gamma(X,\mathfrak g_P^*\otimes\Omega_X)\longrightarrow\Gamma(X,(\mathfrak g^*\!/\!/ G)_{\Omega_X}),$$
其中 $({-})_{\Omega_X}$ 表示由 $\mathfrak g^*$ 上的伸缩作用产生的 $\mathbb G_m$-扭转；取次数为 $d_i$ 的齐次生成元 $p_i$ 后，该目标为 $\bigoplus_i H^0(X,\Omega_X^{d_i})$。

*记号*：$\mathcal A_G$ 称为 Hitchin 基；$p_i$ 是 $\mathbb C[\mathfrak g^*]^G$ 的次数 $d_i$ 齐次生成元；$\Omega_X^{d_i}=\Omega_X^{\otimes d_i}$；$\mathfrak g^*\!/\!/G=\operatorname{Spec}\mathbb C[\mathfrak g^*]^G$ 为不变量商。本卡 $d_i$ 取次数（讲义 ch11 约定）；讲义 ch14 与 Frenkel 取指数 $d_i^{\mathrm{exp}}=d_i-1$，把底空间写成 $\bigoplus_i\Omega_X^{d_i^{\mathrm{exp}}+1}$（参 `hitchin-base` 卡），两套约定差 1。

## 要点

- $\mathcal A_G=\bigoplus_i H^0(X,\Omega_X^{d_i})$ 按每个齐次生成元的次数 $d_i$ 分别扭转后取直和。
- Hitchin 映射 $h$ 把 $(P,\varphi)$ 送到 $(p_i(\varphi))_i$。
- $\mathrm{Nilp}_{\mathrm{glob}}=h^{-1}(0)$，即全局幂零锥是 Hitchin 纤维化的零纤维。
- 用不变记号写，$h$ 就是 $\Gamma(X,\mathfrak g_P^*\otimes\Omega_X)\to\Gamma(X,(\mathfrak g^*\!/\!/G)_{\Omega_X})$。

## 关键公式

- $$\mathcal A_G:=\bigoplus_i H^0(X,\Omega_X^{d_i})$$
- $$h:T^*\operatorname{Bun}_G\longrightarrow\mathcal A_G,\qquad(P,\varphi)\longmapsto(p_i(\varphi))_i$$
- $$\mathrm{Nilp}_{\mathrm{glob}}=h^{-1}(0)$$

## 定理与证明

### 全局幂零锥是 Hitchin 零纤维（要点（有缺口））

$\mathrm{Nilp}_{\mathrm{glob}}=h^{-1}(0)$，其中 $h:T^*\operatorname{Bun}_G\to\mathcal A_G$ 为 Hitchin 映射。

1. 把 $\varphi_x\in\mathcal N_{\mathfrak g^*}$ 翻译成所有不变多项式在 $\varphi_x$ 处取零。  
   *为什么*：幂零锥正是 $\mathbb C[\mathfrak g^*]^G$ 的正次数生成元的公共零点。
2. 逐点条件等价于 $(p_i(\varphi))_i=0$ 作为 $\mathcal A_G$ 中的截面。  
   *为什么*：截面在每点取零即整体为零。

> 缺口：讲义只以「于是」给出该等式，未展开证明；幂零锥与不变多项式公共零点的对应是标准事实，本章未证。

*出处*：定义与命题（§11.5，讲义无编号） / 原书 p.59


## 易错点

- 扭转必须逐生成元进行：目标按 $\bigoplus_i H^0(X,\Omega_X^{d_i})$ 计算，不能先取商 $(\mathfrak g^*\!/\!/G)$ 再统一张量 $\Omega_X$——各生成元权不同。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§11.5 全局幂零锥，p.59（PDF p.59），`源码/chapters/ch11.tex:101-113（Hitchin 映射与零纤维，§11.5）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv：https://arxiv.org/abs/1606.08523 — L925：『Set A_G(X)=H^0(X,(g^*//G)⊗ω_X)』——按不变多项式 p_i 的次数 d_i 作扭转即 ⊕_i H^0(X,Ω_X^{d_i})，正是卡里 A_G 的定义与 notation 里『逐生成元扭转』的说明（卡里取 Ω_X=ω_X）。
- arXiv：https://arxiv.org/abs/1606.08523 — L926-934：『Then the Hitchin integrable system is the natural map Hitch: T^*Bun_G(X)→A_G(X), Hitch(E,φ)=φ induced by g^*→g^*//G』，紧接着『The global nilpotent cone … is the zero-fiber 𝒩_{X,G}=Hitch^{-1}(0)』——即卡里 h:(P,φ)↦(p_i(φ))_i 与 Nilp_glob=h^{-1}(0)。

## 关联

- `glc/concept/global-nilpotent-cone-higgs`
- `glc/concept/betti-nilpotent-conjecture`
