---
id: glc/concept/double-adjunction
type: concept
track: H
---

# 双伴随性与自对偶代数

> 定理 16.8.1：尖点函子的左、右伴随典范等价；由此 $\mathcal A_{G,\mathrm{irr}}$ 完美且自对偶。

**问题**：双伴随性把单子问题转化成了什么？

## 定义

定理 16.8.1 断言存在伴随的典范等价 $\mathbb L^L_{G,\mathrm{cusp}}\simeq\mathbb L^R_{G,\mathrm{cusp}}$。其结果是：代数 $\mathcal A_{G,\mathrm{irr}}$ 作为 $\operatorname{LocSys}^{\mathrm{irr}}_{\check G}$ 上的复形是完美的，并且典范自对偶。

*记号*：$\mathbb L^L_{G,\mathrm{cusp}}$、$\mathbb L^R_{G,\mathrm{cusp}}$ 分别为左、右伴随；$\mathcal A^\vee_{G,\mathrm{irr}}$ 为对偶复形；余代数 $\mathcal B_{G,\mathrm{irr}}$ 与 $\mathcal A_{G,\mathrm{irr}}$ 是同一对象、不同结构。

## 要点

- 证明概述：通过上面使用的局部化与系数图表比较两侧；自守尖点范畴和 $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G})$ 都带有自然对偶。
- $\mathbb L_G$ 与 FLE、谱 Poincaré 函子和 Whittaker 系数的相容性，将 $\mathbb L_{G,\mathrm{cusp}}$ 的对偶函子识别为同一个函子；因此左伴随和右伴随相同。
- 右伴随给出与左伴随相同的核，但采用相反的伴随约定；因此与 $\mathcal A_{G,\mathrm{irr}}$ 对偶的对象是同一个对象，只是现在将它看作余代数。
- 将这一余代数记为 $\mathcal B_{G,\mathrm{irr}}$，即 $\mathcal B_{G,\mathrm{irr}}:=\mathcal A^\vee_{G,\mathrm{irr}}$，且 $\mathcal A^\vee_{G,\mathrm{irr}}\simeq\mathcal A_{G,\mathrm{irr}}$。
- 正是在这一步，双伴随性将单子问题转化为关于谱侧伪真 Ran 推前的几何陈述。

## 关键公式

- $\mathbb L^L_{G,\mathrm{cusp}}\simeq\mathbb L^R_{G,\mathrm{cusp}}$
- $\mathcal B_{G,\mathrm{irr}}:=\mathcal A^\vee_{G,\mathrm{irr}},\qquad \mathcal A^\vee_{G,\mathrm{irr}}\simeq\mathcal A_{G,\mathrm{irr}}$

## 定理与证明

### 定理 16.8.1（双伴随性）（要点（有缺口））

存在伴随的典范等价 $\mathbb L^L_{G,\mathrm{cusp}}\simeq\mathbb L^R_{G,\mathrm{cusp}}$。

1. 通过局部化与系数图表比较两侧。  
   *为什么*：两侧都可用 §16.3–§16.4 的图表与 Whittaker 系数落到同一比较框架。
2. 用自守尖点范畴与 $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G})$ 的自然对偶，以及 $\mathbb L_G$ 与 FLE、谱 Poincaré 函子、Whittaker 系数的相容性，把 $\mathbb L_{G,\mathrm{cusp}}$ 的对偶函子识别为同一个函子。  
   *为什么*：对偶函子相同即意味着左、右伴随重合。

> 缺口：讲义标为概述（Sketch），细节见 [ABC24b]。

*出处*：定理 16.8.1 / 原书 p.81


## 易错点

- $\mathcal B_{G,\mathrm{irr}}$ 不是新的代数：它作为对象与 $\mathcal A_{G,\mathrm{irr}}$ 相同，只是改看余代数结构；若把它当成另一个对象会重复计算。
- 双伴随性只断言左、右伴随典范等价，并没有说 $\mathbb L_{G,\mathrm{cusp}}$ 本身已经是等价；等价仍要靠保守性加单子为恒等。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§16.8 双伴随性与自对偶代数，p.81-82（PDF p.81-82），`源码/chapters/ch16.tex:182-195（定理 16.8.1 与 $\mathcal B_{G,\mathrm{irr}}$ 的定义）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv:2409.08670 (ABC24b)：https://arxiv.org/abs/2409.08670 — 原文：「We prove that the Langlands functor 𝕃_G …, when restricted to the cuspidal category, is ambidextrous」——卡定理 16.8.1（𝕃^L_{G,cusp} ≃ 𝕃^R_{G,cusp}）即此。
- arXiv:2409.08670 (ABC24b)：https://arxiv.org/abs/2409.08670 — 原文：「…it implies that A_{G,irred} is self-dual as an object of QCoh(LS^irred_Ĝ). In particular, it is perfect, and hence compact.」——支持卡的完美、典范自对偶。
- arXiv:2409.08670 (ABC24b)：https://arxiv.org/abs/2409.08670 — 原文给出 A_{G,irred} ≅ B^Op_{G,irred}（作为 QCoh(LS^irred_Ĝ) 的对象）——支持卡 B := A^∨、A^∨ ≅ A 的自对偶表述。

## 关联

- `glc/concept/cuspidal-conservativity`
- `glc/concept/generic-oper-coalgebra`
- `glc/concept/numerical-rank-one`
