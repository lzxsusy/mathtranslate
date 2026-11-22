# 第 12 篇 · Edward Witten《Fivebranes and Knots》（arXiv:1101.3216v2，150 页）

## 1. 骨架（节标题 → 一句话）

| 节 | 页 | 一句话 |
|---|---|---|
| 1 Introduction | 6–17 | CS 的 Wilson 期望值是纽结多项式；Khovanov 同调应实现为某个 4d TFT 的态空间上 Q 的上同调，Euler 特征回到 J(q)。 |
| 1.4.1 Basic Idea | 13–15 | D3-NS5（带 θ）↔ CS on W；经 S-对偶到 D3-D5、再 T-对偶到 D4-D6，才能把路径积分读成 5d 希尔伯特空间上的迹。 |
| 2.1 D3-NS5 with theta | 18–22 | 半 BPS 边界条件由参数 a 刻画，(2.8)(2.9) 是 δX、δA 的边界条件；(2.14) 把 a 与 θ 联系起来。 |
| 2.1.1 Wick rotation | 22 | 欧氏化后边界作用 (2.16)，超对称荷满足 Γ0…Γ9ε=−iε。 |
| 2.2 Twisting | 23–25 | SO′(4) 同时转切向与四个法向，4 个标量变 one-form φ、2 个变复标量 σ；残余 U(1) 生成元 F。 |
| 2.2.2 Comparing | 23–25 | 手征 εℓ、εr 与 t 的关系 (2.20)–(2.28)；(2.28) t²=τ̄/τ 是关键。 |
| 2.2.3 Global formulation | 25–26 | Type IIB on T*V0×R²，D3 包 V0、NS5 包 T*W；W 是特殊拉格朗日截面。 |
| 2.2.4 Wilson loops | 26–29 | 体内无超对称 Wilson 线；边界上取 A_w=A+wφ，(2.40) w=(t−t⁻¹)/2。 |
| 2.3 Localization | 32–33 | 加 Q-恰当项把路径积分局域化到 V±=V0=0。 |
| 2.4 Relation to CS | 33–36 | 边界项化为 iΨCS(A_w)，测度关系 (2.66) 给出 CS 水平移动 k→k+h sign k。 |
| 2.5–2.6 Choice of V | 37–40 | V=W×R⁺ 时 y=∞ 的边界条件由 ρ:π1(W)→G_C 定；W=R³ 时 ρ 平凡。 |
| 3.1 EM duality | 40–42 | G↔G∨、τ∨=−1/(n_gτ)、Ψ∨=−1/(n_gΨ)、q=exp(2πi/(n_gΨ))。 |
| 3.2 Partition function | 42–46 | Z(q)=Σ_s q^{n_s}(−1)^{g_s}；与 CS 比较得 q=exp(2πi/(n_g(k+h sign k)))。 |
| 3.3 Dual boundary condition | 46–48 | G∨ 侧的边界条件是 D3-D5（Dp-D(p+2)），即 regular Nahm pole：φ⃗=t⃗/y+…，t⃗ 为主嵌入。 |
| 3.4 Embedding tangent bundle | 48–50 | 一阶方程迫使 A|_W=ω，ad(E)≅TW（差 spin 结构/π1(W)→Z(G∨)）。 |
| 3.5 Framing anomaly | 50–57 | P 不再拓扑不变；P̂=P−(b/8π)CS_grav，b=Σj(j+1)(2j+1)/(3h∨)=n_g dim G h/6。 |
| 3.6 't Hooft operators | 57–72 | 由沿 S 的奇异模型解定义；SU(2) 完整解、线奇异、双侧解。 |
| 3.7 Framing anomaly for knots | 72–76 | 框架移 1 单位使 CS(ω(j)) 移 −j(j+1)，故 Z 乘 q^{j(j+1)}；P∈Z+j。 |
| 4.1 Lift to 5d | 77–79 | 4d N=4 = 5d 最大超对称 YM 紧化在 S¹；K(V)=H(V) 上 Q 的上同调。 |
| 4.1.2 Bigrading | 79–80 | P（V 上瞬子数）与 F（扭化未破缺 R-对称）给 Z×Z 分次。 |
| 4.2 Procedure | 80–82 | K₀ 以解集 S 为基，Qψ_s=Σ n_st ψ_t（瞬子数矩阵），K=H(K₀,Q)。 |
| 4.2.1 Relation to CS | 82–85 | 只有 y=−1 的指标可算：L(q,−1)=Σ q^{n_s}(−1)^{f_s}；猜想 (4.10) Z^CS=Tr_K q^P(−1)^F。 |
| 4.3 Non-simply-laced | 85–87 | 用 G* 的外自同构 ζ 取 ζ-不变部分，化到 G∨ 的解。 |
| 5 Top-down | 89–122 | 6d (0,2) 沿 M4×D 扭化得 4d TFT；U(1)_D 约化回 5d SYM+D6，给出 (4.10) 的 UV 完备化与 q-分次的几何意义。 |
| 5.3.2 Morse theory | 108–110 | 5d 方程是 Morse 流方程，F 是正则化 Morse 指标，故给真正的 Z 分次。 |
| 5.4 q-grading | 114–120 | q=∫⋆J；紧支面算子使 ΔP̂=jχ(Σ)+j(j+1)Σ∩Σ。 |
| 6 Another path | 123–143 | 用余维 2 单值化缺陷重走：CS↔N=4+Hitchin 缺陷，S-对偶后再升到 5/6 维。 |
| 6.5 Using the duality | 141–143 | 只有 R³ 的 unknot 能算：J=(−q^{j+1}+q^{−j})Σ_{t≥0}q^t。 |

## 2. 主定理清单

1. **(1.9)**（p10）J(q;L)=Tr_{𝒦(L)}(−1)^F q^P：Jones 多项式是 Khovanov 同调的分次 Euler 特征。性质而非定理，作为全文目标。
2. **猜想 (1.9)/(4.10)**（p10, p84）：CS 配分函数等于 K(W³×R⁺)=H(V) 上 q^P(−1)^F 的迹；作者用 K 与 𝒦 区分，明说未证明相等（p77、p85 "conjecturally"）。
3. **(2.45)/(2.49)**（p30）：典范参数 Ψ=θ/2π+(4πi/g²)(t−t⁻¹)/(t+t⁻¹)；D3-NS5 物理参数下 Ψ=|τ|²/Re τ，恒为实。
4. **(2.28)**（p25）：t²=τ̄/τ（分子带横杠；txt 抽取丢杠，PDF p25 已放大核对）。
5. **(2.66)–(2.68)**（p36–37）：测度重写使 CS 水平移动 k→k+h sign(k)，即 Ψ=k+h sign(k)。
6. **(3.13)**（p42）：q=exp(2πi/(n_g(k+h sign k)))，与 (1.3) 的 q=exp(2πi/(k+h)) 在 k>0、单连通时一致。
7. **(3.44)–(3.45)**（p57）：b=Σ j_i(j_i+1)(2j_i+1)/(3h∨)=n_g dim G h/6；G₂ 时两边=336。
8. **(5.36)**（p105）：5d 超对称方程 F⁺−¼B×B−½D_yB=0、F_{yμ}+D^νB_{νμ}=0；其解集是 K 的经典基。
9. **(5.62)**（p119）：ΔP̂=jχ(Σ)+j(j+1)Σ∩Σ；框架移 1 单位给 q^{j(j+1)}，与 §3.7 一致。
10. **(6.20)/(6.24)**（p142）：unknot 的 J(q;K₀,j)=(−q^{j+1}+q^{−j})Σ_{t≥0}q^t。

## 3. 与已译文献接口

- **01（KW06, hep-th/0604151）**：本文 §2 的扭化、t、Ψ 直接取自 KW06；(2.45) 与 KW06 (3.50) 逐项相同，(2.28) 与 KW06 (3.52) 互逆。KW06 的 q=−t²（其 (5.12)）与本文 q 不同义，勿混。
- **02（分歧与几何 Langlands）**：§3.3 的 Nahm pole 与 tame/wild ramification 是同一套边界条件语言；本文的 regular Nahm pole 对应主嵌入。
- **06（镜像对称与 Hitchin）**：§4–§5 的 4d TFT 在 W 上的边界条件与 Hitchin 模空间的 A/B-膜词典相通；§6.2 直接用 Hitchin 方程 (6.3) 定义单值化缺陷。
- **11（路径积分新视角）**：本文 §2.4 把 4d 路径积分写成 3d "contour" 积分，测度因子 (2.66) 的讨论与路径积分定义的细节相关。
- **16（几何内窥）**：G∨ 与 G* 的外自同构 ζ（§4.3、§5.5）即内窥的群论核心；A-D-E 四对列在 p121 脚注 40。
- **23（四维规范场论中的纽结不变量）**：同一条 D3-NS5/D3-D5 路线，本文是其在 Khovanov 方向上的展开。
- **28（Hitchin 量子化与 Hecke 特征层）**：§1.4.3 p17 明说几何 Langlands 的 4d TFT 在边界 W 上与 CS 相关，Ψ 即 CS level；Khovanov 同调曾用几何 Hecke 变换的模空间定义。
- **36（Langlands 与共形场论讲义）**：整体图景与术语（S-对偶、Langlands 对偶群、't Hooft 算子）以此为准。

### 3.1 术语与旧卡的撞名处理（term_index 结果）

- `ggl12/concept/khovanov-homology` 初名 "Khovanov 同调与双分次"，与 `functoriality:functoriality/concept/khovanov-homology`（Khovanov homology）撞英文名；按"译名以旧卡为准、同概念不重复造卡"，旧卡讲函子性（cobordism 映射），本卡只讲双分次与 Euler 特征（(1.8)(1.9)），故本卡改名为"Khovanov 同调的双分次结构"、alias 加限定，语义上更专，不另立重复卡。
- `ggl12/concept/nahm-pole-boundary-condition` 初名 "Nahm 极点边界条件"，与 `ggl22:ggl22/concept/nahm-pole-bc`（Nahm 极点边界条件）撞中文名；旧卡是同一概念的一般定义，本卡改题"正则 Nahm 极点与主嵌入"，只强调 principal embedding 与 (3.17)–(3.21) 的推导，related 不跨包（包外 id 不能写），故记在这里备查。
- 其余 16 张卡 term_index 无撞名；术语表 terms.tsv 的定名与旧卡一致（twist=扭化、eigenbrane=特征膜、Hecke eigensheaf=Hecke 特征层、't Hooft 算子不译、BPS 不译、canonical coisotropic brane=典范余各向同性膜、ramification=分歧）。

## 4. 核对与勘误

### 4.1 外部校正动作清单（XREF 五项逐条回填）

| # | 核什么 | 怎么核 | 结论 |
|---|---|---|---|
| 1 | 主定理陈述与符号 | 摘要 + KW06 + nLab + 1108.3103 | 主张是"候选"K(V)，作者明说未证 K=𝒦；摘要"manifestly invariant description"与 (4.10) 一致。未见夸大到"证明"。 |
| 2 | 关键公式系数/符号/指数 | KW06 (3.50)(3.52)；nLab；本篇 (2.49)(3.5)(2.41) 互验 | (2.45)=(3.50) 逐项一致；(2.28) 与 (3.52) 互逆并推出 (2.49)；(2.40)(2.41) 复算一致。 |
| 3 | 命题编号与交叉引用 | 抽查 (2.52)→(3.27)、(3.11)→(3.30)、(5.51)→(3.33)、(5.62)→§3.7 | 指向正确；未见错引。 |
| 4 | 数值/维数一致性 | (3.21) 维数求和；G₂ 336；ν/2 半整性；k+h sign k | (3.21) Σ(2j_i+1)=dim G 对 SU(N) 成立；G₂ 的 j=1,5、n_g=3、dim=14、h=h∨=4 使 (3.45) 两边=336；ν 分量给 P∈Z+ν/2，j=1/2 时与 q^{1/2} 一致。 |
| 5 | 记号前后一致 | 通读 §2–§5 | 唯一陷阱：本文 h 指 G 的对偶 Coxeter 数、h∨ 指 G∨ 的（p42 脚注 14 明说，与常见记号相反）；全文自洽。t、Ψ、q 在 §2/§3/§4 同义（q 与 KW06 的 q 不同义）。 |

### 外部来源

| 来源 | 定位 | 核了什么 |
|---|---|---|
| Kapustin–Witten, hep-th/0604151（库内 01） | §3.5，eq. (3.50)–(3.52) | Ψ=(τ+τ̄)/2+((τ−τ̄)/2)(t−t⁻¹)/(t+t⁻¹) 与本文 (2.45) 逐项相同；t²=−(Ψ−τ̄)/(Ψ−τ) 与 (2.28) 互逆，代 Ψ=|τ|²/Re τ 得 t²=τ̄/τ。 |
| nLab, "Khovanov homology"（2025-11-10 修订） | §Interpretation in QFT | 复述 (D3-NS5)→S(D3-D5)→T(D4-D6) 链与"圆周为欧氏时间、路径积分给 Tr(−1)^F e^{−βH}"，支持 §1.4.1/§4.1；并记 Φ_Σ:𝒦(K)→𝒦(K′)。 |
| Witten, arXiv:1108.3103（库内 13） | p8、p10 | 作者本人在后续综述中仍把 K(V) 的 Q-上同调称为 Khovanov 同调的 candidate，Z×Z 分次与 q-分次说法与本文一致。 |
| arXiv:1101.3216 abs 页（v2 元数据，XREF 抓取） | comment 行 | v2 2011-08-11，"numerous small corrections from v. 1; 148 pp"，确认所据为 v2；PDF 150 页含 1 页 arXiv 封面，印刷页码 1–149。 |
| 本篇内部数值自检（不计独立来源） | p57 (3.44)–(3.45) | G₂：j=1,5，n_g=3，dim=14，h=h∨=4，左右=336；复算成立。 |

### 勘误

1. **E1（low，p20）**：Neumann 极限句写 "D3Xa = F3µ = 0"，同页 (2.8) 的指标是 c，a 是同页的边界条件参数；按上下文应为 D3Xc（或 D3X⃗）=0。仅内部证据，按 §9.2 记 low，卡片保留原文写法并在 provenance_note 标「存疑（见 errata E1）」。
2. **非笔误、但抽取文本会误读的两处**：(2.28) 的横杠在 txt 抽取中丢失（PDF p25 放大图确认是 τ̄/τ）；p20 的 "D3-NS5 与 D3-\overline{NS5}" 上划线在 txt 中丢失。二者均按 PDF 判读，未记入 errata。
3. 除此之外本稿未发现笔误。v2 的 "numerous small corrections" 已在该版内，无法用 v1 逐条比对（本机只有 v2）。

## 5. 不懂 / 遗留

1. §5.3.2 Morse 函数 S（(5.42)）的构造，以及"CS 只 circle-valued 故 Floer 理论 Z/4hZ 分次、本文 S 实值故 F 给真 Z 分次"这一步，只跟到结论，w 项的抵消未验算。
2. §3.6.4–3.6.5 的 SU(2) 显式解（(3.61) ansatz、r=−1 的线奇异解）没有逐步验算，只能确认其满足 (3.46) 的定性描述。
3. §5.4.1 (5.53) 的系数 1/4 与 p1 归一化的换算：按 p1=(1/8π²)Tr F∧F 能对上，但未能独立核 p1 的约定。
4. §6.3–6.4（p127–140）只读了标题与结论，未细读 S-对偶与升维的推导；notes 中按"未细读"处理。
5. (3.16) 的矩阵 m_{ρ∨,ρ} 在 W 非 R³ 时没有显式形式，作者本人也承认；无法判其对错。
6. §3.5.3 的 CS_grav 用 two-framing 定义，CS_grav=4CS(ω) 的系数 4 依赖约定；未与 [77] 原文核对。
