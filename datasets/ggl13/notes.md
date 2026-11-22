# 笔记：Witten《Khovanov 同调与规范理论》

## 基本信息

- 原文：Edward Witten, *Khovanov Homology and Gauge Theory*, arXiv:1108.3103v2 [math.GT]，2012-10-02 修订（v1 为 2011-08-15）。
- 篇幅：18 个 PDF 页（印刷页 1–17，末页参考文献占一页）；本资料卡一律用 **PDF 页序**。
- 体裁：会议/综述式短文，**没有编号定理**，只有编号公式；论证多处以「it turns out」「one expects」「there should be」的形式给出，细节推给 [2]（Fivebranes and Knots）与 [3]（Gaiotto–Witten）。
- 首页仍留着模板占位 `hep-th/yymm.nnnn`，是 v1 模板未清理的残留，不是内容。
- 一句话概括：用四维椭圆方程（复 CS 的梯度流）的解数复现 Jones 多项式，用它的五维版本给出 Khovanov 同调的候选，边界条件由纳姆极点与对偶群表示给出，而 t∈RP¹ 的族把几何 Langlands 对偶接进来。

## 全文骨架（PDF 页 / 印刷页）

| 节 | PDF 页 | 印刷页 | 内容 | 关键式 |
| --- | --- | --- | --- | --- |
| 标题页 | p001 | — | 标题、作者、摘要、遗留占位符 | — |
| §1 Introduction | p002 | 1 | 纲领：四维椭圆方程 → Jones，五维 → Khovanov | — |
| §2 Gradient Flow Of Complex Chern-Simons | p002–p005 | 1–4 | 复 CS、h₀、乘子 φ₀、梯度流、四维方程族、t∈RP¹、实形式对合 | (2.1)–(2.15) |
| §3 Relation To The Jones Polynomial | p006–p008 | 5–7 | M=W×ℝ+、临界点、解的计数、J(q;K,R)、CS 路径积分、Lefschetz 喉管 | (3.1)–(3.4) |
| §4 Khovanov Homology | p008–p011 | 7–10 | 范畴化 Casson→Floer，再对 Jones 做一次，五维、链复形、Z×Z、link cobordism | (4.1)–(4.3) |
| §5 The Boundary Condition | p012–p013 | 11–12 | 纳姆方程、纳姆极点、椭圆边界条件、一般 W 的标架/自旋、纽结模型解 | (5.1)–(5.3) |
| §6 Categories | p013–p016 | 12–15 | 拉伸纽结、约化三维方程、几何 Hecke 变换、oper、Gaudin 自旋链、A-模型范畴 | (6.1)–(6.2) |
| §7 Knot Projections | p016–p017 | 15–16 | 改 y→∞ 条件、Coulomb 分支、准阿贝尔、投影内建、顶点模型 | (7.1) |
| References | p018 | 17 | 17 条 | — |

图：图 1（p006，M=W×ℝ+ 与临界点）、图 2（p010，M*×ℝ+ 中的 Σ）、图 3（p011，link cobordism）、图 4（p014，拉伸纽结）、图 5（p015，ℝ²×ℝ+ 上的标记点）、图 6（p016，纽结投影）。

## 主结果（按可信度分层）

1. **方程族 (2.14)**（p004）：复 CS 的梯度流按自对偶/反自对偶分解后得到
   (F−φ∧φ)⁺=t(d_Aφ)⁺，(F−φ∧φ)⁻=−t⁻¹(d_Aφ)⁻，d_A⋆φ=0，t=(1−cos α)/sin α=tan(α/2)∈RP¹。
   原文在 p004 只给结论（「turns out」），p005 补 t=0/∞ 的极限与 φ→−φ 对合。
2. **计数函数**（p007，式 (3.2)）：J(q;K,R)=Σ a_n q^n，a_n 为瞬子数 n 的解的带符号计数。**猜想**（原文用 claim）：G∨=SU(2)、R 为二维表示、W=ℝ³ 时即为 Jones 多项式。细节见 [2]。
3. **范畴化**（p008–p011）：把 φ₀ 换成 D/Ds、把 W 换成 ℝ×W，得五维方程；时不变解给链复形基、时变解给微分，同调称 **候选** Khovanov 同调；Z×Z 分级（上同调次数 + q-次数=瞬子数）；等变 Euler 特征等于 J(q;K,R)；允许一般 Σ 得 link cobordism 候选。
4. **边界条件**（p012–p013）：y=0 处只允许渐近于 φᵢ=tᵢ/y（tᵢ 给 Kostant 意义的主 𝔰𝔲(2) 子代数）的解；一般 W 上要求 ad(E)≅TW 的协变常值同构，于是需要 W 的标架化，G=SU(2) 时还需要自旋结构；纽结情形每个 G∨ 不可约表示对应一个沿 K 奇异的模型解。
5. **§6 约化**（p014–p016）：[Dᵢ,Dⱼ]=0 与 Σ[Dᵢ,Dᵢ†]=0；t=1 与 [4] 的推广 Bogomolny 方程一致、描述几何 Hecke 变换；一般 t 是 ℝ²×ℝ+ 上带 Hermite 度规的平坦 G_C 丛；y=0 使其成为 ℂ 上带奇点的 oper，与 Gaudin 自旋链相关。
6. **§7 投影与顶点模型**（p016–p017）：φ→Σcᵢdxⁱ（cᵢ∈𝔱），c≠0 破缺到 Coulomb 分支；尺度大于 1/|c| 时准阿贝尔；G=SU(2) 时 c 给向量 a，决定投影；[3] 由此把 J(q;K,R) 映射到顶点模型，不依赖量子场论论证。

## 公式索引（编号 → PDF 页 → 作用）

| 式 | 页 | 内容 | 作用 |
| --- | --- | --- | --- |
| (2.1) | p002 | CS(A)=1/4π∫_W Tr(A∧dA+⅔A∧A∧A) | 复 CS 的实形式 |
| (2.2) | p002 | ds²=−∫_W Tr δA∧⋆δA | 联络空间上的（形式）度规 |
| (2.3) | p003 | dA/ds=∇CS(A) | 最朴素的梯度流 |
| (2.4) | p003 | F⁺=0 | W×ℝ 上同一方程的写法（自偶部分） |
| (2.5) | p003 | CS(A) 复化到 G_C | 相位来源 |
| (2.6) | p003 | h₀=−Re(e^{iα}CS(A)) | 复 CS 化出的实值函数 |
| (2.7) | p003 | ds² 只 G-不变 | 为什么必须放弃 G_C 不变性 |
| (2.8) | p003 | dA/ds=−∇h₀ | 换 Morse 函数 |
| (2.9) | p003 | ω=∫_W Tr δA∧⋆δφ | 辛形式 |
| (2.10) | p004 | μ=d_A⋆φ | 矩映射 |
| (2.11) | p004 | h=h₀+∫d³x√g Tr φ₀μ | 加乘子得到实值 h |
| (2.12) | p004 | φ₀ 的范数条件 | 让乘子项良定义 |
| (2.13) | p004 | dΦ/ds=−∇h(Φ) | 真正要解的梯度流 |
| (2.14) | p004 | (F−φ∧φ)⁺=t(d_Aφ)⁺，(F−φ∧φ)⁻=−t⁻¹(d_Aφ)⁻，d_A⋆φ=0 | 四维椭圆方程组，全文核心 |
| (2.15) | p004 | t=(1−cos α)/sin α=tan(α/2) | 参数化，t∈RP¹=ℝ∪∞ |
| (3.1) | p007 | ∫_M Tr F∧F | 瞬子数（拓扑定义需标架） |
| (3.2) | p007 | J(q;K,R)=Σ aₙqⁿ | 计数函数 |
| (3.3) | p007 | ∫_U DA e^{ikCS(A)}Tr_R P exp∮_K A | CS 路径积分表示 |
| (3.4) | p007 | (3.3) 推广到中间维 cycle Γ | 与 N=4 路径积分对接的桥 |
| (4.1) | p008 | F=0 | Casson 的计数对象 |
| (4.2) | p008 | F+⋆d_Aφ₀=0 | 折叠后的 Bogomolny 方程 |
| (4.3) | p010 | 与 (2.14) 逐字相同的三式 | 链复形的基（时不变解） |
| (5.1) | p012 | dX₁/dy+[X₂,X₃]=0（及循环） | 纳姆方程 |
| (5.2) | p012 | dφ₁/dy+[φ₂,φ₃]=0 | 平移不变 ansatz 约化后的方程 |
| (5.3) | p012 | φᵢ=tᵢ/y，[t₁,t₂]=t₃ | 纳姆极点 |
| (6.1) | p014 | [Dᵢ,Dⱼ]=0 | 约化三维方程（全纯性） |
| (6.2) | p014 | Σᵢ[Dᵢ,Dᵢ†]=0 | 约化三维方程（矩映射/实条件） |
| (7.1) | p016 | φ→Σᵢcᵢdxⁱ（y→∞） | 新的无穷远条件 |

## 逐节细读（原文里没进卡片的句子）

**§2（p002–p005）**：为什么要绕这么大一圈？因为「没有便利的 G_C-不变度规」——p003 明说 the space of complex connections 上找不到既便利又具全 G_C 对称的度规，所以先取实部（h₀），再用只 G-不变的 Kähler 度规，代价是必须另加一个伴随值一形式 φ₀ 与乘子项。这一步的物理读法是「把复 CS 当势能、把 φ₀ 当拉格朗日乘子」，数学上则是把一个复值函数的梯度流拆成实部与虚部两部分条件。(2.14) 的得到方式是：梯度流沿联络方向给出 F 的自偶/反自偶部分，沿 φ 方向给出 d_Aφ 的相应部分，两组按 t 配比；p004 只说 turns out，没有给逐项代数。t 的两个端点值得单记：t=0 与 t=∞ 时方程退化为「Bogomolny 方程 + 实形式条件」，这正是 p005 说「与实形式的 Floer 理论对接」的意思；而 φ→−φ 是 t↦−1/t 型的对合，可与实形式的内/外对合 τ 复合。

**§3（p006–p008）**：三步走——(i) 把 W×ℝ+ 上的 N=4 超对称路径积分写成对临界点的计数；(ii) 用电磁对偶把「G、参数 t」换成「G∨、−1/t」；(iii) 把这个路径积分解释成三维理论在 U_C 上的路径积分，其中积分 cycle Γ 若取成「对 y=∞ 临界点的 Lefschetz 顶针」，就与本篇的四维方程等价。关键限制：一般 W 上 Γ 并不等于整个 U，只有 W=ℝ³ 时二者才一致，所以「计数 = Jones」只在这个情形被断言。另有两个细节容易漏：瞬子数的拓扑定义需要两端把丛识别起来（p007 提到 the boundary conditions at the two ends give identifications of the bundle），而标架化的依赖恰好复现 Jones 多项式的 framing 依赖——这不是缺陷，是必须的。

**§4（p008–p011）**：作者自己给的类比是「Casson 不变量之于 Floer 上同调，正如 Jones 之于 Khovanov」。技术要点是 φ₀ 在方程里只以 [d_A,φ₀] 的形式出现（一次，线性），所以把 φ₀ 换成 D/Ds（沿新时间方向的协变导数）时，方程自动变成 F⁺=0 型的瞬子方程——这就是「升一维」为什么可行的全部理由。T*M=T*W⊕ℝ 提供 φ₀ 这一项也在这里用到：M=W×ℝ+ 时 T*M 分解出一个平凡 ℝ 方向，正好当 φ₀。链复形基取时不变解、微分数时变解，这不是外加的公理，而是「五维方程本身就是梯度流」的直接结果。

**§5（p012–p013）**：先在最简单的 W=ℝ³、G=SO(3) 上做，纳姆极点就够；推广到一般 W 时出现一个不太被注意的群论条件：tᵢ 要给出 ad(E)≅TW 的同构，协变常值迫使 A|_W 就是 W 的 Levi-Civita 联络，于是「W 必须可标架化」不是技术假设而是方程的要求。G=SU(2) 时更进一步：TW 要提升成 SU(2) 丛，所以自旋结构属于边界条件的一部分。一般 G 时用主嵌入 ρ:𝔰𝔲(2)→𝔤 从 Levi-Civita 联络拉回，只有 ρ 的像整个落在 SU(2)（而非只到 SO(3)）时才需要自旋结构——这句话是 p013 的原文，卡片里照录了。

**§6（p013–p016）**：把纽结沿一个方向「拉伸」是为了让三维约化有意义（图 4 画的就是这个极限）。约化后的方程 (6.1)(6.2) 里 Dᵢ 的构造依赖 t：t=1 时它就是 [4] 的推广 Bogomolny 方程，描述几何 Hecke 变换，模型解有闭式（[2,11]）；一般 t 做一个换元后变成 ℝ²×ℝ+ 上带 Hermite 度规的平坦 G_C 丛加矩映射条件。ℝ²×ℝ+ 单连通，所以没有单值问题，全部有趣结构来自 y=0/∞ 的边界：y=0 把 ℂ 上的平坦丛变成 oper，纽结处允许奇点但要求无单值，奇点类型由 G∨ 的表示分类（[14]），这条线与 Gaudin 自旋链的可积结构相连。

**§7（p016–p017）**：把 y→∞ 的条件从「趋于零」改成「趋于 Σcᵢdxⁱ」，A=0 时是精确解，且 [15] 已有这类无穷远条件的纳姆方程理论可依。解数在 c 的连续形变下不变 ⇒ 任意 c 都给同一个 Jones 多项式；G=SU(2) 时 c 只有一个分量，给出 ℝ³ 中一个向量 a，a 的方向决定投影方向，于是投影被内建。c≠0 时规范群破缺到极大环面（Coulomb 分支），尺度 ≫1/|c| 的区域方程准阿贝尔、可用阿贝尔方程近似；p017 承认「有一处重要例外」，没有展开。[3] 就是沿这条线把 J(q;K,R) 直接写成顶点模型的配分函数。



## 卡片地图（8 概念 + 4 推导）

概念卡：

1. `ggl13/concept/complex-cs-morse-function` — h₀、μ、乘子项、梯度流 (2.13)。为什么不能直接拿 CS 当 Morse 函数。
2. `ggl13/concept/t-family-elliptic-equations` — (2.14) 三式、t=tan(α/2)、端点极限、实形式对合、与 KW06 的关系。
3. `ggl13/concept/solution-count-jones` — 瞬子数 (3.1)、a_n、J(q;K,R)、标架依赖、猜想的三个条件。
4. `ggl13/concept/khovanov-complex-candidate` — 五维 X=M*×ℝ+、Σ、链复形与微分、Z×Z、等变 Euler、link cobordism。
5. `ggl13/concept/nahm-pole-boundary-condition` — 纳姆极点作为椭圆边界条件、一般 W 的协变常值同构、标架化/自旋结构。
6. `ggl13/concept/knot-boundary-condition` — 纽结的奇异常规解、每个 G∨ 表示一个模型解、R 是唯一通道。
7. `ggl13/concept/reduced-equations-oper` — Dᵢ、矩映射、t=1 的几何 Hecke 变换、oper、Gaudin、A-模型范畴。
8. `ggl13/concept/knot-projection-coulomb` — (7.1)、Coulomb 分支、准阿贝尔、投影内建、顶点模型。

推导卡：

1. `ggl13/deriv/complex-cs-gradient-flow` — 复 CS → h → 梯度流 → (2.14) → t∈RP¹。
2. `ggl13/deriv/casson-to-khovanov` — 范畴化是同一台机器：两次「φ₀→D/Ds + 升一维」。
3. `ggl13/deriv/nahm-pole-from-ansatz` — 平移不变 ansatz → 纳姆方程 → 极点 → 椭圆边界条件 → 一般 W。
4. `ggl13/deriv/jones-to-vertex-model` — CS 路径积分 → 喉管 → N=4 对偶 → Coulomb 分支 → 顶点模型。

取舍说明：原计划 9 张概念卡（含「Casson 不变量」单卡），但 Casson 的全部内容都服务于「范畴化的第一步」，与推导卡 D2 重复，故砍掉并入 D2；「半稳定性条件」只在 p006 一句带过（复平坦联络需半稳定才会被计数），不足以独立成卡，写进 `solution-count-jones` 与概念卡 1 的正文。「瞬子数的标架反常」并入 `solution-count-jones` 而不单独立卡。

## 与已译文献的接口

- **#12 = 本文 [2]《Fivebranes And Knots》**：本文反复把细节推给它——p008「for a generic W…」，p009「See [2] for details」，p015 说 t=1 的模型解可闭式写出「[2,11]」。**本篇的增量**是给出一张完整、显式的方程与边界条件清单（(2.14)、(5.1)–(5.3)、(6.1)–(6.2)、(7.1)）以及 t∈RP¹ 的族与 §7 的投影内建；#12 承担五维理论与细节论证。两篇不要互相照搬卡片：#12 的卡片若讲五维场论，本篇卡片只讲「升维这一步是什么」。
- **#23 = 本文 [3]《Knot Invariants From Four-Dimensional Gauge Theory》**：p015 把「更透明的结构」归给它，p017 把「到顶点模型的直接映射」归给它。**本篇的增量**是路线与 t 族——本文**不执行**从 4d 规范场论到顶点模型的推导，只说「可以」（it is possible [3]）。因此本篇的 §7 卡片必须写明「顶点模型来自 [3]」，不能写成本文结果。
- **#14 = 1401.6996《Two Lectures on the Jones Polynomial and Khovanov Homology》**：同一作者 2014 年的两讲，晚于本文，题名即覆盖 Jones 与 Khovanov 两条线。**本篇相对 #14 的增量**是：t-族的原始陈述与几何 Langlands 的接口、§5 边界条件的一般 W 处理（标架化/自旋结构的精确群论条件）、§6 的 A-模型范畴猜测与 oper 联系。若 #14 讲得更慢更细，那些论证属于 #14，不能回填成本篇的内容；两篇重叠处只保留本篇的原始措辞与页码。
- **#01 = 本文 [4] KW06**：t=1 时 (2.14) 的来源（p004、p015 两次提到）。库内 `kw06/deriv/one-parameter-family` 的 (3.29) 与本篇 (2.14) 差 t→−t，等价于 φ→−φ 的约定，**不是笔误**；引用时写清约定。
- **#19 ggl19**：同在几何 Langlands 一侧，但 #19 走 B-膜/Azumaya/扭化 D-模，本篇走四维方程的解数与纳姆边界；术语对齐（扭化、特征层、oper 不译），但**不要把两边的构造互相当作同一件事**。
- 术语母本：`gw06`（纳姆方程、纳姆极点）、`functoriality`（Khovanov 同调、Floer 上同调）、`csw`（Jones 多项式）、`seidel`（Lefschetz 顶针）、`kw06`（Bogomolny 方程、瞬子）。本篇没有重复造这些概念的卡，只在需要处引用。

## 术语与译名决定

| 英文 | 中文定名 | 依据/备注 |
| --- | --- | --- |
| Nahm's equations / Nahm pole | 纳姆方程 / 纳姆极点 | 沿 gw06 旧卡，不用「Nahm 方程」 |
| Lefschetz thimble | Lefschetz 顶针 | 沿 seidel 的 correction（由「指套」改定），p008 首见 |
| oper | oper（不译） | 沿 bdh/ggl19 惯例 |
| Bogomolny equation | Bogomolny 方程 | 沿 kw06；注意 p015 原文误排 Bogomoly |
| instanton number | 瞬子数 | 沿 kw06 |
| framing | 标架化（framing 依赖保留英文） | 「framing anomaly」译「framing 反常」更顺 |
| Coulomb branch | Coulomb 分支 | 库内无旧译，按通行译法 |
| quasi-abelian | 准阿贝尔 | 同上 |
| selfdual / anti-selfdual | 自对偶 / 反自对偶 | 通行 |
| semistability | 半稳定性 | p006 一句带过 |
| principal su(2) subalgebra (Kostant) | 主 𝔰𝔲(2) 子代数（Kostant 意义） | Kostant 旧译「Kostant 截面/切片」在别处，此处按字面 |
| GNO dual group | GNO 对偶群 | 保留缩写 |
| geometric Hecke transformation | 几何 Hecke 变换 | 沿 gtgl15 |
| link cobordism | link 配边 | 保留 link 不译，避免与「链环」混淆 |

## 核对与勘误

### 外部来源（逐条核过的五项）

| 编号 | 外部来源 | 核对对象 | 结论 |
| --- | --- | --- | --- |
| X1 | arXiv abs 页 1108.3103 | 版本史、comment | **两个版本**：v1 2011-08-15、v2 2012-10-02；comment 仍写「16 pp」，两版都是 52 KB。本篇 txt 对应 v2、18 页 |
| X2 | arXiv PDF 首页（p001） | 版本标记与模板残留 | 首页写 `arXiv:1108.3103v2 [math.GT] 2 Oct 2012`，与 X1 一致；另有遗留占位符 `hep-th/yymm.nnnn` |
| X3 | INSPIRE-HEP 记录 | 被引数与文献身份 | 被引 50（抓取时）；确认 [4]=hep-th/0604151 即 KW06 |
| X4 | nLab「Khovanov homology」 | 术语与定位 | 确认 Khovanov 同调是 Jones 的范畴化、双分级、配边给态射，并引 Witten 2011 的四维 TQFT 解释；nLab 无 Kapustin–Witten 专页（404） |
| X5 | 库内 kw06 推导卡（式 (3.29)） | (2.14) 的符号与 t 约定 | 两式差 t→−t，等价于 φ→−φ，**判为约定差异而非笔误** |
| X6 | arXiv 页面 0705.4571 | 参考文献 [5] 的编号 | 确认该号为 Gaitsgory《Twisted Whittaker Model And Factorizable Sheaves》，故 p018 的 `0705:4571` 是分隔符笔误 |
| X7 | arXiv 两版 PDF 逐页 diff（v1 15 Aug 2011 / v2 2 Oct 2012） | 作者修版究竟改了什么 | **4 处实质修改**：①p4 与 p9，v1 `Ω1(M) = Ω1(W) ⊕ R` → v2 `T*M = T*W ⊕ R, where R is a trivial real line bundle of rank 1`（作者自己的符号纠错）；②p8，v1「The count of solutions is the same」→ v2「the same, apart from rather degenerate solutions」；③p8–9，v1 消失定理结论 `φ0 = 0` → v2 `φ0 covariantly constant`；④p1 删去脚注 1（Berkeley 会议致谢）。其余为脚注编号顺移 |

### 外部校正动作清单（五项逐条）

1. **版本与页数**：X1 显示两版；`XREF.md` 生成时误记为「版本数 1」（抓取只看到一条版本记录），此处以 X1 更正为 2 版，页数以本篇 PDF 的 18 页为准，comment 的「16 pp」是 v1 页数遗留。
2. **标题与摘要**：X1 的标题、摘要与 p001 逐字一致，无需改。
3. **参考文献编号**：p018 逐条对照 arXiv，[2]=1101.3216、[3]=1106.4789、[4]=hep-th/0604151、[5]=0705.4571（笔误 e5）、[14]=math/0407524 均确认。
4. **关键公式**：以 X5 核对 (2.14)，符号差为约定；其余公式（(2.1)、(3.1)、(5.2)、(5.3)、(6.1)、(6.2)）逐字照录，未做改写。
5. **术语与符号**：以库内旧卡为准（见术语表），本篇未引入与旧卡冲突的新译名；`t`、`α`、`φ₀`、`μ`、`G∨` 的用法与原文一致。
6. **版本差异（X7）**：把 v1、v2 两版 PDF 逐页取文本做 difflib 比对（54 行差异），发现作者在 v2 里自己改掉了四处实质内容（见 X7 行）。核查本库底本 `pdf/13_IX_1108.3103.pdf`：首页写 `arXiv:1108.3103v2`，`T*M = T*W` 命中 2 次、`Ω1(M) = Ω1(W)` 0 次、`φ0 covariantly` 1 次、「apart from rather degenerate」1 次、Berkeley 脚注 0 次 → **底本就是 v2，卡片所据文本已是作者订正后的版本**，不存在「照 v1 的错写成卡」的问题。反过来，这组 v1→v2 的修正正是本篇「外部校正有用」的正面证据：如果当初只拿到 v1，`φ0 = 0` 与 `Ω1(M) = Ω1(W) ⊕ R` 这两处都会被当成原文照抄进卡。

### 勘误

本稿发现 5 处排印问题：4 处 high（e1–e3 有同篇另一处正确拼写作第二依据，e5 有 arXiv 页面佐证），1 处 low（e4 只有语法判断，属存疑，卡片不改）。逐条见 `errata.tsv`：

| 序 | 位置 | 原写法 | 订正 | 置信度 | 处理 |
| --- | --- | --- | --- | --- | --- |
| e1 | p004 | Lagrange muliplier | multiplier | high | 卡片不引该句；推导卡挂 correction |
| e2 | p013 | Riemannian connnection | connection | high | 卡片不引该句；两张卡挂 correction |
| e3 | p015 | extended Bogomoly equations | Bogomolny | high | 正文按正确拼写；概念卡挂 correction |
| e4 | p017 | On a length scale large than 1/|c| | larger than | low | 仅一处依据，存疑，**卡片不改** |
| e5 | p018 | arXiv:0705:4571 | arXiv:0705.4571 | high | 参考文献，无对应卡片 |

另有一处 p008「not the Jones polynomial, This means」的逗号后大写，属排版疏漏而非术语/公式错误，未登入 errata.tsv（避免把风格问题混进勘误表）。

## 不懂 / 存疑的问题

1. **(2.13)→(2.14) 的代数没有写**：本文只说「turns out」。我按 KW06 的分解方式核对过符号（t 与 −t⁻¹ 的位置），但没有逐项验证 φ∧φ 与 d_Aφ 的自对偶/反自对偶投影，因此推导卡的这一步标 A（原文结论）而非「已复核」。
2. **五维方程的椭圆性未证**：p009 只说「this turns out to be an elliptic equation. (See [2] for details.)」，本文没有给符号计算；把「候选 Khovanov 同调」的分析基础算作已建立是有风险的。
3. **a_n 的有限支撑是猜想**：p007「Conjecturally, a_n vanishes for large enough |n|」；这直接关系到 J(q;K,R) 是否是多项式（而不是形式幂级数），本文未证。
4. **等变 Euler 特征的精确定义**：p010–p011 说瞬子数在 W×ℝ+ 上「有微妙之处，恰好匹配 CS 的 framing 反常」，但没有给出等变参数如何进入；这是我认为全篇最模糊的一处。
5. **§7 的「例外轨迹」是什么**：p017 说准阿贝尔近似「有一处重要例外，但可以被理解」，未展开；我怀疑是纽结附近瞬子尺寸与 1/|c| 相当的区域，但原文未说，卡片只照录「有例外」。
6. **空纽结的秩 1 是校准还是定理**：p013 把它放在「plausible (but unproved)」里，是猜想；不要当成 normalization 的定理。
7. **版本差异未逐字比对**：arXiv 有 v1/v2 两版，本篇按 v2 做；v1 与 v2 的实质差异（尤其 §7 是否新增）我没有逐页 diff，若质检要求版本敏感，这是遗留工作。
