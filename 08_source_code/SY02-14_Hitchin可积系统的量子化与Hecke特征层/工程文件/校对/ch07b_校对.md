# 第 7 章后半（p.296–p.366）校订报告

- 校订对象（本人所有，仅动这 7 个文件）：`源码/units/ch07_u07.tex`（p.296–305，415 行）、`ch07_u08.tex`（p.306–315，184 行）、`ch07_u09.tex`（p.316–325，193 行）、`ch07_u10.tex`（p.326–335，167 行）、`ch07_u11.tex`（p.336–345，197 行）、`ch07_u12.tex`（p.346–355，176 行）、`ch07_u13.tex`（p.356–366，216 行）
- 依据：页面图像 `工程文件/work/pages/p296.png`–`p366.png`（1445×1870，整页预览 1125×1456 可读）；公式与字形一律以图像为准，文本层 `工程文件/work/en/pNNN.txt` 只用于查词与散文对照（Fraktur/花体码位、⊗̂ 等一律回查图像或按原书符号逻辑复核）
- 对照简报：`工程文件/reports/ch07_u07.md`–`ch07_u13.md`（仅作线索，结论一律自行对图核对）
- 结论：**改动 4 处（P1×2、P2×2）**，均为行内替换或新增一条 Tutor Note，未增删正文行；编译 `grep -c "^!" main.log` = **0**

## 一、已核对范围

| 单元 | 原书页 | 内容 | 核对方式 | 结论 |
|---|---|---|---|---|
| u07 | p.296–p.299 | 逆向态射；7.10.21 注；7.10.22 引理与证明（含脚注「并且当然，仅当」）；7.10.23(i)(ii) 与脚注；7.10.24 定义、$\mathcal{C}$-扭晶体函子性、$\mathcal{C}^{triv}$、$X_{\text{ét}\,cr}/X_{Zar\,cr}$；7.10.25；(344)；7.10.26 引理、7.10.27、7.10.28（tdo 与晶体 gerbe）；(345) | 逐页读图 | 无改动 |
| u07 | p.300–p.305 | (346)(347)；7.10.32 命题（「(347) 是右幺作用」）；7.11 节头；7.11.1（严格意义下的归纳概形、$\aleph_0$-归纳概形、归纳-$P$ 性质）；注与既约/形式概形/完备化；形式光滑、合理子概形；7.11.2(i)(ii)(iii)；7.11.3 $\mathcal{O}^p$-模（脚注 p=投射极限）；注 (i)(ii)；7.11.4 $\mathcal{O}^!$-模；7.11.5 $K$-等变；7.11.6 | 逐页读图 | 无改动 |
| u08 | p.306–p.315 | 7.11.7 (348)(349)；7.11.8 命题 (350)(351) 与 $\operatorname{Sym}^\cdot\to\Gamma^\cdot$ 脚注；$\sigma_n$ 证明；7.11.9 Diff-双模/幺半范畴、注 (i)(ii)、Diff-代数、$D^!$-模、$\Gamma(X,D)$；弱 $K$-作用；7.11.10 层论看法 (i)(ii)、Diff-代数数据；7.11.11 关键例子 $\mathcal{D}(\mathcal{O}_Y):=\varinjlim\operatorname{Diff}(\mathcal{O}_{Y'},\mathcal{O}_Y)$；扭版本 a./b.、$\mathcal{D}_{\mathcal{L}}$、$\mathcal{D}_{\mathcal{L}^h}$、$h=-t\,d/dt$；7.11.12 $\Omega$-复形、$f^{\cdot}_\Omega$；7.11.13 (352)(353)；7.11.14 拟紧支撑 | 逐页读图（$f^{\cdot}$ 的上标点 8× 放大确认） | 无改动 |
| u09 | p.316–p.317 | 7.11.15(iii)、7.11.16 推前 $f_{\cdot}$（点确实在下标，与 p.316 图一致）、积分态射 $i_f$、7.11.17 Hecke 幺半范畴；7.11.18 $U_i$、$\mathcal{B}=K\backslash Y$、$(F_n\circledast T)_i$ 与 $(F_n\circledast T)'_i$、Cone 式 | 逐页读图（$\bar m_{U_i}$、$\dot p_{U_i\Omega}$ 均 10× 放大） | **2 处 P1（问题 1）** |
| u09 | p.318–p.325 | 7.12 节头；7.12.1–7.12.3；7.12.4；(354)(355)；7.12.6(i)(ii)(iii)；(i)(ii) 与三条证明段；7.12.7；7.12.8 定理（Raynaud–Gruson）；Remark 与「$F\subset A$ 应为 $S$」脚注；另一证明 $0\to\mathcal{P}\xrightarrow{1-f}\mathcal{P}\to P\to 0$ 与 Arinkin 脚注；7.12.9–7.12.11；7.12.12–7.12.14（含「subshemes」原样）；7.12.15；7.12.16 与「stritly」原样；7.12.16 证明 (a)–(d)；7.12.17 与 (356) | 逐页读图 | 无改动 |
| u10 | p.326 | 脚注（$H^2$ 论证）续；「defining ideals (English?)」句；7.12.18 命题、注、证明起 | 逐页读图 | **1 处 P2（问题 3，新增批注）** |
| u10 | p.327–p.335 | (357)–(364)；7.12.19 例；7.12.20 命题与证明；7.12.21 (0)(i)(ii)（$R_{mn}$ 原书确印 $[[x_{m+n},\dots,x_{m+n}]]$）；7.12.22 命题、引理、证明；7.12.23 命题、引理 (361)(362)、$\tilde X=X_0\times Y$；7.12.24 (a)(a′)(a″)(b)(c)(d)（含 $f_{ni}\in\operatorname{Ker}(A_{n+2}\to A_2)$、$\tilde l':M\to K_{\mathfrak{p}}$ 两处原书笔误） | p.327/328/330/331/334 文本层逐句；p.329/332/333/335 读图 | 无改动 |
| u11 | p.336–p.337 | 7.13 节头（「redundand」原样）；7.13.1（$\mathrm{Cl}^\cdot$ 直立 vs $\mathcal{C}l^\cdot$ 花体，滤链、$\operatorname{gr}$、$E^{\flat}=\operatorname{End}^{\flat}_F:=\mathrm{Cl}^0_1$）；注 (i)(ii)；7.13.2（$\mathcal{A}^\cdot=\mathcal{C}l^\cdot\otimes\mathcal{R}$、$\mathcal{L}ie$、$i^c_n$） | 逐页读图（两种 Cl 字形对照） | 无改动 |
| u11 | p.338–p.345 | 7.13.3 引理与证明；注 $\mathfrak{n}_{\heartsuit}$；7.13.4–7.13.5；(365)(366)；7.13.6–7.13.8（「It suuffices」批注）；注（$\mathrm{Cl}_i\otimes R/\mathrm{Cl}_{i-1}\otimes R$）；7.13.9–7.13.15；(367)–(370)；7.13.16–7.13.17（$\overline{\mathrm{Cl}}$ 与 $\overline{\mathcal{C}l}$）；7.13.18（$E_\pm$、$E_{tr}$、$\operatorname{tr}$） | p.345 读图；p.338/340/343 文本层逐句，其余按 7.13.1–7.13.2 已定字形规则复核 | 无改动 |
| u12 | p.346–p.355 | 7.13.18 末（迹的良定义、$s_\pm$、(373)、注 (i)(ii)(iii)）；7.13.19（$F'$、$F^{\circ}$、$K\widehat{\otimes}K$、(374)、(375) 前后）；7.13.20 引理、证明、Parshin 留数脚注；$\overline{\mathrm{Cl}}_F$ 的拓扑；7.13.21–7.13.22；7.13.23–7.13.24；7.13.25（原书残句）；7.13.26–7.13.27（$C_{\mathfrak{g}}(V)$、(375)、(376)、$\lambda_A$）；7.13.28–7.13.30；7.14 节头、7.14.1–7.14.3 | p.355 读图；p.346/347/348/349/351/354 文本层逐句 | 无改动 |
| u13 | p.356–p.359 | $\omega_{K\backslash Y}$、 (378)、$\lambda_{\mathfrak{k}}$、$C_Y^{\cdot}$ 存在唯一、$G$-作用；注（原书两处 $C_y^{\cdot}$ 的笔误已在原位）；7.14.4–7.14.6：(379)；7.14.7 注（「filtrartion」原样）与 (380)；7.14.8 引理 (381)(382) 与证明、(383)；7.14.9 例（原书括号不配对）；7.14.10 | 逐页读图（p.356 的 $C_y^{\cdot}$ 两处 10× 放大；p.358 (380) 的 $\omega_{(K\backslash Y)}$ 放大） | **1 处 P2（问题 2）** |
| u13 | p.360–p.366 | 7.15 节头；7.15.1（两处「??」引用）；7.15.2–7.15.4：(384)(385)(386)；7.15.5（(i)(ii)(iii)）；7.15.6；7.15.7（$\Gamma\mathcal{D}^{\chi\circ}$ 原样）；7.15.8 定理、注；7.15.9–7.15.13（(388)–(391)）；7.15.14–7.15.17（(i) 与 Schubert 分层、7.15.15、证明中的 7.15.7(iii) 原样） | p.360 读图；p.361/362/363/364/365/366 文本层逐句 | 无改动 |

核对方式说明（据实登记）：本次共 **43 页逐页读图**（p.296–p.326、p.329、p.332–p.333、p.335–p.337、p.345、p.355–p.356、p.358–p.360），其余 28 页（p.327–p.328、p.330–p.331、p.334、p.338–p.344、p.346–p.354、p.357、p.361–p.366）以 OCR 文本层逐句对照原文散文，公式与符号逐个回读译本（凡可疑处一律回查图像，例如 p.324「stritly」、p.356 两处 $C_y^{\cdot}$、p.358 (380) 的括号、p.317 m̄/ṗ 的上标点）；未发现仅凭文本层导致误判的情形。

## 二、问题清单

| # | 位置 | 原文（p.317） | 原译 | 改为 | 理由 |
|---|---|---|---|---|---|
| 1 | `ch07_u09.tex:36` | $(F_n\circledast T)_i:=\bar m_{U_i}\cdot\dot p_{U_i\Omega}(F_n\boxtimes T_{j(n,i)})|_{\mathcal{B}_i}$ | `\bar m_{U_i}\cdot p_{U_i\Omega}(…)` | `\bar m_{U_i}\cdot p^{\cdot}_{U_i\Omega}(…)` | 原书两处 $p$ 都带上标点（$p^{\cdot}_{U_i\Omega}$，与 7.11.12 的 $f^{\cdot}_\Omega$ 同一记法），译文漏掉上标点。**P1（公式符号漏上标）** |
| 2 | `ch07_u09.tex:40` | 同上，(357) 的 $'$ 版 | 同上 | 同上 | 同一算式第二处，一并改。**P1** |

| # | 位置 | 原文（p.356） | 原译 | 改为 | 理由 |
|---|---|---|---|---|---|
| 3 | `ch07_u13.tex:20` | an irreducible graded $\mathrm{Cl}^{\cdot}_{\mathfrak{g}}$-module（直立 Cl） | `\operatorname{Cl}^{\cdot}_{\mathfrak{g}}` | `\mathrm{Cl}^{\cdot}_{\mathfrak{g}}` | 全工程 Clifford 记号约定为「直立 `\mathrm{Cl}`（量子/准经典）、花体 `\mathcal{C}l`（经典分次）」，u11/u12 共 74 处均作 `\mathrm{Cl}`；u13 仅此 1 处用 `\operatorname{Cl}`，渲染结果虽同，但源码记号不统一。**P2（记号源不统一）** |

| # | 位置 | 说明 | 处理 | 理由 |
|---|---|---|---|---|
| 4 | `ch07_u10.tex:11`（新增一行 `%` 注释） | 原书 p.326 正文即印作 "a fundamental system of “defining ideals (English?)” (“Idéaux de définition”; see EGA I 10.5.1)"，括号里的 `(English?)` 是作者对英文术语的夹注，不是译者残留 | 正文照录不动，其后新增 1 条 Tutor Note 说明 | 译本原有读起来像未清理的占位符；按「原书笔误照录 + 批注」的既定处理补注，不改正文。**P2（缺批注，易被误读为漏译）** |

合计：**P1×2、P2×2，共 4 处**。均为行内替换 / 新增注释行，未增删正文段落，未改任何 `\SourcePage`、`\bdp`、`\bdsec`、`\tag`、label、Tutor Note 的既有内容。

## 三、未改动但存疑

1. **`ind-finite type` 保留英文**（u08 行 7/12/99/107、u09 行 121/124/132、u10 行 14/16、u13 等处），而 u07 行 253/407 译作「归纳有限型」，与本段其余页面上的「ind-affine」「ind-quasiquasi-compact」「pro-algebra」等拉丁写法为伍。若统一译成中文，需在 7 个文件里改 30 余处，属**文风层面的整体取舍**，超出单条 P1/P2 的改法，故**未动**，交总校裁定（见「需裁定」1）。
2. **«N 是其幂幺根»（p.360，u13 行 91）** 原书作 "Let $N\subset B\subset G$ be a Borel subgroup and its radical"，只说 radical；译文补了「幂幺」。数学上 Borel 的根即幂幺根，不产生歧义，但严格说是加词。属可改可留的小差异，**未动**。
3. **$\omega$ 的括号两套写法**：p.355 与 (378)(380) 原书印 $\omega_{(K\backslash Y)}$（带括号），p.356 首句、p.357 的 $\omega^{\ast}_{(K\backslash Y)}$、p.358 的 (383) 以后各处印 $\omega_{K\backslash Y}$（不带）。译本 u12 行 175 / u13 行 12/16/36/49 与 u13 行 8/64/70/72 已逐处对应原书，**不是译本内部的不一致，故未统一**（见「需裁定」2）。
4. **u12 行 111（p.351）** 原书 "We assume that $\mathcal{R}$ is complete and separated and topology." 本身就是残句，译本照录作「……且是拓扑。」读起来别扭；已由译者原批注说明，按照录原则**未动**。
5. **p.321（u09 行 16 批注）「有限 $F\subset A$」**：原书脚注前文设的是不可数集 $S$，此处印作 $A$；译本照录并加批注，**未动**（批注引文与图一致，已核）。
6. **p.324「stritly」**：原书确印 `stritly`（10× 放大确认），译者批注亦作 `stritly`，两者一致，**未动**。
7. **p.356 两处 $C_y^{\cdot}$**：原书确印 "The fiber $C^{\cdot}_y$ of $C^{\cdot}_y$ at $y$"（第二处应为 $C^{\cdot}_Y$，10× 放大确认），译本照录并批注，**未动**。
8. **u13 行 89/139 的「??」**：原书 p.360 两处、p.362 一处交叉引用未解析，印作「??」；行 89 已有批注，行 139（「7.15.8--??」）无批注但正文照录，**未动**。
9. **p.362「explicitely」、p.345「homogenuous」、p.353「homoguenous」、p.336「redundand」、p.347「agebra」、p.350「where natural」、p.340「suuffices」、p.358「filtrartion」**：均已在译本对应处批注（本次逐条对图复核，批注引文无误），**未动**。
10. **$D^{\flat}_i\subset\overline{\mathrm{Cl}}_F$（u12 行 56）**：p.349 该处 OCR 只给出 "Cl_F"，无法判读上划线；按 7.13.17（p.345）确立的 $\overline{\mathrm{Cl}}$ 记法与上下文（$D^{\flat}_i$ 的自然 Tate 拓扑来自完备 Clifford 代数），保留 `\overline{\mathrm{Cl}}_{F}`，**未动**。

## 四、术语与记号一致性

- **Clifford 记号（本次重点核对）**：原书 p.336–p.337 逐字放大对照确认——量子/准经典 Clifford 代数印**直立** $\mathrm{Cl}$（`\mathrm{Cl}^{\cdot}`、`\mathrm{Cl}^{\cdot}_i`、`\mathrm{Cl}^{0}_1`、$\mathrm{Cl}_F$、$\overline{\mathrm{Cl}}^{\cdot}$），经典（分次）Clifford 代数印**花体** $\mathcal{C}l$（`\mathcal{C}l^{\cdot}`、`\mathcal{C}l^{\cdot}_i=\operatorname{gr}_i\mathrm{Cl}^{\cdot}$、$\mathcal{C}l^{0}_1$、$\overline{\mathcal{C}l}^{\cdot}$、$\overline{\mathcal{C}l}^{a}_{i}$）。核对结果：u11 共 86 处、u12 共 19 处、u13 共 1 处，**逐处与图对应无误**，仅 u13 行 20 的 `\operatorname{Cl}` 改为 `\mathrm{Cl}`（问题 3），全章统一为含 0 处 `\operatorname{Cl}`。✓
- **p.345 的一处原书自相矛盾照录**：「置 $E^{\flat}:=\overline{\mathcal{C}l}^{0}_1$；这是 $\mathrm{Cl}^{\cdot}$ 的李子代数……」原书此处确印无上划线的直立 Cl（图已核），译本照录，未擅改。✓
- **迹**：全部 `\operatorname{tr}`（u12 行 9/11/13/20/22/24/33 与 u11 行 196），与原书直立 "tr" 一致；无 `\tr`、无 `\operatorname{Tr}`。✓
- **$\otimes$ 的三类**：普通 `\otimes`、完备化 `\widehat{\otimes}`（u12 行 40/42/44/45/53、u11 行 170/183 等，原书均印 $\widehat{\otimes}$）、分次外积 `\boxtimes`（u09 行 36/40，原书 $\boxtimes$）、Hecke 卷积 `\circledast`（u09 行 36/40/42/43 等 6 处，原书 $\circledast$）——逐处与图一致。✓
- **$\flat$ / $\natural$ / $\heartsuit$ / $\dagger$**：$\flat$（$E^{\flat}$、$\mathfrak{n}^{\flat}$、$\mathfrak{k}^{\flat}$、$\mathfrak{b}^{\natural}$、$\mathfrak{n}_{\heartsuit}$、$X^{\dagger}$、$B^{\dagger}$）均按原书字形；u13 的 $\natural$（$\mathfrak{b}^{\natural}$、$\mathfrak{h}^{\natural}$、$U^{\natural}\mathfrak{h}$）与 $\dagger$ 区分正确。✓
- **等号族**：原书 $\simeq$ 处译本 `\simeq`（如 u13 行 16/21/206、u12 行 155、u10 行 78 的 $\simeq$）；原书 $\cong$ 处沿用 `\cong`（u12 行 24）；原书 $=$ 处不升级为 $\simeq$。u09 行 197 `\simeq`、u10 多处按原书保留。未发现 ≅/≃/= 混用。✓
- **$\subset$ / $\subseteq$**：原书一律 $\subset$，译本 `\subset`，本 7 个文件**无** `\subseteq`。✓
- **半直积 / loc / glob**：`\ltimes`、`^{\mathrm{loc}}`、`^{\mathrm{glob}}` 在本人 7 个文件内**出现 0 次**（属其他单元范围），无需处理。✓
- **箭头**：`\to`（一阶）、`\hookrightarrow`（闭/开嵌入）、`\twoheadrightarrow`、`\xrightarrow{\sim}`（同构）与原书逐处对应；u10 行 89 的 `\twoheadrightarrow`、u12 行 18 的 `\xrightarrow{(-,+)}` 与原书一致。✓
- **术语**：D-模（不写 D-module）、扭微分算子（tdo 首次出现处保留 tdo 缩写）、象征、滤链、伴随分次、完整、局部系统、Hecke 特征层、oper、torsor、gerbe、归纳概形、形式概形、凝聚、开有界李子代数、半无限、c-格、Mittag-Leffler（不译）、Baer 和、Harish-Chandra 对、反占优（anti-dominant）——均与 `工程文件/work/术语表.md` 一致，7 个文件内无第二种译法。✓
- **$\operatorname{}$**：Bun/Op/Hitch 未在本段出现；本段 Der、Diff、End、Ext、Hom、Spec、Spf、Sym、gr、Lie、Res、tr、id、Coker、Im、Ker、Pic、Conn、Bar、ad 等全部 `\operatorname{}`，未见裸写。✓
- **编号**：`\SourcePage{296}`–`{366}` 共 71 处，页界均落在原书换页断句处（例如 u13 行 8 从「丛 $\omega_{K\backslash Y}=\det\Omega_{K\backslash Y}$ 沿投影……」续起，与 p.355/p.356 断句一致）；`\bdp`/`\bdsec` 与原书编号逐一对应；`\tag{344}`–`\tag{391}` 全部对图核过编号与内容。✓

## 五、自检

- 改动：**4 处（P1×2、P2×2）**；`git diff` 等价检查——`ch07_u09.tex` 2 行行内替换、`ch07_u13.tex` 1 行行内替换、`ch07_u10.tex` 新增 1 行 `%` 注释。
- 未触碰：`ch07_u01.tex`–`ch07_u06.tex`（另一位校订员在改）、`源码/chapters/`、`main.tex`、其他章、`工程文件/work/术语表.md`、`符号表.md`；未改任何 `\SourcePage`/`\bdp`/`\bdsec`/`\tag`/label；未删改任何既有 Tutor Note。
- 源码卫生：7 个文件内 `$` 成对（脚本扫描无奇数行）；`\begin`/`\end` 环境全部配对；新增注释行以 `%` 开头，不影响排版。
- 编译：`源码/` 整体复制到 `C:\Users\admin\Downloads\_rev_ch07b\`，`export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH" && xelatex -interaction=nonstopmode main.tex` 连跑两遍 → `grep -c "^!" main.log` = **0**，`main.log` 中 Warning 计数 **0**，仅 5 处 Overfull \hbox（长公式行的常规溢出，非错误），生成 `main.pdf`（1.39 MB）。改动均已在上列文件内生效（编译副本内 `grep` 复核：`p^{\cdot}_{U_i\Omega}`×2、`\mathrm{Cl}^{\cdot}_{\mathfrak{g}}`×1、新增批注×1）。
- 未运行 `工程文件/scripts/assemble.py`；辅助产物只在 `C:\Users\admin\Downloads\_rev_ch07b\`（编译副本，未污染工程目录）与 `C:\Users\admin\Downloads\_crop*.png`（核对用的裁剪放大图，可随时删除）。

## 需主译/总校裁定

1. **`ind-finite type` 是否统一译作「归纳有限型」**：现状为 u07 中文、u08–u13 英文并存（本人未动，理由见三.1）。若裁定统一，建议整体替换为「归纳有限型」并同步 u01–u06 的同类写法，属跨单元批量改动，请指派人统一执行。
2. **$\omega_{(K\backslash Y)}$ vs $\omega_{K\backslash Y}$**：经 p.355/356/358/359 逐页核对，两套写法是**原书自身**的不一致，译本已逐处对应。建议**保持照录**（不加批注、不强行统一）；若总校要求全章统一书写，则必须偏离底本字形，需明确授权。
3. **p.326 的 `(English?)`**：本次仅加批注、正文照录（问题 4）。若项目政策不允许校订员新增批注，可删除该行注释，正文不动。
