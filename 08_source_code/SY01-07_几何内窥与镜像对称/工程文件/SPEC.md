# 交付规范（SPEC）——本项目唯一契约，冲突时以本文件为准

项目：Edward Frenkel & Edward Witten, *Geometric Endoscopy and Mirror Symmetry*,
arXiv:0710.5939v3 [math.AG]（2008 年 4 月 5 日），130 页（正文 1–127，参考文献 127–130）。
产出：简体中文学术版 LaTeX 源码（分片）+ 公式保全 + 学术级审校批注 + 可编译 PDF。

---

## 0. 你负责什么

你只负责写 **分配给你的** `.tex` 分片文件（路径见分工表），内容是你所负责页面的完整中译正文。
**不要**写导言区、**不要** `\begin{document}`、**不要** `\input`、**不要**修改 `main.tex` / `preamble.tex`、
**不要**动别人的分片、**不要**改 `GLOSSARY.md`（发现术语问题写进回报，由 Lead 裁定）。

文件开头必须写：

```latex
% ============================================================
% 分片：s03a-genus1  对应原文 PDF 第 21--27 页（印刷页 21--27）
% 负责章节：3.1--3.5（§3 标题起）
% 译者：<你的名字>   审校状态：初稿
% ============================================================
```

## 1. 材料（全部在 workspace 下；文本用 read 工具读，图像用 read_image 看）

| 材料 | 路径（相对 `fw_endoscopy/`） | 用途 |
|---|---|---|
| 整页图像（160 dpi） | `pages/page-NNN.png`（NNN 为 PDF 页码，补零三位） | **公式与版面的唯一权威** |
| 每页文字层 | `text/page-NNN.txt` | 正文措辞参考（**公式在此不可信**） |
| 局部放大工具 | `tools/crop.py` | 公式看不清时放大细看 |
| 术语表（已冻结） | `GLOSSARY.md` | 强制统一术语，**不得跨片改动** |
| 全程约定 | 本文件 | 结构、公式、批注、文风 |

页码约定：**PDF 页码 = 印刷页码**（arXiv 首页为第 1 页，正文第 3 页起）。引用原文一律写「原书 p.N」。

文字层会把 `\frac{1}{\sqrt2}` 拆成 `1 √ 2`、丢掉上下标、把花体字变成普通字母。**绝不能照抄文字层里的公式**；公式一律看页面图像。

放大某个公式区域（PDF 点坐标，页面 612×792 pt；`--rect x0,y0,x1,y1`）：

```powershell
$py="<本地路径>"
& $py fw_endoscopy\tools\crop.py --page 22 --rect 120,300,520,430 --dpi 500 --out fw_endoscopy\tools\z1.png
```

然后 `read_image` 读 `z1.png`。若仍认不出符号：写 `\textcolor{red}{??}` 并在同一行加注释
`% [待确认: 第 N 页第 k 个公式，符号无法辨认]`，继续往下做，不要猜；并在回报中列出。

## 2. 分片分工表（页码均为 PDF 页 = 印刷页）

| 文件 | 页码 | 章节 |
|---|---|---|
| `s01-intro.tex` | 3（§1 标题起）-- 13 | §1 Introduction + 1.1--1.9（**Lead 样板**） |
| `s02-duality.tex` | 13（§2 标题起）-- 21 | §2 Duality, Branes, and Endoscopy + 2.1--2.3 |
| `s03a-genus1.tex` | 21（§3 标题起）-- 27 | §3 Explicit Example In Genus One + 3.1--3.5 |
| `s03b-genus1.tex` | 27 -- 42 | 3.6--3.11（无 § 标题） |
| `s04a-branes.tex` | 42（§4 标题起）-- 51 | §4 A-Branes And D-Modules + 4.1--4.6 |
| `s04b-branes.tex` | 51 -- 56 | 4.7--4.9（无 § 标题） |
| `s05a-spectral.tex` | 56（§5 标题起）-- 66 | §5 Spectral Covers, Hecke Operators, and Higher Genus + 5.1--5.2 |
| `s05b-hecke.tex` | 66 -- 76 | 5.3 't Hooft/Hecke Operators |
| `s06-categories.tex` | 76（§6 标题起）-- 87 | §6 Categories Of Eigensheaves + 6.1--6.6 |
| `s07-classical.tex` | 87（§7 标题起）-- 96 | §7 The Classical Story + 7.1--7.4 |
| `s08-functions.tex` | 96（§8 标题起）-- 111 | §8 From Hecke Eigensheaves To Hecke Eigenfunctions + 8.1--8.10 |
| `s09-other.tex` | 111（§9 标题起）-- 119 | §9 Other groups + 9.1--9.4 |
| `s10-gerbes.tex` | 119（§10 标题起）-- 124 | §10 Gerbes + 10.1--10.5 |
| `s11-appendix.tex` | 124（§11 标题起）-- 127 | §11 Appendix. L-packets for SL2 |
| `references.tex` | 127 -- 130 | 参考文献（**Lead 负责**，不计入分片） |

片段边界：起始页从该页第一个属于你范围的词开始；结束页到最后一个属于你范围的词（整段/整式）结束为止。
本项目的分片边界全部落在小节标题处（s03a/s03b、s04a/s04b、s05a/s05b 均在小节交界），一般不会切在句中；
若确实遇到句中切分，按语义完整取，并注释 `% [跨页接续: 原文第 N 页/N+1 页]`。

## 3. 结构

- 用 `\section{中文标题}` / `\subsection{...}` / `\subsubsection{...}`，**层级与原文严格一致**。
  原文 `§1`、`§2` 等数字编号由 LaTeX 自动生成，**不要手写编号**。
- 原文的非编号斜体小标题（如 §3 中 *Second Component* 之类的独立行）用 `\subsection*{...}`，
  与原文视觉层级一致，不加编号。
- 每个 `\section` 开头（仅出现 `\section` 的地方，s03b/s04b/s05b 等续片不要写）紧接标题之后写：

```latex
\begin{keytakeaway}
\textbf{核心物理图像：}……
\textbf{数学工具：}……
\textbf{主要结论：}……
\end{keytakeaway}
```

（`keytakeaway` 环境由 `preamble.tex` 定义，直接用；四行左右，每行一句到两句，具体、有信息量。）
- 每页起始处插入页码锚点注释：`% ==== 原文 PDF 第 N 页（印刷页 N）====`。
- 原文的 `\subsection` 编号（2.1、2.2……）自动生成即可；正文中引用「§2.3」用字面文字，不用 `\ref`（原文没有 `\label` 体系）。
- 脚注用 `\footnote{...}`，编号自动生成；原文脚注编号会整体偏移，属正常。
- 定理、命题、引理、推论、定义：原文用斜体段落或带编号的陈述。若原文明确编号（如 `Theorem 7.1`），
  用 `\begin{theorem}[...]`（preamble 已定义）并保留原文编号：`\begin{theorem}[Theorem 7.1]`；
  若原文无编号，用斜体段落或 `\begin{theorem*}`，不要自创编号。

## 4. 数学保真（最高优先级）

1. **每个带编号公式必须锁号**：`\begin{equation}\tag{2.1} ... \end{equation}`，编号完全照抄原文（含章节号）。
   多行公式用 `\begin{equation}\begin{aligned}...\end{aligned}\tag{2.3}\end{equation}`，`\tag` 放在 `equation` 层。
2. 原文无编号的展示公式用 `\[ ... \]`，**不要**自动编号，不要自创编号。
3. 行内公式 `$...$`；不要用 `\(...\)`。
4. 上下标、希腊字母、指标位置严格按图像。**不要改动符号名**（如 $\phi$、$\sigma$、$\mathcal{E}$、${}^{L}G$、
   $\mathcal{M}_H(C;G)$、$\mathrm{Bun}_G$、$\mathcal{A}_{cc}$）。
5. 常用写法：`\mathrm{Tr}`、`\operatorname{Tr}`、`\mathrm{d}`（原文直立体）与 `d`（原文斜体）按图像区分；
   `\mathbb{Z}`、`\mathbb{C}`、`\mathbb{P}^1`、`\mathcal{O}(n)`、`\mathcal{N}=4`、`\mathfrak{sl}_2`、`\hat{\mathfrak{g}}`。
6. 矩阵用 `pmatrix`；**不允许 Unicode 数学符号**（`α`、`∑`、`∫`、`→`、`≤` 等）出现在数学里。
7. 原文疑似笔误（指标重复、符号不一致、指数写错、编号跳号）：**照抄原样**，紧跟一行
   `% [原文疑误: 说明理由 + 建议]`。不确定的用 `% [存疑: ...]`。
8. 引用原文公式一律写字面编号，如「式 (2.1)」，不用 `\ref`。
9. 长公式、情形讨论（cases）、交换图：交换图一律用
   `\[ \begin{array}{ccc} ... \end{array} \]`（配 `\rightarrow`、`\searrow` 等）重建，
   与原文箭头方向、上下位置一致；**不要**用 `CD` 环境（本工程未载 amscd，宏 `\CD` 已占用为 D-模记号）。

## 5. 文风与术语

- 学术书面中文，简洁、无口语、无「让我们」「大家」「可以看到」这类填充。
  第一人称 "we" 译作「我们」（数学论文惯例）；"I" 译作「作者」或改用无主句。
- 首次出现的术语在该处给英文原词：`规范场论（gauge theory）`；其后只用中文。
  但 `GLOSSARY.md` 中标注「保留英文」的术语（gerbe、oper、brane 等）一律保留英文，不译。
- 模型名、人名、群名、文献编号、公式编号、图号保持原样：`Calabi–Yau`、`Hitchin`、`SL_2`、`[KW]`、`(2.17)`。
  人名按 GLOSSARY：`Ngô Bảo Châu（吴宝珠）`。
- 数学环境内一律英文/符号，中文只能出现在 `\text{...}` 或 `\mbox{...}` 里。
- 保留原文的省略、跳跃、模糊之处：**直译原意 + 批注**，严禁自行补全物理内容、严禁删段、严禁合并段落、严禁「总结式改写」。
- 原文的方括号插入语、破折号、引号照译：中文引号用全角「」或“”；英文里的人名不译。
- 术语服从 `GLOSSARY.md`。GLOSSARY 未收的新术语：按「中文学界通行译名 → 否则保留英文」判定，
  首次出现给括注，并在回报中列出建议，由 Lead 追加。

## 6. 批注（必须做，宁少勿滥，每条都要有技术含量）

1. `% [Tutor Note: ...]` —— 放在相关公式或段落的**上一行或紧接下一行**独立成行。内容限于三类：
   - **推导补足**：作者用 "It is obvious that / one easily sees / clearly" 跳过的地方，写出被跳过的关键一步或所用定理
     （如 Springer 对应、Kazhdan–Lusztig 参数化、Grothendieck–Springer 纤维化、Morse 理论、指标定理、Fourier–Mukai 变换）。
   - **易错预警**：指标升降、张量缩并、符号约定（如 ${}^{L}G$ 的上标位置、$\mathrm{Spin}$ 双重覆盖、$\theta$ 特征、奇异上同调的平移、
     $q$-数与 $v$ 的取值、$\mathbb{C}^\times$ 与 $\mathbb{C}$ 的区别）易错处必须提示核对原文哪一条约定。
   - **物理图像**：说明该式在 Hitchin 纤维化/镜像对称/膜范畴/D-模中的含义（一句话，具体）。
   每片**至少 4 条、至多 12 条**（页数 ≥ 15 的片可到 14 条）；纯文献罗列处可减少。
2. `% [原文疑误: ...]` —— 确认为原文笔误时用，必须给出判断依据；不确定写 `% [存疑: ...]`，禁止断言。
3. `% [背景补充: ...]` —— 仅在原文术语对中文读者有实质门槛时（如「轨形」「Springer 对应」「稳定迹公式」）加一句准确解释；
   **不超过 2 条/分片**。
4. 所有批注用中文，`%` 后空一格；不要用 `\marginpar`、不要用 `\todo`。批注内不得再出现 `%`，不得写跨行公式。

## 7. 图表

- 本文 130 页，经位图与矢量图形检测：**无带框表格、无编号 Figure**；
  唯有一处不编号插图：**原书 p.18**（奇异 Hitchin 纤维的两个图，A-模型 $G=SL_2$ 与 B-模型 ${}^{L}G=SO_3$）。
  该图由 **Lead 裁剪并插入**；负责 p.18 的分片（s02-duality）只要在该页对应位置写
  `% FIGURE-PLACEHOLDER: p18 Hitchin fibers`，不要自己插图、不要写 `figure` 环境。
- 若你在实际页面里发现别处还有真正的图形：立刻在该页注释 `% [待剥离图: 第N页，说明内容]`，并在回报中告知 Lead；
  分片里先留 `% FIGURE-PLACEHOLDER-N`。

## 8. 自检（提交前必须执行）

```powershell
$py="<本地路径>"
& $py fw_endoscopy\tools\lint_frag.py fw_endoscopy\sections\<你的文件>
```

检查项：无导言区/`\begin{document}`、环境配对、花括号平衡、`\tag` 编号格式合法且不重复、无 Unicode 数学符号、
无遗留英文正文段落、`%` 批注格式合法、`keytakeaway` 只出现在 `\section` 之后。**必须 0 error**。

## 9. 回报格式（最后一条消息）

```
文件：sections/xxx.tex
覆盖：PDF 第 a--b 页；章节 …
公式：共 N 个带号公式，编号 (x.y)--(x.z)，无缺号
批注：Tutor Note N 条、原文疑误 N 条、存疑 N 条
术语：新增建议 …（没有写「无」）
问题：无 / 具体问题（跨页句子、无法辨认符号、疑似原文笔误）
```

## 10. 禁止事项

- 禁止机翻腔、禁止删减、禁止把公式写成图片、禁止改符号、禁止自作主张「修正」原文。
- 禁止在数学里写中文；禁止改版式；禁止自定义 `\newcommand`（`preamble.tex` 已有的宏见 §12）。
- 禁止声称已验证未验证的内容。拿不准就标注。
- 禁止越界写别人的分片、`main.tex`、`preamble.tex`、`GLOSSARY.md`。

## 11. 常用宏（preamble.tex 已定义，可直接用）

`\Bun`（$\mathrm{Bun}$）、`\CD`（$\mathcal{D}$）、`\CM`（$\mathcal{M}$）、`\CH`（$\mathcal{H}$）、
`\CC`、`\ZZ`、`\RR`、`\PP`、`\Tr`、`\tr`、`\dd`（$\mathrm{d}$）、`\ii`（$\mathrm{i}$）。
其余符号一律直接写标准 LaTeX（`\mathcal{M}_H(C;G)`、`{}^{L}G`、`\mathrm{Bun}_G`）。
**不要**用 `\glos`、`\en`、`\zh` 等本文件未列出的宏。
