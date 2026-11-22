# 第 20 篇 · 通读笔记

| 项 | 内容 |
| --- | --- |
| 中文题名 | 拓扑场论、高阶范畴及其应用 |
| 英文题名 | Topological Field Theory, Higher Categories, and Their Applications |
| 作者 | Anton Kapustin（Caltech） |
| 出处 | ICM 2010 报告，arXiv:1004.2307，22 页，9 幅图 |
| 版本 | v1 2010-04-14；v2 2010-04-22（XREF 记 2 版，逐页核对按 v2） |
| 分类 | math.QA；MSC 81T45（主）、18D05（次） |
| 数据集前缀 | ggl20/ |
| 交付 | 概念卡 10、推导卡 4、terms 31 条、excerpts 4 段、errata 1 条 |

## 0 页码约定

卡片、errata、notes 里的 `p.N` 一律指 **PDF 页序**（p001–p022）。逐页核对过页脚印刷页码：p002 起页脚数字与 PDF 页序相同（p011 页脚即 "11"），故两种编号在本篇重合、不会歧义。公式号用原文编号 (1)–(6)；原文**没有**编号的定理/命题，本笔记自编 S1–S16，卡片不援引 S 号。

## 1 一句话

n 维 TFT 应按余维分层成取值在 k-范畴里的扩展函子；2d 与 3d 的物理讨论给出 brane 范畴与变界线 2-范畴这两个可操作的层次；Rozansky–Witten 模型把 3d 情形算出来，其边界条件使 D_{Z2}(Coh(Y)) 的 monoidal 形变由 Maurer–Cartan 方程控制；四维 GL 扭化理论则把几何 Langlands 等价实现为 Montonen–Olive 对偶在 CP¹ 参数族上一个特殊点（t=i ↔ t=1）的推论。

## 2 文章骨架

| 节 | PDF 页 | 一句话 | 关键公式或对象 |
| --- | --- | --- | --- |
| §1 引言 | p001–p002 | Atiyah 公理化 + 扩展 TFT 猜想：低维流形也应有赋值，粘合对应 Hom | F(N12) ≃ Hom(F(N1), F(N̄2)) |
| §2.1 二维 | p003–p005 | 边界条件是 brane，构成 C-线性范畴；态射空间 V_AB 来自半平面初态 | V_AB × V_BC → V_AC |
| §2.2 三维 | p006–p008 | 变界线算子本身成范畴，故边界条件成 2-范畴；结合性只到同构加五边形 | 式 (1) W_XY × W_YZ → W_XZ |
| §2.3 n 维 | p009–p010 | 给 (n−k−1)-流形配 k-范畴；缺陷是 D_k 的对象；融合给 monoidal/编织结构 | D_k := F(S^{n−k−1}) |
| §3 RW 模型 | p010–p015 | 靶为全纯辛流形的 3d 拓扑 sigma 模型；圆周↦D_{Z2}；形变由 MC 方程控制 | 式 (2)(3)(4)(5) |
| §4 四维与 GLC | p016–p018 | MO 对偶 + 扭化族 CP¹；曲面范畴 F(G,t,C) 与圆周 2-范畴 F(G,t,S¹) | 式 (6) |
| §5 开放问题 | p019–p020 | 正确框架是 (∞,n)-范畴；最强陈述是点上的 3-范畴等价；四块分解推出曲面等价 | pants / cup / plumbing fixture |
| 参考文献 | p020–p022 | 39 条，含 KW06、Kontsevich、Lurie、Rozansky–Witten | [1]–[39] |

## 3 主命题清单（原文无编号定理，自编 S1–S16）

- **S1**（p001）Atiyah：n 维 TFT = monoidal 函子 Bord_n → Vect；闭 n-流形给配分函数。
- **S2**（p002）扩展 TFT：n−2 维流形 ↦ C-线性范畴，n−3 维 ↦ 2-范畴，依此类推；p009 重述为 (n−k−1)-流形 ↦ k-范畴。
- **S3**（p002）粘合：N12 由 N1、N2 沿边界粘成 ⇒ F(N12) ≃ Mor(F(N1), F(N̄2))。
- **S4**（p003–p004）2d：brane 构成 C-线性范畴，Hom(A,B) = V_AB，合成 = 融合积。
- **S5**（p006–p008）3d：边界条件构成 2-范畴；1-态射 = W_XY，2-态射 = V_AB；融合积式 (1) 满足五边形。
- **S6**（p008）3d TFT 在区间上的 KK 约化给 brane 范畴一个 monoidal 结构；反之数学上自然的 monoidal 结构多半来自这种约化。
- **S7**（p009）缺陷 = D_k 的对象；0 维给向量空间的元素（态操对应），1 维给范畴对象，2 维给 2-范畴对象。
- **S8**（p010）实心球挖两孔给融合积 D_k × D_k → D_k；n−k>2 时交换，n−k=2 时只编织。
- **S9**（p011）RW：S = Q(V) + S₀；S₀ = ∫(Ω(ρ,Dρ) + ⅓Ω(ρ,R(ρ,ρ,η)))；ρ↔A、Ω↔κ 的 CS 类比；配分函数是有限型不变量。
- **S10**（p012）圆周 ↦ D_{Z2}(Coh(X))；ExtFT 给导出张量积的非对称编织形变；Ω→λΩ 时第 p 阶修正 ~ λ^{1−p}。
- **S11**（p013）孤立交点处 Hom ≅ MF(W2−W1)；D12(φ) = D2·φ − (−1)^{|φ|}φ·D1，D12² = c2−c1。
- **S12**（p014）β 取值 ⊕_{p≥2}Sym^p(TY) 的 (0,1)-形式，满足 ∂̄β + ½[β,β] = 0；规范变换式 (4)；猜想：MC 解满射到 monoidal 形变空间。
- **S13**（p015）Z-分次情形只有次数 3 的解，p≥2 ⇒ 唯一零解；故 brane 2-范畴 ≈ D^b(Coh(Y)) 上的模范畴。
- **S14**（p016–p017）GL 扭化是 CP¹ 参数族；GLC 来自 t=i ↦ t=1 的 MO 对偶特例。
- **S15**（p017–p018）F(G,i,C) ≃ F(^LG,1,C)；式 (6)：F(G,i,S¹) ≃ F(^LG,1,S¹) 且与编织 monoidal 结构相容。
- **S16**（p019–p020）F(G,t,S¹) 是刚性编织 monoidal 2-范畴；任一闭曲面由四块粘成 ⇒ 2-范畴等价推出曲面范畴等价。

## 4 与已译文献的接口

| 篇目 | 可对接点 | 本文位置 | 库内落点 |
| --- | --- | --- | --- |
| 01 电磁对偶与几何朗兰兹（kw06） | MO 对偶、GL 扭化、A/B 模型、几何 Langlands 对应 | p016–p017 | kw/concept/geometric-langlands、kw/concept/topological-twist、kw/deriv/twist-construction |
| 02 规范理论、分歧与 GLC（SY02-06） | 分歧情形；本文只在脚注提更一般的 QGL | p017 脚注 8 | 仅方向性接口，本文不分歧 |
| 06 镜像对称、Hitchin 与朗兰兹（SY05-25） | M_flat(G_C,C) 的复结构与辛结构两面 | p017 | 本文只用两面对照 B/A 模型 |
| 11 量子力学路径积分的新视角（SY03-01） | 路径积分与 Q-正合论证 | p011、p016 | 方法论接口 |
| 16 几何内窥与镜像对称（SY01-07） | 内窥与 MO 对偶的关系 | p016 | 本文只提 MO，未展开内窥 |
| 23 四维规范场论中的纽结不变量（SY05-01） | 4d 扭化理论的可观测量与线算子 | p016 | 拓扑扭化的用法 |
| 28 Hitchin 可积系统的量子化与 Hecke 特征层（bdh） | Hecke 特征层；本文引 [12] Frenkel–Gaitsgory | p019 | bdh/concept/hecke-eigensheaf |
| 36 朗兰兹纲领与共形场论讲义（SY03-21） | 朗兰兹对偶 ^LG 与紧单群 | p016–p017 | bdh/concept/langlands-dual |

说明：本机 `out/` 只有 10、12、13、17、19、22 五个已完成包，01/02/06/11/16/23/28/36 的包**不在**本机，接口按 `XREF.md` §3 的题名表与发布仓 `datasets/` 的实际卡片对接（已核到 kw06 的 67 张卡、bdh 的 Hecke/朗兰兹卡、glc 的 GLC 卡、ggl19 的扭化卡）。因此本表是「篇目级 + 卡级」的混合接口，不是逐句对读。

## 5 term_index 撞名检查

`python tools/term_index.py check out/20_ggl20/cards` → `检查 14 张卡，与既有语料撞名 0 处`。为绕开旧卡已占的通用词形（GL 扭化、几何朗兰兹、A-模型、B-模型、拓扑扭化、Hecke 特征层、导出范畴、Fukaya 范畴等），卡题一律写成更专的形式（如「GL 扭化族与形变参数 t」「二维 TFT 的 brane 范畴」），aliases 也避开了这些词形。

## 核对与勘误

外部校正按 `XREF.md` §4 的五项动作清单逐条做，结论如下。

### 外部校正动作清单

| # | 核什么 | 结论 | 依据 |
| --- | --- | --- | --- |
| 1 | 主定理陈述与符号 | 一致。p002「n−k 维 ↦ k−1-范畴」与 p009「(n−k−1)-流形 ↦ k-范畴」是换指标 k′=k−1 的同一句话；p019–p020 的 3-范畴等价与曲面等价互相蕴含 | 本篇 p002、p009、p019–p020；nLab extFT |
| 2 | 关键公式系数与符号 | 一致。S₀ 的 ⅓ 与 CS 的 ⅓ 同源；D12² = c2−c1 的符号在两处独立复述中相同；MC 方程 (3) 的 ½ 是标准形式 | 本篇 p011、p013–p014；arXiv:hep-th/9612216；arXiv:0810.5415；arXiv:q-alg/9709040 |
| 3 | 命题编号与交叉引用 | 原文无编号定理；编号公式仅 (1)–(6)，与所在页逐一核对无误；[17] 在 p014 指矩阵分解与形变猜想，与参考文献 [17] = Kapustin–Rozansky–Saulina 一致 | 本篇 p020–p022 参考文献 |
| 4 | 数值与维数一致性 | 一致。n=2、3、4 三个例子分别给范畴、2-范畴、3-范畴；D_k 的 k 与 S^{n−k−1} 的维数互补，k=0 时回到 S^{n−1} 的态空间 | 本篇 p003、p006、p009、p018 |
| 5 | 记号前后一致 | 一处滑动：p010 融合配边句把 to 写成 and（同页图 8 图注作 from … to …；p019 的 pants 句亦作 from S¹×S¹ to S¹），记 E1；× 的写法作者前后一致，不作改动。其余 Q_l/Q_r、V_AB、W_XY、C_XY、F(G,t,C) 前后一致 | 本篇 p004、p007、p010、p019；见 E1 |

### 外部来源

| 来源（URL 或 arXiv 号） | 定位 | 核了什么 |
| --- | --- | --- |
| nLab: extended functorial field theory（https://ncatlab.org/nlab/show/extended+topological+field+theory） | 定义段 | n-extended TFT = 对称 n-张量函子；(d−n)-流形 ↦ R-线性 (n−1)-范畴，支持 S2/S7 的分层 |
| nLab: Rozansky-Witten theory（https://ncatlab.org/nlab/show/Rozansky-Witten+theory） | Feynman rules 段 | 只有 CS 传播子与 trivalent 图，支持 S9 的 CS 类比 |
| arXiv:hep-th/9612216（Rozansky–Witten 原文） | abstract | 「finite type invariant of 3-manifolds」「Riemann curvature ... structure constants」，支持 S9 |
| arXiv:0810.5415（Kapustin–Rozansky–Saulina I） | abstract 与 appendix | 边界条件 = 复 Lagrange 子流形、边界条件成 2-范畴且 1-维缺陷线给态射、Z/2-分次导出范畴的范畴化与矩阵分解，支持 S4/S5/S11/S12 |
| arXiv:q-alg/9709040（Kontsevich） | abstract | 形式性定理把多重向量场 Lie 超代数与 Hochschild 复形联系起来，支持 S12/S13 的 A∞ 类比 |
| arXiv:0905.0465（Lurie） | abstract | Baez–Dolan 配边假设给出扩展 TFT 的分类，支持 §5 与 S16 |
| datasets/ggl19（ggl19/deriv/montonen-olive-parameter-map） | 第 1 步 | MO 在 t 上的作用是 t↦t|τ|/τ；τ=i 时给 t=i↦1，核对 p017 无误 |
| datasets/kw06（kw06/derivations/psi-special-points） | 第 3 步 | t↦1/t 来自定向反转（KW06 eq (3.56)），不是 S-对偶，排除一处误判 |

### 勘误

本稿登记一条 **low**：E1（p010 融合配边的记号滑动，见 `errata.tsv` 唯一数据行）。受影响卡片 `ggl20/concept/defect-k-category` 的 pitfalls 已注明存疑，公式仍按原文写，不写 `corrections`。

- **E1 详述**：原文 p010 写 `gives a canonical bordims from S^{n−k−1}×S^{n−k−1} and S^{n−k−1}`（`bordims` 亦为拼写滑动）。同页图 8 的图注作 `from S^{n−k−1}×S^{n−k−1} to S^{n−k−1}`，p019 的 pants 配边句也作 `from S¹×S¹ to S¹`，可见 `and` 应为 `to`；`×` 是作者在此语境固定使用的写法（记两个 incoming 分支），本篇两处一致，不按 `⊔` 改。判 low 的理由：只有本篇内部的用法对照支持 `and → to`，没有第二处独立文献直接复述这句话；按 BRIEF §9.2，只有一处冲突 ⇒ 记 low，卡片保留原文写法。
- **排除项 1（曾疑 p017 的 t=i↦t=1 是笔误）**：若 MO 只是 t↦1/t，则 t=i 应映到 −i，与原文冲突。但 ggl19 的参数映射卡给出 t↦^Lt = t|τ|/τ，τ=i 时 |τ|/τ = −i，故 t=i ↦ 1，与原文一致；t↦1/t 属于定向反转（kw06 卡，KW06 eq (3.56)）。不记 errata。
- **排除项 2（曾疑 p002 与 p009 的指标矛盾）**：p002 说「n−k 维 ↦ k−1-范畴」，p009 说「(n−k−1)-流形 ↦ k-范畴」，取 k′ = k−1 即同一陈述，非笔误。
- **排版小疵（不计 errata）**：p002 脚注 2 `writiing`；p008/p010 `Kaluza-Klien`；p010 `bordims`；p013 `holomoprhic`；p014 `Schouten-Nijenjuis`；p016 脚注 6 缩写 `ETFT`；p009 `assigns an k-category` 的冠词。这些不影响数学内容，只在术语表备注里留痕。

## 不懂

1. **p012 的量子修正幂次**：原文只说「Ω→λΩ 时第 p 阶修正 ~ λ^{1−p}」，没给推导。我按费曼图数了顶点数，但没算出为什么恰好是 1−p 而不是别的次数；Planck 常数类比是 Ω 的逆这句话我也没完全对上。
2. **p014 的 [β,β] 为何不必为零**：原文说 1-形式楔积反对称、Sym•TY 的括号对称，两者合起来使括号对两个奇元素「整体对称」。我按分次 Lie 括号验算，只能确认它不自动消失，没能写出 [β,β] 的具体表达式。
3. **p015 的次数账**：Z-分次情形只有次数 3 的 MC 解，这一步依赖 C* 作用使 Ω 权重 2、Sym^pTY 放在次数 2p。我算不清为什么「全纯辛形变 = 次数 3 解」，于是 S13 只能照述。
4. **p018 的 g_C[2]**：把 g_C 放在上同调次数 2 的纯偶分次流形上、再取 G_C-等变 B-模型，等变结构与导出范畴的相容性我没搞懂，只能说「原文如此」。
5. **p019–p020 的四块分解**：pants、cup、两个 plumbing fixture 具体怎么粘出任意闭曲面，原文只给图 9，文字没写粘法；我无法复原，故 S16 的「等价类与切法无关」只能照述。
6. **p013 的 c 平移**：矩阵分解对象带常数 c，原文未说明为什么 c 的平移属于等价关系。我按 D² = W2−W1+c 推断 c 与 W 的常数平移同步，但没找到明确陈述。
