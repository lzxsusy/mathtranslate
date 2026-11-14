# ch02a 报告（原书 p.530–p.538 前）

文件：`src/chunks/ch02a.tex`（398 行）　术语提案：`work/proposals/ch02a.tsv`（7 条）

## 1. 内容与结构

- 起点：p.530 的 `CHAPTER 2` / `Categories of coherent sheaves and functors between them` → `\chapter{凝聚层范畴及其间函子}`；紧接 `2.1. Basic properties of categories of coherent sheaves` → `\section{凝聚层范畴的基本性质}`，节标题后一条 `\takeaway{}`（≤120 字，概述 (6)/(8)/(9)、HA(X)、霍奇竖列与 K 群）。
- 终点：p.538 的 `2.2. Examples of equivalences: flopping birational transformations` 标题**之前**（该标题及其后全部归 ch02b，本块未译一字）。
- 段落：逐段照译，未合并、未拆分、未删句。顺序为：本章约定与 Serre 函子 → (6) → 态射给出的三个导出函子 → Φ_E/(7) → Ψ_E（无编号）→ 引理 2.1.1 与 (8) → 左伴随的证明链 → 一般图表 X←Z→Y 的说明 → 三重积的投影图与三函子 → ⊠_Y → 命题 2.1.2 与 (9) → 三个问题 1)2)3) → 定理 2.1.3 → 定理 2.1.4 → Auteq 与 G(X) 段 → 猜想与全忠实准则 → 定理 2.1.5（两个正交性条件）→ 摩天楼层的说明 → 命题 2.1.6 → 命题 2.1.7 → 其证明（p.535）→ 核的显式形式段 → Ad_E/(11)(12)(13) → HA(X) 定义与典范等同 → 定理 2.1.8 → 典范代数/反典范代数段 → 推论 2.1.9 → 定理 2.1.3 与 2.1.9 的对比段 → 谱序列与 (14) → 推论 2.1.10 与 (15)(16) → v_ξ/w_ξ/(17) → 复合公式 ζ → ε/(18) → φ_E/ψ_E/(19) → 命题 2.1.11 → 推论 2.1.12 → K 群段与交换图 → “交换。”
- 陈述环境共 **12** 条，编号全部手工照抄原书、未用 `\label`/`\ref`：引理 2.1.1、命题 2.1.2、定理 2.1.3[8]、定理 2.1.4[8]、定理 2.1.5[7]、命题 2.1.6、命题 2.1.7、定理 2.1.8、推论 2.1.9、推论 2.1.10、命题 2.1.11、推论 2.1.12。证明环境 4 处（引理 2.1.1、命题 2.1.7、定理 2.1.8、推论 2.1.10）＋推论 2.1.12 的证明，与原书一致。
- 页标记 `% [原文 p.N]` 共 **9** 条（530–538），跨页段落标在换页处（如 p.530/531 之间的直接像函子一句、p.531/532 之间的“只是把其中的对象换成…”、p.533/534 之间的定理 2.1.5 条件 2)）。

## 2. 公式与图

### 编号公式（14 条，(6)–(19)）

全部 `\begin{equation}` + `\tag{n}` 手工编号，逐条与 200 dpi 页图核对：

- (6) `\Hom(\cE,\cF)=\Hom(\cF,\cE\otimes\omega_X[n])^{*}` ——页图用 `=`（不是 ≅），照录。
- (7) `\Phi_{\cE}(\,\cdot\,):=\Rb q_*\bigl(\cE\otL p^*(\,\cdot\,)\bigr)`；Ψ_E 的同式 display **无编号**（页图亦无）。
- (8) `\Phi^{*}_{\cE}\cong\Psi_{\cE^{\vee}\otimes q^{*}\omega_Y[m]}` 与 `\Phi^{!}_{\cE}\cong\Psi_{\cE^{\vee}\otimes p^{*}\omega_X[n]}`，一句两式、中间“和”。
- (9) `\cG=\Rf p_{13*}\bigl(\cE\boxtimes_Y\cF\bigr)`（页图小写 p，见 §3 校勘）。
- (10) `\Phi_{\cF_1\boxtimes\cF_2}\circ\Phi_{\cE_1\boxtimes\cE_2}\cong\Phi_{\cG_1\boxtimes\cG_2}`。
- (11) `\Phi_{\cF\boxtimes\cE}:\Db(X\times X)\to\Db(Y\times Y)`；(12) `\Phi_{Ad_{\cE}(\cG)}\cong\Phi_{\cE}\circ\Phi_{\cG}\circ\Phi_{\cE}^{-1}`；(13) `Ad_{\cE}(i_{X*}\omega^{k}_{X})\cong i_{Y*}\omega^{k}_{Y}`。
- (14) `\mathrm{HA}_{i,k}(X)\cong\bigoplus_{p+q=i}H^{p}(X,\bigwedge\nolimits^{q}T_X\otimes\omega^{k}_{X})`（`\bigwedge\nolimits^{q}` 沿用 ch00a 写法）。
- (15)(16) 推论 2.1.10 内两条编号式；(17) v_ξ/w_ξ 一式两行；(18) ε 的定义；(19) φ_E 与 ψ_E——页图分两行、编号在**第二行**，故用 `align` + 首行 `\notag`。

### 未编号 display（24 处）

X←p X×Y→q Y；Ψ_E；引理 2.1.1 的四行同构链（`aligned`，右端对齐于 ≅）；X←p Z→q Y；三函子 Φ_E/Φ_F/Φ_G；三个 R π 公式（`gathered`，第二行“以及”）；HA(X) 定义；典范等同；⊠ 的定义式；Φ_{E1},Φ_{E2},Φ_{E1⊠E2}；Φ_G/Φ_H；Φ_{G1}/Φ_{G2}；命题 2.1.7 的定义域/值域；ℱ ≅ E^∨⊗p*ω_X[n] ≅ E^∨⊗q*ω_Y[m]；Ad_E 的 type；Ext^{i}_{X×X}≅Ext^{i}_{Y×Y}；⊕H^0=⊕HA_{0,k}（两式）；HA_{i,k}(X)=Ext^i(O_Δ,i_{X*}ω_X)；HA(X)≅⊕⊕H^p 的代数同构；v_ξ/w_ξ 的 type；ζ 的公式；φ_{XZ} 段前的复合说明；命题 2.1.11 的两个函子；ch·√td_X:K(X)→H^*(X,ℚ)。

### 交换图（2 个，TikZ 手排，未用 `\figdiag`）

1. p.532 的“投影图”，用 `tikzcd`（`row sep=3.6em,column sep=2.4em,ampersand replacement=\&`）重排为 3×3 矩阵：顶点 X×Y×Z（上中）、X×Y / X×Z / Y×Z（中排）、X / Y / Z（下排）；上排三条箭头标 `p_{12}`、`p_{13}`、`p_{23}`；中排到 X / Y / Z 的六条箭头标 `p^{1}_{12}`、`p^{2}_{12}`、`p^{1}_{13}`、`p^{3}_{13}`、`p^{2}_{23}`、`p^{3}_{23}`（页图标签为矢量轮廓、文字层抽不出字符，经 800 dpi 放大核为小写 p 加上标/下标）。七点、无 ≅ 标注。
2. p.538 的 K 群方块，`row sep=3.0em,column sep=3.4em`：上 `K(X)\xrightarrow{\overline{\Phi}_{\cE}}K(Y)`，下 `H^{*}(X,\Q)\xrightarrow{\overline{\vp}_{\cE}}H^{*}(Y,\Q)`，两侧竖箭头标 `\ch\cdot\sqrt{\td_X}` / `\ch\cdot\sqrt{\td_Y}`。四顶点一方块。

两图均用 `\begin{center}\begin{tikzcd}[…]` 直接排版（`\diag` 的固定列宽放不下投影图），`&` 一律写作 `\&`。已渲染复核：六边形箭头指向、标签归属与原书一致，宽度未越出版心，`Overfull \hbox` 为 0。

其余单行数学式（X←Z→Y 一类）按体例手写，未占图位。

### 页图与文字层的出入（逐条已进正文批注）

| 位置 | 页图 | 文字层 | 处理 |
|---|---|---|---|
| p.533 Auteq 式 | `\Aut X\times(\Pic(X)\oplus\Z)` | 抽出 `⋉` | 照录 `\times`，加 Tutor Note（按上下文应为半直积号） |
| p.532 (9) | `\mathbf{R}p_{13*}`（小写 p） | `Rp13*` | 照录，加 Tutor Note（同段三函子作 `\Rf\pi`） |
| p.535 HA 定义 | `\mathrm{HA}_{i,k}`（下标） | 下标 | 与引言 p.515 的 `\mathrm{HA}^{i,k}`（上标）不一致，在译注中说明、各照所据页图 |
| p.537 ε 的定义式前 | `\eps\in H(X\times Y,\Q)`（缺 `*`） | 同（缺 `*`） | 照录，加 Tutor Note |
| p.538 推论 2.1.12 | `\Db(X)\to\Db(Z)` 与 `H^{*}(X)\to H^{*}(Y)` 并存 | 同 | 照录，加 Tutor Note |
| p.531 (8) | `\Phi^{*}_{\cE}`、`\Phi^{!}_{\cE}` | 星号/叹号位置易失 | 按页图恢复 |

## 3. 译注

`\yizhu{}` 共 **6** 条（每条 60–200 字、以【来源：…】收尾，来源只取 A 级）：

1. Serre 函子（p.530，式 (6) 后）：定义、与 Serre 对偶的等价性、(13)/(16) 对它的依赖；来源：原书式 (6)+定义 1.1.3、Hartshorne《Algebraic Geometry》III.7。
2. 核与积分变换（p.531，Ψ_E 后）：kernel object 的说法、(7) 的三步结构、取 O_Δ 得恒等、取 Poincaré 丛得 Fourier–Mukai；来源：原书式 (7) 及其后一段。
3. `\boxtimes_Y`（p.532，命题 2.1.2 前）：定义为 p^*_{12}E⊗^L p^*_{23}F，下标 Y 的含义，与后文无下标外张量积的区别；来源：原书 (9) 前后的定义。
4. `Ad_{\cE}`（p.535，(13) 后）：“共轭”式的做法、与 (9) 是同一件事、保 O_Δ 与 ω 幂是 HA 不变性的依据；来源：原书 (11)–(13)。
5. `\mathrm{HA}(X)`（p.535，定义后）：两个分次方向的意义、i=0 行给出典范/反典范代数、上标/下标不一致的说明；来源：原书引言 p.515 与 §2.1 本处、推论 2.1.9。
6. `\vp_{\cE}`（p.537，(19) 后）：上同调层面的影子、√td 修正项的必要性（GRR 保证）、与 K 群方块交换的关系；来源：原书 (18)–(19) 与命题 2.1.11 前的说明。

`% [Tutor Note: …]` 校勘批注共 **5** 条：p.532 的 p/π（(9) 后）、p.533 的 ×/⋉（Auteq 式后）、p.537 缺上标 `*`（(19) 后）、p.538 的 Z/Y（推论 2.1.12 后）、块末边界声明（文件末行）。

## 4. 术语

- 照用冻结表（`work/glossary.tsv`）：三角范畴、正合函子、特异三角、凝聚层、典范层、Serre 对偶、丰富、极丰富、射影簇、光滑、完备、线丛、张量积、外张量积、核（kernel object 核对象）、积分变换、分次代数、典范同构、Hodge 菱形、霍奇菱形、陈特征、Todd 类、Grothendieck 群、Grothendieck–Riemann–Roch、自等价、全忠实、伴随、摩天楼层、代数闭链、Poincaré 丛、平移、flop。
- 冻结表无、本块必须译出者 → 新定 **7** 条，已写入 `work/proposals/ch02a.tsv`：Serre functor 　Serre 函子（A）、bigraded algebra 　双分次代数（A）、canonical algebra 　典范代数（A）、anticanonical algebra 　反典范代数（A）、quasi-inverse functor 　拟逆函子（A）、semidirect product 　半直积（A）、verticals of the Hodge diamond 　霍奇菱形的竖列（A）。
- 说明：Serre functor、quasi-inverse functor 与 ch03a 的提案重复（该块 p.548 亦出现），两处译名一致，可合并为一条。`\mathrm{HA}(X)` 保留英文缩写，不另立译名。

## 5. 存疑

1. **块边界比 BRIEF 多一页**。任务正文把“推论 2.1.12 与 K 群交换图”列入本块，而二者排在 p.538（BRIEF 记作 ch02a = 530–538 前、8 页）。本块按“止于 2.2 标题之前”处理，故实收 p.530–538（9 页），文件末有 Tutor Note 登记。若 Lead 判定这两段归 ch02b，删去 `ch02a.tex` 末 4 段（`% [原文 p.538]` 至“交换。”）即可，其余内容不受影响。
2. **p.533 `\Aut X\times(\Pic(X)\oplus\Z)`**：页图印乘号、文字层抽出半直积号；按上下文（G(X) 为半直积）应以 ⋉ 为是，属原书排版笔误。已照录页图并批注，未静默改字。
3. **p.532 (9) 的小写 `p`**：同段三函子作 `\Rf\pi^{3}_{13*}`，而 (9) 作 `\Rf p_{13*}`。已照录并批注。
4. **p.535 `\mathrm{HA}_{i,k}` 与引言 p.515 `\mathrm{HA}^{i,k}`**：同一对象上标/下标不一致，无法判断孰为原意；本块各照所据页图，未统一（若全书统一为上标，需 Lead 跨块裁决）。
5. **p.537 `\eps\in H(X\times Y,\Q)` 缺 `*`**：页图与文字层一致缺，上下文（(17) 与推论 2.1.12 证明均用 `H^{*}`）应为 `H^{*}`；照录并批注。
6. **p.538 推论 2.1.12 的 Z/Y**：`\Phi_{\cE}:\Db(X)\to\Db(Z)` 与 `\vp_{\cE}:H^{*}(X,\Q)\to H^{*}(Y,\Q)` 并存，据命题 2.1.11 的记号应为 `\Db(X)\to\Db(Y)`；照录并批注。
7. **p.532 “the composition law give just described”**：英文笔误（give→given），中译按“刚刚描述过的那一条”处理，未加批注。
8. **编译状态**（两图改 TikZ 后重测）。① 隔离最小构建（`work/build_min02a`：preamble + frontmatter + ch00a + ch02a，lualatex ×2）：`file:line=无「!」行 fatal=0 undefined=0 missingchar=0 overfull=0`，输出 `main.pdf (16 pages)`。② 整书构建（指令指定方式：`cd src; lualatex -interaction=nonstopmode -output-directory=...\build_ch02a main.tex`）：`main.pdf (137 pages)`，`file:line=无「!」行 fatal=0 undefined=0 missingchar=0 overfull=0`；本块在 PDF 中占 p.25–35（印刷页 21–29）。注：中途一次构建曾出现 84 条 `! Argument of \tikz@quote@@parser has an extra }` / `l.44`，`grep` 定位为 `chunks/ch03a.tex:44` 的并发编辑残影，与 b 块无关，重编后消失。
9. **工具限制**：本仓库 `latex_look` 不可用（auto 选 xelatex，本项目须 lualatex，且报 “the produced PDF is invalid or truncated”）；且 `src/main.pdf` 会被并发编译的其他译者写坏，故版面复核一律在 `work/build02a` 的隔离副本上用 pymupdf 渲 125 dpi PNG 进行（脚本 `work/render.py`）。

## 6. 与邻块的边界

- 原书首句（本块从这里开始）：p.530 `CHAPTER 2 / Categories of coherent sheaves and functors between them`，`2.1. Basic properties of categories of coherent sheaves.` 之后 “From now on, we consider only bounded derived categories of coherent sheaves on smooth complete algebraic varieties.”
- 原书末句（本块在这里收尾）：p.538 “Using the Riemann–Roch theorem, one can show that the diagram [K(X) → K(Y)，H^*(X,ℚ) → H^*(Y,ℚ)] is commutative.”
- 起点之前：p.530 上半页仍属第 1 章（命题 1.3.6[17]、1.3.7[17]、1.3.8[17] 与式 (3)(4)(5)），归 ch01b，本块未重复译。
- 终点之后：`2.2. Examples of equivalences: flopping birational transformations` 标题及其正文（定义 2.2.1、2.2.2 等）归 ch02b，本块未译一字；本块末行的 Tutor Note 已标明此边界。
