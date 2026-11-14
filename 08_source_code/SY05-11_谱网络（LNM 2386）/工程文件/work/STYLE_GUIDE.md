# STYLE_GUIDE.md —— 硬性规范（先于分工，违反者返工）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 项目：Springer LNM 2386《Spectral Networks: Bridging higher-rank Teichmüller theory and BPS states》中文译注本
> 底本：514 页 PDF；**印刷页码 = PDF 页号 − 40**；26 章 + 附录 A + Glossary + Bibliography + Index
> 编译：xelatex ×2（Lead 统一执行，译者不编译）

---

## §1 页码体系（三套编号只用一套）

- **一律用印刷页码**（= PDF 页号 − 40）。片段里的 `% [原文 p.xx]` 指印刷页码。
- 图像文件 `work/pages/pNNN.png` 用的是 **PDF 页号**（p001–p514）。查图时按 PDF 页号找。
- 不要自己换算后混用；报告里写印刷页码 + PDF 页号（如 `p.87 / PDF p127`）。

## §2 交付物格式（片段规则）

- 每个分块交付 **一个 .tex 文件**：`work/src/part/<block>.tex`（块名由任务书给定，如 `ch03.tex`、`ch17a.tex`）。
- 文件**只含正文片段**：
  - ✅ `\chapter{...}`（**只允许出现在任务卡指明的新章开头**，标题按任务卡给的中文译名）、`\section{...}`、`\subsection{...}`、`\subsubsection{...}`、段落、公式、环境、`\Fig{...}`、`% [原文 p.xx]` 注释
  - ❌ 禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\def`、`\input`、`\include`、`\tableofcontents`、`\part{}`
- 章的「续块」（如 ch17b）**不写 `\chapter`**，直接从正文继续。
- 附录 A 的章标题写 `\chapter*{附录 A\quad 李论基础}`（不参与编号，节编号用 `\section*`? —— 不：用 `\section{...}` 但配合 `\setcounter{section}{0}`；见任务卡说明）。
- 文件编码 **UTF-8 无 BOM**，换行 LF。写完用工具核一次。
- `\section` 标题**不带编号**（编号由 LaTeX 自动生成，和原文一致）；若原文标题里含数学（如 `$\Theta$-positivity`），写成 `\section{$\Theta$ 正性}`，**不要**在标题里放会使 pdf 书签出错的裸数学以外的内容。

## §3 公式编号（唯一真值：原文图像）

- 所有**编号公式**必须与原文一一对应，不缺、不重、不跳、不自造：
  ```latex
  \begin{equation}
    ... \tag{1.1}
  \end{equation}
  ```
- 多行对齐：`\begin{align} ... \\ ... \tag{1.2} \end{align}`，**每行都要 \tag**（共用一号就每行同一 tag，或按原文拆号）。
- 同一行并列多式共用一号：`A=B,\qquad C=D \tag{1.7}`
- 无编号公式用 `\[ ... \]` 或 `equation*`。
- 正文引用写**纯文本**「式 (1.1)」/「(1.1)」，**不用** `\eqref`/`\ref`（tag 是手工的，自动引用不可靠）。
- 每章编号总数以 `work/tags.txt` 对应章为准；**图像为准**，若图像与 tags.txt 不一致，以图像为准并在报告里注明。

## §4 定理类环境（编号手工给定）

原文形如 `Definition 1.1` / `Theorem 3.4` / `Example 2.2` / `Remark 1.3` / `Exercise 1.5`。

```latex
\begin{definition}[1.1] ... \end{definition}
\begin{theorem}[3.4] ... \end{theorem}
\begin{proposition}[2.7] ... \end{proposition}
\begin{lemma}[2.8] ... \end{lemma}
\begin{corollary}[2.9] ... \end{corollary}
\begin{example}[2.2] ... \end{example}
\begin{exercise}[1.5] ... \end{exercise}
\begin{remark}[1.3] ... \end{remark}
\begin{notation}[1.4] ... \end{notation}
\begin{convention}[1.6] ... \end{convention}
\begin{claim}[1.7] ... \end{claim}
```
- **编号必须照抄原文**，不许自增编号。
- 证明：`\begin{proof} ... \end{proof}`（已汉化为「证明」）；原文 `Proof of Theorem 1.1` → `\begin{proof}[定理 1.1 的证明]`。
- 原文无编号的「定理/定义」，用 `\begin{theorem} ... \end{theorem}`（无方括号）。

## §5 插图（Lead 已裁好，只能引用，不得自造）

- **图目录 `work/figures/*.png` 与 `figures.json` 由 Lead 独占维护（全本已按「图注分带」算法统一重裁）。发现某图裁错/串图/缺图，不要自己改图：把「PDF 页码 + 图号 + 现象」报给 Lead。**
- 图的真值：`work/figures/fig_X_Y.png`；清单见 `work/figures.json`（字段：page=PDF 页号, num=图号, file=文件, caption=英文图注）。
- 用法（宽度自己按图的形状定，0.4–1.0 之间，**不许超过 `\linewidth`**）：
  ```latex
  \Fig[0.75\linewidth]{figures/fig_1_3.png}{1.3}{改变基点。}
  ```
  或原图无编号时用 `\FigNoNum{...}{...}`。
- 图注要**翻译**（中文），保留原图注里的数学与文献引用编号。
- 子图 (a)(b) 已合成一张图，图注里照原文写「(a) ...；(b) ...」。
- **禁止**：自己不画 TikZ 图、不造图、不省略图。图在，就必须放。

## §6 表格

- 原文若有表格（`Table X.Y`），按原文**重排为 LaTeX 表格**（booktabs），内容照抄不增删，表注翻译。
- **禁止造表**；没有表就不写表。

## §7 批注（Tutor Note）

- 只放在 LaTeX 注释里，不进入排版：`% [Tutor Note: ...]`
- 批注必须满足其一：① 可验证的易错点（给核对方法）；② 补出的省略论证（说清用哪条定理/哪篇文献）；③ 原文笔误（给正确形式 + 判断依据）。
- 批注是**注释**，里面的 `$` 不会被 TeX 处理，可自由用；但**不要写不成对的 `$`**（自检脚本会误报）。
- 批注用中文；公式可用 `$...$`。
- 密度：每 3–5 页至少 1 条有信息量的批注；不写「本段讲的是……」这类空话。

## §8 数学宏（统一用 preamble 已定义的，禁止自造）

已定义（详见 `work/src/preamble.tex`）：
`\R \C \Z \Q \N \PP \HH \DD \OO \g \h \n \sl \gl \so \su \sp`
`\Tr \tr \rank \diag \Spec \Hom \End \Aut \GL \SL \PSL \PGL \SO \SU \U \Mat \Rep \Loc \Fib \Iso \im \coker \sgn \const \vol \area \length`
`\de \dd \ee \ii \op{...}`

- 希腊字母：正文里写 `$\zeta$`、`$\vartheta$`，**不要**直接写 Unicode 希腊字母（正文字体缺字形）。
- 缺宏怎么办：**不要自己 `\newcommand`**，在报告里列出来，Lead 统一加。
- 常用但未预定义的，直接用标准 LaTeX：`\mathfrak{...}`、`\mathcal{...}`、`\mathbb{...}`、`\operatorname{...}`、`\overset`、`\xrightarrow`。

## §9 术语（glossary.tsv 冻结表）

- 开工前必须读 `work/glossary.tsv`；**表里有的术语必须照表译**。
- 表里没有的：按数学/物理惯例译，首次出现「中文（English）」，后续只用中文；并在报告里列出「新增术语」。
- 人名按惯例：Teichmüller 泰希米勒、Hitchin 希钦、Fock–Goncharov 福克–贡恰罗夫、Seiberg–Witten 塞伯格–威滕、Stokes 斯托克斯、Virasoro 维拉索罗、WKB 保留 WKB、BPS 保留 BPS、Gromov–Witten 格罗莫夫–威滕、Fenchel–Nielsen 芬切尔–尼尔森。
- 保留英文原文的：BPS、WKB、S-对偶（S-duality）、N=2、class S（S 类）、opers、cameral、cluster（用「簇」）。

## §10 禁止事项（红线）

1. **不造假**：不插图、不造表、不补文献、不加作者没说的话。
2. **正文一字不改**：原文笔误照原样译，只在批注里指出并给正确形式。
3. **不臆测公式**：图像看不清就写 `% [Tutor Note: 原文此处公式模糊，待核：...]` 并在报告里列出页码，**不猜**。
4. **不写 markdown**：`**粗体**` 在 LaTeX 里会印成星号；要用就 `\textbf{}`。
5. **不批量正则改写**（Lead 也一样）：语法问题单点修复。
6. **不用 `\ref`/`\eqref`/`\cite`**：交叉引用与文献引用一律写纯文本编号（如「式 (3.4)」「见 [12]」）。
7. **不删内容**：习题、例子、注、脚注一律译；脚注用 `\footnote{}`。
8. **不翻译 Bibliography 条目正文**（由 Lead 统一处理，英文原样保留）。

## §11 每块自查清单（交付前必须过一遍）

- [ ] 本块覆盖的每一页都译了，无漏段、无漏公式、无漏图
- [ ] 每个编号公式都有 `\tag{X.Y}`，编号与原文逐个核对（**看图像**）
- [ ] 每个定理/定义/例/习题编号与原文一致（不是自己数的）
- [ ] 所有图都放了 `\Fig`，图号与图注与原文一致
- [ ] 无 `\documentclass` / `\usepackage` / `\newcommand` / `\begin{document}`
- [ ] 无 ASCII 直引号乱码、无 markdown 粗体、无未闭合 `$`
- [ ] `% [原文 p.xx]` 段落锚点齐全（每页至少一个）
- [ ] 文件编码 UTF-8 无 BOM

## §12 报告格式（每次交付后回给 Lead）

```
块名：ch03
覆盖：印刷 pp.21–36（PDF p61–p76），全部完成 / 部分完成（缺 p.xx）
公式：原文 3.1–3.7 全部落实；另发现未编号公式 N 条（已用 equation*）
图：Fig 3.1, 3.2 已放；无漏图
定理：Definition 3.1–3.4, Theorem 3.1, Example 3.1–3.2, Remark 3.1 已核
批注：M 条（列出最重要 3 条）
存疑/需 Lead 裁决：<页码 + 具体问题>
新增术语：xxx（English）...
缺宏：\xxx
```

## §9b 章首摘要与宏补充（2026-11-03 追加）

- 每章开头都有 Springer 式 Abstract：一律写 \ChapterAbstract{中文译文}（preamble 已定义，排为小字缩进块），**不要**用 \begin{abstract}（book 类没有该环境）。
- 追加宏：\Sp（辛群）、\Sym（对称矩阵）、\Stab（稳定化子）、\Homeo。
- 数学里**不要用 \iddots**（本机未装 mathdots），需要斜向省略号用 \ddots。