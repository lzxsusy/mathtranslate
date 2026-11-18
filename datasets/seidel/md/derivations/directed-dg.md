# directed A∞ 范畴为何可换成 dg 范畴

> `seidel/deriv/directed-dg` ｜ track A ｜ draft

**目标**：证明：有限 directed A∞ 范畴 $\B$ 拟同构于一个 dg 范畴，其 hom 空间有限维。

**自测**：推论 C 说 $\F(X)$ 拟同构于 hom 空间有限维的 dg 范畴，这一步是怎么做到的？

## 前提

- $\B$ 有限、directed：存在排序使 $i<j$ 时 $\hom(V_j,V_i)=0$。
- $\B$ 的 hom 空间有限维。

## 步骤

1. **按 directed 排序，$\B$ 的运算矩阵是分块上三角的；高阶 $\mu^d$（$d\ge3$）只影响上三角部分。**  
   为什么：反向分块为零，故高阶运算不会把低层送到高层之外。  
   锚点：原书 p.287 §18（证据 B）

2. **逐对消去高阶运算：用同伦变换（ twisting cochain）把 $\mu^d$ 的吸收到低阶，得到同调等价的 dg 范畴。**  
   为什么：这是 A∞ 范畴的「去高阶化」标准技巧；directed 性保证消去在有限步终止。  
   锚点：原书 p.287 §18（证据 B）

3. **所得 dg 范畴的 hom 空间仍有限维，因为消去只做可逆线性变换。**  
   为什么：同伦变换不改变 underlying 分次向量空间。  
   锚点：原书 p.287 §18（证据 B）

4. **故 $\B$ 拟同构于有限维 hom 的 dg 范畴，推论 C 成立。**  
   为什么：把 $\B$ 代回 $\Tw\B\simeq\F(X)$ 即得。  
   锚点：原书 p.290 §18（证据 B）

## 结果

directed + 有限 ⇒ 可 dg 化且 hom 有限维；这是推论 C 的全部内容。

## 缺口

- 第 2 步的消去需选择同伦；不同选择给出拟同构的 dg 范畴，不唯一。

## 易错点

- 非 directed 的 A∞ 范畴一般不能这样 dg 化；directed 性是关键。
- dg 化不改变同调范畴，但会改变链层次的代表元。
- 「有限维 hom」指分次向量空间维数有限，不是链复形长度有限。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§18，p.287–290（原书 p.287 §18）

关联：`seidel/deriv/theorem-b-construction`、`seidel/concept/a-infinity-category`、`seidel/concept/exact-triangle`

来源说明：据原书 §18（p.287–290）与推论 C（p.5）转述。
