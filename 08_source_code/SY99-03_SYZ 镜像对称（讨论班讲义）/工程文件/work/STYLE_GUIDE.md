# STYLE_GUIDE —— 《学习讨论班：SYZ 镜像对称》中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（v1.0 / Lead 独占维护，队友**只读**；改动须 Lead 书面通知）

## 0. 底本（实测，勿再猜）

- 底本不是 PDF，而是**网页**：`https://diewildkatze.com/SYZ.html`（学习讨论班讲义，2026-11-04 抓取）。
  原始 HTML 存于 `work/../raw/SYZ.html`（106,386 字节）。
- **公式的唯一真值 = 网页 HTML 里 MathJax 的 LaTeX 源码**。本工程已用脚本把 HTML 解析成
  「逐块源文」（`work/source/chunks_src/*.md`），其中的 `$…$`、`$$…$$` 就是作者写的原始 LaTeX。
  **请逐字转写，不要凭记忆改写数学**。
- **实测统计**（`work/source/stats.txt`）：6 章正文 + 参考文献；共 246 个源块；
  独立公式（`$$…$$`）38 处；**编号公式 0 条**；定理类环境 62 个；证明 12 个；
  表格 3 张；交换图 3 个（q.uiver.app 嵌入，用 tikz-cd 重画）；**插图 0 张**（`<img>` 标签数 0）。
- 底本**没有页码**。因此本工程用「**源块编号**」代替页码作为定位与验收锚点，见 §8。
- 底本章号：Introduction = 第 1 章，Lagrangian Torus Fibrations = 第 2 章，
  SYZ Mirror Symmetry for Toric Fano Varieties = 第 3 章，
  Focus-focus Singularities and Almost Toric Fibrations = 第 4 章，
  SYZ Mirror Symmetry for Toric Varieties, Continued = 第 5 章。
  卷首的 Overview 无章号，用 `\section*`（不编号，但进目录）。

## 1. 可用素材（全部在 `<本地路径>`）

| 路径 | 内容 |
|---|---|
| `source/chunks_src/<你的片段>.md` | **你的源文**：逐块给出，每块以 `<<Bnnn kind>>` 开头。逐块翻译、逐块登记。 |
| `source/blockmap.tsv` | 全部 246 块的总表（id / 章 / 类型 / 摘要）。 |
| `source/sections/NN_*.md` | 整章源文（查上下文用）。 |
| `glossary.tsv` | 术语冻结表（制表符分隔：英文 TAB 中文）。 |
| `src/preamble.tex` | 导言区（Lead 独占）。**你只读，不得修改。** |
| `src/chunks/*.tex` | 你的输出文件。 |
| `STYLE_GUIDE.md` / `BRIEF.md` / `TIMELINE.md` | 本文件 / 分工与边界 / 边界裁决。 |

源块类型（`<<Bnnn kind>>` 里的 kind）：
- `p` 普通段落；`li` 列表项；`h3` 小节标题（原文 `<h3>`）；
- `env` 定理类环境，正文以 `**Definition.**` / `**Theorem(Name).**` 之类粗体标签开头；
- `prf` 证明（`**Proof.**` / `**Sketch of Proof.**`）；
- `table` 表格（已给成 `| … | … |` 行）；`quiver` 交换图（给的是 q.uiver.app 的 URL）。

## 2. 片段规则（硬性）

- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\def`、
  `\title`、`\tableofcontents`、`\section*`（除 BRIEF 明确授权你写章标题的情况）。
- 文件写到 `work/src/chunks/<片段名>.tex`（UTF-8 **无 BOM**、**LF** 换行）。文件名由 BRIEF 指定。
- 层级：章 = `\section{…}`，小节 = `\subsection{…}`。**只有 BRIEF 指定的「章首片段」写 `\section`**，
  同章的其他片段**不要**再写 `\section`。
- 段落之间空一行。不要写 `\par`。不要用 markdown 的 `**粗体**`（会原样印出星号）。
- 原文粗体小标题/整句粗体 → `\textbf{…}`；原文斜体 `_…_` → `\emph{…}`。
- 原文列表（`-`）→
  ```latex
  \begin{itemize}[leftmargin=1.4em,itemsep=1pt,topsep=2pt]
    \item …
  \end{itemize}
  ```
  有序列表用 `enumerate`，同样带 `[leftmargin=1.4em,itemsep=1pt,topsep=2pt]`。
- 原文引用 `[[Kon94]]`、`[CO06]`、`[[Eva23], Chapter 6]` → **纯文本** `[Kon94]`、`[CO06]`，
  不要 `\cite`，不要加链接。
- 中文标点：句号「。」、逗号「，」、顿号「、」、书名号「《》」；数学环境内用英文标点。
  破折号用 `---`，范围号用 `--`（如 `[45--54]`），**不要**直接敲 U+2013/U+2014。

## 3. 定理类环境（底本无编号，一律用无编号环境 + 可选作者名）

| 源块标签 | 写法 |
|---|---|
| `**Definition.**` | `\begin{definition*} … \end{definition*}` |
| `**Theorem.**` / `**Theorem(Name).**` | `\begin{theorem*}[Name] … \end{theorem*}` |
| `**Lemma.**` / `**Proposition.**` / `**Corollary.**` | 对应的 `lemma*` / `proposition*` / `corollary*` |
| `**Remark.**` / `**Example.**` / `**Exercise.**` / `**Statement.**` | `remark*` / `example*` / `exercise*` / `statement*` |
| `**Definition/Proposition(Batyrev).**` | `\begin{definition*}[Batyrev；原文标为 Definition/Proposition]`（保留原文的双重身份） |
| `**Proof.**` | `\begin{proof} … \end{proof}` |
| `**Sketch of Proof.**` | `\begin{proof}[证明梗概] … \end{proof}` |
| 其他粗体标题句（如 `**Topological monodromy on torus bundle.**`、`**Nodal integral affine structure.**`） | **不是定理环境**，用 `\para{拓扑单值化。}` 或直接 `\textbf{…}` 行内强调，按语义判断 |

- 作者名/文献名在可选参数里照译或保留原文（人名保留拉丁字母，如 `[Bondal--Orlov]`）。
- `\begin{theorem*}` 与正文之间空一行；环境内容**必须完整**（不许把环境截断到别的文件里）。

## 4. 公式（本工程最关键的一条）

- 底本**没有任何编号公式**，也**没有任何 `\tag`**。因此：
  **不许出现 `\tag`、不许自造编号、不许写 `\label{...}` / `\ref` / `\eqref`。**
- `$$ … $$` → 独立公式：
  ```latex
  \[
    …
  \]
  ```
  多行/需要对齐时用 `align*` / `gather*` / `multline*`（**带星号**，不编号），换行用 `\\`，
  对齐点用 `&`。**不要**用 `$$` 或 `eqnarray`。
- 行内 `$…$` 原样保留（可整理空格，但符号一个不能变）。`\big/`、`\big(` 等保持原样。
- 上下标、希腊字母、花体（`\mathcal`）、哥特体（`\mathfrak`）、正体（`\mathrm`/`\operatorname`）
  **逐个字符**照抄源文；注意 `\check{X}`（镜像空间）、`\Bbbk`（基域）、`\ast`、`\dotsb`。
- 源文中的宏已全部在 preamble 定义或为标准宏（含 `\Hom`、`\ev`、`\hol`、`\Bbbk`）。
  **不要自造 `\newcommand`**；确需新宏时在回执里报告，由 Lead 加进 preamble。
- 源文已知瑕疵（**照译，不许自己改数学**）：
  `\espan` 应为 `\operatorname{span}`（第 2 章）。转写时写成 `\operatorname{span}`，
  并在该处加 `% [Tutor Note: 底本源文作 \espan，应为 span 之意；已按 span 排印]`。
- 文本层里若出现 `\dotsb,` 之后缺空格、`(\mathfrak{m}^1 )^2` 之类多余空格：可清理空格，不改符号。

## 5. 表格与交换图

**表格**（全工程 3 张，BRIEF 指定归属）：
```latex
\begin{table}[htbp]
\centering
\small
\begin{tabular}{lll}
\toprule
… & … & … \\
\midrule
… & … & … \\
\bottomrule
\end{tabular}
\tabtitle{1}{讨论班日程}
\end{table}
```
列格式按内容定（`lll`/`llc`/`p{…}`）；表格里出现数学必须用 `$…$`；`\tabtitle{编号}{表题}` 手工编号，
编号次序按 BRIEF 指定的「表 1 / 表 2 / 表 3」。

**交换图**（全工程 3 个，都在第 2 章，由 tr-02 负责）：用 `tikz-cd`，
节点标签、箭头方向、箭头标签**一个不差**照 BRIEF 给的结构写。样式示例：
```latex
\begin{tikzcd}
  M \arrow[r, "G"] \arrow[dr, "H"'] & \R^n \\
  & \R^n \arrow[u, "\psi"']
\end{tikzcd}
```
- 需要曲线箭头时用 `\arrow[rr, "\pi", bend left=20]` 之类；需要点线用 `dotted`。
- 节点标签含中文时照常写；数学标签用 `$…$`（tikz-cd 里标签会自动进数学模式，**不要**给整个标签套 `$`）。

## 6. 批注（Tutor Note）

格式固定为 **LaTeX 注释行**，编译后不显示：
```latex
% [Tutor Note: ……]
```
要求：
- **密度：每个片段文件 ≥ 3 条；全工程 ≥ 30 条**。位置紧跟被注释的段落/公式之后。
- 内容必须是以下之一（**不许写空话、不许凑数**）：
  1. **可验证的易错点**：给出核对方法/数值锚点（如「取 $n=1$ 退化到一维验证」）；
  2. **补出的省略论证**：作者写 "it is easy to see / one can show" 而跳过的地方，指出用了哪条定理；
  3. **原文笔误**：必须给正确形式 + 判断依据（上下文自洽/文献对照/量纲），并同步写进回执；
  4. **术语首现**：给英文原词（首次出现处）；
  5. **译文取舍**：某句多义时说明为何这样译。
- 批注里可以有 `$…$`，但**不得出现不成对的 `$`**（自检脚本会误报）。
- 批注要具体到**源块编号**，例如 `% [Tutor Note: B062 的 $\mu(u)=2\sum_i(u\cdot D_i)$ 中的 2 来自 Maslov 指标的标准化约定]`。

## 7. 禁止事项（违反即返工）

1. 不改原文内容：**不删、不增、不"顺手修正"正文**；原文有误 → 照译 + 批注 + 回执报告。
2. 不编造：图、表、公式、文献、作者没说过的结论，一个字都不加。底本无图，**不许自己造图**。
3. 不用 `\newcommand`、不改 preamble/main、不编译（编译由 Lead 统一做，避免编译目录互相踩）。
4. 不用 markdown 语法（`**`、`##`、`>` 引用块、`- ` 列表须转成 LaTeX 环境）。
5. 不留未翻译的整句英文（专有名词、人名、模型名、缩写如 SYZ/HMS/CFT/LG 可保留）。
6. 不写「本节重点」「小结」之类原文没有的章节。
7. 不写 `\tag`、`\label`、`\ref`、`\eqref`、`\cite`、`\bibliography`。

## 8. 定位与验收锚点（代替页码）

- 每个**源块**翻译完，在该块译文的**紧前面**写一行：
  ```latex
  % [源 B062]
  ```
  （`B062` 用你源文件里的块号；**每块恰好一次**，不缺、不重、不跳。`h3` 块用于 `\subsection`，
  也要写 `% [源 Bnnn]`。）
- 每个片段文件开头写：
  ```latex
  % ===== 底本 第 N 章《章名》；片段 tr0Xa；源块 Bxxx--Byyy =====
  ```
- 这是 **Gate 0** 的机器可验指标（`check.py` 会比对全部 246 个块是否都被覆盖且恰好一次）。

## 9. 边界规定

- 你的片段从句子中间开始时：**直接从该处续写**，不要重写上文，也不要删。
- 跨块句子「开始者写完」；块边界以 BRIEF 给出的首尾锚点为准。
- 定理/环境的 `\begin`/`\end` **不许跨文件**：若一个环境正好被块边界切开，由**开始它的那位**写成完整环境
  （必要时把该环境的内容看全），并在回执里说明。
- 边界有歧义：**宁可多读一段源文**（`source/sections/NN_*.md`），并在回执里说明。

## 10. 自检清单（提交前逐项过；`check.py` 会再查一遍）

- [ ] 分配的源块**全部**覆盖，每块恰好一行 `% [源 Bnnn]`，无多余、无自造块号；
- [ ] 每个 `$$…$$` 都转成了 `\[…\]`/`align*` 等，符号逐字核对（上下标、指标、花体、正体）；
- [ ] 无 `\tag`、`\label`、`\ref`、`\eqref`、`\cite`、`\newcommand`、`\documentclass`、`\usepackage`；
- [ ] 花括号平衡、`\left/\right` 配对、`\begin/\end` 配对（同名同数）、`$` 成对；
- [ ] 中文标点规范；无 U+FFFD 乱码；UTF-8 无 BOM、LF；
- [ ] 批注数量达标（≥3 条/文件），且每条都具体、可验证；
- [ ] 覆盖本块全部正文、脚注、列表、表格、交换图、小节标题；
- [ ] 术语与 `glossary.tsv` 一致（新术语回执报告）。

## 11. 回执格式（发给 Lead 的消息，固定 5 项）

1. **文件**：写了哪些 `.tex`，覆盖源块区间（如 `B012–B023`）；
2. **公式**：转写了几处独立公式 / 是否有拿不准的符号（点名块号）；
3. **原文可疑/笔误**：块号 + 原文 + 判断依据（没有就写「无」）；
4. **新增术语**：英文 → 中文（没有就写「无」）；
5. **自检结果**：§10 清单逐项 pass/fail（`check.py` 若已由 Lead 跑过，写 Lead 的结论）。
