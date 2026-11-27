# 第 15 篇 · 外部核对底稿（xref）

- arXiv: `0710.2097`　抓取时间：2026-11-27T21:00:48
- 本文件是**机器抓的数据**，不是结论。下面每一栏都要人去核，并把核过的写进
  `notes.md` 的「## 核对与勘误」节；判为原文笔误的写进 `errata.tsv`。

## 1. arXiv 版本史（有 v2/v3 就要逐条核修版差异）

- 版本数：**1**　初版 2007-10-10　最后更新 2007-10-10
- 版本：v1 Wed, 10 Oct 2007
- 标题：The algebra of Wilson-'t Hooft operators
- 作者：Anton Kapustin, Natalia Saulina
- 分类：hep-th
- comment：55 pages, latex
- journal-ref：Nucl.Phys.B814:327-365,2009（期刊版可能已修正笔误，值得对照）

**摘要原文**（正文与摘要的数值/符号若冲突，必有一处错）：

> We study the Operator Product Expansion of Wilson-'t Hooft operators in a twisted N=4 super-Yang-Mills theory with gauge group G. The Montonen-Olive duality puts strong constraints on the OPE and in the case G=SU(2) completely determines it. From the mathematical point of view, the Montonen-Olive duality predicts the L^2 Dolbeault cohomology of certain equivariant vector bundles on Schubert cells in the affine Grassmannian. We verify some of these predictions. We also make some general observations about higher categories and defects in Topological Field Theories.

## 2. 引文概况

- INSPIRE recid 763840　被引 **52** 次　参考文献 0 条

最近的被引（挑与本文最相关的 2–3 篇复述去看）：

- Lie Algebra Cohomology and Seiberg-Witten Theory　`2611.29713`
- $K_{\mathfrak{q}}$-algebras　`2609.38702`
- Spherical DAHA as an algebra of framed BPS states　`2609.07911`
- Schur connections: Chord counting, line operators, and indices　`2506.17384`
- D-branes and the planar limit of Chern-Simons theory. Link invariants　`2506.03246`
- Renormalization Group Flow in Schur quantization　`2503.16685`
- Integrability, Defects, and Flows in 2 and 4 Dimensional Quantum Field Theories　`—`
- Branes and Representations of DAHA $C^\vee C_1$: affine braid group action on category　`2412.19647`

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
| 1 | 主定理的陈述与符号 | 摘要 + 被引论文的复述 + 库内互引篇 | 与摘要、gtgl15/concept/hitchin-equations、kw06/concept/thooft-operator、gw06/concept/wilson-t-hooft 三处一致；唯一差异是 Hitchin 方程差一个 i（符号约定，不记勘误） |
| 2 | 关键公式的系数/符号/指数 | 至少另 2 处独立出处（库内卡、nLab、另一篇 arXiv） | (40)(43)(44)(53)–(55) 逐项复算一致；§6.5 的 3+1=2×2=4 自洽；F₂ 的 Kähler 商权与 Hodge 数一致 |
| 3 | 命题编号与交叉引用 | 正文内引用处是否指向正确条目 | p053 把乘积恒等式称作 eq. (42)，实际应为 eq. (43)（p037）→ errata.tsv E1，置信度 low |
| 4 | 数值/维数一致性 | 两边算一遍（如 dim、rank、指数） | TP¹ 的 3、EH 的 1、Euler 特征 4=4、C_μ≅P¹ 的维数均复算一致 |
| 5 | 记号与前后定义 | 同一符号在 §1 与 §5 是否同义 | bΛ(G)=Λ_cw×Λ_w（p9）与 Λ_w⊕Λ_cw（p2）同义；t=v/u（本篇）与 ggl20 卡的 t=u/v 是约定差 |

可用外部检索：arXiv abs 页、nLab（`ncatlab.org/nlab/show/…`）、
作者后续论文、库内 46 篇、`datasets/*` 既有卡片。每条结论都要写下**出处定位**
（页/式号/§）。

