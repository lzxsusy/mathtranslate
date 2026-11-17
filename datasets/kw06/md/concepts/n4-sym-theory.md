# $\mathcal N=4$ 超对称杨–米尔斯理论

> `kw/concept/n4-sym-theory` · 轨道 A · 四维物理与对偶 · 状态 dev

> **先自测**：$\mathcal N=4$ 超对称杨–米尔斯理论是什么，它在整条论证链里起什么作用？

## 一句话

十维超对称杨–米尔斯降维得到的四维最大超对称规范理论：16 个超荷、$\mathrm{SU}(4)_R$ R-对称与复耦合 $\tau$；本文对它作拓扑扭化、紧化并读出几何 Langlands。

## 定义

四维 $\mathcal N=4$ 超对称杨–米尔斯理论由十维超对称杨–米尔斯理论作维数约化得到：十维的规范场给出一规范场，正手征旋量给出四个外尔费米子，再加六个实标量，共 16 个超荷。它的 R-对称群为 $\mathrm{SU}(4)_R\cong\mathrm{Spin}(6)$，复耦合为 $\tau=\theta/2\pi+4\pi\ii/e^2$。

**记号**：$G$ 紧致规范群；$e$ 规范耦合；$\theta$ 角；$\tau$ 复耦合；$M_H(G,C)$ 为 Hitchin 模空间。

## 要点（为什么需要它）

1. 整条推导链的起点：正是它的 16 个超荷允许三种扭化，其中 GL 扭化才通向几何 Langlands。
2. 十维降维自动产生 $\mathrm{SU}(4)_R$，这个 R-对称群正是扭化时被对角嵌入自旋群的那一半。
3. 复耦合 $\tau$ 同时装下 $\theta$ 与 $1/e^2$，S-对偶群 $\Gamma$ 才作用其上，进而定义扭化族的规范参数 $\Psi$。
4. 紧化到黎曼曲面 $C$ 后低能有效理论是 $M_H(G,C)$ 上的 sigma 模型，这是全文几何词典的来源。

## 核心公式

$$
$$I_4=\frac1{e^2}\int d^4x\,\mathrm{Tr}\Big(\frac12 F_{\mu\nu}F^{\mu\nu}+\sum_{i=1}^6 D_\mu\phi_iD^\mu\phi_i+\frac12\sum_{i,j=1}^6[\phi_i,\phi_j]^2\Big)$$$$\{Q^{AX},Q^Y_{\dot A}\}=\delta^X_Y\sum_{\mu=0}^3\Gamma^\mu_{A\dot A}P_\mu,\qquad \{Q,Q\}=\{\bar Q,\bar Q\}=0$$
$$

$$
$$\{Q^{AX},Q^Y_{\dot A}\}=\delta^X_Y\sum_{\mu=0}^3\Gamma^\mu_{A\dot A}P_\mu,\qquad \{Q,Q\}=\{\bar Q,\bar Q\}=0$$
$$

## 定理与证明（或缺口）

### 十维降维给出的四维场内容

十维超对称杨–米尔斯理论（规范场加一个正手征旋量）约化到四维后，给出一个规范场、四个外尔费米子与六个实标量，共 16 个超荷，按 $(2,1,4)\oplus(1,2,\bar4)$ 变换。

> 证明状态：**sketch**。原文 p.6–8 只说『most easily constructed by dimensional reduction』并列出四维表示，未逐步推导场内容；此条为按原文整理的物理陈述。

出处：`B p.6`

### 四维 $\mathcal N=4$ 超代数

两组超荷满足 $\{Q^{AX},Q^Y_{\dot A}\}=\delta^X_Y\sum_\mu\Gamma^\mu_{A\dot A}P_\mu$，且 $\{Q,Q\}=\{\bar Q,\bar Q\}=0$。

> 证明状态：**gap**。原文 p.11 直接给出 (2.15) 作为十维 (2.9) 的维数约化，未给证明。

出处：`B p.11 eq (2.15)`

## 常见误解

- 把 $\mathcal N=4$ 与 $\mathcal N=2$ 混淆：前者的 $\mathrm{SU}(4)_R$ 才允许 GL 扭化，$\mathcal N=2$ 的扭化只给出 Donaldson 型理论。
- 以为 $\tau$ 只是耦合常数：$\theta$ 与 $1/e^2$ 组合成上半平面的复参数，S-对偶作用在 $\tau$ 上而非单独作用在 $e$ 上。
- 误以为扭化是截断超对称：理论仍是同一个 $\mathcal N=4$，只是重新选取了对角嵌入。

## 相关卡

[超荷](../concepts/supercharge.md) · [R-对称](../concepts/r-symmetry.md) · [$\theta$ 角](../concepts/theta-angle.md) · [S-对偶](../concepts/s-duality.md)

## 出处（印刷页）

- B p.6–7（B p.6）
- B p.9（B p.9 eq (2.10)）
- B p.11（B p.11 eq (2.15)）

> 说明：A=原文：场内容、作用量 (2.10)、超代数 (2.15) 与 R-对称表示 (2.14)（B p.6–11）；C=整理：summary、key_points、pitfalls 的措辞；定理的 sketch/gap 标注按原文证据如实给出。
