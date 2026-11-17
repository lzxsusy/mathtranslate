# Langlands 对偶群

> `kw/concept/langlands-dual-group` · 轨道 A · 四维物理与对偶 · 状态 dev

> **先自测**：Langlands 对偶群是什么，它在整条论证链里起什么作用？

## 一句话

把 $G$ 的根数据取对偶（权格与余权格互换）得到的群 ${}^LG$：$\mathrm{SU}(N)\leftrightarrow\mathrm{PSU}(N)$、$E_8$ 自对偶；它同时是 GNO 对偶群，几何 Langlands 的右侧就出现它。

## 定义

Langlands 对偶群 ${}^LG$ 是根数据 $(X^*,X_*,\dots)$ 取对偶所得的群；对紧致李群，它就是交换 $G$ 的权格与余权格得到的群，也等于电磁对偶中的 GNO 对偶群。

**记号**：${}^LG$；根与余根；权格 $X^*=\Lambda_{\rm w}$ 与余权格 $X_*=\Lambda_{\rm cw}$。

## 要点（为什么需要它）

1. 几何 Langlands 的陈述两侧是 $G$-丛与 ${}^LG$-局部系统，没有 ${}^LG$ 就无法写出这个对应。
2. 它把 S-对偶中『群被替换』说清楚：换群不是任意的，而是根数据对偶。
3. Table 1 的对应（如 $\mathrm{Spin}(2n)\leftrightarrow\mathrm{SO}(2n)/\mathbb Z_2$）是检验物理对偶的离散数据。
4. 它统一自对偶（$E_8$、$G_2$）与非自对偶情形，并解释非 simply-laced 的 $n_g$ 修正来自根与余根长度不同。

## 核心公式

$$
$$\Lambda_{\rm rt}({}^LG)=\Lambda^\vee_{\rm rt}(G),\qquad \Lambda_{\rm w}({}^LG)=\Lambda^\vee_{\rm w}(G)$$$$\mathrm{SU}(N)\leftrightarrow\mathrm{PSU}(N),\qquad \mathrm{Sp}(n)\leftrightarrow\mathrm{SO}(2n+1)$$
$$

$$
$$\mathrm{SU}(N)\leftrightarrow\mathrm{PSU}(N),\qquad \mathrm{Sp}(n)\leftrightarrow\mathrm{SO}(2n+1)$$
$$

## 定理与证明（或缺口）

### Table 1 对偶对应

GNO/Langlands 对偶给出：$\mathrm{U}(N)\leftrightarrow\mathrm{U}(N)$、$\mathrm{SU}(N)\leftrightarrow\mathrm{PSU}(N)$、$\mathrm{Spin}(2n)\leftrightarrow\mathrm{SO}(2n)/\mathbb Z_2$、$\mathrm{Sp}(n)\leftrightarrow\mathrm{SO}(2n+1)$、$\mathrm{Spin}(2n+1)\leftrightarrow\mathrm{Sp}(n)/\mathbb Z_2$、$G_2$ 与 $E_8$ 自对偶。

> 证明状态：**gap**。原文 p.3 的 Table 1 只列例子，未给推导；一般构造由根数据对偶给出（我们的整理）。

出处：`B p.3`

### 非 simply-laced 的 $n_g$ 修正

$S$ 变换在非 simply-laced 群上为 $\tau\mapsto-1/(n_g\tau)$，$n_g=2$ 对 $F_4$、$n_g=3$ 对 $G_2$；这反映根与余根长度之比。

> 证明状态：**sketch**。原文 p.11 只给出结果与矩阵 (2.17)，未证明；p.13 说也可由 BPS 质量公式看出。

出处：`B p.11 eq (2.17)`

## 常见误解

- 把 Langlands 对偶群等同于 $G$ 的复化 $G_\mathbb C$：对紧致 $G$，${}^LG$ 的极大紧子群一般不是 $G$。
- 以为对偶只换群不换格：根数据对偶同时交换权格与余权格，这正是磁荷所在。
- 忽略中心：$\mathrm{SU}(N)$ 与 $\mathrm{PSU}(N)$ 李代数相同但对偶群不同。

## 相关卡

[GNO 对偶群](../concepts/gno-dual-group.md) · [S-对偶](../concepts/s-duality.md) · [几何 Langlands 对应](../concepts/geometric-langlands.md) · [非单连通群的 n_g 修正与 Table 1](../derivations/table1-and-ng.md)

## 出处（印刷页）

- B p.3（B p.3）
- B p.11（B p.11 eq (2.17)）
- B p.13（B p.13）

> 说明：A=原文：Table 1、GNO 对偶=Langlands 对偶 (B p.3)、$n_g$ 修正 (B p.11)；C=整理：根数据对偶的公式表述、summary、key_points、pitfalls（原文只给例子，未给根数据构造）。
