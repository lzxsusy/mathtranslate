# R-对称

> `kw/concept/r-symmetry` · 轨道 B · 扭化与拓扑 · 状态 dev

> **先自测**：R-对称是什么，它在整条论证链里起什么作用？

## 一句话

作用在超荷上的内部对称群；$\mathcal N=4$ 时为 $\mathrm{SU}(4)_R\cong\mathrm{Spin}(6)$，扭化就是把它的一个 $U(1)$ 嵌进自旋群，其中心 $I$ 也标定 S-对偶的相因子。

## 定义

R-对称是作用在超荷上、与时空对称群交换的内部对称群。四维 $\mathcal N=4$ 超杨–米尔斯理论的 R-对称群为 $\mathrm{SU}(4)_R\cong\mathrm{Spin}(6)$，超荷按 $4$ 与 $\bar4$ 变换。

**记号**：$X,Y=1,\dots,4$ 为 $\mathrm{SU}(4)_R$ 指标；$I$ 为中心元；$\mathrm{Spin}(6)\cong\mathrm{SU}(4)_R$。

## 要点（为什么需要它）

1. 扭化的定义就是把 R-对称的一部分与自旋群对角嵌入，不了解 $\mathrm{SU}(4)_R$ 就无法写出 GL 扭化。
2. $\mathrm{SU}(4)_R$ 的中心 $I$ 作用在超荷的相因子上，使 $\hat\varphi$ 只定义到 $\hat\varphi+\pi/2$，这决定 S-对偶双覆盖的结构。
3. 它把超荷分成 $4$ 与 $\bar4$，对应 $(2,1,4)\oplus(1,2,\bar4)$ 的表示分解，是扭化后超荷分类的依据。
4. 对偶变换被要求与 $\mathrm{SU}(4)_R$ 交换，这是一条实质选择，固定了超荷相因子。

## 核心公式

$$
$$\mathrm{Spin}(6)\cong\mathrm{SU}(4)_R,\qquad (2,1,4)\oplus(1,2,\bar4)$$$$I:\ \mathbf4\mapsto\ii\,\mathbf4,\qquad \bar{\mathbf4}\mapsto-\ii\,\bar{\mathbf4},\qquad \hat\varphi\to\hat\varphi+\frac{\pi}{2}$$
$$

$$
$$I:\ \mathbf4\mapsto\ii\,\mathbf4,\qquad \bar{\mathbf4}\mapsto-\ii\,\bar{\mathbf4},\qquad \hat\varphi\to\hat\varphi+\frac{\pi}{2}$$
$$

## 定理与证明（或缺口）

### 对偶变换可与 $\mathrm{SU}(4)_R$ 交换

设 $\gamma\in\Gamma$ 为 S-对偶变换。$\gamma$ 与庞加莱群交换，且可乘一个 $\mathrm{SU}(4)_R$ 元素使其与 $\mathrm{SU}(4)_R$ 交换；于是 $\gamma$ 在 $4$ 与 $\bar4$ 超荷上按 $e^{\ii\hat\varphi}$ 与 $e^{-\ii\hat\varphi}$ 作用。

1. 共轭作用给出 $\mathrm{SU}(4)_R$ 的一个自同构。
   - *为什么*：$\gamma$ 是理论的自同构，把 R-对称群映到自身。
2. 该自同构必为内自同构。
   - *为什么*：原文 p.13 脚注 4：经典理论没有在时空上作用平凡、而在 $\mathrm{SU}(4)_R$ 上为外自同构的对称。
3. 用 $\mathrm{SU}(4)_R$ 元素抵消这个内自同构，得到与 $\mathrm{SU}(4)_R$ 交换的对偶变换。
   - *为什么*：内自同构可由 $\mathrm{SU}(4)_R$ 元素实现，乘其逆即可。

出处：`B p.13`

### 中心 $I$ 的作用

$\mathrm{SU}(4)_R$ 的中心由 $I$ 生成，$I$ 在 $4$ 上作用为 $\ii$、在 $\bar4$ 上为 $-\ii$；故 $\hat\varphi$ 定义到 $\hat\varphi+\pi/2$。

> 证明状态：**gap**。原文 p.14 直接陈述该中心作用（$\mathrm{SU}(4)$ 表示论事实），未给证明。

出处：`B p.14`

## 常见误解

- 把 R-对称当成与时空无关的普通内部对称：它的指标与超荷的时空手征性绑定，$(2,1,4)\oplus(1,2,\bar4)$ 的配对才关键。
- 以为中心元 $I$ 是单位：$I$ 在 $4$ 与 $\bar4$ 上分别为 $\pm\ii$，且 $I^2=(-1)^F$，这正是 S-对偶需要双覆盖的原因。
- 以为扭化用到整个 $\mathrm{SU}(4)_R$：实际只用一个 $U(1)_K$，剩下的 $\mathrm{SU}(2)_\ell\times\mathrm{SU}(2)_r$ 仍保留。

## 相关卡

[$\mathcal N=4$ 超对称杨–米尔斯理论](../concepts/n4-sym-theory.md) · [超荷](../concepts/supercharge.md) · [拓扑扭化](../concepts/topological-twist.md) · [GL 扭化的构造：选哪个 Spin(4)](../derivations/twist-construction.md)

## 出处（印刷页）

- B p.10（B p.10 eq (2.14)）
- B p.13（B p.13）
- B p.18（B p.18）

> 说明：A=原文：$\mathrm{Spin}(6)\cong\mathrm{SU}(4)_R$ 与 (2.14) (p.10)、脚注 4 的三步论证 (p.13)、中心 $I$ 的作用 (p.14)、扭化嵌入 (p.18)；C=整理：summary、key_points、pitfalls。
