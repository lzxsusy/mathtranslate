# B-模型（B 扭化 sigma 模型）

> `kw/concept/b-model` · 轨道 D · 二维、膜与算子 · 状态 dev

> **先自测**：B-模型的超对称方程为什么把映射逼成常数，它为什么只依赖复结构？

## 一句话

取 $J_+=J_-=\hat J$ 的扭化；方程合成 $(1-\mathrm i\hat J)\dd\Phi=0$ 故映射为常数，模型只依赖复结构 $\hat J$，在 $\Psi=\infty$ 处出现。

## 定义

扭化取 $J_+=J_-=\hat J$ 的二维 sigma 模型称 B-模型：两族超对称方程合成 $(1-\mathrm i\hat J)\dd\Phi=0$，在欧氏符号的 $\Sigma$ 上蕴含 $\dd\Phi=0$，即 $\Phi$ 为常数。本文在 $\Psi=\infty$（$t=\pm\mathrm i$）取它，靶空间为 $M_H(G,C)$。

**记号**：$\hat J$：扭化用的复结构；$\dd\Phi$：$\Sigma$ 上取值于拉回切丛的一形式。

## 要点（为什么需要它）

1. 它与 $\Psi=0$ 处的 A-模型构成 S-对偶两端，是镜像对称（§5.3）的一半。
2. 它依赖复结构，因此可以问它在 $I,J,K$ 中是哪一种；c.c. 膜在 $J$ 中是 B-膜就用到这一点。
3. 它的边界条件 B-膜要求支撑子流形与 Chan–Paton 丛都全纯。
4. B-模型只保留复结构信息，镜像对称于是把复结构问题翻译成 A-模型的辛几何问题。

## 核心公式

$$
$J_+=J_-=\hat J,\qquad (1-\mathrm i\hat J)\dd\Phi=0\ \Longrightarrow\ \dd\Phi=0$$\Psi=\infty:\quad \text{B-模型，靶空间 }M_H(G,C)\text{，复结构 }J$
$$

$$
$\Psi=\infty:\quad \text{B-模型，靶空间 }M_H(G,C)\text{，复结构 }J$
$$

## 定理与证明（或缺口）

### B-模型方程蕴含映射为常数

取 $J_+=J_-=\hat J$，方程 (5.5)(5.6) 合并为 $(1-\mathrm i\hat J)\dd\Phi=0$，其复共轭为 $(1+\mathrm i\hat J)\dd\Phi=0$，故 $\dd\Phi=0$。

1. 把 $J_+=J_-=\hat J$ 代入两族超对称方程 (5.5)(5.6)。
   - *为什么*：B-模型的定义就是两个复结构相等，全纯与反全纯条件必须同时成立。
2. 两式合并成 $(1-\mathrm i\hat J)\dd\Phi=0$。
   - *为什么*：$\partial\Phi$ 与 $\bar\partial\Phi$ 拼成 $\dd\Phi$，两个条件分别落在 $(1,0)$ 与 $(0,1)$ 部分。
3. 取复共轭得 $(1+\mathrm i\hat J)\dd\Phi=0$，两式相减得 $2\mathrm i\hat J\dd\Phi=0$，$\hat J$ 可逆故 $\dd\Phi=0$。
   - *为什么*：$\hat J$ 在实切丛上可逆，故 $\hat J\dd\Phi=0$ 只有零解。

出处：`B p.59 eq (5.5)`

## 常见误解

- 把“映射为常数”误当成模型无内容；常数映射只说明经典解平凡，拓扑场论的信息在扭化与算子中。
- 忘记 $\hat J$ 必须是可积复结构；非可积的 $J_\pm$ 会落进广义复几何。
- 把 B-模型与 B-膜混淆：前者是体理论，后者是它的边界条件。

## 相关卡

[A-模型（A 扭化 sigma 模型）](../concepts/a-model.md) · [镜像对称（本文版本）](../concepts/mirror-symmetry.md) · [B-膜](../concepts/b-brane.md) · [S-对偶 = 镜像对称（全文心脏）](../derivations/sdual-mirror.md)

## 出处（印刷页）

- B p.59（B p.59 eq (5.5)）
- B p.70（B p.70）

> 说明：A=原文 p.59 的方程与“映射为常数”结论；B=复共轭相减这一步的重建；C=$\Psi=\infty$ 归属 B-模型的读法。
