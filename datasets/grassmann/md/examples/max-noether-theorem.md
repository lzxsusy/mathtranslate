# Max Noether 定理即 $K_{0,2}=0$

> `grassmann/example/max-noether-theorem` · 轨道 2 · Koszul 上同调 · 状态 draft

> **这张卡练什么**：为什么「$K_{0,2}=0$」这一个小小的上同调消没，恰好就是 Max Noether 的射影正规性？

## 一句话

Green 猜想 $p=0$ 的情形：非超椭圆曲线的 $K_{0,2}(C,K_C)$ 消没等价于典范曲线射影正规，即经典 Max Noether 定理——Green 猜想把它推广到所有 $p$。

## 背景定义

$C$ 是亏格 $g\ge3$ 的光滑曲线，$K_C$ 非常充裕，典范嵌入记为 $C\subset\mathbb{P}^{g-1}=\mathbb{P}H^0(C,K_C)^{\vee}$。取 $L=K_C$、$p=0$、$q=2$，则 $K_{0,2}(C,K_C)\cong\mathrm{coker}\bigl(\mathrm{Sym}^2H^0(C,K_C)\to H^0(C,K_C^{\otimes2})\bigr)$；它消没当且仅当典范曲线是射影正规的（由二次式切出）。

## 设定

$g\ge3$，$C$ 非超椭圆，$L=K_C$ 非常充裕，$p=0$、$q=2$。

## 计算

由定理 2.6 取 $p=0$：$K_{0,2}=\mathrm{coker}(H^0\otimes H^0\to H^0(K^2))$；反对称部分映到 $0$，故 $K_{0,2}=\mathrm{coker}(\mathrm{Sym}^2H^0(K)\to H^0(K^{\otimes2}))$。维数上 $\dim\mathrm{Sym}^2H^0(K)=\binom{g+1}{2}=\frac{g(g+1)}{2}$，$h^0(K^{\otimes2})=3g-3$，两者在 $g=3$ 时为 $6$ 与 $6$，$g\ge4$ 时前者更大，故消没是一个真条件。

## 要点

- $K_{0,2}$ 是 $\mathrm{Sym}^2H^0(K_C)\to H^0(K_C^2)$ 的上核；它为零 $\iff$ 该乘法满射 $\iff$ 二次式已经切出典范曲线（射影正规）。
- 超椭圆曲线是反例：$\mathrm{Cliff}=0$，猜想只对 $p<0$ 陈述，此时 $K_{0,2}\neq0$（典范曲线落在有理正规曲线上）。
- 这是 Green 猜想 $p=0$ 的全部内容；$p=1$ 是 Enriques–Babbage–Petri，$p\ge2$ 才是真正的新猜想。
- $g=3$ 的非超椭圆曲线是光滑平面四次曲线（三棱），$K_{0,2}=0$ 但 $K_{1,2}\neq0$，正落在 EBP 的例外清单里。

## 关键公式

$$
K_{0,2}(C,K_C)\cong\mathrm{coker}\bigl(\mathrm{Sym}^2H^0(C,K_C)\to H^0(C,K_C^{\otimes2})\bigr)
$$

$$
K_{0,2}(C,K_C)=0\iff C\subset\mathbb{P}^{g-1}\ \text{射影正规}
$$

$$
h^0(C,K_C^{\otimes2})=3g-3,\qquad \dim\mathrm{Sym}^2H^0(C,K_C)=\frac{g(g+1)}{2}
$$

## 相关定理

- **Max Noether 定理**：设 $C$ 是亏格 $g\ge3$ 的非超椭圆曲线。则典范曲线 $C\subset\mathbb{P}^{g-1}$ 射影正规，等价地 $K_{0,2}(C,K_C)=0$，即典范曲线由二次超曲面切出。
- **Green 猜想的 $p=0$ 情形**：猜想 4.1 取 $p=0$：当 $\mathrm{Cliff}(C)\ge1$（即 $C$ 非超椭圆）时有 $K_{0,2}(C,K_C)=0$。这正是 Max Noether 定理，故猜想在 $p=0$ 已被经典结果验证。

## 易错点

- 把 $K_{0,2}=0$ 与「$C$ 非超椭圆」直接等同：还要 $g\ge3$；$g=2$ 时典范映射是 $2:1$，$K_{0,2}\neq0$。
- 上核里反对称部分映到零，所以 $K_{0,2}=\mathrm{coker}(\mathrm{Sym}^2\to H^0(K^2))$，不是 $\mathrm{coker}(H^0\otimes H^0\to H^0(K^2))$；两者维数差 $\binom{g}{2}$。
- 「射影正规」是相对典范嵌入说的，不是曲线本身的几何性质；换一个非常充裕线丛，$K_{0,2}$ 的含义随之改变。

## 用到哪些概念

- [Green 猜想](../concepts/greens-conjecture.md)
- [Koszul 对偶](../concepts/koszul-duality.md)
- [Clifford 指标](../concepts/clifford-index.md)

## 相关卡

- [Enriques–Babbage–Petri 定理即 $K_{1,2}=0$](../examples/enriques-babbage-petri.md)
- [Green 猜想](../concepts/greens-conjecture.md)
- [Petri 映射](../concepts/petri-map.md)

## 出处

- ch2 §4.1 例 4.2（Max Noether）；中译 p.44（英文 PDF p.48），源码 `chapters/ch02.tex:612`
- ch2 §4.1 Green 猜想与 Betti 表；中译 p.44（英文 PDF p.48），源码 `chapters/ch02.tex:604`
