# STYLE_GUIDE —— 植田一石《ホモロジー的ミラー対称性》中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，保留权利，仅限非商业学术研读，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

（Lead 独占维护；译者只读，**不得修改**本文件、`src/preamble.tex`、`src/main.tex`）

## 0. 底本（实测）

- 原文：植田一石（Kazushi Ueda）《ホモロジー的ミラー対称性》，东京大学大学院数理科学研究科 2015 年度冬学期讲义录，PDF **64 页**。
- 底本文件：`src/植田一石_ホモロジー的ミラー対称性_原文.pdf`。
- **页映射：PDF 页号 = 原文页码**（第 1 页底部印 “1”），无偏移。
- 结构：**34 节 + 参考文献**。节标题见 `work/BRIEF.md` 的表；*节号来自原文*，`\section` 自动编号应与之一致。
- **编号公式 371 条**，形如 `(2.1)`, `(18.11)`, `(30.26)`；`work/tags.txt`（tag→页）、`work/tags_bypage.txt`（页→tags）是抽样清单，**可能有漏检/误检，以页面图像为准**。
- 图共 **11 幅**：图 13.1–13.2（p22）、17.1–17.3（p29）、31.1–31.4（p44）、32.1–32.2（p46）。图注形如 `図 13.1: 消滅経路の特集合`。

## 1. 可用素材（全部在 `work/`）

| 路径 | 内容 |
|---|---|
| `work/pages/pNNN.png` | 逐页 150 dpi 渲染图（NNN = 三位页号）。**公式的唯一真值。** |
| `work/split/pNNN.txt` | 逐页文字层。正文词句可参考；**数学符号一律不可信**（上下标错位、希腊字母错、花体丢字形、分式拆散）。 |
| `work/full.txt` | 整本文字层（检索用）。 |
| `work/tags.txt` / `work/tags_bypage.txt` | 编号公式清单（抽样）。 |
| `work/figs.tsv` | 图标题清单。 |
| `work/glossary.tsv` | 术语冻结表（日文\t中文）。**必须遵守**。 |
| `work/tools/crop.py` | 裁图脚本（从页面 PNG 裁出插图）。 |
| `src/preamble.tex` | 导言区。**只读。** |
| `src/chunks/*.tex` | 译者输出文件（见 BRIEF 分工）。 |

**文字层可靠度**：✅ 正文单词、段落边界、脚注、节标题、定理名；❌ 一切数学（必须逐页看 `pages/pNNN.png` 逐符号抄）。

## 2. 片段规则（硬性）

- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、`\tableofcontents`。
- 输出到 BRIEF 指定的 `src/chunks/cNN.tex`（UTF-8 无 BOM、LF 换行）。一个 chunk 通常一个文件；过长可拆 `cNN-a.tex`/`cNN-b.tex`，但**要告诉 Lead**。
- `\section{…}` = 原文「**N 标题**」。**节标题只由该节起始页所属块写一次**；若你负责的页里出现的是前一节的续文（没有节标题行），**不要**再写 `\section`，直接接续正文即可。
- 段落之间空一行；不要写 `\par`；不要用 markdown 粗体。
- 原文行内粗体小标题 → `\para{标题。}`。
- 脚注：`\footnote{…}` 就地写。原文脚注编号自动生成，不必管原编号。
- 定理类环境：用 preamble 定义的环境（见 §4），**不要手写** `\textbf{定理 30.3.}`。原文编号与自动编号若对不上，保留原文编号含义，并在 `% [Tutor Note: …]` 注明。

## 3. 公式（最关键）

- **编号公式必须与原文一一对应**：不缺、不重、不跳、不重排、不自造：
  ```latex
  \begin{equation}
      \sum_{i=1}^{k} w_i n_i = 0 \tag{2.4}
  \end{equation}
  ```
  多行用 `align`/`gather`，每个编号一行一个 `\tag{}`；一条编号跨多行时只在最后一行 `\tag`。
- 原文大量公式**没有编号**：用 `\[ … \]` 或 `equation*`，**绝不自己加编号**。
- 正文引用写纯文本：「式 (2.4)」「§30」「图 13.1」；不要 `\ref`/`\eqref`。
- 文献引用写纯文本：`[GSW87]`、`[FJR13, PV]`；不要 `\cite`。
- 微分 `\dd`、偏导 `\partial`、花体 `\cO`、黑板体 `\R \C \Z \PP`；分式/根号/上下标/指标位置逐符号核对图像。

## 4. 宏与环境（preamble 已定义，不要自造）

- 集合：`\R \C \Z \N \Q \PP`；花体：`\cA … \cZ`；哥特：`\fg \fM \fT \fX \fY \fZ`
- 算子：`\dd \ee \ii \id \rank \Hom \End \Ext \Tot \Spec \Coh \Perf`
- 定理类（**同一节共享计数器**，直接用）：
  `definition`（定义）、`theorem`（定理）、`proposition`（命题）、`lemma`（引理）、
  `corollary`（推论）、`example`（例）、`remark`（注）、`notation`（记号）、
  `construction`（构造）、`claim`（断言）、`question`（问题）、`exercise`（习题）
- 图：`\begin{figure}[htbp]\centering\includegraphics[width=0.7\textwidth]{figures/fig13.1.png}\figtitle{13.1}{消没路径的临界集}\end{figure}`
- 表：`booktabs` 三线表 + `\tabtitle{1}{…}`。
- 译者注：`\transnote{…}`（**仅**在必要处：原文明显笔误、术语有歧义、需要补一句背景时；不要滥用）。

## 5. 术语

- **以 `work/glossary.tsv` 为准**；表里没有的，按下列原则：数学术语用中国大陆通行译名；专有名词（人名、理论名）保留原文/英文；首次出现可在括号中附原文，如「相干层（連接層）」。
- 日文汉字 ≠ 简体：幾何→几何、函数→函数、解析→解析、複素→复、実→实、体→域（体=field 时译「域」）、環→环、束→丛（fiber bundle）、層→层、圏→范畴、関手→函子、射→态射、核→核、余核→余核、直和→直和、双対→对偶、変異→变位、例外→例外、半直交→半正交、完全→正合（exact 时）。
- 人名：Kontsevich、Fukaya（深谷賢治）、Seidel、Lefschetz、Hitchin、McLean、Berkovich、Liouville、Arnold 等照原文拼写；日本人名用汉字（深谷、植田、高橋、入谷、梶浦、野原、秦泉寺）。

## 6. 批注体例

- 对原文的疑问（疑似笔误、符号冲突、缺失引用）一律写成独立行注释：
  ```
  % [Tutor Note: 原文 (18.7) 的符号似应为 …，此处按原文保留，请审校确认。]
  ```
- **绝不**把「我觉得」写进正文；**不**补写原文省略的论证。
- 每完成一个 chunk，在文件末尾写一行：`% CHUNK cNN DONE pages pXXX–pYYY`

## 7. 自检（交付前逐条走）

1. `grep -c "\\\\tag{" 你的文件` 与该 chunk 的 tag 数（BRIEF 有给）是否一致（允许 ±0）。
2. 所有 `\begin{…}` 有对应 `\end{…}`；`\left(`/`\right)` 配对。
3. 没有中文全角括号误用于数学、没有 markdown 语法残留。
4. 每个 `\section` 只在节起始页出现一次。
5. 输出文件用 UTF-8 无 BOM 保存。
