# 关键段落精译

[p.008] 本文一开始就把规范群取成复 Lie 群 $G$（例如 $SL(2,\mathbb{C})$），$A$ 是三维流形 $M$ 上 $G$-丛的联络。这样的联络有一个复值的 Chern–Simons 不变量
$$W(A)=\frac{1}{4\pi}\int_M\operatorname{Tr}\Bigl(A\wedge dA+\frac{2}{3}A\wedge A\wedge A\Bigr),$$
归一化使它只在规范变换下差 $2\pi$ 的整数倍。要紧的是：$W$ 的虚部其实是良定义的实数，而实部取值在 $\mathbb{R}/2\pi\mathbb{Z}$ 中。为了得到量子理论，我们从一个经典作用量 $I$ 出发，它是 $\operatorname{Re}W$ 与 $\operatorname{Im}W$ 的线性组合；因为 $e^{iI}$ 必须良定义，$\operatorname{Re}W$ 的系数必须是整数，而 $\operatorname{Im}W$ 的系数可以是任意复数。于是作用量的一般形式是 $I=-s\operatorname{Im}W+\ell\operatorname{Re}W$，其中 $s\in\mathbb{C}$、$\ell\in\mathbb{Z}$；等价地可写成 $I=\frac t2W(A)+\frac{\tilde t}2W(\tilde A)$，$t=\ell+is$、$\tilde t=\ell-is$。当 $s$ 为实数时，$I$ 为实、被积函数有界，路径积分才有通常的振荡积分意义；$s$ 非实时必须另想办法，这正是全文要处理的问题。

[p.011] 在无穷维路径积分里寻找合适的积分 cycle，乍看无从下手；救场的是 Morse 理论与最速下降——换个说法，就是 Picard–Lefschetz 理论。它的基本想法是：把候选的积分 cycle 与扩张作用量 $I(A,\tilde A)$ 的临界点集的分支联系起来。对本文而言，这套形式之所以可用，是因为临界点是可以显式描述的：只要 $t$、$\tilde t$ 都不为零，临界点方程就是 $F=\tilde F=0$，即两个联络都平坦；于是临界点不过是一对平坦联络，也就是基本群 $\pi_1(M)$ 到复 Lie 群 $G$ 的一对同态。对每个临界点 $p_\sigma$，取从它出发沿 $\operatorname{Re}I$ 向下流的积分 cycle $J_\sigma$，即 Lefschetz 顶针；任何一个合适的积分 cycle $C$ 都等价于这些顶针的整系数线性组合 $C=\sum_\sigma n_\sigma J_\sigma$，而系数可由 $C$ 与向上流 cycle $K_\sigma$ 的相交配对给出：$n_\sigma=\langle C,K_\sigma\rangle$。

[p.066] 把 $A$ 拉回到 $I\times M$ 上，并把 $A$ 在时间方向的分量取为零当作规范条件，就可以用曲率分量 $F_{ti}$ 代替 $dA_i/dt$；同样把 $\varphi$ 看成 $I\times M$ 上的 $ad(E)$ 值 1-形式，其时间分量 $\varphi_t$ 取为零。给 $I\times M$ 配上度规 $dt^2+g$，用四维 Hodge 星算子，取 (4.7) 的线性组合，就发现这些方程可以写成具有四维对称性的形式
$$(F-\varphi\wedge\varphi)_+=uD\varphi_+,\qquad (F-\varphi\wedge\varphi)_-=-u^{-1}D\varphi_-,$$
其中 $u=\frac{1-\cos\alpha}{\sin\alpha}$、$u^{-1}=\frac{1+\cos\alpha}{\sin\alpha}$，而 $v_\pm=\frac12(v\pm\star v)$。严格说，四维对称性在我们这里被 $\varphi_t=0$ 这个条件破坏；但只要放松这个条件，方程就有完整的四维对称性。矩映射 $\mu=d_A\star_M\varphi$ 照例是流方程的守恒量；我们主要关心 $\mu=0$ 的解，于是在 (4.8) 之外再加条件 $d_A\star\varphi=0$。此后所说的「流方程」都指这个椭圆方程组。

[p.118] 对八字结，体积猜想来自这样一个观察：当 $\gamma$ 从离开实轴的方向趋于 $1$ 时，$J_n(q)$ 的大 $n$ 行为粗略地是 $J_n(q)\sim\exp(nV/2\pi)$，其中 $V$ 是纽结补的双曲体积。部分的解释是：$nV/2\pi$ 正是解析延拓后的 Chern–Simons 路径积分指数 $I=ikW(A)$ 在复临界点 $A_+$ 处的值，所以围绕 $A_+$ 展开就会给出按 $\exp(V/2\pi)$ 增长的贡献。可这里一直有个困惑：对物理值（正整数 $k,n$），半经典极限由实临界点主导，复临界点的贡献（如果有）是指数小的；那么为什么只要 $\gamma$ 离 $1$ 一点点，就能看到指数增长？答案在于：一旦离开整数 $k$，我们就不该在复值联络模空间 $\mathcal{U}_\mathbb{C}$ 上工作，而要在使 $W(A)$ 取复值的覆盖 $\widehat{\mathcal{U}}_\mathbb{C}$ 上工作。一个给定的平坦联络对应无穷多个临界点，它们只差 $W(A)$ 的复提升；当积分 cycle 按这些顶针展开时，只差提升的贡献在整数 $k$ 时可以相消，而 $k$ 一旦不是整数，就会给出指数增长。把这条机制落实到八字结，就得到 $J_n\sim\exp(nV/2\pi)\bigl(e^{-i\pi k}-e^{i\pi k}\bigr)$：两个只差提升的顶针带相反符号，正是整数 $k$ 时相消、非整数时增长的原因。
