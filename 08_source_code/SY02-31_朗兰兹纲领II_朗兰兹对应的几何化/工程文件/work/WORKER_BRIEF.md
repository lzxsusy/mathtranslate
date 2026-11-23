# worker 工作说明（SY02-31）

工程根目录（下称 `$P`）：

`C:/Users/admin/Desktop/数译发布/gitee_shuyi/08_source_code/SY02-31_朗兰兹纲领II_朗兰兹对应的几何化`

你的任务：把分配给你的底本 PDF 页范围，**全文**译成中文 LaTeX，写入分配给你的 `源码/chunks/ch-aX-YY.tex`。不删节、不概括、不写「略」。

## 先读这四样（按顺序）

1. `$P/工程文件/work/STYLE_GUIDE.md` —— 排版体例，硬性规则，逐条遵守。
2. `$P/源码/chunks/ch-a1-00.tex` —— 样板（第 1 篇开头），模仿其结构、语气、密度。
3. `$P/工程文件/work/glossary.tsv` —— 术语表（`english ⇥ 中文 ⇥ 等级 ⇥ 依据 ⇥ 首现`）。用 grep 搜你遇到的术语；表里没有的，按 STYLE_GUIDE §6 处理。
4. 原文与页面图：
   - 文本：`C:/Users/admin/Downloads/lp2_work/pages/pNNN.txt`（三位数页号，一页一文件）
   - 图像：`C:/Users/admin/Downloads/lp2_work/png/pNNN.png`（140dpi，用 `read_image` 工具看；**公式必须回图核对**）

## 硬性要求

- 每页**开头**放 `\ysrc{印刷页码}`，印刷页码 = PDF 页码 − 13。页锚放在段落之间或节标题前，不放在行文中。
- 若你的范围从某篇的标题页开始（如 PDF 52、138、180、434、484）：开头写
  ```latex
  \chapter{该篇中文标题}
  \ysrc{印刷页码}
  \begin{center}{\small\itshape 作者名}\end{center}
  \medskip
  \noindent\textbf{摘要.} ……（译原文 Abstract）
  ```
  再接目录、正文；作者名的英文拼写在标题页上，中文名按译名惯例（无惯例者保留原文）。
- 定理类用 `\begin{thm}{原文编号}` 等环境（见 STYLE_GUIDE §3），编号照抄原文。
- **不要用 `\cite`**：正文引用照原文写 `[FS21]`、`[Hel20b, §4]`。参考文献条目保留英文，`References` 标题译「参考文献」，环境用 `\begin{refs}\item … \end{refs}`。
- 图：能用 `tikz-cd` 重绘的交换图就重绘；复杂图用 STYLE_GUIDE §4 的占位框，并在回报里逐条列出「p.XX 图未重绘」。
- 底本笔误：正文照原，脚注 `\tn{…}` 说明，不悄悄改。
- 只写你这一个文件。**不要编译**（我统一编译）。**不要改** glossary、preamble、main.tex 或别人的 chunk。

## 写文件的方式

用 `write` 工具直接写 UTF-8 文件（不要用 heredoc / PowerShell 重定向，Windows 控制台 GBK 会炸）。
内容长就一次写完整文件；不要写一半就停。写完用 `ops_inspect_local_file` 抽查首尾各 20 行，确认没有截断、没有 markdown 代码围栏（` ``` `）混进 tex。

## 回报（最后一条消息）

1. 目标文件路径 + 覆盖的 PDF 页 / 印刷页范围；
2. 疑点清单：术语（表里没有的）、可疑记号、疑似笔误、未重绘的图（逐条）；
3. 任何没解决的问题。
