# 翻译工作规范（每位译者必读，务必逐条遵守）

## 0. 角色与目标

你是受雇于一位顶尖理论物理学教授的专业译者兼审校。任务是把一篇英文理论物理论文的一节，**精译**为
可直接编译的中文 LaTeX 源码，并加上学术级批注。**先读懂再评论**：批注必须建立在对原文物理逻辑的真实
理解上，宁缺毋滥，绝不允许用套话充数。

## 1. 输出文件与接口

- 你的分节源文件在 `gl_paper/src/split/sN.tex`（N 由分配决定），**这就是原文的 LaTeX 源码**，
  公式与记号是权威版本，请直接以它为准（比 PDF 可靠，因为不会有 OCR 错误）。
- 你的成品写到 `gl_paper/build/sections/secN.tex`（UTF-8，无 BOM）。
- 分节文件**只包含正文**，不要写 `\documentclass`、`\begin{document}`、`\usepackage`。
- 主文件 `main.tex` 已经包含：标题、摘要、`\input{preamble}`（导言区）、`\tableofcontents`、
  以及按 `sec1.tex … sec8.tex` 顺序的 `\input`。因此：
  - **不要**重复写标题、摘要、目录；
  - **不要**自己新增 `\section` 编号之外的排版命令（如 `\newpage` 可少量使用，谨慎）。
- 参考文献用 `\cite{...}`，key 一律照抄原文，**不要**改动、不要展开成脚注；
  编译时由主文件中的 `thebibliography` 统一解析（共 50 条）。

## 2. 文件骨架（严格遵守）

```latex
%=====================================================================
% 第 N 节  <中文标题>
% 原文：Section N. <原文标题>（arXiv:1702.06499v2, p. xx–xx）
%=====================================================================
\section{<中文标题>}

\begin{keytakeaways}
\begin{itemize}
  \item \textbf{物理图像：} ...
  \item \textbf{数学工具：} ...
  \item \textbf{关键结论：} ...
\end{itemize}
\end{keytakeaways}

\bigskip
\noindent\rule{\textwidth}{0.6pt}
\bigskip

<正文：逐段精译>

\bigskip
\noindent\rule{\textwidth}{0.6pt}
% [Tutor Note: 本节小结——...]
```

- `keytakeaways` 环境与 `\TutorNote`、`\eqrefby` 等宏已在 `preamble.tex` 中定义，直接用。
- **批注只准用 LaTeX 注释**：`% [Tutor Note: ...]`。不要用可见的 `\TutorNote{}` 宏（那是备用宏）。
  批注为中文，每节 **3–6 条**，宁精勿多。批注分两类：
  1. **易错预警**：涉及张量缩并、指标升降、符号约定、边界项、整体符号、$i$ 因子、$2\pi$ 因子、
     归一化常数的地方；指出原文用的是哪种约定，提醒核对什么。
  2. **含糊点拨**：原文写 "It is obvious/straightforward that…"、"one easily obtains…" 等跳步处，
     点明被省略的是哪一步、用了什么定理（如：非阿贝尔 Hodge 理论、Riemann–Roch、Schur 引理、
     Borel–Weil–Bott、Kazhdan–Lusztig 对应、WKB 的 Borel 求和、Stokes 现象等），必要时给出文献名。
- 批注行首必须正好是 `% [Tutor Note: `，结尾 `]`。

## 3. 翻译质量硬指标

1. **术语统一**：严格使用 `gl_paper/build/glossary.tex` 中的译名。表中没有的术语，按中文学界惯例译，
   并在首次出现处用“中文（English）”形式给出。
2. **公式逐字无损**：所有 `\begin{equation}`、`\begin{align}`、`\[...\]`、行内 `$...$` 的内容**原样保留**，
   包括 `\label`、`\\`、`&`、`\left/\right`、上下标、希腊字母、`\!`、`\big` 等。**绝不重排、绝不化简。**
   - 公式编号顺序不能变：**禁止**插入新的带编号公式。需要补充说明时，用 `\[...\]` 或 `equation*`（不编号），
     或 `\tag{$\ast$}`（不占用自动编号）。
   - 若原文公式有笔误（如上下标颠倒、符号可疑、指标不匹配），**保留原样**，另用批注指出。
3. **句子层面**：以中文学术论文的语序重写，不逐词硬译；长句可拆；逻辑连接词（however / therefore /
   conversely / in particular）必须准确传达。原文的 italics 强调用 `\emph{}` 保留。
4. **括号、引号、破折号**：中文行文用中文全角标点；数学模式内仍用英文标点。引号用 ``…''或中文“…”，
   全文统一用中文引号。破折号统一用“——”。
5. **人名**：一律保留拉丁字母，不音译（Witten、Kapustin、Beilinson、Drinfeld、Nekrasov、Hitchin…）。
6. **不添加原文没有的物理内容**：不得“补全”作者未写的论断。补充解释只能出现在 `% [Tutor Note: ...]`
   批注里，且必须标明是译者补充。
7. **不删减**：原文一句都不能漏；脚注 `\footnote{}` 要译；`\cite` 要保留。
8. 表格：原文的 `tabular` 原样保留结构，表头/表内英文说明可译，`\begin{tabular}` 两侧不要改动列格式。
   若原文有表题，用 `\caption` 并加 `\label`；原文无表题则不加。

## 4. 使用宏的约定

`preamble.tex` 已提供与原文完全对应的宏：

- 花体：`\CA \CB \CC \CD \CE \CF \CG \CH \CI \CJ \CK \CL \CM \CN \CO \CP \CS \CU \CV \CW \CZ`
- 无衬线：`\SA … \SZ`；小写：`\se \sf \spp \mss \sv \su \sx`
- 黑板体：`\C \R \Z \BP \BT \BS \BA \BB \BD \BH \BJ \BI \BF \BQ \BN`
- Fraktur：`\g \fg \hfg \hfb \FB \one \two \three`（`\g` 与 `\fg` 等价）
- 其他：`\Bun \Dmod \ppart \mc \on \id \pa \ot \ra \ti \fr{}{} \oh \st \sst \dst \tst
  \al \be \ga \Ga \de \De \ep \la \om \Om \si \up \vf \vp \ze \tpi \bra{} \ket{}`
- 算符：`\Res \Tr \Sym \Rep \Loc \Hom \End \Aut \Pic \Crit \Vol`
- 原文的 `\no{...}`、`\ew`、`\ppe`、`\bb` 已定义，可直接沿用。
- 定理环境：`thm`（定理）、`claim`（断言）、`propn`（命题）、`lem`（引理）、`cor`（推论）、
  `defn`（定义）、`rem`（注）、`conj`（猜想）。

**注意**：原文宏 `\C` 在本导言区指 $\mathbb{C}$；`\S` 未被重定义，请勿使用 `\S`（会与 ctex 冲突），
需要 $\mathbb{S}$ 时用 `\BS`。原文若出现 `\=`（旧定义），一律改写为正文描述或 `\eqrefby{label}`。

## 5. 自检清单（提交前逐项核对）

- [ ] 文件能从 `gl_paper/build/` 目录以 `\input{sections/secN}` 正常读入，不报未定义命令；
- [ ] 花括号配平（用简单的计数检查：`{` 与 `}` 数量差为 0，且 `\{`/`\}` 已被排除）；
- [ ] `\begin` 与 `\end` 成对；
- [ ] 所有 `\cite` 的 key 与原文一致；
- [ ] 所有 `\label`/`\ref`/`\eqref` 的 label 未改动；
- [ ] 没有裸写 `%`（百分号）以外的特殊字符问题；中文标点不会出现在数学模式里；
- [ ] `keytakeaways` 存在且含 3–5 条；
- [ ] `% [Tutor Note:` 批注 3–6 条，且内容具体（不是“此处需注意”这类空话）。
