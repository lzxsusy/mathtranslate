# Petri 曲线

> `grassmann/concept/petri-curve` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **先自测**：为什么「一般曲线是 Petri 曲线」这句话足以支撑整章 $k=n+1$ 的结论？

## 一句话

若对每个线丛 $L$，$(L,H^0(L))$ 的 Petri 映射都单射，则称 $C$ 为 Petri 曲线；一般曲线都是 Petri 曲线，这类曲线上 $k=n+1$ 的存在性问题几乎完全解决。

## 定义

曲线 $C$ 称为 **Petri 曲线**，如果对每个线丛 $L$，凝聚系 $(L,H^0(L))$ 的 Petri 映射都是单射，即 $H^0(L)\otimes H^0(K\otimes L^{-1})\to H^0(K)$ 恒为单射。经典 Brill–Noether 理论的标准结果是：任意亏格的一般曲线都是 Petri 曲线。

**记号约定**：$K$ 为典范丛；等价说法是「$C$ 满足 Petri 条件」。

## 要点（为什么需要它）

- Petri 曲线 = 所有 $L$ 上 Petri 映射单射，由引理 1.8 的 $n=1$ 情形，这等价于每个 $(L,H^0(L))$ 处模空间光滑且维数等于 $\rho$。
- 一般曲线是 Petri 曲线（经典结果），所以 $k=n+1$ 的结论对一般曲线无条件成立；特殊曲线会失败，例如带 $g^1_3$ 的三棱曲线，当 $g\ge5$ 时源维数 $2(g-2)$ 已超过靶维数 $g$，不可能单射。
- $k=n+1$ 时（$C$ Petri）$G_L(n,d,n+1)\neq\emptyset\iff\beta(n,d,n+1)\ge0\iff d\ge g+n-[\frac{g}{n+1}]$（推论 6.3），这是整章最干净的存在性判据。
- 例 7.5 里 Petri 曲线再次出现：$g=10$ 时 $K3$ 曲面上的某些 Petri 曲线带有秩 $5$ 的二次超曲面，使 $d_0=12$ 而非 $13$。

## 关键公式

$$
H^0(L)\otimes H^0(K\otimes L^{-1})\hookrightarrow H^0(K)\quad\forall L\in\Pic(C)
$$

$$
d\ge g+n-\left[\frac{g}{n+1}\right]\iff\beta(n,d,n+1)\ge0
$$

$$
G_L(n,d,n+1)\neq\emptyset\iff d\ge g+n-\left[\frac{g}{n+1}\right]
$$

## 定理与证明（或缺口）

### 推论 6.3（$k=n+1$ 的存在性判据）

设 $C$ 是 Petri 曲线。则 $G_L(n,d,n+1)\neq\emptyset$ 当且仅当 $\beta(n,d,n+1)\ge0$，当且仅当 $d\ge g+n-[\frac{g}{n+1}]$。

**证明状态：只引出处，原书不重证**


出处：中译 p.121（推论 6.3）

### 定理 6.7（$g\ge n^2-1$ 时的模型定理）

设 $k=n+1$ 且 $g\ge n^2-1$。则模型定理对 $(n,k)$ 成立，即存在性完全由 $\alpha>0$、$(n-k)\alpha<d$ 与 $d\ge d_0$ 决定，其中 $d_0=g+n-[\frac{g}{n+1}]$。

**证明状态：只引出处，原书不重证**


出处：中译 p.123（定理 6.7）

## 易错点

- 把「一般曲线是 Petri 曲线」读成「所有曲线都是」：三棱、平面五次等特殊曲线会失败，这正是 Green 猜想里 Clifford 指标小的那些曲线。
- Petri 曲线是对所有线丛的要求，不是只对 $K$ 的要求；只验 $L=K$ 得到的是「典范曲线 Petri」，比 Petri 曲线弱。
- 把 Petri 条件与「$C$ 非超椭圆」混淆：超椭圆曲线对 $L=K$ 也满足 Petri 单射（$g\ge3$ 时），但它在 $g^1_2$ 上失败。

## 相关卡

- [Petri 映射](../concepts/petri-map.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)
- [Clifford 指标](../concepts/clifford-index.md)
- [$g=10$、$(2,12,4)$ 的 $d_0$（例 7.5）](../examples/example-genus-10-d0.md)

## 出处

- ch7 §1 定义 1.9（Petri 曲线）；中译 p.118（英文 PDF p.132），源码 `chapters/ch07.tex:126`
- ch7 §1 Petri 曲线的经典结果；中译 p.118（英文 PDF p.132），源码 `chapters/ch07.tex:129`
