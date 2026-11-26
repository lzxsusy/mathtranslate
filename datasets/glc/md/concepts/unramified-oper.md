---
id: glc/concept/unramified-oper
type: concept
track: H
---

# 非分歧 oper 空间

> 穿孔圆盘上底层局部系统可延拓到圆盘的 oper 组成的纤维积，是临界 FLE 的谱空间。

**问题**：为什么 $\operatorname{Op}_{\check G}(D)\to\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 不是同构？

## 定义

令 $D=\operatorname{Spec} k[[t]]$、$D^\times=\operatorname{Spec} k((t))$、$L^+G=G[[t]]$、$LG=G((t))$。非分歧 oper 空间定义为纤维积
$$\operatorname{Op}^{\mathrm{unr}}_{\check G}:=\operatorname{Op}_{\check G}(D^\times)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D).$$
因此，它的一个点是穿孔圆盘上的 oper，其底层 $\check G$-局部系统可延拓到 $D$。映射 $\operatorname{Op}_{\check G}(D)\to\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 不是同构：局部系统可以延拓，并不迫使 oper 约化也正则地延拓。

*记号*：$D=\operatorname{Spec} k[[t]]$，$D^\times=\operatorname{Spec} k((t))$，$L^+G=G[[t]]$，$LG=G((t))$；$I$ 是 $\check{\mathfrak g}$ 的简单根指标集，$\check\alpha_i$ 为简单根，$f_i\in\check{\mathfrak g}_{-\check\alpha_i}$ 为简单负根向量；$\check\lambda\in X^*(\check T)^+$ 为优势权，等价地是 $G$ 的优势余权。

## 要点

- 非分歧只要求底层局部系统延拓到 $D$，并不要求 oper 约化在 $D$ 上也正则延拓；所以谱空间取纤维积 $\operatorname{Op}_{\check G}(D^\times)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)$，即「在 $D^\times$ 上是 oper、在 $D$ 上只是局部系统」。
- 它具有分支或形式片 $\operatorname{Op}^{\mathrm{unr},\check\lambda}_{\check G}$，而 $\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}\subset(\operatorname{Op}^{\mathrm{unr},\check\lambda}_{\check G})_{\mathrm{red}}$；后者正是按缺陷 $\check\lambda$ 切出的正则分层。
- 选平凡化后，$D^\times$ 上的 oper 形如 $\nabla=d+\omega$，$\omega\in\check{\mathfrak g}((t))\,dt$；非分歧意味着经某个 $\check G((t))$-规范变换后成为 $d+\eta$，$\eta\in\check{\mathfrak g}[[t]]\,dt$。
- 同一个规范变换未必使 $\eta\bmod\check{\mathfrak b}[[t]]$ 在 $t=0$ 处满足一般位置条件；缺陷由优势权 $\check\lambda\in X^*(\check T)^+$ 度量。
- 在相应的正则分层上 $\eta\bmod\check{\mathfrak b}[[t]]=\sum_{i\in I}t^{\langle\check\lambda,\check\alpha_i\rangle}\psi_i(t)f_i\,dt$，其中 $\psi_i\in k[[t]]$、$\psi_i(0)\ne0$。
- 集合意义下 $\operatorname{Op}^{\mathrm{unr}}_{\check G}(k)=\coprod_{\check\lambda\in X^*(\check T)^+}\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}(k)$。

## 关键公式

- $\operatorname{Op}^{\mathrm{unr}}_{\check G}:=\operatorname{Op}_{\check G}(D^\times)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)$
- $\eta\bmod\check{\mathfrak b}[[t]]=\sum_{i\in I}t^{\langle\check\lambda,\check\alpha_i\rangle}\psi_i(t)f_i\,dt$
- $\operatorname{Op}^{\mathrm{unr}}_{\check G}(k)=\coprod_{\check\lambda\in X^*(\check T)^+}\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}(k)$
- $\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}\subset(\operatorname{Op}^{\mathrm{unr},\check\lambda}_{\check G})_{\mathrm{red}}$

## 易错点

- 把 $\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 当成 $\operatorname{Op}_{\check G}(D)$：后者的点还要在 $t=0$ 处满足一般位置条件，而前者只要求底层局部系统延拓；译注特别提醒，缺这一对比就看不懂 §15.2 为何要用 $\check\lambda$ 分层去度量「缺陷」。
- $\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 有形式片 $\operatorname{Op}^{\mathrm{unr},\check\lambda}_{\check G}$，而 $\operatorname{Op}^{\mathrm{reg},\check\lambda}_{\check G}$ 只是其既约化的一部分；把正则分层直接当成整个形式片会丢掉非既约结构。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.2 非分歧 oper，p.72-73（PDF p.72-73），`源码/chapters/ch15.tex:23-33（$\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 的定义、$\check\lambda$ 分层与分解）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/oper — nLab 无 oper 条目（HTTP 404），无法核验非分歧 oper 的纤维积定义。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — §2.2 把 Op^unr 定义为与平凡局部系统同构的 oper，并给出 (2.1) Op^unr ≃ ⊔_{λ∈Λ+} Op^{unr,λ} 与 (Op^{unr,λ})_red ≃ Op^{reg,λ}；支持卡里纤维积的直观、集合分解与 Op^{reg,λ}⊂(Op^{unr,λ})_red，但未逐字给出 η 的 t^{⟨λ,α_i⟩}ψ_i f_i 展开式。

## 关联

- `glc/concept/pointwise-fle`
- `glc/concept/critical-weyl-object`
- `glc/concept/multipoint-localization`
