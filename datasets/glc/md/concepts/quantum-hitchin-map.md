---
id: glc/concept/quantum-hitchin-map
type: concept
track: G
---

# 量子 Hitchin 映射

> 临界扭转微分算子层 $\mathcal D_{\mathrm{crit}}$ 的全局截面代数同构于 oper 空间上的函数代数 $A$，其相伴分次同构于 $T^*\operatorname{Bun}_G$ 上的函数。

**问题**：量子 Hitchin Hamilton 量的交换代数为什么就是 $\operatorname{Op}_{\check G}(X)$ 上的函数代数，经典极限对应哪个同构？

## 定义

令 $\mathcal D_{\mathrm{crit}}$ 为 $\operatorname{Bun}_G$ 上临界扭转微分算子层。局部临界中心通过局部化作用于全局微分算子：若一对 $(\mathfrak h,K)$ 作用于光滑叠 $Y$，而 $y\in Y$ 是 $K$-不动点，则齐性模型上的不变微分算子映入 $Y$ 上的微分算子：$(U(\mathfrak h)/U(\mathfrak h)\mathfrak k)^K\longrightarrow\Gamma(Y,\mathcal D_Y)$。取 $Y=\operatorname{Bun}_G$、$\mathfrak h=\mathfrak g((t))$、$K=G[[t]]$，得到 $\mathfrak z_{\mathrm{crit}}(D_x)=\operatorname{End}(\mathbb V_{\mathrm{crit},x})\longrightarrow\Gamma(\operatorname{Bun}_G,\mathcal D_{\mathrm{crit}})$。这些局部映射与变量 $x$ 中的联络相容，因此下降到水平截面：$\mathfrak z_{\mathrm{crit}}(X)\longrightarrow\Gamma(\operatorname{Bun}_G,\mathcal D_{\mathrm{crit}})$；取相伴分次给出经典 Hitchin 映射 $\operatorname{gr}\mathfrak z_{\mathrm{crit}}(X)\longrightarrow\Gamma(T^*\operatorname{Bun}_G,\mathcal O)$。置 $A:=\Gamma(\operatorname{Op}_{\check G}(X),\mathcal O)=\Gamma(X_{\mathrm{dR}},\mathfrak z_{\mathrm{crit}})$、$A^{\mathrm{cl}}:=\Gamma(\operatorname{Hitch}_{\check G}(X),\mathcal O)\simeq\operatorname{gr}A$。

*记号*：$\mathcal D_Y$ 为 $Y$ 上的微分算子层；$U(\mathfrak h)$ 为泛包络代数；$\mathfrak k=\operatorname{Lie}K$；$X_{\mathrm{dR}}$ 为 $X$ 的 de Rham 景；$T^*\operatorname{Bun}_G$ 为余切叠。

## 要点

- 局部化把临界中心打到全局微分算子：$\mathfrak z_{\mathrm{crit}}(D_x)=\operatorname{End}(\mathbb V_{\mathrm{crit},x})\to\Gamma(\operatorname{Bun}_G,\mathcal D_{\mathrm{crit}})$。
- 这些局部映射与变量 $x$ 中的联络相容，才能下降到水平截面 $\mathfrak z_{\mathrm{crit}}(X)\to\Gamma(\operatorname{Bun}_G,\mathcal D_{\mathrm{crit}})$。
- 取相伴分次得到经典 Hitchin 映射 $\operatorname{gr}\mathfrak z_{\mathrm{crit}}(X)\to\Gamma(T^*\operatorname{Bun}_G,\mathcal O)$。
- 两个同构：$A\xrightarrow{\sim}\Gamma(\operatorname{Bun}_G,\mathcal D_{\mathrm{crit}})$ 与 $A^{\mathrm{cl}}\xrightarrow{\sim}\Gamma(T^*\operatorname{Bun}_G,\mathcal O)$。
- 量子 Hitchin Hamilton 量的交换代数就是 $\check G$-oper 空间上的函数代数；第二个同构是经典陈述：$T^*\operatorname{Bun}_G$ 上的全局函数来自 Hitchin 底空间。
- $A=\Gamma(\operatorname{Op}_{\check G}(X),\mathcal O)=\Gamma(X_{\mathrm{dR}},\mathfrak z_{\mathrm{crit}})$，把 oper 空间上的函数与临界中心在 de Rham 景上的全局截面等同。

## 关键公式

- $(U(\mathfrak h)/U(\mathfrak h)\mathfrak k)^K\longrightarrow\Gamma(Y,\mathcal D_Y)$
- $A:=\Gamma(\operatorname{Op}_{\check G}(X),\mathcal O)=\Gamma(X_{\mathrm{dR}},\mathfrak z_{\mathrm{crit}}),\qquad A^{\mathrm{cl}}:=\Gamma(\operatorname{Hitch}_{\check G}(X),\mathcal O)\simeq\operatorname{gr}A$
- $A\xrightarrow{\sim}\Gamma(\operatorname{Bun}_G,\mathcal D_{\mathrm{crit}}),\qquad A^{\mathrm{cl}}\xrightarrow{\sim}\Gamma(T^*\operatorname{Bun}_G,\mathcal O)$

## 定理与证明

### 量子 Hitchin 映射的同构性（要点（有缺口））

上述映射为同构：$A\xrightarrow{\sim}\Gamma(\operatorname{Bun}_G,\mathcal D_{\mathrm{crit}})$ 与 $A^{\mathrm{cl}}\xrightarrow{\sim}\Gamma(T^*\operatorname{Bun}_G,\mathcal O)$。

1. 讲义给出同构陈述并引 [BD91]，本章未证。  
   *为什么*：同构性属于 Beilinson–Drinfeld 的量子化定理，超出本章的叙述范围。

> 缺口：讲义只述不证（§14.4 未编号定理），引 [BD91]；正特征方向上的另一路见 [BCTZ16]。

*出处*：§14.4 定理（讲义未编号）/ 原书 p.70


## 易错点

- 本节定理在讲义中未编号；英文正文把它称作 Theorem 14.5.1，而编号 14.5.1 实际属于 §14.5 的 Hecke 特征层定理，引用时勿混。
- 第二个同构是经典陈述（$T^*\operatorname{Bun}_G$ 上的全局函数来自 Hitchin 底空间），不要与量子的第一个同构混为一谈。
- $A^{\mathrm{cl}}\simeq\operatorname{gr}A$ 与 $A\cong\Gamma(\operatorname{Bun}_G,\mathcal D_{\mathrm{crit}})$ 是不同层面的陈述：前者是相伴分次，后者是同构本身。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§14.4 全局微分算子与量子 Hitchin 映射，p.70（PDF p.70），`源码/chapters/ch14.tex:97-117（局部化、A 与 A^cl、同构定理）`

## 核验

状态：`external-confirmed`（2026-11-18）
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — “construct a filtered commutative algebra z(X) with σz(X): gr z(X)→zcl(X) and hX: z(X)→Γ(BunG,D0) … σBunG∘gr hX = hclX∘σz(X)”；“2.2.4(v) implies … hγX: z(X)→Γ(BunγG,D0) is an isomorphism”——支持 A≅Γ(Bun_G,D_crit) 及 gr 后回到经典 Hitchin 映射。
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — “For each γ∈π1(X) the morphism zcl(X)→Γ(BunγG,P) is an isomorphism”——支持 A^cl≅Γ(T*Bun_G,O)。
- BD：https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf — spectrum of z ≅ moduli of Lg-opers；Ag(X) 是 Opg(X) 的坐标环——支持 A:=Γ(Op(X),O)=Γ(X_dR,z_crit) 与 A^cl≃gr A。
- BCTZ16：https://arxiv.org/abs/1603.01327 — “In a celebrated unpublished manuscript Beilinson and Drinfeld quantize the Hitchin integrable system … In this note we show for G=GL(n) that those results admit a short proof by reduction to positive characteristic”——支持卡中“正特征方法见 [BCTZ16]”的指针（仅摘要级）。

## 关联

- `glc/concept/feigin-frenkel-center`
- `glc/concept/hecke-eigensheaf-oper`
- `glc/concept/aut-sigma-module`
- `glc/concept/hitchin-base`
