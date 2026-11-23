# SPEC —— 译文体例规范（LaTeX 层）

本文件规定**怎么排**；`BRIEF.md` 规定**怎么译、怎么交付**。两者一起读。

---

## 1. 一章配一个文件

命名：`源码/sections/sNN-关键词.tex`（NN 两位数，接 main.tex 里的 `\input` 顺序）。
文件内**不写** `\documentclass`、`\begin{document}`、`\input{preamble}`——main.tex 已含。

## 2. 骨架（照抄，只改内容）

```latex
\chapter{导引}% 原文 Chapter I: Introduction
\srcpage{7}

\section{局部 Langlands 对应}% 原文 I.1. The local Langlands correspondence

局部 Langlands 对应旨在描述局部域 $E$ 上约化群 $G$ 的光滑不可约表示 $\pi$ ……

\srcpage{8}

\section{总体图景}% 原文 I.2. The big picture

……\yizhu{本文的“空间 $\Spec E$”指 $E$ 上的谱，不应与曲线上的闭点混同。}{A：原文 §I.2 首段；Stacks Project Tag 01HX}
```

要点：
- `\chapter{中文题}`，原章号不再重编（LaTeX 自动给 I、II…）。原文里 `Chapter I` 的引用写「第 I 章」。
- `\section{中文节名}`，**原文的 I.1、I.2 编号不写进标题**，靠 LaTeX 自动编号；需要交叉引用时用 `\ref`。
- 每页起点放 `\srcpage{N}`（N = PDF 页 = 印刷页）。
- 段落之间空行；不许把一段拆成多段，也不许把两段并成一段。

## 3. 环境

| 原文 | 译法 |
|---|---|
| Theorem / Proposition / Lemma / Corollary | `\begin{theorem}` / `proposition` / `lemma` / `corollary` |
| Definition / Example / Construction / Question | `definition` / `example` / `construction` / `question` |
| Remark / Conjecture | `remark` / `conjecture` |
| Proof | `\begin{proof} … \end{proof}`（`amsthm` 自带，译作「证明」） |
| 无编号的段（类似"Remark."开头） | 用 `\begin{remark}[无编号]` 或加 `*` 环境 |

编号：LaTeX 按「章.节.序」自动编号，与原文编号不必强同；**报告里给对齐表**即可（`BRIEF.md` §5.2）。

## 4. 译注

```latex
\yizhu{术语首次出现时的解释或译法说明。}{A：原文 §I.1 第 2 段；nLab "geometric Langlands"}
\yizhuw{上下文可推、但找不到外部依据的说明。}
```
- 注文用中文书面语，一两句，别写成小论文（≤120 字为宜）。
- 来源等级：`A`（原始论文/经典教材/原文自身）、`B`（nLab / Stacks / ProofWiki，须与 A 交叉）、`I`（本库既有译法与卡片）。
- 同一术语全书只注一次（首次出现处）；后续复用写 `\yizhu{同 §I.1 注。}{I：本工程 glossary}`。

## 5. 公式与交换图

```latex
\begin{equation}\label{eq:I.2.1}
  \Bun_G(E) \xrightarrow{\ \sim\ } \bigl[G(E)\backslash G(\AA_E)/K\bigr]
\end{equation}
```
- 编号：原文 `(2.1)` 之类**保留原编号文字**，label 用 `eq:I.2.1` 便于对齐。
- 多行：`align` + `\label` 每行。
- 交换图：`tikz-cd`，节点即公式，箭头标原文字（如 `\ar[r,"\sim"]`）。**不许截图代图**。
- 花体、德文尖角体：用 `\mathcal`、`\mathfrak`；原文字体不确定就渲染图像看，别猜。

## 6. 脚注与引用文献

- 作者原脚注：`\footnote{...}`，**保留原序号顺序**，内容照译；脚注里含文献引用时保留 `[Far16]` 式标签。
- 文献表：`sections/back-bibliography.tex`，保持原 `[键盘标签]` 与条目原文（作者、题名、期刊、年份）
  **不译题名**（书目条目保留英文），只可加译注说明。
- 正文引用 `[Far16]` 原样保留，不要改成 `\cite`（避免重编号）。

## 7. 编译检查

```bat
cd 源码
build.bat check sections\s01-chI-1.tex a   :: 产出 _check_a.pdf，0 error 才算过（末尾 a/b/c 是并行标签，别和同伴撞）
build.bat                                   :: 整书两遍
```
日志看三样：`! ` 报错、`Undefined control sequence`、`Missing character`。

## 8. 常见坑（本工程已踩过）

1. `\AA` 会被 LaTeX 占用（Å），preamble 已 `\renewcommand`，直接用即可。
2. 中文与数学之间要空格：`设 $G$ 为约化群`（不是 `设$G$为`）。
3. `ctex` 下 `\chapter*` 不会进目录，需要 `\addcontentsline`。
4. 译注里的 `%`、`&`、`_`、`#` 必须转义，否则编译炸。
5. 长公式用 `align` 拆行，别硬塞一行导致 Overfull。
6. 图片一律 `figures/` 下 PNG，文件名英文小写连字符；图注末尾标「（原文 p.N）」。
7. **`.bat` 文件必须 CRLF 行尾**。用 UTF-8 + LF 存盘，cmd 会把 `set PATH=%MIKTEX%;%PATH%` 之后的行吃掉，报 `'it' is not recognized`／`'fail' is not recognized` 这种鬼话。改 build.bat 后先跑一次 `build.bat check` 验证。
8. `build.bat check <file> <tag>` 的 tag 用于并行：三个人同时编译时各用 a/b/c，产物是 `_check_a.tex/_check_a.pdf`，互不覆盖。没有 tag 时退回 `_check.*`。
9. Windows/MSYS 里调批处理：`MSYS2_ARG_CONV_EXCL='*' cmd /c 'build.bat check sections\s01-chI-1.tex a'`（否则 `/c` 被当成路径）。
