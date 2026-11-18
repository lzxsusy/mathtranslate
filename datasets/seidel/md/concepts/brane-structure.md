# 膜结构

> `seidel/concept/brane-structure` ｜ track B ｜ draft

**一句话**：把分次与相对 Pin 结构一起加在 Lagrangian 上；它使 Floer 复形有整数分次、模空间有定向。

**自测**：为什么单有 Lagrangian 子流形还不够，还要额外加「膜结构」？

## 定义

$L$ 上的膜结构是一对 $(\alpha,P)$：分次 $\alpha:L\to\R$（见 Maslov 指标卡）与相对 Pin 结构 $P$。等价地，它是 $L$ 到抽象膜空间
$$\mathrm{Gr}(V)^\#\longrightarrow K(\Z/1)\times K(\Z/2,2)$$
的一个提升点 $\Lambda^\#$，其中第一个因子记录分次 $\mu$，第二个记录 $w_2$。

记号：$K(\Z/2,2)$ 的分类给出相对 $w_2$；$\operatorname{char}\K\ne2$ 时 Pin 结构才保证定向线一致。

## 要点

- 膜结构 $=$ 分次 $+$ 相对 Pin 结构；两者分别负责 Floer 复形的分次与模空间的定向。
- 抽象膜空间 $\mathrm{Gr}(V)^\#$ 是 $\mathrm{Gr}(V)$ 的 $2$-连通覆叠；$n\le2$ 时连通性退化，需分别处理。
- 全书默认所有对象带膜结构；忘记它会使 $\mu^1$ 的符号与分次失去意义。

## 公式

$$\mathrm{Gr}(V)^\#\to K(\Z/1)\times K(\Z/2,2),\qquad \Lambda^\#\mapsto(\mu,w_2)$$
$$\det(D_{D,\rho})\cong\lambda^{\mathrm{top}}(\rho(0))$$

## 定理与证明

### 膜结构给出 Floer 复形的整数分次

若 $L_0,L_1$ 带膜结构，则 $CF^*(L_0,L_1)$ 有整数分次，且 $\mu^1$ 的次数为 $1$。

（sketch；来源：原书 p.163 §11h）

1. 分次 $\alpha_i$ 给出每个交点 $x$ 的整数 $\mu(x)=\alpha_1(x)-\alpha_0(x)$。  
   为什么：交点处两条 Lagrangian 的相位差取整即分次。
2. 条带模空间的维数等于 $\mu(x)-\mu(y)-1$；维数 $0$ 的条带满足 $\mu(y)=\mu(x)-1$。  
   为什么：指数定理把模空间维数写成 Maslov 指标差。
3. Pin 结构给每条条带的定向线一致定向，故 $\mu^1$ 的矩阵元带确定符号。  
   为什么：定向线的相容性来自相对 Pin 结构。

缺口：细节见原书 §11h、§12。

## 易错点

- Pin 结构不是 Spin 结构；对不可定向的 Lagrangian，只能用 Pin。
- 相对 $w_2$ 依赖参考 Lagrangian；换参考会改变提升，但不改变存在性。
- $\operatorname{char}\K=2$ 时符号消失，膜结构的部分作用退化；全书因此假设 $\operatorname{char}\K\ne2$。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§11h，p.163–165（原书 p.163 §11h）

关联：`seidel/concept/maslov-index`、`seidel/concept/fukaya-category`、`seidel/concept/exact-lagrangian`

来源说明：据原书 §11h（p.163–165）转述；译者注 A06-xx。
