---
id: MS-17
zh: 局部化与等变上同调
en: localization and equivariant cohomology
aliases: [等变上同调, 局部化定理, Atiyah–Bott 局部化, 等变 Euler 类, 非等变极限]
layer: L1
prereqs: [MS-15]
sources:
  - "Cox–Katz 1999, PDF p.299–305（印刷页 276–282）：定义 9.1.1、命题 9.1.2、推论 9.1.3–9.1.4、命题 9.1.5、例题 9.1.1.1/9.1.2.1/9.1.3.1"
  - "Cox–Katz 1999, PDF p.306–316（印刷页 283–293）：式 (9.14)、定理 9.2.1、引理 9.2.2、定理 9.2.3（1/d³）"
  - "Cox–Katz 1999, PDF p.317–323（印刷页 294–300）：引理 9.2.4、定理 9.2.6（6+1/8）、定义 9.3.1、§9.3.2 虚拟局部化"
  - "B 级：本书 §9.1 节内索引（等变上同调 PDF p.299；局部化定理 PDF p.300；等变积分 PDF p.302）"
  - "B 级：nLab『equivariant cohomology』『Atiyah–Bott localization』词条（nLab 标签待补）"
status: draft
review:
  drafter: agent-231
  reviewer: lead
  blindtest: pending
glossary_refs: ["SY01-24 术语表 #21（叠 / stack）", "SY01-24 术语表 #32（虚拟基本类 / virtual fundamental class）", "缺『等变上同调 / 局部化』词条，待补"]
symbols_refs: ['$H_T^*(X)$', '$\mathcal R_T$', '$\operatorname{Euler}_T(N_j)$', '$\lambda_i$', '$\langle I_{0,n,\beta}\rangle_G$']
updated: 2026-11-20
---

# MS-17 局部化与等变上同调

## 1. 一句话

把环面作用簇的上同调类局部化到固定点轨迹，使 GW 积分化为可算的有限和。

## 2. 为什么需要它

1. **第 11 章证明镜像定理的主工具。** 本章章首明说，局部化「将提供第十一章证明镜像定理所需的一些工具」（PDF p.298；chapter09.tex:3）。第 2 章已预告 Givental 版证明要在稳定映射模空间上对等变上同调用局部化公式（chapter02.tex:433–444、458）；第 10 章指出参数 $\hbar$ 自然地来自等变上同调（chapter10.tex:847，[Givental2]）；第 11 章把本章的 $\mathcal R_T$ 换成分式环 $\mathcal R_G$，令 $\lambda_i,\hbar$ 都取逆，权为 $\{\lambda_i+r\hbar\}$（chapter11.tex:156、120）。缺了局部化，这条证明链的 $\hbar$ 方向无从定义。
2. **本书招牌计数全部靠它算出来。** $N_d$ 定义在 $H^*(\overline M_{0,n}(X,\beta))$ 上，而 $T=(\mathbb C^*)^{r+1}$ 在 $\overline M_{0,n}(\mathbb P^r,d)$ 上的作用使固定点分支与法丛权都可算：直线数 $2875$（例题 9.1.3.1，PDF p.304–305）、光滑有理曲线 $d$ 重覆盖的 $1/d^3$（定理 9.2.3，PDF p.312）、六结点五次曲线二重覆盖的 $6+\frac18$（定理 9.2.6，PDF p.320）都只是局部化求和。若不局部化，第七章关于瞬子数 $n_{10}=6\times17\,601\,000+\cdots$ 的论断（chapter07.tex:2204、2216）证不完。
3. **「计数几何用局部化」的起点。** PDF p.298 明说：就计数几何而言，局部化首次由 [ES2] 利用 Hilbert 概形上的环面作用引入；命题 9.1.5 正是 [ES2] 的 Bott 留数表述，例题 9.1.3.1 则是它最干净的应用。

## 3. 定义（全假设）

### 3.1 等变上同调（Borel 构造，定义 9.1.1，PDF p.299）

设 $G$ 为紧连通 Lie 群，$EG\to BG$ 为主 $G$ 丛且 $EG$ 可缩（同伦等价意义下唯一）。$X$ 为 $G$-空间，令
$$X_G=X\times_G EG,\qquad i_X:X\hookrightarrow X_G\ \text{（纤维包含）},$$
定义 $$H_G^*(X):=H^*(X_G),$$
系数一律取 $\mathbb C$。$H_G^*(\mathrm{point})=H^*(BG)$；沿 $X\to\mathrm{point}$ 拉回使 $H_G^*(X)$ 成为 $H^*(BG)$-模，称 $H^*(BG)$ 为**系数环**。$i_X$ 诱导**遗忘映射** $i_X^*:H_G^*(X)\to H^*(X)$。

环面情形 $G=T=(\mathbb C^*)^n$：$BT=(\mathbb{CP}^\infty)^n$。设 $M(T)$ 为特征标群，$\rho\mapsto c_1(L_\rho)$ 给出 $M(T)\simeq H^2(BT;\mathbb Z)$，复化得 $\operatorname{Sym}(M(T))\otimes\mathbb C\simeq H^*(BT;\mathbb C)$，$\psi(\rho)$ 称 $\rho$ 的**权**。基本特征标 $\rho_i(t_1,\dots,t_n)=t_i$ 的权记 $\lambda_i$，则
$$H_T^*(\mathrm{point})=H^*(BT)\simeq\mathbb C[\lambda_1,\dots,\lambda_n],\qquad \lambda_i=c_1(\mathcal O(\lambda_i)). \tag{9.1}$$
在此等同下 $i_{\mathrm{point}}^*$ 即把全部 $\lambda_i$ 映到 $0$，称**非等变极限**（PDF p.299）。

### 3.2 等变向量丛、等变 Chern 类与 Euler 类（PDF p.299）

**等变向量丛**是 $X$ 上的向量丛 $E$，连同 $G$ 在 $E$ 上的提升作用、且在纤维上线性。此时 $E_G$ 是 $X_G$ 上的丛；**等变 Chern 类** $c_k^G(E):=c_k(E_G)\in H_G^*(X)$；若 $\operatorname{rank}E=r$，**等变 Euler 类** $\operatorname{Euler}_G(E):=c_r^G(E)\in H_G^*(X)$。本书自 PDF p.299 起把 Euler 类看作**上同调类**（第 7 章中它是同调类，即最高 Chern 类的 Poincaré 对偶）。若 $E$ 分解为等变线丛 $E\cong\bigoplus_iL_{\chi_i}$，则
$$\operatorname{Euler}_G(E)=\prod_i\chi_i(\lambda).$$
例题 9.1.1.1（PDF p.299）：$G=(\mathbb C^*)^n$ 对角作用于 $\mathbb C^n$、$X=\mathrm{point}$ 时 $E_G\simeq\mathcal O(\lambda_1)\oplus\cdots\oplus\mathcal O(\lambda_n)$，故 $c_k^G(E)=\sigma_k(\lambda_1,\dots,\lambda_n)$（第 $k$ 个初等对称函数）。

### 3.3 局部化的假设（PDF p.300）

设环面 $T=(\mathbb C^*)^n$ 作用于**光滑流形**（或光滑代数叠的底层轨形，见 3.5）$X$。由 [Iversen]，固定点轨迹 $X^T$ 是光滑连通分支 $Z_j$ 之并。令 $i_j:Z_j\hookrightarrow X$ 为包含，$N_j$ 为 $Z_j$ 在 $X$ 中的法丛（等变向量丛），故 $\operatorname{Euler}_T(N_j)\in H_T^*(Z_j)$。
$i_j$ 诱导限制 $i_j^*:H_T^*(X)\to H_T^*(Z_j)$；另有 Gysin 推前 $i_{j!}:H_T^*(Z_j)\to H_T^*(X)$，满足**自交公式**
$$i_j^*\circ i_{j!}(\alpha)=\alpha\cup\operatorname{Euler}_T(N_j). \tag{9.3}$$
令 $\mathcal R_T:=\mathbb C(\lambda_1,\dots,\lambda_n)=\operatorname{Frac}H^*(BT)$，则 $H_T^*(Z_j)\otimes_{H^*(BT)}\mathcal R_T$ 有定义。**关键假设**（[AB] 的观察）：$\operatorname{Euler}_T(N_j)$ 在 $\mathcal R_T$-局部化后**可逆**。

### 3.4 局部化定理与积分公式（命题 9.1.2 PDF p.300；推论 9.1.3 PDF p.302）

在上述假设下存在同构
$$H_T^*(X)\otimes\mathcal R_T\ \xrightarrow{\ \sim\ }\ \bigoplus_jH_T^*(Z_j)\otimes\mathcal R_T,\qquad
\alpha\longmapsto\Bigl(\tfrac{i_j^*(\alpha)}{\operatorname{Euler}_T(N_j)}\Bigr)_j,$$
其逆由 $(\alpha_j)_j\mapsto\sum_ji_{j!}(\alpha_j)$ 诱导；等价地，对任意 $\alpha\in H_T^*(X)\otimes\mathcal R_T$，
$$\alpha=\sum_ji_{j!}\Bigl(\tfrac{i_j^*(\alpha)}{\operatorname{Euler}_T(N_j)}\Bigr).$$
当 $X$ **完备**时，$\pi_X:X_T\to BT$ 的推前由沿纤维积分给出，称**等变积分** $\int_{X_T}:H_T^*(X)\to H^*(BT)$，于是
$$\int_{X_T}\alpha=\sum_j\int_{(Z_j)_T}\frac{i_j^*(\alpha)}{\operatorname{Euler}_T(N_j)}. \tag{推论 9.1.3}$$

### 3.5 代数叠版本（推论 9.1.4，PDF p.303）

设 $X$ 是具 $T$ 作用的**光滑代数叠的底层轨形**（局部商图 $U/H$，$U$ 光滑，$H\subset\operatorname{GL}(n,\mathbb C)$ 小群）。仿 3.4 定义 $Z_j,i_j,N_j,\operatorname{Euler}_T(N_j)$ 后，
$$\int_{X_T}\alpha=\sum_j\int_{(Z_j)_T}\frac{i_j^*(\alpha)}{a_j\,\operatorname{Euler}_T(N_j)},$$
其中 $a_j$ 是 $Z_j$ 一般点所对应对象的自同构群的阶（轨形稳定化子阶）。对 $\overline M_{0,n}(\mathbb P^r,d)$ 的固定点分支 $\overline M_\Gamma$，$a_\Gamma=|A_\Gamma|$，$A_\Gamma$ 由式 (9.14) 的正合列确定：
$$1\longrightarrow\prod_e\mathbb Z/d_e\mathbb Z\longrightarrow A_\Gamma\longrightarrow\operatorname{Aut}(\Gamma)\longrightarrow1. \tag{9.14}$$

### 3.6 本书用法

PDF p.299 用 Borel 构造（拓扑版；代数构造引 [EG]）定义 $H_G^*$，随即取 $G=T=(\mathbb C^*)^n$；$\mathcal R_T$ 是**交换代数意义**的分式域局部化（与第 11 章对分式环 $\mathcal R_G$ 的用法对照，chapter11.tex:156）；PDF p.303 把它推广到光滑代数叠，加 $a_j$ 因子；PDF p.321 的定义 9.3.1 以 $H_G^*(\mathrm{point})$ 为取值环定义等变 GW 不变量。与 [AB] 的标准表述无实质出入，只是本书只用 $(\mathbb C^*)^n$、复系数，不对一般紧 Lie 群算例。**本卡页码一律为 PDF 物理页（即 `\SourcePage{N}`，印刷页 $+23$）。**

## 4. 最小例子（能算出）

### 4.1 $\mathbb P^1$：例题 9.1.2.1 取 $r=1$（PDF p.300–302）

$T=(\mathbb C^*)^2$ 作用 $(t_0,t_1)\cdot(x_0,x_1)=(t_0^{-1}x_0,t_1^{-1}x_1)$，使齐次形式 $x_i$ 的权为 $\lambda_i$；固定点 $q_0=[1:0],q_1=[0:1]$。

1. **环结构。** 由 $\prod_{j=0}^r(p-\lambda_j)=0$（式 (9.7)，$p=c_1(\mathcal O_{\mathbb P_T^r}(1))$）取 $r=1$：
$$H_T^*(\mathbb P^1)=\mathbb C[p,\lambda_0,\lambda_1]\big/\bigl((p-\lambda_0)(p-\lambda_1)\bigr),\qquad i_j^*(p)=\lambda_j.$$
2. **法丛的权。** $N_j=T_{q_j}\mathbb P^1=\operatorname{Hom}(\mathbb C q_j,\mathbb C^2/\mathbb C q_j)$，权 $\lambda_j-\lambda_k$（$k\ne j$），故
$$\operatorname{Euler}_T(N_0)=\lambda_0-\lambda_1,\qquad \operatorname{Euler}_T(N_1)=\lambda_1-\lambda_0.$$
3. **等变积分（推论 9.1.3）。**
$$\int_{\mathbb P^1_T}p=\frac{\lambda_0}{\lambda_0-\lambda_1}+\frac{\lambda_1}{\lambda_1-\lambda_0}=\frac{\lambda_0-\lambda_1}{\lambda_0-\lambda_1}=1 .$$
4. **二次类。** 由关系式 $p^2=(\lambda_0+\lambda_1)p-\lambda_0\lambda_1$ 与上一步，
$$\int_{\mathbb P^1_T}p^2=\frac{\lambda_0^2}{\lambda_0-\lambda_1}+\frac{\lambda_1^2}{\lambda_1-\lambda_0}=\frac{\lambda_0^2-\lambda_1^2}{\lambda_0-\lambda_1}=\lambda_0+\lambda_1 .$$
5. **非等变极限与一致性检查。** $\lambda_i\to0$ 时 $\int H=1$、$\int H^2=0$，正是普通 $\mathbb P^1$ 上的次数；又 $\int_{\mathbb P^1_T}1=\frac1{\lambda_0-\lambda_1}+\frac1{\lambda_1-\lambda_0}=0$，与普通 $\int_{\mathbb P^1}1=0$ 相合。
6. **Lagrange 插值核对。** 取 $F(p)=p$：
$$\frac{\lambda_0(p-\lambda_1)}{\lambda_0-\lambda_1}+\frac{\lambda_1(p-\lambda_0)}{\lambda_1-\lambda_0}=\frac{p(\lambda_0-\lambda_1)}{\lambda_0-\lambda_1}=p .$$

### 4.2 二重覆盖的 $1/8$：定理 9.2.3 证明中 $d=2$ 的显式求和（PDF p.313–314）

空间 $\overline M_{0,0}(\mathbb P^1,2)$ 有三个固定点分支 $\Gamma_1,\Gamma_2,\Gamma_3$（例题 9.2.1.1），每个 $a_\Gamma=2$。被积函数是障碍丛 $\mathcal V=R^1\pi_{1*}e_1^*(\mathcal O(-1)\oplus\mathcal O(-1))$ 的等变 Euler 类。

1. $\Gamma_1$（链图，$f_1(p)=q_1$）：$\operatorname{Euler}_T(N_{\Gamma_1})=2(\lambda_1-\lambda_0)^2$（式 (9.?)，PDF p.313）；$\mathcal V$ 的两权为 $-\lambda_1,-\lambda_1$，故 $\operatorname{Euler}_T(\mathcal V)=\lambda_1^2$。
2. $\Gamma_2$（交换 $\lambda_0,\lambda_1$）：$\operatorname{Euler}_T(N_{\Gamma_2})=2(\lambda_0-\lambda_1)^2$，$\operatorname{Euler}_T(\mathcal V)=\lambda_0^2$。
3. $\Gamma_3$（$f_3(z_0,z_1)=(z_0^2,z_1^2)$）：$\operatorname{Euler}_T(N_{\Gamma_3})=(\lambda_0-\lambda_1)(\lambda_1-\lambda_0)$；$\mathcal V$ 两权均为 $-\frac{\lambda_0+\lambda_1}2$，故 $\operatorname{Euler}_T(\mathcal V)=\bigl(\frac{\lambda_0+\lambda_1}2\bigr)^2$。
4. 由推论 9.1.4（每项除 $a_\Gamma=2$）：
$$\frac{\lambda_1^2}{2\cdot2(\lambda_1-\lambda_0)^2}+\frac{\lambda_0^2}{2\cdot2(\lambda_0-\lambda_1)^2}
+\frac{\bigl(\frac{\lambda_0+\lambda_1}2\bigr)^2}{2(\lambda_1-\lambda_0)(\lambda_0-\lambda_1)}
=\frac{\lambda_0^2+\lambda_1^2-\frac12(\lambda_0+\lambda_1)^2}{4(\lambda_0-\lambda_1)^2}=\frac{\frac12(\lambda_0-\lambda_1)^2}{4(\lambda_0-\lambda_1)^2}=\frac18 .$$
5. **数值复核（本卡，python 精确有理数）**：$(\lambda_0,\lambda_1)=(2,3)$ 时三项为 $\frac94,1,-\frac{25}8$，和 $\frac18$；$(5,7)$ 时 $\frac{49}{16},\frac{25}{16},-\frac92$，和 $\frac18$。若漏掉 $a_\Gamma=2$，和变成 $\frac14$——这正是 §7 误解 2 的反例。
6. **一般 $d$。** 限制到 $T'=\mathbb C^*\times\{1\}$（$h=\lambda_0$）后只有单边图非零：障碍 Euler $=(-1)^{d-1}((d-1)!)^2h^{2d-2}/d^{2d-2}$，$\operatorname{Euler}_{T'}(N_\Gamma)=(-1)^{d-1}(d!)^2h^{2d-2}/d^{2d-2}$，再除 $a_\Gamma=d$，比值为 $1/d^3$（PDF p.315–316）。

### 4.3 五次三维簇的直线数 $2875$：例题 9.1.3.1（PDF p.304–305）

$T=(\mathbb C^*)^5$ 作用于 $\mathbb C^5$ 诱导 $G(2,5)$ 的作用，$10$ 个孤立固定点 $L_I$ 对应 $\mathbb P^4$ 的坐标直线（$I\subset\{1,\dots,5\}$，$|I|=2$）。由命题 9.1.5（本卡以 $\lambda=(2,3,5,7,11)$ 与 $\lambda=(\frac12,\frac13,\frac15,\frac17,\frac1{11})$ 两组精确有理数代入十项求和，均得 $2875$，即 $\lambda_i$ 全部消去），
$$\langle I_{0,0,1}\rangle=\int_{G(2,5)}c_6(\operatorname{Sym}^5U^*)=\sum_{|I|=2}\frac{\prod_{a=0}^5(a\lambda_{i_1}+(5-a)\lambda_{i_2})}{\prod_{i\in I}\prod_{j\notin I}(\lambda_i-\lambda_j)}=2875 .$$

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | $H_T^*(\mathrm{point})=\mathbb C[\lambda_1,\dots,\lambda_n]$，$i_{\mathrm{point}}^*$ 即非等变极限 $\lambda_i\to0$ | PDF p.299，式 (9.1) | 极限是拉回，不是形式代入 |
| 2 | 自交公式 $i_j^*i_{j!}(\alpha)=\alpha\cup\operatorname{Euler}_T(N_j)$ | PDF p.300，式 (9.3) | Gysin 推前的全部计算依赖它 |
| 3 | 局部化同构，逆为 $\sum_ji_{j!}$；等价地 $\alpha=\sum_ji_{j!}(i_j^*\alpha/\operatorname{Euler}_T(N_j))$ | PDF p.300，命题 9.1.2 | 可看作 Lagrange 插值的推广（PDF p.302） |
| 4 | 积分公式 $\int_{X_T}\alpha=\sum_j\int_{(Z_j)_T}i_j^*(\alpha)/\operatorname{Euler}_T(N_j)$ | PDF p.302，推论 9.1.3 | 需 $X$ 完备 |
| 5 | 光滑代数叠版本分母多出 $a_j$（一般点对象的自同构群阶） | PDF p.303，推论 9.1.4；式 (9.14) | 模空间计算必须用它 |
| 6 | 孤立固定点 + Chern 多项式：$\int_XP(c_k(E))=\sum_jP(\sigma_k(\ell_j(\lambda)))/\prod_kt_j^k(\lambda)$ | PDF p.304，命题 9.1.5 | 即 [ES2] 的 Bott 留数；轨形版每项除 $a_j$ |

## 6. 推导流程（D1…Dn）

- **D1** 取主 $G$ 丛 $EG\to BG$（$EG$ 可缩），令 $H_G^*(X):=H^*(X\times_GEG)$，得系数环 $H^*(BG)$ 与遗忘映射。依据：定义 9.1.1，PDF p.299。
- **D2** 取 $G=(\mathbb C^*)^n$：由特征标权得 $H_T^*(\mathrm{point})=\mathbb C[\lambda_1,\dots,\lambda_n]$；把等变向量丛的 Chern 类定义为 $c_k(E_G)$，最高类为等变 Euler 类。依据：PDF p.299，式 (9.1)；例题 9.1.1.1。
- **D3** 对光滑 $X$：固定点轨迹光滑（[Iversen]），法丛等变、故有 $\operatorname{Euler}_T(N_j)$；取分式域 $\mathcal R_T$，则各 $\operatorname{Euler}_T(N_j)$ 可逆（[AB]）。依据：PDF p.300。
- **D4** 由自交公式 (9.3) 验证 $\alpha\mapsto(i_j^*\alpha/\operatorname{Euler}_T(N_j))_j$ 与 Gysin 求和互逆，得局部化同构。依据：命题 9.1.2，PDF p.300。
- **D5** 对 $\mathbb P^r$ 具体化：$\prod(p-\lambda_j)=0$ 定环结构，$i_j^*(p)=\lambda_j$，$\operatorname{Euler}_T(N_j)=\prod_{k\ne j}(\lambda_j-\lambda_k)$，局部化映射 (9.11)，对偶基 $\phi_j=\prod_{k\ne j}(p-\lambda_k)$，得 Lagrange 恒等式。依据：例题 9.1.2.1，PDF p.300–302。
- **D6** 向 $\mathrm{point}$ 推前（$X$ 完备时沿纤维积分）得积分公式。依据：推论 9.1.3，PDF p.302。
- **D7** 换成光滑代数叠的底层轨形（局部商图 $U/H$），逐块在 $U$ 上工作，分母出现稳定化子阶 $a_j$。依据：推论 9.1.4，PDF p.303。
- **D8** 固定点孤立时把 $E|_{Z_j}$、切空间分解为特征标，代入积分公式，得 Chern 多项式的 Bott 留数形式；对 $G(2,5)$ 用 $c_6(\operatorname{Sym}^5U^*)$ 得 $2875$。依据：命题 9.1.5，PDF p.304；例题 9.1.3.1，PDF p.304–305。
- **D9** 把 $T$ 作用搬到 $\overline{\mathcal M}_{0,n}(\mathbb P^r,d)$：固定点由带 $i_v,S_v,d_e$ 的树 $\Gamma$ 描述，$a_\Gamma=|A_\Gamma|$ 由式 (9.14) 给出，法丛 Euler 类由定理 9.2.1 的三因子公式给出。依据：PDF p.306–309。
- **D10** 代入推论 9.1.4：$d$ 重覆盖得 $1/d^3$（定理 9.2.3，PDF p.312）；六结点五次曲线二重覆盖得 $6+\frac18$（定理 9.2.6，PDF p.320）；一般情形用等变虚拟基本类与虚法丛（§9.3.2，PDF p.322–323，[GPa]）。

## 7. 常见误解与反例（≥2）

**误解 1：局部化只对孤立固定点成立。** 错：命题 9.1.2 与推论 9.1.3 对任意光滑固定分支 $Z_j$ 成立，孤立点只是 $Z_j$ 为点的特例（PDF p.300、302）。命题 9.1.5 才是「固定点孤立」的加强形式，两者不可混用：前者的分母是分支法丛的 Euler 类，后者是切空间权之积。

**误解 2：在模空间上照搬光滑簇的公式，$a_j$ 可以不管。** 错：模空间是代数叠，必须除稳定化子阶 $a_j$（推论 9.1.4，PDF p.303）。反例：$\overline M_{0,0}(\mathbb P^1,2)$ 的三个分支各有 $a_\Gamma=2$；本卡 §4.2 算得正确值 $\frac18$，若漏掉因子 $2$ 和为 $\frac14$，与定理 9.2.3 的 $1/d^3=\frac18$ 不符。

**误解 3：先把 $\lambda_i\to0$ 再算，或等变不变量就是普通不变量。** 错：非等变极限是拉回 $i_{\mathrm{point}}^*$，只能在 $\mathcal R_T$ 中算完之后取（PDF p.299、p.321 的恒等式 $i_{\mathrm{point}}^*\langle I\rangle_G=\langle I\rangle(i_X^*\alpha)$）。反例见 §4.1：$\int p^2=\lambda_0+\lambda_1\to0$ 而 $\int p=1$；若先令 $\lambda=0$，所有分母 $(\lambda_j-\lambda_k)$ 都退化，公式整体失效。

**误解 4：多重覆盖公式 $1/d^3$ 对任何曲线都成立。** 错：定理 9.2.3 要求光滑有理曲线**刚性嵌入** Calabi–Yau 三维簇（PDF p.312）。反例：一般五次三维簇上的六结点有理平面五次曲线，其二重覆盖对 $N_{10}$ 的贡献是 $6+\frac18$，而非 $2^{-3}=\frac18$（定理 9.2.6，PDF p.320）；多出的 $6$ 来自六个点分支（各贡献 $1$），须用等变虚拟基本类处理。

**误解 5：本书前后所说的「Euler 类」是同一个东西。** 错：第 7 章的 Euler 类是**同调类**（最高 Chern 类取 Poincaré 对偶），PDF p.299 起改为**上同调类**，公式里的 $\operatorname{Euler}_T(N_j)$ 是后者；两者只在可对偶的场合互相换算，局部化公式中不能换成同调类。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999（本书） | PDF p.298–305，§9.1（定义 9.1.1、命题 9.1.2、推论 9.1.3–9.1.4、命题 9.1.5、例题 9.1.2.1/9.1.3.1） | 等变上同调、Atiyah–Bott 局部化、积分公式、代数叠版本、Bott 留数与 $2875$ |
| Cox–Katz 1999（本书） | PDF p.306–316，§9.2.1–9.2.2（式 (9.14)、定理 9.2.1、引理 9.2.2、定理 9.2.3） | 稳定映射固定点图、法丛 Euler 类、$d$ 重覆盖贡献 $1/d^3$ |
| Cox–Katz 1999（本书） | PDF p.317–323，§9.2.3–9.3（引理 9.2.4、定理 9.2.6、定义 9.3.1、§9.3.2） | 六结点曲线二重覆盖 $6+\frac18$、等变 GW 不变量、虚拟局部化 |
| SY01-24《镜像对称》（Siebert 讲义中译本） | 术语表 #21「叠 / stack」p.24；#32「虚拟基本类」p.46；无「等变上同调 / 局部化」词条 | **冲突**：SY01-24 把 stack 作「叠」，本书 PDF p.303 作「光滑代数叠的底层轨形」；按 _冲突表 T3「视卡片而定」，本卡取「代数叠」。另：术语表无等变上同调条目（术语缺口，非冲突），其主线是 HMS 辛侧，不涉及 GW 局部化 |
| SY01-25《同调镜像对称与环面纤维化》资料卡 | 卡 04 §一（25 条核心术语，无等变上同调/局部化）；§五 与后续工作接口 | 无对应词条（术语缺口）；其辛侧 $A_\infty$/Morse 模型与本书 GW 侧分工不同（_冲突表 U4），属适用范围差异，非术语冲突 |
| Atiyah–Bott 1984（[AB]） | Topology **23**，1–28 | 局部化定理（命题 9.1.2）与「$\operatorname{Euler}_T(N_j)$ 可逆」的观察；PDF p.298、300 明引 |
| Iversen 1972（[Iversen]） | Invent. Math. **16**，229–236 | 环面作用在代数簇上固定点轨迹的光滑性；PDF p.300 明引 |
| Kontsevich 1995（[Kontsevich2]） | The Moduli Space of Curves，Progr. Math. **129**，Birkhäuser，335–368 | 稳定映射的固定点图与法丛 Euler 类（定理 9.2.1 的来源）；PDF p.298、306 明引 |
| Ellingsrud–Strømme 1996（[ES2]） | J. Amer. Math. Soc. **9**，175–193 | Bott 留数用于计数几何（直线数等）；PDF p.298、304 明引，命题 9.1.5 的表述来源 |
| Graber–Pandharipande 1997（[GPa]） | preprint，alg-geom/9708001（本书引） | 虚拟基本类的局部化公式（虚法丛版本）；PDF p.323 |

## 9. 前置与后继

- **前置：** MS-15（稳定映射与虚拟基本类，_queue.md 指定）——本卡的靶空间 $\overline{\mathcal M}_{0,n}(\mathbb P^r,d)$ 与虚拟基本类都来自它。另需第 7 章的上同调、Chern 类与 Gysin 推前、以及分式域（交换代数）的基本语言；Borel 构造的定义在 PDF p.299 现场给出，不假定读者懂拓扑群。
- **后继：** MS-05（GW 不变量：定理 9.2.3/9.2.6 修正 $N_d$ 的多重覆盖贡献，$N_{10}=n_1 10^{-3}+n_2 5^{-3}+n_5 2^{-3}+n_{10}$，chapter07.tex:2216）；MS-04（量子上同调：Bott 留数与量子环结构）；MS-18/MS-19（Frobenius 流形、量子超平面截面原理）；第 11 章镜像定理证明（用 $\mathcal R_G$ 与权 $\lambda_i+r\hbar$，chapter11.tex:156、120；该章卡未在 _queue.md 立项，待补）。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- 只给签名与关键假设，允许 sorry
structure EquivariantCohomology (G X : Type) where
  BG  : Type                     -- 分类空间；G = (ℂ*)^n 时 BG = (ℂP^∞)^n
  HT  : ℤ → Type                 -- H_G^*(X) = H^*(X ×_G EG)，分级环
  Hpt : Type                     -- H^*(BG) = ℂ[λ₁,…,λₙ]，系数环
  forget : HT 0 → H X           -- i_X^*：非等变极限（λ_i ↦ 0）
-- 局部化数据：固定点分支 Z、法丛等变 Euler 类、限制 i_j^* 与 Gysin 推前 i_{j!}、分式域 R_T
structure LocalizationData (HT RT : Type) [CommRing HT] [CommRing RT] [Algebra HT RT] where
  Z      : Type
  [fintypeZ : Fintype Z]
  HZ     : Z → Type
  [ringHZ : (j : Z) → CommRing (HZ j)]
  iStar  : (j : Z) → HT → HZ j   -- i_j^*
  euler  : (j : Z) → HZ j        -- Euler_T(N_j)
  gysin  : (j : Z) → HZ j → HT   -- i_{j!}

-- 命题 9.1.2（PDF p.300）：H_T^*(X) ⊗ R_T ≅ ⊕_j H_T^*(Z_j) ⊗ R_T
theorem atiyah_bott_isomorphism (L : LocalizationData HT RT) :
    Function.Bijective (fun α : HT => fun j : L.Z => L.iStar j α) := by sorry
-- 推论 9.1.3（PDF p.302）：∫_{X_T} α = Σ_j ∫_{(Z_j)_T} i_j^*(α)/Euler_T(N_j)
theorem localization_integral (L : LocalizationData HT RT) (α : HT) :
    equivariantIntegral α = ∑ j : L.Z, equivariantIntegral (L.iStar j α / L.euler j) := by sorry
-- 推论 9.1.4（PDF p.303）：光滑代数叠版本，分母乘轨形稳定化子阶 a_j
theorem orbifold_localization_integral (L : LocalizationData HT RT)
    (a : L.Z → ℕ) (ha : ∀ j, 0 < a j) (α : HT) :
    equivariantIntegral α = ∑ j : L.Z, (1 / (a j : ℚ)) * equivariantIntegral (L.iStar j α / L.euler j) := by sorry
-- 定理 9.2.3（PDF p.312）：刚性嵌入 CY 三维簇的光滑有理曲线的 d 重覆盖贡献 1/d³
def multipleCoverContribution (d : ℕ) : ℚ := sorry
theorem multiple_cover_contribution (d : ℕ) (hd : 0 < d) :
    multipleCoverContribution d = 1 / (d : ℚ) ^ 3 := by sorry
```

## 11. 待核清单

- [ ] **冲突（术语）**：SY01-24 术语表 #21 把 stack 作「叠」，本书 PDF p.303 作「光滑代数叠的底层轨形」；按 _冲突表 T3「视卡片而定」本卡取「代数叠」，需回填术语表并复核 T3 措辞。
- [ ] **冲突（书内位置）**：_queue.md 记 MS-17 于「第 7 章 §7.3」，而译本第 7 章是 Gromov–Witten，局部化在第 9 章 §9.1（chapter09.tex:1 `\chapter{局部化}`；PDF p.298 起）。本卡按第 9 章 §9.1–9.3 写，_queue.md「主要书内位置」列待改。
- [ ] **术语缺口**：SY01-24 术语表与 SY01-25 卡 04 的 25 条核心术语均无「等变上同调 / 局部化 / Atiyah–Bott」条目；建议随术语表批次补条（en: equivariant cohomology; localization），并与 _冲突表 登记。
- [ ] **页码口径**：本卡按 `\SourcePage{N}` = PDF 物理页（印刷页 +23）标注（如 PDF p.300 = 印刷 p.277）；既有 MS-16 等卡写作「p.192（PDF p.192）」的口径与本卡不一致，待 lead 统一。
- [ ] §4.2 的 $d=2$ 三项求和与 §4.3 的 $2875$ 均为本卡补算的数值复核：前者经 python 精确有理数验算（$(\lambda_0,\lambda_1)=(2,3),(5,7)$ 均得 $\frac18$；书中只给结果 $\frac18$，PDF p.314），后者代入两组精确有理数均得 $2875$（书中只写「计算得到 2875」，PDF p.305）；代数化简与代入值待复核。
- [ ] 定理 9.2.6 中「$6$」的来历（六个点分支各贡献 $1$）依 PDF p.320 证明，并用到 PDF p.320 前文「虚拟基本类在六点处退化为通常点类」的论证与 [BS] Macaulay 计算（PDF p.319–320），未逐行核。
