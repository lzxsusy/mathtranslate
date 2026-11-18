# kshms 资料卡 · 总目录

一卡一文件，按轨道（track）分组；点标题进单卡。

## track A · CFT 与几何退化

| 原文 | 标题 | 一句话 |
| --- | --- | --- |
| 猜想 1 | [坍缩的 Gromov–Hausdorff 极限：整仿射 Monge–Ampère 流形](conj-01-collapse-gh-limit.md) | 若 $\mathcal{X}_{mer}$ 在 $q=0$ 处极大退化，则按直径重新标度的 $X_q^{new}$ 在 Gromov–Hausdorff 度量下收敛到紧度量空间 $\bar Y$，其光滑部分带整仿射结构、有势度量与常体积元，即一个实 Monge–Ampère 流形。 |
| 推论 1 | [对偶联络保持整仿射结构](cor-01-integral-affine-dual.md) | 若 $\nabla_Y$ 的和乐含于 $GL(n,\mathbb{Z})$，则命题 2 的对偶联络 $\nabla^\vee_Y$ 也在 $Y^\vee$ 上给出整仿射结构，对偶协变格取代数对偶 $(T^{\mathbb{Z}}_Y)^\vee$。 |
| 定义 1 | [极大退化（$m=n$）](dfn-01-maximal-degeneration.md) | 单参数 Calabi–Yau 族在 $q=0$ 处，若体积按 $|q|^{2k}(\log|q|)^m$ 增长而对数因子的幂次取到上界 $m=\dim X$，则称该退化是极大的；这是「大复结构极限」的解析刻画。 |
| 引理 1 | [Legendre 变换保持 Monge–Ampère 方程](lem-01-legendre-transform-monge-ampere.md) | 凸区域上满足 Monge–Ampère 方程的 $K$，其 Legendre 变换 $\widehat K$ 仍满足同一方程；证明把方程读作 $dK$ 的拉格朗日图像上两个体积形式的相等。 |
| 命题 1 | [极大退化当且仅当单值算子的幂零指数为 $n+1$](prp-01-maximal-degeneration-nilpotent.md) | 极大退化可等价地刻画为单值算子 $T$ 满足 $(T-\operatorname{Id})^{n+1}=0$ 而 $(T-\operatorname{Id})^{n}\ne0$：体积增长中对数因子的最高幂次，正是 $T$ 的幂零指数。 |
| 猜想 2 | [坍缩的首项渐近：$X_q^{new}$ 逼近 $\varepsilon$-环面丛](conj-02-collapse-ma-model.md) | 猜想 1 的加强版：存在 $C>0$ 与扭 $t(q)$，使 $X_q^{new}$ 在切空间层面按 $o(1)$ 逼近环面丛 $X^{\varepsilon(q),t(q)}$（$\varepsilon(q)=C(\log|q|)^{-1}$），并整体收敛到配对 $(\bar Y,Y^{sing})$。 |
| 定义 2 | [Monge–Ampère 流形](dfn-02-monge-ampere-manifold.md) | 三元组 $(Y,g,\nabla)$：$\nabla$ 平坦，$g$ 在仿射坐标下是局部势函数 $K$ 的 Hessian，且 $\det(\partial_i\partial_jK)$ 为常数；这是环面纤维化对偶的几何语言。 |
| 命题 2 | [对偶 Monge–Ampère 流形的典范存在性](prp-02-dual-monge-ampere-manifold.md) | 每个 Monge–Ampère 流形 $(Y,g_Y,\nabla_Y)$ 都有典范对偶 $(Y^{\vee},g^{\vee}_Y,\nabla^{\vee}_Y)$：底流形与度量不变，只把平坦联络换成对偶联络，切局部系随之换成对偶局部系。 |
| 猜想 3 | [几何镜像对称：对偶族的坍缩极限互为对偶 Monge–Ampère 流形](conj-03-dual-ma-manifolds.md) | 几何镜像对称的猜想形式：一对对偶 Calabi–Yau 族在极大退化处，坍缩极限的光滑部分互为对偶的 Monge–Ampère 流形，其整仿射结构也互为对偶。 |
| 命题 3 | [Clemens 复形 $\bar Y(X_0)$ 与稳定约化模型的选取无关](prp-03-clemens-complex-model-independence.md) | 对具稳定约化的模型作不同选取，由本质除子张成的 Clemens 复形 $\bar Y(X_0)$ 可以典范等同；于是 $\bar Y$ 只依赖 $X$ 与体积形式，不依赖模型。 |
| 注 1 | [本文的几何讨论对应 $N=2$ 超共形场论](rmk-01-scft-vs-cft.md) | 全文的口径声明：§2 的数据与公理实为 $N=2$ 超共形场论的版本，$H^{p,q}$ 是 Hermite 超向量空间；因细节不影响主要结论，下文不再区分 CFT 与 SCFT。 |
| 注 2 | [严格定义的 CFT 只有两类，$\sigma$ 模型两者都不是](rmk-02-rigorous-cft-classes.md) | 数学上严格定义的 CFT 只有有理理论与格共形场论两类，本文要谈的 $\sigma$ 模型两者都不是；路径积分构造尚缺，故改用「CFT 的退化」来谈论 $\sigma$ 模型。 |
| 注 3 | [CFT 模空间的紧化应包含 Einstein 流形模空间的紧化](rmk-03-einstein-vs-gromov.md) | 简单坍缩的目标空间应是 Ricci 平坦流形，故 CFT 模空间的紧化必须包含 Einstein 流形模空间的紧化；作者引 Gromov 预紧性定理作类比，并推测极限目标空间的 Ricci 曲率非负。 |
| 注 4 | [$K$ 凸故 Legendre 变换局部可用；$\bar Y$ 何时是同调球](rmk-04-convex-potential-legendre.md) | 两点技术说明：$(g_{ij})$ 正定使势 $K$ 凸、Legendre 变换局部可用（§3.2 对偶所需）；并预期 $X_q$ 单连通且中间 Hodge 数消失时 $\bar Y$ 是同调球，例子中同胚于 $S^n$。 |
| 注 5 | [Gross–Wilson 独立提出同类猜想并在退化 K3 上验证](rmk-05-gross-wilson-k3.md) | 文献归属与证据：Gross–Wilson 独立提出同类猜想并在退化 K3 上验证；本文正文只在复阿贝尔簇情形使猜想成立（§8 定理 4），一般情形仍是猜想。 |
| 注 6 | [用 Legendre 变换做镜像对称的想法早已有之](rmk-06-legendre-idea.md) | 文献归属注：把 Legendre 变换用于镜像对称的想法此前已有（[H]、[Le]）；本文的新意是把它与整仿射结构、环面纤维化的对偶接起来。 |
| 注 7 | [忽略 $B$ 场：全篇假设 $B=0$](rmk-07-b-field-zero.md) | 全篇的全局约定：几何镜像对称的描述忽略 $B$ 场，此后恒设 $B=0$——对偶因此成为纯黎曼几何加整仿射结构的陈述。 |
| 勘误 0 | [p1：$H^2(X,\mathbb{Z})$ 应为 $H^2(X^\vee,\mathbb{Z})$](p01-h2-x-vs-xdual.md) | §1 讨论 $q$ 的指数时把辛侧流形的上同调写成了复侧流形：应是 $[\omega^\vee]\notin H^2(X^\vee,\mathbb{Z})$。 |
| 勘误 0 | [p9：$SU(2)$ WZW 模型中心荷的 $\phi_n/\phi_k$ 混写](p09-wzw-phi-n-vs-phi-k.md) | §2.5 同一句话里 $SU(2)$ WZW 模型的中心荷足标出现两种写法（$\phi_n$ 与 $\phi_k$），应统一。 |
| 勘误 0 | [p11：$\S2.7$ 多出一个右括号](p11-extra-paren.md) | §2.7 讲「镜像对称给出两个邻域之间的等同」一句括号不配对（多一个右括号）。 |
| 勘误 0 | [p14：命题 1 内 $T-\mathrm{Id}$ 与 $T-\mathrm{id}$ 混用](p14-t-id-vs-t-id.md) | 命题 1 同一陈述内把单值算子减单位算子写成 $T-\mathrm{Id}$ 与 $T-\mathrm{id}$ 两种。 |

## track B · $A_\infty$ 形式框架

| 原文 | 标题 | 一句话 |
| --- | --- | --- |
| 定义 3 | [非幺 $A_\infty$-代数](dfn-03-nonunital-a-inf-algebra.md) | 域 $k$ 上的分次模 $A$ 连同余自由张量余代数 $T_+(A[1])$ 上一个 $+1$ 次、平方为零的余微分 $d$；等价于给出一列满足 $A_\infty$ 关系的运算 $m_n$。 |
| 猜想 4 | [$A_\infty$-预范畴与带严格单位态射的 $A_\infty$-范畴：等价类一一对应](conj-04-strict-unit-equivalence.md) | 仿照预范畴定义带严格单位态射的 $A_\infty$-范畴的等价后，猜想两边的等价类一一对应——即把 $A_\infty$-范畴嵌入预范畴框架不会丢失等价信息。 |
| 定义 4 | [非幺 $A_\infty$-代数之间的态射](dfn-04-nonunital-a-inf-morphism.md) | 两个非幺 $A_\infty$-代数之间的态射是张量余代数 $T_+(V[1])\to T_+(W[1])$ 之间与余微分交换的零次态射，展开为一列 Taylor 系数 $f_n$ 的方程组。 |
| 猜想 5 | [有向 $A_\infty$-预范畴与可数 $A_\infty$-范畴：等价类一一对应](conj-05-directed-equivalence.md) | 有向 $A_\infty$-预范畴（对象类 $\simeq\mathbb{Z}$、横截序列递增）的等价类，猜想与带严格单位态射、对象类可数的 $A_\infty$-范畴的等价类一一对应。 |
| 定义 5 | [非幺 $A_\infty$-范畴](dfn-05-nonunital-a-inf-category.md) | 对象类、每对对象的 $\operatorname{Hom}$ 分次模、以及对每个对象序列的复合 $m_n$；要求任意对象序列的 $\operatorname{Hom}$ 直和构成非幺 $A_\infty$-代数。 |
| 定义 6 | [非幺 $A_\infty$-范畴之间的函子](dfn-06-nonunital-a-inf-functor.md) | 对象映射 $\phi$ 加一族 $f_n$（$n\ge0$），使每个对象序列的 $\operatorname{Hom}$ 直和之间的映射成为 $A_\infty$-态射（定义 4）。 |
| 定义 7 | [非幺 $A_\infty$-预范畴](dfn-07-nonunital-a-inf-pre-category.md) | 在非幺 $A_\infty$-范畴上加一个横截序列类：$\operatorname{Hom}$ 与复合 $m_n$ 只对横截序列定义，横截性对子序列封闭，方程与定义 5 相同。 |
| 定义 8 | [非幺 $A_\infty$-预范畴之间的函子](dfn-08-nonunital-a-inf-pre-functor.md) | 对象映射 $\phi$ 须把横截序列送到横截序列，$f_n$ 只在横截序列上定义，并要求递增指标直和之间的映射是 $A_\infty$-态射。 |
| 定义 9 | [拟同构（$A_\infty$-预范畴中的态射）](dfn-09-quasi-isomorphism.md) | 非幺 $\mathcal{A}_\infty$-预范畴中的零次态射 $f$，若 $m_1(f)=0$ 且左乘、右乘 $f$ 都给出复形的拟同构，就称为拟同构；它在横截框架下替代了同构态射的地位。 |
| 定义 10 | [扩张性质与 $A_\infty$-预范畴](dfn-10-extension-property.md) | 要求任意有限族横截序列都能在两端各接上一个与给定对象拟同构的对象而仍保持横截；满足此性质的非幺预范畴称为 $A_\infty$-预范畴，这是单位态射的同伦替代。 |
| 定义 11 | [$\mathcal{A}_\infty$-函子（预范畴之间）](dfn-11-a-inf-functor.md) | 两个 $A_\infty$-预范畴之间的 $A_\infty$-函子，就是相应的非幺预范畴函子中把拟同构映为拟同构的那些；它比定义 12 的等价函子少一条本质满条件。 |
| 定义 12 | [$\mathcal{A}_\infty$-等价函子](dfn-12-a-inf-equivalence-functor.md) | $A_\infty$-函子若在对象上本质满（每个对象都拟同构于某个 $\phi(X)$），且对一切横截对象序列诱导态射 $A_\infty$-代数的拟同构，则称等价函子。 |
| 定义 13 | [$A_\infty$-预范畴的等价](dfn-13-a-inf-precategory-equivalence.md) | 两个 $A_\infty$-预范畴称为等价，若存在有限链把二者连接，且链上相邻两项之间（任一方向）都有 $A_\infty$-等价函子；等价函子由此生成等价关系。 |
| 定义 14 | [带严格单位态射的 $\mathcal{A}_\infty$-范畴](dfn-14-strict-identity-a-inf-category.md) | 在非幺 $A_\infty$-范畴的每个 $\operatorname{Hom}^0(X,X)$ 中指定 $1_X$，使 $m_2$ 以它为左右单位、且 $n\ne2$ 时任何位置插入 $1$ 都使 $m_n$ 为零，即得带严格单位态射的 $A_\infty$-范畴。 |
| 定义 15 | [有向 $\mathcal{A}_\infty$-预范畴](dfn-15-directed-a-inf-precategory.md) | 对象类与 $\mathbb{Z}$ 双射、横截序列恰为指标严格递增序列的 $A_\infty$-预范畴；此时扩张性质化为「每个对象在两侧都有与之拟同构的对象」。 |
| 注 8 | [非幺 $A_\infty$-代数就是单对象的非幺 $A_\infty$-范畴](rmk-08-one-object-category.md) | 非幺 $A_\infty$-代数可看成只有一个对象 $X$、自同态空间为 $A$ 的非幺 $A_\infty$-范畴；此后代数层面的构造都可逐字搬到范畴层面。 |
| 注 9 | [取 $m_1$ 上同调得到非幺范畴 $H(\mathcal{C})$](rmk-09-cohomology-category.md) | 把非幺 $A_\infty$-范畴的态射空间换成 $m_1$ 的上同调、复合改由 $m_2$ 诱导，得到非幺范畴 $H(\mathcal{C})$；对象不变，高阶运算不再出现。 |
| 注 10 | [预范畴上部分定义的 $m_2$ 在 $H(\mathcal{C})$ 上唯一延拓](rmk-10-precategory-extension.md) | 对 $A_\infty$-预范畴，$m_2$ 只在横截序列上有定义；取 $m_1$ 上同调后它可唯一延拓，使 $H(\mathcal{C})$ 成为通常范畴，这一步依赖定义 10 的延拓性质。 |
| 勘误 0 | [p25：定义 7 复合方程的下标错位](p25-dfn7-subscript.md) | 定义 7 的复合方程把 $m_j$ 的 $j$ 个变元写成 $a_l,\dots,a_{l+j}$（应为 $a_l,\dots,a_{l+j-1}$），与 $m_j$ 的元数及定义 3 的同一方程都不合。 |
| 勘误 0 | [p26：应为「非幺 $A_\infty$-范畴」而非「预范畴」](p26-pre-categories-vs-categories.md) | §4.3 首段说「与非幺 $A_\infty$-预范畴的情形不同」，但比较对象是定义 6（范畴的函子）与定义 8（预范畴的函子）所诱导的 $A_\infty$-态射，故应为「范畴」。 |
| 勘误 0 | [p27：定义 13 的 $C_0=D$ 应为 $C_n=D$](p27-dfn13-c0-cn.md) | 定义 13 写 $\mathcal{C}_0=\mathcal{C}$、$\mathcal{C}_0=\mathcal{D}$，与所取有限序列 $(\mathcal{C}_0,\dots,\mathcal{C}_n)$ 不合；同处的 $0\le i\le k-1$ 亦应为 $0\le i\le n-1$。 |

## track C · Fukaya 与退化

| 原文 | 标题 | 一句话 |
| --- | --- | --- |
| 定理 1 | [Fukaya 范畴的等价类只依赖连通分支](thm-01-fukaya-category-equivalence-class.md) | 在相容殆复结构空间的某个第二纲集 $\Sigma$ 上，只要 $(J_1,\Omega_1)$ 与 $(J_2,\Omega_2)$ 同伦，两个 Fukaya 范畴就等价；故等价类只依赖这对数据所在空间的连通分支。 |
| 命题 4 | [小哈密顿形变不改变对象的拟同构类](prp-04-fukaya-hamiltonian-deformation-quasi-iso.md) | 由 $\mathcal{F}(V)$ 的对象 $(L,\rho)$ 经小哈密顿形变得到的 $(L_t,\rho_t)$，与 $(L,\rho)$ 拟同构；这条延拓性质让横截序列可以补足缺失的对象。 |
| 命题 5 | [Fukaya–Oh 范畴：$\eta\to0$ 的极限与 $\mathcal{F}^\eta_{unram}$ 等价](prp-05-fukaya-oh-limit-equivalence.md) | $\mathcal{F}^\eta_{unram}(X^{\vee})$ 的复合映射在 $\eta\to0$ 时于 $\mathbb{C}_\varepsilon$ 的 adic 拓扑下收敛，所得极限 $A_\infty$-预范畴对充分小的 $\eta$ 与原范畴等价，记为 $FO(X^{\vee})$。 |
| 定义 16 | [Fukaya 范畴的对象（三元组）](dfn-16-fukaya-objects.md) | Fukaya 范畴的对象是三元组：带自旋结构的紧定向拉格朗日子流形、其上的局部系、以及辐角函数的连续提升；并要求辛形式在相对球面类上的配对为零。 |
| 定义 17 | [Fukaya 范畴的态射空间](dfn-17-fukaya-morphism-spaces.md) | 对支撑横截的两个对象，态射空间取各交点处局部系纤维间线性映射的直和，再张量系数域；Maslov 指标给出 $\mathbb{Z}$-分级。 |
| 注 11 | [条件 $([\omega],\beta)=0$：为绕开 $m_0$ 而设的方便假设](rmk-11-zero-pairing-condition.md) | 要求 $([\omega],\beta)=0$ 只是为避免非平凡 $m_0$ 带来的复合问题；环面与拉格朗日子环面满足它，adic 拓扑下足够小的 $m_0$ 也有替代处理。 |
| 注 12 | [非零 $B$ 场：可以并入定义，但本文不并入](rmk-12-b-field-omitted.md) | 本文各节定义都可修改以容纳非零 $B$ 场；作者选择不改，只为避免记号膨胀。这是书写约定，不是把 $B$ 场情形排除在外。 |
| 注 13 | [Maslov 指标等于 $f_1-f_2$ 的 Morse 指标](rmk-13-maslov-equals-morse.md) | 当 $L_i$ 在交点局部是 $df_i$ 的图时，$x\in L_1\cap L_2$ 处的 Maslov 指标等于 $f_1-f_2$ 在 $p^\vee(x)$ 的 Morse 指标；Floer 分级因此化为 Morse 分级。 |
| 注 14 | [假设 $\dim Y>1$：一维情形另行处理](rmk-14-dimension-assumption.md) | 后文假设 $\dim Y>1$；$\dim Y=1$ 时构造略有不同但更简单，且 $\mathcal{F}^\eta_{\mathrm{unram}}(X^\vee)$ 不依赖 $\eta$，故不能把一般维数结论直接照搬。 |
| 注 15 | [越过横截对象：纤维环面上的局部系](rmk-15-non-covering-objects.md) | 可把 $FO(X^\vee)$ 推广到非分歧覆盖之外的拉格朗日子流形：在投影的纤维环面上取局部系。奇纤维时几乎所有纤维不带全纯盘，故得到无 $m_0$ 的新对象，但坏点集 $Z$ 稠密使整体图景复杂。 |

## track D · Morse 机器

| 原文 | 标题 | 一句话 |
| --- | --- | --- |
| 引理 2 | [投影算子 $R_\delta$ 的三条性质](lem-02-projection-operator.md) | 由对角线邻域上的闭 $n$-形式 $\rho_\delta$ 定义的积分算子 $R_\delta$ 是复形同态、在交点处实现相交数，并带有同伦 $h_\delta$ 使 $dh_\delta+h_\delta d=\mathrm{id}-R_\delta$。 |
| 定理 2 | [Morse 范畴与 de Rham 范畴等价](thm-02-morse-de-rham-equivalence.md) | 光滑函数的 Morse $A_\infty$-预范畴 $\mathcal{M}(Y)$ 与 de Rham $A_\infty$-范畴 $\mathrm{DR}(Y)$ 等价：先用同调扰动把 de Rham 复形压到 Morse 复形上，再逐树比较高阶复合。 |
| 定理 3 | [子复形上的 $\mathcal{A}_\infty$-代数结构](thm-03-subcomplex-a-inf-structure.md) | 设 $B=\operatorname{Im}\Pi$ 是 $\mathcal{A}_\infty$-代数 $A$ 上幂等投影的像，且 $1-\Pi=dH+Hd$；把平面树的尾顶点配 $i$、旧顶点配 $m_k$、新顶点配 $H$、根配 $p$ 所得的 $m_n^B$ 满足 $\mathcal{A}_\infty$-约束。 |
| 命题 6 | [$m_1^B$ 定义了 $B$ 上的微分](prp-06-m1b-differential.md) | 把 $m_1$ 沿投影 $\Pi$ 与嵌入 $i$ 压到子复形 $B=\Pi(A)$ 上，得到 $m_1^B=p\circ m_1\circ i$，它满足 $(m_1^B)^2=0$，故 $B$ 上有一个微分。 |
| 命题 7 | [嵌入 $i:B\to A$ 可延拓为 $A_\infty$-拟同构](prp-07-a-inf-quasi-isomorphism-b-to-a.md) | 存在典范的 $A_\infty$-态射 $g:B\to A$：$g_1$ 取嵌入 $i$，高阶 $g_n$ 由带同伦 $H$ 的平面树给出，它给出 $A_\infty$-代数的拟同构，故 $A$ 与 $B$ 在 $A_\infty$ 意义下等价。 |
| 命题 8 | [Morse 投影算子 $\Pi_\delta$：幂等、与 $d$ 交换、像同构于 Morse 复形](prp-08-morse-projector-pi-delta.md) | 用磨光核 $R_\delta$ 与临界点的稳定、不稳定流定义的算子 $\Pi_\delta$ 是投影：$\Pi_\delta^2=\Pi_\delta$、$\Pi_\delta d=d\Pi_\delta$，且它在 Morse 复形上的像典范同构于 $M^*(Y,f)$。 |
| 定义 18 | [$T$-横截的函数序列](dfn-18-t-transversal.md) | 给定带 $k+1$ 条尾的平面树 $T$，若对维数不超过零的每个交点序列，梯度树模空间的子流形族都横截，则称函数序列为 $T$-横截；$k=1$ 时退化为 Morse–Smale 条件。 |
| 定义 19 | [横截的对象序列（Morse 范畴）](dfn-19-transversal-objects.md) | 若对象序列的任意子序列对任意带 $m+1$ 条尾的二元树都 $T$-横截，则称该对象序列横截；这是 Morse 范畴中高阶复合得以定义的前提。 |
| 定义 20 | [Morse 范畴的高阶复合 $m_k$](dfn-20-morse-composition.md) | 对横截的对象序列，$m_k$ 按带 $k+1$ 条尾的定向二元平面树求和：每棵树取梯度树模空间的带符号点数，作用在临界点基上得到输出临界点。 |
| 注 16 | [只考虑虚维数 $\le 0$ 的模空间](rmk-16-virtual-dimension.md) | 与 Fukaya 范畴一样，Morse 侧只考虑虚维数不超过零的模空间 $\mathcal{M}(T;f_0,\dots,f_k;x_0,\dots,x_k)$；维数严格为负时 $T$-横截条件迫使它为空。 |
| 注 17 | [扰动构造逐范畴成立；命题 4、5 应在 operad 代数上成立](rmk-17-perturbation-general.md) | 同调扰动可逐态射空间搬到任意非幺 $A_\infty$-范畴：给定 $\Pi_{X,Y},H_{X,Y}$ 后公式不变，所得范畴与原范畴等价；作者并预期命题 4、5 对 operad 上的代数也成立。 |
| 注 18 | [投影算子的另一典范元素 $\sum [S_x]\otimes R_\delta([U_x])$](rmk-18-alternative-canonical-element.md) | $\Pi_\delta$ 也可用典范元素 $\sum_x[S_x]\otimes R_\delta([U_x])$ 定义，而不必用 $\sum_x R_\delta([S_x])\otimes R_\delta([U_x])$；命题 8 的结论对新元素同样成立。 |
| 勘误 0 | [p46：引理 2 的三处排印疏漏](p46-lemma2-typos.md) | 引理 2 有三处排印疏漏：第 2) 款 $Z_1,Z_2\in Y$ 应为 $\subset Y$；等价链末项多一个右括号；末段第二个 $m_k^{M(Y)}$ 应为 $m_k^{DR_0^{tr,\Pi}(Y)}$。 |
| 勘误 0 | [p46：$\S6.6$ 末「with with」重出](p46-with-with.md) | 定理 3 之后一句「move on $Y$ with with different speeds」重出一个 with。 |

## track E · 刚性解析与凝聚层

| 原文 | 标题 | 一句话 |
| --- | --- | --- |
| 命题 9 | [刚性解析模型：$Y^{an}\simeq\mathcal{Y}^{an}$（Mumford 构造）](prp-09-mumford-construction.md) | 整仿射实环面 $Y$ 的刚性解析空间 $Y^{an}$ 同构于某个 $\mathbb{C}_{\varepsilon}$ 上阿贝尔簇的解析化；这让度量坍缩的黎曼几何描述与非阿基米德解析描述给出同一个对象。 |
| 命题 10 | [解析侧收尾：$C(Y)$ 与 $D^b_{\mathcal{A}_\infty}(\mathcal{Y})$ 的 $\mathcal{A}_\infty$-等价](prp-10-analytic-hms.md) | 把 $\mathcal{O}_Y$ 换成解析侧的消解不改变 $\mathcal{A}_\infty$-结构：$C(Y)$ 与射影代数簇 $\mathcal{Y}$ 的 $\mathcal{A}_\infty$-增强导出范畴等价，这是 GAGA 在 $\mathcal{A}_\infty$ 层面的体现。 |
| 定义 21 | [形式 Laurent 级数层 $\mathcal{O}_{\mathbb{R}^n}(U)$](dfn-21-formal-laurent-series.md) | $\mathcal{O}_{\mathbb{R}^n}(U)$ 由在开集 $U$ 上满足增长条件的形式 Laurent 级数组成，系数在 $\mathbb{C}_\varepsilon$ 中；它是刚性解析空间 $Y^{an}$ 的局部模型。 |
| 定义 22 | [刚性解析空间 $Y^{an}$](dfn-22-rigid-analytic-space.md) | 对带整仿射结构的光滑流形 $Y$，用局部数据 $(U_i,\mathcal{O}_{U_i})$ 经 $GL(n,\mathbb{Z})\ltimes\mathbb{R}^n$ 的作用粘合，得到 $\mathbb{C}_\varepsilon$ 上的刚性解析空间 $Y^{an}$。 |
| 注 19 | [扭曲结构层 $\mathcal{O}'_Y$：为什么 $Y^{an}$ 是「错的」](rmk-19-oy-tilde.md) | 带奇异纤维坍缩时，按 $\mathcal{O}_Y$ 造的刚性解析空间 $Y^{an}$ 不紧、也嵌入不了射影紧化；作者猜测应换成同构于 $\mathcal{O}_Y$ 的扭曲层 $\mathcal{O}'_Y$，其同构类由 $H^1(Y,\underline{\mathrm{Aut}}(\mathcal{O}_Y))$ 分类——这是非阿贝尔簇情形镜像对称所需的新要素。 |

## track F · 同调镜像猜想

| 原文 | 标题 | 一句话 |
| --- | --- | --- |
| 定理 4 | [阿贝尔簇的同调镜像对称](thm-04-abelian-hms.md) | 对阿贝尔簇的镜像对 $(X,X^\vee)$，$C(Y)$ 的满子范畴 $F(C_{unram}(Y))$ 与 $X^\vee$ 的 Fukaya–Oh 范畴 $\mathcal{A}_\infty$-等价；这是本文对同调镜像猜想的表述。 |
| 命题 11 | [半群 $\psi^t$ 使滤过下降](prp-11-spectrum-semigroup.md) | 由 $1$-形式 $\mu$ 对应的向量场 $\xi$ 生成的半群 $\psi^t$，把态射层茎上的 $\mathbb{R}$-滤过整体下移 $\int_0^t\mu$；这是 $\phi^t$ 能连续延拓到完备化的关键。 |
| 命题 12 | [$\phi^t$ 连续延拓到完备化的态射空间](prp-12-continuous-extension.md) | 因为 $\psi^t$ 使滤过下降，只在指数有限和上定义的 $\phi^t$ 可连续延拓到整个态射空间 $\mathrm{Hom}_{C(Y)}(E_1,E_2)$，即延拓到滤过的完备化上。 |
| 命题 13 | [极限 $\psi^{\infty}(\beta)$ 存在（$t\to+\infty$）](prp-13-psi-infinity-limit.md) | 紧支集截面经 $\psi^t$ 推动后，当 $t\to+\infty$ 有极限 $\psi^{\infty}(\beta)$，落在分布值 Dolbeault 形式空间中，其像由不稳定流形对应的分布张成。 |
| 命题 14 | [$FO(X^{\vee})$ 与 $C^{tr,\Pi}_{unram,0}(Y)$ 的 $m_k$ 公式吻合](prp-14-mk-formulas-agree.md) | 把标量扩到 $\mathbb{C}_{\varepsilon}\widehat{\otimes}\Omega^{*0}$、并经 $\nu(X_i,X_j)$ 认同态射空间后，Fukaya–Oh 侧与 $C^{tr,\Pi}_{unram,0}(Y)$ 侧的 $m_k$ 公式逐条相同，故两范畴 $\mathcal{A}_\infty$-等价。 |
| 注 20 | [用 $\mathbb{R}$-滤过代替谱](rmk-20-spectrum-filtration.md) | 不必用谱，也可以在态射空间上取 $\mathbb{R}$-滤过 $\mathrm{Hom}(E_1,E_2)^{\le s}$：它由态射层完备张量积的茎上的一族不等式定义，且 $\alpha$ 落在第 $s$ 层当且仅当对每个 $y$ 都有 $\mathrm{Sp}_y(\alpha)\subset(-\infty,s]$。 |
| 注 21 | [平坦环面上的截断 theta 级数](rmk-21-truncated-theta.md) | 若把环面 $Y=\mathbb{R}^n/\mathbb{Z}^n$ 配上平坦度量、只取 $X^{\vee}$ 中的平坦拉格朗日子环面，则 $FO(X^{\vee})$ 的全部高次复合都能写成显式的「截断 theta 级数」，与椭圆曲线情形所见的级数同型。 |
| 勘误 0 | [p57、p58：$C^{tr,\Pi}_{unrum,0}(Y)$ 应为 $unram$](p57-unrum-vs-unram.md) | §8.3 两处把 $C^{tr,\Pi}_{unram,0}(Y)$（unramified，非分歧）拼作 $unrum$。 |

## track G · 复情形附录

| 原文 | 标题 | 一句话 |
| --- | --- | --- |
| 引理 3 | [Poincaré 丛上的典范联络](lem-03-connection-on-poincare-bundle.md) | 在 $T_Y\times_YT^*_Y$ 的典范平凡化上用 $\overline{\nabla}=\nabla_0+\frac{2\pi i}{\varepsilon}\sum_jx_j^\vee dx_j$ 定义的联络，在两组甲板变换下都不变，故下降为 Poincaré 丛 $P$ 上的联络。 |
| 命题 15 | [曲率 $(0,2)$-部分平凡：$\nabla_E$ 是全纯联络](prp-15-holomorphic-connection.md) | 复情形中 $F(L,\rho)$ 上的诱导联络 $\nabla_E$ 的曲率 $(0,2)$-部分为零，故 $\nabla_E$ 全纯；这使镜像函子的像落在全纯向量丛范畴里。 |
| 定义 23 | [Dolbeault 态射空间 $\mathrm{Hom}_{\mathrm{Dolb}}$](dfn-23-hom-dolb.md) | 对 $X$ 上两个全纯向量丛，$\mathrm{Hom}_{\mathrm{Dolb}}$ 取取值于 $\mathrm{Hom}(E_1,E_2)$ 的 $(0,*)$-形式空间；配以 $\bar{\partial}$-微分后成为 dg-代数。 |
| 注 22 | [$\varepsilon\to0$ 时系数是渐近级数](rmk-22-asymptotic-coefficients.md) | 当 $\varepsilon$ 不是固定常数而是趋于 $0$ 的参数时，Dolbeault 形式展开的系数不再是函数，而是形如 $\sum_{j\ge1}e^{-\lambda_j/\varepsilon}f_{j,i_1\dots i_n}$ 的渐近级数；展开式中出现的指数集合正对应非阿基米德情形的谱 $\mathrm{Sp}_y(\alpha)$。 |
