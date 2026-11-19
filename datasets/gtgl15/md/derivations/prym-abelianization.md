# 一般纤维的阿贝尔化：$F\cong\mathrm{Prym}(D/C)$

> `gtgl15/deriv/prym-abelianization` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev · 5 步

> **要回答的问题**：为什么 Hitchin 一般纤维可以写成 Prym 簇的 torsor，而不是别的阿贝尔簇？

## 一句话

利用非分歧点的本征分解 $E_p=\bigoplus_i\mathcal L_{q_i}$ 与推前 $E=\psi_*\mathcal L$，一般纤维是 $\mathrm{Prym}(D/C)$ 的 torsor，维数吻合。

## 目标

把 Hitchin 一般纤维识别为 $\mathrm{Prym}(D/C)$ 的 torsor，并核对维数。

## 前提

- $\psi:D\to C$ 是 $N$ 重谱覆盖，$D$ 光滑（判别式非零、零点单重）。
- 非分歧点 $p\in C$ 上 $\varphi(p)$ 有 $N$ 个不同本征值，本征空间分解 $E_p=\bigoplus_i\mathcal L_{q_i}$。
- $\Lambda(\mathcal L)=\det\psi_*(\mathcal L)\cong\mathrm{Nm}(\mathcal L)\otimes K^{-N(N-1)/2}$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 在非分歧点处 $E_p=\bigoplus_i\mathcal L_{q_i}$；说明 $(E,\varphi)$ 在非分歧点上由线丛 $\mathcal L$ 的纤维完全决定。 | $\varphi$ 在本征基下是对角的。 | `A p.13 eq (2.24)` | A·原文明确写了 |
| 2 | 整体构造：给定 $D$ 上线丛 $\mathcal L$，令 $E=\psi_*\mathcal L$、$\varphi=\psi_*(y)$；这是 $C$ 上秩 $N$ 的希格斯丛。 | 推前与 $y$ 乘法是可逆的构造。 | `A p.14 eq (2.25)` | A·原文明确写了 |
| 3 | 固定 $\Lambda(\mathcal L)\cong\mathcal O$（$SU(N)$ 情形），由 $\Lambda\cong\mathrm{Nm}\otimes K^{-N(N-1)/2}$ 得 $\mathrm{Nm}(\mathcal L)$ 固定。 | $\Lambda$ 与 $\mathrm{Nm}$ 只差一个固定 twist。 | `A p.15 eq (2.34)` | A·原文明确写了 |
| 4 | $\mathrm{Nm}(\mathcal L)$ 固定意味着 $\mathcal L$ 落在 $\mathrm{Prym}(D/C)$ 的 torsor 中；$\mathrm{Prym}(D/C)=\ker(\mathrm{Nm}:\mathrm{Jac}(D)\to\mathrm{Jac}(C))$。 | Prym 的定义。 | `A p.26 eq (3.5)` | A·原文明确写了 |
| 5 | 维数：$\dim\mathrm{Prym}=g_D-g_C=(N^2-1)(g-1)=\dim\mathcal V$，与 $\S2.4$ 一致。 | 维数吻合是必要条件。 | `A p.8 eq (2.6)` | B·原文暗示、我们补的中间步 |

## 结论

$SU(N)$ 的 Hitchin 一般纤维同构于 $\mathrm{Prym}(D/C)$ 的 torsor；$N$ 为偶数时 torsor 结构依赖 $K^{1/2}$ 的选取。

## 缺口

- 第 5 步的维数核对用了 $\S2.4$ 的 $\dim\mathcal V$ 公式，而非直接来自 Prym 的构造。
- 偶 $N$ 时纤维只是 torsor，不是典范阿贝尔簇；原文 $\S2.6.3$ 用 $K^{1/2}$ 处理，未给范畴层面的严格证明。

## 最容易讲错的地方

- Prym 不是 $\mathrm{Jac}(D)$：维数差 $g_C$，不要漏掉 norm 条件。
- torsor 与群本身不同：要选基点才能把纤维当群；基点选择依赖 $K^{1/2}$。
- 非分歧点的直和分解不能套到分歧点：那里 $\varphi-y$ 的核仍是一维但余核不是直和。

## 相关卡

[阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · [谱曲线](../concepts/spectral-curve.md) · [核线丛与余核线丛](../concepts/kernel-cokernel.md) · [希钦纤维化](../concepts/hitchin-fibration.md) · [核与余核线丛的关系 $\mathcal L\cong\mathcal N(\mathcal R)$](../derivations/kernel-cokernel-relation.md)

## 出处（印刷页）

- A p.13–14（A p.13 eq (2.24)）
- A p.15（A p.15 eq (2.34)）
- A p.26（A p.26 eq (3.5)）

> 说明：A4：eq (2.24)(2.25)(2.34)(3.5) 均在原文；B1：维数核对与 torsor 的表述是整理时补的。最没把握处：偶 $N$ 的 torsor 结构原文分散在 $\S2.6.3$ 与 $\S3.2$。
