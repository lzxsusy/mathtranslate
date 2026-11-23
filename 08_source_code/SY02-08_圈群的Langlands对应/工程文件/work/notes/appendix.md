# appendix 校订笔记（附录 A 李代数与泛包络代数，原书印刷 p.379–385 / PDF p.389–395）

## 一、交付概览

| 项 | 结果 |
|---|---|
| 正文文件 | `源码/chapters/appendix.tex`（本次唯一改动的源文件；未触碰 main.tex / preamble.tex / 其它章节） |
| 规模 | 306 行 → 308 行（12 条译注全部行内插入；新增 1 条 Tutor Note 注释占 2 行）；27638 → 35266 bytes；revision `03144b41f6420162507ac814ad59d590ea472a243e065414d7f95494202eb50d` |
| 编码/换行 | UTF-8 无 BOM，CRLF（Python 断言，未混入 LF） |
| 编号公式 | 1 个（`\tag{A.4-1}`，中心扩张正合列），`\tag` 逐字未动 |
| 定理环境 | `lemma` A.2.1、`theorem` A.2.2（PBW），未动；`\begin`/`\end` 各 11 个，配对 |
| `% [Tutor Note` | 22 → 23 条：原 22 条一条未删，新增 1 条（L200，登记 $h_i,h_i,f_i$ 笔误），补充 1 条旧注（L210，coroot→coweight） |
| keypoints | 5 组，未动 |
| 正式译注 | 12 条 `\transnote`：A 级 12 条、B 级 0 条、`[译者按（无外部依据）]` 0 条 |
| 改动条数 | 18 条 = 正文文字 4（中文 3、术语 1）＋ 译注 12 ＋ 源码 Tutor Note 2（新增 1、补充 1） |
| 公式改动申请 | **无**（详见第五节） |

## 二、改动分类（正文文字 4 处，行号为改后）

**中文 3 条**

1. L20（原书 p.379）：`李代数是带双线性形式（即李括号）的向量空间` → `李代数是带双线性运算（即李括号）的向量空间`。中文里"双线性形式"通常指标量值双线性型（如 Killing 型、Cartan 型），而李括号取值于 $\mathfrak g$；"运算"更准确，也与本节后文的"双线性运算"一致。
2. L147（原书 p.383，keypoints）：`余根格 $\check Q$ 与 外尔群 $W$ 由根数据决定` → `余根格 $\check Q$ 与外尔群 $W$ 由根数据决定`（多余空格）。
3. L222（原书 p.383）：`与 $\mathfrak g$ 相伴的 外尔群 $W$` → `与 $\mathfrak g$ 相伴的外尔群 $W$`（多余空格）；同句挂译注 #8。

**术语 1 条**

4. L108（原书 p.381）：`取商的伴随分次代数相当容易` → `取商的分次伴随代数相当容易`。`glossary.tsv` 第 126 行定为「分次伴随代数」（associated graded algebra），与 L104 及相邻口吻一致。

**旧译已修、本次只登记、未回溯改动的原书笔误**（不计入 18 条）

- `want want`（p.380，旧注 B004 记已修，今 L73）；`This gives is`（p.385，旧注 B021 记已修，今 L306）；`h_i,h_i,f_i`（p.383，旧译静默改为 `h_i,e_i,f_i`，本次补可见译注 #5 与 Tutor Note L200）。

## 三、译注 12 条（格式：序号｜行号｜类型｜一句话卡点｜来源｜级别｜旧注行号）

| # | 行号 | 类型 | 一句话卡点 | 来源 | 级别 | 旧注行号 |
|---|---|---|---|---|---|---|
| 1 | 112 | 易错 | $\operatorname{gr}F\cong F$ 的"并非典范"指须在每个 $F_{\le i}$ 中选 $F_{\le i-1}$ 的补空间/代表元；$\operatorname{Symb}(I)$ 取每个元素的最高次部分 | 原书 p.381 | A | 114（B006） |
| 2 | 140 | 易错 | 定理 A.2.2 的 $a_1\le\cdots\le a_n$ 是弱递增（允许相等）；"按字典序排列"指固定有序基 $\{J^a\}$ 后的不降序列 | 原书 p.381 定理 A.2.2 | A | 138（B008） |
| 3 | 153 | 背景 | "正定"排除双曲型；正定对应半单，"单"还须矩阵不可分解（Dynkin 图连通）；本书约定 $a_{ij}=\alpha_j(h_i)=\langle\alpha_j,\alpha_i^\vee\rangle$，Dynkin 图按 $a_{ij}a_{ji}=4\cos^2(\pi/m_{ij})$ 连边 | 原书 p.382（原文即引 [Kac 1990]）；Kac 1990, Ch.4 | A | —（新增） |
| 4 | 153 | 原文笔误 | 应作 $a_{ij}=0$ 当且仅当 $a_{ji}=0$（原书印作 $a_{ji}\neq0$，与 $a_{ij}\le0$ 合看自相矛盾）；例外型应为"五个"（同段只列 $E_6,E_7,E_8,F_4,G_2$） | 原书 p.382 同段；Kac 1990 引言（广义 Cartan 矩阵 $a_{ij}=0\Rightarrow a_{ji}=0$）与 Ch.4 | A | 155、157（B009+B010 合并） |
| 5 | 198 | 原文笔误 | 原书"由 $h_i,h_i,f_i$ 生成"，第二个 $h_i$ 应为 $e_i$（译文按 $e_i$）；"重新标度 $e_i$（或 $f_i$）"的原因是 $[e_i,f_i]$ 可能只是 $h_i$ 的非零倍数 | 原书 p.383；Kac 1990, Ch.1（由 $h_i,e_i,f_i$ 与 Serre 关系定义 $\mathfrak g(A)$） | A | —（新增；另新增 Tutor Note L200） |
| 6 | 206 | 背景 | 四个格是根数据的具体化：$P,\check P$ 对应 §1.1.5 的 $X^*(T),X_*(T)$，$Q,\check Q$ 由单根/单余根张成；两侧分居 $\mathfrak h^*/\mathfrak h$，对偶群交换 $P$ 与 $\check P$（$\mathrm{SL}_n\leftrightarrow\mathrm{PGL}_n$） | 原书 p.5–6、p.383；并见本版 §1.1.5 译注 | A | 210、214（B014+B015 合并） |
| 7 | 208 | 原文笔误 | 原书主语 "The coroot lattice" 应为 coweight lattice：余根格已定义为 $\check Q=\operatorname{span}_{\mathbb Z}\{h_i\}$，满足 $\alpha_j(\check\omega_i)=\delta_{i,j}$ 的元素是基本余权；公式左端应为 $\alpha_j(\check\omega_i)$（原文两处指标都写 $i$，与 $\delta_{i,j}$ 不闭合） | 原书 p.383（同页上一段的四格定义）；并见本版 §1.1.5 | A | 208（B013；主语错误为本版新发现） |
| 8 | 222 | 易错 | $\check\alpha_i$ 是单余根的另一种写法，即 $\check\alpha_i=h_i=\alpha_i^\vee$，并非基本余权 $\check\omega_i$；检验 $s_i(\alpha_i)=-\alpha_i$、$s_i(\alpha_j)=\alpha_j-a_{ij}\alpha_i$ | 原书 p.383；Kac 1990, Ch.6（Weyl 群与根系统） | A | —（新增） |
| 9 | 240 | 易错 | "$\mathfrak a$ 在 $\hat{\mathfrak g}$ 中中心"严格说要求 $[\mathfrak a,\hat{\mathfrak g}]=0$，原书只验 $x\in\mathfrak g$ 已足够；分裂 $\hat{\mathfrak g}\cong\mathbb C\mathbf 1\oplus\mathfrak g$ 并非典范 | 原书 p.383–384；并见本节后文对同构类的分类 | A | 240（B016） |
| 10 | 265 | 背景 | 对半单（特别单）李代数 Whitehead 引理给出 $H^2(\mathfrak g,\mathbb C)=0$，故 A.4 的一维中心扩张对 $\mathfrak g$ 本身只给平凡扩张；真正的用武之地是 §A.5 圈代数 $L\mathfrak g=\mathfrak g\otimes\mathbb C[t,t^{-1}]$ | 原书 p.384；并见 §A.5 与第 2 章 | A | 265（B018） |
| 11 | 302 | 易错 | 式 (1.3-3) 具体为 $c(x\otimes f,y\otimes g)=\kappa(x,y)\operatorname{Res}_{t=0}(f\,dg)$；$\kappa$ 的不变性保证 $c$ 是李代数 2-上循环（Jacobi 的中心项），反称性给出 $c$ 反称 | 原书 p.385（引式 (1.3-3)，见原书 §1.3）；Kac 1990, Ch.7（仿射代数作为圈代数的中心扩张） | A | 253（B017） |
| 12 | 304 | 背景 | 附录未给 $\kappa$ 归一化：第 2、3 章取 $\kappa_0$ 使长根平方长 2，$\kappa=k\kappa_0$，$h^\vee=1+\langle\rho,\theta^\vee\rangle$（$\mathfrak{sl}_n$ 为 $n$、$\mathfrak{sl}_2$ 为 2），临界 $\kappa_c=-h^\vee\kappa_0\iff k=-h^\vee$，中心荷 $c=k\dim\mathfrak g/(k+h^\vee)$；不固定归一化则 $k,h^\vee,\kappa_c$ 无从谈起 | 原书 p.38 式 (2.1-10)–(2.1-11)、p.63–64；Kac 1990, Ch.6（标准化不变型、对偶 Coxeter 数与 $\rho$） | A | 306（B022） |

补充两条源码注释（不计入 12 条译注）：

- **L200 新增 Tutor Note**：登记原书 p.383 的 $h_i,h_i,f_i$ 笔误与旧译的静默修正，与 L198 译注呼应。
- **L210 补充旧 Tutor Note**：原注只说"公式应为 $\alpha_j(\check\omega_i)=\delta_{i,j}$"，仍把对象称"余根格生成元"；追加说明原书主语 "The coroot lattice" 亦误，应为余权格 $\check P$。原注文字未删。

旧注处置统计：22 条中 **11 条升级**为 9 条译注（B006、B008、B009、B010、B013、B014、B015、B016、B017、B018、B022），**11 条保留未升级**（B001、B002、B003、B004、B005、B007、B011、B012、B019、B020、B021），另新增 3 条独立译注（#3、#5、#8）。B019（旧注 L290，诊断报告标"可删"）按任务书"Tutor Note 可补充不可删"保留，未升级。

## 四、原书笔误台账（6 条原书笔误 + 1 条旧注勘误）

| # | 原书页 | 原文（照录） | 应为 | 处置 | 页图依据 |
|---|---|---|---|---|---|
| 1 | p.380 | "we clearly want want the corresponding $T(\mathfrak g)$-module" | 单个 want | 旧译只译一次（B004 已修）；不设可见译注（纯重复词，不影响数学） | p390 整页 + 2x 裁切 |
| 2 | p.382 | "$a_{ij}=0$ if and only if $a_{ji}\neq0$" | $a_{ji}=0$ | 保留原文 + 译注 #4 | `p392_top.png`（3x）、`p392_a.png` |
| 3 | p.382 | "four infinite families and six exceptional ones"（同段只列 $E_6,E_7,E_8,F_4,G_2$） | five | 保留原文 + 译注 #4；keypoints（L145）已写"五个例外型" | `p392_top.png`、`p392_a.png` |
| 4 | p.383 | "generated by $h_i,h_i,f_i$" | 第二个 $h_i$ 应为 $e_i$ | 译文按 $e_i$（旧译静默修正，公式未动）+ 译注 #5 + Tutor Note L200；**U18 未收，本版新发现** | `p393_top.png`（3x） |
| 5 | p.383 | "The coroot lattice is spanned by elements $\check\omega_i\in\mathfrak h$ defined by the formula $\alpha_i(\check\omega_i)=\delta_{i,j}$" | "The coweight lattice" 且 $\alpha_j(\check\omega_i)=\delta_{i,j}$ | 保留字面 + 译注 #7 + 旧注 L210 补充；**主语错误 U18 未收，本版新发现**；指标错误 U18 已收 | `p393_cow_full_6x.png`、`p393_cow_formula_10x.png`、`p393_lat2/3.png` |
| 6 | p.385 | "This gives is the formal loop algebra" | "This gives the formal loop algebra" | 旧译已处理（B021 已修）；不设可见译注 | p395 整页 |
| 7 | （旧注勘误，非原书） | 旧注原句把满足 $\alpha_j(\check\omega_i)=\delta_{i,j}$ 的元素称为"余根格生成元" | 应为基本余权，张成余权格 $\check P$ | 旧注 L210 追加一句说明，原文未删 | 同 #5 |

## 五、公式改动申请

**无。** 理由：

1. 附录全部数式与页图逐条核对，旧译转写无误，无需申请改动，也未写 `formula-fixes.tsv`。
2. 唯一曾被怀疑的 p.383 公式 $s_i(\lambda)=\lambda-\langle\lambda,\check\alpha_i\rangle\alpha_i$，经 16 倍裁切页图（`p393_sym16.png`）确认中间符号是 **$\check\alpha_i$（α 上加 caron，单余根的另一种写法 $=h_i=\alpha_i^\vee$）**，不是 $\check\omega_i$；旧译 `\check\alpha_i` 正确，保持不动。
3. 其余数式（张量代数直和分解、PBW 单项式 $J^{a_1}\cdots J^{a_n}$、`\tag{A.4-1}` 正合列、中心扩张括号与 2-上循环条件、$L\mathfrak g$ 括号、引用的 (1.3-3)）均逐字比对页图，未改动。

## 六、页图清单

页图目录：`C:\Users\admin\Documents\deepseek-harness\default-workspace\frenkel-loop\pages\pNNN.png`（875×1344，约 112 dpi）。放大裁切文件（Pillow 4x–16x）在 `C:/Users/admin/Downloads/appx_crops/`。

| PDF 页 | 印刷页 | 核读内容 | 裁切文件 |
|---|---|---|---|
| p389 | 379 | A.1 李代数定义、括号反称与 Jacobi、表示、"bilinear form"、A.2 起首 $T(\mathfrak g)$ | 整页读图 |
| p390 | 380 | "want want" 笔误、泛性质交换图、PBW 滤过链、$U(\mathfrak g)\cong\operatorname{Sym}(\mathfrak g)$ | 整页 + 2x |
| p391 | 381 | $\operatorname{gr}F$ 定义、非典范同构、$\operatorname{Symb}$ 取首项、Lemma A.2.1、Theorem A.2.2（弱递增、字典序） | 整页 + 2x |
| p392 | 382 | A.3 分类段逐字：positive definite、$a_{ii}=2$、$a_{ij}\le0$、$a_{ij}=0$ iff $a_{ji}\neq0$、four families + six exceptional、Cartan 分解 | `p392_top.png`（3x）、`p392_a.png`、`p392_b.png`（2x） |
| p393 | 383 | $h_i,h_i,f_i$、Serre 关系与三组括号、$\mathfrak{sl}_{n+1}$ 例、四格、coroot lattice 句、$s_i$ 公式 | `p393_top.png`（3x）、`p393_lat2.png`/`p393_lat3.png`（4x）、`p393_cow_full_6x.png`、`p393_cow_formula_10x.png`、`p393_sym16.png` |
| p394 | 384 | A.4 中心扩张、正合列、分裂与括号、2-上循环、$H^2$；A.5 起首 | 整页 + 2x |
| p395 | 385 | 圈代数、$H^2(L\mathfrak g,\mathbb C)$、公式 (1.3-3)、$\hat{\mathfrak g}^{\mathrm{pol}}_\kappa$、形式圈、留数、$\hat{\mathfrak g}_\kappa$ | 整页 + 2x |

备注：PDF p396–p401（印刷 p387–392）为 `bibliography.tex`，不属于本附录，未纳入作业范围。

## 七、自检清单

- `\transnote{`：12 条（脚本解析计数）；每条 ≤4 句（最长 4 句）；均紧跟被注句末、未进入数学环境（`\[...\]` 之外）。
- `% [Tutor Note:`：23 条（原 22 条全部保留 + 新增 1 条）；原 22 条行号 31,35,43,73,75,114,126,138,155,157,173,188,210,212,216,242,255,267,292,300,306,308 未删（旧注 208→210 因新增两行整体后移），新增在 L200。
- `\tag{A.`：1 个（A.4-1），未动；`\tag` 总数不变。
- 环境：`\begin{` 11 / `\end{` 11；`lemma`/`theorem`/`keypoints` 均配对。
- `$` 配对：未转义 `$` 1096 个（偶数）；花括号净差 0；无 `\\transnote`（双反斜杠误写）0 处。
- 编码：UTF-8 无 BOM；换行全为 CRLF（未混入 LF）。
- 范围：仅改 `源码/chapters/appendix.tex`；main.tex / preamble.tex / 其它章节未动；未编译（任务要求）。

## 八、遗留问题与说明（诚实）

1. **页范围更正**：任务书写「PDF p.389–p.401、印刷 p.379–p.391」；实测附录 A 正文只到 PDF p.395 = 印刷 p.385，PDF p.396–401 是 `bibliography.tex` 的参考文献页，且 STYLE_GUIDE.md:88 的六段偏移表为 PDF 261–395 → −10、396–401 → −9。本笔记与 brief 均按实际 7 页（p.389–395）说明；未改其它文件。
2. **两处原书笔误为本版新发现、U18 未收**：p.383 的 "generated by $h_i,h_i,f_i$"（第二个应为 $e_i$）与 "The coroot lattice"（应为 coweight lattice）。已在正文加可见译注（#5、#7）并补 Tutor Note 登记/补充。建议 U18 报告在下一轮补收此两条。
3. **Zbl 号缺小数点（U18）**：`Zbl 02121180`、`Zbl 01886039` 应为 `Zbl 0212.1180`、`Zbl 0188.6039`。该两条属参考文献条目、不在本章正文，按任务书只在笔记记录，正文未动。
4. **旧注 11 条未升级**（B001/B002/B003/B005/B007/B011/B012/B019/B020/B021 及已修的 B004）：或已被 keypoints/相邻译注覆盖，或与相邻译注内容重叠；为控注密度保留为源码注释，未删。B019 虽诊断报告标"可删"，按任务书"可补充不可删"保留。
5. **译注 #9 来源页写 p.383–384**：A.4 标题在印刷 p.383 页末，定义续至 p.384，故取跨页。
6. **未编译**：按任务要求未运行 LaTeX；所有校验均为静态脚本 + 页图人工核对。
7. 术语核对：本章未出现 "unipotent"（幂幺规则未触发）；"residue" 译"留数"（L302 起）、"Weyl" 译"外尔群"、"cocycle/coboundary" 译"上循环/上边缘"、"associated graded" 译"分次伴随代数"，与 glossary.tsv 一致。
