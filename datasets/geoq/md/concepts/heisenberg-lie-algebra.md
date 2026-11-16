# 海森堡李代数 $h_V$

> `geoq/concept/heisenberg-lie-algebra` · 轨道 C · 海森堡群与表示 · 状态 draft

> **先自测**：为什么海森堡李代数的括号只需由辛形式给出，而新增的基元 $K$ 必须落在中心？

## 一句话

在 $2n$ 维辛空间 $V$ 上添一维中心 $K$，用辛配对定义括号 $[u,v]=\omega(u,v)K$，得 $2n+1$ 维二阶幂零李代数；辛基下它化为 $n$ 组正则对易关系，辛群自动作用为自同构。

## 定义

设 $(V,\omega)$ 为 $2n$ 维实辛空间，$K$ 是新增的形式符号。考虑直和 $h_V=V\oplus\mathbb R K$，并把括号规定为 $[u+\lambda K,\ v+\mu K]:=\omega(u,v)K$：$V$ 内部先用 $\omega$ 配对再乘 $K$，而 $K$ 与所有元素交换。该括号双线性、反对称，雅可比恒等式自动成立（见本节命题），于是得到 $2n+1$ 维李代数 $h_V$。若取辛基 $\{e_1,\dots,e_n,f_1,\dots,f_n\}$，括号简化为 $[e_i,f_j]=\delta_{ij}K$，其余括号为零；特别地 $V=\mathbb R^{2n}$ 时记 $h_n$，而任意辛空间都与 $h_n$ 同构。

**记号约定**：$\{e_1,\dots,e_n,f_1,\dots,f_n\}$ 为 $(V,\omega)$ 的辛基，即 $\omega(e_i,f_j)=\delta_{ij}$、$\omega(e_i,e_j)=\omega(f_i,f_j)=0$；$K$ 是中心的基元；$\operatorname{Aut}(h_V)$ 记李代数自同构群；下标 $i,j$ 取 $1,\dots,n$，重复指标不求和。

## 要点

- 括号的取值全部落在中心：$[u,v]=\omega(u,v)K\in\mathbb{R}K$，$V$ 分量只充当参数，不会产生新的 $V$ 分量。
- 由 $[h_V,h_V]=\mathbb{R}K$ 与 $K$ 中心可得 $[h_V,[h_V,h_V]]=0$，即 $h_V$ 二阶幂零（步长 2），其 Killing 形式恒为零；下一节 BCH 级数只保留到第二项，根子在这里。
- 辛基把括号完全对角化：$[e_i,f_j]=\delta_{ij}K$ 是 $n$ 组互不耦合的正则对易关系，所有同型括号为零。
- 任何 $2n$ 维辛空间都辛同构于 $\mathbb{R}^{2n}$，故 $h_V\cong h_n$；海森堡李代数只依赖 $n$，不依赖具体辛空间。
- $\varphi\in\operatorname{Sp}(V)$ 诱导 $u+\lambda K\mapsto\varphi(u)+\lambda K$，这是李代数自同构，于是有群同态 $\operatorname{Sp}(V)\to\operatorname{Aut}(h_V)$。

## 关键公式

$$
$[u+\lambda K,\ v+\mu K]=\omega(u,v)K,\qquad [K,h_V]=0$
$$

$$
$[e_i,f_j]=\delta_{ij}K,\qquad [e_i,e_j]=[f_i,f_j]=[e_i,K]=[f_i,K]=0$
$$

$$
$[h_V,h_V]=\mathbb{R}K,\qquad [h_V,[h_V,h_V]]=0,\qquad \dim h_V=2n+1$
$$

$$
$\varphi(u+\lambda K)=\varphi(u)+\lambda K\qquad(\varphi\in\operatorname{Sp}(V))$
$$

$$
$h_V\cong h_n,\qquad h_n:=h_{\mathbb{R}^{2n}}$
$$

## 定理与证明

### 命题（$h_V$ 是李代数，辛基下括号对角）

设 $(V,\omega)$ 是 $2n$ 维辛向量空间，$h_V=V\oplus\mathbb{R}K$ 上定义 $[u+\lambda K,v+\mu K]=\omega(u,v)K$。则该括号双线性、反对称并满足雅可比恒等式，$(h_V,[-,-])$ 是 $2n+1$ 维二阶幂零李代数；在辛基下 $[e_i,f_j]=\delta_{ij}K$，其余括号全为零。

**完整证明**

1. 双线性与反对称：括号只读取 $u,v$ 的 $V$ 分量，$\lambda,\mu$ 不进入表达式；$\omega$ 双线性，故括号对两个变量都线性。交换 $u,v$ 时 $\omega(u,v)$ 变号而 $K$ 是固定基元，故反对称。
   - *为什么*：李代数公理的前两条直接继承辛形式，$K$ 分量根本不出现在括号里，所以对 $\lambda,\mu$ 没有任何额外要求。
2. 雅可比恒等式：任取 $x,y,z\in h_V$，内层括号 $[y,z]=\omega(y,z)K$ 是中心元，故 $[x,[y,z]]=0$；循环求和的三项逐个为零，恒等式成立。
   - *为什么*：这正是「中心」的作用：只要内层括号落在 $\mathbb{R}K$，外层括号就消失，于是雅可比恒等式不需要任何计算，同时也说明了二阶幂零。
3. 辛基下的括号：辛基的定义就是 $\omega(e_i,f_j)=\delta_{ij}$、$\omega(e_i,e_j)=\omega(f_i,f_j)=0$，代入 $[u,v]=\omega(u,v)K$ 即得 $[e_i,f_j]=\delta_{ij}K$，其余组合为零；又 $K$ 中心，故 $[e_i,K]=[f_i,K]=0$。
   - *为什么*：辛基把 $\omega$ 的矩阵化成标准形，唯一非零的配对就是 $e_i$ 与 $f_i$，所以括号表只有 $n$ 个非零项。
4. 维数与幂零性：$\dim h_V=2n+1$。由 $\omega$ 非退化，对每个 $u\neq0$ 都存在 $v$ 使 $\omega(u,v)\neq0$，故 $[h_V,h_V]=\mathbb{R}K$ 恰为一维；又 $[\mathbb{R}K,h_V]=0$，故 $h_V$ 二阶幂零。
   - *为什么*：非退化性保证 $[h_V,h_V]$ 不会退化成 $0$；而它落在中心保证再取一次括号就归零——这两点合起来给出「步长 2」，是下一节指数化的前提。

来源：ch05b.tex:29-55（原书 p.272）

## 易错点

- $V$ 不是 $h_V$ 的子李代数：$[V,V]=\mathbb{R}K\not\subset V$，所以 $h_V$ 不是 $V$ 与 $\mathbb{R}K$ 的直和 Lie 代数（直和会要求 $[V,V]=0$）。
- 中心是整个 $\mathbb{R}K$，不只是基元 $K$：$[u,\lambda K]=0$ 对任意实数 $\lambda$ 成立；说「$K$ 是中心」时要能答出 $\lambda K$ 也在中心。
- 不要拿半单代数的直觉套它：$h_V$ 幂零、Killing 形式恒为零、指数映射是整体微分同胚，因此没有紧致群与半单代数那种对应。
- 括号系数依赖辛基的归一化：若取 $\omega(e_i,f_j)=c\,\delta_{ij}$，则 $[e_i,f_j]=c\,\delta_{ij}K$。$\delta_{ij}$ 不是与 $\omega$ 无关的约定。

## 相关卡

- [辛向量空间与辛基](../concepts/symplectic-vector-space.md)
- [海森堡群 $H_V$ 与中心扩张](../concepts/heisenberg-group.md)
- [薛定谔表示 $T_\hbar$](../concepts/schrodinger-representation.md)
- [斯通–冯·诺依曼定理](../concepts/stone-von-neumann.md)

## 出处

- §5.3.1 海森堡李代数，p.272（PDF p.273），源码 `ch05b.tex:29-64`
