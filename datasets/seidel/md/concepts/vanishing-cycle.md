# 消失圈

> `seidel/concept/vanishing-cycle` ｜ track C ｜ draft

**一句话**：绕临界值平行移动的极限：临界点附近缩成一点的球面 $S^{n-1}$，位于光滑纤维中，是 Lagrangian。

**自测**：为什么绕临界值走一圈会在纤维里留下一个球面？

## 定义

设 $p$ 是临界点，$\gamma:[0,1]\to\C$ 是从正则值 $t_0$ 到临界值 $\pi(p)$ 的道路。沿 $\gamma$ 的平行移动把 $X_{t_0}$ 中的点送到临界纤维附近；其极限落在 $p$ 的消失球面上的点构成
$$V_\gamma=\{x\in X_{t_0}:\text{沿 }\gamma\text{ 的平行移动收敛到 }p\}.$$
当 $\gamma$ 是简单环路时，$V_\gamma$ 是 $X_{t_0}$ 中的 Lagrangian 球面 $S^{n-1}$。

记号：$n-1=\dim_\C X-1$ 是球面维数；$\gamma$ 的选取只影响 $V_\gamma$ 的哈密顿同痕类。

## 要点

- $V_\gamma\cong S^{n-1}$ 是 Lagrangian 球面，其 Maslov 指标为零。
- 绕临界值一周的 monodromy 正是沿 $V_\gamma$ 的 Dehn twist（Picard–Lefschetz 公式）。
- 消失圈是 Fukaya 范畴中的自然对象；定理 A 的归纳就靠它们生成纤维的 Fukaya 范畴。

## 公式

$$V_\gamma\cong S^{n-1}\subset X_{t_0},\qquad T_\gamma=\text{Dehn twist along }V_\gamma$$
$$\mu(V_\gamma)=0$$

## 定理与证明

### 消失圈是 Lagrangian 球面

对非退化临界点 $p$ 与简单道路 $\gamma$，$V_\gamma$ 是 $X_{t_0}$ 中的 Lagrangian 球面。

（sketch；来源：原书 p.221–223 §16）

1. 局部模型 $\pi=z_1^2+\cdots+z_n^2$ 中，临界纤维的奇点邻域是一个二次锥。  
   为什么：Morse 引理的复版本。
2. 用 $|z|^2$ 的梯度流把锥附近的点推到距离 $\sqrt{|t|}$ 的球面 $S^{n-1}$ 上。  
   为什么：这是 Milnor 纤维的标准模型：纤维同胚于 $TS^{n-1}$。
3. 平行移动保持辛形式，故 $V_\gamma$ 是 Lagrangian；其维数为 $n-1$。  
   为什么：monodromy 是辛同胚，把 Lagrangian 映为 Lagrangian。

缺口：完整证明见原书 §16a–16b。

## 易错点

- $V_\gamma$ 依赖道路 $\gamma$；换道路得到同一球面的不同 Dehn twist 像，不要当成同一个子流形。
- 球面维数是 $n-1$（纤维的实维数减一的一半的兩倍），容易与 $n$ 混。
- 消失圈未必是纤维中唯一的 Lagrangian 球面；它只是由临界点指定的一族。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§16，p.221–223（原书 p.221 §16）

关联：`seidel/concept/lefschetz-fibration`、`seidel/concept/thimble`、`seidel/concept/matching-cycle`

来源说明：据原书 §16（p.221–223）转述；译者注 A09-xx。
