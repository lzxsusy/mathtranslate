# tr-c 译手报告（ch05：§4a 带群作用的 Weinstein 扇形）

日期：2026-11-13　译手：tr-c　工作目录：`<本地路径>`

## 1. 交付物

| 文件 | 内容 | 规模 |
| --- | --- | --- |
| `src/chunks/ch05.tex` | 原文 §4「Fukaya Categories of Discrete Quotients」前半（4a）的中文译注 | 204 行，对应 main.tex 1055–1190 |
| `work/reports/tr-c-terms.tsv` | 本 chunk 新增/统一术语 | 32 条（不含 terms_zh.tsv 已冻结者） |
| `work/check/ch05_test.tex` | 自检脚手架（`\input{../../src/preamble.tex}` + `\input{../../src/chunks/ch05.tex}`） | 4 行 |
| `work/check/ch05_test.pdf` / `.log` | 两遍 xelatex 的产物 | 5 页 |

未改动 `src/preamble.tex`、`src/main.tex`、`work/terms_zh.tsv` 及其他 chunk；未执行 git 操作。

## 2. 边界与页码标记

- 起点：`\section{离散商的 Fukaya 范畴}`（`\label{sec:Fukaya-category-discrete-quotient}`，main.tex 1055）。
- 终点：第一个 `\end{exmp}`（main.tex 1190）。按 lead 的切分指示（m00062），**不收** `exmp:wrapped-Fukaya-cat-twice-punctured-equivariant`（main.tex 1191 起整体归 ch06），因此本 chunk 不放 keytakeaways。
- 页码标记共 5 个，均位于页起点（main.tex 行号取自 `work/page_start.json`）：

| 标记 | main.tex 行 | 落点 |
| --- | --- | --- |
| `% [原文 p.20]` | 1020（本节所在页） | 文件首、`\section` 之前 |
| `% [原文 p.21]` | 1073 | `\begin{thm}[商的包裹 Fukaya 范畴]` 前 |
| `% [原文 p.22]` | 1096 | 「假设 $(X,Z,\omega)$ 是有限型的」段前 |
| `% [原文 p.23]` | 1146 | 「为证明该断言」段前 |
| `% [原文 p.24]` | 1179 | `L_1[0]` 约定句前 |

- **关于 p.24**：lead 消息中说 p.24 归 ch06，但 `work/page_start.json` 实测 p.24 起点是 main.tex 1179，位置在 ch05 第一个例子内部（`L_0/L_1` 命名之后、第三条 $CW^{\ast}$ 公式之前），例子整体属于本 chunk，故仍标了 p.24。若全书按「p.24 归 ch06」统一，删除 `ch05.tex` 第 184 行的标记即可，正文不受影响。
- p.20 不在 `work/pagemarks/ch05.txt` 的列表中（它只列 21–24），按 ch00 的体例补标 chunk 首页所在页。

## 3. 译注与概念框

本 chunk 含 4 条 `yizhu`、2 个 `conceptbox`，无 `keytakeaways`。

- `conceptbox{轨道范畴（orbit category)}`：取自 `work/concepts_library.md` 第 85–89 行「轨道范畴与导出自等价」条目；参考 Keller, *On triangulated orbit categories*, arXiv:math/0610212；`\cite{FKQ24}`。
  - 注意：tr-e 在 ch08 也写了同一概念的框（见 `work/reports/tr-e.md` 第 3 节）。按全书顺序 §4a 才是首现，若 Lead 要求全书只留一个框，建议保留本节、删 ch08 那个（或反过来由 Lead 定），本节框已按 §4 的用法改写成「本节用它描述商掉群作用的 A 侧」。
- `conceptbox{Viterbo 限制（Viterbo restriction)}`：概念库中无对应条目，按 GPS20/GPS24S 的含义自写，参考 `\cite{GPS24S}`。
- `yizhu` 1「两种商不是一回事」：$\mathcal{W}(X)/G$（轨道范畴）与 $\mathcal{W}(X)_G$（同伦商）的差别，以及为何等价只在扭完成后成立。
- `yizhu` 2「限制的方向」：Viterbo 限制是 $\mathcal{W}(X_2)\to\mathcal{W}(X_1)$，与开子集上同调限制同向；方向记反会误判包含关系。
- `yizhu` 3「定义里的同伦极限」：$\varprojlim$ 指同伦极限而非普通极限；先取极限再用余核生成满子范畴，二者合起来避开「无限型没有有限型完成化」的问题。
- `yizhu` 4「特征 $k$ 的双重身份」：$k$ 既是 $\mathbb{Z}$-重覆盖的层数（deck 变换），又是 $\mathbb{G}_m$-作用的特征；$CW^{\ast}$ 的星号才是同调次数。

## 4. 编译自检

命令：在 `work/check` 下对 `ch05_test.tex` 连跑两遍 `xelatex -interaction=nonstopmode -halt-on-error`（`latex_look` 另做了 3 遍含 SyncTeX 的构建）。

| 项目 | 结果 |
| --- | --- |
| exit code | 0 |
| `!` 错误 | 0 |
| Overfull \hbox | 0 |
| Underfull \hbox | 0 |
| Missing character | 0 |
| 页数 | 5 |
| 警告 | 14 条，全部为 Citation undefined（FKQ24、Christ26、GPS20、CE12、GPS24S、KW25、FLTZ12）+ 1 条 `There were undefined references`；孤立 chunk 不带 `.bib`，属预期 |

- 单独编译时定理编号为 1.x（文件里只有一节）；全书里由 preamble 的共享计数器自动得到 4.x，未手写编号、未用 `\tag`。
- 目检：用 `latex_look` 逐页看过 p.1–p.5。两张 tikz 图（图 1 生成 Lagrangian；图 2 用 $1$-手柄连接两个「标准副本」）与 tikzcd 无穷箭图均正常渲染，无溢出、无图注错位；enumerate 渲染为 (i)(ii)(iii)。
- 曾疑 `yizhu` 框左下角有孤立「。」，像素采样证明是 tcolorbox 的圆角描边（frame 色 (140,70,0)，3–4 px），非文字问题。

## 5. 原文问题与存疑

1. **`compcat`**（main.tex 1096）：应为 `compact`（"zero away from a given compact subset"）。已按 compact 译作「某个给定紧子集之外为零」，未保留错拼。
2. **"$X/G$ is still a Weinstein sector on $X$"**（main.tex 1059）：商空间不是「$X$ 上」的扇形，`on X` 疑为衍文。译文略去 `on X`，未擅自替换成别的说法，请 Lead 定夺是否在原文勘误表里记一笔。
3. **"acting exact symplectically, discrete continuously and freely"**（main.tex 1056）：`discrete` 与 `continuously` 并列可疑（疑为 "discretely" 的重复）。按「$G$ 离散、作用是连续的」处理，译作「该作用精确辛、连续并且自由」。
4. **大包裹与包裹范畴同名**：`defn:wrapped-Fukaya-cat-inf-sectors`（main.tex 1104、1107）把两者都记作 $\mathcal{W}(X)$，到显示里才用 $\mathcal{W}^{big}(X)$。照原文保留（数学内容不动），建议 Lead 在全书层面统一记号。
5. **`\begin{enumerate}[\indent (i)]`**（main.tex 1085）：原稿应是用 `enumerate` 包的 `label=` 语法；本项目 preamble 用 `enumitem`，原样照抄会直接失败：`! Missing \endcsname inserted.`（`<to be read again> \indent`，`l.30 \begin{enumerate}[\indent (i)]`）。已改为 `\begin{enumerate}[label=(\roman*)]`，渲染 (i)(ii)(iii)。**建议写进 brief**：其他 chunk 若照抄该写法也会同样报错。
6. **"set $L_1[0]$ to be the Lagrangian in the $1$-handle to the right of $X_0[0]$ where $L_1[0]$ lies in"**（main.tex 1179）：句子指代自身，疑原文笔误（可能想说 $L_0[0]$）。译文按字面处理并尽量可读（「…那个 $1$-手柄里的 Lagrangian，$L_1[0]$ 就位于其中」），未擅自改数学。
7. **"in any larger Weinstein domains"**（main.tex 1107）：单复数不一致，照译。
8. **`From \cite{FLTZ12} we know ...`**（main.tex 1120）：`FLTZ12` 在 `main.bib` 中存在，自检报 undefined 只因 test 文件不带文献库。
9. **`\Bbbk`**：原稿 preamble 载 `bbold`；本项目 preamble 未载，但 `amssymb` 提供同名字形，编译通过、无 Missing character，故未提议改 preamble。

## 6. 术语

新增/统一术语 32 条见 `work/reports/tr-c-terms.tsv`（与 `terms_zh.tsv` 重复者未列）。关键决定：

- wrapped Fukaya category 沿用「包裹 Fukaya 范畴」；无限型版本作「大包裹 Fukaya 范畴」$\mathcal{W}^{big}$。
- cocore / generalized cocore / homological cocore 统一作「余核 / 广义余核 / 同调余核」。
- handle 作「手柄」，写作「$1$-手柄」「$\mathbb{Z}$ 份 $1$-手柄」。
- exhaustion 作「穷竭」；finite type / infinite type 作「有限型 / 无限型」。
- ideal boundary at infinity 作「无穷远理想边界」，与「扇形边界」（sectorial boundary）区分。
- twisted completion 作「扭完成」（与 terms_zh 的「扭 Künneth 公式」保持一致）。
- homotopy limit 作「同伦极限」，homotopy quotient 作「同伦商」。
- 公式内 `\text{if/and/otherwise}` 统一译为 `\text{若}/\text{与}/\text{否则}`，与 ch06–ch09、ch14 的既有译法一致。
