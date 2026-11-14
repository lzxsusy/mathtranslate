# 翻译与排版规范（SPEC）——本文件是唯一契约，冲突时以本文件为准

项目：Murad Alim, *Lectures on Mirror Symmetry and Topological String Theory*
（arXiv:1207.0496v1 [hep-th], 44 页，2012）→ 简体中文学术版 LaTeX 源码 + 审校批注。

---

## 0. 你的产出是什么

你只负责**一个** `.tex` 片段文件（路径见任务单），内容是任务单指定页码区间（PDF 页码）的完整正文。
**不要**写导言区，不要 `\begin{document}`，不要 `\input`，不要改动他人文件，不要改 `main.tex`。
Lead 负责装配、编译、交叉引用与参考文献转换。

文件必须以如下注释开头：

```latex
% ============================================================
% 片段：s03a  对应原文 PDF 第 12--18 页
% 内容：§3 引言、3.1--3.4
% 译者：<你的名字>   审校状态：初稿
% ============================================================
```

---

## 1. 输入材料（全在 workspace 下，用 read 工具读，不要用 shell cat）

| 材料 | 路径 | 用途 |
|---|---|---|
| 整页图像 | `paper1207/pages/page-XX.png`（XX = PDF 页码，150 dpi，1241×1754） | **公式、符号、排版细节的唯一权威** |
| 每页文字层 | `paper1207/text/page-XX.txt` | 仅用于辨认英文措辞与句子切分 |
| 放大工具 | `paper1207/zh/tools/crop.py` | 公式看不清时放大 |

**文字层不可信**：本 PDF 的文字层在公式处会丢失上下标、把 $\frac{1}{2}$ 拆成 `1` `2`、把括号映射成 `\x10`、
把 `fi` 连字映射成乱码（如 `xed`），部分词还会出现 `锟斤拷` 类乱码。**
**一切公式必须逐字符对照整页图像转写**；文字层只帮你确认英文单词和行文顺序。

放大示例（PowerShell，先设 `$py` 与 `$env:PYTHONIOENCODING='utf-8'`）：

```powershell
$py = '<本地路径>'
& $py paper1207\zh\tools\crop.py --page 18 --rect 100,200,520,430 --zoom 3 --out paper1207\zh\tools\z1.png
```

之后用 read_image 看 `z1.png`。页面坐标系：整页 612×792 pt，原点左上。一般公式区域 x∈[100,520]。
读不清就反复放大，**绝不猜符号**。

---

## 2. 翻译准则（学术中文本土化）

- 以中文学界约定术语为准，**首次出现**给出英文原词：`镜像对称（mirror symmetry）`，其后只用中文。
- 语体：书面学术中文，简洁、准确、无口语（不用“让我们”“大家”“我们可以看到”）。
- 数学环境内部一律保持英文/符号原样；中文只能出现在 `\text{...}`、`\mbox{...}` 或 `\mathrm{...}` 内。
- 文献编号 `[12]`、公式编号 `(3.5)`、人名（Witten, Vafa, Bershadsky, Cecotti, Ooguri, Batyrev, Candelas）、
  模型名（Ising、Maxwell、Chern–Simons、Calabi–Yau、Gromov–Witten、Picard–Fuchs）保持原样。
- **不许**改写逻辑：原文的省略、跳跃、疑似笔误必须原样保留并加批注，不得自行补全推导。
- 原文的强调（斜体）用 `\emph{}`；不要整段加粗。
- 原文的破折号 `—`、连字符范围 `–` 分别用 `——`、`--`。

### 术语表（强制）

| English | 中文 | English | 中文 |
|---|---|---|---|
| mirror symmetry | 镜像对称 | mirror pair | 镜像对 |
| topological string theory | 拓扑弦理论 | topological field theory (TFT) | 拓扑场论 |
| A-model / B-model | A 模型／B 模型 | topological twist | 拓扑扭转 |
| superconformal algebra | 超共形代数 | SCFT | 超共形场论 |
| chiral ring | 手征环 | chiral field | 手征场 |
| deformation | 形变 | deformation family | 形变族 |
| moduli space | 模空间 | moduli | 模 |
| marginal operator | 边缘算符 | exactly marginal | 精确边缘 |
| operator product expansion (OPE) | 算符乘积展开 | conformal weight | 共形权 |
| central charge | 中心荷 | spectral flow | 谱流 |
| Ramond / Neveu–Schwarz sector | Ramond／Neveu–Schwarz 扇区 | U(1) current | $U(1)$ 流 |
| Grassmann | 格拉斯曼 | BRST operator | BRST 算符 |
| nilpotent | 幂零 | Q-exact | $Q$-恰当 |
| cohomology class | 上同调类 | cohomological | 上同调型 |
| Riemann surface | 黎曼面 | genus | 亏格 |
| worldsheet | 世界面 | target space | 靶空间 |
| nonlinear sigma model | 非线性 sigma 模型 | Kähler manifold | 凯勒流形 |
| Calabi–Yau (CY) threefold | 卡拉比–丘（CY）三维流形 | complex structure | 复结构 |
| Kähler class | 凯勒类 | Kähler moduli | 凯勒模 |
| cohomology | 上同调 | Hodge structure | 霍奇结构 |
| variation of Hodge structure | 霍奇结构的变化 | Hodge filtration | 霍奇滤过 |
| Picard–Fuchs equation | Picard–Fuchs 方程 | period | 周期 |
| mirror map | 镜像映射 | quantum cohomology | 量子上同调 |
| Gromov–Witten invariant | Gromov–Witten 不变量 | instanton | 瞬子 |
| prepotential | 预势 | free energy | 自由能 |
| genus expansion | 亏格展开 | higher genus amplitude | 高亏格振幅 |
| Yukawa coupling | 汤川耦合 | topological metric | 拓扑度规 |
| special geometry | 特殊几何 | Zamolodchikov metric | Zamolodchikov 度规 |
| Gauss–Manin connection | Gauss–Manin 联络 | flat coordinate | 平坦坐标 |
| section | 截面 | line bundle | 线丛 |
| canonical bundle | 典范丛 | holomorphic | 全纯 |
| anti-holomorphic | 反全纯 | holomorphic anomaly equation | 全纯反常方程 |
| background independence | 背景无关性 | geometric quantization | 几何量子化 |
| BPS state | BPS 态 | M-theory | M 理论 |
| type IIA / IIB | IIA／IIB 型 | geometric engineering | 几何工程 |
| Seiberg–Witten theory | Seiberg–Witten 理论 | duality | 对偶 |
| non-perturbative | 非微扰 | perturbative | 微扰 |
| effective action | 有效作用量 | correlation function | 关联函数 |
| partition function | 配分函数 | path integral | 路径积分 |
| Feynman diagram | 费曼图 | anomaly | 反常 |
| conifold | 锥形流形（conifold） | quintic | 五次超曲面 |
| orbifold | 轨形（orbifold） | toric geometry | 环面几何 |
| reflexive polyhedron | 自反多面体 | polyhedron | 多面体 |
| Landau–Ginzburg | 朗道–金兹堡 | topological sigma model | 拓扑 sigma 模型 |
| tt* equations | $tt^*$ 方程 | polynomial structure | 多项式结构 |
| generator | 生成元 | boundary condition | 边界条件 |
| holomorphic ambiguity | 全纯模糊性（ambiguity） | moduli of Riemann surfaces | 黎曼面模空间 |
| Beltrami differential | Beltrami 微分 | line bundle | 线丛 |
| bundle of states | 态丛 | ground state | 基态 |

人名、机构名、期刊名不译（Harvard University、Tsinghua University、Nucl.Phys. 等）。
“Witten”“Vafa”等姓氏直接用拉丁字母。

### 术语一致性

同一术语全篇必须统一；若你发现更合适的中文译法，在片段文件末尾用注释列出建议，**不要**擅自混用两种译名。

---

## 3. 数学保真（最高优先级）

1. **每个带编号公式必须锁号**：`\begin{equation}\tag{3.21} ... \end{equation}`。
   编号完全照抄原文，**不依赖自动编号**，**不自创编号**。多行公式用 `aligned`/`gathered`/`split`，
   `\tag` 放在 `equation` 内。
2. 无编号公式用 `\[ ... \]` 或 `equation*`。
3. 张量与指标严格按图中位置：`T_{\mu\nu}`、`\epsilon^{0123}`、`G^{\pm}_{m\pm a}`、`\bar\partial_{\bar\imath}`；
   注意原文的 `\imath`/`\jmath`（无点 i、j）与普通 `i`/`j` 的区别；原文用 `Z^*` 表示镜像流形。
4. 固定写法：`\mathbb{Z}`、`\mathbb{C}`、`\mathbb{P}^4`、`\mathcal{M}`、`\mathcal{H}`、`\mathcal{F}^{(g)}`、
   `\mathrm{tr}`、`\mathrm{e}^{2\pi i}`、`\mathrm{d}`（微分）、`\partial_z`、`\bar\partial_{\bar z}`、
   `\Omega`、`\omega`、`\varpi` 区分清楚；Hodge 星号用 `\star`。
5. 原文**笔误**（上下标矛盾、符号不一致、指数写错、因子 2 漏写等）：**照抄原样**，并紧接一行加
   `% [原文疑误: ... 理由 ... 建议 ...]`，同时在正文相应位置放一条 `yizhu`（见 4.3），标题用 `[原文疑误]`。
6. 无法辨认的符号：写 `\colorbox{yellow}{??}` 并在同行注释 `% [待确认: 第 N 页第 k 个公式，符号无法辨认]`；
   交付前此类标记必须为 0。不要猜。
7. 矩阵/数组环境：原文的矩阵用 `pmatrix`、`bmatrix`、`vmatrix`；原文用表格形式排版的分段映射（如 3.2 式）
   用 `equation` + `array` 复现其版式，**仍然保留 \tag**。原文的 `\underbrace` 用 `\underbrace{...}_{...}`。
8. 不要在公式环境里用中文；不要用 Unicode 数学符号（α、∑、→、×、≥ 一律换 LaTeX 命令）。
9. 希腊字母、花体、双线体按原文：$c$ 为 central charge，$J$ 为 $U(1)$ 流，$G^\pm$ 为超流，
   $T$ 为能动张量；$F_g$、$\mathcal{F}^{(g)}$ 严格照原文（原文有时写 $F^{(g)}$，有时写 $\mathcal{F}^{(g)}$，照抄）。
10. 公式编号清单见任务单，**逐一核对，一个都不能少**。

---

## 4. 结构、批注与图表

### 4.1 节标题与页码锚点

- 用 `\section{...}`、`\subsection{...}`、`\subsubsection{...}`，**层级与原文完全一致**，标题中译。
  例：`\subsection{$N=2$ 超共形代数}`、`\subsubsection{A 扭转}`。
- 编号由 LaTeX 自动生成，与原文 2.1、3.4.1 等一致。
- 每个 `\section`/`\subsection` 后加 `\label{sec:<编号>}`（如 `\label{sec:3.5}`），便于 Lead 用 `\ref{}`。
- 每页起始处插入页码锚点注释：`% ==== 原文 PDF 第 N 页 ====`。

### 4.2 本节重点（每个 `\section` 开头必须有）

紧接 `\section{...}` 标题之后、正文之前插入：

```latex
\begin{keytakeaways}
  \begin{itemize}[leftmargin=1.4em,itemsep=2pt,topsep=2pt]
    \item \textbf{物理图像}：……
    \item \textbf{数学工具}：……
    \item \textbf{关键结论}：……
  \end{itemize}
\end{keytakeaways}
```

3–5 条，必须是该节**真实内容**的提炼（不是标题复述），不得引入原文没有的主张。
若你的片段从某一 `\section` 中间开始（如只含 3.5 节的后半），仍在该 `\section` 首次出现处放；
若片段内出现新的 `\section`（如 s03a 含 §3 开头），则每个 `\section` 都要有。
`\subsection` 不要求。

### 4.3 审校批注（Tutor Note，成品中**可见**）

批注必须进入排版结果，同时保留 `% [Tutor Note: ...]` 源码注释。格式固定为：

```latex
% [Tutor Note: 易错点] $C_{ijk}$ 的指标升降与 (3.18) 的联络约定
\begin{yizhu}[易错点]
此处推导极易出现符号错误：……（2--4 句，给出可核对的具体约定/文献/页码）。
\end{yizhu}
```

- `% [Tutor Note: 类型] 一句话摘要` 写在 `\begin{yizhu}` 的**前一行**；类型取：易错点／含糊点／物理图像／原文疑误。
- `yizhu` 环境由导言区定义（橙色方框、全文连续编号），**你直接使用，不要定义**。
- 方框内文字会被排版：行内数学必须写 `$...$`；禁止裸写 `T_Ising`、`e^{-2πi/8}`、`√2`、`×`、`→`、`ψ`。
- 每个 `\section` 3–6 条，必须**有实质信息**，只允许三类：
  1. **易错点预警**：复杂指标缩并、符号约定、定向、$2\pi$ 因子、反常系数、$\chi/24$ 修正、
     微分形式与张量指标的对应、$\bar\partial$ 与 $\partial$ 的作用次序等，须点名“核对原文哪个约定/公式”。
  2. **含糊点拨**：作者写 “it is obvious / one finds / it can be shown / straightforward” 而跳过论证处，
     指出被省略的实质（例如用了哪种定理、哪种标准化、哪篇文献），**不虚构定理内容**。
  3. **物理图像**：把形式推导背后的物理讲清楚（仍不得虚构结论）。
- 禁止空话（“此处很重要，请注意”之类）。原文明显笔误优先写成 `[原文疑误]` 批注。
- 脚注翻译用 `\footnote{...}`，内容中译；脚注编号自动生成，不必对齐原文。

### 4.4 图与表

全文**只有一张插图**：原文第 31 页式 (4.24) 与 (4.25) 之间的亏格 $g$ 黎曼面示意（原文未编号）。
由 s04a 片段负责插入：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.95\linewidth]{figures/figure-1.png}
  \caption{全纯反常方程 (4.24) 的费曼图式图解：左边为亏格 $g$ 的黎曼面，右边为两类退化情形
    （$g_1+g_2=g$ 与 $g-1$），插入算符以 $\times$ 标记，$D_i$ 表示对相应模参数的协变导数。
    （原文第 31 页，式 (4.24) 之后；原文未编号，此处编号为译者所加）}
  \label{fig:1}
\end{figure}
```

其文字以原文为准，可微调，但必须准确、附原文位置。正文中若提到此图，用 `图~\ref{fig:1}`。
**其他片段没有图**；若你在自己页码范围内发现任何示意图（非公式矩阵），不要自行截图，
在交付报告里写明页码与内容，由 Lead 处理。

### 4.5 文献引用

**不要**写 `\cite`。照抄原文的 ASCII 方括号数字样式：`[26]`、`[1--3]`（范围用 `--`；原文写法是
`[1, 2, 3]` 的可以保留逗号形式，但范围必须用 `--`）、脚注内的 `[9, 34]` 照抄。
Lead 会用脚本统一转成 `\cite{ref...}`。

### 4.6 列表与强调

`itemize`/`enumerate` 带 `[leftmargin=1.4em,itemsep=1pt,topsep=2pt]`。
原文的 `•` 列表用 `itemize` 复现。

---

## 5. 硬性禁止

- 禁止 `\newcommand`/`\def`/`\usepackage`/`\documentclass`/`\begin{document}`/`\tableofcontents`。
- 禁止 Unicode 数学符号；正文标点用全角，数学内用半角。
- 禁止自行增删内容、合并小节、改变论证顺序、跳过公式、跳过脚注。
- 禁止把 `keytakeaways` 写成空壳。
- 禁止插入与物理无关的插图或装饰。
- 禁止改动 `main.tex`、他人片段、`figures/`（除 s04a 插图引用）。

---

## 6. 交付前自检（逐条确认后再报告完成）

1. `\begin`/`\end` 全部配对，花括号平衡。
2. 任务单列出的每个公式编号都有 `\tag{}`，编号与原文逐一对应，无重复、无遗漏。
3. 片段内每个 `\section` 都带 `keytakeaways`；Tutor Note ≥ 3 条/节且无空话。
4. 所有脚注、所有小节标题、所有编号公式均已译出。
5. 无残留英文整句（作者名、术语首现、文献、期刊名除外）。
6. 片段内不含 `\usepackage`/`\newcommand`/`\documentclass`。
7. 报告（用 send_message 发给 lead）：(a) 文件路径与行数；(b) 覆盖的页码/公式编号；
   (c) `% [待确认]` 与 `% [原文疑误]` 清单；(d) 你认为原文存在问题或翻译拿不准的 ≤3 条要点。
