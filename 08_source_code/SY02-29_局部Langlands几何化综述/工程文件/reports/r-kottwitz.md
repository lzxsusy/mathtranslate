# r-kottwitz — §8 Kottwitz 猜想（原文 p.36–p.42）

译手：kottwitz　｜　底本：`fargues_ov/Fargues_Geometrization_overview.pdf` p.36–p.42

## 1. 交付

| 文件 | 内容 |
|---|---|
| `源码/sections/s10-kottwitz.tex` | 原文 §8 全文（8.1 + 8.2.1 + 8.2.2），285 行 |
| `工程文件/reports/r-kottwitz.md` | 本报告 |
| `工程文件/work/trace-kottwitz.md` | 逐段译法 trace、公式清单、页码锚点 |

**编译自检**（必做项）：
```
cd 源码 && build.bat check sections/s10-kottwitz.tex f
→ [OK] _check_f.pdf（7 页，0 error，0 overfull box）
```
`_check_f.pagemarks` = `36 37 38 39 40 41 42`（7 个锚全部登记）。

**页锚**：p.36 段首（`\section` 后）；p.37 句中（`\srcpageinl`，落在"开层对应｜的是这样的轨迹"处，与原文页界一致）；p.38 / p.39 / p.40 / p.41 段首；p.42 文件末尾。

**统计**：section 1，subsection 2，subsubsection* 2，定理类环境 8，编号公式 1（(9)），无号展示式 30 余条，tikz-cd 交换图 7 张，`\yizhuw` 译注 10 条。

**七张交换图**（全部照原文对象与箭头重排）：
1. p36 笛卡尔方（`[P^{n−1,◊}/GL_n] → [Spa(E)/GL_n]`，竖箭头 `i`、`(x₁,id)`）
2. p38 五节点图（Spa、Hecke、Bun、Bun×Spa）
3. p38 Frobenius 2-胞腔（`x_{b^σ}` / `x_b` 双弯箭头 + `\Downarrow`）
4. p38 两个周期态射 `π_{dR}` / `π_{HT}`
5. p39 两步构造方（含 `h←`、`h→`）
6. p39 真基变换方（`[Gr^{≤μ}…] → [Spa(◊)…]`）
7. p40 三行四列分解图（`j` 与 Bun 之间的 hook 箭头、`x_b` 反向同构）

## 2. 编号对齐表

| 原文 | 译文 | 标签 | 备注 |
|---|---|---|---|
| 8. Kottwitz conjecture on the cohomology of basic RZ spaces ([22]) | `\section{Kottwitz 猜想：基本 RZ 空间的上同调（[22]）}` | — | "RZ" 按原文缩写保留 |
| 8.1. The fundamental example: Lubin–Tate and Drinfeld spaces | `\subsection{基本例子：Lubin--Tate 空间与 Drinfeld 空间}` | — | |
| (9) | `\begin{equation}\tag{9}` | `eq:8.9` | 原文公式号，用 `\tag` 硬保 |
| Remark 8.1 | `remark` | `rem:8.1` | ✔ 8.1 |
| 8.2. The general case | `\subsection{一般情形}` | — | 原文此标题孤立在 p.37 末行 |
| 8.2.1. Local Shtuka moduli spaces | `\subsubsection*{8.2.1 局部 shtuka 模空间}` | — | 标题内保留原文号 |
| Proposition 8.2 | `proposition` | `prop:8.2` | ✔ 8.2 |
| Remark 8.3 | `remark` | `rem:8.3` | ✔ 8.3 |
| 8.2.2. The link with moduli spaces of p-divisible groups | `\subsubsection*{8.2.2 与 $p$-可除群模空间的联系}` | — | |
| Theorem 8.4 | `theorem` | `thm:8.4` | ✔ 8.4 |
| Remark 8.5 | `remark` | `rem:8.5` | ✔ 8.5 |
| Remark 8.6 | `remark` | `rem:8.6` | ✔ 8.6 |
| Theorem 8.7 (Scholze–Weinstein) | `theorem` | `thm:8.7` | ✔ 8.7 |
| Remark 8.8 | `remark` | `rem:8.8` | ✔ 8.8 |

**关于 `conjecture` 环境**：本块**没有**猜想环境需要排。原文 §8 只在行文里引用 §7 的猜想（"According to the conjecture one has"、"The conjecture thus predicts that"、"The conjecture predicts the following"），并未在此重述猜想，故任务书提示的 `\begin{conjecture}[Kottwitz]` 情形在本块不出现；本节实际出现的编号环境恰为 Remark 8.1 … Remark 8.8 这 8 个。

定理环境用共享计数器 `[section]`，在本块内顺序恰为 8.1→8.8，与原文**逐条同号**（在整体构建中 `s10` 是第 8 个 `\section`：`s01` 用 `\section*`，`s02–s09` 为 §1–§7，故本节号 = 8）。

正文内引用照原文保留：§7、§6、定义 6.8、推论 6.10、文献号 [22] [23] [30]。

## 3. 译注（10 条，全部为 `\yizhuw`，无外部文献依据）

| # | 位置 | 要点（为什么加） |
|---|---|---|
| 1 | 8.1 开头 b 矩阵后 | 解释 b 的矩阵形状 ← 斜率 1/n 基本元；`ℰ_b=O(1/n)`、`J_b=σ-中心化子`。不解释则后文"b 是基本的"无着落 |
| 2 | 8.1 Hodge–Tate 正合列后 | Lubin–Tate 塔与 Drinfeld 塔在无穷水平互为对偶，故"Drinfeld 覆盖的 RZ 版本"是把同一族挠子换到 RZ 一侧读 |
| 3 | p.39 末 L-包处 | `S_φ` = 中心化子分量群，`π_0(S_φ)` 即 L-包指标集——否则 `x₁*𝓕_φ` 的分解式看不出依据 |
| 4 | "可容许轨迹"处 | "可容许"是 RZ 术语：它是 `π_{dR}` 的定义域，`π_{HT}` 把它映到 Newton 层 |
| 5 | Hecke 性质展示式后 | 原文未定义 `IC_μ`（相交上同调复形），并说明该式"算什么" |
| 6 | p.40 "各包含映射都是开子集"后 | `κ(b)` 是 Kottwitz 不变量，取值于 `Z(Ĝ)^Γ` 特征群，决定 Newton 层——是后文筛选 L-包的依据 |
| 7 | "约化整模型"处 | `\ul{G}` 与 `G` 的区别（整模型/一般纤维），level 取在 `\ul{G}(Z_p)` |
| 8 | "把 Ğ-结构纳入进来"后 | `𝓑𝓣` 是 p-可除群（Barsotti–Tate 群）的叠；按定义 6.8 修改后才记录 Ğ-结构 |
| 9 | "一道练习"后 | "decent" 是原文沿用的技术形容词，未给定义，译文保留原文 |
| 10 | "平凡化模空间"后 | 原文若干处给 `G(Q_p)`、`J_b(Q_p)` 加下划线且未说明，译文照排、不改数学内容 |

## 4. 疑点表

| # | 页 | 原文 | 处理 |
|---|---|---|---|
| 1 | 36 | "The open stratum **correspond** to" | 主谓不一致；译作"开层对应的是…"，不改原意 |
| 2 | 36 | "to give **one self** an element" | oneself 的误拼；译"给自己一个元素" |
| 3 | 37 | "**This is means** the smooth-equivariant cohomology complex…" | 语法不通（疑为 This means）；照译"这是说…" |
| 4 | 37 | "the well known realization … **for in** the cohomology of Drinfeld tower" | 疑衍词 for；译"在 Drinfeld 塔上同调中" |
| 5 | 38 | "It **equipped** with an action" | 缺 is；译"它带有…作用" |
| 6 | 38 | "commutes **wit** the action" | with 的误拼；不影响译义 |
| 7 | 38 | "**We note** Q̌_p for L" | note 用作 denote；译"记 L=Q̌_p" |
| 8 | 39 | Newton 层写作 `Gr^{≤μ,b} ⊂ Gr^{≤−μ}` | 前后指数不一致（≤μ,b 与 ≤−μ）；**照排**，未擅改 |
| 9 | 39–40 | `G(Q_p)`、`J_b(Q_p)` 多处带下划线（`\ul{…}` 覆盖整串） | 原文如此、未给说明；照排 + 译注 10 |
| 10 | 40 | 命题中 `ρ ∈ Ŝ_φ` 又写 `ρ|_{Z(Ĝ)^Γ}=κ(b)` | 符号层次略乱；照排 |
| 11 | 40 | Remark 8.3 用 `Z(Ĝ^Γ)`，命题用 `Z(Ĝ)^Γ` | 原文不一致；**照排**（Γ 一在帽内、一在帽外） |
| 12 | 40 | "this is left to the **courageous reader**…" | 作者自述性插话，照译"这留给勇敢的读者……" |
| 13 | 41 | "Hodge **chocaracter**" | cocharacter 的误拼；译"Hodge 余特征" |
| 14 | 41 | "**rigification**"（两处） | rigidification 的误拼；译"刚性化" |
| 15 | 41 | "the couple (H,ρ) **is** the p-divisible group together with…" | 英文表述残缺；译"这一对指的是…" |
| 16 | 41 | `G`（一般纤维）与 `\ul{G}`（整模型）混用 | 用 `\ul{G}` 逐处区分，见译注 7 |
| 17 | 41 | `\mathcal{BT}`（花体 BT） | 与 preamble 的 `\BT`（正体）不同；按原文用 `\mathcal{BT}`，请 Lead 决定全书统一 |
| 18 | 41 | "We use the results of section 6" 等跨节引用 | 只写"§6/定义 6.8/推论 6.10"，未加 `\ref`（其他块的标签我不可见） |
| 19 | 42 | p.42 全页为 §9（"9. The abelian case"），§8 无 p.42 正文 | 任务书要求 7 个锚，故 `\srcpage{42}` 置于**本文件末尾**；**请 Lead 让 s11 不要重复锚 42**，否则分页标记会重复登记 |
| 20 | p.3（导引） | "study of this key case is the main ingredient that lead the author to his conjecture." | 该自述句在**导引**（s01 块），不在 §8.1；本块无法保留，若需保留请 s01 译手处理。§8 内唯一同类自述是疑点 12（已保留） |

文献引用按原文以方括号数字排版（`[22]`、`[23]`、`[30]`），未写 `\cite{}`：文献键由 `s99` 决定，我不能猜键名以免整体构建出现 ?。若 Lead 统一改用 `\cite`，本文件 3 处方括号号需同步替换。

## 5. 新增术语建议（glossary 未收）

| 原文 | 建议译名 | 出现处 |
|---|---|---|
| admissible locus | 可容许轨迹 | p.39 |
| Newton stratum | Newton 层 | p.39 |
| quasi-isogeny | 拟同源 | p.41 |
| rigidification | 刚性化 | p.41 |
| reductive integral model | 约化整模型 | p.41 |
| partially proper | 部分 proper | p.41 |
| covariant isocrystal | 共变等晶体 | p.41 |
| Hodge cocharacter | Hodge 余特征 | p.41 |
| cuspidal | 尖（的） | p.37、p.40 |
| supercuspidal | 超尖（的） | p.40 |
| minuscule | 极小（minuscule） | p.38、p.40 |
| Weil descent datum | Weil 下降数据 | p.38 |
| square integrable representation | 平方可积表示 | p.37 |
| discrete Langlands parameter | 离散 Langlands 参数 | p.37 |
| intersection cohomology (complex) | 相交上同调（复形） | p.40 |
| perverse sheaf | 反常层 | p.37 |
| HN stratification | HN 分层 | p.36 |
| pro-étale torsor | pro-étale 挠子 | p.39 |
| formal scheme | 形式概形 | p.41 |
| basic element (of B(G,μ)) | 基本元 | p.38、p.40 |
| local shtuka moduli space | 局部 shtuka 模空间 | p.38 |
