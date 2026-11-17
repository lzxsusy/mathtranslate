---
id: glc/concept/km-whittaker-duality
type: concept
track: H
---

# Kac–Moody–Whittaker 对偶与常数项相容性

> 常数项相容性 (16.2) 需用 KM–Whittaker 对偶：临界 KL 范畴之间的函子由半无限上同调给出。

**问题**：为什么常数项相容性比 Eisenstein 相容性更难？

## 定义

§16.5：证明 (16.1) 的方法不能直接证明常数项相容性 (16.2)。在 Eisenstein 图表中，所有箭头都指向推前所需的方向；对于 $\operatorname{CT}_P$，必须反转这些箭头，而简单的几何论证不再适用。替代方法是 Kac–Moody–Whittaker 对偶：在非临界水平比较 $\operatorname{Whit}_\kappa(M)$ 与 $\operatorname{Whit}_\kappa(G)$（经 $\operatorname{coeff}_M$、$\operatorname{coeff}_G$ 与 $\operatorname{Eis}_P$ 的方块）。

*记号*：$\operatorname{CT}_P$ 为常数项函子；$\mathfrak u$ 是 $P$ 的幺幂根基的 Lie 代数；$\operatorname{SI}^{\mathrm{spec}}_{\check P^-}$ 为谱侧的半无限范畴；$\operatorname{KL}_{G,\mathrm{crit}}$ 为临界 Kazhdan–Lusztig 范畴。

## 要点

- 特殊化到临界水平（等价地，特殊化到 FLE 退化中量子参数的边界值），局部 Whittaker 范畴被球面临界 Kac–Moody 范畴替换。
- 在 $\operatorname{IndCoh}$ 约定下，FLE 识别 $\operatorname{KL}_{G,\mathrm{crit}}\simeq\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$ 与 $\operatorname{KL}_{M,\mathrm{crit}}\simeq\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check M})$。
- 相应的局部函子为 $r^{\mathrm{KM}}_P:\operatorname{KL}_{G,\mathrm{crit}}\to\operatorname{KL}_{M,\mathrm{crit}}$，$M\longmapsto C^{\infty/2}(\mathfrak u((t)),M)$。
- 它的谱对应物是 $r^{\mathrm{op}}_{\check P}:\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})\to\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check M})$，由 $\operatorname{SI}^{\mathrm{spec}}_{\check P^-}$ 中的单位对象给出。
- 这些函子证明了常数项立方体的顶面与侧面；剩余的前面与后面并非仅由半无限论证推出，而是通过手征方法证明。这就完成了常数项相容性 (16.2) 的证明。

## 关键公式

- $r^{\mathrm{KM}}_P:\operatorname{KL}_{G,\mathrm{crit}}\longrightarrow\operatorname{KL}_{M,\mathrm{crit}},\qquad M\longmapsto C^{\infty/2}(\mathfrak u((t)),M)$
- $r^{\mathrm{op}}_{\check P}:\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})\longrightarrow\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check M})$
- $\operatorname{CT}^{\mathrm{spec}}_{\check P}\circ\mathbb L_G\simeq\mathbb L_M\circ\operatorname{CT}_P$（图表 (16.2) 交换）

## 定理与证明

### 定理（常数项相容性，图表 16.2，无编号）（要点（有缺口））

图表 (16.2) 交换：$\operatorname{CT}^{\mathrm{spec}}_{\check P}\circ\mathbb L_G\simeq\mathbb L_M\circ\operatorname{CT}_P$，即自守常数项函子与谱侧 $\operatorname{CT}^{\mathrm{spec}}_{\check P}$ 在 Langlands 函子下相容。

1. 在非临界水平比较 $\operatorname{Whit}_\kappa(M)$ 与 $\operatorname{Whit}_\kappa(G)$，用 $\operatorname{coeff}$ 与 $\operatorname{Eis}_P$ 的方块。  
   *为什么*：这给出 (16.2) 在非临界水平的模型；临界水平是其边界值。
2. 特殊化到临界水平：Whittaker 范畴被 $\operatorname{KL}$ 范畴替换，FLE 把它们识别为非分歧 oper 上的 $\operatorname{IndCoh}$。  
   *为什么*：于是自守侧的函子变成 $r^{\mathrm{KM}}_P$，谱侧变成由 $\operatorname{SI}^{\mathrm{spec}}_{\check P^-}$ 单位对象给出的 $r^{\mathrm{op}}_{\check P}$。
3. 用 $r^{\mathrm{KM}}_P$ 与 $r^{\mathrm{op}}_{\check P}$ 证明常数项立方体的顶面与侧面，其余前面与后面用手征方法。  
   *为什么*：讲义指出前后两面不是半无限论证的推论，必须另用手征方法；四面合起来即 (16.2)。

> 缺口：讲义只给证明路径（顶面与侧面由半无限函子给出，前后两面用手征方法），未展开细节；见 [CCF24]。

*出处*：§16.5 / 原书 p.79-80


## 易错点

- 把 $r^{\mathrm{KM}}_P$ 与 $r^-_P$ 混为一谈：$r^{\mathrm{KM}}_P$ 是 $\operatorname{KL}$ 范畴之间由 $C^{\infty/2}(\mathfrak u((t)),-)$ 给出的函子，$r^-_P$ 是 Whittaker 范畴之间由半无限核给出的限制函子；与 $J^-$ 配对的是后者。
- $r^{\mathrm{KM}}_P$ 里是 $\mathfrak u$（$P$ 的幺幂根基），而半无限对应用的是 $P^-$；讲义说这一「$P^-$ 与 $P$ 的错位」正是第二伴随性的表现，不是笔误。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§16.5 为何常数项更困难，p.79-80（PDF p.79-80），`源码/chapters/ch16.tex:121-135（KM–Whittaker 对偶、$r^{\mathrm{KM}}_P$ 与 $r^{\mathrm{op}}_{\check P}$）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv:2409.07051 (CCF24)：https://arxiv.org/abs/2409.07051 — 原文：「Assuming the validity of GLC for M, there exists a unique datum of commutation for the upper lid …」，并给出 CT^-_{*,ρ_P(ω_X)}[−δ] 与 CT^{−,spec} 的交换方块——即卡 (16.2)（CT^spec_P̂∘𝕃_G ≃ 𝕃_M∘CT_P）的带扭/移位版本。
- arXiv:2409.07051 (CCF24)：https://arxiv.org/abs/2409.07051 — 原文确有 Kac–Moody 型 Jacquet 函子（对 𝔫^-_P 的 BRST 约化）与 oper 侧对偶函子的一般构造，支持卡的路线；但卡中 r^KM_P: M↦C^{∞/2}(u((t)),M) 与 r^op 由 SI^spec 单位对象给出的逐字陈述未见。

## 关联

- `glc/concept/semi-infinite-category`
- `glc/concept/eisenstein-compatibility`
- `glc/concept/cuspidal-conservativity`
