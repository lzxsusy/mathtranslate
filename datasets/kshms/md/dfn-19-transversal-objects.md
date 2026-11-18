# 横截的对象序列（Morse 范畴）

`kshms/concept/dfn-19-transversal-objects` · track D（Morse 机器） · 原文 定义 19

**问题**　在 Morse 范畴里，什么样的对象序列才允许定义全部高阶复合？

**摘要**　若对象序列的任意子序列对任意带 $m+1$ 条尾的二元树都 $T$-横截，则称该对象序列横截；这是 Morse 范畴中高阶复合得以定义的前提。

**别名**　transversal sequence of objects；横截对象序列；Morse $A_\infty$-预范畴的横截性

## 陈述

若对任意 $m\ge1$、任意带 $m+1$ 条尾的二元树 $T$，任意子序列 $(f_{i_0},\dots,f_{i_m})$（$i_0<\dots<i_m$）都是 $T$-横截的，则称对象序列 $(f_0,\rho_0),\dots,(f_k,\rho_k)$ 是横截的。

## 记号

$\mathcal{M}(Y)$ 的对象是二元组 $(f,\rho)$：$f:Y\to\mathbb{R}$ 光滑，$\rho$ 是 $Y$ 上有限维复向量空间的局部系；$T$ 是定向二元平面树。

## 要点

- 横截性是对整个对象序列下的定义，要求任意子序列、任意树同时 $T$-横截，条件比单个 $T$-横截强得多。
- 横截对象序列的态射空间取 Morse 复形 $M^*(Y,f_0-f_1,\rho_0^*\otimes\rho_1)$，系数由两个局部系的对偶张量给出。
- 通有的函数族自动满足全部横截性：原文指出 $(C^\infty(Y))^{\mathbb{Z}}$ 中存在第二纲集，使任一递增子序列对任一平面树都 $T$-横截。
- 有了横截序列，$m_k$（$k\ge2$）才在 Morse 范畴中被定义；非横截情形再借哈密顿形变延拓。

## 公式

$$(f_0,\rho_0),\dots,(f_k,\rho_k)\ \text{横截}\iff \forall\,(f_{i_0},\dots,f_{i_m})\ \text{对任意二元树 }T\ \text{为 }T\text{-横截}$$

$$\mathrm{Hom}_{\mathcal{M}(Y)}(W_0,W_1)=M^*(Y,f_0-f_1,\rho_0^*\otimes\rho_1)$$

## 易错点

- 「任意子序列」包括长度更短的子序列，验证时不能只看整串 $(f_0,\dots,f_k)$。
- 树的尾数 $m+1$ 与子序列长度匹配，且 $m\ge1$；$m=0$ 不在定义范围内。
- 横截性只约束函数 $f_i$，$\rho_i$ 作为对象数据附带；不要以为局部系也参与 $T$-横截条件。

## 相关卡

- `kshms/concept/dfn-18-t-transversal`
- `kshms/concept/dfn-20-morse-composition`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §6.2（原文 p.39）；锚点 `源码/chunks/ch06.tex:151-155（定义 19）`

> 原文 p39 §6.2；定义 19 之后紧接 Morse 复形态射空间与 $m_k$ 的构造，$m_k$ 只在横截序列上定义。
