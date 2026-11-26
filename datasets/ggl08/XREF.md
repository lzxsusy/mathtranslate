# 第 08 篇 · 外部核对底稿（xref）

- arXiv: `0905.2720`　抓取时间：2026-11-25T21:00:31
- 本文件是**机器抓的数据**，不是结论。下面每一栏都要人去核，并把核过的写进
  `notes.md` 的「## 核对与勘误」节；判为原文笔误的写进 `errata.tsv`。

## 1. arXiv 版本史（有 v2/v3 就要逐条核修版差异）

- 版本数：**1**　初版 2009-05-17　最后更新 2009-05-17
- 版本：v1 Sun, 17 May 2009
- 标题：Geometric Langlands From Six Dimensions
- 作者：Edward Witten
- 分类：hep-th
- comment：30 pp

**摘要原文**（正文与摘要的数值/符号若冲突，必有一处错）：

> Geometric Langlands duality is usually formulated as a statement about Riemann surfaces, but it can be naturally understood as a consequence of electric-magnetic duality of four-dimensional gauge theory. This duality in turn is naturally understood as a consequence of the existence of a certain exotic supersymmetric conformal field theory in six dimensions. The same six-dimensional theory also gives a useful framework for understanding some recent mathematical results involving a counterpart of geometric Langlands duality for complex surfaces. (This article is based on a lecture at the Raoul Bott celebration, Montreal, June 2008.)

## 2. 引文概况

- INSPIRE recid 820682　被引 **193** 次　参考文献 0 条

最近的被引（挑与本文最相关的 2–3 篇复述去看）：

- Generalized symmetries and manifest duality. I. Flat spacetime　`—`
- Dear Quantizers, Stochastic $\approx$ Brane　`2609.38209`
- Asymptotic limits in class-$\mathcal{S}$ theories and non-Abelian Hodge theory　`2609.26883`
- On interacting non-Abelian antisymmetric tensor field models　`2607.12798`
- Weyl anomaly coefficients of holographic defect CFTs at weak and strong coupling　`2604.19881`
- Soft cutoffs in the covariant phase space of dynamical reference frames　`2603.11966`
- A Scattering Transform for Noncommutative Instantons　`2601.07949`
- Holographic interpolations of defect CFTs　`2512.14853`

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
| 1 | 主定理的陈述与符号 | 摘要 + 被引论文的复述 + 库内互引篇 | 已核，无冲突。摘要、KW06 §1/§3、nLab「geometric Langlands correspondence」页三处一致：本篇 §1.2 p.3 的 Coh(Y_{G∨}(C)) ≃ D-mod(Z_G(C)) 与 nLab 的 OMod(Loc_{^LG}(Σ)) ≃ DMod(Bun_G(Σ)) 是同一陈述的两种写法；Y_G = Hom(π₁(C),G)、Z_G = 全纯 G-丛模栈的定义见 p.3。 |
| 2 | 关键公式的系数/符号/指数 | 至少另 2 处独立出处（库内卡、nLab、另一篇 arXiv） | 已核，判出一处 high 笔误（E1）。τ = θ/2π + 4πi/e² 与 KW06 (2.12)、Gukov–Witten (2.26) 一致；但 p.8 (3.4) 的 θ 项缺 i，而 KW06 (4.16)（欧氏号差）与 Gukov–Witten (2.38)(2.39) 均带 i，且本篇 p.4 的瞬子数取整论证要求 iθn ⇒ 记 E1（high，见 `errata.tsv`）。 |
| 3 | 命题编号与交叉引用 | 正文内引用处是否指向正确条目 | 已核。39 条参考文献逐条对到库内篇目：[7]=28、[9]=01、[10]=06、[12]=02、[13][14]=21/22、[36]=07；库内 11/16/23/36 本篇未引。式号定位另核：(5.4)(5.5) 在 **p.17**（非 p.16），(5.2) 定义于 p.15（p.11/16/17/23/27 均回引）。 |
| 4 | 数值/维数一致性 | 两边算一遍（如 dim、rank、指数） | 已核。rank H̃³(W×TN_k) = 2gk = rank(H¹(W)⊗Γ_k) ✓；dim R = (#Z)^g（p.12）与 level 1 WZW 共形块数 \|Z\|^g ✓；Sp(4) 复维 4/实维 8 与 Sp(2r), r=2 ✓；TN_k 无穷远纤维周长 2πR 与 (5.9) U(∞)=1/R² ✓。 |
| 5 | 记号与前后定义 | 同一符号在 §1 与 §5 是否同义 | 已核。τ 在 §1.2/§3/§4 同义（θ/2π+4πi/e²）；(4.2) 的 τ 指 T² 模参数，§3 (3.5) 已把二者等同。G∨ 在 §1.2 为 GNO/Langlands 对偶群，§4.1 p.14 明确 simply-laced 单连通时 G∨ = G_ad。P 在 §5.3 为 S¹ 旋转生成元、§5.5.1 等于瞬子数、§5.5.2 等于 L₀，三处同义。H̃³ 于 §5.4.1 p.22 定义。 |

可用外部检索：arXiv abs 页、nLab（`ncatlab.org/nlab/show/…`）、
作者后续论文、库内 46 篇、`datasets/*` 既有卡片。每条结论都要写下**出处定位**
（页/式号/§）。
