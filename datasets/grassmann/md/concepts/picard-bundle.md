# Picard 丛

> `grassmann/concept/picard-bundle` · 轨道 8 · 阿贝尔簇上的正则性 · 状态 draft

> **先自测**：为什么 Picard 丛本身是『负』的，却仍能用张量 $\Theta$ 之后的消没定理控制 $W_d$ 的方程？

## 一句话

曲线上次数足够大的线丛被视作 Jacobian 上的层，其 Fourier–Mukai 变换叫 Picard 丛；它的射影化是对称积，而张量幂的 $IT_0$ 性质给出 $W_d$ 理想层的消没。

## 定义

设 $C$ 是亏格 $g\ge2$ 的光滑曲线，$J(C)=\operatorname{Pic}^0(C)$。取次数 $n\ge2g-1$ 的线丛 $L\in\operatorname{Pic}^n(C)$，经 Abel–Jacobi 把它看作 $J(C)$ 上的层；它满足 $IT_0$。称其 Fourier–Mukai 变换 $$\mathcal E=\mathcal E_L:=\mathbf R\widehat{\mathcal S}(L)$$ 为**第 $n$ 个 Picard 丛**（它是 $\operatorname{Pic}^n(C)$ 上的向量丛）。对任意 $M\in\operatorname{Pic}^n(C)$，对应的 $\mathcal E_M$ 都是 $\mathcal E_L$ 的平移，且 $\mathbb P(\mathcal E_L)\cong C_n=\operatorname{Sym}^nC$。

**记号约定**：$C_n=\operatorname{Sym}^nC$；$\Theta$ 是 $J(C)$ 的主极化（theta 除子）；$W_d\subset J(C)$ 是 $d$ 次特殊除子的轨迹；$\pi_k\colon C^k\to J(C)$ 是去对称化的 Abel–Jacobi 映射；$r_J$ 是乘 $r$ 映射。

## 要点（为什么需要它）

- 命题 7.15：$n\gg0$ 时对每个 $1\le k\le g-1$，$\otimes^k\mathcal E\otimes\mathcal O(\Theta)$ 满足 $IT_0$——先把负丛扭正，才能谈消没。
- 引理 7.16 把 $\otimes^k\mathcal E$ 的消没归到 $C^k$ 上的 Serre 消没：$\otimes^k\mathcal E$ 满足 $WIT_g$，其变换是 $(-1_J)^*\pi_{k*}(L\boxtimes\cdots\boxtimes L)$，再用 Leray 与投影公式。
- 定理 7.18：对每个 $1\le d\le g-1$，$\mathcal I_{W_d}(2\Theta)$ 满足 $IT_0$；证明走 $W_d$ 的行列式结构与 Eagon–Northcott 复形，归到 $h^i(S^kE\otimes\mathcal O(\Theta))=0$。
- 注 7.19：更强地，$\mathcal I_{W_d}(k\Theta)$ 对所有 $k\ge2$ 满足 $IT_0$；命题 7.22 进一步给出 $\mathcal I_{W^1_{g-1}}(2\Theta)$ 是 $M$-正则的。
- 整条链是 §7.3 半齐次丛方法的先声：都是『先在同源拉回下拆成线丛直和，再用 $IT_0$ 与消没』。

## 关键公式

$$
\mathcal E:=\widehat L=\mathbf R\widehat{\mathcal S}(L)\in\operatorname{Pic}(J(C)),\qquad \mathbb P(\mathcal E)\cong C_n
$$

$$
\otimes^k\mathcal E\ \text{满足 }WIT_g,\qquad \widehat{\otimes^k\mathcal E}=(-1_J)^*\pi_{k*}(L\boxtimes\cdots\boxtimes L)
$$

$$
0\to\wedge^mF^*\otimes S^{m-n}E\otimes\det E\to\cdots\to\wedge^nF^*\to\mathcal I_{W_d}\to0
$$

## 定理与证明（或缺口）

### 定理 7.18（$W_d$ 的理想层满足 $IT_0$）

设 $C$ 是亏格 $g\ge2$ 的光滑曲线，$\Theta$ 是 $J(C)$ 的主极化。则对每个 $1\le d\le g-1$，$\mathcal I_{W_d}(2\Theta)$ 满足 $IT_0$。

**证明状态：完整**

1. $W_d$ 是两族向量丛（秩分别为 $m$ 与 $n=m+d-g+1$）的退化轨迹，其理想层由 Eagon–Northcott 复形整体消解：$0\to\wedge^mF^*\otimes S^{m-n}E\otimes\det E\to\cdots\to\wedge^nF^*\to\mathcal I_{W_d}\to0$。
   - *为什么*：退化轨迹的坐标环由该复形给出，这是行列式结构的标准结论。
2. 把复形切成短正合列，逐项用 $H^i(\wedge^aF^*\otimes S^bE\otimes\mathcal O(2\Theta))=0\ (i>0)$ 做超上同调消去，只剩 $h^i(S^kE\otimes\mathcal O(\Theta))=0$，其中 $1\le k\le m-n=g-d-1$。
   - *为什么*：长正合列把高次上同调逐层推给下一项，$\wedge^aF^*$ 是局部自由故可移出 $H^i$。
3. 特征 $0$ 下 $S^kE$ 是 $\otimes^kE$ 的直和项，而命题 7.15 已给 $\otimes^kE\otimes\mathcal O(\Theta)$ 满足 $IT_0$（$k\le g-1$），故扭任意 $\alpha$ 后 $h^i$ 全为零，即 $\mathcal I_{W_d}(2\Theta)$ 满足 $IT_0$。
   - *为什么*：直和项的消没由母体继承；$k\le m-n=g-d-1\le g-1$ 正好落在命题 7.15 的范围。


出处：中译 p.151，定理 7.18 与注 7.19（chapters/ch08.tex:610 起的 §7.2）

### 命题 7.22（$W^1_{g-1}$ 的理想层是 $M$-正则的）

$\mathcal I_{W^1_{g-1}}(2\Theta)$ 是 $M$-正则的。

**证明状态：只引出处，原书不重证**


出处：中译 p.152，命题 7.22，证明引 [vGI]（$T_{C_{g-1}}\cong p_*\mathcal O_D(D)$）

## 易错点

- Picard 丛是『负』的：它的射影化是对称积 $C_n$，$\mathcal O_{\mathbb P}(1)$ 并不充裕，Kodaira 型消没不能直接套；必须像命题 7.15 那样先张 $\otimes^k\mathcal E\otimes\mathcal O(\Theta)$ 把正性拿回来。
- 中译 p.150 §7.2 开头那句『将 $C$ 上次数 $n\ge2g-1$ 的线丛 $L$ ……满足 $IT_0$』缺主句（英文原文以 $L$ 为主语），读起来像在定义某个对象；正确读法是『设 $L$ 是……线丛，它满足 $IT_0$；其变换 $\mathcal E_L=\widehat L$ 称为 Picard 丛』。同页『第 $n$ Picard 丛』还漏了『个』。
- 定理 7.18 的证明只用到『$L$ 满足 $IT_0$』这一点（注 7.17），换成任意 $IT_0$ 向量丛命题照旧；别把它读成只有 $L=\mathcal O_C(np)$ 这类特殊选取才有结论。

## 相关卡

- [$M$-正则层](../concepts/m-regular-sheaf.md)
- [Verlinde 丛](../concepts/verlinde-bundle.md)
- [半齐次向量丛](../concepts/semihomogeneous-bundle.md)

## 出处

- ch8 §7.2 Jacobian 上的 Picard 丛；中译 p.150（英文 PDF p.166），源码 `chapters/ch08.tex:610`
