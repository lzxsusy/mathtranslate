# 镜像对称

> `siebert/concept/mirror-symmetry` ｜ track O ｜ draft

**一句话**：一对 Calabi–Yau 流形交换 A 模型与 B 模型的对应：数值形态是 Yukawa 耦合相等，同调形态是 Fukaya 范畴与导出范畴等价。

**自测**：为什么一个流形的曲线计数（A 模型）会等于另一个流形的周期积分（B 模型）？

## 定义

设 $(X,\omega)$ 为紧 Calabi–Yau 流形。Witten 1988 的拓扑扭曲把二维 $N=(2,2)$ 超共形场论分成 A 模型 $A(X)$ 与 B 模型 $B(X)$：$A(X)$ 只依赖辛流形 $(X,\omega)$，$B(X)$ 只依赖复流形 $(X,I)$。镜像对称断言存在另一个 Calabi–Yau 流形 $Y$，使得\n$$A(X)=B(Y),\qquad B(X)=A(Y),$$\n并且在 B 侧 $h^{1,1}$ 与 $h^{2,1}$ 互换（原书 (0.9)，p.8）。$Y$ 称为 $X$ 的镜像。

记号：$A(X)$、$B(X)$ 记两套二维拓扑场论；$\langle\,\rangle_A$、$\langle\,\rangle_B$ 记两侧的三点函数（Yukawa 耦合）；$q=e^{2\pi iw}$ 是 Kähler 侧坐标。

## 要点

- 两种形态：数值镜像指 Yukawa 耦合（更一般地 $F_B$）相等，见 p.7–8、p.17；同调镜像指 $D^b\mathcal F(X)\simeq D^b(Y)$ 的 A∞ 等价，见 p.9 与第 6 章。
- A/B 配对：$A(X)=B(Y)$、$B(X)=A(Y)$；B 侧把 $h^{1,1}$ 与 $h^{2,1}$ 互换，五次超曲面的 Hodge 菱形 $1/101,101/1$ 因此对到镜像的 $101/1,1/101$。
- 为什么需要：A 模型侧曲线计数没有一般位置、模空间维数不对（p.24 的 375 条直线就是警告），B 模型的周期则由 Picard–Fuchs 方程控制、可逐项计算；镜像把难算的一侧换成可算的一侧。
- A 模型的严格数学定义要到 1993 年的 Gromov–Witten 理论才建立；此前 $A(X)$ 只是物理对象，讲义 Warning 0.1 特别提醒这一点。
- 镜像不只是『两个流形配对』：COGP 用它预测了五次超曲面的 $n_3=317206375$，而当时的枚举几何算错了这个数（p.23）。

## 公式

$$A(X)=B(Y),\qquad B(X)=A(Y)$$
$$\langle h,h,h\rangle_A=\langle\partial_w,\partial_w,\partial_w\rangle_B,\qquad q=e^{2\pi iw}$$
$$h^{1,1}(X)=h^{2,1}(Y),\qquad h^{2,1}(X)=h^{1,1}(Y)$$

## 定理与证明

### 数值镜像对称（Yukawa 耦合版本）

设 $X$ 为五次三维超曲面、$Y_z$ 为其镜像族。存在镜像映射 $q=c\,z+O(z^2)$，使得 $X$ 的 A 模型 Yukawa 耦合 $5+\sum_{d>0}N_dd^3q^d$ 等于 $Y_z$ 的 B 模型三点函数 $\int_{Y_z}\widetilde\Omega\wedge\partial_z^3\widetilde\Omega$（在 $w$ 坐标下）。

（sketch；来源：原书 p.17、p.22–23）

1. 把 B 侧三点函数写成 $\int\Omega\wedge\partial_z^3\Omega$ 并归一化 $\widetilde\Omega=\Omega/\varthetaarphi_0$，再用 Picard–Fuchs 方程把它化为只含 $z$ 的有理函数。  
   为什么：$\Omega$ 只定到非零倍数，不归一化则三点函数乘上任意常数，等式无从谈起。
2. 在 $z$ 坐标下展开成 $q=e^{2\pi iw}$ 的幂级数，其中 $w=\int_{eta_1}\Omega/\int_{eta_0}\Omega$ 是镜像映射。  
   为什么：A 侧的 $q$ 是 Kähler 参数，必须通过镜像映射与复结构参数 $z$ 联系起来才能比较。
3. 逐项比较得到 $n_1=2875$、$n_2=609250$、$n_3=317206375$。  
   为什么：这三个数与枚举几何（$n_1,n_2$ 已由 Katz 1986 算出）和后续 GW 计算一致，是该陈述最强的检验。

缺口：讲义 p.17 只给陈述与计算路线，完整证明由 Givental 1996 给出（p.23）；Givental 的证明用的是等变 GW 不变量与量子上同调，不在本讲义范围内。

### A/B 模型的配对

拓扑扭曲后 $A(X)$ 只依赖 $(X,\omega)$，$B(X)$ 只依赖 $(X,I)$；镜像对 $(X,Y)$ 满足 $A(X)=B(Y)$ 且 $B(X)=A(Y)$。

（none；来源：原书 p.8）


缺口：讲义把它作为物理事实/公设陈述（p.8），没有数学证明；这正是第 6 章要用同调镜像把它变成可证命题的原因。

## 易错点

- 讲义 Warning 0.1：$A(X)$ 作为二维拓扑场论算的是 $IIB(X)$ 在某些极限下的量；不要把它当成『$X$ 上所有 Gromov–Witten 不变量』的现成定义。
- $B$ 侧三点函数必须先归一化才有意义：$F_B$ 在 $\Omega\mapsto c\Omega$ 下会平移，讲义 Warning 0.2 用 $\exp(\int_{\alphalpha_1}\Omega/\int_{\alphalpha_0}\Omega)$ 消掉这个模糊。
- 讲义第 9 页把同调镜像写成 $D\,\mathrm{Fuk}(X)=D^b(\mathcal O_Y)$，这是幻灯片式简写：严格版本要取 $H^0(\mathrm{Tw}^\Pi\mathcal F(X))$、系数取 Novikov 域、右边是 $D^b(Y)$（见 6.18）。
- 镜像对不是唯一的：同一个 $X$ 可以有不同的镜像实现（不同退化族/不同紧化），『镜像』是一族而非一个点。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，概览 §1 计数镜像对称，p.7–9（原书 p.7–9（概览 §1））

关联：`siebert/concept/calabi-yau-manifold`、`siebert/concept/homological-mirror-symmetry`、`siebert/concept/yukawa-coupling`

来源说明：原书 p.7–9（定义、A/B 配对、Warning 0.1–0.2、同调镜像的预告）。核过 nLab「mirror symmetry」（last revised 2024-04-01；homological+mirror+symmetry 重定向到该页）；Stacks Project 无镜像对称相关章节。
