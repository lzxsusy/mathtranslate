# 《量子场论动力学》中文译注工程 — 翻译与排版规范（v1）

本文件是本工程**唯一**的翻译规范。每页译文都必须逐条遵守。

## 0. 文献信息

- 原文：Edward Witten, *Dynamics of Quantum Field Theory*，原载 AMS 丛书
  *Quantum Fields and Strings: A Course for Mathematicians*, Vol. 2（1999）第 4 部分，pp. 1119–1424。
- 本 PDF：306 页扫描件（400 dpi），带 OCR 文本层。**扫描页 p.N 对应原书印刷页码 N+1118**
  （例如扫描第 3 页 = 印刷第 1121 页），页眉为 `E. WITTEN, DYNAMICS OF QUANTUM FIELD THEORY`。
- 全书结构：p.1–2 导言；p.3–283 第 1–19 讲；p.284 空白；p.285–291 习题（Exercises）；
  p.292 空白；p.293–306 部分习题解答（Solutions to Selected Exercises）。

## 1. 输入

- 页面图像：`witten_qft/pages/pNNN.png`（150 dpi 灰度扫描，清晰可读）。**所有公式、符号、上下标、
  希腊字母、张量指标、图注必须以图像为准转写。**
- OCR 文本：`witten_qft/text/pNNN.txt`。它**只**用于快速定位段落与普通英文句子；OCR 对数学符号
  错误极多，禁止直接照抄。典型 OCR 讹误对照：

  | OCR | 实为 | OCR | 实为 |
  |---|---|---|---|
  | `fi`, `¢`, `</>` | `\lambda`, `\phi`, `\psi` | `IR`, `en`, `cpn` | `\mathbb{R}`, `\mathbb{C}`, `\mathbb{CP}^n` |
  | `£` | `\mathcal{L}` | `S-rnatrix`, `rnatrix` | `S-matrix` |
  | `VJ`, `i/J` | `\psi`, `\bar\psi` | `8`, `8µ` | `\partial`, `\partial_\mu` |
  | `A`, `A+`, `A-` | `\lambda`, `\lambda_+`, `\lambda_-` | `E`, `N` | `\Sigma`, `\mathcal{N}` |
  | `w`, `n` | `\omega`, `\pi` | `x`, `X` | 需按上下文判定 |

  公式一律重新键入，不要试图"清洗" OCR 字符串。

## 2. 输出

- 输出为**单个 .tex 片段**（由 Lead 汇总进主文件），路径由任务指定，例如 `witten_qft/sections/lec09.tex`。
- 片段中**禁止**出现 `\documentclass`、`\usepackage`、`\begin{document}`；但可直接使用
  `amsmath / amssymb / mathrsfs / graphicx / hyperref / ctex` 提供的命令。
- 文件第一行写 `% 原文 pp.N–M（印刷 pp.N+1118–M+1118）`。
- 每一页正文开始处插入页标记：`% ===== 原文 p.N =====`（N 为扫描页号），每页必须有，
  这是覆盖度检查的依据。
- 分段的第二部分文件**不要**再写 `\section`，直接承接第一部分内容。

## 3. 结构与格式

```latex
% 原文 pp.129–136（印刷 pp.1247–1254）
\section{Lecture 9：孤子}

\begin{keytakeaways}
本节重点（3–6 句，中文）：本讲在 $1+1$ 维标量场论中引入拓扑孤子……核心数学工具是……
主要结论是……
\end{keytakeaways}

% ===== 原文 p.129 =====
\subsection{孤子的拓扑分类}
正文……

\begin{equation}
  \tag{9.1}
  \label{eq:9-1}
  \mathcal{L}=\tfrac12(\partial_\mu\phi)^2-V(\phi)
\end{equation}
```

规则：

1. **逐页完整翻译**，包括正文、Remark、脚注、题注、习题。允许汉语语序调整、长句拆分、
   术语加括注；**禁止**省略、概括、合并段落或以"（略）"代替。
2. 章节标题译为中文（专名、数学符号保留），例如
   `\section{Lecture 5：$\sigma$ 模型的大 $N$ 极限与 Grassmann 流形}`。
   保留原文的 Lecture 编号。
3. 小节用 `\subsection{中文标题}`；原文的 §N.0 编号可在注释中标注 `% 原文 §5.0`。
4. **公式编号必须与原文一致**：`\begin{equation}` + `\tag{1.5}` + `\label{eq:1-5}`。
   行内公式用 `$...$`，不用 `\(...\)`。多行用 `align` 并在首行 `\tag{...}`。
   原文未编号的展示公式用 `\[...\]`（**不要**编号）。
5. 作者用 "I/we" 时照译为"我/我们"；"It is obvious/clear that" 等照译，但在批注中指出省略。
6. 原文文献代号（如 `[I-Perturbative QFT]`、`[II-CFT]`）原样保留，可在首次出现处加
   `% [Tutor Note: 指本丛书第 I/II 卷对应章节……]`。
7. 首次出现的术语用「中文（English）」格式；同一术语全文统一（见 §5 术语表）。
8. 中文用全角标点；数学模式内用半角；公式与中文之间不留空格（LaTeX/xeCJK 自动处理）。
9. 不要添加原文没有的物理内容；原文跳步处只能加**批注**，不能私自补公式。

## 4. 图表

- 原文每一张 Figure/Diagram 都必须以下列形式插入到对应段落：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.62\textwidth]{figs/fig_p185_1.png}
  \caption{$\tau\gg0$ 与 $\tau\ll0$ 两个区域之间的解析延拓。（原文 Figure 4，p.185）}
  \label{fig:p185-1}
\end{figure}
```

- 图片路径固定为 `figs/fig_pNNN_k.png`：pNNN 为扫描页号，k 为该页第 k 张图（从 1 起）。
- **自己裁剪图片**：先看页面图像确定图的范围（归一化坐标 x0,y0,x1,y1，原点左上），再运行

```
& "<本地路径>" witten_qft\tools\crop_fig.py --page 185 --box 0.10,0.40,0.90,0.72 --out witten_qft/figs/fig_p185_1.png
```

  然后用 `read_image` 查看裁出的图片，确认完整、无多余正文、无截断；不满意就调整 box 重裁（最多 2 次）。
  图注（caption）必须翻译为中文，并注明「原文 Figure k，p.N」。
- 若原文图中有重要文字标注（如 $r\gg0$、$r\ll0$、$A$、$\Sigma$），在 caption 中简要说明。

## 5. 术语表（统一译法）

| English | 中文 | English | 中文 |
|---|---|---|---|
| quantum field theory | 量子场论 | gauge theory | 规范场论 |
| gauge field / connection | 规范场 / 联络 | gauge transformation | 规范变换 |
| holonomy | 和乐（群） | anomaly | 反常 |
| path integral | 路径积分 | partition function | 配分函数 |
| correlation function | 关联函数 | vacuum expectation value | 真空期望值 |
| spontaneous symmetry breaking | 自发对称性破缺 | order parameter | 序参量 |
| effective action | 有效作用量 | effective potential | 有效势 |
| renormalization (group) | 重整化（群） | beta function | $\beta$ 函数 |
| asymptotic freedom | 渐近自由 | confinement | 禁闭 |
| instanton | 瞬子 | soliton | 孤子 |
| monopole | 磁单极子 | vortex | 涡旋 |
| supersymmetry (SUSY) | 超对称 | superfield | 超场 |
| chiral superfield | 手征超场 | superpotential | 超势 |
| moduli (space) | 模（空间） | moduli space of vacua | 真空模空间 |
| topological field theory | 拓扑场论 | Donaldson theory | Donaldson 理论 |
| Seiberg–Witten theory | Seiberg–Witten 理论 | $u$-plane | $u$ 平面 |
| sigma model | $\sigma$ 模型 | Wess–Zumino–Witten model | Wess–Zumino–Witten 模型 |
| Wilson loop | Wilson 圈 | 't Hooft loop | 't Hooft 圈 |
| BRST quantization | BRST 量子化 | ghost | 鬼场 |
| Faddeev–Popov determinant | Faddeev–Popov 行列式 | Grassmann (variable) | Grassmann（变量） |
| Bose–Fermi correspondence | Bose–Fermi 对应 | bosonization | 玻色化 |
| large $N$ limit | 大 $N$ 极限 | 't Hooft limit | 't Hooft 极限 |
| Landau–Ginzburg | Landau–Ginzburg | quantum cohomology | 量子上同调 |
| mirror symmetry | 镜像对称 | Calabi–Yau | Calabi–Yau |
| Donaldson–Thomas | Donaldson–Thomas | intersection theory | 相交理论 |
| operator product expansion (OPE) | 算符乘积展开（OPE） | conformal field theory (CFT) | 共形场论（CFT） |
| representation / irrep | 表示 / 不可约表示 | character | 特征标 |
| index theorem | 指标定理 | characteristic class | 示性类 |
| Chern–Simons | Chern–Simons | theta angle | $\theta$ 角 |
| Higgs mechanism | Higgs 机制 | Goldstone boson | Goldstone 玻色子 |
| loop correction | 圈修正 | tadpole | 蝌蚪图 |
| S-matrix | $S$ 矩阵 | LSZ | LSZ 约化公式 |

人名保留拉丁拼写（Witten, 't Hooft, Seiberg, Polyakov, Wilson, Donaldson 等），
不加"的"。数学名词按国内教材惯例（如上表）。

## 6. 审校批注（Tutor Note）——本工程的核心增值

- 格式：独立注释行 `% [Tutor Note: ...]`，可跨行，但每条以 `% [Tutor Note:` 开头。
- 密度：**每 4–6 页至少 1 条，每个任务文件至少 3 条**。
- 必须针对**具体位置**的**具体问题**，禁止空泛套话。三类内容：
  1. **易错预警**：指标缩并、符号约定、Wick 转动、Grassmann 符号、拓扑项归一化
     （如 $\frac{\theta}{8\pi^2}\int F\wedge F$）、超对称变换中的费米子符号、欧氏/闵氏约定等。
     例：`% [Tutor Note: 此处由 (3.14) 到 (3.15) 用了 $\gamma$ 矩阵的迹公式；注意作者采用欧氏约定 $\{\gamma_\mu,\gamma_\nu\}=2\delta_{\mu\nu}$，若换用闵氏约定 $(\mathrm{tr}\,\gamma^\mu\gamma^\nu)=4\eta^{\mu\nu}$ 会整体差一个负号。]`
  2. **含糊点拨**：作者写 "It is obvious that…" / "One can show…" 时，指出省略的证明思路
     与可查文献（如 Coleman 定理、Atiyah–Singer 指标定理、Weinberg 的场论教材、
     Witten 原文、Nakahara《Geometry, Topology and Physics》等）。
     例：`% [Tutor Note: 作者称"显然真空唯一"，实为 $d=1+1$ 维 Coleman 定理（连续对称性不能自发破缺，参见 Sidney Coleman, Comm. Math. Phys. 31 (1973) 259）的推论；证明依赖红外行为，与 $d\ge3$ 的情形本质不同。]`
  3. **原文勘误/存疑**：发现笔误、符号不一致、编号跳跃时如实指出，并说明依据。
- 批注语言为中文，术语规范；引用文献给出作者+期刊/书名即可，**不得编造页码或结论**；
  不确定时写"详见原始文献"。

## 7. 质量自检（写完后逐条核对）

1. 页标记覆盖任务给定页范围，无缺页、无重复。
2. 每个编号公式有 `\tag{...}`，编号与原文一致；无编号公式未误编号。
3. 环境、花括号、`$` 全部配对（可运行 `python witten_qft/tools/qc.py <你的文件>` 自检）。
4. 所有 `\includegraphics` 指向的文件真实存在。
5. 无整段未翻译英文；无 OCR 乱码（¢、£、fi、IR2、VJ、8µ 等）。
6. 术语与本规范第 5 节一致；同一概念前后译名统一。

## 8. 返回结果（JSON）

任务提示会给出 schema；除写文件外，返回：

- `file`：输出文件路径
- `pages`：覆盖的页号数组
- `figures`：`[{page, file, box:[x0,y0,x1,y1], caption_cn}]`（无图为空数组）
- `tutor_notes`：批注条数
- `issues`：遇到的疑难（OCR 无法辨认、原文疑似错误、被裁图遮挡等），无则空字符串

以返回的 JSON 为交付凭据，不要粘贴 .tex 全文。
