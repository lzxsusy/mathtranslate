# 分裂闭包与幂等元的实现

> `seidel/deriv/split-generation` ｜ track A ｜ draft

**目标**：证明 $\Tw\A$ 对幂等元封闭：每个幂等 $e\in\hom(X,X)$ 都在 $\Tw\A$ 中有像。

**自测**：为什么 $\Tw\A$ 不需要再形式地添幂等元，就已经是分裂闭的？

## 前提

- $\A$ 是 A∞ 范畴，$X\in\Tw\A$，$e:X\to X$ 满足 $e^2=e$（在同伦意义下）。
- $\Tw\A$ 的锥由上一张卡给出。

## 步骤

1. **取 $Y=\Cone(e)$，即 $(X\oplus X,\delta)$，$\delta$ 的非零分量为 $e$。**  
   为什么：锥的构造；$e$ 是次数 $0$ 的闭态射。  
   锚点：原书 p.68 §4（证据 A）

2. **由 $e^2=e$，$\delta^2=0$；MC 方程成立。**  
   为什么：幂等性正是锥成为扭曲复形的条件。  
   锚点：原书 p.68 §4（证据 A）

3. **存在投影 $p:X\to Y$ 与包含 $i:Y\to X$，满足 $p\circ i=\id_Y$、$i\circ p=e$。**  
   为什么：锥的泛性质给出这对态射；$i\circ p=e$ 是构造的直接计算。  
   锚点：原书 p.68 §4（证据 A）

4. **故 $Y$ 是 $e$ 的像；任意幂等元都在 $\Tw\A$ 中分裂。**  
   为什么：分裂的定义就是存在这样的 $i,p$。  
   锚点：原书 p.68 §4（证据 A）

## 结果

$\Tw\A$ 是分裂闭的；$\Pi(\Tw\A)$ 与 $\Tw\A$ 在 $H^0$ 上一致。

## 缺口

- 上述构造在 dg 情形最清楚；A∞ 情形需把 $e^2=e$ 理解为同伦意义下的幂等。

## 易错点

- $\Tw\A$ 的分裂闭性不等于 $\A$ 本身分裂闭；$\A$ 一般不是。
- $e$ 必须在 $H^0$ 中是幂等，而不是链层次严格幂等。
- $\Pi(\Tw\A)$ 与 $\Tw\A$ 的差别在对象层面，不在同调层面；不要重复添加。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§4，p.68–70（原书 p.68 §4）

关联：`seidel/concept/karoubi-envelope`、`seidel/concept/twisted-complex`、`seidel/concept/split-generation`

来源说明：据原书 §4（p.68–70）转述；译者注 A03-xx。
