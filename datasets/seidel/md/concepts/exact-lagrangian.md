# 正合 Lagrangian 子流形

> `seidel/concept/exact-lagrangian` ｜ track B ｜ draft

**一句话**：Liouville 形式在 $L$ 上恰当：$\lambda|_L=da$。它排除非平凡全纯盘，使 Floer 理论只需处理条带，是全书的技术前提。

**自测**：为什么 Seidel 全书只讨论正合 Lagrangian，而不处理一般的紧致 Lagrangian？

## 定义

设 $(M,\omega,\lambda)$ 是紧致带角的正合辛流形：$\omega=d\lambda$，且 $\lambda$ 的负 Liouville 向量场沿所有边界面向内。紧致 Lagrangian 子流形 $L\subset M$（默认无边且 $L\cap\partial M=\emptyset$）称为正合的，若存在 $a\in C^\infty(L)$ 使
$$\lambda|_L=da .$$
等价地，$[\lambda|_L]=0\in H^1(L;\R)$。

记号：$a$ 称为 $L$ 的 primitive；它只在相差常数的意义下确定。$\lambda$ 的选取也影响 $a$，但不影响正合性。

## 要点

- 正合性等价于 $[\lambda|_L]=0$；对单连通 $L$ 自动成立，对环面则是额外条件。
- 全纯盘的面积等于 $\lambda$ 沿边界的积分；正合性使该积分为零，而非平凡全纯盘面积必为正，故不存在。
- 正因为没有盘，Floer 方程的解只剩条带，紧化与定向都大幅简化；这是全书的技术前提。

## 公式

$$\lambda|_L=da,\qquad \int_D u^*\omega=\int_{\partial D}u^*\lambda=\int_{\partial D}da=0$$
$$\text{能量：}E(u)=\int|\partial_s u|^2=\int u^*\omega$$

## 定理与证明

### 正合 Lagrangian 上没有非平凡全纯盘

设 $u:(D,\partial D)\to(M,L)$ 是全纯盘，$L$ 正合。则 $u$ 是常值映射。

（complete；来源：原书 p.99 (7.5)、p.112 §8l）

1. 能量恒等式：$E(u)=\int_D u^*\omega=\int_{\partial D}u^*\lambda$。  
   为什么：对全纯曲线，能量等于辛面积；Stokes 定理把面积写成边界积分。
2. 边界落在 $L$ 上，$u^*\lambda=u^*da=d(a\circ u)$。  
   为什么：正合性 $\lambda|_L=da$ 拉回到边界。
3. 于是 $E(u)=\int_{\partial D}d(a\circ u)=0$。  
   为什么：闭曲线上的恰当形式积分为零。
4. 能量为零的全纯映射是常值。  
   为什么：$ar\partial u=0$ 且 $E(u)=0$ 给出 $du=0$。

## 易错点

- 正合不等于哈密顿同痕于零截面；后者是更强的几何结论。
- primitive $a$ 只在相差常数意义下确定，不要把它当成 $L$ 上的函数规范。
- 原书 §7 默认 $L$ 紧致无边且 $L\cap\partial M=\emptyset$；带边 Lagrangian 需另行约定边界条件。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§7，p.96–100（原书 p.96 §7）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§8l，p.112–112（原书 p.112 §8l）

关联：`seidel/concept/floer-complex`、`seidel/concept/brane-structure`、`seidel/deriv/lefschetz-induction`

来源说明：据原书 §7（p.96–100）与 §8l（p.112）转述；译者注 A04-xx。
