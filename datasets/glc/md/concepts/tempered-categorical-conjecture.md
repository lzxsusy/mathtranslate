---
id: glc/concept/tempered-categorical-conjecture
type: concept
track: F
---

# 温和范畴猜想

> 温和部分的预期等价：自守范畴的温和子范畴应等同于谱叠上的拟凝聚层，补上 Eisenstein 生成即完整范畴猜想。

**问题**：温和猜想为什么加上 Eisenstein 相容性就等价于完整范畴猜想？

## 定义

还有一个范围较小的预期等价：$\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$。从基本思想上说，温和部分是 $\operatorname{DMod}(\operatorname{Bun}_G)$ 中能够被 Whittaker 系数检测到的部分。整个自守范畴由温和紧对象的 Eisenstein 级数生成：$\operatorname{DMod}(\operatorname{Bun}_G)=\bigl\langle\operatorname{Eis}_P(\operatorname{DMod}(\operatorname{Bun}_M)^{\mathrm{temp},c})\mid P\subset G\bigr\rangle$。因此，温和猜想连同上述 Eisenstein 相容性，等价于完整的范畴猜想。

*记号*：$\operatorname{DMod}(\operatorname{Bun}_M)^{\mathrm{temp},c}$ 是温和紧对象；$\langle-\rangle$ 表示在 $\operatorname{DMod}(\operatorname{Bun}_G)$ 中生成的子范畴；$\operatorname{Eis}_P$ 是 §10.4 的 Eisenstein 函子。

## 要点

- 猜想：$\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$。
- 思想背景：温和部分是能被 Whittaker 系数检测到的部分。
- 整体范畴由温和紧对象的 Eisenstein 级数生成：$\operatorname{DMod}(\operatorname{Bun}_G)=\langle\operatorname{Eis}_P(\operatorname{DMod}(\operatorname{Bun}_M)^{\mathrm{temp},c})\mid P\subset G\rangle$。
- 因此温和猜想连同 §10.4 的 Eisenstein 相容性等价于完整范畴猜想。
- 它与第 9 章 §9.8 的 $\widetilde D(\operatorname{Bun}_G)=\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}$ 是同一个温和部分。

## 关键公式

- $\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$
- $\operatorname{DMod}(\operatorname{Bun}_G)=\bigl\langle\operatorname{Eis}_P(\operatorname{DMod}(\operatorname{Bun}_M)^{\mathrm{temp},c})\mid P\subset G\bigr\rangle$

## 定理与证明

### 温和猜想（§10.5，未编号 conjecture）（要点（有缺口））

$\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$。

1. 在温和部分比较两侧：左端是 $\operatorname{DMod}(\operatorname{Bun}_G)$ 的温和子范畴，右端是谱叠上的拟凝聚层。  
   *为什么*：这是完整范畴猜想在“温和”这一半上的截断，范围更小、更容易检验。
2. 补上 Eisenstein 生成 $\operatorname{DMod}(\operatorname{Bun}_G)=\langle\operatorname{Eis}_P(\operatorname{DMod}(\operatorname{Bun}_M)^{\mathrm{temp},c})\mid P\subset G\rangle$。  
   *为什么*：Eisenstein 把各 Levi 的温和部分拼成整个自守范畴，于是两部分合起来就是完整猜想。

> 缺口：这是猜想，讲义未给证明；它只是完整范畴猜想中“温和”的那一半，另一半由 Eisenstein 相容性提供。

*出处*：§10.5 / 原书 p.55-56


## 易错点

- “等价于完整范畴猜想”是有条件的：必须连同 §10.4 的 Eisenstein 相容性一起；单靠温和猜想本身不够。
- 生成性用的是温和**紧**对象（$\operatorname{temp},c$），漏掉“紧”字会把生成范畴写大。
- 别把它与 §10.6 的 Betti 版本混同：这里左右两端都是 de Rham 的 $\operatorname{DMod}$ 与 $\operatorname{LocSys}_{\check G}$。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§10.5 温和对象与 Whittaker 检测，p.55-56（PDF p.55-56），`§10.5 温和猜想与 Eisenstein 生成（ch10.tex:109-131，p.55-56）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv：https://arxiv.org/abs/2108.02719 — 摘要支持 DMod(Bun_G)^temp≃QCoh(LocSys_Ĝ) 及子范畴与辅助点无关。
- arXiv：https://arxiv.org/abs/2405.03599 — 摘要称猜想各形式（de Rham/Betti、restricted/non-restricted、tempered/non-tempered）等价；支持本卡「温和猜想+Eisenstein 相容性⟺完整猜想」。摘要未给 DMod(Bun_G)=⟨Eis_P(DMod(Bun_M)^{temp,c})⟩ 的生成公式。

## 关联

- `glc/concept/tempered-object`
- `glc/concept/categorical-langlands-conjecture`
- `glc/concept/eisenstein-functor`
