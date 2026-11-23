# 译手作业合同（STYLE_GUIDE）

本文件是《无穷范畴讲义》中译本的**唯一施工标准**。译手只写 `源码/chunks/lecNN.tex` 一个文件，不改 `preamble.tex`、`main.tex`、`front/` 与任何其他讲次。

## 0. 一句话目标

把底本第 NN 讲**逐段、逐式、逐条**译成中文，编号与原书完全一致，能通过 `xelatex` 编译，且不增、不删、不改数学内容。

## 1. 交付物

- 路径：`08_source_code/SY02-27_无穷范畴讲义/源码/chunks/lecNN.tex`（NN 为两位讲号）。
- 文件开头必须照抄（把讲号、讲题、页码换成该讲的）：

```latex
% =============================================================================
%  lec03.tex —— 第 3 讲 单纯集（底本 PDF 第 16–27 页）
% =============================================================================
\lecture{3}{单纯集}
\begin{center}\small\color{black!55}（底本 PDF 第 16–27 页）\end{center}
```

- 讲题用 `工程文件/work/lecture_pages.tsv` 与 `工程文件/work/src/lecNN.txt` 首行的英文题，译法见 §3 对照表；讲题由 Lead 统一，不得自创。
- 全文只用一个 `\lecture`，讲内节用 `\section`，不写 `\subsection`（原书没有二级节；附录除外）。

## 2. 编号：本工程最硬的约束

原书每讲独立编号；讲内 `\section` 为 `1.` `2.` ……；**每一节内，一切带编号的对象共用一个计数器**，依次是 `节号.序号`。因此：

- 每个编号对象都必须按原书顺序出现，**一个不能少、一个不能多、不能换序**。
- 普通编号段落（原书以 `2.1.` `2.3.` 直接开头的段落）用 `\nitem`。
- 其余编号对象用下列环境，**环境名必须与原文的类别一致**：

| 原文 | 环境 | 打印 |
|---|---|---|
| Slogan | `slogan` | 口号 |
| Definition | `definition` | 定义 |
| Theorem | `theorem` | 定理 |
| Proposition | `proposition` | 命题 |
| Lemma | `lemma` | 引理 |
| Corollary | `corollary` | 推论 |
| Conjecture | `conjecture` | 猜想 |
| Claim | `claim` | 断言 |
| Example | `example` | 例 |
| Exercise | `exercise` | 练习 |
| Challenge | `challenge` | 挑战 |
| Construction | `construction` | 构造 |
| Variant | `variant` | 变体 |
| Remark | `remark` | 注 |
| Notation | `notation` | 记号 |
| Warning | `warning` | 警告 |
| Convention | `convention` | 约定 |
| Question | `question` | 问题 |
| Theorem-Definition | `theoremdef` | 定理—定义 |

不要用 `\begin{definition}[...]` 的可选参数；原书编号由环境自动给出，不要手打编号。

### 2.1 标签与交叉引用

每个编号对象在环境开始后（或 `\nitem` 后）立刻加标签，标签名固定为 `L<讲号>-<原书编号>`：

```latex
\begin{definition}\label{L2-2.2}
...
\end{definition}

\nitem\label{L2-2.3} ...
```

同讲内引用写作 `定理~\ref{L2-2.2}`、`\eqref{L1-4.1}`、`练习~\ref{L2-2.7}`。**不要手打“定理 2.2”**，一律用 `\ref`，否则编号错位时无法发现。

跨讲引用（原文 `[Lecture 2, Definition 2.20]`）**不用 `\ref`**，写成“第 2 讲定义 2.20”。原因：单讲编译时别的讲的标签不存在，`\ref` 会出 `??`。跨讲编号按原书照抄，不得自行换算。

### 2.2 附录

原书每讲末尾的 `Appendix A. ...` 用：

```latex
\appendixsection{中文标题}
```

它会打印“附录 A　中文标题”，并把该讲此后的 `nitem` 编号自动变成 `A.1`、`A.2`……。附录内照常使用 `\begin{exercise}` / `\nitem`，不要手打 `A.1`。若有 `Appendix B`，再写一次 `\appendixsection{...}`。附录结束后本讲即结束（下一讲由 `\lecture` 重置）。

### 2.3 参考文献

每讲末尾的 `References` 用：

```latex
\subsection*{参考文献}
\begin{itemize}[leftmargin=2.6em,itemsep=0.15em,label={}]
\item [Lur09] Jacob Lurie. \emph{Higher Topos Theory}. Princeton University Press, 2009.
\end{itemize}
```

文献条目**不翻译书名**，只保留原条目；`[Lur09]` 这类标签原样保留。正文中的引用 `[Lur09]` 原样保留。

## 3. 术语

以 `工程文件/work/glossary.tsv` 为准。首见时可写“中文（English）”，其后只用中文。讲题统一译法：

| 讲 | 英文题 | 中文题 |
|---|---|---|
| 1 | Introduction | 引言 |
| 2 | Model categories | 模型范畴 |
| 3 | Simplicial sets | 单纯集 |
| 4 | Quasi-categories | 拟范畴 |
| 5 | Quasi-category of quasi-categories | 拟范畴的拟范畴 |
| 6 | Limits and colimits: definition | 极限与余极限：定义 |
| 7 | Limits and colimits: functoriality | 极限与余极限：函子性 |
| 8 | Limits and colimits: model categories | 极限与余极限：模型范畴 |
| 9 | Limits and colimits: Kan extensions | 极限与余极限：Kan 扩张 |
| 10 | Limits and colimits: commutativity | 极限与余极限：交换性 |
| 11 | Yoneda lemma | Yoneda 引理 |
| 12 | Adjoint functors | 伴随函子 |
| 13 | Presentable infinity categories | 可表现 ∞-范畴 |
| 14 | Spectra | 谱 |
| 15 | Stable infinity categories | 稳定 ∞-范畴 |
| 16 | t-structures | t-结构 |
| 17 | Derived infinity categories | 导出 ∞-范畴 |
| 18 | Dold–Kan correspondence | Dold–Kan 对应 |
| 19 | Cartesian fibrations | 笛卡尔纤维化 |
| 20 | Straightening and unstraightening | 平展与去平展 |
| 21 | Infinity operads | ∞-操作子 |
| 22 | Algebras | 代数 |
| 23 | Modules I | 模 I |
| 24 | Modules II | 模 II |
| 25 | Lurie tensor products and smash products | Lurie 张量积与 smash 积 |
| 26 | Tensor products of infinity operads | ∞-操作子的张量积 |
| 27 | E_infty rings | E_∞-环 |

拿不准的术语：查 glossary；仍无，则用“中文（English）”并在交付说明里列出，不要自造一个与 glossary 冲突的译名。

## 4. LaTeX 合同

- **只许使用 `preamble.tex` 已定义的宏**。常用：`\cC \cD \cA …`（花体）、`\Z \Q \R \C \N`、`\Spec \Hom \Map \Fun \End \Aut \id \coker \im \Ker \Ob \Mor \colim \hocolim \holim \Ind \Pro \PSh \Sh \Sing \Sp \Spc \Cat \Set \sSet \Grpd \Kan \Ch \Mod \Alg \coAlg \Vect \Ab \Grp \Top \Ho \hTop \hGrpd \Ring \ho`、`\op \ot \we \ra \la \To \from \into \onto \defeq`、`\yizhu{}`。需要新符号时用 `\operatorname{...}` 或直接写，**不要 `\newcommand`**，不要改 preamble。
- 上下标、花体、粗体保持原书：`\mathfrak{g}`、`\mathcal{C}`、`\mathbf{1}`（单位对象）、`\Delta^n`、`\Lambda^n_i`、`\partial\Delta^n`、`\pi_{\le n}X`。
- 公式编号：`\begin{equation}\label{L3-1.1}...\end{equation}`；多行用 `aligned`、`cases`、`gathered`；交换图用 `tikzcd`。原书公式编号形如 `(1.1)`，由 `\numberwithin{equation}{section}` 自动给出，不要手打。
- 列表：项目符号用 `\begin{itemize}[leftmargin=2.2em,itemsep=0.1em]`；编号列表用 `\begin{enumerate}[label=(\arabic*),leftmargin=2.4em,itemsep=0.1em]`。
- 强调：原文斜体/粗体的关键术语用 `\textbf{...}`；不要把整段加粗。
- 脚注：`\footnote{...}`，位置照原文。
- 图：原书共 5 幅编号图。lec03、lec04 的译手在原文 Figure 出现处写

```latex
\begin{center}\FIGPLACEHOLDER{1}\end{center}
```

并在同一位置保留“图 1”的正文引用。图由 Lead 统一重绘替换；不要自己画，也不要删掉图号。

## 5. 翻译规范

1. **逐段对应**：原书一段译一段；不合并、不拆分段落（公式块可合并成一行显示）。
2. **数学不动**：符号、下标、量词、条件、编号一律照抄；只译自然语言。原文的笔误（如 `pathes`、`wihch`、`diﬃcult`、`iﬀ`）按正字理解，不另出注。
3. **中文可读**：避免“的的不休”与英文语序；长句可断为两句，但不得改变逻辑关系（因果、充分必要、量词范围）。
4. **不增不删**：不补原文没有的定理、例子、证明；不删练习、注、附录。原文说“Challenge”就译“挑战”，不要降格为“练习”。
5. **保留人名与文献标签**：Eilenberg、MacLane、Quillen、Joyal、Lurie、Kan、Yoneda、Grothendieck、Bénabou、Whitehead、Dold、Kan、Segal、Rezk、Dwyer、Hirschhorn、Hovey、Cisinski 等保留拉丁拼写；`[Lur09]` 原样。
6. **英文残留**：除人名、文献标签、首次出现的术语英文、以及 `E_k`/`E_\infty`/`t-structure`/`smash`/`anima` 等约定保留词外，正文不得出现英文句子或英文连接词。
7. **译注**：每讲 0–4 条，只在确有需要时加（术语取舍、背景补充、原文疑点）。格式：

```latex
\yizhu{……。\textbf{[来源：B]}}
```

依据等级：A＝可核对的公开文献（写出作者/书名/编号），B＝同类教材通例，I＝据上下文推断。无外部依据写 `\textbf{[译者按（无外部依据）]}`。**禁止编造文献页码**；不确定就标“译者按（无外部依据）”。
8. **来源黑名单**：不得引用知乎、百度百科/知道、CSDN、简书、公众号、B 站、个人博客、“XX 笔记”类网站。译注中也不要出现这些来源。

## 6. 源文本的噪声

`工程文件/work/src/lecNN.txt` 是 PDF 文字层抽取，已尽量还原上下标，但仍有：

- 词间空格偶尔丢失（`inthisﬁeld`）：按语义断词。
- 多行公式的 `⊕`、`∑` 上下限被拆成独立行：按数学含义重构为 `\sum_{i=0}^{n-1}`、`\bigoplus_{i=0}^{n-1}`。
- 下标被拆成 `A_{n−1}` 之类：直接用 `A_{n-1}`。
- 项目符号 `●` 后可能没有空格：按列表处理。
- 页眉 `LECTURE n` 与页码已由抽取器删除；脚注以 `[脚注 n]` 标出，放在对应位置。
- 分页标记 `===== PDF PAGE n =====` 不要抄进译文。

**公式拿不准时，必须看页图**：仓库外底本目录下的页图 `_底本/SY02-27/pages/pNNN.png`（NNN 为三位 PDF 页码）。用 `read_image` 工具查看，不要猜。

## 7. 自检与交付

1. 写完后运行：

```bash
cd "08_source_code/SY02-27_无穷范畴讲义"
python 工程文件/tools/compile_chunk.py NN
```

必须零 error（warning 可接受）。有 error 就改到通过。
2. 自查清单：
   - [ ] `\lecture` 讲号、讲题、页范围正确；
   - [ ] 节数与源文一致；
   - [ ] 每个编号对象都有标签，编号顺序与源文逐一对应；
   - [ ] 没有手打编号；
   - [ ] 没有英文句子；
   - [ ] 公式编号与环境类型正确；
   - [ ] 附录用 `\appendixsection`；
   - [ ] 参考文献条目齐全；
   - [ ] 编译零 error。
3. 交付说明（回给 Lead，不超过 200 字）：讲号；编号对象总数；节数；译注条数；编译结果；存疑术语/公式清单（若有）。

## 8. 常见错误（会直接退回）

- 把 `\nitem` 写成 `\begin{definition}` 或反过来（会改变编号语义）。
- 漏掉编号对象，导致后续编号整体错位。
- 手打“定理 2.3”而不用 `\ref`。
- 用 `\newcommand` 或改 `preamble.tex`。
- 把整段英文原样留下。
- 把 `Appendix` 写成 `\section`（编号会变成 5.1）。
- 公式里用 `\text{...}` 包中文（应用 `\text{中文}` 时确保在数学环境内且用 xeCJK 可排；不确定就移出公式）。
