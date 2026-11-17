---
id: glc/concept/hecke-eigensheaf-general
type: concept
track: B
---

# Hecke 特征层（一般 $G$）

> 若 $\mathcal{F}\in D(\operatorname{Bun}_G)$ 对每个 $V$ 有同构 $H_V(\mathcal{F})\simeq V_E\boxtimes\mathcal{F}$，则称它以 $E$ 为特征值。

**问题**：一般 $G$ 的 Hecke 特征层定义中，「与 $\operatorname{Rep}(\check{G})$ 的张量积相容」为什么不能省？

## 定义

设 $E_{\check{G}}$ 是 $X$ 上的 $\check{G}$-局部系统，对 $V\in\operatorname{Rep}(\check{G})$ 令 $V_E$ 为 $X$ 上相应的局部系统。整体 Hecke 函子为 $H_V:D(\operatorname{Bun}_G)\to D(X\times\operatorname{Bun}_G)$，$\mathcal{F}\mapsto(\operatorname{supp},\overrightarrow{h})_!(m^*\operatorname{Sat}_V\otimes\overleftarrow{h}^*\mathcal{F})$；在固定点 $x\in X$ 处它限制为 $H_{V,x}:D(\operatorname{Bun}_G)\to D(\operatorname{Bun}_G)$，$\mathcal{F}\mapsto\overrightarrow{h}_{x,!}(m_x^*\operatorname{Sat}_V\otimes\overleftarrow{h}_x^*\mathcal{F})$。$\operatorname{Sat}_V$ 的反常归一化包括通常的移位与扭曲。若对每个 $V\in\operatorname{Rep}(\check{G})$，在 $D(X\times\operatorname{Bun}_G)$ 中都有函子性的同构 $H_V(\mathcal{F})\simeq V_E\boxtimes\mathcal{F}$，并且这些同构与 $\operatorname{Rep}(\check{G})$ 中的张量积相容，则称对象 $\mathcal{F}\in D(\operatorname{Bun}_G)$ 是以 $E_{\check{G}}$ 为特征值的 Hecke 特征层。特别地，在 $x\in X$ 处逐纤维有 $H_{V,x}(\mathcal{F})\simeq(V_E)_x\otimes\mathcal{F}$。

*记号*：$m$：相对位置映射（§2.5 记 $m_x:\operatorname{Hecke}_{G,x}\to\operatorname{Hecke}_{G,x}^{\mathrm{loc}}$），$\operatorname{Sat}_V$：$V$ 对应的相对 Satake 层（§2.5；在 $X$ 上的整体族中用同一记号）；$(\operatorname{supp},\overrightarrow{h})$：整体 Hecke 对应的支撑与修改后投影；$V_E$：$V$ 沿 $E$ 所得的 $X$ 上局部系统。

## 要点

- 同构必须是函子性的（对 $V$ 的态射自然），并且要与 $\operatorname{Rep}(\check{G})$ 中的张量积相容，两条一起才构成定义。
- 整体形式在 $D(X\times\operatorname{Bun}_G)$ 中用外张量积 $V_E\boxtimes\mathcal{F}$；在固定点 $x$ 处逐纤维有 $H_{V,x}(\mathcal{F})\simeq(V_E)_x\otimes\mathcal{F}$。
- 这是层论层面对经典条件的替代：一个自守函数应是所有球面 Hecke 算子的特征向量。
- $\operatorname{Sat}_V$ 的反常归一化包括通常的移位与扭转，Hecke 函子的归一化约定须与之配套。

## 关键公式

- $H_V:D(\operatorname{Bun}_G)\longrightarrow D(X\times\operatorname{Bun}_G),\qquad\mathcal{F}\longmapsto(\operatorname{supp},\overrightarrow{h})_!(m^*\operatorname{Sat}_V\otimes\overleftarrow{h}^*\mathcal{F})$
- $H_V(\mathcal{F})\simeq V_E\boxtimes\mathcal{F}$
- $H_{V,x}(\mathcal{F})\simeq(V_E)_x\otimes\mathcal{F}$

## 易错点

- 只对每个 $V$ 单独有同构不够：定义还要求这些同构与 $\operatorname{Rep}(\check{G})$ 的张量积相容，否则得不到函子性。
- $E$ 是 $X$ 上的 $\check{G}$-局部系统，特征值不是 $G$-局部系统；$V_E$ 是 $V$ 沿 $E$ 得到的局部系统。
- $\boxtimes$（$X\times\operatorname{Bun}_G$ 上的外张量积）与 $\otimes$（固定点处的张量积）不是同一个运算。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§2.6 Hecke 函子与特征层，p.14（PDF p.14），`源码/chapters/ch02.tex:136-141（定义 2.6.1）`

## 核验

状态：`external-confirmed`（2026-11-18）
- zbMATH（评论 Zbl 1234.11155）：https://zbmath.org/1234.11155 — 评论原文「H^V(S(E_Ĝ)) ≃ S(E_Ĝ) ⊠ V_{E_Ĝ}, where H^V: D^b(Bun_G) → D^b(Bun_G × X) are the Hecke functors, defined for each V ∈ Rep(Ĝ)」支持定义 2.6.1 的「对每个 V 有函子性同构 H_V(F) ≃ V_E ⊠ F」。
- IAS Arbeitsgemeinschaft 2016 讲义：https://www.math.ias.edu/~lurie/ffcurve/Arbeitsgemeinschaft2016GL.pdf — 「T^i(F) ≅ F ⊠ ∧^i E_σ for all i = 1,…,n」给出 GL_n 情形的 Hecke 特征层定义，与卡中定义 2.6.1 的特例一致。

## 关联

- `glc/concept/unramified-global-gl`
- `glc/concept/hecke-eigensheaf-gl1`
- `glc/concept/global-hecke-stack`
- `glc/concept/minuscule-hecke-reduction`
