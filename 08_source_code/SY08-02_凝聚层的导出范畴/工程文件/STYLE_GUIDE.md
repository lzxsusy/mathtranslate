# STYLE_GUIDE —— Orlov 2003 综述中文译注本 · 写作规范

> 本文件是**唯一**写作规范。与任何旧工程（functoriality_work、SY08-01）的习惯冲突时，以本文件为准。
> Lead 独占：译者只读，不得修改。

---

## 0. 任务与边界

底本：D. O. Orlov, *Derived categories of coherent sheaves and equivalences between them*,
Russian Math. Surveys **58**:3 (2003) 511–591（= Uspekhi Mat. Nauk 58:3 89–172）。
英文版，81 页。译者只负责分配给你的那一块（chunk）。

**你只写一个文件**：`<HOME>\Downloads\orlov_derived_work\src\chunks\<chunk>.tex`
**你只写一份报告**：`<HOME>\Downloads\orlov_derived_work\work\reports\<chunk>.md`

不得改动 `src/preamble.tex`、`src/main.tex`，不得改动别人的 chunk，不得动 `src/chunks/ch00a.tex`（Lead 的样板块）。

---

## 1. 页映射与原料

- 书页（印刷页码）= PDF 页 − 510。chunk 文件名与「原文 p.N」标记都用**书页**。
- 你的源文本：`work/src/<chunk>.txt`，每页以 `===== BOOK PAGE N =====` 起首。
- 你的页图：`work/pages/pNNN.png`，其中 **NNN = 书页 − 510**，200 dpi 灰度。例：书页 545 → `work/pages/p035.png`（= 545 − 510）。

### 1.1 文字层与页图的分工（铁律）

- **叙述文字**：`work/src/<chunk>.txt` 可信。
- **公式、交换图、表格、任何带上下标/上下限/花体/箭头的行**：文字层**一律不可信**，必须打开对应页图核对。
  已实测的崩溃样式：`q^T_X\otimes\omega^k_X` 抽成 `qTX ⊗ωk X`；`\tilde X` 的波浪线整个丢失（抽成 ` X`）；
  交换图抽成若干散行；`\bigoplus_{i=1}^{k}` 抽成 `k i=1`。
- 核对办法（任选，推荐前两个）：
  1. 直接 `read_image` 读 `work/pages/pNNN.png`（最省事）；
  2. 只关心某一处时，用裁切脚本放大：`& $py tools\crop.py --book 545 --search "ΦE" --pad 30 --out x.png`（`$py` 见 §9）；
  3. 列出该页所有文本块坐标：`& $py tools\crop.py --book 545 --blocks`。
- 若页图与文字层冲突，**以页图为准**，并在报告里登记该处（页码 + 原文抽出的样子 + 页图实际的样子）。

---

## 2. 施工顺序（每块照此走）

1. 通读 `work/src/<chunk>.txt` 全块，先弄清这一块的论证骨架（谁依赖谁）。
2. 逐页对照页图，把所有公式抄成 LaTeX 并核对（含 `\tag` 编号、上下标、花体、`\tilde`、`\widehat`）。
3. 译成 `<chunk>.tex`：**段序、段数与原书一致**；页标记逐页插入。
4. 编译（§9），修到 0 error / 0 missing character。
5. 写完 `work/reports/<chunk>.md`（§10 模板），**最后才回报**。

---

## 3. LaTeX 体例

### 3.1 页标记

每页起首插一行注释（原书页码，不是 PDF 页码）：

```latex
% [原文 p.545]
```

章首页、续页都要插。跨页的段落：标记插在**页图换页处**，即使它落在段落中间（原文的分页是硬边界，照插）。

### 3.2 章、节

```latex
% ch01a / ch02a / ch03a / ch04 / ch05a 各自开头写：
\chapter{预备知识}            % 第1章
\section{三角范畴与正合函子}   % 编号自动成为 1.1，与原书一致
```

其余块不再写 `\chapter`，只写本块起始的 `\section`（若该块以新节开头）。
节标题译文（已冻结，照用）：

| 编号 | 原书 | 译文 |
|---|---|---|
| 1 | Preliminaries | 预备知识 |
| 1.1 | Triangulated categories and exact functors | 三角范畴与正合函子 |
| 1.2 | Derived categories and derived functors | 导出范畴与导出函子 |
| 1.3 | Derived categories of sheaves on schemes | 概形上层的导出范畴 |
| 2 | Categories of coherent sheaves and functors between them | 凝聚层范畴及其间函子 |
| 2.1 | Basic properties of categories of coherent sheaves | 凝聚层范畴的基本性质 |
| 2.2 | Examples of equivalences: flopping birational transformations | 等价的例子：flop 双有理变换 |
| 3 | Fully faithful functors between derived categories | 导出范畴之间的全忠实函子 |
| 3.1 | Postnikov diagrams and their convolutions | Postnikov 图及其卷积 |
| 3.2 | Fully faithful functors between the derived categories of coherent sheaves | 凝聚层导出范畴之间的全忠实函子 |
| 3.3 | Construction of the object representing a fully faithful functor | 代表全忠实函子的对象之构造 |
| 3.4 | Proof of the main theorem | 主定理的证明 |
| 3.5 | Appendix: the n-Koszul property of a homogeneous coordinate algebra | 附录：齐次坐标代数的 n-Koszul 性质 |
| 4 | Derived categories of coherent sheaves on K3 surfaces | K3 曲面上凝聚层的导出范畴 |
| 4.1 | K3 surfaces and the Mukai lattice | K3 曲面与 Mukai 格 |
| 4.2 | The criterion for equivalence of derived categories of coherent sheaves | 凝聚层导出范畴等价的判别准则 |
| 5 | Abelian varieties | 阿贝尔簇 |
| 5.1 | Equivalences between categories of coherent sheaves on Abelian varieties | 阿贝尔簇上凝聚层范畴之间的等价 |
| 5.2 | Objects representing equivalences, and groups of auto-equivalences | 代表等价的对象与自等价群 |
| 5.3 | Semi-homogeneous vector bundles | 半齐次向量丛 |

### 3.3 陈述环境（编号手工照抄，绝不用自动编号）

原书陈述的编号形如 `Theorem 2.1.8`、`Lemma 1.1.2`、`Definition 2.2.1`、`Proposition 5.1.12`、
`Corollary 5.1.17`、`Example 2.2.5`、`Remark 3.2.4`、`Corollary 2.1.10`。

```latex
\begin{theorem}{2.1.8}
设 $X$ 与 $Y$ 是光滑射影簇……
\end{theorem}

\begin{proposition}[Orlov]{3.2.1}     % 可选方括号 = 附加名，一般不用
…
\end{proposition}

\begin{proof}
…
\end{proof}
```

可用环境（名字→显示）：`theorem` 定理、`proposition` 命题、`lemma` 引理、`corollary` 推论、
`definition` 定义、`example` 例、`remark` 注、`notation` 记号、`conjecture` 猜想、`question` 问题、`assumption` 假设。

- **编号必填**，照抄原书（原书按节编号：定理 2.1.8 = 第 2 章第 1 节第 8 条）。
- 原书陈述**末尾没有任何符号**（无 ■、无 □）。本译本同样不加。
- 若原书编号本身异常（例如 §1.1 里出现 `Definition 1.3` 而不是 `1.1.7`），**照录原编号**，在报告与 `% [Tutor Note: …]` 里说明。
- 原书陈述若直接带文献引用（`(see [8])`、`([34])`），照译在陈述正文里，如「（见 [8]）」。
- 原文的 `Proof.` 一律 `\begin{proof}…\end{proof}`；证明末原书没有符号就不要加。
- 原书**不用**「Remark 2.1.5」这类编号时，就用普通段落，不要硬造环境。

### 3.4 公式

- 原书**只有** (1)–(31) 这 31 个编号公式。凡原书印了编号的，用
  ```latex
  \begin{equation}
  \Phi_{\cE}(\,\cdot\,):=\Rb q_*\bigl(\cE\otL p^*(\,\cdot\,)\bigr) \tag{1}
  \end{equation}
  ```
  编号写原书号，不重排、不跳号。
- 无编号的行间公式用 `equation*`（或 `\[ \]`），**不要**用 `$$`。
- 行内公式一律 `$...$`；中文标点不放进公式里（`$X$ 上`，不是 `$X$上`）。
- 多行对齐用 `align`/`aligned`（禁 `eqnarray`）。
- 大算子：`\bigoplus`、`\bigwedge`、`\prod` 的上下限照原书写（例如 `\bigoplus_{i=0}^{i=n}`）。
- 分式、根式、范数、绝对值照原书。

### 3.5 交换图与示意图（重要）

**不要把交换图逐字打成文字或随意用 tikzcd 重排。** 一律用占位命令，由 Lead 从页图裁切后统一插入：

```latex
% [原文 p.545]
……考虑下图：
\figdiag{545}{a}
```

- 第一个参数 = **书页**，第二个 = 该页第几个图（a、b、c…，按页内自上而下、自左而右编号）。
- 若图是嵌在句子中间的（如 `X \xleftarrow{p} X\times Y \xrightarrow{q} Y` 这种**一行**的箭头串），
  **直接在行内/行间用数学写**，不要用 `\figdiag`：
  ```latex
  \begin{equation*}
  X\xleftarrow{\ p\ }X\times Y\xrightarrow{\ q\ }Y
  \end{equation*}
  ```
  判据：页图上是**单个数学行**（没有方框、没有分叉）→ 手写；页图上是**二维交换图或带箭头的方块/漏斗**→ `\figdiag`。
- 用 `\figdiag` 时，前面要有一句自然的引出语（「考虑下图：」「有如下交换图：」），后面接续的论证要对图说话（「图中两个方块交换，故……」）。
- 每个 `\figdiag` 都要在报告里登记：书页、字母、一句话说明图上有什么（节点数、箭头方向、有没有标注如 `\cong`、`\eta`）。

### 3.6 小节内的小标题

原书用 `a)`、`b)`、`1)`、`2)` 这类行内编号时，照用：

```latex
\begin{enumerate}[label=\alph*),leftmargin=2.4em,itemsep=1pt,topsep=2pt]
\item …
\end{enumerate}
```

原书用 `---` 接排的项（如公理 T1 的 a)、b)）可保留为独立段落，用 `\textbf{a)}` 起首，不强行列表化。

### 3.7 引理/定理的交叉引用

正文里引用陈述时，**用中文 + 原编号**：「由定理 2.1.8」「见引理 1.1.2」「推论 2.1.10 表明」。
不要用 `\ref`（本工程不用自动编号，`\ref` 会给出错误编号）。

### 3.8 脚注

原书**没有脚注**。不得新增脚注来解释概念——概念解释一律走 §6 的译注。

---

## 4. 数学内容纪律

1. **逐符号核对**页图。上下标、正负号、`\otimes` 与 `\oplus`、`\cong` 与 `=`、`\to` 与 `\mapsto`、花体 `\mathcal` 与粗体 `\mathbf` 都是事故高发处。
2. **不补写原文没有的内容**。原文跳步就照跳；解释放到译注里，且要标明是译者补的。
3. **不缩译、不删句**。原文一句就是一句；英文长句拆成两三个中文短句是允许的（§8），但不得丢信息。
4. **原书笔误照录**（例如符号印错、下标漏掉、引用编号错），译文保留原样，另加
   `% [Tutor Note: 页图印作 …，据上下文应为 …；此处照录。]`
5. 段数与原书一致；不要合并、拆分原文段落（列举项内部可以按中文习惯断行）。
6. 数学对象的名字、人名按术语表处理：`Mukai`、`Orlov`、`Bondal`、`Kuznetsov`、`Grothendieck`、`Verdier`、`Serre`、`Koszul`、`Postnikov`、`Chern`、`Todd`、`Hodge`、`Poincaré` 等保留拉丁字母，不音译。
   - 例外：已经汉化定型的「阿贝尔簇」（abelian variety）、「黎曼–罗赫」（Riemann–Roch）、「霍奇结构」（Hodge structure）、「陈特征」（Chern character）按术语表。

---

## 5. 语言规范（硬性）

**禁用句式**（出现即算不合格）：

- 「被……所……」→ 改成主动或「由……」。
- 「进行……的……」/「对……进行……」→ 改成动词。
- 「对于……而言」→ 「对……」或直接省略。
- 「作为一个……的……」堆叠。
- 「我们有……」滥用（数学里保留「我们有如下正合列」这种是可以的，但不要每段都用）。

**必须**：

- 全角标点：，。；：？！（）【】—— …… 引号用 `“”`（**不用** `「」`，这是简体出版物的规矩）。
- 英文词/公式与汉字之间留**半角空格**：`光滑射影簇 $X$ 上`、`Mukai 格`、`flop 收缩`。
- 数字与汉字之间不留空格（「第 3 章」这样的序数词按本库习惯留空格：「第 3 章」）。
- 破折号 `——`（中文双破折号），不用 `—`。
- 长句拆分：英文一个 60 词的句子，中文宁可断成 2–3 句，用「；」「，而」「因此」承接。
- 时态与人称：论文体，不用「我们将会看到」，用「下面将看到」；「we prove」→「我们证明」。

---

## 6. 译注规范（本工程的重点）

两类，各有专用写法。

### 6.1 概念性批注：`\yizhu{…}`（正文可见，随文排）

用于**解释概念、交代背景、指出与 nLab/经典文献的对应**。放在第一次出现该概念的那段之后。

```latex
\yizhu{完美复形（perfect complex）指局部同构于有限秩自由层构成的有界复形的对象；
在有界导出范畴里它们构成三角子范畴，正是使得 $\otimes^{\mathbf L}$ 保持有界的那类对象。
【来源：原书 §2.1 式 (6) 前后；Stacks Project, Tag 08E8；nLab, \emph{perfect complex}（B 级，已与前者交叉核对）】}
```

写作要求：

- 每条 60–200 字，一段话说完，不分条。
- **必须**以 `【来源：…】` 结尾，或 `〔译者按（上下文推断，无外部依据）：…〕`。
- 来源分级（照本库房规 §2.5）：
  - **A 级**：原书本身（给页码/定理号）、原始论文（给文献号）、经典教材（Hartshorne、Weibel、Kollár–Mori、章璞《三角范畴与导出范畴》等，给章节）。
  - **B 级**：nLab、Stacks Project（写 Tag 号）、EMS、MathWorld、DLMF。**单独 B 级一律标「待核」**；能给出 A 级交叉验证的要写「已与……交叉核对」。
  - **I 级**：本库既往译本/术语库。
  - **线索级**（英文维基、MO）：只能用来找线索，不得作为译注依据。
- **绝对禁止**：知乎、百度百科/知道、CSDN、简书、微信公众号、个人博客、B 站、视频课笔记、AI 摘要。这些内容不得出现在你的译注、报告、上下文里。
- **禁止抄 nLab 原文**。要用自己的话重述，只保留必要的术语与结论；不得整段翻译 nLab。
- **不得编造来源**。不确定某个 nLab 页面名是否存在，就不要写 nLab；改用 A 级或 `〔译者按（上下文推断，无外部依据）〕`。
- 数量：每块 **2–6 条**（10 页以上的块可到 8 条），宁精勿滥。只注真正会让读者卡住的概念，不注「显然」的东西。
- 不做「术语表式」罗列（那是附录 A 的事），也不做「这段话的意思是……」式的复述。

### 6.2 校勘性批注：`% [Tutor Note: …]`（正文不印，进附录 B）

用于**页图与文字层的出入、原书笔误、术语取舍、编号异常、跨块边界**。写成 LaTeX 注释，放在相关行之后：

```latex
% [Tutor Note: 页图此处印作 $\mathbf{R}^{\bullet}q_*$，而 §2.2 以下同一函子印作 $\mathbf{R}\pi_*$；本译本统一作 $\mathbf{R}q_*$。]
```

- 一句一条，写清「页图是什么 / 文字层是什么 / 本译本怎么处理 / 为什么」。
- 原书笔误一律**照录 + 批注**，绝不静默改字。

**两条硬约束**：`\yizhu` 与 `% [Tutor Note:]` 里都不得出现黑名单来源；`\yizhu` 里不得出现未标来源的断言（除「显然」「由定义」这类）。

---

## 7. 术语

- 冻结表：`work/glossary.tsv`（英文→中文→等级→备注）。**只读**，按表译；表里没有的按 §2.5 与 §5 的规矩自定，但必须
  1. 首次出现处写成「中文（English）」，
  2. 在报告 §4 里登记，
  3. 写入 `work/proposals/<你的名字>.tsv`（列：英文 / 中文 / 建议等级 / 首现页码 / 理由）。
- 英文保留规则：无稳定通行译名，或两种译名并存 → 保留英文（`flop`、`Fourier–Mukai 变换`、`Postnikov 系统`、`Ext`、`Tor`、`RHom`）。
- 同一术语在同一块里**必须**始终同一译法。

---

## 8. 记号宏（preamble 已定义，直接用，不要自己 `\newcommand`）

| 宏 | 输出 | 用途 |
|---|---|---|
| `\Db(X)` / `\db(X)` | $\mathbf{D}^{b}(X)$ | 有界导出范畴（原书粗体 D） |
| `\Dm` / `\Dp` / `\Du` | $\mathbf{D}^{-}$ / $\mathbf{D}^{+}$ / $\mathbf{D}$ | 上下有界/无界 |
| `\Rf f_*` | $\mathbf{R}f_*$ | 直接像的全导出函子 |
| `\Lf f^*` | $\mathbf{L}f^*$ | 逆像的全导出函子 |
| `\Rb` | $\mathbf{R}^{\bullet}$ | 原书 (1) 处的带点记号 |
| `\otL` | $\otimes^{\mathbf{L}}$ | 导出张量积 |
| `\cO \cE \cF \cL \cM \cG \cA…\cZ` | $\mathcal{O}$ 等 | 花体 |
| `\PP \bA \Z \Q \C \R` | 空心体 | |
| `\coh(X)` `\Qcoh(X)` | $\mathrm{coh}(X)$ | 小写直立 |
| `\Ext` `\Tor` `\RHom` `\Aut` `\Auteq` `\Tot` `\Cone` `\Cyl` `\ch` `\td` `\Td` `\End` `\Hom` `\Spec` `\Pic` `\rank` `\im` `\Ker` `\Coker` `\Supp` `\codim` | 直立算子 | |
| `\iso` | $\xrightarrow{\ \sim\ }$ | 同构箭头 |
| `\into` `\onto` | ↪ ↠ | |
| `\tilde X` `\hat A` | | 波浪线/帽子必须显式写，文字层会丢 |

需要新宏 → 在报告里提出，**不要**在 chunk 里 `\newcommand`。

---

## 9. 编译与自检

```powershell
$py = "<HOME>\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
cd <HOME>\Downloads\orlov_derived_work\src
lualatex -interaction=nonstopmode main.tex
```

（本工程路径全 ASCII，可直接编译；MiKTeX 不能写中文路径，**不要**把工程挪到中文目录。）
`main.tex` 用 `\InputIfFileExists` 注入各块，缺块也能编译，所以你随时可以整书编译。
只查你那块的错误时，用：

```powershell
$env:PYTHONUTF8="1"
Select-String -Path main.log -Pattern "^(\./chunks/ch01a|!|l\.\d+)" -Context 0,2
```

**验收线**：你的块不得引入 `!` 开头的错误、不得有 `Missing character`（缺字）、不得有 `Overfull \hbox` 超过 5pt 的行
（真排不下就调整措辞或断行，不要靠 `\sloppy` 糊过去）。

---

## 10. 报告模板（`work/reports/<chunk>.md`）

```markdown
# <chunk> 报告（原书 p.X–p.Y）

## 1. 内容与结构
- 本块覆盖的小节与页码：
- 主要陈述清单（编号 + 一句话）：定理 …、命题 …、引理 …、推论 …、定义 …、例 …、注 …

## 2. 公式与图
- 编号公式：无 / (12)(13)（列出编号）
- `\figdiag` 占位：p.545 a（Postnikov 系统，节点 X_0..X_n 与 Tot）、p.546 b（…）
- 页图与文字层的出入（逐条：页码 + 文字层抽出 + 页图实际 + 处理）

## 3. 译注
- `\yizhu` 条数：N；分别注了什么（一行一条）
- `% [Tutor Note:]` 条数：M；分别注了什么（一行一条）

## 4. 术语
- 用了冻结表但觉得不妥的：
- 新定术语（已写入 proposals/<名>.tsv）：

## 5. 存疑（必须老实写）
- 未解决的疑点（页码 + 问题 + 我的猜测）：
- 编译状态：`file:line=… fatal=… undefined=… missingchar=… overfull=…`

## 6. 与邻块的边界
- 本块从哪句开始（原书首句）、到哪句为止（原书末句）：
- 有没有把邻块的内容多译/漏译：
```

---

## 11. 禁止事项（触犯即退回重做）

1. 改动 `preamble.tex` / `main.tex` / 别人的 chunk / `ch00a.tex`。
2. 用自动编号（`\label`/`\ref`/`\begin{theorem}` 不带编号参数）。
3. 自造宏、自造环境、加载新宏包。
4. 把交换图逐字打成文字、或用 tikzcd 自行重排后与原图不一致。
5. 补写原文没有的数学内容（含「顺便说明」「显然可以推广」）。
6. 静默修改原书笔误。
7. 编造文献编号、页码、nLab 页面名、Stacks Tag 号。
8. 引用黑名单来源。
9. 只交 tex 不交报告，或报告写「一切正常」而无实质内容。
10. 把整块内容压缩成摘要式翻译（漏句、漏证、漏「显然」）。
