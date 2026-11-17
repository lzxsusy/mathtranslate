---
id: glc/concept/critical-weyl-object
type: concept
track: H
---

# 临界 Weyl 对象与 Drinfeld–Sokolov 像

> 临界 Weyl 对象 $\mathbb W^{\check\lambda}_{\mathrm{crit}}$ 的 DS 像是正则 oper 分层上的函数，FLE 下对应 $(i_{\check\lambda})_*\mathcal O$。

**问题**：$\mathbb W^{\check\lambda}_{\mathrm{crit}}$ 在 FLE 下的像是什么？

## 定义

令 $\mathbb W^{\check\lambda}_{\mathrm{crit}}$ 为相应最高权（Schubert 标号 $\check\lambda$）的临界 Weyl 对象，并令 $i_{\check\lambda}:\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}\hookrightarrow\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 为 §15.2 正则分层的包含。

*记号*：$\check\lambda$ 同时是最高权与 Schubert 标号；$\mathfrak z^{\mathrm{reg},\check\lambda}$ 是正则分层 $\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$ 对应的交换代数；$(i_{\check\lambda})^{\operatorname{IndCoh}}_*$ 是 $\operatorname{IndCoh}$ 下的推前。

## 要点

- Drinfeld–Sokolov 约化给出 $\Psi(\mathbb W^{\check\lambda}_{\mathrm{crit}})\simeq\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{End}(\mathbb W^{\check\lambda}_{\mathrm{crit}})$ 且 $\operatorname{Spec}\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$。
- 在 FLE 下，在相应 $\operatorname{IndCoh}$ 约定下，$\mathbb W^{\check\lambda}_{\mathrm{crit}}$ 对应于 $(i_{\check\lambda})^{\operatorname{IndCoh}}_*\mathcal O_{\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}}$。
- 因此球面临界范畴的支撑恰好是非分歧 oper 轨迹；自守侧的非分歧对应于谱侧单值性平凡。
- $\operatorname{End}(\mathbb W^{\check\lambda}_{\mathrm{crit}})$ 与 $\mathfrak z^{\mathrm{reg},\check\lambda}$ 的等同是 Drinfeld–Sokolov 约化的输出，不是形式恒等式。

## 关键公式

- $\Psi(\mathbb W^{\check\lambda}_{\mathrm{crit}})\simeq\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{End}(\mathbb W^{\check\lambda}_{\mathrm{crit}})$
- $\operatorname{Spec}\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$
- $\mathbb W^{\check\lambda}_{\mathrm{crit}}\ \longleftrightarrow\ (i_{\check\lambda})^{\operatorname{IndCoh}}_*\mathcal O_{\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}}$

## 定理与证明

### Weyl 对象的 Drinfeld–Sokolov 像（§15.2）（要点（有缺口））

$\Psi(\mathbb W^{\check\lambda}_{\mathrm{crit}})\simeq\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{End}(\mathbb W^{\check\lambda}_{\mathrm{crit}})$ 且 $\operatorname{Spec}\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$；在 FLE 下 $\mathbb W^{\check\lambda}_{\mathrm{crit}}$ 对应 $(i_{\check\lambda})^{\operatorname{IndCoh}}_*\mathcal O_{\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}}$。

1. 用 Drinfeld–Sokolov 约化计算 $\Psi(\mathbb W^{\check\lambda}_{\mathrm{crit}})$。  
   *为什么*：$\Psi$ 是 FLE 的底层函子（§15.3），它在 Weyl 对象上的像给出该对象在谱侧的支撑。
2. 由 $\operatorname{Spec}\mathfrak z^{\mathrm{reg},\check\lambda}\simeq\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$ 读出像为 $(i_{\check\lambda})^{\operatorname{IndCoh}}_*\mathcal O$。  
   *为什么*：正则分层上的函数环是其坐标环，$\operatorname{IndCoh}$ 下正对应推前结构层。

> 缺口：讲义只述不证：这是 Drinfeld–Sokolov 约化的已知计算，本书此处未给细节，原书引 [FG05]、[FG07]。

*出处*：§15.2（Weyl 对象段）/ 原书 p.73


## 易错点

- $\mathfrak z^{\mathrm{reg},\check\lambda}$ 不是整个中心 $\mathfrak z_{\mathrm{crit}}$：它只对应正则分层 $\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$，随 $\check\lambda$ 改变。
- 等式 $\Psi(\mathbb W^{\check\lambda}_{\mathrm{crit}})\simeq\operatorname{End}(\mathbb W^{\check\lambda}_{\mathrm{crit}})$ 里 $\Psi$ 是半无限上同调，不是 $\operatorname{Hom}$ 或 $\operatorname{End}$ 的记号替换。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.2 非分歧 oper，p.72-73（PDF p.72-73），`源码/chapters/ch15.tex:41-44（Weyl 对象及其 FLE 像）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — Prop 3.5 与 (3.5)：Ψ(Vλ_crit) ≃ z^{reg,λ}，行 367-368 给出 z^{reg,λ} ≃ End(Vλ_crit)；支持卡里两条等式。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — §2.2 定义 z^{reg,λ} 为 Z_g 对应 Op^{reg,λ} 的商（行 346-352），Spec(z^{reg,λ}) ↪ Spec(Z^{unr,λ}) 是正则嵌入（行 417）；支持 Spec z^{reg,λ} ≃ Op^{reg,λ}。
- Arinkin–Beraldo–Campbell–Chen–Færgeman–Gaitsgory–Lin–Raskin–Rozenblyum, Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE：https://arxiv.org/abs/2405.03648 — Lemma 7.3.10 证明中：Weyl 模 Vλ_crit 在 DS^{enh,rfnd} 下的像是 Op^{λ-reg} 的结构层 O_{Op^{λ-reg}}；支持卡里 FLE 像 (i_λ)_*O 与支撑断言。

## 关联

- `glc/concept/pointwise-fle`
- `glc/concept/drinfeld-sokolov-reduction`
- `glc/concept/unramified-oper`
