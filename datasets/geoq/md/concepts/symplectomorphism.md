# 辛同胚与哈密顿流

> `geoq/concept/symplectomorphism` · 轨道 A · 相空间的辛几何 · 状态 draft

> **先自测**：为什么哈密顿方程的解一定保持辛形式，而保辛的变换又为什么不必是哈密顿流？

## 一句话

满足 $\varphi^*\omega=\omega$ 的微分同胚；哈密顿流是单参数辛同胚群，$f=f(q)$ 时它平移纤维，把 $L_\alpha$ 送到 $L_{\alpha+df}$。

## 定义

若 $(M,\omega)$ 与 $(M',\omega')$ 都是辛流形，则满足 $\varphi^*\omega'=\omega$ 的微分同胚 $\varphi:M\to M'$ 叫辛同胚。当两边是同一辛流形而 $\omega'=\omega$ 时，这些同胚组成群 $\operatorname{Symp}(M,\omega)$。哈密顿向量场 $V_f$ 的流 $\varphi_t$ 叫哈密顿流；命题 5.1.21 与例 5.1.32 表明每个 $\varphi_t$ 都保持 $\omega$。

**记号约定**：$\varphi^*$ 是形式的拉回；$\varphi_t$ 表示 $V_f$ 的流，即 $\frac{d}{dt}\varphi_t(x)=V_f(\varphi_t(x))$、$\varphi_0=\mathrm{id}$；$\mathrm{Symp}(M,\omega)$ 为辛同胚群；$\mathrm{Ham}(M,\omega)$ 为哈密顿向量场全体；$f_{,ij}:=\partial^2f/\partial q^i\partial q^j$。

## 要点

- 辛同胚把辛形式原样拉回，因而保持所有由 $\omega$ 造出的量：泊松括号、哈密顿向量场的对应、刘维尔体积 $\omega^n/n!$，以及「拉格朗日子流形」这一性质。
- 「保辛」是比「保体积」强得多的条件：$\dim\ge4$ 时存在雅可比行列式为 $1$ 却不保 $\omega$ 的微分同胚，两者只在 $2$ 维重合。
- 所有哈密顿流都是辛同胚（例 5.1.32），但并非所有辛同胚都是哈密顿流：环路积分 $\int_C\iota_X\omega$ 一般不为零，$\iota_X\omega$ 闭而不恰当，这类向量场只能局部写成 $V_f$。
- 辛同胚群在哈密顿流的方向上无穷维；$\mathrm{Ham}\subset\mathrm{Symp}$ 的差别由 $H^1(M;\mathbb{R})$ 度量，环面 $T^2$ 上的常向量场平移就是标准反例。
- 在 $T^*X$ 上，$f=f(q)$ 只依赖底流形坐标时 $V_f=\sum_i\partial_{q^i}f\,\partial_{p_i}$ 是纯竖直的，流把每个纤维整体平移 $t\,df$，$q$ 不动——这是「势函数只推动动量」的几何版本。
- 流的存在性依赖完备性：非紧流形上哈密顿向量场的积分曲线可能在有限时间爆破，此时只能谈局部辛同胚。

## 关键公式

$$
$\varphi^*\omega=\omega,\qquad \mathrm{Symp}(M,\omega)=\{\varphi\in\mathrm{Diff}(M)\mid\varphi^*\omega=\omega\}$
$$

$$
$\frac{d}{dt}\Big|_{t=0}\varphi_t^*\omega=\mathcal{L}_{V_f}\omega=0$
$$

$$
$f=f(q):\quad V_f=\sum_i\frac{\partial f}{\partial q^i}\,\frac{\partial}{\partial p_i},\qquad \varphi_t(q,p)=\left(q,\;p+t\,df(q)\right)$
$$

$$
$\varphi_1(L_\alpha)=L_{\alpha+df},\qquad \varphi_1(L_0)=L_{df}$
$$

## 定理与证明

### 命题 5.1.31：辛同胚保持拉格朗日子流形

设 $\varphi:(M,\omega)\to(M',\omega')$ 是辛同胚，$L\subset M$ 是拉格朗日子流形。则 $\varphi(L)\subset M'$ 是 $(M',\omega')$ 的拉格朗日子流形。

**完整证明**

1. $\varphi$ 是微分同胚，故 $\dim\varphi(L)=\dim L=\frac12\dim M=\frac12\dim M'$，半维条件保持。
   - *为什么*：微分同胚保持维数，拉格朗日定义中的维数要求自动传递。
2. 任取 $y=\varphi(x)\in\varphi(L)$ 与 $u,v\in T_y\varphi(L)$，存在 $u'=d\varphi^{-1}u$、$v'=d\varphi^{-1}v\in T_xL$，且 $\omega'_y(u,v)=(\varphi^*\omega')_x(u',v')=\omega_x(u',v')$。
   - *为什么*：把 $\varphi(L)$ 上的切向量拉回 $L$，辛同胚的定义正好把 $\omega'$ 换成 $\omega$。
3. 由 $u',v'\in T_xL$ 与 $\omega|_L=0$ 得 $\omega_x(u',v')=0$，故 $\omega'|_{\varphi(L)}=0$，即 $\varphi(L)$ 拉格朗日。
   - *为什么*：两个条件都验证完毕，结论成立。

来源：ch05a.tex:772-783（原书 p.263，定义 5.1.30 与命题 5.1.31）

### 例 5.1.32：哈密顿流是辛同胚

设 $V_f$ 是 $f$ 的哈密顿向量场，$\varphi_t$ 是它的流（存在处）。则对每个 $t$ 有 $\varphi_t^*\omega=\omega$，即哈密顿流由辛同胚组成；特别地 $\frac{d}{dt}\varphi_t^*\omega=0$。

**完整证明**

1. 对 $t$ 求导：$\frac{d}{dt}(\varphi_t^*\omega)=\varphi_t^*\big(\mathcal{L}_{V_f}\omega\big)$，这里用了流与李导数的关系 $\frac{d}{dt}\varphi_t^*\alpha=\varphi_t^*\mathcal{L}_{V_f}\alpha$。
   - *为什么*：把「随时间变化」化为「沿生成向量场的李导数」，后者已有命题 5.1.21 可用。
2. 由命题 5.1.21，$\mathcal{L}_{V_f}\omega=0$，故 $\frac{d}{dt}(\varphi_t^*\omega)=0$。
   - *为什么*：这是整个论证的核心：哈密顿向量场保辛形式。
3. 常导数为零意味着 $\varphi_t^*\omega$ 与 $t$ 无关；在 $t=0$ 处 $\varphi_0=\mathrm{id}$，值为 $\omega$，故对一切 $t$ 有 $\varphi_t^*\omega=\omega$。
   - *为什么*：初值加上导数为零就唯一确定整条曲线，无需解流方程。

来源：ch05a.tex:785-796（原书 p.263，例 5.1.32）

### 例 5.1.32 续：$f=f(q)$ 时哈密顿流是纤维平移，且 $\varphi_1(L_\alpha)=L_{\alpha+df}$

设 $f=f(q)$ 只依赖底流形坐标，$V_f$ 为哈密顿向量场，$\varphi_t$ 为其流。则 $V_f=\sum_i(\partial f/\partial q^i)\,\partial_{p_i}$，$\varphi_t(q,p)=(q,\,p+t\,df(q))$；对任意闭 $1$-形式 $\alpha$，$\varphi_1(L_\alpha)=L_{\alpha+df}$，特别 $\varphi_1(L_0)=L_{df}$。

**完整证明**

1. 设 $V=\sum_i(a^i\partial_{q^i}+b_i\partial_{p_i})$，则 $\iota_V\omega=\sum_i(b_i\,dq^i-a^i\,dp_i)$；要求它等于 $df=\sum_i(\partial_{q^i}f)\,dq^i$，逐项比较得 $b_i=\partial_{q^i}f$、$a^i=0$。
   - *为什么*：这是解 $\iota_V\omega=df$ 的标准手法：先写出 $\iota_V\omega$ 的坐标式再比对系数。
2. 于是 $V_f=\sum_i(\partial_{q^i}f)\,\partial_{p_i}$ 是纯竖直的；其积分曲线满足 $\dot q^i=0$、$\dot p_i=\partial_{q^i}f(q)$，而 $q$ 为常数时右端是常数，故 $q(t)=q(0)$、$p_i(t)=p_i(0)+t\,\partial_{q^i}f(q)$。
   - *为什么*：常微分方程右端不显含 $t$ 且只依赖常数 $q$，直接积分即可。
3. 因此 $\varphi_t(q,p)=(q,\,p+t\,df(q))$；它在 $T^*X$ 上把纤维 $\pi^{-1}(q)$ 整体平移 $t\,df(q)$，是仿射变换。
   - *为什么*：把第 2 步的结果写成映射，就得到纤维平移的几何图像。
4. 点 $(q,\alpha_q)\in L_\alpha$ 被送到 $(q,\alpha_q+df_q)$，这正是截面 $\alpha+df$ 在 $q$ 处的值，故 $\varphi_1(L_\alpha)=L_{\alpha+df}$；取 $\alpha=0$ 得 $\varphi_1(L_0)=L_{df}$。
   - *为什么*：逐点计算后与 $L_{\alpha+df}$ 的定义逐点比对即得，无需再用拉格朗日性。

来源：ch05a.tex:797-812（原书 p.263）

## 易错点

- 方向别弄反：辛同胚要求 $\varphi^*\omega=\omega$（拉回），不是 $\varphi_*\omega=\omega$ 的随手写法。对微分同胚两者等价（$\varphi_*=(\varphi^{-1})^*$），但对不可逆的映射只能谈拉回，混用会在映射复合时把顺序搞错。
- $\mathrm{Symp}\neq\mathrm{Ham}$：环面 $T^2$ 上取常向量场 $X$，它的平移流保辛，但 $\iota_X\omega$ 是常系数 $1$-形式，沿闭路积分非零，故不恰当，$X$ 不是整体哈密顿向量场。把「保辛」直接当成「某个 $f$ 的哈密顿流」会丢掉 $H^1(M;\mathbb{R})$ 这个障碍。
- 保体积不等于保辛：$\mathbb{R}^4$ 上 $(q^1,q^2,p_1,p_2)\mapsto(q^1,\,q^2+p_1,\,p_1,\,p_2)$ 是行列式为 $1$ 的剪切，却把 $\omega$ 变成 $\omega+dp_2\wedge dp_1\neq\omega$。只在 $2$ 维时两者才一致。
- 非紧流形上哈密顿向量场的流未必对所有 $t$ 存在（如 $V=q^2\partial_q$ 在 $\mathbb{R}$ 上有限时间爆破），此时 $\varphi_t$ 只是局部的，不能无条件当作单参数群。
- 符号约定整套绑定：本书 $\iota_{V_f}\omega=df$ 且 $\omega=\sum dp_i\wedge dq^i$，给出 $V_f=\sum(\partial_{q^i}f\,\partial_{p_i}-\partial_{p_i}f\,\partial_{q^i})$；若改用 $\omega=\sum dq^i\wedge dp_i$，同一 $f$ 的 $V_f$ 整体变号，$\varphi_t(q,p)=(q,p+tdf)$ 也会变成 $(q,p-tdf)$。

## 相关卡

- [哈密顿向量场与泊松括号](../concepts/hamiltonian-vector-field.md)
- [拉格朗日子流形、可投影与相函数](../concepts/lagrangian-submanifold.md)
- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)
- [辛流形（symplectic manifold）](../concepts/symplectic-manifold.md)
- [哈密顿流是辛同胚（$f=\tfrac12q^2$ 与 $f=q^1q^2$）](../examples/hamiltonian-flow-symplectomorphism.md)

## 出处

- §5.1.4 定义 5.1.30、命题 5.1.31、例 5.1.32，p.263（PDF p.264），源码 `ch05a.tex:772-812`
