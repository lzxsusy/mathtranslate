# A 模型（辛侧）

> `siebert/concept/a-model` ｜ track A ｜ draft

**一句话**：拓扑扭曲的辛侧理论，只依赖 $(X,\omega)$；其 Yukawa 耦合 $5+\sum N_dd^3q^d$ 是 $d$ 次有理曲线的 GW 生成函数。

**自测**：A 模型为什么只依赖辛结构，它的 Yukawa 耦合到底在数什么曲线？

## 定义

A 模型指把二维 $\mathcal N=(2,2)$ 非线性 σ 模型沿 $X$ 的辛结构作拓扑扭曲所得的二维拓扑场论 $A(X)$，它只依赖辛流形 $(X,\omega)$，不依赖复结构。数学上它给出 $X$ 的 Gromov–Witten 不变量与量子上同调。对五次超曲面，$H^2(X;\ZZ)=\ZZ\cdot h$（$h$ 为超平面类），三点函数即 Yukawa 耦合
$$\langle h,h,h\rangle_A=5+\sum_{d>0}N_d\,d^3q^d=5+\sum_{d>0}d^3n_d\frac{q^d}{1-q^d}\in\QQ[[q]],$$
其中 $N_d$ 是 $d$ 次有理曲线的 Gromov–Witten 计数（含多重覆盖），$n_d$ 是本原计数，$q=e^{2\pi iw}$ 是 Kähler 模的典范坐标。

记号：$q=e^{2\pi iw}$：Kähler 模的典范坐标（$w$ 为周期比，见 mirror-map 卡）；$N_d$：含多重覆盖的 $d$ 次 GW 计数；$n_d$：$d$ 次本原有理曲线数；$h$：超平面类，$h^3=\int_Xh\wedge h\wedge h=5$。

## 要点

- A 模型只看辛结构：$A(X)$ 的构造只用到 $(X,\omega)$，复结构完全不进入；镜像的 B 模型则只看复结构。这是『辛侧 $\leftrightarrow$ 复结构侧』的由来。
- 拓扑扭曲后的 $A(X)$ 并不等于完整的 SCFT：原书 Warning 0.1 说 $A(X)$ 只计算 $IIB(X)$ 在特定极限下的量；只有假设 $\mathrm{SCFT}_A(X)=\mathrm{SCFT}_B(Y)$ 时才有 $A(X)=B(Y)$（Note 0.1）。
- 常数项 $5=h^3$ 是经典（次数 0）贡献，不是 $d=1$ 的 GW 数；$d=1$ 的贡献是 $n_1=2875$ 条直线。
- $N_d$ 与 $n_d$ 是两套计数：$N_d$ 把多重覆盖各算一次，$n_d$ 只算本原曲线；由 (1.48) 逐项比较得 $N_d=\sum_{k\mid d}k^{-3}n_{d/k}$（如 $N_2=n_2+n_1/8$）。
- 镜像对称把 A 模型的三点函数等同于 B 模型的三点函数：$\langle h,h,h\rangle_A(q)=\langle\partial_w,\partial_w,\partial_w\rangle_B(z)$，$q=e^{2\pi iw(z)}$（见 mirror-map-periods 卡）。

## 公式

$$\langle h,h,h\rangle_A=5+\sum_{d>0}N_d\,d^3q^d=5+\sum_{d>0}d^3n_d\frac{q^d}{1-q^d}\in\QQ[[q]]$$
$$h^3=\int_Xh\wedge h\wedge h=5,\qquad n_1=2875,\quad n_2=609250,\quad n_3=317206375$$

## 定理与证明

### A 模型的 Yukawa 耦合是 GW 生成函数

对光滑五次超曲面 $X\subset\PP^4$，$\langle h,h,h\rangle_A=5+\sum_{d>0}N_dd^3q^d$，其中 $N_d$ 是 $d$ 次有理曲线的 GW 计数；用本原计数 $n_d$ 重写即 (1.48)。

（sketch；来源：原书 p.17）

1. $H^2(X;\ZZ)=\ZZ\cdot h$，故三次插入只有 $h$ 一种取法，Yukawa 耦合被一个数完全决定。  
   为什么：弱 Lefschetz 给 $H^2(\PP^4)\cong H^2(X)$，秩为 1；三重对称形式在秩 1 空间上只有一个分量。
2. $d$ 次曲线的贡献为 $d^3N_dq^d$：三个插入点各约束曲线经过一个超平面，三次约束把三个标记点固定，剩下 $d^3$ 个自由度。  
   为什么：$\overline M_{0,3}(X,d)$ 的虚拟维数为 $d$；三个点条件 cutting down $3$ 维，余下 $d^3$ 来自 $\PP^1$ 的 $3$ 维自同构群在 degree-$d$ 映射上的作用。
3. 把多重覆盖按本原次数重排：$\sum_dN_dd^3q^d=\sum_dn_dd^3q^d/(1-q^d)$。  
   为什么：$k$ 重覆盖的 $d$ 次曲线对应本原次数 $d/k$，其 $q$ 幂为 $(q^{d/k})^k$，对 $k$ 求和即几何级数 $q^d/(1-q^d)$。

缺口：$N_d$ 的严格定义（稳定映射模空间、虚拟基本类）在第 3 章；本卡只引用原书 §6.1 的陈述与数值。

## 易错点

- 把 $A(X)$ 当成完整的 $\mathrm{SCFT}_A(X)$：拓扑扭曲只保留一个子代数，$A(X)$ 只计算 $IIB(X)$ 的某些极限量。
- 把 $5$ 当成 $d=1$ 的 GW 不变量：$5$ 是经典项 $h^3$，$n_1=2875$ 才是直线数。
- $N_d\neq n_d$：$N_1=n_1$，但 $N_2=n_2+n_1/8$、$N_3=n_3+n_1/27$；$1/k^3$ 因子来自 $k$ 重覆盖，不能逐项等同。
- $q$ 不是 $z$：A 模型的展开变量是 $q=e^{2\pi iw}$，$z$ 是镜像族的复结构参数；把两者混同会得到错误的系数。
- $H^2(X)$ 秩为 1 只对五次超曲面（$h^{1,1}=1$）成立；不要把这个简化推广到一般 Calabi–Yau 三维流形。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，概览，p.8–9（原书 p.8–9）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §6.1 A 模型，p.17–17（原书 p.17）

关联：`siebert/concept/b-model`、`siebert/concept/yukawa-coupling`、`siebert/concept/mirror-map`

来源说明：原书 p.8–9（概览：A/B 模型的定义、Warning 0.1、Note 0.1）与 p.17（§6.1，1.47–1.48）。nLab「Yukawa coupling」（2026-05-25）与「mirror symmetry」（2024-04-01）核过相关表述；GW 不变量的严格定义未在 nLab 逐条核对。
