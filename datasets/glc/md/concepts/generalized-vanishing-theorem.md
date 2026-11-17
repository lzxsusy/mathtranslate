---
id: glc/concept/generalized-vanishing-theorem
type: concept
track: F
---

# 广义消失定理

> Ran Hecke 幺半作用唯一地经 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 分解，这是广义消失猜想的范畴形式。

**问题**：为什么“作用唯一地经 $\operatorname{QCoh}(\operatorname{LocSys})$ 分解”就算把消失猜想升成了范畴形式？

## 定义

设 $G$ 是约化群、$\check G$ 为其 Langlands 对偶，$X$ 是光滑射影曲线。由 §9.3，Hecke 函子给出幺半作用 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}\to\operatorname{End}(\operatorname{DMod}(\operatorname{Bun}_G))$，并有幺半局部化函子 $\operatorname{Loc}_{\check G}:\operatorname{Rep}(\check G)_{\mathrm{Ran}}\to\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$。定理断言：该幺半作用唯一地经由 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 分解，即下图交换，且分解在同构意义下唯一。

*记号*：$\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 是 Ran 空间上的因子化表示范畴；分解的唯一性是相对于已给定的幺半作用而言的。

## 要点

- 幺半作用 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}\to\operatorname{End}(\operatorname{DMod}(\operatorname{Bun}_G))$ 唯一地经 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 分解。
- 这是广义消失猜想的范畴形式。
- 其证明使用 Kac–Moody 表示的 Beilinson–Drinfeld 局部化（见 [Gai10, Gai04]）。
- 与定理 9.3.1 合起来：知道 Ran Hecke 作用后，谱作用不再需要额外选择。
- 它是 §9.4 把 $\operatorname{Av}_E^d$ 的消失化到谱侧上同调计算的依据。

## 关键公式

- $\operatorname{Rep}(\check G)_{\mathrm{Ran}}\longrightarrow\operatorname{End}(\operatorname{DMod}(\operatorname{Bun}_G))\ \text{factors uniquely through}\ \operatorname{QCoh}(\operatorname{LocSys}_{\check G})$

## 定理与证明

### 广义消失定理（定理 9.3.2）（要点（有缺口））

幺半作用 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}\to\operatorname{End}(\operatorname{DMod}(\operatorname{Bun}_G))$ 唯一地经由 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 分解。这是广义消失猜想的范畴形式。其证明使用 Kac–Moody 表示的 Beilinson–Drinfeld 局部化。

1. 先用定理 9.3.1 把 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 认成 $\operatorname{Rep}(\check G)_{\mathrm{Ran}}$ 的 Verdier 商。  
   *为什么*：有了商，就只剩“作用在商的核上为零”这一件事要证。
2. 对 Kac–Moody 表示作 Beilinson–Drinfeld 局部化，验证该作用在核上为零。  
   *为什么*：这是原文唯一给出的证明线索；局部化把整体 Hecke 作用化成局部 Kac–Moody 代数上的计算。

> 缺口：讲义只写“其证明使用 Kac–Moody 表示的 Beilinson–Drinfeld 局部化”，未给细节；完整证明见 [Gai10]（另见 [Gai04]）。

*出处*：定理 9.3.2 / 原书 p.50


## 易错点

- 唯一性是对“已给定的幺半作用”说的：换一个只保留幂零支撑的作用（§9.5 的 $D_{\mathrm{Nilp}}$ 情形）得到的是另一套陈述，不蕴涵整个 $D(\operatorname{Bun}_G)$ 上的消失定理。
- 别把它与定理 9.3.1 混为一谈：9.3.1 说 $\operatorname{Loc}$ 是 Verdier 商（关于范畴），9.3.2 说作用经它分解（关于作用）。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§9.3 Ran 作用与局部到整体，p.50（PDF p.50），`定理 9.3.2（ch09.tex:65-71，p.50）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Gaitsgory, Recent progress in geometric Langlands theory (Seminaire Bourbaki, talk of 2016-02-16)：https://arxiv.org/abs/1606.09462 — §2.3.3「if this action factors through an action of QCoh(LocSys_Ǧ(X)) on C, then it does so uniquely. Moreover, this happens if and only if the objects in ker(Ev) act on C by zero」；Theorem 2.3.5「The action of ker(Ev) ⊂ Rep(Ǧ,Ran(X)) on D(Bun_G(X)) is zero」——逐字支持卡中「唯一地经由 QCoh 分解」。
- Gaitsgory, A generalized vanishing conjecture (manuscript, 2010-10-18)：https://people.mpim-bonn.mpg.de/gaitsgde/GL/GenVan.pdf — Conjecture 1.6 说 Rep(Ǧ)[Ran] 在 D(Bun_G) 上的作用经 QCoh(LocSys_Ǧ) 分解，即广义消失猜想；Corollary 1.8 给出谱投影——支持卡中「这是广义消失猜想的范畴形式」。
- Gaitsgory, A generalized vanishing conjecture (manuscript, 2010-10-18)：https://people.mpim-bonn.mpg.de/gaitsgde/GL/GenVan.pdf — Main Lemma 2.2 对 F∈ker(Loc_{Ǧ,cl}) 与 M∈KL_{G,crit}[Ran] 陈述消去性，并说它是「an easy corollary of (a generalization of) the main [theorem of BD]」——逐字支持卡中「证明使用 Kac–Moody 表示的 Beilinson–Drinfeld 局部化」。

## 关联

- `glc/concept/ran-hecke-action`
- `glc/concept/averaging-vanishing-theorem`
- `glc/concept/averaging-kernel`
