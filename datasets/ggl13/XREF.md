# 第 13 篇 · 外部核对底稿（xref）

- arXiv: `1108.3103`　抓取时间：2026-11-22T10:08:39
- 本文件是**机器抓的数据**，不是结论。下面每一栏都要人去核，并把核过的写进
  `notes.md` 的「## 核对与勘误」节；判为原文笔误的写进 `errata.tsv`。

## 1. arXiv 版本史（有 v2/v3 就要逐条核修版差异）

- 版本数：**2**　初版 2011-08-15　最后更新 2012-10-02
- 版本：v1 Mon, 15 Aug 2011；v2 Tue, 2 Oct 2012
  > 本篇有多个版本。**先 diff 各版正文**再判定笔误——作者修版常常正是替我们改掉了一处错。
- 标题：Khovanov Homology And Gauge Theory
- 作者：Edward Witten
- 分类：math.GT
- comment：16 pp

**摘要原文**（正文与摘要的数值/符号若冲突，必有一处错）：

> In these notes, I will sketch a new approach to Khovanov homology of knots and links based on counting the solutions of certain elliptic partial differential equations in four and five dimensions. The equations are formulated on four and five-dimensional manifolds with boundary, with a rather subtle boundary condition that encodes the knots and links. The construction is formally analogous to Floer and Donaldson theory in three and four dimensions. It was discovered using quantum field theory arguments but can be described and understood purely in terms of classical gauge theory. (Based on a lecture at the conference Low-Dimensional Manifolds and High-Dimensional Categories, University of California at Berkeley, June 2011).

## 2. 引文概况

- INSPIRE recid 924193　被引 **50** 次　参考文献 0 条

最近的被引（挑与本文最相关的 2–3 篇复述去看）：

- Reductions in Khovanov-Rozansky operator formalism　`2605.01584`
- Quantum Invariants of 3-Manifolds and Links: A Survey　`—`
- Khovanov-Rozansky matrix factorization reduction for bipartite links　`2511.08244`
- Quantum invariants of 3-manifolds and links: a review　`2509.02939`
- Operator lift of the Reshetikhin-Turaev formalism to Khovanov-Rozansky topological quantum field theory　`2508.05191`
- Haydys-Witten Instantons and Symplectic Khovanov Homology.　`—`
- Homological knot invariants from mirror symmetry.　`2207.14104`
- Knot categorification from mirror symmetry Part II: Lagrangians　`2105.06039`

## 3. 库内可直接对照的篇目（已全译或已有卡，优先拿它们的措辞来校）

| 序 | 中文题名 | 可核什么 |
|---|---|---|
| 01 | 电磁对偶与几何朗兰兹纲领（67 张卡 `datasets/kw06`） | 扭化参数 t、S-对偶、brane 词典 |
| 02 | 规范理论、分歧与几何朗兰兹纲领（中译 SY02-06） | 分歧、wild ramification、算子 |
| 06 | 镜像对称、Hitchin 方程与朗兰兹对偶（SY05-25） | Hitchin 模空间、A/B-膜词典 |
| 11 | 量子力学路径积分的新视角（SY03-01） | 量子化、路径积分定义 |
| 16 | 几何内窥与镜像对称（SY01-07） | 内窥、Langlands 对偶群 |
| 23 | 四维规范场论中的纽结不变量（SY05-01） | 四维 N=4、边界条件 |
| 28 | Hitchin 可积系统的量子化与 Hecke 特征层（`datasets/bdh`） | D-模、量子化、特征层 |
| 36 | 朗兰兹纲领与共形场论讲义（SY03-21） | 整体图景、术语定名 |

## 4. 外部校正动作清单（本栏必须逐条回填）

| # | 核什么 | 怎么核 | 结论 |
|---|---|---|---|
| 1 | 主定理的陈述与符号 | 摘要 + 被引论文的复述 + 库内互引篇 | |
| 2 | 关键公式的系数/符号/指数 | 至少另 2 处独立出处（库内卡、nLab、另一篇 arXiv） | |
| 3 | 命题编号与交叉引用 | 正文内引用处是否指向正确条目 | |
| 4 | 数值/维数一致性 | 两边算一遍（如 dim、rank、指数） | |
| 5 | 记号与前后定义 | 同一符号在 §1 与 §5 是否同义 | |

可用外部检索：arXiv abs 页、nLab（`ncatlab.org/nlab/show/…`）、
作者后续论文、库内 46 篇、`datasets/*` 既有卡片。每条结论都要写下**出处定位**
（页/式号/§）。

