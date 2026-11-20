---
id: MS-12
zh: 单值性与最大幺幂
en: monodromy and maximally unipotent
aliases: [单值性, 最大幺幂单值性, 最大幺幂边界点, MUM 点]
layer: L1
prereqs: [MS-11]
sources:
  - "A 级：Cox–Katz 1999, §5.1.3, p.75（PDF p.98）——单值性变换的定义与单值性定理 [Landman]"
  - "A 级：Cox–Katz 1999, §5.1.4–5.1.5, p.75–78（PDF p.98–101）——式 (5.3)(5.4)(5.5)(5.6)"
  - "A 级：Cox–Katz 1999, §5.2.1–5.2.2, p.78–82（PDF p.101–105）——命题 5.2.1、定义 5.2.2、式 (5.7)(5.9)(5.12)"
  - "A 级：Morrison 1993, Astérisque 218, 243–271 [Morrison3]——定义 5.2.2 的来源（PDF p.104）"
  - "A 级：Landman 1973, Trans. AMS 181, 89–126 [Landman]——单值性定理（PDF p.98）"
  - "B 级：SY01-24（Siebert 讲义中译本）第 1 章，原书 p.20–21——PF 方程基本解与 N=T−I 的显式链"
status: draft
review:
  drafter: agent-227
  reviewer: lead
  blindtest: pending
glossary_refs: [monodromy, maximally unipotent monodromy, monodromy weight filtration, Picard–Lefschetz transformation, nilpotent orbit theorem]
symbols_refs: ['$T$', '$N=\log T$', '$W_\bullet$', '$m_{ij}$', '$y_k$']
updated: 2026-11-20
---

# MS-12 单值性与最大幺幂

## 1. 一句话

周期绕过边界点时怎么变、镜像映射起点是否成立，就看它。

## 2. 为什么需要它

1. **给镜像映射定起点。** 镜像对称要在「大复结构极限」处取 A 模型坐标；本书把这个极限点写成最大幺幂边界点（定义 5.2.2，PDF p.104），要求存在唯一全纯周期 $y_0$ 与 $r$ 个对数周期 $y_k$。没有最大幺幂性，$y_k/y_0$ 所定义的镜像映射无从谈起（PDF p.105）。
2. **把「算」降成「判」。** 直接解析延拓求单值性矩阵几乎不可行；命题 5.2.1 把 1 维模情形的最大幺幂性翻译为 Picard–Fuchs 方程指标方程的根条件（PDF p.102），于是只需读方程系数，不必解方程。
3. **为权滤过与混合 Hodge 结构供料。** 最大幺幂性使 $N=\log T$ 的单值性权滤过 (5.4) 退化成 Hodge–Tate 型（式 (5.10)–(5.11)，PDF p.103），这是 MS-13（极限混合 Hodge 结构）与 MS-06（PF 方程）之间的桥。
4. **支撑整性陈述。** 定义 5.2.2 里的矩阵 $(m_{ij})$ 给出镜像侧交数矩阵，其整性猜想 [Morrison6] 只在最大幺幂点处提起（PDF p.105）。

## 3. 定义（全假设）

**假设。**
(H1) $X\to S$ 是光滑射影族，$\dim X=d$，$S$ 光滑；单值性用局部系统 $H^n(X_t,\mathbb C)$ 描述，$n=d$（主要情形 $d=n=3$）。
(H2) 有光滑紧化 $\bar S$，边界 $D=\bar S-S$ 是正规交叉除子，$p=D_1\cap\cdots\cap D_r$ 是 $D$ 的 0 维 strata，且 $\dim\bar S=r$（局部坐标 $z_1,\dots,z_r$，$D_i=\{z_i=0\}$）。
(H3) 取小多圆盘 $\Delta^r$ 与去心 $\Delta^{*r}$，基点 $t_0\in\Delta^{*r}$；$T_i$ 是沿绕 $D_i$ 的小回路 $\gamma_i$ 解析延拓给出的 $H^n(X_{t_0},\mathbb C)$ 自同构。书中称单值性变换，亦称 Picard–Lefschetz 变换（PDF p.98）；其共轭类只依赖 $D_i$，不依赖回路与基点。
(H4) 只处理 $T_i$ 幺幂的情形。单值性定理只给拟幺幂 $(T_i^m-I)^{n+1}=0$（PDF p.98），故一般需取有限覆叠 $z_i=w_i^m$ 使 $T_i^m$ 幺幂；书中直接假设各 $T_i$ 幺幂后再取对数（PDF p.98）。

**定义 3.1（单值性算子）。** 每个 $T_i$ 如上（H3）。本文把 $T_i$ 本身称单值性算子，把 $\langle T_1,\dots,T_r\rangle$ 称单值群——两者必须区分，见《_冲突表》U2。

**定义 3.2（幺幂 / 最大幺幂，1 维模）。** 设 $r=1$，$T=T_1$，$n=3$，$\dim H^3=4$。称 $T$ 幺幂，若 $T-I$ 幂零；此时
$$N=\log T:=\sum_{k\ge1}\frac{(-1)^{k+1}}{k}(T-I)^k$$
幂零且 $\exp N=T$。称 $T$ 最大幺幂，若 $T$ 幺幂且 $(T-I)^3\ne0$（等价地 $N^3\ne0$）。由 (H4) 的 $(T^m-I)^4=0$ 与幺幂性得 $(T-I)^4=0$，故最大幺幂等价于幂零指数恰为 $4=n+1$（PDF p.101）。一般 $d$ 维写法：$N^d\ne0$ 且（由单值性定理）$N^{d+1}=0$（PDF p.105）。

**定义 3.3（最大幺幂边界点，$r$ 维模）。** 设 $N_i=\log T_i$ 幂零，取 $a_i>0$，$N=\sum_i a_iN_i$，令 $W_\bullet$ 为 $N$ 的单值性权滤过 (5.4)：
$$W_0=\operatorname{im}(N^n),\quad W_1=\operatorname{im}(N^{n-1})\cap\ker N,\quad W_2=\operatorname{im}(N^{n-2})\cap\ker N+\operatorname{im}(N^{n-1})\cap\ker(N^2),\ \dots,\quad W_{2n-1}=\ker(N^n),\quad W_{2n}=H^n .$$
称 $p$ 为**最大幺幂边界点**，若：
(i) 各 $T_i$ 幺幂；
(ii) 对任意正 $a_i$，上述 $W_\bullet$ 满足 $\dim W_0=\dim W_1=1$、$\dim W_2=1+r$；
(iii) 存在 $W_2$ 的基 $g_0,\dots,g_r$（$g_0$ 张成 $W_0$）与可逆矩阵 $(m_{ij})$，使 $N_i(g_j)=m_{ij}g_0$（PDF p.104）。
$r=1$ 时定义 3.3 与定义 3.2 等价（即 $N^d\ne0$ 判据，PDF p.105，[Morrison2]）。

**本书用法。** 本书单值性算子记作 $\mathcal T$，$N=\log T$ 而**不是** $T-I$；§5.1.3 的「单值性变换」就是 $T_j$ 本身。术语按本书作「单值性」（不写单值化、单值变换），SY01-24 作「单值变换」，见 §8 冲突行。

## 4. 最小例子（能算出）

**设定。** 五次超曲面镜像族 $X_\psi\subset\mathbb P^4$，$z=\psi^{-5}$，其 Picard–Fuchs 方程为 (5.12)（PDF p.104）：
$$(1+5^5z)\delta^4y+2\cdot5^5z\,\delta^3y+7\cdot5^4z\,\delta^2y+2\cdot5^4z\,\delta y+24\cdot5z\,y=0,\qquad \delta=z\frac{d}{dz}.$$
$h^{2,1}=1\Rightarrow h^3=2(h^{3,0}+h^{2,1})=2(1+1)=4$（PDF p.101）。$z=0$ 处指标方程为 $\lambda^4=0$，故该点单值性 $T$ 最大幺幂（命题 5.2.1，PDF p.102）。按式 (5.7) 的基写 $T$（PDF p.101）：
$$T=I+E,\qquad E=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\0&0&0&0\end{pmatrix},\qquad E^4=0,\quad E^3=\begin{pmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}\neq0.$$
故 $(T-I)^3=E^3\ne0$、$(T-I)^4=0$：幂零指数为 $4=n+1$，$T$ 最大幺幂（PDF p.101）。逐项计算：
(I) 对数
$$N=\log T=E-\tfrac12E^2+\tfrac13E^3=\begin{pmatrix}0&1&-\frac12&\frac13\\0&0&1&-\frac12\\0&0&0&1\\0&0&0&0\end{pmatrix},\quad N^2=E^2-E^3,\quad N^3=E^3,\quad N^4=0 .$$
(II) 校验 $\exp N=T$：$\exp N=I+N+\tfrac12N^2+\tfrac16N^3=I+E+\left(-\tfrac12+\tfrac12\right)E^2+\left(\tfrac13-\tfrac12+\tfrac16\right)E^3=I+E$，因为 $\tfrac13-\tfrac12+\tfrac16=0$。
(III) 绕 $k$ 周：$T^k=I+kE+\binom{k}{2}E^2+\binom{k}{3}E^3$。取 $k=5$：$T^5=\begin{pmatrix}1&5&10&10\\0&1&5&10\\0&0&1&5\\0&0&0&1\end{pmatrix}$，即 $g_3\mapsto g_3+5g_2+10g_1+10g_0$，从而 $y_3\mapsto y_3+5y_2+10y_1+10y_0$；绕行时 $\frac{\log z}{2\pi i}\mapsto\frac{\log z}{2\pi i}+1$，与渐近式 $y_i\sim\frac{c}{i!}\left(\frac{\log z}{2\pi i}\right)^i$（PDF p.102）所示的对数增长相符。
(IV) 权滤过（$n=3$）：$\ker N=\langle g_0\rangle$，$\operatorname{im}N^k=\langle g_0,\dots,g_{3-k}\rangle$，算出 $\dim W_\bullet=(1,1,2,2,3,3,4)$，故 $W_{2k}=W_{2k+1}$（式 (5.11)，PDF p.103），且 $\dim W_2=2=1+r$（$r=1$），定义 3.3(ii) 成立。
(V) 留数：指标方程 $\lambda^4$ 的系数全零，即 $f_1(0)=\cdots=f_4(0)=0$，由 (5.9)（PDF p.102）得 $\operatorname{Res}(\nabla)=E$；于是 $T$ 与 $\exp(-2\pi iE)=I-2\pi iE-2\pi^2E^2+\tfrac{4\pi^3i}{3}E^3$ 共轭（式 (5.5)，PDF p.100）。后者特征值全为 $1$、只有一个 $4$ 阶 Jordan 块，确与 $T=I+E$ 同型。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
| 1 | 单值性定理：存在整数 $m>0$ 使 $(T_j^m-I)^{n+1}=0$，故 $T_j$ 拟幺幂、特征值为单位根 | PDF p.98，[Landman] | 只给拟幺幂；幺幂需假设或取有限覆叠（H4） |
| 2 | 留数判据：$\exp(-2\pi i\operatorname{Res}(\nabla))$ 与 $T$ 共轭；$T$ 幺幂 $\iff$ $\operatorname{Res}(\nabla)$ 幂零；$\operatorname{Res}$ 特征值 $\lambda$ 有理且 $0\le\lambda<1$ | PDF p.100，式 (5.5)，[Deligne1] | 是连接 PF 方程与单值性的枢纽 |
| 3 | 命题 5.2.1：(i) $T$ 幺幂 $\iff$ 指标方程根全为整数；(ii) 1 维模时 $T$ 最大幺幂 $\iff$ 指标方程对某整数 $\ell$ 为 $(\lambda-\ell)^4=0$ | PDF p.102 | 证明用友矩阵 (5.9)，反方向用 (5.10)–(5.11) |
| 4 | 最大幺幂 $\iff$ $(T-I)^3\ne0$ 且 $(T-I)^4=0$（等价地 $N^3\ne0$、$N^4=0$）；此时 $N^3\Omega(0)\ne0$ | PDF p.101、p.103 | $n=3$、$\dim H^3=4$ 的情形；一般 $d$ 维为 $N^d\ne0$ |
| 5 | 权滤过性质：$N(W_k)\subset W_{k-2}$；$N^k:W_{n+k}/W_{n+k-1}\xrightarrow{\sim}W_{n-k}/W_{n-k-1}$；$F_{\lim}$ 使 $(W_\bullet,F_{\lim})$ 成为混合 Hodge 结构 | PDF p.99，式 (5.4) | 最大幺幂时退化为 Hodge–Tate（$W_{2k}=W_{2k+1}$，PDF p.103） |
| 6 | $r$ 维定义 5.2.2：$\dim W_0=\dim W_1=1$、$\dim W_2=1+r$、$(m_{ij})$ 可逆，于是有唯一全纯解与 $r$ 个对数解；$N^d:W_{2d}/W_{2d-1}\cong W_0$ 故 $N^d\ne0$ | PDF p.104–105，[Morrison3]；[Morrison2] | $r=1$ 时定义 5.2.2 $\iff$ $N^d\ne0$ |

## 6. 推导流程（D1…Dn）

**D1（读指标方程）。** 正则奇点方程 $\delta^my+f_1\delta^{m-1}y+\cdots+f_my=0$ 的指标方程为 $\lambda^m+f_1(0)\lambda^{m-1}+\cdots+f_m(0)=0$，解按 $z^\lambda$ 展开（式 (5.6)，PDF p.100–101）。
**D2（化一阶系统、留数替换单值性）。** 以 $(\Omega,\nabla_\delta\Omega,\dots,\nabla_\delta^{m-1}\Omega)$ 为基，$z=0$ 处联络矩阵的留数 $\operatorname{Res}(\nabla)$ 是友矩阵 (5.9)；$T$ 与 $\exp(-2\pi i\operatorname{Res}(\nabla))$ 共轭，且 $T$ 幺幂 $\iff$ $\operatorname{Res}(\nabla)$ 幂零（式 (5.5)，PDF p.100，[Deligne1]）。
**D3（指标根 = 留数特征值）。** 由 D2 的友矩阵形状，$\lambda$ 是指标根 $\iff$ $\lambda$ 是 $\operatorname{Res}(\nabla)$ 的特征值（PDF p.102）。于是 $T$ 幺幂 $\iff$ 指标根全为整数，得命题 5.2.1(i)。
**D4（最大性 = 幂零指数最大）。** $\dim H^3=4$，单值性定理给 $(T-I)^4=0$；$N=\log T$ 与 $T-I$ 都是 $T-I$ 的无常数项多项式，幂零指数相同，故最大幺幂 $\iff$ $(T-I)^3\ne0$ $\iff$ $N^3\ne0$（PDF p.101）$\iff$ $\operatorname{Res}(\nabla)$ 是单个 4 阶零 Jordan 块 $\iff$ 指标方程 $(\lambda-\ell)^4=0$，得命题 5.2.1(ii)（PDF p.102）。
**D5（反方向：权滤过对齐）。** 仅知 $(T-I)^3\ne0$ 只说明某个解增长如 $(\log z)^3$；要证指标根四重，须把 $N^3\ne0$ 与 $F_{\lim}$ 对齐：取 $W_6=H^3$、$W_5=\ker N^3$，由 $\dim(W_6/W_5)=1$ 得 $F^3_{\lim}\oplus W_5=H^3$（式 (5.10)）从而 $N^3\Omega(0)\ne0$；再用 $\nabla_\delta^j\Omega(0)=(-1/2\pi i)^jN^j\Omega(0)\bmod F^{4-j}_{\lim}$（式 (5.3)，PDF p.99）读出 $\nabla_\delta^j\Omega$ 的零点阶，得指标根全等于同一整数 $\ell$（PDF p.103）。
**D6（极限 Hodge 结构）。** 同一步还给出 $W_{2k}=W_{2k+1}$ 与 $F^p_{\lim}\oplus W_{2p-1}=F^p_{\lim}\oplus W_{2p-2}=H^3$（式 (5.11)），即 Hodge–Tate 型：最大幺幂点处极限 Hodge 结构退化到最简（PDF p.103）。
**D7（多参数）。** $r=h^{d-1,1}>1$ 时单个 $N_i$ 的幂零指数可能不够（例 5.4.2 中 $N_2^2=0$），故定义 5.2.2 改用正组合 $N=\sum a_iN_i$ 的权滤过，并要求 $\dim W_0=\dim W_1=1$、$\dim W_2=1+r$ 以及 $g_j$ 使 $N_i(g_j)=m_{ij}g_0$（PDF p.104）。
**D8（判据几何化）。** $N^d:W_{2d}/W_{2d-1}\xrightarrow{\sim}W_0$，故 $N^d\ne0$；配合单值性定理 $N^{d+1}=0$，$r=1$ 时定义 5.2.2 $\iff$ $N^d\ne0$（PDF p.105，[Morrison2]）。
**D9（镜像侧读法）。** 换基 $g_k'=\sum_jg_jm^{jk}$（$(m^{jk})=(m_{jk})^{-1}$）使 $N_j(g_k')=\delta_{jk}g_0$，则 $y_k=y_0\frac{\log z_k}{2\pi i}+\text{全纯}$，此即镜像映射坐标；$g_0$ 对应点类、$g_i$ 对应曲线类，(m_{ij}) 对应交数矩阵 $(-T_i\cdot C_j)$（PDF p.105）。

## 7. 常见误解与反例（≥2）

1. **误解「$N=T-I$」。** 本书 §5.1.4 起一律 $N_j=\log T_j$（PDF p.98），式 (5.3) 的常数 $-1/(2\pi i)$ 与定义 5.2.2(iii) 都按 $\log$ 写；SY01-24 式 (1.86) 则记 $N=T-I$。两者幂零指数相同，但矩阵不同：对 §4 的 $T=I+E$，$T-I=E$ 而 $\log T=E-\frac12E^2+\frac13E^3$，$(2,3)$ 元分别为 $0$ 与 $-1/2$。
2. **误解「幺幂就是最大幺幂」。** 五次族在 $z=-5^{-5}$ 处指标根为整数，$T$ 幺幂，但不是最大（可证 $N^2=0$）；在 $z=\infty$（$w=1/z$）指标根为 $\{1/5,2/5,3/5,4/5\}$，甚至不是幺幂（PDF p.104）。
3. **误解「$r$ 维多参数时逐个 $T_i$ 幺幂就够了」。** 加权五次 $P(1,1,2,2,2)$（$h^{2,1}=2$，$\dim H^3=6$）中 $N_2^2=0$，用 $N_2$ 单独定义的权滤过不满足定义 5.2.2；必须用正组合 $a_1N_1+a_2N_2$（其三次方 $\ne0$）（PDF p.113，印刷 p.90）。且 $z_1=z_2=0$ 是最大幺幂点，$D_1\cap D_2$ 的其他交点不是。
4. **误解「最大幺幂性可以直接从方程系数读出，与规范/截面无关」。** 规范变换 $\Omega'=g\Omega$（$g=a_\ell z^\ell+\cdots$）把指标根整体平移 $\ell$（PDF p.101），故「指标方程 $=(\lambda-\ell)^4$」中的 $\ell$ 依赖规范；不变量是 $T$ 及其 $\log$ 的幂零结构。方程系数只是判据，不是定义。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
| Cox–Katz 1999 | §5.1.3，PDF p.98（印刷 p.75） | 用绕 $D_j$ 的回路定义单值性变换 $T_j$，陈述单值性定理 $[Landman]$：$(T_j^m-I)^{n+1}=0$ |
| Cox–Katz 1999 | §5.1.4–5.1.5，PDF p.98–101（印刷 p.75–78） | 式 (5.3) $\bar\nabla_{\delta_j}=-(1/2\pi i)N_j$；权滤过 (5.4)；留数 (5.5) 与指标方程 (5.6) |
| Cox–Katz 1999 | §5.2.1–5.2.2，PDF p.101–105（印刷 p.78–82） | 1 维模判据 (5.7)(5.9)、命题 5.2.1、五次例 (5.12)；$r$ 维定义 5.2.2（引 [Morrison3]）与 $N^d$ 判据 |
| Cox–Katz 1999 | §5.4 例 5.4.2，PDF p.112–113（印刷 p.89–90） | $P(1,1,2,2,2)$：$N_2^2=0$、只有正组合才定义出所需权滤过的书内反例 |
| SY01-24（Siebert 讲义中译本） | 第 1 章，原书 p.20–21；式 (1.76)、(1.81)–(1.86) | 显式给出 $N=T-I$ 与链 $\alpha_0\mapsto\alpha_1\mapsto\beta_1\mapsto\beta_0\mapsto0$（$N^3\ne0$、$N^4=0$），条件同本书但未用「最大幺幂」之名。**冲突**：术语表 #18 作「单值变换」monodromy，本书作「单值性」（《_冲突表》T1）；且其 $N=T-I$ 与本书 $N=\log T$ 不同（U2） |
| SY01-25（同调镜像对称与环面纤维化） | 资料卡 01-结果清单 命题 1（p.13）；04-术语文献勘误「极大退化」「[LTY] 极大单值」 | 用 $(T-\mathrm{Id})^nv\ne0$、$(T-\mathrm{Id})^{n+1}v=0$ 刻画 $q=0$ 处「极大退化」。**冲突**：名称作「极大退化/极大单值」而非本书「最大幺幂」，且只在 $q=0$、1 维情形陈述，未涉及定义 5.2.2 的 $W_2$ 与 $(m_{ij})$ |
| Morrison 1993（Astérisque 218, 243–271）[Morrison3] | 定义 5.2.2 的来源（本书 PDF p.104 引） | 给出 $r$ 维最大幺幂边界点的三条件定义，本卡定义 3.3 即其书内表述 |
| Morrison 1993（Jour. AMS 6, 223–247）[Morrison2] | 本书 PDF p.105 引 | 五次镜像 $r=1$ 情形验证 $N^d\ne0$ 判据及其整性 |
| Landman 1973（Trans. AMS 181, 89–126）[Landman] | 本书 PDF p.98 引 | 单值性定理的原始出处 |

## 9. 前置与后继

**前置。** 队列登记 MS-11 为硬前置（Gauss–Manin 联络与大复结构极限的话头）；逻辑上还需 MS-13（单值性定理、权滤过 (5.4)）与 MS-06（Picard–Fuchs 方程、指标方程 (5.6)/友矩阵 (5.9)）。
**后继。** MS-13（极限混合 Hodge 结构以最大幺幂为输入；$W_{2k}=W_{2k+1}$ 是 Hodge–Tate 的判据）；MS-06（用指标方程定位 MUM 点，五次例见 PDF p.104）；§6 镜像映射与大复结构极限、§7 Yukawa 耦合的归一化（用 $y_0$ 归一 $\Omega$）；以及 SY01-25 命题 1 所代表的「极大退化」上同调刻画。
**位置提示待核。** 队列把「第 3 章」列为本卡主要位置，但第 3 章为环面几何（chapter03.tex，PDF p.54 起），全文无「单值性」「幺幂」；MUM 内容实际集中在 §5.1.3–5.2.2（PDF p.98–105）。见 §11 Q2。

## 10. 形式化接口（Lean 可 sorry）

```lean
import Mathlib.LinearAlgebra.Matrix.GeneralLinearGroup
import Mathlib.LinearAlgebra.Matrix.Charpoly.Coeff
import Mathlib.FieldTheory.IsAlgClosed.Spectrum

namespace MirrorSymmetry

open Matrix

variable {n : ℕ}

/-- 幺幂：T = I + N，N 幂零。 -/
def IsUnipotent (T : Matrix (Fin n) (Fin n) ℂ) : Prop :=
  ∃ N : Matrix (Fin n) (Fin n) ℂ, N ^ n = 0 ∧ T = 1 + N

/-- 幂零对数：log(I+N) = N − N²/2 + N³/3 − …（N 幂零时为有限和）。 -/
noncomputable def logUnipotent (N : Matrix (Fin n) (Fin n) ℂ) : Matrix (Fin n) (Fin n) ℂ :=
  ∑ k ∈ Finset.range n, ((-1 : ℂ) ^ (k + 1) / (k + 1 : ℂ)) • N ^ (k + 1)

/-- 单值性算子：H³(X_t,ℂ) 上由绕边界除子一周的解析延拓给出的自同构。 -/
structure MonodromyOperator where
  T : Matrix (Fin 4) (Fin 4) ℂ

/-- 1 维模、CY 三维簇（dim H³ = 4）的最大幺幂：单值性定理给 (T−I)⁴ = 0，
    「最大」即 (T−I)³ ≠ 0（Cox–Katz，PDF p.101）。 -/
def MaximallyUnipotent1Dim (T : Matrix (Fin 4) (Fin 4) ℂ) : Prop :=
  (T - 1) ^ 4 = 0 ∧ (T - 1) ^ 3 ≠ 0

/-- 命题 5.2.1 的矩阵版：指标方程 λ⁴ + f₁λ³ + f₂λ² + f₃λ + f₄ 以 ℓ 为四重根，
    等价于留数友矩阵为单一零 Jordan 块（即最大幺幂）。 -/
theorem mum_iff_indicial_quadruple (ℓ : ℂ) (f₁ f₂ f₃ f₄ : ℂ)
    (h₁ : f₁ = -4 * ℓ) (h₂ : f₂ = 6 * ℓ ^ 2) (h₃ : f₃ = -4 * ℓ ^ 3) (h₄ : f₄ = ℓ ^ 4)
    (hdet : f₄ - f₁ * f₂ * f₃ / 3 + f₁ ^ 2 * f₃ / 2 ≠ 0) :
    MaximallyUnipotent1Dim (companion f₁ f₂ f₃ f₄) := by
  sorry

/-- $r$ 维定义 5.2.2 的接口：各 $T_i$ 幺幂、权滤过维数条件、$(m_{ij})$ 可逆。 -/
structure MUMBoundaryPoint (r : ℕ) where
  T : Fin r → Matrix (Fin 4) (Fin 4) ℂ
  hUnipotent : ∀ i, IsUnipotent (T i)
  W : Fin 7 → Submodule ℂ (Fin 4 → ℂ)
  hDim0 : Module.finrank ℂ ↥(W 0) = 1
  hDim1 : Module.finrank ℂ ↥(W 1) = 1
  hDim2 : Module.finrank ℂ ↥(W 2) = 1 + r
  m : Fin r → Fin r → ℂ
  hInvertible : Matrix.det (Matrix.of m) ≠ 0
  hLogRelation : ∀ i j, ¬ (Matrix.of (fun _ _ => (0:ℂ)) = (1:Matrix (Fin 4) (Fin 4) ℂ))

end MirrorSymmetry
```

## 11. 待核清单

**冲突（已登记 §8；只陈述差异，不判定谁对）：**
- **C1（《_冲突表》T1）**：SY01-24 术语表 #18 作「单值变换」monodromy；本书作「单值性」（PDF p.98 作「单值性变换」）。本卡按本书口径用「单值性」。
- **C2（《_冲突表》U2）**：SY01-24 讨论 Picard–Fuchs 方程的「单值变换群」，并令 $N=T-I$（原书 p.21，式 (1.86)）；本书 §5.1.4 起讨论权滤过上的算子 $N=\log T$（PDF p.98、p.104）。作用对象与 $N$ 的定义都不同；本卡显式区分「单值性算子」与「单值群」，$N$ 一律取 $\log$。
- **C3（SY01-25）**：SY01-25 命题 1（01-结果清单 p.13）把同一幂零条件称「极大退化/极大单值」（04-术语文献勘误「[LTY] 极大单值」），本书称「最大幺幂单值性/最大幺幂边界点」；且 SY01-25 只在 $q=0$、1 维情形陈述，本书定义 5.2.2 是 $r$ 维并含 $W_2$、$(m_{ij})$ 条件。名称与适用范围不同。

**待核（未定论，不写死）：**
- **Q1**：SY01-24 术语表无「最大幺幂」条；其式 (1.86) 条件等价但未命名。本书定义 5.2.2 引 [Morrison3]，故该词非本书自造；仍需核 SY01-24 原文（Siebert 讲义）是否有对应术语。
- **Q2**：队列「第 3 章」位置提示与正文不符（第 3 章为环面几何，无「单值性/幺幂」词条）；MUM 实际位置为 §5.1.3–5.2.2（PDF p.98–105）。建议队列更正。
- **Q3**：单值性定理的整数 $m>0$（PDF p.98）；与标准陈述 $m\ge0$ 的对照见《_冲突表》§三（原译笔误已订正，属 MS-13）。本卡按书内 $m>0$ 引用。
- **Q4**：PDF p.100 去心圆盘基下 $T$ 的特征值，中译作 $\exp(-2\pi i\lambda)$，英文 OCR（p100）作 $\exp(2\pi iX)$；本卡不写该式符号，待对照原书图像。
- **Q5**：[Schmid] 幂零轨道定理与 [Deligne1] LNM 163 的具体定理号/页码未落到文献表条目；本卡只按书内引用标注，未核原文。
- **Q6**：例 5.4.2（$P(1,1,2,2,2)$）书内只给一个方向的 PF 方程，$N_1,N_2$ 的完整权滤过未逐项核；本卡只用 $N_2^2=0$ 与「正组合三次方 $\ne0$」两点。
- **Q7**：SY01-25 的「[LTY]」标签未在其资料卡中展开全称与文献信息，待其资料卡补核。
