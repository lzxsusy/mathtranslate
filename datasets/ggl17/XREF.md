# 第 17 篇 · 外部核对底稿（xref）

- arXiv: `1111.0691`　抓取时间：2026-11-22T21:00:28
- 本文件是**机器抓的数据**，不是结论。下面每一栏都要人去核，并把核过的写进
  `notes.md` 的「## 核对与勘误」节；判为原文笔误的写进 `errata.tsv`。

## 1. arXiv 版本史（有 v2/v3 就要逐条核修版差异）

- 版本数：**3**　初版 2011-11-02　最后更新 2013-08-29
- 版本：v1 Wed, 2 Nov 2011；v2 Thu, 22 Aug 2013；v3 Thu, 29 Aug 2013
  > 本篇有多个版本。**先 diff 各版正文**再判定笔误——作者修版常常正是替我们改掉了一处错。
- 标题：Quasi-Topological Gauged Sigma Models, The Geometric Langlands Program, And Knots
- 作者：Meng-Chwan Tan
- 分类：hep-th
- comment：164 pages. Minor cosmetic changes. To appear in ATMP
- journal-ref：Adv.Theor.Math.Phys.19: 277-450, 2015（期刊版可能已修正笔误，值得对照）

**摘要原文**（正文与摘要的数值/符号若冲突，必有一处错）：

> We construct and study a closed, two-dimensional, quasi-topological (0,2) gauged sigma model with target space a smooth G-manifold, where G is any compact and connected Lie group. When the target space is a flag manifold of simple G, and the gauge group is a Cartan subgroup thereof, the perturbative model describes, purely physically, the recently formulated mathematical theory of "Twisted Chiral Differential Operators". This paves the way, via a generalized T-duality, for a natural physical interpretation of the geometric Langlands correspondence for simply-connected, simple, complex Lie groups. In particular, the Hecke eigensheaves and Hecke operators can be described in terms of the correlation functions of certain operators that underlie the infinite-dimensional chiral algebra of the flag manifold model. Nevertheless, nonperturbative worldsheet twisted-instantons can, in some situations, trivialize the chiral algebra completely. This leads to a spontaneous breaking of supersymmetry whilst implying certain delicate conditions for the existence of Beilinson-Drinfeld D-modules. Via supersymmetric gauged quantum mechanics on loop space, these conditions can be understood to be intimately related to a conjecture by Hohn-Stolz [1] regarding the vanishing of the Witten genus on string manifolds with positive Ricci curvature. An interesting connection to Chern-Simons theory is also uncovered, whence we would be able to (i) relate general knot invariants of three-manifolds and Khovanov homology to "quantum" ramified D-modules and Lagrangian intersection Floer homology; (ii) furnish physical proofs of mathematical conjectures by Seidel-Smith [2] and Gaitsgory [3, 4] which relate knots to symplectic geometry and Langlands duality, respectively.

## 2. 引文概况

- INSPIRE recid 944465　被引 **4** 次　参考文献 0 条

最近的被引（挑与本文最相关的 2–3 篇复述去看）：

- Higher AGT correspondences, $\mathcal{W}$-algebras, and higher quantum geometric Langlands duality from M-theory　`1607.08330`
- Static Charges in the Low-Energy Theory of the S-Duality Twist　`1201.2679`
- On the Six-Dimensional Origin of the AGT Correspondence　`1112.0260`
- Eight dimensional physics and the Langlands program - A short note　`1111.5113`

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

