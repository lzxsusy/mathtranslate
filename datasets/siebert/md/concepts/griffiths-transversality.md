# Griffiths 横截性

> `siebert/concept/griffiths-transversality` ｜ track A ｜ draft

**一句话**：Gauss–Manin 联络把 Hodge 滤过恰好降一阶：$\nabla F^k\subseteq F^{k-1}\otimes\Omega^1$；由此 $W_0=W_1=W_2=0$，$W_4=2W_3'$。

**自测**：为什么沿模空间求导只会把 Hodge 滤过降低一阶，这个事实又怎样把四阶 Picard–Fuchs 方程降成一阶？

## 定义

设 $\pi:\mathcal Y\to M$ 是 Calabi–Yau 流形族，$F^k=\bigoplus_{p\ge k}H^{p,n-p}\subset H^n$ 是 Hodge 滤过。Gauss–Manin 联络 $\nabla^{GM}$ 满足 Griffiths 横截性
$$\nabla^{GM}F^k\subseteq F^{k-1}\otimes\Omega^1_M,$$
即沿模空间求导恰好把 Hodge 滤过降一阶。等价地，若 $\Omega$ 是全纯 $n$ 形式（$\Omega\in F^n$），则 $\partial_z^k\Omega\in F^{n-k}$。

记号：$F^k$：Hodge 滤过；$\nabla^{GM}$：Gauss–Manin 联络；$\Omega$：全纯 $n$ 形式；$W_k=\int\Omega\wedge\partial_z^k\Omega$；$c_k$：PF 方程在 $d/dz$ 形式下首项归一化后的系数。

## 要点

- 横截性的内容：$F^k$ 不是平坦子丛，求导不保持 $F^k$，而是恰好降一阶到 $F^{k-1}$；这比『$F^k$ 全纯』强，也是滤过『非分裂』的精确表述。
- 对 $n=3$：$\Omega\in F^3$，$\partial\Omega\in F^2$，$\partial^2\Omega\in F^1$，$\partial^3\Omega\in F^0=H^3$；$\partial^4\Omega$ 仍在 $F^0$ 中，故 $\Omega,\ldots,\partial^4\Omega$ 这 5 个截面落在 4 维空间里，必线性相关——这是 PF 方程四阶的来源。
- 类型配对：$\int_Y\alpha\wedge\beta\neq0$ 只当 $\alpha\wedge\beta$ 为 $(3,3)$ 型，即 $\alpha\in H^{p,q},\beta\in H^{p',q'}$ 需 $p+p'=3=q+q'$；这给出 $W_0=W_1=W_2=0$。
- 由 $0=d^2W_2/dz^2=2W_3'-W_4$ 得 $W_4=2W_3'$；与 PF 的 $W_4+\sum c_kW_k=0$ 联立，得到 $W_3'+\frac12c_3W_3=0$。
- $c_3(z)=6/z-2\cdot5^5/(1-5^5z)$ 可由 PF 算子按 $d/dz$ 展开、以 $d^4$ 系数归一化后读出；积分给出 $W_3\propto1/(z^3(5^5z-1))$（1.101）。

## 公式

$$\nabla^{GM}F^k\subseteq F^{k-1}\otimes\Omega^1_M$$
$$W_k=\int_Y\Omega\wedge\partial_z^k\Omega:\qquad W_0=W_1=W_2=0,\qquad W_4=2W_3'$$
$$W_3'+\frac12c_3W_3=0,\qquad c_3(z)=\frac6z-\frac{2\cdot5^5}{1-5^5z}$$

## 定理与证明

### Griffiths 横截性给出 $W_0=W_1=W_2=0$

设 $\Omega$ 为 Calabi–Yau 三维流形族的全纯三形式，$W_k=\int_Y\Omega\wedge\partial_z^k\Omega$。则 $W_0=W_1=W_2=0$，且 $W_4=2W_3'$。

（sketch；来源：原书 p.22–23）

1. $\Omega\in F^3$，且 $\partial_z^k\Omega\in F^{3-k}$（对 $k$ 归纳使用 $\nabla F^j\subseteq F^{j-1}\otimes\Omega^1$）。  
   为什么：每求导一次用一次横截性；这是整个论证的唯一输入。
2. $\Omega\wedge\partial_z^k\Omega$ 的类型为 $(3+p,3-p)$，其中 $p\ge3-k$；$k<3$ 时 $p>0$，总类型不是 $(3,3)$。  
   为什么：$\Omega$ 是 $(3,0)$ 型，$\partial_z^k\Omega\in F^{3-k}=\bigoplus_{p\ge3-k}H^{p,3-p}$；逐项相乘即得类型。
3. 由类型配对，$k<3$ 时 $\int_Y\Omega\wedge\partial_z^k\Omega=0$，即 $W_0=W_1=W_2=0$。  
   为什么：紧 Kähler 流形上 $(6,0)$、$(5,1)$ 等类型的全纯形式不存在，积分只取 $(3,3)$ 分量。
4. $k=3$ 时 $\partial^3\Omega$ 含 $H^{0,3}$ 分量，$\Omega\wedge$ 之得 $(3,3)$，故 $W_3$ 可非零；又 $0=d^2W_2/dz^2=\cdots=2W_3'-W_4$，故 $W_4=2W_3'$。  
   为什么：两次求导的边界项给出恒等式，配合 $W_2=0$ 消去中间项；这正是把 PF 的四阶方程降为一阶的关键。

缺口：讲义未逐项展开 $c_3$ 的计算；本卡只记录 (1.100)，并用符号计算复核过：把 (1.76) 按 $d/dz$ 展开、以 $d^4$ 系数归一化，$d^3$ 系数确为 $6/z-2\cdot5^5/(1-5^5z)$。

## 易错点

- 横截性不是『$F^k$ 是平坦或全纯子丛』：$\nabla$ 不保持 $F^k$，只把它送进 $F^{k-1}$；把滤过当直和分解会丢掉 $\partial$ 的幂零部分。
- $W_k$ 用的是未归一化的 $\Omega$；若换成 $\Omega^\nu=\Omega/\varphi_0$，$W_k$ 的定义与 ODE 都要重算（见 b-model 卡）。
- $W_0=W_1=W_2=0$ 是类型配对的严格结果，不表示这些积分『数值很小』；它们恒为零。
- $c_3$ 是 PF 方程在 $d/dz$ 形式下 $d^3$ 的系数（首项归一化后），不是 $\theta$ 形式下的系数；两者差 $z$ 的幂。
- $W_4=2W_3'$ 只在 $n=3$ 且 $W_2=0$ 时成立；不要把它当作所有维数的通用恒等式。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §11.1 Griffiths 横截性，p.22–23（原书 p.22–23）

关联：`siebert/concept/b-model`、`siebert/deriv/picard-fuchs-derivation`、`siebert/deriv/mirror-map-periods`

来源说明：原书 p.22–23（1.95–1.101：Hodge 滤过、横截性、$W_k$ 的消没与 $W_3$ 的 ODE）。nLab 没有 Griffiths transversality 条目（slug 404）；按 nLab「Hodge theory」（2023-10-18）的滤过表述与原著核对。$c_3$ 的系数用 sympy 1.14.0 对 (1.76) 作 $d/dz$ 展开复核。
