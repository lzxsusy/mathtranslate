# 消失圈

> `seidel/concept/vanishing-cycle` ｜ track C ｜ draft

**一句话**：沿消失路径平行移动的极限：临界点附近缩成一点的 Lagrangian 球面 $S^n$，位于光滑纤维中。

**自测**：为什么沿临界值走一条道路会在纤维里留下一个球面？

## 定义

设 $\gamma:[0,1]\to S$ 是消失路径：嵌入道路，$\gamma^{-1}(\operatorname{Critv})=\{1\}$。Lefschetz thimble $\Delta_\gamma$ 是 $E$ 中唯一嵌入的 Lagrangian $(n+1)$-球，满足 $\pi(\Delta_\gamma)=\gamma([0,1])$、$\pi(\partial\Delta_\gamma)=\{\gamma(0)\}$。其边界
$$V_\gamma=\partial\Delta_\gamma\subset E_{\gamma(0)}$$
是纤维中的 Lagrangian 球面，称为沿 $\gamma$ 的消失圈。等价地，
$$V_\gamma=\{x\in E_{\gamma(0)}:\text{沿 }\gamma\text{ 的平行移动当 }t\to1\text{ 时收敛到临界点}\}.$$

记号：$n=\dim_\C E-1$ 是纤维的复维数，故 $V_\gamma\cong S^n$；$\gamma$ 的选取只影响 $V_\gamma$ 的哈密顿同痕类。

## 要点

- $V_\gamma\cong S^n$ 是 Lagrangian 球面，且因它界定 Lagrangian 盘而自动正合。
- 绕临界值一周的 monodromy 正是沿 $V_\gamma$ 的 Dehn twist（Picard–Lefschetz 公式）。
- 消失圈是 Fukaya 范畴中的自然对象；定理 A 的归纳就靠它们生成纤维的 Fukaya 范畴。

## 公式

$$V_\gamma\cong S^n\subset E_{\gamma(0)},\qquad \text{monodromy}=\tau_{V_\gamma}$$
$$\mu(V_\gamma)=0$$

## 定理与证明

### 消失圈是 Lagrangian 球面

对非退化临界点 $p$ 与消失路径 $\gamma$，$V_\gamma=\partial\Delta_\gamma$ 是 $E_{\gamma(0)}$ 中的 Lagrangian 球面 $S^n$，且自动正合。

（sketch；来源：原书 p.221–223 §16）

1. 局部模型 $\pi=z_1^2+\cdots+z_{n+1}^2$ 中，临界纤维的奇点邻域是一个二次锥。  
   为什么：Morse 引理的复版本。
2. 用 $|z|^2$ 的梯度流把锥附近的点推到距离 $\sqrt{|t|}$ 的球面 $S^n$ 上。  
   为什么：这是 Milnor 纤维的标准模型：纤维同胚于 $TS^n$。
3. 平行移动保持辛形式，故 $V_\gamma$ 是 Lagrangian；其维数为 $n$。  
   为什么：monodromy 是辛同胚，把 Lagrangian 映为 Lagrangian。

缺口：完整证明见原书 §16b。

## 易错点

- $V_\gamma$ 依赖道路 $\gamma$；换道路得到同一球面的不同 Dehn twist 像，不要当成同一个子流形。
- 消失圈是 $n$ 维球面 $S^n$（$n=\dim_\C E-1$），不是 $S^{n-1}$；维数由纤维的复维数决定。
- 消失圈未必是纤维中唯一的 Lagrangian 球面；它只是由临界点指定的一族。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§16，p.221–223（原书 p.221 §16b）

关联：`seidel/concept/lefschetz-fibration`、`seidel/concept/thimble`、`seidel/concept/matching-cycle`

来源说明：据原书 §16b（p.221–223）转述；译者注 A09-xx。
