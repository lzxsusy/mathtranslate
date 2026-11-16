# Segal–Bargmann 空间

> `geoq/concept/segal-bargmann-space` · 轨道 C · 海森堡群与表示 · 状态 draft

> **先自测**：为什么把权 $e^{-|z|^2/\hbar}$ 放进内积之后，乘法算子 $z^i$ 的伴随就恰好是 $\hbar\partial_{z^i}$？

## 一句话

$\mathbb{C}^n$ 上以 $e^{-|z|^2/\hbar}$ 为权的全纯 $L^2$ 空间；$a_i^\dagger=z^i$ 与 $a_i=\hbar\partial_{z^i}$ 互为伴随，单项式基 $\lambda_I$ 使它同构于福克空间，海森堡群在其上作用为巴格曼–福克表示。

## 定义

在 $\mathbb{C}^n$ 上先固定高斯权内积 $\langle f|g\rangle_\hbar=\frac{1}{(\pi\hbar)^n}\int_{\mathbb{C}^n}\mathrm{d}^{2n}z\,\overline{f(z)}g(z)e^{-|z|^2/\hbar}$，其中常数取成使常函数 $1$ 的范数为 $1$，并记 $\|f\|_\hbar^2=\langle f|f\rangle_\hbar$。所谓 Segal–Bargmann 空间，指的是由 $\mathbb{C}^n$ 上全纯且范数有限的函数组成的集合 $\mathcal{F}_n=\left\{f:\mathbb{C}^n\to\mathbb{C}\ \middle|\ f\ \text{全纯且}\ \|f\|_\hbar<\infty\right\}$。按命题 5.3.5，它配有希尔伯特空间结构。其上 $a_i^\dagger=z^i$ 与 $a_i=\hbar\partial_{z^i}$ 互为伴随，对易子为 $[a_i,a_j^\dagger]=\delta_{ij}\hbar$；海森堡群经巴格曼–福克表示 $\rho_\hbar$ 作用在 $\mathcal{F}_n$ 上，而斯通–冯·诺依曼定理保证它与薛定谔表示酉等价。

**记号约定**：$z=(z^1,\dots,z^n)\in\mathbb{C}^n$，$\mathrm{d}^{2n}z$ 是 $2n$ 维勒贝格测度，$|z|^2=\sum_i|z^i|^2$；全纯指 $\partial_{\bar z^i}f=0$；$I=(i_1,\dots,i_n)$ 是多重指标，$|I|=\sum_ki_k$，$I!=\prod_ki_k!$，$\mathbf z^I=\prod_k(z^k)^{i_k}$。

## 要点

- 权与归一化：$\int_{\mathbb{C}}e^{-|z|^2/\hbar}\mathrm{d}^2z=\pi\hbar$，故 $\langle1|1\rangle_\hbar=1$；这个常数决定了 $\lambda_I$ 的范数正好是 $1$，而不是 $\hbar^{|I|}I!$。
- 全纯加高斯权使逐点赋值连续：由多圆盘上的平均值性质与柯西–施瓦茨不等式，在每个紧集上有 $|f(z_0)|\leq C_V\|f\|_\hbar$；于是 $L^2$ 收敛蕴含局部一致收敛，$\mathcal{F}_n$ 完备（命题 5.3.5）。
- 伴随对：把 $\bar z^i$ 改写成 $-\hbar\partial_{z^i}$ 作用在权函数上再分部积分，得 $\langle z^if|g\rangle_\hbar=\langle f|\hbar\partial_{z^i}g\rangle_\hbar$，即 $(z^i)^\dagger=\hbar\partial_{z^i}$，从而 $[a_i,a_j^\dagger]=\delta_{ij}\hbar$。
- 单项式基：$\lambda_I=\mathbf z^I/\sqrt{\hbar^{|I|}I!}$ 正交归一（命题 5.3.7），且 $\lambda_I=\prod_k\frac{(a_k^\dagger)^{i_k}}{\sqrt{\hbar^{i_k}i_k!}}\,1$ 正是福克空间（Fock space）的激发态，$|I|$ 是总粒子数。
- 群作用：$(\rho_\hbar(\mathbf w)f)(\mathbf z)=e^{\frac{1}{\hbar}\left(\bar{\mathbf w}\cdot\mathbf z-\frac12|\mathbf w|^2\right)}f(\mathbf z-\mathbf w)$；由定理 5.3.3，它与 $T_\hbar$ 酉等价，交织算子就是 Segal–Bargmann 变换 $\mathcal{B}$。

## 关键公式

$$
$\langle f|g\rangle_\hbar=\frac{1}{(\pi\hbar)^n}\int_{\mathbb{C}^n}\mathrm{d}^{2n}z\,\overline{f(z)}g(z)e^{-|z|^2/\hbar}$
$$

$$
$\langle z^if|g\rangle_\hbar=\langle f|\hbar\partial_{z^i}g\rangle_\hbar,\qquad a_i^\dagger=z^i,\quad a_i=\hbar\partial_{z^i},\quad[a_i,a_j^\dagger]=\delta_{ij}\hbar$
$$

$$
$\lambda_I(\mathbf z)=\frac{\mathbf z^I}{\sqrt{\hbar^{|I|}I!}},\qquad \langle\lambda_I|\lambda_J\rangle_\hbar=\delta_{IJ}$
$$

$$
$(\rho_\hbar(\mathbf w)f)(\mathbf z)=e^{\frac{1}{\hbar}\left(\bar{\mathbf w}\cdot\mathbf z-\frac12|\mathbf w|^2\right)}f(\mathbf z-\mathbf w)$
$$

$$
$(\mathcal{B}\psi)(\mathbf z)=\frac{1}{(\pi\hbar)^{n/4}}\int_{\mathbb{R}^n}\mathrm{d}^n\mathbf x\,e^{-\frac{1}{2\hbar}\left(\mathbf z\cdot\mathbf z-2\sqrt2\,\mathbf z\cdot\mathbf x+\mathbf x\cdot\mathbf x\right)}\psi(\mathbf x)$
$$

## 定理与证明

### 命题 5.3.6（乘法与求导互为伴随）

设 $f,g$ 是关于 $\mathbf z=(z^1,\dots,z^n)$ 的多项式函数。则 $\langle z^if|g\rangle_\hbar=\langle f|\hbar\partial_{z^i}g\rangle_\hbar$，即乘法算子 $z^i$ 的伴随是 $\hbar\partial_{z^i}$。

**完整证明**

1. 写出左端并注意 $\overline{z^if}=\bar z^i\bar f$。关键恒等式：$\partial_{z^i}e^{-|z|^2/\hbar}=-\frac{\bar z^i}{\hbar}e^{-|z|^2/\hbar}$，故 $\bar z^ie^{-|z|^2/\hbar}=-\hbar\partial_{z^i}e^{-|z|^2/\hbar}$。
   - *为什么*：高斯权是唯一能把 $\bar z^i$ 吸收进去的因子：$|z|^2=z\bar z$ 对 $z^i$ 求导正好给出 $\bar z^i$，这才让「乘 $\bar z$」变成「求导」。
2. 把 $\bar z^ie^{-|z|^2/\hbar}$ 换成 $-\hbar\partial_{z^i}e^{-|z|^2/\hbar}$ 后分部积分。全纯性给出 $\partial_{z^i}\overline{f(z)}=0$，边界项因高斯衰减而消失，导数整个落到 $g$ 上，得到 $\hbar\int\overline{f(z)}\,\partial_{z^i}g(z)\,e^{-|z|^2/\hbar}$。
   - *为什么*：分部积分把导数从权函数搬到 $g$；$f$ 全纯保证 $\bar f$ 被 $\partial_z$ 杀死——若 $f$ 只是光滑函数，这一步会多出 $\partial_{z^i}\bar f$ 项，伴随关系就不成立。
3. 两边同除公共归一化 $(\pi\hbar)^n$，得 $\langle z^if|g\rangle_\hbar=\langle f|\hbar\partial_{z^i}g\rangle_\hbar$。
   - *为什么*：归一化常数在等式两边相同，不影响结果；它只在计算具体范数（如 $\|\lambda_I\|$）时起作用。

来源：ch05b.tex:280-302（原书 p.276）

### 命题 5.3.7（单项式基正交归一）

$\{\lambda_I\}_I$ 构成 $\mathcal{F}_n$ 的一组正交归一基，其中 $\lambda_I(\mathbf z)=\mathbf z^I/\sqrt{\hbar^{|I|}I!}$。

**完整证明**

1. 正交性：把 $\mathbf z^I$ 写成 $(a^\dagger)^I$、把 $\langle\mathbf z^I|$ 写成 $\langle1|a^I$（$a_i^\dagger=z^i$ 且 $a_i$ 是其伴随），则 $\langle\mathbf z^I|\mathbf z^J\rangle_\hbar=\langle1|a^I(a^\dagger)^J|1\rangle_\hbar$，而 $a_i1=0$，故 $I\neq J$ 时为 $0$。
   - *为什么*：把内积搬到真空上算是福克空间的标准技巧，它把积分问题变成代数问题；代价是要先确认 $a_i$ 确实湮灭常数。
2. 范数：反复用 $[a_i,a_i^\dagger]=\hbar$ 把 $a_i^{i_i}(a_i^\dagger)^{i_i}$ 化为 $\hbar^{i_i}i_i!$，得 $\langle\mathbf z^I|\mathbf z^I\rangle_\hbar=\hbar^{|I|}I!$；也可用极坐标直接核对：$\int_0^\infty r^{2k+1}e^{-r^2/\hbar}\mathrm{d}r=\frac12\hbar^{k+1}k!$。
   - *为什么*：两种算法给出同一个数，说明 $\hbar$ 只以 $\hbar^{|I|}$ 的整体幂出现，这正是 $\lambda_I$ 里 $\sqrt{\hbar^{|I|}}$ 的来源。
3. 归一化：除以 $\sqrt{\hbar^{|I|}I!}$ 后 $\|\lambda_I\|_\hbar=1$，不同指标仍正交。
   - *为什么*：正交性在整体缩放后不变，只需把每个向量的长度调到 $1$。
4. 完备性：对 $f\in\mathcal{F}_n$ 取泰勒级数 $f=\sum_Ic_I\mathbf z^I$（在紧集上一致收敛）；用 $P_R(0)$ 上的截断 $\chi_R$ 先算 $\langle\mathbf z^I\chi_R|\mathbf z^J\chi_R\rangle_\hbar=\delta_{IJ}d_{I,R}$，其中 $d_{I,R}$ 随 $R$ 增大且 $d_{I,R}\to\hbar^{|I|}I!$；一致收敛给出 $\|f\chi_R\|_\hbar^2=\sum_I|c_I|^2d_{I,R}$，令 $R\to\infty$ 得 $\|f\|_\hbar^2=\sum_I|c_I|^2\|\mathbf z^I\|_\hbar^2$。
   - *为什么*：这个范数等式说明 $f$ 落在 $\{\lambda_I\}$ 的闭张成里；否则右边会严格小于 $\|f\|^2$，基就不完备。
5. 综合 1–4：$\{\lambda_I\}$ 正交、归一并对每个 $f$ 满足范数等式，故构成一组正交归一基。
   - *为什么*：在希尔伯特空间里，「正交归一 + 对全空间成立帕塞瓦尔等式」就是正交基的判据，不需要再单独证明稠密性。

来源：ch05b.tex:331-374（原书 p.277）

### 命题 5.3.8（升算子的范数恒等式与公共定义域）

设 $f\in\mathcal{F}_n$，则 $\|z^if\|_\hbar^2=\hbar\|f\|_\hbar^2+\|\hbar\partial_{z^i}f\|_\hbar^2$；特别地 $a_i$ 与 $a_i^\dagger$ 在 $\mathcal{F}_n$ 上有相同的定义域。

**证明提纲**

1. 先对基向量验证：$z^i\lambda_I=\sqrt{\hbar(i_I+1)}\,\lambda_{I+e_i}$，$\hbar\partial_{z^i}\lambda_I=\sqrt{\hbar i_I}\,\lambda_{I-e_i}$（$i_I=0$ 时为零），故 $\|z^i\lambda_I\|_\hbar^2=\hbar(i_I+1)$，而右端为 $\hbar+\hbar i_I$，两边相等。
   - *为什么*：单项式基把两个算子都变成「移动一个指标」的算子，范数可以直接从系数读出，不需要做积分。
2. 一般情形 $f=\sum_Ic_I\lambda_I$：只要已知 $z^if$ 与 $\hbar\partial_{z^i}f$ 仍可按 $\{\lambda_I\}$ 展开，就可用帕塞瓦尔等式逐项比较，得到同一个恒等式。
   - *为什么*：这是「由基向量推到全空间」的标准通道，但它要求算子作用后仍留在空间里、且级数可逐项取范数——这两点书中没有验证。
3. 定义域相同：恒等式两边同有限或同无限，故 $z^if\in L^2_\hbar$ 当且仅当 $\hbar\partial_{z^i}f\in L^2_\hbar$。
   - *为什么*：这正是命题的第二个断言；它保证升、降算子互为真正的（而非形式的）伴随。

> **缺口**：书中对一般情形的证明只用一句「由帕塞瓦尔等式得到」带过；真正缺的是两步：先说明 $z^i$ 与 $\partial_{z^i}$ 作用后仍留在 $\mathcal F_n$（这需要先验估计），再验证逐项极限可与范数交换。


来源：ch05b.tex:377-387（原书 p.278）

## 易错点

- 全纯与反全纯不能混：$\mathcal{F}_n$ 里是全纯函数，$a_i^\dagger=z^i$ 是乘 $z$，$a_i=\hbar\partial_z$；若把共轭 $\bar z$ 当成升算子，命题 5.3.6 的伴随关系会整个算反。
- 内积关于第一个变量共轭线性，所以 $\langle z^if|g\rangle$ 里出现的是 $\bar z^i$ 而不是 $z^i$——这正是能把 $\bar z^i$ 换成 $-\hbar\partial_{z^i}$ 的原因；约定反过来写，符号就要跟着改。
- $\hbar$ 的位置：$a_i=\hbar\partial_{z^i}$ 而不是 $\partial_{z^i}$，于是 $[a_i,a_j^\dagger]=\delta_{ij}\hbar$；若把 $\hbar$ 从 $\partial$ 上挪走，对易子变成 $\delta_{ij}$，$\lambda_I$ 的归一化因子也得改。
- 书内两处系数疑误（原文已加旁注）：命题 5.3.5 证明末行的系数按量纲应为 $(\pi\hbar)^{n/2}$ 而原文写作 $(\pi\hbar)^n$；Segal–Bargmann 变换酉性计算中的指数应为 $-\frac{1}{4\hbar}(\mathbf x-\mathbf y)\cdot(\mathbf x-\mathbf y)$ 而原文写成 $-\frac{1}{4\hbar}(\mathbf x\cdot\mathbf x-\mathbf y\cdot\mathbf y)^2$。结论不受影响，但照抄公式时要当心。

## 相关卡

- [薛定谔表示 $T_\hbar$](../concepts/schrodinger-representation.md)
- [斯通–冯·诺依曼定理](../concepts/stone-von-neumann.md)
- [海森堡群 $H_V$ 与中心扩张](../concepts/heisenberg-group.md)
- [海森堡李代数 $h_V$](../concepts/heisenberg-lie-algebra.md)

## 出处

- §5.3.4 巴格曼–福克表示，p.275–280（PDF p.276–281），源码 `ch05b.tex:220-554`
- §5.3.4 巴格曼–福克表示与 Segal–Bargmann 变换，p.278–280（PDF p.279–281），源码 `ch05b.tex:389-554`
