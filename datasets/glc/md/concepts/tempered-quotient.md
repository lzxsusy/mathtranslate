---
id: glc/concept/tempered-quotient
type: concept
track: F
---

# $t$ 正合性背后的商范畴

> 为修补“$\operatorname{Av}_E^1$ 是 $t$-正合”这一错误陈述，构造 Verdier 商使其上 $t$-正合、继承反常 $t$-结构且在尖点对象上保守。

**问题**：“$\operatorname{Av}_E^1$ 是 $t$-正合的”为什么是错的，正确的替代是什么？

## 定义

最初证明中的困难是 $t$-正合性。看似诱人的陈述“$\operatorname{Av}_E^1$ 是 $t$-正合的”是错误的。正确做法是构造一个 Verdier 商 $D(\operatorname{Bun}_m)\twoheadrightarrow\widetilde D(\operatorname{Bun}_m)$，具有三项性质：$\widetilde{\operatorname{Av}}_E^1$ 是 $t$-正合的；该商继承反常 $t$-结构；复合 $D(\operatorname{Bun}_m)_{\mathrm{cusp}}\to D(\operatorname{Bun}_m)\to\widetilde D(\operatorname{Bun}_m)$ 是保守的。这是对 $\operatorname{Av}_E^1$ 那个错误正合性陈述的 Springer 型替代；Gaitsgory 最初构造 $\widetilde D$ 的方法在技术上相当复杂。

*记号*：$\widetilde{\operatorname{Av}}_E^1$ 是 $\operatorname{Av}_E^1$ 经该商下降得到的函子；$D(\operatorname{Bun}_m)_{\mathrm{cusp}}$ 是尖点对象子范畴；“保守”指函子反射同构。

## 要点

- “$\operatorname{Av}_E^1$ 是 $t$-正合的”这一陈述是错的。
- 替代品是 Verdier 商 $D(\operatorname{Bun}_m)\twoheadrightarrow\widetilde D(\operatorname{Bun}_m)$，其上 $\widetilde{\operatorname{Av}}_E^1$ 是 $t$-正合的。
- 该商继承反常 $t$-结构，且 $D(\operatorname{Bun}_m)_{\mathrm{cusp}}\to\widetilde D(\operatorname{Bun}_m)$ 保守。
- 现代解释是把这个商取为温和部分：$\widetilde D(\operatorname{Bun}_G)=D(\operatorname{Bun}_G)^{\mathrm{temp}}$。
- 几何 Ramanujan 定理说明尖点对象是温和的（[Ber21]）；Eisenstein／常数项的形式体系补上其余的非尖点部分，这为旧的商范畴提供概念上更清楚的替代。

## 关键公式

- $D(\operatorname{Bun}_m)\twoheadrightarrow\widetilde D(\operatorname{Bun}_m),\qquad \widetilde D(\operatorname{Bun}_G)=\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}$

## 定理与证明

### 商范畴的三项性质（§9.8）（要点（有缺口））

存在 Verdier 商 $D(\operatorname{Bun}_m)\twoheadrightarrow\widetilde D(\operatorname{Bun}_m)$，使得 $\widetilde{\operatorname{Av}}_E^1$ 是 $t$-正合的、该商继承反常 $t$-结构、且复合 $D(\operatorname{Bun}_m)_{\mathrm{cusp}}\to D(\operatorname{Bun}_m)\to\widetilde D(\operatorname{Bun}_m)$ 保守。

1. 取商为温和部分：$\widetilde D(\operatorname{Bun}_G)=D(\operatorname{Bun}_G)^{\mathrm{temp}}$。  
   *为什么*：这是讲义给出的现代解释，把 Gaitsgory 最初的技术性构造换成概念上更清楚的对象。
2. 用几何 Ramanujan 定理（尖点对象温和，[Ber21]）保证尖点部分落在该商里。  
   *为什么*：保守性只需在尖点对象上验证，而尖点对象已被说明整体落在温和部分。
3. 非尖点部分由 Eisenstein／常数项形式体系补上。  
   *为什么*：这样商范畴既含尖点部分又含 Eisenstein 部分，覆盖整个 $D(\operatorname{Bun}_G)$。

> 缺口：讲义只列出该商的三项性质并说 Gaitsgory 最初的构造“在技术上相当复杂”，未给构造与验证；现代解释取 $\widetilde D(\operatorname{Bun}_G)=D(\operatorname{Bun}_G)^{\mathrm{temp}}$ 亦未在此证明。

*出处*：§9.8 / 原书 p.52-53


## 易错点

- 不要引用“$\operatorname{Av}_E^1$ 是 $t$-正合的”：讲义明确说这是错误的，正确说法是它只在辅助 Verdier 商上 $t$-正合。
- 保守性只对复合 $D(\operatorname{Bun}_m)_{\mathrm{cusp}}\to\widetilde D(\operatorname{Bun}_m)$ 断言，不是整个 $D(\operatorname{Bun}_m)\to\widetilde D(\operatorname{Bun}_m)$ 保守。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§9.8 t 正合性背后的商范畴，p.52-53（PDF p.52-53），`§9.8 t 正合性背后的商范畴（ch09.tex:148-160，p.52-53）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Gaitsgory, On a vanishing conjecture appearing in the geometric Langlands correspondence, Annals 160(2) 617-682：https://arxiv.org/abs/math/0204081 — 「(0) D̃(Bun_n) inherits the perverse t-structure from D(Bun_n), (1) the Hecke functors defined on D(Bun_n) descend to D̃(Bun_n) and are exact, and (2) the subcategory of objects of D(Bun_n) that map to 0 in D̃(Bun_n) is orthogonal to cuspidal complexes」——逐字支持卡中三项性质；卡的「复合在尖点上保守」是 (2) 的等价改写。
- Gaitsgory, On a vanishing conjecture appearing in the geometric Langlands correspondence, Annals 160(2) 617-682：https://arxiv.org/abs/math/0204081 — 「a natural idea would be to show that the 'elementary' functor Av^1_E is exact. The latter, however, is false.」——逐字支持卡中「Av_E^1 是 t-正合的是错的」。
- Gaitsgory-Raskin, Proof of the geometric Langlands conjecture I: construction of the functor：https://arxiv.org/abs/2405.03599 — GR24a §0.3.6 引入 D-mod(Bun_G)^temp 及 L_{G,temp}: D-mod(Bun_G)^temp→QCoh(LS_Ǧ) 的温和 GLC；Ber21 摘要「any cuspidal D-module on Bun_G is tempered」——支持卡中「现代解释取 D̃(Bun_G)=DMod(Bun_G)^{temp}」与「几何 Ramanujan 定理说尖点对象温和」的背景，但没有一个来源把旧的商 D̃ 与 DMod^temp 逐字等同，故此条记 partial。

## 关联

- `glc/concept/tempered-categorical-conjecture`
- `glc/concept/gaitsgory-original-proof`
- `glc/concept/tempered-object`
