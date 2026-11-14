# B｜Jones 的范畴化与 Khovanov 同调（T6）

**一句话**：1989 年这篇论文给的是 Jones 多项式的三维路径积分表示——一个数；Khovanov 同调是同一个多项式在同调层面的提升（一族双分次向量空间，Jones 是它的分次 Euler 特征）。两者**不是推论关系**：本文没有任何范畴化的构造或暗示；物理上把两者接起来的是 2007–2011 年 Witten 的工作——把 3d CS 写成 4d N=4 SYM 在半空间上的边界理论，再升到 4/5 维的椭圆方程，Khovanov 同调作为 BPS 态空间的上同调出现。

## 一、Khovanov 同调：定义与"退回 Jones"

（标准构造，本机无 Khovanov 原文，未逐字核；arXiv:math/9908171 已核，Duke Math. J. 101 (2000) 359–426 已核）

- 取链环投影图 D 的 n 个交叉点，每个交叉点作 0/1 两种光滑化 ⇒ 2^n 个圆图；每个顶点配 V^{⊗k}（V 二维分次空间，次数按圆数平移），每条边配鞍点协边诱导的映射；微分 d=Σ(−1)^i∂_i，d²=0；Kh(L)=H_*(C(D)) 与投影无关。
- 双分次 (i,j)：同调次数与 q 次数；分次 Euler 特征 Σ(−1)^i q^j dim Kh^{i,j} = Ĵ(L)。
- Witten 的写法 [W11 (1.9) p.9]：J(q;L)=Tr_{K(L)}(−1)^F q^P，即"取等变指标/Euler 特征从 Kh 退回 Jones"；F 只以 mod 2 进入 ⇒ 同调含更多信息，而"the additional information is really essential"。

## 二、"范畴化"是什么意思

- 不是换写法，而是把"数"换成"复形/分次向量空间"，并要求取 Euler 特征退回原不变量：Jones 是 Kh 在 K₀/超迹下的影子。
- 附带得到**函子性**：纽结协边 Σ: K→K′ 给线性映射 Φ_Σ: Kh(K)→Kh(K′)，拼接相乘 [W11 (1.10) p.10]。这一层 1989 的 TQFT 完全没有（那里只有"数→数"）。
- 也回答了 1989 解释不了的事：Jones 系数是整数。CS 路径积分给 Laurent 多项式，但不说系数为何是整数；Kh 把 a_n 解释为（Z₂ 分次）向量空间维数 [W11 p.8]。Witten 自己把这写成 §1.1.2 的标题："What Chern-Simons Theory Doesn't Explain"。

## 三、物理来源：Witten 2011、Kapustin–Witten 2007，与本文什么关系

- 出发点 [W11 摘要 p.1]：D3-brane 终止在带 θ 角的 NS5 上；一边可化为 D3 世界体边界上的 CS，一边可用 S/T 对偶；两支合起来给出 Jones 与 Khovanov 同调的"流形无关"描述——4/5 维椭圆方程解的计数。
- 机制 [W11 §1.4.1 p.12]：W 上 CS 路径积分 = N=4 SYM 在 V=W×R⁺ 上的路径积分，纽结 = 边界上的 Wilson 算子；再用对偶。要从"数"到"向量空间"，需要面算子而非线算子：4d TQFT on M=R×W，面算子支在 Σ=R×K 上，态空间给 (W,K) 一个双分次向量空间 [p.9]。
- 他自己的点题 [W11 p.107]："the fact that the four-dimensional equations (5.38) can be 'lifted' … to five dimensions is part of the reason that Chern-Simons gauge theory can be 'categoriﬁed,' which is just a fancy way to say that it can be derived from a theory in one dimension higher."——**范畴化 = 从高一维理论导出**，这是全篇最该记住的一句。
- Kapustin–Witten 2007 的角色：提供 4d N=4 SYM 的拓扑扭曲族（参数 t）、Wilson–'t Hooft 与面算子框架。W11 明说跟随 [63] 的约定（其 §2）、扭曲细节见 [63] §3、Wilson–'t Hooft 算子见 [63] §6.2。但 KW 本身讲几何 Langlands，Khovanov 不是它的推论，只是同一扭曲框架的另一个应用。
- 2008 年那篇（1108.3103）把构造"去物理化"：4/5 维椭圆方程 + 编码纽结的边界条件，形式上类比 Floer/Donaldson 理论，"可用经典规范理论描述"；并自承 Khovanov 同调还"没有类似的直接计算"。
- 与 1989 的关系：不同维度（3 vs 4/5/6）、不同构造（路径积分 vs BPS 态/椭圆方程上同调）、不同参数层面（1989 固定整数 k，q 是单位根；Kh 是 q 的多项式，对所有 level 同时）。所以既不是推论，也不是"把 k 取某个值"。

## 四、本文有没有范畴化暗示？——没有

- 全文没有 homology、chain complex、categorification 一类构造；不变量是数 Z(M; links)。唯一擦边处是 p.372：解 (3.4) 需要"q 数联络"，其和乐 "would presumably be an element of a 'quantum group', not an ordinary classical group. Indeed, it seems likely that the theory of quantum groups [35] can be considered to …"——"presumably / seems likely" 双重 hedging，且说的是量子群，不是同调。
- 但本文有"半截"结构：对曲面 Σ 给向量空间 ℋ_Σ（§3），对 3-流形给数——已具 Atiyah TQFT 雏形，只是取值为 Vect 而非复形，缺 Z-分次与微分。范畴化要做的正是把 ℋ_Σ 换成复形、把 Z(M) 换成上同调。

## 五、要把本文理论范畴化，缺什么（开放问题）

1. **一维提升**：需 4d（或 5d/6d）理论，其边界约化给 CS；1989 的 3d 理论自身没有"多出来的一维"来放同调方向（W11 p.107）。
2. **超荷与双分次**：需要 Q²=0 与 U(1)×U(1) 给 (i,j) 分次；纯 CS 只有规范约束（ghost 数一维），没有 R-对称性（W11 p.9 用 N=4 的 F、P）。
3. **标架/半形式反常**：CS 路径积分依赖 W 的 framing（更一般 two-framing），换标架乘 q 的幂 [W11 p.7]；1989 自己也在 §2 用 η 不变量处理这个相位（(2.16)–(2.17)）。要得到良定义的 Z-分次复形，必须把反常典范化，否则只到射影层面。
4. **表示范畴升级**：1989 的 Wilson 线只带一个表示（level k 的可积表示），对应一个模张量范畴；范畴化要求它被一个 2-范畴（模范畴的范畴）替换——一般 G 未知，A 型有 Khovanov–Rozansky/Soergel 双模路线（未核原文）。
5. **level 与 q 的错位**：1989 的不变量定义在 q=e^{2πi/(k+N)}（固定 level），Kh 是 q 的多项式（所有 level 同时）；"逐 level 范畴化"与 Khovanov 同调不是同一件事——这正是 W11 必须走 4d/5d 参数化理论的原因。

## 六、本地线索：Seidel–Smith 与 Abouzaid–Smith

- `<本地路径>`（lead 给的 Desktop 路径不存在，实际在 Downloads 下）§5.2 记：Seidel–Smith 引理 44、`thm:Skh=Kh` = Abouzaid–Smith 2019（Kh_symp 与 Jones 的 Khovanov 范畴化一致）。该笔记对应的综述是 Wehrheim–Woodward, arXiv:2210.11159（已核）。
- 含义：Kh_symp 由辛几何独立构造（nilpotent slice / 曲线 Hilbert 概型的 Fukaya 范畴、Lagrangian 对应）；Seidel–Smith 证它是链环不变量（引理 44），Abouzaid–Smith 证它与 Khovanov 同调同构（arXiv:1504.01230 已核；期刊卷页未核）。这是**纯数学**的范畴化路线，不过 CS 路径积分、不过 4d 超对称。
- 对研讨班：1989 的"CS→Jones"与"Kh_symp→Kh"之间，目前没有一条已知定理把 CS 的 Wilson 线直接变成 Kh 的链复形；T6 的真空就在这里。

## 七、最没把握 + 锚点

1. Khovanov 立方体构造我只按标准叙述写，**未读 Khovanov 原文**（本地无 PDF），细节（符号、q 次数的精确平移）可能有一处归一化差异。
2. "纯 CS 只有 ghost 数一维"是我的重建，1989 原文并未用 BRST 语言讨论分次。
3. Seidel–Smith 引理 44 的具体内容来自通读笔记转述，**未核原文**；Abouzaid–Smith 的期刊卷页亦未核。

| 断言 | 锚点 |
|---|---|
| Jones = Kh 的超迹/等变指标 | [W11 (1.9) p.9] |
| 系数是整数、Kh 解释之 | [W11 p.8] |
| 协边给线性映射 Φ_Σ | [W11 (1.10) p.10] |
| CS = N=4 SYM on W×R⁺ | [W11 §1.4.1 p.12] |
| "范畴化 = 从高一维导出" | [W11 p.107] |
| 面算子/双分次的要求 | [W11 p.9] |
| 标架依赖、换标架乘 q 幂 | [W11 p.7] |
| KW 扭曲约定/§3/§6.2 | [W11 引用 [63] 处]；KW=hep-th/0604151 |
| 本文"量子群"hedging | [src p.372] |
| 1989 只有数/ℋ_Σ 无复形 | [src §3 p.366–374] |
| Skh=Kh、引理 44 | 通读笔记:55（未核原文） |
