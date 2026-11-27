---
id: glc/concept/fundamental-local-equivalence
type: concept
track: G
---

# 基本局部等价（预期形式）

> 临界 Kazhdan–Lusztig 范畴预期等价于 $\operatorname{Op}^{\mathrm{unr}}_{\check G,x}$ 上的 $\operatorname{IndCoh}$；§14.5 构造只用到真空生成部分。

**问题**：基本局部等价用什么替换 §14.5 的真空生成图像，相对构造又写成什么？

## 定义

§14.5 的构造只使用临界 Kac–Moody 范畴中由真空模生成的部分；示意地，有由真空对象生成的子范畴经 $\operatorname{Loc}_x$ 到 $\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$、并与 $\operatorname{QCoh}(\operatorname{Op}_{\check G}(D_x))$、$\operatorname{QCoh}(\operatorname{Op}_{\check G}(X))$ 相联系的方块。下一步是用整个临界范畴替换这个真空生成的子范畴，预期的局部形式是基本局部等价。置 $\operatorname{Op}^{\mathrm{unr}}_{\check G,x}:=\operatorname{Op}_{\check G}(D_x^\times)\times_{\operatorname{LocSys}_{\check G}(D_x^\times)}\operatorname{LocSys}_{\check G}(D_x)$。于是，忽略通常的 $*$ 型与 $!$ 型 $\operatorname{IndCoh}$ 约定的区别，$\operatorname{KL}_{G,\mathrm{crit},x}\simeq\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G,x})$。局部化应当提升为相对构造 $\operatorname{KL}_{G,\mathrm{crit},x}\otimes_{\operatorname{QCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G,x})}\operatorname{QCoh}(\operatorname{Op}_{\check G}(X\setminus\{x\})^{\mathrm{unr}})\to\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$，其中 $\operatorname{Op}_{\check G}(X\setminus\{x\})^{\mathrm{unr}}:=\operatorname{Op}_{\check G}(X\setminus\{x\})\times_{\operatorname{LocSys}_{\check G}(X\setminus\{x\})}\operatorname{LocSys}_{\check G}(X)$。

*记号*：$\operatorname{KL}_{G,\mathrm{crit},x}$ 为临界 Kazhdan–Lusztig 范畴；$D_x^\times=\operatorname{Spec} k((t))$；$\times_{\operatorname{LocSys}}$ 为沿局部系统叠的纤维积；$\operatorname{IndCoh}$ 为 ind-凝聚层范畴。

## 要点

- $\operatorname{Op}^{\mathrm{unr}}_{\check G,x}$ 是纤维积：穿孔圆盘上的 oper 配上在 $D_x$ 上可延拓的 $\check G$-局部系统。
- 基本局部等价断言 $\operatorname{KL}_{G,\mathrm{crit},x}\simeq\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G,x})$，但要忽略 $*$ 型与 $!$ 型 $\operatorname{IndCoh}$ 约定的区别。
- §14.5 只用真空模生成的子范畴；FLE 把它换成整个临界范畴。
- 相对构造把局部等价与 $X\setminus\{x\}$ 上的 oper 数据张量起来，得到 $\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$ 中的对象。
- 这是从 oper 的 Beilinson–Drinfeld 特征层通向 [FG05]、[FG07] 更广临界水平局部理论的桥梁。

## 关键公式

- $\operatorname{Op}^{\mathrm{unr}}_{\check G,x}:=\operatorname{Op}_{\check G}(D_x^\times)\times_{\operatorname{LocSys}_{\check G}(D_x^\times)}\operatorname{LocSys}_{\check G}(D_x)$
- $\operatorname{KL}_{G,\mathrm{crit},x}\simeq\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G,x})$（忽略 $*$／$!$ 约定）
- $\operatorname{KL}_{G,\mathrm{crit},x}\otimes_{\operatorname{QCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G,x})}\operatorname{QCoh}(\operatorname{Op}_{\check G}(X\setminus\{x\})^{\mathrm{unr}})\longrightarrow\operatorname{DMod}_{\mathrm{crit}}(\operatorname{Bun}_G)$

## 定理与证明

### 基本局部等价（预期）（要点（有缺口））

忽略通常的 $*$ 型与 $!$ 型 $\operatorname{IndCoh}$ 约定的区别，$\operatorname{KL}_{G,\mathrm{crit},x}\simeq\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G,x})$，其中 $\operatorname{Op}^{\mathrm{unr}}_{\check G,x}:=\operatorname{Op}_{\check G}(D_x^\times)\times_{\operatorname{LocSys}_{\check G}(D_x^\times)}\operatorname{LocSys}_{\check G}(D_x)$。

1. 讲义把该等价作为「预期的局部形式」陈述，并说局部化「应当提升为」相对构造。  
   *为什么*：这是猜想性的框架陈述，本章不证明。

> 缺口：讲义只述不证（§14.6 明确写「预期的局部形式」与「应当提升」）；完整陈述与证明见 [FG05]、[FG07]（讲义引）。

*出处*：§14.6 真空生成与下一步的局部图景 / 原书 p.71


## 易错点

- $\operatorname{Op}^{\mathrm{unr}}_{\check G,x}$ 是纤维积，不是 $\operatorname{Op}_{\check G}(D_x^\times)$ 本身：它额外要求底层局部系统在 $D_x$ 上可延拓。
- 等价陈述里「忽略 $*$ 与 $!$ 型 $\operatorname{IndCoh}$ 约定的区别」是讲义明写的 caveat，引用时不能省。
- 这是预期（猜想性）陈述，不要当成已证的定理使用。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§14.6 真空生成与下一步的局部图景，p.71-72（PDF p.71-72），`源码/chapters/ch14.tex:149-164（真空生成方块、Op^unr 与 FLE）`

## 核验

状态：`source-only`（2026-11-18）
- FG05：https://arxiv.org/abs/math/0508382 — “a local geometric Langlands correspondence … assigns to a local system on the punctured disc … a category equipped with an action of the formal loop group G((t)). We propose a conjectural description of these categories as categories of representations of the corresponding affine Kac-Moody algebra of critical level”——支持卡的“预期/猜想”定位与 D_x^× 上局部系统的作用。
- FG07：https://arxiv.org/abs/0711.1132 — “Consider the category of spherical ĝ-modules of critical level. In this paper we prove that this category is equivalent to the category of quasi-coherent sheaves on the ind-scheme of opers on the punctured disc which are unramified as local systems.”——支持 Op^unr_{Ǧ,x}:=Op(D_x^×)×_{LocSys(D_x^×)}LocSys(D_x) 的纤维积形状（球形、QCoh 版）。
- FG05：https://arxiv.org/abs/math/0508382 — “we prove that a certain quotient category of representations of critical level is equivalent to the category of quasicoherent sheaves on a thickening of the scheme of nilpotent opers”——是幂零 oper 的加厚，不是 Op^unr 上的 IndCoh；不能支持卡中 KL_{G,crit,x}≃IndCoh(Op^unr_{Ǧ,x})。
- FG05：https://arxiv.org/abs/math/0508382 — KL_{G,crit,x}≃IndCoh(Op^unr_{Ǧ,x})（忽略 * 与 ! 约定）及相对构造 KL⊗_{QCoh(Op^unr)}QCoh(Op(X∖{x})^unr)→DMod_crit(Bun_G) 未在 FG05/FG07 找到逐字陈述；讲义本身写作“预期的局部形式/应当提升”，是猜想而非定理。

## 关联

- `glc/concept/hecke-eigensheaf-oper`
- `glc/concept/aut-sigma-module`
- `glc/concept/feigin-frenkel-center`
