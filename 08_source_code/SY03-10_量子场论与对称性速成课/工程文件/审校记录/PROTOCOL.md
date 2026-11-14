# 翻译规范（PROTOCOL）—《A Crash Course on QFT and Symmetry》中文译注版

本文件是本项目所有译者（Lead 与各 teammate）必须遵守的统一规范。**先通读本文件，再动手。**

---

## 0. 项目与源文件

- 英文原著：Si Li（李思），*A Crash Course on QFT and Symmetry*，version 2025.7，103 页 PDF。
- 母本 PDF（唯一权威底本）：`<本地路径>`
  （桌面 `<本地路径>` 为同一文件的副本）。
- 已提取的逐页纯文本：`qftx/pages/pNNN.txt`（NNN = 001…103，UTF-8）。
- 已渲染的逐页图片：`qftx/png/pNNN.png`（140 dpi；核对公式、图表时用 `read_image` 查看）。
- 参考交叉资料：`qftx/ref_student_notes_clean.tex` —— 同一位作者 2025 年同一门课
  由学生 Xinyu Xiang 整理的英文笔记（LaTeX 源码）。**仅用于核对公式记号，
  不得作为译文内容来源；不得照抄其句子。**

## 1. 分片与输出位置

输出均为 UTF-8、LF 换行、无 BOM 的 `.tex` 片段，写入 `qftx/tex/`：

| 片段 | 页码（PDF 页） | 内容 |
|---|---|---|
| part01.tex | 1–6 | 标题页/摘要/前言 + 第 1 章 Introduction（1.1, 1.2） |
| part02.tex | 7–14 | 第 2 章 Cohomology and Integration（2.1, 2.2） |
| part03.tex | 15–22 | 第 3 章 Classical Field Theory（3.1–3.3） |
| part04.tex | 23–30 | 第 4 章 Algebraic Aspects of Symmetry（4.1–4.3） |
| part05.tex | 31–40 | 第 5 章 Perturbative Expansion（5.1–5.3） |
| part06.tex | 41–47 | 第 5 章（续）：5.4 Canonical Quantization、5.5 Counter-term and Renormalization |
| part07.tex | 48–55 | 第 6 章 BRST-BV Formalism（6.1–6.3） |
| part08.tex | 56–60 | 第 6 章（续）：6.4–6.6 |
| part09.tex | 61–70 | 第 7 章 Effective Theory of BV Quantization（7.1–7.4） |
| part10.tex | 71–76 | 第 8 章 Factorization Algebra（8.1, 8.2） |
| part11.tex | 77–86 | 第 9 章 Topological Quantum Mechanics（9.1–9.4） |
| part12.tex | 87–92 | 第 9 章（续）：9.5 Global Theory |
| part13.tex | 93–101上 | 第 10 章 Two-dim Chiral QFT（10.1–10.6，含 p101 开头的 Theorem 10.12） |
| part14.tex | 101–103 | References（参考文献，照录不译条目，仅统一标点） |

**页码对应关系**：PDF 第 N 页 = 正文页脚页码 N-1（PDF 第 1 页为标题页，无页脚号）。
例如 PDF p033 的页脚是 32。图题中标注“原文 p.32”请以**页脚页码**为准，
并同时给出 PDF 页号（写成“原文 p.32 / PDF p.33”）。

## 2. 文档结构映射

- 章：`\section{中文标题}` —— 自动编号即原文的 1, 2, …, 10（引入章前不要有其它编号 section）。
  章标题建议中英并出：`\section{经典场论（Classical Field Theory）}`
- 节：`\subsection{中文标题（English）}` —— 自动编号 1.1、1.2 …，与原文一致。
- 更细的小标题：用 `\subsubsection{…}`（原文有少量无编号小标题，用 `\paragraph{…}`）。
- 目录、页码、交叉引用由 LaTeX 自动生成，**不要**写 `\addcontentsline`、`\setcounter`。

## 3. 定理类环境（编号必须与原文一致）

原文的定理类块**编号是手动的**（如 Definition 2.1、Example 5.4、Theorem 10.12），
其中编号是“节号.序号”。请使用 preamble.tex 中定义的环境，**把原文编号作为参数**：

```latex
\begin{wdefn}{2.1}
  环 $R$ 上的上链复形是一列 $R$-模映射 ...
\end{wdefn}

\begin{wexam}{5.1}（两点函数）   % 原文的括号副标题照译，写在环境首行
  两点函数 ...
\end{wexam}

\begin{wthm}{10.12}
  ...
\end{wthm}
```

可用环境：`wdefn`（定义）、`wthm`（定理）、`wprop`（命题）、`wlem`（引理）、
`wcor`（推论）、`wclaim`（Claim/断言）、`wexam`（例）、`wrem`（注）、
`wnota`（Notation/记号）、`wconstr`（构造）、`wquest`（问题）。
带星号版本（`wdefn*` 等）用于原文无编号者。
原文的 “Proof.” 用标准 `\begin{proof} … \end{proof}`（ctex 会自动排“证明”）。
若原文是 “Proof of Theorem X” 之类，写 `\begin{proof}[定理 X 的证明]`。

## 4. 公式规范（最高优先级）

1. **原文所有展示公式均不编号**（已逐页核对：文本层无 (n.m) 形式编号）。
   因此一律用 `\[ … \]` 或 `\begin{equation*} … \end{equation*}`，**不要**用
   `\begin{equation}`、不要 `\tag`、不要 `\label{eq:...}`。
   例外：原文极少数公式带 `(*)` 或 `(∗)` 标记，用 `\tag*{$*$}` 保留（放在 equation* 内），
   并在 `% [Tutor Note: ...]` 里说明出处。
2. **逐符号无损**：上下标、希腊字母、花体（`\mathcal`/`\mathscr`/`\mathfrak`）、
   粗体（`\mathbf`/`\boldsymbol`/`\bm`）、重音（`\bar`/`\hat`/`\tilde`）、
   括号尺寸（`\left( … \right)`）、`\bigwedge`/`\wedge`、`\partial`/`\nabla`、
   `\imath`/`\jmath`、`\hbar`、`\slashed` 等，必须与原图逐一对照。
3. **文本层中公式是线性展开的**（分式被拆成多行、积分号与上下限分列）。
   因此**必须**对照 `qftx/png/pNNN.png` 还原为正确的 LaTeX 结构（分式、根式、矩阵、
   上下限、对齐）。不确定时放大图片确认（可用 Python/PIL 裁切放大后 `read_image`）。
4. 多行公式用 `aligned`/`gathered`/`cases`/`pmatrix` 等；对齐点与原图一致。
5. 原文的 `d`（微分）、`i`（虚数）、`e`（指数）在排印上多为直立体；
   统一写 `\dd`、`\ii`、`\ee`（见 preamble 宏）。若原文语义是变量 $d$/$i$/$e$，照常。
6. 算子名用 `\operatorname{}`（如 `\operatorname{Tr}`、`\operatorname{Crit}`）；
   preamble 已定义常用宏，能复用就复用。
7. **禁止**：私自补充原文没有的公式、私自“修正”原文公式（疑似笔误照录+批注）、
   用占位符（`???`、`TODO`）交付。

## 5. 图表规范

- 原文有两张**编号图**（Figure 1：p.19 页脚/PDF p20；Figure 2：p.47 页脚/PDF p48），
  以及大量**正文内嵌示意图**（交换图、Feynman 图、流形/区间示意图、Riemann 面等）。
- 图由 Lead 统一从 PDF 裁切为 `qftx/figures/fig_pNNN_k.png`（NNN=PDF 页号，k=该页自上而下第 k 张）。
- **你的任务**：在正文中图应出现的位置写一个标记注释，格式严格如下：

```latex
% [FIG: page=20, k=1, caption=自发对称性破缺, desc=势能曲线与两个极小点]
```

  随后**不要**自己插入 figure 环境（Lead 会按标记插入）。若原文该图有图题，
  `caption=` 写**中文图题**；无图题的示意图，`caption=` 写简洁中文描述。
  `desc=` 用中文描述图形内容，便于 Lead 裁切定位。
- 若同一页有多张独立图，按自上而下 k=1,2,3… 编号。
- 表：原文第 6 章有一张变量对照表（PDF p55）。表格用 `tabular` + `booktabs`
  **重排**（不要裁图），表头译中文，并保留原文栏目内容。

## 6. 译注（Tutor Note）规范

格式（LaTeX 注释，紧跟所批注段落/公式之后，单独一行）：

```latex
% [Tutor Note: ...]
```

必须覆盖以下情形（每个片段至少 5 条、至多 15 条，宁精勿滥）：

1. **易错预警**：涉及指标缩并、符号约定、$\epsilon$ 张量、Wick 转动、
   $i$ 因子、号差 $\eta_{\mu\nu}$、路径积分测度等，必须写明“此处极易出现符号错误，
   请注意核对原文的 XXX 约定”。
2. **含糊点拨**：原文出现 “It is obvious that… / One can show… / left as exercise” 时，
   指出被省略的论证实质（依赖哪条定理、哪类估计、哪篇文献），**不得编造**；
   不确定就写“此处证明从略，建议参阅 XXX”。
3. **原文疑误**：形近符号、上下标错位、系数不符、笔误、前后记号不一致等，
   照录原文并在批注中说明“疑为……，请核对原书 p.N”。
4. **术语/记号依据**：非常见译名首次出现处，注明译名依据（如 dimer 二聚体、
   descent 下降、twist 扭曲、propagator 传播子）。
5. **物理图像点拨**：对关键构造（BV 拉格朗日、有效重整化、因子化代数、
   Fedosov 量子化等）可加 1–2 句“该构造的几何/物理含义是……”。

**Tutor Note 一律用中文，不得进入排版正文**（严格以 `%` 开头）。

## 7. 每章“本节重点（Key Takeaways）”

- 每个 `\section` 开头（即 part01/02/03/04/05/07/09/10/11/13 的开头；
  part06/08/12 是章的续篇，不要重复）插入：

```latex
\begin{keypoints}
  \item 核心物理图像：……
  \item 数学工具：……
  \item 主要结论：……
  \item 译者评注：……（1–2 句，指出该节在全书中的位置与难点）
\end{keypoints}
```

- 3–5 条，每条一句到两句，**必须基于该节实际内容**，不得空泛。

## 8. 语言与术语

- 学术中文，术语用中文学界通行译法；首次出现可写“中文（English）”，后文只用中文。
- 长句拆分，逻辑连接词显化；**不得增删原意**，不得添加原文没有的物理断言。
- 公式内一律用数学符号，不夹中文；中文与行内公式间空一格（ctex 自动处理，不必手工加空格）。
- 引文标记（如 `[35]`）照录为 `[35]`（用 `\textup{[35]}` 或直接方括号）。
- 章节标题中英并出；正文专有名词保留英文原拼写（如 BRST、BV、Fedosov、Wick）。

### 术语表（必须遵守）

| English | 中文 | English | 中文 |
|---|---|---|---|
| action | 作用量 | gauge theory | 规范场论 |
| field space | 场空间 | gauge symmetry | 规范对称性 |
| observable | 可观测量 | gauge fixing | 规范固定 |
| action principle | 作用量原理 | ghost field | 鬼场 |
| equation of motion | 运动方程 | anomaly | 反常 |
| Noether's theorem | Noether 定理 | BRST operator | BRST 算子 |
| Noether current/charge | Noether 流/荷 | BV formalism | BV 形式 |
| conserved current | 守恒流 | master equation | 主方程 |
| de Rham cohomology | de Rham 上同调 | classical/quantum master equation | 经典/量子主方程 |
| cochain complex | 上链复形 | polyvector field | 多向量场 |
| chain complex | 链复形 | Schouten bracket | Schouten 括号 |
| differential form | 微分形式 | divergence operator | 散度算子 |
| exterior derivative | 外微分 | shifted symplectic structure | 平移辛结构 |
| compact support | 紧支集 | quantization | 量子化 |
| Poincaré lemma | Poincaré 引理 | deformation quantization | 形变量子化 |
| Stokes' theorem | Stokes 定理 | star product | 星积 |
| Cartan formula | Cartan 公式 | Moyal product | Moyal 积 |
| Lie derivative | Lie 导数 | Fedosov quantization | Fedosov 量子化 |
| contraction | 缩并 | index theorem | 指标定理 |
| vector field | 向量场 | heat kernel | 热核 |
| principal bundle | 主丛 | propagator | 传播子 |
| connection | 联络 | correlation function | 关联函数 |
| curvature | 曲率 | Green's function | Green 函数 |
| Chern-Simons | Chern-Simons | Feynman graph/diagram | Feynman 图 |
| Yang-Mills | Yang-Mills | loop | 圈 |
| sigma model | $\sigma$ 模型 | tadpole | 蝌蚪图 |
| partition function | 配分函数 | Wick's theorem | Wick 定理 |
| path integral | 路径积分 | Gaussian integral | 高斯积分 |
| Wiener measure | Wiener 测度 | renormalization | 重整化 |
| asymptotic expansion | 渐近展开 | counter-term | 抵消项 |
| perturbative expansion | 微扰展开 | regularization | 正则化 |
| Chevalley-Eilenberg complex | Chevalley-Eilenberg 复形 | cut-off | 截断 |
| differential graded algebra (dga) | 微分分次代数 | effective field theory | 有效场论 |
| differential graded Lie algebra (DGLA) | 微分分次 Lie 代数 | homotopy RG flow | 同伦重整化群流 |
| $L_\infty$-algebra | $L_\infty$ 代数 | factorization algebra | 因子化代数 |
| graded bracket | 分次括号 | prefactorization algebra | 预因子化代数 |
| Jacobi identity | Jacobi 恒等式 | cosheaf | 余层 |
| antisymmetrization | 反对称化 | sheaf | 层 |
| sign rule | 符号规则 | disc/annulus | 圆盘/圆环 |
| representation | 表示 | operator product expansion (OPE) | 算子乘积展开 |
| module | 模 | vertex algebra | 顶点代数 |
| dual | 对偶 | chiral | 手征 |
| tensor product | 张量积 | holomorphic | 全纯 |
| symmetric algebra | 对称代数 | current | 流 |
| exterior algebra | 外代数 | central charge | 中心荷 |
| determinant | 行列式 | modular | 模的 |
| Pfaffian | Pfaffian | chiral boson | 手征玻色子 |
| elliptic complex | 椭圆复形 | $\beta\gamma$/$bc$ system | $\beta\gamma$/$bc$ 系统 |
| index | 指标 | deformation | 形变 |
| closed/exact | 闭/恰当 | obstruction | 障碍 |
| homotopy | 同伦 | Kuranishi | Kuranishi |
| chain homotopy | 链同伦 | cotangent | 余切 |
| Poincaré dual | Poincaré 对偶 | symplectic | 辛 |
| holonomy | 和乐（群） | instanton | 瞬子 |
| soliton | 孤子 | instanton | 瞬子 |
| domain wall | 畴壁 | topological | 拓扑的 |
| spontaneous symmetry breaking | 自发对称性破缺 | vacuum expectation value | 真空期望值 |
| cluster decomposition | 集团分解 | locality | 局域性 |
| tempered distribution | 缓增分布 | smooth | 光滑 |
| compact manifold | 紧流形 | RG flow | 重整化群流 |

## 9. 交付前自检清单（逐项确认，写在给 Lead 的回复里）

- [ ] 页码覆盖：本片段的每一页（PDF 页范围）都有对应译文，无整段遗漏。
- [ ] 定理/定义/例编号与原文一致，无跳号、无重号。
- [ ] 所有展示公式均为 `\[ … \]`/`equation*`，无 `\tag`（$*$ 标记除外）。
- [ ] 括号/环境/数学定界符配平（可用 `qftx/tools/lint.py` 自查）。
- [ ] 无 BOM、无乱码、无 `???`/`TODO`/`……待补`。
- [ ] 已按规范放置 `% [FIG: ...]` 标记；已给出 keypoints。
- [ ] 已加入 5–15 条 `% [Tutor Note: ...]`。
- [ ] 仅修改自己的 `qftx/tex/partNN.tex`，未触碰他人文件与 `main.tex`/`preamble.tex`。

## 10. 工具

- 运行 Python：`<本地路径>`
  （用 `&` 调用；PyMuPDF 在 `<本地路径>`，用 `sys.path.insert` 引入）。
- 编译验证（只 Lead 做）：见 `qftx/tools/compile.ps1`。
