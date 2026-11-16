# 恰当拉格朗日 $L_{df}$ 与相函数（$f=q^1q^2$）

> `geoq/example/exact-lagrangian-phase-function` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：相函数 $f$ 如何唯一决定一张恰当拉格朗日子流形，而这张子流形又为什么完全迷向？

## 一句话

取 $X=\mathbb{R}^2$、$f=q^1q^2$，写出 $L_{df}=\{p_1=q^2,\ p_2=q^1\}$，验证 $\lambda|_L=df$、$\omega|_L=0$，并用切向量直接核对迷向性。

## 设定

取 $X=\mathbb{R}^2$，坐标 $q^1,q^2$；$T^*X\cong\mathbb{R}^4$，坐标 $q^1,q^2,p_1,p_2$，$\omega=dp_1\wedge dq^1+dp_2\wedge dq^2$，$\lambda=p_1dq^1+p_2dq^2$。令 $f(q^1,q^2)=q^1q^2$，$L=L_{df}\subset T^*X$。

## 计算

**第 1 步**：算 $df=q^2\,dq^1+q^1\,dq^2$，按 $p_i=\partial f/\partial q^i$ 读出 $L=\{(q^1,q^2,p_1,p_2)\mid p_1=q^2,\ p_2=q^1\}$，这是 $\mathbb{R}^4$ 中的一张 $2$ 维平面。

> 为什么：相函数的偏导数直接给出截面，无需解任何方程。

**第 2 步**：验证 $\lambda|_L=df$：沿截面 $S_{df}(q)=(q^1,q^2,q^2,q^1)$ 拉回，$\lambda=p_1dq^1+p_2dq^2$ 变成 $q^2dq^1+q^1dq^2=d(q^1q^2)$。

> 为什么：这正是恒等式 $S_\alpha^*\lambda=\alpha$ 在 $\alpha=df$ 时的具体形态。

**第 3 步**：由此 $\omega|_L=d(\lambda|_L)=d(df)=0$，且 $\dim L=2=\frac12\dim\mathbb{R}^4$，故 $L$ 是恰当拉格朗日子流形。

> 为什么：半维条件由截面保证，迷向条件由 $d^2=0$ 保证，两条合起来即拉格朗日。

**第 4 步**：直接核对：$L$ 上的切向量形如 $u=(a,\,b,\,b,\,a)$（分量次序 $q^1,q^2,p_1,p_2$，因 $\dot p_1=\dot q^2=b$、$\dot p_2=\dot q^1=a$）。对 $u=(a,b,b,a)$、$v=(a',b',b',a')$，$\omega(u,v)=(b\,a'-a\,b')+(a\,b'-b\,a')=0$。

> 为什么：把两个切向量代进 $\omega$ 的分量式，两项成对相消——这是迷向性最直接的证据。

## 结果

$L_{df}=\{p_1=q^2,\ p_2=q^1\}$ 是 $T^*\mathbb{R}^2$ 的恰当拉格朗日子流形，相函数为 $f=q^1q^2$；$f\mapsto f+c$ 给出同一张 $L$，故相函数只定到常数。

## 复核

维数与特例：$\dim L=2=\frac12\dim T^*\mathbb{R}^2$；在 $L$ 上取点 $(q^1,q^2)=(2,3)$，则 $p=(3,2)$，$\lambda|_L$ 在该点沿 $\partial_{q^1}$ 的值为 $p_1=3$，而 $df(\partial_{q^1})=q^2=3$，一致。另取 $f\equiv0$ 得 $L_0=\{p=0\}$，即零截面，同样满足 $\omega|_{L_0}=0$。

## 易错点

- 不要写成 $p_i=f(q)$：正确关系是 $p_i=\partial f/\partial q^i$；把相函数本身当成动量会得到 $\lambda|_L=f\,dq$，一般并不闭。
- $f$ 是底流形 $X$ 上的函数，不是 $T^*X$ 上的函数；相函数不能依赖 $p$。
- $f=q^1q^2$ 是二次函数，$L$ 恰是线性平面；一般 $f$ 给出的 $L$ 是弯曲的，但总还是 $X$ 上的图（可投影）。

## 用到哪些概念

- [拉格朗日子流形、可投影与相函数](../concepts/lagrangian-submanifold.md)
- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)

## 相关卡

- [余切丛 $T^*X$ 的典范辛形式（$X=\mathbb{R}^2$）](../examples/cotangent-bundle-symplectic.md)

## 出处

- §5.1.4 例 5.1.28：恰当拉格朗日与相函数，p.262（PDF p.263），源码 `ch05a.tex:746-753`
