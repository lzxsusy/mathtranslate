---
id: csw/example/kz-two-point
type: example
track: E
---

# KZ 两点函数与共形权

> 两点共形块 $\Psi=(z_1-z_2)^{-2h_j}$，指数是共形权 $h_j$；$SU(2)$、$k=1$ 时 $h_{1/2}=1/4$。

**问题**：解两点 KZ 方程，验证指数正好是 $-2h_j$。

## 设定

取 $n=2$、插入 $R_j,R_j$，并设 $\Omega_{12}=\sum_aT^a_{(1)}T^a_{(2)}$（$T^a$ 取 $\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab}$，定义表示 $C_2=\frac34$）。KZ：$\kappa\partial_{z_1}\Psi=\frac{\Omega_{12}}{z_1-z_2}\Psi$，$\kappa=k+h^\vee$。

## 计算

1. 两点块只依赖 $z=z_1-z_2$，设 $\Psi=z^{\alpha}$，代入得 $\kappa\alpha z^{\alpha-1}=\Omega_{12}z^{\alpha-1}$，即 $\kappa\alpha=\Omega_{12}$。 *（比较 $z$ 的幂次即可。）*
2. 单态分量上 $\Omega_{12}=\frac12[C_2^{(12)}-C_2^{(1)}-C_2^{(2)}]=-C_2(j)$（$C_2^{(12)}=0$）。 *（$SU(2)$：$C_2(j)=j(j+1)$。）*
3. 故 $\alpha=-C_2(j)/\kappa$；取 $h_j=C_2(j)/(2\kappa)$ 时 $\alpha=-2h_j$，取 $h_j=C_2(j)/\kappa$ 时 $\alpha=-h_j$——两种 $h$ 的定义在文献中都常见，差一个因子 2。 *（本卡用 $h_j=C_2(j)/(2\kappa)$，故 $\alpha=-2h_j$；主文用 $h_j=j(j+1)/(k+2)=C_2(j)/\kappa$，故 $\alpha=-h_j$。）*

## 结果

$\Psi=z^{-C_2(j)/\kappa}$，$\kappa=k+h^\vee$。$SU(2)$、$k=1$、$j=\frac12$：$C_2=\frac34$、$\kappa=3$，指数 $-\frac14$；按主文 $h_{1/2}=\frac14$，即 $\Psi=z^{-h_{1/2}}$。

## 核对

$k=1$：$h_{1/2}=\frac{(1/2)(3/2)}{1+2}=\frac14$，指数 $-\frac14$ 与 $|z|^{-2h}$ 的 $2h=\frac12$ 差因子 2——差别正是 $\Omega$ 归一化，写公式前必须先声明。

## 陷阱

- $\Omega_{12}$ 的归一化决定指数是 $-h$ 还是 $-2h$：本卡声明 $\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab}$。
- $\kappa=k+h^\vee$ 不能写成 $k$；$SU(2)$ 用 $k+2$。
- 符号：$\Omega_{12}$ 在单态上为负，$\alpha$ 才为负，物理上要 $|z|^{-2h}$ 的衰减。

## 相关卡片

- [knizhnik-zamolodchikov](../concepts/knizhnik-zamolodchikov.md)
- [bwb-su2](../examples/bwb-su2.md)
- [level-shift-check](../examples/level-shift-check.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.2 与 §2（共形权，p.360、p.370），印刷页 [360, 370] / PDF 页 [10, 20]（witten1989/sections/s02-weak-coupling.tex（(2.25) 附近））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
