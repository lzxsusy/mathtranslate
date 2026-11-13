# 翻译与排版规范（TASI Chern-Simons 讲义中译工程）

本文件是每个翻译子代理必须遵守的**硬性规范**。违反规范的产物会被退回重做。

## 0. 工作对象

原文：Gregory W. Moore, *Introduction To Chern-Simons Theories*（2019 TASI 讲座讲义，249 页 PDF，TeX 排版）。
你的任务：把分配给你的**页码范围**内的全部英文内容，无损转写并翻译为**中文学术 LaTeX 源码片段**，写入指定输出文件。

原文 PDF 页（即 PDF 阅读器显示的页码）= 印刷页码 + 1。例如印刷第 39 页 = PDF 第 40 页 = `work/pages/p040.png`。

## 1. 输入与输出

- 文本层（供快速通读 prose）：`work/chunks/cNN.txt`，逐页以 `===== PDF p.X (printed p.Y) =====` 分隔。**文本层里的公式是残缺的**（上下标丢失、符号错位），只能用来读句子结构，**公式一律以页面图片为准**。
- 页面图片：`work/pages/pNNN.png`（150 dpi，NNN = PDF 页码，三位补零）。**必须逐页用 `read_image` 看过**，据此转写公式、符号、编号、脚注、图注。
- 图表成品：`figures/figNN.png`（已裁好的原图）。
- **输出**：把 LaTeX 片段写入 `chunks/cNN.tex`（UTF-8，无 BOM）。只写正文片段：不要 `\documentclass`、不要 preamble、不要 `\begin{document}`、不要 `\end{document}`、不要 `\tableofcontents`、不要 `\appendix`、不要 `\bibliography`。

## 2. 翻译标准

- 简体中文书面学术语体。术语以中文学界惯例为准（见 §9 词表，词表优先）。
- 术语**首次出现**时在中文后括注英文原词，例如「和乐群（holonomy group）」「反常（anomaly）」；后文不再重复。
- 忠实、完整：**不删句、不并段、不概括、不增补原文没有的物理内容**。原文一个段落对应译文一个段落。
- 原文的口语化/玩笑/自嘲照译（作者文风要保留），不要改成生硬教科书腔。
- 公式里的变量名、算符名、群名（$SU(2)$、$U(1)$、$\mathfrak{g}$ 等）保持原样，不译。
- 人名首次出现给中文 + 原文：Witten（威滕）→ 建议直接写 Witten，不必音译；数学家/物理家人名一律保留拉丁字母。
- 脚注：`\footnote{...}`，内容照译。
- 数字、单位、文献编号 `[15]`、章节引用「Appendix C」「Section 2.2」按原文，可写「附录 C」「第 2.2 节」但需与原文编号一致。
- 连字修复：PDF 文本层里的 `ﬁ ﬂ ﬀ ﬃ ﬄ` 要还原成 `fi fl ff ffi ffl`。

## 3. 章节层级（必须精确复刻原文编号）

| 原文编号形态 | LaTeX 命令 |
|---|---|
| `1.` `2.` … `11.`，`A.` … `M.` | `\section{中文标题}` |
| `2.1` `4.5` `B.2` | `\subsection{中文标题}` |
| `2.2.7` `4.5.3` `I.7.1` | `\subsubsection{中文标题}` |

- 每个标题行后面必须加注释保留英文原题：`\section{大视野导论} % 原文: 1. Introduction: The Grand Overview`
- 编号由 LaTeX 自动生成，**不要手写编号**（不要写 `\section{2.1 ...}`）。
- 只在原文出现标题的位置输出标题命令；你的片段可能从某个小节的**中间**开始，此时**不要**补标题。
- 标点：中文标题内不用英文句点；标题后的原文句号不要。

## 4. 公式（本工程最重要的一条）

- 行内公式：`$...$`。独立公式：`\begin{equation}...\end{equation}`。
- **每个带编号的公式必须用 `\tag{}` 复刻原编号，并用 `\label{}` 标注**，编号从页面图片上逐字抄：

```latex
\begin{equation}
  \delta \mathrm{cs}(A) = 2\,\mathrm{tr}\,(\delta A\, F) - d\,\mathrm{tr}(A\,\delta A)
  \tag{1.6}
  \label{eq:1.6}
\end{equation}
```

- 无编号公式用 `\begin{equation*}...\end{equation*}`（不要 `\[ \]`，保持统一）。
- 多行对齐用 `\begin{align}` + 每行 `\tag{x.y}`（原文若每行都有编号）；`\label{eq:x.y}` 放在 **第一个** `\tag` 所在行末尾之前。对齐点用 `&`，不要滥用。
- 正文里引用公式编号时写 `\eqref{eq:1.6}`（会自动生成括号），不要手打「(1.6)」——除非该公式在原文中根本没有编号。
- 符号转写要求：上下标、希腊字母、花体（`\mathcal`）、哥特体（`\mathfrak`）、黑板粗体（`\mathbb`）、粗体向量（`\mathbf` / `\bm`）、 accents（`\hat \tilde \bar \dot \prime`）、`\wedge \otimes \oplus \cong \simeq \sim \partial \nabla \oint \int \sum \prod \langle \rangle \| \cdot \times \star \ast` 必须逐字核对。**宁可多看一眼图片，也不要猜。**
- 微分号：原文若用直立体 `d`，保持 `d`（可 `\mathrm{d}` 或直接 `d`，同一片段内部统一即可）。
- 矩阵用 `pmatrix/bmatrix`；分段函数用 `cases`；范数 `\|`；`\operatorname{tr}`、`\operatorname{Tr}`、`\operatorname{Re}`、`\operatorname{dim}`、`\operatorname{deg}` 等用 `\operatorname{}`。
- 原文若确有**笔误/疑似错误**：照原文转写，**不要擅自改**，在该公式后加一行注释：`% [Tutor Note: 原文此处疑有笔误：$\partial_\mu$ 应为 $\partial^\mu$；核对 (2.41) 的量纲可知……]`。

## 5. 图

原图已裁好，路径 `figures/figNN.png`，NN 与原文图号一致。用：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.85\textwidth]{figures/fig05.png}
  \caption{$\mathbb{R}^3$ 中两条相互链接的曲线 $C_1$ 与 $C_2$。（原文 Fig.~5，第 62 页）}
  \label{fig:5}
\end{figure}
```

- `\caption` 中文，图号由 LaTeX 自动生成（原文图号连续，故自然对齐）；括号内注明原文图号与**印刷页码**。
- 图放在原文图注所在的段落位置（作者通常把图放在图注页正文之前或之后，就近即可，但**不可移到别的章节**）。
- 若图注很长，完整翻译，不要节略。
- 不要用 TikZ 重画图，不要插入任何与原文无关的图片。

## 6. 每节重点（Key Takeaways）

**每个 `\section` 开头**（正文第一段之前）插入：

```latex
\begin{keytakeaways}
  \item 物理图像：……
  \item 数学工具：……
  \item 核心结论：……
\end{keytakeaways}
```

3–5 条，每条一句到两句，必须基于该节实际内容，**不许空话套话**（禁止「本节十分重要」这类零信息句子）。`\subsection` 开头不要求。

## 7. 批注（Tutor Note）

在关键处插入 LaTeX 注释（不进入排版），格式严格为：

```latex
% [Tutor Note: 此处推导极易出现符号错误……]
```

至少覆盖下列类型，每 2–3 页不少于 1 条，全片段 3–8 条：

1. **易错点**：涉及指标缩并、符号约定、归一化、升降指标、留数/解析延拓、相位因子时，点明该核对什么，并引原文公式编号。
2. **含糊点**：作者写 "It is obvious that / One easily checks / It is well-known that" 而跳过证明时，说明被省略的是什么（哪条定理、哪类泛函分析/代数几何结果），建议查阅什么文献或附录。
3. **逻辑跳步**：从 A 到 B 缺了中间一步时，把中间步骤用一句话点出（只点逻辑，**不引入新物理**）。
4. **翻译取舍**：某术语有多种中文译法时说明取舍。

不要写空洞评语（「这里很重要」「值得注意」）。批注要具体到公式编号/定理名称。

## 8. 原文自带批注的处理

作者在稿件里留了大量编辑标记（如 `**** NEED TO COMMENT ON ...`、`♣say what problem they were addressing♣`、`AGOL THEOREM ... NEED TO SAY SOMETHING ABOUT ...`、脚注里 `[1988 ??]`）。这些是**原文的一部分**，必须保留：

- 正文中可见保留为小号灰字：`{\small\itshape ［原文标记：……］}`（内容译出，保留原意），同时加注释 `% [原文待办标记，原文 p.X]`。

## 9. 术语表（优先使用）

| English | 中文 | English | 中文 |
|---|---|---|---|
| Chern-Simons theory | Chern-Simons 理论 | gauge theory | 规范场论 |
| gauge field | 规范场 | gauge transformation | 规范变换 |
| connection | 联络 | curvature | 曲率 |
| holonomy | 和乐（群） | flat connection | 平坦联络 |
| anomaly | 反常 | framing anomaly | 标架反常 |
| moduli space | 模空间 | phase space | 相空间 |
| symplectic form | 辛形式 | Kähler quotient | Kähler 商 |
| geometric quantization | 几何量子化 | prequantum line bundle | 预量子线丛 |
| Hilbert space | Hilbert 空间 | path integral | 路径积分 |
| partition function | 配分函数 | correlation function | 关联函数 |
| Wilson line/loop | Wilson 线/圈 | line defect | 线缺陷 |
| linking number | 环绕数 | knot invariant | 纽结不变量 |
| Jones polynomial | Jones 多项式 | braiding | 编织 |
| fusion rules | 融合规则 | conformal block | 共形块 |
| primary field | 主场 | highest weight representation | 最高权表示 |
| affine Lie algebra | 仿射 Lie 代数 | central extension | 中心扩张 |
| central charge | 中心荷 | Virasoro algebra | Virasoro 代数 |
| stress-energy tensor | 能动张量 | operator product expansion | 算符乘积展开 |
| WZW model | WZW 模型 | Wess-Zumino term | Wess-Zumino 项 |
| chiral algebra | 手征代数 | rational CFT | 有理共形场论 |
| modular transformation | 模变换 | theta function | theta 函数 |
| spin structure | 旋量结构 | spin-c structure | spin$^c$ 结构 |
| bordism | 配边 | cobordism | 配边（同义，按原文） |
| topological field theory | 拓扑场论 | extended TFT | 扩展拓扑场论 |
| category | 范畴 | tensor category | 张量范畴 |
| groupoid | 群胚 | functor | 函子 |
| vector bundle | 向量丛 | line bundle | 线丛 |
| characteristic class | 特征类 | Chern class | Chern 类 |
| Chern-Weil theory | Chern-Weil 理论 | invariant polynomial | 不变多项式 |
| de Rham cohomology | de Rham 上同调 | differential cohomology | 微分上同调 |
| anyon | 任意子 | nonabelion | 非阿贝尔任意子 |
| fractional quantum Hall effect (FQHE) | 分数量子 Hall 效应 | edge state | 边缘态 |
| supersymmetry | 超对称 | holography | 全息 |
| Lie algebra | Lie 代数 | dual Coxeter number | 对偶 Coxeter 数 |
| representation | 表示 | irreducible | 不可约 |
| sum over topologies | 拓扑求和 | semiclassical approximation | 半经典近似 |
| level (of CS theory) | 能级（CS 理论的 k） | coupling constant | 耦合常数 |

其余未列术语：查中文学界通行译法，拿不准就「中文（English）」并列。

## 10. 格式细节

- 段落之间空一行；不要手工 `\\` 换行；不要 `\noindent` 满天飞。
- 中文标点用全角（，。；：？！「」），数学环境内保持英文标点。
- 中文与行内公式之间留空格（可选，但同一片段内统一）。
- 列表用 `\begin{enumerate}` / `\begin{itemize}`；编号列表若要复刻原文 (1)(2)(3)，用 `\begin{enumerate}[(1)]`（enumitem 已加载）。
- 原文的 `\item` 列表常被 PDF 拆成 "1." 等编号，按语义还原列表。
- 不要出现空 `\section`；不要在片段里留 `TODO`。
- 可用的宏包（已在主文件加载，不要再 `\usepackage` 于片段中）：amsmath, amssymb, amsthm, mathtools, bm, graphicx, hyperref, xcolor, geometry, enumitem, booktabs, array, ctex。
- 已定义的定理环境：`theorem lemma proposition corollary definition example remark`（中文名已配好）。定理编号由 LaTeX 自动生成，原文若编号不同，加注释说明，不要手打编号。
- 自定义环境：`keytakeaways`（见 §6）。
