# 翻译与排版规范（SPEC）

项目：S. Gukov & E. Witten, *Gauge Theory, Ramification, And The Geometric Langlands Program*
（arXiv:hep-th/0612073v2, 160 页）→ 简体中文学术版 LaTeX 源码 + 图表 + 审校批注。

本文件记录本译本的体例约定与术语标准；改稿前请先读 `README.md` 与本文。

---

## 1. 翻译准则（学术中文本土化）

- 以中文学界约定术语为准；每个术语**首次出现**写 `中文（English）`，其后只用中文。
- 语体：书面学术中文，简洁、准确；不用口语。
- 数学环境内部保持原样；中文只出现在 `\text{...}` 或 `\mbox{...}` 中。
- 文献编号、公式编号、图号、人名、模型名（Ising、Chern–Simons、Nahm、Hitchin、Langlands）、
  群名（$SL(2,\mathbb{C})$、$G_2$）保持原样。
- **不改写逻辑**：原文的省略、跳跃、疑似笔误原样保留并加批注，不自行补全推导。
- 逐段对应翻译，不合并/拆分原文段落。

## 2. 术语表（强制统一）

| English | 中文 | English | 中文 |
|---|---|---|---|
| gauge theory | 规范场论 | gauge field | 规范场 |
| surface operator | 面算符 | line operator | 线算符 |
| Wilson operator / line | 威尔逊算符／线 | 't Hooft operator | 't Hooft 算符 |
| monodromy | 单值性 | holonomy | 和乐 |
| ramification | 分歧 | tame / wild ramification | 驯服／野分歧 |
| unipotent | 幂幺 | nilpotent | 幂零 |
| flat connection | 平坦联络 | complex structure | 复结构 |
| Higgs bundle | 希格斯丛 | ramified Higgs bundle | 带分歧的希格斯丛 |
| parabolic bundle / structure | 抛物丛／抛物结构 | Hitchin fibration | 希钦纤维化 |
| Hitchin's equations | 希钦方程 | hyper-Kähler | 超 Kähler |
| moduli space | 模空间 | holomorphic | 全纯 |
| connection | 联络 | curvature | 曲率 |
| Hodge star | 霍奇星算符 | cohomology | 上同调 |
| spectral sequence | 谱序列 | exact sequence | 正合列 |
| fibration | 纤维化 | singularity | 奇点 |
| codimension | 余维 | normal bundle | 法丛 |
| gauge transformation | 规范变换 | adjoint | 伴随 |
| simply-connected | 单连通 | semi-simple | 半单 |
| regular / non-regular | 正则／非正则 | coadjoint orbit | 余伴随轨道 |
| moment map | 矩映射 | symplectic | 辛 |
| brane / $A$-brane / $B$-brane | 膜／$A$-膜／$B$-膜 | mirror symmetry | 镜像对称 |
| sigma model | 西格玛模型 | topological twist | 拓扑扭曲 |
| super Yang–Mills | 超杨–米尔斯理论 | $S$-duality | $S$-对偶 |
| electric-magnetic duality | 电磁对偶 | theta angle | $\theta$ 角 |
| Levi subgroup | 列维子群 | Borel subgroup | 博雷尔子群 |
| parabolic subgroup | 抛物子群 | unipotent radical | 幂幺根 |
| Weyl group | 外尔群 | affine Weyl group | 仿射外尔群 |
| affine braid group | 仿射辫群 | root / coroot | 根／余根 |
| weight / coweight | 权／余权 | character / cocharacter lattice | 特征格／余特征格 |
| Langlands program | 朗兰兹纲领 | geometric Langlands | 几何朗兰兹 |
| ${\cal D}$-module | ${\cal D}$-模 | twisted ${\cal D}$-module | 扭曲 ${\cal D}$-模 |
| line bundle | 线丛 | sheaf | 层 |
| derived category | 导出范畴 | resolution | 消解 |
| Springer resolution | 施普林格消解 | Hecke algebra | 赫克代数 |
| instanton | 瞬子 | monopole | 磁单极子 |
| dyon | 双子 | characteristic class | 特征类 |
| Chern class | 陈类 | determinant line bundle | 行列式线丛 |
| Dirac operator | 狄拉克算符 | orbifold | 轨形 |
| linear sigma model | 线性西格玛模型 | Seiberg–Witten | 塞伯格–威滕 |
| Nahm's equations | 纳姆方程 | Nahm pole | 纳姆极点 |
| intersecting branes | 相交膜 | compactification | 紧化 |
| Riemann surface | 黎曼面 | genus | 亏格 |

## 3. 数学保真

1. **公式编号锁定原文编号**：每个编号公式写作
   ```latex
   % 式 (2.15)
   \setcounter{equation}{14}
   \begin{equation}\label{eq:2.15}
     ...
   \end{equation}
   ```
   编号由 `\numberwithin{equation}{section}` 自动给出，与原文 (2.1)–(2.63)、(3.1)–(3.109)、
   (4.1)–(4.20)、(5.1)–(5.18)、(6.1)–(6.24)、(A.1)–(A.18) 逐一对应。
   增删公式时必须同步修改 `\setcounter`。
2. 张量与指标：`T_{\mu\nu}`、`\epsilon^{0123}`、`(-1)^{F_L}`，上下标严格按原文位置。
3. 字符 `–`（范围连字符）、`′`（撇）、`†`、`\star`（Hodge 星号）区分清楚；不使用 Unicode 数学符号。
4. 原文**笔误**：照抄原样，紧接其后加 `\begin{yizhu}[原文疑误]...\end{yizhu}` 说明理由与建议。

## 4. 结构、批注与图表

### 4.1 页锚点
`% ==== 原文 §X.X：PDF 第 N 页（印刷第 N-1 页）====`，PDF 页码 = 印刷页码 + 1。

### 4.2 本节重点（每个 `\section` 开头必须有）

```latex
\begin{keytakeaways}
  \begin{itemize}[leftmargin=1.4em,itemsep=2pt,topsep=2pt]
    \item \textbf{物理图像}：……
    \item \textbf{数学工具}：……
    \item \textbf{关键结论}：……
  \end{itemize}
\end{keytakeaways}
```
3–5 条，必须是该节真实内容的提炼，不引入原文没有的主张。
例外：附录 B（记号索引，`sB-notation.tex`）是纯符号表，按索引体例不加「本节重点」，
其内容说明见该片段开头的译注。

### 4.3 译注（成品中可见）

```latex
\begin{yizhu}此处作者省略了证明：…… 其核心是…… 定理；建议核对原文第 N 页脚注 m。\end{yizhu}
\begin{yizhu}[原文疑误]原文 (x.y) 的右端漏写自变量；此处照原文保留，建议核对 PDF 第 N 页。\end{yizhu}
\begin{yizhu}[易错点]此处涉及 $G/\mathbb{T}$ 与 $\Lambda_{\mathrm{wt}}$ 的对偶配对……\end{yizhu}
```

三类内容：**易错点**（指标缩并、符号约定、因子 $2\pi$、定向）、**含糊点拨**（作者用
it is obvious / one finds 跳过之处，指出被省略论证的实质与可查文献）、**物理图像补充**。
每片段 3–8 条（按篇幅），全书累计 78 条，不设每节硬性上限。
方框内行内数学必须写 `$...$`。译注可整体关闭：`main.tex` 中 `\showyizhutrue` → `\showyizhufalse`。

### 4.4 图与表
- 图 1–9 编号自动生成，与原文对应；caption 中译，末尾固定加 `（原文 Fig.~N，PDF 第 M 页）`。
- 表 1（PDF 第 12 页）用 LaTeX 原生 `tabular` 重排（原文是 harvmac 的 `\halign`）。
- 引用图号用 `图~\ref{fig:3}`、表号用 `表~\ref{tab:1}`。

### 4.5 文献引用
正文用 `\cite{refN}`，编号与原文 `[N]` 一致；参考文献表保留英文著录，`\bibitem{refN}` 顺序即原文编号。

### 4.6 脚注
`\footnote{...}` 内容中译，数学原样。

## 5. 硬性禁止

- 禁止 `\usepackage`、`\documentclass`、`\newcommand`/`\def` 出现在 `sections/*.tex` 中。
- 禁止 Unicode 数学符号（`×`、`→`、`√`、`α`、`≅`、`⊗` …）；一律用 LaTeX 命令。
- 禁止全角括号/引号进入数学环境；正文标点用全角。
- 禁止改动 `\label`、`\setcounter`、`\cite` 键名、`\includegraphics` 路径。
- 禁止插入与物理无关的插图或装饰。

## 6. 原文记号宏

原文是 harvmac 源码，作者用了大量记号宏（`\EUM`→$\mathcal{M}$、`\MH`→$\mathcal{M}_H$、
`\TT`→$\mathbb{T}$、`\CA`→$\mathcal{A}$ 等）。这些宏在 `macros.tex` 中定义并保留在正文里，
以保证数学与原文逐字一致；完整对照表见同目录 `MACROS.md`。
