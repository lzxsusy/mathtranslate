# 镜像五次超曲面的 Picard–Fuchs 方程的推导

> `siebert/deriv/picard-fuchs-derivation` ｜ track A ｜ draft

**目标**：对镜像五次超曲面族 $Y_z$ 推导其周期所满足的四阶 Picard–Fuchs 方程
$$\bigl[\theta^4-5z(5\theta+1)(5\theta+2)(5\theta+3)(5\theta+4)\bigr]\varphi=0,\qquad\theta=z\partial_z,$$
并说明『四阶』与系数 $5$ 的来源。

**自测**：镜像五次超曲面的 Picard–Fuchs 方程为什么恰好是四阶的，算子前的系数 $5$ 又是从哪里来的？

## 前提

- $Y_z$：Dwork 族 $f_\psi=\sum_{i=0}^4x_i^5-5\psi\,x_0x_1x_2x_3x_4$ 在 $z=(5\psi)^{-5}$ 处的纤维；$\Omega(\psi)=5\psi\,\mathrm{Res}_{Y_z}(\tilde\Omega/f_\psi)$ 为全纯三形式（原书 (1.57)–(1.59)）。
- 周期 $\varphi_\gamma(z)=\int_\gamma\Omega$ 是 Gauss–Manin 联络的平坦截面；$H^3(Y_z,\CC)$ 的秩为 $b_3=4$（$h^{3,0}=h^{2,1}=h^{1,2}=h^{0,3}=1$）。
- Griffiths 极点阶数约化：$\partial_z^k\Omega=\mathrm{Res}\bigl(g_k\tilde\Omega/f^{k+1}\bigr)$，$\deg g_k=5k$；若 $g_k\in J(f)=(\partial_0f,\ldots,\partial_4f)$，则可用 $\mathrm{Res}(g\tilde\Omega/f^n)=\mathrm{Res}(h\tilde\Omega/f^{n-1})$ 把极点阶数降低（$\deg h=\deg g-4$）。

## 步骤

1. **先定阶数：$\varphi,\partial_z\varphi,\partial_z^2\varphi,\partial_z^3\varphi,\partial_z^4\varphi$ 是 $b_3=4$ 维局部系统中的 5 个截面，必线性相关，相关系数是 $z$ 的（全纯）函数，故周期满足一个四阶线性 ODE。**  
   为什么：方程阶数由局部系统的秩决定，而不是由 $h^{2,1}+1=2$ 或模空间维数决定。$b_3=4$ 是因为 $Y_z$ 的 Hodge 菱形是 $1/1\;1/1$（镜像把 $X$ 的 $101$ 与 $1$ 互换）；若 $h^{1,1}(Y_z)$ 不是 1，阶数会变。  
   锚点：原书 p.19（证据 A）

2. **把导数写成留数：$\partial_z^k\Omega=\mathrm{Res}(g_k\tilde\Omega/f^{k+1})$，其中 $g_k$ 是多项式、$\deg g_k=5k$。**  
   为什么：每次对 $1/f$ 求 $\partial_z$（等价于 $\partial_\psi$ 乘常数）都把极点阶数加一，同时 $\partial_\psi$ 作用在 $f_\psi$ 上产生 $5x_0x_1x_2x_3x_4$ 这个五次项，故分子次数每次加 5。把 $\Omega$ 写成留数是让『求导』变成『分子多项式次数增加』的关键，否则无法用 Jacobian 理想做约化。  
   锚点：原书 p.19–20（证据 B）

3. **考察 $k=4$：极点阶数 $5$、分子次数 $20$。五次超曲面的 Jacobian 环 $R=\CC[x]/(\partial_0f,\ldots,\partial_4f)$ 的 socle 次数是 $5\cdot(5-2)=15$，故 $R_d=0$（$d>15$）；于是 $g_4\in J(f)$，$\partial^4\Omega$ 必可降阶。反之 $k=3$ 时次数恰为 $15$，$g_3$ 的类在 $R_{15}\cong\CC$ 中一般非零，不能降阶。**  
   为什么：这是全推导的枢纽：$k=4$ 是第一个分子次数超过 socle 次数的阶，因此四阶导数是第一个『必然可约』的导数——方程阶数正是 4，不多不少。$R_{15}$ 一维对应 $h^{0,3}=1$，也解释了为什么 $\partial^3\Omega$ 的留数类就是 Yukawa 方向（$W_3$）。  
   锚点：原书 p.20（证据 A）

4. **约化：$g_4=\sum_i h_i\,\partial_if$，用 $\mathrm{Res}(g_4\tilde\Omega/f^5)=\mathrm{Res}(h\tilde\Omega/f^4)$（$\deg h=20-4=16$）逐次把极点阶数从 5 降到 4、3、2、1，最终得到 $\partial_z^4\Omega=\sum_{k=0}^3c_k(z)\,\partial_z^k\Omega$，$c_k(z)$ 为有理函数。**  
   为什么：每一步都靠『$g\in J(f)$ 时可把 $g$ 写成 $\sum h_i\partial_if$、再分部积分降一阶』；因为 $z$ 作为参数进入 $g_k$ 的系数，降阶后的 $c_k$ 会依赖 $z$——这正是 ODE 的系数。若 $g_4$ 不在 $J(f)$ 中，这一步就失败，方程会是五阶。  
   锚点：原书 p.20（证据 A）

5. **对周期积分：把 $\partial_z^4\Omega=\sum c_k\partial_z^k\Omega$ 在闭链 $\gamma$ 上积分，得 $\varphi^{(4)}=\sum c_k\varphi^{(k)}$，即一个四阶线性 ODE；再以 $\theta=z\partial_z$ 改写。**  
   为什么：周期是 $\Omega$ 的积分，$\partial_z$ 与 $\int_\gamma$ 交换（$\gamma$ 是拓扑闭链，不随 $z$ 变），所以 $\Omega$ 的线性关系直接变成周期的线性关系。改用 $\theta$ 是因为 $z=0$ 是正则奇点、四个指数全为 0，$\theta$ 形式让指标方程与系数结构（整数、$5$ 的幂）透明。  
   锚点：原书 p.20（证据 A）

6. **用 $\varphi_0(z)=\sum_{n\ge0}\frac{(5n)!}{(n!)^5}z^n$ 反验算子：$\theta^4$ 作用给 $n^4a_n$；$5z\prod_{j=1}^4(5\theta+j)$ 作用给 $5\prod_{j=1}^4(5(n-1)+j)\,a_{n-1}=5(5n-4)(5n-3)(5n-2)(5n-1)a_{n-1}$。而级数系数比 $a_n/a_{n-1}=\frac{5^5\prod_{j=1}^4(n-j/5)}{n^4}=\frac{5(5n-1)(5n-2)(5n-3)(5n-4)}{n^4}$，代入即逐项相消。**  
   为什么：这一步把『四阶』与『系数 5』同时钉死：若第二项前面的常数写成 $1$ 或 $25$，级数就不满足方程。已知 $\varphi_0$ 是解（由 (1.66) 的显式级数），而四阶方程的解空间是 4 维、算子由首一化唯一确定，故算子被完全确定；这也说明讲义从约化到 (1.76) 虽未写出中间系数，结论是自洽的。  
   锚点：原书 p.19–20（证据 B）

## 结果

$\bigl[\theta^4-5z(5\theta+1)(5\theta+2)(5\theta+3)(5\theta+4)\bigr]\varphi=0$，$\theta=z\partial_z$；$z=0$ 为正则奇点，四个指标均为 $0$，故有 $\log z$ 解（见 mirror-map-periods 卡）。

## 缺口

- 讲义没有写出从 $\mathrm{Res}(g_4\tilde\Omega/f^5)$ 降到 $c_k(z)$ 的中间系数；本卡没有重建 reduction 的代数细节，而是用 $\varphi_0$ 逐项代入验证 (1.76)，再由『四阶 + 首一』的唯一性确定算子。
- $g\in J(f)\Rightarrow$ 留数可降阶（Griffiths 定理）与 $\mathrm{Res}(g\tilde\Omega/f^n)=\mathrm{Res}(h\tilde\Omega/f^{n-1})$ 的符号/常数因子未证，只引用。
- 『$z=0$ 正则、四指数全为 0』讲义只断言；本卡未给 indicial 方程的完整计算（虽可直接由算子的 $\theta$ 形式读出）。
- $z=5^{-5},\infty$ 处的单值性与解析延拓未涉及。

## 易错点

- $\theta\neq\partial_z$：$\theta=z\partial_z$；(1.76) 直接展成 $d/dz$ 形式时系数会差 $z$ 的幂，比对时容易误判系数。
- PF 方程是镜像族 $Y_z$（$h^{2,1}=1$）的方程，不是原五次超曲面 $X$ 的；$X$ 侧的对象是量子上同调/GKZ 系统。
- 第二项是 $5z\prod_{j=1}^4(5\theta+j)$，不是 $z\prod(\theta+j)$ 或 $25z\prod(5\theta+j)$；系数 $5$ 由 $\varphi_0$ 的系数比 $5^5/(5^4)=5$ 决定。
- 算子阶数是 $b_3=4$，不是 $h^{2,1}+1=2$；把『单参数族』误当成『二阶方程』是常见错误。
- $\varphi_0$ 是 (1.76) 的一个解，不是唯一解：解空间 4 维，其余三个含 $\log z$ 及其幂，不能把 $\varphi_0$ 当成通解。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §9.1–§9.2（其他周期、方程推导、Griffiths 极点阶数约化），p.19–20（原书 p.19–20）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §8 归一化，p.19–19（原书 p.19）

关联：`siebert/concept/picard-fuchs-equation`、`siebert/concept/griffiths-transversality`、`siebert/deriv/mirror-map-periods`

来源说明：原书 p.19–20（§8 的 (1.60)–(1.66) 与 §9 的 (1.70)–(1.76)）。Jacobian 环 socle 次数 $5(5-2)=15$ 与 $R_{15}\cong\CC$ 按 Griffiths 留数理论核对；系数比 $a_n/a_{n-1}$ 与算子逐项作用用 sympy 1.14.0 复核。
