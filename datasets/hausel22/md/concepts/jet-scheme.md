# jet 概形 $J_d(X)$

> `hausel22/concept/jet-scheme` · 轨道 E · 仿射 Grassmannian 与重数代数 · 状态 dev

> **先自测**：为什么重数代数会等于一个 jet 概形的坐标环？

## 一句话

$J_d(X)$ 是 $X$ 上 $d-1$ 阶 jet 的模概形，其 $\C$-点是从 $\Spec\C[z]/(z^d)$ 到 $X$ 的映射；它是猜想 3.12(4) 里的核心对象。

## 定义

对概形 $X$ 与整数 $d\ge1$，定义 $J_d(X)(\C)=\Hom(\Spec(\C[z]/(z^d)),X)$，称为 $X$ 的 $d-1$ 阶 jet 概形。$J_1(X)=X$；$J_d$ 是 $X$ 上的（当 $X$ 光滑时为丛，秩 $=\dim X\cdot(d-1)$）。猜想 3.12(4) 说：当 $\mu=(d+1)\omega_k$ 时 $Q_\mu\cong\C[J_d(Q_{\omega_k})]\cong\C[J_d(\Spec H^*(\Gr(k,n),\C))]$。

**记号**：$J_d(X)$；$\C[z]/(z^d)$；$d-1$ 阶；$Q_{\omega_k}=H^*(\Gr(k,n);\C)$。

## 要点（为什么需要它）

1. $J_d$ 记录的是「$d$ 个无穷接近的点」的信息：$d=1$ 是点本身，$d=2$ 是切向量，$d=3$ 开始含二阶信息。
2. 阶数是 $d-1$ 而不是 $d$：$\C[z]/(z^d)$ 的长度为 $d$，对应的 jet 阶数为 $d-1$。
3. $J_d$ 与「对称幂」不同：$\Sym^d$ 允许 $d$ 个点分开，$J_d$ 强制它们重合（带 $z$-结构）。
4. 猜想 3.12(4) 把重数代数与 jet 概形联系起来，这正是「重数 = 无穷接近的点数」这一直觉的代数化。

## 核心公式

$$
$$J_d(X)(\C)=\Hom\big(\Spec(\C[z]/(z^d)),X\big)$$$$Q_\mu\cong\C\big[J_d(\Spec H^*(\Gr(k,n),\C))\big],\qquad \mu=(d+1)\omega_k$$
$$

$$
$$Q_\mu\cong\C\big[J_d(\Spec H^*(\Gr(k,n),\C))\big],\qquad \mu=(d+1)\omega_k$$
$$

## 定理与证明（或缺口）

### $n=2$ 的三个显式重数代数（注 3.14）

当 $n=2$ 时：$Q_{\delta_c^{2\omega_1}}\cong\C[a_0]/(a_0^2)$；$Q_{\delta_c^{2\omega_1}}\cong\C[a_0,a_1]/(a_0^2,a_0a_1)$；$Q_{\delta_c^{3\omega_1}}\cong\C[a_0,a_1,a_2]/(a_0^2,a_0a_1,a_0a_2+a_1^2)$。

> 证明状态：**sketch**。原文给出三式的最后形式与 $(a_0^2,a_0a_1)=(a_0,a_1)^2\cap(a_0)$ 的解释，但未写 jet 概形的逐步计算；且 (3.9)(3.10)(3.11) 的角标原文有笔误（见译注）。

出处：`A p.2243 eq (3.9)`

## 常见误解

- 阶数错位：$J_d$ 是 $d-1$ 阶 jet 概形，不是 $d$ 阶；$J_1(X)=X$ 是最简单的检查。
- 把 $J_d(X)$ 与对称幂 $\Sym^d X$ 混淆：前者强制点重合，后者允许分开。
- 原文式 (3.9)(3.10)(3.11) 的角标写作 $2\omega_1,2\omega_1,3\omega_1$，与 $\mu=(d+1)\omega_1$ 不符（应为 $2,3,4\omega_1$），照录时不可「顺手改对」，须加译注说明。
- 猜想 3.12(4) 只说 $\mu=(d+1)\omega_k$ 的情形，不能推广到任意 $\mu$。

## 相关卡

[仿射 Grassmannian $\Gr$](../concepts/affine-grassmannian.md) · [局部重数代数 $Q_\calE$](../concepts/local-multiplicity-algebra.md) · [$n=2$ 时的三个重数代数与 jet 概形](../derivations/jet-scheme-n2.md)

## 出处（印刷页）

- A p.2243（A p.2243 eq (3.9)）
- A p.2243（A p.2243 eq (3.11)）

> 说明：A=原文 §3.3 的 jet 概形定义（定理 3.12(4) 下的句子）与注 3.14 的三式；B=把「阶数为什么是 $d-1$」讲清楚；C=与对称幂的对比是我们补的。最没把握处：$J_d(\Spec H^*(\Gr(k,n)))$ 的显式结构，原文说「竟然可以如此复杂」，未给一般公式（见注 3.15）。
