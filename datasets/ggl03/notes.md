# 第 03 篇 · Gukov–Witten《Rigid Surface Operators》笔记

- 题名：Rigid Surface Operators；作者：Sergei Gukov, Edward Witten；arXiv:0804.1561 [hep-th]（2008-04-09）。
- 出版：Adv. Theor. Math. Phys. 14 (2010) 87–178（92 pp）；arXiv 注释 90 pp；本 PDF 90 页。
- 阅读范围：PDF p001–p090（印刷页 1–89）。页码换算：PDF 页 = 印刷页 + 1（p003 页脚 2、p045 页脚 44 已核）；本笔记与卡片一律用 PDF 页。
- 分工：§2.1 大量复述 KW06（hep-th/0612073）；§2.2–§2.5 是本文新构造；§3 给出 sigma model 解释；§4 定义指纹；§5–§6 做对偶匹配；§7 连到量子化；§8 弦论构造；附录 A/B 为例外群与小秩表、so/sp 矩阵实现。

## 1. 骨架（节标题 → 一句话）

- §1 Introduction：把曲面算子与 Wilson/'t Hooft 算子类比，提出本文主题——不含任何连续参数的「刚性」half-BPS 曲面算子，并说明其可能是 minimal/irreducible、且自动共形不变的。
- §2.1 Review：回顾 KW06 的构造——旋转不变 Hitchin 解由 t-值四元组 (α,β,γ,η) 与 Levi 子群 L 刻画，单值性 U=exp(−2π(α−iγ)) 是超对称可观测量的共轭类。
- §2.2 The Limit α,β,γ→0：常值解退化时让位于带自由参数 f 的 Nahm 解 (2.5)，给出比 1/r 弱的对数奇异 (2.6)，其单值性幂零，闭包为 C′。
- §2.3 Searching For Rigid Surface Operators：SL(N,C) 除中心外没有刚性类；Sp(2N) 与 SO(N) 的最小幂零类是刚性类的第一批例子；一般判据落在分拆的重数/间隙条件上。
- §2.4 Strongly Rigid Semisimple Orbits：G 的半单元素 S_i 也可强刚性，其中心化子是删去扩张 Dynkin 图一个节点得到的 Levi 子群 L(Θ_i)。
- §2.5 Combining The Two Constructions：任意 V∈G_C 写成半单部分乘幂零部分 V=SU，刚性问题化归两个因子的刚性问题。
- §3.1 Coupling To Sigma Models：把 4d SYM 与支撑在 D 上的超多重态耦合，Hitchin 方程右端出现超凯勒矩映射的 delta 源。
- §3.2 An Example：Kronheimer 的 Q_{α,β,γ} 在一个复结构下就是 ξ=α−iγ 在 g_C 中的轨道，矩映射取 X_i(0)。
- §3.3 Another Example：SU(2) 的 Y=R4 与 Y′=R4/Z2 对照，提出「幂零轨道闭包作为 sigma model 靶」与 su(2) 嵌入算子等价。
- §3.4 Rigid Surface Operator For The Dual Group：SO(3) 的 S=diag(1,−1,−1) 类弱刚性、其双覆盖 S² 是 S̃ 的轨道；由此提出第一个对偶猜想（SU(2) 的 Y ↔ SO(3) 的 S）。
- §3.5 Minimal Surface Operators：用「D 上的手征算子都是体手征算子的极限」作极小性判据，定义 irreducible surface operator / surface eigen-operator。
- §4.1 Invariant Polynomials：P(φ) 是 half-BPS 局部算子，S-对偶把它送到对偶李代数上的 P̃；dim C 是最基本的对偶不变量。
- §4.2 Polar Polynomials：P(φ) 沿 D 的极点结构（极多项式）由 dim C/2 个复参数刻画，其重参数化不变关系是精细指纹。
- §4.3 Center vs. Topology：中心扭化 z∈Z(G) 与对偶侧基本群特征类 f̂ 是两类离散不变量，对偶要求 Z(G)_V=eπ1(^LG)∨ (4.25)。
- §5 Duality For Strongly Rigid Surface Operators：秩 2–4 逐对比较极多项式与离散不变量；SO(5)/Sp(4) 交换单幂零与半单，SO(9)/Sp(8) 首次出现无法配对的类。
- §6 More Examples：用 special 幂零轨道与 Kazhdan–Lusztig 类系统化对偶，给出 B_N/C_N 的 special rigid 分拆映射 (6.9)。
- §7 Duality And Quantization：曲面算子决定 G_R-表示的中心特征 ζ=η+iγ，猜测对偶类的半单部分满足 ^LS=exp(2πζ)；special 轨道恰是「可量子化」的。
- §8 Stringy Constructions：全息 D3′-brane、RP5 的离散挠率、相交膜模型与 LLM 冒泡几何分别实现上述参数与对偶。
- 附录 A：用 Bala–Carter 记号列出例外群 G2/F4/E6/E7/E8 的刚性幂零轨道及其维数、基本群、special 性。
- 附录 B：给出 sp(2N) 与 so(2N+1) 的矩阵实现、根与余根，并说明不变量多项式 Tr φ^k 在对偶下的对应。

## 2. 主定理清单

1. p009–p011，(2.5)–(2.16)：α,β,γ→0 时 Nahm 解 (2.5) 给出对数奇异 (2.6)；其单值性 U′=exp(−2π(t1−it3)/(s1+1/f)) 幂零，故共轭类为幂零类 C′；C_ξ 在 ξ→0 的极限是 C′∪C0（Tr U=2）。
2. p015–p017，§2.3：SL(N,C) 除中心元外没有刚性共轭类（半单类可调参数；主幂零类可形变到 regular 类）。
3. p017–p018，§2.3：Sp(2N) 的最小幂零类 λ=[2,1^{2N−2}]（复维 2N）在 N>1 时刚性；SO(N) 的最小非零幂零类（分拆 [2,2,1,…]）在 N>4 时刚性。
4. p019–p021，§2.3：SO(N)/Sp(2N) 的幂零轨道强刚性的必要条件——分拆无间隙，且 SO(N) 的奇部/Sp(2N) 的偶部不出现重数 2；充分性引 [12] §7.3。
5. p022–p023，§2.4：SO(N) 的 S_i=diag(1,…,1,−1,…,−1)（2i 个 −1）在 i>1 时强刚性，i=1 只弱刚性；Sp(2N) 中 1≤i≤N−1 的 S_i 强刚性；这些是 SO/Sp 中仅有的刚性半单元。
6. p024–p026，§2.4：一般 G 的强刚性半单元满足 G_S=L(Θ_i)，Θ_i=Δ~\{α_i}，S_i=exp(2πiω∨_i/a_i)；S 的阶整除 Coxeter 标号 a_i，故可共轭进紧群；伴随形式按 Z(G_sc) 作用取商 (2.40)。
7. p027–p029，§2.4–§2.5：扭化条件 Φ(r,θ+2π)=SΦ(r,θ)S^{-1} (2.41) 与 Nahm 奇异 (2.42) 可组合，得单值性 V=SU (2.43)；强刚性类由 (Θ_i, l(Θ_i) 各因子的刚性幂零轨道) 标号。
8. p031–p033，§3.1–§3.2：耦合 sigma model 时 Hitchin 方程的源是矩映射 delta 函数 (3.2)；旋转 ansatz 化为 Nahm 方程 (3.4)，r→0 极限要求 (a,b,c)→(µ1,µ2,µ3) 且矩映射分量交换；Kronheimer Q_{α,β,γ} 满足矩映射 µ⃗=(X1(0),X2(0),X3(0)) (3.7)。
9. p036–p037，§3.3：对幂零轨道 C（闭包 C̄），su(2) 嵌入构造的算子与耦合到靶 C̄ 的 sigma model 算子等价（提案）；SU(2) 情形由 Q_{α,β,γ} 的 Eguchi–Hanson 极限 α,β,γ→0 给出 Y′=R4/Z2 而获支持。
10. p038–p040，§3.4：第一个对偶猜想——SU(2) 的刚性算子（幂零锥双覆盖 Y=R4）对偶于 SO(3) 的弱刚性类 S=diag(1,−1,−1)；理由是两者复维都是 2，而 M_H 维数增量 n 在一切对偶下不变。
11. p044–p046，§4.2：曲面算子的极多项式——φ=n/z+… 时 P(φ) 的极点由 φ 的正则部分决定，B 的维数增加 dim C/2，故 P(φ) 的奇异模式由 dim C/2 个复参数刻画；SU(2) 的指纹是 Tr φ² 有可变单极点 (4.6)。
12. p049–p051，§4.2：把 φ 在每个 z≠0 对角化到 t_C（只到 Weyl 群 W），绕原点的单值性给出 w∈W；w 是曲面算子的不变量，即 Kazhdan–Lusztig 映射（幂零轨道→W 的共轭类）。
13. p051–p053，§4.3：中心扭化给出 Z/Z_V 个新算子，对偶侧拓扑由 π1(^LG)∨/eπ1(^LG)∨ 分类；对偶要求 Z(G)_V=eπ1(^LG)∨ (4.25)，即一側全中心可观测当且仅当另一侧全拓扑可观测。
14. p055–p060，§5：强刚性算子的对偶表——SO(5)/Sp(4) 与 SO(8) 自对偶完全匹配；SO(7)/Sp(6) 的 6/8/12 维类一一配对；SO(9)/Sp(8) 的 18 维类四个极多项式全同、24 维类无法配对，说明仅靠强刚性类不够。
15. p063–p066，§6：special 幂零轨道在 Springer 对应下配对；对 B_N/C_N 的 special rigid 分拆给出显式映射 (6.9)，并验证维数与 Kazhdan–Lusztig 类一致。
16. p070–p072，§7：量子化猜想——附着于类 C 的 G_R-表示的中心特征 ζ=η+iγ (7.4)，对偶类的半单部分满足 ^LS=exp(2πζ) (7.5)；幂零轨道对偶到幂零轨道当且仅当该轨道 special（可量子化）。
17. p072–p075，§8：全息实现——刚性曲面算子对应探针 D3′-brane（AdS3×ℓ），D3′ 的 holonomy (α,η) 与 Higgs 渐近 (β,γ) 即四参数；S-对偶交换 α 与 η。

## 3. 与已译文献接口

- KW06（库内 01，hep-th/0612073，67 卡）：本文 §2.1 逐字复述其 Hitchin 方程 (2.1)、旋转 ansatz (2.2) 与单值性；本文 (7.6) 的 (α,η)→(η,−α) 来自 KW06 §2.6（B 源 p.30）。凡引用 KW06 的公式，本包用 B 源并回查 PDF 页码。
- 02（分歧）：曲面算子在二维面上有奇异性，正是分歧点的几何对应；野分歧对应更高阶极点，本文 §2.2 的「比 1/r 更弱」是 tame 端最弱的容忍度。
- 06（Hitchin）：§2.1 的 M_H、§4.2 的 Hitchin 纤维化 π:M_H→B 与 Hitchin 模空间的超凯勒结构直接相连；极多项式就是 B 上的坐标。
- 16（内窥）：§4.3 的中心/拓扑对偶（Z(G) 对 π1(^LG)）与内窥的群论框架同源；本文把它实现为曲面算子的离散不变量。
- 28（bdh）：§7 把曲面算子与 G_R-表示的中心特征相连，是量子化/表示论接口；special 轨道=可量子化轨道。
- 15（Kapustin–Saulina）：同属「曲面算子与 S-对偶」路线，可对照其拓扑扭曲与算子乘积。
- ggl12（KW06 的后续卡）：canonical-parameter、canonical-coisotropic-brane 等卡与本文 §3.1、§7 的 B+ 边界条件相关。
- 术语沿用库内约定：twist=扭化，eigenbrane=特征膜，Hecke eigensheaf=Hecke 特征层，'t Hooft 算子不译，canonical coisotropic brane=典范余各向同性膜，ramification=分歧，wild=野分歧，endoscopy=内窥，BPS 不译。

## 核对与勘误

### 外部来源

| 来源 | 定位 | 核了什么 |
|---|---|---|
| arXiv 摘要页 | https://arxiv.org/abs/0804.1561 | 标题、作者、2008-04-09、hep-th、90 pp、摘要主旨（刚性=无连续参数；对偶只部分成功） |
| INSPIRE-HEP | https://inspirehep.net/literature/783139 | 期刊 Adv. Theor. Math. Phys. 14 (2010) 87–178、DOI 10.4310/ATMP.2010.v14.n1.a3、texkey Gukov:2008sn、被引 270 |
| Caltech Authors 记录 | https://authors.library.caltech.edu/records/fvwqv-cbd70 | 出版版元数据与摘要，确认与 arXiv 版同一文稿 |
| KW06 原文（B 源） | 库内 pdf/02_I_hep-th_0612073.pdf，PDF p.6、p.30 | (2.1)–(2.2) 的 Hitchin 方程/ansatz 逐字一致；(α,β,γ,η)→(η,β,γ,−α) 与本文 (7.6) 一致 |
| nLab: geometric Langlands correspondence | https://ncatlab.org/nlab/show/geometric+Langlands+correspondence | §Relation to S-duality：Hecke 变换↔'t Hooft 算子、local system↔electric eigenbrane，确认本文所处的 S-对偶/几何 Langlands 语境 |
| nLab: Hitchin fibration | https://ncatlab.org/nlab/show/Hitchin+fibration | Hitchin base / Hitchin 纤维化的背景（未给方程，只作语境旁证） |
| Witten, Gauge Theory And Wild Ramification | https://arxiv.org/abs/0710.0631 | 摘要确认「new surface operators associated with higher order singularities」，支持 §2.2 的奇异度容忍与 02 篇接口 |

### 五项清单（按 XREF.md 动作清单逐条）

1. 主定理陈述与符号：摘要、引言、§2–§8 的陈述与 arXiv/INSPIRE 摘要一致；KW06 的 (2.1)–(2.2) 与本文 (2.1)、(2.4) 逐字一致，符号 α,β,γ,η,A,φ 含义相同。结论：无冲突。
2. 关键公式系数/符号/指数：Hitchin (2.1)、Nahm (2.3)、U=exp(−2πξ) (2.8) 与 KW06 一致；极多项式 (4.5)、(4.14) 用 φ=n/z+… 直接代入复算一致；Sp(2N) 最小轨道维数 2N 与 (4.1) 复算一致。结论：无系数冲突；只有 (3.16) 的矩阵符号错误（E1）。
3. 命题编号与交叉引用：抽查 (2.27)→(2.28)/(2.30)、(3.9)、(4.1)、(4.25)、(6.9)、(7.4)–(7.7)、(8.9)–(8.12) 的正文引用，均指向正确条目；audit_locators 对全部 locator 的式号—页码检查通过。结论：无编号错位。
4. 数值/维数一致性：§2.3 表（A_N 2N、B_N 4N−4、C_N 2N、D_N 4N−6、E6 22、E7 34、E8 58、G2 6、F4 16）与 (4.1) 复算一致；§5 各表逐行维数复算一致；Sp(2N) 半单类 diag(u,u^{-1},1,…) 的维数 2(2N−1)=4N−2，确实大于 2N。结论：一致。
5. 记号与前后定义：α,β,γ,η 在 §2.1 与 §7 同义；S 在 §2.4 是半单单值性、在 §3.4 同义；C 与 C̄（闭包）区分一致；唯一冲突是 (7.4)、(7.6)、(7.7) 三式的 η 符号不能同时成立（E2，low/open，疑为 η 的符号约定差异，卡片保留原文）。

### 勘误

本稿发现 2 条：E1 为 (3.16) 的提升矩阵符号错误（medium，见 errata.tsv；已在 dual-group-rigid-operator 卡用订正形式并加 corrections）；E2 为 (7.7) 与 (7.4)+(7.6) 的 η 符号不一致（low，open，存疑，卡片保留原文并标注）。无 high 级勘误：没有找到与两处独立出处同时冲突且篇内另有独立不自洽的笔误。

## 4. 不懂 / 待查

- (7.7) 的负号是否只是 η 的符号约定（例如单值性方向取反），还是真笔误：需要作者后续文或 KW06 的 η 定义原文才能定；本包按存疑处理，不改公式。
- §4.2 的 (5.6)（p060，p8=(1/48)p4²−¼p2²p4+¼p2⁴+(2/3)p2p6）只按原文抄录，未用 Schur 多项式独立复算。
- §6 的 Fig.2（B3/C3 的 Hasse 图）与「删去非 special 后图有反序对合」只按文字理解，未逐边核图。
- §8.1 的「D3′-brane 数目 = Levi 的阿贝尔因子数」只按文字接受，未独立数各例的 brane 数。
- 附录 A 的 Bala–Carter 记号 X_N(a_i) 与各轨道 π1 值按原文抄录，未独立核 π1。
- (2.26) 的 C^{2N}/Z2 超凯勒结构、以及 §3.3 的 sigma model 等价一般 G 情形仍是提案（原文对 SU(2) 才给论证），卡片按「提案」标注。

## 5. 交付与自检

- cards/concepts：10 张；cards/derivations：4 张（见 cards/ 目录）。
- terms.tsv：25 条；excerpts.md：4 段；errata.tsv：2 条。
- 检查：tools/lint_cards.py --strict、tools/verify_pages.py --strict、tools/term_index.py check、audit_locators.py（用 txt 目录名 03 实跑）均通过；命令与输出见 workflow.md。
