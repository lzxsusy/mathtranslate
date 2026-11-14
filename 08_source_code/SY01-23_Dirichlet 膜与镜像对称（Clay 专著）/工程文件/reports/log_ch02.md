# ch02 校订日志（rv-ch02）

负责文件：`chapters/ch02.tex`；负责 PDF 页码 37–118（第2章）。
对照材料：`review/chunks/ch02/` 下 8 块。

## 已核对范围
- 块1 p037-046 ✅：ch02-intro-001 ~ ch02-2.1.5-003（含定理 A/B、脚注、例 2.2 引入、图1–图6 图题、Theorem 2.1、2.1.5 直和构造 2.1–2.17）
- 块2 p048-057 ✅：ch02-example-2.2 ~ 块末导出范畴 K（含三个基本问题、极大范畴、2.1.6 自旋理论、脚注6、2.18–2.19、Example 2.3、Example 2.4、2.1.7 上链理论 2.25–2.28、Note 2.5）
- 块3 p058-067 ✅：ch02-2.1.7-009 ~ ch02-2.3-002（含 2.2.1 分类定理、2.29–2.42、Theorem 2.6/2.8、Lemma 2.7、Note 2.9、2.2.2 B 场、2.2.3 Hochschild/循环上同调 2.43–2.46、图13、2.2.4 自旋理论与模2分次范畴 2.47–2.49、2.3 节开头、图14）
- 块4 p068-077 ✅：ch02-2.3-003 ~ ch02-2.5.3-003（含图14 后段 2.50–2.55、2.3.1 Cardy/Ishibashi 2.56–2.61、2.4 Landau–Ginzburg 2.57–2.66、Example 2.10、2.4-009~011、2.5 节、2.5.1 与流形上同调 2.67–2.73、2.5.2 Chas–Sullivan 2.74–2.77、2.5.3 B 模型 2.78–2.79、Atiyah 类）
- 块5 p078-088 ✅：ch02-2.5.3-004 ~ ch02-2.6.3.2-002（含 Witten 闭弦代数、$\partialbar$ 复形与导出范畴、§2.6 等变理论开头、2.6.1 规范化 S_G/扭曲扇区/Turaev 同伦 TFT/2.80–2.82、2.6.1-011~014 的 2.83/2.84 与 Theorem 2.11、Remark 2.12、2.6.2 Gauss 定律与 2.86、2.6.3 Turaev 分类、2.6.3.1 X//G 与 $|\mathcal{C}|$、B 场/二上链 2.88–2.91、2.6.3.2 小环路代数 2.92–2.93、图15/16/19–23 图题）。原文 p82 缺页，2.6.1-010 后半未能逐句对照（见待确认）。
- 块6 p089-098 ✅：ch02-2.6.3.2-003 ~ ch02-2.6.6-001（含 2.94–2.97、Theorem 2.13 及证明、轨形理论/Theorem 2.14 及证明、Morita 等价脚注、图24–26 图题、2.6.4 等变开闭弦缝合条件 2.98–2.104、Theorem 2.15、图27–29 图题、2.6.4-007~010 的 2.105/2.106、图30 图题、2.6.5 与 Theorem 2.16/Note 2.17/定理2.18/充实范畴讨论/Theorem 2.19、2.6.6 开头）。零改动，偏差均记入待确认。
- 块7 p099-108 ✅：ch02-2.6.6-002 ~ ch02-2.7.2-016（含世界面可观测量与边界态 $B_a$、定理2.20/2.110、Note 2.21、与 [26] 的扭曲等变 K 理论比较、§2.7 附录开头、2.7.1 经典定理的 Morse 证明（2.111、图31–35）、2.7.2 开闭弦情形（边界临界点 $0\pm/1\pm$、图36–40））。零改动，偏差均记入待确认。
- 块8 p109-118 ✅：ch02-2.7.2-017 ~ ch02-2.8-002（含两个内部临界点同层的五种构型、图41–43 图题与 2.112、图44–47 图题、2.7.3 等变闭弦理论（2.7.3-001~014：$G$-丛、Dehn 扭转、$c_{g_1,g_2}$、图32/35 情形的交换性证明、2.84 公理推导）、2.7.4 等变开闭弦理论（2.7.4-001~007：图48/49 的映射、2.111 的 $G$-作用推广）、2.8 笔记）。零改动，偏差均记入待确认。

## 改动记录
| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 1 | ch02-thm-B-001 / L42 | "the category of finite-dimensional B-twisted G-vector bundles on X" | 经逆 B 场扭曲的 $G$ 等变向量丛范畴 | 经 B 场扭曲的 $G$ 等变向量丛范畴 | 误译（多译） | 原文只说 B-twisted，无"逆"；"逆场"是后文定理 2.18 中 $b_o=b^{-1}$ 的细节，此处不得提前 |
| 2 | ch02-2.1.6-004 / L327（eq 2.18） | $\theta_{\mathcal{C}}(\psi^\mu\psi_\nu)=\delta^\mu_\nu$ | $\theta_a(\psi^\mu\psi_\nu)=\delta^\mu_\nu$ | $\theta_{\mathcal{C}}(\psi^\mu\psi_\nu)=\delta^\mu_\nu$ | 数学错 | 迹的下标应为闭弦代数 $\mathcal{C}$，非 $a$（$a$ 是边界条件对象） |
| 3 | ch02-example-2.4-002 / L401 | "by the commutative Lie algebra $\Omega^0(S)$ of smooth real-valued functions on $S$" | 由 $S$ 上光滑复值函数构成的交换 Lie 代数 $\Omega^0(S;\mathbb{C})$ | 由 $S$ 上光滑实值函数构成的交换 Lie 代数 $\Omega^0(S)$ | 数学错 | 原文为 real-valued、$\Omega^0(S)$；复化在下一句才做（复化 Vect(S) 得 $\Lambda^0$） |
| 4 | ch02-2.1.7-009 / L490 | "a canonical cochain functor ... which takes Cartesian products to tensor products" | 把 Cartesian 乘积映为张量积 | 把笛卡尔乘积映为张量积 | 未译 | Cartesian 未译，属漏译；规范中文译名"笛卡尔乘积" |
| 5 | ch02-proof-2.6 / L542 | "The images $\iota_a(\varepsilon_x)=P_x$ are central simple idempotents." | 是中心幂等元 | 是中心的单幂等元 | 漏译 | 漏译 "simple"；证明下文依赖 $P_x$ 是单（极小）幂等元 |
| 6 | ch02-2.2.3-007 / L711 | "is the category of holomorphic vector bundles on a compact Calabi-Yau manifold" | 来自……全纯向量丛的上链范畴及其对偶配对 | 是……全纯向量丛的范畴 | 多译（改变内容） | 原文是"全纯向量丛的范畴"，非"上链范畴及其对偶配对"；后者是 §2.5 才会引入的结构 |
| 7 | ch02-2.2.4-005 / L752 | "In either case, the argument ... shows ... that the algebra $\mathcal{O}_{aa}$ is the full matrix algebra of a vector space $W$." | 将开弦代数限制为相应的分次单代数 | 说明开弦代数 $\mathcal{O}_{aa}$ 是某个向量空间 $W$ 的全矩阵代数 | 误译 | 原文结论是"$\mathcal{O}_{aa}$ 是 $W$ 的全矩阵代数"；"限制为分次单代数"既非原文也不成立。原译下一句重复同一断言，故同时删去重复的"$\mathcal{O}_{aa}$ 是……全矩阵代数，且" |
| 8 | ch02-2.5.1-007 / L986 | "This is always possible if $\chi(N_Y)$, which is the self-intersection number of $Y$ in $X$, is non-zero, and also possible if $Y$ is a Lagrangian submanifold ..." | 当 $Y$ 连通，且它的 Euler 数与在 $X$ 中的自交数均非零时，这样的选择总是可能的；如果两者都为零，也可以任取非零的 $\theta_o$。 | 只要 $\chi(N_Y)$（即 $Y$ 在 $X$ 中的自交数）非零，这样的选择总是可能的。 | 误译（增改条件） | 原文条件只有 $\chi(N_Y)\ne0$（括号内说明它就是自交数），译文却拆成"连通 + Euler 数非零 + 自交数非零"并补"两者都为零"的分支，改变了命题 |
| 9 | ch02-2.3-011 / L819 | "the closed string theories defined by a Riemannian torus $T$ and its dual $T^*$" | 由 Riemann 环面 $T$ 及其对偶环面 $T^*$ | 由黎曼环面 $T$ 及其对偶环面 $T^*$ | 术语错 | 原文是 Riemannian torus（带度量的平坦环面），非 Riemann（黎曼本人）；中文标准译名"黎曼环面" |
| 10 | ch02-2.5.2-001 / L997 | "$\mathcal{O}_{YZ}$ is a symmetric algebra, and is not self-dual as a vector space." | 作为向量空间不与其完整代数对偶同构 | 作为向量空间不是自对偶的 | 误译 | 原文是"不是自对偶的"，译文"不与其完整代数对偶同构"改换了命题（任何有限维空间都同构于其代数对偶，原意是配对非完美） |
| 11 | ch02-2.5.3-001 / L1046 | "Let $X$ be a complex variety of complex dimension $d$ with a trivialization of its canonical bundle." | 设 $X$ 是复维数为 $d$ 的紧光滑 Kähler 复簇 | 设 $X$ 是复维数为 $d$ 的复簇 | 多译（加假设） | 原文只要求复簇 + 典范丛平凡化；"紧、光滑、Kähler"三项均为译者添加的强假设，改变了定理适用范围 |
| 12 | ch02-2.6.3.2-013 / L1406 | "the category of boundary conditions for the gauged theory $C$" | 等变理论 $\mathcal{C}$ 的边界条件范畴 | 规范化理论 $\mathcal{C}$ 的边界条件范畴 | 术语错 | 原文明言 gauged theory；本章 2.6.1 已明确区分"等变理论"与"规范化理论"（L1099），§2.6.2 亦用"规范化理论"，此处译名与全章不一致 |
| 13 | ch02-2.6.6-002 / L1647 | "In the gauged theory associated to a Turaev algebra $C=T(X,b,\theta)$ ..." | 在与 Turaev 代数 $\mathcal{C}=T(X,b,\theta)$ 关联的等变理论中 | 在与 Turaev 代数 $\mathcal{C}=T(X,b,\theta)$ 关联的规范化理论中 | 术语错 | 同上：gauged theory 应为"规范化理论"，与 2.6.1/2.6.2 的术语区分一致 |

## 待确认 / 未改（供 Lead 判断）
- ［非负/正］ch02-2.2.1-009 末段：原文 "a tuple of positive integers $w_x=\dim W_x$"，译作「一组非负整数」。"非负"更合数学（可空支撑），但偏离原文，暂保留。
- ［索引顺序］eq 2.41（约 L625）：译文作 $\mathcal{O}_{aa_x}$，原文 pdftotext 两处均为 $O_{a_x a}$；疑似索引互换，需核 PDF 原图。
- ［补充词］ch02-example-2.4-003 / L408：「作为 $L_1$ 与 $L_2$ 上互逆的逐纤维标量乘法」多出"互逆的"（原文仅 "fibrewise multiplications"），数学上正确，暂不改。
- ［补充词］ch02-2.1.6-004 / L325：「选取齐次基」原文仅 "a basis"，"齐次"为合理补充，暂不改。
- ［译者增补］多处解释性增补（Lemma 2.7 证明中补 $W_a=0$ 或 $W_b=0$ 的平凡情形；2.43 后补 $V=W^0$ 与 $\operatorname{End}(V)\otimes\mathbb{C}[\eta]$；循环上同调处补符号公式；2.2.4-006 补"带有相容 Frobenius 结构、有限多单对象"等）：内容正确、不矛盾，但均非原文所有，暂按 P3 保留，供 Lead 裁定。
- ［非负/正 · 系统性问题］块4 又见两处 positive→"非负"：2.54 后 "boundary states can only be added with positive integral coefficients"→「只能以非负整数系数相加」；2.56 后 "with positive integral $N$"→「$N$ 为非负整数」。与块3 同型（共 3 处），疑译者有意修正（$\dim W_x$ 可为零），暂保留，供 Lead 统一裁定。
- ［增补推导］eq 2.54 后译者补「$\mathcal{L}_B$ 对乘法封闭 ⟺ $1/\sqrt{\theta_x}\in\mathbb{Z}$；若含单位元则须 $\theta_x=1$」，原文只有 "is not closed under multiplication ... unless $\theta_x=1$"；推导数学上正确但超出原文，暂保留。
- ［公式增改］eq 2.58 译文 $\theta(\phi)\coloneqq-\operatorname{Res}_{X=\infty}\frac{\phi(X)\,\mathrm{d}X}{W'(X)}$，原文 "$\theta(\phi):=\mathrm{Res}_{X=\infty}\phi(X)/W'(X)$"（无负号、无 dX）；与例 2.10 的 $\theta_i=\pm1/(2\sqrt q)$ 自洽，疑译者按无穷远留数符号约定修正，暂保留。另 2.67 后 $\chi(TX)=\sum_i(-1)^{\deg\omega_i}\omega_i\omega^i$ 多出符号（原文 $\sum_i\omega_i\omega^i$）。
- ［引用核对 · 保留译文］p69 原文 "in §2.7"，译文作 2.6（等变节实为 §2.6，已核对章节结构）；p76 原文 "We have mentioned in §2.1"，译文作 2.2.3（$\operatorname{HH}^0$ 的定义确在 2.2.3）。两处疑为原书笔误，译文改后与正文一致，保留。
- ［小增补］「具有孤立临界点的多项式」L855、「当 $n=2$ 且 $q\ne0$ 时」L898、2.65 后「$w_1,w_2$ 为整数；实际向量丛的秩则为非负整数」、「按路径的方向」L997、「在内部次数都为零时……Koszul 符号」L1013 附近：解释性增补，内容不矛盾，暂按 P3 保留。
- ［增译 · 块5 · 待裁定］p78 2.5.3-006：原文 "$\widehat{C}=\{A\to A\otimes A\to A\otimes A\otimes A\to\cdots\}$"，译文作「对于一个局部代数模型，Hochschild 上链的形状是 $\{A\to\operatorname{Hom}_{\mathbb{C}}(A,A)\to\operatorname{Hom}_{\mathbb{C}}(A\otimes A,A)\to\cdots\}$」，并补「局部多重微分上链的层及其导出整体截面……」两句。Hom 形式是 Hochschild 上链的标准写法，疑译者有意修正原书排版，但属公式改动，未擅改，提请复核。
- ［增译 · 块5］另有多处：p78 §2.6 开头补「并且相应对称性可以规范化时」；p84 定理 2.11 补「各分量有限维的」「结合含幺」「满足分次相容性 2.81」；p85 在「两个 B 场定义同构的 Turaev 代数」前补「要求同构在给定的 $\mathcal{C}_1$ 上为恒等映射时」；p86 补「范畴的神经这个有向单纯集的几何实现」「这里 $X$ 是有限集合」；p87 补「（取值于 $\mathbb{C}^{\times}$ 而不是 $\mathbb{C}$，是为了保证乘积非退化）」「将起点坐标表示的 $b$ 转换为……坐标表达」。均属解释性增补，暂留。
- ［未核对 · 材料缺页］块5 中原文 PDF 第 82 页缺失（图页），故 2.6.1-010 后半（有孔环面上的丛、$L_\psi/R_\psi$ 与 eq 2.83 的导出过程）无法逐句对照；译文内部记号自洽（已验 $c\cdot d=h$、$h g^{-1}h^{-1}\cdot c=g^{-1}$）。
- ［图题核对］块5 已核图15、图16、图19、图20、图21、图22、图23 图题，除图15「因此，乘积通常不交换」多出「通常」（原文 "the product is not commutative"）外均忠实。
- ［公式修正 · 保留］块6 eq 2.95 的 $b_{g_1x}$：原文三处均作 $b_x$，译文第 2、3 因子改用 $b_{g_1x}$。按 2.90/2.94 约定验算得 $z_x(g_2,g_1)=b_x(g_1,g_2)b_{g_1x}(g_1g_2,g_1^{-1})/b_{g_1x}(g_1,g_1^{-1})$，且 $g_1x=x$ 时化为 2.96 的 $b_x(g,h)/b_x(h,g)$，故为有意修正，保留。
- ［公式修正 · 保留］块6 2.6.3.2-004 环面公理两端值补 $1/\theta(\varepsilon_x)$ 因子（原文无）：与下文 $\Delta_1=\sum_x\theta(\varepsilon_x)^{-1}\varepsilon_x\otimes\varepsilon_x$ 及 2.96 自洽，属修正，保留。
- ［术语 · 保留］块6 2.6.4-005：原文称 $\iota$ 为 "ring homomorphism"，而 2.102 实为反序乘法；译文作「环反同态，也就是 $\mathcal{C}^{\mathrm{op}}\to\mathcal{O}$ 的环同态」，与公式一致，保留。
- ［系统性约定 · 保留］块6 起开弦扭曲一律 $b_o=b^{-1}$（2.6.5-001/002、定理2.16「$b_o$ 是 $b$ 在 $H$ 上限制的逆」、Note 2.17「逆上闭链 $b_{x_0}^{-1}$」、定理2.18「经 $b_o=b^{-1}$ 扭曲」）；原文 2.16 仅作 "b_o ... which is the restriction of b"。译文按 2.6.4 的反同态约定统一，保留。
- ［增补推导 · 暂留］块6 2.6.5-006：译者补出「$\iota$ 为反同态、$\mathcal{C}_x^{\mathrm{op}}$ 作用在 $E_x$ 上；令 $R_g=\iota_g(\ell_{g,x})^{-1}$，则 $R_gR_h=b_x(g,h)^{-1}R_{gh}$、$\rho_g=\operatorname{Ad}(R_g)$，故 $V$ 的射影二上闭链为 $b_{x_0}^{-1}$」；原文仅一句 "the algebra homomorphism $C\to O$ makes $C_x$ act on $E_x$, and so $V$ is a projective representation ... with the cocycle $b_{x_0}$"。增补自洽，暂留。
- ［公式改动 · 提请复核］块6 定理 2.19 的 2.109：原文 $\phi_a\circ f=(g\cdot f)\circ\phi_b$，译文作 $(g^{-1}\cdot f)\circ\phi_b$，并补「各分量的乘法以这些族的反向分量复合给出，从而 $\mathcal{C}_g\mathcal{C}_h\subset\mathcal{C}_{gh}$」；疑按反同态约定统一，未擅改。
- ［读法冲突 · 需统一］块6「底层普通范畴」：p98 原文 "The underlying ordinary category is the category of boundary conditions for the orbifold theory"，译文作「取 $G$ 不变态射得到的底层普通范畴」；同页另有「仅仅遗忘 $G$ 作用……另一个普通范畴」。两处对「底层」取法不同（取不变量 vs 遗忘作用）。
- ［小增补］块6 2.6.5-001 把原文 "when $C$ is semisimple" 改为「当 $\mathcal{C}_1$ 半单时」；2.6.3.2-007 补「沿另一个方向」；定理2.18 补「极大」「$G$ 不变平方根」等澄清性增补。
- ［增译］块7 2.6.6-002 增「带扭曲扇区标记的」「任取绕边界的平行移动」；$B_a=\sum_g\iota^{g,a}(1)$（原文 pdftotext 作 $\iota_{g,a}$，上下标丢失；按 2.104 伴随关系验算与 $\theta_{\mathcal{C}}(\phi B_a)=\theta_{\mathcal{O}}(\iota_g(\phi))$ 一致，译文正确，不改）。
- ［增译］块7 2.6.6-003 增「也就是定理2.14所确定的交叉积代数的中心」，并补 $h\in H_G^3(X,\mathbb{Z})$ 为「开弦扭曲 $b_o=b^{-1}$ 所对应的类」；2.6.6-005 增「在按边界取向作对应之后」「不可约特征标」。
- ［大段增译 · 待裁定］块7 2.6.6-007：译文加「在同一上同调类中选取圆周值的二上闭链代表，并为 $E$ 选取相容的 Hermitian 度量」「先假设 $E_x$ 对每个稳定子群都包含该扭曲下的所有不可约射影表示」「稳定射影 Hilbert 空间丛／稳定 Hilbert 丛」；且 2.6.6-008 整段（一般 $E$ 加辅助丛 $F$、$\widehat{E}=(E\oplus F)\otimes\mathcal{H}$、$\operatorname{id}_E\otimes T$ 与恒等算符、核 $\cong E$ 而余核为零、保证射影丛稳定）在原文 p100 中不存在——疑译者据 [26] 补写。
- ［公式增改］块7 2.7.1-005：译文 $f_s(u,v)=c\pm u^2+v^3$，原文 $\pm u^2+v^3$（译文加常数 $c$，相当于把临界值归一化）。
- ［结构调整 · 暂留］块7 2.7.2-001：译文加开头句「给定 2.1.2 中的开闭弦代数数据……」并新增两个 definition* 环境（边界非退化临界点、Morse 函数），原文为正文叙述。
- ［小增补］块7 2.7.2-003「朝内法向导数」（原文 the sign of the normal derivative）、「指标分别为0与1」（原文 opposite index）；2.7.1-002「微分 $\mathrm{d}f$」（原文 gradient $df$）。
- ［公式存疑 · 未改］块7 2.7.2-005：译文 $\phi\psi=\iota_a(\psi)\phi=\phi\iota_b(\psi)$；原文 pdftotext 作 "$\phi\psi=\iota_a(\phi)\psi=\iota_b(\phi)\psi$"（类型不通，疑排版/抽取错位），待核 PDF 原图。
- ［记号 · 保留］块7 2.7.2-012 用 $\iota^a,\iota^b$（原文 $\iota_a/\iota_b$ 上下标不明），与「$\iota^a\colon\mathcal{O}_{aa}\to\mathcal{C}$ 是 $\mathcal{C}$ 模映射」一致，保留。
- ［术语 · 已改两处］"gauged theory" 在 2.6.3.2-013（L1406）、2.6.6-002（L1647）曾误译为「等变理论」，已按 2.6.1 的术语区分改为「规范化理论」（改动 12、13）；2.6.6-001「等变边界条件范畴」对应 "for a $G$-gauged theory" 且含增补，暂留待裁。
- ［增译 · 块8］2.7.4-003：译文补「$g_1,g_2$ 表示相应分裂配边中，两条出弦所选平凡化相对于局部参考平凡化的转换元素」——原文此处只说 $\xi_i,\xi^i$ 是对偶基，属解释性增补。
- ［增译 · 块8］2.7.3-004 补「为左图的情形(i)」；2.7.3-005 补「的时间反转」（图15 配边）；2.7.4-002 开头补「取 2.6.4 中的等变开闭弦代数数据。」；2.7.2-016 补「其中 $\psi_m\in\mathcal{O}_{ca}$」。均属解释性增补。
- ［修正 · 保留 · 块8］2.7.4-004：原文 "The corresponding map is $\iota^g$, with adjoint $\iota_g$"（pdftotext 上下标丢失），译文作「相应映射是 $\iota^g$；……其伴随映射为 $\iota_{g^{-1}}$」，与 2.104 的配对一致，属修正，保留。
- ［上下标 · 保留 · 块8］2.7.3-005 及 2.7.3-008/009/012/013 中 $\phi_i/\phi^i$、$\psi_i/\psi^i$：原文 pdftotext 均作同层下标，译文按类型（如 $\phi\phi^i\in\mathcal{C}_{g_1}$）改为上标，均自洽，保留。
- ［原文笔误 · 保留译文 · 块8］2.7.4-006：原文 "when $\phi'\in\mathcal{O}_{ab}$ and $\phi_i$ and $\phi^i$ are dual bases for $\mathcal{O}_{ab}$ and $\mathcal{O}_{ba}$"，译文作「当 $\phi'\in\mathcal{O}_{bb}$，且 $\phi^i,\phi_i$ 分别是 $\mathcal{O}_{ab},\mathcal{O}_{ba}$ 的对偶基」；按类型验算只有 $\phi'\in\mathcal{O}_{bb}$ 自洽，疑原文笔误，保留译文。
- ［推导核验 · 块8］eq 2.112：原文 pdftotext 各迹下标均作 $\theta_b$；译文按类型分别用 $\theta_a$（$O_{aa}$）与 $\theta_c$（$O_{cc}$），验算自洽，保留。
