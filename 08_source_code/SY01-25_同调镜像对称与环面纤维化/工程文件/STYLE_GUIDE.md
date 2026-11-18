# 风格指南 · SY01-25《同调镜像对称与环面纤维化》中译注本

## 0. 身份与目标

读者是懂微分几何与同调代数、但不做镜像对称的数学研究者（研究生三年级以上）。
目标文本：**读起来像一本中文数学专著里的一节**，而不是「英文原文的逐词对照」。
硬约束排序：数学正确性 > 术语一致 > 可读性 > 文采。任何情况下不允许为了顺口而改动命题真假。

## 1. 文体

- 正文用书面语，不用「我们觉得」「大家知道」；原文的 *we* 译为「我们」可以保留（作者确实在提出主张）。
- 段落切分随原文，不随意合并/拆分段落；原文一句太长时允许断成两句，但不得丢掉逻辑连接词
  （Thus / Hence / Henceforth / In particular / Moreover 必须显式译出：因此／于是／今后／特别地／此外）。
- 禁止口语、网络语、感叹号；禁止「让我们……」（改为「我们来……」或直接陈述）。
- 中文标点：逗号、句号、顿号、「」使用全角；数学公式周围不加全角空格；`$...$` 前后不留空格由 LaTeX 处理。
- 数字与公式混排：中文与行内公式之间不加空格（LaTeX 自然处理字距）。

## 2. 术语

- 一律以 `工程文件/work/glossary.tsv` 为准。**首次**出现给「中文（English）」，之后只用中文。
  例：整仿射结构（integral affine structure）……此后只写「整仿射结构」。
- 人名一律不音译：Kontsevich、Soibelman、Fukaya、Gromov、Hausdorff、Monge、Ampère、Legendre、
  Kähler、Calabi、Yau、Hodge、de Rham、Dolbeault、Berkovich、Narain、Virasoro、Morse、Smale、
  Floer、Hochschild、Deligne、Karoubi、Bridgeland、Fourier、Mukai、Alexandrov、Ricci、Einstein、
  Bott、Poincaré、Massey、Koszul、Puiseux、Laurent、Amoeba 等。
- 复合词按「中心词后置」：homological mirror symmetry → 同调镜像对称；torus fibration → 环面纤维化。
- 不新造四字词；可用「……性」「……化」「……结构」「……范畴」等常规后缀。
- 表外术语：先查 glossary，未收则按学界通行译法，并在译注中首次给出英文，同时登记到报告的
  「新增术语」表（格式：english → 中文 → 出处页）。

## 3. 数学排版

- 公式**只信页面图像**：凡独立公式（display）、定理陈述中的公式、上下标密集的式子，必须
  `read_image` 回看 `工程文件/work/pages/pNNN.png` 逐符号核对；文字层（pNNN.txt）只作取文用，其上下标、
  希腊字母、重音一律不可信（pdftotext 会把 `X^{mer}_q` 打散）。
- 原文的编号一律照抄：定理 1、定义 5、命题 12、注 19……（每类环境在 preamble 中已各自连续编号，
  直接用 `\begin{thm}` 等即可自动得到正确编号；**不要**手写编号）。
- 引用节号写「§6.3」；引用定理写「定理 3」。原文「the theorem from 6.3」指的是 §6.3 中的定理，不要
  误当「定理 6.3」。
- 花体/黑板体：用 preamble 的宏（`\A \F \Z \R \C \M` 等）或直接 `\mathcal{}`、`\mathbb{}`；不要用
  `\mathbbm`、`\mathrsfs`（未加载）。
- 只允许使用 amsmath/amssymb/mathtools/bm/tikz/tikz-cd 的命令与 preamble 已定义的宏。**不得**新增
  `\newcommand`（会与主文件冲突）；确需新宏时在报告中说明，由 Lead 统一加进 preamble。
- 交换图用 `tikz-cd`；示意图用 `tikz`，节点文字用中文，标签用数学体。

## 4. 译注（`yizhu` 环境）——克制使用

只在下列三种情形写译注，每条 1–4 句，能一句话说清就一句话：

1. **术语/背景**：某个概念对目标读者不显然（如「幂零轨道定理」的内容、SYZ 猜想与本文的关系），
   给出最小必要解释；可引文献（用原文的 `[SYZ]` 之类标签，不要自己编引用）。
2. **原文的省略或含糊**：原文写 "one can show" 而未给证明，或记号未定义即使用——指出「原文此处未展开，
   可参见……」，**不得**自行补出证明冒充原文。
3. **原文的笔误/矛盾**：明确写「译者按：原文此处……，疑为……之误」，并给出判断依据。

禁止：把译注写成小论文；在译注里引入原文没有的定理；对原文做「修正」而不标注。

## 5. 原文错误的处理

发现原文数学错误或排版错误时：**译文照原文译出**（数学内容不动），紧随其后加一条译注说明问题。
若只是排版错误（如上下标错位、缺括号），按数学意义修正并在译注中说明「原文排版如此」。

## 6. 交付格式

- 每个 chunk 文件（`源码/chunks/chNN.tex`）是**纯正文**：不含 `\documentclass`、`\begin{document}`、
  不含 `\input{preamble}`；从 `\section{...}` 或 `\subsection{...}` 开始。
- 节标题用 `\section{中文标题}`（不写节号，LaTeX 自动编号）；小节用 `\subsection{...}`。
- 图表：`\begin{figure}[htbp]\centering ... \caption{中文图题}\label{fig:...}\end{figure}`。
- 每个 chunk 末尾用注释标出对应原文页码：`% [原文 p4–p12]`。
- 数学环境后不要空行堆叠；用 `\begin{proof}...\end{proof}`（preamble 已设 `proofname` 为「证明」）。
- 不在正文里写「（见下页）」「（转下页）」这类排版性提示。

## 7. 参考文献

原文 p63–66 的参考文献表**不译**，整体放在 `源码/back/references.tex`，条目照原文英文抄录，
仅把标题行改为「参考文献」。正文引用沿用原文标签 `[SYZ]`、`[Ko]` 等，不改写为数字。
