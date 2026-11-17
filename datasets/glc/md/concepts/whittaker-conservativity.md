---
id: glc/concept/whittaker-conservativity
type: concept
track: H
---

# Whittaker 系数的保守性

> 限制到温和部分后，重整化 Whittaker 系数函子保守——系数为零则对象本身为零；de Rham 与受限（Betti／可构造）两种形式各有一条。

**问题**：保守性定理对哪个子范畴断言「系数为零则对象为零」，它的论证最后一步为什么能推出 $\mathcal F=0$？

## 定义

本章记录的是重整化 Whittaker 系数函子的保守性。在范畴 Langlands 的 de Rham 形式中，预期有 $\operatorname{DMod}(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$ 以及 $\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$；在 Betti 理论或可构造理论中，相应的谱叠是 $\operatorname{LocSys}^{\mathrm{restr}}_{\check G}$，自守侧使用 $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$，即层范畴中具有幂零奇异支撑的部分。所谓「保守」意味着：若系数为零，则对象本身为零。

*记号*：$\operatorname{IndCoh}_{\mathrm{Nilp}}$ 为奇异支撑落在全局幂零锥内的 ind-凝聚层；$\operatorname{Shv}_{\mathrm{Nilp}}$ 为幂零奇异支撑部分的层范畴；上标 $\mathrm{temp}$ 表示温和部分（见「温和范畴」卡）。

## 要点

- 定理同时陈述 de Rham 与受限两条函子的保守性，目标范畴分别是 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 与 $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{restr}}_{\check G})$。
- 在 de Rham 实现中，对应的可构造范畴是特征簇包含于全局幂零锥的正则完整 $D$ 模的 ind-完备化。
- 它并非整个 $\operatorname{DMod}(\operatorname{Bun}_G)$，而是正则完整且具有幂零支撑的部分。
- 「保守」按讲义定义：若系数为零，则对象本身为零。
- 论证收尾用「温和与反温和之交为零」：$\operatorname{SS}(\mathcal F)\subset\mathrm{Nilp}_{\mathrm{irreg}}$ 给出 $\mathcal F$ 反温和，与温和性合起来迫使 $\mathcal F=0$。

## 关键公式

- $\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\xrightarrow{\operatorname{Coeff}^{\mathrm{ren}}}\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$
- $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)^{\mathrm{temp}}\xrightarrow{\operatorname{Coeff}^{\mathrm{ren}}_{\mathrm{restr}}}\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{restr}}_{\check G})$

## 定理与证明

### Whittaker 系数的保守性（要点（有缺口））

限制到温和部分后，$\operatorname{Coeff}^{\mathrm{ren}}:\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\to\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 与 $\operatorname{Coeff}^{\mathrm{ren}}_{\mathrm{restr}}:\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)^{\mathrm{temp}}\to\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{restr}}_{\check G})$ 都保守：若系数为零，则对象本身为零。

1. 用受限／幂零形式的范畴 Langlands 所提供的比较方块，把 de Rham 情形归约到 $\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)$ 内的同一机制。  
   *为什么*：比较方块的竖直箭头是所选形式体系中可用的比较或投影函子（讲义明言不是同一公共范畴中的字面包含）。
2. 设 $\mathcal F\in\operatorname{Shv}_{\mathrm{Nilp}}(\operatorname{Bun}_G)^{\mathrm{temp}}$ 且 $\operatorname{Coeff}^{\mathrm{ren}}_{\mathrm{restr}}(\mathcal F)=0$；Hecke 相容性于是蕴涵每个 $D$-系数都消失。  
   *为什么*：$\operatorname{Coeff}^{\mathrm{ren}}$ 与 Hecke／谱作用相容（§13.6）。
3. 由 Hecke 移动定理得 $\operatorname{SS}(\mathcal F)\subset\mathrm{Nilp}_{\mathrm{irreg}}$。  
   *为什么*：否则存在 $D$ 使 $\mathrm{Nilp}_{\mathrm{Kos}}$ 成为 $\operatorname{SS}(V^D\star\mathcal F)$ 的分支，与 $D$-系数全为零矛盾。
4. 于是 $\mathcal F$ 是反温和的；温和子范畴与反温和子范畴的交为零，故 $\mathcal F=0$。  
   *为什么*：反温和的刻画来自 §13.4 的微局部定理。
5. 同一论证经比较方块给出 de Rham 情形的陈述。  
   *为什么*：两种形式由同一比较方块联系。

> 缺口：论证在 §13.6 末尾以 proof 环境给出，但比较方块在 §13.4 只作「示意」列出，微局部指标定理与 Hecke 移动定理均引自 [FR25]（讲义未证），故记 sketch；相关定理的证明见 [FR25]。

*出处*：§13 章首定理（讲义未编号）/ 原书 p.64（证明见 §13.6 末，p.67）


## 易错点

- 保守性只对温和部分断言；讲义明说 de Rham 侧的范畴不是整个 $\operatorname{DMod}(\operatorname{Bun}_G)$，所以不能把它推广到全范畴。
- de Rham 侧谱叠是 $\operatorname{LocSys}_{\check G}$，Betti／可构造侧是 $\operatorname{LocSys}^{\mathrm{restr}}_{\check G}$，两条函子的目标不同。
- 此处的「保守」是范畴论意义（函子在对象层面不丢信息），不是「系数非零」这种逐点判据。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），第 13 章 章首；§13.6 其他 Whittaker 系数与 Hecke 平移，p.64-67（PDF p.64-67），`源码/chapters/ch13.tex:12-19（章首定理）、134-139（§13.6 末尾的证明）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FR25：https://arxiv.org/abs/2207.02955 — coeff^enh: D(Bun_G)^temp→QCoh(LocSys_Ǧ) 保守——卡第一条箭头逐字对应
- FR25：https://arxiv.org/abs/2207.02955 — 「coeff^enh: Shv_Nilp(Bun_G)^temp→QCoh(LocSys^restr) is conservative」——卡第二条箭头逐字对应
- FR25：https://arxiv.org/abs/2207.02955 — Shv_Nilp(Bun_G)^{anti-temp}=Shv_{Nilp_irreg}(Bun_G)，且 Nilp_irreg 上对象皆反温和——支持卡中「反温和」一环
- FR25：https://arxiv.org/abs/2207.02955 — 设 coeff^enh(F)=0，经 §10.2.5 与 §10.1 的非消失判据归约，最终得 F 反温和——与卡 proof 的论证链一致

## 关联

- `glc/concept/renormalized-whittaker-coefficient`
- `glc/concept/global-nilpotent-cone`
- `glc/concept/hecke-moving-theorem`
- `glc/concept/microlocal-index-theorem`
