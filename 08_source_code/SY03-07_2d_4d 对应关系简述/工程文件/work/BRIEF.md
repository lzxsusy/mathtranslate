# BRIEF —— 分工、边界与接续点（v1，Lead 冻结）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 0. 一句话

把 Tachikawa 的 *A brief review of the 2d/4d correspondences*（arXiv:1608.02964v5，46 页）
译成中文 LaTeX 译注本。**6 位译者**按原文章节边界切块，每块 5–7 页；Lead 负责前置（标题/摘要/
译者说明/§1/参考文献）与全流程合成、编译、校验。

**开工前必须按顺序把下面 4 个文件全文读完**（绝对路径）：

1. `<本地路径>` —— 硬规范，逐条遵守
2. `<本地路径>` —— 本文件（分工/边界）
3. `<本地路径>` —— 术语冻结表
4. `<本地路径>` —— Lead 的边界裁决

## 1. 实测底本数据（**不要凭印象，以下是脚本实测值**）

| 项 | 实测值 |
|---|---|
| 作者 / 标题 | Yuji Tachikawa（立川裕二）/ *A brief review of the 2d/4d correspondences* |
| 编号 | IPMU-16-0048；arXiv:1608.02964v5（2016-10-15）；综述文集 *Localization techniques in quantum field theories* 第 13 章 |
| 总页数 | 46（正文 pp.1–41，参考文献 pp.41–46） |
| 页码偏移 | **0**（PDF 页号 = 印刷页码） |
| 版面 | US Letter，612 × 792 pt |
| 图 | **13 幅（图 1–13）**，全部为矢量图（0 张位图），已裁为 `work/figures/figN.png` |
| 表 | **0 张**（原文没有任何 Table） |
| 编号公式 | **137 条**：1.1 / 2.1–2.72 / 3.1–3.11 / 4.1–4.27 / 5.1–5.26（**§6 无编号公式**） |
| 参考文献 | 77 条（`[1]`–`[77]`，0 缺号 0 重号；由 Lead 用脚本转录，译者不管） |
| 附录 / 习题 / 要点框 | **都没有** |
| 脚注 | pp.3、pp.8 等零星出现（脚注 1 起） |

> 真值表：`work/tags.txt`（tag → 页码）、`work/tags_bypage.txt`（页 → tag）。**这是验收唯一依据。**

## 2. 分工总表

| 块 | 负责人 | 原文页 | tag 区间 | 写的 chunk 文件 | 归属的章节标题 |
|---|---|---|---|---|---|
| c00 | Lead | p.1–2 | — | `c00.tex` | 标题页/摘要/译者说明 |
| c01 | Lead | p.3 + p.4 上半 | **1.1** | `c01.tex` | `\section{Introduction}` |
| tr-01 | **tr-01** | **pp.4–9** | **2.1–2.30** | `tr01a.tex` `tr01b.tex` `tr01c.tex` | `\section{Two two-dimensional theories}`、`\subsection{Two-dimensional Yang-Mills theories}`、`\subsubsection{Action}`、`\subsubsection{On the cylinder}`、`\subsubsection{On a general surface}`、`\subsubsection{q-deformation}` |
| tr-02 | **tr-02** | **pp.10–16** | **2.31–2.72** | `tr02a.tex` `tr02b.tex` `tr02c.tex` | `\subsection{The Liouville theory}`、`\subsubsection{Free boson theory}`、`\subsubsection{Interacting theory}`、`\subsubsection{Four-point function: general structure}`、`\subsubsection{Four-point function: explicit expressions}` |
| tr-03 | **tr-03** | **pp.16–21** | **3.1–3.11** | `tr03a.tex` `tr03b.tex` | `\section{A class of four-dimensional theories}`、`\subsection{N=2 supersymmetric gauge theories}`、`\subsection{Class S theories of type SU(2)}`、`\subsubsection{Construction from three-punctured spheres and cylinders}`、`\subsubsection{One-punctured torus}`、`\subsubsection{Four-punctured sphere}`、`\subsubsection{General consideration}` |
| tr-04 | **tr-04** | **pp.21–28** | **4.1–4.27** | `tr04a.tex` `tr04b.tex` `tr04c.tex` | `\section{Two supersymmetric backgrounds}`、`\subsection{General yoga of supersymmetric localization}`、`\subsection{$S^1\times S^3$}`、`\subsection{$S^4$}`、`\subsubsection{General structure}`、`\subsubsection{Classical and one-loop factors}`、`\subsubsection{Instanton contributions}` |
| tr-05 | **tr-05** | **pp.28–36** | **5.1–5.26** | `tr05a.tex` `tr05b.tex` `tr05c.tex` | `\section{Two correspondences and an interpretation}`、`\subsection{$S^1\times S^3$ and the two-dimensional Yang-Mills}`、`\subsection{$S^4$ and the Liouville theory}`、`\subsection{Six-dimensional interpretation}`、`\subsubsection{6d $\cN=(2,0)$ theory and 4d class S theories}`、`\subsubsection{Alternative derivations of the correspondences}` |
| tr-06 | **tr-06** | **pp.36–41** | **无编号公式** | `tr06a.tex` `tr06b.tex` | `\section{Future directions}`、`\subsection{Two unsolved problems in the SU(2) case}`、`\subsection{More objects in the SU(2) case}`、`\subsection{Using 6d $\cN=(2,0)$ theories of other types}`、`\subsection{Other spacetimes, other theories}`、`\section*{致谢}`（用 `\section*{致谢}` + `\addcontentsline`） |
| c-refs | Lead | pp.41–46 | — | `c-refs.tex` | `\section*{参考文献}` |

> 章节标题一律用 `\section` / `\subsection` / `\subsubsection`（**自动编号**，不要手写编号）。
> `\section*{致谢}` 这类带星标题：紧随其后加 `\addcontentsline{toc}{section}{致谢}`。

## 3. 边界锚点表（**逐字对齐，这是防重复/防遗漏的唯一依据**）

每块的**起点锚点**与**终点锚点**都在这里写死。**起点含锚点句，终点到锚点句之前为止。**

| 边界 | 位置 | 裁决 |
|---|---|---|
| Lead → tr-01 | p.4 的 `2 Two two-dimensional theories` 标题 | Lead 的 c01 在「…possible future directions.」这句**写完为止**（含句号）；tr-01 **从这个 `\section` 标题开始**，第一句正文是「Let us first study two-dimensional Yang-Mills theories.」 |
| tr-01 → tr-02 | p.10 顶部 `2.2 The Liouville theory` 标题 | tr-01 在 **p.9 最后一句**「It is known that the same deformation arises also string theoretically [13], although the underlying quantum group is not directly visible there.」处**结束**；tr-02 **从 p.10 的 `\subsection` 标题开始**，第一句是「We will now study the second two-dimensional field theory, known as the Liouville theory.」 |
| tr-02 → tr-03 | p.16 的 `3 A class of four-dimensional theories` 标题 | tr-02 在 **式 (2.72) 之后那句**「It is instructive at this point to write a program in a computer algebra system of the reader's choice to compute the conformal block to the arbitrary order in $q$.」处**结束**；tr-03 **从 `\section` 标题开始**，第一句是「In this section we introduce a class of four-dimensional $\cN=2$ supersymmetric gauge theories…」 |
| tr-03 → tr-04 | p.21 的 `4 Two supersymmetric backgrounds` 标题 | tr-03 在 **p.21**「…a single quantum field theory, of which various distinct Lagrangians are just avatars.」处**结束**；tr-04 **从 `\section` 标题开始**，第一句是「In this section we first discuss the general idea of supersymmetric localization, following the approach pioneered by [21]…」 |
| tr-04 → tr-05 | p.28 的 `5 Two correspondences and an interpretation` 标题 | tr-04 在 **p.28**「…the $S^4$ localization of [6] was originally conceived to derive this fact quantum field theoretically.」处**结束**；tr-05 **从 `\section` 标题开始**，第一句是「Here comes the crux: we compute the partition functions of the class of 4d $\cN=2$ theories…」 |
| tr-05 → tr-06 | p.36 的 `6 Future directions` 标题 | tr-05 在 **p.36**「…The details can be found in the paper [37].」处**结束**；tr-06 **从 `\section` 标题开始**，第一句是「At this point we have gone through the very basics of the 2d/4d correspondence…」 |
| tr-06 → c-refs | p.41 `References` 之前 | tr-06 到**致谢最后一句**「This work is supported in part by JSPS Grant-in-Aid for Scientific Research No. 25870159 and in part by WPI Initiative, MEXT, Japan at IPMU, the University of Tokyo.」**为止**；`References`（77 条）由 Lead 的 `c-refs.tex` 写，tr-06 **不要碰** |

## 4. 图归属（13 幅，谁写哪个图）

| 图 | 原文页 | 归属 | 内容提要 |
|---|---|---|---|
| 图 1 | p.5 | tr-01 | 周长为 $L$ 的圆柱面 |
| 图 2 | p.6 | tr-01 | 圆盘与三孔球面上的和乐 |
| 图 3 | p.6 | tr-01 | 通过粘接圆柱改变圆盘面积 |
| 图 4 | p.7 | tr-01 | 把圆盘缝到孔上 |
| 图 5 | p.8 | tr-01 | 四孔球面切成两个三孔球面 |
| 图 6 | p.13 | tr-02 | 四穿刺球面由两个三穿刺球面粘成 |
| 图 7 | p.17 | tr-03 | 三穿刺球面 ↔ $Q_{aiu}$，$\SU(2)^3$ 对称性 |
| 图 8 | p.18 | tr-03 | 参数为 $\tau$ 的圆柱 ↔ $\SU(2)$ 矢量多重态 |
| 图 9 | p.19 | tr-03 | 单穿刺环面由三穿刺球面粘两点得到 |
| 图 10 | p.20 | tr-03 | 四穿刺球面的三种不同分解 |
| 图 11 | p.27 | tr-04 | Young 图 $Y=(5,4,3,2,2,1)$ 与盒子 $s=(2,2)$ 的臂长/腿长 |
| 图 12 | p.35 | tr-05 | 六穿刺球面的两种不同分解 |
| 图 13 | p.35 | tr-05 | 六维理论在 $S^4\times$ Riemann 面上及其维数约化 |

**写法**（`figN.png` 由 Lead 裁好放在 `work/figures/`，`\graphicspath` 已配）：

```latex
\begin{center}
  \includegraphics[width=0.45\textwidth]{fig5.png}
  \figtitle{5}{四孔球面切成两个三孔球面（原文图 5）}
\end{center}
```
宽度自选 0.35–0.55 之间，按原图比例；图注必须**忠实中译**原文 `Figure N:` 后那句话。

## 5. 工作方法（照做，别自创）

1. 先读 `work/split/pNNN.txt`（逐页文字层）**把握论证结构**——文字层只用于定位，
   **数学一律不可信**（见 STYLE_GUIDE ⑨）。
2. 再逐页 `read_image` 看 `work/pages/pNNN.png`（200 dpi，全 46 页已渲染）。
   公式**逐符号抄写**，核对上下标、希腊字母、花体、`\bar`/`\overline`、分子分母归属。
3. 看不清就裁图放大（500–1000 dpi）：
   ```powershell
   $py = "<本地路径>"
   & $py "<本地路径>" 5 120 90 480 260 "$env:TEMP\p5fig.png" 500
   ```
   坐标是 PDF 点：整页宽 612、高 792，原点左上。
4. **不要编译**（Lead 统一编译）。**不要改** `preamble.tex` / `main.tex` / `STYLE_GUIDE.md` /
   `BRIEF.md` / `glossary.tsv` / 别人的 chunk。
5. 边译边写，先写 `a` 片（前 2–3 页），再写 `b`、`c`；写一个存一个，避免一次性大文件。
6. 每个式子的编号以 `tags_bypage.txt` 该页的清单为准（**那是我从 PDF 右边界实测出来的**）。
7. 批注密度：每 2–3 页 ≥1 条 `% [Tutor Note: ...]`，每节 ≥3 条（STYLE_GUIDE ⑤）。

## 6. 环境

| 项 | 值 |
|---|---|
| 项目根 | `<本地路径>` |
| 页图 / 文字层 | `work\pages\pNNN.png` / `work\split\pNNN.txt` |
| 公式真值表 | `work\tags.txt`、`work\tags_bypage.txt` |
| 裁图工具 | `work\tools\crop.py <页> <x0> <y0> <x1> <y1> <out.png> [dpi]` |
| Python | `<本地路径>`（含 pymupdf） |
| LaTeX | `<本地路径>`（LuaLaTeX 1.24 / TeX Live 2026） |
| 交付目录 | `deliverable\`（Lead 打包） |

## 7. 完成时（回执 5 项，见 STYLE_GUIDE ⑪）

写完 → 自查 → `send_message` 给 `lead`，标题写明「tr-0N 交稿」。**交稿后不要停等，**
Lead 可能会派交叉校对任务给你（校别人的一块，只写报告不改文件）。
