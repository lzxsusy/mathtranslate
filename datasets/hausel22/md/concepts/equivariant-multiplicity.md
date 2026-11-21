# 等变重数 $m_\calE(t)$

> `hausel22/concept/equivariant-multiplicity` · 轨道 D · 幂零锥上的等变重数 · 状态 dev

> **先自测**：为什么 $m_\calE(t)$ 在非常稳定时会变成多项式？

## 一句话

等变重数是用 $\T$-等变 Euler 型写出的比值，对非常稳定 $\calE$ 是系数非负、回文、首一的多项式。

## 定义

对 $\calE\in\M^{s\T}$ 定义等变重数 $m_\calE(t):=\chi_\T(\Sym(T^{+*}_\calE))/\chi_\T(\Sym(\calA^*))\in\Z(t)$，其中 $\chi_\T$ 是等变 Euler 型 $\chi_\T(X;\calF_1,\calF_2)=\sum_{k,l}\dim(H^k(R\mathcal{H}om(\calF_1,\calF_2))^l)(-1)^kt^{-l}$。对非常稳定的 $\calE$，$m_\calE(t)$ 是多项式，系数非负、回文、首一，且 $m_\calE(1)=m_{F_\calE}$（即 $\calE$ 所在幂零锥分量的重数）。

**记号**：$m_\calE(t)$；$T^{+*}_\calE$；$\calA^*$；$\chi_\T$；$F_\calE$。

## 要点（为什么需要它）

1. $m_\calE(t)$ 是「分母为 $\chi_\T(\Sym\calA^*)$」的有理函数：几何上它度量 $W^+_\calE$ 相对于 $\calA$ 的等变体积比。
2. 非常稳定时它变成多项式，这是定理 3.5 的全部内容，也是「非常稳定」这个条件真正的用处。
3. $m_\calE(1)=m_{F_\calE}$ 把新定义与旧的「幂零锥分量重数」接上：新对象在 $t=1$ 处退化成经典重数。
4. 它与 §3.2 定义 3.11 的重数 $m_\calE=[\C(W^+_\calE):\C(\calA)]$ 不同：前者是多项式，后者是整数（一般纤维的基数）。

## 核心公式

$$
$$m_\calE(t):=\frac{\chi_\T(\Sym(T^{+*}_\calE))}{\chi_\T(\Sym(\calA^*))}\in\Z(t)$$$$\chi_\T(X;\calF_1,\calF_2)=\sum_{k,l}\dim\big(H^k(R\mathcal{H}om(\calF_1,\calF_2))^l\big)(-1)^kt^{-l}\in\C((t))$$
$$

$$
$$\chi_\T(X;\calF_1,\calF_2)=\sum_{k,l}\dim\big(H^k(R\mathcal{H}om(\calF_1,\calF_2))^l\big)(-1)^kt^{-l}\in\C((t))$$
$$

## 定理与证明（或缺口）

### 重数多项式的性质（定理 3.5）

若 $\calE$ 非常稳定，则 $m_\calE(t)\in\Z[t]$ 是多项式，系数非负、回文（$t^{\deg}m_\calE(1/t)=m_\calE(t)$）、首一，且 $m_\calE(1)=m_{F_\calE}$。

> 证明状态：**sketch**。原文引用 [HH, Cor 5.4]，未给证明；回文性的几何来源只说「由 Poincaré 对偶」。

出处：`A p.2238 eq (3.4)`

## 常见误解

- 别把 $m_\calE(t)$（多项式）与 §3.2 的重数 $m_\calE$（整数）混用；两者同名但不是一回事，原文用 $t$ 的出现在前者。
- 有理函数 $\chi_\T(\Sym T^+)/\chi_\T(\Sym\calA^*)$ 只有对非常稳定 $\calE$ 才是多项式；对一般 $\calE$ 只是有理函数。
- 回文性写成 $m(t)=m(1/t)$ 是错的，正确的形式是 $t^{\deg m}m(1/t)=m(t)$。
- $m_\calE(1)=m_{F_\calE}$ 里右边是幂零锥分量的重数，不是 Hitchin 纤维的重数；这两个「重数」在原文里是不同的量。

## 相关卡

[非常稳定 Higgs 丛](../concepts/very-stable-higgs-bundle.md) · [局部重数代数 $Q_\calE$](../concepts/local-multiplicity-algebra.md) · [非常稳定 $\Rightarrow$ 重数是多项式](../derivations/multiplicity-polynomial.md)

## 出处（印刷页）

- A p.2238（A p.2238 eq (3.4)）
- A p.2238（A p.2238 eq (3.5)）

> 说明：A=原文 §3.1.2 的定义式 (3.4) 与定理 3.5；B=把「非常稳定 ⇒ 分母被约掉」的理由补出来；C=「等变体积比」的解释是我们补的直觉。最没把握处：回文性在原文只归因于 Poincaré 对偶，具体机制（$\T$-权与 Calabi–Yau 形式的配对）未展开。
