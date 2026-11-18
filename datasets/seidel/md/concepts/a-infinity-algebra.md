# A∞ 代数

> `seidel/concept/a-infinity-algebra` ｜ track A ｜ draft

**一句话**：带一串多重线性运算 μ^d 的分次向量空间：μ¹ 是微分，μ² 是同伦意义下的乘法，高阶 μ^d 修正结合律的失效。

**自测**：为什么 Fukaya 范畴里的复合只在同伦意义下结合，却仍能当成代数对象来算？

## 定义

$A=\bigoplus_{k\in\Z}A^k$ 是分次向量空间，带一族多重线性映射 $\mu^d:A^{\otimes d}\to A$（$d\ge1$），$\deg\mu^d=2-d$，并对每个 $d\ge1$ 满足
$$\sum_{r+s+t=d}(-1)^{\star_r}\mu^{r+1+t}(a_d,\ldots,a_{r+s+1},\mu^s(a_{r+s},\ldots,a_{r+1}),a_r,\ldots,a_1)=0,\qquad \star_r=|a_1|+\cdots+|a_r|-r .$$
$d=1$ 时化为 $\mu^1\mu^1=0$；$d=2$ 时化为带 Koszul 符号的 Leibniz 规则；$d\ge3$ 的项度量 $\mu^2$ 偏离严格结合律的程度。

记号：$\mu^d$ 的次数是 $2-d$；$a_i$ 的次数记作 $|a_i|$；$\star_r=|a_1|+\cdots+|a_r|-r$，其中 $r$ 是内层运算右侧的元素个数（原书 (1.2) 的这个符号记作 $\star_n$）。

## 要点

- $\mu^1$ 是微分，$(\mu^1)^2=0$；$\mu^2$ 是乘法，但它只在同伦意义下结合。
- dg 代数是 $\mu^{\ge3}=0$ 的特例；A∞ 代数是它的同伦放宽，因此任何 dg 代数都可看作 A∞ 代数。
- 本书把 Fukaya 范畴的复合放到这一层：链层次上没有严格结合的 $\mu^2$，只有 $\mu^3$ 等同伦修正。

## 公式

$$\sum_{r+s+t=d}(-1)^{\star_r}\mu^{r+1+t}(a_d,\ldots,a_{r+s+1},\mu^s(a_{r+s},\ldots,a_{r+1}),a_r,\ldots,a_1)=0,\qquad \star_r=|a_1|+\cdots+|a_r|-r$$
$$\mu^1\circ\mu^1=0,\qquad \mu^1\mu^2(a_2,a_1)=(-1)^{|a_1|}\mu^2(\mu^1a_2,a_1)-\mu^2(a_2,\mu^1a_1)$$

## 定理与证明

### 最低阶的 A∞ 关系

$d=1$ 的 A∞ 关系等价于 $\mu^1\mu^1=0$；$d=2$ 的关系等价于 $\mu^1$ 是 $\mu^2$ 的导子（带 Koszul 符号）。

（complete；来源：原书 p.3、p.7–8 §1）

1. 在 $d=1$ 的求和中，只有 $s=1,r=t=0$ 一项合法，其余项需要 $s\ge2$ 或 $s=0$。  
   为什么：求和的指标满足 $r+s+t=1$ 且 $s\ge1$，故唯一可能是 $(r,s,t)=(0,1,0)$。
2. 这一项就是 $\mu^1(\mu^1(a_1))=0$，即 $(\mu^1)^2=0$。  
   为什么：代入关系式，外层取 $\mu^{1}$、内层取 $\mu^{1}$。
3. $d=2$ 时合法的 $(r,s,t)$ 为 $(0,2,0)$、$(0,1,1)$、$(1,1,0)$，分别给 $\mu^1\mu^2$ 与两个 $\mu^2(\mu^1\otimes\id)$、$\mu^2(\id\otimes\mu^1)$ 项。  
   为什么：三项相加为零，移项并用 $\star_r=|a_1|+\cdots+|a_r|-r$ 定符号，即得 $\mu^1\mu^2(a_2,a_1)=(-1)^{|a_1|}\mu^2(\mu^1a_2,a_1)-\mu^2(a_2,\mu^1a_1)$。

## 易错点

- $\mu^d$ 的次数是 $2-d$；写成 $d-2$ 会把所有公式的次数弄反。
- 符号约定因作者而异。本书采用 “bar-convention”（原书 p.9 注 (iv)），符号由 $\star_r=|a_1|+\cdots+|a_r|-r$ 给出，而不是常见的 $(-1)^{r+st}$；直接套用别处的 A∞ 关系常差一个符号。
- 「非含幺」只表示定义里不把单位元列为数据，不表示单位元不存在（原书 p.8 Remark 1.1(i)：应读作 “not necessarily unital”）。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§1，p.3–8（原书 p.3–8 §1）

关联：`seidel/concept/a-infinity-category`、`seidel/concept/twisted-complex`、`seidel/deriv/mu-d-grading`

来源说明：原书 p.3（定义）、p.7–8（非含幺与符号）；译者注 A01-01（nLab A-infinity-algebra，B 级）。
