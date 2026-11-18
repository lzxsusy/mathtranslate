# directed A∞ 范畴为何可换成 dg 范畴

> `seidel/deriv/directed-dg` ｜ track A ｜ draft

**目标**：证明 Cor 5.27：directed A∞ 范畴拟同构于一个仍 directed 且 $\mu^d=0\,(d>2)$ 的 dg 范畴；并说明 hom 有限维在 directed 情形可保住。

**自测**：推论 C 说 $\F(X)$ 拟同构于 hom 空间有限维的 dg 范畴，这一步是怎么做到的？

## 前提

- $\B$ 有限、directed：存在排序使 $i<j$ 时 $\hom(V_j,V_i)=0$。
- $\B$ 的 hom 空间有限维。

## 步骤

1. **directed 性给出标号，$\hom_\B(V_j,V_i)=0$（$i<j$），且所有 $\hom$ 有限维；故 $\B$ 的运算矩阵按标号分块上三角。**  
   为什么：这是 (5n) 的 directed 定义；有限维来自 $\B$ 有限。  
   锚点：原书 p.82 §5n（证据 A）

2. **取 $\B^!=\B^!(V)$（(5n) 的 directed 子范畴），Yoneda 给出 cohomologically full and faithful 的 $\B^!\to\mathcal P=\mathrm{mod}(\B^!)$，像 $I(Y_k)$ 是 $\mathcal P$ 中的例外聚集。**  
   为什么：$\mathcal P$ 严格含幺、hom 有限维，故例外聚集的 directed 子范畴可以直接取。  
   锚点：原书 p.87 §5p（证据 A）

3. **$\A_\infty$-模的高阶复合恒为零（$\mathcal P$ 是严格含幺的模范畴），故该 directed 子范畴实际上是 dg 范畴 $\C^!$（$\mu^d=0,d>2$）。**  
   为什么：原文：vanishing of higher order composition maps is a general property of A∞-modules。  
   锚点：原书 p.87 §5p（证据 A）

4. **于是 $\B\simeq\B^!\simeq\C^!$ 仍 directed 且为 dg；p.87 强调只有 directed 情形能同时保住 hom 有限维（一般情形用 Cor 2.14 会失去有限维）。**  
   为什么：Cor 5.27 的结论；$\Tw$ 继承有限维，故推论 C 成立（p.303）。  
   锚点：原书 p.87 §5p（证据 A）

## 结果

directed + 有限 ⇒ 有 dg 模型且 hom 有限维；推论 C 由此把 $\B_{1,!}$ 换成 dg 的 $\C^!$（p.303）。

## 缺口

- dg 模型只在拟同构意义下唯一，且证明走 A∞-模的 Yoneda 像，不是「用 twisting cochain 逐对消去」；后者只是 dg 情形的直观。
- 一般 A∞ 范畴也有 dg 模型（Cor 2.14），但会失去 hom 有限维，故 directed 假设不可省。

## 易错点

- 非 directed 的 A∞ 范畴不能这样保有限维地 dg 化；directed 性是关键。
- dg 化不改变同调范畴，但会改变链层次的代表元。
- 「有限维 hom」指分次向量空间维数有限，不是链复形长度有限。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§5n, §5p，p.82–87（原书 p.87 Corollary 5.27）

关联：`seidel/deriv/theorem-b-construction`、`seidel/concept/a-infinity-category`、`seidel/concept/exact-triangle`

来源说明：据原书 §5n（p.82）、§5p 与 Cor 5.27（p.87）、p.303 转述；译者注 A03-17。
