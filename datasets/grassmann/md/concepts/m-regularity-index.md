# $M$-正则性指标 $m(L)$

> `grassmann/concept/m-regularity-index` · 轨道 8 · 阿贝尔簇上的正则性 · 状态 draft

> **先自测**：一个线丛要在点处被扭多少阶之后才失去 $M$-正则性，这个临界阶数凭什么和 Seshadri 常数挂钩？

## 一句话

把线丛沿点幂零理想扭到最狠仍保持 $M$-正则性的临界阶数记为 $m(L)$；它与 Seshadri 常数只差渐近缩放，因而给出用正则性控制正性的定量工具。

## 定义

设 $(X,\Theta)$ 是极化阿贝尔簇、$L$ 是 $X$ 上的线丛。记 $$m(L):=\max\Bigl\{l\ \Big|\ L\otimes\mathfrak m_{x_1}^{k_1}\otimes\cdots\otimes\mathfrak m_{x_p}^{k_p}\ \text{对一切互异的 }x_i\in X\text{ 与一切 }k_i\ge0,\ \sum k_i=l\ \text{都是 }M\text{-正则的}\Bigr\},$$ $$p(L,x):=\max\{l\mid L\otimes\mathfrak m_x^l\ \text{是 }M\text{-正则的}\},\qquad \rho(L):=\sup_n\frac{m(L^n)}{n},\qquad \rho'(L):=\sup_n\frac{p(L^n)}{n}.$$ 定理 7.4 断言 $\varepsilon(L)=\rho'(L)\ge\rho(L)\ge1$，特别地 $\varepsilon(L)\ge\max\{m(L),1\}$。

**记号约定**：$\mathfrak m_x$ 是点 $x$ 的极大理想；$L\otimes\mathfrak m_x^k$ 表示把 $L$ 在 $x$ 的 $k$ 阶无穷小邻域上扭一次；$\varepsilon(L)$ 是 Seshadri 常数；$k$-射流充裕（定义 7.6）= 对任意互异点组与 $\sum k_i=k+1$，$H^0(L)\to H^0(L\otimes\mathcal O/\mathfrak m_{x_1}^{k_1}\otimes\cdots)$ 满射。

## 要点（为什么需要它）

- 量词顺序是关键：先固定 $l$，再要求『对一切互异点组、一切 $k_i\ge0$ 且 $\sum k_i=l$』都正则；故 $m(L)$ 越大条件越强，它记录最坏点与最坏分配，而不是某组点。
- $m$ 沿幂次近似线性：$m(L^n)\ge m(L)+n-1$（式 14），于是 $\rho(L)\ge1$；与 $p(L)\ge m(L)$ 合成定理 7.4 的前半 $\rho'\ge\rho\ge1$。
- 后半靠引理 7.8：$L^{n+1}$ 在 $x$ 处的射流充裕阶满足 $s(L^{n+1},x)\ge m(L^n)$，逐点取 $\sup$ 再与式 14 夹逼，得 $\varepsilon(L)=\rho'(L)$。
- 推论 7.11/7.12 是定量版：主极化 Jacobian 上 $m(n\Theta)\le\sqrt g\,n$，任意阿贝尔簇上 $m(n\Theta)\le(g!)^{1/g}n$。
- 问题 7.10 问是否总有 $\varepsilon(L)=\rho(L)$（而非只 $\ge$），本章只证了 $\ge$，这一格是公开的空白。

## 关键公式

$$
m(L):=\max\{l\mid \operatorname{codim}V^i(L\otimes\mathfrak m_{x_1}^{k_1}\otimes\cdots)>i\ \ (\forall i>0,\ \forall x_i,\ \textstyle\sum k_i=l)\}
$$

$$
\varepsilon(L)=\rho'(L)\ge\rho(L)\ge1,\qquad \varepsilon(L)\ge\max\{m(L),1\}
$$

$$
m(L^n)\ge m(L)+n-1
$$

## 定理与证明（或缺口）

### 定理 7.4（$M$-正则性指标与 Seshadri 常数）

对极化阿贝尔簇 $(X,\Theta)$ 上的线丛 $L$ 有 $\varepsilon(L)=\rho'(L)\ge\rho(L)\ge1$，特别地 $\varepsilon(L)\ge\max\{m(L),1\}$。

**证明状态：完整**

1. 命题 7.7：(i) $L^n$ 是 $(n+m(L)-2)$-射流充裕的；(ii) $k$-射流充裕蕴含 $m(L)\ge k+1$。两式合成 $m(L^n)\ge m(L)+n-1$（式 14）。
   - *为什么*：把『扭到某阶仍正则』翻译成『射流充裕阶』，再沿 $n$ 代数累加。
2. 由 $\sup_n\frac{m(L)+n-1}{n}=1$ 得 $\rho(L)\ge1$；又因单点是点组的特例，$p(L)\ge m(L)$，故 $\rho'(L)\ge\rho(L)$。
   - *为什么*：两个 $\sup$ 只差把点组换成单点，逐项比较即得。
3. 引理 7.8 给 $s(L^{n+1},x)\ge m(L^n)$，与式 14 合起来得 $\limsup_n\frac{s(L^n,x)}{n}\ge\rho(L)$；而 Seshadri 常数的射流刻画是 $\varepsilon(L)=\sup_n\frac{s(L^n,x)}{n}$（$x$ 处取 $\sup$ 后与 $x$ 无关），故 $\varepsilon(L)\ge\rho(L)$，对逐点版 $p$ 再取 $\sup$ 得 $\varepsilon(L)=\rho'(L)$。
   - *为什么*：两个方向的不等式合起来夹出等号；$\varepsilon$ 与 $x$ 无关来自极化阿贝尔簇的齐性。


出处：中译 p.147–148，定义 7.1–7.3 与定理 7.4（chapters/ch08.tex:488）

## 易错点

- 中译省掉了『所有非负整数 $k_i$』这半句，容易被读成『存在某组 $k_i$ 使层正则』；照后者读，$m(L)$ 变成最优情形指标，与定理 7.4 的方向正好相反。
- 引理 7.8 与定义 7.6 差一：定义 7.6 的 $k$-射流充裕要求 $\sum k_i=k+1$，故引理 7.8 的『$l$-射流充裕』严格说只给 $s\ge l-1$。这可能是 [PP2] 的约定不同；渐近化后 $\sup$ 相同，定理 7.4 不受影响，但推论 7.11/7.12 的常数可能差 1。
- 别把 $m(L)$ 直接当成 Seshadri 常数：定理 7.4 只给 $\varepsilon(L)\ge m(L)$，反向不等号正是问题 7.10 的内容，本章没有证。

## 相关卡

- [$M$-正则层](../concepts/m-regular-sheaf.md)
- [$m$-$\Theta$-正则性](../concepts/m-theta-regular.md)
- [$GV$-层](../concepts/gv-sheaf.md)

## 出处

- ch8 §7.1 $M$-正则性指标与 Seshadri 常数；中译 p.147（英文 PDF p.164），源码 `chapters/ch08.tex:488`
