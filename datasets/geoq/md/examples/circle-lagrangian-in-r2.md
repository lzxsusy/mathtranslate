# $\mathbb{R}^2=T^*\mathbb{R}$ 中的圆是拉格朗日子流形

> `geoq/example/circle-lagrangian-in-r2` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：一维的圆为什么满足拉格朗日条件，而它的 $\lambda|_L$ 又为什么没有整体原函数？

## 一句话

$L=\{p^2+q^2=R^2\}\subset T^*\mathbb{R}$ 是一维拉格朗日；算得 $\lambda|_L=-R^2\sin^2\theta\,d\theta$、周期 $-\pi R^2$，故闭而不恰当，且不可投影。

## 设定

取 $X=\mathbb{R}$，$T^*\mathbb{R}\cong\mathbb{R}^2$，坐标 $q,p$，$\omega=dp\wedge dq$，$\lambda=p\,dq$。令 $R>0$，$L=\{(q,p)\mid p^2+q^2=R^2\}$，按 $q=R\cos\theta$、$p=R\sin\theta$ 定向（$0\le\theta<2\pi$）。

## 计算

**第 1 步**：维数：$L$ 是圆周，$\dim L=1=\frac12\dim\mathbb{R}^2$；一维流形上任何 $2$-形式必为零，故 $\omega|_L=dp\wedge dq|_L=0$，$L$ 是拉格朗日子流形。

> 为什么：迷向性在一维时是维数现象，不需要算任何东西。

**第 2 步**：限制 $\lambda$：$dq=d(R\cos\theta)=-R\sin\theta\,d\theta$，故 $\lambda|_L=p\,dq=R\sin\theta\cdot(-R\sin\theta)\,d\theta=-R^2\sin^2\theta\,d\theta$，它确实闭（$d\lambda|_L=\omega|_L=0$）。

> 为什么：把 $\lambda$ 用一个参数显式写出，后面的周期积分才有被积函数。

**第 3 步**：算周期：$\int_L\lambda=\int_0^{2\pi}(-R^2\sin^2\theta)\,d\theta=-R^2\pi$，非零。

> 为什么：$\lambda|_L$ 的上同调类由它沿闭链的积分读出，非零就排除了恰当性。

**第 4 步**：反证不恰当：若 $\lambda|_L=dg$ 对某个 $g$ 成立，则由斯托克斯定理 $\int_L\lambda=\int_Ldg=0$（$\partial L=\varnothing$），与第 3 步的 $-\pi R^2$ 矛盾。

> 为什么：无边界流形上恰当形式的积分必为零，这是判别恰当性最省力的障碍。

**第 5 步**：不可投影：投影 $\pi(q,p)=q$ 在 $(-R,R)$ 上是双值的（$p=\pm\sqrt{R^2-q^2}$），故 $L$ 不是任何截面 $S_\alpha$ 的像。

> 为什么：可投影按定义就是「$L$ 是底流形上的图」，双值性直接把它否定。

## 结果

$L$ 是 $T^*\mathbb{R}$ 的一维拉格朗日子流形，$\lambda|_L$ 闭但不恰当，$L$ 既不可投影、也不是恰当拉格朗日；$\lambda|_L$ 的周期为 $-\pi R^2$，等于 $-\mathrm{Area}(D)$，$D=\{p^2+q^2<R^2\}$。

## 复核

斯托克斯复核：$\int_L\lambda=\int_Dd\lambda=\int_Ddp\wedge dq=-\mathrm{Area}(D)=-\pi R^2$，与参数化算出的值一致；把 $L$ 反向定向（$\theta\mapsto-\theta$）后两个积分同时变号为 $+\pi R^2$。

## 易错点

- 一维时拉格朗日条件是免费的，但这只说明「$\omega$ 限制为零」；若把它推广成「任何子流形都拉格朗日」就错了，极大性（半维）始终要求。
- $\lambda|_L$ 闭是因为 $\omega|_L=0$，不要误读为 $\lambda|_L$ 恰当；恰当性被非零周期挡住。
- 圆不可投影，但它仍是拉格朗日；把「可投影」当成拉格朗日的必要条件会错杀这个例子。

## 用到哪些概念

- [拉格朗日子流形、可投影与相函数](../concepts/lagrangian-submanifold.md)
- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)

## 相关卡

- [恰当拉格朗日 $L_{df}$ 与相函数（$f=q^1q^2$）](../examples/exact-lagrangian-phase-function.md)

## 出处

- §5.1.4 例 5.1.29：圆作为拉格朗日子流形，p.262（PDF p.263），源码 `ch05a.tex:754-771`
