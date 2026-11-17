---
id: glc/concept/averaging-vanishing-theorem
type: concept
track: F
---

# 平均消失定理

> $E$ 不可约且秩 $r>m$ 时，修改次数一旦超过 $rm(2g-2)$，平均函子整体为零。

**问题**：消失定理的门槛为什么恰好是 $rm(2g-2)$，这个数从哪里来？

## 定义

设定同 §9.1：$X$ 是亏格 $g$ 的光滑射影曲线，$D(-)$ 是所选层理论，$E$ 是秩 $r$ 的不可约局部系统，$m<r$，$\operatorname{Av}_E^d$ 是由 Laumon 层 $\mathcal{L}_E^d$ 作上修改的平均函子。定理断言：在这一设定下，只要修改次数 $d$ 超过 $rm(2g-2)$，$\operatorname{Av}_E^d$ 就是零函子。

*记号*：$r=\operatorname{rank}(E)$，$m$ 是被修改丛的秩，$g$ 是曲线亏格；$rm(2g-2)$ 等于 $\dim H^1(X,E'\otimes E)$（$E'$ 为任意秩 $m$ 局部系统），这是定理的定量来源（引理 9.4.1）。

## 要点

- 假设：$E$ 不可约、$\operatorname{rank}(E)=r>m$，并为简便假设 $g>1$。
- 结论：只要 $d>rm(2g-2)$，就有 $\operatorname{Av}_E^d=0$。
- 采用移位与扭曲的标准归一化，同样的表述适用于通常的层论情形。
- 它就是此前以 $r=n$、$m=k<n$ 使用的定理（见第 6 章的洁净延拓与 §8.6 的尖点性论证）。
- 讲义强调重点不是 $\mathcal{L}_E^d$ 的构造，而是从几何 Langlands 的谱一侧理解该函子为何应当消失。

## 关键公式

- $d>rm(2g-2)\quad\Longrightarrow\quad\operatorname{Av}_E^d=0$

## 定理与证明

### 消失定理（定理 9.1.1）（要点（有缺口））

假设 $E$ 不可约、$\operatorname{rank}(E)=r>m$，并为简便假设 $g>1$。则只要 $d>rm(2g-2)$，就有 $\operatorname{Av}_E^d=0$。采用移位与扭曲的标准归一化，同样的表述适用于通常的层论情形。

1. 取 $G=\operatorname{GL}_m$，把 $\operatorname{Av}_E^d$ 写成 Ran Hecke 作用在平均核 $\mathcal{A}_{E,d}=(\operatorname{Sym}^d(\mathrm{St}_m\otimes E))_{X^{(d)}}$ 上的像（§9.4）。  
   *为什么*：这样消失问题就搬到谱侧：由定理 9.3.2，该作用经 $\operatorname{QCoh}(\operatorname{LocSys}_{\operatorname{GL}_m})$ 分解。
2. 谱侧该拟凝聚层在秩 $m$ 局部系统 $E'$ 处的纤维是 $\mathrm{R}\Gamma(X^{(d)},(E'\otimes E)^{(d)})$。  
   *为什么*：于是函子消失归结为一个初等上同调消失。
3. 用引理 9.4.1：$d>rm(2g-2)$ 时该上同调为零，故 $\operatorname{Av}_E^d$ 作用为零。  
   *为什么*：引理 9.4.1 的证明是曲线上的 Euler 示性数加 Künneth，与 $E$ 的具体选取无关。

> 缺口：定理 9.1.1 在 §9.1 只给陈述；de Rham 情形的证明在 §9.3–§9.4（定理 9.3.2 加引理 9.4.1），讲义把它作为“从谱一侧理解”的要点而非在此证明。其他层论与一般约化群的情形 §9.5 只作为猜想性输入。

*出处*：定理 9.1.1 / 原书 p.48


## 易错点

- 门槛是秩的乘积 $rm(2g-2)$，不是 $r+m$：它等于 $\dim H^1(X,E'\otimes E)$，来自曲线上的 Euler 示性数。
- 定理断言的是函子整体为零（对所有对象、所有 $d_1,d_2$ 分支求和后），不是“对每个对象在足够大的 $d$ 上为零”的弱陈述。
- 假设里的 $g>1$ 在原文中标明“为简便”，引用时不要把它写成定理本质需要的条件。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§9.1 平均函子，p.48（PDF p.48），`定理 9.1.1（ch09.tex:12-16，p.48）`

## 核验

状态：`external-confirmed`（2026-11-18）
- Gaitsgory, On a vanishing conjecture appearing in the geometric Langlands correspondence, Annals 160(2) 617-682：https://arxiv.org/abs/math/0204081 — 「Assume that E is irreducible, of rank > n. Then for d, which is greater than (2g−2)·n·rk(E), the functor Av^d_E is identically equal to zero.」——与卡中定理 9.1.1 的假设（E 不可约、rank r>m）、门槛 d>rm(2g−2)（n=m）及结论 Av_E^d=0 完全一致；论文正文证明之。
- Gaitsgory, Recent progress in geometric Langlands theory (Seminaire Bourbaki, talk of 2016-02-16)：https://arxiv.org/abs/1606.09462 — 「Suppose that E is irreducible and rk(E) > n and d > (2g−2)·n·rk(E). Then Av_{E,d} = 0.」——同一门槛、同一结论的独立重述。
- Gaitsgory, On a vanishing conjecture appearing in the geometric Langlands correspondence, Annals 160(2) 617-682：https://arxiv.org/abs/math/0204081 — §1.6 说明 Conjecture 1.3 蕴含 L(π,σ) 是次数 ≤ m·n·(2g−2) 的多项式——支持卡 pitfall 把门槛 rm(2g−2) 解释为 dim H^1(X,E'⊗E) 的定量来源（同一 Euler 示性数计算，见讲义引理 9.4.1）。

## 关联

- `glc/concept/upper-modification-averaging`
- `glc/concept/elementary-vanishing-lemma`
- `glc/concept/generalized-vanishing-theorem`
