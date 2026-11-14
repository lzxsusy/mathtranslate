# STYLE_GUIDE —— 译本硬规范（2112.14764《4d N=2 超共形场论漫游指南》中文译注本）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 本文件是**硬约束**。违反任何一条，交稿即被打回。
> 项目根：`<本地路径>`
> 工作区：`work\`（只读素材）、`work\src\chunks\`（你写文件的地方）
> 底本：arXiv:2112.14764v3，122 页（Letter 612×792 pt），**PDF 页号 = 印刷页码 + 1**

---

## 1. 页码体系

- 你的任务书写的是 **PDF 页号**（1–122），与 `work\pages\pNNN.png`、`work\split\pNNN.txt` 的编号一致。
- 每页原文起始处插一行注释：`% [原文 p.N]`（N = 印刷页码 = PDF 页号 − 1）。
- 每个片段文件开头写：`% ===== 原文 PDF pp.A–B（印刷 pp.a–b）=====`
- 印刷页码出现在 PDF 页脚：`split\pNNN.txt` 末行通常是印刷页码（如 `26`）。

## 2. 片段规则

- 每个译者交付 **3 个文件**：`trNNa.tex`、`trNNb.tex`、`trNNc.tex`（建议每 4–5 页一个）。
- 文件内容就是**纯正文 LaTeX 片段**：不要 `\documentclass`、不要 `\usepackage`、不要 `\begin{document}`、不要 `\end{document}`、不要 `\newcommand`。
- 只能用 `preamble.tex` 里已定义的宏（见 §5）。**需要新宏 → 在回执里向 Lead 申请，不要自己定义。**
- 编码 **UTF-8 无 BOM**，换行 **LF**。写完自己检查一遍（见 §10）。
- **只写自己块内的文件**；绝不改 `preamble.tex`、`main.tex`、别人的 `chunks/*.tex`。

## 3. 公式编号（唯一真值）

- 原文**每一个编号公式**都必须原样复刻编号，用 `\tag{}`：

```latex
\begin{equation}
  \Delta \ge f(j,\bar j,R,r) + \delta_A
  \tag{2.10}
\end{equation}
```

- 你的块有一个 **tag 区间**（见任务书）。区间内**不缺、不重、不跳、不重排、不自造**；区间外的编号一个都不许写（除非行文中引用，见下）。
- 多行公式（`align`/`gather`/`split`）：每行一个编号就每行一个 `\tag`；一条编号跨多行时 `\tag` 放在最后一行。
- 行文引用公式：写纯文本「式 (2.28)」「(2.28)」，**不要** `\ref`/`\eqref`/`\label`。
- 无编号公式：用 `\[ ... \]` 或 `equation*`，**绝不**自造编号。
- 公式太宽越界：`\begin{equation}\resizebox{0.985\textwidth}{!}{$\displaystyle ...$}\tag{X.Y}\end{equation}`。
- **公式的数学符号一律不可信文字层**：必须逐页看 `work\pages\pNNN.png` 逐符号抄写。
  看不清就用 `crop.py` 放大：
  `& $py "$ROOT\work\tools\crop.py" <PDF页号> <x0> <y0> <x1> <y1> <out.png> [dpi]`（页面 612×792 pt，默认 500 dpi）

## 4. 可用宏（preamble 已定义；直接用）

| 宏 | 含义 | 宏 | 含义 |
|---|---|---|---|
| `\R \C \Z \N \Q` | ℝ ℂ ℤ ℕ ℚ | `\cN` | $\mathcal{N}$（N=2 的超对称数）|
| `\cM \cB \cC \cD \cF \cG \cH \cL \cO \cP \cQ \cS \cT \cU \cV \cW \cX \cY \cZ \cA \cJ \cK \cE \cI \cR` | 花体 | `\fg \fh \ft \fu` | 哥特体 g h t u |
| `\fsu \fso \fsp \fgl` | 哥特 su so sp gl | `\SU \SO \SL \Sp \PSU \PSL \GL` | 正体群名 |
| `\Tr \tr \diag \sgn \rk \rank \Pf \Res \vol` | 算子名 | `\half` | $\tfrac12$ |
| `\dd \ee \ii` | 正体 d e i | `\para{...}` | 行内粗体小标题（独立成段）|
| `\figtitle{N}{...}` | 图题（手工编号）| `\tabtitle{N}{...}` | 表题（手工编号）|
| `\ie \eg \cf` | i.e. e.g. cf. | `\bQ \bq \bepsilon \btheta` | 带上横线 |

**不允许**自造 `\newcommand`；不允许 `\text{中文}` 以外的奇怪命令；中文字体不用管（ctex 自动）。
数学里需要中文说明时用 `\text{...}`（amsmath 已加载）。

## 5. 批注格式

- 一律 `% [Tutor Note: ...]` 单行注释，**不进入排版**。
- 每 2–3 页 ≥1 条，每节 ≥3 条；质量优先于数量。
- 只写**可验证**的内容：易错点（为什么这里要 $\bar$、指标归属、为何 unitarity bound 里有 $\delta_A$）、
  补出原文省略的推导步骤、原文笔误的正确形式、与前后文的呼应。
- 允许在批注里出现 `$...$`，但**绝不允许不成对的 `$`**（自检脚本会误报）。
- **指控原文笔误前，必须先用 500+ dpi 裁图复核**（文字层会把 `n_\ell-1` 抽成 `n_{\ell-1}` 之类）；
  未复核就写进批注 = 打回。

## 6. 结构元素写法

**定义**（原文酒红色左边框）：`Definition 2.3: Coulomb Branch M_CB` →

```latex
\begin{definitionbox}{定义 2.3：库仑分支 $\cM_{\mathrm{CB}}$}
  ……正文……
\end{definitionbox}
```

**例**（原文蓝色左边框）：`Example 4.1:` →

```latex
\begin{examplebox}{例 4.1：}
  ……正文……
\end{examplebox}
```

（例标题原文只有编号时，就只写「例 4.1：」。）

**习题**（原文细黑全框）：`Exercise 2.1 Show that ...` →

```latex
\begin{exercisebox}{习题 2.1}
  Show that ……（译为中文）
\end{exercisebox}
```

**图**：

```latex
\begin{center}
  \includegraphics[width=0.78\linewidth]{figN.png}
\end{center}
\figtitle{N}{译文图注}
```

- 图号 N 用原文编号；`width` 可按图调整（0.5–0.95）；**不要用 `\caption`/`\label`/自动编号**。
- 图内的英文标注是原图固有的，**不要重画、不要擦除**；图注中译，必要时在批注里说明图内标注含义。
- 图必须放在原文图附近（原文该页之后、下一个图之前均可）。

**表**：用 `booktabs`：

```latex
\begin{center}
\begin{tabular}{lccc}
\toprule
... & ... & ... & ... \\
\midrule
... \\
\bottomrule
\end{tabular}
\end{center}
\tabtitle{N}{译文表题}
```

- 复杂表可用 `array`/`multirow`/`m{}` 列；宽表用 `\small` 或 `\resizebox{\textwidth}{!}{...}`。
- 表题原文含出处的（如 "adapted from [5]"）照译并保留引用号。
- **表的行列归属必须逐格核对**（原文的列是「文献」「CFT」等限定列时尤其小心）。

**行内小标题**：原文 `\textbf{Tame punctures.}` → `\para{驯服穿刺点。}`

**脚注**：`\footnote{...}` 就地；脚注编号由 LaTeX 自动排，但**条数与位置必须与原文一致**（原文每页脚注逐条核对）。

**章节标题**：编号**手工给定**（不用自动编号，避免全书的编号被某一块的疏漏带偏）。
只写你任务书里**明确分配给你的**标题，格式固定：

```latex
\SEC{2}{4d $\cN=2$ 超对称基础}          % 一级：\SEC{编号}{中文标题}
\SUB{2.1}{$\cN=2$ 超共形对称性与表示}    % 二级：\SUB{编号}{中文标题}
\SUBSUB{4.8.1}{一般的 $\cN=(2,0)$ 理论}  % 三级：\SUBSUB{编号}{中文标题}
```

- 编号照原文**原样**（如 `\SUB{2.1}`、`\SUBSUB{4.8.2}`），标题中文自拟但要与原文含义一致。
- **不要写别人的标题**；原文标题在页中被切断（续行）时按完整标题写一次即可。

## 7. 禁止事项（违反即打回）

1. `\documentclass` / `\usepackage` / `\begin{document}` / `\newcommand` / `\def` / `\renewcommand`；
2. Markdown 语法（`**粗体**`、`# 标题`、`- 列表` 全部不许出现在 .tex 正文里，`itemize` 要写 LaTeX）；
3. `\ref` / `\eqref` / `\cite` / `\label` / `\tag` 之外的自动编号机制；
4. 自造公式编号、漏写 `\tag`、把 (2.10) 写成 (2.9)；
5. 整段英文原文留在正文（必须全译；专有名词、缩写、人名、期刊名保留英文）；
6. 批注里不成对的 `$`；
7. 修改别人文件 / 修改 `preamble.tex` / `main.tex`；
8. 用正则批量改写 `.tex`；
9. 编译（Lead 统一编译；你只需保证语法正确）。

## 8. 边界规定

- **跨页句「开始者写完」**：句子在本页开始、下一页继续，由**开始的那一页所属的译者写完**。
  所以：你的块末尾若是半句，**把它写完整，并标 `% [边界] 本句已写完，下一位 tr-MM 从下一页首句续`**；
  你的块开头若是半句，**直接续写，不要重译上文、不要补写前一句**。
- 相邻块的 `\section` 标题归属见 BRIEF.md「标题归属」列，**严格按表**，不要越界。
- 发现边界与 BRIEF 不符（例如某节标题其实在上一页），**按实际页面写，并在回执里报告**，Lead 会同步邻居。

## 9. 文字层可靠度（必须牢记）

| 内容 | 可信度 |
|---|---|
| 正文单词、段落边界、脚注、章节标题、表题图题 | ✅ 可信，用来定位与理解 |
| **数学符号** | ❌ 一律不可信：`\frac{m}{2}` 可能抽成 `2m`；上下标错位；`ω` 抽成 `f`、`α` 抽成 `a`、`\mathcal{N}` 抽成 `N`；`n_\ell-1` 抽成 `n_{\ell-1}`；`ε` 抽成 `ϵ` |

→ **每个公式必须逐页看图像逐符号抄写**。这也是「原文笔误」指控必须先裁图复核的原因。

**另一个文字层坑（人名/术语常见）**：变音符号会被抽成独立的组合字符，例如
`K¨ahler`（应为 Kähler）、`Garc´ıa`（应为 García）、`N´u˜nez`（应为 Núñez）、`¨uber`。
译文里**必须写成正常字符**（Kähler / García / Núñez），不要照抄 `¨`/`´`/`ˆ`。

## 10. 自检清单（交稿前逐项过）

- [ ] 我块内 tag 区间完整：从 `X.Y` 到 `X'.Z` 每条都在，无重复、无自造、无跳号
- [ ] 每个 `equation` 都有 `\tag{}`；无编号公式没有 `\tag`
- [ ] 花括号平衡；`\begin`/`\end` 配对；`$` 成对
- [ ] 没有禁用命令（§7）；没有 Markdown 语法；没有整段英文
- [ ] 定义/例/习题用的环境名正确（`definitionbox`/`examplebox`/`exercisebox`），编号照抄
- [ ] 我的图/表都写了（`\includegraphics{figN.png}` + `\figtitle{N}{}` / `\tabtitle{N}{}`），编号照抄
- [ ] 每 2–3 页 ≥1 条 `% [Tutor Note: ...]`
- [ ] 文件是 UTF-8 无 BOM、LF；文件非空（>1 KB）
- [ ] 边界：开头半句已续写、结尾半句已写完；没有重复邻居的内容

## 11. 回执格式（写完 send_message 给 lead，固定 5 项）

```
【tr-NN 交稿】
① 文件与页段：trNNa/b/c.tex，原文 PDF pp.A–B（印刷 pp.a–b）
② tag 区间：X.Y–X'.Z 共 N 条（核对过：不缺/不重/不跳）；存疑：<无 / 列出>
③ 原文可疑或笔误：<页 + 式号 + 判据；无则写「无」>
④ 新增术语：<英文 → 中文，逐条；无则写「无」>
⑤ 自检：tag 完整 pass / 括号 pass / 环境配对 pass / $ 成对 pass / 无禁用命令 pass / UTF-8-LF pass / 批注 N 条
```

## 12. 术语表（冻结，必须一致；完整表见 `work\glossary.tsv`）

| 英文 | 中文 | 英文 | 中文 |
|---|---|---|---|
| superconformal field theory (SCFT) | 超共形场论 | Coulomb branch | 库仑分支 |
| Higgs branch | 希格斯分支 | mixed branch | 混合分支 |
| moduli space | 模空间 | vacuum moduli space | 真空模空间 |
| multiplet | 多重态 | supermultiplet | 超多重态 |
| vector multiplet | 矢量多重态 | hypermultiplet | 超多重态（超场）/超多重态 |
| chiral | 手征的 | anti-chiral | 反手征的 |
| primary operator | 主算子 | descendant | 后裔 |
| shortening condition | 缩短条件 | null state | 零态 |
| unitarity bound | 幺正性界 | central charge | 中心荷 |
| anomaly | 反常 | 't Hooft anomaly | 't Hooft 反常 |
| prepotential | 预势 | Seiberg-Witten curve | Seiberg–Witten 曲线 |
| Argyres-Douglas theory | Argyres–Douglas 理论 | special geometry | 特殊几何 |
| electric-magnetic duality | 电磁对偶 | monodromy | 单值性 |
| puncture | 穿刺点 | regular puncture | 正则穿刺点 |
| irregular / wild puncture | 非正则（野）穿刺点 | Riemann surface | 黎曼面 |
| Class S | Class S（保留英文） | UV curve | UV 曲线 |
| five-brane | 五维膜 | NS5-brane | NS5 膜 |
| geometric engineering | 几何工程 | elliptic fibration | 椭圆纤维化 |
| singularity | 奇点 | quotient | 商（quotient） |
| S-fold | S-折（保留 S-fold） | orientifold | 定向折叠 |
| flavor symmetry | 味对称性 | global symmetry | 整体对称性 |
| superconformal index | 超共形指标 | operator spectrum | 算子谱 |
| conformal bootstrap | 共形自举 | OPE | 算符乘积展开（OPE）|
| marginal | 边缘的 | exactly marginal | 恰当边缘 |
| beta function | beta 函数 | RG flow | 重整化群流 |
| nilpotent orbit | 幂零轨道 | Young tableau | 杨图 |
| Hitchin system | Hitchin 系统 | spectral curve | 谱曲线 |
| magnetic quiver | 磁振子（magnetic quiver）| quiver | 箭图 |
| gauge theory | 规范理论 | SQCD | SQCD（保留）|
| superpotential | 超势 | Kähler potential | Kähler 势 |
| Weyl anomaly | Weyl 反常 | conformal manifold | 共形流形 |
| codimension-two defect | 余维二缺陷 | line operator | 线算子 |
