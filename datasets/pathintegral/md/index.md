# 路径积分资料卡 · 索引

共 50 张卡。

## 总览

- [概念] [路径积分总览：从费曼核到量子 HKR](concepts/overview-path-integral.md) —— 第 2 章的主线：把传播子写成路径和，用时间切片与高斯积分算出精确核，再用驻定相位得到半经典核、格林函数与 WKB，最后进入威克定理、费曼图与量子 HKR。

## A · 基础与时间切片

- [概念] [费曼核与传播子](concepts/feynman-kernel.md) —— 把时间演化算子写成积分核，并把它解释为对所有路径按 $e^{iS/\hbar}$ 加权求和；经典极限由驻定相位给出。
- [概念] [自由粒子的精确核 $K_0$](concepts/free-particle-kernel.md) —— 自由粒子的费曼核可在动量基下化为一个高斯积分；算出的相位正是匀速直线轨道的作用量，系数给出 $n$ 维归一化。
- [概念] [虚时间与欧氏路径积分](concepts/imaginary-time.md) —— 令 $t=-i\tau$ 后振荡权重变成实衰减权重，欧氏核有了条件维纳测度，并等同于统计力学的密度矩阵。
- [概念] [路径积分的定义与形式测度](concepts/path-integral-definition.md) —— 把切片公式推到 $N\to\infty$，得到路径空间上的振荡积分；$[D\mathbf{x}]$ 只是记号，严格化要等欧氏化之后。
- [概念] [位置与动量表示（连续谱基）](concepts/position-momentum-representation.md) —— 把连续谱的位置、动量本征向量当形式基使用：δ 归一、完备性、平面波核，以及两套系数之间的傅里叶变换。
- [概念] [时间切片与复合律](concepts/time-slicing.md) —— 把长时间演化切成许多小段：复合律负责接缝，短时核负责给出「动能减势能」的相位，两者合起来就装配出作用量。

## B · 高斯路径积分与谐振子

- [概念] [有限维高斯积分](concepts/gaussian-integral.md) —— 把 $n$ 维二次型高斯积分化为 $n$ 个一维积分之积，得到命题 2.3.1 的无源项与带源项公式；纯虚系数情形由解析延拓给出，整体相位由惯性指数决定。
- [概念] [谐振子配分函数](concepts/harmonic-oscillator-partition.md) —— 对谐振子传播子取迹并延拓到虚时间，算出 $\operatorname{Tr}e^{-\beta\hat H}=1/(2\sinh(\beta\hbar\omega/2))$，与能谱直接求和一致，从而独立检验了 zeta 正则化与归一化常数。
- [概念] [谐振子传播子（Mehler 核）](concepts/harmonic-oscillator-propagator.md) —— 把谐振子路径积分的涨落算子 $A=-\mathrm{d}^2/\mathrm{d}t^2-\omega^2$ 用 zeta 正则化算出 $\det A=2\sin\omega T/\omega$，配合经典作用量得 Mehler 核；$\omega T\in\pi\mathbb{Z}$ 处出现焦散奇点。
- [概念] [zeta 函数正则化与泛函行列式](concepts/zeta-regularization.md) —— 把发散的 $\prod_m\lambda_m$ 换成 $\zeta_A(s)=\sum_m\lambda_m^{-s}$ 在零点的导数值，定义 $\det A=e^{-\zeta_A'(0)}$；对自由粒子的涨落算子算出 $\det A=2T$，再与已知核比对定出归一化常数 $N$。

## C · 渐近方法与半经典

- [概念] [雅可比场与 Van Vleck 行列式](concepts/jacobi-field-van-vleck.md) —— 经典轨迹族对初速度的变分给出雅可比场；它与基本解 $\varphi_0$ 相同，使 $\det A=2\varphi_0$，并把前因子写成作用量二阶导的平方根。共轭点处前因子发散。
- [概念] [拉普拉斯方法](concepts/laplace-method.md) —— 实积分 $\int g\,e^{-\lambda f}\mathrm{d}x$ 在 $\lambda\to+\infty$ 时由 $f$ 的唯一极小点邻域主导；二阶展开给出高斯首阶，$n$ 维推广只把 $f''$ 换成黑塞行列式。
- [概念] [莫尔斯流与最速下降曲线](concepts/morse-flow.md) —— 用流方程 $\mathrm{d}z/\mathrm{d}u=-\overline{f'(z)}$ 生成最速下降曲线：$\operatorname{Im}f$ 守恒、$\operatorname{Re}f$ 单调下降，鞍点的稳定/不稳定流形给出围道的两支。
- [概念] [半经典费曼核](concepts/semiclassical-kernel.md) —— 在 $\hbar\to0$ 时对路径积分用驻定相位：经典轨道给出 $S_{cl}$ 相位，涨落的二阶变分给出前因子；平方根分支还藏着 Maslov 相位。
- [概念] [最速下降法](concepts/steepest-descent.md) —— 把复围道连续形变到 $\operatorname{Im}f$ 为常数、经过鞍点的路径，使 $|e^{-\lambda f}|$ 沿路下降最快，再用高斯积分取首阶。
- [概念] [斯托克斯现象与艾里函数](concepts/stokes-phenomenon.md) —— 有多个鞍点时渐近式是各项之和；参数跨过某些射线时某一项的系数会离散跳变。艾里积分的两个鞍点 $\pm1$ 给出 $e^{\pm\frac{2}{3}\mathrm{i}\lambda}$ 两项。
- [概念] [斯托克斯射线与渐近求和](concepts/stokes-rays-asymptotic-summation.md) —— 解析延拓艾里积分时，λ 平面虚轴上的两条射线让两条最速下降曲线相接；跨过射线时鞍点权重跳变，而首阶渐近保持不变。
- [概念] [时间切片方法的行列式极限](concepts/time-slicing-determinant.md) —— 把涨落积分切成 N 段，离散行列式满足三项递推；步长趋零时递推化为雅可比方程，$\varepsilon\det A_N$ 趋于 $\varphi_0$，独立验证半经典前因子。
- [例子] [自由粒子的半经典核](examples/free-particle-semiclassical.md) —— 对自由粒子做驻定相位：经典轨道是直线，作用量为 $m(x''-x')^2/(2T)$，前因子恰好复现精确传播子。
- [例子] [$\int_C e^{\mathrm{i}z^2}\,\mathrm{d}z$ 的围道计算](examples/fresnel-integral.md) —— 把 $\int_{\mathbb{R}}e^{-\lambda x^2}\mathrm{d}x$ 解析延拓到 $\lambda=-\mathrm{i}$，用旋转 $45^\circ$ 的围道把振荡积分化为高斯积分，得 $e^{\mathrm{i}\pi/4}\sqrt{\pi}$。
- [例子] [Gamma 函数的拉普拉斯渐近](examples/gamma-asymptotics.md) —— 用拉普拉斯方法从 $\Gamma(s)$ 的积分表示导出斯特林公式，练习找极小、算二阶导与配平方。
- [例子] [谐振子的半经典核](examples/harmonic-oscillator-semiclassical.md) —— 求出谐振子的经典轨道与作用量，用作用量二阶导得半经典核，与精确 Mehler 核相同；$\sin\omega T=0$ 处出现焦散。
- [例子] [高斯积分 $\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$ 的最速下降围道](examples/steepest-descent-gaussian.md) —— 对 $\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$ 取 $f=-\mathrm{i}z^2$，由 $\operatorname{Im}f$ 为常数定出直线 $y=x$，把振荡积分化为高斯积分。
- [例子] [$\alpha z^2/2$ 的鞍点流线与最速下降围道](examples/stokes-rays-linear.md) —— 对 $\int_C e^{\lambda\alpha z^2/2}\mathrm{d}z$ 解流方程，得两支 $\pm e^{Au}e^{\mathrm{i}(\pi-\theta)/2}$，合成过原点的直线围道，积分为 $\mathrm{i}\sqrt{2\pi/(\lambda\alpha)}$。

## D · 格林函数与 WKB

- [概念] [连接公式再探](concepts/connection-formula.md) —— WKB 解在转折点失效，需用艾里函数把两侧解接起来；路径积分把这套匹配解释为复平面上绕转折点的解析延拓与 $\theta=\pi/3$ 处的斯托克斯跳跃。
- [概念] [固定能量格林函数](concepts/fixed-energy-green-function.md) —— 把只向未来传播的费曼核对时间差作傅里叶变换，得到预解算子 $(E-\hat H+i\epsilon)^{-1}$ 的核；其极点给出束缚态能级，$+i\epsilon$ 既保证收敛又给出推迟性。
- [概念] [量子隧穿](concepts/quantum-tunneling.md) —— 势垒内 $E<V$，经典轨道要沿复时间走，$\int p\,\mathrm{d}x$ 的势垒段变成虚数；与散射渐近式比较即得透射概率 $e^{-\frac{2}{\hbar}\int_a^b\sqrt{2m(V-E)}\mathrm{d}x}$。
- [概念] [半经典格林函数](concepts/semiclassical-green-function.md) —— 对时间积分用最速下降法：鞍点同时要求经典轨道与能量固定，每个鞍点贡献端点速度的平方根与相位 $\int p\,\mathrm{d}x$；围道形变决定哪些鞍点入选。
- [概念] [经由路径积分的 WKB](concepts/wkb-path-integral.md) —— 把半经典格林函数的端点速度换成 $\sqrt{2(E-V)/m}$，$G$ 就呈 WKB 形状：振幅 $\propto p^{-1/2}$、相位由 $\int p\,\mathrm{d}x$ 给出，与定态 WKB 波函数同构。
- [例子] [自由粒子的固定能量格林函数](examples/free-green-function.md) —— 从自由粒子的动量积分出发，用留数算出固定能量格林函数，并写成 $e^{ik|x''-x'|}$ 的闭式。
- [例子] [自由粒子的半经典格林函数](examples/free-semiclassical-green.md) —— 用半经典公式重算自由粒子格林函数，验证它与精确解逐项相同。
- [例子] [线性势的半经典格林函数](examples/linear-potential.md) —— 线性势的经典轨道、精确核、四个鞍点与分情形的围道取舍，是连接公式的原型。
- [例子] [散射态的渐近行为](examples/scattering-asymptotics.md) —— 用朗斯基行列式拼出散射态格林函数，由 $x\to\pm\infty$ 的边条件读出透射振幅 $A$。
