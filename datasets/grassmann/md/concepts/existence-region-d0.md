# $d_0$ 与存在域 $U(n,d,k)$

> `grassmann/concept/existence-region-d0` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **先自测**：为什么 $d_0$ 不能由「$\beta\ge0$ 的最小 $d$」算出来？

## 一句话

$d_0(n,k)$ 是使 $G(\alpha;n,d,k)$ 非空的最小次数，$U(n,d,k)$ 是其中 $E$ 稳定的部分；模型定理断言存在性只由 $d\ge d_0$ 与式 (1) 决定。

## 定义

记 $d_0=d_0(n,k):=\min\{d\colon\text{对某个满足式 (1) 的 }\alpha,\ G(\alpha;n,d,k)\neq\emptyset\}$。又记 $U(n,d,k):=\{(E,V)\in G_L(n,d,k)\mid E\ \text{稳定}\}$ 与 $U^s(n,d,k):=\{(E,V)\mid (E,V)\ \text{对某个}\ \alpha>0,\ \alpha(n-k)<d\ \text{是}\ \alpha\text{-稳定}\}$。式 (1) 是 $\alpha>0$、$d>0$、$\alpha(n-k)<d$。

**记号约定**：$G_L(n,d,k)$ 为固定线丛 $L=\det E$ 的纤维；$B(n,d,k)$ 为 Brill–Noether 轨迹。

## 要点（为什么需要它）

- 式 (1) 是存在域的必要边界：由引理 1.3，$G(\alpha;n,d,k)\neq\emptyset$ 迫使 $\alpha>0$、$d>0$、$\alpha(n-k)<d$；$k\ge1$ 时 $\alpha>0$ 尤其不能省。
- $U$ 与 $U^s$ 的分工：$U$ 要求底层的 $E$ 稳定（这样才落到 $\mathcal{M}(n,d)$ 上），$U^s$ 要求凝聚系本身对某个 $\alpha$ 稳定；定理 2.1 说固定 $n,k$ 时充分大的 $d$ 总有 $U\neq\emptyset$。
- $d_0$ 不是 $\beta\ge0$ 的阈值：注 4.2（$0<k\le n$ 时式 (2) 严格强于 $\beta\ge0$）与注 8.4 各给一个方向的失败，故 $d_0$ 只能靠构造与消没定理确定。
- 已知值：$0<k\le n$ 时 $d_0=\max\{1,n-g(n-k)\}$（$k<n$）、$d_0=n+1$（$k=n$）（推论 4.3）；$k=n+1$ 时 $d_0=g+n-[\frac{g}{n+1}]$（推论 6.6）。

## 关键公式

$$
d_0(n,k)=\min\{d\colon\exists\alpha\ \text{满足式 (1)},\ G(\alpha;n,d,k)\neq\emptyset\}
$$

$$
\alpha>0,\qquad d>0,\qquad \alpha(n-k)<d
$$

$$
U(n,d,k):=\{(E,V)\in G_L(n,d,k):E\ \text{稳定}\}
$$

## 定理与证明（或缺口）

### 引理 1.3（存在域的必要条件）

若 $G(\alpha;n,d,k)\neq\emptyset$，则 $\alpha>0$、$d>0$ 且 $\alpha(n-k)<d$（式 (1)）。

**证明状态：提纲（有缺口）**


> **缺口**：原文只写「这可由 $\alpha$-稳定性的定义轻易推出」，没有展开。要点是对 $(E,V)$ 取适当的真凝聚子系（含 $V$ 的适当子空间或秩较低的子丛）逐个验证 $\mu_\alpha(F,W)<\mu_\alpha(E,V)$，三个不等式分别对应 $\alpha>0$、$d>0$ 与 $\alpha(n-k)<d$。


出处：中译 p.118（引理 1.3）

### 定理 2.1（充分大次数时存在）

对任意固定的 $n,k$，所有充分大的 $d$ 都满足 $U(n,d,k)\neq\emptyset$；$k\le n$ 见 [16,18]，$k>n$ 见 [3,49]。

**证明状态：只引出处，原书不重证**


出处：中译 p.119（定理 2.1）

### 推论 4.3（$0<k\le n$ 时的 $d_0$）

设 $0<k\le n$。则模型定理成立，且 $d_0=\max\{1,n-g(n-k)\}$（当 $k<n$）、$d_0=n+1$（当 $k=n$）。

**证明状态：只引出处，原书不重证**


出处：中译 p.120（推论 4.3）

## 易错点

- 把 $d_0$ 算成「$\beta\ge0$ 的最小 $d$」：$\beta\ge0$ 既不充分也不必要（注 4.2、8.4），二者只在特定 $(n,k)$ 上巧合一致。
- 漏掉 $\alpha(n-k)<d$ 里 $n-k$ 的符号：$k>n$ 时这个条件对 $\alpha>0$ 自动满足，所以 $k>n$ 的存在域与 $k\le n$ 形状完全不同。
- 把 $U(n,d,k)\neq\emptyset$ 与 $G(\alpha;n,d,k)\neq\emptyset$ 等同：前者要求底层 $E$ 稳定，后者只要求凝聚系 $\alpha$-稳定；模型定理的 (c) 正是说 $d\ge d_0$ 时两者可以同时满足。

## 相关卡

- [模型定理](../concepts/model-theorem.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)
- [Petri 映射](../concepts/petri-map.md)
- [有效除子的斜率](../concepts/slope-of-effective-divisor.md)

## 出处

- ch7 §2 $d_0$ 的定义；中译 p.119（英文 PDF p.133），源码 `chapters/ch07.tex:165`
- ch7 §2 $U(n,d,k)$ 与 $U^s(n,d,k)$；中译 p.119（英文 PDF p.133），源码 `chapters/ch07.tex:139`
