# 报告：ch03b

## 块名与页段
- 块名：`ch03b`
- 原书页段：p.180–192（PDF 181–193），共 13 页
- 输出文件：`src/chunks/ch03b.tex`
- 本章末块，块末含 `\chapterreview{}`（第 3 章结束）

## 块界说明
本块首行落在定理 3.3.6（驻相渐近展开）**证明的后半段**：PDF 181＝原书 p.180 顶端即 "Proof: Assume x0 = 0 and φ(0) = 0…"，定理陈述与原书 p.179 的正文属上一块 ch03a。故本块用 `\begin{proof}[定理 3.3.6 的证明]` 从证明起译，不重复陈述，文件第 5 行已写块界注释。本块不含 `\chapter`（章首 `\chapter{经由伪微分算子的量子化}` 由 tr06 的 ch03a 承担）。

## 节清单（标题按原文，编号由工程生成）
- §3.4 复合公式（3.4.1 外尔量子化与 Moyal 乘积；3.4.2 科恩–尼伦伯格量子化）
- §3.5 带阶函数的象征类（3.5.1 阶函数与象征类〔内含无编号粗体子标题「量子化」〕；3.5.2 渐近展开；3.5.3 \(L^2\) 性质）
- §3.6 维格纳变换（3.6.1 维格纳变换；3.6.2 维格纳分布）
- 块首另有例 3.3.7（原书 p.180–181），属 §3.3，未另起 `\section`。

## 陈述编号清单（手工照抄原文）
| 环境 | 编号 | 位置 |
|---|---|---|
| example | 例 3.3.7 | 块首（§3.3 收尾） |
| proposition | 命题 3.4.1 | §3.4.1 |
| proposition | 命题 3.4.2 | §3.4.2 |
| definition | 定义 3.5.1 | §3.5.1 |
| proposition | 命题 3.5.2 | §3.5.1 |
| example | 例 3.5.3 | §3.5.1 |
| definition | 定义 3.5.4 | §3.5.1 |
| proposition | 命题 3.5.5 | §3.5.1 |
| definition | 定义 3.5.6 | §3.5.2 |
| theorem | 定理 3.5.7（博雷尔引理） | §3.5.2 |
| theorem | 定理 3.5.8 | §3.5.2 |
| theorem | 定理 3.5.9（卡尔德隆–韦扬库尔） | §3.5.3 |
| theorem | 定理 3.5.10（紧性） | §3.5.3 |
| definition | 定义 3.6.1 | §3.6.1 |
| example | 例 3.6.2 | §3.6.1 |
| proposition | 命题 3.6.3 | §3.6.2 |
| proposition | 命题 3.6.4 | §3.6.2 |
| example | 例 3.6.5 | §3.6.2 |

共 18 条，与原文一致（定理 3.3.6 的陈述在 ch03a，本块只有其证明）。正文对 §3.3.5、§3.4.1、例 3.6.2、[63, 53]、[32] 等交叉引用的编号照抄。

## 图清单（原书页, 文件, 处理方式）
| 原书页 | 文件 | 处理方式 |
|---|---|---|
| p.186 | `figures/fig_p187_a.png` | 裁切 PNG（\(2/t\) 蓝曲线、\(\chi(t)\) 红曲线、虚线、横轴 1,2,\(t\)、纵轴 1,2；width 0.42\textwidth），图内只有数学符号，无整句英文，附 `% [图：原书 p.186，图内文字照原样保留]` |

`python tools\figtool.py auto 181 193` 全块只报出这 1 张候选图，其余页面无真图（p.190–192 的维格纳函数部分亦无图）。

## 自检
```
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch03b.pdf
```
```
OK   ch03b       字符 25065  节 3 小节  7 陈述 18 公式  77 图 1(TikZ  0) 批注 0
合计：问题 0 条，提示 0 条
```
草稿 16 页，已渲染 `work/preview/ch03b_1..16.png` 逐页抽查：公式与原书一致、无溢出页边、图清晰、中文标点为全角。

## 未决术语（已记 `work/term_requests_ch03b.md`）
标准量子化（standard quantization）、科恩–尼伦伯格量子化（Kohn–Nirenberg）、半范数（semi-norm）、多指标（multi-index）、驻相法（stationary phase）、准概率分布（quasi-probability distribution）、相干态（coherent state）、拉盖尔多项式（Laguerre polynomials）、不确定性原理（uncertainty principle）、博雷尔引理、主象征。

## 存疑处
1. **点记号字体**：原书第 3 章用粗正体 $\mathbf{x},\boldsymbol{\xi}$ 表示 $\R^n$（相位空间 \(\R^{2n}\)）中的点；译文全章统一用斜体 \(x,\xi\)，与本块前段及全书其余各章一致，未改粗体。**Lead 2026-11-07 裁定：同意保持斜体，全书统一（第 1、2、4 章本就用斜体，译本不必复刻底本的局部排版差异）。**
2. **Moyal 乘积的星号**：原文 ∗ 与 ⋆ 混排，译文统一用 `\star`；标准量子化的乘积记 `\star_{KN}`。微分算子统一记 \(D_x^\hbar\)（= ħ 缩放的一阶导数），首次出现处已随文说明。**Lead 2026-11-07 裁定：同意。**
3. **原文笔误（未改正文）**：原书 p.190 第 1 段 "as a substitute for the the nonexistent joint probability distribution" 中 "the" 重复，属英文排版笔误，中文译文按单次「的」处理，未在正文加 `Tutor Note`（不影响数学内容）。
4. **原书 p.192 的 $\mathrm{Wig}_{\psi_n}$**：原文此处只写下标 \(\psi_n\)（前面构造的是 $\mathcal W_{z_1,z_2}$），译文照抄下标，未擅自补写为 \(\mathcal W\)。
5. **谐振幅射的 $\mathcal H$**：原书例 3.6.5 用花体 \(\mathcal H\) 表示谐振子哈密顿量，与第 1 章经典哈密顿量宏 `\HP` 不同源，本块直接用 `\mathcal H`（`\HP` 用于 §1.11 的经典哈密顿量）。
