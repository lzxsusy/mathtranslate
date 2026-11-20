# STYLE_GUIDE —— Mark Gross《Tropical Geometry and Mirror Symmetry》中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`
（v1.0 / Lead 独占维护，队友只能读，不得修改）

## 0. 底本（实测，勿再猜）
- 原文：Mark Gross, *Tropical Geometry and Mirror Symmetry*, AMS CBMS Regional Conference Series in Mathematics **114**, 2011（NSF-CBMS 2008 Kansas State 十讲）。
- PDF：`src/Gross_TropicalGeometryAndMirrorSymmetry.pdf`，**共 332 页**。
- **页码对应（本版 PDF 是重排/OCR 版）：PDF 页号（1-based）= 印刷页 + 15**。
  - PDF p.1–15 = 书名页/目录/前言（前言 ix–xiv，引论 xi–xvi 的罗马页码）；
  - PDF p.16 = 第一篇扉页；正文印刷 pp.1–306；参考文献印刷 pp.307–312（PDF 322–327）；索引 pp.313–315（不译）。
- **编号公式共 128 条**：1.1–1.5, 2.1–2.43, 3.1–3.9, 4.1–4.18, 5.1–5.44, 6.1–6.10（4.7 在文字层缺失，见 `tags.txt` 与 `probe.md`）。
  清单：`work/tags.txt`（tag→页码）、`work/tags_bypage.txt`（页→tags）。
- **定理类环境共用一个章节内计数器**：Definition 1.1 / Examples 1.2 / Definition 1.3 / … / Lemma 1.13 / Example 1.14 / Proposition 1.15 …
  中文统一为：定义/例/注/记号/构造/引理/命题/定理/推论，编号照原文（preamble 已按章自动编号，见 §4）。
- **图：全书按“章内连续编号”**（第一章 Figure 1..25，第二章重新从 Figure 1 开始，等等），标题形如 `Figure 12. ...`；
  图在文字层里可能漏检，**以页面图像为准**。
- 原文每一节末尾常有 "References and further reading" 小节，照译。

## 1. 可用素材（全部在 `work/`）
| 路径 | 内容 |
|---|---|
| `pages/pNNN.png` | 逐页 150 dpi 渲染图（NNN = 三位 PDF 页号）。**公式的唯一真值。** |
| `split/pNNN.txt` | 逐页 PDF 文字层。正文词句可参考，**数学符号一律不可信**（OCR 会把 ⊂ 抽成 鈯、τ 抽成 蟿、⊗ 抽成 ⊙ 等）。 |
| `full.txt` | 整本文字层（检索用）。 |
| `tags.txt` / `tags_bypage.txt` | 128 条编号公式清单。 |
| `figs.tsv` | 文字层里检测到的图标题（可能不全，只作参考）。 |
| `glossary.tsv` | 术语冻结表（英文 \t 中文）。 |
| `tools/crop.py` | 裁图脚本（裁原图/图形公式）。 |
| `src/preamble.tex` | 导言区（Lead 独占）。**你只读，不得修改。** |
| `src/chunks/*.tex` | 你的输出文件。 |

**文字层可靠度分级**：
- ✅ 正文单词、段落边界、脚注、章节标题、定理名 —— 可参考；
- ❌ **数学一律不可信**：上下标错位、希腊字母错、花体/黑板体丢字形、分式拆散。**每个公式必须逐页看图像逐符号抄写。**

## 2. 片段规则（硬性）
- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、`\tableofcontents`、`\part`（除非 BRIEF 指定你写）。
- 文件写到 `src/chunks/cNN{a,b,c}.tex`（UTF-8 无 BOM、LF 换行），按 a→b→c 拼接。可拆多个文件。
- 章节层级：`\section{…}` = 原文章（第 N 章）；`\subsection{…}` = 原文 x.y 节；原文不再深的小节一般不需要 `\subsubsection`。
  - **章标题只由该章起始块写**（见 BRIEF；自动编号，不要手写“第 1 章”字样）。
  - 小节标题 `\subsection{热带超曲面}`（自动编号 1.1），**不要**在标题里手写编号。
- 段落之间空一行。不要写 `\par`。不要用 markdown 的 `**粗体**`。
- 原文行内粗体小标题（如 "**The balancing condition.**"）→ `\para{平衡条件。}`
- 原文脚注：`\footnote{…}` 就地写。
- 原文定理类环境：用 preamble 定义的环境（见 §4），**不要**手写 `\textbf{Theorem 1.1.}`。

## 3. 公式（本工程最关键的一条）
- 编号公式**必须与原文一一对应，不缺、不重、不跳、不重排、不自造**：
  ```latex
  \begin{equation}
      \sum_{i=1}^{k} w_i n_i = 0 \tag{1.1}
  \end{equation}
  ```
  多行用 `align`/`gather`，每个编号一行一个 `\tag{}`；一条编号跨多行时只在最后一行 `\tag`。
- **原文大量公式没有编号**：用 `\[ … \]` 或 `equation*`，绝不自己加编号。
- 正文引用写纯文本："式 (1.1)"、"§2.3"、"Figure 2"/"图 2"（章内编号）——**不要** `\ref`/`\eqref`。
- 文献引用写纯文本：`[27]`、`[27, 28]`、`[45–54]`；不要 `\cite`。
- 微分：`\dd`（= `\mathrm{d}`）；偏导 `\partial`；花体 `\cM \cO …`；黑板体 `\R \C \Z \PP`。
- 分式、根号、积分、求和上下限、指标位置务必与图像核对；`\left(`/`\right)` 要配对。

## 4. 宏与环境（preamble 已定义；不要自造 `\newcommand`）
- 集合：`\R \C \Z \N \Q \PP`
- 花体：`\cA … \cZ`；哥特：`\fg \fh \fM \fN \fT \fX \fY \fZ`
- 算子：`\dd \ee \ii \diag \sgn \id \Re \Im \rk \rank \vol \half \ie \eg \cf`
- 定理类环境（**按章自动编号，直接用**）：
  ```latex
  \begin{definition} ... \end{definition}
  \begin{example} ... \end{example}      % 原文 "Example 1.6."；"Examples 1.2." 用 examples 环境
  \begin{proposition} ... \end{proposition}
  \begin{lemma} ... \end{lemma}
  \begin{theorem} ... \end{theorem}
  \begin{corollary} ... \end{corollary}
  \begin{remark} ... \end{remark}
  \begin{notation} ... \end{notation}
  \begin{construction} ... \end{construction}
  ```
  编号与原文一致（共用一个章节内计数器）。若某条原文编号与自动编号对不上（跳号/重号），**不要改编号**，在批注里注明。
- 图注/表注：`\figtitle{2}{...}` → 版面上印"图2：..."；`\tabtitle{1}{...}`。
- 习题：`\begin{exercise} ... \end{exercise}`（原文只有 1 条 Exercise）。
- 需要别的符号用标准命令（`\mathbb{}`、`\mathcal{}`、`\mathfrak{}`、`\operatorname{}`、`\langle/\rangle`、`\le`、`\otimes`、`\cong`、`\subset`）。

## 5. 图（按章内编号，原文图号照抄）
- 你的块里出现的图，**由你负责裁图并插入**：
  1. `read_image` 看 `pages/pNNN.png`，确认图的范围（不要把正文/图注裁进去，也不要把图裁断）；
  2. 用 `work/tools/crop.py` 裁 400–600 dpi 的 PNG，存到 `work/figures/f<章>_<图号>.png`（如 `f1_12.png` = 第 1 章 Figure 12）；
     裁之前先看 `crop.py` 文件头用法；
  3. 插入：
     ```latex
     \begin{figure}[htbp]
     \centering
     \includegraphics[width=0.8\textwidth]{f1_12.png}
     \figtitle{12}{原文图注的中译}
     \end{figure}
     ```
- 图片名不要带路径前缀（`\graphicspath` 已指向 `work/figures/`）。
- 图注照原文翻译；图内文字保持原图（不重画、不造图）。
- 若图是“示意图/公式图”，优先按原图裁剪；不要自己画 TikZ 除非极简（Lead 裁决）。

## 6. 表
原文表极少；出现时用 `booktabs` 的 `tabular`，表题 `\tabtitle{...}{...}`，编号照原文。

## 7. 批注（Tutor Note）
格式：`% [Tutor Note: ……]`（LaTeX 注释，编译后不显示）。
- 密度：每 2–3 页 ≥ 1 条，每节 ≥ 3 条；
- 内容：可验证的易错点（给核对锚点）、作者省略的论证（补定理/文献）、原文笔误（给正确形式 + 依据）、术语首现（附英文）；
- 批注要具体到页/式号；不要空话；批注里 `$` 必须成对。

## 8. 页码标注
每进入新的一页，在内容前加注释：`% [原文 p.13]`；片段开头写 `% ===== 原文 pp.12–24（PDF p.27–39）=====`。

## 9. 禁止事项（违反即返工）
1. 不改原文：不删、不增、不“顺手修正”正文；原文有误 → 照译 + 批注。
2. 不编造：图、表、公式、文献、结论，一个字都不加。
3. 不用 `\newcommand`、不改 preamble/main、不编译（编译由 Lead 统一做）。
4. 不用 markdown 语法。
5. 不留未翻译的整句英文（人名、术语缩写、模型名可保留）。
6. 中文标点：句号“。”、逗号“，”、顿号“、”；数学环境内用英文标点。
7. 不要另加“本节重点/导读”之类原文没有的内容。

## 10. 边界与接续
- 若从句子/公式中段开始：**直接续写**，不重写、不删上文。
- 跨页句子“开始者写完”。
- 每块的 tag 区间首尾必须与邻居接上；有歧义宁可多看一页图并在回执说明。
- 章标题/篇扉页只由 BRIEF 指定的人写。

## 11. 自检清单（写文件前逐项过）
- [ ] 本块 tag 区间完整：起始…结束一个不缺、无重复、无自造；
- [ ] 每个编号公式与页面图像逐符号核对；
- [ ] 花括号平衡、`\left/\right` 配对、`\begin/\end` 配对、`$` 成对；
- [ ] 无禁用命令、无 `**`、无 U+FFFD、UTF-8 无 BOM、LF；
- [ ] 覆盖本块全部正文、脚注、定理环境、图注、末尾 "References and further reading"；
- [ ] 图已裁好、插入、图注已译；
- [ ] 批注密度达标；
- [ ] 每页有 `% [原文 p.N]`。

## 12. 回执格式
1) 文件与覆盖页段；2) tag 区间及跳号/存疑；3) 图号与文件名清单；4) 原文可疑处（页+式号+依据）；5) 新术语（英→中）；6) 自检逐项 pass。
