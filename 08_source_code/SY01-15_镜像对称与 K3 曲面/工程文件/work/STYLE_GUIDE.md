# STYLE_GUIDE —— 植田一石《ミラー対称性と K3 曲面》中译 LaTeX 工程规范

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

（Lead 独占维护；译者只读，**不得修改**本文件、`src/preamble.tex`、`src/main.tex`）

## 0. 底本（实测，2026-11-06）

- 原文：植田一石（Kazushi Ueda，大阪大学理学研究科）《ミラー対称性と K3 曲面》，
  京都大学数理解析研究所**講究録 第 1918 卷**（「ミラー対称性の展望」，2014 年）**第 127–151 页**（原文 25 页）。
- 底本文件：`src/JP11_植田一石_ミラー対称性とK3曲面_25p.pdf`（另存于 `待完成的翻译工程\01_日本学派\`）。
- **页映射：原书页 = PDF 页 + 126**（PDF 第 1 页 = 原书 p.127，第 25 页 = p.151）。行文与批注一律写「原书 p.N」。
- 结构：**8 节 + 4 个小节 + 参考文献**（p.148–151）。节起始页见 `work/BRIEF.md`。
- **编号公式 99 条**，形如 `(1.1)`、`(4.16)`、`(8.10)`；**每节从 1 起连续编号**：
  §1: 1.1–1.2（2 条）；§2: 2.1–2.2（2）；§3: 3.1–3.3（3）；§4: 4.1–4.29（29）；
  §5: 5.1–5.13（13）；§6: 6.1–6.9（9）；§7: 7.1–7.9（9）；§8: 8.1–8.32（32）。
- **插图 9 幅**：図7.1（p.138）、図8.1・8.2（p.142）、図8.3（p.145）、図8.4・8.5・8.6・8.7・8.8（p.147）。
  已按原页面裁切为 `src/figures/fig7_1.png` … `fig8_8.png`（450 dpi，仅图不含原日文图注）。**无表格。**
- 定理类：定義2.1、予想3.1、定義4.1、定理6.1、定理8.1、定理8.2（preamble 已按共用计数器定义）。

## 1. 可用素材

| 路径 | 内容 |
|---|---|
| `work/pages/pNNN.png` | 逐页 150 dpi 渲染图。**公式的唯一真值。** |
| `work/split/pNNN.txt` | 逐页文字层（MuPDF 提取）。正文单词可读；数学是被隐形排入的 TeX 源文字，**上下标、\mho 等特殊符号常损坏，一律不可信**。 |
| `work/full.txt` | 整本文字层（检索用）。 |
| `work/tags_bypage.txt` | 每页编号公式清单（按右边界位置筛出，与原文一致）。 |
| `work/glossary.tsv` | 术语冻结表（日文→中文）。**必须遵守**。 |
| `src/figures/` | 9 幅插图 PNG（只读，不要改）。 |
| `src/preamble.tex` | 导言区。**只读。** |

**文字层可靠度**：✅ 正文单词、段落边界、节标题、定理名、文献编号；
❌ 一切数学（`\mho`（℧）被提成「び」「U」、`\check`、花体、上下标、矩阵全部错位）——必须逐页看 `pages/pNNN.png` 逐符号抄。
公式密集处（如 (4.22)、(5.12)、(8.10)、(8.11)、(8.19)、(8.22)、(8.30)）可用脚本放大裁图核对：`python work\tools\crop.py <页> x0 y0 x1 y1 <输出>`。

## 2. 片段规则（硬性）

- **只输出片段**：禁止 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、`\tableofcontents`、`\begin{thebibliography}`。
- 输出到 BRIEF 指定的 `src/chunks/cNN.tex`（UTF-8 无 BOM、LF 换行）。
- `\section{…}` = 原文「**N 标题**」；`\subsection{…}` = 「**8.1 标题**」。**节标题只由该节起始页所属块写一次**；续页不写。
- 段落之间空一行；不要写 `\par`；不要用 markdown 粗体（`**…**`）。
- 原文的**哥特体强调**（如「**Hodge 理論的ミラー対称性**」「**ホモロジー的ミラー対称性**」「**Strominger-Yau-Zaslow 予想**」「**Aspinwall-Morrison の意味でのミラー対**」）→ `\textbf{…}`。
- 脚注：`\footnote{…}` 就地写（原文本文基本无脚注；若出现必须译出）。
- 定理类环境：用 preamble 定义的 `definition / theorem / conjecture`，**不要手写**「\textbf{定義 2.1.}」。带括号题名写可选参数：`\begin{definition}[Dolgachev {[DoI96]}]`、`\begin{theorem}[Iritani {[Iri11, Theorem 6.9]}]`、`\begin{theorem}[{[HNU, Theorem 1.1]}]`——**题名里的文献编号用纯文本**。
- 参考文献引用一律**纯文本**：`[HNU]`、`[Iri11, Theorem 6.9]`、`[BHPVdV04, Corollary VIII.3.9]`；不要 `\cite`。
- 页码标记：每页开头写一行 `% ===== 原书 p.128 =====`（原书页 = PDF 页 + 126），供复核。

## 3. 公式（最关键）

- **编号公式必须与原文一一对应**：不缺、不重、不跳、不重排、不自造：
  ```latex
  \begin{equation}
      \sum_{i=1}^{k} w_i n_i = 0 \tag{4.2}
  \end{equation}
  ```
  多行用 `align`/`gather`，每个编号一行一个 `\tag{}`；一条编号跨多行时只在最后一行 `\tag`。
- 原文大量公式**没有编号**：用 `\[ … \]` 或 `equation*`，**绝不自己加编号**。
- 正文引用写纯文本：「式 (4.16)」；不要 `\ref`/`\eqref`。
- **`\mho`（℧，U+2127）**：第 2 节起反复出现，是复化 Kähler 类向量
  $\mho=\exp(B+\sqrt{-1}\omega)\in H^*(Y;\mathbb{C})$ 的记号。直接写 `\mho`（amssymb 已提供），
  **不要**写成 $U$、$\Omega$、$\upsilon$ 之类。
- `\check{}`：镜像侧记号 $\check Y,\check X,\check M,\check N,\check\Omega,\check{\mathcal D}$ 等；逐处看图像确认是否带 check。
- 花体 $\mathscr{F}$：Hodge 滤过 $\mathscr{F}_B,\mathscr{F}_A$ 用 `\mathscr`（preamble 已载 mathrsfs）。
- 矩阵：**行内**小矩阵用 `\left(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\right)`；**独立式**矩阵用 `\begin{pmatrix}…\end{pmatrix}`。原式如 $E_8\perp E_8\perp\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr)$。
- 集合式内的自然语言条件（如「任意の $m\in\Delta$ に対し」）照原文用中文写在花括号内，与符号混排：
  $\Delta=\{\delta\in\Pic(Y)\mid(\delta,\delta)=-2\}$ 这类纯符号式不加中文。
- 长分式/根号/上下标/指标位置逐符号核对图像；`-\frac{1}{2}(v,v)e+f+v` 一类注意括号层级。
- 公式里不要出现中文；中文说明写在公式外。
- 原文行末标点（`.`）在公式内保留按原图；句末标点按中文习惯放在公式之后。

## 4. 插图

- 图已裁好，**只写浮动体，不要重新画图**：
  ```latex
  \begin{figure}[htbp]
    \centering
    \includegraphics[width=0.42\textwidth]{fig8_3.png}
    \caption{参数空间的双有理变换（原书 p.145）}
  \end{figure}
  ```
- 图号由 `figure` 计数器按节自动生成（图 7.1、图 8.1…），**不要手写「图 8.x」编号**。
- 图注中文文本见 BRIEF「图注」表；图注末尾统一加「（原书 p.N）」。
- 图放在首次引用它的段落之后（`[htbp]`）；图号顺序必须与原文一致（8.1→8.8）。
- 宽高建议：横长图（8.3）`width=0.72\textwidth`；竖长图（8.4、8.5）`height=6.5cm`；
  其余 `width=0.34–0.45\textwidth`；以不超出、不挤压正文为准，编译后目视检查。

## 5. 术语与文风

- **以 `work/glossary.tsv` 为准**；表里没有的：数学术语用中国大陆通行译名；专有名词（人名、理论名、流形名）保留原文/英文（K3、Kähler、Hermite、Lagrange、Calabi–Yau、Fano、Gorenstein、Deligne–Mumford、Hodge、Hilbert、Hesse、Noether–Lefschetz、Torelli、Baily–Borel、Batyrev、Dolgachev、Aspinwall–Morrison、Iritani、Strominger–Yau–Zaslow、Gauss–Manin、Dubrovin、Horn–Kapranov、Laﬀorgue、Gromov–Witten、Weierstrass、Picard、Chow 等）。
- 日文汉字 ≠ 简体：複素→复、実→实、体→域（field）、束→丛（fiber bundle）/层（sheaf）、圏→范畴、射→态射、層→层、多様体→流形、軌道体→轨形、偏極→极化、反射的→自反的、反正準→反典范。
- 人名：日本人名写汉字（植田、向井、佐竹、塩田、長野、橋本、入谷、小林、櫛引、鳴木）；欧美名照原文拼写。
- 中文数学文风：一句一个逻辑重心；消灭「被……所……」「进行……的讨论」「对于……而言」；「以及」不要堆叠；英文术语与数字两侧留半角空格（`K3 曲面`、`第 4 节`、`$k$-线性`）。
- 全角中文标点；公式句末标点放在公式之后（……为 $x^2$。）。
- **不补写、不改写**：原文省略的论证、含糊的表述、疑似笔误，保留原样，只写 `% [Tutor Note: …]`。

## 6. 批注体例

- 对原文的疑问（疑似笔误、符号冲突、缺失引用）一律写成独立行注释：
  ```
  % [Tutor Note: 原书 (8.10) 末尾 3125a_1^2a_2^2a_3^2a_5^2 之后的句点疑为排版符；此处按原图保留。]
  ```
- **绝不**把「我觉得」写进正文；**不**补写原文省略的论证。
- 批注只写三类：易错预警（符号、指标、约定）、含糊点拨、背景直觉（一两句）。禁止「很重要／值得注意」这类空话。
- 每条批注必须给具体信息；LaTeX 注释里**不要再出现 `%`**。
- 每完成一个 chunk，在文件末尾写一行：`% CHUNK cNN DONE pages pXXX–pYYY`

## 7. 自检（交付前逐条走）

1. `\tag{` 的条数 = BRIEF 给你的 tag 数（允许 ±0）；tag 与 `work/tags_bypage.txt` 对得上。
2. 所有 `\begin{…}` 有对应 `\end{…}`；`\left(`/`\right)` 配对；`$` 成对。
3. 没有中文全角括号误用于数学、没有 markdown 语法残留、没有反引号。
4. 每个 `\section`/`\subsection` 只在节/小节起始页出现一次。
5. 输出文件 UTF-8 无 BOM、LF；不出现 `\r`。
6. 公式已逐条回 `pages/pNNN.png` 核对（尤其分式、根号、上下标、矩阵、大运算符上下限）。
7. 本章 figure 环境里的文件名、图注与 BRIEF 表一致。

自检命令（在 `src/` 下）：`python ..\check.py`（tag 数、环境配对、编码一次过）。

## 8. 交回格式（send_message 给 lead）

```
chunk cNN 完成：pages pXXX–pYYY（原书 p.A–p.B），tag NN 条（首 (a.b)，末 (c.d)）
图：无 / 图 8.1、8.2
存疑：1) … 2) …
```
