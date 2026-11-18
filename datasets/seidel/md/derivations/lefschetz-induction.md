# 定理 A 的归纳路线

> `seidel/deriv/lefschetz-induction` ｜ track C ｜ draft

**目标**：概述定理 A 的证明结构：对维数 $n$ 归纳，把 $X^1$ 的 Fukaya 范畴化归为纤维的 Fukaya 范畴加一个消失圈。

**自测**：定理 A 说「可由 PL 组合数据计算」，这个归纳到底按什么进行？

## 前提

- $X\subset\C^N$ 是 $n+1$ 维仿射代数簇，$X^1=X\cap\C^{N-1}$ 是超平面截面。
- 对 $X$ 取 Lefschetz 纤维化 $\pi:X\to\C$，临界点 $p_1,\ldots,p_m$，消失圈 $V_i\subset X^1$。

## 步骤

1. **由 Lefschetz 理论，$X^1$ 的 Fukaya 范畴由消失圈 $V_i$ 与它们之间的 Floer 复形生成。**  
   为什么：这是定理 A 的几何输入：$X^1$ 的紧致 Lagrangian 可由消失圈生成。  
   锚点：原书 p.303 §19（证据 B）

2. **每个 $V_i$ 是 $X^1$ 中的 Lagrangian 球面，其自同态与相互态射由 PL 数据（匹配路径、辫 monodromy）给出。**  
   为什么：球面的 Floer 理论可显式计算；相互态射由匹配路径的相交数决定。  
   锚点：原书 p.295 §19（证据 B）

3. **把 $V_i$ 作为对象、Floer 复形作为态射，得到有限 A∞ 范畴 $\B$；由第 1 步，$\Tw\B$ 与 $\Tw\F(X^1)$ 拟等价。**  
   为什么：生成性把「所有对象」化归为「生成元」；$\Tw$ 容纳锥与直和。  
   锚点：原书 p.303 §19（证据 B）

4. **$\B$ 的构造只用到 $X$ 的 PL 数据，故 $\Tw\F(X^1)$ 可由这些数据计算；对 $n$ 归纳。**  
   为什么：$V_i$ 本身是 $n-1$ 维球面，其 Fukaya 范畴又可由低维 PL 数据描述。  
   锚点：原书 p.303 §19（证据 B）

## 结果

$\Tw\F(X^1)$ 由有限 A∞ 范畴 $\B$ 的扭曲复形计算，而 $\B$ 的构造是组合的；归纳降至 $n=1$ 以下。

## 缺口

- 第 1 步的「生成」是定理 A 的核心几何定理，本书 §19 才证明；此处只给路线。

## 易错点

- 归纳是对 $X^1$ 的维数 $n$，不是对 $X$ 的维数 $n+1$；差一维是消失圈的维数。
- $\B$ 的对象是消失圈而非所有 Lagrangian；生成性保证不丢对象。
- 定理 A 要求 $n\ge1$、$d\ne2$、$\operatorname{char}\K\ne2$；这些条件分别对应归纳起点、Calabi–Yau 维数与 Pin 结构。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§19，p.303–307（原书 p.303 §19）

关联：`seidel/concept/lefschetz-fibration`、`seidel/concept/vanishing-cycle`、`seidel/deriv/theorem-b-construction`

来源说明：据原书 §19（p.303–307）与引言 p.4 转述；路线图为本书证明结构的概括。
