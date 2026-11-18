# 扭曲复形

> `seidel/concept/twisted-complex` ｜ track A ｜ draft

**一句话**：把链复形的分块微分换成满足广义 Maurer–Cartan 方程的下三角连接 δ；Tw A 由此容纳映射锥、直和与平移。

**自测**：为什么扭曲复形的微分不是「逐块相加」，而要写成连接 δ 并解 Maurer–Cartan 方程？

## 定义

$\A$ 上的预扭曲复形是 $(X,\delta_X)$，其中
$$X=\bigoplus_{i\in I}V^i\otimes X_i,\qquad \delta_X=(\delta^{ji}_X),\qquad \delta^{ji}_X=\sum_k\varphi^{ji}_k\otimes x^{ji}_k,$$
$V^i$ 是有限维分次向量空间、$X_i\in\A$，$\varphi^{ji}_k\in\Hom_\K(V^i,V^j)$、$x^{ji}_k\in\hom_\A(X_i,X_j)$，且 $|\varphi^{ji}_k|+|x^{ji}_k|=1$。
若 $\delta_X$ 严格下三角（存在有限递减滤过使各商上的诱导微分为零），并满足广义 Maurer–Cartan 方程
$$\sum_{r\ge1}\mu^r_{\dagger\A}(\delta_X,\ldots,\delta_X)=0,$$
则称 $(X,\delta_X)$ 为扭曲复形；它们构成 A∞ 范畴 $\Tw\A$。

记号：$I$ 有限；$\delta_X$ 的总次数为 $1$。在 dg 特例中把 $E_i$ 放在次数 $i$，则 $q_{ji}:E_i\to E_j$ 的内部次数为 $i-j+1$，总次数仍为 $1$。

## 要点

- 分次来自 $V^i$ 的平移；$\delta^{ji}$ 由若干满足 $|\varphi|+|x|=1$ 的项混合而成，双次数不固定，不能只按内部次数记账。
- 严格下三角保证 Maurer–Cartan 求和有限；没有它，方程只是形式级数。
- $\Tw\A$ 的复合被 $\delta$ 形变（原书 (3.20)），结合律等价于 $\delta$ 的 MC 方程——这是该构造的核心机制。

## 公式

$$\delta_X\in\hom^1_{\dagger\A}(X,X),\qquad \sum_{r\ge1}\mu^r_{\dagger\A}(\delta_X,\ldots,\delta_X)=0$$
$$\text{dg 特例：}\ d_T=d+q,\qquad dq+q\circ q=0$$

## 定理与证明

### 映射锥是扭曲复形

设 $\A$ 是 dg 范畴，$f:X\to Y$ 是次数 $1$ 的闭态射。取 $X_0=Y$、$X_1=X$、$V^0=V^1=\K$，把 $\delta$ 的唯一非零分量取为 $\delta^{0,1}=f$（由 $X_1=X$ 指向 $X_0=Y$），则 $(X,\delta)$ 是扭曲复形，其 $H^0$ 是映射锥 $\Cone(f)$。

（complete；来源：原书 p.43–44 §3l、p.35 §3e）

1. 总次数：$f$ 的次数为 $1$，$\varphi^{0,1}:\K\to\K$ 取次数 $0$，故 $\delta$ 的总次数为 $1$。  
   为什么：扭曲复形要求连接的总次数为 $1$；这里没有额外的平移。
2. 严格下三角：按 $F^0=V^0\otimes X_0\oplus V^1\otimes X_1$、$F^1=V^0\otimes X_0$、$F^2=0$ 取滤过，$\delta$ 把 $F^0$ 送入 $F^1$、把 $F^1$ 送入 $0$，故商上的诱导连接为零。  
   为什么：$\delta$ 只有分量 $\delta^{0,1}$，它严格降低滤过次数。
3. MC 方程：$\delta^2=0$（下三角），$d_Yf+fd_X=0$（$f$ 是次数 $1$ 的闭态射，即 $\mu^1_{\dagger\A}(\delta)=0$），故 $\sum_r\mu^r_{\dagger\A}(\delta,\ldots,\delta)$ 只剩 $r=1,2$ 两项且都为零。  
   为什么：$r\ge3$ 的项含 $\delta^2$ 因子而消失；$r=1$ 给 $d\delta+\delta d=0$，$r=2$ 给 $\delta^2=0$。
4. 微分矩阵为 $\begin{pmatrix}d_Y&f\\0&d_X\end{pmatrix}$，其 $H^0$ 正是 $\Cone(f)$。  
   为什么：按 $Y\oplus X$ 分块直接读出映射锥的微分。

## 易错点

- $q_{ji}$ 的内部次数是 $i-j+1$，前提是 $E_i$ 放在次数 $i$；漏掉这个平移就会算出错误的次数。
- 预扭曲复形与扭曲复形不是一回事：下三角与 MC 方程是后者的额外条件。
- $\delta$ 是连接（严格下三角、对角为零）；$\A$ 的内部微分 $d_i=\mu^1_{X_i}$ 不进入 $\delta$ 的分量，而是出现在 $\mu^1_{\dagger\A}(\delta)$ 里，扭曲复形的总微分是 $d+\delta$。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§3l，p.43–44（原书 p.43–44 §3l）

关联：`seidel/concept/a-infinity-category`、`seidel/concept/karoubi-envelope`、`seidel/deriv/twisted-differential`

来源说明：原书 p.43–44 §3l（定义、MC 方程、复合 (3.20)）；译者注 A01-02（引言的简化说法）、A05-09。
