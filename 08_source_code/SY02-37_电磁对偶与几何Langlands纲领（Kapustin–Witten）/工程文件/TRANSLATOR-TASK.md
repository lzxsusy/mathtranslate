# KW06 分片翻译任务单（发给每个译者智能体）

## 0. 一分钟背景

底本：Anton Kapustin & Edward Witten, *Electric-Magnetic Duality And The Geometric Langlands Program*,
arXiv:hep-th/0604151v3（2007-01-16），231 页，12 节，146 篇参考文献。

工程根目录（所有相对路径都相对它）：`C:\Users\admin\Downloads\KW06_work\`

- `skel/NN-sXX.tex` —— **从 arXiv harvmac 源码自动生成的英文 LaTeX 脚手架**（公式、编号、`\label`、`\cite` 已全部就位，可直接编译）。分片编号 NN 是 01–36，sXX 是节号。你只译英文散文，**不动数学**。
- `zh/NN-sXX.tex` —— 你要写的**中文译稿**（目录已建好）。文件名与 skel 一一对应。
- `logs/NN-sXX.md` —— 你要写的**分片日志**（目录已建好）。
- `brief/SPEC.md` —— 体例硬规范，**必读**。
- `brief/GLOSSARY.tsv` —— 111 条术语强制译法，**必读**，遇到表内词必须照用。
- `brief/SECTION-MAP.md` —— 12 节 ↔ 原文印刷页 ↔ PDF 页 ↔ 分片 ↔ 任务。
- `brief/reading/witten2008.txt` —— Witten 2008 短综述（13 页，arXiv:0802.0999）**开工前必读**。
- `brief/reading/frenkel2009.txt` —— Frenkel 2009 综述《规范场论与几何朗兰兹纲领》（32 页，arXiv:0906.2747）**开工前必读**。
- `kw06_pages/pNNN.txt`（`C:\Users\admin\Downloads\kw06_pages\`）—— 原文逐页 pdftotext 文本，核对段落用（PDF 页 = 印刷页 + 1）。

## 1. 开工前的强制阅读（顺序）

1. `brief/BRIEF.md`（5 分钟，看任务与验收）
2. `brief/SPEC.md`（体例，逐条照做）
3. `brief/GLOSSARY.tsv`（把表扫一遍，记不熟的术语）
4. `brief/reading/witten2008.txt` —— **通读**：这是同一作者对同一批思想的短综述，给你全局物理图像。
5. `brief/reading/frenkel2009.txt` —— **通读**：这是数学侧（几何 Langlands）的权威综述，给你每个几何对象的标准名称与动机。
6. 你分到的 `skel/NN-sXX.tex` 全部内容（先通读再落笔；SPEC 第一条就是「先通读后落笔」）。

> 这两篇综述不是装饰：KW06 的很多段落是「物理直觉 + 数学陈述」交替的，读过综述才知道作者在类比什么。
> 读的时候在日志里记：读了哪几节、哪几页印象最深。**日志要真实**，没读就不要写读过了。

## 2. 每片的翻译动作

对每一个 `NN-sXX.tex`：

1. 读 `skel/NN-sXX.tex` 全文。
2. 写 `zh/NN-sXX.tex`：
   - **逐段 1:1**：原文一段 → 译文一段，不合并、不省略、不追加（SPEC §1）。
   - **数学一字不改**：所有 `$...$`、`\[...\]`、`equation`/`aligned`/`matrix`/`cases` 内容、`\setcounter`、`\label`、`\tag*`、`\cite`、`\eqref`、`\ref`、`\footnote` 的结构与位置全部保持原样。中文只能出现在 `\text{}` 或 `\mbox{}` 里，**不能**出现未包裹的中文在数学环境。
   - **公式编号注释 `% 式 (2.15)` 必须原样保留**（这是锚点，`tools/check_zh.py` 会核对数量）。
   - 术语：`GLOSSARY.tsv` 里的词照用；表中没有的，首次出现写「中文（English）」形式并登记到日志术语表。
   - 标题：`\section{}`/`\subsection{}` 译成中文，`\label` 不动。
   - 图表 caption 译成中文，保留结尾「（原文 Fig.~N）」/「（原文 Table~N）」。
   - 原文笔误/自相矛盾处：照录原意，然后在 `yizhu` 里以「[原文疑误]」开头说明。
3. **`yizhu` 译注盒**：每片 3–8 条，放在该片末尾（用 `\begin{yizhu}...\end{yizhu}`，preamble 已定义橙框）。四类，按需选用：
   - 「易错点」——中英术语陷阱、公式里容易看漏的符号；
   - 「含糊点拨」——原文一句话背后省略的推理（补一句为什么）；
   - 「物理图像」——把数学对象对应回规范场/膜的操作（读过 Witten 2008 就能写）；
   - 「原文疑误」——照录后指出可能笔误。
   补白一律以「按：」起首。来源等级（可选标注）：`[A]` 原始文献/`[B]` 权威综述或 nLab/`[I]` 译者推断。
4. **`keytakeaways`**：**只在该节第一片**（`SECTION-MAP.md` 里标了「节首」的那片）的 `\section` 之后写 3–5 条（物理图像/数学工具/关键结论/边界展望）。其余片不写。
5. 写 `logs/NN-sXX.md`（模板见 SPEC §8）：覆盖情况、自检清单、P1/P2 问题、术语决定、**检索记录**。

## 3. 自检（必做）

```bash
cd /c/Users/admin/Downloads/KW06_work
export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"
"/c/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe" tools/check_zh.py NN-sXX
```

输出 `0/1 zh 文件有问题` 才算过。它会同时检查：能否编译、禁用命令、Unicode 数学符号、
`% 式 (N)` 锚点数、`\setcounter`/`\label`/`\cite` 数是否与 skel 一致。

## 4. 检索（遇到拿不准的术语/数学事实时）

允许并鼓励，但**只记真实发生过的**：

- 本地 nLab 索引：`C:\Users\admin\Downloads\无穷范畴参考资料\nlab-pages.tsv`（20215 条，`grep -i "hitchin" ...`）
- 本地知识库：`node C:\Users\admin\Downloads\kb-redesign\bin\kb.mjs locate "Hitchin fibration"`
- 网络：`web_search`（关键词）、`web_fetch`（arXiv abstract / ncatlab.org 页面）
- 禁止来源：知乎、百度、CSDN、简书、微信公众号、B 站、个人博客（SPEC 黑名单）。

日志里写清：查了什么、用什么查的、结论是什么、是否改变了译法。

## 5. 交付纪律

- **只写你自己的文件**：`zh/<你分到的 NN-sXX>.tex` 与 `logs/<同名>.md`。不要改 `skel/`、`preamble.tex`、`macros*.tex`、别人的文件。
- 不新建目录、不改工具脚本。
- 全部写完后，在最终回复里逐片汇报：文件名、字符数、`check_zh` 结果、yizhu 条数、检索了几次、有什么 P1 级遗留。
