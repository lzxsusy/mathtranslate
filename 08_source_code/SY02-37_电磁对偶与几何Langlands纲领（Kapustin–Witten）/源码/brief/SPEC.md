# SPEC：KW06 中译体例与硬约束

> 底本：A. Kapustin & E. Witten, *Electric-Magnetic Duality And The Geometric Langlands Program*,
> arXiv:hep-th/0604151v3。译文从 arXiv harvmac 源码（`src_orig/glshort.tex`）逐段生成。
> 本规范由 lead 制定；译者不得自行改动体例，遇到规范未覆盖的情况写进 `logs/` 并保持原样。

---

## 1. 输入 / 输出

- 输入：`skel/NN-sXX.tex`（**只读**，不改）。
- 输出：`zh/NN-sXX.tex`（新建，与输入同序、同结构）。
- 日志：`logs/NN-sXX.md`。
- 每片独立编译不作要求；但**必须自检**：`\begin`/`\end` 配对、花括号平衡、无 Unicode 数学符号。

## 2. 逐段翻译

1. **段落 1:1 对应**：原文一个自然段 → 译文一个自然段；不合并、不拆分、不调整顺序。
2. `\section` / `\subsection` 的标题要译；`\label{...}` 一个字都不能改。
3. 文献引用 `\cite{refN}` 保持原样、保持原位置（中文语序里按中文习惯放到句末或主语后均可，但不得删除、不得合并）。**同一段内多个连续 cite 保持原相对顺序**。
4. `\footnote{...}` 内容要译（脚注也是正文）。
5. 原文的 italics/`\it`/强调：若脚手架里是 `{\it ...}`，译成中文时保留斜体命令包裹中文不必强求，改用手动强调 `\emph{...}` 或不强调均可，但**不得引入原文没有的强调**。
6. 破折号、括号、分号层级照原文；英文长句可拆为两句中文，但**不得改变逻辑连接词的含义**。
7. 原文的 `it is easy to see`、`one finds`、`as we have explained` 等口语化表述，按学术中文写（「不难看出」「可得」「如前所述」），不额外补证明。

## 3. 术语（强制）

1. 首选 `brief/GLOSSARY.tsv`（111 条，来自既有解经本术语章，含「易混淆点」列）。
2. 其次 `C:\Users\admin\Desktop\数译发布\gitee_shuyi\01_corpus_zh\数语规范\TERMS.tsv`（1820 条，标 `frozen` 者为定案）。
3. 两处都无：按学科惯例自定，**首次出现**写「中文（English）」，并在 `logs/` 的「新增术语」里登记，全工程只此一译。
4. 下列为全书**固定译法**（与 GLOSSARY 一致，冲突时以此为准）：

| English | 中文 | 备注 |
|---|---|---|
| electric-magnetic duality | 电磁对偶 | 连接号用「-」 |
| S-duality / T-duality | S-对偶 / T-对偶 | 保留连字符 |
| Montonen-Olive duality | Montonen-Olive 对偶 | 人名保留 |
| Langlands dual group | Langlands 对偶群 | 记 ${}^L G$ |
| geometric Langlands program | 几何 Langlands 纲领 | 不写「程序」 |
| Hecke eigensheaf | Hecke 特征层 | 不写「本征层」 |
| eigenbrane | 特征膜 | 不写「特征膜」 |
| topological twisting | 拓扑扭化 | 不写「扭曲」；动词「扭化」 |
| twisted D-module | 扭化 D-模 | |
| Hitchin moduli space / fibration | Hitchin 模空间 / Hitchin 纤维化 | Hitchin 保留拉丁 |
| Higgs bundle / Higgs field | Higgs 丛 / Higgs 场 | |
| hyper-Kähler | 超凯勒 | |
| generalized complex structure | 广义复结构 | |
| sigma model | sigma 模型 | 不写「西格玛模型」 |
| A-model / B-model | A-模型 / B-模型 | |
| A-brane / B-brane | A-膜 / B-膜 | |
| line operator / loop operator | 线算子 / 圈算子 | |
| Wilson operator | Wilson 算子 | |
| 't Hooft operator | 't Hooft 算子 | 撇号照抄 |
| order operator / disorder operator | 有序算子 / 无序算子 | |
| monopole / monopole bubbling | 单极子 / 单极子冒泡 | |
| instanton | 瞬子 | |
| Bogomolny equations | Bogomolny 方程 | |
| BPS | BPS | 不译 |
| gauge theory / gauge field | 规范场论 / 规范场 | |
| supercharge | 超荷 | |
| scalar supercharge | 标量超荷 | |
| R-symmetry | R-对称 | |
| vacuum expectation value | 真空期望值 | |
| moduli space | 模空间 | |
| coherent sheaf | 相干层 | |
| derived category | 导出范畴 | |
| flat connection / local system | 平坦联络 / 局部系统 | |
| affine Grassmannian | 仿射 Grassmann 流形 | 原文 loop Grassmannian 同 |
| Schubert cell / cycle | Schubert 胞腔 / Schubert 循环 | |
| canonical coisotropic brane | 典范余各向同性膜 | 统一用「余各向同性」，不写「余迷向」 |
| Jacobian / Prym | Jacobi 簇 / Prym 簇 | |
| spectral curve | 谱曲线 | |
| integrable system | 可积系统 | |
| Seiberg-Witten curve | Seiberg-Witten 曲线 | |
| Nahm pole / Nahm equations | Nahm 极点 / Nahm 方程 | |
| conformal field theory | 共形场论 | |
| boundary condition | 边界条件 | |
| Riemann surface / genus | 黎曼面 / 亏格 | |

5. 群名、流形名、人名、模型名保留原文：$SU(N)$、$G_2$、$E_8$、$Spin(2n)$、$\mathrm{SL}(2,\mathbb{Z})$、Kapustin、Witten、Hitchin、Beilinson、Drinfeld、Frenkel、Gaitsgory、Atiyah、Goddard–Nuyts–Olive (GNO)、Nahm、Seiberg。

## 4. 数学保真（最重要）

1. **数学环境内一字不改**：公式、符号、指标、上下标、括号、矩阵、`\eqalign`→`aligned` 后的内容全部照搬。中文只能进 `\text{...}` / `\mbox{...}`。
2. **禁止**改动：`\setcounter{equation}{...}`、`\label{...}`、`\tag*{...}`、`\cite{...}`、`\ref{...}`、`\eqref{...}`、`\section/\subsection` 的顺序与数量、`\begin{equation}` 的编号注释 `% 式 (N)`。
3. 编号公式的 `% 式 (N)` 注释行**必须保留**（它是译对时的锚）。
4. 禁止 Unicode 数学符号（`≤ ≥ → ∈ × −`），一律 `\le \ge \to \in \times -`。
5. 原文笔误（含下标错、因子 $2\pi$ 缺失、符号相反）：**照抄**，紧接其后加 `\begin{yizhu}[原文疑误]……\end{yizhu}`。
6. 公式里的 `\Bbb{Z}`、`\EUN`、`\MH`、`\TT` 等是 `macros.tex` 提供的 harvmac 记号宏，**不要改名、不要展开**。

## 5. 结构元件（译者所加，非原文）

### 5.1 本节重点 `keytakeaways`

只在**每节的第一片**（见下方分工表的「节首」标记）的 `\section` 之后加：

```latex
\begin{keytakeaways}
  \begin{itemize}[leftmargin=1.4em,itemsep=2pt,topsep=2pt]
    \item \textbf{物理图像}：……
    \item \textbf{数学工具}：……
    \item \textbf{关键结论}：……
    \item \textbf{边界与展望}：……（可选）
  \end{itemize}
\end{keytakeaways}
```

3–5 条，必须概括该节真实内容；不得引入原文没有的主张。

### 5.2 译注 `yizhu`

每片 3–8 条（按篇幅），三类内容：

```latex
\begin{yizhu}[易错点]……\end{yizhu}
\begin{yizhu}[含糊点拨]……\end{yizhu}
\begin{yizhu}[物理图像]……\end{yizhu}
\begin{yizhu}[原文疑误]……\end{yizhu}
```

要求：
- 针对**具体位置**的**具体难点**（指标缩并的约定、因子 $2\pi$、定向、$I,J,K$ 三个复结构的用法、$\Psi$ 取值、$G$ 与 ${}^L G$ 混淆、A-膜/B-膜的层次、`\text{instant}` 之类），不写「本节很重要」的空话。
- 行内数学写 `$...$`；讲背景可引 Witten 08 / Frenkel 09 的说法（写「参见 Witten 2008 综述」即可，不要伪造页码）。
- 明确区分：**原文说了什么** / **我补了什么**。补的内容以「按：」起首。

### 5.3 图与表

- 图已由脚手架生成：`\includegraphics{figures/figure-N.png}` + `\caption{...（原文 Fig.~N）}`。**caption 的英文要译**，保留「（原文 Fig.~N）」。
- 3 张表已在脚手架里排成 `tabular`（`tab:gno-dual`、`tab:sdual-models`、`tab:centers`），**caption 的英文要译**，表内英文表头（$G$、Model、Group、Center）按术语表译。
- 引用写 `图~\ref{fig:...}`、`表~\ref{tab:...}`。

### 5.4 页锚（可选）

在 `\subsection` 或大段开头可加 `% 原书 PDF p.N`，N 必须核对 `C:\Users\admin\Downloads\kw06_pages\pNNN.txt`（PDF 页 = 印刷页 + 1）后写。**没核对就不写**。

## 6. 硬禁止清单

- ❌ 在 `zh/*.tex` 里出现 `\usepackage`、`\documentclass`、`\newcommand`、`\def`、`\newenvironment`
- ❌ 改动 `\label` / `\setcounter` / `\cite` / `\ref` 键名
- ❌ 增删编号公式、调换公式顺序
- ❌ Unicode 数学符号
- ❌ 用「本征」译 eigen-（一律「特征」，eigenvalue 除外按 GLOSSARY）
- ❌ 把 `twisting` 译成「扭曲/扭转」（用「扭化」）
- ❌ 照抄既有解经本/既有译本的句子
- ❌ 略译整段、省略句子（原文有 5 句，译文必须 5 句的信息量）

## 7. `logs/NN-sXX.md` 格式

```markdown
# 分片 NN-sXX 校对日志

## 覆盖
原文行 / 段落数 / 公式数（编号段）

## 自检
- [ ] 段落 1:1
- [ ] label/cite/setcounter 未改（`diff <(grep -o '\\label{[^}]*}' skel/NN) <(grep -o ... zh/NN)`）
- [ ] 无 Unicode 数学符号
- [ ] yizhu 条数：N

## P1（必须修）
- 位置｜问题｜处置

## P2（可选优化）
- 位置｜问题｜建议

## 术语
- 新增：English → 中文（首现位置）
- 冲突：GLOSSARY 与原文用法不一致处及取舍

## 检索记录（诚实汇报）
| 工具 | 查询 | 命中/失败 | 结果如何影响译文 |
|---|---|---|---|
| web_search / web_fetch(nLab) / kb-local / GLOSSARY | ... | ... | ... |
```
