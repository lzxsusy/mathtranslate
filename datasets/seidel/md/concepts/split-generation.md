# 分裂生成

> `seidel/concept/split-generation` ｜ track A ｜ draft

**一句话**：最小的包含给定族的「分裂闭三角子范畴」就是全范畴；等价地，每个对象都是该族有限次锥与直和项的组合。

**自测**：什么时候一族对象足以「生成」整个三角范畴，而不只是生成一个稠密子范畴？

## 定义

设 $\A$ 是三角范畴，$\mathcal S\subset\mathrm{Ob}\A$。称 $\mathcal S$ 分裂生成 $\A$，若包含 $\mathcal S$ 的最小分裂闭三角子范畴等于 $\A$。这里「三角子范畴」要求对平移、锥、直和封闭，「分裂闭」要求对直和项封闭。等价说法：每个 $X\in\A$ 都同构于某个由 $\mathcal S$ 中对象经有限次锥、平移、直和所得对象的直和项。

记号：$\Tw\A$ 中的分裂生成常写作「$\mathcal S$ split-generates $\Tw\A$」。

## 要点

- 分裂生成强于生成：生成只要求取锥与平移，分裂生成还允许取直和项。
- 在 $\Tw\A$ 中，锥与直和已经内建；分裂生成的关键是直和项，即幂等分裂。
- 本书用「逐次扭转是否为零」作判据（推论 5.7）：若一族对象使所有对象的逐次扭转为零，则该族分裂生成。

## 公式

$$\mathcal S\ \text{split-generates}\ \A\iff \A=\langle\mathcal S\rangle^{\mathrm{split}}_{\mathrm{tri}}$$

## 定理与证明

### 逐次扭转判别（推论 5.7）

若一族对象 $\mathcal S$ 使得每个 $X\in\A$ 的逐次扭转 $T_{\mathcal S}^k(X)$ 最终为零，则 $\mathcal S$ 分裂生成 $\A$。

（sketch；来源：原书 p.60、§5）

1. 逐次扭转给出一个滤过，其关联分次由 $\mathcal S$ 中的对象组成。  
   为什么：每次扭转把一个对象换成 cone，锥的滤过商落在生成族里。
2. 滤过有限（逐次扭转为零），故 $X$ 可由生成族的锥与直和项迭代得到。  
   为什么：三角范畴中「滤过商属于子范畴」推出对象本身属于该子范畴，前提是对直和项封闭。
3. 因此 $X$ 属于 $\mathcal S$ 的分裂闭三角子范畴；$X$ 任意，故等于全范畴。  
   为什么：分裂闭性由子范畴定义给出。

缺口：原书推论 5.7 的陈述还要求 $\A$ 本身具有某些有限性；引用时须核对 §5 的假设。

## 易错点

- 「生成」与「分裂生成」不可混用；只证了生成，不能推出 $\Tw$ 的每个对象都是直和项。
- 在 $\Tw\A$ 里做分裂生成时，直和项由幂等给出；忘记幂等完备化会漏掉对象。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§4–5，p.55–74（原书 p.55–74 §4–5）

关联：`seidel/concept/karoubi-envelope`、`seidel/concept/exact-triangle`、`seidel/deriv/split-generation`

来源说明：原书 p.60（推论 5.7）、p.70–74（§5e）；译者注 A04-04。
