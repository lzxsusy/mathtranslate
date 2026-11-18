# 扭曲复形

> `seidel/concept/twisted-complex` ｜ track A ｜ draft

**一句话**：把链复形的分块微分换成满足广义 Maurer–Cartan 方程的下三角连接 δ；Tw A 由此容纳映射锥、直和与平移。

**自测**：为什么扭曲复形的微分不是「逐块相加」，而要写成连接 δ 并解 Maurer–Cartan 方程？

## 定义

$\A$ 上的预扭曲复形是 $(X,\delta_X)$，其中
$$X=\bigoplus_{i\in I}V^i\otimes X_i,\qquad \delta_X=(\delta^{ji}_X),\qquad \delta^{ji}_X=\sum_k\varphi^{ji}_k\otimes x^{ji}_k,$$
$V^i$ 是有限维分次向量空间、$X_i\in\A$，$\varphi^{ji}_k\in\Hom_\K(V^i,V^j)$、$x^{ji}_k\in\hom_\A(X_i,X_j)$，且 $|\varphi^{ji}_k|+|x^{ji}_k|=1$。
若 $\delta_X$ 严格下三角（存在有限递减滤过使各商上的诱导微分为零），并满足广义 Maurer–Cartan 方程
$$\sum_{r\ge1}\mu^r_{\Tw\A}(\delta_X,\ldots,\delta_X)=0,$$
则称 $(X,\delta_X)$ 为扭曲复形；它们构成 A∞ 范畴 $\Tw\A$。

记号：$I$ 有限；$\delta_X$ 的总次数为 $1$。在 dg 特例中把 $E_i$ 放在次数 $i$，则 $q_{ji}:E_i\to E_j$ 的内部次数为 $i-j+1$，总次数仍为 $1$。

## 要点

- 分次来自 $V^i$ 的平移；$\delta^{ji}$ 不是单一次数的态射，不能只记一个矩阵。
- 严格下三角保证 Maurer–Cartan 求和有限；没有它，方程只是形式级数。
- $\Tw\A$ 的复合被 $\delta$ 形变（原书 (3.20)），结合律等价于 $\delta$ 的 MC 方程——这是该构造的核心机制。

## 公式

$$\delta_X\in\hom^1_{\Tw\A}(X,X),\qquad \sum_{r\ge1}\mu^r(\delta_X,\ldots,\delta_X)=0$$
$$\text{dg 特例：}\ d_T=d+q,\qquad dq+q\circ q=0$$

## 定理与证明

### 映射锥是扭曲复形

设 $\A$ 是 dg 范畴，$f:X\to Y$ 是次数 $1$ 的闭态射。取 $X_0=Y$、$X_1=X$、$V^0=V^1=\K$，把 $\delta$ 的唯一非零分量取为 $\delta^{1,0}=f$，则 $(X,\delta)$ 是扭曲复形，其 $H^0$ 是映射锥 $\Cone(f)$。

（complete；来源：原书 p.43–44 §3l、p.35 §3e）

1. 总次数：$f$ 的次数为 $1$，$V^0\to V^1$ 的张量因子取次数 $0$，故 $\delta$ 的总次数为 $1$。  
   为什么：扭曲复形要求连接的总次数为 $1$；这里没有额外的平移。
2. 严格下三角：按 $F^0=X$、$F^1=V^1\otimes X$、$F^2=0$ 取滤过，商上微分为零。  
   为什么：$\delta$ 只有一个从第 $0$ 层到第 $1$ 层的分量，滤过逐层下降。
3. MC 方程：$\delta^2=0$（下三角），$d\delta=0$（$f$ 闭），故 $\sum_r\mu^r(\delta,\ldots,\delta)=0$ 只剩 $r=1,2$ 两项且相消。  
   为什么：高次项含 $\delta^2$ 因子；低次项是 $d\delta+\delta^2$。
4. 微分矩阵为 $\begin{pmatrix}d_Y&f\\0&d_X\end{pmatrix}$，其 $H^0$ 正是 $\Cone(f)$。  
   为什么：按 $Y\oplus X$ 分块直接读出映射锥的微分。

## 易错点

- $q_{ji}$ 的内部次数是 $i-j+1$，前提是 $E_i$ 放在次数 $i$；漏掉这个平移就会算出错误的次数。
- 预扭曲复形与扭曲复形不是一回事：下三角与 MC 方程是后者的额外条件。
- $\delta$ 与 $\A$ 的内部微分 $d_i$ 不是一回事；$d_i$ 只是 $\delta$ 中 $V^i$ 为一维时的特例。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§3l，p.43–44（原书 p.43–44 §3l）

关联：`seidel/concept/a-infinity-category`、`seidel/concept/karoubi-envelope`、`seidel/deriv/twisted-differential`

来源说明：原书 p.43–44 §3l（定义、MC 方程、复合 (3.20)）；译者注 A01-02（引言的简化说法）、A05-09。
