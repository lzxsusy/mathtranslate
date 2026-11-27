---
id: page/geometric-langlands
kind: topic
title: 几何 Langlands 对应：从 Drinfeld 到 FGV
aliases: [几何 Langlands, geometric Langlands, Drinfeld–Langlands 对应]
status: draft
version: 0.1
updated: 2026-11-27
covers: [geometry/geometric-langlands, geometry/bun-n, geometry/local-system, geometry/hecke-eigensheaf, geometry/hecke-correspondence, geometry/geometric-class-field-theory, geometry/picard-variety, geometry/perverse-sheaf, geometry/verdier-duality, geometry/affine-grassmannian, algebra/langlands-correspondence]
compiled_from:
  - id: sy0246/concept/drinfeld-langlands-correspondence
    hash: pending
  - id: sy0246/concept/main-theorem-fgv
    hash: pending
  - id: sy0246/concept/gl1-aut-e
    hash: pending
  - id: sy0246/concept/hecke-operator
    hash: pending
  - id: sy0246/concept/vanishing-theorem
    hash: pending
readers: 研究生（懂层与叠的语言，未系统学过几何 Langlands）
rights: rewritten
---

# 几何 Langlands 对应：从 Drinfeld 到 FGV

> **本页是 v0.1 骨架**：第 0–1 节已按底本写好并挂链，第 2–7 节只给结构，待 A1–A6 按 `04_playbook/27` 的阅读包补写。
> 页面规矩：**不手打定理、只转引**；每个数学断言必须挂词条链接或引文块，否则不合稿。

## 0. 一句话与两条边

几何 Langlands 是数论中 Langlands 对应的几何化：曲线 $X$ 上秩 $n$ 的局部系统，对应 $\operatorname{Bun}_n(X)$ 上的 Hecke 特征反常层。两边分别是**谱侧**（局部系统，即曲线的“Galois 表示”）与**自守侧**（向量丛模空间上的层）。

Laumon 在 Bourbaki 报告开篇的定位（原文 p1，译文 p2）：

> La correspondance de Drinfeld-Langlands, dite aussi de Langlands géométrique, est un analogue conjectural … pour un groupe réductif déployé G sur une extension finie F de k(t), où k est un corps arbitraire.
>
> 译文：Drinfeld–Langlands 对应，又称几何 Langlands 对应，是 Langlands 对应在以下情形的猜想类比：$k(t)$ 的有限扩张 $F$ 上的分裂约化群 $G$，其中 $k$ 是任意域。

本页只讲**处处非分歧、$X$ 射影、$G=\GL_n$** 的情形——这正是 [Frenkel–Gaitsgory–Vilonen](https://arxiv.org/abs/math/0012255) 解决的情形。

## 1. 对应的陈述

### 1.1 谱侧

$X$ 为 $\C$ 上光滑射影连通曲线（Betti 设定）或 $\F_q$ 上光滑完备曲线（$\ell$-进设定）。谱侧的对象是 $X$ 上秩 $n$ 的**不可约局部系统** $E$，见 {{entry:geometry/local-system}}。

> 两套设定不可混：Betti 设定取 $k=\C$、系数域特征 $0$；$\ell$-进设定取 $k$ 任意、系数域 $\overline{\Q}_\ell$。见 {{entry:geometry/geometric-langlands}} 与 Laumon 906 §0（原文 p2–3）。

### 1.2 自守侧

自守侧是**向量丛的模叠** $\Bun_n(X)$：$X$ 上秩 $n$ 向量丛构成的代数叠，光滑、纯维数 $n^2(g-1)$，按次数分成连通分支 $\Bun_n^d(X)$，见 {{entry:geometry/bun-n}}。它上面有 Hecke 对应给出的算子，见 {{entry:geometry/hecke-correspondence}}。

### 1.3 对应本身

对每个不可约秩 $n$ 局部系统 $E$，应当存在 $\Bun_n(X)$ 上的反常层 $\Aut_E$，它在每个连通分支上不可约，并且是 $E$ 的**Hecke 特征层**。后者的定义（Laumon 906 定义 2.1，原文 p7）：

> Soit $E$ un système local irréductible de rang $n$ sur $X$. … $K$ … a la propriété de Hecke relativement à $E$ s'il existe un isomorphisme $H(K)\simeq E\boxtimes K$ …

严格定义与两套约定（$K$ 是否必须不可约）见 {{entry:geometry/hecke-eigensheaf}}；本页采用 Laumon 的约定：**要求 $K$ 不可约**。FGV 原文只要求 $K\neq 0$，这一差别见 §3。

## 2. 自守侧：Hecke 算子

> TODO（A3）：Hecke 叠、两个投影、$H(K)=(q,p')_*p^*K[n-1]$、$H\circ H$ 的 $S_2$-等变。
> 证据：Laumon 906 §2（原文 p6–8，译文 p6–7）；{{entry:geometry/hecke-correspondence}}、{{entry:algebra/hecke-operator}}。

## 3. 谱侧：Hecke 特征层与两套约定

> TODO（A3）：特征方程；Laumon 要求 $K$ 不可约，FGV 只要求 $K\neq0$；不可约性在定理 2.2 中的作用。
> 证据：Laumon 906 定义 2.1（p7）、FGV `math/0012255` §1.1 式 (1.3)（原文 p4）。

## 4. $\GL_1$：几何类域论

$n=1$ 时对应不是猜想而是定理，它就是几何类域论。核心是 Abel–Jacobi 映射 $\phi:X\to\Pic^0(X)$ 与下面的定理（Laumon 906 定理 1.2，原文 p5）：

> Pour tout système local $E$ de rang 1 sur $X$, il existe un unique système local (rigidifié à l'origine) $\Aut_E$ de rang 1 sur $\Pic^0(X)$ tel que $\phi^*\Aut_E=E$.

即：秩 $1$ 局部系统都能沿 Abel–Jacobi 下降。见 {{entry:geometry/geometric-class-field-theory}}、{{entry:geometry/picard-variety}}；Abel–Jacobi 词条 `geometry/abel-jacobi` 待建（P0 补）。

## 5. 主定理（$\GL_n$）

> TODO（A1+A3）：定理 2.2 的陈述与“每个连通分支上不可约”；$n=2$（Drinfeld）与任意 $n$（FGV）；定理 2.2 与 FGV 主猜想的关系（Laumon 把它陈述为定理，FGV 原文把一般情形列为猜想，两者的差别在“已证范围”）。
> 证据：Laumon 906 定理 2.2（原文 p8，逐字引文见 `资料卡/01-结果清单.md`）；FGV Conjecture 1.3（p4）。

## 6. 证明路线

> TODO（A5）：三条线——
> ① Whittaker → Laumon 层 → 齐次 Fourier 变换 → 洁净性 → 沿 $\Bun'_n\to\Bun_n$ 下降（FGV / Laumon 906 §3–§7）；
> ② Scholze 1252 的现代叙述（`SY02-45`，中译 45 页）；
> ③ 消没定理（Gaitsgory）在①的哪一步用、条件 $d>in(2g-2)$ 的含义。
> 证据：`SY02-46` §6–§7；{{entry:geometry/perverse-sheaf}}、{{entry:geometry/affine-grassmannian}}。

## 7. 现状与开放问题

> TODO（A6）：$\GL_n$ 已证（Drinfeld $n=2$、FGV 任意 $n$）；一般约化群仍是猜想；$p$ 进与局部情形；形式化现状只有语句骨架（`datasets/leanstmt` 的 `laumon906-g01`，`sorry=1`）。
>
> **物理侧不在本页**：Kapustin–Witten 与超对称场论由《超对称场论》卷负责（另一队）；本页只留一句接口，不写任何物理内容。

## 8. 怎么读这页

- 想先看**历史线索**：从 §0 → §1 → §5 读，三节不超过 3,000 字。
- 想先看**技术核心**：§2 → §3 → §6，配 `SY02-46` §2–§7（15 页）。
- 想看**现代版证明**：§6 的②，配 `SY02-45`（45 页）。
- 每节末的“证据”行给出页码与词条；引文块的法文都可在底本对应页逐字核对。

## 引用与出处

- G. Laumon, *Travaux de Frenkel, Gaitsgory et Vilonen sur la correspondance de Drinfeld–Langlands*, Séminaire Bourbaki 906 (2002), 19 p. — 中译注本：`08_source_code/SY02-46_…/成品/`；arXiv `math/0207078`。
- E. Frenkel, D. Gaitsgory, K. Vilonen, *On the geometric Langlands conjecture*, arXiv `math/0012255`（54 p.）。
- D. Gaitsgory, *On a vanishing conjecture appearing in the geometric Langlands correspondence*, arXiv `math/0204081`（60 p.）。
- 词条：见 front-matter 的 `covers`。

<!-- 变更记录：v0.1 2026-11-27 建骨架，§0–§1 成文，§2–§7 待补。 -->
