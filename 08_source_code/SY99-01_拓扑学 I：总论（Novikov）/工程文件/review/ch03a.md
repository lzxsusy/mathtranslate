# 核验报告 · ch03a（原书 p.40 中部–p.46）
核验人：丁　　作者：甲　　日期：2026-11-09

## 结论

需修改 3 处（均为体例/文字，改动量小）；译文整体质量高。7 页逐页对照 pages\p047.png–p053.png（原书 p.40–p.46）：无漏句、无漏段，公式 (1.1)–(1.4) 与原书逐符号一致，图 3.1–3.5 编号连续、图题均译自原书，Definition 1.1 / 1.2 与原书无 □ 的判定一致（`definition*` 正确），原书两处笔误（p.41 的 σ_n/σ^n 混用、p.42 的 "mu.st"）都已加批注并给出理由，未出现「只写疑有笔误」式空泛批注。

Lead 指定的两条额外重点，结论如下：
1. **4 条原书脚注（非我们的译注）**：花括号配平（`\footnote{}` 4 个开闭全对，内有 2 处 `\emph{}` 亦配对，无悬空）；4 条都落在与原书相同的句子之后（注 1→「…格的规则性得以保持。」；注 2→「…组合不等价。」；注 3→「…PL 流形 $M$ 成立。」；注 4→「…PL 结构与拓扑结构之间的关系。」）；脚注内无裸 ASCII 数学、无未加 `$` 的 `\cal`/`\mathcal`（全文 `\mathcal` 与 `\cal` 均为 0）。跨 p.44–45 的 Kirby–Siebenmann 长注虽跨页，但内容是逐句对译原书第 4 条脚注（"by other topologists…" 起为 p.45 页底续文），闭合 `}` 落在第 82 行，LaTeX 的脚注机制会把它整条排到当页页底，**位置正确**。
2. **`$` 配对**：全文 372 个 `$`，逐行统计无一行出现奇数个 `$`（即不存在跨行 `$…$`），起止全成对；`\xrightarrow` 未使用（0 处），不存在上下标写坏的问题。（Lead 提的第 56–60、176–177 行与当前文件对不上——现行文件共 123 行，我通篇按上述办法查，无跨行 `$`。）

## 必须改（影响正确性/体例）

1. **`\takeaway` 超长：第 10 行实测 202 字，超 STYLE_GUIDE 上限 120 字。** 现为「单纯复形是把连续对象离散化的最小装置……它们把拓扑问题化归为组合问题。」建议压缩为 1–2 句、保留四个要点（两条公理、重心重分、χ(K)、组合等价/单纯逼近）。另：全书各块 takeaway 长度不一（ch01 171、ch03b 168、ch03h 163、ch03i 227、ch04c 129……），若 Lead 决定放宽此上限，宜统一改 STYLE_GUIDE 并说明，避免逐块返工。
2. **第 89 行脱字（重字）：「但它通过一个同伦同伦于 $f$」**——连续两个「同伦」，句子读不通。原书 p.45："but homotopic to $f$ by means of a homotopy throughout which the motion of each image point is confined to a single simplex of $K_2$." 应改「但它与 $f$ 同伦，且该同伦过程中每个像点的移动都限制在 $K_2$ 的单个单形之内」（或「它通过一个同伦而与 $f$ 同伦，且……」）。
3. **页标记独占一行、落在句中，造成多余空格（2 处）**。
   - 第 80–82 行：`…一些困难已被` ⏎ `% [原文 p.45]` ⏎ `其他拓扑学家克服；…`。标记行独占一行时，TeX 换行产生一个空格，排版成「已被 其他」；STYLE_GUIDE 规定跨页句中途的页标记写在**上一行行尾**（注释吃掉行尾，不产生空格）。应把 `% [原文 p.45]` 移到第 80 行行尾。
   - 第 99–101 行：`…即满足 $H_1=$` ⏎ `% [原文 p.46]` ⏎ `$H_2=0$ 但…`。换行 + 页标记把两段行内公式隔开，排版成「$H_1=$ $H_2=0$」，等号后多一空格；且页标记嵌在公式中间。建议页标记移到第 99 行行尾、公式连写为 `$H_1=H_2=0$`（原书 p.45–46 该处正是 "with $H_1=H_2=0$ but with $\pi_1\ne0$"）。

## 建议改（可读性/文风/增益）

1. 第 12 行「最易于严格处理」：原书 "the most elementary, convenient, and most easily rigorous and cleanest means"，可作「最简单、最方便、最容易做到严格，也最干净」；现同句四个「最」并列，略拗。
2. 第 82 行「任何情形下……将在第 4 章 §5 末尾指出」：原书 p.44 末行是 "In any case for"，跨页到 p.45 "each $n\ge5$ …"。现整句放在 p.45 标记之后，逐页归属略偏（不影响正文）。若求严，可把「任何情形下，」留在 p.44 标记前。
3. 第 80 行脚注 4 的 Madsen–Milgram 书名按原书印作 *Classifying Spaces in Surgery and Cobordism of manifolds*（实际书名是 *The Classifying Spaces for Surgery and Cobordism of Manifolds*，作者顺序 Madsen, Milgram）。照排正确；若愿意方便读者，可在注末补半句说明原书此处书名/作者顺序与版权页略有出入。
4. 第 34–36 行的「1. … 2. …」列表在 ctex 下与正文行距略松（原书为行内 1./2.）；可改 `\begin{enumerate}` 之外的行内写法，或保留现状，不影响正确性。

## 抽查记录

- 逐页对照 pages\p047.png–p053.png（原书 p.40–p.46）：
  - p.40：第 3 章标题与 §1 标题「Simplicial complexes」对应正确；首段（Poincaré 引入、为同调/上同调提供最初等途径、但具体计算不便）全对。
  - p.41：σ_n 与 σ^n 混用已由第 19 行批注说明（原书确先写 σ_n 再写 σ^n）；(1.1) `$x\in\sigma^n,\ x=\sum x^j\alpha_j,\ \sum x^j=1,\ x^j\ge0$` 逐符号对；(1.2) `$\sigma_j^{n-1}=(\alpha_0,\dots,\hat\alpha_j,\dots,\alpha_n)$` 对；Fig 3.1 图内 (a) 0-dimensional、(b) 1-dimensional、(c) 2-dimensional、(d) 3-dimensional 与题注一致；单纯复形两条公理逐句对。
  - p.42：更一般复形（凸多面体/多胞形）与「合并」（consolidation）对；Remark 立方复形全段对；原书确印 "subdivisions mu.st be such as to preserve the regularity of the lattice in R^3"（`mu.st` 为排印脱字），第 51 行批注正确并给出理由；脚注 1「Novikov's problem, considered recently by N.P. Dolbilin, M.A. Stanko and M.I. Shtogrin」逐字相符；Fig 3.2 (a) I⁰…(d) I³ 与题注一致；(1.3) 对。
  - p.43：(1.3) 后 γ_j 定义、n 维、m 维骨架逐句对；重分与重心重分（点不重分、一维中点引入新顶点、再对 n 维单形按归纳法）逐句对；Fig 3.3 原书题注 "The barycentric subdivision of a simplex" 与译文题注「单形的重心重分」相符；Definition 1.1 原文 "combinatorially equivalent… isomorphic to a subdivision of each of them." 无 □，`definition*` 正确；Hauptvermutung 段起（Moise 1950 年代、Milnor ≥6 维）对。
  - p.44：Edwards 二重悬挂（同调 3 球面的二重悬挂同胚于 5 球面、其三角剖分与 σ⁶ 的边界组合不等价）逐句对；脚注 2 Freedman–Donaldson 对；不变量层次段（Alexander 1920 年代、Pontryagin 类积分由 Thom–Rohlin–Schwarz 定理组合定义、Reidemeister–Whitehead 挠；Novikov 1960 年代中期与 Edwards–Chapman 1970 年代）逐句对；Sullivan 理论（$H_3(M;\Z)$ 无 2-挠）与脚注 3（最初版本无限制、与 Browder/Novikov 1967 春讨论、"at least as of 1994"）对；Kirby–Siebenmann 段与脚注 4（含第 268–296 页、"do not seem to be complete independently of references to certain of Sullivan's results"）对。
  - p.45：脚注 4 续文（"by other topologists…"、Milgram–Madsen 书、1967 年尚未发展的工具）对；单形映射、单纯映射（由顶点像决定）、PL 映射（适当重分之间单纯、不必重心）逐句对；单纯逼近定理与其变体两版逐句对；Definition 1.2（组合邻域）对；可定向性定义（相邻 n 单形诱导的 (n−1) 面定向相反）对；「每个 PL 流形都是拓扑流形、但并非每个三角剖分都是 PL 流形」与 Edwards 定理引入对。
  - p.46：Fig 3.4 原书题注 "(a) The cone on K  (b) The suspension ΣK=(CK)₁∪(CK)₂" 与题注一致；锥（每点用区间连到 K 外新顶点）、悬挂 (1.4) `$\Sigma K=(CK)_1\cup_K(CK)_2$` 对；Fig 3.5 原书题注 "Subdivisions of cylinders on simplices" 与译文「单形上柱体的重分」相符；末段（楔和、映射柱、乘积经标准重分搬进单纯复形类）与原书末句逐字对，块止于 p.46 末句、p.47 顶端括注留给 ch03b，接缝正确。
- 公式编号：原书 (1.1)–(1.4) 共 4 个，文件实写 4 个 tag，无缺号、无重号、无自造编号。
- 图：原书 Fig 3.1–3.5 共 5 张，src\figures\fig3_1.png–fig3_5.png 全部存在且在正文按 3.1→3.5 递增；图题均译自原书，未把 "Fig." 行译进图内。
- 批注：9 条 % [Tutor Note]，逐条核对数学内容——σ_n/σ^n 记号说明、重心坐标、γ_j 计数与 χ 的取值（点 1、线段 1、圆周 0）、组合等价与同构之别、mu.st 脱字、拓扑不变量的层次、单纯逼近两版之别、组合邻域与重心重分的必要性、∪_K 的粘合与图 3.5——均正确；关于原书笔误的两条都给了理由。
- 术语：与 work\glossary.tsv 一致（simplicial complex 单纯复形、barycentric subdivision 重心重分、suspension 悬挂、skeleton 骨架、simplicial map 单纯映射、PL 流形/分片线性、orientable 可定向）；人名全用拉丁拼写（Poincaré、Euler–Poincaré、Alexander、Pontryagin、Reidemeister–Whitehead、Sullivan、Kirby–Siebenmann、Edwards、Chapman、Milnor、Moise、Browder、Novikov、Freedman、Donaldson、Milgram、Madsen、Hauptvermutung、Dolbilin/Stanko/Shtogrin）；未出现 monodromy「单值化」旧译，未出现「相交指标」误用。
- 自检：`python work\check_chunk.py src\chunks\ch03a.tex` → OK（页 40..46 共 7 页、tag 4、陈述 3、Tutor Note 9）；唯一 WARN 是「陈述环境 remark 编号为空」——原书 p.42 的 "Remark." 确无编号（斜体段首标号），判定正确；UTF-8/LF、末行 `% CHUNK ch03a DONE` 正常，页标记 40→46 递增无重复。
