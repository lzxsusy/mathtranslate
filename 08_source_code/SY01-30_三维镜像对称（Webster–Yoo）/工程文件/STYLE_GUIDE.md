# 风格指南 · SY01-30《三维镜像对称》中译注本

> 本工程服从 `04_playbook/01_数学文献翻译纪律.md` **v2.1** 与 `01_corpus_zh/数语规范/`（README + STYLE_NL + STYLE_FORMAL）。
> 本文件只写这部书的具体约定；与《纪律》冲突时以《纪律》为准。

## 0. 身份与目标

原文：Ben Webster, Philsang Yoo, *3-dimensional mirror symmetry*, arXiv:2308.06191v1，Notices of the AMS 科普型综述，正文 23 页。

读者：懂代数几何/辛几何基本语言、但不做 3d QFT 的数学研究者（研究生三年级以上）。
目标文本：**读起来像一篇中文数学综述**，不是逐词对照；数学正确性 > 术语一致 > 可读性。

这是一篇**综述/科普**，不是专著：作者用「房子与密道」的比喻讲研究史。译文要保留这个语气和比喻，不要改成教科书腔，也不要为了「严谨」把作者的第一人称改成无人称。

## 1. 文体

- 书面语；原文 *we* 译「我们」（作者确实在提出主张），*one* 视语境译「人们」或「我们」。
- 保留原文段落切分；一句太长允许断成两句，但不得丢逻辑连接词（Thus / Hence / In particular / However / Of course / After all 必须显式译出：因此／于是／特别地／然而／当然／毕竟）。
- 比喻与口语化表达（dark mansion、secret passage、treasure hunt、x-ray specs、bon mot）**照译**，可加引号；不要删成平铺直叙。
- 禁止网络语、感叹号；中文标点全角（，。；：「」）。
- 脚注全部译出；Wiles 那段英文引语照译并注明「——Andrew Wiles」。

## 2. 术语

- 一律以 `工程文件/work/glossary.tsv` 为准；表外术语按学界通行译法，首次出现给「中文（English）」，并在交付说明里列出。
- 人名、定理名、软件/语言名不译：Webster、Yoo、Springer、Slodowy、Nakajima、Koszul、Hilbert、Fukaya、Langlands、Betti、de Rham、Kähler、Calabi–Yau、Hitchin、Verma、Weyl、Dynkin、Cartan、Jordan、Clue（桌游名，译「《妙探寻凶》」并给英文）。
- 复合词中心词后置：symplectic resolution → 辛消解；quiver gauge theory → 箭图规范理论。
- 缩写首次出现给全称：TQFT（拓扑量子场论）、QFT（量子场论）、SUSY（超对称）、BFN。
- 中文与拉丁字母之间**不加空格**（`Koszul对偶` 除外——按数语规范 §3，拉丁词与汉字直接相连；但 `Koszul 对偶` 这类「人名+汉字」在本库既有译文里保留一个半角空格，本工程从既有习惯，写作 `Koszul 对偶`、`Springer 消解`）。
- 数字与公式：原文 "3-dimensional" 在标题/术语中译「三维」，正文中 "3d" 译「三维」。

## 3. 数学排版

- 公式、编号、环境一律照原文：定理/命题/定义/例/注/问题/猜想用 preamble 已定义的环境（`theorem`、`proposition`、`definition`、`ex`、`note`、`ques`、`conjecture`、`physics`），**不要手写编号**，自动编号与原文一致（每节内连续）。
- 只允许使用 `源码/preamble.tex` 里定义的宏（`\C \R \Z \fM \XA \XB \XS \rkone` 等）与 amsmath/amssymb/mathtools/bm/tikz/tikz-cd/tqft 的标准命令；**不得新增 `\newcommand`**。
- `tikzpicture` 块、`wrapfigure` 块：原样保留（只译节点文字与图注）。`wrapfigure` 里的图若比 `\linewidth` 宽（中文版实测 21.8pt），用 `\resizebox{\linewidth}{!}{...}` 包住 `tikzpicture`，不改图本身的比例参数。
- 长行内公式在定理陈述里超出 `\linewidth` 时，改成行间公式（`\[ ... \]`），不改数学。
- 引用一律保留 `\cite{...}`（含可选参数如 `\cite[\S 3]{BLPGco}`），key 不改。
- `\label`/`\ref` 保留原名（不改 key），`\ref` 的显示文字由 LaTeX 生成。
- 原文 `\maybelater{...}` 是作者留白（宏体为空 ⇒ **原文 PDF 不印**），整段删除；删除后在 `资料卡/04-术语文献勘误.md` 登记「原文哪一节没印、主旨是什么」，便于日后补译。实测有两处：§2.5 整节、§5 整节。
- 原文 `\phil{...}` / `\ben{...}` 是作者给合作者的内部批注（`fixme` 宏），**不译、不保留**。
- 只有原文印出的内容才进译文；不要用「作者写了但没印」的段落给译文加料。判断依据：拿 `work/sy0130/orig/main.pdf` 的实测页与文本比对。

## 4. 译注（`yizhu` 环境）——每节 0–2 条

只在这三种情形写，每条 1–3 句：
1. **术语/背景**：读者可能不熟的概念（如「辛消解」「BNF 空间」「稳定包络」）给最小必要解释，可引原文文献标签。
2. **原文省略**：作者写 "it can be shown" 而不展开——指出「原文未展开」，**不得**补证明冒充原文。
3. **原文笔误/记号冲突**：明确写「译者按：原文此处……，疑为……之误」。

禁止把译注写成小论文；禁止在译注里引入原文没有的定理。

## 5. 数学内容

- 一切数学陈述照原文；发现原文错误时译文照译，紧随其后加译注说明。
- 原文的 "Physics Motivation" 环境译「物理动机」，保留其编号。
- 公式里的英文单词（如 `\mathrm{rk}`、`\operatorname{Spec}`）不译。

## 6. 编译与文献表

- 命令：`xelatex main.tex` → `biber main` → `xelatex main.tex` ×2。不要在仓库里留 `.bbl`（.gitignore 已忽略），文献表由 `源码/main.bib` 经 biber 重建。
- `main.bib` 是 2026-11-22 从 arXiv 随文 `.bbl`（format 3.2）反推的 30 条；原包不带 `.bib`。若上游将来给出 `.bib`，以它为准、重跑 biber。
- 编译自检：`0 error`、`0 overfull`、`0 undefined`；页数与 BRIEF 的结构表对得上（正文 24 页 + 扉页/说明/目录/术语表）。

## 7. 交付

- 每块 chunk 是纯正文，从 `\section`/`\subsection` 开始，不含 preamble、不含 `\begin{document}`。
- chunk 末尾加一行注释标明对应原文页码范围：`% [原文 p4–p7]`（按 PDF 页；页眉页码见 BRIEF §2）。
- 交付前自检：① 每个 `\begin{...}` 都有配对 `\end{...}`；② 没有未译的英文整句（公式、人名、术语括号内英文除外）；③ 所有 `\cite` key 与原文一致；④ 没有新增宏。
