---
id: glc/concept/geometric-class-field-theory
type: concept
track: A
---

# 非分歧类域论（特征标形式）

> $\ell\ne\operatorname{char}(K)$，$K^\times\backslash\mathbb{A}_K^\times$、$\operatorname{Gal}_{\overline K/K}$ 非分歧特征标几乎双射。

**问题**：非分歧特征标 $\xi$ 与 $\rho$ 之间的对应由哪条等式刻画，两侧的「非分歧」各指什么？

## 定义

设 $K$ 为整体域，$\mathbb{A}_K$ 为其阿代尔环，$\operatorname{Gal}_{\overline K/K}$ 为其绝对 Galois 群，$\ell\ne\operatorname{char}(K)$。对每个有限素位 $v$，$\pi_v$ 是 $K_v$ 的一个素元所确定的类（模 $\mathcal{O}_v^\times$ 后有良好定义），$\operatorname{Fr}_v$ 是 $\operatorname{Gal}_{\overline{\kappa_v}/\kappa_v}$ 中几何 Frobenius 的一个提升（模惯性群 $I_v$ 后有良好定义）。称特征标 $\xi:K^\times\backslash\mathbb{A}_K^\times\to\overline{\mathbb{Q}}_\ell^\times$ 非分歧，是指对所有有限素位 $v$，$\xi$ 在 $\mathcal{O}_v^\times$ 上平凡；称特征标 $\rho:\operatorname{Gal}_{\overline K/K}\to\overline{\mathbb{Q}}_\ell^\times$ 非分歧，是指对所有有限素位 $v$，$\rho$ 在 $I_v$ 上平凡。定理断言：这两类非分歧特征标之间存在一个几乎双射，它由等式 $\xi(\pi_v)=\rho(\operatorname{Fr}_v)$ 刻画。

*记号*：$\mathbb{A}_K$：$K$ 的阿代尔环；$\overline{\mathbb{Q}}_\ell$：$\ell$-进系数域；$K_v$：$K$ 在有限素位 $v$ 处的完备化，$\mathcal{O}_v$ 为其整数环，$\kappa_v$ 为其剩余域；$I_v\subset\operatorname{Gal}_{\overline K/K}$：惯性群；$\operatorname{Fr}_v$：几何 Frobenius（模惯性群后良好定义）。「几乎双射」是讲义有意使用的不精确用语，精确陈述在后续讲授中给出。

## 要点

- 对应由局部 Frobenius 元刻画：对每个有限素位 $v$ 有 $\xi(\pi_v)=\rho(\operatorname{Fr}_v)$。
- 非分歧性在两侧各是一条平凡性条件：$\xi$ 在 $\mathcal{O}_v^\times$ 上平凡，$\rho$ 在 $I_v$ 上平凡。
- 对数域，由于 $\overline{\mathbb{Q}}_\ell^\times$ 完全不连通，互反映射的连通核无法被取值于 $\overline{\mathbb{Q}}_\ell^\times$ 的特征标检测到，因此对应只能是「几乎」双射。
- 对 $\mathbb{F}_q$ 上的函数域，精确表述改用 Weil 群 $W_{\overline K/K}$。

## 关键公式

- $\{\xi:K^\times\backslash\mathbb{A}_K^\times\to\overline{\mathbb{Q}}_\ell^\times\ \text{非分歧}\}\longleftrightarrow\{\rho:\operatorname{Gal}_{\overline K/K}\to\overline{\mathbb{Q}}_\ell^\times\ \text{非分歧}\}$
- $\xi(\pi_v)=\rho(\operatorname{Fr}_v)$
- $\theta_K:K^\times\backslash\mathbb{A}_K^\times\longrightarrow\operatorname{Gal}_{\overline K/K}^{\mathrm{ab}}\simeq\operatorname{Gal}_{K^{\mathrm{ab}}/K}$

## 定理与证明

### 非分歧类域论（特征标形式）（要点（有缺口））

设 $\ell\ne\operatorname{char}(K)$。存在一个几乎双射
$$\{\text{非分歧特征标 }\xi:K^\times\backslash\mathbb{A}_K^\times\to\overline{\mathbb{Q}}_\ell^\times\}\longleftrightarrow\{\text{非分歧特征标 }\rho:\operatorname{Gal}_{\overline K/K}\to\overline{\mathbb{Q}}_\ell^\times\},$$
它由等式 $\xi(\pi_v)=\rho(\operatorname{Fr}_v)$ 刻画；非分歧是指对一切有限素位 $v$，$\xi$ 在 $\mathcal{O}_v^\times$ 上平凡、$\rho$ 在 $I_v$ 上平凡。


> 缺口：讲义只述不证：§1.1 陈述该对应并解释「几乎」与「非分歧」，未给出证明；这是整体类域论的经典结论，讲义把它当作全篇的出发点。

*出处*：定理 1.1.1 / 原书 p.5


## 易错点

- 「几乎双射」不是同构：对数域，$\overline{\mathbb{Q}}_\ell^\times$ 完全不连通，互反映射的连通核检测不到，于是只在「几乎」的意义下对应；当成严格双射就丢掉了这一技术性缺口。
- 两侧的非分歧条件必须成对使用：$\xi$ 在 $\mathcal{O}_v^\times$ 上平凡与 $\rho$ 在 $I_v$ 上平凡是同一条非分歧性在自守侧与 Galois 侧的表述，只要求一侧不成陈述。
- 系数域是 $\overline{\mathbb{Q}}_\ell$（讲义写作 $\mathbb{Q}_\ell$ 的代数闭包），且要求 $\ell\ne\operatorname{char}(K)$；函数域情形的精确陈述要把 $\operatorname{Gal}^{\mathrm{ab}}$ 换成 Weil 群。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§1.1 几何类域论，p.5（PDF p.5），`源码/chapters/ch01.tex:23-33（定理 1.1.1）`
- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§1.1 几何类域论，p.5（PDF p.5），`源码/chapters/ch01.tex:9-16（互反映射与局部 Frobenius）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Artin+reciprocity+law — 页面给出互反映射 𝕀_K→Gal(K^ab/K)，(a_v)↦∏_v Frob_v^{ord_v(a_v)}；并说明数域情形该映射经 idèle 类群分解、再商去单位分支后为同构。这支持卡里 θ_K 的公式与「几乎」的成因（Q̄_ℓ^× 完全不连通、连通核检测不到），但页面没有逐字陈述「非分歧 ξ 与非分歧 ρ 的几乎双射、由 ξ(π_v)=ρ(Fr_v) 刻画」这条定理。
- nLab：https://ncatlab.org/nlab/show/class+field+theory — 页面只有 Idea/History/References，未陈述定理 1.1.1 的非分歧特征标对应。

## 关联

- `glc/concept/hecke-eigensheaf-gl1`
- `glc/concept/gl1-trace-character`
- `glc/concept/deligne-gl1-existence`
