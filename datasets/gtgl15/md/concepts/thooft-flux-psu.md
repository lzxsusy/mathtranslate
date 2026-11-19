# 't Hooft flux 与 $PSU(N)$ 分量

> `gtgl15/concept/thooft-flux-psu` · 轨道 B · 对偶环面与 T-对偶 · 状态 dev

> **先自测**：为什么去掉中心 $Z_N$ 之后，模空间会分裂成由离散拓扑荷标号的分量？

## 一句话

$PSU(N)=SU(N)/\mathbb Z_N$ 的希格斯丛按 't Hooft flux $\xi\in H^2(C,\mathbb Z_N)$ 分成 $N$ 个分量，其 Hitchin 纤维是 $\mathrm{Pic}$ 模掉 $\mathrm{Jac}(C)$。

## 定义

$PSU(N)$ 丛在 $C$ 上的拓扑由 't Hooft flux $\xi\in H^2(C,\mathbb Z_N)\cong\mathbb Z_N$ 刻画。固定 $\xi=d$ 的分量记 $\MH^{(d)}(PSU(N))$，其 Hitchin 纤维是 $F^{(d)}_{PSU(N)}=\mathrm{Pic}_{c_0+d}(D)/\mathrm{Jac}(C)=\Lambda^{-1}(S_0)/\Gamma_N$，其中 $\Gamma_N$ 是 $N$-阶线丛群。对偶地，$\MH^{(d)}_{PSU(N)}$ 与带非平凡 gerbe 的 $\MH(SU(N))$ 对偶（$\S6.3$、KW06 §7 的离散 B-场）。

**记号**：$\xi\in H^2(C,\mathbb Z_N)$；$d$；$\Gamma_N\cong\mathbb Z_N$；$F^{(d)}_{PSU(N)}$。

## 要点（为什么需要它）

1. $PSU(N)$ 丛的拓扑荷是 $H^2(C,\mathbb Z_N)$ 的元素：$N$ 个离散选择，对应 't Hooft flux。
2. 每个分量内部的纤维是阿贝尔簇商 $\mathrm{Jac}(D)/\mathrm{Jac}(C)$，不再是 Prym 本身。
3. $\Gamma_N$（$N$-阶线丛）作用在 $F_{SU(N)}$ 上，商掉它得到 $F^{(0)}_{PSU(N)}$（eq (2.38)）。
4. 对偶的不是 $PSU(N)$ 与 $PSU(N)$，而是 $PSU(N)$ 与 $SU(N)$：自由侧的分量数对应另一侧的 gerbe。
5. 't Hooft flux 是 4d 理论的离散 $\theta$ 角/离散 B-场的几何来源；也是 §7 中非阿贝尔赫克本征值出现 $c_1$ 修正的根源。

## 核心公式

$$
$$0\to\mathbb Z_N\to SU(N)\to PSU(N)\to1,\qquad \xi\in H^2(C,\mathbb Z_N)$$$$F^{(d)}_{PSU(N)}=\mathrm{Pic}_{c_0+d}(D)/\mathrm{Jac}(C)\cong F_{SU(N)}/\Gamma_N$$
$$

$$
$$F^{(d)}_{PSU(N)}=\mathrm{Pic}_{c_0+d}(D)/\mathrm{Jac}(C)\cong F_{SU(N)}/\Gamma_N$$
$$

## 定理与证明（或缺口）

### PSU(N) 纤维的分量结构

$\MH^{(d)}(PSU(N))$ 的纤维是 $\mathrm{Pic}_{c_0+d}(D)/\mathrm{Jac}(C)$，且 $\mathrm{Jac}(C)$ 由 $\psi^*$ 的像给出。

> 证明状态：**sketch**。完整分类的证明原文引用 [1]；本文给出的是与谱曲线一致的陈述。

出处：`A p.18`

## 常见误解

- $\xi\in H^2(C,\mathbb Z_N)$ 不是 $H^2(C,\mathbb Z)$：它是 $N$-挠的，只有 $N$ 个值。
- $PSU(N)$ 的 Hitchin 纤维不是“Prym”：要再商掉 $\mathrm{Jac}(C)$，维数少 $g$。
- 不要漏掉 $c_0+d$ 的平移：不同的 't Hooft flux 对应不同的 $\mathrm{Pic}$ 分量。
- 对偶一侧带的是 gerbe（离散 B-场），不是普通流形；把对偶说成“$PSU$ 对 $PSU$”是错的。

## 相关卡

[希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [对偶环面纤维化与 T-对偶](../concepts/dual-torus-fibration.md) · [Gerbe 与 $B$-场（离散电/磁荷）](../concepts/gerbe-bfield.md) · [阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · ['t Hooft 算符](../concepts/thooft-operator.md)

## 出处（印刷页）

- A p.18–20（A p.18 eq (2.38)）
- A p.26（A p.26 eq (3.8)）
- A p.63–64（A p.64）

> 说明：A=原文 $\S2.6.6$ 的 $PSU(N)$ 拓扑荷与 eq (2.38)–(2.42)、$\S3.2$ 的对偶表述、$\S6.3$ 的 gerbe；B=把分量结构拆成两步；C=与 KW06 §7 离散 B-场的对应按原文引文补。最没把握处：$\Gamma_N$ 作用的精确阶数与 $K^{1/2}$ 的相容性原文未展开。
