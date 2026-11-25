# Enriques–Babbage–Petri 定理即 $K_{1,2}=0$

> `grassmann/example/enriques-babbage-petri` · 轨道 2 · Koszul 上同调 · 状态 draft

> **这张卡练什么**：为什么 $K_{1,2}=0$ 恰好对应「典范曲线是二次超曲面的完全交」，而三棱曲线一定失败？

## 一句话

Green 猜想 $p=1$ 的情形：非超椭圆曲线的 $K_{1,2}(C,K_C)$ 消没等价于典范曲线由二次超曲面切出，即 Enriques–Babbage–Petri 定理；例外恰是超椭圆、三棱与光滑平面五次。

## 背景定义

取 $C$ 为亏格 $g\ge4$ 的光滑曲线，$L=K_C$、$p=1$、$q=2$。$K_{1,2}(C,K_C)$ 度量的是典范曲线的二次超曲面之间的线性合冲：$K_{1,2}=0$ 当且仅当二次式生成的理想已经切出 $C\subset\mathbb{P}^{g-1}$。

## 设定

$g\ge4$、$C$ 非超椭圆，$L=K_C$ 非常充裕，$p=1$、$q=2$；比较 $K_{1,2}(C,K_C)$ 与二次超曲面的截出性。

## 计算

由定理 2.6，$K_{1,2}\cong\mathrm{coker}(\wedge^2H^0(K)\otimes H^0(K)\to H^0(M_{K_C}\otimes K^2))$，其维数由定理 2.8 的差 $\dim K_{1,1}-\dim K_{0,2}$ 控制（$g\ge4$ 时 $p=1<d-g=g-2$）。当 $C$ 三棱时 $g^1_3\subset K_C$ 给出 Petri 映射的核，$K_{1,2}\neq0$；当 $C$ 是光滑平面五次（$g=6$）时同理。

## 要点

- $K_{1,2}=0$ 就是 Petri 映射在 $q=2$ 层的单射性，几何上等价于「典范曲线由二次超曲面截出」。
- 例外清单只有三类：超椭圆（$\mathrm{Cliff}=0$）、三棱（$\mathrm{Cliff}=1$）、光滑平面五次（$g=6$，$\mathrm{Cliff}=1$）；三者都满足 $1\ge\mathrm{Cliff}$，故 $K_{1,2}\neq0$。
- 对三棱曲线，$g^1_3$ 使 Petri 映射出现核，典范曲线落在三次曲面上，二次式切不出来。
- 它是 Green 猜想在 $p=1$ 的全部内容，也是继 Max Noether（$p=0$）之后被证明的第二格。

## 关键公式

$$
K_{1,2}(C,K_C)=0\iff C\subset\mathbb{P}^{g-1}\ \text{由二次超曲面截出}
$$

$$
K_{p,2}(C,K_C)=0\iff p<\mathrm{Cliff}(C)
$$

$$
\mathrm{Cliff}(C)\ge2\iff C\ \text{既不超椭圆、也不三棱、也不是光滑平面五次}
$$

## 相关定理

- **Enriques–Babbage–Petri 定理**：设 $C$ 是亏格 $g\ge4$ 的非超椭圆曲线。则 $K_{1,2}(C,K_C)=0$ 当且仅当典范曲线 $C\subset\mathbb{P}^{g-1}$ 由二次超曲面截出；等价地，当且仅当 $C$ 既不三棱也不是光滑平面五次曲线。
- **Green 猜想的 $p=1$ 情形**：猜想 4.1 取 $p=1$：若 $\mathrm{Cliff}(C)\ge2$，则 $K_{1,2}(C,K_C)=0$；若 $\mathrm{Cliff}(C)\le1$ 则 $K_{1,2}\neq0$。这正是 EBP 定理，故猜想在 $p=1$ 也已被经典结果验证。

## 易错点

- 例外是「光滑平面五次」而不是所有平面曲线：平面四次（$g=3$）属于三棱情形，平面六次以上不在例外表里。
- 把 $K_{1,2}=0$ 当成「理想由二次式生成」：那是 $K_{0,2}=0$（正规生成，Max Noether）；$K_{1,2}$ 管的是二次式之间的合冲。
- 三棱曲线的 $K_{1,2}\neq0$ 并不违反 Green 猜想——猜想只在 $p<\mathrm{Cliff}$ 一侧预言消没，$p=1=\mathrm{Cliff}$ 正在非消没一侧。

## 用到哪些概念

- [Green 猜想](../concepts/greens-conjecture.md)
- [Clifford 指标](../concepts/clifford-index.md)
- [Koszul 对偶](../concepts/koszul-duality.md)

## 相关卡

- [Max Noether 定理即 $K_{0,2}=0$](../examples/max-noether-theorem.md)
- [Green 猜想](../concepts/greens-conjecture.md)
- [Petri 映射](../concepts/petri-map.md)
- [Clifford 指标](../concepts/clifford-index.md)

## 出处

- ch2 §4.1 例 4.3（Enriques–Babbage–Petri）；中译 p.44（英文 PDF p.48），源码 `chapters/ch02.tex:616`
- ch2 §4.1 Green 猜想的形式；中译 p.44（英文 PDF p.48），源码 `chapters/ch02.tex:608`
