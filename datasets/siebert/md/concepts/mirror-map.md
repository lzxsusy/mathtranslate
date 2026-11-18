# 镜像映射

> `siebert/concept/mirror-map` ｜ track A ｜ draft

**一句话**：用周期比 $w=\varphi_1/\varphi_0$ 定义 $q=e^{2\pi iw}$，把镜像族的复结构模与五次超曲面的 Kähler 模接起来；$q=cz+O(z^2)$。

**自测**：镜像映射为什么取周期比再取指数，它把哪两边的模空间接了起来？

## 定义

镜像映射是复结构模参数 $z$ 与 Kähler 模的典范坐标 $q$ 之间的解析变换。对镜像五次超曲面，取 $H_3(Y_z,\ZZ)$ 的辛基 $\beta_0,\beta_1,\alpha_1,\alpha_0$，令
$$w=\int_{\beta_1}\Omega^\nu=\frac{\int_{\beta_1}\Omega}{\int_{\beta_0}\Omega}=\frac{\varphi_1}{\varphi_0},\qquad q=e^{2\pi iw}.$$
在 $z=0$（大复结构极限）附近 $q=cz+O(z^2)$，$c\neq0$；$q$ 就是 $X$ 的 Kähler 模的典范坐标，镜像对称断言 $\langle h,h,h\rangle_A(q)=\langle\partial_w,\partial_w,\partial_w\rangle_B(z)$。

记号：$\varphi_0=\int_{\beta_0}\Omega$，$\varphi_1=\int_{\beta_1}\Omega$；$w$：周期比（典范坐标）；$q=e^{2\pi iw}$；$z=(5\psi)^{-5}$；$c_2$：$\psi_1$ 的积分常数。

## 要点

- 为什么取比值：$\Omega$ 只定义到常数倍数，单个周期 $\varphi_i$ 没有不变意义，比值 $w=\varphi_1/\varphi_0$ 才与 $\Omega$ 的标度无关。
- 为什么取指数：$z\to e^{2\pi i}z$ 时 $\log z\to\log z+2\pi i$，故 $w\to w+1$；取 $q=e^{2\pi iw}$ 后 $q$ 单值，这正是单值变换 $T$ 在典范坐标上的作用。
- $q=cz+O(z^2)$：在 $z=0$ 处 $\varphi_1=\varphi_0\log z+\psi_1$，故 $w=\log z+\psi_1/\varphi_0$，$q=z\,e^{2\pi i\psi_1/\varphi_0}=cz(1+\cdots)$；常数 $c$ 由 $\psi_1$ 的积分常数 $c_2$ 决定。
- $q$ 是把 B 侧复结构模空间接到 A 侧 Kähler 模空间的坐标：$\partial_w$ 对应 $e^{2\pi ih}$（原书 §6.2 的物理对应），三点函数在 $q$ 的展开系数就是 GW 数。
- 镜像映射依赖辛基的选取：换基作 $Sp(4,\ZZ)$ 变换，$w$ 随之作分式线性变换；固定大复结构极限处 $q\sim z$ 的规范化消去这个自由度，剩余常数 $c_2$ 最终由 $n_1=2875$ 的匹配固定。

## 公式

$$q=e^{2\pi iw},\qquad w=\frac{\varphi_1}{\varphi_0}=\frac{\int_{\beta_1}\Omega}{\int_{\beta_0}\Omega}$$
$$\varphi_1=\varphi_0\log z+\psi_1(z),\qquad \psi_1(z)=5\sum_{n\ge1}\frac{(5n)!}{(n!)^5}\Bigl(\sum_{j=n+1}^{5n}\frac1j\Bigr)z^n+c_2$$
$$q=z\,e^{2\pi i\psi_1/\varphi_0}=c\,z+O(z^2)$$

## 定理与证明

### 镜像对称的 Yukawa 陈述

$\langle h,h,h\rangle_A(q)=\langle\partial_w,\partial_w,\partial_w\rangle_B(z)$，其中 $q=e^{2\pi iw(z)}$、$w=\varphi_1/\varphi_0$。

（none；来源：原书 p.17、p.21）


缺口：这是镜像对称的中心陈述（原书 (1.52)），讲义没有证明；定量验证见 mirror-map-periods 卡（展开后读出 $n_1,n_2,n_3$）。

## 易错点

- $q\neq z$：$q=cz+O(z^2)$ 只是大复结构极限的近似；把 $q$ 当 $z$ 会把 $n_1=2875$ 算错。
- 不要漏掉 $2\pi i$：$w$ 是周期比，$q$ 才是指数；$q$ 的展开系数与 $w$ 的展开系数差 $(2\pi i)^k$。
- 比值 $\varphi_1/\varphi_0$ 依赖辛基的选取；换基会作 $Sp(4,\ZZ)$ 变换，必须与 A 侧超平面类 $h$ 的选取一致。
- $\psi_1$ 的常数 $c_2$ 使 $q$ 只定义到常数倍；这个常数最终由 A 侧 $n_1=2875$ 的匹配固定，不能随手取 $0$。
- 原书 (1.51) 用归一化的 $\Omega^\nu$ 定义 $w$，故 $w$ 与 $\varphi_1/\varphi_0$ 只差一个常数；本卡的比值写法是等价的，但归一化常数要在算 Yukawa 时追踪。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §6.3 镜像对称，p.17–17（原书 p.17）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §10 典范坐标与镜像映射，p.21–22（原书 p.21–22）

关联：`siebert/deriv/mirror-map-periods`、`siebert/deriv/picard-fuchs-derivation`、`siebert/concept/b-model`

来源说明：原书 p.17（1.51–1.52）与 p.21–22（§10，1.86–1.92）。nLab「mirror symmetry」（2024-04-01）与「Picard-Fuchs equation」（2023-10-15）核过 mirror map 由周期比定义的说法；(1.52) 在本译本中右端为 $\partial_w$，与同段文字一致。
