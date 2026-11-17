# 希格斯场

> `kw/concept/higgs-field` · 轨道 C · 舞台：曲线与模空间 · 状态 dev

> **先自测**：希格斯场 $\varphi$ 是什么，它为什么同时是场和余切方向？

## 一句话

紧化后在 $C$ 上留下的 $(1,0)$-形式场 $\varphi$，即 $K_C\otimes\mathrm{ad}E$ 的全纯截面；它与联络 $A$ 一起编码 Hitchin 方程，并在复结构 $J$ 下与 $A$ 合成平坦 $G_{\mathbb C}$ 联络。

## 定义

紧化到 $C$ 后，规范场论里取值于伴随丛的 1-形式场在 $C$ 上的 $(1,0)$-部分记为 $\varphi=\varphi_z\,dz$；作为 Hitchin 对的数据，它是 $H^0(C,K_C\otimes\mathrm{ad}E)$ 的全纯截面。它有两个身份：物理上的物质场，以及 $M_H$ 中与 $A$ 配对的几何数据；在复结构 $J$ 下 $A+\mathrm{i}\varphi$ 是平坦的 $G_{\mathbb C}$ 联络。

**记号**：$\varphi=\varphi_z\,dz$；$\varphi\in H^0(C,K_C\otimes\mathrm{ad}E)$；$A+\mathrm{i}\varphi$：$\mathfrak g_{\mathbb C}$-联络；$D\varphi$：协变导数。

## 要点（为什么需要它）

1. 物理来源：扭化把四维理论的 6 个标量中的 4 个重解释为 1-形式 $\varphi$，紧化到 $C$ 后它贡献 $C$ 上的 1-形式零模。
2. 几何身份：$\varphi$ 是稳定丛模空间 $M$ 的余切向量（Serre 对偶），所以 $M_H$ 包含 $T^*M$ 作为开稠密子集。
3. 方程语言：$\nu_I=0$ 等价于 $\bar\partial_A\varphi=0$，故 $\varphi$ 全纯；$\nu_J=0$ 等价于 $F(A+\mathrm{i}\varphi)=0$，故它与 $A$ 合成平坦复联络。
4. 复结构依赖：$\varphi$ 在 $I$ 下是全纯对象，换到 $J,K$ 就不再全纯，这正是超凯勒结构的用处。

## 核心公式

$$
$\varphi=\varphi_z\,dz\in H^0(C,K_C\otimes\mathrm{ad}E)$$F-\varphi\wedge\varphi=0,\qquad D\varphi=D\star\varphi=0$$\nu_I=0\iff\bar\partial_A\varphi=0,\qquad \nu_J=0\iff F(A+\mathrm{i}\varphi)=0$
$$

$$
$F-\varphi\wedge\varphi=0,\qquad D\varphi=D\star\varphi=0$
$$

$$
$\nu_I=0\iff\bar\partial_A\varphi=0,\qquad \nu_J=0\iff F(A+\mathrm{i}\varphi)=0$
$$

## 定理与证明（或缺口）

### Hitchin 方程的复形式（$\nu_J=0$）

$\nu_J=\mu_K+\mathrm{i}\mu_I=0$ 当且仅当 $A+\mathrm{i}\varphi$ 作为 $G_{\mathbb C}$-联络是平坦的，即 $F(A+\mathrm{i}\varphi)=0$。

> 证明状态：**sketch**。原文 p.51 只写出 (4.21) 与 $\nu_J=0\iff F(A+\mathrm{i}\varphi)=0$ 的结论；曲率分裂式按解经本的重建补出（B），原文未展开。

出处：`B p.51`

## 常见误解

- 把 $\varphi$ 当成标量或 0-形式：没有 $dz$ 指标，$A+\mathrm{i}\varphi$ 就不成其为 1-形式联络。
- 把 (4.1) 与 (4.21) 里的 $F$ 当成同一个：前者是实联络 $A$ 的曲率，后者是复联络 $A+\mathrm{i}\varphi$ 的曲率。
- 把某个复结构下的型当成内在性质：同一个实 1-形式 $\varphi$ 在 $I$ 与 $J$ 下分解不同，全纯性随复结构改变。

## 相关卡

[希格斯丛](../concepts/higgs-bundle.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [复结构](../concepts/complex-structure.md) · [紧化到 Hitchin 方程：M = Σ×C](../derivations/compactify-to-hitchin.md)

## 出处（印刷页）

- B p.38–39（B p.39）
- B p.49（B p.49）
- B p.56（B p.56）

> 说明：A=原文（$\varphi$ 作为 $C$ 上的 1-形式零模、$\varphi\in H^0(C,K_C\otimes\mathrm{ad}E)$ 的全纯截面、$F(A+\mathrm{i}\varphi)=0$、扭化中 4 个标量变 1-形式）；B=由原文重建（两个身份的对照、曲率分裂式）；C=标准背景（伴随丛语言的表述）。
