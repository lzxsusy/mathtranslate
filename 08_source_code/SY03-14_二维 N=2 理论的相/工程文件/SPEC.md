# 交付规范（SPEC）——本项目唯一契约，冲突时以本文件为准

项目：Edward Witten, *Phases of N=2 Theories in Two Dimensions*, IASSNS-HEP-93/3, arXiv:hep-th/9301042v3（92 页）
产出：简体中文学术版 LaTeX 源码（分片）+ 公式保全 + 学术级审校批注 + 可编译 PDF。

---

## 0. 你负责什么

你只负责写 **一个** `.tex` 分片文件（路径见分工表），内容是你所负责页面的完整中译正文。
**不要**写导言区、**不要** `\begin{document}`、**不要** `\input`、**不要**修改 `main.tex`、**不要**动别人的分片。
Lead 负责装配与编译。

文件开头必须写：

```latex
% ============================================================
% 分片：s03b-singularity  对应原文 PDF 第 20--28 页（印刷页码 20--28）
% 负责章节：3.2 The "Singularity"
% 译者：<你的名字>   审校状态：初稿
% ============================================================
```

## 1. 材料（全部在 workspace 下，用 read 工具读文本，用 read_image 看图）

| 材料 | 路径 | 用途 |
|---|---|---|
| 整页图像（160 dpi） | `witten9301042-zh/pages/page-NN.png`（NN=PDF 页码，补零两位） | **公式与版面的唯一权威** |
| 每页文字层 | `witten9301042-zh/text/page-NN.txt` | 正文措辞参考（**公式在此不可信**） |
| 局部放大工具 | `witten9301042-zh/tools/crop.py` | 公式看不清时放大细看 |
| 术语表 | `witten9301042-zh/GLOSSARY.md` | 强制统一术语 |

PDF 页码 = 印刷页码。文字层会把 `\frac{1}{\sqrt2}` 拆成 `1` `√` `2` 并丢失上下标，**绝不能照抄文字层里的公式**。

放大某个公式区域（PDF 点坐标，页面 612×792 pt）：

```powershell
$py="<本地路径>"
& $py witten9301042-zh\tools\crop.py --page 22 --rect 120,300,520,430 --dpi 500 --out witten9301042-zh\tools\z1.png
```

然后 `read_image` 读 `z1.png`。若仍认不出符号：写 `\colorbox{yellow}{??}` 并在同一行加注释
`% [待确认: 第N页第k个公式，符号无法辨认]`，继续往下做，不要猜。

## 2. 分片分工表（页码均为 PDF 页码 = 印刷页码）

| 文件 | 页码 | 章节 |
|---|---|---|
| `s01-intro.tex` | 2 -- 4 开头（§2 标题之前） | §1 Introduction |
| `s02a-fieldtheory.tex` | 4（§2 标题起）-- 9 | §2 FIELD THEORY BACKGROUND（前半） |
| `s02b-fieldtheory.tex` | 10 -- 15 | §2 续（后半，至第 15 页末） |
| `s03a-model.tex` | 16 -- 19 | §3 THE C-Y/L-G CORRESPONDENCE + 3.1 The Model |
| `s03b-singularity.tex` | 20 -- 28 | 3.2 The "Singularity" |
| `s03c-applications.tex` | 29 -- 34 | 3.3 Applications |
| `s03d-twisted.tex` | 35 -- 43 | 3.4 The Twisted Models In Detail |
| `s04-geometry.tex` | 44 -- 48 | §4 SOME GEOMETRICAL BACKGROUND |
| `s05a-wps-toric.tex` | 49 -- 57 | §5 GENERALIZATIONS + 5.1 Hypersurfaces In Weighted Projective Space + 5.2 Hypersurfaces In Toric Varieties（5.2 自第 52 页起） |
| `s05b-grassmann-intersect.tex` | 58 -- 65 | 5.3 Hypersurfaces in Grassmannians + 5.4 Intersections Of Hypersurfaces（5.4 自第 62 页起） |
| `s05c-topology.tex` | 66 -- 74 | 5.5 Change Of Topology |
| `s06a-superfields.tex` | 75 -- 81 | §6 EXTENSION TO (0,2) MODELS + 6.1 (0,2) Superfields |
| `s06b-models.tex` | 82 -- 86 | 6.2 Some Models |
| `s07-references.tex` | 87 -- 92 | REFERENCES（文献编号 1--53） |

片段边界：起始页从该页第一个属于你范围的词开始；结束页到最后一个属于你范围的词（整段/整式）结束为止。
若边界处一句话跨页，**从句子中间切分时按语义完整取**，并在注释里注明 `% [跨页接续: 原文第N页/N+1页]`。

## 3. 结构

- 用 `\section{中文标题}`、`\subsection{...}`、`\subsubsection{...}`，**层级与原文严格一致**。原文 `3.1.` = `\subsection`。
- 标题按中文学术习惯译，见 GLOSSARY。章节编号由 LaTeX 自动生成，**不要**手写编号。
- 原文的非编号小标题（如 §2 中的 *Fayet-Iliopoulos term*、*Twisted Chiral Superpotential*、*Symmetries* 等独立成行的斜体小标题）用
  `\subsection*{...}` 或 `\subsubsection*{...}`（保持与原文一样的视觉层级），**不加编号**。
- 在每个 `\section`（仅 §1--§6 这六级）开头，紧接标题之后写：

```latex
\begin{keytakeaway}
\textbf{核心物理图像：}……
\textbf{数学工具：}……
\textbf{主要结论：}……
\end{keytakeaway}
```

（`keytakeaway` 环境由 Lead 在 `main.tex` 中定义，直接用即可。）
每个 `\subsection` 开头可选加一至两句 "要点："，但非必需。
- 每页起始处插入页码锚点注释：`% ==== 原文 PDF 第 N 页（印刷页 N）====`。

## 4. 数学保真（最高优先级）

1. **每个带编号公式必须锁号**：`\begin{equation}\tag{2.1} ... \end{equation}`，编号完全照抄原文。
   多行公式用 `\begin{equation}\begin{aligned}...\end{aligned}\tag{2.3}\end{equation}`，`\tag` 放在 `equation` 层。
2. 原文无编号的展示公式用 `\[ ... \]` 或 `equation*`，**不要**自动编号，不要自创编号。
3. 行内公式 `$...$`；不要用 `\(...\)`。
4. 上下标、希腊字母、指标位置严格按图像：`\bar\theta^{\dot\alpha}`、`\sigma^m_{\alpha\dot\alpha}`、`\epsilon^{0123}`、`q_i`、`x^i`。
   注意 Witten 用 `\omega` 表 Kähler form、`W` 超势、`f` 扭超势、`r` FI 参数、`e` 规范耦合。**不要改动符号名**。
5. 常用固定写法：`\mathrm{Tr}`、`\operatorname{Tr}`、`\mathrm{d}` 仅在原文排成直立体时用，原文斜体 `d` 就写 `d`；`\mathbb{Z}`、`\mathbb{R}`、`\mathbb{C}`、`\mathbb{P}^n`、`\mathcal{O}(n)`、`\mathcal{N}=2`。
6. 矩阵用 `pmatrix`；不要用 Unicode 数学符号（不允许 `α`、`∑`、`∫`、`→` 出现在数学里）。
7. 原文疑似笔误（指标重复、符号不一致、指数写错）：**照抄原样**，紧跟一行
   `% [原文疑误: 说明理由 + 建议]`。
8. 引用原文公式一律写字面编号，如「式 (2.1)」，不用 `\ref`。

## 5. 文风与术语

- 学术书面中文，简洁、无口语、无「让我们」「大家」「可以看到」这类填充。第一人称 "I" 译为「作者」或改用无主句，不写「我」。
- 首次出现的术语在该处给英文原词：`规范场论（gauge theory）`；其后只用中文。
- 模型名、人名、群名、文献编号、公式编号、图号保持原样：`Calabi–Yau`、`Landau–Ginzburg`、`N=2`、`U(1)`、`[3]`、`(2.17)`。
- 数学环境内一律英文/符号，中文只能出现在 `\text{...}` 或 `\mbox{...}` 里。
- 保留原文的省略、跳跃、模糊之处：**直译原意 + 批注**，严禁自行补全物理内容、严禁删段、严禁合并段落、严禁「总结式改写」。
- 脚注用 `\footnote{...}`，编号由 LaTeX 自动生成（原文脚注编号在转换后会整体偏移，属正常，在 Reviewer Note 中说明一次即可，不要逐条注）。
- 原文的方括号插入语、破折号、引号照译：中文引号用「」或“”；英文里的人名不译。

## 6. 批注（必须做，宁少勿滥，每条都要有技术含量）

1. `% [Tutor Note: ...]` —— 放在相关公式或段落的**上一行或紧接下一行**独立成行。内容限于三类：
   - **推导补足**：作者用 "It is obvious that / one easily sees / clearly" 跳过的地方，写出被跳过的关键一步或所用定理（如 Duistermaat–Heckman 定理、Mumford 几何不变量理论、指标定理、超对称 Ward 恒等式）。
   - **易错预警**：指标升降、张量缩并、符号约定（如 $\epsilon_{12}=-1$、度规号差 $(-,+,+,+)$、$\sigma^m$ 的约定）易错处必须提示核对原文哪一条约定。
   - **物理图像**：说明该式在相结构/σ 模型/RG 流中的含义（一句话，具体）。
   每个分片**至少 4 条、至多 12 条**；纯文献罗列处（如 §5 引文段落）可减少。
2. `% [原文疑误: ...]` —— 确认为原文笔误时用，必须给出判断依据，不确定就写 `% [存疑: ...]`，禁止断言。
3. `% [背景补充: ...]` —— 仅在原文术语对中文读者有实质门槛时（如「环面簇」「GIT 商」）加一句准确解释；**不超过 2 条/分片**。
4. 所有批注用中文，`%` 后空一格，不要用 `\marginpar`、不要用 `\todo`。

## 7. 图表

- 本文共 92 页，经矢量图形/位图检测：**无图片、无插图、无带框表格**（全篇为纯文字与公式）。
- 如果你在实际页面里发现**表格样式的排版**（对齐的数值列，例如权重/次数表）：用 `table` + `tabular` 忠实重建，`\caption{表 X（原文第 N 页）}`。
- 如果你发现**任何真正的图形（Figure）**：立刻在该页注释 `% [待剥离图: 第N页，说明内容]`，并在回报中告知 Lead（Lead 负责裁剪与 \includegraphics 插入），分片里先留 `% FIGURE-PLACEHOLDER-N`。

## 8. 自检（提交前必须执行）

```powershell
$py="<本地路径>"
& $py witten9301042-zh\tools\lint_frag.py witten9301042-zh\sections\<你的文件>
```

检查项：无导言区/`\begin{document}`、环境配对、花括号平衡、`\tag` 编号与原文一致且不重复、无 Unicode 数学符号、无遗留英文正文段落、`%` 批注格式合法。**必须 0 error**。

## 9. 回报格式（最后一条消息）

```
文件：sections/xxx.tex
覆盖：PDF 第 a--b 页；章节 …
公式：共 N 个带号公式，编号 (x.y)--(x.z)，无缺号
批注：Tutor Note N 条、原文疑误 N 条
问题：无 / 具体问题（跨页句子、无法辨认符号、疑似原文笔误）
```

## 10. 禁止事项

- 禁止机翻腔、禁止删减、禁止把公式写成图片、禁止改符号、禁止自作主张「修正」原文。
- 禁止在数学里写中文；禁止 `\textwidth` 之外乱改版式；禁止自定义 `\newcommand`（除非 Lead 批准）。
- 禁止声称已验证未验证的内容。拿不准就标注。
