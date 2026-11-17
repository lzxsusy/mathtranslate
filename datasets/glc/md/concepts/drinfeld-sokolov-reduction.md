---
id: glc/concept/drinfeld-sokolov-reduction
type: concept
track: H
---

# Drinfeld–Sokolov 约化（半无限上同调）

> $\Psi(M)=C^{\infty/2}(\mathfrak n((t)),M\otimes k_\chi)$：临界模的半无限上同调，也称 BRST 约化，是 FLE 的底层函子。

**问题**：$\Psi(M)$ 中 $\infty/2$ 与 $k_\chi$ 各指什么？

## 定义

选定标准的非退化加性特征标 $\chi:\mathfrak n((t))\to k$。对临界模 $M$，置
$$\Psi(M):=C^{\infty/2}(\mathfrak n((t)),M\otimes k_\chi).$$
这就是 $M$ 的半无限上同调，也称 BRST 约化。

*记号*：$\mathfrak n\subset\mathfrak g$ 为幂零子代数，$\mathfrak n((t))$ 为其环路版本；$k_\chi$ 是由加性特征标 $\chi$ 给出的一维模；$\infty/2$ 指半无限维数。

## 要点

- FLE 的底层函子是 Drinfeld–Sokolov 约化。
- 在临界水平，$\Psi$ 有一个增强版本，取值于穿孔圆盘上 oper 空间上的层。
- 相应的 Whittaker 陈述读作 $\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{\mathrm{Whit}}\simeq\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times))$。
- 从 Whittaker 形式转到球面／Kazhdan–Lusztig 子范畴，在谱侧相当于施加底层局部系统可延拓到 $D$ 的条件，因此将 $\operatorname{Op}(D^\times)$ 替换为 $\operatorname{Op}^{\mathrm{unr}}$。
- 在临界水平，$\Psi$ 恰好等同于 Drinfeld–Sokolov 约化，因此 $\Psi(M)$ 可以当作 $M$ 的半无限不变量。

## 关键公式

- $\Psi(M):=C^{\infty/2}(\mathfrak n((t)),M\otimes k_\chi)$
- $\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{\mathrm{Whit}}\simeq\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times))$

## 定理与证明

### 命题（Whittaker 形式的 FLE，无编号）（要点（有缺口））

$\widehat{\mathfrak g}_{\mathrm{crit}}\text{-}\mathrm{Mod}^{\mathrm{Whit}}\simeq\operatorname{IndCoh}(\operatorname{Op}_{\check G}(D^\times))$；转到球面／KL 子范畴，在谱侧相当于要求底层局部系统延拓到 $D$，故目标换成 $\operatorname{Op}^{\mathrm{unr}}_{\check G}$。

1. 临界 Whittaker 范畴的谱描述是 $\operatorname{IndCoh}(\operatorname{Op}(D^\times))$。  
   *为什么*：$\Psi$ 在临界水平恰好等于 Drinfeld–Sokolov 约化，其增强版本取值于穿孔圆盘 oper 空间上的层。
2. 从 Whittaker 形式转到球面／Kazhdan–Lusztig 子范畴，在谱侧相当于施加「底层局部系统可延拓到 $D$」的条件。  
   *为什么*：球面子范畴对应非分歧条件，因此 $\operatorname{Op}(D^\times)$ 被替换为 $\operatorname{Op}^{\mathrm{unr}}$。

> 缺口：讲义只述该转述方向，未在本书给出证明；细节见 Frenkel–Gaitsgory 原文与 §15.2 的 FLE 陈述。

*出处*：无编号陈述 / 原书 p.73


## 易错点

- $\infty/2$ 是半无限维数，不是分数次幂：先取 $\mathfrak n((t))$ 在临界中心扩张下的真空模，再作半无限 Chevalley 上链；缺这层，$\Psi$ 就只是一个记号。
- $k_\chi$ 是加性特征标 $\chi$ 给出的一维模；漏掉它，$C^{\infty/2}(\mathfrak n((t)),M)$ 就不是 Drinfeld–Sokolov 约化。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.3 Drinfeld–Sokolov 约化与 Whittaker 形式，p.73（PDF p.73），`源码/chapters/ch15.tex:46-55（$\Psi$ 的定义与 Whittaker 陈述）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Drinfeld-Sokolov+reduction — 页面只有 DS 约化的文献目录，无 ∞/2 或半无限上同调的定义；不能支持卡里 Ψ=C^{∞/2}(n((t)),−⊗k_χ) 的公式。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence and affine Kac–Moody algebras：https://arxiv.org/abs/math/0508382 — 摘要说临界水平某商范畴 ≃ 幂零 oper 加厚上的 QCoh，支持临界 DS/Whittaker 侧的谱描述方向，但未给 C^{∞/2} 公式。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — Prop 3.5 使用 Ψ 并给出 Ψ(Vλ_crit)≃z^{reg,λ}，支持 Ψ 是 DS 型函子及其在 Weyl 对象上的取值；未给 ∞/2 链复形定义。

## 关联

- `glc/concept/pointwise-fle`
- `glc/concept/whittaker-equivalence`
- `glc/concept/critical-weyl-object`
