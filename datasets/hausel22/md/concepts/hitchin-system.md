# Hitchin 系统

> `hausel22/concept/hitchin-system` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：为什么 Hitchin 映射的纤维是阿贝尔簇，而不是更一般的环面？

## 一句话

Hitchin 系统是 Higgs 丛模空间上由特征多项式给出的完全可积系统，一般纤维是阿贝尔簇的主齐性空间。

## 定义

1987 年 Hitchin 考察四维 Yang–Mills 方程在二维上的约化，得到黎曼曲面上自对偶方程解的模空间 $\M$，其上带超 Kähler 度量与复结构 $I,J,K$。在 $I$ 下 $\M$ 是 Higgs 丛（或 Hitchin 对）$(E,\Phi)$ 的模空间 $\M_\Dol$；Hitchin 映射 $h:\M\to\calA$ 取 Higgs 场的特征多项式，当 $\G=\GL_n$ 时 $h(E,\Phi)=\det(x-\Phi)\in\calA:=\bigoplus_{i=1}^n H^0(C;K^i)$；一般 $\G$ 用 $\mathfrak g=\Lie(\G)$ 上的不变多项式在 $\Phi$ 上取值。

**记号**：$\M,\M_\Dol,\M_\DR$；$h$；$\calA$；$(E,\Phi)$；$\omega_I,\omega_J,\omega_K$。

## 要点（为什么需要它）

1. Hitchin 映射是代数完全可积的 Hamilton 系统：$\dim\calA=\dim\M/2$，$h$ 的各分量两两 Poisson 交换。
2. proper 性由 Hitchin（$\SL_2$）、Nitsure、Simpson（$\GL_n$）、Faltings（一般 $\G$）证明；完全可积 + proper ⇒ 一般纤维是阿贝尔簇的主齐性空间。
3. 超 Kähler 结构给出三个复结构：$I$ 下是 $\M_\Dol$，$J$ 与 $K$ 下都同构于平坦联络模空间 $\M_\DR$，见式 (1.1)。
4. Hitchin 系统是几何 Langlands 与镜像对称的交汇点：它同时给出 SYZ 对偶所需的特殊拉格朗日纤维化与 TMS 所需的 Hodge 数比较。

## 核心公式

$$
$$h(E,\Phi)=\det(x-\Phi)\in\calA:=\bigoplus_{i=1}^{n}H^0(C;K^i)$$$$(\M,I)\cong\M_\Dol,\qquad (\M,J)\cong(\M,K)\cong\M_\DR$$
$$

$$
$$(\M,I)\cong\M_\Dol,\qquad (\M,J)\cong(\M,K)\cong\M_\DR$$
$$

## 定理与证明（或缺口）

### Hitchin 系统的完全可积性与 proper 性

关于 $I$-全纯形式 $\omega_\C:=\omega_J+i\omega_K$，$h$ 构成代数完全可积的 Hamilton 系统；$h$ 是 proper 映射；两者合起来推出 $h$ 的一般纤维是阿贝尔簇上的主齐性空间，特别地在拓扑上同构于紧环面。

> 证明状态：**sketch**。原文只罗列归属（谁证了哪一段），没有给出 proper 性或纤维结构的证明。

出处：`A p.2229 eq (1.1)`

## 常见误解

- $h$ 的像空间 $\calA$ 的维数是 $\dim\M/2$，不是 $\dim\M$；把 $h$ 当满射到 $\M$ 是错的。
- $\M_\Dol$ 与 $\M_\DR$ 是同一个流形 $\M$ 的不同复结构，不是两个不同的模空间。
- 对 $\GL_n$ 用 $\det(x-\Phi)$，对 $\SL_n$ 则 $\det$ 恒为 $1$，此时要取 $\End_0$ 与不变多项式，不能照抄 $\GL_n$ 的公式。
- 「一般纤维是阿贝尔簇的主齐性空间」不等于「是阿贝尔簇」：主齐性空间可能没有原点，只有在选好基点后才成为阿贝尔簇。

## 相关卡

[SYZ 镜像对称](../concepts/syz-mirror-symmetry.md) · [拓扑镜像对称](../concepts/topological-mirror-symmetry.md) · [Langlands 对偶群 $\G^\vee$](../concepts/langlands-dual-group.md) · [从 Hitchin 系统读出 SYZ 对偶纤维化](../derivations/syz-from-hitchin.md)

## 出处（印刷页）

- A p.2229（A p.2229 eq (1.1)）
- A p.2232（A p.2232 eq (2.2)）

> 说明：A=原文 §1 的定义、式 (1.1)、可积性与 proper 性的归属；B=把「proper + 可积 ⇒ 纤维是主齐性空间」拆成三步；C=「主齐性空间不必有原点」的提醒是我们补的。最没把握处：$\calA$ 对一般 $\G$ 的确切定义（不变多项式的次数分布），原文只在 $\GL_n$ 情形写出。
