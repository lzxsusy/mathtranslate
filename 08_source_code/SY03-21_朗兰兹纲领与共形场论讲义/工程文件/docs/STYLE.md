# 翻译体例（STYLE）——本书全体译者必须遵守

本书：《朗兰兹纲领与共形场论讲义》中文译注本。
底本：arXiv:hep-th/0512172v1（Frenkel, 2005）之原始 LaTeX 源码。

---

## 0. 你要做什么

- 输入：`<本地路径><id>.tex`（英文原文块，已按节切好）
- 参考：`<本地路径><id>.txt`（旧中译对应段落，仅供措辞参考，数学不可信）
- 术语：`<本地路径>`（262 条，必须遵守）
- 输出：`<本地路径><id>.tex`（UTF-8，只含本块正文）

译文块**不要**写 `\documentclass`、`\begin{document}`、`\input`、`\section`。原块以 `\subsection{...}` 开头就照样以 `\subsection{...}` 开头。

**本阶段只做翻译，不写译注**（`\begin{zhunote}` 由后续工序统一插入）。若你觉得某处非注不可，用一行注释记下：`% ZHU-CAND: 需要解释 XXX，因为……`

---

## 1. 绝对禁止（违反即返工）

1. **不得改动任何数学内容**：`$...$`、`$$...$$`、`\[...\]`、`\begin{equation}...\end{equation}`、`\begin{align}`、`\begin{eqnarray}`、`\begin{CD}...\end{CD}`、`\begin{displaymath}` 内部，**一个字符都不许改**——包括空格、换行、`\,`、`\quad`、大小写、上下标。
2. **不得改动公式编号**：`\label{...}`、`\eqref{...}`、`\Ref{...}`、`\begin{equation}` 的行内编号一律原样保留，位置不动。
3. **不得删除或翻译 `\index{...}`**：`\index{Hecke eigensheaf}`、`\index{$\D$-module!twisted}` 原样保留（索引据此生成）。它的内容保持英文，位置尽量贴回原句对应的词后面。
4. **不得改动 `\cite{...}`**：键名原样，如 `\cite{L}`、`\cite{GNO}`、`\cite{bd}`。多条引用写作 `\cite{a,b}` 时保持原样。
5. **不得改换数学环境**：原文用 `\be ... \ee`、`\bea...\eea`、`\bean...\eean`（作者自定义宏，分别等于 displaymath / eqnarray* / eqnarray）就照抄，不要换成 equation/align。
6. **不得增删 `\footnote`**，脚注内容全译，脚注紧跟原位置。
7. **不得增删段落**：原文一个段落 → 译文一个段落；不要合并、不要拆分、不要自行加小标题。
8. 不得改动 `\label{...}` 的名字（正文有 `\secref{...}` 跨节引用，改了会断）。

---

## 2. 段落与标点

- 段落之间空一行；段首不缩进（排版已自动缩进 2 字）。
- 英文 ``...'' 引号 → 中文 “...”；嵌套用 ‘...’。原文 {\em ...} / \emph{...} 保留命令，只译内容。
- 破折号 `--` → `——`（两字宽，占两个汉字位）；`---` → `——`。句中的插入语用破折号；范围 `1--2` → `1–2`（en dash）。
- 省略号 `...` / `\dots`：原文在公式里的一律不动；行文中的 `...` → `……`。
- 中文与公式之间**不加空格**（xeCJK 自动处理）。中文与英文缩写之间不加空格，如「WZW 模型」写作「WZW 模型」（缩写与汉字间留一个半角空格，全书统一）。
- 句末用中文句号「。」；英文缩写后的句点保留（如 "e.g." → "例如"）。

---

## 3. 术语

- 严格按 `docs\TERMS.md`。表里没有的：首次出现写「中文（English）」，之后只用中文。
- 人名不译：Frenkel, Langlands, Witten, Drinfeld, Laumon, Beilinson, Deligne, Hitchin, Kac, Moody, Satake, Goddard, Nuyts, Olive, Kapustin, Wilson, 't Hooft, Wakimoto, Miura, Weil, Frobenius, Galois, Hecke, Shimura, Taniyama, Borel, Cartan, Killing, Virasoro, Sugawara, Feigin, Ginzburg, Gaitsgory, Arkhipov, Braverman, Finkelberg, Mirković, Vilonen, Ngô, Lafforgue, Laurent, Drinfeld–Sokolov, Kac–Moody, Riemann, Hilbert, Satake。
- 书刊名、文章名保留英文并用 `\emph{}`：`\emph{Langlands Correspondence for Loop Groups}`。
- 缩写保留：CFT, WZW, ACFT, TQFT, SYM, BPS, D-模里的 D, CD（交换图）, oper（小写不译）, ic（相交上同调复形）, holonomic（不译）。

### 最容易错的 20 组（务必核对）

| 英文 | 译文 | 备注 |
|---|---|---|
| Langlands correspondence | 朗兰兹对应 | 不是「朗兰兹纲领」 |
| Langlands Program | 朗兰兹纲领 | 大写 Program |
| geometric Langlands correspondence | 几何朗兰兹对应 | |
| Langlands dual group | 朗兰兹对偶群 | 记作 $^LG$ |
| Hecke eigensheaf | Hecke 本征层 | 不是「特征层」 |
| Hecke operator | Hecke 算符 | |
| perverse sheaf | 反常层 | 旧译如此，全书统一 |
| local system | 局部系统 | 全书统一，不用「局部系」 |
| D-module | D-模 | |
| D-brane | D-膜 | |
| chiral algebra | 手征代数 | |
| conformal block | 共形块 | 「余不变量」co-invariants |
| critical level | 临界水平 | $k=-h^\vee$ |
| affine Lie algebra | 仿射李代数 | |
| affine Grassmannian | 仿射 Grassmannian | 不译 |
| geometric Satake equivalence | 几何 Satake 等价 | |
| Hitchin fibration | Hitchin 纤维化 | |
| spectral curve | 谱曲线 | |
| oper | oper | 全小写，不译 |
| Miura transformation | Miura 变换 | |

---

## 4. 语言风格

- 学术书面语，句子可以比英文略短；避免口语化、避免「其实」「就是说」这类词。
- 忠实优先：不要为了通顺而合并或增补原意。原文的「I have tried to...」（第一人称）保留第一人称「我已尽量……」。
- 原文中的 ``we'' 译「我们」；``one'' 依语境译「人们」（避免「一个人」）。
- 数学陈述要精确：「there exists」→「存在」，「unique」→「唯一」，「up to isomorphism」→「至多相差同构」。
- 不要加原文没有的评语、不要加「值得注意的是」这类填充语（评语一律留给译注）。

---

## 5. 范例（e00 前两段的官方参考译文）

原文（节选）：

```
These lecture notes give an overview of recent results in geometric
Langlands correspondence which may yield applications to quantum field
theory. It has long been suspected that the Langlands duality should
somehow be related to various dualities observed in quantum field
theory and string theory. Indeed, both the Langlands correspondence
and the dualities in physics have emerged as some sort of non-abelian
Fourier transforms. Moreover, the so-called Langlands dual group
\index{Langlands dual group} introduced by R. Langlands in \cite{L}
that is essential in the formulation of the Langlands correspondence
also plays a prominent role in the study of S-dualities
\index{S-duality} in physics and was in fact also introduced by the
physicists P. Goddard, J. Nuyts and D. Olive in the framework of
four-dimensional gauge theory \cite{GNO}.
```

参考译文：

```
本讲义概述几何朗兰兹对应方面的一些近期结果，这些结果有望在量子场论中获得应用。
长期以来，人们一直猜测朗兰兹对偶应当以某种方式与量子场论和弦论中观察到的各种对偶相关。
事实上，朗兰兹对应与物理学中的种种对偶都表现为某种非阿贝尔 Fourier 变换。
此外，R. Langlands 在 \cite{L} 中所引入的所谓朗兰兹对偶群
\index{Langlands dual group}，在朗兰兹对应的表述中不可或缺，
它在物理学中 S-对偶 \index{S-duality} 的研究里同样扮演重要角色；
事实上，这一概念也由物理学家 P. Goddard、J. Nuyts 和 D. Olive
在四维规范场论 \cite{GNO} 的框架中引入。
```

（注意：`\index`、`\cite` 原样保留；`Fourier` 不译；「非阿贝尔」不加连字符；译文里没有加任何评语。）

---

## 6. 交稿前自检（逐条过一遍）

1. 数学是否与 `en/<id>.tex` **逐字符一致**？（建议：把译文里所有 `$...$` 与公式环境抽出来，和原文比字符数/哈希）
2. `\label`、`\eqref`、`\Ref`、`\cite`、`\index` 的数量是否与原文相同？
3. 段落数是否相同？`\footnote` 数量是否相同？
4. 是否把 `\be...\ee` 偷换成了 `\begin{equation}`？
5. 是否有残留的英文整句？（专名、术语首次出现的括号英文除外）
6. 术语是否与 `TERMS.md` 一致？（重点抽查上表 20 组）
7. 文件是否 UTF-8、能否被 xelatex 直接 `\input`？（特殊字符 `& % # _ $` 是否该转义的都转义了：正文里的 `&`→`\&`、`%`→`\%`、`#`→`\#`、`_`→`\_`；公式内不动）
8. 有没有写 `\section`、`\begin{document}` 之类不该出现的东西？
9. 中文标点是否统一（，。；：“”——）？有没有残留半角逗号/句号？
10. 最后通读一遍：像不像一本认真的学术译著？
