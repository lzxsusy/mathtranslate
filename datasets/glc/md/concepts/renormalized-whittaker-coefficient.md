---
id: glc/concept/renormalized-whittaker-coefficient
type: concept
track: H
---

# 重整化 Whittaker 系数

> 由谱作用与 $\operatorname{coeff}$ 的对偶复合（余作用）得到、取值于 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 的 Whittaker 泛函。

**问题**：$\operatorname{Coeff}^{\mathrm{ren}}$ 怎样由标量系数与谱作用造出，为什么不能拿 $\Gamma$ 的恢复性质当定义？

## 定义

谱作用给出 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})\otimes\operatorname{DMod}(\operatorname{Bun}_G)\to\operatorname{DMod}(\operatorname{Bun}_G)$。通过对偶，一个标量值泛函 $c:\operatorname{DMod}(\operatorname{Bun}_G)\to\operatorname{Vect}$ 产生一个谱值泛函，即复合 $\operatorname{DMod}(\operatorname{Bun}_G)\xrightarrow{\operatorname{coact}}\operatorname{QCoh}(\operatorname{LocSys}_{\check G})\otimes\operatorname{DMod}(\operatorname{Bun}_G)\xrightarrow{\operatorname{Id}\otimes c}\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$。取 $c=\operatorname{coeff}$，便得到 $\operatorname{Coeff}^{\mathrm{ren}}$。它的余单位（取全局截面得到的标量形式）恢复原来的标量系数：$\Gamma(\operatorname{LocSys}_{\check G},\operatorname{Coeff}^{\mathrm{ren}}(\mathcal F))\simeq\operatorname{coeff}(\mathcal F)$。

*记号*：$\operatorname{LocSys}_{\check G}$ 为 $\check G$-局部系统的叠；$\operatorname{coact}$ 为谱作用对应的余作用；$\Gamma$ 为全局截面；上标 $\mathrm{ren}$ 表示重整化。

## 要点

- 定义就是上面的余作用公式，而不是 $\Gamma$ 的恢复性质。
- 单凭恢复性质不能刻画取值于 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 的对象，因为 $\operatorname{LocSys}_{\check G}$ 一般不是仿射的。
- 在谱范畴满足通常的刚性假设时，给出到 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 的 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$-线性函子，等价于给出取值于 $\operatorname{Vect}$ 的底层标量函子——这是标量 Whittaker 泛函能够定义谱值泛函的形式原因。
- $\operatorname{Coeff}^{\mathrm{ren}}$ 经由温和部分分解：$\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 在 $\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}$ 上的作用在所有 Satake／Hecke 算子下稳定（第二个基本事实）。
- 同样的说明适用于受限 Betti／可构造情形，那里得到 $\operatorname{Coeff}^{\mathrm{ren}}_{\mathrm{restr}}$。

## 关键公式

- $\operatorname{DMod}(\operatorname{Bun}_G)\xrightarrow{\operatorname{coact}}\operatorname{QCoh}(\operatorname{LocSys}_{\check G})\otimes\operatorname{DMod}(\operatorname{Bun}_G)\xrightarrow{\operatorname{Id}\otimes c}\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$
- $\Gamma(\operatorname{LocSys}_{\check G},\operatorname{Coeff}^{\mathrm{ren}}(\mathcal F))\simeq\operatorname{coeff}(\mathcal F)$
- $\operatorname{Coeff}^{\mathrm{ren}}:\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\longrightarrow\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$

## 定理与证明

### 重整化系数经由温和部分分解（要点（有缺口））

$\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 在 $\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}$ 上的作用在所有 Satake／Hecke 算子下稳定，因此 $\operatorname{Coeff}^{\mathrm{ren}}$ 也经由温和部分分解。

1. 讲义把它作为证明保守性所用的第二个基本事实列出，未给论证。  
   *为什么*：稳定性涉及 Satake／Hecke 算子的整套理论，本章只引用其结论。

> 缺口：讲义只述不证：§13.1 说「这就是证明所用的两个基本事实」的第二条，直接给出该分解。

*出处*：§13.1（讲义未编号的正文陈述）/ 原书 p.65


## 易错点

- 「$\Gamma$ 恢复标量系数」只是余单位影子，不是 $\operatorname{Coeff}^{\mathrm{ren}}$ 的定义；把恢复性质当定义会漏掉 $\operatorname{LocSys}_{\check G}$ 非仿射所带来的信息。
- $\operatorname{Coeff}^{\mathrm{ren}}$ 与 $\operatorname{Coeff}^{\mathrm{ren}}_{\mathrm{restr}}$ 的目标范畴分别是 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 与 $\operatorname{QCoh}(\operatorname{LocSys}^{\mathrm{restr}}_{\check G})$，不能互换。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§13.1 普通系数函子与重整化系数函子，p.64（PDF p.64），`源码/chapters/ch13.tex:28-39（谱作用、余作用与注）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FR25：https://arxiv.org/abs/2207.02955 — 先有 QCoh(LocSys^restr)⊗Shv_Nilp→Shv_Nilp 的作用函子，对第一个张量因子取对偶得余作用，再复合 id⊗coeff，得 coeff^enh，满足 Γ^!∘coeff^enh=coeff 且经 temp 分解——逐条对应卡的余作用定义与 Γ 恢复公式
- FR25：https://arxiv.org/abs/2207.02955 — 「a canonical spectral action of QCoh(LocSys^restr) on Shv_Nilp(Bun_G) that is suitably compatible with Hecke functors」——支持卡定理「QCoh 作用对 Satake/Hecke 稳定，故 Coeff^ren 经温和部分分解」
- FR25：https://arxiv.org/abs/2207.02955 — coeff^enh: D(Bun_G)^temp→QCoh(LocSys_Ǧ) conservative——给出卡定理在 de Rham 侧的整体形式

## 关联

- `glc/concept/whittaker-coefficient`
- `glc/concept/whittaker-conservativity`
- `glc/concept/tempered-category`
