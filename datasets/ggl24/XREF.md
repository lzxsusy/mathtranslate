# 第 24 篇 · 外部核对底稿（xref）

- arXiv: `1005.2846`　抓取时间：2026-11-26T21:00:58
- 本文件是**机器抓的数据**，不是结论。下面每一栏都要人去核，并把核过的写进
  `notes.md` 的「## 核对与勘误」节；判为原文笔误的写进 `errata.tsv`。

## 1. arXiv 版本史（有 v2/v3 就要逐条核修版差异）

- 版本数：**5**　初版 2010-05-17　最后更新 2012-03-06
- 版本：v1 Mon, 17 May 2010；v2 Fri, 28 May 2010；v3 Sat, 28 May 2011；v4 Mon, 6 Jun 2011；v5 Tue, 6 Mar 2012
  > 本篇有多个版本。**先 diff 各版正文**再判定笔误——作者修版常常正是替我们改掉了一处错。
- 标题：Quantization of the Hitchin moduli spaces, Liouville theory, and the geometric Langlands correspondence I
- 作者：J. Teschner
- 分类：hep-th
- comment：81 pages; V2: small corrections and improvements, references added; V3: Discussion of Yang's potential moved to 5.5 and extended, small additons and corrections otherwise; V4: a reference added, V5: final version to appear in ATMP

**摘要原文**（正文与摘要的数值/符号若冲突，必有一处错）：

> We discuss the relation between Liouville theory and the Hitchin integrable system, which can be seen in two ways as a two step process involving quantization and hyperkaehler rotation. The modular duality of Liouville theory and the relation between Liouville theory and the SL(2)-WZNW-model give a new perspective on the geometric Langlands correspondence and on its relation to conformal field theory.

## 2. 引文概况

- INSPIRE recid 855518　被引 **145** 次　参考文献 0 条

最近的被引（挑与本文最相关的 2–3 篇复述去看）：

- Geometries of Quantum Field Theories　`2609.28210`
- Holographic one-dimensional quantum systems　`—`
- A solvable model of 3d quantum gravity　`2605.12590`
- Quantum Flat Connections, KZ equations, and Integrability　`2604.26159`
- Lagrangian correspondences for moduli spaces of Higgs bundles and holomorphic connections　`2604.14127`
- Holographic one-dimensional quantum systems　`—`
- Higher-Rank Mathieu Opers, Toda Chain, and Analytic Langlands Correspondence　`2512.18744`
- Fused Specht polynomials and 𝑐=1 degenerate conformal blocks　`—`

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

