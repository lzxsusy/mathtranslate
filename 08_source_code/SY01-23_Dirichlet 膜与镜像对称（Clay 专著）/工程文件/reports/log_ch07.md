# 第7章 校订日志（rv-preface-ch01 接手 task-9）

负责文件：`chapters/ch07.tex`（现 2117 行）
负责页码：PDF 519–583（书 p509–573），分 7 块
材料：`review/chunks/ch07/p519-528.txt`、`p529-538.txt`、`p539-548.txt`、`p549-558.txt`、`p559-568.txt`、`p569-578.txt`、`p579-583.txt`

## 已核对范围
- p519-528（书 p509-518；ch07-intro-001 … ch07-7.1.4-002）✅ 2026-11-14
- p529-538（书 p519-528；ch07-7.1.4-003 … ch07-7.2.2-001）✅ 2026-11-14
- p539-548（书 p529-538；ch07-7.2.2-002 … ch07-7.2.4-015）✅ 2026-11-14
- p549-558（书 p539-548；ch07-7.2.4-016 … ch07-7.2.5-036）✅ 2026-11-14（本块无改动）
- p559-568（书 p549-558；ch07-7.2.5-037 … ch07-7.3.2-017）✅ 2026-11-14
- p569-578（书 p559-568；ch07-7.3.3-001 … ch07-7.3.6-002）✅ 2026-11-14（本块无改动）
- p579-583（书 p569-573；ch07-7.3.6-003 … ch07-7.3.7-011，含 7.3.6 定义 7.30 后半、定理 7.31、猜想 7.32、7.3.7 SYZ 未来、猜想 7.33、问题 7.34）✅ 2026-11-14（本块无改动）

## 改动记录

| # | 段落 id / 位置 | 原文（英文，摘关键句） | 原译 | 改为 | 类别 | 理由 |
|---|---|---|---|---|---|---|
| 1 | ch07-7.1.1-006 / ch07.tex L75（书 p512） | "with Kähler class of the form **−2a[E]**. The 2-sphere E has **curvature a⁻¹** and **volume 4πa**."（已渲染原书扫描页 p512 图像核实，非 pdftotext 误读） | 其 Kähler 类为 $-\pi a[E]$。二维球面 $E$ 的曲率为 $2/a$，面积为 $2\pi a$。 | 其 Kähler 类为 $-2a[E]$。二维球面 $E$ 的曲率为 $a^{-1}$，面积为 $4\pi a$。 | 数学错误（P1） | 三处数值全部与原文不符：原文 −2a[E] / a⁻¹ / 4πa，且这三个数互洽（$[\omega/2\pi]=\frac{4\pi a}{2\pi}[E]=2a[E]$；Gauss–Bonnet $a^{-1}\cdot4\pi a=4\pi$）。原译改成 −πa[E] / 2/a / 2πa 后与 Kähler 类不自洽，属译文自行改动数值。 |
| 2 | ch07-7.1.1-011 / ch07.tex L106（书 p513） | "the Kähler potential of the Eguchi-Hanson metric with parameter a, **scaled by a factor a/2**, where a > 0 is given by κ = a⁻²"（已看图核实） | …就是参数为 $a$ 的 Eguchi--Hanson 势**乘以 $a$**，其中，$a>0$ 由 $\kappa=a^{-2}$ 给出。 | …就是参数为 $a$ 的 Eguchi--Hanson 势**乘以 $a/2$**，其中，$a>0$ 由 $\kappa=a^{-2}$ 给出。 | 数学错误（P1） | 原文缩放因子是 $a/2$，译文漏掉 1/2。且只有取 $a/2$ 才能与同句"限制到 $\mathbb P^1$ 上的曲率为 $2a^{-2}=2\kappa$"相符（$a^{-1}\div(a/2)=2a^{-2}$）。 |

| 3 | ch07-7.1.5-004 / ch07.tex L327（书 p521） | "take the bilinear form on the tangent space **b(u,v) = −(1/6) ι(u)ρ∧ι(v)ρ∧ρ**"（已渲染原书 p521 图像核实，负号确在；同页 $g=b_\rho(\det K_\rho)^{-1/9}$、$\widehat\rho=*\rho$、$n=8$ 时 $\widehat\rho=-*\rho$ 均与原文一致） | $b_\rho(u,v)=\frac16\iota(u)\rho\wedge\iota(v)\rho\wedge\rho$ | $b_\rho(u,v)=-\frac16\iota(u)\rho\wedge\iota(v)\rho\wedge\rho$ | 数学错误（P1） | 原式带负号，译文漏掉；度量的正定性依赖此符号约定（$g=b_\rho(\det K_\rho)^{-1/9}$）。 |

| 4 | ch07-7.2.3-010 / ch07.tex L639（书 p542） | "one can describe the fibers of $f\colon Y_\Sigma\to\mathbb R^n$ **in case the moment map µ is proper**. This will be the case, say, if the metric is ALE." | "若所用环面度量的完整环面 $T^n$ 的矩映射为适当映射，就可以描述 … 例如，在上述标准 ALE 例子中，这一适当性成立。" | "若矩映射 $\mu$ 为适当映射，就可以描述 $f\colon Y_\Sigma\to\mathbb R^n$ 的纤维；例如，当度量为 ALE 时，情形就是如此。" | 误译（P1） | 原文说的是 $\mu\colon Y_\Sigma\to\mathbb R^{n-1}$（$T^{n-1}$ 作用的矩映射）为 proper，译文换成"完整环面 $T^n$ 的矩映射"，多了原文没有的对象且指错了映射；"适当映射"沿用全书对 proper 的译法不另改。 |

| 5 | ch07-7.3.1-003 / ch07.tex L1453（书 p563） | "In this metric, the 2-sphere E has **curvature a⁻¹** and **volume 4πa**"; 同上文 "with Kähler class of the form **−2a[E]**" | 按照那里所用的归一化，Kähler 类为 $-\pi a[E]$。此度量中，二球面 $E$ 的曲率为 $2/a$，体积为 $2\pi a$。 | 按照那里所用的归一化，Kähler 类为 $-2a[E]$。此度量中，二球面 $E$ 的曲率为 $a^{-1}$，体积为 $4\pi a$。 | 数学错误（P1） | 与改动 #1 同一组数值：原译的 −πa[E] / 2/a / 2πa 与例 7.1 已改正的 −2a[E] / a⁻¹ / 4πa 不一致（此处原译还特意加了"按照那里所用的归一化"），不改会与本段上文自相矛盾。 |
| 6 | ch07-7.3.1-004 / ch07.tex L1456（书 p563） | "the Eguchi-Hanson metric **(parameter ai)** inside the annulus" | 对第 $i$ 个节点，使用例题 7.1 中参数为 $a_i/\pi$ 的**度量**。 | 对第 $i$ 个节点，使用例题 7.1 中参数为 $a_i$ 的度量。 | 数学错误（P1） | 原文参数就是 $a_i$；原译 $a_i/\pi$ 是为配合旧的（错误的）Kähler 类 $-\pi a[E]$ 而作的换算，改动 #5 恢复原书归一化后必须一并改回。 |
| 7 | ch07-7.3.1-005 / ch07.tex L1463（书 p564） | "i.e., if Ω denotes the holomorphic 2-form, then **(i/2)² Ω ∧ Ω̄** is a constant multiple of the volume form ω̃a²/2." | 则 $\tfrac14\Omega\wedge\overline\Omega$ 为体积形式 $\widetilde\omega_a^2/2$ 的一个**正**常数倍。 | 则 $(\tfrac{\mathrm i}2)^2\Omega\wedge\overline\Omega$ 为体积形式 $\widetilde\omega_a^2/2$ 的一个常数倍。 | 数学错误（P1） | 原式是 $(\mathrm i/2)^2=-1/4$，译文把 $(\mathrm i/2)^2$ 写成了 $1/4$ 并称"正常数倍"，符号正好相反（$(\mathrm i/2)^2\Omega\wedge\overline\Omega=\widetilde\omega_a^2/2$ 才是正的体积形式）。 |

## 待确认 / 未改（供 Lead 判断）

- ch07-intro-003：原文 "this is equivalent to f being constant"，译文"这等价于 $f$ 在每个连通分支上为常数"。补了"每个连通分支"（$X$ 紧但未必连通时更准确），未改。
- ch07-intro-004：原文 "If X is compact, Ricci-flat metrics are known to exist by results of Yau [475]"，译文"在上述紧 Kähler、第一 Chern 类为零的情形中…"。译者据上文补了前提条件，语义不歪，未改。
- ch07-7.1.1-004：原文 "because of the absence of continuous families of isometries"，译文"由于所关心的通常例子缺乏连续的等距对称"。多出"所关心的通常例子"，families 译作"对称"，可通，未改。
- ch07-7.1.2-002：译文多出"这里省略从 $U$ 到 $X$ 的拉回记号。"——原文确实省略了 $\pi^*$，属正确的技术说明（可保留的译注），未删。
- ch07-7.1.2-003：原文 "It follows that the (integrable) almost complex structure **J** on the cotangent space is given by $J(\mathrm du_1)=-\mathrm du_2$"，译文作 $J^*(\mathrm du_1)=-\mathrm du_2$（作用在余切空间上写 $J^*$ 更准确），未改。
- ch07-7.1.3-002：译文多出两处说明："这里 $u=u_3$，而 $\mathrm dx$ 与 $\theta_0-\mathrm i V\,\mathrm du$ 在模去 $\mathrm dy$ 后相等"、"若每条纤维上的坐标 $x$ 取遍 $\mathbb C$，则识别为整个 $T^*B$"。数学正确（并与后文 7.1.3-003 的 $(T^*B)/\mathbb Z$ 相衔接），未删。
- ch07-7.1.3-005：原文 pdftotext 里 $Y$、$X$ 的上划线丢失（"Y = D × S¹"、"on the relative compactification X → Y"），译文用 $\overline Y$、$\overline X\to\overline Y$，与原书版式一致，未改。
- ch07-7.1.1-006/011、7.1.2-005/006 等处译者把原文的普通段落包成 `example` / `note` / `theorem*` + `proof` 环境（版式处理，GUIDE P3 不动）。
- ch07-7.1.5-002（书 p521）：原文 "for n = 8 we want stabilizer **SU(3)**"，译文"要求稳定子单位分支为 $\operatorname{PSU}(3)=\operatorname{SU}(3)/\mathbb Z_3$"，并在 $n=6$ 处同样加了"单位分支"。若八维 3-形式取 $\mathfrak{su}(3)$ 伴随表示，中心 $\mathbb Z_3$ 作用平凡，稳定子确为 $\operatorname{SU}(3)/\mathbb Z_3$，译文比原文更精确（与 ch01 中 $\mathrm O(d,d;\mathbb Z)$ vs $\mathrm{SO}$ 同类情形）。未改，待 Lead 定。
- ch07-7.1.5-003（书 p521）：译文引入原文没有的记号 $\eta_\rho$、约定 $D\phi_\rho(\dot\rho)=\dot\rho\wedge\eta_\rho$、以及 $\eta_\rho=\tfrac13*\rho$。均与齐次性 $\rho\wedge\eta_\rho=\frac np\phi(\rho)$ 自洽，属可保留译注。
- ch07-7.1.5-008（书 p522）：译文多出"此结构可积且 $\Omega$ 全纯""当概复结构与二形式 $\omega$ 相容时"等说明；并把 "defines a $G_2$-holonomy metric" 译作"定义完整群**包含于** $G_2$ 的度量"（闭合+余闭合严格给出的是 $\mathrm{Hol}\subseteq G_2$），未改。
- ch07-7.1.5-010（书 p533）：原文 "In the case when the classes A and B are trivial we have that the fibers are nearly Kähler."，译文改写为"…前述受约束泛函的正型临界点给出近 Kähler 纤维，并可以作为这一流的初始数据"，多出"初始数据"一层意思（与 Hamilton 流上下文相容），未改。
- ch07-7.1.5-008 的 3-形式 $\frac{r^2}{\lambda}\mathrm dr\wedge\omega+r^3\rho$ 与 $\mathrm d\widehat\rho=-4\lambda\sigma,\ \mathrm d\omega=3\lambda\rho$：已渲染原书 p522 图像核实，**与译文完全一致**，无改动。
- 7.2.1 节 "current / rectifiable current" 译法在同一节内混用"流/可求长流"与"整流"（如"取一列代表该类的整流"、"体积最小的可求长整流"）。属术语不统一（P2），未改，供 Lead 判断是否统一为"流/可求长流"。
- ch07-7.2.1-014：原文 "off a set of (Hausdorff) codimension two"，译文"Hausdorff 余维**至少**为二的集合"。Almgren 正则性定理的正确表述确为余维 ≥ 2，译文更准确，未改。
- ch07-7.2.1-005：原文 "ι*Ω is of type (0,n) and thus ι*Ω = ±Ω"，译文作"调整 Ω 的常数相位后，可以取 $\iota^*\Omega=\pm\overline\Omega$"，并补出"选择满足 $-\iota^*[\omega]=[\omega]$ 的 Kähler 类"的论证。译文修正了原文的记号疏漏（(0,n) 型应为 $\overline\Omega$），未改。
- ch07-7.2.2-004（书 p539）：原文 "The moment map is µ(z1,z2,z3) = (|z1|²−|z2|², |z1|²−|z3|²), assuming ω is the standard symplectic form."；译文先明确 $\omega=\tfrac{\mathrm i}2\sum\mathrm dz_j\wedge\mathrm d\bar z_j$，再给 $\mu=-\frac12\bigl(|z_1|^2-|z_2|^2,\ |z_1|^2-|z_3|^2\bigr)$。按 $\iota(\rho(\xi))\omega=\mathrm d\langle\mu,\xi\rangle$ 复算，此 $\omega$ 下确需带 $-\frac12$，译文自洽且比原文更明确，未改。
- ch07-7.2.3-005（书 p540）：原文 "if e*1,…,e*n ∈ σ∨, then z1,…,zn extend … **This can always be arranged.**"；译文改为"若**某个** $e_i^*\in\sigma^\vee$，则 $z_i$ 延伸为 $Y_\sigma$…"并补"一般并不能使所有 $e_i^*$ 同时位于 $\sigma^\vee$ 中，但乘积 $z_1\cdots z_n$ 总是正则的"。以 Example 7.8(1) 验算：$e_1^*=(1,0,0)$ 对 $(-1,-1,1)$ 取值为 $-1<0$，确不能同时落在 $\sigma^\vee$，译文修正了原文的疏漏。未改，请 Lead 定是否保留这种"更正原文"的处理。
- ch07-7.2.4-002（书 p544）：译文补出"将 Lie 代数生成元重标为标准生成元的 $-2$ 倍"以解释矩映射与 $2a$ 的归一化（原文仅 "(The factor of 2 is a convenient normalization.)"）；与后文 $X=2\mathrm i(\bar z_1\partial_{\bar z_1}-z_1\partial_{z_1}-\cdots)$、$\iota(X)\Omega=-2\mathrm i\,\mathrm d(z_1z_2)\wedge\mathrm dz_3$、$\mu^{-1}(2a)$ 全部自洽，未改。
- ch07-7.2.4-012（书 p548）：原文仅写 "v is determined by u"；译文补出符号选取（$y\neq0$ 时取 $u$ 与 $y$ 反号、$v=-xy/u$；$y=0$ 时 $u=0$、$v=x\sqrt{x^2+2a}$）。代入 (7.4) 核验正确，属可保留补偿，未改。
- ch07-7.2.3-003 "crepant partial resolution" 译"保典部分消解"：译法少见但可理解（$K_{Y_\Sigma}=0$），未改。
- 第 4 块（p549-558 / 书 p539-548）**无改动**。已逐段核过并确认一致：$F(z_1,z_2,z_3)=(a,b)$ 的三情形分段、$F^{-1}(a,c)=M_{a,c}$ 的证明、判别的 $\{0\}\times\mathbb C$、定理 7.12（$C^{k+3,\alpha}$/弱解二分）、定义 7.13 的重数与缠绕数 $\frac1{2\pi\mathrm i}\int_\gamma\mathrm dz/z$、定理 7.15/7.16（$\sum k_i\le l-1$）、锥与链环定义、$s$-ind 公式 $-b_0(\Sigma)-m^2-2m+1+\dim G+\sum_{\alpha\in D_\Sigma\cap[0,2]}m_\Sigma(\alpha)$ 及其 $0,6,20,50,\ldots$（已按 $b_0=1,\dim G=m-1$ 逐项复算全部吻合）、环面锥的 $g_{ij}=\frac1m(\delta_{ij}+1)$ 与特征值 $m\sum n_i^2-\sum n_in_j$、锥形奇点定义（$|\varphi-\varphi'|=O(r^{\mu-1})$ 等）、$L^p_{k,\alpha}$ 与余核维数 $\sum_i\sum_{\alpha}m_{\Sigma_i}(\alpha)$、渐近锥形定义与例题 7.17、定理 7.18、$Y(M)\in H^1(\Sigma,\mathbb R)$ 与 $\int_{\varphi_i(D)}\omega=\pi a_i$、定理 7.21。
- 7.2.4-026（定义 7.13）：原文 "A zero (b,c) … is called singular if a = c = 0 and v1(b,0) = v2(b,0)."（按字面是恒真的，因为 $(b,c)$ 已是零点）；译文补成 "$v_1(b,0)=v_2(b,0)=0$"，语义才成立，属必要补正，未改。
- 7.2.4-034（书 p551）：原文只笼统说 "let $f_\beta\in C^{3,\alpha}(S)$ be the solution to the Dirichlet problem"；译文按定理 7.12 分情形补出"$a\neq0$ 时 $f_\beta\in C^{3,\alpha}(\overline S)$；$a=0$ 时取 $C^1$ 弱解"，并补"不同 $a$ 时位于不同矩映射水平集"，与上下文相容，未改。
- 7.2.5-013（书 p554）：原文仅说 "with cones $C'_1,\ldots,C'_n$"；译文补"对应的锥分别与原锥 $\operatorname{SU}(m)$ 等价，且保持相应收敛率"（与锥形奇点定义相容），未改。
- 7.2.5-010（书 p554）：原文嵌入为 $\varphi'\colon\Sigma\times(0,R')\to B_{R'}$，译文写作 $\to B_R$（后文复合 $D\circ\varphi'$ 映到 $D(B_R)$，$R'\le R$ 时等价），属可忽略的记号简化，未改。
- 7.2.5-002 / 7.2.5-009（书 p552-553）：译文分别补"以下讨论原点为唯一奇点、链环光滑的锥"与"当时唯一已知的非平凡稳定奇异锥例子"（原文 "This is the only known example of a stable cone"），均为限量性说明，未改。
- 7.2.6-004（书 p550）：原文 "The line segment r1 + r2 = 1 **with r1, r2 ≥ 0**"，译文作"$r_1+r_2=1$、**$r_1,r_2>0$**"，端点归属略有差别（不影响图景），未改。
- 7.3.1-010（书 p564）：原文 "Limits of Ricci-flat metrics **with bounded volume and diameter** on a K3 surface"，译文作"体积**不塌缩**、直径有界的 Ricci 平坦度量的极限"。"体积有界"与"不塌缩"含义不同（非塌缩在原文中是由有界性推出的结论），属轻微不精确，未改（P2）。
- 7.3.2-002（书 p565）：译文末尾补出"并选择 $E$ 的符号，使 $E\cdot\operatorname{Re}\Omega>0$"（原文此处无此句，但为下文 $\check B,\check\omega$ 的归一化所必需），属可保留补正，未改。
- 7.3.2-003（书 p565）：原文周期域写作 $\mathrm O(3,19)/\bigl(\mathrm O(2)\times\mathrm O(1,19)\bigr)$，译文作 $\mathrm O(3,19)/\bigl(\operatorname{SO}(2)\times\mathrm O(1,19)\bigr)$。复维数同为 20，但该齐性空间的稳定子应为 $\mathrm O(2)$（含二维平面内的反射），译文 $\operatorname{SO}(2)$ 是记号偏差。未改，请 Lead 定是否改回。
- 7.3.2-006（书 p566）：原文只写 "$\Omega_K\cdot E=0$ implies that $E$ is the class of an effective divisor with $E^2=0$"；译文补"结合 $E\cdot\omega_K>0$"。该补充使断言成立（$\Omega_K\cdot E=0$ 单独只给出 $E$ 为特殊 Lagrange 类），属必要补正，未改。
- 7.3.2-010（书 p567）：原文 "The filtration in fact coincides with the weight filtration…"，译文加"**适当重新编号后**，这一滤过……一致"，是为调和 $F_0/F_1$ 编号与权滤过编号的差异，未改。
- 第 6 块（p569-578 / 书 p559-568）**无改动**。核过且一致：7.3.3 的半平坦度量构造（$F_\alpha$ 作用、$\pi\colon T^*_{\mathbb{CP}^1}\to X$、$X^0=T^*_{B_0}/\Lambda$、$\omega$ 的 $W,b$ 表示、(K1)(K2)、$\omega_{\mathrm{SF}}$ 的 $W=\epsilon/\operatorname{Im}(\bar\tau_1\tau_2)$ 与 $b=-\frac W\epsilon[\cdots]$、三条刻画性质、Kähler 势 $\varphi$、$\|R\|=O(\epsilon)$）；7.3.4 的 Ooguri--Vafa 度量（$\overline Y,Y$、$\bar\pi$ 与构造 6.86 的紧化、$V_0$ 级数、$a_n=1/(n\epsilon)$、$a_0=2(-\gamma+\log2\epsilon)/\epsilon$、引理 7.26 的 Bessel 展开与指数界、命题 7.27 的周期 $\frac1{2\pi\mathrm i}\log y+\mathrm i h(y)+C$、命题 7.28 的 $C'\epsilon^{-1}(\log\epsilon^{-1})^{-2}<\|R\|_{C^0}<C\epsilon^{-1}\log\epsilon^{-1}$）；7.3.5 的粘合构造（引理 7.29、$\mathrm dg=\tau_1\mathrm dy$、截断函数 $\psi$、$([\omega_{\rm new}]+aE)^2=[\omega_{\rm new}]^2+2a\epsilon$、$u_\epsilon$ 的 $C^0/C^2/C^{k,\alpha}$ 估计）。
- 7.3.4-004（书 p573）：原书此处写 "We are led therefore to take $V=V_0+f(y_1,y_2)$"（漏了 $/\epsilon$），与同页引理 7.26 及下一段的 $V_0+f(y)/\epsilon$ 不一致；译文统一作 $V=V_0+f/\epsilon$，与原书意图及后文自洽，未改。
- 7.3.4-008（书 p574）：原书 "$\int_\gamma\mathrm dx_1=\int_\gamma(\theta_0+a\,\mathrm du)=a\epsilon+\int_\gamma\theta_0$"；译文作 "$\int_\gamma(\theta_0+a\,\mathrm du)=-a\epsilon+\int_\gamma\theta_0$" 并自行补"即 $\int_\gamma\mathrm du=-\epsilon$"。二者差一个定向约定（$a$ 可在 $\mathbb R$ 中任取），最终"适当选择 $a$ 使 $C=0$"的结论不受影响，故未改；如 Lead 认为应与原文一致，可把符号改回 $+a\epsilon$ 并删去"即 $\int_\gamma\mathrm du=-\epsilon$"。
- 7.3.5-007（书 p567）：已渲染原书 p567 图像核实，原文确为 $F_\epsilon=\log\frac{\Omega\wedge\overline\Omega/2}{\omega_\epsilon^2}$，与译文完全一致（此前疑有漏 $/2$，已排除）。
- 7.3.5-009（I）（书 p567）：原文 "ensures that the Sobolev constant is bounded below by $O(\epsilon^5)$"，译文写成"有 $c\epsilon^5$ 的下界"（把 $O$ 换成显式常数，语义更明确），未改。
- 7.3.6-002（书 p568）定义 7.30：译文改用"遍历共同度量空间 $Z$ 与等距嵌入、取 Hausdorff 距离下确界"的标准定义，而原书用的是 $f\colon X\to Y$、$g\colon Y\to X$ 的 $\epsilon$-逼近定义（原文续在下一页）。定义等价，但改写幅度较大，待第 7 块核对定义其余部分后一并判断（第 7 块已核完，结论见本段末条）。
- 7.3.6-003（书 p569）：原书只说 "Then we say that the Gromov-Hausdorff distance between $X$ and $Y$ is at most ǫ. The Gromov-Hausdorff distance $d_{GH}(X,Y)$ is the infimum of all such ǫ."；译文合并两种定义后写成"则 $d_{\mathrm{GH}}(X,Y)\le\epsilon$。所有这类 $\epsilon$ 的下确界记为 $\delta(X,Y)$，有 $d_{\mathrm{GH}}(X,Y)\le\delta(X,Y)\le2d_{\mathrm{GH}}(X,Y)$"，即引入原文没有的 $\delta$ 与双边不等式。该不等式是标准事实（$\epsilon$-等距映射给出的距离与 $d_{GH}$ 相差不超过 2 倍），译文的处理使前后两种定义自洽；但确实多出原文内容。因删改会牵动整个定义块（7.3.6-002/003），未改，**请 Lead 定是否恢复成原文的"下确界"表述**。
- 7.3.6-006（定理 7.31，书 p569）：原文 "$B$ 上的度量由判别集补集上的标准 Riemann 度量**诱导**"；译文作"$B$ 的度量为判别集补集上的标准 Riemann 度量的**度量完备化**"。多出"度量完备化"（与 $B$ 是 $B_0$ 的紧化相符），属可保留的明确化，未改。
- 7.3.6-004（书 p569）：译文在"紧 Ricci 平坦流形族预紧"前补"固定维数"（原文由上下文隐含），未改。
- 7.3.7-008（书 p582-583）：译文末尾补出"虽然构造中保持椭圆纤维化的复结构固定，但旋转回 SYZ 所用的复结构时，这一扰动也改变了相应复结构"（原文无此句，但与 Ooguri--Vafa 构造相容）；同段把 "semi-flat metric" 译作"半平坦**超 Kähler** 结构"，多出"超 Kähler"，未改。
- 第 7 块（p579-583 / 书 p569-573）**无改动**。核过且一致：定义 7.30 的 $\epsilon$-逼近条件、Gromov 预紧性（[391] 第 281 页推论 1.11）、长度空间、塌缩定义；定理 7.31 的成立条件（$\int_{X_i}\omega_i^2$ 与 $i$ 无关、纤维面积 $\epsilon_i\to0$）与 "$(X_i,\epsilon_i\omega_i)$ 收敛到 $B$"、局部周期 $\tau_1,\tau_2$ 与 $\operatorname{Im}(\bar\tau_1\bar\tau_2)\mathrm dy\otimes\mathrm d\bar y$；证明思路中 McLean 度量的两种写法与 $2g(\partial/\partial y,\partial/\partial\bar y)=\int\mathrm dx_1\wedge\mathrm dx_2=\operatorname{Im}(\bar\tau_1\tau_2)$；猜想 7.32（$X_\infty$ 同胚于 $S^n$、$\Delta$ 余维二、Monge--Ampère 度量）；7.3.7 的 SYZ 极限猜想 7.33（$B_\infty$ 与 $X_\infty$ 差尺度等距、$B_{\infty,0}$ 的 Hausdorff 余维二 $\Delta$）与五步证明途径、镜象构造四步、问题 7.34、Gross--Siebert 一段。

## 小结（7 块全部完成）

- 核对范围：PDF 519–583（书 p509–573），7 块，全部逐段对照完毕。
- 落地改动 7 处，均为内容/数学层面的 P1 问题：数学错误 6 处（#1 #2 #3 #5 #6 #7）、误译 1 处（#4）。无标点/文字类改动。
- 待确认 24 条（见上），主要是"译文比原文更精确或补出原文省略的条件"一类，建议保留；唯一需要 Lead 拍板的是 7.3.6-003 定义 7.30 引入 $\delta$ 与 $2$ 倍不等式的处理、7.3.2-003 周期域稳定子 $\operatorname{SO}(2)$ vs $\mathrm O(2)$、7.3.4-008 的 $a\epsilon$ 符号。
- 未运行 latexmk/xelatex（按分工由 Lead 统一编译）；未改动其他章节、main.tex、figures、references.bib、glossary.csv；临时渲染图已全部删除。
