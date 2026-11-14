# 翻译与排版规范（SPEC）——本文件是唯一契约，冲突时以本文件为准

项目：Ran Luo, Qing-Rui Wang, Yi-Nan Wang,
*Lecture Notes on Generalized Symmetries and Applications*（arXiv:2307.09215v3，83 页）
→ 简体中文学术版 LaTeX 源码 + 图表 + 审校批注。

> 说明：本文件是翻译阶段各个分片（任务单）共同遵守的规范。最终交付的分片文件命名为
> `sections/s00-front`、`s01-intro`、`s02a-higher-form`、`s02b-trifecta`、`s03a-anomalies`、
> `s03b-classification`、`s04a-applications`、`s04b-cmt`、`s05a-higher-group`、`s05b-crossed`、
> `s05c-physical`、`s06-appa`、`s07-appb`，装配关系与编译方法见 `README.md`。

---

## 0. 你的产出是什么

你只负责**一个** `.tex` 片段文件（路径见任务单），内容是原文若干节/小节的完整正文。
**不要**写导言区、不要 `\begin{document}`、不要 `\input`、不要 `\usepackage`、不要 `\newcommand`，
不要改动他人文件，不要改动 `main.tex`。Lead 负责装配与编译。

文件必须以如下注释开头：

```latex
% ============================================================
% 片段：s02a  对应原文 section2.tex 第 1--354 行；PDF 第 6--15 页
% 内容：§2 Higher-Form Symmetry（2.1--2.2）
% 译者：<你的名字>   审校状态：初稿
% ============================================================
```

---

## 1. 输入材料（全部在 workspace 下；务必用 read 工具读文本，用 read_image 看页面）

| 材料 | 路径 | 用途 |
|---|---|---|
| 原文 LaTeX 源码 | `work2/src/section2.tex` 等（按任务单的行号区间） | **公式的唯一权威**：公式一律从此处**逐字复制**，不要从 PDF 重打 |
| 整页图像 | `work2/pages/page-XX.png`（XX = PDF 页码，160 dpi） | 版式、图表位置、**确认原文实际排版内容**的唯一权威 |
| 每页文字层 | `work2/text/page-XX.txt` | 正文措辞参考、定位页码（公式在此不可信） |
| 已裁好的编号图 | `deliverable-2307.09215/figures/figure-N.png` | 直接 `\includegraphics`（仅 7 张编号图，见 §4） |

**两条铁律**：
1. **数学公式逐字复制源码**（含 `\be ... \ee`、`\[ ... \]`、`\begin{align}`、`\begin{aligned}`、
   `\begin{tikzpicture}`、`\begin{tikzcd}`、`\label`、`\cite` 键、上下标、括号）。
   不重打、不“顺手化简”、不补全、不调换顺序。源码中的 `\be`/`\ee` 已在导言区定义，
   分别等于 `\begin{equation}`/`\end{equation}`，请原样保留。
2. **只翻译源码中真正出现在 PDF 里的内容**。源码中被 `%` 注释掉、或因修订而删除的段落，
   PDF 里没有的，**不要译、不要输出**。若你怀疑某段是否为注释，对照整页图像确认。

源码与 PDF 的公式编号一一对应（`\numberwithin{equation}{section}`），因此**禁止增删公式环境**：
少一条或多一条 `\be...\ee` 都会让该节之后所有公式编号错位。

---

## 2. 翻译准则（学术中文本土化）

- 以中文学界约定术语为准（见 §3 术语表）。**首次出现**在所属节内给出英文原词，形如：
  `高形式对称性（higher-form symmetry）`，其后只用中文。
- 语体：书面学术中文，简洁、准确。不用“让我们”“大家”“可以看到”式口水话；
  不用“笔者”“本文将”之类元话语（原文没有的不加）。
- **逐段对应翻译**：原文每一段都要译，不许合并、不许跳译、不许概括成要点。
  句序可以按中文习惯调整，但不得改变逻辑关系（因果、条件、转折）。
- 数学环境内部一律保持英文/符号原样；中文只能出现在 `\text{...}` 中
  （例如源码 `{\rm Ground\ states}` → `\text{基态}`；`\text{ or }` → `\text{ 或 }`）。
- 文献编号、图号、公式编号、人名、模型名（Ising、Maxwell、Chern–Simons、Wess–Zumino）、
  群名（$\mathbb{Z}_2$、$SU(N)$）、代数量（$N$-ality）保持原样或按术语表处理。
- 定理/定义环境的可选标题要译：`\begin{example}[Electromagnetism in $M^d$]`
  → `\begin{example}[$M^d$ 中的电磁学]`。
- 原文的 `\textbf{Remark}:` → `\textbf{注}：`；`\textbf{Proof}` 与 `proof` 环境由导言区处理，
  不要手写“证明”二字。
- 标点：正文用全角标点（，。；：？！、），数学内用半角；引号用中文双引号“”。
  中文与行内公式之间不加空格（XeTeX 自动处理）。
- **不许**改写逻辑：原文的省略、跳跃、疑似笔误必须原样保留（公式照抄）并在译注中指出。

---

## 3. 术语表（强制；未列出的按中文学界通用译法）

| English | 中文 | English | 中文 |
|---|---|---|---|
| generalized symmetry | 广义对称性 | generalized global symmetry | 广义整体对称性 |
| higher-form symmetry | 高形式对称性 | higher-group symmetry | 高群对称性 |
| $p$-form symmetry | $p$-形式对称性 | 0-form / 1-form | 0-形式 / 1-形式 |
| topological operator | 拓扑算符 | topological defect | 拓扑缺陷 |
| topological defect network (TDN) | 拓扑缺陷网络（TDN） | symmetry operator | 对称性算符 |
| symmetry generator | 对称性生成元 | invertible symmetry | 可逆对称性 |
| non-invertible symmetry | 非可逆对称性 | gauging | 规范化（动词“作规范化”） |
| gauge field | 规范场 | background gauge field | 背景规范场 |
| gauge transformation | 规范变换 | flat connection | 平坦联络 |
| holonomy | 和乐 | Wilson loop / Wilson line | 威尔逊圈 / 威尔逊线 |
| 't Hooft line | 't Hooft 线 | 't Hooft loop | 't Hooft 圈 |
| 't Hooft anomaly | 't Hooft 反常 | anomaly | 反常 |
| anomaly inflow | 反常流入 | anomaly polynomial | 反常多项式 |
| anomaly matching | 反常匹配 | ABJ anomaly | ABJ 反常 |
| SPT (symmetry-protected topological) phase | 对称保护拓扑相 | symmetry fractionalization | 对称性分数化 |
| symmetry extension | 对称性扩张 | symmetry breaking | 对称性破缺 |
| group cohomology | 群上同调 | Čech cohomology | Čech 上同调 |
| cochain / cocycle / coboundary | 上链 / 上闭链 / 上边缘 | chain complex | 链复形 |
| bordism | 配边 | cobordism | 配边 |
| bordism group | 配边群 | classifying space | 分类空间 |
| universal bundle | 万有丛 | principal bundle | 主丛 |
| differential cohomology | 微分上同调 | Postnikov class | Postnikov 类 |
| Postnikov tower | Postnikov 塔 | crossed module | 交叉模 |
| crossed extension | 交叉扩张 | 2-group | 2-群 |
| weak $n$-group | 弱 $n$-群 | group extension | 群扩张 |
| central extension | 中心扩张 | exact sequence | 正合列 |
| fusion / fusion rule | 融合 / 融合规则 | fusion category | 融合范畴 |
| fusion tree | 融合树 | modular tensor category | 模张量范畴 |
| anyon | 任意子 | toric code | 环面码 |
| topological order | 拓扑序 | Hamiltonian | 哈密顿量 |
| ground state | 基态 | lattice gauge theory | 格点规范理论 |
| string operator | 弦算符 | monopole | 磁单极子 |
| Wu–Yang monopole | 吴–杨磁单极子 | instanton | 瞬子 |
| $\theta$ angle | $\theta$ 角 | Maxwell theory | 麦克斯韦理论 |
| Chern–Simons theory | 陈–西蒙斯理论 | BF theory | BF 理论 |
| Yang–Mills theory | 杨–米尔斯理论 | supergravity (SUGRA) | 超引力（SUGRA） |
| M-theory | M 理论 | SCFT | 超共形场论 |
| geometric engineering | 几何工程 | decoupling limit | 退耦极限 |
| non-compact | 非紧 | singularity | 奇异点 |
| cone | 锥 | torsion | 挠 |
| homology / cohomology | 同调 / 上同调 | Atiyah–Hirzebruch spectral sequence | Atiyah–Hirzebruch 谱序列 |
| Stiefel–Whitney class | Stiefel–Whitney 类 | Pontryagin class | Pontryagin 类 |
| spin structure | 自旋结构 | Pin structure | Pin 结构 |
| fermionic system | 费米子系统 | bosonic system | 玻色子系统 |
| effective field theory (EFT) | 有效场论 | partition function | 配分函数 |
| correlation function | 关联函数 | ground state degeneracy | 基态简并度 |
| entanglement | 纠缠 | operator product expansion | 算符乘积展开 |
| conformal field theory (CFT) | 共形场论 | primary field | 初级场 |
| current | 流 | charge | 荷 |
| representation | 表示 | irrep | 不可约表示 |
| Young diagram | 杨图 | $N$-ality | $N$-性 |
| Dynkin diagram | Dynkin 图 | Lie algebra | 李代数 |
| gauge group | 规范群 | quotient | 商 |
| homomorphism | 同态 | isomorphism | 同构 |
| category theory | 范畴论 | object / morphism | 对象 / 态射 |
| functor | 函子 | natural transformation | 自然变换 |
| 2-category | 2-范畴 | composition | 复合 |
| simplicial | 单纯（形） | triangulation | 三角剖分 |
| good cover | 良覆盖 | atlas | 图册 |
| sheaf / presheaf | 层 / 预层 | restriction map | 限制映射 |
| Hilbert space | 希尔伯特空间 | path integral | 路径积分 |
| lattice model | 格点模型 | unitarity | 幺正性 |
| self-duality | 自对偶 | polarization | 极化 |
| flux | 通量 | linking number | 环绕数 |
| intersection number | 交点数 | domain wall | 畴壁 |
| symmetry TFT (SymTFT) | 对称性拓扑场论（SymTFT） | topological quantum field theory (TQFT) | 拓扑量子场论 |
| higher gauging | 高阶规范化 | half gauging | 半空间规范化 |
| defect | 缺陷 | interface | 界面 |
| orbifold | 轨形 | Kramers–Wannier duality | Kramers–Wannier 对偶 |
| bosonization | 玻色化 | anomaly-free | 无反常 |
| gauge anomaly | 规范反常 | global anomaly | 整体反常 |
| ultraviolet (UV) / infrared (IR) | 紫外 / 红外 | renormalization group (RG) | 重整化群（RG） |
| conformal anomaly | 共形反常 | central charge | 中心荷 |
| index theorem | 指标定理 | Berry phase | Berry 相位 |

---

## 4. 图表（严格执行）

原文**只有 7 张编号图**（Figure 1–7）与 **1 张编号表**（Table 1）；另有若干**不编号**的示意图
（它们没有 `\caption`，在原文中也不显示编号）。

### 4.1 编号图（用 `figure` 环境 + 已裁好的 png）

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.62\linewidth]{figures/figure-2.png}
  \caption{……中译图注……（原文 Figure~2，PDF 第 7 页）}
  \label{Fig:1FormQM}
\end{figure}
```

- 文件名、宽度、页码见任务单；`\label` 沿用源码原键，**不要改**。
- 原文图注为**空**的（Figure 1、Figure 2、Figure 7）：写 `\caption{}`，并在上一行加注释
  `% [原文图注为空]`。不得自拟图注。
- 图注末尾必须带 `（原文 Figure~N，PDF 第 M 页）`。
- 图插入位置：放在原文出现该图的段落之后（就近原则）。

### 4.2 不编号的示意图 / 公式中的图（TikZ）

原文正文中约 35 处 `tikzpicture` / `tikzcd`（有的在 `\be...\ee` 里，有的在 `\begin{center}` 里）
是**公式的一部分**，必须**逐字复制源码的 TikZ 代码**，不要转成图片、不要重画。

### 4.3 表格

- **Table 1**（`tab:bordpts`，PDF 第 37 页）：用原生 `tabular` 环境重排（源码已有），caption 中译，
  `\label{tab:bordpts}` 保留。不要用图片。
- **第二张表**（`tab:Z2U1`，源码无 `\caption`，PDF 中不编号）：用原生 `tabular` 放在
  `\begin{center}` 中，**不加 `\caption`**（否则会破坏表编号）。表内英文（Wilson line 等）按术语表中译。
- 若源码表格的列格式在你机器上排版溢出，可微调列间距（`\setlength{\tabcolsep}`），
  但不得改动表格内容与结构。

---

## 5. 结构、本节重点与译注

### 5.1 节标题

- 用 `\section` / `\subsection` / `\subsubsection`，**层级与原文完全一致**，标题中译。
- 编号由 LaTeX 自动生成（原文 1–5、A–B；2.1、2.2.1 等自动复现）。
- 若你的片段从某小节中间开始（例如从 2.3 起），**不写** `\section`，只写 `\subsection`；
  若片段从某节正文开始，则按任务单写的层级写标题。
- 每个 `\label{sec:...}` 原样保留（节标题后的 label 不要丢）。
- 每页起始处插入页码锚点：`% ==== 原文 PDF 第 N 页 ====`（N 为 PDF 页码）。

### 5.2 本节重点（每个 `\section` 开头必须有，由该节起始文件的译者写）

```latex
\begin{keytakeaways}
  \begin{itemize}[leftmargin=1.4em,itemsep=2pt,topsep=2pt]
    \item \textbf{物理图像}：……
    \item \textbf{数学工具}：……
    \item \textbf{关键结论}：……
  \end{itemize}
\end{keytakeaways}
```

3–5 条，必须是**该节真实内容**的提炼（物理图像、数学工具、结论），不得空话，
不得引入原文没有的主张。附录 A、B 同样要有。

### 5.3 译注（Tutor Note，成品中可见；橙色方框、全文连续编号）

```latex
\begin{yizhu}作者此处省略了证明：其核心是利用 Stokes 定理与……；建议核对原文第 N 页脚注 m。\end{yizhu}
\begin{yizhu}[原文疑误]原文 (x.y) 两端差一个整体符号；此处照原文保留，详见 PDF 第 N 页。\end{yizhu}
```

- 方框内文字**会被排版**：行内数学必须写成 `$...$`，不得出现裸 `T_Ising`、`√2`、`→`、`ψ`。
- 三类才允许写（**每条都必须有实质信息**）：
  1. **易错预警**：指标缩并、符号约定、因子 $2\pi$、定向、规范选取、$S$/$T$ 作用次序等，
     点名“核对原文哪个约定/哪个公式”；
  2. **含糊点拨**：作者用 “it is easy to see / obvious / one can show” 跳过证明之处，
     指出被省略论证的实质与可查定理/文献（如 Stokes 定理、正合列、AHSS、五边形方程）；
  3. **原文疑误**：公式与文字矛盾、上下标/符号不一致、引用编号错位等——**照原文保留**并注明。
- **数量**：起始文件（含 `\section`）3–6 条；非起始文件 2–4 条。
- 不要写“此处很重要，请注意”这类空话；不要用译注替代正文翻译。
- 不要使用 `% [Tutor Note: ...]` 旧式注释承载批注正文（注释在成稿中不可见）；
  `% [原文疑误]`、`% [原文图注为空]` 这类**流程性标记**保留为注释即可。

---

## 6. 硬性禁止

- 禁止 `\usepackage`、`\documentclass`、`\begin{document}`、`\newcommand`、`\def`、`\input`、`\tableofcontents`。
- 禁止 Unicode 数学符号（`π`、`→`、`√`、`≈`、`×` 等）；一律 LaTeX 命令。
- 禁止自创宏、禁止改动导言区定义的计数方式。
- 禁止增删公式、合并小节、改变论证顺序、跳过段落或脚注。
- 禁止把正文改写成要点列表、禁止“本节内容见上/下”式偷懒。
- 禁止插入与物理无关的插图或装饰。
- 禁止出现 `[待确认]` 占位符：确实无法辨认时写 `\colorbox{yellow}{??}` 并在同行注释说明，交付前必须清零。

---

## 7. 交付前自检（逐条确认后再报告完成）

1. `\begin`/`\end` 全部配对，花括号平衡。
2. 本片段内公式环境数目与顺序 == 源码对应行号区间内的数目与顺序（逐条数一遍）；
   带 `\label` 的公式 label 全部保留。
3. 每个 `\section` 都带 `keytakeaways`；译注条数达标且无空话。
4. 编号图/表已按任务单插入（对照 §4），caption 与页码标注齐全。
5. 无残留英文整句（作者名、术语首现、文献、单位、模型名除外）。
6. 无 `\usepackage`/`\newcommand`/`\input`/`\documentclass`。
7. 报告（用 send_message 发给 lead）：
   (a) 完成文件路径与行数；
   (b) 本片段覆盖的 source 行号区间、插入的图/表编号；
   (c) 公式环境计数（源码 vs 你的文件）；
   (d) 译注编号清单（各条一句话摘要）；
   (e) 你认为原文存在问题或翻译拿不准的 ≤3 条要点。
