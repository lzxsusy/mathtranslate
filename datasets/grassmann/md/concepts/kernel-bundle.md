# 核丛

> `grassmann/concept/kernel-bundle` · 轨道 2 · Koszul 上同调 · 状态 draft

> **先自测**：为什么 $\wedge^{p+1}M_L$ 的上同调能替代 $\wedge^{p+1}H^0(L)$ 的缩并？

## 一句话

整体生成线丛的截面求值映射的核 $M_L$ 是秩 $h^0(L)-1$ 的向量丛，把 Koszul 上同调写成它的外幂的上同调，是从 Betti 数走向族上计算的转换器。

## 定义

设 $L$ 是射影簇 $X$ 上整体生成的线丛，定义**核丛** $M_L:=\mathrm{Ker}\bigl(H^0(X,L)\otimes\mathcal{O}_X\xrightarrow{\mathrm{ev}}L\bigr)$，它是 $X$ 上秩为 $h^0(X,L)-1$ 的向量丛。对任意凝聚层 $\mathcal{F}$ 及 $p\ge0$、$q\in\mathbb{Z}$ 有短正合列 $0\to\wedge^{p+1}M_L\otimes\mathcal{F}\otimes L^{q-1}\to\wedge^{p+1}H^0(L)\otimes\mathcal{F}\otimes L^{q-1}\to\wedge^pM_L\otimes\mathcal{F}\otimes L^q\to0$。

**记号约定**：$\mathrm{ev}$ 为求值映射；$\det M_L=L^{-1}$。

## 要点（为什么需要它）

- 由 $0\to M_L\to H^0(L)\otimes\mathcal{O}\to L\to0$ 取行列式得 $\det M_L=L^{-1}$，于是 $\wedge^{r-1}M_L\cong M_L^{\vee}\otimes L^{-1}$（$r=\mathrm{rk}M_L$），这是例 2.2 与定理 2.8 中所有「外幂换对偶」的来源。
- 定理 2.6 给出两种写法：$\mathrm{coker}$ 形式便于算维数，$\ker$ 形式（长正合列）便于判消没。
- 取 $\mathcal{F}=\mathcal{O}_X$、$q=2$ 得 $K_{p,2}\cong\mathrm{coker}(\wedge^{p+1}H^0(L)\otimes H^0(L)\to H^0(\wedge^pM_L\otimes L^2))$，这正是定理 3.5 中向量丛 $\mathcal{B}$ 的定义。
- $L$ 必须整体生成：否则 $\mathrm{ev}$ 不满射，$M_L$ 只是子层而非丛，「秩 $h^0(L)-1$」不成立。

## 关键公式

$$
M_L:=\mathrm{Ker}\bigl(H^0(X,L)\otimes\mathcal{O}_X\xrightarrow{\mathrm{ev}}L\bigr)
$$

$$
0\to\wedge^{p+1}M_L\otimes\mathcal{F}\otimes L^{q-1}\to\wedge^{p+1}H^0(L)\otimes\mathcal{F}\otimes L^{q-1}\to\wedge^pM_L\otimes\mathcal{F}\otimes L^q\to0
$$

$$
\det M_L=L^{-1},\qquad \wedge^{r-1}M_L\cong M_L^{\vee}\otimes L^{-1}
$$

## 定理与证明（或缺口）

### 定理 2.6（Lazarsfeld）

记号同上。则 $K_{p,q}(X,\mathcal{F},L)\cong\mathrm{coker}\bigl(\wedge^{p+1}H^0(L)\otimes H^0(\mathcal{F}\otimes L^{q-1})\to H^0(\wedge^pM_L\otimes\mathcal{F}\otimes L^q)\bigr)\cong\ker\bigl(H^1(X,\wedge^{p+1}M_L\otimes\mathcal{F}\otimes L^{q-1})\to\wedge^{p+1}H^0(L)\otimes H^1(\mathcal{F}\otimes L^{q-1})\bigr)$。

**证明状态：完整**

1. 对 $0\to M_L\to H^0(L)\otimes\mathcal{O}_X\to L\to0$ 取外幂并张量 $\mathcal{F}\otimes L^{q-1}$，得中间项为 $\wedge^{p+1}H^0(L)$、两端为 $\wedge^{p+1}M_L$ 与 $\wedge^pM_L\otimes L$ 的短正合列。
   - *为什么*：外幂 $\wedge^{p+1}$ 把该正合列的核/上核恰写成相邻两阶外幂，扭上 $L$ 后即得所述的短正合列。
2. 取整体截面，Koszul 微分经 $\wedge^{p+1}H^0(L)\otimes H^0(\mathcal{F}\otimes L^{q-1})\to H^0(\wedge^pM_L\otimes\mathcal{F}\otimes L^q)$ 分解，故 $K_{p,q}$ 等于这个映射的上核。
   - *为什么*：Koszul 复形的微分按定义就是缩并复合乘法，而它在 $H^0$ 层面的像正是这个映射。
3. 对同一短正合列取上同调，连接同态把该映射的上核识别为 $H^1(\wedge^{p+1}M_L\otimes\mathcal{F}\otimes L^{q-1})\to\wedge^{p+1}H^0(L)\otimes H^1(\mathcal{F}\otimes L^{q-1})$ 的核。
   - *为什么*：长正合列中「中间项的上核」与「下一项映射的核」自然同构，这一步不依赖任何额外选择。


出处：中译 p.36（定理 2.6，引 Lazarsfeld 1989）

## 易错点

- 把 $M_L$ 写成求值映射的余核：余核是 $L$ 本身，核才是 $M_L$；两者维数差了一整条正合列。
- $h^0(L)=1$ 时 $M_L=0$，此时 $\wedge^pM_L=0$（$p\ge1$）、$K_{0,q}=H^0(L^q)$，别把「秩 $0$ 的丛不存在」当成反例。
- 短正合列两端的 twist 是 $L^{q-1}$ 与 $L^q$，写成一个 $L^q$ 会同时错两处指标。

## 相关卡

- [Koszul 对偶](../concepts/koszul-duality.md)
- [Koszul 闭链与退化轨迹](../concepts/koszul-cycle.md)
- [Green 维数公式](../concepts/greens-dimension-formula.md)
- [对偶张成](../concepts/dual-span.md)

## 出处

- ch2 §2.3 核丛；中译 p.35（英文 PDF p.39），源码 `chapters/ch02.tex:209`
- ch2 §2.3 定理 2.6；中译 p.36（英文 PDF p.40），源码 `chapters/ch02.tex:225`
