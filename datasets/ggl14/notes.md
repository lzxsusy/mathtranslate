# 第 14 篇 · Witten《Jones 多项式与 Khovanov 同调两讲》首轮卡片化

- 英文题名：Two Lectures on the Jones Polynomial and Khovanov Homology
- 作者：Edward Witten；arXiv:1401.6996v1 [math.GT]，2014-01-27，26 页
- 底本：pdf/14_X_1401.6996.pdf；文本 txt/14/p001–p026.txt
- 页码约定：本文所有页码均为 **PDF 页序**，PDF 页 = 印刷页 + 1（p002 页脚为 1，p025 页脚 24，p026 页脚 25）。
- 卡片：概念 10 张、推导 4 张；id 前缀 `ggl14/`。

## 1. 骨架

| 节 | 页（PDF） | 一句话 |
| --- | --- | --- |
| 摘要 | p1 | 两步走：把三维 CS 改写成四维理论，再用电磁对偶把 q 认成瞬子数；第二讲加第五维得 Khovanov 同调。 |
| 第一讲 · 顶点模型 | p2–p3 | 纽结投影切段标 ±，交叉权重取 q 的函数，求和得框架纽结不变量。 |
| 第一讲 · CS 与 q | p3–p5 | CS 是唯一可写的规范不变局部泛函，k 须整数；G∨=SU(2) 二维表示给 Jones 多项式，q=exp(2πi/(k+2))。 |
| 第一讲 · 大 k 与复临界点 | p5–p7 | 大 k 渐近由平坦联络（复化后是复平坦联络）给出；volume conjecture 的复临界点在纽结补集上。 |
| 第一讲 · 玩具模型与解析延拓 | p7–p9 | Bessel 积分的围道形变给出非整数 k 的解析延拓；一般形式是 ∫dz/(2πiz)e^{kF(z)}。 |
| 第一讲 · Lefschetz 顶针 | p9–p10 | h=Re(kF) 作 Morse 函数，临界点给顶针，顶针构成相对同调基；整数 k 时两顶针相消。 |
| 第一讲 · CS 的梯度流 | p10–p12 | CS 梯度流是规范固定的瞬子方程，复化后即 KW 方程；顶针积分 (1.25) 是 Jones 的四维写法。 |
| 第一讲 · 电磁对偶 | p12–p14 | 对偶换群 G∨↔G 与耦合 τ↔−1/(n_gτ)；模空间维数 0，只需带符号计数，回应 Atiyah 的挑战。 |
| 第二讲 · KW 方程与瞬子数 | p14–p15 | 在 M=W×R₊ 上数 KW 解，按瞬子数 P 分阶，b_n 为带符号个数，Z(q)=Σb_nq^n。 |
| 第二讲 · V、Q、H | p15–p16 | 解空间 V 上有微分 Q，H=kerQ/imQ 是 Z×Z 分次拓扑不变量，Z(q) 只是其 Euler 特征。 |
| 第二讲 · 五维提升 | p16–p18 | φ_y 换成 D/Dt，四维解成五维梯度流临界点，流线计数给 Q 的矩阵元。 |
| 第二讲 · even/odd Khovanov | p18–p19 | 上同调可作 Z₂ 扭化，π₄(G)=Z₂ 仅对 Sp(2n)，故只有 G∨=SO(2n+1) 一族有两版本。 |
| 第二讲 · Nahm 极点 | p19–p20 | Nahm 方程奇异解 t_i/y 嵌进 KW 方程成 φ_i=t_i/y，即 y→0 的边界条件；空链环同调秩 1。 |
| 第二讲 · 有纽结的边界条件 | p20–p21 | 沿 K 平移不变约化到 R²×R₊，模型解依赖 R∨，奇异在边界上余维 2。 |
| 第二讲 · 曲面与态射 | p21–p23 | 五维里奇异支在二维曲面 Σ 上，正是链环配边的态射；G∨=SU(2) 时期望 Fukaya–Seidel 范畴。 |
| 参考文献 | p24–p26 | [1]–[47]，含 Jones 1985、Witten 1989、KW 2006、Khovanov 2000、Mazzeo–Witten 2013。 |

## 2. 主定理清单

| 编号 | 页 | 一句话 |
| --- | --- | --- |
| (1.1) | p3 | CS(A)=1/(4π)∫Tr(A∧dA+⅔A∧A∧A) 是唯一可写的规范不变局部泛函，Tr 归一使 CS 模 2πZ 不变。 |
| (1.2) | p4 | Z_k(W)=1/vol∫DA e^{ikCS(A)}，k 必须是整数，W 须带 framing。 |
| (1.3)(1.4) | p4 | Wilson 圈 W_{R∨}(K)=Tr_{R∨}P exp(−∮_K A)，插入路径积分得纽结不变量。 |
| (1.5) | p4 | G∨=SU(2)、R∨=二维表示时该不变量是 Jones 多项式，取值 q=exp(2πi/(k+2))；一般群见脚注 4。 |
| 脚注 1 | p2 | 换框架使顶点模型的求和乘 q^{3/4} 的整数次幂；R³ 中纽结有 canonical framing。 |
| (1.15)(1.18) | p9–p10 | 顶针的临界点条件 1+λ(e^w+e^{−w})=0，单顶针贡献 I_p∼e^{kF(p)}(c₀k^{−1/2}+…)。 |
| (1.22) | p11 | CS 的梯度流 ∂A/∂t=−⋆₃F 是 F⁺=0 的规范固定形式，继承四维对称性。 |
| (1.24) | p11 | KW 方程 F−φ∧φ=⋆d_Aφ、d_A⋆φ=0；Hitchin 方程的四维表亲。 |
| (1.25) | p12 | Z_k(R³;K,R∨)=1/vol∫_{Γ₀}DA e^{ikCS(A)}W_{R∨}(K)；CS 在 Γ₀ 单值，故 k 无需整数。 |
| (1.26) | p13 | Z(q;K,R∨)=Σ_n b_n q^n，回应 Atiyah 要 q 对应瞬子数的挑战。 |
| (2.2) | p14 | P=(1/8π²)∫_M Tr F∧F；紧无边界四维流形上取整，等于 c₂。 |
| (2.5)(2.6) | p16 | Z(q)=Σ(−1)^{f_i}q^{n_i}=Tr_V(−1)^Fq^P=Tr_H(−1)^Fq^P；H 才是拓扑不变量。 |
| (2.7)–(2.9) | p17 | φ_y→D/Dt 等替换把 KW 方程升到五维，仍是椭圆方程，且是梯度流 dΦ/dt=−δΓ/δΦ。 |
| (2.10)(2.11) | p18 | Q|i⟩=Σ_{f_j=f_i+1}n_ij|j⟩；n_ij 数五维插值解，带费米子行列式符号。 |
| π₄(G) 表 | p19 | π₄(G)=Z₂ 当 G=Sp(2n) 或 Sp(2n)/Z₂（n≥1），否则 0；故 Khovanov 同调仅在 G∨=SO(2n+1) 一族有两版本。 |
| (2.12)–(2.15) | p20 | Nahm 方程 dX₁/dy+[X₂,X₃]=0；奇异解 X_i=t_i/y；嵌入 KW 后即 φ_i=t_i/y 的 Nahm 极点。 |
| 空链环 | p20 | [44] 证明 R³×R₊ 上 Nahm 极点解唯一，故空链环的 Khovanov 同调秩为 1。 |
| 约化方程 | p21 | 有纽结 K 时沿 K 平移不变，约化到 R²×R₊；模型解依赖 R∨，奇异在边界上余维 2。 |

## 3. 与已译文献接口

| 本篇位置 | 接口文献（id） | 对应内容 | 差异 / 注意 |
| --- | --- | --- | --- |
| p2 脚注 1、p4 | ggl12/concept/framing-anomaly | 框架改变乘 q^{3/4} 的整数幂 | ggl12 从五膜/六维角度讲 framing anomaly，本篇只作顶点模型的脚注。 |
| p3–p4 (1.1)–(1.5) | ggl12/concept/chern-simons-knot-invariant | CS 作用量与 Wilson 圈给 Jones 多项式 | 符号一致；本篇明确写 q=exp(2πi/(k+2))。 |
| p13 电磁对偶 | ggl12 notes §3.1（EM duality，τ∨=−1/(n_gτ)、q=exp(2πi/(n_gΨ))） | 交换群与耦合 | 本篇写 τ∨ replaced by τ=−1/(n_gτ∨)，与标准式互为逆写；见 §4 记号陷阱。 |
| p13 | kw06 kw/concept/s-duality；kw06 kw/concept/gno-dual-group | S-对偶与 GNO 对偶群 | kw06 是原始文献的卡片化，本篇是综述式引用。 |
| p12 扭化 | gtgl15/concept/n4-sym-partial-tqft；ggl12/concept/twisting-n4 | 4d N=4 的部分拓扑扭化 | 本篇只引 [17]，未展开扭化细节。 |
| p14–p16 V/Q/H | ggl12/concept/khovanov-homology | Khovanov 同调作为 Q 的上同调 | ggl12 侧重五膜构造，本篇给出 KW 解空间版本。 |
| p17–p18 五维 | ggl12/concept/khovanov-trace-from-5d；ggl12/deriv/khovanov-trace-from-5d | 五维指标 Tr_H(−1)^F e^{−βH} | 同一构造；本篇把 5d 写成 X=R×M 并给出 Q 的矩阵元。 |
| p20–p21 Nahm 极点 | ggl12/concept/nahm-pole-boundary-condition；ggl22/concept/nahm-pole-bc | Nahm 极点为边界条件 | 记号一致（φ_i=t_i/y、ϱ 主嵌入）。 |
| p18–p19 π₄ 与两版本 | ggl12/concept/non-simply-laced-orbifold | G∨=SO(2n+1) 与 G=Sp(2n) 配对 | 本篇 p14 误作 Sp(2n+1)，正是 errata E1 的依据之一。 |
| p9–p10 顶针 | ggl13/concept/complex-cs-morse-function；ggl13/deriv/complex-cs-gradient-flow | 复 CS 的 Morse 函数与梯度流 | ggl13 是同一作者更早的解析延拓长文，本篇第一讲是其摘要版。 |
| p5–p7 volume conjecture | ggl10/concept/volume-conjecture；ggl10/concept/lefschetz-cycle；ggl10/concept/stokes-jumping | 体积猜想的复临界点与顶针跳变 | 本篇只作评述并明说未解决。 |
| p23 Fukaya–Seidel | ggl20/concept/…（变界线算子 2-范畴）；seidel（A∞ 代数） | 范畴化与 Fukaya–Seidel 范畴 | 本篇只用一句话预期，未构造该范畴。 |

### 3.1 term_index 撞名处理

`tools/term_index.py check out/14_ggl14/cards` 通过（退出码 0），报出 4 处撞名，均按「不同文献、不同 id」处理，跨篇对应写在上面接口表里：

| 本篇卡 | 撞名对象 | 处理 |
| --- | --- | --- |
| ggl14/concept/chern-simons-knot-invariant | ggl12/concept/chern-simons-knot-invariant（同名同题） | 保留各自 id；本篇按 (1.1)–(1.5) 与 q=exp(2πi/(k+2)) 立卡，ggl12 按五膜/六维立卡。 |
| ggl14/concept/five-dimensional-lift | ggl12/concept/khovanov-trace-from-5d（同一 alias「five-dimensional lift」） | 保留各自 id；本篇讲 X=R×M 与 Q 的矩阵元，ggl12 讲五维指标。 |
| ggl14/concept/lefschetz-thimble | seidel/concept/thimble（同一术语） | 保留各自 id；译名统一作「Lefschetz 顶针」，与 seidel 包旧译一致。 |
| ggl14/concept/nahm-pole | ggl13/concept/nahm-pole-boundary-condition（同一 alias） | 保留各自 id；本篇 (2.12)–(2.15) 为嵌入推导，ggl13 为解析延拓长文的边界条件。 |

与 ggl12 撞名的概念不合并 id：两篇是不同文献，术语表以本篇 p 页为准。中文定名沿库内既有约定：「Lefschetz thimble」作 **Lefschetz 顶针**（不用「指套」），「Stokes phenomenon」作 **Stokes 现象**，「twist」作 **扭化**，`'t Hooft`、`BPS` 不译。

**收尾复核**：初版 `term_index.py check` 虽以退出码 0 结束，却列出 4 处撞名（CS 卡与 ggl12 同名同题，五维提升/顶针/Nahm 的裸 alias 分别撞 ggl12/ggl13/seidel）。按「同概念不重复造卡、译名以旧卡为准」逐条判断后，保留各卡 id 与内容，只给标题/alias 加限定词：CS 卡改题「Chern–Simons 配分函数与 Wilson 圈」，五维提升 alias 作 "five-dimensional lift with time direction"，顶针 alias 作 "Lefschetz thimble in complex CS"，Nahm alias 作 "Nahm pole boundary condition from KW equations"。重跑 0 撞名，lint/verify 复跑仍 0 问题；判断过程见 trace 第 16 条。

## 4. 核对与勘误

### 4.1 五项外部校正动作清单

| 项 | 做法 | 结果 |
| --- | --- | --- |
| 1 主定理陈述与符号 | 渲染 PDF p3/p4/p16/p20 与原 txt 逐式对照；与 arXiv 摘要、INSPIRE 元数据比对 | (1.1)(1.4)(1.5)(2.4)(2.5)(2.12)(2.13) 与 txt 一致；摘要与 arXiv abs 逐句一致。 |
| 2 关键公式系数/符号/指数 | 渲染 p2 脚注 1、p3 fig.2 十二格权重、p4 脚注 4、p13 对偶句 | q^{3/4} 无误；fig.2 权重为 q^{1/4},q^{1/4},q^{−1/4},q^{−1/4}/q^{−1/4},q^{−1/4},q^{1/4},q^{1/4}/(q^{1/4}−q^{−3/4}),0,0,(q^{−1/4}−q^{3/4})，与 txt 抽取顺序一致；脚注 4 印刷缺一对括号（E2）；p13 的 τ 句只是写法次序问题，非笔误。 |
| 3 命题编号与交叉引用 | 逐页抽取 (x.y) 式号并与 locator 对照 | 本篇式号为 1.1–1.26、2.1–2.15，无 (2.16)：p19 的 π₄(G) 表在原文中**没有编号**（草稿曾误记为 (2.16)，已改）。 |
| 4 数值/维数一致性 | fig.1 的 3 交叉+2 极大+2 极小=7 段、2^7 项；π₄ 表与标准同伦论 | INSPIRE 的 figure caption 明写 7 与 2^7，与 p2 正文一致；π₄(G)=Z₂ 仅辛群，与 Bott 结果一致。 |
| 5 记号前后一致 | 通篇比对 G∨/G 的用法、Sp(2n) 的维数、术语拼写 | p14 两处问题：`G = Sp(2n+1)`（E1，high）与 `Stieffel-Whitney`（E3，low）；其余记号前后一致。 |

### 外部来源

| 来源 | 定位 | 核对内容 |
| --- | --- | --- |
| arXiv abs 页 1401.6996 | https://arxiv.org/abs/1401.6996 | 标题、摘要与 p1 逐句一致；Comments "26 pp"；仅 v1（2014-01-27）；Subjects math.GT; hep-th; math.DG。 |
| INSPIRE recid 1278911 | https://inspirehep.net/api/literature/1278911 | number_of_pages 26、preprint_date 2014-01-27、texkey Witten:2014xwa；references 47 条与原文 [1]–[47] 一一对应；figures 的 LaTeX caption（含 3+2+2=7、2^7）与原文图注一致。 |
| nLab "Khovanov homology"（2025-11-10 修订） | §Interpretation in QFT | 圆周当欧氏时间时带圆路径积分 = 5d 的 Tr_H(−1)^F e^{−βH}，Khovanov 同调是 H 本身（引 Witten 2011 p.14）；并记 Φ_Σ:𝒦(K)→𝒦(K′)。支持本篇 p16–p18。 |
| nLab "Chern-Simons theory" | 作用量与 Wilson 圈条 | 复述 exp(i∫cs(A))、Z∝∫DA W(Σ,R,A)e^{iS_CS(A)}、k 为 level；为 (1.1)(1.4) 提供独立表述。 |
| 库内 ggl12 卡 | ggl12/concept/nahm-pole-boundary-condition、ggl12/concept/khovanov-trace-from-5d、ggl12/concept/framing-anomaly | 对 Nahm 极点、5d→Khovanov、framing 因子作独立复述；其中对偶对表（G∨=SO(2n+1) ↔ G=Sp(2n)）是 E1 的第二依据。 |
| 库内 kw06 卡 | kw/concept/s-duality（pages [11,16]） | 定义「把 τ 变为 −1/(n_gτ)、把 G 换成 Langlands 对偶群」，与本篇 p13 对偶句一致。 |

### 勘误

| 序 | 位置 | 原写法 | 订正 | 置信度 |
| --- | --- | --- | --- | --- |
| E1 | p14 §2 首段 | `G∨= SO(2n+1) and G = Sp(2n+1), or vice-versa` | `G = Sp(2n)`（古典群中无 Sp(2n+1)；同篇 p19 的 π₄ 表与正文均作 Sp(2n)） | high |
| E2 | p4 脚注 4 | `q = exp(2πi/n_g (k + h∨))` | `q = exp(2πi/(n_g(k + h∨)))`（n_g 与 (k+h∨) 同在分母） | medium |
| E3 | p14 §2 首段 | `there is no second Stieffel-Whitney class` | `Stiefel-Whitney` | low |

三条均已登记到 errata.tsv。E1 波及卡片 ggl14/concept/even-odd-khovanov（已加 corrections），E2 波及 ggl14/concept/dual-instanton-q（已加 corrections）；E3 纯拼写、不波及卡片，状态 wontfix。

另有一处**不是笔误**但极易误判：p13 作 `coupling parameter τ∨ replaced by τ = −1/(n_gτ∨)`，与常见写法 τ∨=−1/(n_gτ) 互为逆写，且 n_g 对 G 与 G∨ 相同，故自洽；txt 抽取把该句压平成乱序（`τ ∨replaced by τ = −1/ngτ ∨`），不可直接用作 quote。同类压平还有 p4 的 (1.5)（txt 作 `q = exp 2πi k + 2`）与 p2 的 `2^7`（txt 作 `27`）。

## 5. 不懂 / 遗留

- **不懂**：五维方程的紧性为何仍未证明（作者只说「certainly elliptic」），以及即使有紧性，Q²=0 与 H 的不变性该如何严格补全。
- **不懂**：even/odd Khovanov 与超群 OSp(1|2) 的对应（脚注 11 引 [38][39]），本文只说「将物理地探讨」。
- **不懂**：G∨=SU(2) 时预期的 Fukaya–Seidel 范畴，其靶空间（R³ 上单极子模空间）与超势如何精确编码纽结位置；本篇只给一句话，未构造。
- **未核**：[44]（Mazzeo–Witten）的椭圆性与唯一性证明、[21] §3.6 的闭式模型解、[38][39] 的 even/odd 细节，本包均只转述引用。
- **遗留**：p23 明说「要解三维约化方程」，本文未解；c 移位的具体值未算；volume conjecture 作者自称未解决。
