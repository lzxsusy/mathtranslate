# 非幺 $A_\infty$-代数之间的态射

`kshms/concept/dfn-04-nonunital-a-inf-morphism` · track B（$A_\infty$ 形式框架） · 原文 定义 4

**问题**　两个非幺 $A_\infty$-代数之间的态射为什么定义为张量余代数之间与余微分交换的零次态射，而不是通常的链映射？

**摘要**　两个非幺 $A_\infty$-代数之间的态射是张量余代数 $T_+(V[1])\to T_+(W[1])$ 之间与余微分交换的零次态射，展开为一列 Taylor 系数 $f_n$ 的方程组。

**别名**　morphism of non-unital $A_\infty$-algebras；$A_\infty$-morphism；$A_\infty$-态射

## 陈述

非幺 $A_\infty$-代数 $(V,d_V)$ 与 $(W,d_W)$ 之间的态射（$A_\infty$-态射）是指张量余代数之间的一个零次态射 $T_+(V[1])\to T_+(W[1])$，它与各自的余微分交换。

## 记号

$(V,d_V)$、$(W,d_W)$：非幺 $A_\infty$-代数；$f_n\colon V^{\otimes n}\to W[1-n]$（$n\ge1$）：态射的 Taylor 系数；$\epsilon_s$、$\gamma_i$：方程的 Koszul 符号；$l_0=0$。

## 要点

- 态射是余代数态射 $T_+(V[1])\to T_+(W[1])$，零次且满足 $f\circ d_V=d_W\circ f$；它不是 $V\to W$ 的线性映射。
- 由 Taylor 系数 $f_n\colon V^{\otimes n}\to W[1-n]$（$n\ge1$）唯一确定；把 $f\circ d_V=d_W\circ f$ 展开就是这些 $f_n$ 的方程组。
- 若 $f_n=0$（$n\ge2$），交换条件退化为 $f_1m_1^V=m_1^Wf_1$，即 $f_1$ 是链映射；一般情形 $f_1$ 只是线性部分。
- 符号 $\gamma_i$ 记录按 $l_1<\cdots<l_i$ 拼接各块 $f_{l_p}$ 时的 Koszul 符号，$\epsilon_s$ 则来自 $m_r^V$ 被移过 $a_1,\dots,a_{j-1}$。

## 公式

$$f\colon T_+(V[1])\to T_+(W[1]),\qquad f\circ d_V=d_W\circ f$$

$$f_n\colon V^{\otimes n}\to W[1-n],\quad n\ge1$$

$$\sum_{1\le l_1<\cdots<l_i=n}(-1)^{\gamma_i}m_i^W\bigl(f_{l_1}(a_1,\dots,a_{l_1}),\dots,f_{n-l_{i-1}}(a_{n-l_{i-1}+1},\dots,a_n)\bigr)=\sum_{s+r=n+1}\sum_{1\le j\le s}(-1)^{\epsilon_s}f_s\bigl(a_1,\dots,a_{j-1},m_r^V(a_j,\dots,a_{j+r-1}),a_{j+r},\dots,a_n\bigr)$$

## 易错点

- 只验证 $f_1m_1=m_1f_1$ 不够：完整条件是 $f\circ d_V=d_W\circ f$，涉及所有 $f_n$。
- 零次指保持 $A$ 的分次；单个 $f_n$ 的次数是 $1-n$，不要与「零次态射」混淆。
- 本条是代数之间的态射；范畴之间的函子（定义 6、定义 8）另有对象映射，不能照搬本条。

## 相关卡

- `kshms/concept/dfn-03-nonunital-a-inf-algebra`
- `kshms/concept/dfn-05-nonunital-a-inf-category`
- `kshms/concept/dfn-06-nonunital-a-inf-functor`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §4.2（原文 p.23）；锚点 `源码/chunks/ch04.tex:66-69（定义 4）`

> 原文 p23 §4.2；译本 ch04.tex:66-69；Taylor 系数方程见 ch04.tex:71-88（原文 p23）。
