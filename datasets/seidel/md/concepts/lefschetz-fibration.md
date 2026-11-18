# Lefschetz 纤维化

> `seidel/concept/lefschetz-fibration` ｜ track C ｜ draft

**一句话**：到 Riemann 面的 proper 全纯映射：临界点非退化、临界值有限，正则纤维光滑、临界纤维是单节点。

**自测**：为什么把流形写成 Lefschetz 纤维化之后，Fukaya 范畴就能按纤维归纳地算？

## 定义

设 $E^{2n+2}$ 是紧致带角辛流形，$S$ 是紧致带边 Riemann 面。全纯映射 $\pi:E\to S$ 称为 Lefschetz 纤维化，若：
(1) $\pi$ 是 proper 的，$\pi$ 在 $\operatorname{Crit}(\pi)$ 外是淹没，且临界点集 $\operatorname{Crit}(\pi)$ 有限；
(2) 每个临界点 $p$ 处可用局部全纯坐标写成
$$\pi(z_1,\ldots,z_{n+1})=z_1^2+\cdots+z_{n+1}^2;$$
(3) 临界值互异；假设每条纤维至多含一个临界点（原书称为「仅为方便」），故临界纤维恰有一个节点。
纤维 $E_t=\pi^{-1}(t)$ 在 $t$ 非临界值时是光滑辛流形；绕临界值一周的 monodromy 是纤维中的 Dehn twist。

记号：$n=\dim_\C E-1$ 是纤维的复维数；纤维实维数 $2n$，总空间实维数 $2n+2$。

## 要点

- 临界点非退化保证局部模型是 $z_1^2+\cdots+z_{n+1}^2$（Morse 引理的全纯版本）。
- 临界值有限且互异；临界纤维是光滑纤维把一个消失球面缩成一点得到的节点。
- monodromy 由绕临界值的环路给出，等于沿消失圈 $V_\gamma$ 的 Dehn twist。

## 公式

$$\pi(z)=z_1^2+\cdots+z_{n+1}^2,\qquad d\pi=2(z_1,\ldots,z_{n+1})$$
$$\text{monodromy}=T_{V_\gamma}\in\mathrm{Symp}(X_{t_0})$$

## 定理与证明

### 临界纤维是节点

在「每条纤维至多一个临界点」的假设下，若 $t_0$ 是临界值，则 $E_{t_0}$ 恰有一个节点，且该节点由临界点 $p$ 给出。

（sketch；来源：原书 p.216–217 §15d）

1. 在 $p$ 的局部坐标中 $\pi=z_1^2+\cdots+z_{n+1}^2$，故 $\pi^{-1}(0)$ 在 $0$ 附近是二次锥。  
   为什么：局部模型直接给出临界纤维的锥形奇点。
2. 该锥在 $0$ 以外光滑，且 $0$ 是唯一奇点。  
   为什么：梯度 $2z$ 只在 $z=0$ 为零。
3. 每条纤维至多一个临界点，故其他点不贡献奇点。  
   为什么：节点数等于临界纤维上的临界点数。

缺口：全局陈述需 properness 与 Sard 定理。

## 易错点

- 临界值必须互异，否则 monodromy 与匹配路径的讨论需合并处理。
- 局部模型是 $z_1^2+\cdots+z_{n+1}^2$，不是 $z_1^2$；少写项会漏掉消失球面的维数 $n$。
- $\pi$ 是到曲线的映射，纤维实维数为 $2n$；不要把 $n$ 当成总空间维数。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§15，p.216–217（原书 p.216 §15d）

关联：`seidel/concept/vanishing-cycle`、`seidel/concept/thimble`、`seidel/deriv/lefschetz-induction`

来源说明：据原书 §15d（p.216–217）转述；译者注 A08-xx。
