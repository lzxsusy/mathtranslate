# 几何量子化资料卡 · 索引

共 48 张卡。

## 总览

- [概念] [几何量子化总览：从相空间到量子希尔伯特空间](concepts/overview-geometric-quantization.md) —— 第 5 章主线：辛几何搭相空间，半经典给出 (L,Ω)，海森堡群给出表示模型，再由预量子化、极化与半形式三步组装成几何量子化。

## A · 相空间的辛几何

- [概念] [相容复结构与可缩性](concepts/compatible-complex-structure.md) —— 与辛形式相容的复结构使辛空间同时具备凯勒结构：二者合成对称正定内积；而全体相容复结构构成可缩空间。
- [概念] [余切丛的典范辛结构与刘维尔形式](concepts/cotangent-bundle.md) —— 对任意 $X$，$T^*X$ 上由 $\lambda_\xi=\xi\circ d\pi$ 定义的整体 $1$-形式使 $d\lambda$ 非退化；截面恒等式 $S_\alpha^*\lambda=\alpha$ 把拉格朗日条件化为 $d\alpha=0$。
- [概念] [哈密顿向量场与泊松括号](concepts/hamiltonian-vector-field.md) —— 由 $\iota_{V_f}\omega=df$ 定义的向量场 $V_f$ 与 $\{f,g\}=V_f(g)$ 构成李代数同态；$V_f$ 保辛形式与体积，且 $V_{\{f,g\}}=[V_f,V_g]$。
- [概念] [拉格朗日子空间与格拉斯曼流形](concepts/lagrangian-grassmannian.md) —— 辛形式在子空间上消失、且维数恰为全空间一半者称拉格朗日；全体这样的子空间构成紧齐性流形，酉群在其上可迁。
- [概念] [拉格朗日子流形、可投影与相函数](concepts/lagrangian-submanifold.md) —— 半维且 $\omega|_L=0$ 的子流形；在 $T^*X$ 上等价于 $\lambda|_L$ 闭。闭 $1$-形式给出可投影者，恰当时相函数只定到常数，而圆例说明闭未必恰当。
- [概念] [马斯洛夫指标与 $\mathcal L(V)$ 的基本群](concepts/maslov-index.md) —— 拉格朗日格拉斯曼流形的基本群是整数，生成元由行列式平方给出；环路对应的整数叫马斯洛夫指标，等于该复合映射的绕数。
- [概念] [辛群 $\operatorname{Sp}(V)$](concepts/symplectic-group.md) —— 保持辛配对的可逆线性变换组成辛群；在标准基下即满足分块矩阵方程的矩阵，维数 $n(2n+1)$，并与正交群、复线性群两两相交于酉群。
- [概念] [辛流形（symplectic manifold）](concepts/symplectic-manifold.md) —— 光滑流形配上闭的、逐点非退化的 $2$-形式；非退化把切空间与余切空间等同，闭性让哈密顿流保辛，$\omega^n/n!$ 给出刘维尔体积。
- [概念] [辛向量空间与辛基](concepts/symplectic-vector-space.md) —— 实向量空间配一个非退化斜对称双线性形式；非退化即零空间平凡，此时维数必为偶数，且总能取到把形式化为标准矩阵的辛基。
- [概念] [辛同胚与哈密顿流](concepts/symplectomorphism.md) —— 满足 $\varphi^*\omega=\omega$ 的微分同胚；哈密顿流是单参数辛同胚群，$f=f(q)$ 时它平移纤维，把 $L_\alpha$ 送到 $L_{\alpha+df}$。
- [例子] [$\mathbb{R}^2=T^*\mathbb{R}$ 中的圆是拉格朗日子流形](examples/circle-lagrangian-in-r2.md) —— $L=\{p^2+q^2=R^2\}\subset T^*\mathbb{R}$ 是一维拉格朗日；算得 $\lambda|_L=-R^2\sin^2\theta\,d\theta$、周期 $-\pi R^2$，故闭而不恰当，且不可投影。
- [例子] [$\mathbb R^2$ 上相容复结构的参数化](examples/compatible-complex-structures-on-r2.md) —— 在 $(\mathbb R^2,\omega_1)$ 上，相容复结构由一个自由参数与一个正参数刻画，整族同胚于可缩的上半平面。
- [例子] [余切丛 $T^*X$ 的典范辛形式（$X=\mathbb{R}^2$）](examples/cotangent-bundle-symplectic.md) —— 在 $T^*\mathbb{R}^2$ 上具体写出 $\lambda=\sum p_idq^i$ 与 $\omega=d\lambda$，检验非退化，并用一次非线性换元验证 $\lambda$ 与 $\omega$ 都不依赖坐标。
- [例子] [恰当拉格朗日 $L_{df}$ 与相函数（$f=q^1q^2$）](examples/exact-lagrangian-phase-function.md) —— 取 $X=\mathbb{R}^2$、$f=q^1q^2$，写出 $L_{df}=\{p_1=q^2,\ p_2=q^1\}$，验证 $\lambda|_L=df$、$\omega|_L=0$，并用切向量直接核对迷向性。
- [例子] [哈密顿流是辛同胚（$f=\tfrac12q^2$ 与 $f=q^1q^2$）](examples/hamiltonian-flow-symplectomorphism.md) —— 对 $f=\frac12q^2$ 解出 $V_f=q\,\partial_p$ 与 $\varphi_t(q,p)=(q,p+tq)$，直接验证 $\varphi_t^*\omega=\omega$；$f=q^1q^2$ 时交叉项同样相消。
- [例子] [$\mathcal L(\mathbb R^2)=\mathbb{RP}^1$ 上的马斯洛夫指标](examples/maslov-index-rp1.md) —— 平面上的拉格朗日格拉斯曼流形是射影直线；绕单位圆一圈的环路经行列式平方后绕两圈，指标为 $2$。
- [例子] [$n=1$ 时 $\operatorname{Sp}(2)=\operatorname{SL}(2)$](examples/sp2-equals-sl2.md) —— 在 $\mathbb{R}^2$ 的标准辛形式下，保持 $\omega$ 的矩阵恰好是行列式为 1 的矩阵，于是辛群退化为特殊线性群。
- [例子] [标准辛基下的相容复结构](examples/standard-compatible-complex-structure.md) —— 在辛基上令 $J_0(e_i)=f_i$、$J_0(f_i)=-e_i$，得到的 $J_0$ 与 $\omega_n$ 相容，$g_{J_0}$ 恰为坐标欧氏内积。
- [例子] [标准辛基给出的两张拉格朗日子空间](examples/standard-lagrangian-subspaces.md) —— 辛基的 $e$ 半边与 $f$ 半边各自张成拉格朗日子空间，二者互为 $\omega$-正交补，并直和成整个空间。
- [例子] [$\operatorname{Sp}(2n)\cap\operatorname{O}(2n)=\operatorname{U}(n)$ 的显式实现](examples/unitary-symplectic-intersection.md) —— 把 $A+iB$ 映为实分块矩阵 $\begin{pmatrix}A&-B\\B&A\end{pmatrix}$，它同时辛且正交，且这一对应是酉群与该交集之间的双射。

## B · 几何半经典量子化

- [概念] [玻尔–索末菲量子化条件](concepts/bohr-sommerfeld.md) —— 拉格朗日子流形上刘维尔形式的限制自动闭，却未必恰当；要求相位因子沿每个闭链单值，就得到 ∮λ 落在 2πℏ 整数倍上的玻尔–索末菲条件。
- [概念] [几何半经典定态](concepts/geometric-semiclassical-state.md) —— 定态的半经典信息浓缩为一对 (L,Ω)：拉格朗日子流形落在能量面上、半密度在哈密顿流下不变；这个定义不依赖投影坐标，因此能跨过焦散描述态。
- [概念] [密度、半密度与刘维尔测度](concepts/half-density.md) —— 密度按雅可比行列式的绝对值变换，因此不依赖定向就能积分；把指数取成 1/2 得半密度，它的模方是测度，WKB 振幅与刘维尔型守恒律都写在它身上。
- [概念] [马斯洛夫修正与 EBK 条件](concepts/maslov-correction.md) —— 半密度只能取到四分相位，沿闭链绕一圈多出 e^{−iπm/2}；把这份马斯洛夫相位并入玻尔–索末菲条件，得到 (1/2πℏ)∮λ−m/4∈ℤ 的凯勒–马斯洛夫（EBK）规则。
- [概念] [WKB 半经典解与哈密顿–雅可比方程](concepts/wkb-approximation.md) —— 把定态波函数写成相位因子乘 ℏ 的幂级数，逐阶代入薛定谔方程：首阶给出哈密顿–雅可比方程，次阶给出输运方程，几何上等于在能量面上选定一张拉格朗日子流形。
- [例子] [一维谐振子的水平集与焦散](examples/harmonic-oscillator-level-set.md) —— 把一维谐振子的能量面解成相平面里的椭圆，验证它是拉格朗日子流形；再找出投影的临界点，得到左右两个焦散。
- [例子] [谐振子的凯勒–马斯洛夫条件给出精确谱](examples/oscillator-ebk-spectrum.md) —— 沿椭圆的刘维尔积分是 2πE/ω，马斯洛夫指标为 2；代入 EBK 条件即得 E=ℏω(n+1/2)，与谐振子的精确谱逐项吻合。

## C · 海森堡群与表示

- [概念] [海森堡群 $H_V$ 与中心扩张](concepts/heisenberg-group.md) —— 用指数映射把 $h_V$ 整体化为单连通幂零群 $H_V$；BCH 因二阶幂零而截断，群律只比向量加法多出 $\frac12\omega(u_1,u_2)$ 的中心项，这正是 $\mathbb{R}$-中心扩张的非平凡 2-上闭链。
- [概念] [海森堡李代数 $h_V$](concepts/heisenberg-lie-algebra.md) —— 在 $2n$ 维辛空间 $V$ 上添一维中心 $K$，用辛配对定义括号 $[u,v]=\omega(u,v)K$，得 $2n+1$ 维二阶幂零李代数；辛基下它化为 $n$ 组正则对易关系，辛群自动作用为自同构。
- [概念] [薛定谔表示 $T_\hbar$](concepts/schrodinger-representation.md) —— 海森堡群在 $L^2(\mathbb{R}^n)$ 上的酉表示：先平移 $\mathbf x\mapsto\mathbf x-\mathbf s$，再乘相位 $e^{\frac{i}{\hbar}(\mathbf r\cdot\mathbf x-\frac12\mathbf r\cdot\mathbf s+\lambda)}$；$\hbar$ 只在相位里出现，标记中心作用 $K\mapsto\frac{i}{\hbar}$。
- [概念] [Segal–Bargmann 空间](concepts/segal-bargmann-space.md) —— $\mathbb{C}^n$ 上以 $e^{-|z|^2/\hbar}$ 为权的全纯 $L^2$ 空间；$a_i^\dagger=z^i$ 与 $a_i=\hbar\partial_{z^i}$ 互为伴随，单项式基 $\lambda_I$ 使它同构于福克空间，海森堡群在其上作用为巴格曼–福克表示。
- [概念] [斯通–冯·诺依曼定理](concepts/stone-von-neumann.md) —— 固定中心特征 $\rho(e^{\lambda K})=e^{\frac{i\lambda}{\hbar}}$ 后，海森堡群的不可约酉表示在酉等价意义下唯一，就是 $T_\hbar$；等价算子只在差一个模 $1$ 相位时唯一。

## D · 几何量子化机器

- [概念] [狄拉克量子化原理 Q1–Q5](concepts/dirac-quantization.md) —— 狄拉克把量子化定义为从经典可观测量到自伴算子的对应，并列出五条要求：实数线性、保单位、实函数自伴、括号关系、完全集保持。四条约束算子代数，第五条约束希尔伯特空间的大小。
- [概念] [格罗嫩沃尔德–范霍夫定理（Groenewold–Van Hove）](concepts/groenewold-van-hove.md) —— 不存在把四次以下多项式都变成自伴算子、保单位、在低次上与标准实现一致、又满足括号关系的映射。证明把 $x^2p^2$ 写成两种泊松括号，两条路给出的算子相差 $\hbar^2/3$。
- [概念] [极化：实极化与凯勒极化](concepts/polarization.md) —— 极化是切丛复化里一族拉格朗日子空间：要求对李括号封闭、与共轭部分相交维数恒定。它把预量子化态砍掉一半变量，实极化给位置波函数，凯勒极化给全纯函数。
- [概念] [预量子化线丛](concepts/prequantization.md) —— 用带相容联络的厄米线丛把经典可观测量提升为截面算子 Q(f)=iℏ∇_{V_f}+f；曲率锁定为 −(i/ℏ)ω 保证括号关系，但希尔伯特空间仍太大。
- [概念] [可量子化条件（陈类整性）](concepts/quantization-condition.md) —— 预量子化线丛存在当且仅当 $\frac{1}{2\pi\hbar}[\omega]$ 是整上同调类，即 $\omega$ 在每个闭曲面上的积分除以 $2\pi\hbar$ 为整数。条件只依赖 $[\omega]$，却随 $\hbar$ 的标定而变。
- [概念] [量子希尔伯特空间与半形式修正](concepts/quantum-hilbert-space.md) —— 在预量子化截面上再要求沿极化方向平行，得到只依赖一半变量的量子希尔伯特空间；紧流形的凯勒情形下它有限维，再把线丛换成张上半形式丛，谐振子谱就从 nℏ 抬成 (n+½)ℏ。
- [概念] [量子算子与 P-保持条件](concepts/quantum-operator.md) —— 只有当哈密顿向量场把极化映回自身时，预量子化算子 Q(f)=iℏ∇_{V_f}+f 才把 P-极化截面送到 P-极化截面。实极化下这类函数是 a(x)+Σb_i(x)p_i，凯勒极化下是二次多项式。
- [例子] [余切丛总可量子化](examples/cotangent-bundle-quantizable.md) —— 余切丛上的刘维尔形式给出恰当的辛形式，陈类自动为零，因此任意余切丛都可预量子化，线丛取平凡丛即可。
- [例子] [全纯线丛上的凯勒极化](examples/holomorphic-line-bundle-polarization.md) —— 对全纯线丛取相容联络，其反全纯分量就是 Dolbeault 算子；令辛形式为曲率的 $i\hbar$ 倍，预量子化自动成立，极化截面即全纯截面。
- [例子] [$\mathbb{C}^n$ 的凯勒极化与全纯截面](examples/kahler-polarization-cn.md) —— 用凯勒势定义辛形式与联络，取反全纯方向的极化后极化截面恰为全纯函数，内积带权 $e^{-K/\hbar}$。
- [例子] [凯勒极化、半形式与 $(n+\frac12)\hbar$ 谱](examples/oscillator-half-form-spectrum.md) —— 在 C 上取 K=|z|² 与凯勒极化，全纯截面上的 Q(H)=ℏz∂_z 只有 nℏ 谱；把态换成 L⊗√K_M 的截面 z^n√dz 后，半形式的 ½ 权重把谱修正为 (n+½)ℏ。
- [例子] [实极化下 P-保持函数的量子化](examples/quantum-operators-real-polarization.md) —— 在 R^{2n} 的竖直极化下，保持极化的函数恰为 a(x)+Σb_i(x)p_i；把它们代入 Q(f) 后动量项与刘维尔形式项相消，只剩 -iℏΣb_i∂_{x^i}+a(x)。
- [例子] [$\mathbb{R}^{2n}$ 的实极化与位置波函数](examples/real-polarization-r2n.md) —— 取动量方向的实拉格朗日极化后，协变常值截面恰为只依赖位置的函数，预量子化空间由此化为位置波函数。
- [例子] [$S^2$ 的可量子化条件 $A\in\frac{\hbar}{2}\mathbb{Z}$](examples/s2-quantization-condition.md) —— 球面上的辛形式总面积为 $4\pi A$，预量子化的整性要求它等于 $2\pi\hbar k$，故 $A$ 只能取 $\hbar/2$ 的整数倍。
- [例子] [线丛张量幂与 $\hbar$ 的重新标定](examples/tensor-power-line-bundle.md) —— 把预量子化线丛换成 $k$ 次张量幂，曲率变为 $k$ 倍，等价于把普朗克常数改成 $\hbar/k$；$k$ 增大即经典极限。
