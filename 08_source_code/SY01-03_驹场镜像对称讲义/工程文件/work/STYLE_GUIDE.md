# STYLE_GUIDE —— 《驹场镜像对称讲义》中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（v1.0 / Lead 独占维护，队友只能读）

## 0. 底本（实测，勿再猜）
- 原文：**Kentaro Hori（堀健太郎）**, *Komaba Lectures on Mirror Symmetry*,
  2016 年 8 月 26–28 日东京大学驹场校区（Komaba）讲义，Kavli IPMU, University of Tokyo。
  元数据：`2016Lec.dvi`（dvips + Ghostscript 生成），无 arXiv 号；作者自述 "A part of the notes ...
  A full version will be available soon"（本讲义为不完整版）。
- PDF：`<本地路径>).pdf`，**共 49 页**（p.1 标题页 + 正文 48 页 + p.49 参考文献）。
- **页码对应：PDF 页号 = 原文印刷页码（页脚数字）+ 1**。即 **PDF p.N ↔ 印刷 p.(N−1)**。
  例：PDF p.16 页脚印 15；PDF p.49 页脚印 48。工程内一律标注 `% [原文 p.N]` 用**印刷页号**。
- **实测**：位图 0 张；矢量图 8 张（Figure 1 p.16、Figure 2 p.17、Figure 3 p.30、Figure 4 p.32、
  Figure 5 p.33、Figure 6 p.35、Figure 7 与 Figure 8 均在 p.36——均指 PDF 页号）。
- **无表格、无 keybox 要点框、无习题、无附录、无致谢**。参考文献 12 条（[1]–[12]，Lead 处理，不译）。
- **编号公式共 139 条**：2.1–2.19, 3.1–3.23, 4.1–4.56, 5.1–5.41（§1 无编号公式）。
  清单见 `work/tags.txt`（tag → PDF 页）与 `work/tags_bypage.txt`（页 → tags）。
  注意：`tags_bypage.txt` 里同页出现的 `2.15`(p13)、`4.35`(p32)、`5.22`(p44)、`5.31`(p46)
  是**正文里的引用**，不是新公式——真实 tag 集合以 `tags.txt` 按唯一化后的 139 条为准。
- **章节结构**（自动编号，必须与原文一致：\section 会打印 1,2,3,4,5；\subsection 打印 2.1 … 5.5）：
  ```
  1  Introduction                        (PDF p.2)
  2  2d (2,2) Supersymmetric QFTs         (p.2)
     2.1 2d (2,2) supersymmetry (p.2)   2.2 A and B (p.2)      2.3 RG flow (p.3)
     2.4 Deformations (p.4)             2.5 Topological Twists (p.5)
     2.6 Examples (p.6)                 2.7 Mirror Symmetry (p.9)
  3  T-duality                            (p.10)
     3.1 T-duality (p.10)               3.2 T-duality as Mirror Symmetry (p.13)
     3.3 A Puzzle and a Solution (p.16)
  4  Gauged Linear Sigma Models           (p.18)
     4.1 The Data (p.18)                4.2 Lagrangian (p.19)   4.3 Phases (p.21)
     4.4 Examples (p.24)                4.5 Moment Polytope and Toric Variety (p.34)
  5  Mirror Symmetry                      (p.38)
     5.1 T-duality of Charged Fields (p.38)   5.2 Superpotential Generation (p.42)
     5.3 Derivation of Mirror Symmetry 1 (p.44)  5.4 Derivation of Mirror Symmetry 2 (p.45)
     5.5 Examples (p.46)
  References                              (p.49)
  ```
  **子节标题归属见 BRIEF 的「标题归属表」；不属于自己块的标题绝对不要写**（否则整本书的编号会错位）。

## 1. 可用素材（全部在 `<本地路径>`）
| 路径 | 内容 |
|---|---|
| `pages/pNNN.png` | 逐页 200 dpi 渲染图（NNN = 三位 **PDF** 页号）。**公式的唯一真值。** |
| `split/pNNN.txt` | 逐页 PDF 文字层（首行 `% PDF p.N (printed N)`）。正文词句可信，**数学符号一律不可信**。 |
| `full.txt` | 整本文字层（检索用）。 |
| `tags.txt` / `tags_bypage.txt` | 139 条编号公式清单。 |
| `figures/fig1.png … fig8.png` | 已裁好的 8 张原图（500 dpi，**不含图注**）。 |
| `glossary.tsv` | 术语冻结表（制表符分隔：英文 \t 中文）。 |
| `src/preamble.tex` | 导言区（Lead 独占）。**你只读，不得修改。** |
| `src/chunks/trNN*.tex` | 你的输出文件。 |
| `tools/crop.py` | 裁图放大：`python crop.py <PDF页码> <x0> <y0> <x1> <y1> <out.png> [dpi]`（PDF 点坐标，整页 612×792） |

**文字层可靠度分级（血泪教训）**：
- ✅ 正文单词、段落边界、脚注、章节标题 —— 可信，用来定位与把握论证；
- ❌ **数学一律不可信**：`\frac{m}{2}` 可能抽成 `2m`，上下标错位、分式拆散、`\tilde` 丢失（本讲义大量
  `\widetilde{X}`、`\tilde\phi`、`\tilde W` 被抽成 `eX`、`eφ`、`fW`）、`\mathcal{C}` 抽成 `C`、
  `\bar` 抽成空白、希腊字母错位。**每个公式必须逐页看图像逐符号抄写。**

## 2. 片段规则（硬性）
- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、
  `\tableofcontents`、`\input`、`\include`。
- 文件写到 `work/src/chunks/<按 BRIEF 指定>.tex`（UTF-8 无 BOM、LF 换行）。可拆成 a/b/c 多个文件，
  **按 a→b→c 顺序拼接**。
- 章节层级：`\section{…}` / `\subsection{…}`；**不写 `\subsubsection`、不写 `\part`**。
  原文的行内粗体/下划线小标题（如 "**The Model $\mathrm{H}_n$**"、"**T-duality on D-branes**"、
  "**Step 1 — Reduction to the CP$^0$ model**"、"**n = 2**"）写成 `\para{…}`（preamble 已定义，
  独立成段、粗体、不缩进），**不要**写成 `\subsection`（会破坏编号）。`n = 2` 这类只是分段标记，也可用 `\para{…}`。
- 段落之间空一行。不要写 `\par`。不要用 markdown 的 `**粗体**`（会原样印出星号）。
- 原文脚注：`\footnote{…}` 就地写在该处（LaTeX 会自动编号；若编号与原文不符，在批注里说明）。
- 原文引用文献：纯文本 `[9]`、`[4, 5]`、`[8, 10]`，**不要** `\cite`。

## 3. 公式（本工程最关键的一条）
- 编号公式**必须与原文一一对应，不缺、不重、不跳、不重排、不自造**：
  ```latex
  \begin{equation}
      ... \tag{3.13}
  \end{equation}
  ```
  多行用 `align` 或 `gather`，每个编号一行一个 `\tag{…}`；原文一条编号带多行时，只在最后一行 `\tag`。
- **原文中大量公式没有编号**（尤其 §2、§4.1–4.3）：这些用 `\[ … \]` 或 `equation*`，绝不自己加编号。
- 正文引用公式写**纯文本**"式 (3.13)"、"式 (5.33)–(5.35)"，**不要** `\ref`/`\eqref`（手工 tag 无法自动交叉引用）。
- **本讲义特有的记号坑（务必照图像抄）**：
  - `\widetilde{X}`（对偶流形）、`\widetilde{T}^n`、`\widetilde{E}`、`\tilde\phi`、`\tilde y`、`\tilde W`
    —— 文字层里常塌成 `eX`、`eφ`、`ey`、`fW`、`eE`；
  - 上标里的 `\frac12`：如 `q_1^{\frac12}`、`\Lambda_{\mathbb{P}^2}^{3}`、`\sigma_1^{\frac{3}{2}}`；
  - 复数坐标 `\overline{\psi}`、`\overline{\varphi}`（文字层里常整块丢失）；
  - `T^{(1)}_{N,d}`、`T^{(1)}_{N,d}(0)`、`\mathrm{H}_n`（模型名，正体下标）；
  - `\CP^{N-1}`、`\WP^2_{1,1,n}`、`\cO_{\CP^{N-1}}(-d)`、`\mathrm{tot}[\cO(-d)\to\CP^1]`；
  - `\mu_F`、`\mathfrak{t}_F`、`\Lambda_G`、`P_W`、`\mathfrak{g}_{\C}`。
- 微分：用 `\dd`（= `\mathrm{d}`）；自然常数用 `\ee`；虚数单位用 `\ii`。
- 演示数学环境之间用 `\begin{equation}` 不要 `$$…$$`。

## 4. 宏（preamble 已定义，直接用；不要自造 `\newcommand`）
- 集合/射影空间：`\R \C \Z \N \Q \CP \WP`
- 花体：`\cA … \cZ`（如 `\cR_A`、`\cC_A`、`\cM_A`、`\cK`）
- 哥特体（李代数）：`\fg \fh \ft \fz \fu \fgl \fsl \fso \fsp`
- 算子/常数：`\dd \ee \ii \Tr \tr \diag \sgn \id \Crit \Hom \Ker \Image \coker \rank \vol \Pf \half \ie \eg \cf`
- 对偶变量：`\tX \tT \tW \tE \tB \tg \tphi \tpsi \ty \tx \te`
- 格式命令：`\para{…}`（行内小标题）、`\figtitle{编号}{图注}`
- 需要其他符号时用标准命令（`\mathbb{}`、`\mathcal{}`、`\mathfrak{}`、`\operatorname{}`、`\langle`、
  `\rangle`、`\cong`、`\simeq`、`\subset`、`\hookrightarrow`、`\oplus`、`\otimes`、`\wedge`、`\partial`）。
  若确实需要新宏：**先在回执里申请，由 Lead 加进 preamble**，不要自己写 `\newcommand`。

## 5. 批注（Tutor Note）
格式固定为 LaTeX 注释行，编译后不显示：
```latex
% [Tutor Note: ……]
```
要求（**密度：每 2–3 页至少 1 条；每个 \section 不少于 3 条**）：
- **可验证的易错点**：给出核对方法/数值锚点（如"由 (4.16) 的 ∂_σ 求导并令其 ∈2πiP 可反推 (4.17)"）；
- **补出的省略论证**：作者说 "it is easy to see / one is supposed to / left as an exercise" 而跳过的地方，
  写清用了什么定理、哪条公式、哪篇文献；
- **原文笔误**：必须给正确形式 + 判断依据（量纲/相邻式自洽/文献对照）——原文确有若干笔误（如 p.31
  "one pont blow up"、p.46 "constanits"、p.44 "(5.26) 推导中的 +σ"），可指出但要先核对图像；
- **术语首现**：给英文原词；
- 不要写空话，不要凑数。批注里可以有 `$…$`，但**不要出现不成对的 `$`**（自检脚本会误报）。
- 批注要具体到页/式号，例如 `% [Tutor Note: p.41 式 (5.20) 的两个 |dy|^2 项分别对应 y1、y2 的纤维度量]`。

## 6. 图（共 8 张，分工指定由谁写；其他人不插图）
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.72\textwidth]{fig3.png}
\figtitle{3}{$\mathrm{H}_n$ 的各相（$n=3$）。}
\end{figure}
```
- 图片名固定 `fig1.png … fig8.png`（`\graphicspath` 已指向 `../figures/`），**不要写路径前缀**。
- 图注（caption）照原文**翻译**；图内文字保持原样（截取的原图，已有英文 "Phase I"）。
- 图内已有英文标签（Phase I/II/III、$\zeta$、$\phi_i$ 等）**不要重画**，照贴原图。
- **不要插图、不要造图**；分工没给你的图不要写。图放在原文同一位置附近即可（`[htbp]`）。
- 原文正文对图的引用写"如图 3 所示"。

## 7. 页码标注
每进入新的一页（原文印刷页），在内容前加一行注释：
```latex
% [原文 p.13]
```
片段开头再加一行：`% ===== 原文 pp.9–16 =====`（印刷页号）。

## 8. 禁止事项（违反即返工）
1. 不改原文内容：**不删、不增、不"顺手修正"正文**。原文字句有误 → 照译 + 批注指出 + 给正确形式。
2. 不编造：图、表、公式、文献、作者没说过的物理结论，一个字都不加。
3. 不用 `\newcommand`、不改 preamble/main、不编译（编译由 Lead 统一做）。
4. 不用 markdown 语法（`**`、`##`、`>` 引用块）——只写 LaTeX。
5. 不留未翻译的整句英文（专有名词、人名、模型名、T-duality、mirror symmetry 等术语按 glossary 处理）。
6. 中文标点：句号"。"、逗号"，"、顿号"、"；数学环境内用英文标点。CJK 与 Latin 之间不要手敲空格。
7. 不加"本节重点"之类的自造内容。
8. 不写 `\section`/`\subsection` 中不属于自己块的标题（见 BRIEF 的标题归属表）。

## 9. 边界规定
- 你的片段若从句子/公式中间开始：**直接从该处续写**，不要重写上一页的内容，也不要删掉上文。
- 跨页句子"开始者写完"（谁先开始这句谁负责把句子写完）。
- 边界处若有歧义：**宁可多看一页图像**，并在回报里说明。
- 公式编号连续性是你和邻居的契约：你负责的区间**首尾都必须接上**（见 BRIEF 的 tag 区间）。

## 10. 自检清单（写文件前逐项过）
- [ ] 本块的 tag 区间完整：*起始 tag* … *结束 tag* 一个不缺、无重复、无自造编号；
- [ ] 每个编号公式与页面图像逐符号核对（上下标、指标、希腊字母、`\widetilde`、`\mathcal` vs 普通）；
- [ ] 花括号平衡、`\left`/`\right` 配对、`\begin`/`\end` 配对、`$` 成对；
- [ ] 无 `\documentclass`/`\usepackage`/`\begin{document}`/`\newcommand`/`**`；
- [ ] 无 U+FFFD 乱码；UTF-8 无 BOM；
- [ ] 覆盖本块全部正文、脚注、图注；
- [ ] 批注数量与质量达标（每 2–3 页 ≥1，每节 ≥3）；
- [ ] 每页都有 `% [原文 p.N]` 标注（N = 印刷页 = PDF 页 − 1）。

## 11. 回执格式（发给 Lead 的消息）
1) 完成文件与覆盖页段（印刷页）；2) tag 区间（如 4.21–4.34）及是否有跳号/存疑；
3) 发现的原文可疑/笔误（页 + 公式号 + 判断依据）；4) 新增术语（英文→中文）；5) 自检确认结果（逐项 pass）。
