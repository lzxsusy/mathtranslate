# A∞ 范畴

> `seidel/concept/a-infinity-category` ｜ track A ｜ draft

**一句话**：对象之间的 hom 是分次向量空间，复合是一族满足 A∞ 关系的多重线性映射；定义不要求恒等态射，含幺性是可后加的结构。

**自测**：把范畴的复合换成「只在同伦意义下结合」的一族运算，会得到什么，又丢掉什么？

## 定义

A∞ 范畴 $\A$ 由下列数据组成：对象集 $\mathrm{Ob}\A$；每对对象 $X,Y$ 一个分次向量空间 $\hom_\A(X,Y)$；对每个 $d\ge1$ 与对象 $X_0,\ldots,X_d$，多重线性映射
$$\mu^d:\hom_\A(X_{d-1},X_d)\otimes\cdots\otimes\hom_\A(X_0,X_1)\longrightarrow\hom_\A(X_0,X_d),\qquad \deg\mu^d=2-d,$$
满足与 A∞ 代数相同的求和关系。恒等态射不列为数据；原书的「非含幺」正是指「不必含幺」（p.8 Remark 1.1(i)），本书另在 §2 区分严格含幺、同伦含幺、上同调含幺（c-unital）三个层次。

记号：$\hom_\A(X,Y)$ 的分次记作 $\hom^k_\A(X,Y)$；$H^0(\A)$ 表示以同样对象、以 $H^0(\hom_\A(X,Y))$ 为态射的普通范畴。

## 要点

- $\hom$ 是分次向量空间而不是集合；对象之间可以没有态射，也可以有正次数态射。
- 取 $0$ 次上同调得到普通范畴 $H^0(\A)$，这是把 A∞ 数据「压回」经典范畴的标准做法。
- 本书区分严格含幺、同伦含幺、上同调含幺三个层次（§2）；Fukaya 范畴只满足最后一种。

## 公式

$$\mu^d:\hom(X_{d-1},X_d)\otimes\cdots\otimes\hom(X_0,X_1)\to\hom(X_0,X_d),\qquad \deg=2-d$$

## 定理与证明

### 取上同调得到普通范畴

若 $\A$ 是上同调含幺的 A∞ 范畴，则以 $\mathrm{Ob}\A$ 为对象、以 $H^0(\hom_\A(X,Y))$ 为态射、以 $\mu^2$ 诱导的映射为复合，得到普通范畴 $H^0(\A)$。

（sketch；来源：原书 p.7–8、p.23 §2）

1. $\mu^1$ 是微分，故可以对每个 $\hom_\A(X,Y)$ 取上同调。  
   为什么：$d=1$ 的 A∞ 关系给出 $(\mu^1)^2=0$。
2. $\mu^2$ 诱导 $H^0(\hom(X,Y))\otimes H^0(\hom(Y,Z))\to H^0(\hom(X,Z))$。  
   为什么：$\mu^1$ 是 $\mu^2$ 的导子，故 $\mu^2$ 把闭链送到闭链、把边界送到边界。
3. 诱导的复合结合，单位元由同伦含幺给出。  
   为什么：$d=3$ 的关系中带 $\mu^1$ 的项在同调上消失，剩下的两项给出 $H^0$ 上的严格结合律（对 $0$ 次类符号为 $+1$）。

缺口：第 3 步只引了 $d=3$ 的关系；把其中带 $\mu^1$ 的项逐项化成边界（从而得到同调上的严格结合律）此处从略。

## 易错点

- 复合顺序：$a_1$ 靠近源点、$a_d$ 靠近终点，$\mu^2(a_2,a_1)$ 表示先 $a_1$ 后 $a_2$；把两个变量的位置写反会改符号。
- 反范畴不是简单地把 $\hom(X,Y)$ 换成 $\hom(Y,X)$，还要对 $\mu^d$ 加 $(-1)^{\star_d}$ 的 Koszul 符号，$\star_d=|a_1|+\cdots+|a_d|-d$（原书 p.8）。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§1–2，p.7–23（原书 p.7–8 §1、p.23 §2）

关联：`seidel/concept/a-infinity-algebra`、`seidel/concept/fukaya-category`、`seidel/concept/twisted-complex`

来源说明：原书 p.7–8（定义与非含幺）、p.23（三种含幺）；译者注 A01-01、A02-05。
