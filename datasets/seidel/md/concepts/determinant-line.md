# 行列式线

> `seidel/concept/determinant-line` ｜ track B ｜ draft

**一句话**：Fredholm 算子的行列式线 $\det(D)=\lambda^{\mathrm{top}}(\operatorname{coker}D)^\vee\otimes\lambda^{\mathrm{top}}(\ker D)$；Cauchy–Riemann 算子的行列式线为模空间提供定向。

**自测**：为什么计数全纯条带时能谈「带符号的点数」，符号从哪里来？

## 定义

对 Fredholm 算子 $D:H\to K$，定义
$$\det(D)=\lambda^{\mathrm{top}}(\operatorname{coker}D)^\vee\otimes\lambda^{\mathrm{top}}(\ker D).$$
对全纯条带的 $\bar\partial$-算子，$\det(D)$ 随参数构成线丛；沿模空间的一个连通分支取定其平凡化，即得到该分支的定向。模空间零维时，每个点带 $\pm1$，求和即带符号计数。

记号：$\lambda^{\mathrm{top}}$ 表示最高外幂；$(-)^\vee$ 是对偶。原书把 $(\operatorname{coker}D)^\vee$ 写在前面；就定向而言对偶冗余，交换因子只差 Koszul 符号。

## 要点

- $\det$ 对直和满足 Koszul 符号下的同构 $\det(D_1\oplus D_2)\cong\det(D_1)\otimes\det(D_2)$。
- 对 $\bar\partial$ 算子，$\ker$ 是全纯截面、$\operatorname{coker}$ 是 $(0,1)$-形式的障碍；指数由 Riemann–Roch/Atiyah–Singer 给出。
- 定向线的相容性（gluing）正是 $\mu^1\mu^1=0$ 中符号相消的来源。

## 公式

$$\det(D_1\oplus D_2)\cong\det(D_1)\otimes\det(D_2),\qquad\text{符号 }(-1)^{\dim\operatorname{coker}D_2\cdot\operatorname{index}D_1}$$
$$\operatorname{index}D=\dim\ker D-\dim\operatorname{coker}D$$

## 定理与证明

### 行列式线与定向

若 $\det(D)$ 已平凡化，则模空间 $\M$ 的每个零维正则点带符号 $\pm1$；粘合公式使带符号计数与边界定向相容。

（sketch；来源：原书 §11a（p.149–152））

1. 把 $\M$ 的切空间等同于 $\ker D$（模去无穷小自同构），其定向由 $\det(D)$ 的平凡化给出。  
   为什么：指数定理把模空间的维数与 $\operatorname{index}D$ 联系起来。
2. 零维且正则时 $\operatorname{coker}D=0$、$\operatorname{index}D=0$，故 $\ker D=0$，$\det(D)$ 的平凡化给出一个符号。  
   为什么：正则性排除 $\operatorname{coker}$，指数为零排除 $\ker$。
3. 边界粘合对应 $\det$ 的张量积同构，故边界两端的符号相反。  
   为什么：Koszul 符号规则保证定向在粘合处相消。

缺口：完整构造见原书 §11a–11d。

## 易错点

- 原书为与复行列式线类比把 $\operatorname{coker}$ 写成对偶形式；就定向而言对偶是冗余的（p.150 明说），漏掉它并不改变定向。
- Koszul 符号来自把向量按奇元素处理；交换两个因子会差一个符号。
- 复行列式线与实行列式线不同；本书用的是实指数与实定向。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§11a，p.149–152（原书 p.149 §11a）

关联：`seidel/concept/floer-complex`、`seidel/concept/maslov-index`、`seidel/deriv/twisted-differential`

来源说明：据原书 §11a（p.149–152）转述；译者注 A06-xx。
