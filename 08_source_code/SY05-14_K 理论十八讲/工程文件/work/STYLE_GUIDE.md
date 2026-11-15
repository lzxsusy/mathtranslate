# STYLE_GUIDE —— 《18 Lectures on K-Theory》(Zois, 2010) 中文译注 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：全库统一 CC BY 4.0，明确欢迎用于训练、蒸馏与商用（署名即可）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（v1.0 / Lead 独占维护，队友只能读，不得修改）

## 0. 底本（实测，勿再猜）

- 原文：Ioannis P. Zois, *18 Lectures on K-Theory*, arXiv:1008.1346v1 [math.KT]，137 页，Letter 纸（612×792 pt）。
- PDF：`<本地路径>).pdf`
  （与 `拓扑K理论讲义\pdfs\04_Zois_18_Lectures_on_K-Theory_2010.pdf` 同一文件，588,443 bytes）。
- **页码对应：PDF 页号 = 原文印刷页码（偏移 0）**。
- **实测**：位图 0 张、插图 0 张、表 0 张；**编号公式 0 条**（全文右栏 `(x.y)` 扫描为 0，展示式一律居中不带号）；
  编号定理类（定义/命题/引理/定理/推论/注/断言）**每个 section 内重新从 1 编号**，如 p.8 的「Definition 1.」「Definition 2.」。
- 全书 22 个 `\section`（编号 1–22）：1 为「Topological K-Theory」总起，2–7 拓扑 K 六讲，8 为解析 K 总起，
  9–14 解析 K 六讲，15 为高阶代数 K 总起，16–21 六讲，22 为附录；pp.134–137 为 References（不译，英文原貌）。
- pp.1–3 为标题页与目录，pp.4–7 为「Introduction and background Bibliography」（要译），pp.8–133 为正文与附录。

## 1. 可用素材（全部在项目 `work\` 下）

| 路径 | 内容 |
|---|---|
| `pages/pNNN.png` | 逐页 200 dpi 渲染图（NNN = 三位页号）。**公式与定理编号的唯一真值。** |
| `split/pNNN.txt` | 逐页 PDF 文字层。正文词句可信，**数学符号一律不可信**。 |
| `full.txt` | 整本文字层（检索用）。 |
| `tags.txt` / `tags_bypage.txt` | 空文件（原文无编号公式，属正常）。 |
| `glossary.tsv` | 术语冻结表（制表符分隔：英文 \t 中文）。 |
| `src/preamble.tex` | 导言区（Lead 独占）。**你只读，不得修改。** |
| `src/chunks/…` | 你的输出文件。 |
| `tools/crop.py` | 放大核对公式用（见 §1bis）。 |

### 1bis. 看不清公式时怎么放大

```powershell
$py = "<本地路径>"
& $py "<项目根>\work\tools\crop.py" <页号> <x0> <y0> <x1> <y1> "<项目根>\work\tmp\zoom.png" [dpi 默认 500]
```
坐标是 PDF 点（整页 612×792）。裁完用 `read_image` 看一眼确认。

### 1ter. 文字层的坑（本稿实测，务必记住）

1. **连字**：`ﬁ`、`ﬂ`、`ﬀ` 是单个 Unicode 字符，`Deﬁnition` 不是 `Definition`。不要据此判断原文拼写。
2. **公式被拍平**：`K(X)` 抽成 `KX`，`\tilde K` 抽成 `˜K`，`\bigsqcup` 抽成 `a`，`\prod` 抽成 `Q`，
   `\mapsto` 抽成 `7→`，上标 `x^{-1}` 抽成 `x−1`，`\mathbb{R}` 抽成 `R`，`\mathcal` 抽成普通字母。
   → **凡公式，一律看 200 dpi 页图逐符号抄，不得直接抄文字层。**
3. **粗体标题丢空格**：`TopologicalK-Theory`、`Vec-torBundles` 是抽取问题，按页图补空格与断词。

## 2. 片段规则（硬性）

- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、`\tableofcontents`。
- 文件写到 `work/src/chunks/trNNa.tex`（UTF-8 无 BOM、LF 换行）。**不要**动别人的 chunk、`preamble.tex`、`main.tex`。
- 章节层级：`\section{…}`；**只写 BRIEF §3 指名归你的标题**，其余标题一律不写（否则编号整体错位）。
- 段落之间空一行。不要写 `\par`。不要用 markdown 语法（`**粗体**`、`##` 会原样印出）。
- 原文的行内粗体小标题（独立成段的 "**Lemma.** …" 之类）用 `\para{…}`；句中强调用 `\emph{…}`（原文斜体）。
- 原文的方括号文献引用（如 `[Atiyah]`、`[Bott]`、`[Milnor]`）**照抄英文方括号**，不要改成 `\cite`，不要翻译键名。
- 原文的列表编号（`1.` `2.` `3.`、`i.` `ii.`）保留原编号：用 `\begin{enumerate}[label=\arabic*.]` 或
  `[label=\roman*.]`；原文如果编号是手写死的，也可直接写成正文「1. …」换行，但**必须与页图一致**。

## 3. 公式（本工程最关键的一条）

- 原文**没有任何编号公式**。因此：
  - **绝不允许**写 `\tag{}`、不要用 `equation`/`align` 的自动编号；展示式一律 `\[ … \]`；
  - 正文引用公式写纯文本「式 (3.2)」之类（本稿基本用不到）。
- 所有展示式**逐符号照原文重排**：
  - 矩阵用 `\begin{pmatrix} … \end{pmatrix}`；
  - 分段函数用 `\begin{cases} … \end{cases}`；
  - 交换图/图表（如六项正合列、纤维化图）用 `tikzcd`：
    `\begin{tikzcd} A \arrow[r,"f"] \arrow[d,"g"'] & B \arrow[d] \\ C & D \end{tikzcd}`，
    `baseline` 只许写 `(current bounding box.center)`；
  - 长公式若超过版心宽度，用 `\[ \resizebox{0.98\textwidth}{!}{$\displaystyle …$} \]` 或 `multline`，但不得改变内容。
- **上下标、花体、希腊字母必须与 200 dpi 页图逐个对照**：`\mathcal` vs 普通、`\bar`/`\tilde`/`\widetilde`、
  `\hat`、`\mathbb{R}` vs `R`、`\varphi` vs `\phi`、`\varepsilon` vs `\epsilon`、`\cong`/`\simeq`/`\approx`、
  `\hookrightarrow`、`\twoheadrightarrow`、`\xrightarrow{f}` 等。
- `\left(` / `\right)` 必须配对；不要用 `$$…$$`；数学环境内用英文标点。

## 4. 宏（preamble 已定义，直接用；**不要自造** `\newcommand`）

- 集合与数系：`\R \C \Z \N \Q \HH \F`（`\F` = 原文的 $\mathbb F$，表示 $\R$ 或 $\C$）
- 算子（正体）：`\GL \SL \SO \SU \U \OO \Hom \End \Aut \Ext \Tor \Tr \ch \ind \rk \sgn \id \im \coker \dd`
- 常用：`\Vect \VectC \Cstar`（= $C^*$）、`\ie \eg \cf`、`\xra`（$\xrightarrow{}$）、`\into`（$\hookrightarrow$）、
  `\onto`（$\twoheadrightarrow$）、`\ot`（$\otimes$）、`\semi`（$\rtimes$）、`\wt`（宽波浪号 `\widetilde`）
- 定理类环境（**编号手工给，号数照原文，每个 section 从 1 重新起**）：
  ```latex
  \begin{defn}{1} … \end{defn}      % 定义 1.
  \begin{prop}{1} … \end{prop}      % 命题 1.
  \begin{lem}{1}  … \end{lem}       % 引理 1.
  \begin{thm}{2}  … \end{thm}       % 定理 2.
  \begin{cor}{1}  … \end{cor}       % 推论 1.
  \begin{rem}{1}  … \end{rem}       % 注 1.
  \begin{claim}{3} … \end{claim}    % 断言 3.
  \begin{proof} … \end{proof}       % 证明. …… □
  ```
  原文的 "Definition 1." "Proposition 2." "Remark 1." "Claim 3." 一律按上述环境写；
  **原文没有编号的**（如 "Examples." "Examples 1." 之类若确无编号）用 `\para{…}` 或普通段落，不得自造编号。
- 其余符号用标准命令（`\bigoplus \bigotimes \bigsqcup \coprod \prod \sum \int \oplus \otimes \cong \simeq \subset` 等）。

## 5. 批注（Tutor Note）

格式固定为 LaTeX 注释行，编译后不显示：

```latex
% [Tutor Note: p.5 定义 3 里 ………]
```

要求（**密度：每 2 页至少 1 条，每节至少 3 条**；全书目标 ≥120 条）：
- **可验证的易错点**：给出核对方法或观察点（如「这里的 $\tilde K$ 是约化 K 群，与 $KX$ 的差别见 p.28 定义 2」）；
- **补出的省略论证**：作者写 "It is straightforward" / "we leave it to the reader" 而跳过的实际论证；
- **原文笔误**：必须给正确形式 + 判断依据，**并且先用 500 dpi 裁图复核原文**；正文照原样译；
- **术语首现**：给英文原词（glossary 里有的不必重复给）；
- **背景/直觉**：一两句，必须具体，禁止"很重要""值得注意"之类空话。
- 批注里可以有 `$…$`，但**不得出现不成对的 `$`**（自检脚本会误报）。

## 6. 页码标注

每进入新的一页（PDF 页），在内容前加一行注释：

```latex
% [原文 p.3]
```

片段开头再加一行：`% ===== 原文 pp.3–5 =====`。

## 7. 禁止事项（违反即返工）

1. 不改原文内容：**不删、不增、不"顺手修正"正文**。原文字句有误 → 照译 + 批注指出 + 给正确形式。
2. 不编造：图、表、公式、文献、作者没说过的结论，一个字都不加。
3. 不用 `\newcommand`、不改 preamble/main、**不编译**（编译由 Lead 统一做）。
4. 不用 markdown 语法。中文标点用「。，、；：？！（）「」」；数学环境内用英文标点。
5. 不留未翻译的整句英文（人名、书名、文献键、$C^*$、$K$-theory 之类记号可保留）。
6. 不写「本节重点」之类原文没有的框/标题；不给原文没有的段落加粗体标题。
7. 参考文献条目**不译**（Lead 统一转录）。

## 8. 边界规定

- 你的块**从 `\section{…}` 开始**（BRIEF §3 指名的标题），到下一页的下一个 `\section` 之前结束；
  最后一块到附录结束。
- 块首若从句子中部开始（只发生在同一 section 内的页边界）：**直接续写该句**，不要重写上文。
- 跨页句「开始者写完」（谁先开始这句谁负责写完）。
- 边界处若有歧义：**宁可多看一页图像**，并在回报里说明。

## 9. 自检清单（写文件前逐项过）

- [ ] 本块覆盖的每一页都有 `% [原文 p.N]` 标注，页段与 BRIEF 一致，无漏页；
- [ ] 本块负责的 `\section` 标题已写（且只写 BRIEF 指名的那些）；
- [ ] 每个展示式与 200 dpi 页面图像逐符号核对（上下标、希腊字母、花体、`\cong` 等）；
- [ ] 定理类编号与原文逐条一致（原文本节从 1 开始，缺号/跳号要写进回报）；
- [ ] 花括号平衡、`\left`/`\right` 配对、`\begin`/`\end` 配对、`$` 成对；
- [ ] 无 `\documentclass`/`\usepackage`/`\begin{document}`/`\newcommand`/`\tag`/`**`；
- [ ] 无 U+FFFD 乱码；UTF-8 无 BOM；LF 换行；
- [ ] 批注数量与质量达标（每 2 页 ≥1 条）；
- [ ] 术语与 `glossary.tsv` 一致，新术语写进回报。

## 10. 回执格式（发给 lead 的消息）

1) 完成文件与覆盖页段（p.X–p.Y）；
2) 本块包含的 `\section` 与定理类编号区间（如「定义 1–6，命题 1–2，定理 1」）及跳号/存疑；
3) 发现的原文可疑/笔误（页码 + 位置 + 判断依据）；
4) 新增术语（英文→中文）；
5) 自检确认结果（逐项 pass）。
