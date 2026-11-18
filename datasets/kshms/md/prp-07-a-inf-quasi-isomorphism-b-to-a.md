# 嵌入 $i:B\to A$ 可延拓为 $A_\infty$-拟同构

`kshms/concept/prp-07-a-inf-quasi-isomorphism-b-to-a` · track D（Morse 机器） · 原文 命题 7

**问题**　子复形 $B$ 与原来的 $A_\infty$-代数 $A$ 只差一个同伦，能否把嵌入升级为 $A_\infty$-拟同构？

**摘要**　存在典范的 $A_\infty$-态射 $g:B\to A$：$g_1$ 取嵌入 $i$，高阶 $g_n$ 由带同伦 $H$ 的平面树给出，它给出 $A_\infty$-代数的拟同构，故 $A$ 与 $B$ 在 $A_\infty$ 意义下等价。

**别名**　A-infinity quasi-isomorphism B to A；$A_\infty$-拟同构 $g:B\to A$；同调扰动的逆方向

## 陈述

存在典范的 $A_\infty$-态射 $g:B\to A$，它给出 $A_\infty$-代数的拟同构。

## 记号

$g=(g_n)_{n\ge1}$：$A_\infty$-态射 $B\to A$；$g_1=i$ 为嵌入；对 $n\ge2$，$g_n=\sum_T g_{n,T}$，$T$ 取遍具有 $n+1$ 个尾的平面树，根部配同伦 $H$；$B=\Pi(A)$ 是 $m_1^B$-复形（命题 6）。

## 要点

- 只取 $g_1=i$ 不够：$i$ 一般不是 $A_\infty$-态射，必须补上高阶 $g_n$ 才能满足 $A_\infty$-态射方程。
- $g_n$ 的树公式与 $m_n^B$ 的树公式同型，唯一差别是根顶点配 $H$ 而不是投影 $p$，这样像才落回 $A$。
- 「拟同构」指 $g_1$ 在 $m_1$-上同调上诱导同构，即 $H^*(B)\cong H^*(A)$；它使 $B$ 成为 $A$ 的等价模型。
- 原文还指出可以显式构造反向的 $A_\infty$-拟同构 $A\to B$，故两个方向都可用。

## 公式

$$g_1=i,\qquad g_n=\sum_{T}g_{n,T}\quad(n\ge2)$$

$$H^*(B)\cong H^*(A)$$

## 证明（sketch）

1. 取 $g_1=i$，并用平面树定义 $n\ge2$ 的 $g_n$：尾配 $i$、内顶点配 $m_k$、新顶点配 $H$、根配 $H$。

   *为什么*：这与 $m_n^B$ 的树公式逐项对应，只把根处的 $p$ 换成 $H$，使 $g_n$ 的像落在 $A$ 而不是 $B$。

2. 把 $g$ 代入 $A_\infty$-态射方程，按树展开逐项比较；不闭合的项由 $1-\Pi=dH+Hd$ 吸收。

   *为什么*：这正是定理 3 证明中同一套计算：$A_\infty$ 关系给出的修正项被 $H$ 与 $d$ 抵消，剩下零。

3. 由 $g_1=i$、$p\circ i=\operatorname{id}_B$ 且 $i\circ p=\Pi$ 与 $\operatorname{id}_A$ 同伦，得 $H^*(B)\cong H^*(A)$，故 $g$ 是拟同构。

   *为什么*：$i$ 与 $p$ 在 $m_1$-上同调上互逆（同伦的映射诱导相同的同调映射），故 $g_1$ 诱导同构。

> 缺口：原文未给证明，只写「用类似的技术可以证明下述结果」（p43）：$g$ 的显式取法（$g_1=i$，$g_n$ 为平面树之和、根配 $H$）给出后，$A_\infty$-态射方程的逐树验证未写出；做法与定理 3 的证明同型，依据同调扰动理论（[GS]、[Me]，译注见 ch07.tex:138）。

## 易错点

- $g$ 不是链映射：$g_1=i$ 单独看并非 $A_\infty$-态射，是高阶项 $g_n$ 补上了态射方程。
- 「拟同构」属 $A_\infty$-代数，意思是 $g_1$ 诱导同调同构；不要与 $B$ 上已构造的 $A_\infty$-结构混为一谈。
- 树公式的符号由定向平面树的 Koszul 规则决定，原文只写「带适当的符号」，漏符号会破坏态射方程。

## 相关卡

- `kshms/concept/prp-06-m1b-differential`
- `kshms/concept/dfn-09-quasi-isomorphism`
- `kshms/concept/dfn-03-nonunital-a-inf-algebra`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §6.4（原文 p.43）；锚点 `源码/chunks/ch07.tex:128-136（命题 7）`

> 原文 p43 §6.4；$g$ 的显式取法见 ch07.tex:132-134，反向拟同构 $A\to B$ 的存在性见 136 行，译注「同调扰动理论」见 138-143。
