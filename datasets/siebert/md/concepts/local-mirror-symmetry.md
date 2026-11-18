# 局部镜像对称

> `siebert/concept/local-mirror-symmetry` ｜ track A ｜ draft

**一句话**：大复结构极限附近的局部模型 u₁u₂u₃u₄=z：消失环面 T³、极大单值 N=T−I，以及单值与 Kähler 侧杯积的对应。

**自测**：为什么大复结构极限附近的局部模型足以决定整个镜像映射？

## 定义

在镜像族 $Y_\psi$ 的 $\psi=\infty$（即 $z=(5\psi)^{-5}\to0$）附近，$Y$ 局部由 $u_1u_2u_3u_4=z$ 描述，消失循环 $\beta_0$ 是环面 $T^3=\{|u_1|=\cdots=|u_4|=|z|^{1/4},\ \arg(u_1u_2u_3u_4)=\arg z\}$（1.54–1.55）。取 $H_3(Y,\ZZ)\cong\ZZ^4$ 的辛基 $\beta_0,\beta_1,\alpha_1,\alpha_0$，绕 $z=0$ 的单值算子 $T$ 满足 $N=T-I$：$N\alpha_0=0$、$N\alpha_1=\alpha_0$、$N\beta_1=\alpha_1$、$N\beta_0=\beta_1$（1.86）。

记号：$z=(5\psi)^{-5}$ 是族参数，$z=0$ 为极大退化点（大复结构极限）；$\Omega$ 为全纯三形式；$T$ 单值算子；$N=T-I$；$\varphi_0=\int_{\beta_0}\Omega$ 是归一化周期。

## 要点

- 局部模型：$\CC^4$ 中 $u_1u_2u_3u_4=z$，$z	o0$ 时纤维退化成四个坐标超平面之并、中间 $T^3$ 缩成一点；这是讲义 p.18 用 $zw=t$ 的 Dehn 扭转图景作类比的高维版本。
- 单值是极大的：一阶系统 $	heta\varthetaarphi=A(z)\varthetaarphi$ 中 $A(0)$ 是 $4	imes4$ 幂零 Jordan 块（1.81），故 $N^4=0$、$N^3
e0$，基本解含到 $(\log z)^3$ 的项（1.82–1.85）。
- 单值 ↔ 杯积：$H^3(Y)=\oplus_pH^{p,3-p}$ 上的单值变换，对应 $\oplus_pH^{p,p}(X)$ 上与 $[\omega_X]$ 的杯积（p.23）；Kähler 锥 $K_X=\{[\omega]\in H^2_{dR}:\omega\text{ 为 Kähler}\}$ 控制这一对应的适用范围。
- 典范坐标：$w=\int_{\beta_1}\Omega/\int_{\beta_0}\Omega$、$q=e^{2\pi iw}$，单值变换在 $w$ 上表现为 $w\mapsto w+1$（$q$ 不变），所以 $q$ 级数在 $z=0$ 附近有意义。
- 与 Fourier 变换的关系：讲义全文没有出现『Fourier 变换』。标准说法是 SYZ 图像下 $T^3$ 纤维上的 T-对偶（Fourier–Mukai 型变换）使单值与杯积对齐；讲义只在 p.9 提 SYZ 纤维化，未展开（见本卡 pitfalls）。

## 公式

$$u_1u_2u_3u_4=z,\qquad \beta_0=\{|u_1|=\cdots=|u_4|=|z|^{1/4},\ \arg(u_1\cdots u_4)=\arg z\}$$
$$N\alpha_0=0,\qquad N\alpha_1=\alpha_0,\qquad N\beta_1=\alpha_1,\qquad N\beta_0=\beta_1,\qquad N^4=0$$
$$w=\frac{\int_{\beta_1}\Omega}{\int_{\beta_0}\Omega},\qquad q=e^{2\pi iw},\qquad T:\ w\mapsto w+1$$
$$\Phi(z)=S(z)z^{R},\qquad A(0)\ \text{为幂零 Jordan 块}$$

## 定理与证明

### Thm 1.5：基本解与单值的幂零性

一阶系统 $\theta\varphi=A(z)\varphi$ 在 $z=0$ 附近有基本解矩阵 $\Phi(z)=S(z)z^{R}$，$S\in M(s,\mathcal O_0)$、$R\in M(s,\CC)$ 常数；当 $A(0)$ 的特征值差不是非零整数时 $R=A(0)$。对五次超曲面 $A(0)$ 是幂零 Jordan 块，故单值极大。

（sketch；来源：原书 p.21（Thm 1.5、1.81–1.86））

1. 在 $z=0$ 处把 $A(z)$ 展开，先解常系数方程 $	heta\varthetaarphi=A(0)\varthetaarphi$，其解为 $z^{A(0)}$ 的列。  
   为什么：常系数方程组可以逐项对角化/幂零化，解就是矩阵指数 $z^{A(0)}=\exp(A(0)\log z)$。
2. $A(0)$ 是 $4	imes4$ 幂零 Jordan 块时，$z^{A(0)}=I+(\log z)A(0)+	frac12(\log z)^2A(0)^2+	frac16(\log z)^3A(0)^3$。  
   为什么：幂零性让矩阵指数的 Taylor 级数在 4 次处截断，这正对应 1.82–1.85 的四个基本解。
3. 一般 $A(z)$ 用 $S(z)$ 的幂级数修正，得到 $\Phi=S(z)z^{R}$；单值 $T$ 由 $z\mapsto e^{2\pi i}z$ 给出，故 $N=T-I=\exp(2\pi iR)-I$ 幂零。  
   为什么：$R$ 幂零 ⇒ $\exp(2\pi iR)-I$ 幂零，单值算子的对数就是 $2\pi iR$。

缺口：讲义未写出 $A(0)$ 的显式矩阵，只论证其为幂零 Jordan 块（1.81）并给出四个基本解的形式（1.82–1.85）。

### 局部模型的消失环面

$u_1u_2u_3u_4=z$ 在 $z\ne0$ 时的纤维中包含环面 $T^3=\{|u_i|=|z|^{1/4},\ \arg(\prod u_i)=\arg z\}$，它在 $z\to0$ 时收缩为一点；其像 $\beta_0\in H_3(Y_\psi,\ZZ)$ 是消失循环。

（sketch；来源：原书 p.18（1.53–1.55））

1. 固定 $|u_i|=|z|^{1/4}$，则 $|u_1u_2u_3u_4|=|z|$ 自动成立，只剩相位约束 $\alpharg(u_1u_2u_3u_4)=\alpharg z$ 一个实条件。  
   为什么：四个模长被固定、一个相位条件，$4-1=3$ 个实维数，正是 $T^3$。
2. 这个 $T^3$ 的任意两个圈在 $Y_\psi$ 中都不相交地缩到 $z=0$ 的奇点，故它在 $H_3$ 中的类 $eta_0$ 是消失循环；用 1.55 把它提升到 $X_\psi$ 上得显式环面。  
   为什么：消失循环的定义就是在临界值附近收缩的循环；1.55 给出它在射影模型中的显式方程。

缺口：讲义给的是构造与验证思路，未证明 $eta_0$ 与其余三个循环构成 $H_3$ 的基。

## 易错点

- $u_1u_2u_3u_4=z$ 只是大复结构极限附近的局部描述，不是整族 $Y_\psi$ 的全局方程；用它算出的结论只在 $z=0$ 附近成立。
- $z=0$ 在镜像族里对应 $\psi=\infty$（大复结构极限），不是 Fermat 点；Fermat 点是 $z=\infty$（$\psi=0$），那里多出 $\ZZ/5$ 对称、出现轨形点。
- 讲义没有写 Fourier 变换：把单值变换解释成 Fourier–Mukai/T-对偶是 SYZ 图像下的标准说法，本卡已把它标为『讲义外』，不要当作讲义结论引用。
- $N^4=0$ 不表示单值平凡：极大单值意味着 $N$ 的 Jordan 块最大，$\log$ 项恰好到 $(\log z)^3$；若指标不是全 0，单值会弱一些。
- $\beta_0=T^3$ 是消失循环，不是一般纤维的中间维循环类；把 $H_3(Y,\ZZ)\cong\ZZ^4$ 中的四个基向量都当成消失循环是错的。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §7 全纯三形式，p.18–19（原书 p.18–19）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §10 典范坐标与镜像映射，p.21–23（原书 p.21–23）

关联：`siebert/concept/picard-fuchs-equation`、`siebert/concept/mirror-symmetry`、`siebert/concept/toric-variety`

来源说明：原书 p.18–19（1.53–1.62 局部模型、消失环面、留数构造）、p.21–23（Thm 1.5、1.81–1.90 单值与基本解、1.105 附近单值↔杯积）。nLab 无 local mirror symmetry 条目（试 local+mirror+symmetry、local+Calabi-Yau 均 404）；nLab「mirror symmetry」（last revised 2024-04-01）有 SYZ 讨论。讲义全文无『Fourier 变换』一词，卡中已明确标注该说法为讲义外解释。
