# 经典模形式

> `goresky04/concept/modular-form-classical` · 轨道 B · 自守侧 · 状态 dev

> **先自测**：模形式与猜想右侧有什么关系，为什么偏偏是 $\SL(2,\bbZ)$ 的权 $k$ 形式？

## 一句话

$\SL(2,\bbZ)$ 的权 $k$ 模形式是上半平面上的全纯函数，在 $\SL(2,\bbZ)$ 作用下按 $k$ 次自守因子变换；尖点形式是其中在尖点处取零的那些。

## 定义

设 $f\colon\he\to\bbC$ 全纯，$\gamma=\binom{a\ b}{c\ d}\in\SL(2,\bbZ)$。称 $f$ 为权 $k$ 模形式，若 $f\bigl(\frac{az+b}{cz+d}\bigr)=(cz+d)^k f(z)$ 对一切 $\gamma$ 成立，且在尖点处具有适当的增长条件（$f$ 的 Fourier 展开只有非负指数项）。若进一步在尖点处取零（只有正指数项），称 $f$ 为尖点形式；尖点形式构成空间 $S_k$。

**记号**：$\he=\{z:\Im z>0\}$ 上半平面；$q=e^{2\pi iz}$；$f=\sum_{n\ge0}a_nq^n$ 为 Fourier 展开。

## 要点（为什么需要它）

1. 自守因子 $(cz+d)^k$ 的作用是让 $f(z)(dz)^{k/2}$ 在 $\SL(2,\bbZ)$ 下不变；这是几何上「权」的来源，不是随手加的。
2. 「在尖点处取零」这个条件正是「尖点」一词的来源，也是右端要求 cuspidal 的古典原型。
3. 模形式空间 $M_k$ 有限维；$\dim S_k$ 由 Riemann–Roch 给出，这使「Hecke 特征值」成为一族离散的数据。
4. $q$ 展开把一个函数变成一串系数 $(a_1,a_2,\dots)$，Hecke 算子作用在这串系数上——这就是右侧「数据」的具体形态。

## 核心公式

$$
$f\bigl(\tfrac{az+b}{cz+d}\bigr)=(cz+d)^k f(z)$，$\binom{a\ b}{c\ d}\in\SL(2,\bbZ)$$f(z)=\sum_{n\ge 0}a_nq^n$，$q=e^{2\pi iz}$；$f\in S_k\iff a_0=0$
$$

$$
$f(z)=\sum_{n\ge 0}a_nq^n$，$q=e^{2\pi iz}$；$f\in S_k\iff a_0=0$
$$

## 定理与证明（或缺口）

### 有限维性（古典）

$M_k(\SL(2,\bbZ))$ 有限维，$S_k$ 是其子空间；当 $k<0$ 或 $k$ 为奇数时 $M_k=0$。

> 证明状态：**sketch**。原文没有证明，只说「众所周知」；完整证明见 [Sh1] 或 [K]。

出处：`A p.8`

## 常见误解

- 权 $k$ 与自守因子指数必须统一：有的书写 $f(\gamma z)=(cz+d)^kf(z)$，有的书把 $k$ 换成 $2k$，对照文献时要先确认约定。
- 模形式与自守形式不是同义词：前者是 $\SL(2,\bbZ)$ 的古典对象，后者是平代环上的对象；两者通过 (6.1.1) 等同，但不是定义上相同。

## 相关卡

[Hecke 对应与 Hecke 算子](../concepts/hecke-operator.md) · [从模形式到平代环上的自守形式（(6.1.1)）](../derivations/adelic-equivalence.md) · [Eichler–Shimura：$n=2$ 情形猜想的证明](../concepts/eichler-shimura-theorem.md)

## 出处（印刷页）

- A p.7–9（A p.8）

> 说明：对应原文 §5.1–§5.2；有限维性一条原文只作背景提了一句，本卡按 [Sh1][K] 的通行说法补齐。
