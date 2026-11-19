# S-对偶

> `kw/concept/s-duality` · 轨道 A · 四维物理与对偶 · 状态 dev

> **先自测**：S-对偶是什么，它在整条论证链里起什么作用？

## 一句话

四维 $\mathcal N=4$ 的强弱对偶猜想：$\tau\mapsto-1/(n_g\tau)$，同时把 $G$ 换成 ${}^LG$、电换磁；它与 $T:\tau\mapsto\tau+1$ 生成离散群 $\Gamma$。

## 定义

S-对偶猜想断言四维 $\mathcal N=4$ 超杨–米尔斯理论存在一个量子对称 $S$，它把 $\tau$ 变为 $-1/(n_g\tau)$、把规范群 $G$ 换成 Langlands 对偶群 ${}^LG$ 并交换电与磁荷；$S$ 与经典对称 $T:\tau\mapsto\tau+1$ 一起生成子群 $\Gamma\subset\mathrm{SL}(2,\mathbb R)$。

**记号**：$n_g$ 为 lacing number（$ADE$ 为 1，$B,C,F_4$ 为 2，$G_2$ 为 3）；$\tau=\theta/2\pi+4\pi\ii/e^2$；$\Gamma$ 为 $\mathrm{SL}(2,\mathbb Z)$ 或其非单边变体。

## 要点（为什么需要它）

1. 全文的关键物理输入：二维极限下 $S$ 变成 $M_H(G,C)$ 与 $M_H({}^LG,C)$ 之间的镜像对称，两个几何由此连接。
2. 只有把 $\theta$ 与 $e$ 合成 $\tau$，强弱对偶才成为 $\mathrm{SL}(2,\mathbb Z)$ 的算术作用，这是 $\theta$ 角在本文中不可省的原因。
3. 非单边群必须用 $n_g$ 修正反演：$S:\tau\mapsto-1/(n_g\tau)$，$n_g=2,3$ 正对应 $F_4$、$G_2$（$\mathrm{Spin}(2k+1)$ 与 $\mathrm{Sp}(k)$ 也取 $n_g=2$，见 KW2006 p.12）。
4. $S$ 在超荷上不是经典作用，而是手征旋转；其相因子含平方根，故作用群是 $\Gamma$ 的双覆盖，需用 $(-1)^F$ 扩张。

## 核心公式

$$
$$S=\begin{pmatrix}0&1\\-1&0\end{pmatrix}:\quad \tau\mapsto-\frac{1}{\tau},\qquad T:\ \tau\mapsto\tau+1$$$$\exp\big(-\ii\hat\varphi(\gamma)\big)=\Big(\frac{|c\tau+d|}{c\tau+d}\Big)^{1/2},\qquad \gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma$$$$\tau\mapsto\frac{a\tau+b}{c\tau+d},\qquad (\tilde m,\tilde n)\mapsto(\tilde m,\tilde n)M^{-1}$$
$$

$$
$$\exp\big(-\ii\hat\varphi(\gamma)\big)=\Big(\frac{|c\tau+d|}{c\tau+d}\Big)^{1/2},\qquad \gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma$$
$$

$$
$$\tau\mapsto\frac{a\tau+b}{c\tau+d},\qquad (\tilde m,\tilde n)\mapsto(\tilde m,\tilde n)M^{-1}$$
$$

## 定理与证明（或缺口）

### S-对偶猜想

四维 $\mathcal N=4$ 理论在 $\tau\mapsto-1/(n_g\tau)$ 下等价于以 ${}^LG$ 为规范群、电与磁互换的理论；该对称把 Coulomb 分支上的 $\mathrm{SL}(2,\mathbb Z)$ 作用提升为全理论的对称。

> 证明状态：**gap**。原文 p.11 明确称为『S-duality conjecture』；p.15 只给出低能有效理论上的 $\mathrm{SL}(2,\mathbb Z)$ 作用与中心荷变换，未给证明。

出处：`B p.11 eq (2.16)`

### 中心荷在 $\mathrm{SL}(2,\mathbb Z)$ 下的变换

在 Coulomb 分支上，$\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ 作用后 $Z\mapsto\frac{|c\tau+d|}{c\tau+d}Z$。

> 证明状态：**sketch**。原文 p.15 只写『one deduces』，未展示代数细节；下面两步是我们补出的骨架。

出处：`B p.15 eq (2.24)`

## 常见误解

- 把 S-对偶说成只是 $\tau\mapsto-1/\tau$：必须同时把 $G$ 换成 ${}^LG$ 并交换电/磁荷，漏掉群的对偶就只剩算术作用。
- 以为 $S$ 是经典拉氏量的对称：除 $T$ 外 $\Gamma$ 不含经典对称，$S$ 是量子对称，只能在 BPS 谱等量子数据上检验。
- 忽略 $n_g$：非单边时反演是 $-1/(n_g\tau)$；把 $F_4$ 也写成 $-1/\tau$ 是常见错误。

## 相关卡

[电磁对偶](../concepts/electromagnetic-duality.md) · [Langlands 对偶群](../concepts/langlands-dual-group.md) · [$\theta$ 角](../concepts/theta-angle.md) · [S-对偶 = 镜像对称（全文心脏）](../derivations/sdual-mirror.md)

## 出处（印刷页）

- B p.11（B p.11 eq (2.16)）
- B p.15（B p.15 eq (2.24)）
- B p.16（B p.16 eq (2.25)）

> 说明：A=原文：猜想表述、(2.16)、(2.24)、(2.25)（B p.11–16）；C=整理：summary、key_points、pitfalls 与定理二的两步骨架；猜想按原文标为 gap。
