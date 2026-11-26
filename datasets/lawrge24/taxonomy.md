# lawrge24 · 卡片总表

底本：LAWRGE 2024 NOTES, *Relative Langlands Duality*（2024-12-03，73 页）。页码为原文 PDF 页；`§N` 对应 `chNN.txt`。

## O · 总览：主陈述、两侧理论、证明地图

| id | 标题 | 类型 | 摘要 |
|---|---|---|---|
| `lawrge/concept/a-and-b-theories` | 自守侧 $A_G$ 与谱侧 $B_{\check G}$ | 概念 | Langlands 对偶是同一个四维 TQFT 的两侧理论 $A_G$ 与 $B_{\check G}$ 的等价：自守侧给函数、表示或层，谱侧给对偶群 $\check G$ 的 Langlands 参数。 |
| `lawrge/concept/proof-map` | 全书证明地图：从 TQFT 到 $L$-层 | 概念 | 全书路线：TQFT 语言（§1–§4）→ 算术–拓扑字典与边界条件（§2–§3）→ 局部硬定理（§7–§11）→ 整体猜想（§13–§15）。 |
| `lawrge/concept/relative-langlands-duality` | 相对朗兰兹对偶：主陈述 | 概念 | 把 Langlands 对偶读成四维 TQFT 的两侧边界：$G$-簇 $X$ 的周期层应与对偶超球 $\check X$ 的 $L$-层匹配，局部形式则是 Plancherel 公式。 |

## A · TQFT 语言与算术–拓扑字典（§1–§3）

| id | 标题 | 类型 | 摘要 |
|---|---|---|---|
| `lawrge/concept/arithmetic-topological-dictionary` | 算术–拓扑字典 | 概念 | 把数论对象与低维流形逐行对应：$\mathbb Q$ 对 3-流形、$\mathbb Q_p$ 对 2-流形、素理想对纽结、$\mathcal O_{\mathfrak p}$ 对管状邻域；它是类比，不是定理。 |
| `lawrge/concept/bordism-category` | 配边范畴 $\mathsf{Bord}^n$ | 概念 | 配边范畴的对象是 $(n-1)$ 维闭流形、态射是 $n$ 维配边，复合是沿公共边界黏合；无交并给它对称幺半结构，定向让进入/出去边界可区分。 |
| `lawrge/concept/boundary-conditions` | 边界条件作为理论的对象 | 概念 | 相对 Langlands 等于 Langlands 加装饰：$G$-空间 $X$ 让带边理论在 $A_G(C)$ 之外多给一个对象 $\mathcal O_{G,X}$；整体侧是周期函数，局部侧是 $X(F_v)$ 上的函数。 |
| `lawrge/concept/lagrangian-tqft` | 拉格朗日 TQFT 与场空间 | 概念 | 拉格朗日 TQFT 把 $Z$ 分解为「场空间函子 $F_Z$ + 线性化 $G$」：$F_Z$ 把配边送到场空间或栈，$G$ 取函数或层，$Z=G\circ F_Z$。 |
| `lawrge/concept/langlands-as-4d-tqft` | Langlands 作为四维 TQFT | 概念 | 把 Langlands 对偶读成四维 TQFT：算术对象给边界，$A_G$ 与 $B_{\check G}$ 是同一四维理论的两侧；黏合给出 Hom 与诱导表示，Hecke 算子内建。 |
| `lawrge/concept/tqft-axioms` | 拓扑量子场论的两条公理 | 概念 | TQFT 是配边范畴到线性范畴的对称幺半函子：无交并映到张量积，且在流形族上局部常值；两条公理分别编码量子叠加与拓扑不变性。 |
| `lawrge/deriv/tqft-1d-assignment` | 一维 TQFT 的赋值 | 推导 | 从配边公理读出 1 维定向 TQFT：点给 $V$ 与 $V^\vee$，杯帽给配对与余配对，圆给 $\dim V$，映射环面给 $\operatorname{tr}Z(f)$。 |

## B · 边界条件、raviolo、Hecke 与 Satake（§4、§7）

| id | 标题 | 类型 | 摘要 |
|---|---|---|---|
| `lawrge/concept/affine-grassmannian` | 仿射 Grassmann 流形 $\mathrm{Gr}=G(F)/G(O)$ | 概念 | 把 raviolo 上的丛按粘接函数拆开后，Hecke 范畴就是 $G(O)$-等变仿射 Grassmann 流形上的层范畴；$\mathrm{Gr}=G(F)/G(O)=LG/L^+G$。 |
| `lawrge/concept/derived-satake` | 导出 Satake：$\operatorname{Shv}(\mathrm{Gr})\simeq\operatorname{IndCoh}(\Omega\check{\mathfrak g}/\check G)$ | 概念 | 导出 Satake 把整个层范畴与对偶侧的奇点范畴等同：$\operatorname{Shv}(\mathrm{Gr})\simeq\operatorname{IndCoh}(\Omega\check{\mathfrak g}/\check G)=\operatorname{QCoh}(\check{\mathfrak g}^*[2]/\check G)$，并与纤维函子相容。 |
| `lawrge/concept/e3-structure` | $E_3$ 结构：三重碰撞给出的对称幺半结构 | 概念 | Hecke 范畴被证明是 $E_3$-范畴：三层叠点的碰撞给出三级乘法；$E_3$ 的交换性正是几何 Satake 中卷积对称幺半的来源，而在分歧点处 $E_3$ 退化。 |
| `lawrge/concept/geometric-satake` | 几何 Satake 等价：$\operatorname{Shv}(\mathrm{Gr})^\heartsuit\simeq\operatorname{Rep}(\check G)$ | 概念 | 几何 Satake 断言仿射 Grassmann 流形上层的 perverse heart 与对偶群的表示范畴对称幺半等价，卷积对应张量积；它是经典 Satake 的范畴化。 |
| `lawrge/concept/hecke-category` | Hecke 范畴 $\mathcal A_G(R)$：碰撞乘法与叠点 | 概念 | Hecke 范畴是 raviolo 上（等价地 $G(O)$-等变仿射 Grassmann 流形上）的层范畴；乘法由三个叠点的碰撞映射给出，原文承认推前的定义域有细节略去。 |
| `lawrge/concept/koszul-duality` | Koszul 对偶：从 $\operatorname{Loc}_{\check G}(R)$ 到 $\check{\mathfrak g}^*[2]/\check G$ | 概念 | Koszul 对偶把 raviolo 上局部算子的范畴从环路空间搬到奇点空间：$\operatorname{IndCoh}(\operatorname{Loc}_{\check G}R)\simeq\operatorname{QCoh}(\check{\mathfrak g}^*[2]/\check G)$，幺半结构由卷积变成张量。 |
| `lawrge/concept/raviolo-hecke` | raviolo 与 Hecke 范畴：把 Hecke 算子几何化 | 概念 | 在曲面 $\Sigma$ 上删去小圆盘的配边无法直接代数化，原文用 raviolo $R=D\sqcup_{D^\times}D$ 代替球面；$R$ 上的层范畴就是 Hecke 范畴。 |
| `lawrge/concept/spectral-action` | 谱作用：$\widehat\otimes_{x\in\Sigma}\operatorname{Rep}\check G$ 经 $\operatorname{QCoh}(\operatorname{Loc}_{\check G}\Sigma)$ 分解 | 概念 | 谱作用定理说：在每个点取 $\mathrm{ev}_x$ 得到的限制张量积 $\widehat\otimes_x\operatorname{Rep}\check G$ 在 $\mathcal A_G(\Sigma)$ 上的作用，经 $\operatorname{QCoh}(\operatorname{Loc}_{\check G}\Sigma)$ 的作用分解。 |

## C · 球簇、对偶群、小 Weyl 群、超球（§8–§10）

| id | 标题 | 类型 | 摘要 |
|---|---|---|---|
| `lawrge/concept/dual-group` | 对偶群 $\check G_X$：由相对 Cartan 与小 Weyl 群装配 | 概念 | 球簇 $X$ 的对偶群 $\check G_X\subset\check G$ 由相对 Cartan $A_X$ 与小 Weyl 群 $W_X$ 决定；它是 $H_G$ 作用经 $\mathbb C[\operatorname{Rep}\check G_X]$ 分解的载体，$\check A_X\to\check A$ 一般不单。 |
| `lawrge/concept/hyperspherical-structure` | 超球簇的结构定理 | 概念 | 定理 10.22 说每个超球簇都由 $(G,H,\iota,S)$ 经 Whittaker 归纳造出；对 $M=T^*X$ 时，对偶侧再多一个由颜色决定的 $\check S$。 |
| `lawrge/concept/hyperspherical-variety` | 超球簇 | 概念 | 超球簇是球簇余切空间的公理化：带交换 $G_{gr}$ 的 Hamilton $G$-簇，要求仿射、余迷向、一般稳定化子连通、矩映射像触及幂零锥、分次作用中性。 |
| `lawrge/concept/little-weyl-group` | 小 Weyl 群 $W_X$ | 概念 | 小 Weyl 群 $W_X$ 是球簇 $X$ 的 Weyl 群：它作用在 $\mathfrak a_X$ 上，可由 $G$-不变赋值、$T^*X/\!/G$ 或 Knop 对 $B$-轨道的作用三种等价方式定义。 |
| `lawrge/concept/multiplicity-free` | 多重数自由：$F[X]$ 中每个最高权至多出现一次 | 概念 | $F[X]$ 作为 $G$-模多重数自由，指每个最高权模 $V_\chi$ 的重数至多 $1$；对拟仿射 $X$，这与「$X$ 是球簇」等价，也是局部内积有限性 (8.16) 成立的条件。 |
| `lawrge/concept/rank-one-freeness` | 秩一自由猜想：$S(X(F))^{G(O)}$ 在 $H_X^G$ 上秩一 | 概念 | 对球簇 $X$，期望球 Schwartz 空间的 $G(O)$-不变部分在 $H_X^G=\mathbb C[\operatorname{Rep}\check G_X]$ 上秩一自由、由 $1_{X(O)}$ 生成；这把局部 Plancherel 化成对偶群的矩阵元。 |
| `lawrge/concept/relative-cartan` | 相对 Cartan 子群 $A_X$ | 概念 | 球簇 $X$ 的 $B$-本征函数只依赖万有 Cartan $A$ 的一个商 $A_X$；对偶地 $\check A_X\to\check A$ 一般不是单射，$\check A_X$ 只是 $\check G_X$ 的极大环面。 |
| `lawrge/concept/spherical-variety` | 球簇：带开稠 Borel 轨道的 $G$-簇 | 概念 | 球簇是正规不可约、某个（等价于任意）Borel 子群有开稠轨道的 $G$-簇；它是相对朗兰兹中 $X$ 侧的正确对象类，局部理论要靠它才能让多重数自由与秩一自由成立。 |
| `lawrge/deriv/dual-group-assembly` | 对偶群 $\check G_X$ 的装配：从 $A_X$、$W_X$ 到 $\mathrm{SL}_2$ 平移 | 推导 | 先由 $B$ 在开轨道上的作用定出 $A_X$，再用 Knop 的赋值锥定出 $W_X$，由此装配 $\check G_X\subset\check G$，最后用主 $\mathrm{SL}_2$-三元组把嵌入平移到 (10.2) 所需的形式。 |
| `lawrge/deriv/rank-one-freeness-derivation` | 秩一自由猜想的推导：从基本向量到 $H_X^G$-模同构 | 推导 | 从 $1_{X(O)}$ 出发，经 Satake 作用、Plancherel 内积与 fusion 乘法，把秩一自由拆成「生成」与「无关系」两步，并指出原文只把它写成期望。 |

## D · Plancherel 与局部范畴化猜想（§8、§11）

| id | 标题 | 类型 | 摘要 |
|---|---|---|---|
| `lawrge/concept/local-conjecture` | 局部范畴化猜想及其修正 | 概念 | 局部猜想把内积等式的两侧提升为范畴等价 $\mathrm{Sh}_c(X_{F/O})\cong\mathrm{QCoh}(\check M/\check G)$；原文自标此式不全对，修正要用 shearing 把分次调正。 |
| `lawrge/concept/local-plancherel` | 局部 Plancherel 公式 | 概念 | 局部 Plancherel 公式断言 $\mathcal C_c(X(F))^{G(O)}\cong\mathbb C[\mathrm{Rep}\,\check G_X]$ 且保持内积，内积由 $\check M$ 的 $q$-特征标在紧形式 $\check G_c$ 上积分给出。 |
| `lawrge/concept/plancherel-density` | Plancherel 密度 | 概念 | Plancherel 密度是球 Schwartz 空间内积在 Satake 侧的核：它等于对偶 Hamilton 空间 $\check M$ 的 $q$-特征标，因此只由 $\check M$ 决定。 |
| `lawrge/concept/shearing` | shearing 修正 | 概念 | shearing 是按 $G_{gr}$ 的半整数分次重设 $\mathbb G_m$-作用的操作，把左边 Frobenius 的 $q^{1/2}$ 与右边整分次对齐，修正后的局部猜想为 (11.19)。 |
| `lawrge/concept/trace-formula-hom` | 内积作为 Hom 上的迹 | 概念 | 把 $\chi_V\chi_W$ 看成 $\mathrm{Hom}(W,V)$ 的特征标，Plancherel 内积就化成 $q^{-1/2}$ 在 $\mathrm{Hom}(\underline W,\underline V)$ 上的迹，再由 sheaf–function 对应对回 Frobenius 的迹。 |
| `lawrge/deriv/inner-product-trace` | 从 Plancherel 内积到 Hom 上的迹 | 推导 | 把 $\chi_V\chi_W$ 读成 $\mathrm{Hom}(W,V)$ 的特征标，Plancherel 内积依次化成 $q^{-1/2}$ 在分次 Hom 上的迹、层范畴的 Hom 上的迹，最后化成 Frobenius 在 $IC$-层 Hom 上的迹。 |

## E · 周期层、L-层、整体猜想、L-函数与例子（§5、§12–§15）

| id | 标题 | 类型 | 摘要 |
|---|---|---|---|
| `lawrge/concept/beilinson-projection` | Beilinson 投影 | 概念 | 把 $\mathrm{Shv}(\mathrm{Bun}_G)$ 投到满足条件 N 的子范畴 $\mathrm{Shv}_N(\mathrm{Bun}_G)$ 的局部化函子 $(-)_{\mathrm{spec}}$。周期层一般不在 $\mathrm{Shv}_N$ 里，整体几何猜想必须先投影；但对 Hecke 特征层做配对时投影不改变答案。 |
| `lawrge/concept/eisenstein-example` | Eisenstein 例：$X=G/N$ | 概念 | 取 $X=G/N$、$T$ 从右侧作用，则 $\mathrm{Bun}^X_{G\times T}=\mathrm{Bun}_B$ 坐在 $\mathrm{Bun}_G\times\mathrm{Bun}_T$ 上方，周期层 $\mathcal P_{G\curvearrowright G/N\curvearrowright T}$ 表示的积分变换就是 Eisenstein 级数函子，其伴随是常项函子；对偶侧把 $N$ 换成 $\check N$、$T$ 换成 $\check T$。 |
| `lawrge/concept/fixed-points` | 导出不动点 | 概念 | $\pi_1(\Sigma)$ 经 $\rho$ 作用在 $\check X$ 上，其不动点必须按导出意义取，即映射空间 $\mathrm{Maps}(\mathrm{pt}/H,Y)$：经典点只是 $H^0$，$H^{\ge1}$ 也要计入，其中 $H^1$ 贡献外代数，正是 L-层纤维与 $L(T_x)$ 的来源。 |
| `lawrge/concept/global-conjecture` | 整体几何猜想 | 概念 | 相对朗兰兹对偶的整体几何形式：周期层经 Beilinson 投影后与 L-层在几何 Langlands 下匹配；朴素版本对 Betti/étale 失效，必须把 A 侧换成满足条件 N 的 $\mathrm{Shv}_N(\mathrm{Bun}_G)$。 |
| `lawrge/concept/hitchin-gaiotto` | Hitchin 截面与 Gaiotto 拉格朗日 | 概念 | Kostant 截面是特征多项式映射 $\check{\mathfrak g}^*/\!/\check G\to\mathfrak c$ 的截面，Hitchin 截面是它的整体类比（$T^*\mathrm{Bun}_G$ 到 Hitchin 基的截面，横截相交整体幂零锥）；Gaiotto 拉格朗日则是 $\mathrm{Bun}^M_G\to\mathrm{Maps}(\Sigma,\mathfrak g^*/G)$ 的像。 |
| `lawrge/concept/l-function` | L-函数 | 概念 | 同时具备 Euler 积、解析延拓与函数方程 $s\leftrightarrow1-s$ 的函数。在相对对偶里它不是事先给定的解析对象，而是周期与自守形式的配对 $\langle\mathcal P_X,f\rangle$，其值要么为 $0$，要么是一个 L-函数。 |
| `lawrge/concept/l-sheaf` | L-层 | 概念 | 谱侧的对应物：在对偶作用 $\check G\curvearrowright\check X$ 的局部系叠上取对偶层的 $*$-前推，得到 $\mathrm{Loc}_{\check G}$ 上的 L-层 $\mathcal L_{\check X}=\check\pi_*\omega$；它的纤维是导出不动点上的上同调，只在不动点孤立处相干。 |
| `lawrge/concept/miraculous-duality` | 奇迹对偶 | 概念 | 群情形 $X=G$ 的周期层与 L-层分别是沿对角线的 $\Delta_!k$ 与 $\Delta_!\omega$；这一匹配编码 Gaitsgory 的奇迹对偶：$\mathrm{Shv}(\mathrm{Bun}_G)$ 上的 Verdier 对偶对应谱侧的 Serre 对偶。 |
| `lawrge/concept/period-sheaf` | 周期层 | 概念 | 把 $G$ 在 $X$ 上的作用沿曲线 $\Sigma$ 整体化：在带截面的 $G$-丛叠 $\mathrm{Bun}^X_G$ 上取常层的 $!$-前推，得到 $\mathrm{Bun}_G$ 上的周期层 $\mathcal P_X=\pi_!k$，它是周期函数 $\Theta_{G,X}$ 的层论对应物。 |
| `lawrge/concept/tate-example` | Tate 例：$\zeta$ 作为周期 | 概念 | 取 $X=\mathbb A^1$、$G=\mathbb G_m$，Riemann 的积分把 $\zeta(s)$ 写成 theta 级数的 Mellin 变换；展开（unfolding）后逐位计算局部积分，$p$ 位直接给出 $\zeta_p(s)=1/(1-p^{-s})$。这是周期层反演 L-函数的最小模型。 |
| `lawrge/concept/whittaker-sheaf` | Whittaker 层 | 概念 | 来自 $M=T^*G/\!/_fN\curvearrowright G$ 与 $G\curvearrowright\mathrm{pt}$ 这对超球对偶的层：谱侧 Whittaker 层 $\mathcal L_{\mathrm{Whit}}$ 匹配 $\mathcal P_\bullet=k_{\mathrm{Bun}_G}$，而把两端归一化后它换成 $\mathcal L_\bullet=\mathcal O_{\mathrm{Loc}_{\check G}}$，A 侧换成沿一个特征取截面的 $\mathcal P_{\mathrm{Whit}}$。 |
| `lawrge/deriv/l-sheaf-fiber` | L-层的纤维：从导出不动点到 $\wedge^*H^1$ | 推导 | 从 L-层的定义 $\mathcal L_{\check X}=\check\pi_*\omega$ 出发，纤维等于 $R\Gamma(\check\pi^{-1}E,\omega)$；导出不动点的切复形是 $H^1(\Sigma,T_x)[-1]$，其上对偶层的截面是外代数 $\wedge^*H^1(\Sigma,T_x)$，取 Frobenius 交错迹即得 $L(T_x)$ 与配对 $\sum_xL(T_x)$。 |
| `lawrge/deriv/zeta-unfolding` | $\zeta$ 的展开：从周期积分到 Euler 积 | 推导 | 从 Riemann 的积分恒等式出发，把 $\zeta(s)$ 写成 theta 级数的 Mellin 变换；经 Poisson 求和与展开（忽略 $\gamma=0$），整体积分按位因子化，$p$ 位局部积分算得 $\zeta_p(s)=1/(1-p^{-s})$，全体相乘即 Euler 积，$\gamma=0$ 项与 $\zeta_\infty$ 一起给出函数方程。 |
