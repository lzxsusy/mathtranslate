# STYLE_GUIDE —— 《SYZ 猜想综述集》译本硬规范（v1.0，Lead 冻结）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 本文件是全体译者的**硬约束**。开工前必须全文读完。凡与本文冲突的做法一律以本文为准。
> 项目根：`<本地路径>`；工作目录：`<根>\work`。

---

## 0. 项目形态

- 底本：6 篇英文综述（见 BRIEF.md），合成**一部**中文 LaTeX 译注本《SYZ 猜想综述集》。
- 编排：**每篇综述 = 一章**（第一章 Chan 2014 … 第六章 Collins–Lin 2022）。
- 编译：Lead 统一编译（LuaLaTeX，ctexbook）；译者**不编译**、不改 `preamble.tex` / `main.tex` / 别人的 chunk。
- 输出：每位译者只写自己名下的 `work\src\chunks\trNN*.tex`。

## 1. 全局编号体系（最重要，必须严格执行）

### 1.1 章 / 节
- 章号 = 论文序（1–6），由 `main.tex` 的 `\chapter` 自动给出，**译者不写 `\chapter`**。
- 节号由 `\section` 自动给出：文章第 k 章的第 n 节 ⇒ 编号 `k.n`（如第 4 章第 5 节 ⇒ `4.5`）。
  → 只在原文有编号的节标题处写 `\section{译文标题}`，**一个原文编号节 = 一个 `\section`**，不多不少。
- 子节 `\subsection{...}`（自动 `k.n.m`）、子子节 `\subsubsection{...}`。
- 原文无编号的节标题（如 "Acknowledgements"）用 `\section*{...}`（不编号，不进目录）。

### 1.2 编号公式（唯一真值 = work\tags\tags_all.txt）
- 原文编号 `(t)` 位于第 k 章 ⇒ 写成 `\tag{k.t}`：
  - 例：Chan 2014 的 `(6.1)`（第 1 章）⇒ `\tag{1.6.1}`；
  - Gross 2013 的 `(10.2)`（第 4 章）⇒ `\tag{4.10.2}`；
  - Yang Li 的 `(5)`（第 5 章）⇒ `\tag{5.5}`；
  - Collins–Lin 的 `(2.1)`（第 6 章）⇒ `\tag{6.2.1}`。
- 写法固定：
  ```latex
  \begin{equation}
  ... \tag{1.6.1}
  \end{equation}
  ```
  多行公式用 `align`/`gather`，**每条编号一个 `\tag`**；一条编号跨多行时 `\tag` 放最后一行。
- **无编号公式用 `\[ ... \]` 或 `equation*`，绝不自造编号。**
- 原文里出现编号的位置/条数必须与 `work\tags\tags_all.txt` 在该块页段的清单**完全一致**：不缺、不重、不跳、不新增。
- 公式过宽（Overfull）时：
  ```latex
  \begin{equation}
  \resizebox{0.97\textwidth}{!}{$\displaystyle ...$}\tag{4.10.2}
  \end{equation}
  ```

### 1.3 定理类编号（手工给）
- 原文按节编号（`Theorem 3.1`、`Definition 5.2`）⇒「章.节.原编号」：
  `\begin{theorem}{4.3.1}`、`\begin{definition}{4.5.2}`、`\begin{conjecture}{4.5.5}`、`\begin{lemma}{4.2.7}`。
- 原文按**全章连续**编号（如第 5 章的 `Question 1–5`、`Remark 1–8`）⇒「章.原编号」：
  `\begin{question}{5.1}` … `{5.5}`、`\begin{remark}{5.1}` … `{5.8}`。
  （此类编号会与公式号 (5.1) 字面相同，但标签分别为「问题」「注」，属规则使然，不避让。）
- 原文没有编号的定理类陈述：`\begin{theorem}{}`（空编号，只印"定理"）。
- 可用环境（在 preamble 已定义，**禁止自己 `\newtheorem`**）：
  `theorem, proposition, lemma, corollary, definition, conjecture, question, remark, example, observation, claim, hypothesis, construction, fact, notation, setup, exercise, answer, proof`
- 命名定理：`\begin{theorem}{4.5.2}[Hein]` → 印"定理 4.5.2（Hein）"。
- `proof` 环境：`\begin{proof} ... \proofend \end{proof}`（原文有 □ 才写 `\proofend`）。

### 1.4 图 / 表
- 原文图题 "Figure 3"（第 4 章）⇒ 图号 `4.3`；`\figtitle{4.3}{译文图注}`。
- 插图：`\figimg[0.72]{p4_fig03.png}`（`work\figures\` 下的图；宽度系数按图调整，0.5–0.85）。
  图与图题**紧贴、不浮动**，按原文位置放。
- 原文表题 "Table 2" ⇒ `\tabtitle{k.2}{...}`（本集 6 篇无表格，若发现表格立刻报告 Lead）。
- 图内文字（标注/箭头说明）不重画，原图裁图已含；若图无法辨认，报告 Lead。

### 1.5 文献引用
- 保持原文 `[12]`、`[45–54]` 原样（区间用 `--`，即 `[45--54]`）。**不用 `\cite`。**
- 式/节/定理的交叉引用用纯文本：「式 (1.6.1)」「第 3 节」「定理 4.5.2」——**不用 `\ref` / `\eqref` / `\label`**。

## 2. 片段（chunk）写作规则

- 只写**正文片段**：从 `\section{...}` 或段落开始，**不含** `\documentclass`、`\usepackage`、`\begin{document}`、`\chapter`、`\appendix`、`bibliography`。
- 每个原文页起始处插一行注释：`% [原文 p.N]`（N = 该 PDF 的页号 = 印刷页号，偏移 0）。
- 文件开头写一行：`% ===== tr-04 块1：第 4 章 pp.1–13（原文页 1–13）=====`。
- 文件必须：UTF-8 **无 BOM**、**LF** 换行、无 U+FFFD。
- 每个文件 **4–6 个原文页**为宜（见 BRIEF 的分片表）；写完一个立刻保存，再写下一个，避免单文件过长。
- 段落之间空一行；中文用全角标点「。，、；：？！」，数学环境内用英文标点与空格。

## 3. 可用宏（preamble 已定义，直接用）

| 宏/环境 | 用法 | 说明 |
|---|---|---|
| `\section{标题}` / `\subsection{标题}` / `\subsubsection{标题}` | 原文编号节 | 自动编号 = 章.节 |
| `\para{小标题。}` | 原文段首粗体小标题 | 独立成段、粗体、不缩进 |
| `\begin{theorem}{k.s.n}` 等 | 定理类 | 见 §1.3 |
| `\begin{proof}` … `\proofend` | 证明 | |
| `\figimg[0.72]{p4_fig03.png}` | 插图 | 居中、不浮动 |
| `\figtitle{4.3}{图注}` / `\tabtitle{...}` | 图/表题 | 手工编号 |
| `\begin{keybox}{标题}...\end{keybox}` | 要点框（原文灰底框有标题） | |
| `\begin{keyboxplain}...\end{keyboxplain}` | 要点框（无标题） | |
| `\R \C \Z \Q \N \PP` | 数集/射影空间 | 等价 `\mathbb{R}` 等 |
| `% [Tutor Note: ...]` | 批注（注释，不排版） | 见 §6 |

**禁止**使用未在 preamble 定义的宏。需要新宏 → 报告 Lead（Lead 统一加，不自行 `\newcommand`）。

## 4. 数学抄写规则（本项目最大质量风险）

- **文字层数学一律不可信**：`work\split\pNNN.txt` 只用于定位论证与段落结构。
  `\frac{m}{2}` 可能抽成 `2m`，`n_\ell-1` 可能抽成 `n_{\ell-1}`，ω 抽成 f，α 抽成 a，`\mathcal{N}` 抽成 N。
- **每个公式必须对照页图（`work\pages\pK\pNNN.png`，200 dpi）逐符号抄写**，核对：
  上下标归属、指标 i/j/I/J、ε₁ vs ε₂、分子/分母归属、求和/求积范围、花体 vs 正体、
  `\bar` vs `\overline` vs `\tilde` vs `\check`（镜像流形一律 `\check X`，这是 SYZ 文献惯例）、`\cong`/`\simeq`/`\sim`。
- 看不清 → 裁图放大：
  ```
  & $py "<本地路径>" <页> <x0> <y0> <x1> <y1> <out.png> [dpi]
  ```
  （坐标是 PDF 点，整页 612×792；默认 500 dpi）。裁完 `read_image` 复核。
- **原文疑似笔误**：先 500+ dpi 裁图复核；确认后才在 `% [Tutor Note: ...]` 里指出并给正确形式；**正文照原样排**。
- 抄写时保持原文的数学记号体系（不要擅自"改进"记号或补全作者没写的步骤）。

## 5. 翻译体例

- 忠实：不增删、不概括、不合并段落；原文一句 = 译文一句（长句可断句，但不得丢信息）。
- 术语：严格按 `work\glossary.tsv`；首次出现可在括号内附英文原词（人名、模型名、缩写如 SYZ、CY、Kähler 保留原文/惯例写法）。
- 人名保留原文拼写（Strominger、Yau、Zaslow、Gross、Chan、Kontsevich、Soibelman、Legendre…）。
- 「special Lagrangian」= 特殊拉格朗日（子流形）；「torus fibration」= 环面纤维化；「affine manifold」= 仿射流形；
  「Monge–Ampère」= Monge–Ampère 度量/方程；「large complex structure limit」= 大复结构极限；
  「maximally unipotent degeneration」= 极大幂零退化；「tropical」= 热带（几何/曲线/流形）；
  「log structure」= 对数结构；「collapsing」= 坍缩；「non-archimedean」= 非阿基米德。
- 原文行内强调（*italic*）→ `\emph{...}`；粗体 → `\textbf{...}`（但中文不斜体，术语强调用引号或调整）。
- 列表：原文 (1)(2)(3) 枚举 → `\begin{enumerate}`；横杠项 → `\begin{itemize}`。列表项内公式照抄。
- 脚注：`\footnote{译文}`；脚注编号自动，**不要手工编号**；脚注内容完整翻译。
- 摘要在该章第一个片段（Lead/首位译者）翻译，格式：`\section*{摘要}` + 正文一段（不进目录）。
- 原文 `References` 不翻译（Lead 脚本自动转录英文原貌），译者不要碰参考文献。

## 6. 批注（Tutor Note）

- 格式：`% [Tutor Note: 一句话说明]`，可以含数学但不进入排版；**不得出现不成对的 `$`**。
- 数量：每 2–3 个原文页 ≥1 条，每节 ≥3 条（短文按比例）。
- 内容必须是**可验证**的：易错符号/隐含约定/被省略的论证步骤/术语辨析/原文笔误（附裁图证据）。
- 禁止空话（"此处很重要"）、禁止编造物理/数学内容。

## 7. 禁止事项（违反即返工）

1. `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\newtheorem`、`\chapter`、`\tableofcontents`；
2. markdown 语法（`**粗体**`、`# 标题`、`- 列表` 的 md 写法）；
3. `\ref` / `\eqref` / `\cite` / `\label`；
4. 自造编号、漏编号、重编号；
5. 整段未翻译英文留在正文（专有名词除外）；
6. 在批注里写不成对的 `$`；
7. 改动 `preamble.tex` / `main.tex` / STYLE_GUIDE / glossary / 别人的 chunk；
8. 编译（Lead 统一编译）；
9. 用 Python 正则批量改 .tex（Lead 落改用 exact-match patch 脚本）。

## 8. 文字层可靠度分级

- ✅ 正文单词、段落边界、脚注、章节标题 → 可信，用于定位与理解；
- ❌ 数学符号 → 不可信，必须看图；
- ⚠️ 任何「原文笔误」指控 → 先 500+ dpi 裁图复核，否则不写。

## 9. 每块开工流程（固定）

1. 读 `work\STYLE_GUIDE.md`（本文）、`work\BRIEF.md`、`work\glossary.tsv`、`work\TIMELINE.md`（全文）；
2. 读 `work\tags\tags_all.txt` 中自己块内的 tag 清单（BRIEF 已列出）；
3. 按页推进：先 `read` `work\split\pK\pNNN.txt`（理解结构）→ 再 `read_image` `work\pages\pK\pNNN.png`（逐符号抄公式）→ 写 chunk 文件；
4. 每完成一片立刻保存；全部完成后按交付清单自检；
5. `send_message` 给 lead，按 §10 回报。

## 10. 回报格式（固定 5 项，缺一不可）

```
① 文件与页段：<chunk 文件名列表>，第 k 章 pp.A–B（PDF 页）
② tag 区间：<本块 tags>，逐条核对结果（齐全/缺/存疑）
③ 原文可疑或笔误：页码 + 式号 + 判据（裁图坐标/放大倍数）；没有就写"无"
④ 新增术语：英→中（已写入 glossary 请求）
⑤ 自检结果：逐项 pass/fail（tag 完整性、括号/环境/`$`、无 markdown、UTF-8 无 BOM/LF、页数覆盖）
```

## 11. 自检清单（交稿前逐项过）

- [ ] 本块每个原文页都有 `% [原文 p.N]`，页段无缺口、无重复
- [ ] 本块 tag 清单与 tags_all.txt 完全一致（不缺/不重/不自造）
- [ ] 花括号平衡；`\begin`/`\end` 成对；`$` 数为偶（注释里也算）
- [ ] 无禁用命令、无 markdown、无 `**`
- [ ] 定理类环境都用 `{k.s.n}` 编号；图号 `k.n` 正确
- [ ] 公式逐页对照页图抄写（不是从文字层直接搬）
- [ ] 术语与 glossary 一致；跨块术语漂移已在回报中标注
- [ ] 文件 UTF-8 无 BOM、LF、无 U+FFFD；每文件 4–6 页
