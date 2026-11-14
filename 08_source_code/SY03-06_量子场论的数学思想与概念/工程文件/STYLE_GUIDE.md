# 翻译工作规范（每位译者必读，逐条遵守）

## 0. 角色与目标

你是受雇于一位顶尖理论物理/数学物理学教授的专业译者兼审校。任务是把 Etingof 讲义
《Mathematical ideas and notions of quantum field theory》（arXiv:2409.03117v1）中的**一章（或半章）**
精译为可直接编译的中文 LaTeX 源码，并加学术级批注。**先读懂再评论**：批注必须建立在真实理解之上，
宁缺毋滥，绝不允许用套话充数。

## 1. 文件接口

- **权威底本（英文 LaTeX 源码，逐字可靠）**：`w2409/src_parts/pXX.tex`（分配给你的那个文件）。
  这是 arXiv 原始 TeX，公式绝对可靠；**不要**以 PDF 文本抽取结果为准。
- **你的成品**：`w2409/build/sections/secXX.tex`（UTF-8，无 BOM）。文件名按下面的分配表。
- 成品**只含正文**：不要写 `\documentclass`、`\begin{document}`、`\usepackage`、`\tableofcontents`，
  不要重复标题页与摘要。导言区、定理环境、宏都已由 `main.tex` + `preamble.tex` + `macros.tex` 备好。
- 你的分节文件会被 `main.tex` 以固定顺序 `\input`，因此**不要**改动章节顺序，也不要新增 `\section`。
- 编译：`cd w2409/build && ../.tools/tectonic/tectonic.exe -X compile --keep-logs main.tex`
  （tectonic 缓存目录用 `TECTONIC_CACHE_DIR=...\.tools\texcache`）。**你不需要反复全量编译**，
  用自检脚本即可；如要试编译，见第 6 节。

## 2. 铁律：公式与结构逐字无损

1. **所有数学内容原样保留**：`$$ ... $$`（本文大量使用）、`$...$`、`\begin{equation}`、
   `\begin{pmatrix}`、`\begin{cases}`、`\begin{gathered}`、`\begin{aligned}` 的内容
   **一个字符都不许改**：不重排、不化简、不改上下标、不改希腊字母、不改 `\left/\right`、
   不改 `\frac/\tfrac`、不改 `\!`、`\,`、`\big` 等间距命令、不改 `\rm`。
2. **绝对禁止**把 `$$...$$` 改成 `\[...\]` 或 `equation` 环境；**禁止**新增带编号的公式。
   需要译者补充说明时，只能写在 `% [Tutor Note: ...]` 注释里。
3. `\label{...}`、`\ref{...}`、`\eqref{...}`、`\cite{...}` 的**键名一律不得改动**（`\cite` 键如 `QFS`、`W`、`IZ`）。
4. 定理/引理/命题/推论/定义/例/注/习题/证明等环境：`\begin{...}` 与 `\end{...}` 成对保留，
   环境名与嵌套结构不变；环境内的正文要译。
5. 图：`\begin{figure}...\end{figure}` 块只允许翻译 `\caption{...}` 里的文字；
   `\includegraphics[...]{figures/fig-NN.png}` 与 `\label{...}` 一字不改；
   **不要**自己加 `\figorig`（主控统一添加原文页码）。
6. 原文的 `\subsection{...}` 标题要译；`{\it ...}` 译为 `\emph{...}`；`{\bf ...}` 译为 `\textbf{...}`。
7. 脚注 `\footnote{...}` 要翻译；`\begin{exercise}`（习题）是正文一部分，必须翻译，不得跳过。
8. **一句都不能删**。原文的所有段落、注、习题、过渡句都要有对应中文。
9. 原文若确有笔误（符号、指标、归一化因子可疑），**保留原样**，另用批注指出，不要擅自改正。

## 3. 翻译质量

1. **术语统一**：严格按 `w2409/glossary.md` 的译名；表中没有的，按中文学界惯例译，
   首次出现用“中文（English）”标注（全书只首次，若你不确定前面是否出现过，就只在术语表未收时标注）。
2. **学术书面语**：以中文学术论文语序重写，不逐词硬译；长句可拆；逻辑连接词
   （however / therefore / conversely / in particular / note that）必须准确传达。
   避免“让我们”“我们可以看到”这类口语；用“我们”“可见”“注意”。
3. **标点**：正文用中文全角标点（，。；：、？！（）“”——）；数学模式内保持英文标点。
   破折号用“——”，引号用“”，不用 `` ''。
4. **人名/专名**：一律保留拉丁字母（Feynman、Witten、Deligne、Berezin、Wightman、Virasoro、Morse、
   Kac、Zagier、Harer、Wigner、Hermite、Legendre、Cayley、Bott、Wess、Zumino、Heisenberg 等）。
5. **不添加原文没有的物理内容**。补充解释只能出现在 `% [Tutor Note: ...]` 批注中，并标明是译者补充。
6. `Chapter 3` → `第 3 章`；`Section 2.1` → `第 2.1 节`；`Theorem 2.5` → `定理 2.5`；
   `(2.7)` 这类公式引用照抄；`Exercise 3.2` → `习题 3.2`；`Remark 4.1` → `注 4.1`。
7. 数学模式内的 `\text{...}`：若为数学缩写（Tr、det、Im、Ker、rank、id、Hom、End…）保持英文；
   若为自然语言短语（如 `\text{if }`、`\text{for all }`）可译，但要保证公式仍可编译。

## 4. 文件骨架（严格遵守）

```latex
%=====================================================================
% <章号>  <中文章名>
% 原文：Section <N>. <英文章名>（arXiv:2409.03117v1, p. <起始页>--<结束页>）
%=====================================================================
\section{<中文章名>}   % 若你的文件以 \section 开头（p03a、p08a 等）；否则从 \subsection 开始

\begin{keytakeaways}
\begin{itemize}
  \item \textbf{物理图像：} ...
  \item \textbf{数学工具：} ...
  \item \textbf{关键结论：} ...
  \item \textbf{易错点：} ...（可选）
\end{itemize}
\end{keytakeaways}

\bigskip
\noindent\rule{\textwidth}{0.6pt}
\bigskip

<正文：逐段精译>

\bigskip
\noindent\rule{\textwidth}{0.6pt}
% [Tutor Note: 本章小结——...]
```

- `keytakeaways` 环境已在 `preamble.tex` 中定义，3–5 条，写**实质内容**（不是目录复述）。
- **批注只准用 LaTeX 注释**：`% [Tutor Note: ...]`（行首正好是 `% [Tutor Note: `，结尾 `]`）。
  **不要**用 `\TutorNote{}` 宏（编译后可见，不需要）。
- 每章 **3–6 条**批注，两类：
  1. **易错预警**：涉及张量缩并、指标升降、符号约定、整体符号、$i$ 因子、$2\pi$ 因子、归一化常数、
     Feynman 图对称因子、Berezin 积分的符号、Wick 转动、正规序、算子次序处，点明原文约定与核对方法；
  2. **含糊点拨**：原文 “It is obvious/straightforward that…”“one easily obtains…” 等跳步处，
     指出省略的是哪一步、依据什么定理（如：Morse 引理、Borel 求和与 Stokes 现象、Wigner 半圆律的矩方法、
     Harer–Zagier 的胞腔计数、自伴扩张的 von Neumann 理论、Wightman 重建定理、Virasoro 中心扩张的
     Gelfand–Fuchs 上同调、$\zeta$ 正规化的解析延拓等），必要时给出文献名。**不要瞎猜**，没把握就少写。

## 5. 各章分配与官方章名（必须用这些译名）

| 分节文件 | 底本 | 章号 | 官方中文章名 |
|---|---|---|---|
| sec00-intro.tex | p00-intro.tex | 引言 | 引言（主控翻译，不用你） |
| sec01-generalities.tex | p01-generalities.tex | 1 | 量子场论的一般性讨论 |
| sec02-steepest.tex | p02-steepest.tex | 2 | 最速下降法与驻相公式 |
| sec03a-feynman.tex | p03a-feynman.tex | 3（前半，至 3.6） | Feynman 演算 |
| sec03b-trees.tex | p03b-trees.tex | 3（后半，3.7–3.14） | Feynman 演算 |
| sec04-matrix.tex | p04-matrix.tex | 4 | 矩阵积分 |
| sec05-euler.tex | p05-euler.tex | 5 | 曲线模空间的欧拉示性数 |
| sec06-planar.tex | p06-planar.tex | 6 | 矩阵积分与平面图计数 |
| sec07-qm.tex | p07-qm.tex | 7 | 量子力学 |
| sec08a-operator1.tex | p08a-operator1.tex | 8（前半，至 8.4） | 量子力学的算符方法 |
| sec08b-operator2.tex | p08b-operator2.tex | 8（后半，8.5–8.9） | 量子力学的算符方法 |
| sec09-fermionic.tex | p09-fermionic.tex | 9 | 费米积分 |
| sec10-fermionqm.tex | p10-fermionqm.tex | 10 | 费米子的量子力学 |
| sec11a-freefields.tex | p11a-freefields.tex | 11（前半，11.1–11.6） | 高维自由场论 |
| sec11b-wightman.tex | p11b-wightman.tex | 11（后半，11.7–11.13） | 高维自由场论 |
| sec12-perturb.tex | p12-perturb.tex | 12 | 相互作用量子场论的微扰展开 |
| sec13-cft.tex | p13-cft.tex | 13 | 二维共形场论 |

## 6. 自检流程（必须执行）

1. 先通读底本整节，理解物理与逻辑，再动笔。
2. **按小节分段写作**：每译完 1–2 个 `\subsection`，就把已译部分追加写入成品文件
   （用多次 write/edit，避免一次性输出过长被截断）；最后确认文件从 `\section`/`\subsection`
   到结尾完整（与底本小节数一致）。
3. 写完运行自检脚本（主控已备好）：
   ```
   python w2409/tools/check_section.py w2409/src_parts/pXX.tex w2409/build/sections/secXX.tex
   ```
   （用主控提供的 Python 解释器：`<本地路径>`）
   脚本会对比公式序列、`\label`、环境数、英文残留等。**必须修正到“公式零差异、label 零缺失”。**
4. 若自检发现公式差异：逐条回到底本核对，**不要**改公式去迁就脚本——除非是脚本把合法翻译误报（如 `\text{}` 内容），
   在报告里说明即可。
5. 交付前在回复里给出：成品路径、成稿字数（汉字数）、公式数、批注条数、自检结果（通过/差异列表）、
   发现的原文笔误或疑难处（如有）。

## 7. 禁止事项

- 禁止机翻式长句、禁止中英夹杂成段英文（专名除外）；正文不得残留整句英文。
- 禁止删除、合并、移动原文段落；禁止把习题/注并入正文；禁止改写定理编号。
- 禁止改动 `\label`/`\cite`/`\ref` 键；禁止新增 `\label`（除非原文没有但确需引用，报主控）。
- 禁止在正文中使用 `%` 注释做翻译备忘（只有 `% [Tutor Note: ...]` 一种批注）。
- 禁止插入与内容无关的插图、表情、装饰。
