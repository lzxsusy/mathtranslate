---
id: glc/concept/tempered-category
type: concept
track: H
---

# 温和范畴

> 使重构映射的像覆盖整个范畴的 $G(\mathcal K)$-范畴；它是保守性定理成立的子范畴，非分歧时用球面不变量到 Whittaker 不变量的保守性判定。

**问题**：一个 $G(\mathcal K)$-范畴「温和」的判据是什么，非分歧情形下又怎么判定？

## 定义

设 $\mathcal C$ 是 $G(\mathcal K)$-范畴。重构映射 $\operatorname{Wh}(\operatorname{DMod}(G(\mathcal K)))\otimes_{\operatorname{BiWhit}(G)}\operatorname{Wh}(\mathcal C)\to\mathcal C$ 全忠实，其像是由 $\operatorname{Wh}(\mathcal C)$ 生成的 $\operatorname{DMod}(G(\mathcal K))$-子模；因此，$\mathcal C$ 温和，当且仅当这个像是整个 $\mathcal C$。非分歧情形更为明确：带强 $G(\mathcal O)$ 作用的 $G(\mathcal K)$-范畴 $\mathcal C$ 受其球面不变量 $\mathcal C^{G(\mathcal O)}$ 控制，后者是一个 $\operatorname{Sph}_{G,x}$-模；导出 Satake 给出伴随／重构图景 $\operatorname{DMod}(G(\mathcal K)/G(\mathcal O))\otimes_{\operatorname{Sph}_{G,x}}\mathcal C^{G(\mathcal O)}\rightleftarrows\mathcal C$，而几何 Casselman–Shalika 等价将从球面到 Whittaker 的比较识别为通常的从 $\operatorname{Sph}_{G,x}$ 到 $\operatorname{Rep}(\check G)$ 的过渡。因此在非分歧情形中，$\mathcal C$ 温和，当且仅当从球面不变量到 Whittaker 不变量的函子在相关的生成子范畴上保守。

*记号*：$\mathcal O$、$\mathcal K$ 为形式幂级数环与形式 Laurent 级数域；$\operatorname{Sph}_{G,x}$ 为球面 Hecke 范畴；$\mathcal C^{G(\mathcal O)}$ 为球面不变量；$\operatorname{Rep}(\check G)$ 为 $\check G$ 的表示范畴。

## 要点

- 温和性是范畴的性质，判据是重构映射的像等于整个范畴。
- 非分歧情形的判据：从球面不变量到 Whittaker 不变量的函子在相关的生成子范畴上保守。
- 对 $\operatorname{Bun}_G$：每个 $x\in X$ 通过 Hecke 修改给出 $\operatorname{Sph}_{G,x}$ 的作用，Arinkin–Gaitsgory 对 $\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}$ 的定义是从这一作用转到温和谱 Hecke 范畴得到的。
- Færgeman–Raskin 的定理证明这个定义与 $x$ 无关。
- 还有左温和与右温和的变体；在局部预期它们相同，在全局这反映为 Whittaker 系数与所选点无关。

## 关键公式

- $\mathcal C\ \text{温和}\iff \text{重构映射的像}=\mathcal C$
- $\operatorname{DMod}(G(\mathcal K)/G(\mathcal O))\otimes_{\operatorname{Sph}_{G,x}}\mathcal C^{G(\mathcal O)}\rightleftarrows\mathcal C$
- $\operatorname{DMod}(G(\mathcal K))\text{-}\mathrm{Mod}^{\mathrm{temp}}\simeq\operatorname{ShvCat}(\operatorname{LocSys}_{\check G}(D^\circ))$

## 定理与证明

### 非分歧情形的温和性判据（要点（有缺口））

在非分歧情形中，$\mathcal C$ 温和，当且仅当从球面不变量到 Whittaker 不变量的函子在相关的生成子范畴上保守。

1. 用导出 Satake 的伴随／重构图景与几何 Casselman–Shalika 等价，把温和性判据化为该保守性。  
   *为什么*：几何 Casselman–Shalika 把球面到 Whittaker 的比较识别为 $\operatorname{Sph}_{G,x}\to\operatorname{Rep}(\check G)$ 的过渡。

> 缺口：讲义只述不证（§13.2）；所需输入为导出 Satake 与几何 Casselman–Shalika 等价，见 [Gai18]、[FR23]。

*出处*：§13.2 局部 Whittaker 范畴与温和性 / 原书 p.65


## 易错点

- 温和性是范畴的性质，不是单个层的性质；对单个对象只能说它属于 $\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}$。
- 左温和与右温和是不同变体，讲义只说「在局部预期它们相同」，不要当作已证。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§13.2 局部 Whittaker 范畴与温和性，p.65（PDF p.65），`源码/chapters/ch13.tex:61-69（温和性判据与非分歧情形）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FR23：https://arxiv.org/abs/2108.02719 — 「The subcategory D(Bun_G)_{x-temp} ⊂ D(Bun_G) is independent of the choice of point x」——支持卡「DMod(Bun_G)^temp 的定义与 x 无关（Færgeman–Raskin）」
- FR25：https://arxiv.org/abs/2207.02955 — anti-temp 是满子范畴、嵌入有左伴随；temp 是商 D/D^{anti-temp}；投影有全忠实左伴随；[FR] 证与 x 无关——支持卡的温和判据
- nLab：https://ncatlab.org/nlab/show/geometric+Satake+equivalence — 「DMod(Gr_G)^{L+G} ≃ Rep(^L G)」为对称幺半等价（左卷积幺半、右表示张量积）——支持卡「Sph 到 Rep(Ǧ) 的过渡」
- FR25：https://arxiv.org/abs/2207.02955 — §5.3 标题即 The Casselman-Shalika formula；coeff_D ≃ coeff(V^D⋆−)——支持卡「几何 Casselman–Shalika 把球面到 Whittaker 的比较识别为 Sph→Rep(Ǧ)」

## 关联

- `glc/concept/local-whittaker-category`
- `glc/concept/whittaker-conservativity`
- `glc/concept/global-nilpotent-cone`
