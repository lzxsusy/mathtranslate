# 't Hooft 算子

> `kw/concept/thooft-operator` · 轨道 D · 二维、膜与算子 · 状态 dev

> **先自测**：'t Hooft 算子与 Wilson 算子本质差别在哪，为什么它按 Langlands 对偶群的表示分类？

## 一句话

规范理论的 disorder 算子：指定经典场奇点再积分；$U(1)$ 时按磁荷 $m$ 分类，一般群按 $^L G$ 的不可约表示 $^L R$ 分类，记 $T(^L R,S)$。

## 定义

't Hooft 算子是规范理论的 disorder 算子：规定场在余维 2 的曲面 $S$ 附近的奇点，再对其它场做路径积分。其类型由 $\rho:\mathrm U(1)\to G$ 的共轭类给出，等价于 $^L G$ 的一个不可约表示 $^L R$（GNO 对偶），记 $T(^L R,S)$。

**记号**：$S$：奇点所在曲面；$^L R$：$^L G$ 的不可约表示；$m$：$U(1)$ 情形的磁荷。

## 要点（为什么需要它）

1. 它是 Wilson 算子的对偶对象：S-对偶交换 order 与 disorder，表示 $R$ 换成 $^L R$。
2. 它按 $^L G$ 的表示分类（GNO 对偶），这是 §9 把它与 Hecke 算子对上的根据。
3. 在 $\mathbb R\times C$ 上插入它即令丛在一点被修改，修改的权就是 $^L R$ 的权。
4. 拓扑非平凡情形由 $\xi\in H^2(S^2,\pi_1(G))$ 刻画，非平凡当且仅当 $^L G$ 的中心在 $^L R$ 上作用非平凡。

## 核心公式

$$
$\oint_{S^2}c_1(L)=m$（$U(1)$ 的磁荷）$\rho:\mathrm U(1)\to G\ \longleftrightarrow\ {}^LG\ \text{的不可约表示}\ {}^LR$
$$

$$
$\rho:\mathrm U(1)\to G\ \longleftrightarrow\ {}^LG\ \text{的不可约表示}\ {}^LR$
$$

## 定理与证明（或缺口）

### GNO 分类

't Hooft 算子的类型与 $\mathrm{Hom}(\mathrm U(1),G)$ 的共轭类一一对应，而后者等价于 $^L G$ 的最高权，即 $^L G$ 的不可约表示。

> 证明状态：**sketch**。原文 p.84 引用 GNO 对偶 [10] 与 [90]，未给证明；本文只使用结论。

出处：`B p.84`

## 常见误解

- 把 't Hooft 算子当成某联络的 holonomy；它是 disorder 算子，先指定奇点再做路径积分。
- 用 $G$ 的表示 $R$ 而不是 $^L G$ 的表示 $^L R$ 标号它。
- 忽略法丛定向：奇点类型需要 $S$ 的法丛定向才能定义。

## 相关卡

[Wilson 算子](../concepts/wilson-operator.md) · [GNO 对偶群](../concepts/gno-dual-group.md) · [Hecke 算子](../concepts/hecke-operator.md) · ['t Hooft 算子的 Hecke 修改：U(1) 到 U(N)](../derivations/toofty-hecke.md)

## 出处（印刷页）

- B p.81–84（B p.84）
- B p.130（B p.130 eq (9.10)）

> 说明：A=原文 p.81–84 的 disorder 定义与 GNO 分类；B=与 $^L G$ 中心/拓扑类的对应；C=把分类写成定理的措辞。
