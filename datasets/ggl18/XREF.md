# 第 18 篇 · 外部核对底稿（xref）

- arXiv: `0710.5796`　抓取时间：2026-11-23T21:00:49
- 本文件是**机器抓的数据**，不是结论。下面每一栏都要人去核，并把核过的写进
  `notes.md` 的「## 核对与勘误」节；判为原文笔误的写进 `errata.tsv`。

## 1. arXiv 版本史（有 v2/v3 就要逐条核修版差异）

- 版本数：**5**　初版 2007-10-31　最后更新 2008-03-12
- 版本：v1 Wed, 31 Oct 2007；v2 Tue, 6 Nov 2007；v3 Tue, 6 Nov 2007；v4 Mon, 19 Nov 2007；v5 Wed, 12 Mar 2008
  > 本篇有多个版本。**先 diff 各版正文**再判定笔误——作者修版常常正是替我们改掉了一处错。
- 标题：Gauging Spacetime Symmetries on the Worldsheet and the Geometric Langlands Program
- 作者：Meng-Chwan Tan
- 分类：hep-th
- comment：80 pages + appendix. Minor changes, further clarifications and improvements. Published version
- journal-ref：JHEP 0803:033,2008（期刊版可能已修正笔误，值得对照）

**摘要原文**（正文与摘要的数值/符号若冲突，必有一处错）：

> We study the two-dimensional twisted (0,2) sigma-model on various smooth complex flag manifolds G/B, and explore its relevance to the geometric Langlands program. We find that an equivalence - at the level of the holomorphic chiral algebra - between a bosonic string on G/B and a B-gauged version of itself on G, will imply an isomorphism of classical W-algebras and a level relation which underlie a geometric Langlands correspondence for G=SL(N,C). This furnishes an alternative physical interpretation of the geometric Langlands correspondence for G=SL(N,C), to that demonstrated earlier by Kapustin and Witten via an electric-magnetic duality of four-dimensional gauge theory. Likewise, the Hecke operators and Hecke eigensheaves will have an alternative physical interpretation in terms of the correlation functions of local operators in the holomorphic chiral algebra of a quasi-topological sigma-model without boundaries. A forthcoming paper will investigate the interpretation of a ``quantum'' geometric Langlands correspondence for G=SL(N,C) in a similar setting, albeit with fluxes of the sigma-model moduli which induce a ``quantum'' deformation of the relevant classical algebras turned on.

## 2. 引文概况

- INSPIRE recid 766298　被引 **5** 次　参考文献 0 条

最近的被引（挑与本文最相关的 2–3 篇复述去看）：

- On the Six-Dimensional Origin of the AGT Correspondence　`1112.0260`
- SL(2,R) Chern-Simons, Liouville, and Gauge Theory on Duality Walls　`1103.5748`
- Langlands duality in Liouville-H(+)-3 WZNW correspondence　`0805.1254`
- Gauging Spacetime Symmetries On The Worldsheet And The Geometric Langlands Program. II　`0804.0804`
- Geometric Metastability, Quivers and Holography　`0708.0596`

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

