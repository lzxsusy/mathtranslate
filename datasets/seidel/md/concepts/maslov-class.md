# Maslov 类

> `seidel/concept/maslov-class` ｜ track B ｜ draft

**一句话**：Lagrangian 切丛的分类映射从 Lagrangian Grassmannian 拉回万有生成元；它是环路 Maslov 指标的上同调版本，也是分次存在的障碍。

**自测**：Maslov 类为什么是 $H^1(L;\Z)$ 里的一个类，而不是每个交点上的一个整数？

## 定义

设 $(V,\omega_V)$ 是 $2n$ 维辛向量空间，$\mathrm{Gr}(V)\cong U_n/O_n$ 是线性 Lagrangian 子空间的 Grassmannian。万有 Maslov 类是生成元
$$\mu\in H^1(\mathrm{Gr}(V);\Z)\cong\Z.$$
对 Lagrangian 子流形 $L\subset M$，$TL$ 是辛向量丛 $TM|_L$ 的 Lagrangian 子丛。若把 $TM|_L$ 平凡化为 $L\times V$（例如 $M$ 的切丛沿 $L$ 有整体平凡化，或只取相对类），得分类映射 $i:L\to\mathrm{Gr}(V)$，$x\mapsto T_xL$。$L$ 的 Maslov 类定义为拉回
$$\mu_L:=i^*\mu\in H^1(L;\Z).$$
一个常见特例：若只取定 $\det^2TL$ 的平凡化，则 $\mu_L$ 也可由局部相位 $\alpha$（$e^{2\pi i\alpha}=\det^2TL$）的 $d\alpha$ 读出；两种描述在 $TM|_L$ 平凡时一致。它与环路配对给出该环路的 Maslov 指标 $\lambda(\gamma)=\langle\mu_L,[\gamma]\rangle$；配对 $\langle\mu,\cdot\rangle:\pi_1(\mathrm{Gr}(V))\to\Z$ 是同构。

记号：$\mu_L$ 是 $L$ 上的整体上同调类，且是相对类：它依赖 $TM|_L$（或 $\det^2TL$）的平凡化；$\mu(x)$ 则是交点处的整数指标（见 Maslov 指标卡）。$\mu_L\bmod 2=w_1(TL)$；改变 $\det^2TL$ 的平凡化，$\mu_L$ 只平移一个整系数一形式，故必须连同平凡化一起理解。

## 要点

- $H^1(\mathrm{Gr}(V);\Z)\cong\Z$，生成元 $\mu$ 的配对给出同构 $\pi_1(\mathrm{Gr}(V))\to\Z$；故 $\mu_L$ 由它把 $\pi_1(L)$ 的环路送到 $\Z$ 的方式完全决定；非零取值中最小的正数即 $L$ 的最小 Maslov 数 $k$（像为 $k\Z$）。
- $\mu_L=0$ 当且仅当 $L$ 有整体分次 $\alpha:L\to\R$（相对同一平凡化）；因此 Maslov 类是「可分次」的障碍，它的像落在 $k\Z\subset\Z$，$k$ 为最小 Maslov 数。
- $\mu_L\bmod 2=w_1(TL)$：$L$ 可定向是 $\mu_L$ 取偶值的必要条件。$\mathrm{Gr}(V)$ 上 $w_1$ 冗余，正因它是 $\mu$ 的模 $2$ 约化（p.157）。
- 与逐交点指标的分工：$\mu(x)$ 依赖两条 Lagrangian 各自的分次，是交点上的整数；$\mu_L$ 是 $L$ 上的类，只在取环路配对时才化成整数。
- Maslov 类同时控制 determinant line 的 $w_1$：Lemma 11.7 的 $w_1(\det_S)=T(w_2)+(T(\mu)-1)U(\mu)$ 中 $T(\mu)$ 在 $L_k\mathrm{Gr}(V)$ 上取值 $k$，就是 Maslov 指标。

## 公式

$$\mu_L=i^*\mu\in H^1(L;\Z),\qquad \langle\mu_L,[\gamma]\rangle=\lambda(\gamma)$$
$$\langle\mu,\cdot\rangle:\pi_1(\mathrm{Gr}(V))\xrightarrow{\ \sim\ }\Z,\qquad \mu\bmod 2=w_1$$
$$\mu_L\bmod 2=w_1(TL)$$
$$w_1(\det_S)=T(w_2)+(T(\mu)-1)\,U(\mu)$$

## 定理与证明

### 拉回类与环路 Maslov 指标配对

设 $\gamma:S^1\to L$ 是环路，$i\circ\gamma$ 在 $\mathrm{Gr}(V)$ 中横截于各层 $\Sigma_d=\{\Lambda:\dim(\Lambda\cap\Lambda_0)=d\}$。则
$$\langle\mu_L,[\gamma]\rangle=\lambda(i\circ\gamma)=\sum_{s}\mathrm{sign}\,q_{\Lambda_0,\Lambda}(s),$$
右边是对 $\Sigma_1$ 的带符号交数；特别地 $\mu_L=0$ 时 $L$ 上所有环路的 Maslov 指标为零。

（complete；来源：原书 p.157–160 §11e–§11f）

1. 把小环路扰动为与 $\Sigma_1$ 横截、且不遇 $\Sigma_d$（$d\ge2$）。  
   为什么：$\Sigma_1$ 余维 $1$、$\Sigma_d$ 余维 $\ge2$，横截性可由任意小扰动达到，且不改变 $\gamma$ 的同伦类。
2. 在每个穿越点 $s$，$\Lambda(s)\cap\Lambda_0$ 是一维，交叉型 $q_{\Lambda_0,\Lambda}(s)$ 在其上非零，贡献 $\mathrm{sign}\,q=\pm1$；令 $\lambda(\gamma)=\sum_s\mathrm{sign}\,q$。  
   为什么：一维核上的非退化二次型只有正定、负定两种，符号良定义；这就是 §11f 的路径 Maslov 指标（p.159–160）。
3. $\lambda$ 在同伦下不变、对路径拼接可加，从而是群同态 $\pi_1(\mathrm{Gr}(V))\to\Z$。  
   为什么：同伦过程中环路只能扫过余维 $\ge2$ 的层，交数不变；拼接时穿越点集合与符号逐项相加。
4. 由 $\pi_1(\mathrm{Gr}(V))\cong\Z$，$\langle\mu,\cdot\rangle$ 也是同构；在 $n=1$（$\mathrm{Gr}(V)=S^1$）的生成元上两者都等于绕数 $1$，故所有环路上相等。  
   为什么：两个 $\Z\to\Z$ 的同态若在生成元上相等则恒等；$n=1$ 时 Maslov 指标退化为绕数（p.157–158）。

### Lemma 11.7：带边曲面的指数与 determinant line 的 $w_1$

设 $S$ 是亏格 $g$、一个边界的紧 Riemann 面，$\rho\in L\mathrm{Gr}(V)$ 是边界 Lagrangian 环路，$D_{S,\rho}$ 为相应的 $\bar\partial$-算子。则
$$\mathrm{index}(D_{S,\rho})=n\chi(S)+\mu(\rho),$$
且 determinant line 丛的 $w_1$ 为 $w_1(\det_S)=T(w_2)+(T(\mu)-1)U(\mu)$。

（sketch；来源：原书 p.158 Lemma 11.7）

1. （pinch off 边界）把 $S$ 写成圆盘 $D$ 与同亏格闭曲面的连通和；闭曲面上的 $\bar\partial$ 是 $\C$-线性的，其 determinant line 典范平凡，故 $\det_S\cong\det_D$。  
   为什么：由 determinant line 对连通和的乘性 (11.12)，闭曲面部分贡献平凡线丛。
2. （直和公式）对 $\Delta:\mathrm{Gr}(V)\times\mathrm{Gr}(W)\to\mathrm{Gr}(V\oplus W)$ 验证 $(\mathcal L_{k,l}\Delta)^*\det_{S,V\oplus W}\cong\det_{S,V}\boxtimes\det_{S,W}$，并对 $T(w_2),U(\mu)$ 用 Whitney 和公式。  
   为什么：指数在直和下相加，$w_2$ 与 $\mu$ 的 Whitney 公式给出 $T(w_2)+(k+l-1)U(\mu)$ 的乘性。
3. （$n=1$ 计算）$\mathrm{Gr}(V)=S^1$ 时 $\mu(\rho)$ 是绕数；对 $\mu(\rho)=-1$ 的圆盘，$D_{S,\rho}$ 由 Lemma 11.4 单射，再由指数公式可逆，直接验证 (11.16)。  
   为什么：低维模型里 determinant line 的 $w_1$ 就是绕数，给出公式的归一化。
4. 用直和映射在 $H^1(-;\Z/2)$ 上的单射性（至少一个因子维数 $\ge6$）把 $n=1$ 的等式提升到任意 $n$。  
   为什么：任何 $V$ 都可与高维空间直和，公式在单射下被迫成立。

缺口：原书 p.158 只列出上述四条 ingredients，并明说 «we omit the details»；高维归纳与 (11.12) 的乘性验证此处从略。

## 易错点

- 一般辛流形中的 $L$ 没有典范的整数 Maslov 类：必须先取定 $TM|_L$ 的平凡化（或等价的 $\det^2TL$ 平凡化），得到的是相对类；换平凡化会把 $\mu_L$ 平移一个整系数一形式，环路配对随之改变。在 $\R^{2n}$ 中切丛自带平凡化，故有典范的 $\mu_L$。
- $\mu_L$ 与 $\mu(x)$ 不是同一层次的对象：前者是 $L$ 上的上同调类，后者是交点处的整数，只在取环路配对或逐点分次时才降为数。
- 符号约定与 $\det^2$ 的复相位约定绑定；必须与 Maslov 指标卡、Floer 分次卡统一，否则所有指标整体反号。
- $n=1,2$ 时 $\pi_2(\mathrm{Gr}(V))$ 退化（$\pi_2=0$ 或 $\Z$），不能照搬 $n\ge3$ 的 $w_2$ 论证；Maslov 类本身仍由 $\pi_1$ 完全决定。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§11e，p.157–160（原书 p.157–160 §11e–§11f）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§11e Lemma 11.7，p.158–158（原书 p.158 Lemma 11.7）

关联：`seidel/concept/maslov-index`、`seidel/concept/determinant-line`、`seidel/concept/brane-structure`、`seidel/deriv/mu-d-grading`

来源说明：据原书 §11e–§11f（p.157–160）与 Lemma 11.7（p.158）转述；译者注 A06-04。外部：nLab「Maslov index」https://ncatlab.org/nlab/show/Maslov+index，支持句「H^1(LGrass,Z)≃Z. The generator of this cohomology group is called the universal Maslov index u∈H^1(LGrass,Z).」，以及「the tangent bundle is classified by i:Y→LGrass. The Maslov index of Y is the universal Maslov index pulled back along this map i*u∈H^1(Y,Z).」。
