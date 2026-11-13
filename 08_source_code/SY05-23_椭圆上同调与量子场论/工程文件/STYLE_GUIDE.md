# STYLE_GUIDE.md — 硬性规范（违反即返工）

## 1. 文件格式

- 一个块一个文件：`源码/sec1.tex` / `sec2.tex` / `sec3.tex` / `sec4a.tex` / `sec4b.tex` / `refs.tex`。
- **UTF-8 无 BOM，LF 换行**。用 Python 写（`open(..., "w", encoding="utf-8", newline="\n")`），禁止 PowerShell `Out-File` / `Set-Content`。
- 只写自己的文件；不得改 `main.tex` / `preamble.tex` / 别人的块。
- 块文件里**不允许**：`\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\def`、`\input`、`\includegraphics`、`\section`、`\tableofcontents`、`\maketitle`、`\newtheorem`。
- 允许：`\subsection`、`\subsubsection`、`\footnote`、`\label`/`\ref`（尽量少用，见 §4）。

## 2. 页码与结构对应

- 每页开头写 `% [原文 p.N]`（N 为 PDF/印刷页号，从 1 起）。
- 原文的节/小节标题：`\section` 由 Lead 写在 main.tex；**小节标题必须译**，用 `\subsection{...}`；原文每个 §x.y 都是带黑体标题的段落（如 `2.1. The space of quantum mechanical theories is a K(Z, 3).`），译成 `\subsection{量子力学理论的空间是 K(Z,3)}`，编号交给 LaTeX。
- 原文的小标题段落若只是段首斜体短语，不另立结构。

## 3. 公式（最高优先级）

1. **公式只信页面图像**：`工程文件/pages/pNN.png`（200 dpi）。文字层仅用于定位，数学一律不可信。
2. 56 条编号公式全部保留，**手工编号**：
   ```latex
   \begin{equation}
     ...
   \tag{12}
   \end{equation}
   ```
   多行用 `align`，同一个号只出现在最后一行（若原文每行都有号则逐行 `\tag`，与原文一致）。同一号下多式并列用 `\qquad` 分隔。
3. 编号必须与原文**逐条一致**：不重、不漏、不自造。块内公式号清单见 TIMELINE；交稿前 `check_block.py` 会核对。
4. 正文引用公式写纯文本「式 (12)」，**不用 `\eqref`**（手工 tag 无交叉引用）。
5. 行内公式用 `$...$`；不得用 `\(...\)`。
6. 矩阵、cases、交换图：原样排版；交换图用 `\begin{CD}...\end{CD}`（preamble 已载 amscd）或 `array`，实在复杂的（TikZ 级）用 `\figomit` 式文字转述并在批注说明——不得伪造。

## 4. 编号环境（手工编号）

- 环境名 → 中文：`conjecture` 猜想、`definition` 定义、`theorem` 定理、`proposition` 命题、`lemma` 引理、`corollary` 推论、`hypothesis` 假设、`remark` 注、`example` 例、`question` 问题。
- 写法：`\begin{conjecture}[1.1] ... \end{conjecture}`，preamble 已把编号印成 `猜想 1.1`（无括号）。
- **编号严格照原文**：所有类型共用每节一个计数器（原文 1.1, 1.2, …；2.1, 2.2, …）。不得重排、不得跳号。
- 环境标题若原文带说明（`Definition 2.13 (Reflection positivity, sketch).`），译作 `\begin{definition}[2.13（反射正性，略述）]`。
- 证明原文用 `\begin{proof}...\end{proof}`。

## 5. 图与表

- 8 幅图（Figure 1–8）**一律不复刻**（重画即伪造）。在原位置写：
  `\figomit{3}{图注中译（保留 Figure 3 编号）}`
  正文中「见图 3」照译。
- 原文正文引用了 `Table 2` 但需核对是否存在实体表格；若只有引用没有表，照译并在批注中说明「原文此处引用的 Table 2 未在正文出现」。

## 6. 术语与人名

- 严格按 `glossary.tsv` 冻结译名；表里没有的新术语，第一次出现时写「中文（English）」，并**回报给 Lead** 以便补表。
- 人名、理论名、软件名、文献标签**不音译**：Witten、Stolz、Teichner、Segal、Hopkins、Lurie、Atiyah–Bott–Shapiro、Quillen、Ochanine、Landweber–Stong、TMF、K-theory、Spin、string、Ramond、Neveu–Schwarz、Wick 等保留拉丁字母（首次出现可加中文说明）。
- 参考文献条目**整条不译**（作者、标题、期刊、年份原样）。
- 数字与单位：`$n\in\mathbb Z$`；「2 维」用阿拉伯数字；`N=(0,1)`、`N=1`、`1|1` 维等记号原样。

## 7. 中文数学文风

- 陈述句，少用「我们」；「我们」只在作者原话处保留。
- 「iff」→「当且仅当」；「i.e.」→「即」；「e.g.」→「例如」；「cf.」→「参见」。
- 定理/定义内的数学照抄；连接词用中文。
- 括号：中文正文用全角（），公式内用半角。破折号 ——。
- 不写 markdown（`**粗体**` 会被原样印出星号）。

## 8. Tutor Note（批注）

- 形式：`% [Tutor Note: ... ]`，LaTeX 注释，**不进入排版**。
- 只写四类，每条必须有信息量：
  1. 可验证的易错点（给出核对方法，例如「此处 $q=e^{2\pi i\tau}$，核对 p22 式 (41)」）；
  2. 补出原文省略的论证（为什么这一步成立）；
  3. 原文笔误（给正确形式 + 判断依据），同时登记 `ERRATA.md`；
  4. 记号/术语说明（与其它文献的记号差异、物理含义）。
- 每条 ≤ 3 行；整块 ≥ 8 条；不许写「此处很重要」这类空话。
- 不确定的地方写 `% [TODO-LEAD: ...]`，并在回报里说明。

## 9. 自检（交稿前必跑）

```powershell
$env:PYTHONIOENCODING='utf-8'
$py = '<本地路径>'
& $py check_block.py sec2.tex
```
必须输出 `OK`。它会检查：公式号集合、花括号/环境配对、`$` 成对、禁用命令、BOM/CRLF、正文非 ASCII 数学符号。

## 10. 回报格式（一条消息，别写成长文）

```
[块 c02 / sec2.tex] 完成
- 范围：原文 p6–12，§2.1–§2.3
- 公式：19/19（(6)–(19)），check_block OK
- 编号环境：Definition 2.1 … Remark 2.24（共 N 个），编号已对原文
- 图：Figure 1–2 已用 figomit
- 批注：14 条；TODO-LEAD：0
- 疑问：<一句一条，最多 3 条>
```
