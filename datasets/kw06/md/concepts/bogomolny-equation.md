# Bogomolny 方程

> `kw/concept/bogomolny-equation` · 轨道 E · Langlands 与翻译器 · 状态 dev

> **先自测**：Bogomolny 方程是什么，它的解空间为什么与 Hecke 修改空间一致？

## 一句话

三维单极子方程 $F=\star\dd_A\phi$；在 $\mathbb R\times C$ 上给定左右边界条件后，其解空间模规范等于 Hecke 修改空间。

## 定义

Bogomolny 方程是 $F=\star\,\dd_A\phi_0$，即 $\mathbb R^4$ 上平移不变瞬子方程在三维的约化，也就是标准的 BPS 单极子方程。在 $W=\mathbb R\times C$ 上，$C_-$ 固定丛 $E_-$、$C_+$ 令 $\phi_0=0$ 并取协变 Neumann 条件，解模规范后给出 $E_-\to E_+$ 的 Hecke 修改。

**记号**：$A$：规范场；$\phi_0$：伴随标量（$\phi=\phi_0\dd s$）；$\star$：三维 Hodge 星。

## 要点（为什么需要它）

1. 它是 't Hooft 算子的半经典图像：奇点由 Bogomolny 方程的奇异解实现。
2. 解空间在复结构意义上等于 Hecke 修改空间，把 §9 的丛修改与 §10 的解空间连起来。
3. 边界条件决定输入输出：左端固定 $E_-$，右端自由到同构类 $E_+$。
4. 指标 $\dim=\Delta_{^Lw}$ 与 Hecke 修改维数一致，是两边匹配的定量证据。

## 核心公式

$$
$F=\star\,\dd_A\phi_0$$\iota_nF=0,\qquad \phi_0=0\quad (C_+)$
$$

$$
$\iota_nF=0,\qquad \phi_0=0\quad (C_+)$
$$

## 定理与证明（或缺口）

### Bogomolny 解空间等于 Hecke 修改空间

以 $E_-$、$E_+$ 为左右边界条件的 Bogomolny 方程解（模规范）与 $E_-\to E_+$ 的 Hecke 修改一一对应，两者有相同复结构，且解的指标等于 $\Delta_{^Lw}$。

> 证明状态：**sketch**。原文 p.162 只说这“给出一个精确框架”，且只在复结构意义上成立；辛结构沿 $y$ 改变，完整对应还依赖 Pauly–Kronheimer 的指标计算。

出处：`B p.162`

## 常见误解

- 把 Bogomolny 方程当成 Hitchin 方程；维数与边界条件不同，只共享复结构。
- 忽略边界条件：同一方程配不同边界给出完全不同的模空间。
- 把“解空间 = 修改空间”当成辛同构；原文只在复结构层面陈述。

## 相关卡

[Hecke 算子](../concepts/hecke-operator.md) · ['t Hooft 算子](../concepts/thooft-operator.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [一族拓扑场论：t ∈ CP¹ 与 Q² = 0](../derivations/one-parameter-family.md)

## 出处（印刷页）

- B p.127–128（B p.127 eq (9.5)）
- B p.148–150（B p.148–150）
- B p.162（B p.162）

> 说明：A=原文 p.127 的方程、p.148–150 的边界条件、p.162 的复结构等同；B=把解空间与修改空间一一对应；C=指标公式归给 Pauly–Kronheimer（原文只引）。
