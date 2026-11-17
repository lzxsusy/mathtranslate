---
id: glc/concept/cuspidal-conservativity
type: concept
track: H
---

# 尖点函子的保守性

> 定理 16.7.1：$\mathbb L_{G,\mathrm{cusp}}$ 保守；配合左伴随，只需识别单子 $\mathbb L_{G,\mathrm{cusp}}\mathbb L^L_{G,\mathrm{cusp}}$ 为恒等。

**问题**：保守性加上什么条件才能推出 $\mathbb L_{G,\mathrm{cusp}}$ 是等价？

## 定义

§16.7 的第一个输入是保守性。第二个输入是 §16.6 中已经构造的伴随的存在性。因此，要证明 $\mathbb L_{G,\mathrm{cusp}}$ 是等价，只需识别单子
$$\mathbb L_{G,\mathrm{cusp}}\circ\mathbb L^L_{G,\mathrm{cusp}}\in\operatorname{End}(\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G})).$$

*记号*：$\mathcal A_{G,\mathrm{irr}}$ 为谱侧的结合代数对象；$\mathcal A_G=\mathbb L_G\mathbb L^L_G(\mathcal O)$ 为整体版本；$\operatorname{AssocAlg}$ 为结合代数对象的范畴。

## 要点

- 谱范畴是 $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G})$-线性的；因此这个单子是与结合代数对象 $\mathcal A_{G,\mathrm{irr}}:=(\mathbb L_{G,\mathrm{cusp}}\circ\mathbb L^L_{G,\mathrm{cusp}})(\mathcal O_{\operatorname{LocSys}^{\mathrm{irr}}_{\check G}})\in\operatorname{AssocAlg}(\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G}))$ 作张量积。
- 等价地，若在整个谱侧取 $\mathcal A_G=\mathbb L_G\mathbb L^L_G(\mathcal O)$，则 $\mathcal A_{G,\mathrm{irr}}\simeq\mathcal A_G|_{\operatorname{LocSys}^{\mathrm{irr}}_{\check G}}$。
- 这一限制并非仅由 $\operatorname{QCoh}^!$ 的记号形式地推出，而是来自重整化谱范畴与不可约开集上的普通 $\operatorname{QCoh}$-模结构的相容性。
- 因此唯一剩下的任务是 $\mathcal O_{\operatorname{LocSys}^{\mathrm{irr}}_{\check G}}\xrightarrow{\sim}\mathcal A_{G,\mathrm{irr}}$；这个陈述的可约部分已在上文通过 Eisenstein 归纳证明。
- 保守性的证明用 Whittaker 系数与几何 Ramanujan 输入：尖点对象是温和的，而 Whittaker 系数函数在温和子范畴上保守。

## 关键公式

- $\mathbb L_{G,\mathrm{cusp}}\circ\mathbb L^L_{G,\mathrm{cusp}}\in\operatorname{End}(\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G}))$
- $\mathcal A_{G,\mathrm{irr}}:=(\mathbb L_{G,\mathrm{cusp}}\circ\mathbb L^L_{G,\mathrm{cusp}})(\mathcal O_{\operatorname{LocSys}^{\mathrm{irr}}_{\check G}})\in\operatorname{AssocAlg}(\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G}))$
- $\mathcal A_{G,\mathrm{irr}}\simeq\mathcal A_G|_{\operatorname{LocSys}^{\mathrm{irr}}_{\check G}},\qquad \mathcal A_G=\mathbb L_G\mathbb L^L_G(\mathcal O)$

## 定理与证明

### 定理 16.7.1（保守性）（要点（有缺口））

函子 $\mathbb L_{G,\mathrm{cusp}}$ 是保守的。

1. 自守系数函子给出如下形式的方块：$\operatorname{DMod}(\operatorname{Bun}_G)_{\mathrm{cusp}}\xrightarrow{\mathbb L_{G,\mathrm{cusp}}}\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{irr}}_{\check G})$，下方 $\operatorname{Whit}(G)_{\mathrm{Ran}}\xrightarrow{\operatorname{CS}}\operatorname{Rep}(\check G)_{\mathrm{Ran}}$。  
   *为什么*：方块把谱侧与 Whittaker 系数函子连起来，使保守性可沿系数函子检验。
2. 下方的水平函子是 Casselman–Shalika 识别。  
   *为什么*：该识别是等价，因此「$\mathbb L_{G,\mathrm{cusp}}$ 保守」可化为 Whittaker 系数函子的保守性。
3. 由几何 Ramanujan 输入，尖点对象是温和的，而 Whittaker 系数函子在温和子范畴上保守；因此 $\mathbb L_{G,\mathrm{cusp}}$ 是保守的。  
   *为什么*：保守性在子范畴上成立即可推出在全范畴上成立，因为所讨论的对象都在温和子范畴内。

> 缺口：讲义自称「证明思路」，明确依赖几何 Ramanujan 输入（原书引 [FR25]、[Ber21]、[GR24b]），未展开该输入。

*出处*：定理 16.7.1 / 原书 p.81


## 易错点

- 保守性只给出「单子为恒等 ⇒ 等价」的一半：没有左伴随的存在性，保守函子不必是等价；讲义把伴随存在性单列为第二个输入。
- $\mathcal A_{G,\mathrm{irr}}\simeq\mathcal A_G|_{\operatorname{LocSys}^{\mathrm{irr}}_{\check G}}$ 不是 ${\operatorname{QCoh}^!}$ 记号的形式推论，而是重整化谱范畴与不可约开集上普通 $\operatorname{QCoh}$-模结构的相容性；把它当形式恒等式会跳过这一步。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§16.7 尖点函子的已知输入，p.81（PDF p.81），`源码/chapters/ch16.tex:159-180（定理 16.7.1、单子与 $\mathcal A_{G,\mathrm{irr}}$）`

## 核验

状态：`external-confirmed`（2026-11-18）
- arXiv:2409.08670 (ABC24b)：https://arxiv.org/abs/2409.08670 — 原文：「The functor 𝕃_{G,cusp} is conservative.」（引自 [FR, Theorem A]，由 [FR, Theorem B] 与 [Be2, Theorem A] 合成）——卡定理 16.7.1 即此。
- arXiv:2409.08670 (ABC24b)：https://arxiv.org/abs/2409.08670 — 原文：单子 𝕃_{G,cusp}∘𝕃^L_{G,cusp} 等于与结合代数 A_{G,irred}∈QCoh(LS^irred_Ĝ) 作张量积；它是等价当且仅当单位映射 O_{LS^irred_Ĝ} → A_{G,irred} 是同构——与卡的 A_{G,irr} 及剩余任务 O ≅ A_{G,irr} 一致。

## 关联

- `glc/concept/eisenstein-reduction`
- `glc/concept/double-adjunction`
- `glc/concept/numerical-rank-one`
