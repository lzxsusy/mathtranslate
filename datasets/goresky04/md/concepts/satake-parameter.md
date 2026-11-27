# Satake 参数：非分歧局部表示的指纹

> `goresky04/concept/satake-parameter` · 轨道 C · 对应与障碍 · 状态 dev

> **先自测**：为什么一个非分歧局部表示可以被「$n$ 个数」完全决定？

## 一句话

非分歧局部表示 $\pi_p$ 由球 Hecke 代数 $H_p$ 的一个特征（即 $n$ 个数的无序组 $\alpha_1,\dots,\alpha_n$）唯一确定；这组数就是 Satake 参数，也等于 $T_p$ 的特征值。

## 定义

固定素数 $p$，$G_p=\GL(n,\bbQ_p)$，$K_p=\GL(n,\bbZ_p)$。球 Hecke 代数 $H_p$ 是 $K_p$-双不变紧支函数的卷积代数，以双陪集 $K_pgK_p$ 为基。Satake 同构说 $H_p\cong\bbC[X_*(T)]^{W}$，其中 $T$ 是极大环面、$W$ 是 Weyl 群。于是 $H_p$ 的特征由 $T$ 上的一个点（模 $W$）给出，即一个无序的 $n$ 元组 $(\alpha_1,\dots,\alpha_n)\in(\bbC^\times)^n/W$。这个 $n$ 元组就是 $\pi_p$ 的 Satake 参数。

**记号**：$T\subset\GL(n)$ 对角环面；$X_*(T)=\bbZ^n$；$W=S_n$；$\alpha_i$ 记 Satake 参数；$H_p$ 的生成元是 $T_{p,i}$（$i=0,\dots,n$）。

## 要点（为什么需要它）

1. Satake 参数是「非分歧」的等价物：一个局部表示非分歧，当且仅当它有 $K_p$-固定向量，当且仅当它是 $H_p$ 的特征。
2. 参数是无序组（模 $W$）而不是有序组：这正是为什么它只能与「Frobenius 的共轭类」比较，不能与单个矩阵比较。
3. 参数与 $L$ 因子直接相关：$L_p(\pi,s)=\prod_{i}(1-\alpha_ip^{-s})^{-1}$，所以「Satake 参数相等」就是「局部因子相等」。
4. 对 $\GL(2)$，参数是两个数 $\alpha,\beta$；模形式情形下它们由 $\lambda_p$ 与 $p^{k-1}$ 决定，即 $\alpha+\beta=\lambda_p$，$\alpha\beta=p^{k-1}$。

## 核心公式

$$
$H_p=K_p\backslash G_p/K_p$ 为基的卷积代数，$H_p\cong\bbC[X_*(T)]^{W}$$L_p(\pi,s)=\prod_{i=1}^{n}(1-\alpha_ip^{-s})^{-1}$
$$

$$
$L_p(\pi,s)=\prod_{i=1}^{n}(1-\alpha_ip^{-s})^{-1}$
$$

## 定理与证明（或缺口）

### Satake 同构

$H_p\cong\bbC[X_*(T)]^{W}$ 是环同构；因此 $H_p$ 的特征与 $(\bbC^\times)^n/W$ 一一对应。

> 证明状态：**gap**。原文只在注 25 里引用这个同构，没有证明；它属于 $p$ 进群的表示论（Macdonald 公式、球函数）。

出处：`A p.18`

## 常见误解

- 参数是 $(\alpha_1,\dots,\alpha_n)$ 模置换，不是有序组；写 $\{\alpha_i\}$ 时要用花括号或「无序组」。
- Satake 参数依赖归一化：把 $\pi_p$ 乘上一个未分歧特征，参数会整体乘一个数；比较两侧时必须固定同一个归一化（通常要求中心特征与 $|\cdot|^?$ 匹配）。
- 非分歧是必要前提：分歧表示的局部因子更复杂，没有这种「$n$ 个数」的干净描述。

## 相关卡

[自守形式与自守表示](../concepts/automorphic-representation.md) · [Hecke 特征形式与 Fourier 系数](../concepts/hecke-eigenform.md) · [把 Hecke 特征值对上 Frobenius 特征值](../derivations/hecke-to-frobenius.md)

## 出处（印刷页）

- A p.13（A p.13）
- A p.18（A p.18）

> 说明：对应原文 §6.4 与注 25；同构的证明属 Macdonald 公式，原文未给。
