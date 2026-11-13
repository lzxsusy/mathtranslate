# BLOCK_TASKS.md — 译手任务书（Lead 独占维护；常驻，勿改）

本文件是每位译手的唯一任务说明。**开工前必须按顺序读完**：本文件 → `BRIEF.md` → `STYLE_GUIDE.md` → `TIMELINE.md` → `glossary.tsv`。它们全是硬性规范，冲突时优先级：`STYLE_GUIDE.md` > `BLOCK_TASKS.md` > `BRIEF.md` > `TIMELINE.md`。

工程根：`<本地路径>`（下文路径都相对它）。

## 0. 一句话

把 Kenji Ueno《Conformal Field Theory with Gauge Symmetry》(Fields Inst. Monogr. 24) 的**指定块**逐段译成中文 LaTeX 片段 `src/bNN.tex`，公式逐条从页面图抄写并保留原编号，写足够多的译注，交前自检到 `OK`，然后写报告并发消息。

## 1. 素材

- **原文页面图**：`pages\pNNN.png`，`NNN` 是 **PDF 页号**（三位，如 `pages\p010.png`）。**页码换算：PDF 页 = 印刷页 + 9**。
- 公式的**唯一真值**是页面图。`split\pNNN.txt` 是劣质 OCR（`∈`→`G`、`m`→`ra`、公式碎成单字符、随机空格），**只能用来定位段落，绝不能用来抄公式**。
- 看清小字/上下标：用 `crop.py` 放大
  ```
  python crop.py <PDF页> <y0> <y1> <out.png>              # 整宽纵向切片，y 为 0–1 的比例
  python crop.py <PDF页> <x0> <x1> <y0> <y1> <out.png>    # 矩形
  ```
  Python 解释器（含 pymupdf）：
  `<本地路径>`
  例：`& $py crop.py 35 0.05 0.35 tmp\c35a.png`，然后 `read_image` 看 `tmp\c35a.png`。
- Windows 上跑命令：`pwsh`，先 `cd <本地路径>`。

## 2. 产出

每个块**恰好一个文件** `src/bNN.tex`。文件结构：

```latex
% ===== Block B07: 原文 p.54–66 | §3.3 共形块空间的基本性质 | 译手 tr-ch3a =====
% [原文 p.54]
（p.54 的正文）
% [原文 p.55]
（p.55 的正文）
...
```

- 每页开头写一行 `% [原文 p.N]`（N = 印刷页号），表示"以下内容来自该页"。
- 块首若是小节开头，**写小节标题** `\subsection{共形块空间的基本性质}`（用字必须逐字照 `TIMELINE.md` 的「标准中文标题」表，编号让 LaTeX 自动生成，不要手写 `3.3`）。
- 块内出现下一个小节时，同样写 `\subsection{…}`，正文继续。
- 块尾不要写任何结束标记。

## 3. 硬性写法（违反即返工）

1. **逐段译**，不删句、不并段、不缩写；原文一句译一句，段落切分照原文。
2. **公式**：
   - 编号公式一律 `\begin{equation} ... \tag{1.1} \end{equation}`，编号**照原文**，不多不少不重排；原书是每章独立连续编号。
   - 多行公式用 `align`，**每行都带 `\tag`**（如 `\tag{2.14}`）；原文只有末行编号时，前面的行写 `\nonumber`。
   - 无编号公式用 `\[ ... \]`。
   - 正文引用公式写纯文本：「由式 (1.41) 可得」，禁用 `\eqref`、`\ref`、`\label`。
3. **环境**：`definition / theorem / proposition / lemma / corollary / example / remark`，编号**手工给**：
   `\begin{definition}[1.1] ... \end{definition}`。原书这些环境**共用一个章内计数器**，编号必须与原文一致。
   无编号的用星号环境：`\begin{theorem*}[?]` 不要加方括号，直接 `\begin{theorem*}...\end{theorem*}`。
   `Proof.` 译成「证明.」，结尾 `\hfill$\square$`。
4. **三级跑头**（如 `1.1.1 Compact Riemann surfaces.`）：写成
   `\noindent\textbf{1.1.1 紧黎曼曲面.}\quad` 然后紧接正文，**不要**用 `\subsubsection`。
5. **图**：一律不复刻，在原位置写 `\figomit{1.7}{图注译文}`（第一个参数是图号，第二个是图注中文）。
6. **表**：原文若有表格，用 `longtable`/`tabular` 朴素排出；不确定就把表内容改写成行文并加译注说明。
7. **数学里不许出现中文**（`\mbox{}`/`\text{}` 例外）；不许出现 Unicode 数学符号（≤ ≥ ≠ → ∈ ℂ ℝ 等），一律 `\le \ge \ne \to \in \C \R`。
8. **只用 `src/preamble.tex` 里已定义的宏**：`\dd \ee \ii \Tr \SL \GL \End \Aut \id \Hom \Sym \ad \rank \R \C \Z \Q \N \PP \HH \AA \cA...\cX \ol{} \eps \figomit{}`。**禁止** `\newcommand`/`\renewcommand`/`\DeclareMathOperator`/`\usepackage`/`\input`/`\section`/`\chapter`。需要新宏 → 报告 Lead。
9. **禁止**插图、造表、补文献、改正文观点、写 Markdown（不许出现 `**`）、写 `★★★` 之类的字符（`★` 正文无字形）。
10. 原文**笔误**（编号跳号、明显打错的符号）：照原文排，写一条译注指出正确形式，并在报告的 `ERRATA:` 里列出。**不要**擅自改原文。
11. 文件编码：UTF-8 **无 BOM**、行尾 **LF**。用 `write` 工具写通常没问题；若用脚本写，必须 `encoding="utf-8", newline="\n"`。

## 4. 译注（Tutor Note）——本工程的核心增值

在 LaTeX 注释里写译者按语，**不进排版**，格式：

```latex
% [Tutor Note: 这里用了 Cartan 分解，但没写为什么 $\hat{\mathfrak g}$ 的导子作用
%  保持最高权模；补一句：由 $\xi\,\dd/\dd\xi$ 的作用是半单的可得。原文 p.41]
```

每块 **8–20 条**（块小也不少于 8 条）。只写有信息量的四种：
(a) 可验证的易错点（符号、指标、归一化、$\pm$ 号）；
(b) 原文跳过的中间步骤（写出关键一步，不写整段证明）；
(c) 原文笔误；
(d) 术语/记号首次出现的说明与它后面在哪里被用到。
**不要**写"这段话说明了……"式的空话。

## 5. 术语

照 `glossary.tsv`（`英文<TAB>中文<TAB>备注`）。术语首次出现写成「共形块（conformal block）」，之后只用中文。表里没有的术语：自己定一个、全块统一，并在报告 `TERM:` 里列出「english => 中文」。人名不译（Kodaira、Hironaka、Verlinde、Hitchin 保持原样）。

## 6. 长块写作方式（避免一次写太多）

单块若超过约 4 页，**分段写**：先 `write` 前 2–3 页，文件末尾留一行 `% >>>END`；之后每次用 `edit` 把 `% >>>END` 替换成「新内容 + `% >>>END`」；最后把 `% >>>END` 删掉。每次写 2–3 页，写完立刻校对。**不要**把整块塞进一次输出（会截断）。

## 7. 自检（交付前必须做）

```powershell
cd <本地路径>
$py='<本地路径>'
& $py check_block.py src\b07.tex
```
必须看到 `OK`。报 `PROBLEM` 就按提示改到 `OK`（其它块的 `\tag` 连续性由 Lead 统一查，你不用管跨块）。
**不要**自己跑 xelatex（Lead 统一编译；你编译会和别人抢 log 文件）。

## 8. 报告

写 `block-reports/bNN.md`，用下面这个模板，**一条不落**：

```
DONE: B07 / src/b07.tex / 原文 p.54–66 (PDF 63–76) / 印刷页数 13 / \tag 条数 22 / 环境 9 个 / 图 1 个（\figomit）
BOUNDARY: 起 = §3.3 标题（p.54 顶），止 = §3.4 标题前（p.66 末）；p.66 末句 "..." 已译完（/ 留给 B08）
TERM: formal neighbourhood => 形式邻域；propagation of vacua => 真空传播
ISSUES: p.58 图 3.2 的配边箭头看不清，按文字描述译；p.61 式 (3.29) 第二个等号原文缺失，已照排并加注
ERRATA: p.60 "Theorem 3.14" 疑为 "Proposition 3.14"（原文编号跳号）
DIFFICULT:
- p.55 (3.1) 定义里 $\hat{\mathfrak g}_N$ 的作用为什么是良定义的，原文一句话带过，实际要检查 $\xi_j$ 的 Laurent 展开在 $\mathfrak g$ 上有限
- p.59 从 (3.26) 到 (3.27) 用了 Sugawara 构造，跳步 ★★
- p.63 因子化定理的证明引用 [TUY] 的结果，未给细节 ★★★
```

`DIFFICULT:` 是本工程**最重要**的字段：逐条列出「页码 + 公式/位置 + 一句话说明跳了什么、难在哪 + ★ 一至三颗（一跳步=★，要补论=★★，要外部定理=★★★）」。Lead 会据此写《脉络梳理》。宁多勿少。

写完报告后，**给 lead 发一条消息**（`send_message`，target `lead`）：只写 `DONE B07 | tags 22 | env 9 | fig 1 | ERRATA n | DIFFICULT m 条 | 一句话结论`。不要贴译文。然后**立刻开始你负责的下一个块**。

## 9. 块表（本文件为准，`TIMELINE.md` 同样有效）

| 块 | 文件 | 内容（到下一个标题前） | 印刷页 | PDF 页 |
|---|---|---|---|---|
| B01 | `src/b01.tex` | §1.1 紧黎曼曲面（起：§1.1 标题之后） | 1–17 | 10–26 |
| B02 | `src/b02.tex` | §1.2 稳定 $N$-点曲线（到 §1.3 前） | 17–25 | 26–34 |
| B03 | `src/b03.tex` | §1.3 带点曲线的形变（到 §1.4 前） | 25–31 | 34–40 |
| B04 | `src/b04.tex` | §1.4 稳定带点曲线的通用族（到第 2 章前） | 31–36 | 40–45 |
| B05 | `src/b05.tex` | 第 2 章全部（§2.1、§2.2 两个标题都在块内） | 37–46 | 46–55 |
| B06 | `src/b06.tex` | §3.1、§3.2（到 §3.3 前） | 47–54 | 56–63 |
| B07 | `src/b07.tex` | §3.3（到 §3.4 前） | 54–66 | 63–75 |
| B08 | `src/b08.tex` | §3.4（到第 4 章前） | 67–72 | 76–81 |
| B09 | `src/b09.tex` | §4.1、§4.2（到 §4.3 前） | 73–82 | 82–91 |
| B10 | `src/b10.tex` | §4.3（到第 5 章前） | 82–90 | 91–99 |
| B11 | `src/b11.tex` | §5.1、§5.2（到 §5.3 前） | 91–101 | 100–110 |
| B12 | `src/b12.tex` | §5.3、§5.4、§5.5（到 §5.6 前） | 101–116 | 110–125 |
| B13 | `src/b13.tex` | §5.6（到第 6 章前） | 116–130 | 125–139 |
| B14 | `src/b14.tex` | §6.1、§6.2（到 §6.3 前） | 131–140 | 140–149 |
| B15 | `src/b15.tex` | §6.3、§6.4（到 §6.5 前） | 140–151 | 149–160 |
| B16 | `src/b16.tex` | §6.5（到附录前） | 151–160 | 160–169 |
| B17 | `src/b17.tex` + `src/refs.tex` | 附录 p.161–162；参考文献 p.163–166 放 `refs.tex`；索引 p.167–168 **不译** | 161–168 | 170–177 |

- 块与块的分界**页**由双方共用：**各译各的，不跨界**；一句话被分页切开时，**开始它的那一块**负责译完。
- 章节标题（`\section`）由 Lead 写在 `main.tex`，**你不要写**；但块首若紧接小节标题，`\subsection` 由你写（见 §2）。
