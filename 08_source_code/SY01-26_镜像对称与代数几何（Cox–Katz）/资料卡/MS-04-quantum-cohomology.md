---
id: MS-04
zh: 量子上同调
en: quantum cohomology
aliases: [小量子上同调, 大量子上同调, 小量子环, 大量子环, 量子乘积]
layer: L1
prereqs: [MS-05]
sources:
  - "A 级：Cox–Katz 1999, §8.1, PDF p.240–252（印刷 p.217–229）：定义 8.1.1（p.241）、命题 8.1.3（p.241–242）、定理 8.1.4（p.242–243）、命题 8.1.5–8.1.6（p.244）、推论 8.1.7（p.245）、例 8.1.2（p.245–250）"
  - "A 级：Cox–Katz 1999, §8.1.3, PDF p.251–252（印刷 p.228–229）：系数环 R 与 Novikov 环 Λ(ω,Q)"
  - "A 级：Cox–Katz 1999, §8.2, PDF p.252–257（印刷 p.229–234）：定义 8.2.1–8.2.2、引理 8.2.3、定理 8.2.4（WDVV）、定理 8.2.5"
  - "A 级：Cox–Katz 1999, §8.4–8.5, PDF p.262–269（印刷 p.239–246）：Dubrovin 联络、引理 8.5.1、命题 8.5.2–8.5.3"
  - "A 级：Kontsevich–Manin 1994, Comm. Math. Phys. 164, 525–562, §1–2（本书 PDF p.241、p.255 引作 [KoM1]）"
  - "A 级：Batyrev 1993, Astérisque 218, 定理 5.3（本书 PDF p.247 引作 Batyrev2 定理 5.3）"
  - "B 级：Cox–Katz 1999, §8.1–§8.5 节内定义与例题（书内节号，PDF p.240–280）"
status: draft
review: {drafter: agent-222, reviewer: lead, blindtest: pending}
glossary_refs: ["quantum cohomology", "quantum product", "Gromov–Witten invariant", "Novikov ring", "Frobenius algebra", "WDVV equation", "Dubrovin connection", "monodromy"]
symbols_refs: ["$q^\\beta$", "$\\langle I_{0,3,\\beta}\\rangle$", "$g_{ij}$", "$\\Phi$", "$T_i*T_j$", "$\\Lambda(\\omega,Q)$"]
updated: 2026-11-20
---

# MS-04 量子上同调

## 1. 一句话

用量子乘积代替杯积的上同调环，而量子乘积随 Kähler 类变动。

## 2. 为什么需要它

- **镜像定理要靠它陈述 A 侧。** 第 11 章的五次镜像定理（[LLY]，PDF p.356；最早表述见 [Kontsevich3]）说：经镜像映射拉回后，B 模型 Yukawa 势的三阶导数等于 A 模型关联函数。而 A 模型关联函数就是量子乘积的三点函数 $\langle T_i,T_j,T_k\rangle=\int_{V}T_i*T_j*T_k$（定理 8.6.2，PDF p.282）；没有量子乘积，镜像定理的 A 侧无从定义。
- **镜像映射的预言靠它的单值性。** 第 6 章 §6.3（PDF p.172–174）用 Picard–Fuchs 解之比定义镜像坐标 $q$，并在 p.165 指出：镜像映射应把单值性的对数，与 Kähler 锥生成元的杯积对应（该处还给出 $N_1^3=0$、$N_2^2-3N_1N_2=0$）。这个对应正是命题 8.5.3（PDF p.269）：A 模型联络的单值性算子满足 $N_j=\log T_j\sim-T_j\cup$。
- **GW 不变量的计算靠它的环结构组织。** WDVV 方程（定理 8.2.4，PDF p.255–256）就是量子乘积的结合律（定理 8.2.5，PDF p.256–257）；$\mathbb{P}^2$ 的 $N_d$ 递推（PDF p.259–260）正是从 WDVV 解出来的。CY 三维簇上大量子=小量子（p.262），三次函数 $\langle H,H,H\rangle$ 一个对象就装下全部亏格 0 GW 数据。
- **TQFT 视角。** 附录 B.6 把量子乘积解释为二维拓扑量子场论的融合积（页码待核），说明它为什么天然是结合环。

## 3. 定义（全假设）

1. **几何假设。** $X$ 是 $\mathbb{C}$ 上的光滑射影簇；$\omega\in H^2(X,\mathbb{C})$ 是**复化 Kähler 类**，即 $\operatorname{Im}\omega$ 为 Kähler 类（定义 8.1.1，PDF p.241）。$\beta\in H_2(X,\mathbb{Z})$ 取有效曲线类（非有效时模空间为空，不变量取 0）。
2. **GW 不变量。** 由第 7 章定义 7.1.9（PDF p.206）给出三点 GW 类 $I_{0,3,\beta}=\pi_{1*}(\xi\cdot\prod_i e_i^*\alpha_i)\in H^*(\bar M_{0,3})$，$\xi$ 为虚拟基本类；因 $\bar M_{0,3}$ 是单点，得到数 $\langle I_{0,3,\beta}\rangle(\alpha_1,\alpha_2,\alpha_3)\in\mathbb{Q}$，对 $\alpha_i$ 多线性（先对有理类定义，再线性扩张到 $\mathbb{C}$）。
3. **基与配对。** 取 $H^*(X,\mathbb{Q})$ 的齐次基 $T_0=1,T_1,\ldots,T_m$；$g_{ij}=\int_X T_i\cup T_j$ 由 Poincaré 对偶非退化，$(g^{ij})$ 为逆矩阵；升指标 $T^i=\sum_j g^{ij}T_j$，满足 $\int_X T^i\cup T_j=\delta^i_j$。
4. **量子参数。** $q^\beta:=e^{2\pi i\int_\beta\omega}$。这是 Kähler 模进入代数的唯一入口；$\omega$ 改变时 $q^\beta$ 随之改变。
5. **次数条件。** 只有满足
   $$\deg a+\deg b+\deg T_i=2\dim X-2\int_\beta\omega_X$$
   的 $\beta$ 才可能贡献（式 (8.2)，PDF p.241）；等价地 $\deg q^\beta=-2\int_\beta\omega_X=2\int_\beta c_1(X)$，故 $q$ 是带次数的形式变量。不满足式 (8.2) 的项按约定取 0（虚拟基本类的维数与插入次数不匹配）。
6. **小量子乘积（定义 8.1.1，PDF p.241）。** 对 $a,b\in H^*(X,\mathbb{C})$ 定义
   $$a*b=\sum_{i,j}\sum_{\beta}\langle I_{0,3,\beta}\rangle(a,b,T_i)\,g^{ij}q^\beta T_j
   =\sum_i\sum_\beta\langle I_{0,3,\beta}\rangle(a,b,T_i)\,q^\beta T^i .$$
   第二个等号即式 (8.1)。**严格化**（§8.1.3，PDF p.251–252）：Fano 时求和有限（命题 8.1.3，p.241–242），系数取半群环 $R=\mathbb{Q}[q^\beta:\beta\in H_2(X,\mathbb{Z})]$；一般射影簇取 $R=\mathbb{Q}[[q^\beta:\beta\in M(X)_{\mathbb{Z}}]]$（$M(X)$ 为 Mori 锥）；辛情形取 **Novikov 环**
   $$\Lambda(\omega,\mathbb{Q})=\Bigl\{\textstyle\sum a_\beta q^\beta:\ \forall C\in\mathbb{R},\ \#\{\beta:a_\beta\ne0,\ \int_\beta\omega<C\}<\infty\Bigr\}.$$
   CY 上「$\operatorname{Im}\omega$ 足够大时和收敛」是**猜想 8.1.2**（PDF p.241），未证。
7. **小量子上同调环。** $H^*(X,R)$ 在 $*$ 下是以 $T_0=1$ 为单位元的超交换环（定理 8.1.4，PDF p.242–243）；连同配对 $g$ 构成 Frobenius 代数（命题 8.1.6，PDF p.244）。记 $QH^*(X)=(H^*(X,R),*,g)$。
8. **大量子上同调。** 把 $H^*(X,\mathbb{C})$ 看成超流形：齐次基 $T_i$ 配同次数的超交换变量 $t_i$（奇变量平方为 0）。GW 势
   $$\Phi(\gamma)=\sum_{n\ge0}\sum_\beta\frac1{n!}\langle I_{0,n,\beta}\rangle(\gamma^n)q^\beta,\qquad \gamma=\sum_i t_iT_i$$
   （定义 8.2.1，PDF p.253；$\beta=0$ 时隐含 $n\ge3$，否则级数不截断）。大量子乘积 $T_i*T_j=\sum_k\dfrac{\partial^3\Phi}{\partial t_i\partial t_j\partial t_k}T^k$（定义 8.2.2，PDF p.254）。令 $t_0=t_{r+1}=\cdots=t_m=0$（即只留 $H^2$ 变量）便回到小量子乘积（引理 8.5.1，PDF p.265）。

**本书用法。** Cox–Katz 明确把「量子上同调」拆成小/大两个环（PDF p.240），定义 8.1.1 写的是显式依赖复化 Kähler 类 $\omega$ 的版本，并自承「不精确」（$\beta$ 和可能无限），到 §8.1.3 才用形式系数补全。标准公理化路线（Kontsevich–Manin）顺序相反：先给系数环与 GW 类公理，再用三点函数定义乘积；两条路线在本书的例子（Fano、齐性空间、五次）中给出同一个环。

## 4. 最小例子（能算出）

**例 A：$\mathbb{P}^1$ 的小量子环。** 基 $T_0=1,T_1=H$，$\deg H=2$，$\dim X=1$，$c_1=2H$。配对矩阵与逆矩阵都是 $g=\begin{pmatrix}0&1\\1&0\end{pmatrix}$，故 $T^0=H,\ T^1=1$。$\omega_{\mathbb{P}^1}=\mathcal{O}(-2)$，次数条件为 $\deg a+\deg b+\deg T_i=2+4d$。取 $a=b=H$（度和 4）：$4+\deg T_i=2+4d\Rightarrow\deg T_i=4d-2$；$d=1$ 时 $\deg T_i=2$，只有 $T_i=H$ 可贡献。唯一的 GW 数由「$\mathbb{P}^1$ 中两点定唯一的 1 次映射」给出 $\langle I_{0,3,1}\rangle(H,H,H)=1$。于是
$$H*H=\langle I_{0,3,1}\rangle(H,H,H)\,q\,T^1=q\cdot1,\qquad 1*H=H .$$
所以 $QH^*(\mathbb{P}^1)\cong\mathbb{C}[H]/(H^2-q)$，经典环为 $\mathbb{C}[H]/(H^2)$。自检：$q\ne0$ 时 $H$ 可逆（$H\cdot H/q=1$），$q=0$ 时 $H$ 幂零——环结构确实变了（见 §7.1）。

**例 B：$\mathbb{P}^2$ 的小量子环（含结合律数字检验）。** 基 $1,H,H^2$，$c_1=3H$，
$$g=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},\qquad g^{-1}=g,\qquad T^0=H^2,\ T^1=H,\ T^2=1 .$$
$\omega=\mathcal{O}(-3)$，次数条件 $\deg a+\deg b+\deg T_i=4+6d$，即 $\deg q^d=6d$。
- $H*H$：$4+\deg T_i=4+6d$ 无 $d\ge1$ 解，故 $H*H=H^2$（与经典杯积同）。
- $H*H^2$：$6+\deg T_i=4+6d\Rightarrow\deg T_i=6d-2$；$d=1$ 给 $\deg T_i=4$，即 $T_i=H^2$，且 $T^2=1$。GW 数 $\langle I_{0,3,1}\rangle(H,H^2,H^2)=1$（过两点的直线唯一），故 $H*H^2=q\cdot1$。
- 结合律检验：$(H*H)*H^2=H^2*H^2$。后者次数条件 $8+\deg T_i=4+6d\Rightarrow\deg T_i=6d-4$，$d=1$ 给 $\deg T_i=2$，即 $T_i=H$，$T^1=H$，故 $H^2*H^2=qH$。另一边 $H*(H*H^2)=H*(q\cdot1)=qH$。两者相等 ✓。
因此 $QH^*(\mathbb{P}^2)\cong\mathbb{C}[H]/(H^3-q)$（多项式检验：$H^3=H*(H^2)=q$），经典环 $\mathbb{C}[H]/(H^3)$；$q\to0$ 时退化回杯积。这与书上的通式 $\mathbb{C}[H]/\langle H^{r+1}-q\rangle$（例 8.1.2(1)，PDF p.245–246）在 $r=1,2$ 一致。

**例 C：五次三维簇的次数检验。** $V\subset\mathbb{P}^4$ 为五次超曲面，$H$ 为超平面类，$\int_VH^3=5$，$c_1(V)=0$ 故 $\deg q=0$（不再截断次数）。引理 8.1.8（PDF p.248）：只要 $\deg a\ne2$ 或 $\deg b\ne2$，就有 $a*b=a\cup b$。对 $a=b=H$，次数条件迫使 $T_i\in H^2$，唯一贡献者是 $T_i=H$，其配对逆元为 $T^H=\frac15H^2$（因 $\int(\frac15H^2)\cup H=5/5=1$），故
$$H*H=\tfrac15\langle H,H,H\rangle\,H^2,\qquad
\langle H,H,H\rangle=5+\sum_{d\ge1}n_d\frac{d^3q^d}{1-q^d}$$
（一般 CY 三维簇的三点函数，PDF p.249；$n_d$ 为瞬子数，由 $\langle I_{0,0,d}\rangle=\sum_{d=kd'}n_{d'}k^{-3}$ 定义）。$q=0$ 时 $\langle H,H,H\rangle=5$，代回得 $H*H=H^2$，与经典 $\int H^3=5$ 一致 ✓。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | $(H^*(X,R),*)$ 是以 $T_0=1$ 为单位元的超交换环：$a*b=(-1)^{\deg a\deg b}b*a$ | 定理 8.1.4，PDF p.242–243 | 结合律来自第 7 章分裂公理 |
| 2 | Frobenius 代数：$g(a*b,c)=g(a,b*c)=\sum_\beta\langle I_{0,3,\beta}\rangle(a,b,c)q^\beta$，且 $\int_Xa*b=g(a,b)$ | 命题 8.1.6，PDF p.244 | 三点函数 $\langle a,b,c\rangle=\int_Xa*b*c$ |
| 3 | 齐次性：$\deg(a*b)\equiv\deg a+\deg b\pmod 2$（当 $\omega_X$ 被整数 $r$ 整除时可加强为 $\bmod 2r$）；CY 时严格可加且 $H^{p,q}*H^{r,s}\subset H^{p+r,q+s}$ | 命题 8.1.5、推论 8.1.7，PDF p.244–245 | CY 时 $\oplus_pH^{p,p}$ 是子环 |
| 4 | 极限退化：$q\to0$（$\operatorname{Im}\omega\to\infty$）时量子乘积→杯积；$\mathbb{P}^r$ 上显式 $QH^*\cong\mathbb{C}[H]/(H^{r+1}-q)$ | 例 8.1.2(1)，PDF p.245–246；环面簇版见 Batyrev2 定理 5.3，PDF p.246–249 | Batyrev 量子环把 SR 理想换成量子 SR 理想 |
| 5 | CY 三维簇：只要 $\deg a\ne2$ 或 $\deg b\ne2$ 就有 $a*b=a\cup b$（引理 8.1.8）；五次时 $H*H=\frac15\langle H,H,H\rangle H^2$，瞬子数 $n_d$ 藏在 $\langle H,H,H\rangle$ 里 | 引理 8.1.8，PDF p.248；PDF p.249、p.262 | $n_d$ 未必是曲线计数（p.249） |
| 6 | 大量子乘积：结合律 $\Leftrightarrow$ WDVV $\Leftrightarrow$ Dubrovin 联络 $\nabla^\lambda$ 平坦；A 模型联络 $\nabla_{\partial/\partial u_i}(T_j)=T_i*_{\mathrm{small}}T_j$ 平坦，$\lambda=\frac1{2\pi i}$，沿边界单值性幺幂且 $N_j\sim-T_j\cup$ | 定理 8.2.4–8.2.5，PDF p.255–257；PDF p.263、p.267、p.269 | 这是镜像对称把 A 模型联络与 B 模型 Gauss–Manin 联络对齐的依据 |

## 6. 推导流程（D1…D8）

- **D1（GW 类 → 数）。** 第 7 章定义 7.1.9（PDF p.206）：$I_{0,3,\beta}$ 由虚拟基本类拉回、推出到 $\bar M_{0,3}$；因 $\bar M_{0,3}$ 是点，$\langle I_{0,3,\beta}\rangle$ 是三重线性数。
- **D2（定义乘积）。** 用基与配对把 $I_{0,3,\beta}$ 的三重线性数写成结构常数，得定义 8.1.1 与式 (8.1)（PDF p.241）。
- **D3（截断求和）。** 把式 (8.2) 的次数条件代入（PDF p.241），得每个固定 $a,b$ 只有有限个次数档的 $\beta$ 可贡献；Fano/齐性时用命题 8.1.3（PDF p.241–242）证有限，一般情形改用形式系数环（§8.1.3，PDF p.251–252）。
- **D4（结合律）。** 第 7 章分裂公理把 $I_{0,4,\beta}$ 沿 $\varphi:\bar M_{0,3}\times\bar M_{0,3}\to\bar M_{0,4}\cong\mathbb{P}^1$ 拉回，两条结合律表达式对应 $\mathbb{P}^1$ 上两个线性等价点 ⇒ 定理 8.1.4（PDF p.242–243）。
- **D5（Frobenius）。** 由 $I_{0,3,\beta}$ 的三重对称性与配对定义直接重排 ⇒ 命题 8.1.6（PDF p.244）；由此 $\langle a,b,c\rangle=\int_Xa*b*c$。
- **D6（大量子化）。** 把全部 $n\ge3$ 的 $\langle I_{0,n,\beta}\rangle$ 装进 GW 势 $\Phi$（定义 8.2.1，PDF p.253），其三阶导数给出大量子乘积（定义 8.2.2、引理 8.2.3，PDF p.254–255）；限制到 $H^2$ 得小量子乘积（引理 8.5.1，PDF p.265）。
- **D7（WDVV）。** 在 $\bar M_{0,n+4}$ 上两个边界除子 $D(i,j|k,l)$ 与 $D(j,k|i,l)$ 线性等价，用分裂公理逐项算 ⇒ WDVV（定理 8.2.4，PDF p.255–256）⇔ 结合律（定理 8.2.5，PDF p.256–257）。
- **D8（联络与 Hodge 结构变分）。** 以 $\Phi$ 的三阶导数为 $A_{ijk}$ 造 Dubrovin 联络 $\nabla^\lambda$（PDF p.262–263）：曲率为 0 $\Leftrightarrow$ WDVV $\Leftrightarrow$ 结合律；限制到 $H^2$、取 $\lambda=\frac1{2\pi i}$ 得平坦的 A 模型联络（命题 8.5.2，PDF p.267），其单值性幺幂且 $N_j\sim-T_j\cup$（命题 8.5.3，PDF p.269），于是 $(H,\nabla,H_{\mathbb{Z}},F^\bullet)$ 是 Hodge 结构变分（定理 8.5.11，PDF p.277–278），最终与 B 模型的 Yukawa 耦合对齐（定理 8.6.2，PDF p.282）。

## 7. 常见误解与反例（≥2）

1. **误解：$q\to0$ 的极限就是原来的上同调环，所以量子环只是「同一环换记号」。** 反例：$\mathbb{P}^1$ 上 $QH^*\cong\mathbb{C}[H]/(H^2-q)$。取 $q=1$ 时 $\mathbb{C}[H]/(H^2-1)\cong\mathbb{C}\times\mathbb{C}$（$H\mapsto(1,-1)$）有幂等元，而 $q=0$ 时 $\mathbb{C}[H]/(H^2)$ 是局部环、无幂等元：两者不同构。$q$ 是形式参数，只有取极限才退化到经典环，取具体数值不保持环结构。
2. **误解：小量子上同调已经包含全部 GW 不变量。** 反例：$\mathbb{P}^2$ 的小量子环只需 $\langle I_{0,3,1}\rangle=1$ 这一个数；$N_2=1,N_3=12,\ldots$（$d\ge2$ 的曲线数）根本不在小量子环里。用量子乘积比较：$\mathbb{P}^2$ 上大量子乘积 $T_1*T_1=T_2+\Phi_{111}T_1+\Phi_{112}T_0$，而小量子乘积 $T_1*T_1=T_2$（PDF p.259）——两者不是同一个乘积。要全部数据必须用 GW 势/大量子环。
3. **误解：CY 三维簇上量子修正可以忽略。** 反例：五次 $H*H=\frac15\langle H,H,H\rangle H^2$，虽然 $q=0$ 时回到 $H^2$，但 $\langle H,H,H\rangle=5+\sum_d n_d\frac{d^3q^d}{1-q^d}$ 的每项 $n_d$ 都是非平凡 GW 数据（PDF p.249），且 $n_d$ 未必是有理曲线计数（p.249 明说只与带符号计数密切相关）。「大=小」（p.262）指两个环含相同信息，不是指量子修正为零。
4. **误解：量子上同调只依赖 $X$ 的上同调环。** 反例：翻越 $V\dashrightarrow V'$（PDF p.249–250）有 $H^2(V)\cong H^2(V')$、Kähler 锥只沿共同面相接；在各自 Kähler 锥内部，两侧小量子环在数值系数下并不同构，只通过解析延拓联系。$q^\beta=e^{2\pi i\int_\beta\omega}$ 显含 $\omega$，换 Kähler 类就换环。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999 | §8.1，PDF p.240–252（印刷 p.217–229）；定义 8.1.1 在 PDF p.241 | 小量子乘积的定义、次数条件 (8.2)、有限性命题 8.1.3、收敛猜想 8.1.2、环定理 8.1.4、Frobenius 命题 8.1.6 |
| Cox–Katz 1999 | §8.2，PDF p.252–257（印刷 p.229–234） | 大量子上同调：GW 势（定义 8.2.1）、大量子乘积（定义 8.2.2）、WDVV（定理 8.2.4）、结合律（定理 8.2.5） |
| Cox–Katz 1999 | §8.4–8.5，PDF p.262–269（印刷 p.239–246） | Dubrovin 联络 $\nabla^\lambda$ 与 WDVV 的三组等价；A 模型联络 $\nabla=T*_{\mathrm{small}}$ 平坦（命题 8.5.2）、单值性幺幂 $N_j\sim-T_j\cup$（命题 8.5.3） |
| Cox–Katz 1999 | §8.6，PDF p.280–283（印刷 p.257–260） | 定义 8.6.1 数学镜像对；定理 8.6.2：B 模型 Yukawa 耦合 = A 模型三点函数 $\int T_i*T_j*T_k$ |
| SY01-24 术语表 | #31 稳定映射 p.42、#32 虚拟基本类 p.46、#67 Novikov 域 p.99；第 6 章 HMS 只到 Novikov 域与 Hochschild 上同调，p.96–104 | 只覆盖 GW 的输入与系数，**70 条中无「量子上同调/GW 势/WDVV」条目**。**冲突**：monodromy 作「单值变换」（本书作「单值性」，T1）；系数作「Novikov 域」而本书 PDF p.252 定义的是「Novikov 环」$\Lambda(\omega,\mathbb{Q})$（域/环不同，见 §11 C1、C2） |
| SY01-25 资料卡 | `04-术语文献勘误.md` §一（HMS、A∞-预范畴、Morse–Smale 复形）、§二 文献表 [Ko] | 其量子侧走 A∞/Fukaya 与同调扰动，**全书无「量子上同调」条目**，不定义小量子乘积。**冲突**：本书第 8 章用稳定映射+GW 不变量，不引入 A∞-预范畴（U4）；大极限用 $q\to0$，本书用 $q=e^{2\pi it}$ 与 $\operatorname{Im}\omega\to\infty$（U3，见 §11 C3、C4） |
| 原始文献：Kontsevich–Manin 1994 | Comm. Math. Phys. 164, 525–562，§1–2（本书 PDF p.241、p.255 引作 [KoM1]） | GW 类公理化与量子上同调定义的标准来源；定义 8.1.1 与 WDVV 证明均引此 |
| 原始文献：Batyrev 1993 | Astérisque 218，定理 5.3（本书 PDF p.247 引作 Batyrev2 定理 5.3） | 环面簇量子环 $H^*_\omega(X)=\mathbb{C}[x]/(P(\Sigma)+\mathrm{SR}_\omega(\Sigma))$，即例 8.1.2(2) |
| 原始文献：Dubrovin 1996 | LNM 1620，§1–3（本书 PDF p.262 引作 Dubrovin1，页码待核） | Frobenius 流形与 Dubrovin 联络：把「量子乘法 + 配对 + 势」组织成平坦联络 |

## 9. 前置与后继

- **前置（队列登记）：MS-05**（GW 不变量；定义 7.1.9，PDF p.206，本卡定义 8.1.1 的直接输入）。MS-05 自身的前置是 MS-15（稳定映射与虚拟基本类）；本卡还需第 7 章 §7.1–7.2（GW 类/不变量与公理）与 Poincaré 对偶、上同调环。
- **后继：** MS-18（Frobenius 流形与 Dubrovin 联络，本卡 §5 性质 6 的直接展开）；MS-19（量子超平面截面原理，prereqs 为 MS-04、MS-18）；MS-11（Hodge 结构变分，本卡 §8.5 的 A 模型部分）；MS-12（单值性与最大幺幂，$N_j=\log T_j$，PDF p.269）；MS-02（镜像映射，第 6 章 §6.3，PDF p.172–174）；MS-01（镜像对称）；第 10 章量子微分方程（PDF p.324 起，量子 D-模与 J 函数）。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- 只列接口与关键假设；证明一律 sorry。Mathlib 尚无 GW 不变量与虚拟基本类。
import Mathlib.Data.Complex.Basic

namespace MirrorSymmetry

/-- 小/大量子上同调的代数骨架（定义 8.1.1、定理 8.1.4、命题 8.1.6）。
    H 抽象掉 H^*(X,R)；star 即量子乘积，pair 即 g(a,b)=∫_X a∪b。 -/
structure QuantumData where
  H : Type
  [addGroup : AddCommGroup H]
  [module : Module ℂ H]
  deg : H → ℤ                                  -- 次数
  one : H                                      -- T_0 = 1
  pair : H → H → ℂ                             -- Poincaré 配对
  pair_nondegen : ∀ a, (∀ b, pair a b = 0) → a = 0
  B : Type                                     -- 有效曲线类 β 的集合
  q : B → ℂ                                    -- q^β = e^{2πi∫_β ω}
  gw : B → H → H → H → ℂ                       -- ⟨I_{0,3,β}⟩（三重线性）
  star : H → H → H                             -- 量子乘积 a*b
  star_comm : ∀ a b, star a b = star b a
  star_assoc : ∀ a b c, star (star a b) c = star a (star b c)
  one_star : ∀ a, star one a = a
  frobenius : ∀ a b c, pair (star a b) c = pair a (star b c)

/-- 定义 8.1.1（PDF p.241）：a*b = Σ_i Σ_β ⟨I_{0,3,β}⟩(a,b,T_i) q^β T^i，
    其中 T^i 由非退化配对取对偶基给出（g^{ij} 为逆矩阵）。 -/
noncomputable def smallQuantumProduct (Q : QuantumData) (a b : Q.H) : Q.H :=
  Q.star a b

/-- 定理 8.1.4（PDF p.242–243）：超交换结合环；结合律由第 7 章分裂公理证明。 -/
theorem star_associative (Q : QuantumData) (a b c : Q.H) :
    Q.star (Q.star a b) c = Q.star a (Q.star b c) := Q.star_assoc a b c

/-- 命题 8.1.6（PDF p.244）：Frobenius 代数。 -/
theorem frobenius_pairing (Q : QuantumData) (a b c : Q.H) :
    Q.pair (Q.star a b) c = Q.pair a (Q.star b c) := Q.frobenius a b c

/-- 定理 8.2.5（PDF p.256–257）：大量子乘积结合律 ⟺ WDVV（只列签名）。 -/
opaque wdvv (Q : QuantumData) : Prop

theorem assoc_iff_wdvv (Q : QuantumData) :
    (∀ a b c, Q.star (Q.star a b) c = Q.star a (Q.star b c)) ↔ wdvv Q := by
  sorry

/-- 命题 8.5.3（PDF p.269）：A 模型联络单值性算子幺幂，N_j = log T_j 与 −T_j∪ 共轭。 -/
def Unipotent {Q : QuantumData} (N : Module.End ℂ Q.H) : Prop :=
  ∃ k : ℕ, (N - 1) ^ k = 0

end MirrorSymmetry
```

## 11. 待核清单

- [ ] **C1 术语级冲突（SY01-24，T1）**：SY01-24 用「单值变换」，本书用「单值性」（A 模型联络处 PDF p.269）。依《_冲突表》T1 本卡用「单值性」，只登记差异、不判优劣。→ §8 第 5 行。
- [ ] **C2 术语级冲突（SY01-24）**：SY01-24 #67 作「Novikov 域（Novikov field）p.99」，本书 PDF p.252 定义「Novikov 环」$\Lambda(\omega,\mathbb{Q})$：域与环是两个不同对象，是否为 Siebert 讲义口径差异待核。→ §8 第 5 行。
- [ ] **C3 建模口径冲突（SY01-25，U4）**：SY01-25 用 A∞-预范畴/Morse–Smale 复形处理量子侧，本书第 8 章只用稳定映射+GW 不变量，不引入 A∞。两卡不矛盾但不可逐条对照，交 MS-15/16 展开。→ §8 第 6 行。
- [ ] **C4 大极限表述（U3）**：SY01-24 与 SY01-25 用 $q\to0$ 刻画大复结构极限；本书用 $q=e^{2\pi it}$、$t\to i\infty$，且在大半径极限用 $\operatorname{Im}\omega\to\infty$（PDF p.246、p.251–252）。换算 $t=\frac{\log q}{2\pi i}$ 与 Batyrev 环面坐标的对应本卡未核，交 MS-06/MS-19。→ §8 第 5–6 行。
- [ ] 队列 `_queue.md` 把 MS-04 的书内位置记为「第 6–7 章」，实际主章节是**第 8 章**（PDF p.240–297，印刷 p.217–274）；第 6 章（镜像映射）、第 7 章（GW 不变量）是前置。疑为队列行笔误，待维护者确认。
- [ ] 定义 8.1.1（PDF p.241）自承不精确：一般 CY 上 $\beta$ 求和收敛性只有猜想 8.1.2（PDF p.241），而定理 8.1.4 的严格证明依赖 §8.1.3 的形式系数环。本卡 §3 已按「先形式、后数值」写，但书中「不精确定义」到「严格定义」的过渡页码（p.241 vs p.251–252）是否还有中间假设，待核。
- [ ] 外部文献坐标只核到书名/定理号：Kontsevich–Manin 1994 的 §1–2 具体页、Batyrev 1993 定理 5.3 的原书页、Dubrovin 1996 LNM 1620 的 §1–3 页码，均待补（当前 A 级只落到本书引用页 p.241、p.247、p.262）。
- [ ] 队列把最小例子写成 $\mathbb{Z}[p]/(p^{n+1})-q$（整系数），本书用 $\mathbb{Q}$ 系数与 $\mathbb{P}^r$ 记号（例 8.1.2(1)，PDF p.245–246）；系数域差异待核，本卡按本书用 $\mathbb{Q}$。
- [ ] §4 例 C 的 $\langle H,H,H\rangle$ 展开式按 PDF p.249 的一般公式写成 $\sum_d n_d\,d^3q^d/(1-q^d)$，但书中对五次是否用同一归一化（$q=e^{2\pi it}$、$n_d$ 的正负号）未逐项核对，$n_1=2875$ 等数值待从原书页取。
