# STYLE_GUIDE —— Setter 博士论文中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，保留权利，仅限非商业学术研读，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（v1.0 / 2026-11-03 / Lead 独占维护，译者只读）

## 0. 底本（实测，勿再猜）
- 原文：**Kevin Setter**, *Topological Quantum Field Theory and the Geometric Langlands Correspondence*,
  Thesis by, California Institute of Technology, Pasadena, California, **2013**（答辩 2012-08-24）。
  元数据无作者/标题（PDF 由 pdfTeX 生成），作者与标题取自首页；导师 Anton Kapustin。
- PDF：`<本地路径>`，**共 169 页**。
- **页码映射：PDF 页号 = 印刷页码 + 10**（PDF p.11 = 印刷 p.1，PDF p.169 = 印刷 p.159）。
  正文 pp.1–154；pp.155–159 为参考文献（**不译**，保留英文原貌）。
- 结构：9 章 + 附录 A–D（A: 122–131, B: 132–141, C: 142–149, D: 150–154）+ 参考文献。
- **编号公式共 57 条**（1.1–1.3, 2.1–2.4, 3.1–3.11, 5.1–5.8, 7.1–7.9, 8.1–8.3,
  9.1–9.3, B.1–B.14, D.1–D.2）；第 4、6 章与附录 A、C **没有任何编号公式**。
  清单见 `tags.txt` / `tags_bypage.txt`（**唯一验收依据**）。
- **图 10 张**（原文矢量图/位图）：图 1.1(p.3)、2.1(p.17)、4.1–4.2(p.34)、4.3(p.35)、4.4(p.36)、
  4.5–4.6(p.37)、4.7(p.40)、6.1(p.77)。**已由 Lead 按 400 dpi 裁好**在 `src/figures/figXY.png`。
- 定理类环境（**已逐页核实，勿再猜**）：
  - 本论文**没有编号的定理（Theorem）**。印刷 p.97（PDF p.107）的 “Theorem 3.3.8” 是**引用文献 [21] 的定理编号**
    （原文作 “(see Theorem 3.3.8 of [21])”），**不是本论文的定理**，不要建 theorem 环境，照译“（见文献 [21] 的定理 3.3.8）”。
  - 第 9 章：**定义 1–7**（印刷 pp.112–117）与**命题 1–10**（印刷 pp.112–120），编号在本章内顺序，排版为「定义 2.」「命题 7.」。
  - 附录 C：**4 处不编号的「定理」块**（印刷 pp.145、146、146、148），原文排版为 “Theorem.” 后接陈述，
    其中 p.148 的一条陈述本身是 “Proposition 2.2 of [18]”。用 `\begin{theorem} … \end{theorem}`（不带可选编号）。
  - 附录 D：**证的是第 9 章的命题 (1)、(3)、(6)、(7)、(8)**（原文措辞 “proofs of selected propositions”），
    原文排版带圆括号「Proposition (3).」；译作「命题 3.」即可，编号照抄原文（见 §7）。
  - 附录 D 印刷 p.151 原文写 “Theorem 1 tells us…”，但全文并无 Theorem 1——这是**原文的悬空引用**，照译「定理 1」+ 批注说明。
- **大量显示公式没有编号**：这些用 `\[ … \]` 或 `equation*`，**绝不自己加编号**。
- 原文有若干**方框公式**（如式 (1.2)，两个方框 + 双向箭头），见 §3.4。
- **原文没有表格**（0 张表）。不要造表。

## 1. 素材（全部在 `<本地路径>`）
| 路径 | 内容 |
|---|---|
| `pages/pNNN.png` | 逐页 200 dpi 渲染图（NNN = 三位 PDF 页号）。**公式与排版细节的唯一真值。** |
| `split/pNNN.txt` | 逐页文字层，首行 `PDF p.N (footer: M) printed=P`。正文词句可信，**数学符号一律不可信**。 |
| `full.txt` | 整本文字层（全局检索用）。 |
| `tags.txt` / `tags_bypage.txt` | 57 条编号公式清单（tag ↔ 页）。 |
| `src/figures/figXY.png` | 已裁好的 10 张原图（400 dpi，**不要重新裁、不要缩放比例以外的处理**）。 |
| `glossary.tsv` | 术语冻结表（制表符分隔：英文 \t 中文）。**先查表再下笔**。 |
| `src/preamble.tex` | 导言区（Lead 独占，你只读，**不得修改**）。 |
| `src/chunks/*.tex` | 你的输出文件。 |

**文字层可靠度分级（血泪教训）**：
- ✅ 正文单词、段落边界、脚注、章节标题 —— 可信，用来定位与理解论证；
- ❌ **数学一律不可信**：`\frac{m}{2}` 会抽成 `2m`，上下标错位、分式拆散、∫ 抽成孤立符号、
  ω 抽成 f、α 抽成 a、$\cN$ 抽成 N、连字（ﬁ ﬂ ﬀ）也需留意。**显示公式必须逐页看图像逐符号抄写。**

## 2. 片段规则（硬性）
- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、
  `\tableofcontents`、`\appendix`、`\chapter` 的 `*` 变体。
- 文件写到 `src/chunks/<分配给你的文件名>.tex`（UTF-8 **无 BOM**、**LF** 换行；用 write 工具即可）。
- 章节层级：
  - 原文 "Chapter N" → `\chapter{……}`（**章号自动**，你只写章名，如 `\chapter{引言与概述}`）；
  - 原文 "N.M" → `\section{……}`；"N.M.K" → `\subsection{……}`；"N.M.K.L" → `\subsubsection{……}`。
  - **补充说明**：章标题只由该章的负责人在章首写一次；小节标题谁负责起始页谁写；块开头若处于某小节中间，
    **不要再写该小节标题**，直接续写正文。
- 段落之间空一行。不要写 `\par`。不要用 markdown 的 `**粗体**`（会原样印出星号）。
- 原文**行内粗体小标题**（如 "**Tame punctures.**"）→ `\para{……}`（独立成段粗体）。
- 原文斜体强调 → `\emph{……}`。
- 原文脚注 → `\footnote{……}` 就地写在该处。
- 英文引号 'xxx' / "xxx" → 中文引号“……”；括号内英文术语保留原文。
- 人名、机构名、模型名、专有名词（Kapustin、Witten、Gukov、Hitchin、Vafa–Witten、Nahm、Springer…）
  保留英文；术语首现可写“中文（英文）”，此后用中文（见 glossary.tsv）。

## 3. 公式（本工程最关键的一条）
### 3.1 编号公式必须与原文一一对应，不缺、不重、不跳、不重排、不自造
```latex
\begin{equation}
    …… \tag{1.2}
\end{equation}
```
- 多行用 `align`/`gather`，**每个编号一行一个 `\tag{…}`**；原文一条编号跨多行时只在最后一行 `\tag`。
- 只写 `tags.txt` 里属于你页段的编号；**不属于你的编号一个都不要写**；一个都不要漏。
### 3.2 无编号公式
用 `\[ … \]` 或 `equation*`；**不得加编号**。
### 3.3 公式引用（正文中）
写**纯文本**"式 (1.2)"、"式 (3.6)–(3.7)"，**不要** `\ref`/`\eqref`（手工 tag 无法自动交叉引用）。
### 3.4 方框公式（原文的“盒子”图式公式，如式 (1.2)）
```latex
\begin{equation}
  \eqbox{A-膜 \\ $\cM_H(\LG,G)$ 上 \\ 辛形式 $\omega_K$}
  \;\longleftrightarrow\;
  \eqbox{B-膜 \\ $\cM_H(G,C)$ 上 \\ 复结构 $J$} \tag{1.2}
\end{equation}
```
（`\eqbox` 已在 preamble 定义，宽 0.34\textwidth、居中、小字号；内容里可换行 `\\`。）
### 3.5 图形公式（编号公式其实是示意图/箭图）
- **首选 TikZ 重画**（preamble 已加载 tikz + arrows.meta + calc）：节点、连线、标签照原图如实画，
  外面套 `\begin{equation} … \tag{N.M} \end{equation}` 保住编号。
- 若过于复杂：从 `pages/pNNN.png` 裁出图区（**不要裁到原编号**），以 `\includegraphics` 放进 equation 里，
  同样用 `\tag{}` 编号。裁图后**必须 `read_image` 复核**（完整、无截断、无原文编号）。
### 3.6 其它
- 微分用 `\dd`；常数 e 用 `\ee`、虚数单位用 `\ii`；迹 `\Tr`/`\tr`；花体 `\cM \cO \cH …`；
  李代数 `\fg \fh \fsu …`；朗兰兹对偶群用 `\LG`（= `{}^L G`）。
- 分式、根号、积分、求和上下限、`\left(`/`\right)` 全部与图像核对。
- 演示数学环境之间不要用 `$$…$$`。

## 4. 宏（preamble 已定义，直接用；**不要自造 `\newcommand`**）
- 集合：`\R \C \Z \N \Q`
- 花体：`\cA \cB \cC \cD \cE \cF \cG \cH \cI \cJ \cK \cL \cM \cN \cO \cP \cQ \cR \cS \cT \cU \cV \cW \cX \cY \cZ`
- 哥特体：`\fg \fh \ft \fu \fgl \fsl \fsu \fso \fsp`；对偶群：`\LG \LT \Lg`
- 算子：`\dd \ee \ii \Tr \tr \diag \sgn \id \rk \vol \Pf \Res \Mor \Ob \Hom \End \Aut \Re \Im \half \ie \eg \cf \dbar \abs{} \norm{} \ip{}{}`
- 格式：`\para{…}`、`\eqbox{…}`、`\figtitle{编号}{图注}`、`\refitem{编号}{内容}`
- 其它用标准命令：`\mathbb{} \mathcal{} \mathfrak{} \operatorname{} \langle \rangle \leqslant \le \otimes \oplus \cong \simeq \subset \hookrightarrow \star \wedge \partial \bar{} \widehat{} \tilde{} \mathbf{} \mathrm{}`
- **章节标题里尽量不放数学**；必须放时写成 `\texorpdfstring{$S^1$}{S1}`（否则 PDF 书签报错）。

## 5. 批注（Tutor Note）
格式固定为 LaTeX 注释行，编译后不显示：
```latex
% [Tutor Note: ……]
```
要求（**密度：每 2 页至少 1 条；每节不少于 2 条**）：
- **可验证的易错点**：给出核对方法/数值锚点/相邻式自洽检验（如"用 AB 相位、模变换 $S$ 的 $\tau\to-1/\tau$ 反推"）；
- **补出省略论证**：作者说 "it is easy to see / one can show / it follows" 而跳过的地方，写清用了什么定理/文献/章节；
- **原文笔误**：必须给正确形式 + 判断依据（量纲/对称性/相邻式自洽/与经典文献对照）；
- **术语首现**：给英文原词（若 glossary 未收，顺带在回执里回报新词）；
- 不要写空话，不要凑数；批注要具体到页码/公式号，例如
  `% [Tutor Note: p.87 式 (7.3) 的符号约定与 §2.5.2 不一致；按 $t=i$ 时 $\omega_I$ 为辛形式核对]`
- 批注里可以有 `$…$`，但**不要出现不成对的 `$`**（自检脚本会误报）。

## 6. 图（10 张，Lead 已裁好；**只写分工给你那几张**）
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.55\textwidth]{fig41.png}
\figtitle{4.1}{边界条件范畴中的态射对应于位于两段边界交接处的局部算子。}
\end{figure}
```
- 图片名固定 `figXY.png`（`\graphicspath` 已指向 `figures/`），**不要写路径前缀**；
  宽度按图的长宽比自定（0.35–0.9\textwidth 之间，以清晰为准），**不要裁剪、不要改图内内容**。
- 图注（caption）照原文**翻译**；图内文字保持原样（截取的原图）。
- 原文的图在文字流中的位置附近放置；正文引用“图 4.1”用纯文本。

## 7. 定理类环境（编号一律由原文手工给出）
```latex
\begin{theorem}[3.3] …… \end{theorem}     % 排版为「定理 3.3.」
\begin{definition}[2] …… \end{definition} % 「定义 2.」
\begin{proposition}[7] …… \end{proposition} % 「命题 7.」
\begin{proof} …… \end{proof}              % 「证明」
```
- 可用环境：`theorem proposition lemma corollary conjecture claim definition remark example exercise proof`。
- 原文 "Definition 2." → `\begin{definition}[2]`；编号照抄原文，**不重排、不跳号**。

## 8. 页码标注
每进入新的一页（PDF 页），在内容前加一行注释：
```latex
% [原文 p.13]
```
片段开头再加一行：`% ===== 原文 pp.12–24（PDF p.22–34） =====`。

## 9. 禁止事项（违反即返工）
1. 不改原文内容：**不删、不增、不"顺手修正"正文**。原文字句有误 → 照译 + 批注指出 + 给正确形式。
2. 不编造：图、表、公式、文献、作者没说过的物理结论，一个字都不加。
3. 不用 `\newcommand`、不改 preamble/main、**不编译**（编译由 Lead 统一做）。
4. 不用 markdown 语法（`**`、`##`、`>` 引用块）——只写 LaTeX。
5. 不留未翻译的整句英文（专有名词、人名、模型名、缩写可保留）。
6. 中文标点：句号“。”、逗号“，”、顿号“、”、冒号“：”；**数学环境内用英文标点**。
7. 不写“本节重点”“译者按”之类的额外段落（解释一律进 `% [Tutor Note: …]`）。
8. 不写 `\tableofcontents`、不写 `\appendix`、不写 `\chapter*`/`\section*`（编号会错）。

## 10. 边界规定
- 你的页段**首尾都从章节标题处开始**（除 ch06b 从 §6.4.2 起，见 BRIEF），因此**不要重写上一块的内容**。
- 跨页句子“开始者写完”（谁先开始这句谁负责把句子写完）。
- 边界处若有歧义：**宁可多看一页图像**，并在回报里说明。
- 公式编号连续性是你和邻居的契约：你负责的 tag 区间**首尾都必须接上**（见 BRIEF 的 tag 区间）。

## 11. 自检清单（写文件前逐项过）
- [ ] 本块 tag 区间完整：*起始 tag* … *结束 tag* 一个不缺、无重复、无自造编号；无编号公式没被加编号；
- [ ] 每个编号公式与页面图像逐符号核对（上下标、指标位置、希腊字母、`\mathcal` vs 普通）；
- [ ] 花括号平衡、`\left`/`\right` 配对、`\begin`/`\end` 配对、`$` 成对；
- [ ] 无 `\documentclass`/`\usepackage`/`\begin{document}`/`\newcommand`/`**`；
- [ ] 无 U+FFFD 乱码；UTF-8 无 BOM；
- [ ] 覆盖本块全部正文、脚注、图注、定理/定义/命题环境；
- [ ] 批注数量与质量达标（每 2 页 ≥1，每节 ≥2）；
- [ ] 每页都有 `% [原文 p.N]` 标注；
- [ ] 术语与 `glossary.tsv` 一致。

## 12. 回执格式（发给 Lead 的消息，简洁）
1) 完成的文件与覆盖页段（印刷页 / PDF 页）；
2) tag 区间（如 5.1–5.8）及是否有跳号/存疑；
3) 发现的原文可疑/笔误（页码 + 公式号 + 判断依据）；
4) 新增术语（英文→中文）；
5) 自检确认结果（逐项 pass）。
