# Clifford 指标

> `grassmann/concept/clifford-index` · 轨道 2 · Koszul 上同调 · 状态 draft

> **先自测**：为什么同一个整数既能控制线性系的维数，又能控制典范曲线的二次合冲？

## 一句话

曲线所有「有贡献」线性系的 $\deg L-2h^0(L)+2$ 的最小值，衡量曲线离超椭圆有多远，也是 Green 猜想中 Koszul 上同调开始消没的那个临界下标。

## 定义

设 $C$ 是亏格 $g\ge2$ 的光滑射影曲线。对线丛 $L$ 定义 $\mathrm{Cliff}(L):=\deg(L)-2h^0(C,L)+2$。若 $h^0(C,L)\ge2$ 且 $h^1(C,L)\ge2$（即 $L$ 与 $K_C\otimes L^{-1}$ 都至少有两个截面），则称 $L$ **对 Clifford 指标有贡献**，并令 $\mathrm{Cliff}(C):=\min\{\mathrm{Cliff}(L):L\ \text{有贡献}\}$。原文 L17 的写法是 $\mathrm{Cliff}(C)=\min\{\deg L-2r(L):L\in\mathrm{Pic}(C),\ h^i(C,L)\ge2,\ i=0,1\}$，其中 $r(L)=h^0(C,L)-1$，两式只差常数 $2$。

**记号约定**：$r(L)=h^0(C,L)-1$；$K_C$ 为典范丛；$\mathrm{gon}(C)$ 为棱性（gonality）。

## 要点（为什么需要它）

- Clifford 定理给出 $\mathrm{Cliff}(L)\ge0$，且除 $L\cong\mathfrak{g}^1_2$ 外严格为正——这正是经典 Clifford 不等式 $h^0(L)\le\deg(L)/2+1$ 的重新包装。
- 一般 $d$-棱曲线 $\mathrm{Cliff}(C)=d-2$；例外曲线（平面曲线、$K3$ 曲面上的曲线）满足 $\mathrm{Cliff}(C)=\mathrm{gon}(C)-3$（Coppens–Martens）。
- Green 猜想把它变成 Koszul 上同调的下标阈值：$K_{p,2}(C,K_C)=0\iff p<\mathrm{Cliff}(C)$；而定理 2.4 保证 $K_{g-\mathrm{Cliff}(C)-2,1}(C,K_C)\neq0$，两侧一夹就确定了临界值。
- 超椭圆曲线 $\mathrm{Cliff}(C)=0$；恒有 $\mathrm{Cliff}(C)\le\mathrm{gon}(C)-2$，故 Cliff 越小、棱性越小。

## 关键公式

$$
\mathrm{Cliff}(L)=\deg(L)-2h^0(C,L)+2
$$

$$
\mathrm{Cliff}(C)=\min\{\mathrm{Cliff}(L): h^0(C,L)\ge2,\ h^1(C,L)\ge2\}
$$

$$
K_{p,2}(C,K_C)=0\iff p<\mathrm{Cliff}(C)
$$

## 定理与证明（或缺口）

### Clifford 定理（$\mathrm{Cliff}(L)\ge0$）

对亏格 $g\ge2$ 的光滑曲线 $C$ 与任一满足 $h^0(C,L)\ge2$、$h^1(C,L)\ge2$ 的线丛 $L$，有 $\deg(L)-2h^0(C,L)+2\ge0$；等号成立当且仅当 $L$ 是 $\mathfrak{g}^1_2$（即 $C$ 超椭圆）。等价地，$h^0(C,L)\le\frac{1}{2}\deg(L)+1$。

**证明状态：只引出处，原书不重证**


出处：中译 p.43（§4.1，引 Clifford 与 ACGH）

### 定理 2.4 的推论（Cliff 给出非消没的下标）

把典范丛分解为 $K_C=L_1\otimes(K_C\otimes L_1^{\vee})$，若 $L_1$ 对 Clifford 指标有贡献、$h^0(C,L_i)=r_i+1\ge2$，则 $r_1+r_2-1=g-\mathrm{Cliff}(L_1)-2$，故定理 2.4 给出 $K_{g-\mathrm{Cliff}(L_1)-2,1}(C,K_C)\neq0$；取 $L_1$ 使 $\mathrm{Cliff}(L_1)=\mathrm{Cliff}(C)$ 即得 $K_{g-\mathrm{Cliff}(C)-2,1}\neq0$。

**证明状态：提纲（有缺口）**


> **缺口**：原文只写「由定理 2.4 立得」，没有逐项验算：需要由 Serre 对偶把 $h^0(K_C\otimes L_1^{\vee})=h^1(L_1)$ 认出第二个因子有 $\ge2$ 个截面，并核对 $r_1+r_2-1=(h^0(L_1)-1)+(h^1(L_1)-1)-1$ 与 $g-\mathrm{Cliff}(L_1)-2$ 的算术恒等。


出处：中译 p.43–44（§4.1，L583–600）

## 易错点

- 把 $\mathrm{Cliff}(C)$ 直接当成 $\mathrm{gon}(C)-2$：这只对一般 $d$-棱曲线成立，例外曲线（平面五次、$K3$ 截面）有 $\mathrm{Cliff}(C)=\mathrm{gon}(C)-3$。
- 定义里的条件 $h^i(C,L)\ge2$（$i=0,1$）不能省：只要求 $h^0(L)\ge2$ 会把 $\deg$ 很小、$h^1$ 很大的线丛也算进来，得到负值。
- $K_{p,2}=0\iff p<\mathrm{Cliff}$ 的 $p$ 是外幂次数而非亏格；超椭圆时 $\mathrm{Cliff}=0$，阈值落在 $p<0$ 上，$p=0$ 已经非零。

## 相关卡

- [Green 猜想](../concepts/greens-conjecture.md)
- [Green 维数公式](../concepts/greens-dimension-formula.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)
- [Petri 曲线](../concepts/petri-curve.md)

## 出处

- ch2 §1 引言（Clifford 指标的初定义）；中译 p.30（英文 PDF p.34），源码 `chapters/ch02.tex:17`
- ch2 §4.1 Cliff(L) 与 Cliff 定理；中译 p.43（英文 PDF p.47），源码 `chapters/ch02.tex:589`
