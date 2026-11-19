# 希格斯丛与希钦对

> `gtgl15/concept/higgs-bundle` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：为什么四维规范理论在 $C$ 上的低能真空要用希格斯丛而不是普通向量丛来参数化？

## 一句话

希格斯丛是复曲线 $C$ 上全纯丛 $E$ 与取值于 $K$ 的希格斯场 $\varphi$ 组成的对，它同时是希钦方程解与谱曲线几何的载体。

## 定义

设 $C$ 是紧黎曼面，$K$ 是典范丛，$G_\mathbb{C}$ 是复约化群。一个 $G_\mathbb{C}$-希格斯丛是二元组 $(E,\varphi)$：$E\to C$ 是 $G_\mathbb{C}$ 主丛（或相应向量丛），$\varphi\in H^0(C,K\otimes\operatorname{ad}E)$ 是希格斯场。对 $G=SU(N)$ 要求 $\det E\cong\mathcal O$、$\operatorname{Tr}\varphi=0$；对 $G=U(N)$ 允许 $c_1(E)$ 非零。

**记号**：$(E,\varphi)$；$K$；$\varphi_z\,dz$；$\MH$；$\mathcal M$。

## 要点（为什么需要它）

1. $\varphi$ 是 $(1,0)$-形式、取值于 $\operatorname{End}E$；它把 $T^*C$ 上的坐标 $y$ 变成矩阵，$\det(y-\varphi)=0$ 就是谱曲线。
2. $(E,\varphi)$ 的模空间恰是希钦方程解模去规范群：$\varphi$ 与联络 $D$ 通过 $\S2.2$ 的方程耦合。
3. $\varphi=0$ 时希格斯丛退化为稳定全纯丛；$\mathcal M$ 通过 $\varphi=0$ 以 $I$-全纯 Lagrangian 方式嵌入 $\MH$（$\S2.3$）。
4. 对 $U(N)$，$\MH$ 只参数化 $c_1(E)=0$ 的希格斯丛；$c_1\ne0$ 的对象出现在 't Hooft 算符作用之后，需保留 $U(1)$ 规范场（$\S7.1.2$）。
5. 一般 Hitchin 纤维上的点自动稳定（$\S5.2$ 脚注 17）：这是把 Hecke 作用限制在纤维上的关键。

## 核心公式

$$
$$(E,\varphi),\qquad \varphi\in H^0(C,K\otimes\operatorname{End}E)$$$$\det(y-\varphi)=0$$
$$

$$
$$\det(y-\varphi)=0$$
$$

## 定理与证明（或缺口）

### 非阿贝尔 Hodge 对应

$\MH$ 作为实流形同构于 $C$ 上 $G$-平坦联络模空间：复结构 $I$ 来自希格斯丛，$J$ 来自平坦联络。

> 证明状态：**sketch**。原文 $\S2.2$ 只引用 [13][20][21]，未给证明。

出处：`A p.4`

### 一般纤维上的希格斯丛稳定

在 Hitchin 纤维化的一般纤维上，每一点对应的希格斯丛都是稳定的。

> 证明状态：**gap**。原文 $\S5.2$ 脚注 17 一句话带过，证明在 [13][21]。

出处：`A p.56`

## 常见误解

- 希格斯场不是标量：$\varphi$ 是 $(1,0)$-形式，$y$ 只有在谱曲线上才是数值。
- 希格斯丛的稳定性不等同于丛的稳定性：$\varphi$ 进入斜率条件；$\varphi=0$ 时才回到丛的稳定性。
- $\MH$ 非紧，无穷远处的行为影响单极子与拓扑荷的讨论（$\S2.1$）。
- 把 $U(N)$ 与 $SU(N)$ 混为一谈会漏掉 $c_1(E)$ 与中心 $U(1)$ 的作用。

## 相关卡

[希钦方程](../concepts/hitchin-equations.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [稳定丛模空间与余切丛](../concepts/stable-locus.md) · [谱曲线](../concepts/spectral-curve.md) · [二维 $\sigma$-模型与靶空间 $\MH$](../concepts/sigma-model-mh.md)

## 出处（印刷页）

- A p.2–3（A p.2）
- A p.4–5（A p.4 eq (2.1)）
- C p.59–126（C p.59）

> 说明：A=原文 $\S2.1$–$\S2.2$ 的定义与 $\S2.6.5$ 对 $U(N)$ 的说明；B=我们用“特征多项式→谱曲线”的说法重建；C=非阿贝尔 Hodge 对应按标准背景补全。最没把握处：稳定性的精确定义原文只在 $\S5.2$ 脚注 17 提了一句。
