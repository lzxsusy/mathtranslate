# 极小分次自由分解与分次 Betti 数

> `grassmann/concept/graded-minimal-resolution-and-betti-numbers` · 轨道 2 · Koszul 上同调 · 状态 draft

> **先自测**：为什么 $\beta_{pj}$ 只在 $j>p$ 出现，而 $b_{i,j}=\beta_{i,i+j}$ 又要换一次指标？

## 一句话

把射影簇的齐次坐标环写成极小自由 $S$-模分解，各阶自由模的重数 $\beta_{pj}$ 就是 Betti 数；它们完全决定 Hilbert 函数，也是 Koszul 上同调 $K_{p,q}$ 的代数原型。

## 定义

设 $V$ 是 $n$ 维复向量空间，$S:=S(V)$，$X\subset\mathbb{P}V^{\vee}=\mathrm{Proj}(S)$ 为非退化子簇，$S(X)$ 为其齐次坐标环。$S(X)$ 作为分次 $S$-模有**分次极小自由分解** $0\to E_s\to\dots\to E_2\to E_1\to S\to S(X)\to0$，其中 $E_p=\bigoplus_{j>p}S(-j)^{\beta_{pj}(X)}$。整数 $\beta_{pj}(X)$ 称**分次 Betti 数**，$E_p$ 称第 $p$ 阶合冲模。

**记号约定**：$S(-j)$ 为 twist 后的自由模，$S(-j)_d=S_{d-j}$；$h_X(d)=\dim_{\mathbb{C}}S(X)_d$。

## 要点（为什么需要它）

- $\beta_{pj}$ 数的是「内次数 $j$、第 $p$ 阶」的极小生成元个数；$j>p$ 是极小性的直接后果（不出现常数项自由模）。
- Hilbert 函数由 Betti 数完全决定：$h_X(d)=\sum_{p,j}(-1)^p\beta_{pj}(X)\binom{n-1+d-j}{n-1}$，右端在 $d$ 大时是多项式。
- Green 的贡献是把 $\beta_{pj}$ 翻译成与层有关的 $K_{p,q}$：对典范曲线 $b_{p,q}=\dim K_{p,q}(C,K_C)$，「合冲」于是变成「上同调消没」，可以上族。
- 极小分解在同构意义下唯一，$\beta_{pj}$ 才是不变量；非同小的分解里会出现可约去的项，Betti 数就没有意义。

## 关键公式

$$
E_p=\bigoplus_{j>p}S(-j)^{\beta_{pj}(X)}
$$

$$
h_X(d)=\sum_{p,j}(-1)^p\beta_{pj}(X)\binom{n-1+d-j}{n-1}
$$

$$
\beta_{pj}(X)=\dim_{\mathbb{C}}\mathrm{Tor}_p^S(S(X),\mathbb{C})_j
$$

## 定理与证明（或缺口）

### Hilbert 函数由 Betti 数决定（式 (2)）

对任意 $d\ge1$ 有 $h_X(d)=\sum_{p,j}(-1)^p\beta_{pj}(X)\binom{n-1+d-j}{n-1}$。中译正文印作 $\binom{n+d-j}{n}$，译注②指出按 $\dim V=n$（即 $X\subset\mathbb{P}^{n-1}$）应为 $\binom{n-1+d-j}{n-1}$。

**证明状态：完整**

1. 把极小分解逐项取 $d$ 次分次部分，得向量空间的正合列 $0\to(E_s)_d\to\dots\to(E_1)_d\to S_d\to S(X)_d\to0$。
   - *为什么*：分次模的正合列可以逐次取分次部分，正合性保持。
2. 取维数并交错求和，$S(X)_d$ 只剩一项，得 $h_X(d)=\sum_{p}(-1)^p\sum_j\beta_{pj}\dim S_{d-j}$。
   - *为什么*：正合列各项维数的交错和为零，而 $S_d$ 的贡献是 $\binom{n-1+d}{n-1}$、最后被消去。
3. 代入 $\dim S_{d-j}=\binom{n-1+d-j}{n-1}$（并约定 $d<j$ 时该项为 $0$），即得所示公式。
   - *为什么*：由 $\dim S_m=\binom{n-1+m}{n-1}$ 直接代换；$d<j$ 时 $S_{d-j}=0$，按组合二项式约定取零。


出处：中译 p.33（式 (2)，及译注②）

### Betti 数与 Tor

$\beta_{pj}(X)=\dim_{\mathbb{C}}\mathrm{Tor}^S_p(S(X),\mathbb{C})_j$，即同调次数是合冲阶数 $p$、内部分次是 $j$；中译正文把两个指标写反（译注③）。

**证明状态：只引出处，原书不重证**


出处：中译 p.33（引 Eisenbud 交换代数）

## 易错点

- 把 $\beta_{pj}$ 与 $b_{i,j}=\beta_{i,i+j}$ 混用：$b_{0,2}=\beta_{0,2}$，但 $b_{1,1}=\beta_{1,2}$，第二下标的含义差一个 $i$。
- 式 (2) 的二项式下标：$\dim V=n$ 时是 $\binom{n-1+d-j}{n-1}$，原书按 $\mathbb{P}^n$ 印成 $\binom{n+d-j}{n}$（译注②），照抄会在具体算 Hilbert 函数时算错。
- 以为 Betti 数只是 Hilbert 函数的附带品：Hilbert 函数只给交错和，$\beta_{pj}$ 给的是分次结构，Green 猜想的全部内容都在分次层面。

## 相关卡

- [Koszul 对偶](../concepts/koszul-duality.md)
- [性质 (N_p)](../concepts/property-np.md)
- [Green 猜想](../concepts/greens-conjecture.md)
- [Petri 映射](../concepts/petri-map.md)

## 出处

- ch2 §2.1 合冲；中译 p.33（英文 PDF p.37），源码 `chapters/ch02.tex:126`
- ch2 §2.1 式 (2)；中译 p.33（英文 PDF p.37），源码 `chapters/ch02.tex:130`
