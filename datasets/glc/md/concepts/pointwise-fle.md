---
id: glc/concept/pointwise-fle
type: concept
track: H
---

# 临界 FLE（点态形式）

> 定理 15.2.1：临界 KL 范畴等价于非分歧 oper 上的 IndCoh，且对 FG 的 $t$-结构 $t$-正合、与几何 Satake 相容。

**问题**：FLE 的等价对哪个 $t$-结构是 $t$-正合的？

## 定义

定理的左右两端分别是临界 Kazhdan–Lusztig 范畴 $\operatorname{KL}_{G,\mathrm{crit}}=\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{L^+G}$ 与非分歧 oper 空间 $\operatorname{Op}^{\mathrm{unr}}_{\check G}=\operatorname{Op}_{\check G}(D^\times)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)$ 上的 $\operatorname{IndCoh}$。记 $i_{\check\lambda}:\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}\hookrightarrow\operatorname{Op}^{\mathrm{unr}}_{\check G}$。

*记号*：$\operatorname{IndCoh}$ 为 ind-凝聚层范畴；「$*$ 型或 $!$ 型」指 $\operatorname{IndCoh}$ 的两种惯常约定，讲义在此省略；$t$-正合是对标准的 Frenkel–Gaitsgory 阿贝尔 $t$-结构而言。

## 要点

- 等价是 DG 范畴的等价，并且对标准的 Frenkel–Gaitsgory 阿贝尔 $t$-结构 $t$-正合。
- 讲义省略惯常的 $*$ 型或 $!$ 型 $\operatorname{IndCoh}$ 选择。
- 等价与球面范畴的几何 Satake 作用相容。
- 相容性在 Weyl 对象上可见：$\Psi(\mathbb W^{\check\lambda}_{\mathrm{crit}})\simeq\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{End}(\mathbb W^{\check\lambda}_{\mathrm{crit}})$，$\operatorname{Spec}\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$。
- 在 FLE 下 $\mathbb W^{\check\lambda}_{\mathrm{crit}}$ 对应 $(i_{\check\lambda})^{\operatorname{IndCoh}}_*\mathcal O_{\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}}$；因此球面临界范畴的支撑恰好是非分歧 oper 轨迹，自守侧的非分歧对应谱侧单值性平凡。

## 关键公式

- $\operatorname{FLE}_{G,\mathrm{crit}}:\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{L^+G}\xrightarrow{\sim}\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$
- $\Psi(\mathbb W^{\check\lambda}_{\mathrm{crit}})\simeq\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{End}(\mathbb W^{\check\lambda}_{\mathrm{crit}})$
- $\operatorname{Spec}\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$

## 定理与证明

### 定理 15.2.1（临界 FLE，点态形式）（要点（有缺口））

存在 DG 范畴的等价 $\operatorname{FLE}_{G,\mathrm{crit}}:\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{L^+G}\xrightarrow{\sim}\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$，它对标准的 Frenkel–Gaitsgory 阿贝尔 $t$-结构是 $t$-正合的（这里省略惯常的 $*$ 型或 $!$ 型 $\operatorname{IndCoh}$ 选择），且与球面范畴的几何 Satake 作用相容。

1. 在 Weyl 对象上验证相容性：Drinfeld–Sokolov 约化给出 $\Psi(\mathbb W^{\check\lambda}_{\mathrm{crit}})\simeq\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{End}(\mathbb W^{\check\lambda}_{\mathrm{crit}})$ 与 $\operatorname{Spec}\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$。  
   *为什么*：这给出 FLE 下 $\mathbb W^{\check\lambda}_{\mathrm{crit}}$ 的像应等于 $(i_{\check\lambda})^{\operatorname{IndCoh}}_*\mathcal O_{\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}}$。
2. 由此读出球面临界范畴的支撑恰好是非分歧 oper 轨迹。  
   *为什么*：支撑落在 $\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$ 的并上，即 $\operatorname{Op}^{\mathrm{unr}}_{\check G}$；故自守侧的非分歧对应谱侧单值性平凡。

> 缺口：讲义只陈述定理，并以 Weyl 对象说明其相容性，未给出证明；原书引 [FG07]、[ABC24a]。

*出处*：定理 15.2.1 / 原书 p.73


## 易错点

- $\operatorname{IndCoh}$ 前的 $*$ 或 $!$ 约定被省略；引用此定理时必须随语境固定一种，不能两边混用。
- $t$-正合是对标准的 Frenkel–Gaitsgory 阿贝尔 $t$-结构而言；换一个 $t$-结构后不能照搬这一结论。
- 定理只断言与球面范畴的几何 Satake 作用相容，并没有说 $\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$ 上的作用就是逐点乘法。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.2 非分歧 oper，p.72-73（PDF p.72-73），`源码/chapters/ch15.tex:35-44（定理 15.2.1 及 Weyl 对象上的相容性）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Arinkin–Beraldo–Campbell–Chen–Færgeman–Gaitsgory–Lin–Raskin–Rozenblyum, Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE：https://arxiv.org/abs/2405.03648 — Theorem 6.1.4 断言 FLE_{G,crit} 是因子化范畴的等价；引言 365-368 明确写 t-exact equivalence of factorization categories FLE_{G,crit}: KL(G)_crit → IndCoh_*(Op^{mon-free}_{Ǧ})；支持卡里 DG 等价与 t-正合两条。
- Arinkin–Beraldo–Campbell–Chen–Færgeman–Gaitsgory–Lin–Raskin–Rozenblyum, Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE：https://arxiv.org/abs/2405.03648 — §E.10 标题 Compatibility of the FLE with (derived) Satake，正文以 Theorem 6.4.5 为目标；支持卡里「与球面几何 Satake 作用相容」。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — Prop 3.5 与 (3.5)：Ψ(Vλ_crit) ≃ z^{reg,λ}，且 z^{reg,λ} ≃ End(Vλ_crit)（行 367-368）；§2.2 给出 (Op^{unr,λ})_red ≃ Op^{reg,λ} 与 Spec z^{reg,λ} 的正则嵌入；支持卡里 Weyl 对象与支撑断言。

## 关联

- `glc/concept/unramified-oper`
- `glc/concept/critical-weyl-object`
- `glc/concept/whittaker-equivalence`
