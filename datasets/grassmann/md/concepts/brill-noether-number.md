# Brill–Noether 数 $\beta$

> `grassmann/concept/brill-noether-number` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **先自测**：为什么 $\beta(n,d,k)\ge0$ 既不是 $G(\alpha;n,d,k)$ 非空的充分条件，也不是必要条件？

## 一句话

高秩 Brill–Noether 理论中的预期维数 $\beta(n,d,k)=n^2(g-1)+1-k(k-d+n(g-1))$；它给出凝聚系模空间每个分支的维数下界，但 $\beta\ge0$ 与非空性并不等价。

## 定义

设 $C$ 是亏格 $g\ge2$ 的光滑射影曲线。型为 $(n,d,k)$ 的凝聚系的 **Brill–Noether 数**定义为 $\beta(n,d,k):=n^2(g-1)+1-k\bigl(k-d+n(g-1)\bigr)$。它是 $G(\alpha;n,d,k)$ 的预期维数：引理 1.6 断言每个不可约分支的维数都 $\ge\beta(n,d,k)$。

**记号约定**：$n$ 为秩，$d$ 为次数，$k$ 为 $V\subset H^0(E)$ 的维数；$\alpha$ 为稳定性参数。

## 要点（为什么需要它）

- $n=1$ 时 $\beta(1,d,k)=g-k(k-d+g-1)$；令 $k=r+1$ 即经典 Brill–Noether 数 $\rho(g,r,d)=g-(r+1)(g-d+r)$。
- 它是「预期维数」而非「存在判据」：Petri 映射单射时 $G$ 在相应点光滑且维数恰为 $\beta$（引理 1.8），此时 $\beta$ 才有几何意义。
- 两个方向都失败（L153 的「显而易见」猜想）：注 4.2 说明式 (2)（$k\le n+\frac{1}{g}(d-n)$ 且 $(n,d,k)\neq(n,n,n)$）严格强于 $\beta\ge0$，故 $\beta\ge0$ 不充分；注 8.4 给出 $\beta<0$ 而非空的例子，故也不必要。
- 具体反例：$g=10$、$(n,d,k)=(2,12,4)$ 时 $\beta=4\cdot9+1-4(4-12+18)=-3<0$，但例 7.5 说明某些 Petri 曲线上 $G(\alpha;2,12,4)\neq\emptyset$，同时它也是 $d_0$ 只能取 $12$ 或 $13$ 的原因。

## 关键公式

$$
\beta(n,d,k)=n^2(g-1)+1-k\bigl(k-d+n(g-1)\bigr)
$$

$$
\beta(1,d,r+1)=g-(r+1)(g-d+r)=\rho(g,r,d)
$$

$$
\beta(2,12,4)\big|_{g=10}=36+1-40=-3
$$

## 定理与证明（或缺口）

### 引理 1.6（维数下界）

对任意 $\alpha$，$G(\alpha;n,d,k)$ 的每个不可约分支的维数都 $\ge\beta(n,d,k)$；这里 $\beta$ 可正可负（负值时的下界是空话）。

**证明状态：只引出处，原书不重证**


出处：中译 p.118（引理 1.6，引 [28, Cor. 3.14] 与 [17, Cor. 3.6]）

### 引理 1.8（Petri 单射 $\iff$ 光滑且维数 $\beta$）

设 $(E,V)\in G(\alpha;n,d,k)$。则 $G(\alpha;n,d,k)$ 在 $(E,V)$ 处光滑且维数为 $\beta(n,d,k)$，当且仅当 $(E,V)$ 的 Petri 映射是单射。

**证明状态：提纲（有缺口）**


> **缺口**：原文只引用，未给证明。缺的是形变理论两步：把 $G$ 在 $(E,V)$ 处的切空间识别为 Petri 映射的核、把障碍空间识别为其上核（上核为零即光滑性），再由 $\dim=\dim\mathrm{Hom}-\dim\mathrm{Ext}^1$ 得到 $\beta$。


出处：中译 p.118（引理 1.8，引 [17, Prop. 3.10]）

## 易错点

- 把 $\beta\ge0$ 当作存在性判据：注 4.2 与注 8.4 各给一个反例方向，真正的判据是模型定理里的 $d\ge d_0$。
- 把 $\beta$ 与经典 $\rho$ 混用：$n=1$ 时 $\beta(1,d,r+1)=\rho(g,r,d)$，但 $n\ge2$ 时两者没有简单的代入关系，必须用 $n^2(g-1)+1-k(k-d+n(g-1))$。
- 忘记 $k$ 出现在两个位置：$\beta$ 对 $k$ 是二次的，$k$ 增大一次，$\beta$ 变化 $-(2k-1-d+n(g-1))$，不是线性的。

## 相关卡

- [Petri 映射](../concepts/petri-map.md)
- [$d_0$ 与存在域 $U(n,d,k)$](../concepts/existence-region-d0.md)
- [模型定理](../concepts/model-theorem.md)
- [Green 维数公式](../concepts/greens-dimension-formula.md)

## 出处

- ch7 §1 定义 1.5（Brill–Noether 数）；中译 p.118（英文 PDF p.132），源码 `chapters/ch07.tex:98`
- ch7 §1 引理 1.6；中译 p.118（英文 PDF p.132），源码 `chapters/ch07.tex:104`
