# 模型定理

> `grassmann/concept/model-theorem` · 轨道 7 · α-稳定凝聚系 · 状态 draft

> **先自测**：为什么 (c) 比 (a) 与 (b) 合起来更强？

## 一句话

对固定的 $n\ge2,k\ge1$，存在性完全由 $\alpha>0$、$(n-k)\alpha<d$ 与 $d\ge d_0$ 决定；这是整章的「理想图景」，已在若干情形被证明。

## 定义

**模型定理**：对固定且满足 $n\ge2$、$k\ge1$ 的 $n,k$，有 (a) $G(\alpha;n,d,k)\neq\emptyset$ 当且仅当 $\alpha>0$、$(n-k)\alpha<d$ 且 $d\ge d_0$；(b) $B(n,d,k)\neq\emptyset$ 当且仅当 $d\ge d_0$；(c) 若 $d\ge d_0$，则 $U(n,d,k)\neq\emptyset$。

**记号约定**：$B(n,d,k)=\{E\in\mathcal{M}(n,d):h^0(E)\ge k\}$ 为 Brill–Noether 轨迹；$U$ 为 $E$ 稳定的部分。

## 要点（为什么需要它）

- (c) 强于 (a)+(b)：即使 $G$ 非空、$B$ 非空，也可能每个点的底层 $E$ 都不稳定；$U\neq\emptyset$ 排除了这种情形，把抽象存在性升级为 $\mathcal{M}(n,d)$ 上的存在性。
- 已证情形：$0<k\le n$（定理 4.1 与推论 4.3，$d_0$ 显式）；$k=n+1$ 且 $g\ge n^2-1$（定理 6.7）；$k\ge n+2$ 只有部分结果（§7、§8）。
- 在模型定理成立的情形里，$d_0$ 变成唯一未知量；算出 $d_0$ 后非空性判据就是纯数值的不等式。
- 瓶颈在边界：$G(\alpha;n,d,k)$ 的紧化与 $B$ 的紧化需要可约曲线上的无挠层，这正是 §7–§9 与第 9 篇的内容。

## 关键公式

$$
G(\alpha;n,d,k)\neq\emptyset\iff \alpha>0,\ (n-k)\alpha<d,\ d\ge d_0
$$

$$
B(n,d,k)\neq\emptyset\iff d\ge d_0
$$

$$
d\ge d_0\ \Longrightarrow\ U(n,d,k)\neq\emptyset
$$

## 定理与证明（或缺口）

### 模型定理

对固定且满足 $n\ge2$、$k\ge1$ 的 $n,k$，上述 (a)(b)(c) 三条成立。

**证明状态：只引出处，原书不重证**


出处：中译 p.119（模型定理，§2）

### 定理 4.1（$0<k\le n$ 的情形）

设 $0<k\le n$。则 $G(\alpha;n,d,k)\neq\emptyset$ 当且仅当式 (1) 成立且 $k\le n+\frac{1}{g}(d-n)$、$(n,d,k)\neq(n,n,n)$（式 (2)）；若式 (2) 成立且 $d>0$，则 $U(n,d,k)\neq\emptyset$ 且 $G(\alpha;n,d,k)$ 光滑不可约。

**证明状态：只引出处，原书不重证**


出处：中译 p.120（定理 4.1）

### 定理 6.7（$k=n+1$、$g\ge n^2-1$）

设 $g\ge n^2-1$。则模型定理对 $k=n+1$ 成立，其中 $d_0=g+n-[\frac{g}{n+1}]$。

**证明状态：只引出处，原书不重证**


出处：中译 p.123（定理 6.7）

## 易错点

- 把模型定理当成已证的普遍定理：它是「理想图景」，只对部分 $(n,k)$ 成立，$k\ge n+2$ 的一般情形仍开放。
- 忘记 $n\ge2$ 的前提：$n=1$ 时它退化为经典 Brill–Noether 定理的重新表述，不是新内容。
- 把 (a) 里的 $(n-k)\alpha<d$ 简化成 $d>0$：$k<n$ 时这是一个真正的上界，$\alpha$ 太大会破坏稳定性的存在性。
- 把 $B(n,d,k)$ 与 $G(\alpha;n,d,k)$ 的非空性混为一谈：(b) 不含 $\alpha$，(a) 含 $\alpha$，两者由引理 1.4 联系但不是同一命题。

## 相关卡

- [$d_0$ 与存在域 $U(n,d,k)$](../concepts/existence-region-d0.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)
- [对偶张成](../concepts/dual-span.md)
- [大 $\alpha$ 下不半稳定的例子（例 5.3）](../examples/example-non-stability-large-alpha.md)

## 出处

- ch7 §2 模型定理；中译 p.119（英文 PDF p.133），源码 `chapters/ch07.tex:170`
- ch7 §2 模型定理的意义；中译 p.119（英文 PDF p.133），源码 `chapters/ch07.tex:175`
