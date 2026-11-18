# 定理 A 的归纳路线

> `seidel/deriv/lefschetz-induction` ｜ track C ｜ draft

**目标**：概述定理 A 的证明结构：用 Prop 19.7 的 split-生成，把 $\Pi\Tw\F(X^1)$ 化归为 $\Pi\Tw\A_1$，其中 $\A_1$ 由 PL 数据组合地给出。

**自测**：定理 A 说「可由 PL 组合数据计算」，这个归纳到底按什么进行？

## 前提

- $X\subset\C^N$ 是 $n+1$ 维仿射代数簇，$X^1=X\cap\C^{N-1}$ 是超平面截面。
- 对 $X$ 取 Lefschetz 纤维化 $\pi:X\to\C$，临界点 $p_1,\ldots,p_m$，消失圈 $V_i\subset X^1$。

## 步骤

1. **Prop 19.7：消失圈 $V^\#$ split-生成 $\A=\Pi(\Tw\F(M))$（$M=E_\star$ 为纤维），只要 $d\ne2$。**  
   为什么：这是定理 A 的几何输入：$\F(X^1)$ 的 split-闭包由消失圈 split-生成，幂等像也在其中。  
   锚点：原书 p.298 §19（证据 A）

2. **$\A_{k,!}=\F^!(V^{k,\#})$ 的态射与 $\mu^d$ 由匹配路径的相交与多边形计数给出（§13 (13b)），而这些路径与辫 monodromy 属于 PL 数据（§19c）。**  
   为什么：Floer 复形与高阶运算化为有限组合计数，这正是 p.4 的「可计算」定义。  
   锚点：原书 p.196 §13b（证据 A）

3. **(19.6)：$\F(X_k)\to\Tw\A_{k+1,!}$ 上同调全忠实（原文经 $\F$ 的 Lefschetz 纤维化范畴分解，见 p.302）；消失圈在其中的像给出全子范畴 $\B_k\subset\Tw\B_{k+1,!}$，$\B_k\simeq\A_k$。**  
   为什么：由 Prop 18.13（$\F(X_k)\to\F$ 的纤维化范畴全忠实）与定理 18.24（$\Tw\F^!(V^\#)\simeq\Tw\F$ 的纤维化范畴）复合得到；匹配圈的像可逐次算出（p.302）。  
   锚点：原书 p.302 §19d（证据 B）

4. **由 Cor 4.9 与 Lemma 4.7：$\Pi\Tw\F(X^1)\simeq\Pi\Tw\A_1\simeq\Pi\Tw\B_1$，而 $\B_1$ 只由 PL 数据给出；归纳把维数降到 $n=0$（p.303 用 (19.7) 补）。**  
   为什么：split-生成 + 唯一性把「所有对象」换成「生成元」；$n=0$ 时 $\B_{n+1,!}$ 仍可用 §13 的组合方法。  
   锚点：原书 p.303 §19（证据 A）

## 结果

$\Pi\Tw\F(X^1)$ 由有限 A∞ 范畴 $\B_1$ 的扭曲复形计算，而 $\B_1$ 由 PL 数据组合地给出；归纳在 $n=0$ 处由 (19.7) 收尾。

## 缺口

- Prop 19.7 的 split-生成是硬定理（(19.4)+Cor 17.17+Cor 5.8），本卡只引用不证明；$d=2$ 时它失败（Remark 19.8）。
- $n=0$ 需要单独的 (19.7) 论证；定理 A 本身要求 $n\ge1$（p.303、Remark 19.10）。

## 易错点

- 归纳是对 $X^1$ 的维数 $n$，不是对 $X$ 的维数 $n+1$；差一维是消失圈的维数。
- $\B$ 的对象是消失圈而非所有 Lagrangian；split-生成保证不丢对象（包括幂等像）。
- 定理 A 要求 $n\ge1$、$d\ne2$、$\operatorname{char}\K\ne2$；分别对应归纳起点、Calabi–Yau 维数与 Pin 结构。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§19，p.298–303（原书 p.298 §19）

关联：`seidel/concept/lefschetz-fibration`、`seidel/concept/vanishing-cycle`、`seidel/deriv/theorem-b-construction`

来源说明：据原书 §19（p.298–303）与引言 p.4 转述；译者注 A12-03、A12-07。
