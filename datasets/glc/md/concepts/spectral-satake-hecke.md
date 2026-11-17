---
id: glc/concept/spectral-satake-hecke
type: concept
track: H
---

# 临界球面 Hecke 范畴的谱描述

> 临界球面 Hecke 范畴等价于穿孔圆盘粘接局部系统的 Steinberg 叠上的 IndCoh，卷积变为对应作用。

**问题**：临界球面 Hecke 范畴的卷积在 FLE 下变成什么？

## 定义

临界球面 Hecke 范畴被识别为局部系统 Steinberg 叠上的 ind-凝聚层：
$$\operatorname{DMod}(L^+G\backslash LG/L^+G)_{\mathrm{crit}}\simeq\operatorname{IndCoh}\bigl(\operatorname{LocSys}_{\check G}(D)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)\bigr).$$

*记号*：$L^+G\backslash LG/L^+G$ 是球面 Hecke 叠；右端是「两个圆盘上的局部系统沿穿孔圆盘粘起来」的纤维积，即 Steinberg 型叠。

## 要点

- 该叠是 $\operatorname{LocSys}_{\check G}(D)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)$：两个圆盘上的 $\check G$-局部系统沿穿孔圆盘粘起来。
- 在 FLE 下，这个范畴的卷积变成 $\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$ 上自然的对应作用。
- 在 Frenkel–Gaitsgory 最初的证明中，这出现在阿贝尔范畴和阿贝尔几何 Satake 的层面。
- 整体 Langlands 需要 DG／因子化表述。
- 该识别使球面范畴的 Satake 作用可以从谱侧读出来，这是定理 15.2.1 中「与几何 Satake 作用相容」的来源之一。

## 关键公式

- $\operatorname{DMod}(L^+G\backslash LG/L^+G)_{\mathrm{crit}}\simeq\operatorname{IndCoh}\bigl(\operatorname{LocSys}_{\check G}(D)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)\bigr)$
- $\text{卷积}\ \longleftrightarrow\ \operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})\ \text{上的对应作用}$

## 定理与证明

### 命题（球面 Hecke 范畴的谱描述，无编号）（要点（有缺口））

临界球面 Hecke 范畴等价于 $\operatorname{IndCoh}$ 在 Steinberg 叠 $\operatorname{LocSys}_{\check G}(D)\times_{\operatorname{LocSys}_{\check G}(D^\times)}\operatorname{LocSys}_{\check G}(D)$ 上，且 FLE 下卷积变为 $\operatorname{Op}^{\mathrm{unr}}_{\check G}$ 上的对应作用。

1. 该叠由两个圆盘上的 $\check G$-局部系统沿穿孔圆盘粘接而成。  
   *为什么*：球面 Hecke 算子天生涉及两个圆盘（一个插入、一个基点），粘接正是谱侧的对应。
2. 在 FLE 下把卷积翻译成 $\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$ 上的对应作用。  
   *为什么*：球面范畴的 Satake 作用因此可以从谱侧读出，这也是定理 15.2.1 中「与几何 Satake 作用相容」的来源。

> 缺口：讲义只述结论并注明 Frenkel–Gaitsgory 的原始证明在阿贝尔层面，DG／因子化表述属整体 Langlands 的需要，本书未证明。

*出处*：无编号陈述 / 原书 p.73


## 易错点

- 把「卷积」误当成 $\operatorname{IndCoh}(\operatorname{Op}^{\mathrm{unr}}_{\check G})$ 上的逐点乘法：讲义只说它变成「自然的对应作用」，并未写成显式公式。
- 右端两个因子都是 $\operatorname{LocSys}_{\check G}(D)$，粘接发生在 $\operatorname{LocSys}_{\check G}(D^\times)$ 上；写成 $\operatorname{LocSys}_{\check G}(D)\times\operatorname{LocSys}_{\check G}(D)$ 会丢掉这个纤维积。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§15.3 Drinfeld–Sokolov 约化与 Whittaker 形式，p.73（PDF p.73），`源码/chapters/ch15.tex:57-63（临界球面 Hecke 范畴的谱描述）`

## 核验

状态：`source-only`（2026-11-18）
- Arinkin–Beraldo–Campbell–Chen–Færgeman–Gaitsgory–Lin–Raskin–Rozenblyum, Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE：https://arxiv.org/abs/2405.03648 — 全文无 Steinberg 字样；本次检索未命中 DMod(L^+G\LG/L^+G)_crit ≃ IndCoh(LocSys_Ǧ(D)×_{LocSys_Ǧ(D^×)}LocSys_Ǧ(D)) 的逐字陈述。
- Frenkel–Gaitsgory, Local geometric Langlands correspondence: the spherical case：https://arxiv.org/abs/0711.1132 — 全文无 Satake 字样，未覆盖球面 Hecke 范畴的谱描述。

## 关联

- `glc/concept/pointwise-fle`
- `glc/concept/quantum-local-langlands`
- `glc/concept/whittaker-equivalence`
