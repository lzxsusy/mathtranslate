# nLab 调研：共形场论与几何 Langlands 的物理概念（B 组）

本文件为《朗兰兹纲领与共形场论讲义》中文译注本提供「概念是怎么发生的」素材；每条含一句话定义、来历、在讲义中的位置、原文为何未解释、要点与 nLab 链接。
术语译名以 `docs/TERMS.md` 为准（手征代数、共形块、对偶 Coxeter 数、临界水平……）；标「年份待核」处表示未能亲自核对原始文献。
用法：直接改写为 [译注] 脚注或边栏，物理直觉优先于形式定义。

## 顶点代数 / 手征代数（vertex algebra / chiral algebra）

- **一句话定义**：乘法被复平面上一个点参数化的代数；一个顶点代数只描述二维共形场论的全纯（手征）一半。
- **来历**：Borcherds 1986 年在 PNAS 发文《Vertex algebras, Kac–Moody algebras, and the Monster》，为构造 Monster 群的无穷维表示（月光猜想）而引入 vertex algebra；Frenkel–Lepowsky–Meurman 1988 年把它用于 moonshine。Beilinson–Drinfeld 嫌顶点代数的公理「不启发人」，1990 年代（手稿约 1995 年起流传，2004 年由 AMS 出版《Chiral Algebras》）在代数曲线上给出几何版本，称 chiral algebra，这正是讲义使用的语言。
- **在讲义中的位置**：§7.1 与 §8.1 的出发点。讲义讨论「带 Kac–Moody 对称性的共形场论」时不列顶点代数公理，而是直接设一个手征代数，再取其在曲线上的共形块。
- **原文为何未解释**：讲义假定读者熟悉 CFT 的手征代数语言；中文读者最容易把「顶点代数」误当成完整的二维量子场论。
- **要点 / 常见误解**：
  - 顶点代数 ≠ 完整 CFT。它只编码手征一半；完整（亏格 0）理论要两个顶点代数（full field algebra），或一个带反全纯部分的结构。
  - 物理内容就是 OPE 的结合性与定域性；态-场对应 $Y(a,z)=\sum a_{(n)}z^{-n-1}$ 只是把「算符 insertion」写成级数。
  - 代数几何版本（手征代数）才能谈曲线、模空间与 D-模，这才是讲义真正用到的性质。
  - 有理性（每个模完全可约）保证只有有限多个单模，模范畴成为模张量范畴——这是共形块有限维的来源。
- **nLab**：<https://ncatlab.org/nlab/show/vertex+operator+algebra>、<https://ncatlab.org/nlab/show/chiral+algebra>

## 仿射 Kac–Moody 代数（affine Kac–Moody algebra）

- **一句话定义**：圈代数 $\mathfrak g\otimes\mathbb C((t))$ 的一维中心扩张再加导子；由整数「水平」$k$ 标记。
- **来历**：Kac 与 Moody 1968 年各自独立引入 Kac–Moody 代数；仿射型恰是圈代数的中心扩张，因此成为唯一在物理里大获成功的一类（Kac 本人戏称整个 Kac–Moody 理论「是一场灾难」，两个例外是仿射型与 Borcherds 代数）。物理上它就是二维流代数（current algebra），中心项对应量子化产生的 Schwinger 项/反常。
- **在讲义中的位置**：§7.1 用它构造带 Kac–Moody 对称性的手征代数；§8.1 写 $\hat{\mathfrak g}$ 在水平 $k$ 的包络代数，§8.2 讨论其中心。
- **原文为何未解释**：讲义默认读者知道生成元 $J^a_n$、水平 $k$、Verma 模与可积表示这套表示论；中文文献很少点明「中心扩张 = 量子反常」这一物理来源。
- **要点 / 常见误解**：
  - $k$ 不是纯数学参数，而是 WZW 模型的耦合常数（level）；它同时决定中心项系数。
  - 表示论里真正出现的是 $k+h^\vee$，不是 $k$ 本身：可积表示只在 $k$ 为非负整数（或 admissible）时有限多。
  - OPE：$J^a(z)J^b(w)\sim \dfrac{k\,\delta^{ab}}{(z-w)^2}+\dfrac{f^{ab}{}_c J^c(w)}{z-w}$。
  - 临界水平 $k=-h^\vee$ 时中心项与 Sugawara 构造相消，是讲义 §8 的全部出发点。
- **nLab**：<https://ncatlab.org/nlab/show/affine+Lie+algebra>

## 临界水平（critical level）

- **一句话定义**：$k=-h^\vee$ 这一特殊水平；此时 Segal–Sugawara 流变成交换的，理论失去能动张量。
- **来历**：Feigin–Frenkel 1992 年研究临界水平上的表示论，发现中心大到可以同构于 oper 上的函数；物理侧对应非紧群 WZW（如 $SL_2(\mathbb R)$，与 Liouville 理论相近，讲义引 [PW]）。讲义强调：没有能动张量的「共形场论」在物理学家看来荒谬，在数学上却是优点。
- **在讲义中的位置**：§8.1 给出定义（`latex/en/e08a.tex` 第 5 行 $k=-h^\vee$）；§8.2 讨论其中心；索引页码 85–86。
- **原文为何未解释**：要理解这个定义，须先知 Sugawara 构造的分母是 $k+h^\vee$，故 $k=-h^\vee$ 时构造发散、Virasoro 作用消失；一般 CFT 教材不会讲这个退化点。
- **要点 / 常见误解**：
  - 临界水平不是一个「模型」，而是参数空间里的退化点：对称性从 Virasoro×仿射退化为纯仿射。
  - 没有 Virasoro 对称 ≠ 没有共形块：共形块只用到仿射代数的 Ward 恒等式，仍可定义。
  - 中心反而变大：从「一个中心荷 $c$」变成 $\ell=\operatorname{rank}\mathfrak g$ 个生成场。
  - 复结构不能变，但射影联络可以变——这就是 oper 出现的入口，也是几何 Langlands 的物理起点。
- **nLab**：nLab 无独立条目；见 <https://ncatlab.org/nlab/show/chiral+algebra>、<https://ncatlab.org/nlab/show/affine+Lie+algebra>

## 对偶 Coxeter 数（dual Coxeter number, $h^\vee$）

- **一句话定义**：由对偶根系定出的整数，$2h^\vee$ 是伴随表示的 Casimir 特征值，也是 level 的标准平移量。
- **来历**：作为反射群/根系的不变量早已出现（Coxeter 1930 年代的 Coxeter 数），在 Kac–Moody 表示论里被系统使用并命名为 dual Coxeter number（命名年代待核）。其定义为最高根的对偶 Kac 标号之和加一：$h^\vee=1+\sum a_i^\vee$；例：$\mathfrak{sl}_2$ 为 2，$\mathfrak{sl}_N$ 为 $N$，$E_8$ 为 30。
- **在讲义中的位置**：§8.1 的 $k=-h^\vee$；§8.2 的 Sugawara 归一化；`latex/en/e06.tex` 第 478 行指出 $\hat k$ 应按 $G$ 与 ${}^L G$ 的对偶 Coxeter 数平移；索引页码 85。
- **原文为何未解释**：讲义直接使用符号；读者若不知道 $h^\vee$ 同时是 Casimir 特征值与 level 平移量，就无法理解 $k+h^\vee$ 为何处处出现。
- **要点 / 常见误解**：
  - $h^\vee$ 与 Coxeter 数 $h$ 不是一回事：对偶根系把根与余根对调，因此 $h^\vee(G)=h({}^L G)$，$h(G)=h^\vee({}^L G)$；讲义在对偶两侧写 $k+h^\vee$ 时这个互换很关键。
  - Sugawara 中心荷 $c=\dfrac{k\dim\mathfrak g}{k+h^\vee}$，分母就是 $k+h^\vee$。
  - $k=-h^\vee$ 使分母为零，不是「$c=0$」，而是构造本身失效——这正是临界水平的含义。
  - 它是整数，不是连续参数；对单连通群，WZW 的 level 必须是整数。
- **nLab**：nLab 无独立条目；见 <https://ncatlab.org/nlab/show/affine+Lie+algebra>

## Sugawara 构造（Sugawara construction）

- **一句话定义**：用仿射流的二次型造出能动张量 $T=\dfrac{1}{2(k+h^\vee)}\sum_a {:}J^aJ^a{:}$，把仿射代数提升为共形代数。
- **来历**：Sugawara 1968 年（与 Sommerfield 同时）提出「流场论」，试图仅用流代数描述强相互作用；这一想法后来在 CFT 中复活，称 Segal–Sugawara 构造。关键是那个 $1/(k+h^\vee)$ 归一化因子。
- **在讲义中的位置**：§8.2「手征代数的中心」中的 Segal–Sugawara 流（索引页码 87）；§7.1 用它说明 WZW 为何是共形场论。
- **原文为何未解释**：讲义只写「Segal–Sugawara 流」而不写公式；不知道这是二次复合构造，就看不懂「临界水平时它变成交换的」这句话。
- **要点 / 常见误解**：
  - 只在 $k\neq -h^\vee$ 时有定义；临界水平必须另作处理（取极限或只保留中心）。
  - 它把「流」当基本场、把「能量-动量」当复合场，这正是手征代数的物理内容：$T$ 不是独立自由度。
  - 中心荷 $c=k\dim\mathfrak g/(k+h^\vee)$，可用它检验归一化是否正确。
  - 物理直觉：WZW 的共形对称不是假设，而是流代数的代数后果。
- **nLab**：nLab 无独立条目；见 <https://ncatlab.org/nlab/show/affine+Lie+algebra>、<https://ncatlab.org/nlab/show/vertex+operator+algebra>

## WZW 模型（Wess–Zumino–Witten model）

- **一句话定义**：靶空间为李群 $G$ 的二维 sigma 模型，作用量 = 动能项 + Wess–Zumino 拓扑项，量子化后是共形场论。
- **来历**：Wess–Zumino 1971 年只写动能项；Witten 1984 年发现量子化后必须加上三阶的 WZ 项才保持共形不变（《Non-abelian bosonization in two dimensions》），故合称 WZW。Gawedzki 1987 年指出 WZ 项是 $G$ 上 bundle gerbe 联络的面和乐泛函。
- **在讲义中的位置**：§7.1 作为「带 Kac–Moody 对称性的 CFT」的原型；§7.6「例：WZW D-模」把它做成 $\Bun_G$ 上的 D-模。
- **原文为何未解释**：讲义假定读者知道 WZW 的手征代数就是仿射流代数、其共形块等于三维 Chern–Simons 的量子态空间。
- **要点 / 常见误解**：
  - level $k$ 是拓扑项系数，量子化要求整数（否则路径积分不定义），这就是「level 必须整数」的物理来源。
  - 运动方程 $\partial(g^{-1}\bar\partial g)=0$，复化后有通解 $g(z,\bar z)=g_\ell(z)g_r(\bar z)^{-1}$：左移×右移。
  - 它的共形块 = 三维 $G$-Chern–Simons 在带边流形上的量子态空间（全息）。
  - WZW 的 D-膜最简单由 $G$ 中共轭类给出，带 Chan–Paton 扭曲丛。
- **nLab**：<https://ncatlab.org/nlab/show/Wess-Zumino-Witten+model>

## 共形块（conformal block）

- **一句话定义**：固定 Riemann 面上满足 Ward 恒等式（对共形结构依赖正确）但未必满足缝合（sewing）的关联函数空间。
- **来历**：Belavin–Polyakov–Zamolodchikov 1984 年在极小模型里引入共形块，作为 Virasoro 表示论的构建块；数学上 Segal 与 Beilinson–Drinfeld 把它提升为「把曲面映到向量空间」的模函子。Beauville–Laszlo 1993 年指出共形块元素可视为广义 theta 函数。
- **在讲义中的位置**：§7.1 标题即 Conformal blocks；§7.2–7.3 把共形块粘成 $\Bun_G$ 上的层并证明它是 D-模。
- **原文为何未解释**：中文读者对「块」（block）一词陌生；讲义直接把它当作 D-模的纤维使用，不解释其物理含义。
- **要点 / 常见误解**：
  - 共形块 ≠ 关联函数：还缺单值性/缝合数据；它是「潜在的关联函数」。
  - 亏格 0（球面）的共形块已决定整个模函子，因此计算常从四点函数做起。
  - WZW 情形下它就是三维 CS 的量子态空间，维数由 Verlinde 公式给出。
  - 讲义真正关心的是「共形块构成向量丛、丛上有 Hitchin 平坦联络」这一结构；联络平坦性来自共形场论的可积性。
- **nLab**：<https://ncatlab.org/nlab/show/conformal+block>

## 共形块的余不变量层（sheaf of coinvariants）

- **一句话定义**：把每一点处「共形块 = 模掉整体流代数作用」的余不变量 $V/\mathfrak g(X\setminus p)V$ 沿曲线粘起来得到的层。
- **来历**：Feigin–Fuchs 学派与 Beilinson–Drinfeld（《Chiral Algebras》，手稿 1990 年代、2004 年出版）把共形块等同于余不变量；TUY 等人用它构造 WZW 的共形块（具体年份待核）。
- **在讲义中的位置**：§7.3 与 §7.5；索引页码 74、81；`latex/en/e07b.tex` 第 51–53 行给出粘合定义（各点 coinvariants $V/\mathrm{Stab}_p\cdot V$ 再粘）。
- **原文为何未解释**：需要「余不变量」的代数定义（模掉整体向量场的像），讲义只用一句话带过。
- **要点 / 常见误解**：
  - 余不变量 = 商掉「整体」对称作用后的部分；它自动满足 Ward 恒等式，因此是共形块。
  - 它是有限维的（对有理 CFT），但不是「一个数」——随插入点位置变化构成丛。
  - 「sheaf of coinvariants」与「sheaf of conformal blocks」在讲义里基本同义，前者强调代数构造，后者强调几何。
  - 粘合时要在 $\Bun_G$ 上而不是在 $X$ 上取余不变量，这一步才产生 D-模。
- **nLab**：nLab 无独立条目；见 <https://ncatlab.org/nlab/show/conformal+block>、<https://ncatlab.org/nlab/show/chiral+algebra>

## Beilinson–Drinfeld 的共形块层（sheaf of conformal blocks as D-module）

- **一句话定义**：在 $\Bun_G$ 上把每个 $G$-丛对应的共形块空间粘成向量丛，并赋予 Hitchin 平坦联络，从而视为 D-模。
- **来历**：Beilinson–Drinfeld 1990 年代的工作（《Chiral Algebras》2004；未出版的《Quantization of Hitchin's integrable system and Hecke eigensheaves》）；Frenkel–Ben-Zvi《Vertex algebras and algebraic curves》第二版（2004）系统化。Hitchin 1990 年《Flat connections and geometric quantization》给出联络的几何构造。
- **在讲义中的位置**：§7.2「共形块层作为模空间上的 D-模」、§7.3「$\Bun_G$ 上的共形块层」；§9.2 再把它们按 oper 扭转。
- **原文为何未解释**：讲义把「层 + 联络 = D-模」当已知事实；对不熟悉 D-模的读者，这层对应完全看不见。
- **要点 / 常见误解**：
  - D-模不是「微分方程」，而是「带平坦联络的层」的代数化；平坦性让它只依赖局部数据。
  - 共形块层在 $\Bun_G$ 上不平凡：它依赖丛的退化行为（在边界上取余不变量）。
  - Hitchin 联络的平坦性 = 共形场论的可积性（KZ 方程），不是额外假设。
  - 这一层就是几何 Langlands 对应右侧（$\Bun_G$ 一侧）的对象，左侧是 ${}^L G$ 局部系统。
- **nLab**：<https://ncatlab.org/nlab/show/conformal+block>、<https://ncatlab.org/nlab/show/D-module>

## Virasoro 代数（Virasoro algebra）

- **一句话定义**：圆上向量场代数（Witt 代数）的唯一非平凡中心扩张：$[L_m,L_n]=(m-n)L_{m+n}+\frac{c}{12}(m^3-m)\delta_{m+n,0}$。
- **来历**：Virasoro 1970 年在 Veneziano 对偶共振模型中引入约束算符（具体文献与年份待核）；中心项 $c$ 来自量子化的迹反常，因此 $c$ 又称中心荷。它是二维共形对称性的代数表达。
- **在讲义中的位置**：§7.1 共形对称性；§8.1–8.2 与 Segal–Sugawara 流对照（临界水平时 Virasoro 消失）；索引页码 85–88。
- **原文为何未解释**：讲义用「能动张量 $T(z)$」的场语言，不写交换关系；读者不知道 $T$ 的模展开就是 Virasoro 生成元。
- **要点 / 常见误解**：
  - $c$ 是理论的基本参数：自由玻色子 $c=1$，自由费米子 $c=1/2$，弦论要求 $c=26$（含鬼场）。
  - 极小模型 $c<1$，是有理 CFT 的经典例子。
  - 「Virasoro 对称」在物理上就是「无质量、标度不变」的二维理论所必然具有的对称。
  - 临界水平的 WZW 没有 Virasoro 对称，这是 §8 全篇的反常现象，不是笔误。
- **nLab**：<https://ncatlab.org/nlab/show/Virasoro+algebra>

## Feigin–Frenkel 中心（Feigin–Frenkel center）

- **一句话定义**：临界水平 $k=-h^\vee$ 时仿射包络代数 $U(\hat{\mathfrak g})$ 的中心，典范同构于 ${}^L G$-opers 上的函数代数。
- **来历**：Feigin–Frenkel 1992 年《Affine Kac–Moody algebras at the critical level and Gelfand–Dikii algebras》证明该同构，把 Drinfeld–Sokolov 的 W-代数与中心联系起来；Beilinson–Drinfeld 随后给出几何解释（oper 空间）。
- **在讲义中的位置**：§8.2「手征代数的中心」、§8.4「回到中心」；§8.3 先介绍 opers。
- **原文为何未解释**：这里的「中心」是顶点代数意义下的交换子代数，不是群论的中心；讲义没有点明这个双关，读者极易误解。
- **要点 / 常见误解**：
  - 中心是「与所有算符交换的子代数」，临界水平时它足够大，能编码整个 oper。
  - 一般 $\mathfrak g$ 有 $\ell=\operatorname{rank}\mathfrak g$ 个生成场；$\mathfrak{sl}_2$ 时就是那个 Segal–Sugawara 场。
  - 同构 $z(\hat{\mathfrak g})\simeq \mathrm{Fun}\,\mathrm{Op}_{{}^L G}(D)$ 是「Langlands 对偶群从 CFT 里长出来」的精确位置。
  - 讲义说它是「${}^L G$ 的 W-代数的经典极限」，这是同一件事的物理说法。
- **nLab**：nLab 无独立条目；见 <https://ncatlab.org/nlab/show/W-algebra>、<https://ncatlab.org/nlab/show/chiral+algebra>

## Miura 变换（Miura transformation）

- **一句话定义**：把自由玻色场非线性地变成 Virasoro/W-代数生成元的变换；量子版本 $T=-\tfrac12(\partial\phi)^2+Q\,\partial^2\phi$。
- **来历**：Miura 1968 年在研究 KdV 方程时发现（把 KdV 与 mKdV/线性方程联系起来）；量子化后成为 CFT 的玻色化工具，Drinfeld–Sokolov 把它推广到一般 $\mathfrak g$（广义 KdV 层级）。
- **在讲义中的位置**：§8.5 自由场实现；索引页码 96；`latex/en/e08b.tex` 第 206–210 行说 Miura 变换是映射 $\mathrm{Conn}(D)\to\mathrm{Proj}(D)$（联络 → 射影联络）。
- **原文为何未解释**：讲义用几何语言（把联络映成射影联络）而不给公式；读者不知道它在经典极限下就是 KdV 的 Miura 变换。
- **要点 / 常见误解**：
  - 经典 Miura 是坐标变换；量子 Miura 多出 $Q\partial^2\phi$ 项，$Q$ 与背景荷/中心荷有关。
  - 它给出 W-代数的自由场实现：一个玻色子就能实现 Virasoro。
  - 几何版本把 $G$-联络送到 ${}^L G$-oper 的射影联络，这正是 §8.6 中 T-对偶能「换出对偶群」的技术核心。
  - 变换不是单值的：有多支（screening 算符在支之间跳）。
- **nLab**：nLab 无独立条目；见 <https://ncatlab.org/nlab/show/W-algebra>

## Wakimoto 模（Wakimoto module）

- **一句话定义**：用 $\beta\gamma$ 鬼场（Coulomb 气体）的 Fock 空间实现仿射 $\mathfrak{sl}_2$ 在任意 level $k$ 的模。
- **来历**：Wakimoto 1986 年《Fock representations of the affine Lie algebra $A_1^{(1)}$》（Commun. Math. Phys. 104, 605）对 $\mathfrak{sl}_2$ 构造；Feigin–Frenkel 随后推广到一般 $\mathfrak g$ 并研究其可约结构（年份待核）。
- **在讲义中的位置**：§8.5（`latex/en/e08b.tex` 第 109–110 行引 [Wak]，并说 Feigin–Frenkel [FF:si] 作了推广）。
- **原文为何未解释**：讲义只说「Wakimoto 对 $\mathfrak{sl}_2$ 构造了自由场实现」，读者不知道 $\beta\gamma$ 系统、Coulomb 气体与 screening 是什么。
- **要点 / 常见误解**：
  - 自由场 = 无相互作用，但实现的却是相互作用的 WZW；代价是 Fock 空间巨大且高度可约。
  - 物理态要取子空间或上同调，screening 算符负责把「多余」自由度投影掉。
  - level 可以任意（不必整数），因此它是研究非整数 level 表示的主要工具。
  - 它是「自由场实现」的典范例子，也解释了 WZW 关联函数为何可算。
- **nLab**：nLab 无独立条目；见 <https://ncatlab.org/nlab/show/vertex+operator+algebra>

## 自由场实现（free field realization）

- **一句话定义**：把相互作用 CFT（WZW、极小模型）的算符代数嵌入自由玻色/费米场（含 $\beta\gamma$、鬼场）的 Fock 空间。
- **来历**：1970–80 年代 Coulomb 气体方法（Feigin–Fuchs–Frenkel 学派）与 Wakimoto 1986 年构造；物理上称玻色化（bosonization）。具体年份与人名待核。
- **在讲义中的位置**：§8.5 整节标题即 Free field realization。
- **原文为何未解释**：讲义假定读者知道「自由场」指高斯场、其关联函数可由 Wick 定理显式计算；不解释为何要用它。
- **要点 / 常见误解**：
  - 目的很实际：把难算的关联函数化为自由场高斯积分，同时保留对称性信息。
  - 自由场实现里通常有背景荷（背景电荷）调节中心荷，使 $c$ 匹配目标理论。
  - screening 算符改变荷，是投影到物理态的关键；没有它，Fock 空间不对应目标理论的表示。
  - 与 Miura 变换是同一件事的两种说法：一个讲代数同构，一个讲场变量替换。
- **nLab**：nLab 无独立条目；见 <https://ncatlab.org/nlab/show/vertex+operator+algebra>

## T-对偶（T-duality）

- **一句话定义**：把半径 $R$ 的圆换成半径 $1/R$，同时交换动量模与绕数；两种几何数据给出等价的二维 CFT。
- **来历**：Buscher 1987/1988（Phys. Lett. B194 (1987) 59；B201 (1988) 466），前驱为 Kikkawa–Yamasaki 1984；镜像对称是它在 CY 上的特例（Strominger–Yau–Zaslow, hep-th/9606040）。物理直觉：弦既能绕圆又能有动量，能量 $E=\sqrt{(\ell/R)^2+(Rm)^2}$ 在 $(\ell,m)\leftrightarrow(m,\ell)$、$R\leftrightarrow1/R$ 下不变。
- **在讲义中的位置**：§8.6「T-对偶与对偶群的出现」（索引页码 98、100）。
- **原文为何未解释**：讲义只用结论——${}^L G$ 的 W-代数从环面上紧化自由玻色理论的 T-对偶里出现；它不解释 T-对偶本身。
- **要点 / 常见误解**：
  - 不是「把空间换掉」，而是两套几何数据（度规 + $B$ 场）给出同一个量子理论。
  - 开弦情形交换 Neumann 与 Dirichlet 边界条件——这正是 D-膜概念的历史起点。
  - 环面上 T-对偶混合度规与 gerbe（$B$ 场）数据，因此不只是「改半径」。
  - Langlands 对偶的物理来源之一就是它：讲义 §8.6 的论证全靠这一点；Daenzer–van Erp 2014 年把 Langlands 对偶群解释为 T-对偶（arXiv:1211.0763）。
- **nLab**：<https://ncatlab.org/nlab/show/T-duality>

## D-膜（D-brane）

- **一句话定义**：开弦端点所束缚的子流形，等价于二维 QFT 的边界条件（boundary condition）。
- **来历**：Dai–Leigh–Polchinski 1989 年发现 T-对偶把 Neumann 边界条件变成 Dirichlet 条件，从而「发现」D-膜；Polchinski 1995 年识别它是带 R–R 荷的扩展对象。名字来自 Dirichlet。
- **在讲义中的位置**：§6.4「D-模是 D-膜吗？」（`latex/en/e06.tex`）；引言中 Witten 的图景（四维规范场论约化到二维、作用在 D-膜上）。
- **原文为何未解释**：讲义把 D-膜当隐喻使用（D-模像 D-膜），从不定义物理上的 D-膜。
- **要点 / 常见误解**：
  - D-膜是边界条件，不是「一层物质」；它的「位置」由开弦端点自由度决定。
  - B-模型的膜 = 目标空间上的（导出）凝聚层范畴；A-模型的膜 = Fukaya 范畴——这才是「D-模是 D-膜」类比的来源。
  - WZW 的 D-膜最简单由 $G$ 中共轭类给出，带 Chan–Paton 扭曲丛；更一般由 twisted differential K-理论分类。
  - 讲义的用法：Hecke 本征层 ↔ 磁本征膜（'t Hooft 算符的本征膜）。
- **nLab**：<https://ncatlab.org/nlab/show/D-brane>

## 拓扑扭转（topological twist）

- **一句话定义**：把超对称 QFT 的 Lorentz 群与 R-对称群混合，使某个超荷变成标量且幂零，从而得到拓扑不变量。
- **来历**：Witten 1988 年构造拓扑 sigma 模型，1991 年《Introduction to cohomological field theory》（Int. J. Mod. Phys. A 6, 2775）系统总结；把 $N=4$ 超 Yang–Mills 扭转可得到 Donaldson 理论。
- **在讲义中的位置**：§6.4 与关于 Kapustin–Witten 的讨论；讲义用它解释「为什么 D-模可以看作 D-膜」。
- **原文为何未解释**：讲义只在一句话里用「topological twist」，不解释扭转后理论只剩 BRST 上同调。
- **要点 / 常见误解**：
  - 扭转后能动张量成为 BRST 恰当项，故关联函数不依赖度规——这才是「拓扑」。
  - 不同扭转给出 A-模型、B-模型、半扭转模型；选择哪个决定膜范畴。
  - Kapustin–Witten 的 4d TQFT 正是 $N=4$ SYM 的一种扭转（见该条）。
  - 扭转没改变理论的算符内容，只改变「哪些算符存活」。
- **nLab**：<https://ncatlab.org/nlab/show/topological+twist>

## S-对偶（S-duality）

- **一句话定义**：耦合常数 $g\mapsto 1/g$（更一般地 $\mathrm{SL}(2,\mathbb Z)$ 作用在 $\tau=\theta/2\pi+4\pi i/e^2$ 上）下的量子场论等价。
- **来历**：Goddard–Nuyts–Olive 1977 年（Nucl. Phys. B125, 1）指出电菏取值于权格、磁荷取值于对偶群格；Montonen–Olive 1977 年提出规范粒子与磁单极互换的对偶猜想。据 Kapustin–Witten 2006（pp. 3–4），「Montonen–Olive 对偶荷群 = Langlands 对偶群」这一观察归功于 Atiyah 1977 年私下告知 Witten。普通 YM 不真正成立，$N=4$ 超 YM 才像成立（Osborn 1979）。
- **在讲义中的位置**：引言（索引页码 3）与 §6.3–6.4（索引页码 71）；讲义用它说明几何 Langlands 的物理来源。
- **原文为何未解释**：讲义假定读者知道强弱对偶；更重要的是，「S-对偶 ⇒ 几何 Langlands」只是 Witten 的图景，不是定理，原文也没有把它当定理。
- **要点 / 常见误解**：
  - S-对偶不是「同一理论换个参数」，而是两个（可能不同的）理论等价。
  - 电/磁荷格互换正是 $G\leftrightarrow{}^L G$ 的物理版；这是整个类比的种子。
  - type IIB 弦论里它是 axio-dilaton 上的模群作用（F-理论椭圆纤维化）。
  - 4d 的 S-对偶经紧化/扭转后给出 Hitchin 模空间的镜像对称，从而「变成」几何 Langlands——这是物理证明策略，不是数学证明。
- **nLab**：<https://ncatlab.org/nlab/show/S-duality>

## 't Hooft 算符（'t Hooft operator）

- **一句话定义**：沿一条曲线放置磁单极型奇点的线算符，是 Wilson 线的磁对偶。
- **来历**：'t Hooft 1978 年《On the phase transition towards permanent quark confinement》（Nucl. Phys. B138, 1）引入，用来刻画禁闭；Kapustin 2006 年（hep-th/0501015）系统研究 Wilson–'t Hooft 算符与 S-对偶；Kapustin–Witten 2006 年 §9 把它对应到 Hecke 算符。
- **在讲义中的位置**：引言（Kapustin 新引入的 't Hooft 算符经约化后成为 Hecke 算符）；§9.4「Hecke 性质」。
- **原文为何未解释**：讲义只提名字，读者既不知道它是线算符，也不知道它的本征膜正是 Hecke 本征层。
- **要点 / 常见误解**：
  - 它是线算符（沿曲线），不是局域算符；与 Wilson 线互为电/磁对偶。
  - 奇点使场强沿曲线有对数型奇异性（Kapustin–Witten (6.8)–(6.9)），这正是「磁荷沿线的分布」。
  - 在几何 Langlands 图景里：'t Hooft 算符 ↔ Hecke 算符；'t Hooft 本征膜 ↔ Hecke 本征层。
  - 4d 中它一般不是拓扑算符，只在扭转后的 TQFT 里变成可用的拓扑对象。
- **nLab**：<https://ncatlab.org/nlab/show/%E2%80%99t+Hooft+operator>

## Kapustin–Witten 的几何朗兰兹规范论解释（Kapustin–Witten TQFT）

- **一句话定义**：由 $N=4$ 四维超 Yang–Mills 拓扑扭转得到的 4d TQFT（在 $\Sigma\times C$ 上），其 S-对偶被猜想编码 $C$ 上 $G$ 的几何 Langlands 对偶。
- **来历**：Kapustin–Witten 2006 年（arXiv:hep-th/0604151；2007 年发表于 Commun. Number Theory Phys. 1）。
- **在讲义中的位置**：引言中 Witten 的图景；§6.4；§9.6。
- **原文为何未解释**：讲义只说「Kapustin–Witten 的工作表明 Langlands 对偶与 S-对偶密切相关」，完全不展开 TQFT 结构。
- **要点 / 常见误解**：
  - 把 $C$ 紧化掉得到 Hitchin 模空间 $\mathcal M_H(G)$ 上的 A-模型/B-模型；S-对偶表现为 $\mathcal M_H(G)$ 与 $\mathcal M_H({}^L G)$ 的镜像对称。
  - 它交换 Wilson 线与 't Hooft 线，从而交换电本征膜与磁本征膜。
  - 几何 Langlands 的层论侧由「B-膜 → A-膜 → D-模」这一串操作给出。
  - nLab 明确指出：这个方案「尚未变成定理」；数学证明（Gaitsgory 等 2025）走的是完全不同的路线。
- **nLab**：<https://ncatlab.org/nlab/show/Kapustin-Witten+TQFT>

## Hitchin 系统的量子化（quantum Hitchin system）

- **一句话定义**：把 Hitchin 可积系统（余切丛 → Hitchin 基的完全可积系统）量子化，得到的 D-模/量子代数被猜想给出 Hecke 本征层。
- **来历**：Hitchin 1987 年《Stable bundles and integrable systems》引入经典系统；Hitchin 1990 年给出其几何量子化（《Flat connections and geometric quantization》）；Beilinson–Drinfeld 的《Quantization of Hitchin's integrable system and Hecke eigensheaves》（1990 年代，未正式出版）是核心文献；Sugiyama 2007 年（arXiv:0708.2957）给出显式量子化。
- **在讲义中的位置**：§9.5，标题即「Hitchin 系统的量子化」。
- **原文为何未解释**：讲义把「量子化 Hitchin 系统」当作已知框架直接使用，不解释 Hitchin 纤维化为何可积、量子化参数对应什么。
- **要点 / 常见误解**：
  - Hitchin 系统是超 Kähler 模空间上的完全可积系统：纤维是 Jacobian/ Prym 的变形，Hitchin 基上坐标就是谱曲线的系数。
  - 量子化参数 $\hbar$ 与 CFT 的 level（或共形权）对应；取经典极限回到 oper。
  - BD 的量子化把经典 oper 变成 D-模，这一步正是 §9.2「附着于 oper 的 twisted D-模」。
  - 它与 §8 的临界水平 CFT 是同一件事的两条路：一条从 CFT 出发，一条从可积系统出发。
- **nLab**：<https://ncatlab.org/nlab/show/Hitchin+fibration>

## 几何 Langlands 对偶的物理图像（physical picture of geometric Langlands duality）

- **一句话定义**：层论对应 $\mathcal D\mathrm{Mod}(\Bun_G)\simeq \mathcal O\mathrm{Mod}(\mathrm{Loc}_{{}^L G})$ 的物理来源：同一个 4d TQFT 在 S-对偶两侧的两种紧化/边界条件。
- **来历**：数学猜想由 Beilinson–Drinfeld 1990 年代提出（Frenkel 2005 综述）；物理解释由 Kapustin–Witten 2006 年给出，Witten 2009 年（arXiv:0802.0999）进一步阐述。阿贝尔情形已由 Fourier–Mukai 变换证明（Laumon 1985/1996、Rothstein 1996）；一般情形经 Arinkin–Gaitsgory 2012 修正后由 Gaitsgory 等 2025 年证明。
- **在讲义中的位置**：引言与 §9.4–9.6；讲义在数学上严格陈述猜想，物理图像集中在引言。
- **原文为何未解释**：两类论证（物理的 S-对偶 vs 数学的层论）在原文中并置而不统一，读者容易把「物理动机」误当成「证明」。
- **要点 / 常见误解**：
  - 两侧不是「同一对象的两种描述」，而是 S-对偶交换电与磁：Hecke 算符 ↔ 't Hooft 算符，局部系统 ↔ Wilson 本征膜。
  - Hecke 本征层是「磁」侧对象（'t Hooft 本征膜），不是「电」侧；这个方向容易记反。
  - 阿贝尔情形就是 Fourier–Mukai（讲义 §4），可作为整个猜想的「量子力学极限」来理解。
  - 严格化仍是开放问题：Gaitsgory 等的证明是代数几何的，不是物理论证；Langlands 本人 2014 年也对类比的精度有保留。
- **nLab**：<https://ncatlab.org/nlab/show/geometric+Langlands+correspondence>、<https://ncatlab.org/nlab/show/Kapustin-Witten+TQFT>
