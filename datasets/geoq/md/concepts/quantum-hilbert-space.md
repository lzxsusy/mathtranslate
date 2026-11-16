# 量子希尔伯特空间与半形式修正

> `geoq/concept/quantum-hilbert-space` · 轨道 D · 几何量子化机器 · 状态 draft

> **先自测**：预量子化的截面空间为什么太大，加了极化条件之后为什么还要用 √K_M 再修一次？

## 一句话

在预量子化截面上再要求沿极化方向平行，得到只依赖一半变量的量子希尔伯特空间；紧流形的凯勒情形下它有限维，再把线丛换成张上半形式丛，谐振子谱就从 nℏ 抬成 (n+½)ℏ。

## 定义

设 $(\mathcal{L},\nabla)$ 是 $(M,\omega)$ 上的预量子化线丛，$P\subset T^{\mathbb{C}}M$ 是极化。与这一对数据相伴的量子希尔伯特空间取为 $L^2(M,\mathcal{L})_P=\{s\in L^2(M,\mathcal{L})\mid \nabla_Xs=0,\ \forall X\in\Gamma(P)\}$，内积仍用 $\langle s_1|s_2\rangle=\int_M\langle s_1,s_2\rangle\,\frac{\omega^n}{n!}$。半形式修正（half-form correction）把线丛 $\mathcal{L}$ 换成 $\mathcal{L}\otimes\sqrt{K_M}$，其中 $K_M=\Lambda^nT^{*(1,0)}M$ 是典范线丛（canonical bundle），$\sqrt{K_M}$ 是它的平方根丛，量子态取 $\mathcal{L}\otimes\sqrt{K_M}$ 的 $P$-极化截面。

**记号约定**：$K_M$ 的截面就是 $(n,0)$-形式，故 $\sqrt{K_M}$ 的截面称半形式（half-form）；平方根丛存在要求 $c_1(K_M)$ 是偶的整上同调类。$\operatorname{vol}_\omega(M)=\int_M\frac{\omega^n}{n!}$ 是刘维尔体积。$H^0(M,\mathcal{L})$ 记 $\mathcal{L}$ 的全纯截面空间。

## 要点

- $L^2(M,\mathcal{L})$ 的截面依赖全部 $2n$ 个相空间变量，而波函数只应依赖 $n$ 个；极化条件把沿 $P$ 的 $n$ 个方向压成常量，这一步不损失任何信息，只是选定了表象。
- 实极化下得到位置波函数或动量波函数：竖直极化 $P=\operatorname{Span}{\partial_{p_i}\}$ 给 $f(\mathbf x)$，水平极化 $P'=\operatorname{Span}{\partial_{x^i}\}$ 给 $e^{\frac{i}{\hbar}\mathbf x\cdot\mathbf p}g(\mathbf p)$。
- 凯勒极化下量子态是全纯截面；取 $K=|\mathbf z|^2$ 恰好回到 Segal–Bargmann 空间，这是同一套机器在复欧氏空间上的落地。
- 紧复流形上全纯截面空间 $H^0(M,\mathcal{L})$ 有限维；把 $\mathcal{L}$ 换成 $k$ 次张量幂并认同 $\hbar=\frac{1}{2\pi k}$，维数按 $k^n\operatorname{vol}_\omega(M)$ 增长，即 $\operatorname{vol}_\omega(M)/(2\pi\hbar)^n$：相空间体积除以格子体积。
- 半形式修正补的是马斯洛夫相位：态从 $\mathcal{L}$ 的截面换成 $\mathcal{L}\otimes\sqrt{K_M}$ 的截面后，每个自由度多出 $\frac12\hbar$ 的零点能，$n\hbar$ 变成 $(n+\frac12)\hbar$。

## 关键公式

$$
$L^2(M,\mathcal{L})_P=\{s\in L^2(M,\mathcal{L})\mid \nabla_Xs=0,\ \forall X\in\Gamma(P)\}$
$$

$$
$\langle s_1|s_2\rangle=\int_M\langle s_1,s_2\rangle\,\frac{\omega^n}{n!}$
$$

$$
$\mathbb{H}=H^0(M,\mathcal{L})\qquad(M\ \text{紧，凯勒极化})$
$$

$$
$\dim H^0(M,\mathcal{L})\sim\frac{1}{(2\pi\hbar)^n}\operatorname{vol}_\omega(M)$
$$

$$
$Q(\mathscr{H})\,z^n\sqrt{dz}=(n+\frac12)\hbar\,z^n\sqrt{dz}$
$$

## 定理与证明

### 两种极化下的截面刻画

在 $\mathbb{R}^{2n}$ 上取 $\omega=\sum_idp_i\wedge dx^i$、$\theta=\sum_ip_idx^i$、$\nabla=d-\frac{i}{\hbar}\theta$。对竖直极化 $P=\operatorname{Span}{\partial_{p_i}\}$，$P$-极化截面恰为与 $\mathbf p$ 无关的函数 $f(\mathbf x)$；对水平极化 $P'=\operatorname{Span}{\partial_{x^i}\}$，$P'$-极化截面恰为 $f=e^{\frac{i}{\hbar}\mathbf x\cdot\mathbf p}g(\mathbf p)$。

**完整证明**

1. 先算 $\theta(\partial_{p_i})=\sum_jp_jdx^j(\partial_{p_i})=0$，于是 $\nabla_{\partial_{p_i}}f=\partial_{p_i}f-\frac{i}{\hbar}\theta(\partial_{p_i})f=\partial_{p_i}f$。
   - *为什么*：刘维尔形式只含 $dx^j$，与 $p$ 方向缩并为零；竖直极化的协变导数退化成普通偏导。
2. 要求 $\partial_{p_i}f=0$ 对一切 $i$ 成立，等价于 $f$ 不依赖 $\mathbf p$，即 $f=f(\mathbf x)$。
   - *为什么*：这是偏导数为零的直接推论，也说明「竖直极化 = 位置表象」。
3. 再算 $\theta(\partial_{x^i})=p_i$，故 $\nabla_{\partial_{x^i}}f=\partial_{x^i}f-\frac{i}{\hbar}p_if$；置零得 $\partial_{x^i}f=\frac{i}{\hbar}p_if$。
   - *为什么*：水平极化的方向与 $\theta$ 配对非零，方程比竖直情形多一个乘法项。
4. 固定 $\mathbf p$ 对 $x$ 积分得 $f=e^{\frac{i}{\hbar}\mathbf x\cdot\mathbf p}g(\mathbf p)$，代回可逐项验证。
   - *为什么*：右端是 $f$ 的倍数，指数化是唯一解；$g$ 是积分常数，充当动量表象的波函数。

来源：ch05b.tex:1077-1123（原书 p.289）

### 半形式修正把 nℏ 抬成 (n+½)ℏ

在 $\mathbb{C}$ 上取 $\omega=i\partial\bar\partial K$、$K=|z|^2$、凯勒极化 $P=\operatorname{Span}{\partial_{\bar z}\}$、谐振子 $\mathscr{H}=|z|^2$。未修正时预量子化算子 $Q(\mathscr{H})=\hbar z\partial_z$ 在全纯截面 $z^n$ 上的本征值为 $n\hbar$；把量子态改为 $\mathcal{L}\otimes\sqrt{K_M}$ 的截面后，同一个算子在 $z^n\sqrt{dz}$ 上的本征值为 $(n+\frac12)\hbar$。

**完整证明**

1. 未修正的谱：把 $K=|z|^2$、$g_{j\bar m}=i\delta_{jm}$、$g^{\bar mj}=-i\delta^{mj}$ 代入哈密顿场与预量子化公式，得 $Q(\mathscr{H})=\hbar z\partial_z$，作用在 $z^n$ 上给 $n\hbar$。
   - *为什么*：这是例 5.4.15 的直接结论；$z\partial_z$ 在单项式基上对角，所以本征值读数一目了然。
2. 修正后的态空间是 $\mathcal{L}\otimes\sqrt{K_M}$ 的 $P$-极化截面，$K_M$ 在这里由 $dz$ 平凡化，通解写成 $z^n\sqrt{dz}$。
   - *为什么*：半形式丛是与 $\mathcal{L}$ 张量相乘的独立因子，换态空间就必须连带换算子的作用方式。
3. 半形式带 ½ 权重：在 $z\mapsto\lambda z$ 下 $dz\mapsto\lambda dz$，故 $\sqrt{dz}\mapsto\lambda^{1/2}\sqrt{dz}$，即 $z\partial_z\sqrt{dz}=\frac12\sqrt{dz}$。于是 $z\partial_z(z^n\sqrt{dz})=(n+\frac12)z^n\sqrt{dz}$。
   - *为什么*：½ 来自开平方，这正是马斯洛夫相位在几何量子化里的化身；它与 $n$ 无关，只整体平移谱。
4. 两边乘 $\hbar$ 得 $Q(\mathscr{H})(z^n\sqrt{dz})=(n+\frac12)\hbar\,z^n\sqrt{dz}$；$n=0$ 时给出零点能 $\frac12\hbar$。
   - *为什么*：结论与薛定谔算子 $\frac12(p^2+q^2)$ 的已知谱一致，修正的正确性由此得到独立印证。

来源：ch05b.tex:1441-1465（原书 p.295–296）；配合 ch05b.tex:1412-1439（原书 p.295）

## 易错点

- $\sqrt{K_M}$ 不一定存在：要求 $c_1(K_M)$ 为偶数。$\mathbb{C}P^1$ 上 $K_M=\mathcal{O}(-2)$ 可以开方，$\mathbb{C}P^n$ 上 $K_M=\mathcal{O}(-(n+1))$ 只有当 $n$ 为奇数时才行；否则只能改用 $\mathrm{spin}^c$ 结构或放弃半形式。
- 「把 $z^n$ 乘上 $\sqrt{dz}$」不是给波函数乘一个函数：态空间从 $\mathcal{L}$ 换成了 $\mathcal{L}\otimes\sqrt{K_M}$，内积与算子的作用同时改变。若只做形式替换而不让算子对半形式因子求导，谱仍是 $n\hbar$，修正凭空消失。
- 维数渐近式 $\dim H^0\sim\operatorname{vol}/(2\pi\hbar)^n$ 的前提是 $\hbar=\frac{1}{2\pi k}$、$k\to\infty$、$\mathcal{L}_0$ 为正线丛（此时 $i>0$ 的上同调才消失）；对固定的 $\hbar$，$\dim H^0$ 并不等于这个数。

## 相关卡

- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [预量子化线丛](../concepts/prequantization.md)
- [量子算子与 P-保持条件](../concepts/quantum-operator.md)
- [马斯洛夫修正与 EBK 条件](../concepts/maslov-correction.md)
- [Segal–Bargmann 空间](../concepts/segal-bargmann-space.md)
- [凯勒极化、半形式与 $(n+\frac12)\hbar$ 谱](../examples/oscillator-half-form-spectrum.md)
- [线丛张量幂与 $\hbar$ 的重新标定](../examples/tensor-power-line-bundle.md)

## 出处

- §5.4.4 量子希尔伯特空间的定义，p.288–289（PDF p.289–290），源码 `ch05b.tex:1047-1075`
- §5.4.4 例 5.4.8–5.4.11：实极化、凯勒极化与张量幂，p.289–292（PDF p.290–293），源码 `ch05b.tex:1077-1265`
- §5.4.5 半形式修正与谐振子谱，p.295–296（PDF p.296–297），源码 `ch05b.tex:1441-1465`
