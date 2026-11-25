# M(2,0) 的穿墙项

> `grassmann/example/wall-crossing-term-m20` · 轨道 4 · 奇异模空间的相交配对 · 状态 draft

> **这张卡练什么**：为什么 2g 维的积分最后只剩一个单变量幂级数的系数，t=y/Y 这个比值起了什么作用？

## 一句话

沿 Δ=(S¹)^{2g} 爆破，法丛三个直和项给出权 2、−2、−4 与 Euler 类，两次留数塌缩成一个幂级数系数，得 W 的闭式。

## 背景定义

**穿墙项** $W$ 是式 (1) 中的差值项：取 $\tilde\mu$ 的小正则值 $\epsilon$，把
$$B=\int_{\tilde\mu^{-1}(0)/T}\kappa(\alpha\beta\mathcal{D})-\int_{\tilde\mu^{-1}(\epsilon)/T}\kappa(\alpha\beta\mathcal{D})$$
用定理 6.1 写成夹在 $0$ 与 $\epsilon$ 之间（即 $0<\mu_T(F)<\epsilon$）的 $T$-不动点分支上的留数之和，就是穿过墙时配对的变化量；在 $M(2,0)$ 的第一次爆破处，这串留数塌缩成一个幂级数系数。

## 设定

取亏格 $g\ge2$，$M(2,0)$（本节不固定行列式），$K=SU(2)$，$T$ 为极大环面，$Y$ 是 $H_T^2(\mathrm{pt})$ 的生成元。第一次爆破沿 $\Delta=(S^1)^{2g}\cong\mathrm{Jac}$（稳定子群为整个 $SU(2)$ 的点集）。例外除子中具有正矩映射的 $T$-不动点分支为
$$\mathbb{P}\big(T_{\mathrm{Jac}}\otimes\mathbb{R}\begin{pmatrix}0&1\\0&0\end{pmatrix}\big)\cong\mathbb{P}T_{\mathrm{Jac}}\cong\mathbb{P}^{g-1}\times\mathrm{Jac},$$
其法丛为 $\mathcal{O}_{\mathbb{P}^{g-1}}(-1)\oplus[T_{\mathrm{Jac}}\otimes\mathbb{R}\binom{1\ \ 0}{0\ -1}\otimes\mathcal{O}(1)]\oplus[T_{\mathrm{Jac}}\otimes\mathbb{R}\binom{0\ 0}{1\ 0}\otimes\mathcal{O}(1)]$，$T$ 在三个直和项上的权分别为 $2,-2,-4$；$y=c_1(\mathcal{O}_{\mathbb{P}^{g-1}}(1))$。

## 计算

第一步（Euler 类）：$e_T(L)=c_1(L)+\mathrm{wt}\cdot Y$ 逐项算，$T_{\mathrm{Jac}}$ 上 $T$-作用平凡故只经矩阵的权进入，得
$$e_F=(-y+2Y)(y-2Y)^g(y-4Y)^g .$$
第二步（留数）：穿墙项
$$W=-\frac12\int_{\mathbb{P}^{g-1}\times\mathrm{Jac}}\mathrm{Res}_{Y=0}\frac{\eta e^{\bar\omega}|_\Delta\,\mathcal{D}^2}{(-y+2Y)(y-2Y)^g(y-4Y)^g}.$$
只有当 $\eta e^{\bar\omega}|_\Delta=c\,Y^{3g-3}\gamma^g/g!$（$\gamma=\sum_{j=1}^{g}d^jd^{j+g}$，$\int_\Delta\gamma^g/g!=1$）时非零；代入后
$$W=-\frac{1}{2^{3g}}\int_\Delta\mathrm{Res}_{y=0}\mathrm{Res}_{Y=0}\frac{Y^{g-2}}{y^g}\Big(1-\frac{y}{2Y}\Big)^{-g-1}\Big(1-\frac{y}{4Y}\Big)^{-g}.$$
第三步（塌缩成系数）：$\mathrm{Res}_{y=0}$ 要求 $m-g=-1$ 即 $m=g-1$，剩下 $Y^{-1}$ 由 $\mathrm{Res}_{Y=0}$ 取走，两次留数等价于取 $t^{g-1}$ 的系数（$t=y/Y$）：
$$W=-\frac{1}{2^{3g}}\mathrm{Coeff}_{t^{g-1}}\Big[\Big(1-\frac{t}{2}\Big)^{-g-1}\Big(1-\frac{t}{4}\Big)^{-g}\Big].$$
验算：$g=2$ 时 $(1-\frac t2)^{-3}=1+\frac32t+\cdots$、$(1-\frac t4)^{-2}=1+\frac12t+\cdots$，系数 $[t^1]=\frac32+\frac12=2$，故 $W=-2/2^{6}=-\frac{1}{32}$；$g=3$ 时 $[t^2]=\frac52+\frac32+\frac38=\frac{35}{8}$，故 $W=-\frac{35}{8\cdot 2^{9}}=-\frac{35}{4096}$。结果只依赖 $g$，说明整条流水线对所有亏格给出一致的闭式。

## 要点

- 三个权 $2,-2,-4$ 与三个底数 $-y+2Y$、$y-2Y$、$y-4Y$ 是同一条信息的两种写法，数错一个权就数错一次幂。
- 第一个直和项是例外除子的法向（秩 1），后两个在例外除子内部是法向的；把「法向」读成「垂直」（中译 p.74）会以为后两块互相垂直。
- 只有 $Y^{3g-3}\gamma^g/g!$ 这一项有贡献：$\mathrm{Res}_{y=0}$ 定出 $t$ 的幂次，$\mathrm{Res}_{Y=0}$ 定出 $Y$ 的幂次，两者合起来就是一个系数。
- $W$ 是式 (1) 中的穿墙项 $B$，与 $A$（正则值处的非奇异配对）相加才是 $\widetilde{\mathcal{M}}(2,0)$ 上的配对。

## 关键公式

$$
e_F=(-y+2Y)(y-2Y)^g(y-4Y)^g
$$

$$
W=-\frac{1}{2^{3g}}\mathrm{Coeff}_{t^{g-1}}\Big[\Big(1-\frac{t}{2}\Big)^{-g-1}\Big(1-\frac{t}{4}\Big)^{-g}\Big]
$$

$$
W(g=2)=-\frac{1}{32},\qquad W(g=3)=-\frac{35}{4096}
$$

## 相关定理

- **$M(2,0)$ 第一次爆破的穿墙项（式 (4)）**：沿 $\Delta=(S^1)^{2g}$ 爆破后，穿墙项为
$$W=-\frac{1}{2^{3g}}\mathrm{Coeff}_{t^{g-1}}\Big[\Big(1-\frac{t}{2}\Big)^{-g-1}\Big(1-\frac{t}{4}\Big)^{-g}\Big],\qquad t=y/Y,$$
它由法丛的等变 Euler 类 $(-y+2Y)(y-2Y)^g(y-4Y)^g$ 经两次留数塌缩得到。

## 易错点

- 把第三个直和项的 $\times\mathcal{O}(1)$ 当真：原文印作 $\times$（中译保留原印，只加脚注），几何上是张量积 $\otimes\mathcal{O}(1)$，用 $\times$ 算不出权 $-4$。
- 把 $g$ 次幂算成一次：$T_{\mathrm{Jac}}$ 秩为 $g$，两个块各带 $g$ 次幂，漏掉指数会把 $W$ 的量级算成 $2^{-g}$ 而不是 $2^{-3g}$。
- 把 $t$ 当成独立变量去对 $y$ 与 $Y$ 分别展开：$t=y/Y$ 是比值，只有它的系数是无量纲数，分开展开会多出 $Y$ 的负幂。

## 用到哪些概念

- [部分消奇异](../concepts/partial-desingularization.md)
- [配对的留数公式](../concepts/residue-formula-for-pairings.md)
- [Kirwan 映射与正根类](../concepts/kirwan-map-and-class-d.md)
- [扩张模空间](../concepts/extended-moduli-space.md)

## 相关卡

- [配对的留数公式](../concepts/residue-formula-for-pairings.md)
- [部分消奇异](../concepts/partial-desingularization.md)
- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)

## 出处

- ch4 §3 式 (3)–(4)；中译 p.76（英文 PDF p.82），源码 `chapters/ch04.tex:119`
