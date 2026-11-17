---
id: glc/concept/frobenius-twisted-trace
type: concept
track: G
---

# Frobenius 扭曲的迹与谱分解

> 把 $\operatorname{Fr}$ 与迭代 Hecke 变换复合后的范畴迹（取值于 $\operatorname{QLisse}(X^I)$）猜想为相应 shtuka 模空间的上同调。

**问题**：为什么说范畴迹形式体系把几何 Langlands 到函数论 Langlands 的过渡「几何化」了？

## 定义

对 $V_I\in\operatorname{Rep}(\check G)^{\otimes I}$，构造以 $X^I$ 为参数的自函子
$$\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\xrightarrow{\operatorname{Fr}}\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\xrightarrow{H_I(V_I,{-})}\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)\otimes\operatorname{QLisse}(X^I).$$
它的范畴迹是对象
$$\operatorname{Tr}(H_I(V_I,{-})\circ\operatorname{Fr};\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G))\in\operatorname{QLisse}(X^I).$$
猜想中的识别是：这个对象就是相应 shtuka 模空间的上同调。

*记号*：$\operatorname{Fr}$ 为 Frobenius 自函子（$k=\mathbb F_q$、$\ell$-进层）；$H_I(V_I,{-})$ 为迭代 Hecke 变换；$\operatorname{QLisse}(X^I)$ 为拟光滑层范畴；$\operatorname{Tr}$ 为 §12.7 的范畴迹。

## 要点

- 对 $V_I\in\operatorname{Rep}(\check G)^{\otimes I}$，$H_I(V_I,{-})\circ\operatorname{Fr}$ 是以 $X^I$ 为参数的自函子，其范畴迹落在 $\operatorname{QLisse}(X^I)$ 中。
- 猜想中的识别：这个迹对象就是相应 shtuka 模空间的上同调。
- 因此范畴迹形式体系把从几何 Langlands 到函数论 Langlands 的过渡、以及 V. Lafforgue 的游走算子都几何化了 [Gai16a, Laf18]。
- $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{restr}}_{\check G})$ 在 $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$ 上的谱作用，把迹提升为 Frobenius 扭曲不动点叠上的拟凝聚层。

## 关键公式

- $$\operatorname{Tr}(H_I(V_I,{-})\circ\operatorname{Fr};\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G))\in\operatorname{QLisse}(X^I)$$
- $$\operatorname{LocSys}^{\mathrm{restr},\operatorname{Fr}}_{\check G}:=\operatorname{LocSys}^{\mathrm{restr}}_{\check G}\times_{\operatorname{LocSys}^{\mathrm{restr}}_{\check G}\times\operatorname{LocSys}^{\mathrm{restr}}_{\check G},\ \Delta,\ (\operatorname{Id},\operatorname{Fr})}\operatorname{LocSys}^{\mathrm{restr}}_{\check G}$$

## 定理与证明

### 迹对象的 shtuka 识别与谱分解（要点（有缺口））

$\operatorname{Tr}(H_I(V_I,{-})\circ\operatorname{Fr};\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G))$ 猜想等于相应 shtuka 模空间的上同调；取全局截面时，$\operatorname{Fr}$ 扭曲的不动点叠 $\operatorname{LocSys}^{\mathrm{restr},\operatorname{Fr}}_{\check G}$ 上的拟凝聚层恢复自守迹空间。

1. 把 Hecke 作用与 Frobenius 复合，得到以 $X^I$ 为参数的自函子。  
   *为什么*：Hecke 变换带 $X^I$ 参数，Frobenius 与它交换到所需程度。
2. 取范畴迹，得到 $\operatorname{QLisse}(X^I)$ 中的对象。  
   *为什么*：自函子作用在可对偶范畴上，迹有定义。
3. 猜想该对象等于 shtuka 模空间的上同调，并用谱作用把它提升为 $\operatorname{LocSys}^{\mathrm{restr},\operatorname{Fr}}_{\check G}$ 上的拟凝聚层。  
   *为什么*：谱作用给出 $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{restr}}_{\check G})$-线性结构。

> 缺口：这是猜想性识别，讲义未证明（p.63）；相关构造见 [Gai16a, Laf18]，本章只述其几何化图景。

*出处*：命题（§12.7，讲义无编号） / 原书 p.63


## 易错点

- $\operatorname{LocSys}^{\mathrm{restr},\operatorname{Fr}}_{\check G}$ 是沿 $(\operatorname{Id},\operatorname{Fr})$ 的纤维积，不是普通的不动点叠；它的点是受限 Weil $\check G$-局部系统，而不是通常的局部系统。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§12.7 范畴迹与有限域上的函数，p.63（PDF p.63），`源码/chapters/ch12.tex:148-160（Frobenius 扭扭曲的迹与谱分解，§12.7）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — Sht~_{I,V}:=Tr(H(V,-)∘(Frob_BunG)_*,Shv_Nilp(Bun_G))∈QLisse(X^I)，并猜想 Sht~≃Sht（shtuka 上同调）。
- arXiv:2010.01906 (AGK20a)：https://arxiv.org/abs/2010.01906 — (LocSys^restr_Ĝ(X))^{Frob} 的点是 Weil Ĝ-局部系统；Tr((Frob_BunG)_*,Shv_Nilp)≃Γ(LocSys^arith,Drinf)。

## 关联

- `glc/concept/categorical-trace`
- `glc/concept/restricted-categorical-langlands`
- `glc/concept/restricted-spectral-stack`
