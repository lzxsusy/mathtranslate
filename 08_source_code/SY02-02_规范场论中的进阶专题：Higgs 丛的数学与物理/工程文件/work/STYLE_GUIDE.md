# STYLE_GUIDE —— 《Higgs 丛的数学与物理》中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：全库统一 CC BY 4.0，明确欢迎用于训练、蒸馏与商用（署名即可）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（v1.0 / Lead 独占维护；队友只读不改。项目根：`<本地路径>`）

## 0. 底本事实（已实测，勿再猜）
- 原文：**Laura P. Schaposnik**, *Advanced topics in gauge theory: mathematics and physics of Higgs bundles*，
  arXiv:1907.09800v1 [math-ph]，2019-07-23；PCMI 2019 研究生暑期学校短课程讲义。
- PDF：`<本地路径>`，**53 页，单栏，letter 612×792 pt**。
  **PDF 页号 = 原文印刷页码（偏移 0）**。页眉：奇数页 "Laura P. Schaposnik / 页码"，偶数页 "页码 / Mathematics and physics of Higgs bundles"。
- 结构：§1 Introduction pp.1–2；§2 pp.3–14（2.1 p3 / 2.2 p6 / 2.3 p7 / 2.4 p8 / 2.5 问题集 I p13）；
  §3 pp.15–25（3.1 p15 / 3.2 p16 / 3.3 p22 / 3.4 问题集 II p24）；§4 pp.26–38（4.1 p26 / 4.2 p29 / 4.3 问题集 III p37）；
  §5 pp.39–48（5.1 p39 / 5.2 p42 / 5.3 p45 / 5.4 问题集 IV p47）；致谢 p49；参考文献 pp.49–53（不译）。
- **编号体系（最关键）**：原文在每一节内使用**统一递增计数器**，定理/命题/引理/定义/例/注/猜想/**编号公式**/图/表
  **共用同一个序号**。例：§2 中 Definition 2.1 → Example 2.2 → Definition 2.3 → … → Example 2.11 → **式 (2.12)** → Definition 2.13 → …。
  实测 66 条：46 条文字条目（`work/statements.tsv`）+ 20 条编号公式（`work/tags.txt`），**逐节连续，无缺无重**。
  另有 20 道习题 **Problem 1–20**（`work/problems.tsv`，编号与节无关，独立递增）。
- 图：仅 **2 张**——Figure 2.24（p.12，位图，`fig1.png`）、Figure 5.10（p.43，箭图，`fig2.png`）。
- 表：仅 **2 张**——Table 4.7（p.31）、Table 4.8（p.31）。
- 原文**公式编号在左侧**（leqno）；preamble 已用 `\documentclass[...,leqno]`，`\tag{2.7}` 会印在左侧，与原文一致。

## 1. 可用素材（都在 `work/`）
| 路径 | 内容 |
|---|---|
| `pages/pNNN.png` | 逐页 200 dpi 渲染图（NNN = 三位 PDF 页号）。**公式/符号的唯一真值。** |
| `split/pNNN.txt` | 逐页文字层（已做 ligature 归一：ﬁ→fi 等）。正文词句可信，**数学一律不可信**。 |
| `full.txt` | 整本文字层（检索用）。 |
| `tags.txt` | 20 条编号公式（编号 ⇥ 页码）。 |
| `statements.tsv` | 46 条文字条目（kind ⇥ 编号 ⇥ 页码）。 |
| `problems.tsv` | 20 道习题（编号 ⇥ 页码）。 |
| `tags_bypage.txt` | 页 → 本页全部条目/公式（分工与自查用）。 |
| `figures/fig1.png, fig2.png` | 已裁好的 2 张原图（由 tr-qa 提供，500 dpi）。 |
| `glossary.tsv` | 术语冻结表（英文 ⇥ 中文，制表符分隔）。 |
| `src/preamble.tex` | 导言区（Lead 独占）。**你只读，不得修改。** |
| `src/chunks/trNN{a,b,c}.tex` | 你的输出文件。 |

**文字层可靠度（血泪教训）**：
- ✅ 正文单词、段落边界、脚注、章节标题 —— 可信，用来定位与理解；
- ❌ **数学符号不可信**：`(2.12)` 可能粘连、上下标错位、`G_C` 抽成 `GC`、`\mathcal{M}_{G_{\C}}` 抽成 `MGC`、
  `\Lambda^2 E` 抽成 `Λ2E`、`↦` 抽成 `7→`、`\mathrm{End}_0` 抽成 `End0`、`\mathbb{P}^1` 抽成 `P1`。
  **每个公式、每个上下标必须逐页看 200dpi 页图逐符号抄写。**

## 2. 片段规则（硬性）
- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、`\tableofcontents`、`\begin{titlepage}`。
- 文件写到 `work/src/chunks/trNN{a,b,c}.tex`（**UTF-8 无 BOM、LF 换行**）。按 a→b→c 顺序拼装；
  建议每 2–3 页写一个文件（a/b 两片，页数多的用 c），**不要等全部读完再写**。
- 章节标题由**指定的人**写（见 BRIEF「标题归属」）：`\section{…}`、`\subsection{…}`。
  原文 `2.5. Problem set I.` 是 **subsection**，写作 `\subsection{问题集 I}`（编号由 LaTeX 自动生成 2.5，**不要手写编号**）。
- 段落之间空一行；不要写 `\par`；不要用 markdown（`**粗体**`、`##`、`>`）。
- **编号条目环境**（编号一律照抄原文，参数里只写编号）：
  ```latex
  \begin{thm}{2.6} 正文…… \end{thm}          % 定理
  \begin{prop}{4.4} …… \end{prop}            % 命题
  \begin{lem}{…} …… \end{lem}                % 引理
  \begin{coro}{…} …… \end{coro}              % 推论
  \begin{defn}{2.9} …… \end{defn}            % 定义
  \begin{exmp}{2.10} …… \end{exmp}           % 例
  \begin{rem}{2.20} …… \end{rem}             % 注
  \begin{conj}{2.25} …… \end{conj}           % 猜想
  ```
  - 原文编号后带括注时，把括注写进参数：`Theorem 4.2 ([59] Theorem 11).` →
    `\begin{thm}{4.2（[59] 定理 11）} 设 $\Sigma$ 是…… \end{thm}`
  - 环境体自动用楷体（`\kaishu`），你不用再写字体命令；环境内可有行间公式。
- **问题（Problem）**：`\begin{prob}{1} \textbf{复 Higgs 丛。}作为练习…… \end{prob}`
  —— 编号 `{1}` 是纯数字（1–20）；原文 "Problem 1. Complex Higgs bundles." 的粗体标题译成 `\textbf{…。}` 放在环境体开头。
- **问题集（Problem set I–IV）**：是小节标题 `\subsection{问题集 I}`，后面一句话说明（照译）。
- 子项列表：
  - 原文 `i. ii. iii.`（Problem 内部）→ `\begin{enumerate}[label=(\roman*),leftmargin=2.2em] \item … \end{enumerate}`
  - 原文 `(1) (2)`（正文编号列表）→ `\begin{enumerate}[label=（\arabic*）,leftmargin=2.2em] \item … \end{enumerate}`
  - 原文 `•` → `\begin{itemize}[leftmargin=1.4em,itemsep=1pt,topsep=1pt] \item … \end{itemize}`
  - Problem 3 里的 `−` 破折号子项（"– the fixed point set …"）→ `\begin{itemize}[label=--,leftmargin=2.6em]`。
- 脚注：`\footnote{…}` 就地写在该处。**脚注编号必须与原文一致**（原文每页/每节重新编号时，用 `\footnotemark`/手动？——本项目原文脚注编号按页连续，LuaLaTeX 自动编号即可；如发现对不上，在回执里报告 Lead）。
- 原文行内粗体小标题（如 `Bibliography.`、`Tame punctures.`）→ `\para{中译}`（独立成段、粗体、不缩进）。
- **原文的三级编号行内小标题（`X.Y.Z.` 形式）一律用 `\para` 手工写编号**，例如
  `\para{4.2.2.\ 非阿贝尔化}`——不要用 `\subsubsection` 自动编号（若有人漏写前一条，全书编号会整体错位；
  编号的唯一真值来自原文）。全书的 `X.Y.Z` 小标题共 7 条：
  `2.4.1`（p11，tr-01）、`3.2.1`（p19，tr-02）、`4.2.1`（p30，tr-04）、`4.2.2`（p33，tr-05）、
  `4.2.3`（p34，tr-05）、`4.2.4`（p35，tr-05）、`5.1.1`（p39，tr-06）。

## 3. 公式（本工程最关键的一条）
- 编号公式**必须与原文一一对应，不缺、不重、不跳、不重排、不自造**：
  ```latex
  \begin{equation}
      F_A + [\Phi,\Phi^*] = 0 \tag{2.7}
  \end{equation}
  ```
  多行用 `align`/`gather`，每行一个 `\tag`；一条编号跨多行时只在最后一行 `\tag`。
- **原文绝大多数公式没有编号**（本讲义只有 20 条编号公式）：这些用 `\[ … \]` 或 `equation*`，**绝不自造编号**。
- 正文引用公式写**纯文本**："式 (2.12)"、"式 (2.7)–(2.8)"，**不要** `\ref`/`\eqref`。
- 文献引用写纯文本：`[36,41,60]`、`[59, Proposition 23]`、`[89, Theorem 4.12]`；**不要** `\cite`。区间用 `--`（如 `[45--54]`）。
- 定理/例/图的引用写纯文本："定理 2.6"、"例 2.14"、"图 2.24"、"表 4.7"、"第 2.3 节"、"习题 3"。
- 常用记号（preamble 已定义，直接用）：`\C \R \Z \PP \E`、`\cM \cA \cB \cO \cS …`、`\fg \fh \fm \fsu \fsp \fso \fsl`、
  `\Gl \Sl \SO \SU \Sp \PSL \U`、`\Prym \Rep \Hom \End \Sym \Jac \Pic \rk \rank \Tr \tr \diag \id \im`、
  `\dd \ee \ii \half \ie \eg \cf`。
- 其他标准命令直接用：`\mathbb{}`、`\mathcal{}`、`\mathfrak{}`、`\operatorname{}`、`\langle \rangle`、
  `\left( \right)`、`\otimes \oplus \cong \simeq \subset \hookrightarrow \xrightarrow{}`、`\leqslant`（原文 ⩽ 用 `\le` 亦可）、
  `\bar{}`、`\hat{}`、`\widetilde{}`、`\overline{}`、`\mathbb{P}^1`。
- 矩阵：`\begin{pmatrix} … \end{pmatrix}`；大括号分段函数用 `\left\{ … \right.`。
- 交换图/箭图：本讲义正文没有 tikz 图（Figure 5.10 由 tr-qa 裁图），不用画。
- **不要用 `\newcommand`**；preamble 缺宏 → 在回执里报告 Lead 补，不要自己在片段里定义。

## 4. 图与表（各只有 2 个，归属见 BRIEF，只有指定的人写）
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.75\textwidth]{fig1.png}
\figtitle{2.24}{两个 2 阶极点的触手。}
\end{figure}
```
```latex
\begin{table}[htbp]
\centering
\small
\begin{tabular}{llllll}
\toprule
…… & …… & …… \\
\midrule
…… & …… & …… \\
\bottomrule
\end{tabular}
\tabtitle{4.7}{经典李代数的紧形式 $\mathfrak{u}$}
\end{table}
```
- 图注照原文翻译；图内文字保持原图（不重画）。图片名固定 `fig1.png`/`fig2.png`，**不写路径**，宽度只用 `width=0.6–0.8\textwidth`。
- 表必须逐格核对（原文 Table 4.7 六列、Table 4.8 四列；**列归属易错**，逐格对照页图）。

## 5. 批注（Tutor Note）
格式固定为 LaTeX 注释行，编译后不显示：
```latex
% [Tutor Note: ……]
```
密度：**每 2–3 页至少 1 条；每节不少于 3 条**。必须是下面几类之一：
- **可验证的易错点**：给出核对方法/数值锚点（如"这里 $\pi_1(\mathrm{Prym}(S,\Sigma))$ 的秩由 $2g-2$ 维 Prym 的复维数 $g-1$ 决定"）；
- **补出的省略论证**：作者说 "it is easy to see / one can show" 而跳过的地方；
- **原文笔误**：必须给正确形式 + 判断依据（相邻式自洽/文献对照/500dpi 裁图复核）；**正文照原样排**；
- **术语首现**：给英文原词（如"超多边形空间（hyperpolygon space）"）。
不要写空话、不要凑数。批注里可以有 `$…$`，但**不得出现不成对的 `$`**。
批注要具体到页码/式号，例如 `% [Tutor Note: p.21 式 (3.8) 的 $\pi_1(\wedge)$ 应为……，见原文 p.20 的短正合列]`。

## 6. 页码标注（强制）
- 每进入新的一页（PDF 页），在该页内容前加一行：`% [原文 p.13]`
- 片段开头加一行：`% ===== 原文 pp.13–15 =====`
- 页脚注跟在对应页内容之后。

## 7. 禁止事项（违反即返工）
1. 不改原文内容：**不删、不增、不"顺手修正"正文**；原文字句有误 → 照译 + 批注指出 + 给正确形式。
2. 不编造：图、表、公式、文献、作者没说过的结论，一个字都不加。
3. 不用 `\newcommand`、不改 preamble/main/STYLE_GUIDE/别人的 chunks、**不编译**（编译由 Lead 统一做）。
4. 不用 markdown 语法。
5. 不留未翻译的整句英文（人名、期刊名、$G_{\C}$、SL(2,C)、Prym、Higgs、Hitchin、Langlands 等专名与缩写保留英文；
   参考文献不译）。
6. 中文标点：句号"。"、逗号"，"、顿号"、"；数学环境内英文标点。**不要用 U+2013「–」作中文破折号**（用 `--`）。
7. 不写"本节重点"之类的总结段。

## 8. 术语（`glossary.tsv` 冻结）
首次出现括注英文：如" Higgs 丛（Higgs bundle）"；此后统一用中文。人名/模型名/缩略语（Higgs、Hitchin、Prym、
Langlands、Stokes、F-theory、Calabi-Yau、SL(2,C)、$\mathcal{M}_{G_{\C}}$）保留英文/原记号。
新术语由你在回执里报告，Lead 汇总后再全书归一。

## 9. 边界规定
- 你的片段若从句子/公式中间开始：**直接续写**，不要重写上文，也不要重复上一块已写的内容。
- **跨页句子"开始者写完"**：谁先开始这句，谁负责把它写完（必要时多读下一页）。
- 边界歧义：多看一页页图，并在回执里说明。
- 编号连续性是你和邻居的契约：你负责的编号区间**首尾必须接上**（见 BRIEF）。

## 10. 自检清单（写文件前逐项过）
- [ ] 本块编号区间完整：起始编号 … 结束编号，一个不缺、无重复、无自造；
- [ ] 每个编号公式与页图逐符号核对（上下标、指标位置、希腊字母、`\mathcal`/`\mathfrak`/正体）；
- [ ] 花括号平衡、`\left`/`\right` 配对、`\begin`/`\end` 配对、`$` 成对；
- [ ] 无 `\documentclass`/`\usepackage`/`\begin{document}`/`\newcommand`/`**`；
- [ ] 无 U+FFFD 乱码；UTF-8 无 BOM；LF 换行；
- [ ] 覆盖本块全部正文、脚注、图注/表题、习题子项；
- [ ] 批注数量与质量达标（每 2–3 页 ≥1，每节 ≥3）；
- [ ] 每页都有 `% [原文 p.N]` 标注；
- [ ] 逐段对照 `split/pNNN.txt`，**无整句/整段漏译**。

## 11. 回执格式（send_message 给 lead）
1) 完成文件与覆盖页段；2) 编号区间（如 2.13–2.25）及跳号/存疑；
3) 发现的原文可疑/笔误（页码 + 编号 + 判断依据）；4) 新增术语（英→中）；
5) 自检结果（逐项 pass）；6) 未尽事项/需要 Lead 处理的问题。
