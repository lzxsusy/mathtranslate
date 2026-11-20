# 中心、基本群与庞特里亚金对偶

- **id**：`gw06/concept/center-pontryagin`
- **类型**：concept
- **位置**：附录A
- **问题**：为什么 Z(G) 与 π_1(G) 恰好是这两组格的商，庞特里亚金对偶又如何让它们在 G 与 ^LG 之间互换？

> 群中心与基本群由格商给出：Z(G)=Λ_cowt/Λ_cochar、π_1(G)=Λ_cochar/Λ_cort，并在庞特里亚金对偶下随对偶群互换。

## 定义

对局部紧阿贝尔群 $A$，记 $A^\vee=\mathrm{Hom}(A,U(1))$；庞特里亚金对偶断言 $B=A^\vee$ 时 $A=B^\vee$。把 $A=\mathbb{T}$ 与 $A=\mathcal{Z}(G)$ 用上，得 $\Lambda_\char=\mathrm{Hom}(\mathbb{T},U(1))$（式 (A.8)），即特征格就是环面到 $U(1)$ 的同态。不可约表示 $R$ 的最高权 $w\in\Lambda_\char$ 决定中心元的作用：$w\in\Lambda_\rt$ 时 $\mathcal{Z}(G)$ 平凡地作用，于是 $\mathcal{Z}(G)^\vee=\Lambda_\char/\Lambda_\rt$（式 (A.10)），等价地 $\mathcal{Z}(G)=\Lambda_\cowt/\Lambda_\cochar$（式 (A.11)）。同理，把 $\pi_1(G)$ 的元素提升到泛覆盖所确定的中心元，得到 $\pi_1(G)^\vee=\Lambda_\wt/\Lambda_\char$（式 (A.12)），等价地 $\pi_1(G)=\Lambda_\cochar/\Lambda_\cort$（式 (A.13)）。物理上 $\mathcal{Z}(G)$ 决定 't Hooft 通量的相位、$\pi_1(G)$ 决定规范丛的扭结类，两者在对偶下互换正是电磁对偶在拓扑层面的表现。两个商都有限，这正是单连通群与伴随型群之间只差一个有限群的原因。

**记号**：$A^\vee=\mathrm{Hom}(A,U(1))$：庞特里亚金对偶群；$\mathcal{Z}(G)$：$G$ 的中心；$\pi_1(G)$：基本群；$\Lambda_\char$、$\Lambda_\cochar$：特征格与其余特征格；$\Lambda_\rt$、$\Lambda_\cort$、$\Lambda_\wt$、$\Lambda_\cowt$：四个根/权格。

## 关键点

- $\mathcal{Z}(G)^\vee=\Lambda_\char/\Lambda_\rt$（式 (A.10)）与 $\mathcal{Z}(G)=\Lambda_\cowt/\Lambda_\cochar$（式 (A.11)）是同一事实的两面，靠式 (A.6) 与式 (A.7) 的对偶性互推。
- $\pi_1(G)^\vee=\Lambda_\wt/\Lambda_\char$（式 (A.12)）、$\pi_1(G)=\Lambda_\cochar/\Lambda_\cort$（式 (A.13)）：两个商分别从环面侧与对偶侧量出基本群。
- 庞特里亚金对偶 $(A^\vee)^\vee=A$ 把有限群对应到有限群；把它用于式 (A.14) 并与式 (A.11)、(A.13) 比较，即得式 (A.15) 的两条互换关系。
- 判据：$\Lambda_\char=\Lambda_\wt$ 等价于 $G$ 单连通（此时 $\pi_1=0$）；$\Lambda_\char=\Lambda_\rt$ 等价于伴随型（此时 $\mathcal{Z}(G)=0$，但 $\pi_1(G)=\Lambda_\cowt/\Lambda_\cort$ 一般非零）。
- 对偶交换中心与基本群：$\pi_1({}^LG)=\mathcal{Z}(G)^\vee$、$\mathcal{Z}({}^LG)=\pi_1(G)^\vee$（式 (A.15)），故 $G$ 单连通当且仅当 $^LG$ 伴随型。

## 公式

```latex
\Lambda_\char={\rm Hom}(\mathbb{T},U(1))
```
```latex
{\mathcal Z}(G)^\vee = \Lambda_\char/\Lambda_\rt
```
```latex
{\mathcal Z}(G)=\Lambda_\cowt/\Lambda_\cochar
```
```latex
\pi_1(G)^\vee=\Lambda_\wt/\Lambda_\char
```

## 常见错误

- 把 $\mathcal{Z}(G)$ 与 $\mathcal{Z}({}^LG)$ 当成相等的群：由式 (A.15) 它们互为对偶，阶相同但配对不同；误以为相等会把 $SU(N)$ 与 $PSU(N)$ 的中心/基本群算反。
- 把“中心地作用”当成平凡作用：若以为每个中心元都作用为 $1$，则式 (A.10) 的商写成零，进而把伴随型群误判为单连通。
- 把商写成 $\Lambda_\cort/\Lambda_\cochar$：对非单连通群（如 $PSU(N)$）这个商为零，会把它的基本群算成零，从而误判为单连通。

## 批注

### 易错预警：单连通不等于中心平凡

“单连通”只等价于 $\Lambda_\char=\Lambda_\wt$，即 $\pi_1(G)=0$；它绝不意味着 $\mathcal{Z}(G)=0$——$SU(N)$ 单连通而中心是 $\mathbb{Z}_N$，由 $\mathcal{Z}(G)^\vee=\Lambda_\wt/\Lambda_\rt$ 读出。把两者混同会把 $SU(N)$ 误当作伴随型，从而错用式 (A.13)。$PSU(N)$ 则相反：中心平凡而基本群为 $\mathbb{Z}_N$，两条判据正好交换，不能互相替代。反过来，由 $\pi_1(G)=0$ 也推不出 $\mathcal{Z}(G)=0$：$SU(N)$ 就是反例。

### 含糊点拨：“中心地作用”要补出什么

原文说 $\mathcal{Z}(G)$ acts centrally，意思是每个中心元 $z$ 在不可约表示 $R$ 上作用为标量 $e^{i\theta}$。哪个标量由最高权 $w\in\Lambda_\char$ 决定：$w\in\Lambda_\rt$ 时 $\theta=0$。补出这一层，才能理解为什么商掉 $\Lambda_\rt$ 才得到 $\mathrm{Hom}(\mathcal{Z}(G),U(1))$。同理，$\pi_1(G)$ 的元素在泛覆盖的表示上也作用为标量，式 (A.12) 正是用了这一点，它把群中心与环面的对偶联系起来。

### 背景直觉：为什么对偶交换中心与基本群

中心决定 't Hooft 通量（面算符的拓扑荷），基本群决定规范丛的扭结类。$S$-对偶交换电与磁，因此也交换这两类拓扑数据，这就是式 (A.15) 的物理内容；在几何朗兰兹中，它对应 $G$ 与 $^LG$ 的算符标号互换。注意对偶侧出现的是 $\mathcal{Z}({}^LG)$，不要把它与 $\pi_1(G)$ 混为一谈。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 附录 A；印刷页 [146, 148] / PDF 页 [147, 149]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/sA-duality.tex:100-160`
- 式 (A.8)–(A.15)：特征格、庞特里亚金对偶、中心与基本群及其对偶交换；印刷页 146–148，原文 PDF 第 147–149 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
