# Koszul 上同调

> `grassmann/concept/koszul-cohomology` · 轨道 A · 跨章基础 · 状态 draft

> **先自测**：Koszul 上同调为什么能把极小自由分解里的 Betti 数，改写成只依赖层与截面乘法的对象？

## 一句话

由缩并映射与乘法映射构成的双复形的上同调；p 记外幂次数、q 记扭次数，把曲线的合冲翻译成可计算的层上同调。

## 定义

设 $X$ 是复射影簇，$L\in\Pic(X)$，$\mathcal F$ 是凝聚层，$p\ge0$、$q\in\mathbb Z$。缩并映射 $\bigwedge^{p+1}H^0(L)\otimes H^0(L)^\vee\to\bigwedge^pH^0(L)$ 与乘法 $H^0(L)\otimes H^0(\mathcal F\otimes L^{q-1})\to H^0(\mathcal F\otimes L^q)$ 组成复形 $$\bigwedge^{p+1}H^0(L)\otimes H^0(\mathcal F\otimes L^{q-1})\to\bigwedge^pH^0(L)\otimes H^0(\mathcal F\otimes L^q)\to\bigwedge^{p-1}H^0(L)\otimes H^0(\mathcal F\otimes L^{q+1}),$$ 其中间项处的上同调记作 $K_{p,q}(X,\mathcal F,L)$；$\mathcal F=\mathcal O_X$ 时简记 $K_{p,q}(X,L)$。

**记号约定**：$p$ 数用了多少个线性形式（外幂次数），$q$ 数把 $L$ 乘进 $\mathcal F$ 几次（扭次数）；$q$ 可以取负。

## 要点（为什么需要它）

- $p$ 与 $q$ 是两个独立的次数，没有「总次数 $p+q$」的读法；角色读反会让整张 Betti 表错位一格（批注 1）。
- 当 $L$ 充分正、$X$ 射影正规时，$K_{p,q}$ 是极小分解的对应分次分支；$\mathcal F=\mathcal O_X$ 时退化为 Green 的 $K_{p,q}(X,L)$。
- 例 2.1：$L$ 充裕时，$L$ 正规生成当且仅当对所有 $q\ge2$ 有 $K_{0,q}(X,L)=0$。
- 定理 2.6（核丛刻画）把 $K_{p,q}$ 写成截面乘法的上核，从而可以搬到族上、算退化轨迹的虚类（§3）。

## 关键公式

$$
\bigwedge^{p+1}H^0(L)\otimes H^0(\mathcal F\otimes L^{q-1})\to\bigwedge^pH^0(L)\otimes H^0(\mathcal F\otimes L^q)
$$

$$
K_{p,q}(X,\mathcal F,L)\cong\operatorname{coker}\bigl(\bigwedge^{p+1}H^0(L)\otimes H^0(\mathcal F\otimes L^{q-1})\to H^0(\bigwedge^pM_L\otimes\mathcal F\otimes L^q)\bigr)
$$

## 定理与证明（或缺口）

### 定理 2.6（Lazarsfeld）

记号同上，$M_L=\operatorname{Ker}(H^0(L)\otimes\mathcal O_X\to L)$。则 $K_{p,q}(X,\mathcal F,L)\cong\operatorname{coker}\bigl(\bigwedge^{p+1}H^0(L)\otimes H^0(\mathcal F\otimes L^{q-1})\to H^0(\bigwedge^pM_L\otimes\mathcal F\otimes L^q)\bigr)\cong\ker\bigl(H^1(\wedge^{p+1}M_L\otimes\mathcal F\otimes L^{q-1})\to\wedge^{p+1}H^0(L)\otimes H^1(\mathcal F\otimes L^{q-1})\bigr)$。

**证明状态：完整**

1. 由 $M_L\subset H^0(L)\otimes\mathcal O_X$ 的外幂过滤，得短正合列 $0\to\wedge^{p+1}M_L\otimes\mathcal F\otimes L^{q-1}\to\wedge^{p+1}H^0(L)\otimes\mathcal F\otimes L^{q-1}\to\wedge^pM_L\otimes\mathcal F\otimes L^q\to0$。
   - *为什么*：把 $\wedge^{p+1}(H^0(L)\otimes\mathcal O_X)$ 按「用 $M_L$ 替换几个因子」分层，第一层商恰为 $\wedge^pM_L\otimes L$。
2. 取整体截面，Koszul 微分经 $\wedge^{p+1}H^0(L)\otimes H^0(\mathcal F\otimes L^{q-1})\to H^0(\wedge^pM_L\otimes\mathcal F\otimes L^q)$ 分解。
   - *为什么*：这使 $K_{p,q}$ 恰好等于该映射的上核，即第一个同构。
3. 对上式取上同调长正合列，$K_{p,q}$ 又是连接映射 $H^0(\wedge^pM_L\otimes\cdots)\to H^1(\wedge^{p+1}M_L\otimes\cdots)$ 的核。
   - *为什么*：长正合列把上核与连接映射的核等同，得第二个同构；coker 形式用来造丛，ker 形式用来算维数。


出处：中译 p.35（§2.3 定理 2.6，Lazarsfeld）

## 易错点

- 把 $K_{p,q}$ 读成「$p$ 阶合冲的 $q$ 次分支」：$p$ 是外幂次数、$q$ 是扭次数，二者不同次（批注 1）。
- 把 $q<0$ 的项当成零：只要 $L^q$ 有意义，$q$ 可取负，消没陈述里不能默默略去这些位置。
- 把 $K_{0,2}=0$ 直接当作 $\nu_2$ 是同构：$K_{0,2}=\operatorname{coker}(\operatorname{Sym}^2H^0(L)\to H^0(L^2))$，只有两空间同维时「不满射」才等价于「不同构」（批注 8）。

## 相关卡

- [极小分次自由分解与分次 Betti 数](../concepts/graded-minimal-resolution-and-betti-numbers.md)
- [核丛](../concepts/kernel-bundle.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch2 §2.2 Koszul 上同调的定义；中译 p.34（英文 PDF p.38），源码 `chapters/ch02.tex:148`
