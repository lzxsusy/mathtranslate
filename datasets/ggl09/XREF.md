# 第 09 篇 · 外部核对底稿（xref）

- arXiv: `0905.4795`　抓取时间：2026-11-26T21:00:33
- 本文件是**机器抓的数据**，不是结论。下面每一栏都要人去核，并把核过的写进
  `notes.md` 的「## 核对与勘误」节；判为原文笔误的写进 `errata.tsv`。

## 1. arXiv 版本史（有 v2/v3 就要逐条核修版差异）

- 版本数：**2**　初版 2009-05-29　最后更新 2009-11-06
- 版本：v1 Fri, 29 May 2009；v2 Fri, 6 Nov 2009
  > 本篇有多个版本。**先 diff 各版正文**再判定笔误——作者修版常常正是替我们改掉了一处错。
- 标题：Geometric Langlands And The Equations Of Nahm And Bogomolny
- 作者：Edward Witten
- 分类：hep-th
- comment：37 pp

**摘要原文**（正文与摘要的数值/符号若冲突，必有一处错）：

> Geometric Langlands duality relates a representation of a simple Lie group $G^\vee$ to the cohomology of a certain moduli space associated with the dual group $G$. In this correspondence, a principal $SL_2$ subgroup of $G^\vee$ makes an unexpected appearance. Why this happens can be explained using gauge theory, as we will see in this article, with the help of the equations of Nahm and Bogomolny. (Based on a lecture at Geometry and Physics: Atiyah 80, Edinburgh, April 2009.)

## 2. 引文概况

- INSPIRE recid 821658　被引 **35** 次　参考文献 0 条

最近的被引（挑与本文最相关的 2–3 篇复述去看）：

- Potent categorical representations　`2510.07482`
- Coulomb Branches in 3d $\mathcal{N} = 4$ Revisited　`2412.17904`
- Tannakian QFT: from spark algebras to quantum groups　`2411.04194`
- Relative Langlands Duality　`2409.04677`
- A Panorama Of Physical Mathematics c. 2022　`2211.04467`
- A QFT for non-semisimple TQFT　`2112.01559`
- Supersymmetric Ground States of 3d $\mathcal{N}=4$ Gauge Theories on a Riemann Surface　`2105.08783`
- Branes, Quivers, and the Affine Grassmannian　`2102.06190`

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

