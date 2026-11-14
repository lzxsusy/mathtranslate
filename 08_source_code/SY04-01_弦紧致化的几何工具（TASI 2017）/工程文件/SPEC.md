# 交付规范（SPEC）——本项目的唯一技术契约；与英文原文冲突时以英文原文（页面图像）为准

项目：Lara B. Anderson & Mohsen Karkheiran,
*TASI Lectures on Geometric Tools for String Compactifications*,
arXiv:1804.08792v1 [hep-th], 24 Apr 2018；PoS（TASI 2017 Summer School, Boulder CO），原 PDF 共 61 页。
**印前提示：本 PDF 的印刷页码 = PDF 页码 − 1（PDF p1 为标题页，无页码；PDF p2 起印刷页为 1）。**
本文件、页图像、分片文件中出现的"第 N 页"一律指 **PDF 页码**。

> **作者更正（必须遵守）**：本文作者是 **Lara B. Anderson 与 Mohsen Karkheiran（Virginia Tech）**，不是 Edward Witten。
> 任何译注、说明、README、文档标题都不得把本文署名为 Witten；行文中提到 Witten 只能出现在真实相关性处（如 Gukov–Vafa–Witten 超势、Green–Schwarz–Witten 教材 [11]）。
> 原文版权：PoS，CC BY-NC-ND 4.0；译文仅供学习，须在译序中说明。

---

## 0. 你负责什么

你只负责写 **一个（或两个）** `.tex` 分片文件（路径见第 3 节分工表），内容是你所负责页面的**完整中文译注正文**。
**不要**写导言区（preamble）；**不要**写 `\begin{document}`；**不要**写 `\input`；**不要**改 `main.tex`；**不要**动别人的分片、`figures/`、`main.tex`、`build.ps1`。
Lead 负责装配、编译与全局审校。

分片文件开头必须写：

```latex
% ============================================================
% 分片：s03b  对应原文 PDF 第 15--25 页（印刷页 14--24）
% 负责章节：3.3 Algebraic approaches to CY Geometry；3.4 Reid's Fantasy
% 译者：<你的名字>   审校状态：初稿
% ============================================================
```

---

## 1. 材料（全部在工作区 `gk1804/` 下；用 read 读文本，用 read_image 看页面图像）

| 材料 | 路径 | 用途 |
|---|---|---|
| 整页图像（150 dpi 灰度） | `pages/page-NN.png`（NN = 01–61） | **公式、版式、脚注的唯一权威** |
| 每页文字层 | `text/page-NN.txt` | 仅用于正文措辞与定位；**公式在此不可信** |
| 局部放大工具 | `tools/crop.py` | 公式看不清时放大细看 |
| 图表文件 | `figures/fig01.png` … `fig10.png` | 直接 `\includegraphics` |
| 公式编号清单 | `notes/eq-inventory.md` | 每页应出现的带号公式（仍需以图像核对） |
| 术语表 | `GLOSSARY.md` | 强制统一术语 |
| 原文合并文本 | `fulltext.txt` | 跨页上下文检索 |

放大某个公式区域（PDF 点坐标，页面 595.276 × 841.89 pt，原点左上）：

```powershell
$py = "<本地路径>"
& $py gk1804\tools\crop.py --page 22 --rect 120,300,500,430 --out gk1804\tmp\z1.png
```

然后 `read_image` 看 `gk1804\tmp\z1.png`。**文字层会把分数、上下标、希腊字母拆散并丢失信息，绝不允许照抄文字层里的公式。**

---

## 2. 分片分工表（PDF 页码）

| 文件 | PDF 页 | 章节（原文编号） | 必须锁定的公式编号 | 图表 |
|---|---|---|---|---|
| `sections/s01-intro.tex` | 2–4（到 `2. An Illustration` 标题**之前**） | 1. Introduction | 无 | 图 1 |
| `sections/s02-heterotic.tex` | 4（从 `2. An Illustration…` 标题**起**）–8 | 2. An Illustration…；2.1 Dimensional Reduction；SU(3) 结构 | (2.1)–(2.27) | 图 2、表 1 |
| `sections/s03a-cy.tex` | 9–15（到 `3.3` 标题**之前**为止） | 3. Manifolds（示例 1、2）；3.1；3.2 | (3.1)–(3.7) | 图 3、4、5、6、7 |
| `sections/s03b.tex` | 15（从 `3.3` 标题**起**）–26（到 `3.5` 标题**之前**） | 3.3；3.4（含 p26 顶部 3.4 收尾段） | (3.8)–(3.39) | 图 8、9 |
| `sections/s03c.tex` | 26（从 `3.5` 标题**起**）–33 | 3.5；3.6；3.7 | (3.40)–(3.58) | 无 |
| `sections/s04-bundles.tex` | 34–45（到 `5. Conclusions` 标题**之前**） | 4. Role of bundles…；4.1–4.4 | (4.1)–(4.34) | 表 2 |
| `sections/s05-conclusions.tex` | 45（从 `5. Conclusions` **起**）–54（到 `References` **之前**） | 5. Conclusions；A. Appendix | (A.1)–(A.46) | 图 10 |
| `sections/s06-refs.tex` | 54–61 | References | 无 | 无 |

边界规则：起始页从**该页第一个属于你范围的词**开始，结束页到**最后一个属于你范围的词（整段/整式）结束**。跨页断句按语义取完整，并加注 `% [跨页接续: 原文 PDF 第 N 页→第 N+1 页]`。
相邻分片在装配时直接拼接：**不要人为补句、不要删句、不要合并段落。**

---

## 3. 结构规则

- 用 `\section{中文标题}`、`\subsection{...}`、`\subsubsection{...}`，**层级与原文严格一致**：原文 `3.` = `\section`；`3.1` = `\subsection`；`3.1.1` = `\subsubsection`。
  标题编号由 LaTeX 自动生成（`\section` 计数与原文一致，附录用 `\appendix`）。
- 每个标题后紧跟一行注释给原文英文标题，便于对照：`% EN: 3.1 A brief overview of Calabi-Yau manifolds`。
- 原文的非编号小标题（如 `• Complex manifold`、`Example 1: Calabi-Yau Solutions`、`Observation:`、`Idea:` 等自成一行的粗体/斜体小标题）用 `\subsection*{...}` / `\subsubsection*{...}` 或 `\paragraph{...}`，保持与原文一致的视觉层级，**不加编号**。
- 每个 `\section`（含附录 A）标题之后，紧跟：

```latex
\begin{keytakeaway}
\textbf{核心物理图像：}……
\textbf{数学工具：}……
\textbf{主要结论：}……
\end{keytakeaway}
```

（`keytakeaway` 环境由 `main.tex` 定义，直接用即可。§5 之后的致谢段不写 keytakeaway。）
- 每页起始处插入页锚注释：`% ==== 原文 PDF 第 N 页 ====`。
- 原文脚注用 `\footnote{...}`，编号由 LaTeX 自动生成（与原文字号整体偏移属正常，不手工编号）。

---

## 4. 数学保全（最高优先级）

1. **每个带编号公式必须锁号**：`\begin{equation}\tag{2.17} ... \end{equation}`，编号完全照抄原文。
   多行公式用 `\begin{equation}\begin{aligned}...\end{aligned}\tag{2.3}\end{equation}`；`\tag` 放在 `equation` 层。
   `\tag` 允许形式：`2.1`、`3.76`、`4.34`、`A.1`、`A.46`。**不得缺号、不得重号、不得自创编号。**
2. 原文无编号的展示公式用 `\[ ... \]`，**不要**自动编号。
3. 行内公式 `$...$`（不要用 `\(...\)`）。
4. 上下标、希腊字母、指标位置严格按图像；花体 `\mathcal{H}`/`\mathcal{N}`、德文尖角体 `\mathfrak`、黑板体 `\mathbb{Z}`、`\mathbb{C}`、`\mathbb{P}^1`、`\mathbb{R}` 必须与原文一致。**不要改动符号名。**
5. 常用固定写法：`\operatorname{Tr}`、`\operatorname{Hom}`、`\operatorname{Ind}`、`\mathrm{d}`（原文直立体 d 时）、`\mathcal{O}(n)`、`\bar\partial`、`\wedge`、`\otimes`、`\oplus`、`\simeq`。
6. 矩阵用 `pmatrix/bmatrix`；交换图原文没有就不要造。
7. **源码中禁止出现 Unicode 数学符号**（α、∂、∫、→、≥、×、⊗ 等一律用 LaTeX 命令）；中文只能出现在 `\text{...}`、`\mbox{...}` 或正文里。原文中混排的中文/英文术语（如 "Pheno"）保留原样。
8. 推导中易错处（张量缩并、指标升降、符号约定、指数取舍）必须加 `% [Tutor Note: ...]` 说明"核对哪一条约定"。
9. 原文疑似笔误：**照抄原样**，紧跟一行 `% [原文疑误: 依据 + 建议]`；不确定用 `% [存疑: ...]`，禁止臆断。
10. 引用原文公式写"式 (2.1)"，图写"图 3"，节写"第 3.4 节"，参考文献写 `[37]`（**不要用 `\cite`**）。
11. 原文字体强调（斜体术语、破折号、引号）照译：中文引号用「」或""；英文人名/模型名不译。

---

## 5. 文风与术语

- 学术书面中文，简洁、无口语、无"让我们""大家""可以看到"这类填充；第一人称 "we" 译为「我们」或改无主语，"let us" 译为「下面」或省略。
- 术语以 `GLOSSARY.md` 为准；首次出现的术语在该处给出英文原词：`规范场论（gauge theory）`，其后只用中文。
- 模型名、人名、群名、文献编号、公式编号、图号保持原样：`Calabi–Yau`、`Landau–Ginzburg`、`$E_8$`、`$U(1)$`、`[3]`、`(2.17)`、`Figure 1`（正文写"图 1"）。
- 严格直译原意，**不删段、不并段、不"总结式改写"**；作者跳跃、含糊、省略之处，直译原意 + Tutor Note。
- 图表：`\begin{figure}[htbp]\centering\includegraphics[width=0.7\textwidth]{figures/figXX.png}\caption{中文标题。（原文 Figure N，原文 PDF 第 P 页）}\label{fig:N}\end{figure}`；正文引用写"图 N"。图表插入位置以原文出现处为准。
- 表格用 `booktabs`（`\toprule/\midrule/\bottomrule`）重建，内容逐格照抄原文；表格标题译为中文并标注原文位置。

---

## 6. 批注（Tutor Note）——宁精勿滥，每条都要有技术含量

在关键位置插入 LaTeX 注释（不进入 PDF），单独一行：

```latex
% [Tutor Note: 此处 $H$ 进入的是扭转后的联络 $D+\tfrac18H$；若漏掉 $\tfrac18$ 因子，$\eta_0$ 的和乐群会误判为 SO(6) 而非 SU(3)。
```

每个分片 **至少 4 条、建议 6–10 条**，覆盖三类：
1. **易错预警**：符号约定、指标升降、张量缩并、代数变换中真正容易出错之处（写明核对哪一条约定）；
2. **含糊点拨**：作者写 "it is obvious/clear that…" 而实际省略证明之处，说明省略了什么、依据哪条定理（如 Berger 分类、Yau 定理、Donaldson–Uhlenbeck–Yau 定理、Atiyah–Singer 指标定理）；
3. **背景/直觉**：该构造的几何或物理意义，一两句点到为止。
禁止空话（"很重要""值得注意"）。注释里不要出现 `%` 字符（会截断注释）。

---

## 7. 交付前自检（必须逐条做，最后在汇报里逐项确认）

0. 本机 PowerShell 禁止运行 `.ps1` 脚本，**不要用** `pwsh -File`。统一用下面两条命令
   （`$py` 为 `<本地路径>`，
   在**工作区根目录**即 `default-workspace` 下运行）：
   ```
   & $py gk1804\tools\test_fragment.py --fragment sections/sXX.tex     # 必须 COMPILE OK
   & $py gk1804\tools\verify.py --fragment sections/sXX.tex            # 必须无 [ERROR]
   ```
2. 对照 `notes/eq-inventory.md` 与本分片页图像：你的 `\tag{}` 集合与规定区间**完全一致**，无缺号/重号。
3. 全文搜索分片：无 Unicode 数学符号（`[αβγδ∂∫→≥≤×·⊗⊕≈≠∞ℏ]` 等）；无 `\cite`；无 `\begin{document}`。
4. 逐式核对页面图像：每个公式的上下标、分数、根号、指标、正负号与原图一致。
5. 页锚齐全（你负责的每一页都有 `% ==== 原文 PDF 第 N 页 ====`）。
6. 每个 `\section` 有 keytakeaway；标题均带 `% EN:` 原文行。
7. 汇报（用 send_message 给 lead，要短）：文件路径、写出的 tag 区间、备注条数、表/图处理情况、**发现的原文疑误/存疑清单**（页码 + 一句话）、你未解决的风险点。

---

## 8. 拒绝规则

- 遇到无法辨认的符号/公式（放大后仍不可辨）：不要猜。在该处写 `\colorbox{yellow}{??}`，同行加
  `% [存疑: 第 N 页第 k 个公式，符号无法辨认]`，并在汇报中列明"第 N 页出现无法识别的数学符号，需人工确认"。
- 不要加任何与物理无关的插图、装饰、表情、二次元元素。
