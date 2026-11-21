# SYZ 镜像对称

> `hausel22/concept/syz-mirror-symmetry` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：为什么 Hitchin 系统给出的纤维化正好满足 SYZ 的要求？

## 一句话

SYZ 猜想镜像的两个 Calabi–Yau 流形纤维化在同一底上、一般纤维是互为对偶的特殊拉格朗日环面。

## 定义

Strominger–Yau–Zaslow 1996 年提出：Calabi–Yau $3$ 维流形 $X$ 与它的镜像 $Y$ 应当纤维化在同一个底 $B\cong S^3$ 上（式 (2.1)），并且一般纤维是互为对偶的特殊拉格朗日 $3$-环面。$L\subset X$ 特殊拉格朗日指：$L$ 拉格朗日（$\omega_X|_L=0$）且 $\Im(\Omega_X)|_L=0$；反过来 $Y$ 是 $Fuk(X,\omega_X)$ 中这类对象的模空间。

**记号**：$X,Y$；$B\cong S^3$；$\omega_X$；$\Omega_X$；特殊拉格朗日 $L$。

## 要点（为什么需要它）

1. 特殊拉格朗日 = 拉格朗日 + Calabi–Yau 体积形式的虚部消失；两个条件缺一不可。
2. Hitchin 系统天然给出这样的纤维化：$\M_\Dol\to\calA$ 的纤维关于 $\omega_\C=\omega_J+i\omega_K$ 全纯拉格朗日，$\M_\DR\to\calA$ 的纤维在 $J$ 结构下特殊拉格朗日。
3. 底不一样：SYZ 的底是 $S^3$（复三维），Hitchin 的底是 $\calA$（高维仿射空间），所以原文说两者「在几何情境上并不相同」。
4. SYZ 的数学实现（Gross–Siebert 纲领）在原文写 §2.1 时「已取得许多成果，新近更有突破」，但完整的对偶纤维化构造至今仍缺失。

## 核心公式

$$
$$\omega_X|_L=0,\qquad \Im(\Omega_X)|_L=0$$$$\omega_\C=\omega_J+i\omega_K,\qquad \omega_\C|_{\text{fiber}}=0$$
$$

$$
$$\omega_\C=\omega_J+i\omega_K,\qquad \omega_\C|_{\text{fiber}}=0$$
$$

## 定理与证明（或缺口）

### Hitchin 纤维化的特殊拉格朗日性

在复结构 $J$ 下，$\M_\DR\to\calA$ 与 $\M^\vee_\DR\to\calA$ 的一般纤维是特殊拉格朗日纤维化：$\omega_J$ 沿纤维消失，$\omega_K$ 与 $J$-全纯 Calabi–Yau 形式 $(\omega_K+i\omega_I)^{2d}$ 的虚部也沿纤维消失。

> 证明状态：**sketch**。原文只陈述结论与「这意味着」的解释，没有给出 $(\omega_K+i\omega_I)^{2d}$ 的逐点计算。

出处：`A p.2232 eq (2.3)`

## 常见误解

- 特殊拉格朗日不只是「拉格朗日」：还要求 $\Im(\Omega_X)$ 在 $L$ 上为零，漏掉这条就失去了 Calabi–Yau 的校准结构。
- SYZ 的底是 $S^3$，Hitchin 的底是 $\calA$；把 $\calA$ 说成 $S^3$ 是错的（维数都不对）。
- $\M_\Dol$ 的纤维是全纯拉格朗日（关于 $\omega_\C$），$\M_\DR$ 的纤维才是特殊拉格朗日（关于 $J$ 结构）；两个说法对应不同的复结构。
- $Y$ 不是「$X$ 的某个子流形」，而是 $Fuk(X,\omega_X)$ 中特殊拉格朗日环面加 $U(1)$-局部系统的模空间。

## 相关卡

[镜像对称（三个方面）](../concepts/mirror-symmetry.md) · [Hitchin 系统](../concepts/hitchin-system.md) · [从 Hitchin 系统读出 SYZ 对偶纤维化](../derivations/syz-from-hitchin.md)

## 出处（印刷页）

- A p.2230（A p.2230 eq (2.1)）
- A p.2232（A p.2232 eq (2.3)）

> 说明：A=原文 §2.1 的 SYZ 表述与 §2.3 的特殊拉格朗日性；B=把「完全可积 ⇒ 复拉格朗日 ⇒ 特殊拉格朗日」拆成三步；C=「底维数不同」的比较是我们按 §2.1 末句补的。最没把握处：$(\omega_K+i\omega_I)^{2d}$ 的虚部消失，原文未给计算。
