---
id: MS-05
zh: Gromov–Witten 不变量
en: Gromov–Witten invariant
aliases:
  - GW 不变量
  - Gromov–Witten 类
  - GW 数
layer: L1
prereqs:
  - MS-15
  - MS-16
sources:
  - "A 级：Cox–Katz《镜像对称与代数几何》定义 7.1.9（PDF p.206）；§7.1 构造 PDF p.190–206；§7.3 公理 PDF p.214–218；§7.4.2 PDF p.220–223"
  - "A 级：Kontsevich–Manin 1994 [KoM1]（GW 类公理，本书 p.214–218 转述；原始文献定理号待核）"
  - "B 级：Fulton–Pandharipande《Notes on stable maps and quantum cohomology》（[FP]，本书 p.191 推荐为入门讲义）"
  - "B 级：本书第 7 章 §7.1–§7.4（PDF p.190–238）"
status: draft
review:
  drafter: agent-223
  reviewer: lead
  blindtest: pending
glossary_refs:
  - stable map / 稳定映射
  - virtual fundamental class / 虚拟基本类
  - expected dimension / 预期维数
  - stack / 代数叠
symbols_refs:
  - "$I_{g,n,\\beta}$"
  - "$\\langle I_{g,n,\\beta}\\rangle$"
  - "$[\\overline{\\mathcal M}_{g,n}(X,\\beta)]^{\\mathrm{virt}}$"
  - "$N_d$"
updated: 2026-11-20
---

# MS-05 Gromov–Witten 不变量

## 1. 一句话
把过指定圈的曲线计数提升为稳定映射模空间上的有理数。

## 2. 为什么需要它
- **给 A 模型的曲线计数一个严格定义。** 本书 p.190 开篇用有理曲线数 $n_\beta$ 写 A 模型关联函数，但那里的 $n_\beta$ 只是「代表 $\beta$ 的有理曲线条数」的朴素说法；曲线条数本身既不一定有限，也不是变形不变的，GW 不变量把同样的信息装进 $\langle I_{g,n,\beta}\rangle\in\mathbb Q$，即使模空间维数超出预期（p.195）或曲线非嵌入（多重覆盖，p.225–226）也有定义。
- **量子上同调的乘法常数。** 本书 p.191 明言第 8 章要用这些不变量构造量子上同调环，p.219 又说量子上同调是由 $\langle I_{0,n,\beta}\rangle$ 构造出来的。没有 GW 不变量，MS-04 的量子乘积只是记号。
- **镜像对称的比较对象。** 镜像定理（第 11 章）比较 A 模型与 B 模型的关联函数，而 A 模型侧的系数就是 GW 不变量；且比较要求 A 模型侧在复结构形变下不变（p.190），这正是形变公理（p.217）的内容。
- **让 2875 这类数有合法来源。** 一般五次三维簇上直线数的严格说法是 $\langle I_{0,0,\ell}\rangle=2875$（p.196–197、p.207）；普通基本类在这里给不出零维类，必须用虚拟基本类。

## 3. 定义（全假设）

**假设。** $X$ 为 $\mathbb C$ 上光滑射影簇（§7.3 陈述公理时明确要求光滑射影，p.214；模空间的存在性本身只需 $X$ 射影，p.192–193）。$\beta\in H_2(X,\mathbb Z)$，$g,n\ge 0$，$\alpha_1,\dots,\alpha_n\in H^*(X,\mathbb Q)$。记 $\overline{\mathcal M}_{g,n}(X,\beta)$ 为稳定映射的模叠（p.193：$\mathbb C$ 上的固有代数叠），$\overline M_{g,n}(X,\beta)$ 为其粗模空间（p.192–193），$\overline M_{g,n}$ 为稳定曲线模空间，$n+2g\ge 3$ 时它是维数 $3g-3+n$ 的轨形（p.192）。$\omega_X$ 指 $X$ 的**典范类** $K_X$（p.194；$\int_\beta\omega_X=-\int_\beta c_1(TX)$，见 p.210）。设 $\xi=[\overline{\mathcal M}_{g,n}(X,\beta)]^{\mathrm{virt}}$ 为虚拟基本类（p.199–205，构造见 MS-15；本书按 p.204 的宽松记法把它写在粗模空间上），$\deg\xi=\dim^{\exp}=(1-g)(\dim X-3)-\int_\beta\omega_X+n$（p.194）。赋值映射 $e_i:\overline{\mathcal M}_{g,n}(X,\beta)\to X$ 取第 $i$ 个标记的像（p.195）。

**（i）GW 类（仅当 $n+2g\ge 3$）。** 由结构映射 $\pi=(\pi_1,\pi_2):\overline{\mathcal M}_{g,n}(X,\beta)\to X^n\times\overline M_{g,n}$（p.194）与投影 $p_1,p_2$，定义
$$I_{g,n,\beta}(\alpha_1,\dots,\alpha_n)=PD^{-1}p_{2*}\big(p_1^*(\alpha_1\otimes\cdots\otimes\alpha_n)\cap\pi_*(\xi)\big)\in H^*(\overline M_{g,n},\mathbb Q),$$
其中 $PD$ 为 Poincaré 对偶（定义 7.1.9(i)，p.206；等价的 Gysin 写法见 p.194）。

**（ii）GW 不变量（对一切 $n,g\ge 0$）。**
$$\langle I_{g,n,\beta}\rangle(\alpha_1,\dots,\alpha_n)=\int_{\xi}e_1^*\alpha_1\cup\cdots\cup e_n^*\alpha_n\in\mathbb Q$$
（定义 7.1.9(ii)，p.206；$e_i$ 的等价说法见 p.195）。

**相容性与备注。** $n+2g\ge 3$ 时 $\langle I_{g,n,\beta}\rangle(\alpha)=\int_{\overline M_{g,n}}I_{g,n,\beta}(\alpha)$（p.206）。类要求 $n+2g\ge3$（等价于 $2g-2+n\ge1$，使 $\overline M_{g,n}$ 存在且为轨形，p.192）；不变量本身对所有 $n,g\ge0$ 有定义（p.194 末）。系数取 $\mathbb Q$ 而非 $\mathbb Z$。本书注明：许多文献用 Chow 群，Behrend 用相对虚拟基本类给出类似定义（p.206）。

**本书用法。** 一律取定义 7.1.9 的口径：类取值在 $H^*(\overline M_{g,n},\mathbb Q)$、不变量取 $\mathbb Q$ 值，虚拟基本类按 p.204 的宽松记法写在粗模空间上；$\omega_X$ 一律指典范类，代入其他文献的 $c_1(TX)$ 公式时须整体反号。

## 4. 最小例子（能算出）

**设定与化简。** 取 $X=\mathbb P^2$，$\beta=d\ell$，$g=0$，$c_1(T\mathbb P^2)=3H$ 故 $\int_\beta\omega_X=-3d$。次数条件（式 (7.17) 在 $\mathbb P^2$、$g=0$ 的化简，p.215、p.220）为
$$\sum_i\deg\alpha_i=6d-2+2n .$$
取每个 $\alpha_i=[\mathrm{pt}]$（$\deg=4$）：$4n=6d-2+2n\iff n=3d-1$。于是唯一「全用点」的非平凡情形是
$$N_d:=\langle I_{0,3d-1,d}\rangle(\underbrace{[\mathrm{pt}],\dots,[\mathrm{pt}]}_{3d-1}),\qquad d\ge1$$
（p.221），其几何意义是 $\mathbb P^2$ 中过 $3d-1$ 个一般位置点的 $d$ 次有理曲线条数（p.221；「按重数计数」由齐性空间定理 p.218 保证）。

**基值与递推（Kontsevich，p.221）。** $\langle I_{0,2,1}\rangle([\mathrm{pt}],[\mathrm{pt}])=1$（过两点直线唯一），即 $N_1=1$；对 $d\ge2$，
$$N_d=\sum_{\substack{d_1+d_2=d\\ d_1,d_2>0}}N_{d_1}N_{d_2}\Big(d_1^2d_2^2\binom{3d-4}{3d_1-2}-d_1^3d_2\binom{3d-4}{3d_1-1}\Big).$$

**算 $d=2$。** 只有 $(d_1,d_2)=(1,1)$：$\binom{2}{1}=2$，$\binom{2}{2}=1$，系数 $d_1^2d_2^2=d_1^3d_2=1$，故 $N_2=1\cdot1\cdot(1\cdot1\cdot2-1\cdot1\cdot1)=1$。与书中 $N_2=1$ 一致。

**算 $d=3$（具体数字）。** 两项：
- $(d_1,d_2)=(1,2)$：$d_1^2d_2^2=4$，$\binom{5}{3\cdot1-2}=\binom51=5$，$d_1^3d_2=2$，$\binom{5}{3\cdot1-1}=\binom52=10$，贡献 $1\cdot(4\cdot5-2\cdot10)=20-20=0$；
- $(d_1,d_2)=(2,1)$：$d_1^2d_2^2=4$，$\binom{5}{4}=5$，$d_1^3d_2=8$，$\binom{5}{5}=1$，贡献 $1\cdot(20-8)=12$。

相加得 $N_3=0+12=\mathbf{12}$，即 $\mathbb P^2$ 中过 8 个一般位置点的 3 次有理曲线有 **12** 条（= 平面三次曲线 Severi 簇的次数），与 p.221 列出的 $N_1,\dots,N_5=1,1,12,620,87304$ 一致。检验链条：$d=3$ 时 $n=3d-1=8$，$\sum\deg\alpha_i=8\cdot4=32$，右端 $6\cdot3-2+2\cdot8=18-2+16=32$ ✓。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|------|------------------|------|
| 1 | 次数公理：$\deg I_{g,n,\beta}(\alpha)=2(g-1)\dim X+2\int_\beta\omega_X+\sum_i\deg\alpha_i$；最高次条件式 (7.17)：$\sum_i\deg\alpha_i=2(1-g)\dim X-2\int_\beta\omega_X+2(3g-3+n)$ | p.215 | 固定 $(g,n,\beta)$ 后只有有限个次数组合可能非零；$\omega_X=K_X$（p.194） |
| 2 | 除子公理：$\alpha_n\in H^2(X,\mathbb Q)$ 时 $\pi_{n!}I_{g,n,\beta}(\dots,\alpha_n)=\big(\int_\beta\alpha_n\big)I_{g,n-1,\beta}(\dots)$，其中 $\pi_n:\overline M_{g,n}\to\overline M_{g,n-1}$ 为忘却最后一点；对不变量在最高次条件成立时同样成立 | p.216 | 反复插入 $H^2$ 类可把不变量降到 $N_d$；五次三维簇上即 $\langle I_{0,n,d}\rangle(H,\dots,H)=d^nN_d$（p.224） |
| 3 | 分裂公理：$g=g_1+g_2$、$n=n_1+n_2$（$n_i+2g_i\ge2$）时 $\varphi^*I=\sum_{\beta_1+\beta_2=\beta}\sum_{i,j}g^{ij}I(\dots,T_i)\otimes I(T_j,\dots)$，$\varphi:\overline M_{g_1,n_1+1}\times\overline M_{g_2,n_2+1}\to\overline M_{g,n}$ | p.217 | 与约化公理合称复合律（Ruan–Tian）；量子上同调结合律的代数来源 |
| 4 | 形变公理：光滑固有族 $\mathcal X\to T$（$T$ 连通），$\beta_t,\alpha_i$ 为局部常值截面时 $I^{X_t}_{g,n,\beta_t}(\alpha)$ 不随 $t$ 改变 | p.217 | 对应 SY01-24 命题 3.12；相邻纤维间 $\beta$ 沿路径平行移动，在单值性下确定 |
| 5 | 基本类公理：$n+2g\ge4$ 时 $I_{g,n,\beta}(\alpha_1,\dots,\alpha_{n-1},[X])=\pi_n^*I_{g,n-1,\beta}(\alpha_1,\dots,\alpha_{n-1})$，故不变量满足 $\langle I_{g,n,\beta}\rangle(\dots,[X])=0$；有效性：$\beta$ 非有效（或辛侧 $\int_\beta\omega<0$）时 $I=0$ | p.215–216 | 插入 $[X]$ 不施加条件，故不增条件地提升 $n$；退化情形用来筛选可能非零的不变量 |
| 6 | 树级重构定理：$X$ 光滑射影、$H^*(X,\mathbb Q)$ 由 $H^2$ 生成；若已知所有 $-\int_\beta\omega_X\le\dim X+1$ 且 $\deg\alpha_3=2$ 的 $\langle I_{0,3,\beta}\rangle$，则全部树级 GW 类被确定 | p.219–220（Kontsevich–Manin） | $\mathbb P^2$ 时只需 $\langle I_{0,3,1}\rangle([\mathrm{pt}],[\mathrm{pt}],[\ell])=1$（p.220）即可生成一切 $N_d$ |

## 6. 推导流程（D1…Dn）

- **D1｜从「曲线集合」到「带标记映射」。** 朴素问题数的是 $C\subset X$ 的条数（式 (7.1)，p.190）；Kontsevich 的观察是改成 $(C,p_1,\dots,p_n)$ 加映射 $f:C\to X$，条件为 $f_*[C]=\beta$、$f(p_i)\in Z_i$（式 (7.3)，p.192）。依据：p.190–192。
- **D2｜模空间。** 稳定映射的定义（4 条稳定性条件）与稳定映射族的定义使函子 $S\mapsto\{$纤维稳定、亏格 $g$、类 $\beta\}$ 可表：$X$ 射影时它有射影粗模空间（p.192），并有固有代数叠结构（p.193，Kontsevich 陈述、Behrend–Manin 证明）。依据：p.192–193。
- **D3｜结构映射与遗忘。** 由极限分割得 $\pi_1:\overline{\mathcal M}_{g,n}(X,\beta)\to X^n$ 与 $\pi_2\to\overline M_{g,n}$；$n+2g\ge3$ 时收缩不稳定分支（Knudsen）使 $\pi_2$ 存在（p.193–194）。依据：p.194。
- **D4｜预期维数。** 稳定映射的切—障碍复形给出 $\dim^{\exp}=\dim\mathrm{Ext}^1-\dim\mathrm{Ext}^2$（长度为 2、完美障碍理论的 Euler 特征），Hirzebruch–Riemann–Roch 算得 $\chi(f^*\Theta_X)=-\int_\beta\omega_X+(1-g)\dim X$，从而得 p.194 的 $\dim^{\exp}=(1-g)(\dim X-3)-\int_\beta\omega_X+n$。依据：p.197–198（推导），p.194（结论）。
- **D5｜虚拟基本类。** 对完美障碍理论（Li–Tian 的切—障碍复形或 Behrend–Fantechi 的完美障碍理论）用内蕴法锥构造 $\xi$，其次数等于预期维数；模空间实际维数可大于预期，故一般 $\xi\ne[\overline M]$。依据：p.199–203；凸簇情形的特例见 p.203。
- **D6｜类与不变量。** 用 $\xi$ 代替普通基本类代入 Gysin/推前公式，得定义 7.1.9 的 (i)(ii)；$n+2g\ge3$ 时两者由投影公式相容。依据：p.194–195（用 $\xi$ 改写的推前公式与赋值映射公式），p.206（定义 7.1.9）。
- **D7｜公理验证。** 代数侧（Behrend–Manin、Li–Tian、Behrend–Fantechi、Behrend）与辛侧（Ruan–Tian 等）分别验证 §7.3 的公理；两类定义的比较在可迁线性群作用情形由 p.218 定理给出 $\langle I\rangle^{\mathrm{LRT}}=\langle I\rangle^{\mathrm{BFS}}$。依据：p.214–218。
- **D8｜可计算性（$\mathbb P^2$）。** 取 $\xi=I_{0,3d,d}([\mathrm{pt}]^{\times(3d-2)},[\ell],[\ell])\in H^*(\overline M_{0,3d})$（次数 $2\dim\overline M_{0,3d}-2$），用遗忘映射 $\varphi:\overline M_{0,3d}\to\overline M_{0,4}\cong\mathbb P^1$ 把三个边界点的线性等价拉回（p.221–222），再与 $\xi$ 相交并用分裂公理（对角线类 $\Delta=[\mathrm{pt}]\otimes[\mathbb P^2]+[\ell]\otimes[\ell]+[\mathbb P^2]\otimes[\mathrm{pt}]$）化为 $N_d$ 与 $N_{d_1}N_{d_2}$ 的等式，即 §4 的递推。依据：p.221–223。
- **D9｜可计算性（CY 三维簇）。** 亏格零 GW 不变量完全由 $N_\beta=\langle I_{0,0,\beta}\rangle$ 与交数决定（除子公理），而 $N_\beta$ 化为 $\int_{\overline M_{0,0}(\mathbb P^4,d)}c_{5d+1}(\mathcal V_d)$；多重覆盖使 $N_d=\sum_{k\mid d}n_{d/k}k^{-3}$，须先扣掉才能得曲线数。依据：p.224–226。
- **D10｜去向。** 三点不变量给出量子乘积（第 8 章），等变版本与引力关联数在 p.219 提一句（第 9、10 章），镜像比较在第 11 章。依据：p.191、p.219。

## 7. 常见误解与反例（≥2）

- **误解 1：GW 不变量就是曲线条数。** 反例：本书 p.191 明说 GW 不变量可以是分数甚至负数；五次三维簇上 $N_d$ 与真实曲线数 $n_d$ 相差多重覆盖：$N_d=\sum_{k\mid d}n_{d/k}k^{-3}$（p.225–226）。只有在齐性空间且插入圈取一般位置时（p.218 定理）它才严格等于按重数计的带标记映射数。
- **误解 2：$\xi$ 就是模空间的普通基本类 $[\overline M_{g,n}(X,\beta)]$。** 反例：Fermat 五次 $V$ 上 $\overline M_{0,0}(V,\ell)$ 由一个 50 分支的单参数族（维数 1）与 375 条孤立直线（维数 0）组成，而预期维数为 0；普通基本类连次数都不对，虚拟基本类给出零圈与 $\langle I_{0,0,\ell}\rangle=20\cdot50+5\cdot375=2875$（p.196–197）。仅当 $X$ 为凸簇（p.203：射影空间、齐性空间）才有 $\xi=[\overline M]$。
- **误解 3：$n+2g<3$ 时 GW 不变量没有定义。** 反例：只有 GW **类**要求 $n+2g\ge3$（$M̄_{g,n}$ 须为维数 $3g-3+n$ 的轨形，p.192）；不变量对所有 $n,g\ge0$ 有定义（p.194 末、定义 7.1.9(ii)），如 $\langle I_{0,0,\ell}\rangle=2875$（$n=g=0$）与 $\langle I_{0,2,1}\rangle([\mathrm{pt}],[\mathrm{pt}])=1$（p.221）。
- **误解 4：各种定义已被证明等价。** 事实：代数侧 Li–Tian 与 Behrend–Fantechi/Behrend 的构造「应等价，但证明尚未写出」（p.218）；已证的是 LTi4：LTi2=LTi3、Siebert2：Behrend=Siebert1，以及可迁线性群作用（如 $\mathbb P^2$）时 LRT=BFS（p.218 定理）。一般情形的等价仍开放，故本书 p.191 称「Gromov–Witten 不变量」是对记号的宽松使用。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|------|------|----------------|
| Cox–Katz（本书） | 定义 7.1.9（p.206）；§7.1 构造 p.190–206；§7.3 公理 p.214–218；§7.4.2 p.220–223 | 主定义（GW 类与 GW 不变量双轨陈述）与全部公理；本卡 §3–§6 的出处 |
| SY01-24《镜像对称》（Siebert 讲义中译本） | 第 3 章（Gromov–Witten 理论），小节「Gromov–Witten 不变量」源码 `ch03.tex:381–408`（含障碍理论、定义式 3.117、形变不变性命题 3.12） | 同一定理体系（障碍理论→虚拟类→不变量→形变不变性）。**冲突：** 其虚拟类取值在 Chow 群 $A_d$ 而非 $H^*(-,\mathbb Q)$，且定义多一个插入 $\gamma\in H^*(\overline M_{g,k})$（把 GW 类与 $\gamma$ 配对）；本书 p.206 只注明许多文献用 Chow 群，未证两套表述等价。其「单值变换」按 _冲突表 T1 裁定为「单值性」 |
| SY01-25《同调镜像对称与环面纤维化》 | 资料卡 `04-术语文献勘误.md` 的术语表与文献表 | 不处理 GW 不变量（主题为 HMS/SYZ）。**冲突：** 其文献表用缩写 [GW] 指 **Gross–Wilson**（K3 的独立验证），不是 Gromov–Witten；引用时勿混 |
| Kontsevich–Manin 1994（[KoM1]） | 本书 p.214–218（公理体系）、p.219–220（树级重构定理）转述 | GW 类公理的原始出处，定义了线性/有效/次数/等变/基本类/除子/点映射/分裂/约化/形变/动机公理 |
| Li–Tian；Behrend–Fantechi（[LTi2]、[BF]） | 本书 p.199–203（构造）、p.214、p.218（等价性讨论） | 虚拟基本类的两套构造：完美切—障碍复形与完美障碍理论；p.218 说二者「应等价但证明尚未写出」 |
| Kontsevich 1995（[Kontsevich2]） | 本书 p.207（例题 7.1.6.1 首见） | 首次用稳定映射计算五次三维簇的 GW 不变量 $\langle I_{0,0,d\ell}\rangle=\int_{\overline M_{0,0}(\mathbb P^4,d)}c_{5d+1}(\mathcal V_d)$；§2.2 |

## 9. 前置与后继

- **前置（本卡默认已会）：** MS-16 预稳定曲线与 $\overline M_{g,n}$（含 $\overline M_{0,4}\cong\mathbb P^1$ 的三边界点线性等价，p.221–222 直接用）；MS-15 稳定映射与虚拟基本类（$\xi$ 的构造、次数等于预期维数、p.204 宽松记法、p.203 凸簇特例）。
- **后继（用本卡）：** MS-04 量子上同调（三点不变量给量子乘积，p.190、p.219）；MS-17 局部化与等变上同调（用来算 $\int c_{5d+1}(\mathcal V_d)$ 一类积分）；MS-18 Frobenius 流形与关联函数；MS-19 量子超平面截面（相对 GW 不变量）；MS-01 镜像对称（比较 A/B 关联函数，依赖形变公理 p.217）。
- **上游依赖关系：** MS-15 依赖 MS-16；本卡与 MS-17 共享「虚拟基本类的可计算性」这一前提。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- MS-05 形式化接口（签名级；证明体一律可 sorry）
-- 依据：定义 7.1.9（p.206）、公理表（p.214–218）
variable (X : Type) [SmoothProjectiveVariety X]
variable (Mbar : ℕ → ℕ → H₂ X ℤ → Type)   -- M̄_{g,n}(X,β)（模叠或粗模空间）
variable (MbarCurve : ℕ → ℕ → Type)        -- M̄_{g,n}

-- 虚拟基本类；其次数 =(1-g)(dim X - 3) - ∫_β ω_X + n（p.194）
axiom virtualFundamentalClass (g n : ℕ) (β : H₂ X ℤ) : H_* (Mbar g n β) ℚ

-- GW 类：仅当 n + 2g ≥ 3（定义 7.1.9(i)，p.206）
noncomputable def gwClass (g n : ℕ) (β : H₂ X ℤ) (h : 3 ≤ n + 2 * g)
    (α : Fin n → H^*(X, ℚ)) : H^*(MbarCurve g n, ℚ) := sorry

-- GW 不变量：所有 n, g ≥ 0（定义 7.1.9(ii)，p.206）
noncomputable def gwInvariant (g n : ℕ) (β : H₂ X ℤ)
    (α : Fin n → H^*(X, ℚ)) : ℚ := sorry

-- 相容性：n + 2g ≥ 3 时 ⟨I⟩ = ∫_{M̄_{g,n}} I（p.206）
theorem gwInvariant_eq_integral (g n : ℕ) (β : H₂ X ℤ) (h : 3 ≤ n + 2 * g)
    (α : Fin n → H^*(X, ℚ)) : gwInvariant g n β α = sorry := sorry

-- 公理（p.215–217）：次数、有效性、除子、分裂、形变，逐条留 sorry
theorem gw_degree_axiom : sorry := sorry
theorem gw_divisor_axiom : sorry := sorry
theorem gw_splitting_axiom : sorry := sorry
theorem gw_deformation_axiom : sorry := sorry
```

## 11. 待核清单

- [ ] **[GW] 缩写冲突：** SY01-25 文献表用 [GW] 指 Gross–Wilson，不是 Gromov–Witten；需在术语表统一或禁止裸用，待 lead 确认后同步 `_冲突表.md`。
- [ ] **SY01-24 定义差异：** 其第 3 章用 Chow 群 $A_d$ 中的虚拟类并多一个 $\gamma$ 插入，与本书定义 7.1.9（$H^*(-,\mathbb Q)$、无 $\gamma$）是否只差记号/取值范畴；本书 p.206 仅注明「许多文献用 Chow 群」，未证两套表述等价。
- [ ] **SY01-24 术语表缺条：** 70 条中无「Gromov–Witten 不变量」，仅有 stable map #31、virtual fundamental class #32、expected dimension #43；是否补录待定。
- [ ] **原始文献精确定位：** Kontsevich–Manin 1994 公理所在定理号、Li–Tian（JAMS 11, 1998）与 Behrend–Fantechi（Invent. Math. 128, 1997）的具体定理号；本书只给 [KoM1]/[LTi2]/[BF] 标签，卷期页码未核。
- [ ] **$\omega_X$ 符号约定：** 本书取典范类（$\int_\beta\omega_X=-\int_\beta c_1(TX)$，p.194、p.210），多数文献用 $c_1(TX)$；跨文献套公式须换算（附录 C p.325 译注亦提到原文未交代 $\omega_X$）。
- [ ] **记号漂移：** 第 7 章用 $N_d$ 记 A 模型 GW 数，第 11 章改用 $K_d$ 并把 $N_d$ 移作 GLSM 射影空间齐次式元组数（译注 u117，PDF p.355）；跨章引用须核对。
- [ ] **宽松记法：** p.195、p.204 混用 $[\overline M_{g,n}(X,\beta)]^{\mathrm{virt}}$ 与 $[\overline{\mathcal M}_{g,n}(X,\beta)]^{\mathrm{virt}}$（校订记录第 111 条）；若 MS-15 统一记号，本卡需同步。
- [ ] 上述条目待同步至 `_冲突表.md` 第三节；本轮受「禁止改写既有文件」约束未写入。
