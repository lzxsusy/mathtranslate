# SY02-31 译文风格与 LaTeX 体例（worker 必读）

本文件是《朗兰兹纲领 II：朗兰兹对应的几何化》中文译注本的硬性排版规则。样板：`源码/chunks/ch-a1-00.tex`。译者说明：`源码/front/translator.tex`。

## 1. 文件与范围

- 只写分配给你的那个 `源码/chunks/ch-aX-YY.tex`，不改别的文件，不编译（统一编译）。
- 覆盖分配给你的 PDF 页范围内的**全部**内容：正文、定理、注、例、公式、脚注、图表标题、参考文献条目。不删节，不概括，不写「略」。
- 页边界处被截断的句子照译到页末即可；下一片从下一页开头接着译。
- 译文用简体中文。人名、地名、机构名保留原文（Langlands、Fargues、Scholze…）；已成惯例的（Weil 群、Hecke 算子）照惯例。

## 2. 页锚（必须）

每个 PDF 页的**起始处**放一个 `\ysrc{印刷页码}`。印刷页码 = PDF 页码 − 13（第 1 篇从印刷页 3 起）。
例：PDF 第 18 页 → `\ysrc{5}`。
页锚写在段落之间或节标题之前，不要写在段落中途；不要重复。

## 3. 结构

- 篇标题（只有第 1 片需要）：`\chapter{中文标题}`，下一行 `\ysrc{3}`，再 `\begin{center}{\small\itshape 作者名}\end{center}`。
- 节：`\section{标题}`、`\subsection{…}`、`\subsubsection{…}`。编号自动按篇内 1,2,3… 与原文一致（preamble 已设 `\thesection=\arabic{section}`）。
- 原文的 `\begin{theorem}`/`Proposition`/`Lemma`/`Corollary`/`Definition`/`Remark`/`Example`/`Question`/`Conjecture`/`Notation`/`Hypothesis`/`Fact`/`Problem`/`Claim` 一律用带编号参数的环境：

```latex
\begin{thm}{1.2.3}
…\label{thm:dat-1-2-3}
\end{thm}
\begin{proof} … \end{proof}
```

可用环境名：`thm prop lem cor conj defn rem exam ques claim notn hyp fact prob`，编号照抄原文（含篇内编号，如 `{2.4.1}`）。原文没有编号的定理式段落用 `\begin{thm}{}`（空编号会显示「定理.」，因此**不加编号的场合改用** `\begin{rem}{}` 不合适——此时直接写 `\textbf{定理.}` 起段）。
- 证明结束自动加 □；原文自带证毕符号的删掉。
- 原文的 `Acknowledgements` → `\section*{致谢}`；`References` → `\section*{参考文献}` + `\begin{refs} \item … \end{refs}`。
- 附录：`\section{附录 A. …}`（原文 "Appendix A" 保留字母编号，不改成数字）。

## 4. 公式

- 行内 `$…$`，行间 `\[ … \]`，多行对齐 `align*`/`align`（原文有编号的用 `align` 并 `\tag{2.4.3}` 保留原编号）。
- 公式必须逐符号核对页面图像（`read_image` 读 `png/pNNN.png`），特别是上下标、花体、帽子、双线体、$\ell$ 与 $1$、$p$ 与 $\rho$。
- 交换图：简单者用 `tikz-cd` 重绘；复杂或含大量对象者，用

```latex
\begin{center}
\fbox{\parbox{0.8\textwidth}{\centering\small 图（底本 p.\,XX）：<一句话说明图的形状>}}
\end{center}
```
并在回报里说明「p.XX 图未重绘」。
- 底本笔误：正文照原样，另加脚注 `\tn{底本此处作 ……，疑为 …… 之误。}`，不悄悄改。

## 5. 引用与文献

- **不要用 `\cite`**。正文中的方括号引用照抄原文：`[FS21]`、`[Hel20b, §4]`、`[Zhu25, Theorem 1.2]`。
- 参考文献条目保留英文原貌（作者、标题、刊名、卷、页码、DOI、MR 号），只把标题 `References` 译成「参考文献」。条目里不翻译标题。

## 6. 术语

- 以 `工程文件/work/glossary.tsv` 为准；同一术语全篇一致。
- 首次出现时括注英文：`凝聚层（coherent sheaf）`；此后不再括注。
- 禁音译、禁生造词。遇到术语表里没有的词：按字面义直译并在回报里列出（我会补进术语表），不要自己造一套。

## 7. 语言纪律

- 避免「被……所」「进行……的」「对于……而言」；长句按中文语序拆分，但保留原文的逻辑连接（因此、然而、特别地）。
- 数学陈述用陈述语气，不写「我们可以看到」。
- 英文缩写首次出现给中文全称 + 缩写：`局部 Langlands 对应（LLC）`。
- 中英文之间、中文与行内公式之间不额外加空格（LaTeX 自动处理），但英文术语内部按原文空格。

## 8. 交回时回报

1. 文件路径 + 覆盖的 PDF 页 / 印刷页范围；
2. 遇到的疑点（术语、记号、疑似笔误、图）；
3. 未解决的项（我会进 `疑点清单.tsv`）。
