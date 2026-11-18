# Maslov 指标等于 $f_1-f_2$ 的 Morse 指标

`kshms/remark/rmk-13-maslov-equals-morse` · track C（Fukaya 与退化） · 原文 注 13

**问题**　Fukaya 范畴里由 Maslov 指标给出的分级，为什么在环面纤维化情形可以用 Morse 指标来计算？

**摘要**　当 $L_i$ 在交点局部是 $df_i$ 的图时，$x\in L_1\cap L_2$ 处的 Maslov 指标等于 $f_1-f_2$ 在 $p^\vee(x)$ 的 Morse 指标；Floer 分级因此化为 Morse 分级。

**别名**　Remark 13；Maslov index equals Morse index；Floer 分级与 Morse 分级的对照

## 陈述

可以验证：对如上所述的两个横截拉格朗日子流形 $L_1$ 与 $L_2$，任意 $x\in L_1\cap L_2$ 处的 Maslov 指标等于光滑 Morse 函数 $f_1-f_2:Y\to\mathbb{R}$ 在 $p^\vee(x)$ 处的 Morse 指标，这里 $f_i$ 使得在 $x$ 的局部有 $L_i=\operatorname{graph}(df_i)\ \bigl(\mathrm{mod}\,(T^{\mathbb{Z}}_Y)^\vee\bigr)$，$i=1,2$。

## 这条注在全文中的作用

这条注是 §5 把 Fukaya–Oh 范畴与 Morse $A_\infty$-范畴对齐的分级依据：它保证两侧的 $\mathbb{Z}$-分级来自同一个整数。后文命题 5 的等价因此在分级层面可信，而不只是形式上的拟同构。

## 易错点

- 只对横截的 $L_1,L_2$，且在 $x$ 局部可写成 $\operatorname{graph}(df_i)$（模 $(T^{\mathbb{Z}}_Y)^\vee$）时成立；一般 Lagrange 子流形没有这个等式。
- $p^\vee(x)$ 是 $x$ 在 $Y$ 上的投影，Morse 指标取在 $Y$ 的临界点 $p^\vee(x)$ 处，不是取在 $x$ 处。
- 等式说的是指标相等，不是链复形同构；符号与定向仍需另行核对。

## 相关卡

- `kshms/concept/dfn-16-fukaya-objects`
- `kshms/concept/dfn-17-fukaya-morphism-spaces`
- `kshms/remark/rmk-14-dimension-assumption`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §5.2（原文 p.33）；锚点 `源码/chunks/ch05.tex:137-139（注 13）`

> 原文 p33 §5.2；中译注本 ch05.tex:137-139。
