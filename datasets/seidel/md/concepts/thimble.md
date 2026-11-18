# 顶针（thimble）

> `seidel/concept/thimble` ｜ track C ｜ draft

**一句话**：临界点上方沿道路的消失盘之并：全空间中的 Lagrangian $(n+1)$-球，边界是纤维中的消失圈。

**自测**：消失圈在总空间里「长成」什么？为什么它是个 Lagrangian 盘？

## 定义

设 $p$ 是临界点，$\gamma:[0,1]\to S$ 是从正则值到 $\pi(p)$ 的消失路径。Lefschetz thimble $\Delta_\gamma$ 是 $E$ 中唯一嵌入的 Lagrangian $(n+1)$-球，满足
$$\pi(\Delta_\gamma)=\gamma([0,1]),\qquad \pi(\partial\Delta_\gamma)=\{\gamma(0)\}.$$
其边界 $V_\gamma=\partial\Delta_\gamma$ 是纤维 $E_{\gamma(0)}$ 中的消失圈。等价地，$\Delta_\gamma=\bigcup_{t\in\gamma}D_t$，其中 $D_t\subset E_{\gamma(t)}$ 是消失盘。

记号：$n=\dim_\C E-1$；$\Delta_\gamma$ 实维数 $n+1$，边界 $V_\gamma\cong S^n$ 在纤维中。

## 要点

- $\Delta_\gamma$ 是 $E$ 中的 Lagrangian $(n+1)$-球，$\partial\Delta_\gamma=V_\gamma$。
- 不同道路 $\gamma$ 给出 Lagrangian 同痕的 thimble；其边界消失圈相差 monodromy。
- thimble 是 Lefschetz 纤维化 Fukaya 范畴中的自然对象，对应临界点的消失盘。

## 公式

$$\Delta_\gamma\cong D^{n+1},\qquad \partial\Delta_\gamma=V_\gamma\cong S^n$$
$$\omega|_{\Delta_\gamma}=0$$

## 定理与证明

### thimble 是 Lagrangian 球

$\Delta_\gamma$ 是 $E$ 中的 Lagrangian $(n+1)$-球，边界为消失圈 $V_\gamma\cong S^n$。

（sketch；来源：原书 p.221–223 §16b）

1. $D_t$ 是 $E_{\gamma(t)}$ 中的消失盘（实 $n$ 维），其切空间 Lagrangian。  
   为什么：消失盘由平行移动/梯度流构造。
2. 沿 $\gamma$ 的移动方向与 $D_t$ 的切空间共同张成 $T_\gamma$ 的切空间，辛形式在此平面上为零。  
   为什么：$\gamma$ 的切向量与 $D_t$ 的切向量在复结构中正交。
3. 故 $T_\gamma$ 每点切空间 Lagrangian，即为 Lagrangian 盘。  
   为什么：逐点验证。

缺口：完整证明见原书 §16b。

## 易错点

- thimble 在总空间中，不在纤维中；不要与匹配圈混淆。
- $\gamma$ 的选取改变 thimble，但只差 Lagrangian 同痕；边界消失圈则差 monodromy。
- thimble 的边界是消失圈；匹配圈是两个 thimble 沿公共消失圈粘成的球面，二者不同。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§16，p.221–223（原书 p.221 §16b）

关联：`seidel/concept/vanishing-cycle`、`seidel/concept/matching-cycle`、`seidel/concept/lefschetz-fibration`

来源说明：据原书 §16b（p.221–223）转述；译者注 A09-xx。
