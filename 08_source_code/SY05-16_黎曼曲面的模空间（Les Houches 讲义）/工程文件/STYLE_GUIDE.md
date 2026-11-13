# STYLE_GUIDE.md — 硬性规范（违反 = 返工）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 本文件由 Lead 独占维护，队友**只读**。
> 底本：Giacchetto–Lewański, *Les Houches lecture notes on moduli spaces of Riemann surfaces*, arXiv:2410.13273v2, 46 页。

## §0 一句话

**照原文逐段译；公式逐条看图抄；编号一个不多一个不少；不插图、不造表、不编物理。**

## §1 页码体系

- **PDF 页号 = 印刷页码**（偏移 0），两种说法通用。片段里所有位置标注写成 `% [原文 p.16]`。
- 每个片段文件开头必须有：
  ```latex
  % ===== Block D: PDF p.16–20 | 原文 §2.3（前半） | 唯一编号公式 2.36–2.61 =====
  ```
- 每到新的一页（原文页），在正文流里插一行注释 `% [原文 p.17]`。这行**只能插在两个段落之间**，不能插在数学环境或句子中间。

## §2 片段规则（最重要）

- 每个块只产出**一个文件** `src/<你负责的文件名>.tex`，内容是可直接 `\input` 的**片段**。
- **禁止**出现：`\documentclass`、`\usepackage`、`\newcommand`、`\renewcommand`、`\DeclareMathOperator`、`\begin{document}`、`\end{document}`、`\usepackage`、`\input`、`\includegraphics`、`\tableofcontents`、`\maketitle`。
- **禁止**自己定义宏、环境、计数器。需要新宏 = 报告 Lead，由 Lead 加进 `src/preamble.tex`。
- 章节标题由 Lead 在 `main.tex` 里写，**队友不要写 `\section` / `\subsection`**（唯一例外：块内确实有原文子标题的，见 §9）。

## §3 公式编号（唯一真值）

1. 每条原文编号公式 → `equation` + `\tag{}`：
   ```latex
   \begin{equation}
     \overline{\mathcal{M}}_{g,n} = \cdots
     \tag{2.36}
   \end{equation}
   ```
2. 多行对齐且**每行各有一个编号**：用 `align`，每行 `\tag{...}`：
   ```latex
   \begin{align}
     A &= B \tag{2.41}\\
     C &= D \tag{2.42}
   \end{align}
   ```
3. 多行对齐但**只有最后一行有编号**：前面的行 `\nonumber`：
   ```latex
   \begin{align}
     A &= B \nonumber\\
     C &= D \tag{2.43}
   \end{align}
   ```
4. 同一编号下有多个并列式子：写成一行，用 `\qquad` 分隔，共用一个 `\tag`：
   ```latex
   A=B, \qquad C=D \tag{2.44}
   ```
5. 原文无编号的显示公式 → `\[ ... \]`，**禁止**给它们编 `\tag`。
6. **`\tag` 里的数字必须与原文完全一致**，不得重排、不得跳号、不得自造。块的标签清单见 TIMELINE.md，开始/结束各一条锚点公式。
7. 正文中引用公式写**纯文本**：`式 (2.40)`，**禁止** `\eqref` / `\ref`（手工 tag 无交叉引用）。
8. 原文若把公式编号印错（重号、跳号），**照原样排**，并在 `% [Tutor Note: ...]` 里指出。

## §4 数学宏（只用 preamble 已定义的，禁止自造）

preamble 里已提供（完整清单见 `src/preamble.tex` 顶部注释）：

```
\dd \ee \ii \Tr \Aut \PD \id \R \C \Z \Q \N \PP \HH
\cM \Mc \cH \cF \cD \cL \cO \cA \cB \cE \cG \cP \cS \cU \cV \cX
\Ho \CohFT \TR \Vol \WP \VWP \eps \wt \ol \figomit
```

- `\cM_{g,n}` = $\mathcal M_{g,n}$；`\Mc_{g,n}` = $\overline{\mathcal M}_{g,n}$。
- `\Ho` = $H^{\bullet}$。`\PD` = $\mathrm{PD}$。`\dd` = $\mathrm{d}$（积分微分、微分形式）。
- 其他一律写**普通 LaTeX**（`\mathcal{Q}`、`\mathrm{GL}`、`\operatorname{Aut}` 之类），**不要**新建宏。
- 不要用 `\text{}` 里的中文（数学里不出现中文；必须出现时用 `\mbox{中文}` 且尽量改写掉）。
- 逐字对应原文符号，**不要**为了好看改符号：原文用 $\mathcal M$ 就写 `\mathcal M`，原文用 $\mathrm{M}$ 就写 `\mathrm{M}`。

## §5 批注格式（Tutor Note）

- 一律写在 LaTeX 注释里，**不进入排版**：
  ```latex
  % [Tutor Note: 这里作者把 $\omega_{g,n}$ 的展开写成 ...；核对方法：取 $g=0,n=3$ 时 ... ]
  ```
- 批注里可以自由用 `$...$`（注释不被 TeX 处理），**但 `$` 必须成对**（check.py 的 `$` 计数会误报）。
  实在需要单个 `$` 时写成 `\$`。
- **批注必须值得写**，满足其一：
  1. **可验证的易错点**：给出核对方法（取特殊值 / 量纲 / 与已知小 $g,n$ 比较）；
  2. **补出的省略论证**：说清用了什么定理、哪一步跳了、为什么成立；
  3. **原文笔误**：给出正确形式 + 判断依据（数值检验 / 相邻式自洽 / 与经典文献对照）。
  4. **术语/记号说明**：原文记号切换处（如 $\overline{\mathcal M}$ 与 $\mathrm{M}$ 混用）、跨领域术语的辨析。
- **不要**写"这一段很重要"“需要注意”这类空话；不要复述原文。
- 每块 **8–25 条**批注，宁缺毋滥。批注总数目标 ≈ 150–220 条。
- 批注不许出现**不成对的 `}`**、不许出现 `\` 结尾的行（避免续行吃掉下一行注释）。
- 原文本身的笔误/排版瑕疵，必须登记进 `ERRATA.md`（Lead 汇总）：一行一条，格式 `p.N | 原文位置 | 原文写法 | 正确写法 | 判断依据`。

## §6 环境（定理/习题/例/注）

原文编号是**每个 section 一套主计数器**（定义/定理/命题/例共用）+ **习题单独一套计数器**。已实测序列见 TIMELINE.md。用法：

```latex
\begin{definition}[2.1]    % 印出「定义 2.1」
...
\end{definition}

\begin{exercise}[2.1]      % 印出「习题 2.1」
...
\end{exercise}
```

可用环境：`definition`（定义）、`theorem`（定理）、`proposition`（命题）、`example`（例）、`exercise`（习题）、`corollary`（推论，备用）、`remark`（注，备用）。

- **编号必须手工给**，`[]` 里写原文编号。**禁止**依赖自动计数器（本译注本用 `\section*` 风格编号会跳）。
- 原文没有编号的定理/定义（若有）→ 用 `definition*` / `theorem*` 星号环境，印出「定义」不带号。
- **注意**：`[2.1]` 里不要出现数学；不要写 `[习题 2.1]`（环境自动加"习题"二字）。

## §7 禁止事项

1. **不插图**：不写 `\includegraphics`、不画 TikZ、不画 Asymptote。原文有图的位置 → 用
   ```latex
   \figomit{7}{紧化模空间 $\overline{\mathcal M}_{g,n}$ 的图示：把退化的边界点补进去。}
   ```
   （第一个参数是原文 Figure 编号，第二个是**图注译文**+如果需要一句话说明图上画了什么——但**只能写原文图注与正文明确说过的内容**，不许脑补。）位置在图出现处，紧跟其图注所在位置。
   正文里 "see figure 5" 照译成"见图 5"，**不要**改成别的编号。
2. **不造表**：原文的 3 张表（Table 1/2/3）**要照抄重排**（那是原文数据，不是造表），表题译成中文并保留 `Table N`：
   ```latex
   \begin{table}[htbp]\centering\small
   \caption*{表 1：用拓扑递归关系算出的部分 $\psi$ 类相交数。}
   \begin{tabular}{...}\toprule ... \bottomrule\end{tabular}
   \end{table}
   ```
   表的内容**逐格看图抄**，数字错一位就是硬伤。除这 3 张外，**不许新增任何表**。
3. **不补文献**：参考文献照抄，不加不减（块 I 负责）。正文方括号引用照抄：`[DM69]`、`[Zvo12]`。
4. **不改正文**：原文说错的、写怪的、笔误的，**照原样译**，在 Tutor Note + ERRATA.md 里指出。
5. **不写 Markdown**：`**粗体**` 会原样印成星号。要强调用 `\emph{}` 或 `\textbf{}`。
6. **不写 HTML/Unicode 花哨符号**：数学符号一律 LaTeX 命令。特别地：
   - 希腊字母：正文里**不要**直接写 Unicode `ζ`，写 `$\zeta$`（缺字风险）。
   - 不许出现全角标点以外的奇怪字符；中英文之间不要手动加空格（xeCJK 自动处理）。
   - `≤ ≥ ≠ → ← ↔ ∞ ∑ ∫` 等一律 `\le \ge \ne \to \leftarrow \leftrightarrow \infty \sum \int`。
7. **不删原文内容**：包括原文的打字错误、重复词、括号不配对（在批注里指出，但正文照译）。
8. **不翻译人名/文献标题/期刊名**：Witten、Givental、Kontsevich 等保留拉丁字母；参考文献条目整条不译（仅块 I 处理）。
9. **不写 `\begin{document}` 级的任何东西**，不写目录。
10. **不做静默省略**：任何你以为"可能不重要"的段落，都要译；真搞不定就写 `% [TODO-LEAD: ...]` 并在回报里说明。

## §8 边界规定

- **标题归属**：章节标题（`\section`/`\subsection`）由 Lead 写。块边界若正好落在某个 `\subsection` 标题上，由**后一块**开始，你在文件开头写 `% [NOTE: 本块从 §2.2 标题后开始]`，并**不要**自己写 `\subsection`。
- **跨页句子**：谁开始谁写完（"开始者写完"）。宁可多看一页图像，不要交半句。
- **跨块句子**：以 TIMELINE.md 的锚点为准。开始一条编号公式的块负责**整条公式**；结束块负责到锚点公式为止（含）。
- 如果实际边界与任务书不符：**不要自己改**，照任务书写，并在回报里 `BOUNDARY: ...` 说明实际接续点。Lead 裁决后写进 TIMELINE.md 并通知上下游。
- 图片/表格跨越块边界时：表格整体归**表格标题所在页**的块。

## §9 写作风格（中文学术翻译）

- 用**成熟的数学中文**：「我们有」「由此得到」「注意到」「不失一般性」「如下」。
- 第一人称复数照译（"we" → "我们"）。
- 长句可以拆分，但**不许删信息、不许加解释**（解释进批注）。
- 术语严格按 `glossary.tsv`；glossary 里没有的，第一次出现给"中文（English）"，之后只用中文。
- 中英混排处直接接排，不手动加空格（xeCJK 会处理）。数字与单位、公式与中文之间不要多余空格。
- 参考文献引用 `[DM69]` 原样保留，不加空格、不改方括号。
- 强调（原文斜体）→ `\emph{}`；小型大写 → 普通大写或 `\textsc{}` 慎用。
- 项目符号列表照译，用 `itemize`/`enumerate`（原文 bullet 是 `•` 的 → `itemize`）。
- 原文的 `Theorem 2.2` 等在正文中提及 → "定理 2.2"。

## §10 交付与回报

- 文件写到 `<本地路径><文件名>.tex`，**UTF-8 无 BOM、LF 换行**。
  用 Python 写文件时用 `encoding="utf-8", newline="\n"`；**不要**用 PowerShell `Out-File -Encoding utf8`（带 BOM，会炸）。
- 自己先跑：
  ```
  $env:PYTHONIOENCODING='utf-8'
  python check_block.py <你的文件名>
  ```
  必须 `OK`（检查：`\tag` 集合与任务书清单一致、花括号平衡、环境配对、`$` 偶数、禁用命令、BOM、非 ASCII 数学符号）。
- **不要自己编译**（编译由 Lead 统一做）。不要动别人的文件、不要动 main.tex/preamble.tex。
- 回报内容（一条消息，简洁）：
  ```
  DONE <文件名> | PDF p.a–b | 公式 n 条（首 2.x 尾 2.y）| 环境: ... | 批注 k 条 | 图: 略 m 处 | 表: 抄 n 张
  BOUNDARY: 实际接续点（若有出入）
  ISSUES: 需要 Lead 裁决/补宏/核对的问题（每条一行）
  ERRATA: 发现的原文笔误
  ```
