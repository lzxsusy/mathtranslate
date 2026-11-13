# 翻译工作规范（《局部同调镜像对称》中译注本）

本文件是全体译手必读的施工规范。**先读 `src/chunks/ch00.tex`（Lead 样板章）与 `work/terms_zh.tsv`（本项目冻结术语表），再动笔。**

## 0. 底本

- 原文：arXiv:2611.07202v1 [math.SG]，**Local Homological Mirror Symmetry**，56 页，Si-Yang Liu、Kyungmin Rho。
- 逐块源码：`src/chunks/_src/<ch>_src.tex`（按原文 main.tex 行号切好，每 20 行有 `%% ---- 原文行 N ----` 标记）。
- 原文 PDF 页 ↔ 源行映射：`work/page_start.json`。译文里**每页开头**插一行注释 `% [原文 p.N]`（N 为 PDF 页码，从 1 开始）。
- 原文 PDF 文本：`<本地路径>`（带 `===== PDF PAGE n =====` 标记）。**公式一律以 `_src` 里的 LaTeX 源码为准**（PDF 文本层常把上下标压平、希腊字母压坏）。

## 1. 输出

每块译文写到 `src/chunks/<ch>.tex`，**只写正文内容**（不含 `\documentclass`/导言区），可含 `\section`、`\subsection`、环境、公式、图。要求：

- 文件开头一行注释：`% chNN 译文：原文 §...（main.tex 第 A–B 行）`
- 定理类环境名与原文一致：`thm dfn defn prp prop crl cor conj nota ques exmp example lmm lemma rmk cnv exer proof`。**所有 label 原样保留**（`\label{thm:...}`），交叉引用 `\ref{}`/`\eqref{}` 原样保留。
- 编号自动生成：所有定理类环境共享计数器、按节编号；**不要手写编号，不要改节的顺序**。原文节标题即 `\section{Introduction}` 等，译文写 `\section{引言}`；`\subsection` 同理（原文小节标题如 "Statement of the result." 译作「主要结果」）。
- 带编号的公式环境原样保留（原文只有 4 个 `equation` + 1 个 `align`）；`\[ \]` 保持不编号。
- 图：`\begin{figure}` 整段原样保留（含 `\includegraphics`、`\caption`、`\label`），caption 译为中文；`\begin{tikzcd}`/`tikzpicture` 原样保留，图内英文标签可译（中文用 `\text{}` 包裹）。
- 表格按原文保留。

## 2. 数学正确性（最高优先级）

- 逐符号对照 `_src`：上下标、指标、符号（$\pm$、$\otimes$、$\circ$、$\comp$）、括号层级不得出错。
- **不臆造、不补写、不删减**。原文有笔误（拼写、明显的上下标笔误）时：**正文照原文排印**，在 `\begin{yizhu}` 中说明（"原文作 X，疑为 Y"），不要悄悄改。
- 原文中 `\emph{...}` 标记的术语，译为中文并用 `\emph{...}`（导言区已把 `\emph` 定义为黑体加粗）。
- 人名：音译 + 首现括注原文（Kontsevich（孔采维奇）），之后只用音译；已有通行译名者用之。**数学名词不音译**（Fukaya、Liouville、Weinstein、Künneth、Floer、Čech、Orlov、Kartal、SYZ、HMS 等保留英文）。
- 引用 `\cite{...}` 原样保留（参考文献保留英文，不译）。

## 3. 文风

- 学术书面语，简洁准确，避免口语。**禁用**：「被……所」「进行……的」「对于……而言」「起到……的作用」「有着……的意义」等病灶句式（终审会 grep）。
- 全角中文标点；英文术语、数字、公式两侧留半角空格（如「Fukaya 范畴」「A∞-函子」「$2$-范畴」）。
- 行内公式后的句末标点放在公式之后，用全角（例：……同构 $\mathcal{F}(X)\simeq\Coh(Y)$。）。
- 长句可拆分，但不改变逻辑；并列结构保持。
- 术语按 `work/terms_zh.tsv`，**不得自创第二译法**；表里没有的新术语，首次出现给「中文（英文）」并登记到 `work/terms_zh.tsv`（追加，不覆盖他人）。

## 4. 三类译者批注（可见方框）

一律用导言区已定义的三个环境，**每个 chunk 至少 2 个 `yizhu` + 1 个 `conceptbox`**（附录块可少些）：

### 4.1 `\begin{yizhu}[短标题] ... \end{yizhu}`
橙色方框，全局连续编号。只写三类内容：

1. **易错预警**：记号陷阱（同一符号两义、上下标易混、原文记号与常见约定相反）、原文笔误/存疑处、读者最容易误解的一步。
2. **含糊点拨**：原文一句话带过但论证跳步的地方——补一句"此处用到 X 定理 / 因为 Y，所以 Z"的提示（**只提示思路，不代替证明**）。
3. **背景直觉**：这个构造/定理在几何上想干什么（一两句）。

禁止空话（"此处很重要""读者需注意"），禁止摘抄正文，单条 60–300 字。**标题**写主题（如 `[为什么是映射柱]`、`[原文笔误]`、`[记号警告]`）。

### 4.2 `\begin{conceptbox}{概念名} ... \end{conceptbox}`
紫色侧栏，**概念回顾**，不编号。用于正文首次出现、但对非专家不显然的概念（如"包裹 Fukaya 范畴""Weinstein 扇形""对数爆破""扭 Künneth 公式""轨道范畴"）。写法：

- 3–6 句：定义/构造要点 → 关键性质 → 本文为什么需要它。
- 可含 1–2 个行内公式，不放大段推导。
- **准确性**：以 nLab 条目、原始文献为准；有疑问就查。每个概念框末尾一行小字给出处，例如：
  `\par\smallskip\noindent{\footnotesize 参考：nLab, \emph{Weinstein manifold}；\cite{GPS24S} 第 2 节。}`
- 同一概念全书只开一次框（前文已开过就 `\ref` 到它，不重复开）。全书的框清单见 `work/concepts.tsv`（由 Lead 维护，写入前先看）。
- 不要开成"教科书章节"：控制在 6 句以内。

### 4.3 `\begin{keytakeaways} ... \end{keytakeaways}`
蓝色方框，**每节末尾一个**（若该 chunk 含整节）。3–5 条 `\item`，概括本节在证明链条中的位置、核心构造、结论。这是给读者的地图，不是摘要复述。

## 5. 编译自检（每个 chunk 必须做）

1. 在 `work/check/` 下建 `<ch>_test.tex`：
   ```latex
   \documentclass[11pt,a4paper]{article}
   \input{../../src/preamble.tex}
   \begin{document}
   \input{../../src/chunks/<ch>.tex}
   \end{document}
   ```
2. `xelatex` 跑两遍（在 `work/check/` 目录内），要求：**0 error**；允许的 warning 只有 "Reference ... undefined"（因为跨块引用）与 "There were undefined references"。**不得有 Overfull \hbox 超过 5pt、不得有 Missing character**。
3. 编译日志摘要写到 `work/check/<ch>_log.txt`（只留 error/warning 行）。
4. 若 chunk 内有 `\cite`，测试时可加 `\bibliographystyle{alpha}` 与 `\bibliography{...}` 忽略（无 bib 时会报 warning，可接受）。

## 6. 交付与登记

- 完成后向 Lead 报告：chunk 名、译文字数、`yizhu`/`conceptbox`/`keytakeaways` 数量、新增术语（若有）、编译结果（error 数）、存疑处清单。
- 只改自己名下的 chunk 文件；**不要动** `src/main.tex`、`src/preamble.tex`、`src/front/`、他人 chunk、`work/terms_zh.tsv` 之外的文件（术语可追加到 terms_zh.tsv，用 `>>` 追加，勿重写）。

## 7. 常用对照（速查）

| 原文 | 译法 |
|---|---|
| wrapped Fukaya category $\mathcal{W}$ | 包裹 Fukaya 范畴（首现「包裹（wrapped）」） |
| Fukaya category $\mathcal{F}$ | Fukaya 范畴 |
| Weinstein sector | Weinstein 扇形（首现括注 sector） |
| Liouville sector | Liouville 扇形 |
| stop | 停止位（stop） |
| sectorial descent | 扇形下降 |
| proper descent | 真下降 |
| mapping cylinder | 映射柱 |
| toric degeneration | 环簇退化 |
| log blow-up / log structure | 对数爆破 / 对数结构 |
| projective bundle $\mathbb{P}(\mathcal{O}\oplus\mathcal{L})$ | 射影丛 |
| principal $\mathbb{G}_m$-bundle | $\mathbb{G}_m$-主丛 |
| sparse/near 等见 terms_zh.tsv | |
