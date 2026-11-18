# Karoubi 完备化（幂等完备化）

> `seidel/concept/karoubi-envelope` ｜ track A ｜ draft

**一句话**：把每个幂等态射 e 形式地分裂成对象 (X,e)；三角范畴的幂等完备化仍是三角范畴，且函子保持三角结构。

**自测**：为什么「分裂闭包」不是再添几个对象，而是把幂等态射当对象？

## 定义

范畴 $\A$ 的 Karoubi 完备化 $P\A$ 的对象是二元组 $(X,e)$，其中 $X\in\A$、$e:X\to X$ 满足 $e^2=e$；态射 $(X,e)\to(Y,e')$ 是 $\A$ 中的 $f:X\to Y$ 且 $e'fe=f$。复合继承 $\A$ 的复合。直观上 $(X,e)$ 是「$e$ 的像」的形式分裂。

记号：$P\A$ 也记作 $\mathrm{Kar}(\A)$ 或 $\A^{\mathrm{idem}}$。

## 要点

- $(X,e)$ 不是 $X$ 的子对象；它只在完备化里与「像」等同。
- 三角范畴的幂等完备化仍是三角范畴，且完备化函子 $\A\to P\A$ 保持三角。
- $\Tw\A$ 已经包含直和与锥，但一般不正合于幂等分裂；$\Pi(\Tw\A)$ 才把两者都补齐。

## 公式

$$\mathrm{Ob}(P\A)=\{(X,e):X\in\A,\ e^2=e\},\qquad \hom_{P\A}((X,e),(Y,e'))=\{f:e'fe=f\}$$

## 定理与证明

### 幂等在完备化中分裂

在 $P\A$ 中，每个幂等态射 $f:(X,e)\to(X,e)$ 都有核（像），即存在对象 $(Y,p)$ 使 $f$ 分解为投影与包含。

（sketch；来源：原书 p.55–56 §4）

1. 取 $Y=X$、$p=f$；由 $f^2=f$ 知 $(X,f)$ 是 $P\A$ 的对象。  
   为什么：$P\A$ 的对象正是幂等态射。
2. 包含 $i:(X,f)\to(X,e)$ 取 $i=f$，投影 $q:(X,e)\to(X,f)$ 取 $q=f$。  
   为什么：$e f e=f$ 且 $f e f=f$，故 $i,q$ 都是合法态射。
3. $q\circ i=f^2=f=\id_{(X,f)}$，而 $i\circ q=f$ 正是原来的幂等。  
   为什么：复合直接计算；这说明 $f$ 在 $P\A$ 中被分解为投影与包含。

缺口：这里只验证了形式分裂；三角结构的继承需要额外验证，见原书 §4。

## 易错点

- 不要把 $(X,e)$ 当成 $\ker e$ 或 $\im e$；完备化只提供形式分裂。
- $\Tw\A$ 与 $P\A$ 是两种不同的完备化：前者补锥与平移，后者补幂等；$\Pi(\Tw\A)$ 才同时补齐。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§3–4，p.3–56（原书 p.3、p.41–56 §4）

关联：`seidel/concept/twisted-complex`、`seidel/concept/split-generation`、`seidel/concept/exact-triangle`

来源说明：原书 p.3（引言中的用法）、p.55–56 §4；译者注 A01-03（nLab Karoubi envelope，B 级）、A04-01。
