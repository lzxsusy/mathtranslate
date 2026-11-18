# 有向 A∞ 范畴

> `seidel/concept/directed-a-infinity-category` ｜ track A ｜ draft

**一句话**：对象带偏序、反向 hom 全为零的严格含幺 $A_\infty$ 范畴；高阶运算被偏序切成有限块，故必拟同构于 hom 有限维的 dg 范畴。

**自测**：为什么只要对象带一个偏序、反向 hom 为零，高阶 $A_\infty$ 结构就能被彻底消去而不撑大 hom 空间？

## 定义

有向 $A_\infty$ 范畴是带 $m$ 个对象 $Y_1,\ldots,Y_m$（连同这个排序）的严格含幺 $A_\infty$ 范畴 $\A^\to$，满足
$$\hom_{\A^\to}(Y_i,Y_j)=\begin{cases}0,&i>j,\\ \K\cdot e_{Y_i},&i=j,\\ \text{$\K$ 上有限维},&i<j.\end{cases}$$
因严格含幺，只需给出偏序允许的那些运算
$$\mu^d:\hom(Y_{i_{d-1}},Y_{i_d})\otimes\cdots\otimes\hom(Y_{i_0},Y_{i_1})\longrightarrow\hom(Y_{i_0},Y_{i_d})[2-d],\qquad i_0<\cdots<i_d,$$
其余合成的定义域里必含一个零因子，从而自动为零。于是整个 $\A^\to$ 只由有限多个 $\K$ 中的数（(5.30) 的矩阵系数）决定。
$\Tw\A^\to$ 中的对象写成 $X=\bigoplus_{i=1}^m V^i\otimes Y_i$，微分 $\delta_X=(\delta_X^{ji})$ 自动满足下三角条件；任意 $X$ 都同构于对角微分全零的 $\tilde X$，再用 Postnikov 分解 (5.32) 逐层重建。

记号：$m=|\mathrm{Ob}\,\A^\to|$；$\mu^d$ 的定义域要求 $i_0<\cdots<i_d$，这正是 (5.30) 的下标范围；有向性也写作「$\hom(Y_i,Y_j)=0$ 当 $i>j$」。

## 要点

- 有向性 = 偏序 + 严格含幺：$i>j$ 时 hom 为零，$i=j$ 时只有单位元，$i<j$ 时有限维。次序是范畴数据的一部分，不是附加结构。
- 整个范畴只由有限多个数决定：所有 $\mu^d$ 都是 (5.30) 型的有限维矩阵，没有无限维的合成空间，所以「消去高阶运算」不会撑大 hom。
- 推论 5.27：任意有向 $A_\infty$ 范畴都拟同构于仍有向的 dg 范畴，且 hom 仍有限维。一般 $A_\infty$ 范畴只能做到 dg 化（推论 2.14），保不住有限维。
- 证明走的是模范畴：$P=\mathrm{mod}(\A^\to)^{fin}$ 既严格含幺又只有有限维 hom，$I(Y_k)$ 在其中构成例外集（推论 5.26：$P$ 是 $\A^\to$ 的三角化包络）。
- $\Tw\A^\to$ 的对象可化为对角微分全零再逐层搭回：$X_k\cong\Cone(S^{-1}X_{k-1}\to Z_k\otimes Y_k)$，这就是 (5.32) 的 Postnikov 分解。

## 公式

$$\hom_{\A^\to}(Y_i,Y_j)=0\quad(i>j),\qquad \hom(Y_i,Y_i)=\K\cdot e_{Y_i},\qquad \dim_\K\hom(Y_i,Y_j)<\infty\ (i<j)$$
$$\mu^d:\hom(Y_{i_{d-1}},Y_{i_d})\otimes\cdots\otimes\hom(Y_{i_0},Y_{i_1})\to\hom(Y_{i_0},Y_{i_d})[2-d],\qquad i_0<\cdots<i_d\quad(5.30)$$
$$X=\bigoplus_{i=1}^m V^i\otimes Y_i\in\Tw\A^\to,\qquad \delta_X=(\delta_X^{ji})\ \text{下三角}$$
$$\A^\to\ \rightsquigarrow\ \B:\quad \B\ \text{有向 dg},\ \dim_\K\hom_\B<\infty,\ \A^\to\ \text{与}\ \B\ \text{拟等价}\quad(5.27)$$

## 定理与证明

### 推论 5.27（有向范畴可 dg 化且保有限维）

设 $\A^\to$ 是有向 $A_\infty$ 范畴。则存在有向的 dg 范畴 $\B$（$d>2$ 时 $\mu^d_\B=0$）以及拟等价 $\A^\to\to\B$，且 $\hom_\B$ 仍为有限维。

（complete；来源：原书 p.87 §5p）

1. 令 $P=\mathrm{mod}(\A^\to)^{fin}$ 为有限维严格含幺 $A_\infty$ 模范畴；有向性保证 $\hom_P(M_0,M_1)$ 有限维。  
   为什么：模的 hom 由有限多个 (5.30) 型运算的矩阵系数控制，而每个这样的空间都有限维。
2. Yoneda 模 $I(Y_k)=\hom(-,Y_k)$ 在 $P$ 中构成例外集。  
   为什么：$\hom(Y_k,Y_l)$ 的偏序支撑使 $k>l$ 时为零、$k=l$ 时只有单位元，正是例外集的两条要求。
3. 取由这些 $I(Y_k)$ 张成的有向 $A_\infty$ 子范畴 $\B\subset P$；它继承严格含幺与有限维 hom。  
   为什么：子范畴的 hom 空间是 $P$ 中 hom 空间的直和项，有限维性自动保持。
4. $\B$ 中 $d>2$ 的高阶复合为零，故 $\B$ 是 dg 范畴。  
   为什么：这是 $A_\infty$ 模范畴的一般性质：模范畴里的高阶运算可整体取零而不改变同调。
5. 由推论 5.26，$P$ 是 $\A^\to$ 的三角化包络，$\Tw\B\simeq P\simeq\Tw\A^\to$，故 $\A^\to$ 与 $\B$ 拟等价。  
   为什么：三角化包络由同调范畴决定；两个范畴有等价的包络即在同一拟等价类中。

缺口：第 4 步原书只用一句「as is generally true for categories of modules」带过；要写全需说明模范畴的 $d\ge3$ 运算可按严格含幺性规范地取零。

### (5.30) 决定整个范畴

有向 $A_\infty$ 范畴的 $A_\infty$ 结构等价于给每族下标 $i_0<\cdots<i_d$ 一组 $\K$ 中的矩阵系数；其余分量由零因子与严格含幺强制为零。

（complete；来源：原书 p.80–81 §5m）

1. 严格含幺把 $\mu^1$ 与 $\mu^2$ 中含单位元的分量固定下来。  
   为什么：严格含幺要求 $\mu^2(e,a)=a$、$\mu^2(a,e)=(-1)^{|a|}a$，而 $d\ge3$ 时含单位元的分量为零。
2. 任何 $\mu^d$ 只要有一个因子落在 $i>j$ 的 hom 空间里，该分量必为零。  
   为什么：零空间作张量因子给出零映射，故合成为零。
3. 剩下的分量都被下标 $i_0<\cdots<i_d$ 标定，每个是有限维空间之间的线性映射。  
   为什么：有限维线性映射由矩阵系数决定，共有限多个 $\K$ 元素。

缺口：「等价于给一组系数」指在固定对象与偏序下；换对象或换偏序会得到拟同构但不同的范畴。

## 易错点

- 有向性不止「hom 有限维」：还要求 $i=j$ 时只有 $\K e$、$i>j$ 时为零，并且次序是范畴的一部分。只证了有限维不算有向。
- dg 化不唯一：不同选择（不同的消去次序）给出拟同构但不同构的 dg 范畴，别把 $\B$ 当成典范对象。
- 推论 5.27 说的是「拟同构于有向 dg 范畴」，不是同构；同调范畴不变，链层代表元已经换掉了。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§5m，p.80–81（原书 p.80–81 §5m）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§5p，p.86–87（原书 p.86–87 §5p）

关联：`seidel/deriv/directed-dg`、`seidel/concept/twisted-complex`、`seidel/concept/a-infinity-category`、`seidel/concept/fukaya-category`

来源说明：原书 p.80 定义、(5.30) 在 p.81、推论 5.27 在 p.87 §5p；译者注 A03-17（Seidel §5p 推论 5.27 与推论 2.14，A 级）。
