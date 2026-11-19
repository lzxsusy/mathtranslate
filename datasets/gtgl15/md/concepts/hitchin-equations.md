# 希钦方程

> `gtgl15/concept/hitchin-equations` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：希钦方程的两个方程分别对应超凯勒商的哪一部分条件？

## 一句话

希钦方程把希格斯场与酉联络耦合起来：$F_{z\bar z}-[\varphi_z,\varphi_{\bar z}]=0$ 且 $\varphi$ 全纯，是二维自对偶方程在紧黎曼面上的形式。

## 定义

$C$ 上希格斯丛 $(E,\varphi)$ 与 $E$ 上酉联络 $D$ 满足的方程：$F_{z\bar z}-[\varphi_z,\varphi_{\bar z}]=0$，$D_{\bar z}\varphi_z=D_z\varphi_{\bar z}=0$。用复联络 $\mathcal A=A+i\varphi$ 写，等价于 $\mathcal F=0$、$D\star\varphi=0$。

**记号**：$F$ 为 $D$ 的曲率；$\mathcal A=A+i\varphi$；$\tau=\theta/2\pi+4\pi i/e^2$。

## 要点（为什么需要它）

1. 第二式是 $\bar\partial$ 条件：$\varphi_z\,dz$ 关于 $D$ 全纯；它使 $(E,\varphi)$ 成为全纯希格斯丛。
2. 第一式是 moment map 条件：曲率的 $(1,1)$ 部分被 $[\varphi_z,\varphi_{\bar z}]$ 抵消。
3. 两式合起来是超凯勒矩映射 $(\nu_I,\nu_J,\nu_K)=0$ 的一部分；解模去规范群得 $\MH$（$\S2.2$）。
4. $G=U(1)$ 时方程线性化：$F$ 与 $\varphi$ 解耦，$\varphi$ 只是 $H^0(C,K)$ 中的元素（$\S7.1.1$）。
5. 对紧黎曼面上任意稳定希格斯丛，方程总有解（Hitchin）；这是 $\MH$ 作为模空间的定义方式。

## 核心公式

$$
$$F_{z\bar z}-[\varphi_z,\varphi_{\bar z}]=0,\qquad D_{\bar z}\varphi_z=D_z\varphi_{\bar z}=0$$$$\mathcal F=0,\qquad D\star\varphi=0,\qquad \mathcal A=A+i\varphi$$
$$

$$
$$\mathcal F=0,\qquad D\star\varphi=0,\qquad \mathcal A=A+i\varphi$$
$$

## 定理与证明（或缺口）

### 方程解空间是有限维超凯勒流形

稳定希格斯丛上的希钦方程解模去规范群后是光滑流形，且继承超凯勒结构。

> 证明状态：**gap**。原文 $\S2.2$ 引用 [13][19] 的超凯勒商构造，未给证明。

出处：`A p.4`

### 第二式即全纯性

$D_{\bar z}\varphi_z=0$ 等价于说 $\varphi$ 定义了一个全纯截面 $\varphi\in H^0(C,K\otimes\operatorname{End}E)$。

1. 希格斯场的 $(0,1)$-分量是 $\bar\partial_D$，它在全纯标架下消失。
   - *为什么*：$\bar\partial_D$ 作用在 $\varphi_z$ 上正是 $D_{\bar z}\varphi_z$。
2. $D_z\varphi_{\bar z}=0$ 是它的复共轭，保证 $\varphi$ 的 $(1,0)$ 部分全纯。
   - *为什么*：两式合起来给出 $H^0$ 中的截面。

出处：`A p.5 eq (2.2)`

## 常见误解

- 希钦方程不是三个独立方程：实 moment map 只有一维，另外两个复条件合起来才是两式。
- 符号约定依赖复结构与度量的选取；抄公式时不要漏掉 $[\varphi_z,\varphi_{\bar z}]$ 的符号。
- 有希格斯丛不等于有解：解的存在性要求稳定性，这正是 $\MH$ 与“所有希格斯丛”的区别。
- $U(1)$ 情形没有非平凡耦合，别把非阿贝尔的 $[\varphi,\bar\varphi]$ 项套到 $U(1)$ 上。

## 相关卡

[希格斯丛与希钦对](../concepts/higgs-bundle.md) · [超凯勒商与复结构 I、J、K](../concepts/hyperkahler-quotient.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [二维 $\sigma$-模型与靶空间 $\MH$](../concepts/sigma-model-mh.md) · [希钦方程 = 超凯勒矩映射商](../derivations/hitchin-as-moment-map.md)

## 出处（印刷页）

- A p.4–6（A p.4 eq (2.1)）
- A p.5（A p.5 eq (2.2)）
- C p.59–126（C p.59）

> 说明：A=原文 $\S2.2$ 的方程 eq (2.1)(2.2)；B=把两式解释为超凯勒矩映射的条件；C=紧黎曼面上解的存在性按 Hitchin 1987 背景补全。最没把握处：$\tau$ 归一化只在 $\S3.4$ 与 $\S7.1$ 间接出现。
