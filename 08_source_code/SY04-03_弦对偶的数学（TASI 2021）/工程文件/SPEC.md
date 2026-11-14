# 交付规范（SPEC）——本项目唯一契约，冲突时以本文件为准

项目：Niklas Garner & Natalie M. Paquette,
*TASI Lectures on the Mathematics of String Dualities*,
arXiv:2204.01914v2 [hep-th], 12 Apr 2022（PoS 会议文集，原文 85 页，PDF 页码 = 印刷页码）

产出：简体中文学术版 LaTeX 源码（分片）+ 公式保全 + 图表剥离 + 学术级审校批注 + 可编译 PDF。

> **作者更正**：本 PDF 并非 Witten 的文章，而是 Garner–Paquette 的 TASI 2021 讲义。
> 译文与注释一律以此事实为准，不得在任何地方把作者写成 Witten。

---

## 1. 你负责什么

你只负责写 **一个** `.tex` 分片文件（路径见分工表），内容是你所负责页面的完整中译正文。
**不要**写导言区、**不要** `\begin{document}`、**不要** `\input`、**不要**修改 `main.tex`、**不要**动别人的分片。
Lead 负责装配与编译。

文件开头必须写：

```latex
% ============================================================
% 分片：s02a  对应原文 PDF 第 4--6 页
% 负责章节：§2 Twisting & mirror symmetry；2.1 A modern introduction to twisting；2.1.1 The nilpotence variety
% 译者：<你的名字>   审校状态：初稿
% ============================================================
```

## 2. 材料（全部在 workspace 下，用 read 工具读文本，用 read_image 看图）

| 材料 | 路径（相对 `asi2204-zh/`） | 用途 |
|---|---|---|
| 整页图像（160 dpi） | `pages/page-NN.png` | **公式、版式、脚注的唯一权威** |
| 每页文字层 | `text/page-NN.txt` | 正文措辞参考（**公式在此不可信**） |
| 局部放大工具 | `tools/crop.py` | 公式看不清时放大细看 |
| 术语表 | `GLOSSARY.md` | 强制统一术语 |
| 已剥离图 | `figures/fig01.png` … `fig14.png` | 直接 `\includegraphics` |
| 公式内嵌示意图 | `figures/inline/eq-p42-a.png` 等 5 个 | 树图/阶梯图的矢量裁图 |

PDF 页面尺寸 595.276 × 841.89 pt。文字层会把分数、上下标、花体字母拆散并丢失信息，**绝不能照抄文字层里的公式**；文字层只用来定位和读纯英文句子。

放大某个公式区域：

```powershell
$py="<本地路径>"
& $py asi2204-zh\tools\crop.py --page 22 --rect 120,300,520,430 --dpi 500 --out asi2204-zh\tools\z1.png
```

然后 `read_image` 读 `z1.png`。若仍认不出符号：写 `\colorbox{yellow}{??}` 并在同一行加注释
`% [待确认: 第N页第k个公式，符号无法辨认]`，继续往下做，不要猜。

## 3. 分片分工表（页码均为 PDF 页码 = 印刷页码）

| 文件 | 页码 | 章节 | 必须锁定的公式编号 |
|---|---|---|---|
| `s01-intro.tex` | 1 – 3 上半（至 p3 上 §1 结束） | 标题页信息（不必写 title）+ §1 Introductory remarks | 无 |
| `s02a.tex` | 3（§2 标题起）– 6 | §2 + 2.1 + 2.1.1 | (2.1)–(2.7) |
| `s02b.tex` | 7 – 9 | 2.1.2 Twisting homomorphisms；2.1.3 Gradings；2.1.4 Equivariant cohomology | 无 |
| `s02c.tex` | 10 – 14 | 2.2 + 2.2.1 + 2.2.2（至 p14 末） | (2.8)–(2.20) |
| `s02d.tex` | 15 – 17 | 2.2.3 Landau–Ginzburg models | (2.21)–(2.29) |
| `s02e.tex` | 18 – 21 | 2.3 + 2.3.1 + 2.3.2 + 2.3.3（至 p21 末） | (2.30)–(2.34) |
| `s02f.tex` | 22 – 26 | 2.3.4 Deformations；2.4 + 2.4.1 | (2.35)–(2.43) |
| `s02g.tex` | 27 – 28 | 2.4.2 $B$-branes and coherent sheaves | (2.44)–(2.46) |
| `s02h.tex` | 29 – 32 | 2.4.3 $A$-branes and the Fukaya category（至 §3 前） | (2.47)–(2.54) |
| `s03a.tex` | 33 – 36 | §3 Homotopy & further developments；3.1 + 3.1.1 + 3.1.2 | (3.1)–(3.8) |
| `s03b.tex` | 37 – 40 | 3.1.3 The secondary product | (3.9)–(3.16) |
| `s03c.tex` | 41 – 44 | 3.2 + 3.2.1 | (3.17)–(3.24) |
| `s03d.tex` | 45 – 46 | 3.2.2 Example: Landau–Ginzburg $B$-model | (3.25)–(3.31) |
| `s03e.tex` | 47 – 50 | 3.2.3 Bulk local operators and Hochschild cohomology | (3.32)–(3.46) |
| `s03f.tex` | 51 – 54 | 3.2.4 Example: $B$-twisted free chiral multiplet；3.2.5；3.2.6 | (3.47)–(3.59) |
| `s03g.tex` | 55 – 60 | 3.3 + 3.3.1 + 3.3.2 + 3.3.3 | (3.60)–(3.76) |
| `s04.tex` | 61 – 65 | §4 Concluding remarks；§5 Acknowledgments；`\appendix`；A + A.1 + A.2 | (A.1)–(A.9) |
| `s05.tex` | 66 – 68 | B + B.1 + B.2 + B.3 | (B.1)–(B.13) |
| `s06.tex` | 69 – 71 | B.4 + B.5 | (B.14)–(B.25) |
| `s07.tex` | 72 – 76 | B 收尾（B.26–B.27）；C + C.1 + C.2 + C.3 | (B.26)–(C.16) |
| `s08-refs.tex` | 77 – 85 | References（文献 1–151） | 无 |

边界规则：起始页从**该页第一个属于你范围的词**开始；结束页到**最后一个属于你范围的词（整段/整式）结束**。
若边界处一句话跨页，**按语义完整取**，并在注释里注明 `% [跨页接续: 原文第N页/N+1页]`；你的分片与相邻分片在装配时是直接拼接的，不要人为补句、不要删句。

## 4. 结构

- 用 `\section{中文标题}`、`\subsection{...}`、`\subsubsection{...}`，**层级与原文严格一致**：
  原文 `1.` / `2.` = `\section`；`2.1` = `\subsection`；`2.1.1` = `\subsubsection`；
  A/B/C 为附录（`s04` 内写 `\appendix` 后用 `\section{...}` 自动得 A）。
- 标题按中文学术习惯译，见 GLOSSARY；章节编号由 LaTeX 自动生成，**不要**手写编号。
- 原文的非编号小标题（如 *A brief aside*、*Symmetries* 等独立成行的斜体/加粗小标题）用
  `\subsection*{...}` 或 `\subsubsection*{...}`（保持与原文一样的视觉层级），**不加编号**。
- 每个 `\section`（含附录 A/B/C）开头，紧接标题之后写：

```latex
\begin{keytakeaway}
\textbf{核心物理图像：}……
\textbf{数学工具：}……
\textbf{主要结论：}……
\end{keytakeaway}
```

（`keytakeaway` 环境由 Lead 在 `main.tex` 中定义，直接用即可。）
§5 Acknowledgments 不写 keytakeaway。
- 每页起始处插入页码锚点注释：`% ==== 原文 PDF 第 N 页 ====`。
- 每个带编号公式前不要加锚点；锚点只在页首。

## 5. 数学保真（最高优先级）

1. **每个带编号公式必须锁号**：`\begin{equation}\tag{2.1} ... \end{equation}`，编号完全照抄原文。
   多行公式用 `\begin{equation}\begin{aligned}...\end{aligned}\tag{2.3}\end{equation}`，`\tag` 放在 `equation` 层。
   `\tag` 允许的形式：`2.1`、`3.76`、`A.1`、`B.12`、`C.9`。
2. 原文无编号的展示公式用 `\[ ... \]` 或 `equation*`，**不要**自动编号，不要自创编号。
3. 行内公式 `$...$`；不要用 `\(...\)`。
4. 上下标、希腊字母、指标位置严格按图像；花体（`\mathcal{H}`、`\mathcal{N}`）、德文尖角体（`\mathfrak`）、
   黑板粗体（`\mathbb{Z}`、`\mathbb{C}`、`\mathbb{P}^1`、`\mathbb{R}`）必须与原文一致。
   **不要改动符号名**：如 $Q_\pm,\bar Q_\pm$、$\mathcal{H}^n$、$H^\bullet$、$H^{\bullet,\bullet}$、$\mu_n$、$\ell_n$、$\hbar$。
5. 常用固定写法：`\operatorname{Tr}`、`\operatorname{Hom}`、`\mathrm{d}`（原文直立 d 时）、
   `\mathcal{O}(n)`、`\mathcal{N}=(2,2)`、`\bar\partial`、`\wedge`、`\otimes`。
6. 矩阵用 `pmatrix`；不要用 Unicode 数学符号（不允许 `α`、`∑`、`∫`、`→`、`≃` 出现在源码里）。
7. 原文疑似笔误（指标重复、符号不一致、指数写错）：**照抄原样**，紧跟一行
   `% [原文疑误: 说明理由 + 建议]`。不确定就写 `% [存疑: ...]`，禁止断言。
8. 引用原文公式一律写字面编号，如「式 (2.1)」，不用 `\ref`；引用文献写 `[37]`，不用 `\cite`。

## 6. 文风与术语

- 学术书面中文，简洁、无口语、无「让我们」「大家」「可以看到」这类填充。
  第一人称 "we" 译为「我们」或改用无主句；"let us" 译为「下面」或省略；不写「我」。
- 首次出现的术语在该处给英文原词：`规范场论（gauge theory）`；其后只用中文。
- 模型名、人名、群名、文献编号、公式编号、图号保持原样：`Calabi–Yau`、`Landau–Ginzburg`、
  `$A_\infty$`、`$L_\infty$`、`$U(1)$`、`[3]`、`(2.17)`、`Figure 1`。
- 数学环境内一律英文/符号，中文只能出现在 `\text{...}` 或 `\mbox{...}` 里。
- 保留原文的省略、跳跃、模糊之处：**直译原意 + 批注**；严禁自行补全物理内容、严禁删段、严禁合并段落、
  严禁「总结式改写」。
- 脚注用 `\footnote{...}`，编号由 LaTeX 自动生成（会与原文编号整体偏移，属正常，不要手工编号，
  也不必逐条说明）。
- 原文的方括号插入语、破折号、引号照译：中文引号用「」或“”；英文人名不译。

## 7. 批注（必须做，宁少勿滥，每条都要有技术含量）

1. `% [Tutor Note: ...]` —— 放在相关公式或段落的**上一行或紧接下一行**独立成行。内容限于三类：
   - **推导补足**：作者用 "It is obvious that / one easily sees / clearly / a short computation" 跳过的地方，
     写出被跳过的关键一步或所用定理（如 Duistermaat–Heckman 定理、Morse 理论、Hochschild–Kostant–Rosenberg
     定理、指标定理、超对称 Ward 恒等式、Stokes 定理的边界项来源）。
   - **易错预警**：指标升降、张量缩并、符号约定（如 Koszul 符号、$\epsilon$ 约定、$(-1)^{F}$、度规号差）
     易错处必须提示核对原文哪一条约定。
   - **物理图像**：说明该式在扭变/TQFT/镜像对称/全息中的含义（一句话，具体）。
   每个分片**至少 4 条、至多 12 条**；纯文献罗列处可减少。
2. `% [原文疑误: ...]` —— 确认为原文笔误时用，必须给出判断依据；不确定就写 `% [存疑: ...]`。
3. `% [背景补充: ...]` —— 仅在原文术语对中文读者有实质门槛时加一句准确解释（如「Koszul 对偶」「导出范畴」
   「轨道空间」）；**不超过 2 条/分片**。
4. 所有批注用中文，`%` 后空一格，不要用 `\marginpar`、不要用 `\todo`。

## 8. 图表（Lead 已剥离，你只需插入）

原文共 14 幅图（`figures/fig01.png` … `fig14.png`，300 dpi 矢量渲染）与 2 张表。插入规范：

- 图必须放在**原文对应段落之后**，用 figure 环境，位置参数 `[t]` 或 `[htbp]`：

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.92\linewidth]{figures/fig10.png}
  \caption{三穿孔球面及生成其包裹 Fukaya 范畴的三个拉格朗日子流形（红、蓝 $\sim$ 黑、绿）。
  阴影圆盘贡献一个 $A_\infty$ 三重积，它与非零三重积 $\mu_3(\psi_1,\psi_2,\psi_3)$ 互为镜像。
  （原文第 47 页，Figure 10）}
\end{figure}
```

- 图号由 LaTeX 自动生成，顺序与原文一致；**不要**写 `\caption{图 10: ...}` 之外的手工编号。
- 分片与图的对应：`s02b` fig01；`s02f` fig02–fig05；`s02h` fig06；`s03a` fig07；`s03b` fig08；
  `s03c` fig09；`s03e` fig10–fig12；`s03f` fig13–fig14。其余分片无图。
- 表 1（第 19 页）与表 2（第 21 页）在 `s02e` 中，用 `table` + `tabular` + `booktabs` 忠实重建，
  `\caption{...（原文第 19 页，Table 1）}`；表内符号用数学模式，Footnote 级说明保持原意。
- **公式内嵌示意图**（原文用树图/阶梯图画的公式，已裁成图片，直接放进 `equation*` 或 `equation`）：

| 文件 | 页码 | 内容 | 用法 |
|---|---|---|---|
| `figures/inline/eq-p42-a.png` | 42 | $\mu_1,\mu_2,\mu_3$ 对应的有根树 | 单独一行 `\begin{equation*}\includegraphics[width=0.95\linewidth]{...}\end{equation*}` |
| `figures/inline/eq-p42-b.png` | 42 | $A_\infty$ 前两条关系的树图形式 | 同上 |
| `figures/inline/eq-p43-a.png` | 43 | 第三条 $A_\infty$ 关系的树图形式 | 同上 |
| `figures/inline/eq-p44-a.png` | 44 | 第 $n$ 条 $A_\infty$ 关系的树图形式 | 同上 |
| `figures/inline/eq-p69-a.png` | 69 | $\mathbb{Z}$-分次复形的阶梯图（B.18） | `\begin{equation}\tag{B.18}\includegraphics[width=\linewidth]{...}\end{equation}` |

  使用这些图片时，在同一行加注释：`% [说明: 该式为原文矢量树图/阶梯图，按原图无损嵌入]`。

## 9. 自检（提交前必须执行）

```powershell
$py="<本地路径>"
& $py asi2204-zh\tools\lint_frag.py asi2204-zh\sections\<你的文件> --expect-tags "2.1-2.7"
```

（`--expect-tags` 用分工表里的编号范围；无编号公式的分片省略该参数。）
检查项：无导言区/`\begin{document}`、环境配对、花括号平衡、`\tag` 与预期完全一致且不重复、
无 Unicode 数学符号、数学里无中文、无遗留英文正文段落、`%` 批注格式合法、页首锚点齐全。
**必须 0 error**。

## 10. 回报格式（最后一条消息，给 Lead）

```
文件：sections/xxx.tex
覆盖：PDF 第 a–b 页；章节 …
公式：共 N 个带号公式，编号 (x.y)–(x.z)，无缺号 / 缺号情况
图：已插入 figNN（N=…）/ 无
批注：Tutor Note N 条、原文疑误 N 条、存疑 N 条、背景补充 N 条
问题：无 / 具体问题（跨页句子、无法辨认符号、疑似原文笔误、需要 Lead 处理的图）
```

## 11. 禁止事项

- 禁止机翻腔、禁止删减、禁止把公式写成图片（内嵌示意图除外）、禁止改符号、禁止自作主张「修正」原文。
- 禁止在数学里写中文；禁止改版式；禁止自定义 `\newcommand`（除非 Lead 批准）。
- 禁止声称已验证未验证的内容。拿不准就标注。
