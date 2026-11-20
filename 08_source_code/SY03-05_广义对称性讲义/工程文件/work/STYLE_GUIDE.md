# STYLE_GUIDE ——《广义对称性讲义》(arXiv:2307.07547v2) 中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（v1.0 / Lead 独占维护，队友只能读）

## 0. 底本（实测，勿再猜）
- 原文：L. Bhardwaj, L. E. Bottini, L. Fraser-Taliente, L. Gladden, D. S. W. Gould,
  A. Platschorre, H. Tillim, *Lectures on Generalized Symmetries*, arXiv:2307.07547v2 [hep-th], 8 Sep 2023。
- PDF：`<本地路径>`，**共 150 页**（页面 612×792 pt，Letter）。
- **页码对应：PDF 页号 = 原文印刷页码（偏移 0）**。正文 pp.1–138；pp.139–150 为致谢 + 参考文献（221 条，不译）。
- **实测**：位图 0 张；矢量图 28 张（Figure 1–28，位置见 BRIEF）；表 1 个（Table 1，p.47）。
- **编号公式共 745 条**：§2: 2.1–2.109；§3: 3.1–3.221；§4: 4.1–4.267；§5: 5.1–5.94；§6: 6.1–6.54。
  清单：`work/tags.txt`（tag→页）、`work/tags_bypage.txt`（页→tags）。**这是验收唯一依据**。
- 原文有 5 种彩色方框（见 §7）：蓝色 **Statement 2.1/2.2/4.1–4.12**、绿色 **Definition 2.1/3.1–3.2/4.1–4.9/5.1–5.2**、
  橙色 **Example 2.1/2.2/2.3/3.1–3.12/4.1–4.19/5.1–5.5/6.1–6.4**、粉色带标题注释框（无编号）、无标题细边框。
- **无**习题、**无**附录、**无** \part。章节结构见 BRIEF 的分工表。

## 1. 可用素材（全部在 `<本地路径>`）
| 路径 | 内容 |
|---|---|
| `pages/pNNN.png` | 逐页 200 dpi 渲染图（NNN = 三位 PDF 页号）。**公式的唯一真值。** |
| `split/pNNN.txt` | 逐页 PDF 文字层。正文词句可信，**数学符号一律不可信**。 |
| `full.txt` | 整本文字层（检索用）。 |
| `tags.txt` / `tags_bypage.txt` | 745 条编号公式清单。 |
| `figures/figN.png` | 已裁好的 28 张原图（400 dpi）。 |
| `glossary.tsv` | 术语冻结表（`英文 ⇥ 中文`，制表符分隔）。 |
| `src/preamble.tex` | 导言区（Lead 独占）。**你只读，不得修改。** |
| `src/chunks/trNN*.tex` | 你的输出文件。 |
| `tools/crop.py` | 裁图放大（用法见文件头，PDF 点坐标，整页 612×792）。 |

**文字层可靠度分级（血泪教训）**：
- ✅ 正文单词、段落边界、脚注、章节标题 —— 可信，用来定位与把握论证；
- ❌ **数学一律不可信**：`\frac{m}{2}` 可能抽成 `2m`，上下标错位、分式拆散、∫ 抽成孤立符号、
  ω 抽成 f、α 抽成 a、`\mathcal{N}` 抽成 N、`\mathbb{Z}` 抽成 Z。**每个编号公式必须看页面图像逐符号抄写。**

## 2. 片段规则（硬性）
- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、`\tableofcontents`、`\ref`、`\eqref`、`\cite`。
- 文件写到 `work/src/chunks/trNN{a,b,c}.tex`（UTF-8 无 BOM、LF 换行；约每 5–6 页一片，按 a→b→c 顺序拼接）。
- 章节层级：`\section{…}` / `\subsection{…}` / `\subsubsection{…}`（LaTeX 自动编号，1–6 与原文一致）。
  **只有 BRIEF 指定给你的标题才由你写**；块首若处在小节中间，直接续写正文、不要重写标题。
- 段落之间空一行。不要写 `\par`。不要用 markdown 的 `**粗体**`。
- 原文的**行内粗体小标题**（如 "**Screening.**"、"**Tame punctures.**"）写成 `\para{屏蔽。}`（preamble 已定义）。
- 原文脚注：`\footnote{…}` 就地写；脚注编号由 LaTeX 自动，与原文不必逐号一致（README 会声明）。

## 3. 公式（本工程最关键的一条）
- 编号公式**必须与原文一一对应，不缺、不重、不跳、不重排、不自造**：
  ```latex
  \begin{equation}
      ... \tag{3.13}
  \end{equation}
  ```
  多行用 `align`/`gather`，每个编号一行一个 `\tag{…}`；原文一条编号带多行时，只在**最后一行** `\tag`。
- 原文中大量公式**没有编号**：用 `\[ … \]` 或 `equation*`，绝不自己加编号。
- 正文引用公式写**纯文本**：「式 (3.13)」「式 (5.1)–(5.3)」，**不要** `\ref`/`\eqref`。
- 参考文献引用写纯文本：`[167]`、`[181–184]`（en-dash 用 `--`），不要 `\cite`。
- 微分：`\dd`（= `\mathrm{d}`），如 `\dd z`、`\dd^2 z`；虚数单位 `\ii`；自然常数 `\ee`。
- 积分测度与上下限、分式、根号、求和/求积范围、上下标归属务必与图像核对；`\left(`/`\right)` 要配对。
- 演示公式用 `equation`/`align`，不要 `$$…$$`。公式过宽可 `\resizebox{0.985\textwidth}{!}{$\displaystyle …$}`（保留 `\tag`）。

## 4. 宏（preamble 已定义，直接用；不要自造 `\newcommand`）
- 集合：`\R \C \Z \N \Q`
- 花体：`\cA … \cZ`（如 `\cO`、`\cN`、`\cG`、`\cS`、`\cM`）
- 哥特体：`\fg \fh \ft \fu \fsu \fso \fsp \fZ`
- 群：`\SU \SO \Sp \U \PSU \PSO \Spin \Pin`、`\SymTFT`
- 算子/常数：`\dd \ee \ii \Tr \tr \diag \sgn \id \Re \Im \rk \rank \vol \half \abs{} \norm{} \ie \eg \cf`
- 格式命令：`\para{…}`、`statementbox`/`definitionbox`/`notebox`/`noteboxplain` 环境、`\figtitle{N}{图注}`、`\tabtitle{N}{表题}`
- 其余用标准命令：`\mathbb{}`、`\mathcal{}`、`\mathfrak{}`、`\operatorname{}`、`\langle`、`\rangle`、`\otimes`、`\oplus`、`\cong`、`\simeq`、`\subset`、`\hookrightarrow`、`\overset{}{}`、`\underset{}{}`、`\xrightarrow{}`。

## 5. 批注（Tutor Note）
格式固定为 LaTeX 注释行，编译后不显示：
```latex
% [Tutor Note: ……]
```
要求（**密度：每 2–3 页至少 1 条；每节（section）不少于 3 条**）：
- **可验证的易错点**：给出核对方法/数值锚点（如「反推 (4.12) 的系数：用 U(1) 电荷量子化 q∈ℤ 可检验」）；
- **补出的省略论证**：作者说 "it is easy to see / one can show" 而跳过的地方，写清用了什么定理/文献；
- **原文笔误**：必须给正确形式 + 判断依据（量纲/相邻式自洽/文献对照），并先 500+ dpi 裁图复核；
- **术语首现**：给英文原词；
- 不要写空话、不要凑数。批注里可以有 `$…$`，但**不要出现不成对的 `$`**（自检脚本会误报）。
- 批注要具体到页码/公式号，例如 `% [Tutor Note: p.55 式 (3.13) 的 2π 因子来自规范场归一化，见 (3.11) 前的约定]`。

## 6. 图（28 张，已由 Lead 裁好；只插图，不造图）
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{fig2.png}
\figtitle{2}{图注照原文翻译……}
\end{figure}
```
- 图片名固定 `figN.png`（`\graphicspath` 已指向 `figures/`），**不要写路径前缀**。
- 图注（caption）照原文**翻译**；图内文字保持原样（截取的原图）。
- 分工没给你的图不要写；图位置按原文（通常紧跟第一次引用的段落之后）。
- 若发现裁图有缺边/带相邻正文，**回报 Lead**，不要自己重裁。

## 7. 彩色方框（原文结构的一部分，必须照译）
| 原文外观 | 环境 | 写法 |
|---|---|---|
| 蓝色框，标题条 "Statement 2.1: …" | `statementbox` | `\begin{statementbox}{陈述 2.1：标题译文} … \end{statementbox}` |
| 绿色框，标题条 "Definition 3.1: …" | `definitionbox` | `\begin{definitionbox}{定义 3.1：标题译文} … \end{definitionbox}` |
| 橙色框，标题条 "Example 2.1: …" | `examplebox` | `\begin{examplebox}{例 2.1：标题译文} … \end{examplebox}` |
| 粉色/浅红框，彩色标题条（无 "Statement/Definition/Example" 字样） | `notebox` | `\begin{notebox}{标题译文} … \end{notebox}` |
| 细边框、无标题条 | `noteboxplain` | `\begin{noteboxplain} … \end{noteboxplain}` |
- 编号（2.1、4.12…）**照抄原文**，写在标题参数里；不要自造编号。
- 方框内的正文照常翻译；可含公式、`\para{}`、列表（`itemize`/`enumerate` 用 `[leftmargin=1.4em,itemsep=1pt,topsep=1pt]`）。
- 若方框跨页断开（原文如此），**合并成一个方框**（内容不丢，别拆成两个编号）。

## 8. 表（原文只有 Table 1，p.47，归 tr-03）
```latex
\begin{table}[htbp]
\centering
\small
\begin{tabular}{lll}
\toprule
…… & …… & …… \\
\midrule
…… & …… & …… \\
\bottomrule
\end{tabular}
\tabtitle{1}{表题译文……}
\end{table}
```
- 逐格核对（列归属、上标、$\mathbb{Z}_2$ 等）；合并单元格用 `\multirow`/`\multicolumn`。

## 9. 页码标注
每进入新的一页（PDF 页），在内容前加一行注释：
```latex
% [原文 p.13]
```
片段开头再加一行：`% ===== 原文 pp.13–28 =====`。

## 10. 禁止事项（违反即返工）
1. 不改原文内容：**不删、不增、不"顺手修正"正文**。原文字句有误 → 照译 + 批注指出 + 给正确形式。
2. 不编造：图、表、公式、文献、作者没说过的物理结论，一个字都不加。
3. 不用 `\newcommand`、不改 preamble/main、不编译（编译由 Lead 统一做）。
4. 不用 markdown 语法（`**`、`##`、`>` 引用块）——只写 LaTeX。
5. 不留未翻译的整句英文（专有名词、人名、模型名、缩写如 CFT/SYM/SQCD/TQFT/SPT/SymTFT 可保留）。
6. 中文标点：句号「。」、逗号「，」、顿号「、」；数学环境内用英文标点。
7. 不写"本节重点"之类原文没有的内容。

## 11. 边界规定
- 你的片段若从句子/公式中间开始：**直接从该处续写**，不要重写上一页的内容，也不要删掉上文。
- 跨页句子「开始者写完」（谁先开始这句谁负责把句子写完）。
- **编号公式连续性是你和邻居的契约**：你负责的 tag 区间**首尾都必须接上**（见 BRIEF）。
- 边界处若有歧义：**宁可多看一页图像**，并在回报里说明。

## 12. 自检清单（写文件前逐项过）
- [ ] 本块 tag 区间完整：*起始 tag* … *结束 tag* 一个不缺、无重复、无自造编号；
- [ ] 每个编号公式与页面图像逐符号核对（上下标、指标位置、希腊字母、\mathcal vs 普通）；
- [ ] 花括号平衡、`\left`/`\right` 配对、`\begin`/`\end` 配对、`$` 成对；
- [ ] 无 `\documentclass`/`\usepackage`/`\begin{document}`/`\newcommand`/`**`；
- [ ] 无 U+FFFD 乱码；UTF-8 无 BOM；
- [ ] 覆盖本块全部正文、脚注、方框、图注/表题；图都插了、编号对；
- [ ] 批注数量与质量达标（每 2–3 页 ≥1，每节 ≥3）；
- [ ] 每页都有 `% [原文 p.N]` 标注。

## 13. 回执格式（发给 Lead 的消息，5 项）
1) 完成文件与覆盖页段；2) tag 区间（如 3.108–4.2）及是否有跳号/存疑；
3) 发现的原文可疑/笔误（页码 + 公式号 + 判断依据）；4) 新增术语（英文→中文）；
5) 自检确认结果（逐项 pass）。
