# STYLE_GUIDE —— 《A slow review of the AGT correspondence》中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（v1.0 / Lead 独占维护，队友只能读）

## 0. 底本（实测，勿再猜）
- 原文：Bruno Le Floch, *A slow review of the AGT correspondence*, arXiv:2006.14025v3 [hep-th], 6 Apr 2022；
  拟发表于 JPhysA（YRISW 2020 讲座的扩展版）。
- PDF：`<本地路径>).pdf`，**共 136 页**。
- **页码对应：PDF 页号 = 原文印刷页码（偏移 0）**。正文 pp.1–106，pp.106–136 为参考文献（1309 条，不译）。
- **实测**：位图 0 张；矢量图 5 张（Figure 1 p.7, Figure 2 p.19, Figure 3 p.56, Figure 4 p.79, Figure 5 p.80）；
  表格 3 个（Table 1 p.10、Table 2 p.13、Table 3 p.61）+ 缩写表 p.105；无目录式附录，只有 Appendix A（p.105–106，特殊函数）。
- **编号公式共 174 条**（1.1–1.10, 2.1, 3.1–3.25, 4.1–4.28, 5.1–5.47, 6.1–6.23, 7.1–7.21, 8.1–8.12, 9.1–9.7）。
  清单见 `work/tags.txt`（tag → 页码）与 `work/tags_bypage.txt`（页 → tags）。
- 原文每节开头有**灰色要点框**（如 "6d viewpoint on 4d N=2 class S theories"），是原文内容，必须照译；
  不要另加"本节重点"。
- 原文有 **Exercise x.y**（如 Exercise 2.2、4.1），编号手工给出。

## 1. 可用素材（全部在 `<本地路径>`）
| 路径 | 内容 |
|---|---|
| `pages/pNNN.png` | 逐页 200 dpi 渲染图（NNN = 三位 PDF 页号）。**公式的唯一真值。** |
| `split/pNNN.txt` | 逐页 PDF 文字层。正文词句可信，**数学符号一律不可信**。 |
| `full.txt` | 整本文字层（检索用）。 |
| `tags.txt` / `tags_bypage.txt` | 174 条编号公式的清单。 |
| `figures/fig1.png … fig5.png` | 已裁好的 5 张原图（400 dpi）。 |
| `glossary.tsv` | 术语冻结表（制表符分隔：英文 \t 中文）。 |
| `src/preamble.tex` | 导言区（Lead 独占）。**你只读，不得修改。** |
| `src/chunks/trNN*.tex` | 你的输出文件。 |

**文字层可靠度分级（血泪教训）**：
- ✅ 正文单词、段落边界、脚注、章节标题 —— 可信，用来定位与把握论证；
- ❌ **数学一律不可信**：`\frac{m}{2}` 可能抽成 `2m`，上下标错位、分式拆散、∫ 抽成孤立符号、
  ω 抽成 f、α 抽成 a、\mathcal{N} 抽成 N。**每个公式必须逐页看图像逐符号抄写。**

## 2. 片段规则（硬性）
- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、`\tableofcontents`。
- 文件写到 `work/src/chunks/trNN{a,b,c}.tex`（UTF-8 无 BOM、LF 换行）。可拆成 a/b/c 多个文件，**按 a→b→c 顺序拼接**。
- 章节层级：`\section{…}` / `\subsection{…}` / `\subsubsection{…}`；原文 "Part I/II/III" 用 `\part{…}`
  （只由分工指定的那一位在正确位置写，见 BRIEF）。
- 段落之间空一行。不要写 `\par`。不要用 markdown 的 `**粗体**`（会原样印出星号）。
- 原文的**行内粗体小标题**（如 "**Tame punctures.**"）写成 `\para{驯服穿刺。}`（preamble 已定义，会独立成段粗体）。
- 原文的**灰色要点框**写成：
  ```latex
  \begin{keybox}{要点框原文标题的中译}
  \begin{itemize}[leftmargin=1.4em,itemsep=1pt,topsep=1pt]
    \item …
  \end{itemize}
  \end{keybox}
  ```
- 原文脚注：`\footnote{…}` 就地写在该处（LuaLaTeX 会正常编号）。
- 原文习题：`\begin{exercise}{2.2} 正文 \end{exercise}`（编号照抄原文）。

## 3. 公式（本工程最关键的一条）
- 编号公式**必须与原文一一对应，不缺、不重、不跳、不重排、不自造**：
  ```latex
  \begin{equation}
      ... \tag{3.13}
  \end{equation}
  ```
  多行用 `align` 或 `gather`，每个编号一行一个 `\tag{…}`；原文一条编号带多行时，只在最后一行 `\tag`。
- **原文中大量公式没有编号**（尤其 §2）：这些用 `\[ … \]` 或 `equation*`，绝不自己加编号。
- 正文引用公式写**纯文本**"式 (3.13)"、"式 (5.33)–(5.35)"，**不要** `\ref`/`\eqref`（手工 tag 无法自动交叉引用）。
- 参考文献引用写纯文本：`[167]`、`[96, 98]`、`[45–54]`、`[2, 363–365]`，与原文一致；不要 `\cite`。
- 微分：用 `\dd`（= `\mathrm{d}`），如 `\dd z`、`\dd^2 z`；与外微分/边界用 `\partial`。
- Hodge 星用 `\star`；共形块用 `\mathcal{F}`；不要用 `unicode-math` 专属命令。
- 分式、根号、积分、求和上下限务必与图像核对；`\left(`/`\right)` 要配对。
- 演示数学环境之间用 `\begin{equation}` 不要 `$$…$$`。

## 4. 宏（preamble 已定义，直接用；不要自造 `\newcommand`）
- 集合：`\R \C \Z \N \Q`
- 花体：`\cN \cO \cM \cB \cC \cD \cE \cF \cG \cH \cI \cL \cP \cQ \cS \cT \cU \cV \cW \cX \cY \cZ`
- 哥特体（李代数）：`\fg \fh \ft \fu \fsu \fso \fsp`
- 算子/常数：`\dd \ee \ii \Tr \tr \diag \sgn \id \Re \Im \rk \vol \half \ie \eg \cf`
- 格式命令：`\para{…}`（行内小标题）、`keybox` 环境、`exercise` 环境、`\figtitle{编号}{图注}`、`\tabtitle{编号}{表题}`
- 需要其他符号时用标准命令（`\mathbb{}`、`\mathcal{}`、`\mathfrak{}`、`\operatorname{}`、`\langle`、`\rangle`、
  `\leqslant`（原文用 ≤ 时优先 `\le`）、`\otimes`、`\oplus`、`\cong`、`\simeq`、`\subset`、`\hookrightarrow`）。

## 5. 批注（Tutor Note）
格式固定为 LaTeX 注释行，编译后不显示：
```latex
% [Tutor Note: ……]
```
要求（**密度：每 2–3 页至少 1 条；每节（section）不少于 3 条**）：
- **可验证的易错点**：给出核对方法/数值锚点（如"用 ζ(0)=−1/2、ζ′(0)=−½log2π 反推"）；
- **补出的省略论证**：作者说 "it is easy to see / one can show" 而跳过的地方，写清用了什么定理/文献；
- **原文笔误**：必须给正确形式 + 判断依据（量纲/相邻式自洽/文献对照）；
- **术语首现**：给英文原词；
- 不要写空话，不要凑数。批注里可以有 `$…$`，但**不要出现不成对的 `$`**（自检脚本会误报）。
- 批注要具体到页码/公式号，例如 `% [Tutor Note: p.55 式 (5.33) 的分母建议用 … 核对]`。

## 6. 图（只有 5 张，分工指定由谁写）
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{fig2.png}
\figtitle{2}{M5 膜与 M5$'$ 膜构型的示意……}
\end{figure}
```
- 图片名固定 `fig1.png … fig5.png`（`\graphicspath` 已指向 `../figures/`），**不要写路径前缀**，不要改宽度以外的参数。
- 图注（caption）照原文**翻译**，图内文字保持原样（截取的原图）。
- **不要插图、不要造图**；分工没给你的图不要写。

## 6bis. 「图形编号公式」（箭图/膜图/裤子分解）的两种做法（Lead 裁决，2026-11-03）
原文有些**编号公式**其实是示意图（如 (1.2) 裤子分解、(1.6) 箭图、(4.21)–(4.28) 箭图、(5.31) 等）。
preamble **已加载 tikz**。两种做法任选，按"忠实 + 可读"取舍：
- **首选 TikZ 重画**：节点用方框 `\node[draw]`、连线用 `\draw`，如实照抄原图节点标签与连线方向，外侧用
  `\begin{equation} … \tag{4.21} \end{equation}` 保留编号（TikZ 图放进 equation 里即可）。
- **复杂图可裁图**：用 `work/tools/crop.py` 裁出原图区域（**不要裁到原来的编号**），
  存为 `work/figures/eq<编号>.png`（如 `eq421.png`），然后
  ```latex
  \begin{equation}
    \includegraphics[width=0.8\textwidth]{eq421.png} \tag{4.21}
  \end{equation}
  ```
  裁图前先用 `read_image` 看整页确认区域，裁完再 `read_image` 复核一次（必须完整、无截断、无原编号）。
- 无论哪种，**编号仍必须与原文一一对应**。普通（非图形）公式一律照常转写，不得用裁图代替。

## 7. 表（原文只有 Table 1、Table 2、缩写表）
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
\tabtitle{2}{Nahm 分类……}
\end{table}
```
- 表题照译；`\tabtitle{编号}{表题}` 手工编号（表 1/表 2）。
- 缩写表（p.105）用 `longtable` 或 `itemize` 均可，格式统一、可读即可。

## 8. 页码标注
每进入新的一页（PDF 页），在内容前加一行注释：
```latex
% [原文 p.13]
```
片段开头再加一行：`% ===== 原文 pp.12–24 =====`。

## 9. 禁止事项（违反即返工）
1. 不改原文内容：**不删、不增、不"顺手修正"正文**。原文字句有误 → 照译 + 批注指出 + 给正确形式。
2. 不编造：图、表、公式、文献、作者没说过的物理结论，一个字都不加。
3. 不用 `\newcommand`、不改 preamble/main、不编译（编译由 Lead 统一做）。
4. 不用 markdown 语法（`**`、`##`、`>` 引用块）——只写 LaTeX。
5. 不留未翻译的整句英文（专有名词、人名、模型名、class S、AGT、CFT 缩写可保留）。
6. 中文标点：句号"。"、逗号"，"、顿号"、"；数学环境内用英文标点。
7. 不写"本节重点"（原文自带的 keybox 已覆盖）。

## 10. 边界规定
- 你的片段若从句子/公式中间开始：**直接从该处续写**，不要重写上一页的内容，也不要删掉上文。
- 跨页句子"开始者写完"（谁先开始这句谁负责把句子写完）。
- 边界处若有歧义：**宁可多看一页图像**，并在回报里说明。
- 公式编号连续性是你和邻居的契约：你负责的区间**首尾都必须接上**（见 BRIEF 的 tag 区间）。

## 11. 自检清单（写文件前逐项过）
- [ ] 本块的 tag 区间完整：*起始 tag* … *结束 tag* 一个不缺、无重复、无自造编号；
- [ ] 每个编号公式与页面图像逐符号核对（上下标、指标位置、希腊字母、\mathcal vs 普通）；
- [ ] 花括号平衡、`\left`/`\right` 配对、`\begin`/`\end` 配对、`$` 成对；
- [ ] 无 `\documentclass`/`\usepackage`/`\begin{document}`/`\newcommand`/`**`；
- [ ] 无 U+FFFD 乱码；UTF-8 无 BOM；
- [ ] 覆盖本块全部正文、脚注、要点框、习题、图注/表题；
- [ ] 批注数量与质量达标（每 2–3 页 ≥1，每节 ≥3）；
- [ ] 每页都有 `% [原文 p.N]` 标注。

## 12. 回执格式（发给 Lead 的消息）
1) 完成文件与覆盖页段；2) tag 区间（如 5.24–5.47）及是否有跳号/存疑；
3) 发现的原文可疑/笔误（页码 + 公式号 + 判断依据）；
4) 新增术语（英文→中文）；5) 自检确认结果（逐项 pass）。
