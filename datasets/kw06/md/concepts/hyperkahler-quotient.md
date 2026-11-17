# 超凯勒商

> `kw/concept/hyperkahler-quotient` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：超凯勒商怎样把 Hitchin 方程的求解变成几何构造？

## 一句话

对超凯勒流形取三个矩映射同时为零、再模去群作用，得 $X/\!/\!/H=\vec\mu^{-1}(0)/H$；它自动继承超凯勒结构，$M_H=\mathcal W/\!/\!/G$ 是主要例子。

## 定义

设超凯勒流形 $X$ 上李群 $H$ 保持三个复结构地作用，并有三个矩映射 $\mu_I,\mu_J,\mu_K$；则 $\vec\mu^{-1}(0)/H$ 继承超凯勒结构，称为超凯勒商 $X/\!/\!/H$。取 $X=\mathcal W$（$C$ 上所有 $(A,\varphi)$ 构成的仿射空间）、$H$ 为规范群，三个矩映射同时为零恰是 Hitchin 方程，于是 $M_H=\mathcal W/\!/\!/G$。

**记号**：$X/\!/\!/H=\vec\mu^{-1}(0)/H$；$\vec\mu=(\mu_I,\mu_J,\mu_K)$；$\nu_I=\mu_J+\mathrm{i}\mu_K$；$M_H=\mathcal W/\!/\!/G$。

## 要点（为什么需要它）

1. 技术核心：把「解三个方程再模去规范群」翻译成「取矩映射零点再除以群」，于是超凯勒性由矩映射的线性代数给出。
2. 三个零点分别对应 (4.1) 的方程：$\mu_I=0$ 给 $F-\varphi\wedge\varphi=0$，$\nu_I=0$ 给 $\varphi$ 的全纯性，合起来就是 Hitchin 方程。
3. 物理解释：二维 $(4,4)$ 规范理论中 hypermultiplet 参数化 $X$，低能有效理论就是 $X/\!/\!/H$ 上的 sigma 模型，这是 $M_H$ 成为靶空间的来源。
4. 两种商必须区分：(I) 实矩映射约束加 $G$-商给出超凯勒流形；(II) 直接取 $G_{\mathbb C}$-商只得到复流形。

## 核心公式

$$
$\mu_I=-\frac{1}{2\pi}\int_C\mathrm{Tr}\,\epsilon\,(F-\varphi\wedge\varphi)$$M_H=\mathcal W/\!/\!/G=\vec\mu^{-1}(0)/G$
$$

$$
$M_H=\mathcal W/\!/\!/G=\vec\mu^{-1}(0)/G$
$$

## 定理与证明（或缺口）

### 超凯勒商定理（HKLR）

若 $X$ 是超凯勒流形、$H$ 保持三个复结构地作用且三个矩映射存在，则 $\vec\mu^{-1}(0)/H$ 继承超凯勒结构。

> 证明状态：**gap**。原文 p.46 引用 [61]（HKLR）的定理，只陈述结论，未复述证明。

出处：`B p.46`

### Hitchin 方程等价于三个矩映射同时为零

对 $X=\mathcal W$、$H$ 为规范群，Hitchin 方程 (4.1) 等价于 $\mu_I=\mu_J=\mu_K=0$ 同时成立，故 $M_H=\mathcal W/\!/\!/G$。

> 证明状态：**sketch**。原文 p.45 只说「a short computation shows」，未展示积分细节；对照关系见 (4.11) 与 (4.20)。

出处：`B p.45`

## 常见误解

- 只取一个矩映射就作商：那只是辛商，得到的空间一般不再是超凯勒，三个复结构无法同时使用。
- 把 $M_H$ 当成某个普通 GIT 商：必须三个矩映射同时为零，只用 $\mu_I=0$ 一项不够。
- 以为 $\mathcal W$ 无穷维使构造失效：矩映射对每个 $\epsilon$ 逐点积分，超凯勒商仍成立，只是得到的 $M_H$ 非紧。
- 混淆实矩映射与全纯矩映射：$\nu_I=\mu_J+\mathrm{i}\mu_K$ 不是第四个矩映射。

## 相关卡

[矩映射](../concepts/moment-map.md) · [超凯勒流形](../concepts/hyperkahler-manifold.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [超凯勒商与三个复结构 I, J, K](../derivations/hyperkahler-quotient.md)

## 出处（印刷页）

- B p.45（B p.45）
- B p.46（B p.46 eq (4.11)）
- B p.49（B p.49 eq (4.20)）

> 说明：A=原文（三个矩映射的显式式 (4.11)、Hitchin 方程等于三个矩映射零点、HKLR 商定理、二维 $(4,4)$ 理论的解释）；B=由原文重建（两种商的对照、$\nu_I$ 与全纯性的对应）；C=标准背景（辛商与超凯勒商的区别）。
