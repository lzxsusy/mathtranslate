# Fukaya 范畴

> `seidel/concept/fukaya-category` ｜ track B ｜ draft

**一句话**：以紧致分次 Lagrangian 膜为对象、Floer 复形为 hom、全纯圆盘计数为高阶运算的 A∞ 范畴；只在同伦意义下含幺。

**自测**：为什么 Fukaya 范畴不能直接当成 dg 范畴，而必须保留全部高阶 μ^d？

## 定义

设 $(M,\omega)$ 是正合辛流形。Fukaya 范畴 $\F(M)$ 的对象是带膜结构的紧致 Lagrangian 子流形 $L\subset M$；态射空间是 Floer 复形 $CF^*(L_0,L_1)$。高阶运算
$$\mu^d:\hom(L_{d-1},L_d)\otimes\cdots\otimes\hom(L_0,L_1)\longrightarrow\hom(L_0,L_d)[2-d]$$
计数边界落在 $L_0,\ldots,L_d$ 上的全纯圆盘，按 $d+1$ 个边界点的循环次序与定向带符号求和。

记号：$\mu^d$ 的次数为 $2-d$；$d=1$ 是 Floer 微分，$d=2$ 是 Floer 乘积。

## 要点

- $\mu^d$ 满足 A∞ 关系，来自圆盘模空间紧化后的边界分层（条带、圆盘粘合）。
- $\F(M)$ 一般不是 dg 范畴：$\mu^2$ 只在同伦意义下结合，$\mu^3$ 度量其失效。
- $\F(M)$ 一般没有严格单位元；只有同调单位元，由闭链的 cohomological unit 给出。

## 公式

$$\mu^d:\bigotimes_{i=1}^d\hom(L_{i-1},L_i)\to\hom(L_0,L_d)[2-d]$$
$$\sum_{r+s+t=d}(-1)^{\ast}\mu^{r+1+t}(\ldots,\mu^s(\ldots),\ldots)=0$$

## 定理与证明

### Fukaya 范畴满足 A∞ 关系

对任意 $d\ge1$，$\mu^d$ 满足 A∞ 恒等式；其证明是圆盘模空间紧化边界的逐层计数。

（sketch；来源：原书 p.113–120 §9）

1. 取 $d+1$ 个边界标记的圆盘模空间，其维数为 $d-2$。  
   为什么：Konsevich 指标公式给出圆盘模空间的维数。
2. 紧化边界由圆盘分裂为两个圆盘（或条带）给出，对应 A∞ 和的各项。  
   为什么：Gromov 紧性的边界分层恰好是分裂树的组合型。
3. 边界的带符号计数为零，即得 A∞ 关系。  
   为什么：一维紧致带边流形的边界点数和为零。

缺口：完整证明需横截性与定向；原书 §9、§12 分别对初步与完整版本给出。

## 易错点

- $\F(M)$ 不是严格范畴：对象之间的同构、函子性都要在 A∞ 层面处理。
- 不要把它与导出 Fukaya 范畴 $D^\pi\F(M)$ 混同；后者由扭曲复形与分裂闭包得到。
- 系数域与膜结构的选择会改变范畴；$\operatorname{char}\K=2$ 时定向退化。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§9，p.113–120（原书 p.113 §9）

关联：`seidel/concept/exact-lagrangian`、`seidel/concept/brane-structure`、`seidel/concept/twisted-complex`

来源说明：据原书 §9（p.113–120）与 §12 转述；译者注 A05-xx。
