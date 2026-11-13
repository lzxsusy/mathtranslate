# tr-g 译手报告（ch11 / ch12）

## 1. 交付物

| 文件 | 内容 | 原文范围 |
| --- | --- | --- |
| `src/chunks/ch11.tex` | §6b 后半：$G$-等变凝聚导出 dg-范畴的定义（`dfn:GEquivQCohdg`）、$\widehat{G}$-作用、限制 dg-函子（`defn`）、推论 `crl:RestrictionFunctionEm` 及其证明 | main.tex 3658–4215 |
| `src/chunks/ch12.tex` | §6c 扭 Künneth 公式：$\Ku$ 的定义（对象/态射/高阶结构）、$(\Ku^n)$ 构成 $A_\infty$-函子的命题、定理 `thm:Kunneth-embedding`、推论（扭版本拟嵌入）；§6 章末 keytakeaways | main.tex 4216–4655 |
| `work/terms_zh_tr-g.tsv` | 本两章新增术语 8 条 | — |
| `work/check/ch11_test.tex`、`ch12_test.tex` | 自检脚手架（两遍 xelatex） | — |
| `work/check/mathdiff.py`、`one.py` | 公式逐符号比对脚本（见 §5） | — |

未改动 `src/preamble.tex`、`main.tex`、`work/terms_zh.tsv` 及他人 chunk；未做 git 操作。

## 2. 页码标记与 pagemark 偏差（重要）

`work/pagemarks/ch11.txt`、`ch12.txt` 由自动映射生成，**与真实 PDF 页界有系统偏差**（行号普遍落在真实页面的上一页中部或前部）。我按 `<本地路径>` 中的 `===== PDF PAGE n =====` 分页与页脚页码核对，取真实页界放置 `% [原文 p.N]`：

| marker | 位置 | 真实原文页 |
| --- | --- | --- |
| ch11 `% [原文 p.43]` | 文件第 2 行（chunk 起点，6.4 Definition 后半） | p.43 |
| ch11 `% [原文 p.44]` | `\begin{defn}[限制 dg-函子]` 前（6.6 Definition） | p.44 |
| ch11 `% [原文 p.45]` | 证明中「由命题~\ref{prop:HInvariantsOfHomSpace}，每个直和项分解为」前 | p.45 |
| ch12 `% [原文 p.45]` | `\subsection{扭 Künneth 公式}` 前 | p.45 |
| ch12 `% [原文 p.46]` | `\item 态射：` 前 | p.46 |
| ch12 `% [原文 p.47]` | 定理 `thm:Kunneth-embedding` 的 `\begin{proof}` 前 | p.47 |

ch11 起点落在 p.43 中部，与 ch10 末尾的 p.43 marker 重复属正常（两个 chunk 共用同一页）。建议 lead 若统一全书 marker，可直接沿用上表。

## 3. 译注、概念框与要点

ch11（2 yizhu + 1 conceptbox）
- yizhu「dg 加强到底加强了什么」：$H^0$ 与三角范畴等价、每个 hom 保留为链复形；并指出原文「quasi-coherent sheaves」与 $D^b(\Coh_G(X))$（凝聚层）字面不符，译文照原文。
- yizhu「限制函子的记号方向」：原文正文写 $\Res^G_H$、推论及证明写 $\Res_H^G$，上下标互换；说明两者同指 $\Coh_G(X)\to\Coh_H(X)$，正文一律照录。
- conceptbox「轨道范畴」：含 $\hom_{\mathcal{C}/K}(X,Y):=\bigoplus_{\lambda\in\widehat{K}}\hom_{\mathcal{C}}(X(\lambda),Y)$，说明推论「先商掉 $H^\perp$-作用、再遗忘到 $H$」的直观；参考 Keller *On triangulated orbit categories*（arXiv:math/0610212）。ch10 已有「dg 增强」框，故此处不再重复。

ch12（3 yizhu + 1 conceptbox + 1 keytakeaways）
- yizhu「原文此处的断句与记号小疵」：汇总 §6 的三处小疵（见 §6 第 1–3 条）。
- yizhu「『扭』扭在哪里」：普通 Künneth 给 $\Perf(X)\otimes\Perf(Y)\to\Perf(X\times Y)$；等变情形先得 $\Perf_G(X)\otimes\Perf_G(Y)\to\Perf_{G\times G}(X\times Y)$，须沿对角嵌入 $\Delta$ 拉回并商掉 $(\Delta(G))^\perp\cong\widehat{G}$，才是 $\Perf_G(X\times Y)$。
- yizhu「为什么给出的是 $A_\infty$-函子而不是 dg-函子」：收缩只保证 $T^\ast$ 链映射、$S^\ast T^\ast-\id=\mathbb{H}^\ast d+d\mathbb{H}^\ast$ 同伦意义下成立，故只能逐阶打包为 $A_\infty$-函子。
- conceptbox「扭 Künneth 公式」：Künneth 的范畴层面陈述、等变情形的「多余群方向」与对角拉回、本文用 Eilenberg–Zilber 收缩构造并验证该嵌入；参考 nLab *Künneth theorem*、Eilenberg–Zilber, *On products of complexes*, Amer. J. Math. 75 (1953)。
- keytakeaways（§6 章末，3 条）：dg 提升；限制 dg-函子诱导轨道范畴嵌入；扭 Künneth 嵌入及其对 E–Z 收缩的依赖。

## 4. 编译自检

`work/check/` 下各跑两遍 `xelatex -interaction=nonstopmode`：

| 文件 | 页数 | `!` 错误 | Overfull | Underfull | Missing character |
| --- | --- | --- | --- | --- | --- |
| ch11_test | 3 | 0 | 0 | 0 | 0 |
| ch12_test | 3 | 0 | 0 | 0 | 0 |

剩余只有「Reference/Citation undefined」——孤立 chunk 不含 .bib、他章 label 不在本文件，属预期（`\ref` 显示为 ??）。三页均已导出 PNG 逐页目视检查：定理/命题/推论编号连续，无公式越界、无缺字。

排版微调（公式符号未改）：
- 原文 `\adjustbox{width=170mm}`（ch11 两处）与 `\adjustbox{max width=\textwidth}`（ch12 一处）在本项目 preamble 下不可用（未加载 adjustbox 宏包），改用 `\[ \resizebox{\linewidth}{!}{$\displaystyle …$} \]`。170mm > 版心 160mm，原写法本身会 Overfull。
- ch11 中三处独立成段的 $\phi$ 映射公式（原文为 `$…$`）排为行间公式；内容逐符号一致。
- ch12 中 $\Ku^n$ 的长公式缩放后字号偏小（约 8pt），若 lead 希望放大，可在全书层面允许该式伸出 itemize 缩进。

## 5. 公式逐符号比对

写 `work/check/mathdiff.py`：剔除 `%` 注释行后，抽取 `$$…$$`、`\[…\]`、`align*` 块与行内 `$…$`，归一化（去 `\text{}` 内容、空白、间距命令、括号与 `$`）后与 `_src` 比对；另对每个行内公式做「是否为译文子串」检查。

- ch11：块级 15 个全部一致；行内 51 个全部在译文中出现（仅三处 $\phi$ 公式改为行间，见 §4）。
- ch12：块级 13 个中 12 个逐字一致，余 1 个差异仅在 `\text{ for each }` → `\text{对每个 }`（属公式内文字翻译）；行内 40 个中 38 个一致，余 2 个为 `$\mathfrak{U},\mathfrak{V}$` 改写为 `$\mathfrak{U}$、$\mathfrak{V}$`（中文顿号）与 `\ge`／`\geq` 的等价写法（已统一为原文的 `\geq0`）。
- `\label`、`\ref`、`\cite`、`\tag`、环境名：与 `_src` 一致，未手写编号、未用 `\tag`（已 grep 验证）。

## 6. 原文笔误 / 存疑（均未改原文，按原意译或照录）

1. ch12 开头「…which is clearly $G\times H$-invariant, Then we can define…」：逗号后直接接新句，句子不完整。译文按「这显然是 $G\times H$-不变量。于是我们可以定义…」收句（已在译注说明）。
2. ch12 中 $\Ku^n$ 定义域写作 $\Perf(X;\mathfrak{U})_{dg}\otimes\Perf(Y;\mathfrak{V})_{dg}$，漏掉下标 $G$、$H$；值域却写 $\Perf_{G\times H}(\cdots)_{dg}$。照录，译注提示。
3. ch12 推论证明中「其正交子群作用 $\widehat{G}\cong(\Delta(G))^\perp\curvearrowright\Perf_{G\times G}(Y)$」应为 $\Perf_{G\times G}(X\times Y)$。照录，译注提示。
4. ch11 原文「the dg enhancement of the derived category $D^b(\Coh_G(X))$ of quasi-coherent sheaves」：$D^b(\Coh_G(X))$ 是凝聚层导出范畴，与 quasi-coherent 字面不符。照录，译注提示。
5. ch11 记号 $\Res^G_H$ 与 $\Res_H^G$ 混用（正文一处 vs 推论/证明多处）；照录，译注说明所指相同。建议 lead 定夺是否全书统一为一种。
6. ch11 证明内用 `\hspace{-80mm}`、`\hspace{-30mm}`、`\hspace{-58mm}` 压行，译文保留；实际排版正常无 Overfull，若全书统一可改为左对齐 align。

## 7. 术语

新增 8 条见 `work/terms_zh_tr-g.tsv`（限制 dg-函子、拟嵌入、对角嵌入、正交子群、高阶结构、等变 Künneth 函子、严格作用、受限作用），建议由 lead 合入 `work/terms_zh.tsv`。其余沿用既有术语表（等变、轨道范畴、扭 Künneth 公式、Eilenberg–Zilber 收缩、Čech 复形、完美模、dg 范畴等）；dg / $A_\infty$ 一律保留英文。

另：公式内 `\text{...}` 的英文已按语境译为中文（其中／对每个／是），编译无 Missing character；若全书希望公式内保留英文，可统一替换。
