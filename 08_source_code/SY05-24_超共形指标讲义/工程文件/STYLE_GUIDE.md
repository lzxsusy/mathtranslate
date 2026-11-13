# STYLE_GUIDE.md — SY05-24 中文译注本硬规范

> 本文件是**强制**规范。与 `BRIEF.md` 冲突时以本文件为准；本文件没说的，跟 `工程文件\底本_arXiv-2006.13630.pdf` 的样子走。

## 1. 文件格式

- 只写 `源码\` 下分配给你的块文件；UTF-8 **无 BOM**、**LF** 换行。
- 禁写：`\documentclass`、`\usepackage`、`\section`、`\newtheorem`、`\newcommand`（特殊见 §8）、`\tableofcontents`、`\begin{document}`。
- 禁写 Markdown：`**粗体**`、`# 标题`。
- 数学环境外不写 Unicode 数学符号（`α β γ ≤ ≥ → ∞`），要用 `$\alpha$` 等。
- 中英文之间不强行加空格；标点用全角（，。；：、？！），括号内若纯英文/公式可用半角。
- 一个自然段 = 源码里一行（长行不折），段间空一行。

## 2. 页标记

在每页译文起始处单独一行写：

```latex
% [原文 p.7]
```

- 页码用 **PDF 页序**（1–32），与 `工程文件\pages\pNN.png` 的 NN 一致；不是印刷页码。
- 每页都要有；页首若是接续段落，标记放在该段之前。
- 标记只是注释，不产生输出。

## 3. 公式

- 行间公式一律 `\[ … \]`，编号用 `\tag{1.12}` 放在 `\[ … \tag{1.12}\]` 内。**不要** `equation`/`align` 环境。
- 编号必须与原文一致、**一条不少、一条不多**；号是 (节号.序) 形式。
- 多行对齐公式用 `\begin{aligned}…\end{aligned}` 套在 `\[ \]` 里，整体只打一个 `\tag`。
- 正文引用写：「式 (2.14)」「由 (1.7) 可得」，**不用** `\eqref`/`\ref`。
- 文字层不可信的：分式、上下标、矩阵、`\not=`、`\sim` 与 `\simeq`、`\pm`、根号、`\langle\rangle`、`\Big` 括号。这些必须对页面图。
- 常用宏（preamble 已定义，直接用）：`\sN \sI \sU \sV \Tr \Sym \adj \fund \PE \Li \eps \dd \ee \ii \ol \br \dg \half \third \R \C \Z \Q`；其它按标准 LaTeX 写。

## 4. 编号环境

原文的编号定义/习题/例等，一律用带可选参数的环境，手工给号：

```latex
\begin{exercise}[2.3]
...
\end{exercise}
```

可用环境与用途：

| 环境 | 对应原文 | 备注 |
|---|---|---|
| `exercise` | Exercise 1.1 … | 8 个，编号照原文 |
| `definition` | Definition | 原文若有 |
| `example` | Example | |
| `theorem` / `proposition` / `lemma` / `corollary` | 同名 | |
| `remark` | Remark / 作者的小注 | |
| `solution` | 习题解答（若有） | 原文一般紧接习题 |

- 环境名用英文命令，**输出标题是中文**（preamble 已设好）。
- 不编号的旁注用 `remark` 不带参数即可（preamble 里 `\newtheorem*` 支持无号）。
- 环境与公式号无关，不要混用计数器。

## 5. 表格

- Table 1（p10）、Table 2（p13）必须复刻：`\begin{tabular}{...}` + `booktabs` 风格横线（`\toprule\midrule\bottomrule`）。
- 列宽用 `C{2.2cm}` 形式（preamble 已定义 `C` 列类型，居中式定宽）。
- 逐格对照 `pages\p10.png` / `pages\p13.png`，**文字层里每格是单独一行、顺序被打乱，不能直接抄**。
- 表题写在表格上方：`\textbf{表 1.} N=1 手征多重态的 letters 及其对指标的单字母贡献`（原文 Table 1 无 caption 则不加，只保留表体；以页面图为准）。
- 表内数学照 §3 规范。

## 6. 术语与人名

- **先查 `glossary.tsv`（215 条，冻结）。** 表里有的必须照用，不得自创译名。
- 表里没有的：按惯例译，首次出现给「中文（English）」，如「齐次指数（plethystic exponential）」；并在回报里列「新增术语建议」，由 Lead 入表。
- 人名一律保留拉丁拼写：Witten、Gadde、Seiberg、Cardy、Schur、MacDonald、Killing、Cartan、Weyl、Haar、Vandermonde、't Hooft、Bekenstein、Hawking、Atiyah、Singer、Chern、Simons、Yang、Mills、Kähler、Grassmann、Planck、Newton。
- 缩写（OPE、BPS、SYM、CFT、SUSY、TQFT、QCD、AdS）照原文保留，首次出现给中文全称。
- `$\sN=2$` 走宏，不写 `\mathcal{N}`。

## 7. Tutor Note

- 只在真有价值处加，四种类型：
  1. 术语：为何这样译、与另一译法差别；
  2. 物理动机：这一步在算什么、为什么这么定义；
  3. 易错点：符号约定（如 $(-1)^F$、$\Tr$ 的符号加权）、指标 vs 配分函数的区别；
  4. 文献对应：与 Witten 1982、Kinney–Maldacena–Minwalla–Raju、Romelsberger 等工作 的对应。
- 形式：独立成行，以 `% [Tutor Note: …]` 起（注释不进入 PDF），或需要进 PDF 时用 `remark` 环境。
- 单条 ≤ 3 行；每块 ≥ 8 条。

## 8. 数学写法细则

- 对易子：`[A,B]`；反对易子：`\{A,B\}`。
- 迹：`\Tr`（已定义为算符字体）；不要写 `Tr`。
- 集合：`\R`、`\C`、`\Z`、`\Q`；不要 `\mathbb`。
- 虚数单位 `\ii`，微分 `\dd`，指数 `\ee^{…}`，共轭 `\ol{…}`（均已定义）。
- 多重指标/希腊字母按原文；`\sN` 是超对称数记号的宏。
- 分式优先 `\frac`；行内小分式用 `a/b`；不要 `\dfrac`（行间已够大）。
- 矩阵用 `pmatrix`/`bmatrix`；长等号对齐用 `aligned`。
- 需要新宏：优先用现成宏拼；确实需要时在 `preamble.tex`「追加区」末尾加 `\newcommand`，并在回报中列出（**不要**在块文件里定义）。

## 9. 交付前自检

1. `check_block.py` 输出 `OK`（tags/env 数对得上、无禁用命令、无 BOM/CRLF）。
2. 公式号首尾与 `TIMELINE.md` 一致；逐页对照「本页应有号」。
3. 每页都有 `% [原文 p.N]` 标记；页序无跳号。
4. 表格逐格复核过页面图；习题号齐。
5. 通读一遍中文：无英文残留（人名/缩写/术语首现英文除外）、无「的的」、无未翻译的整句。
6. 疑点全部落成批注 + 回报「未决」清单。

## 10. 回报格式

```
[块 c0X 完成] 文件 sec1a.tex | tags 17/17 | env 0/0 | 批注 11 条 | 行数 412
未决：…
新增术语建议：…
批注分布：术语 4 / 动机 3 / 易错 2 / 文献 2
```

一段话即可，不要贴代码、不要复述原文。
