# tr-03 块交叉校对报告

- 校对对象：`work/src/chunks/tr03a.tex`（pp.45–50）、`tr03b.tex`（pp.51–56）、`tr03c.tex`（pp.57–60）
- 原文范围：pp.45–60；tag 区间 3.108–4.2（含 Table 1, p.47）
- 校对者：tr-02（只读校对，未改动他人任何文件）
- 方法：逐页 `work/pages/pNNN.png`（200 dpi）整页比对；关键公式 `tools/crop.py` 500–900 dpi 局部复核；`work/tags_bypage.txt` 逐页核号；`work/split/pNNN.txt` 文字层核漏译。

## 0. 结论摘要

- **编号公式：116 条 = 3.108–3.221（114 条）+ 4.1、4.2，与 `tags_bypage.txt` 逐页一一对应，无缺、无重、无跳、无自造编号。**
- **抽查 20 条编号公式并逐符号核对：全部与原文一致**（含 Lead 指定的 3.114、3.121、3.140、3.145、3.155、3.167–3.169、3.174–3.175、3.194、3.205、4.1–4.2）。原文本中两处内部矛盾（(3.167) 的 “2p×(m+p)” 与 (3.168) 的 min(2p,m+p)、(3.175) 的对角元错位排版）被忠实照抄并加批注指出，处理正确。
- **Table 1（p.47）逐格核对：14 行数据全部正确**（群名、中心、表示名、荷的 mod 数、Spin(4n) 的 Z2×Z2 二元组），4 列结构、multirow 合并、表题均正确。
- **结构：8 个标题（3.3.3 / 3.3.4 / 3.3.5 / 3.4 / 3.4.1 / 3.4.2 / §4 / 4.1）位置与层级全部正确；6 个方框类型全部正确**（3 个 notebox + 3 个 examplebox）。
- **漏译：pp.45–60 逐页对照无漏译**（含 3 个脚注：p.49 #4、p.55 #5、p.60 #6）。
- 术语：跨块 2 项已由我（tr-02）在自己的块内对齐；本块内部有 1 项不一致（双基础/双重基础）需 tr-03 统一。
- **结论：通过。无公式错误、无漏译、无结构性错误；仅 2 处术语统一（必须改）+ 5 处润色（可选改）。**

## 1. 编号完整性表

| 页 | tags_bypage.txt | tr03 文件中实际 | 所在文件 | 结果 |
|---|---|---|---|---|
| p.45 | 3.108–3.113（6 条） | 3.108–3.113 | tr03a | ✅ |
| p.46 | 3.114–3.121（8 条） | 3.114–3.121 | tr03a | ✅ |
| p.47 | 3.122–3.126（5 条） | 3.122–3.126 | tr03a | ✅ |
| p.48 | 3.127–3.135（9 条） | 3.127–3.135 | tr03a | ✅ |
| p.49 | 3.136–3.146（11 条） | 3.136–3.146 | tr03a | ✅ |
| p.50 | 3.147–3.155（9 条） | 3.147–3.155 | tr03a | ✅ |
| p.51 | 3.156–3.161（6 条） | 3.156–3.161 | tr03b | ✅ |
| p.52 | 3.162–3.169（8 条） | 3.162–3.169 | tr03b | ✅ |
| p.53 | 3.170–3.177（8 条） | 3.170–3.177 | tr03b | ✅ |
| p.54 | 3.178–3.184（7 条） | 3.178–3.184 | tr03b | ✅ |
| p.55 | 3.185–3.189（5 条） | 3.185–3.189 | tr03b | ✅ |
| p.56 | 3.190–3.194（5 条） | 3.190–3.194 | tr03b | ✅ |
| p.57 | 3.195–3.202（8 条） | 3.195–3.202 | tr03c | ✅ |
| p.58 | 3.203–3.210（8 条） | 3.203–3.210 | tr03c | ✅ |
| p.59 | 3.211–3.219（9 条） | 3.211–3.219 | tr03c | ✅ |
| p.60 | 3.220, 3.221, 4.1, 4.2（4 条） | 同 | tr03c | ✅ |
| **合计** | **116** | **116** | — | **✅ 无缺/重/跳** |

> 附注：逐条 tag 的“所在页”也与 `tags_bypage.txt` 的页号一致（已脚本化校验，0 处错位）；每个 `\tag` 前的 `% [原文 p.N]` 页标均正确。

## 2. 逐符号核对表（抽查 20+ 条，200–900 dpi 核对）

| tag | 页 | 原文关键符号 | tr03 转录 | 判定 |
|---|---|---|---|---|
| 3.108 | p.45 | $G^{(1)}=1$ | 同 | ✅ |
| 3.110 | p.45 | $\pi_1(SO(3))=\Z_2$ | 同 | ✅ |
| 3.113 | p.45 | $U(\Sigma_2)=\exp\!\big(\ii\pi\int_{\Sigma_2}w_2\big)$ | 同（$\Sigma_2$，非 $\Sigma_{d-2}$） | ✅ |
| 3.114 | p.46 | $\fg\in\{\mathfrak{su}(n),\mathfrak{so}(n),\mathfrak{sp}(n),\mathfrak{e}_6,\mathfrak{e}_7,\mathfrak{e}_8,\mathfrak{f}_4,\mathfrak{g}_2\}$ | 同 | ✅ |
| 3.118 | p.46 | $G\in\{SU(n),\Spin(n),\Sp(n),E_6,E_7,E_8,F_4,G_2\}$ | 同 | ✅ |
| 3.121 | p.46 | $Z(\cG)=\dfrac{Z(G)}{\cZ}$ | 同 | ✅ |
| 3.122/3.124 | p.47 | $\cZ\subseteq Z(G)\subset G$；$q(R)=q(R')\in\widehat{Z}(\cG)$ | 同（$\subset$ 与 $\subseteq$ 未混；宽帽位置正确） | ✅ |
| 3.129/3.130 | p.48 | $\mathrm{D}_{d-3}=\pi_1(\cG)=\cZ$；$G^{(d-3)}=\widehat{\pi_1(\cG)}=\widehat{\cZ}$ | 同（wide hat 覆盖 $\pi_1(\cG)$） | ✅ |
| 3.134 | p.48 | $U_h^{(m)}(\Sigma_2)=\int_{\Sigma_2}h(w_2),\ h\in\widehat{\cZ}$ | 同 | ✅ |
| 3.140 | p.49 | $G^{(1)}=\widehat{\mathrm{D}}_1=\widehat{\ \widehat{Z}(\cG)/Q_{\mathrm{matter}}\ }$（两层帽子） | 同 | ✅ |
| 3.145 | p.49 | $G^{(1)}=\Z_{\gcd(g,q_1,q_2,\cdots,q_m)}$ | 同 | ✅ |
| 3.146 | p.49 | $q_i\equiv q(R_i)\in\widehat{Z}(\cG)=\Z_g=\{0,1,\cdots,g-1\}$ | 同 | ✅ |
| 3.155 | p.50 | $G_{\min}=\dfrac{\cG}{G^{(1)}}$ | 同 | ✅ |
| 3.167–3.169 | p.52 | $Y=(Z|Q)$；原文写 “$2p\times(m+p)$ matrix”；$\prod_{i=1}^{\min(2p,m+p)}\widehat{\Z}_{q_i^D}$；$\diag(\cdots)\subset\mathrm{SNF}(Y)$ | 全部照抄原文（含 min(2p,m+p)）；批注指出 $Y$ 实为 $p\times(m+p)$、上限应为 $p$ | ✅（忠实 + 批注正确） |
| 3.174/3.175 | p.53 | $Y=\begin{pmatrix}4&0&2\\0&2&1\end{pmatrix}$；$\mathrm{SNF}(Y)=\begin{pmatrix}0&4&0\\0&0&1\end{pmatrix}$ | 同（原文本就是此错位排版，非转录错误） | ✅ |
| 3.187/3.188 | p.55 | $\mathcal{D}_{j,\phi},\ j\notin\Z$；$\mathcal{D}_{j,\phi}\equiv\mathcal{W}_j\mathcal{H}_\phi$ | 同 | ✅ |
| 3.194 | p.56 | $\mathcal{P}(w_2)=\tilde w_2\cup\tilde w_2-\delta\tilde w_2\cup_1\tilde w_2$ | 同（900 dpi 复核：$\delta$ 为余微分、$\cup_1$ 为高阶 cup 积） | ✅ |
| 3.205 | p.58 | $G^{(1)}=\widehat{\mathrm{D}}_1=\widehat{\ \mathrm{D}_\gamma/Q_{\mathrm{matter}}\ }$ | 同 | ✅ |
| 3.218/3.219 | p.59 | $\{\{(0,0),(2,0),(0,1),(2,1)\}\to\widehat{0},\ldots\}$；$\mathrm{D}_\gamma=\{(0,0,0),(0,2,0),(1,1,0),(1,3,0),(0,0,1),(0,2,1),(1,1,1),(1,3,1)\}$ | 同（900 dpi 复核：$\widehat{0}/\widehat{1}$ 为宽帽，8 个元素逐一相符） | ✅ |
| 3.220/3.221 | p.60 | $\mathrm{D}_1=\Z_4$；$G^{(1)}=\Z_4$ | 同 | ✅ |
| 4.1/4.2 | p.60 | $G^{(0)}=U(1)$；$F=\dd A$ | 同 | ✅ |

## 3. Table 1（p.47）逐格核对

结构：4 列（单连通群 / 中心 / 表示 / 表示的荷）✅；`\toprule/\midrule/\bottomrule` ✅；`\multirow` 合并 ✅；`\tabtitle{1}{…}` ✅；表位在 p.47 顶端（先表后正文）✅。

| # | 原表（Simply Connected Group / Center / Representation / Charge） | tr03a 表格 | 判定 |
|---|---|---|---|
| 1 | $SU(n)$ / $\Z_n$ / Fundamental, $\bm{F}$ / 1 mod $n$ | 基础表示 $\bm F$，1 mod $n$ | ✅ |
| 2 | Antisymmetric, $\bm{\Lambda}^2$ / 2 mod $n$ | 反对称表示 $\bm\Lambda^2$，2 mod $n$ | ✅ |
| 3 | Symmetric, $\bm{S}^2$ / 2 mod $n$ | 对称表示 $\bm S^2$，2 mod $n$ | ✅ |
| 4 | $Sp(n)$ / $\Z_2$ / Fundamental, $\bm F$ / 1 mod 2 | 同 | ✅ |
| 5 | $Spin(2n+1)$ / $\Z_2$ / Vector, $\bm F$ / 0 mod 2 | 矢量表示 $\bm F$，0 mod 2 | ✅ |
| 6 | Irreducible Spinor, $\bm S$ / 1 mod 2 | 不可约旋量表示 $\bm S$，1 mod 2 | ✅ |
| 7 | $Spin(4n+2)$ / $\Z_4$ / Vector, $\bm F$ / 2 mod 4 | 同 | ✅ |
| 8 | Irreducible Spinor, $\bm S$ / 1 mod 4 | 同 | ✅ |
| 9 | Irreducible Co-spinor, $\bm C$ / 3 mod 4 | 不可约余旋量表示 $\bm C$，3 mod 4 | ✅ |
| 10 | $Spin(4n)$ / $\Z_2\times\Z_2$ / Vector, $\bm F$ / (1 mod 2, 1 mod 2) | 同（二元组顺序正确） | ✅ |
| 11 | Irreducible Spinor, $\bm S$ / (1 mod 2, 0 mod 2) | 同 | ✅ |
| 12 | Irreducible Co-spinor, $\bm C$ / (0 mod 2, 1 mod 2) | 同 | ✅ |
| 13 | $E_6$ / $\Z_3$ / Fundamental, $\bm{27}$ / 1 mod 3 | 基础表示 $\bm{27}$，1 mod 3 | ✅ |
| 14 | $E_7$ / $\Z_2$ / Fundamental, $\bm{56}$ / 1 mod 2 | 基础表示 $\bm{56}$，1 mod 2 | ✅ |

表题完整对应原文：`Here we list the simply connected groups having non-trivial centers. …For E8, F4 and G2, the center is trivial.` → 中文逐句译出 ✅。

## 4. 结构核对

| 位置 | 原文标题 | tr03 中的写法 | 层级 | 判定 |
|---|---|---|---|---|
| p.46 | 3.3.3 Pure Yang–Mills Theory with General Gauge Group | `\subsubsection{一般规范群的纯 Yang--Mills 理论}`（tr03a:53） | subsubsection | ✅ |
| p.48 | 3.3.4 Including Matter Fields | `\subsubsection{包含物质场}`（tr03a:224） | subsubsection | ✅ |
| p.51 | 3.3.5 Multiple Gauge Group Factors | `\subsubsection{多个规范群因子}`（tr03b:14） | subsubsection | ✅ |
| p.53 | 3.4 Discrete Theta Angle in 4d Gauge Theories | `\subsection{四维规范理论中的离散 theta 角}`（tr03b:144） | subsection | ✅ |
| p.53 | 3.4.1 Pure SO(3)₋ Yang–Mills Theory | `\subsubsection{纯 $\SO(3)_-$ Yang--Mills 理论}`（tr03b:148） | subsubsection | ✅ |
| p.57 | 3.4.2 General Non-Abelian 4d Gauge Theory | `\subsubsection{一般的非 Abel 四维规范理论}`（tr03c:5） | subsubsection | ✅ |
| p.60 | 4 Properties of Higher-Form Symmetries | `\section{高阶形式对称性的性质}`（tr03c:174） | section | ✅ |
| p.60 | 4.1 Background Fields | `\subsection{背景场}`（tr03c:178） | subsection | ✅ |

方框核对：

| 页 | 原文外观 / 标题 | 应有环境 | tr03 实际 | 判定 |
|---|---|---|---|---|
| p.45 | 粉色带标题 “First Homotopy Group of SO(3)” | notebox | notebox（tr03a:23） | ✅ |
| p.50 | 橙色 “Example 3.10: su(n) Gauge Theories with Adjoint and Fundamental Matter” | examplebox | examplebox（tr03a:300） | ✅ |
| p.53 | 橙色 “Example 3.11: An Orthosymplectic Quiver Gauge Theory” | examplebox | examplebox（tr03b:103） | ✅ |
| p.54 | 粉色带标题 “Notation for OPE” | notebox | notebox（tr03b:186） | ✅ |
| p.58 | 粉色带标题 “Quadratic Refinement” | notebox | notebox（tr03c:99） | ✅ |
| p.59 | 橙色 “Example 3.12: An Orthosymplectic Gauge Theory with Discrete Theta Angle” | examplebox | examplebox（tr03c:110） | ✅ |

其它：本块原文无插图，tr03 无 `figure` 环境 ✅（符合；fig9–11 属 tr-02、fig12+ 属 tr-04）。

## 5. 漏译检查（逐页对照 split 文字层）

**结论：无漏译。**

- p.45：3 个 `\para`（电 1-形式对称性 / 't Hooft 算符 / 磁 $(d-3)$-形式对称性 / 拓扑面算符）+ 1 notebox，齐；"in contrast with (3.88)/(3.98)" 类句子均在。
- p.46：3.3.3 引言、"where:" 下两条 itemize 项（$G$ 单连通、$\cZ\subseteq Z(G)$）、"compiled in table 1"、"At the present moment, we do not include any matter fields." 齐。
- p.47：Table 1 + 表题 + 电 1-形式对称性段（含 "identified with the irreducible representations of the simply connected group $G$" 一句）+ (3.122)–(3.126) 齐。
- p.48：磁对称性段 + 拓扑算符段 + 3.3.4 标题 + (3.127)–(3.135) 齐。
- p.49：电 1-形式对称性段 + 脚注 #4（"regarding $\widehat Z(\cG)$ as an additive group"）+ `\para{$G^{(1)}$ 的计算}` + (3.136)–(3.146) 齐。
- p.50：Example 3.10（含 "(3.148)–(3.153)" 全式）+ 磁对称性段 + 拓扑算符段（含 (3.154)、(3.155)）齐。
- p.51：(3.156)、"where $w_2^{\min}$ is…"、"topological surface operators … continue to be (3.134)"、3.3.5 标题、"quiver gauge theories" 加粗句、(3.157)–(3.161) 齐。
- p.52：物质场段（(3.162)–(3.164) 及 "constraints on $R_{i,a}$…"）、高阶形式对称性段、SNF 记账（(3.165)–(3.169)）齐。
- p.53：Example 3.11 全部（(3.170)–(3.176)）+ 3.4 标题+引言 + 3.4.1 标题 + "In the previous subsection…" + (3.177) 齐。
- p.54："…is referred to as the $SO(3)_-$ theory [42]…" 接续句 + `\para{线算符}` + (3.178)–(3.182) + notebox "Notation for OPE"（(3.183)(3.184)）+ "same set (3.178)…spectrum … different. If $\phi$" 齐。
- p.55：跨页句续写（"can be lifted to a cocharacter for $SU(2)$…"）+ (3.185)–(3.188) + 脚注 #5 + Witten 效应段 + (3.189) 齐。
- p.56：`\para{屏蔽}` + (3.190)–(3.192) + "dyonic 1-form symmetry group" 加粗句 + `\para{离散 theta 角}` + (3.193)(3.194) + "$\cP(w_2)$ 为偶类" 段 + "正如普通 theta 角项是场强的平方…" 段 + "As we discussed above…(3.189)" 齐。
- p.57：3.4.2 标题 + (3.195) + `\para{'t Hooft–Wilson 线算符}` + (3.196)(3.197) + `\para{1-形式对称性}` + (3.198)–(3.202) 齐。
- p.58：$\widehat Z(\cG)=\widehat Z(G)/\widehat\cZ$ 段 + (3.203)–(3.205) + `\para{离散 theta 项}` + (3.206)–(3.209) + notebox "Quadratic Refinement"（(3.210)）+ 末句齐。
- p.59：Example 3.12 全部（(3.211)–(3.219)）齐。
- p.60：Example 3.12 收尾（(3.220)(3.221)）+ §4 标题 + 两段引言（含 [4]、[81–121]）+ 4.1 标题 + `\para{重温连续的 0-形式对称性}` + 脚注 #6 + (4.1)(4.2) 齐。

边界接缝：
- 与 tr-02：p.44 末为 (3.107)（"$R_j$ is an $SO(3)$ representation $\iff j\in\Z$"），tr03a 从 p.45 的 `\para{电 1-形式对称性}` 起 —— **无重复、无缺口** ✅。
- 内部：tr03a 末句 "它们可以理解为诱导出群 (3.155)" 在 p.50 收尾，tr03b 以 "这些涡旋位形不能提升为 $\cG$ 的涡旋位形" 起 —— 跨页句切分正确 ✅。
- 与 tr-04：tr03c 末为 (4.2) + 脚注 #6（p.60 结束），tr04a 从 p.61 的 (4.3) 起 —— **无重复、无缺口** ✅。

## 6. 术语核对

| 项 | 其它块用法 | tr03 用法 | 处理 |
|---|---|---|---|
| cocharacter | tr02 原“余特征”、tr06“余特征标” | **余特征标** | 已由我把 tr02 统一为“余特征标”（6 处）；建议定为项目标准 |
| Smith normal form | tr02 原“Smith 标准型” | **Smith 标准形** | 已由我把 tr02 统一为“Smith 标准形”（6 处） |
| bifundamental representation | tr03b 批注“双基础”、tr03b:109 与 tr03c:136 正文“双重基础” | 块内不一致 | **必须改**（见 §7） |
| 其余 | — | — | 与 `glossary.tsv` 一致：单连通、中心、$'t$ Hooft、Pontryagin 对偶、离散 theta 角、涡旋位形、阻碍类、双荷、规范代数、单（simple）、余维、规范丛 等 ✅ |

## 7. 必须改（可替换文本）

| # | 位置 | 现状 | 改为 | 理由 |
|---|---|---|---|---|
| 1 | tr03b.tex:109 | `物质场处于 $\cG$ 的双重基础表示` | `物质场处于 $\cG$ 的双基础表示` | 与 tr03b:47 批注“双基础物质场”、以及项目内统一用词一致 |
| 2 | tr03c.tex:136 | `我们另外加入处于双重基础表示 (3.171) 的物质场` | `我们另外加入处于双基础表示 (3.171) 的物质场` | 同上（同一术语两文件须一致） |

> 除上述 2 处术语外，**未发现必须修改的公式、结构或漏译问题。**

## 8. 可选改（可替换文本，不影响验收）

| # | 位置 | 现状 | 建议 | 理由 |
|---|---|---|---|---|
| 1 | tr03b.tex:232 | `把通常的（相对于离散的）theta 角改变为` | `把通常的（而非离散的）theta 角改变为` | 原文 “the usual (as opposed to discrete) theta angle” 的对比语义 |
| 2 | tr03b.tex:150 | `我们在一般的 $d$ 中讨论了纯 $\SU(2)$ 与 $\SO(3)$ Yang--Mills 理论` | `我们在一般的 $d$ 维时空中讨论了纯 $\SU(2)$ 与 $\SO(3)$ Yang--Mills 理论` | 中文更顺 |
| 3 | tr03a.tex:55 | `考虑一个基于单的非 Abel 规范代数的纯 $d$ 维规范理论` | `考虑一个基于单非 Abel 规范代数的纯 $d$ 维规范理论` | “单”作定语，避免歧义 |
| 4 | tr03a.tex:143 | `这些表示可以等同于单连通群 $G$（…）的、具有如下性质的不可约表示：` | `这些表示可以等同于单连通群 $G$（…）中那些满足下述性质的不可约表示：` | 长句更顺（原文 “having the property that…”） |
| 5 | tr03b.tex:267 附近 | `(3.193) 被称为离散 theta 角`、“分数场强” | 复刻原文强调：`\textbf{离散 theta 角}`、`\emph{分数场强}` | 原文 p.56 对 “**discrete theta angle**” 加粗、“fractional field strength” 用斜体；STYLE_GUIDE 未强制，仅风格统一 |

## 9. 自动检查（脚本结果，供 Lead 复核）

| 文件 | tag 数 | 首–尾 | BOM | CRLF | U+FFFD | `**` | 花括号 | `$` 成对 | begin/end | 禁用命令 |
|---|---|---|---|---|---|---|---|---|---|---|
| tr03a.tex | 48 | 3.108–3.155 | 无 | 无 | 无 | 0 | 298/298 | ✅ | 全配平 | 无 |
| tr03b.tex | 39 | 3.156–3.194 | 无 | 无 | 无 | 0 | 208/208 | ✅ | 全配平 | 无 |
| tr03c.tex | 29 | 3.195–4.2 | 无 | 无 | 无 | 0 | 161/161 | ✅ | 全配平 | 无 |

（禁用命令检查项：`\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\ref{}`、`\eqref`、`\cite`、`$$`。）
