# 多重度 1 定理与尖点谱分解

> `gaits04/concept/multiplicity-one` · 轨 B 尖点与 Langlands 对应 · 状态 reviewed · 核验 source-only

**问题：** 为什么这里是「直和」而不是「直积分」？

**一句话：** 尖点自守表示在 $\operatorname{Funct}_{cusp}$ 中重数至多为 1，且整个尖点空间分解为不可约尖点表示的直和（而非直积分）。

**别名：** `multiplicity one theorem`、`direct sum decomposition`

## 定义

回忆：$\mathrm{GL}_n(\mathbb A)$ 的不可约表示 $\pi$ 称为尖点自守表示，若 $\operatorname{Hom}_{\mathrm{GL}_n(\mathbb A)}(\pi,\operatorname{Funct}_{cusp}(\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A)))\ne0$。一个重要结果（多重度 1 定理）说：上述 $\operatorname{Hom}$ 至多一维。此外，整个空间 $\operatorname{Funct}_{cusp}(\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A))$ 分解为不可约（从而尖点自守）表示的直和，而不是直积分。

**记号：** $\operatorname{Hom}_{\mathrm{GL}_n(\mathbb A)}(\pi,-)$： intertwining 算子空间；重数 = 该空间的维数。

## 要点

- 重数 1 与直和分解是两条独立结论：前者说每个不可约出现的次数，后者说没有连续谱。
- 直和（离散谱）而非直积分，是尖点空间相对 $L^2$ 空间的关键差别：尖点形式全都是「离散」的。
- 两者合起来，$\operatorname{Funct}_{cusp}$ 就是若干不可约表示的（代数）直和，每个出现一次。

## 公式

$$
\operatorname{Hom}_{\mathrm{GL}_n(\mathbb A)}(\pi,\operatorname{Funct}_{cusp})\le 1
$$

## 易错点

- 把「多重度 1」误当成「每个不可约表示只出现一次于整个 $\operatorname{Funct}$」：它只对尖点子空间成立，非尖点部分可以有连续谱与重数。

## 批注

**〔易错预警〕直和 vs 直积分**　原书特意写「直和（而不是直积分）」。若写成直积分，就丢掉了「每个尖点表示出现且仅出现一次」这一信息，后文 §3 里把函数换成层的直觉（一个不可约对应一个对象）也随之失效。

## 相关

[[cuspidal]]、[[langlands-lafforgue]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§1.8，原书 pp. 272（PDF pp. 274）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec1.tex:112-136（§1.8）`
