# 阿贝尔化与 Prym 簇

> `gtgl15/concept/abelianization-prym` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：为什么一个非阿贝尔的希格斯丛可以被一条曲线上的线丛完全代替？

## 一句话

阿贝尔化把希格斯丛 $(E,\varphi)$ 换成谱曲线上的线丛 $\mathcal L$（$E=\psi_*\mathcal L$），于是 Hitchin 一般纤维落在 $D$ 的 Prym 簇里。

## 定义

在非分歧点 $p$ 上，$\varphi(p)$ 的本征空间分解给 $E_p=\bigoplus_i\mathcal N_{q_i}=\bigoplus_i\mathcal L_{q_i}$。反过来，给定 $D$ 上的线丛 $\mathcal L$，令 $E=\psi_*(\mathcal L)$、$\varphi=\psi_*(y)$，就得到 $C$ 上的希格斯丛。因此一般纤维是 $\{\mathcal L\in\mathrm{Pic}(D):\Lambda(\mathcal L)\text{ 固定}\}$，在 $SU(N)$ 情形与 $\mathrm{Prym}(D/C)=\ker(\mathrm{Nm}:\mathrm{Jac}(D)\to\mathrm{Jac}(C))$ 的 torsor 同构。

**记号**：$\psi:D\to C$；$\Lambda(\mathcal L)=\det\psi_*(\mathcal L)$；$\mathrm{Nm}$；$F\cong\mathrm{Prym}(D/C)$。

## 要点（为什么需要它）

1. 阿贝尔化把 $\MH$ 的纤维问题化归为 $D$ 上的线丛问题：非阿贝尔结构被推前操作吸收。
2. $E=\psi_*(\mathcal L)$ 是秩 $N$ 的向量丛，$\varphi=\psi_*(y)$ 的本征值恰是 $y$。
3. $\Lambda(\mathcal L)=\det\psi_*(\mathcal L)\cong\mathrm{Nm}(\mathcal L)\otimes K^{-N(N-1)/2}$，所以固定 $\Lambda$ 等价于固定 norm 映射的像。
4. $\dim\mathrm{Prym}(D/C)=g_D-g_C=(N^2-1)(g-1)=\dim\mathcal V$：维数对上了。
5. 分歧点上要用局部模型验证，推前仍给出 $E$ 与 $\varphi$（eq (2.27)(2.28)）。

## 核心公式

$$
$$E=\psi_*(\mathcal L),\qquad \varphi=\psi_*(y),\qquad F\cong\mathrm{Prym}(D/C)$$$$\dim\mathrm{Prym}(D/C)=g_D-g_C=(N^2-1)(g-1)$$
$$

$$
$$\dim\mathrm{Prym}(D/C)=g_D-g_C=(N^2-1)(g-1)$$
$$

## 定理与证明（或缺口）

### 一般纤维的阿贝尔化

$SU(N)$ 的 Hitchin 一般纤维同构于 $\mathrm{Prym}(D/C)$ 的 torsor。

> 证明状态：**sketch**。分歧点的核对原文 $\S2.6.2$ 用局部模型写出，但没有给出完整纤维同构的证明。

出处：`A p.13`

## 常见误解

- Prym 不是 $\mathrm{Jac}(D)$：要取 norm 为零（或固定）的部分，维数差 $g_C$。
- $E$ 是秩 $N$ 向量丛，$E_p=\bigoplus_i\mathcal L_{q_i}$ 只在非分歧点成立；分歧点上方不是直和。
- $N$ 为偶数时纤维只到 torsor，不是典范的阿贝尔簇；$K^{1/2}$ 的选择会平移它。
- 不要混淆 $\mathcal L$（余核线丛）与 $\mathcal N$（本征向量线丛）：阿贝尔化用 $\mathcal L$，§7 的平移本征丛也用 $\mathcal L$。

## 相关卡

[谱曲线](../concepts/spectral-curve.md) · [核线丛与余核线丛](../concepts/kernel-cokernel.md) · [希钦纤维化](../concepts/hitchin-fibration.md) · [对偶环面纤维化与 T-对偶](../concepts/dual-torus-fibration.md) · [一般纤维的阿贝尔化：$F\cong\mathrm{Prym}(D/C)$](../derivations/prym-abelianization.md)

## 出处（印刷页）

- A p.13–14（A p.13 eq (2.24)）
- A p.15（A p.15 eq (2.34)）
- A p.25–26（A p.26 eq (3.5)）

> 说明：A=原文 $\S2.6.2$ 的非分歧点分解与 eq (2.25)(2.29)、$\S2.6.3$ 的 $\Lambda^{-1}(\mathcal O)$、$\S3.2$ 的 norm 映射；B=把“一般纤维是 Prym torsor”整理成三步；C=维数等式按 $g_D$ 公式计算。最没把握处：Prym 与模 $K^{1/2}$ 的 torsor 结构原文分散在 $\S2.6.3$ 与 $\S3.2$。
