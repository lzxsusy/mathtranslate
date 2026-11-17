---
id: glc/concept/categorical-langlands-conjecture
type: concept
track: F
---

# 范畴形式的几何 Langlands 猜想

> de Rham 情形下 $\operatorname{DMod}(\operatorname{Bun}_G)$ 与谱侧幂零奇异支撑的 ind-凝聚层范畴之间的预期等价。

**问题**：范畴猜想的右端为什么是 $\operatorname{IndCoh}_{\mathrm{Nilp}}$，而不能写成 $\operatorname{QCoh}$？

## 定义

本章取 $k=\mathbb{C}$，系数域也取 $\mathbb{C}$；除非另有说明，均在 de Rham 情形下讨论。记 $\operatorname{LocSys}_{\check G}$ 为 $X$ 上 de Rham $\check G$-局部系统的导出叠。忽略惯常的半扭转，预期的等价采用 Arinkin–Gaitsgory／Gaitsgory–Raskin 的表述（[AG15, GR24a]）：$\operatorname{DMod}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$。右端之所以采用这个范畴，是因为 $\operatorname{LocSys}_{\check G}$ 作为导出叠通常是奇异的。

*记号*：$\operatorname{Bun}_G$ 是 $X$ 上 $G$-丛的模叠；$\operatorname{DMod}$ 是 de Rham $D$ 模范畴；$\operatorname{IndCoh}_{\mathrm{Nilp}}$ 是奇异方向落在幂零锥内的 ind-凝聚层范畴；“半扭转”指两侧各差一个 Tate 扭转 $(\text{--})(1/2)$。

## 要点

- 这是几何 Langlands 的范畴形式：从单个 Hecke 特征层转向整个自守范畴的等价。
- 等价在忽略惯常半扭转的意义下陈述，表述属 Arinkin–Gaitsgory／Gaitsgory–Raskin（[AG15, GR24a]）。
- $\operatorname{LocSys}_{\check G}$ 作为导出叠通常是奇异的，这是右端出现 ind-凝聚层的原因。
- $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$、$\operatorname{IndCoh}(\operatorname{LocSys}_{\check G})$ 以及中间的 $\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$ 确实是不同的范畴。
- 本章随后用导出 Satake（§10.3）、Eisenstein 级数（§10.4）与温和对象（§10.5）三项相容性检验来支持这一猜想。

## 关键公式

- $\operatorname{DMod}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$

## 定理与证明

### 范畴猜想（§10 开头，未编号）（要点（有缺口））

忽略惯常的半扭转，$\operatorname{DMod}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$。

1. 局部检验：导出 Satake 把局部球面范畴识别为谱 Hecke 叠上幂零支撑的 ind-凝聚层（§10.3）。  
   *为什么*：这是全局猜想的局部模型，说明右端的范畴在局部是对的。
2. 结构检验：谱 Eisenstein 函子把 Levi 侧的完美对象送进幂零支撑范畴，且这些对象生成它（§10.4）。  
   *为什么*：说明幂零条件不是可选项，而是 Eisenstein 相容性强制的。
3. 整体检验：温和猜想加 Eisenstein 相容性等价于完整猜想（§10.5）。  
   *为什么*：把猜想拆成“温和部分”与“Eisenstein 生成”两块，各自可以独立检验。

> 缺口：这是猜想，讲义未给证明；§10.1–§10.6 给出的是相容性检验（导出 Satake、Eisenstein、温和对象、Betti 版本），不是证明。

*出处*：§10 开头（未编号猜想）/ 原书 p.53


## 易错点

- 右端是 $\operatorname{IndCoh}_{\mathrm{Nilp}}$，不是 $\operatorname{QCoh}$：在奇异的导出叠上两者不同，用 $\operatorname{QCoh}$ 会丢掉奇异支撑信息。
- 等价是在“忽略惯常半扭转”的前提下写的：两侧的 Tate 扭转差半格，逐项对齐时要补上 $(\text{--})(1/2)$。
- 它是猜想而非定理：讲义只用相容性检验支持它，不要写成已证结论。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§10 范畴猜想（引言），p.53（PDF p.53），`§10 范畴猜想（引言）（ch10.tex:7-15，未编号猜想，p.53）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/geometric+Langlands+correspondence — 页面写明 AG12 精化 (Ind(OMod(Loc_{^L G}(Σ))))_{Nilp_Glob} ≃ DMod(Bun_G(Σ))（conjecture 0.1.6），并称 2025 年已由 Gaitsgory 等证明；这与卡中 de Rham 猜想 DMod(Bun_G) ≃ IndCoh_{Nilp}(LocSys_{\check G}) 是同一猜想的两种写法，Nilp 条件一致。页面未提半扭转 (--)(1/2)。
- arXiv：https://arxiv.org/abs/2405.03599 — 摘要：在 de Rham 与 Betti 情形构造自守→谱侧函子，并证明猜想各形式（de Rham/Betti、restricted/non-restricted、tempered/non-tempered）等价；支持卡中「采用 Gaitsgory–Raskin 表述」。摘要未给 IndCoh_Nilp 公式或半扭转。

## 关联

- `glc/concept/ind-coherent-sheaves`
- `glc/concept/nilpotent-singular-support`
- `glc/concept/tempered-categorical-conjecture`
