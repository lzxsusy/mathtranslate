# STYLE_GUIDE — SY05-30

本卷的排版与行文体例。与 `04_playbook/01_数学文献翻译纪律.md` 冲突时，以《纪律》为准；本文件只写本工程的具体做法。

## 1. 文件与编译

| 文件 | 作用 |
| --- | --- |
| `源码/main.tex` | 主文件：类、宏包、字体、定理环境、记号宏、`\inputif` |
| `源码/chapters/titlepage.tex` | 扉页 |
| `源码/chapters/preface.tex` | 译者说明（底本、范围、页码对照、体例、存疑） |
| `源码/chapters/foreword.tex` | 原书编者前言译文 |
| `源码/chapters/guide.tex` | 全书导读（据前言与各章导言写成，**非译文**） |
| `源码/chapters/ch02a…ch02j.tex` | 第 2 章译文，按原书小节切块 |
| `源码/chapters/bib.tex` | 第 2 章参考文献 [1]–[20] |

- 引擎 xelatex；`ctexbook[a4paper,11pt,openany]`；中文字体 Noto Serif SC / Noto Sans SC。
- 编译三遍（交叉引用 + 目录）；验收：`grep -c '^!' main.log` 为 0、`grep -c Overfull main.log` 为 0。
- **插图**（2026-11-24 定）：**交换图一律 TikZ 重画**（`tikzcd`，标签规则见上）；**示意图不重画**，从底本 PDF 按 300 dpi 裁切存为 `源码/figs/f<章>-<两位图号>.png`，正文用 `\includegraphics[width=<原宽 pt × 1.1>]{figs/f1-01}`，图注仍用中文译文，编号由 `figure` 环境自动推进（不再用 `\figomit`、不再手工 `\setcounter{figure}`）。已裁 42 张：第 1 章 1.1–1.28、第 3 章 3.1–3.13、第 4 章 4.1；第 2 章样张无 `figure` 环境，其行内交换图保持 TikZ。
- `Underfull \hbox` 的处理分三级（2026-11-24 定，四次实测后的结论）：① badness ≥ 5000 必须改写正文（通常是段落里夹了一个不可断的长数学串，改词序或把式子挪到独立显示即可）；② 1000–3500 属轻微松散，preamble 用 `\hbadness=3500` 不再报警，不改正文；③ `Underfull \vbox`（页底拉伸）由 `\raggedbottom` 统一消除。报警门槛的改动必须记在本文件与 `work/进度.md`，不许静默调参。
- `main.pdf` 是本地构建产物，不入仓（`.gitignore` 已覆盖 `源码/main.pdf`），预览图放 `成品/预览/`。

## 2. 文件名与切块

- 一章可跨多文件，命名 `ch<章号><字母>.tex`（`ch02a`…`ch02j`），字母序即正文顺序；切块点落在小节或定理之间，不切在环境内部。
- 每个 `ch*.tex` 文件**只写自己的内容**：不写 `\documentclass`、不写 `\newcommand`、不写 `\section`（章内小节用 `\section`，但**只在 `ch02a.tex` 里写本章的 `\chapter` 与各 `\section`**；其余文件从 `\subsection` 或正文续写）。
- 新增宏只在 `main.tex` 加，且必须能说明为什么现有宏不够用。

## 3. 编号

- 定理类环境编号 = `章.节.序号`，由 `\newtheorem{theorem}{定理}[section]` + `\renewcommand{\thetheorem}{\thesection.\arabic{theorem}}` 自动生成；**手工核对**与原文一致（原文 Definition 2.1.1 ↔ 译文 定义 2.1.1）。
- 公式：`\counterwithin*{equation}{chapter}`，手写 `\tag{2.13}` 与原文对齐；续写同一编号的公式用 `\tag{}` 重复。
- 习题用 `exercise` 环境，编号即原书 2.1.17 之类。
- 交叉引用一律 `\label` + `\ref`；引用原文编号时写「命题 2.2.4」这类中文，不写 `\ref`（那是引用译文自己的标签）。

## 4. 术语

- 首现「中文（英文）」，此后只用中文；英文首现加括号、不斜体。
- 术语表 `work/术语表.tsv` 是唯一权威，五列：`en`、`zh`、`依据`、`首现处`、`备注`；依据用 A（权威工具书/原书自注）、B（nLab/Stacks/ProofWiki 交叉核对）、I（本库既有译法或底本自身约定）。
- 专名保留大写：**Real 黎曼面**（Atiyah 意义）、**Klein 曲面 → 克莱因曲面**（人名译音，术语表中另立 Klein 瓶 = 克莱因瓶）。
- 不造词：拿不准就查 `kb_search` 看本库既有译法，再查 A 级来源。

## 5. 数学写法

- 公式逐符号对照页面图像录入；文本层不可信（连字 ﬂ/ﬁ、重音私用编码）。
- 集合记号 `\{x\}`、`q^{-1}(\{x\})` 不简写为 `q^{-1}(x)`（原文如此，照录）。
- 反群、半直积、增广一律写全：`G^{\mathrm{op}}`、`\rtimes_\alpha`、`\Hom_{\Z/2\Z}`。
- 箭头：`\curvearrowright`（↷ 左作用）、`\curvearrowleft`（↶ 右作用）、`\rtimes`、`\xrightarrow{\ \simeq\ }`。
- 交换图用 `tikz-cd`；标签里**不要出现 `|`**，需要限制记号时写 `\restr{\rho}{\pi_1(X;x)}` 或下标形式；箭头交换标记只写一个 `'`，写成 `"label"'`，不要 `"label"''`（这两个坑各踩过一次，见校订日志 2026-11-24）。

## 6. 译注

```latex
\begin{annote}
原文此处作「…」，与上下文不合；按本意应为「…」。译文按后者写出（参见疑点清单 Q005）。
\end{annote}
```

- 只写三类：原文笔误、原文自相矛盾、术语需要交代来源/约定的地方。
- 每条译注必须能追到 `work/疑点清单.tsv` 的编号；不写「译者认为」这类无来源判断。
- 原文正确而只是难读的地方，**不**加译注；难读是读者的事，不是译者的。

## 7. 中文行文

- 长句拆开；「我们」照原文用，不改成「笔者」。
- 原文的 italics 强调 → 中文用「」或 \emph{}，不都用黑体。
- 数字与英文之间留半角空格（`41 页`、`PDF 页 77`）；中文标点全角。
- 脚注照译，脚注里的文献引用照录。
