# Koszul 对偶

> `grassmann/concept/koszul-duality` · 轨道 2 · Koszul 上同调 · 状态 draft

> **先自测**：指标位移 $p\mapsto r-n-p$ 与 $q\mapsto n+1-q$ 分别来自哪一次对偶？

## 一句话

把 $K_{p,q}(X,L)$ 与 $K_{r-n-p,n+1-q}(X,K_X,L)$ 配对的对偶定理，使非消没与消没成为同一事实的两种写法，是 Green 猜想两种形式的桥梁。

## 定义

设 $L$ 是 $n$ 维光滑射影簇 $X$ 上整体生成的线丛，$r:=\dim|L|$。若 $H^i(X,L^{q-i})=H^i(X,L^{q-i+1})=0$（$i=1,\dots,n-1$），则 **Koszul 对偶**（定理 2.7）为 $K_{p,q}(X,L)^{\vee}\cong K_{r-n-p,n+1-q}(X,K_X,L)$，其中第三个参数表示 twist 所用的线丛仍是 $L$。

**记号约定**：$K_{p,q}(X,K_X,L)$：系数丛取 $K_X$、twist 取 $L$ 的 Koszul 上同调。

## 要点（为什么需要它）

- $p$ 的位移来自外幂对偶：$\wedge^{p+1}H^0(L)^{\vee}\cong\wedge^{r-p}H^0(L)$（因 $\dim H^0(L)=r+1$），再平移 $n$ 是 Serre 对偶带来的维数。
- $q$ 的位移来自 Serre 对偶：$H^0(L^{q-1})$ 被换成 $H^n(K_X\otimes L^{1-q})$，于是「第 $q$ 层 twist」变成「第 $n+1-q$ 层」。
- 曲线 $n=1$ 时假设对 $i=1,\dots,n-1$ 是空条件，故对任何整体生成线丛成立；取 $q=1$ 得 $K_{p,1}(C,L)^{\vee}\cong K_{r-1-p,1}(C,K_C,L)$，这是定理 2.8 证明的第一行。
- 对典范曲线，$b_{p,q}=\dim K_{p,q}(C,K_C)$ 排成 Betti 表后关于中心对称：$b_{i,j}=b_{g-2-i,3-j}$，所有未标出的项为零。

## 关键公式

$$
K_{p,q}(X,L)^{\vee}\cong K_{r-n-p,\,n+1-q}(X,K_X,L)
$$

$$
K_{p,1}(C,L)^{\vee}\cong K_{r-1-p,\,1}(C,K_C,L)
$$

$$
b_{i,j}=b_{g-2-i,\,3-j}
$$

## 定理与证明（或缺口）

### 定理 2.7（Koszul 对偶）

设 $L$ 是 $n$ 维光滑射影簇 $X$ 上整体生成的线丛，$r=\dim|L|$。若 $H^i(X,L^{q-i})=H^i(X,L^{q-i+1})=0$ 对 $i=1,\dots,n-1$ 成立，则 $K_{p,q}(X,L)^{\vee}\cong K_{r-n-p,n+1-q}(X,K_X,L)$。

**证明状态：提纲（有缺口）**


> **缺口**：原文把它作为定理 2.6 的推论一句话带过，没有写出证明。缺的是把 $\wedge^{p}M_L$ 的对偶写成 $\wedge^{r-p}M_L^{\vee}\otimes\det M_L$、再对 Koszul 复形逐项取 $\mathbb{C}$-对偶并与 Serre 对偶配对这两步；两处指标位移正是在这两步里各出现一次。


出处：中译 p.36（定理 2.7，引 Green 1984）

### 例 2.2（$H^1(\mathcal{O}_X)$ 的 Koszul 解释）

若 $L$ 整体生成且 $H^1(X,L)=0$，则 $H^1(X,\mathcal{O}_X)\cong K_{h^0(L)-2,2}(X,L)$。特别地，曲线的亏格可以从非特殊丛的 Koszul 上同调读出。

**证明状态：完整**

1. 记 $r=h^0(L)-1$。定理 2.6 的 $\mathrm{coker}$ 形式取 $p=r-1$、$q=2$：$K_{r-1,2}\cong\mathrm{coker}\bigl(\wedge^{r}H^0(L)\otimes H^0(L)\to H^0(\wedge^{r-1}M_L\otimes L^{2})\bigr)$。
   - *为什么*：$M_L$ 秩为 $r$，$\wedge^{r-1}M_L\cong M_L^{\vee}\otimes\det M_L^{-1}$，而 $\wedge^rH^0(L)\cong H^0(L)^{\vee}$。
2. 由 $\det M_L=L^{-1}$ 得 $\wedge^{r-1}M_L\otimes L^{2}\cong M_L^{\vee}\otimes L$，故 $K_{r-1,2}\cong\mathrm{coker}\bigl(H^0(L)^{\vee}\otimes H^0(L)\to H^0(M_L^{\vee}\otimes L)\bigr)$。
   - *为什么*：把 $\det M_L=L^{-1}$ 代入上一步的外幂同构，$L^{-1}\otimes L^{2}=L$。
3. 对 $0\to M_L\to H^0(L)\otimes\mathcal{O}_X\to L\to0$ 取对偶并扭 $L$，得 $0\to\mathcal{O}_X\to H^0(L)^{\vee}\otimes L\to M_L^{\vee}\otimes L\to0$；取上同调并用 $H^1(X,L)=0$，得上核 $\cong H^1(X,\mathcal{O}_X)$。
   - *为什么*：长正合列中 $H^1(H^0(L)^{\vee}\otimes L)=H^0(L)^{\vee}\otimes H^1(L)=0$，故 $H^0(M_L^{\vee}\otimes L)$ 的上核就是 $H^1(\mathcal{O}_X)$。


出处：中译 p.34（例 2.2，引 ApN08）

## 易错点

- 定理 2.7 的消没假设在曲线（$n=1$）上是空条件，但在曲面（$n=2$）上必须真的验证 $H^1(X,L^{q-1})$ 与 $H^1(X,L^{q})$，不能默认。
- $K_{p,q}(X,K_X,L)$ 的第三个参数是 twist 用的 $L$，系数丛才是 $K_X$；写成 $K_{p,q}(X,K_X)$ 会丢掉全部位移信息。
- Betti 表的对称是 $q\mapsto3-q$，定理 2.7 给的是 $q\mapsto n+1-q=2-q$：对 $K_C$ 差一次平移（Gorenstein 自对偶），原文没有解释，别把两个公式混用。

## 相关卡

- [核丛](../concepts/kernel-bundle.md)
- [性质 (N_p)](../concepts/property-np.md)
- [Green 维数公式](../concepts/greens-dimension-formula.md)
- [Brill–Noether 数 $\beta$](../concepts/brill-noether-number.md)

## 出处

- ch2 §2.4 对偶定理；中译 p.36（英文 PDF p.40），源码 `chapters/ch02.tex:235`
- ch2 §2.2 例 2.2；中译 p.34（英文 PDF p.38），源码 `chapters/ch02.tex:176`
