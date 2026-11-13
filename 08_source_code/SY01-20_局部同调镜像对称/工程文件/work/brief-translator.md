# 译手施工 brief（LHMS 中文译注本）

## 0. 项目

把 arXiv:2611.07202v1《Local Homological Mirror Symmetry》(Si-Yang Liu, Kyungmin Rho, 56 页)
译成中文译注本。项目根：`<本地路径>`。Lead 已完成：导言区
`src\preamble.tex`、前置件 `src\front\s00-front.tex`、样板章 `src\chunks\ch00.tex`、
施工规范 `work\style.md`、术语表 `work\terms_zh.tsv`、页码锚点 `work\page_start.json`。
你负责把分给你的 chunk 从英文译成中文，插入译者批注，并保证单独编译干净。

## 1. 必读（按顺序）

1. `src\chunks\ch00.tex`——**样板章，文风/批注体例照它写**。
2. `work\style.md`——总规范（本 brief 是它的执行版）。
3. `src\preamble.tex`——可用的宏与三个方框环境。
4. `work\terms_zh.tsv`——**术语唯一标准**，凡表中有的必须用表里的译法。
5. `src\chunks\_src\<ch>_src.tex`——你的原文，每 20 行有 `%% ---- 原文行 N ----`
   标记，行号对应 `_work\arxiv_src\main.tex`。
6. `work\pagemarks\<ch>.txt`——该 chunk 内的原文页起点（页号、源行号、该行开头文字）。
7. `work\concepts_library.md`（若已存在）——概念框素材库；不存在就自己写。

## 2. 你只能写这些文件

- `src\chunks\<ch>.tex`（你名下的 chunk，一个文件一个 chunk）
- `work\reports\<你的名字>.md`（完成报告）
- `work\reports\<你的名字>-terms.tsv`（你新造/修正的术语，只有新增时才写）

**不要**改 preamble、main.tex、别的 chunk、work 下公共文件。不要 `git` 操作。

## 3. 数学与结构：原样

- 所有公式（`$...$`、`\[...\]`、`equation`、`align`、`tikzcd`、`tikzpicture`）
  **逐符号照抄**，只把 `\text{...}` / `\mathrm{...}` 里的英文词换成中文（必要时）。
- 环境名、`\label{...}`、`\cite{...}`、`\ref`/`\eqref` 原样保留。定理编号由计数器自动生成，
  你的 chunk 单独编译时编号会从 1 开始，这没关系；**不要手动写编号**，不要用 `\tag`。
- 原稿笔误不要改（如 "gi ve"、"compatification"）：照原意译，必要时用 `yizhu` 提示。
- 原文里被 `%` 注释掉的旧稿不在你的 `_src` 里（已剔除），不要翻译。
- 段落切分基本照原文；原文一个 `\subsection` 一个小节，标题用 `\subsection{...}`。
- 图（`figure`）代码整块保留，`\caption` 译成中文；图内 `\node` 里的英文标签译成中文。

## 4. 中文文风

- 全角标点（，。；：？！）；引号一律「」，不用英文双引号（脚本最后会检查：ASCII `"` 必须为 0）。
- 中文与英文术语/数字之间留**一个半角空格**：`Weinstein 扇形`、`56 页`、`A∞-函子`。
- 行内公式后的句末标点放在公式**后面**：`……满足 $f=g$。`
- 不用病灶句式：「被……所」「进行……的」「对于……而言」「起到……的作用」。
- 术语首现：`中文（English）`，之后只用中文；Fukaya、Weinstein、Künneth、Floer、
  Gromov–Witten 等专名保留英文。
- 不要音译；通行译名优先。
- 译的是论文正文，不是摘要：不省略、不改写、不合并句子导致信息丢失；长句可拆，但逻辑关系
  （因此/然而/事实上）必须保留。

## 5. 三类批注（正文中穿插）

**(a) 译注** `\begin{yizhu}[短标题] ... \end{yizhu}`
- 每个 chunk **至少 2 条**，每条 2–5 句、60–200 字。
- 只写三类内容：易错预警（符号/方向/左右侧易搞反）、含糊处点拨（原文没展开的一步）、
  背景直觉（为什么这么做）。**禁止**空话（"这很重要"）、禁止复述正文。

**(b) 概念回顾** `\begin{conceptbox}{概念名} ... \end{conceptbox}`
- 每个 chunk **至少 1 个**，放在该概念**首次出现处之后**。
- 结构：3–6 句讲清定义 + 直觉 + 本文为什么需要它；最后一行
  `参考：nLab, <条目名>；<文献>.`（取自 `work\concepts_library.md`；自己写的必须给真实可查来源，
  不确定就只写 "参考：nLab, <条目名>" 并在报告里标注待核）。
- 同一概念全书只放一次：你 chunk 里若已在 ch00 或别处出现过（ch00 已有 HMS、局部镜像对称、
  Weinstein 扇形与包裹 Fukaya 范畴、扇形下降与真下降），不要重复放。

**(c) 本节重点** `\begin{keytakeaways} \item ... \end{keytakeaways}`
- 每章/每大节末尾 1 个即可（2–4 条），不是每个 chunk 必须有；chunk 是半节就留给后半的人。
- 标题固定「本节重点（译者所加）」，写"这一节建立了什么、为什么需要、下游怎么用"。

## 6. 页码注释

在 `work\pagemarks\<ch>.txt` 列出的每个页起点处，在**最近的段落边界**插入一行：

```
% [原文 p.23]
```

（源行号只作定位参考，不必精确到行；一段之内偏差可接受。）

## 7. 编译自检（必须做）

在 `<本地路径>` 下建 `<ch>_test.tex`：

```latex
\input{../../src/preamble.tex}
\begin{document}
\input{../../src/chunks/<ch>.tex}
\end{document}
```

然后在该目录执行两遍：

```
xelatex -interaction=nonstopmode <ch>_test.tex
```

要求：**0 个 `!` 错误、0 个 Overfull \hbox、0 个 Missing character**。
（`[?]` 引用未解析是正常的，不要跑 bib。）
Overfull 常见原因：长公式行、长英文术语、`tikzcd` 太宽——优先微调中文措辞/断行，
必要时在公式里加 `\!` 或 `\begin{split}`，不要 `\sloppy`。
Missing character 常见原因：生僻符号——查 `preamble.tex` 是否已有对应宏。

PowerShell 控制台看中文可能乱码，日志细节用 read 工具读 `.log`。

## 8. 报告（完成后立即 send_message 给 lead）

`work\reports\<你的名字>.md` 里写：
1. 完成/未完成的 chunk 与页数；
2. 编译结果（错误数、overfull 数）；
3. yizhu / conceptbox / keytakeaways 各自条数；
4. **存疑清单**：原文可疑处（笔误、指代不明、公式与文字不符）、你拿不准的译法；
5. 新增术语（也写进 `-terms.tsv`）。

消息里给 3–5 行摘要 + 报告路径即可。遇到**数学上无法确定**的地方，宁可保留英文并记入存疑，
也不要猜。
