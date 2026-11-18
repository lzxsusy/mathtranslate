# 顶针（thimble）

> `seidel/concept/thimble` ｜ track C ｜ draft

**一句话**：临界点上方沿道路的消失盘之并：全空间中的 Lagrangian 盘，边界是纤维中的消失圈。

**自测**：消失圈在总空间里「长成」什么？为什么它是个 Lagrangian 盘？

## 定义

设 $p$ 是临界点，$\gamma:[0,1]\to\C$ 从正则值 $t_0$ 到 $\pi(p)$。对每个 $t\in\gamma$，取 $p$ 附近的消失盘 $D_t\subset X_t$；其并
$$T_\gamma=\bigcup_{t\in\gamma}D_t$$
称为 $p$ 沿 $\gamma$ 的 thimble（顶针）。$T_\gamma$ 是以 $V_\gamma=\partial T_\gamma$ 为边界的 Lagrangian 盘。

记号：$T_\gamma$ 的维数为 $n$（实）；边界 $V_\gamma$ 在纤维 $X_{t_0}$ 中。

## 要点

- $T_\gamma$ 是 $X$ 中的 Lagrangian 盘，$\partial T_\gamma=V_\gamma$。
- 不同道路 $\gamma$ 给出 Lagrangian 同痕的 thimble；其边界消失圈相差 monodromy。
- thimble 是 Lefschetz 纤维化 Fukaya 范畴中的自然对象，对应临界点的消失盘。

## 公式

$$T_\gamma\cong D^n,\qquad \partial T_\gamma=V_\gamma\cong S^{n-1}$$
$$\omega|_{T_\gamma}=0$$

## 定理与证明

### thimble 是 Lagrangian 盘

$T_\gamma$ 是 $X$ 中的 Lagrangian 盘，边界为消失圈 $V_\gamma$。

（sketch；来源：原书 p.229–231 §16）

1. 在每个 $t\in\gamma$ 上，$D_t$ 是 $X_t$ 中的消失盘，其切空间 Lagrangian。  
   为什么：消失盘由梯度流构造，是复一维的复子流形。
2. 沿 $\gamma$ 的移动方向与 $D_t$ 的切空间共同张成 $T_\gamma$ 的切空间，辛形式在此平面上为零。  
   为什么：$\gamma$ 的切向量与 $D_t$ 的切向量在复结构中正交。
3. 故 $T_\gamma$ 每点切空间 Lagrangian，即为 Lagrangian 盘。  
   为什么：逐点验证。

缺口：细节见原书 §16e–16f。

## 易错点

- thimble 在总空间中，不在纤维中；不要与匹配圈混淆。
- $\gamma$ 的选取改变 thimble，但只差 Lagrangian 同痕；边界消失圈则差 monodromy。
- thimble 的边界是消失圈，不是匹配圈；匹配圈是两个消失圈的并。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§16，p.229–231（原书 p.229 §16）

关联：`seidel/concept/vanishing-cycle`、`seidel/concept/matching-cycle`、`seidel/concept/lefschetz-fibration`

来源说明：据原书 §16（p.229–231）转述；译者注 A09-xx。
