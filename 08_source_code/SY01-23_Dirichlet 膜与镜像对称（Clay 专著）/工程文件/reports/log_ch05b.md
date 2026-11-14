# ch05 后半 校订日志（rv-ch05b）

负责文件：`chapters/ch05b.tex`（= 原 ch05.tex 第 2221 行起；**ch05b 行号 = 原行号 − 2220**）
负责页码：PDF 367–429（§5.4.5.2 起至章末）
对照块目录：`review/chunks/ch05/`

## 已核对范围

| 块 | 页码 | 状态 | 段落 id 区间 |
|---|---|---|---|
| p363-372.txt | 367–372（跳过 ≤366） | ✅ | ch05-5.4.5.2-002 … ch05-5.4.6.1-002 |
| p373-382.txt | 373–382 | ✅ | ch05-5.4.6.1-003 … ch05-5.5.4.1-002 |
| p383-392.txt | 383–392 | ✅ | ch05-5.5.4.1-003 … ch05-5.5.7-007 |
| p393-402.txt | 393–402 | ✅ | ch05-5.5.7-008 … ch05-5.6.3-intro-002（(5.183) 止） |
| p403-412.txt | 403–412 | ✅ | ch05-5.6.3-intro-003 … ch05-5.8.1-005（书内 p393–402） |
| p413-422.txt | 413–422 | ✅ | ch05-5.8.1-006 … ch05-5.9.1.3-004（书内 p403–412） |
| p423-429.txt | 423–429 | ✅ | ch05-5.9.2-001 … ch05-5.9.4-015（书内 p413–419，第5章末） |

## 改动记录

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 1 | ch05-5.4.5.3-001 / ch05b L26 | "the resulting moduli space is the set of θ-stable configurations as defined in §4.7.3" | 所得模空间，以§4.7.3 定义的 θ 稳定配置为其稳定部分，并在墙上包括多稳定配置。 | 所得模空间，就是§4.7.3 定义的 θ 稳定配置的集合。 | 误译 | 原书无"稳定部分""墙上包括多稳定配置"之说；"is the set of"被译成"以…为其稳定部分"，判断走偏，且多出原文内容 |
| 2 | ch05-5.4.5.3-003 / ch05b L36 | "One such term may be added for each unbroken U(1) of the gauge group" | 规范群中心的每个 U(1) | 规范群的每个未破缺 U(1) | 误译 | unbroken（未破缺）误作"中心"；FI 项对应于未破缺的 U(1) 因子 |
| 3 | ch05-5.4.5.3-004 / ch05b L42, L44 | (5.108) diag(ζ1,…,ζ1, ζ2,…)，下括注 dim(V1)、dim(V2)；"each ζi appearing mi times" | 1_{ρ_i⊗C^{d_i}}；"重复 d_i^2 次" | 1_{C^{d_i}}；"重复 d_i 次" | 数学 | 原书 (5.108) 每个 ζ_i 只重复 dim(V_i)=d_i 次（p358 图版下括注 dim(V1)），且 (5.119) 中 θ_i 乘的是 m_i×m_i 单位阵；译稿把单位阵放到整个等型块 ρ_i⊗C^{d_i} 上，块大小变成 d_i²，错 |
| 4 | ch05-5.4.5.3-006 / ch05b L54, L56 | "The result is, at least in a linear approximation for very small blow-ups, (5.110) a_C = Σ χi(C) ζi" | "对于很小的爆破，至少在线性近似和相应实模参数方向上，其关系由特征标变换给出；按上述每个等型块上标量 ζ_i 的归一化，写为"；a_C=Σ d_i χ_i(C) ζ_i | "其结果是，至少对于很小的爆破，在线性近似下，"；a_C=Σ χ_i(C) ζ_i | 数学 | 原书 (5.110) 无 d_i 因子；译稿为迁就上条错加的归一化而加了 d_i 与自创说明，一并复原 |
| 5 | ch05-5.4.5.3-007 / ch05b L61–L65 | "since the trivial representation is not present (it is not a twisted sector), (5.111) 0 = Σ ζi" | "结合正则表示中的迹条件，得到 0=Σ d_i² ζ_i"；末句"对于 Abel 群，所有 d_i=1，这就是 Σ ζ_i=0" | "于是"；0=Σ ζ_i；删去末句（该句随 d_i² 一起失效） | 数学 | 原书 (5.111) 为 0=Σ ζ_i，无任何 d_i 因子 |
| 6 | ch05-5.4.5.5-001 / ch05b L123, L125 | "each ζi appearing mi times… (5.115) Σ dim(Vi) ζi = 0" | "重复 m_i d_i 次"；Σ m_i d_i ζ_i=0 | "重复 m_i 次"；Σ d_i ζ_i=0（按原书 dim(V_i)=d_i） | 数学 | 译稿系统性把 m_i 换成 m_i d_i；原书明言出现 m_i 次，(5.115) 印的是 dim(V_i)（=d_i，因 d_i 已在本章定义为 dim ρ_i） |
| 7 | ch05-5.4.5.5-003 / ch05b L136, L140, L142, L145 | (5.116) diag(…θ1…θ1…) 下括注 m1,m2；(5.117) Σ(ζi−θi)²；(5.118) θi = ζi − Σ mj ζj / Σ mj | 1_{ρ_i⊗C^{m_i}}；Σ m_i d_i(ζ_i−θ_i)²；Σ m_i d_i θ_i=0；θ_i=ζ_i−(Σ m_j d_j ζ_j)/(Σ m_j d_j) | 1_{C^{m_i}}；Σ(ζ_i−θ_i)²；Σ d_i θ_i=0；θ_i=ζ_i−(Σ m_j ζ_j)/(Σ m_j) | 数学 | 同上条：原书三式均无 d_i 权因子（p360 图版逐字核对）；θ_i 重复 m_i 次即单位阵取在 C^{m_i} 上 |
| 8 | ch05-5.4.5.5-004 / ch05b L150, L153 | "Then (5.116) becomes (5.119) Σ ZaZa† − Σ Za†Za = θi id" | "把不可约表示因子的迹吸收到顶点参数中，记 ϑ_i=d_i θ_i，则方程成为…= ϑ_i id" | "则方程成为…= θ_i id" | 数学 | 原书 (5.119) 右端就是 θ_i id；译稿自创 ϑ_i=d_i θ_i，等于把稳定性参数整体缩放 d_i，与 King 原文及 (5.120) 不符 |
| 9 | ch05-5.4.5.5-005 / ch05b L159 | "(5.120) θ(W) = Σ θi ni" | θ(W)=Σ ϑ_i n_i = Σ d_i θ_i n_i | θ(W)=Σ θ_i n_i | 数学 | 原书 p361 明确 θ(W)=Σ θ_i n_i；ϑ_i 系译稿自创（见上条） |

## 改动记录（第 2 块：p373–382）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 10 | ch05-5.4.6.2-002 / ch05b L224–229 | "these are controlled by the symmetric invariant d : (ad* H)^3 → R of H, present for SU(n) with n ≥ 3. In terms of an explicit matrix representation tR : ad H → Mat(C), anomaly cancellation requires Tr tR = 0; Tr t3R = 0. This is automatic for R real, but otherwise is very restrictive." | "局部规范反常由 $H$ 的对称三次不变量控制…反复要求，对相应生成元…并对三次项作相应对称化。对于实表示 $R$，这些局部条件自动满足…理论还须满足可能存在的整体反常条件。" | 补出 $d\colon(\operatorname{ad}^*H)^3\to\mathbb{R}$ 与 $t_R\colon\operatorname{ad}H\to\operatorname{Mat}(\mathbb{C})$；删"局部"限定、"对相应生成元"、"并对三次项作相应对称化"及整句"理论还须满足可能存在的整体反常条件" | 漏译＋多出原文 | 原书的对称不变量 d 与矩阵表示的定义域被整体略去；"局部""整体反常"两句原书无，属译者增补（Tr t_R³ 本身已是全对称，无需再对称化） |
| 11 | ch05-5.4.6.3-002 / ch05b L246 | "The non-renormalization theorem still allows a non-trivial beta function for W and thus quantum corrections, but it implies that these are exponentially small in the gauge coupling." | …呈指数微小。**此外，若把场作规范化，物理超势耦合仍可通过场的反常维数获得微扰尺度依赖。**指数微小的修正… | 删去加粗整句 | 多出原文 | 该句原书没有，是译者自加的机制说明；原文对应内容只是"仍允许 W 有非平凡 beta 函数" |
| 12 | ch05-5.4.6.4-001 (5.123) / ch05b L253–259 | "These are (approximately, and up to an overall multiplicative factor) β = Λ ∂/∂Λ (1/g²YM) = C2(R) − 3C2(adjoint), where C2(R) is the "second Casimir" of the representation (the quadratic invariant in the enveloping algebra of Lie H). This result is exact for N=2 and N=4" | "以 Λ 为能标，规范耦合的一圈 beta 函数，采用通常的生成元归一化，为 β=Λ∂/∂Λ(1/g²)=(3C2(adj)−T(R))/(8π²)+O(g²)。这里 C2(adj) 是…；T(R) 是…Dynkin 指标…相应的微扰结果一圈精确" | 恢复为"这些 beta 函数（近似地，且相差一个整体乘法因子）为 β=Λ∂/∂Λ(1/g²YM)=C2(R)−3C2(adjoint)"；说明改为 C2(R) 为表示的"第二 Casimir"，即 Lie H 泛包络代数中的二次不变量；"这个结果对 N=2 与 N=4 是精确的" | 数学 | 原书公式是 C2(R)−3C2(adjoint)，且明言只准确到整体乘法因子；译稿换成教科书归一化式（多出 1/8π²、O(g²)、反号、C2(R)→T(R)），并丢掉"近似、相差整体因子"的限定，与原书不符 |
| 13 | ch05-5.4.6.4-002 / ch05b L262 | "using R ≅ (ad H)⊕3 for the N=4 theory, we find that β = 0" | 就得到 $T(R)=3C_2(\mathrm{adj})$ | 就得到 $C_2(R)=3C_2(\mathrm{adj})$ | 数学 | 随第 12 条：原书该例用的是 C2(R)，代回 (5.123) 才有 3C2(adj)−3C2(adj)=0 |
| 14 | ch05-5.4.6.7-002 / ch05b L295 | "the consistency conditions above (anomalies and renormalizability) are required" | 需要满足上述自洽条件，包括反常消除与相应量子理论定义的条件 | 需要满足上述自洽条件，即反常与可重整性 | 漏译 | 括号里是"反常与可重整性"，"可重整性"被含糊成"相应量子理论定义的条件" |
| 15 | ch05-5.5.2-003 / ch05b L416 | "The derived category D(X) is triangulated and thus cannot be equivalent to a category which is not triangulated." | 因而不可能作为三角范畴，等价于一个没有相应结构的范畴 | 因而不可能等价于一个非三角范畴 | 病句 | 原译语序错乱、语义打结（"作为三角范畴，等价于…"），且"没有相应结构"绕圈；原意只是"不可能与非三角范畴等价" |
| 16 | ch05-5.5.3.1-002 / ch05b L455 | "But as closing the loop restores the original metric geometry, the original set of stable A-branes must be restored. This can be described by expressing the set of homology classes of stable branes in an explicit basis." | 原来的稳定 A 膜集合必须恢复；但在一组显式同调基中，它们的标记会改变。 | 原来的稳定 A 膜集合必须恢复；这一点，可以通过在一组显式基中表示稳定膜的同调类来描述。 | 误译 | 原文第二句是"如何描述这一恢复"的方法说明，译稿读成"标记会改变"的新断言，且加了"但"字转折，语义反了 |
| 17 | ch05-5.5.3.1-003 / ch05b L458 | "one starts with a coherent sheaf, and produces an element of H^even(X,Z) which cannot correspond to the Chern character of any sheaf (for example, the rank of the bundle might be negative)" | 得到一个荷类，其有理 Chern 特征标位于 $H^{\mathrm{even}}(X,\mathbb{Q})$，却不可能对应于任何层的 Chern 特征标，例如，秩可能为负 | 得到 $H^{\mathrm{even}}(X,\mathbb{Z})$ 中的一个元素，它不可能对应任何层的 Chern 特征标，例如，丛的秩可能为负 | 数学 | 原文是 H^even(X,Z) 中的整元素不可能是任何层的 Chern 特征标；译稿改成"有理 Chern 特征标位于 H^even(X,Q)"，等于把断言换成了对任何类都成立的废话 |

## 改动记录（第 3 块：p383–392）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 18 | ch05-5.5.4.2-005 / ch05b L557 | "Then E decays into A1, A2, . . . , An so long as (5.137). This suggests the following [Conjecture 5.32]" | $E$ 就可以按该滤过，分解为这些不同相位的因子。**相同相位的稳定因子，应归入同一个半稳定因子；它们内部还可以有稳定因子的扩张。**由此得到下面的猜想。 | $E$ 就可以衰变为 $A_1,\dots,A_n$。由此得到下面的猜想。 | 多出原文 | 加粗整句原书无，且把"分解为 n 个稳定对象"偷换成 Harder--Narasimhan／半稳定语言，与紧随的猜想 5.32 直接冲突 |
| 19 | 猜想 5.32 / ch05b L560 | "For any point in T(Y), the subset of stable objects in D(X) is such that any object E can be decomposed (as in (5.136)) into a unique set of n stable objects Ak satisfying (5.137)." | $D(X)$ 的稳定对象足够丰富，使任意对象 $E$ 都具有形如 (5.136) 的唯一 Harder--Narasimhan 滤过。其非零因子 $A_k$ 半稳定，并满足 (5.137)。同一相位的因子，进一步分解为稳定因子；在相应有限长度条件下，这些稳定因子的同构类及重数，在 Jordan--Hölder 意义下唯一。 | $D(X)$ 中的稳定对象子集，满足：任意对象 $E$ 都可以（如 (5.136)）分解为唯一一组满足 (5.137) 的 $n$ 个稳定对象 $A_k$。 | 数学 | 原书猜想断言"唯一分解为 n 个**稳定**对象"；译稿改成"半稳定因子 + HN/Jordan--Hölder 唯一性"，把 stable 换成 semistable，并引进原书此处没有的滤过语言（原文 this is a conjecture，不是定理） |
| 20 | ch05-5.5.5-004 / ch05b L588 | "One might wonder whether triangles involving branes of different dimension might also be relevant. In the large volume limit they are not." | 在大体积极限中，作为失稳子层，它们受到支撑条件限制： | 在大体积极限中，它们并不相关： | 误译 | 原句只是"大体积极限中它们不相干（不 relevant）"，译稿读成"作为失稳子层受支撑条件限制"，与下句理由重复且语义走偏 |
| 21 | ch05-5.5.5-005 / ch05b L591 | "Thus, we will recover µ-stability as a limit of Π-stability if the condition (5.132) reduces to (5.138) in the large volume limit." | 因此，若条件 (5.132)，在大体积极限中约化为 (5.138)，就把 μ 稳定性，恢复为 Π 稳定性的极限。 | 因此，若条件 (5.132) 在大体积极限中约化为 (5.138)，我们就恢复出作为 Π 稳定性极限的 μ 稳定性。 | 病句 | 原译断句把条件从句割裂（"若条件…，"），且"把 μ 恢复为 Π 的极限"主客颠倒 |
| 22 | ch05-5.5.5-006、5.5.5-008（(5.140)(5.141)(5.142)）/ ch05b L594、L604、L613 | "the lowest component of ch(i∗ F ) … ξ(i∗ E) ≡ − ½ dim(S) (mod 2) … ξ(i∗ E) = − ½ dim(S)" | $\operatorname{ch}(i_*\mathcal{E})$、$\xi(i_*\mathcal{E})$（两处） | $\operatorname{ch}(i_*F)$、$\xi(i_*F)$（两处） | 指代 | 本节把丛统一记作 F（平面 5.5.5-002 已定义），$\mathcal{E}$ 在本节从未定义，读者无法对应 |
| 23 | ch05-5.5.5-010 / ch05b L625、L631 | （原书此段无 proof 环境，直接是正文段落 "The short exact sequence (5.139) induces the triangle (5.144)…"） | 段首套了 `\begin{proof}` … 段末 `\end{proof}` | 删去这两个环境标记，恢复为正文段落 | 体例 | 原文无 "Proof."，前面也没有命题/定理，孤儿 proof 会凭空印出"证明."；且该段是论证而非定理证明 |
| 24 | ch05-5.5.5-010 / ch05b L630 | "G is either locally free or supported on a complex codimension one subspace. Thus ξ(G) is close to either −3/2 or −1." | $G$ 具有正秩，或在同秩包含的情形中，是支撑在复余维1子空间的挠层。 | $G$ 要么局部自由，要么支撑在复余维1的子空间上。 | 误译 | 原文是二分法"局部自由 / 支撑在复余维1"；译稿的"具有正秩""在同秩包含的情形中"是错误添加（挠层的秩为 0），"挠层"倒是可以保留，但结构已乱 |
| 25 | ch05-5.5.6.3-001 / ch05b L723 | "By Serre duality, this Hilbert space of open strings is isomorphic to Hom(OX (b), OX (a)[3])." | 由 Serre 对偶，它与 $\operatorname{Hom}(\mathcal{O}_X(b),\mathcal{O}_X(a)[3])$ 对偶。 | 由 Serre 对偶，这个开弦 Hilbert 空间同构于 $\operatorname{Hom}(\mathcal{O}_X(b),\mathcal{O}_X(a)[3])$。 | 误译 | "isomorphic to"（同构）被译成"与…对偶"；Serre 对偶给的是两者同构，且丢掉主语"开弦 Hilbert 空间" |

## 改动记录（第 4 块：p393–402）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 26 | ch05-5.6.2.2-002（(5.175)）/ ch05b L1073-1076 | "…and compute (5.175) K = L ◦ G." | $\mathcal{K}=\mathcal{G}\circ\mathcal{L}^{-1}$，$\ \mathcal{G}=\mathcal{K}\circ\mathcal{L}$（两条关系） | $\mathcal{K}=\mathcal{L}\circ\mathcal{G}$。 | 数学 | 原书 (5.175) 只有一条关系 K = L∘G；译稿自创了 K = G∘L^{−1} 并附带 G = K∘L。二者一般**不等价**（K=L∘G ⟺ G=L^{−1}K，而 K∘L^{−1}=LGL^{−1}≠K），属公式错误 |
| 27 | ch05-5.6.2.2-009 / ch05b L1152 | "To confirm this one can compute the action of L−1 ◦ K on {F0, F1, F2}." | 可以计算 $\mathcal{K}\circ\mathcal{L}$ 在 {F_0,F_1,F_2} … 的作用 | 可以计算 $\mathcal{L}^{-1}\circ\mathcal{K}$ 在 {F_0,F_1,F_2} … 的作用 | 数学 | 承第 26 条同步修正：原书检验对象是 L^{−1}∘K（= G），不是 K∘L |
| 28 | ch05-5.6.2.2-010 / ch05b L1155 | "…and put G = L−1 ◦ K." | 并在相应约定下令 $\mathcal{G}=\mathcal{K}\circ\mathcal{L}$ | 并在相应约定下令 $\mathcal{G}=\mathcal{L}^{-1}\circ\mathcal{K}$ | 数学 | 同上，与原书一致化 |
| 29 | Definition 5.33 / ch05b L1084 | "The twist functor ΦE is defined as (5.176)…" | 扭转函子 $\Phi_{\mathcal{E}}$，定义为**所用增强中取值映射的锥**， | 扭转函子 $\Phi_{\mathcal{E}}$，定义为 | 病句／多出原文 | "所用增强中取值映射的锥"是讹误添加（原文只说 "is defined as (5.176)"），且把定义搞成同义反复；下句已解释 r 是取值映射 |

## 改动记录（第 5 块：p403–412）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 30 | ch05-5.6.3-intro-016 / ch05b L1313 | "(4) Δ0n1: … This time Δ011 corresponds to the ideal sheaf of a point **I**E,p[1] and is again only marginally stable at the large radius limit." | 对应于点理想层的**扭曲**与移位 $\mathcal{I}_{E,p}(-1)[1]$ | 对应于点理想层的移位 $\mathcal{I}_{E,p}[1]$ | 数学 | 已核对原书影印（PDF 407 = 书内 p397）：原书为 $\mathscr{I}_{E,p}[1]$，**无 $(-1)$ 扭转**；译稿多出扭转因子，把对象换成了另一族 |
| 31 | ch05-5.7.2.1-005 / ch05b L1484 | "However there is a subgroup C ⊂ GL~+(2,R) which does act freely." | 不过，**对于非零范畴**，存在自由作用的子群 | 不过，存在自由作用的子群 | 病句／多出原文 | "对于非零范畴"原文所无，且"非零范畴"无定义；子群 $\mathbb{C}$ 对任何（非平凡）三角范畴都存在，加上该条件反而把陈述限窄 |

## 改动记录（第 6 块：p413–422）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 32 | ch05-5.9.1.3-004 / ch05b L1915 | "Barannikov and Kontsevich [30] showed that **if X is a complex projective variety** then the formal germ to deformations of X, whose tangent space has dimension H1(X,TX), is contained in a larger formal germ…" | **对于相应的光滑射影 Calabi--Yau 情形**，$X$ 的**普通**形变形式胚… | **若 $X$ 是复射影簇**，则 $X$ 的形变形式胚… | 误译 | 原书假设是"复射影簇"，译稿擅自换成"光滑射影 Calabi--Yau"（把定理的适用范围改窄）；Calabi--Yau 只出现在下一句"设 $X_1,X_2$ 是镜像 CY 三维流形" |

## 待确认 / 未改（供 Lead 判断）

1. **原书自身的瑕疵**：p360 文字说 (5.108) 每个 ζ_i 出现 m_i 次，但 (5.115) 印成 Σ dim(V_i) ζ_i = 0、(5.117) 印成不带权的 Σ(ζ_i−θ_i)²，而 (5.118) 又用 m_j——三式不完全自洽。译稿原用 m_i d_i 把它们"自洽化"了。我按原书版面复原（(5.115) 写作 Σ d_i ζ_i，d_i=dim V_i），保留原书的不一致。若 Lead 认可按"每个 ζ_i 出现 m_i 次"统一（即 (5.115) 应为 Σ m_i ζ_i=0、(5.117) 应为 Σ m_i(ζ_i−θ_i)²），可再改。
2. ch05-5.4.5.6-003（ch05b L~195）：原书 "it is a G-equivariant line bundle"；译稿作"$G$ 等变向量丛 O⊗ρ_k，秩 d_k，在一维不可约表示情形中是线丛"，并把"asymptotic region has π1≅G"展开为"在轨形基本群的意义下保留群 G；若群在该区域自由作用，普通基本群也为 G"。属译者为自洽而增补（数学上更准确，非原书内容），未改，避免过度改写。
3. ch05-5.4.5.6-005：译稿增补"采用第4章的协变 Fourier–Mukai 约定，取值映射空间是 Ṽ_k^∨ 的纤维，因此对应丛为 Ṽ_k = R_{ρ_k}^∨"；原书仅 "we have precisely reproduced the definition of the tautological bundles Rρ from (4.12)"。未改（同第2条）。
4. ch05-5.4.5.4-003（p369）：原书 "the pre-image of a point is the orbit of the C* action"；译稿作"非零点的原像…的轨道，原点上则须取闭轨道商"，增补了原点处取闭轨道的内容（数学上合理），未改。
5. ch05-5.4.5.4-004（p369）：原书 "the topology on the two sides is different"；译稿"两侧的整体几何就可以不同"（topology→几何）。轻微走偏，不影响理解，未改。
6. ch05-5.4.6.3-001（p374）：译稿加"在全纯 Wilson 有效作用量的约定下"（脚注同），并把"the beta function for W vanishes"译成"超势 W 的直接微扰重整化为零"、脚注"no direct perturbative vertex renormalization"。含义大体相当（W 不受微扰重整化），但"beta 函数为零"的精确表述被消解；未改，供判断是否统一为"W 的 beta 函数为零"。
7. ch05-5.4.6.5-003（p375）：原书 "These have been conjectured to satisfy minimization principles [251]"；译稿"它们与极值原则有关，特别是确定超共形 R 对称的 a 极大化原则"。ref251 确为 a-极大化文献，增补内容正确，但"被猜想满足极小化原理"变成"与极值原则有关"；未改。
8. ch05-5.4.6.7-005（p376）：D3 膜度规，原书写作 $1+g_sN/r^4$；译稿改写为标准 AdS5×S5 形式 $H=1+L^4/r^4$、$L^4=4\pi g_sN\alpha'^2$，并加一句"常数因子与弦尺度也可以吸收到 r 中"。数学上更规范，但与版面公式不同；未改，若要求严格照版面需回退。
9. 若干译者增补未改（均不影响正确性）：5.4.6.2-005"在所用能标约定下"；5.4.6.6-001"在近似流中"；5.5.1-009 末"移位决定哪个对象作为反膜参与"；5.5.1-010"相容开弦，使相应方块交换"；5.5.2-001"相应分次下"；5.5.3-intro-001"标记集合"；Definition 5.30"本节所称的"；5.5.3.1-004"在相应的光滑射影情形中""等价按自然同构识别"。
10. ch05-5.5.5-002～008（p385–386）：原书把丛记作 E、把子层（并与曲率形式撞名）记作 F，自身混用；译稿为避免撞名改为丛 F（曲率 $\mathcal{F}$）、子层 E，于是 (5.138) 作 $\mu(E)<\mu(F)$、 (5.139) 作 $0\to E\to F\to G\to0$，与原书字母相反（原书 $\mu(F)<\mu(E)$、$0\to F\to E\to G\to0$）。我已把本节内未定义的 $\mathcal{E}$ 统一成 $F$（第 22 条），但**字母与原书相反这一点未动**——若要严格照版面，需把整节 E/F 互换（涉及 5.5.5-002/003/004/005 与 (5.138)(5.139)(5.143)），请 Lead 定。
11. ch05-5.5.6.1-001（p387）：译稿增"$S$ 是 $f$ 的零点除子"（数学上正确、原文无）；ch05-5.5.6.1-003 增"相对于这一衰变道"；ch05-5.5.6.3-009"没有带荷手征物质"（原文 no chiral matter，多"带荷"）。均未改。
12. ch05-5.5.6-intro-002（p386）：原书 "K(X) ≅ Z^4"，译稿作"偶 K 群 $K^0(X)\cong\mathbb{Z}^4$"（解释性补充，可接受）。
13. ch05-5.5.7-004（p392）：译稿增"模去其整数周期"（原文 "so long as the component of B associated to C is nonzero" 无此语），未改。
14. ch05-5.5.7-007（p392）：译文末句"$z=1$ 对应于 $O$，$z=\infty$ 为保典翻转后大 $C'$ 的极限"对应原书 p393 续文，本块文本截到 "$z = 0$ is the large C limit," 为止，留待 p393-402 块核对。—— 已在第 4 块核对：原书 p393 首行即 "z = 1 corresponds to t = O and z = ∞ gives the large C′ limit after the flop transition."，译文一致，**无需改**。
15. (5.170)（p399，已核对原书影印 PDF 399 = 书内 p389）：原书印的是 $0\to\mathcal{O}_X(3)\to\mathcal{O}_X\to\mathcal{O}_E\to0$（**无负号**），但同段说 $E$ 的法丛为 $\mathcal{O}_E(-3)$，标准序列应是 $0\to\mathcal{O}_X(-3)\to\cdots$。译稿与版面一致，故未改；**疑为原书笔误**，是否按 $\mathcal{O}_X(-3)$ 改请 Lead 定。
16. (5.174)（p400）：原书单行 $\operatorname{ch}(K(F))=\operatorname{ch}(F)-\langle\mathcal{O}_E,F\rangle\operatorname{ch}(\mathcal{O}_E)$，$\langle,\rangle$ 为 (5.106) 相交形式；译稿改为两行并用数学 Euler 配对 $\chi$（$\operatorname{ch}(F)-\chi(\mathcal{E},F)\operatorname{ch}(\mathcal{E})$ 及 $+\;I(\mathcal{E},F)$ 形式），并加"其他分支…随相应张量积或量子对称变换"。若按译稿自述 $I=-\chi$，则其"$-\chi$"与书中的"$-\langle\rangle$"差一个符号——需先核 (5.106) 的符号约定，未改。
17. (5.181)(5.182)(5.183)（p402）：译稿把 $\zeta_k$ 定义为 $-\sqrt3\operatorname{Re}(\mathrm{e}^{\frac{\pi\mathrm{i}}6(4k-1)}\psi)$（多一个负号），(5.181) 第二行相应写 $-\;c\sum_im_i\zeta_i/\sum_im_i$，(5.183) 两式也带负号。与原书符号相反但**内部自洽且 $\xi$ 的数值不变**（$\zeta$ 整体变号），未改。
18. (5.179)(5.180)（p401–402）：原书 $H^k(X,E)$、$\operatorname{Hom}(\mathcal{O}_X,E)$，译稿写 $\operatorname{Ext}^k_X(\mathcal{E},\mathcal{E})$、$\mathrm{R}\operatorname{Hom}_X(\mathcal{E},\mathcal{E})$。球面对象的正确定义确实是 $\operatorname{Ext}^*$，数学上更清楚，但与原书版面不同，未改。
19. "五次曲面"（全稿）：§5.5.6 标题及本章多处把 the quintic（$\mathbb{P}^4$ 中的五次超曲面，实为**三维**流形）译作"五次曲面"，同章他处又作"五次三维流形"（L634、L1156、L1879）。建议统一为"五次三维流形"；涉及 10 处、多数在本块以外的段落，未擅自改动。
20. 增补未改（第 4 块）：5.5.7-017 "perverse sheaves" 译作"反常凝聚层"（glossary 只有 perverse coherent sheaf=反常凝聚层，原书是 perverse sheaves，通常译"反常层"）；5.5.7-011 增"在 $\epsilon\to0$ 的近似中"；5.6.1-intro-003 增 Mellin--Barnes 围道说明及译者注"这里的 Kähler 坐标 $t$，与前面镜像方程中的坐标 $t$，按上下文区别"；5.6.2.2-001 增"固定使下面扭转函子对应于该单值化的环路方向…"等约三句；5.6.2.1-005 增"还须指定生成元之间态射上的相容作用"及脚注末句；5.6.2.2-006 增"在当前 $P_0$ 分支中，则取 $\mathcal{O}_E(-1)$"。
21. 5.7.1-002、5.7.1-009（p409–410）：原书为行文中的定义（"We define a stability function…"、"A stability condition is called locally finite if…"），译稿改成 `\begin{definition*}[稳定性函数]`、`\begin{definition*}[局部有限性]` 两个显示定义（原书无此结构，也无编号）。内容无误，属排版/结构层面，未改。
22. 5.7-intro-005（p408）：原书"with equality if and only if E is semistable"，译稿扩写为"等号成立当且仅当所有因子的中心荷位于同一条正实射线上；在相位取于同一适当分支时，这等价于 $E$ 半稳定"（约两句增补，数学上成立），未改。
23. 译者增补（第 5 块，数学上成立、未改）：5.6.3-intro-009 末句"；(5.188) 中远离例外除子的表示，仍然稳定"；5.7.1-007 末句"稳定性函数给出 (a)…给出 (d)"；5.7.1-008 增"半稳定性首先约束像与商的相位…"；5.7.1-009 增"这里的子对象与商，取准 Abel 范畴中的严格子对象与严格商…"；5.8.1-003 增"或者更一般地，是导出范畴中的不可分解对象"；5.8.1-004 增"自配对也满足 $\chi(A,A)=0$""与 $N(D)$ 的秩为2矛盾"；5.7.2.1-004 末句"这也直接表明，两个作用对易"。
24. 5.8.1-001/002（p412）：原书 "The Grothendieck group K(D) ≅ Z⊕Z"、局部同胚 $\mathcal{Z}\colon\operatorname{Stab}(X)\to\operatorname{Hom}_{\mathbb Z}(K(D),\mathbb{C})$，译稿一律写成数值 Grothendieck 群 $N(D)$，并在 5.8.1-001 增"中心荷通过数值 Grothendieck 群分解"。对椭圆曲线 $K(D)=N(D)$ 无害，但与原书记号不同，未改。
25. 5.8.1-001："nonsingular genus one curve" 译作"非奇异亏格1**射影**曲线"（增"射影"）；语境无误，未改。
26. "unimodular"（5.8.2-001、5.8.2-005，p413–414）：原书 "The lattice N(X) is **even and unimodular** of signature (2,ρ)"、"Since the lattice N is **unimodular**…"，译稿作"代数 Mukai 格 $\mathcal{N}(X)$ 是**非退化**偶格""由于 Mukai 配对**非退化**"，并在 5.8.2-001 末增句"完整 Mukai 上同调格 $H^0\oplus H^2\oplus H^4$ 是 $(4,20)$ 偶幺模格；代数子格一般不幺模"。译稿的增补其实指出原书把 $N(X)$ 说成幺模不妥（$\operatorname{Pic}$ 一般不幺模），但与 "unimodular" 字面不符、且"非退化"≠"幺模"（术语）。两处若只改一处会与增补句冲突，故未改，请 Lead 定。
27. 5.8.3.1-004 与 5.8.3.1-006（p416）：译稿把 $\operatorname{Ext}^1$ 方向整体反转：原书 $\operatorname{Hom}^1_D(S_0,S_1)=\mathbb{C}^a$、$(S_1,S_2)$、$(S_2,S_0)$，译稿作 $(S_1,S_0)$、$(S_2,S_1)$、$(S_0,S_2)$，并加注"这里采用右 $B$ 模，单对象的 Ext 箭方向，与 $B$ 的箭图方向相反"；相应地 $P_0,P_1,P_2$ 的非对角元符号与原书**全部相反**（原书 $P_0=\begin{pmatrix}1&3&-3\\0&1&0\\0&0&1\end{pmatrix}$ 等）。全小节内部自洽（与该稿 $\chi$ 符号约定一致），但与版面不同，未改。
28. 5.8.3.2-007（p418）：原书末项印作 $P_2(rg)=P_0(g)$（与 $P_1(rg)=P_0(g)$ 重复，疑笔误），译稿作 $P_2(rg)=P_1(g)$（循环对称）；未改。
29. 5.8.1-006（p413）：原书 $(5.200)$ 为 $\operatorname{GL}(2,\mathbb{R})/\operatorname{SL}(2,\mathbb{Z})$，译稿作 $\operatorname{GL}^{+}(2,\mathbb{R})/\operatorname{SL}(2,\mathbb{Z})$（更准确），并增"在模堆或轨形的意义下…"；未改。
30. 5.9.1.1-003/004（p420）：译稿把 $X$ 与 $Y$ 的角色整体对调（世界面右半记作 $X$、边界态 $B$ 取 $X$ 的、$\Phi_{\mathcal{F}}(B)$ 落在 $Y$），原书相反（左半 $X$、$B$ 为 $Y$ 的边界态、结果在 $X$）；又 5.9.1.1-004 把原书一句 $\Phi_F(B)=\operatorname{Tr}_{\mathcal{H}_{B,F}}(-1)^F$ 扩写为"族指标/BRST 复形/$\mathrm{R}\operatorname{Hom}_X(B^{\vee},\mathcal{F}_y)$"一大段。内部自洽，未改。
31. 增补未改（第 6 块）：5.8.2-007 增"在上同调上作用平凡且保持该分支的部分…其余对称通过 Mukai 格上的作用体现"；5.8.3-intro-001 增"本小节的稳定性空间均针对这个支撑受限的范畴 $D$"；5.8.3-intro-002 把原书"for all $i,j$"改为"对所有 $i\ne j$"，并增"相位在 $(0,1]$ 的稳定对象…其他稳定对象由移位得到"；5.8.3.3-002/007/008 增相位连续性等说明；5.9.1.2-001 增"未除去 $\mathbb{C}$ 的整体作用以前…"。

## 改动记录（第 7 块：p423–429）

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 33 | ch05-5.9.3-003 / ch05b L1959 | "Since the topologically twisted theory is independent of the world-sheet metric, **this operation produces a boundary state E′, still with the same topological twisting E, but now conformally invariant.**" | "拓扑扭曲理论，不依赖世界面度规，因此，**在这一过程与拓扑扭曲兼容、且极限可控时，预期得到共形不变的边界态。在稳定的情形中，它仍对应于原对象 $E$；若极限分裂，则至少保持原来的拓扑荷，边界态由相应稳定因子描述。**" | "由于拓扑扭曲理论不依赖世界面度规，**这一操作给出边界态 $E'$：它的拓扑扭曲仍为 $E$，但现在已共形不变。**" | 漏译＋多出原文 | 原书此句是边界态 $E'$ 的定义（拓扑扭曲不变、共形不变），是 5.9.3-004"若这个极限仍为单个稳定膜…"的前提；译稿把 $E'$ 整个丢掉，换成三句原书所无的臆测（"极限可控""若极限分裂"） |
| 34 | ch05-5.9.3-005 / ch05b L1965 | "It has then been shown that, **to leading order (and all orders for rk E = 1)**, the RG flow is [451]" | "已证明，**在相应导数近似的首阶，并在秩1情形中对曲率的代数幂重求和时**，RG 流为" | "已证明，**在首阶（当 $\operatorname{rk}E=1$ 时则对所有阶）**，RG 流为" | 误译 | 原书说的是 $\alpha'$ 展开的首阶，$\operatorname{rk}E=1$ 时所有阶成立；"相应导数近似""对曲率的代数幂重求和"均为原文所无 |

## 待确认 / 未改（第 7 块）

32. 5.9.4-004（p426）：原书 $F=\operatorname{Im}\Omega$、$A=\operatorname{Im}\Theta$；译稿作 $F=-\operatorname{Im}\Omega$、$A=-\operatorname{Im}\Theta$，并增"取与所用复结构及 $B-F$ 约定相容的符号"，随后仍写 $F=\omega I$、$\omega^{-1}F=I$。$\operatorname{Im}/\operatorname{Re}$ 与复结构约定的符号随 $I$ 的取向而变，译稿内部自洽（与第 4 块 $\zeta_k$ 变号同类），未改。
33. 5.9.2-001（p423）：原书 "This means that E, locally, sits in a moduli space of objects which is cut out in a space of some dimension by the same number of equations, and therefore the moduli space should locally be an isolated point [E]."；译稿增"适当处理自同构以后""因而具有虚维数零"，并拆成"若方程横截，模空间局部就是孤立点"。属澄清性增补，未改。
34. 5.9.4-001（p425）：原书 "On the most elementary level, Geometric Langlands Duality can be formulated as follows."、"defined by the condition that its weight and coweight lattices are exchanged relative to G"；译稿作"可以如下表述其**范畴性主张**"、"由交换根数据给出，特别地，交换权格与余权格，**以及根与余根**"，并增"这里先以相应稳定轨迹及所需扭曲为背景"。增补方向正确但与字面不同，未改。
35. 5.9.4-009/010/011/012（p427–428）增补未改：5.9.4-009 增"因此，这个对称，要求扭曲为半典范扭曲"；5.9.4-010 例中增"携带平凡的物理线丛，并作相应半典范解释"、"局部截面层"；5.9.4-011 增"平方根实际存在时，可通过张量积，与通常的 D 模表述识别"；5.9.4-012 增"具有相应全纯仿射结构"。
36. 5.9.3-004（p424）：原书条件为 "If $E$ is a single brane (has a unique identity operator…)"，译稿作"若**这个极限**仍为单个稳定膜，即具有唯一的恒等算符…"，主语由 $E$ 换成 RG 极限，语义略移但下文（"一般而言，却可能得到一组物理膜 $E_i$"）仍通，未改。

## 备注（第 7 块）

- 5.9.2-001：原书 (Ext 对偶式) 由 pdftotext 抽出的文本为 $\operatorname{Ext}^i_D(E,E)\cong\operatorname{Ext}^{3-i}_D(E,E)$（抽取时丢了上标 $*$），译稿作 $\operatorname{Ext}^{3-i}_D(E,E)^*$，与下句"形变空间与阻碍空间对偶"相符，**正确**，无需改。
- 5.9.4-007 的 Moyal--Wigner 乘积、$\mathcal{D}(Y,\mathcal{L})^{\mathrm{op}}\cong\mathcal{D}(Y,\mathcal{L}^{-1}\otimes K_Y)$、$X^\vee=V^\vee\times V^\vee/\Gamma^\vee$、(5.169) 前的 $\Omega=\frac1\hbar\mathrm{d}p_i\wedge\mathrm{d}q^i=\mathrm{d}\Theta$ 等公式均与版面逐字一致。

## 术语统一（task-12）

### 一、"五次曲面" → "五次三维流形"（6 处，全部改）

原书 "the quintic" 一律指 $\mathbb{P}^4$ 中的五次超曲面，即**五次三维流形**（quintic threefold，原书 p386 明写 "let $X$ be a quintic hypersurface in $\mathbb{P}^4$"，p402 亦作 "quintic threefold"）；无一处指 quintic surface（$\mathbb{P}^3$ 中五次曲面）。同章原有 3 处已译作"五次三维流形"（L634、L1155、L1878），本次据此统一。

| 行号 | 原译 | 改为 | 理由 | 原书页 |
|---|---|---|---|---|
| L631 | `\subsection{五次曲面上的例子}` | `\subsection{五次三维流形上的例子}` | 标题对应原书 "5.5.6. Examples on the quintic" | PDF 386（书内 p376） |
| L666 | `\subsubsection{五次曲面上4膜的稳定性}` | `\subsubsection{五次三维流形上4膜的稳定性}` | 对应 "5.5.6.1. Stability of 4-branes on the quintic" | PDF 387（书内 p377） |
| L674 | 这里考虑的五次曲面上**的**4膜族 | 这里考虑的五次三维流形上的4膜族 | 对应 "All 4-branes corresponding to B-branes on the quintic…" | PDF 387 |
| L709 | 需要精确分析镜像五次曲面的周期 | 需要精确分析镜像五次三维流形的周期 | 对应 "an exact analysis of the periods of the mirror quintic" | PDF 389（书内 p379） |
| L1160 | 五次曲面的情形中，用大半径极限… | 五次三维流形的情形中，用大半径极限… | 对应 "In the case of the quintic we used the large radius limit…" | PDF 402（书内 p392） |
| L1274 | 与 §5.5.6.1 中五次曲面上的4膜相同 | 与 §5.5.6.1 中五次三维流形上的4膜相同 | 对应 "the 4-branes in the quintic as in §5.5.6.1" | PDF 405（书内 p395） |

改后 `grep "五次曲面" ch05b.tex` = 0 处；"五次三维流形" 共 9 处（原 3 + 新 6）。保留项：无。

### 二、unimodular 被译作"非退化"（2 处，改为"幺模"）

| 行号 | 原译 | 改为 | 理由 | 原书页 |
|---|---|---|---|---|
| L1568（5.8.2-001） | 代数 Mukai 格 $\mathcal{N}(X)$ 是**非退化偶格** | 代数 Mukai 格 $\mathcal{N}(X)$ 是**偶幺模格** | 原书 "The lattice $N(X)$ is **even and unimodular** of signature $(2,\rho)$"；且本段末句本就写"代数子格一般不幺模"，原"非退化"与"幺模"混用自相矛盾 | PDF 413（书内 p403） |
| L1600（5.8.2-005） | 由于 Mukai 配对**非退化**，并且… | 由于 Mukai 配对**为幺模的**，并且… | 原书 "Since the lattice $N$ is **unimodular**, and the vectors $n(E)$ span the numerical K group…" | PDF 414（书内 p404） |

注：L1600 原书主语是格 $N$，为最小字面替换只改"非退化→为幺模的"，未动"配对"一词（Lead 若要求完全对齐原句，可改为"由于格 $N$ 是幺模的"）。

保留项：L434"非退化条件 $\partial f\ne0$"、L1900"取适当非退化区域"为另一个词（nondegenerate），保持不动。


