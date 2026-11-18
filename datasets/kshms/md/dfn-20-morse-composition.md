# Morse 范畴的高阶复合 $m_k$

`kshms/concept/dfn-20-morse-composition` · track D（Morse 机器） · 原文 定义 20

**问题**　横截对象序列上的高阶复合 $m_k$ 如何由梯度树模空间的计数写出？

**摘要**　对横截的对象序列，$m_k$ 按带 $k+1$ 条尾的定向二元平面树求和：每棵树取梯度树模空间的带符号点数，作用在临界点基上得到输出临界点。

**别名**　higher compositions in the Morse category；$m_k$ 的树公式；Morse $A_\infty$-结构

## 陈述

对 $k\ge2$，用下述公式定义复合 $m_k$：
$$m_k([y_0],\dots,[y_{k-1}])=\sum_{[T]}\ \sum_{y_k\in\operatorname{Cr}(f_0-f_k)} \operatorname{deg}\bigl(\mathcal{M}(T;f_0,\dots,f_k;y_0,\dots,y_k)\bigr)\cdot[y_k],$$
其中 $[T]$ 是 $T$ 作为抽象定向平面树的等价类，而 $\operatorname{deg}(\cdot)\in\mathbb{Z}$ 一如既往表示带符号计数的总点数。

## 记号

$\operatorname{Cr}(f)$ 为临界点集；$y_i\in\operatorname{Cr}(f_i-f_{i+1})$（$0\le i\le k-1$），$y_k\in\operatorname{Cr}(f_0-f_k)$，满足 $\sum_{0\le i\le k-1}\operatorname{ind}(y_i)=\operatorname{ind}(y_k)+2-k$；$\mathcal{M}(T;\dots)$ 为梯度树模空间。

## 要点

- $m_k$ 按树展开：外层遍历抽象定向平面树的等价类 $[T]$，内层遍历 $f_0-f_k$ 的临界点 $y_k$。
- 系数 $\operatorname{deg}(\mathcal{M}(\dots))$ 是定向紧零维流形的带符号点数，这正是 $T$-横截条件的用处。
- 指标匹配 $\sum_{i=0}^{k-1}\operatorname{ind}(y_i)=\operatorname{ind}(y_k)+2-k$ 保证模空间维数为零，维数不符时按约定为空。
- 公式在局部系平凡且秩一时写出；高秩情形改用平坦联络的和乐类比，与 Fukaya 范畴的处理相同。

## 公式

$$m_k([y_0],\dots,[y_{k-1}])=\sum_{[T]}\sum_{y_k\in\operatorname{Cr}(f_0-f_k)}\operatorname{deg}\bigl(\mathcal{M}(T;f_0,\dots,f_k;y_0,\dots,y_k)\bigr)\cdot[y_k]$$

$$\sum_{0\le i\le k-1}\operatorname{ind}(y_i)=\operatorname{ind}(y_k)+2-k$$

## 易错点

- 求和遍历树的同构类 $[T]$，不是遍历画法；同一抽象树的不同平面嵌入按原文的符号约定另行计符号。
- 符号只写 $\pm$：原文与译文都未把 $m_{k,T}$ 的符号写定，复算时须按 §4 的 Koszul 符号约定逐顶点确定。
- 公式左侧只接收 $k$ 个临界点 $[y_0],\dots,[y_{k-1}]$，$y_k$ 是输出，不要误当输入。

## 相关卡

- `kshms/concept/dfn-18-t-transversal`
- `kshms/concept/dfn-19-transversal-objects`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §6.2（原文 p.39）；锚点 `源码/chunks/ch06.tex:195-203（定义 20）`

> 原文 p39 §6.2；译注「$m_{k,T}$ 的符号」指出原文只写 $\pm$，符号由树的平面定向与 §4 的 Koszul 约定共同决定。
