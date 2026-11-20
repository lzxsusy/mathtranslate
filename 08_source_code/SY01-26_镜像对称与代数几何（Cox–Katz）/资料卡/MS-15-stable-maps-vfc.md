---
id: MS-15
zh: 稳定映射与虚拟基本类
en: stable maps and virtual fundamental class
aliases: [稳定映射, n-标记稳定映射, 虚拟基本类, 虚基本类（旧误写）]
layer: L1
prereqs: [MS-16]
sources:
  - "Cox–Katz 1999, p.192–194（PDF p.192–194）：定义 7.1.1–7.1.2（稳定映射及其族）、定理 7.1.3（粗模空间）、定理 7.1.4（代数叠）"
  - "Cox–Katz 1999, p.194–195（PDF p.194–195）：预期维数式 (7.6)、式 (7.11)–(7.12)、虚拟基本类 $\\xi$ 的引入"
  - "Cox–Katz 1999, p.195–203（PDF p.195–203）：§7.1.3 法锥与引理 7.1.5；§7.1.4 Li–Tian 切—障碍复形、Behrend–Fantechi 完美障碍理论、相对虚拟基本类"
  - "Cox–Katz 1999, p.203–207（PDF p.203–207）：定义 7.1.7（凸）、例题 7.1.5 与式 (7.19)、超额维数命题、定义 7.1.9（GW 类与不变量）"
  - "A 级：Behrend–Fantechi, Invent. Math. 128 (1997)，The intrinsic normal cone（本书 [BF]；命题 7.1.6 引其 p.66–69）"
  - "A 级：Li–Tian, J. Amer. Math. Soc. 11 (1998)，Virtual moduli cycles and Gromov–Witten invariants of algebraic varieties（本书 [LTi2]）"
  - "B 级：Stacks Project『Algebraic Stacks』章与 Perfect obstruction theory 条目；nLab『virtual fundamental class』条目"
status: draft
review:
  drafter: agent-230
  reviewer: lead
  blindtest: pending
glossary_refs: [glossary.tsv 行 61（stable map → 稳定映射）, 行 63（virtual fundamental class，见 §11 冲突）, 行 60（stack → 代数叠）, 行 65（normal cone → 法锥）, 行 66（intrinsic normal cone → 内蕴法锥）, 行 121（tangent–obstruction complex → 切—障碍复形）, SY01-24 术语表 行 31/32]
symbols_refs: ["$\\overline{\\mathcal M}_{g,n}(X,\\beta)$", "$[\\overline M_{g,n}(X,\\beta)]^{\\mathrm{virt}}$", "$E^\\bullet$", "$C_{Z/Y}$", "$\\omega_X$"]
updated: 2026-11-20
---

# MS-15 稳定映射与虚拟基本类

## 1. 一句话

把曲线换成带标记的稳定映射，再用虚拟基本类替掉普通基本类，使 GW 类对一般目标空间也有意义。

## 2. 为什么需要它

- **GW 类的 Gysin 推前需要一个基本类，而模空间一般没有。** 式 (7.3)/(7.8) 把 GW 类写成 $\pi_{2!}\pi_1^*(\alpha_1\otimes\cdots\otimes\alpha_n)$，这只有在 $\overline{\mathcal M}_{g,n}(X,\beta)$ 是预期维数轨形时才是普通基本类的推前；一般情形它有高于预期维数的分支（p.195）。
- **2875 这个数只有用虚拟基本类才合法。** 五次三维簇上恰好 2875 条直线，但 $\overline M_{0,0}(V,\ell)$ 的实际维数是 1（Fermat 五次由 50 个一维分支加 375 条孤立直线组成），预期维数为 0；普通基本类连次数都对不上（p.196–197、p.207）。
- **镜像对称的 A 模型预测以它为前提。** 例题 7.1.6 的 $\langle I_{0,0,d\ell}\rangle=\int_{\overline M_{0,0}(\mathbb P^4,d)}c_{5d+1}(\mathcal V_d)$（p.207）来自 VFC 的推前公式 (7.19)，是后文五次族镜像对称计算（MS-01、MS-06 的 A 模型一侧）的直接输入。
- **§7.2–§7.4 的全部比较都建立在 $\xi$ 上。** 辛侧定义、§7.3 的公理、§7.4 的等价性讨论都默认「已有一个次数等于预期维数的类」（§7.2 起 p.207；§7.3 的公理见 p.214–218）；没有它，GW 不变量只是记号。

## 3. 定义（全假设）

**背景与假设。** $X$ 为 $\mathbb C$ 上光滑射影簇（模空间存在性只需 $X$ 射影，p.192；VFC 构造要用 $X$ 光滑，使 $f^*\Omega_X$、$f^*\Theta_X$ 局部自由，p.198–202）。$\beta\in H_2(X,\mathbb Z)$，$g,n\ge0$，$\omega_X$ 指典范类 $K_X$（p.194）。曲线取 $\mathbb C$ 上连通、射影、算术亏格为 $g$ 的曲线。

**定义 A（$n$-标记稳定映射；定义 7.1.1，p.192）。** 数据 $((C,p_1,\dots,p_n),f)$，$f:C\to X$ 为态射，满足：

1. $C$ 的奇点只有普通二重点；
2. $p_1,\dots,p_n$ 是互异、有次序的光滑点；
3. 若 $C_i\subset C$ 是分支，$C_i\cong\mathbb P^1$ 且 $f|_{C_i}$ 常值，则 $C_i$ 至少含 3 个特殊点（结点或标记点）；
4. 若 $p_a(C)=1$ 且 $n=0$，则 $f$ 非常值。

在条件 1、2 之下，条件 3、4 等价于「$(f,C,p)$ 只有有限个自同构」；无限自同构正是 $n+2g<3$ 时 $\overline M_{g,n}$ 不存在的原因（p.192）。

**定义 B（族与模函子；定义 7.1.2，p.192）。** $S$ 上的 $n$-标记稳定映射是：平坦固有态射 $\mathcal C\to S$、$n$ 个截面 $s_1,\dots,s_n$、态射 $f:\mathcal C\to X$，使每个几何纤维 $s$ 上 $(C_s;(s_i)_s;f_s)$ 都是定义 A 的稳定映射；若各纤维 $p_a(C_s)=g$ 称亏格为 $g$，若 $(f_s)_*[C_s]=\beta$ 称类为 $\beta$。由此得反变函子 $\overline{\mathcal M}_{g,n}(X,\beta):(\mathbf{Sch}/\mathbb C)\to(\mathbf{Sets})$。

**定理（模空间；定理 7.1.3–7.1.4，p.192–193）。** 该函子有粗模空间 $\overline M_{g,n}(X,\beta)$，为 $\mathbb C$ 上射影概形（Alexeev；[FP] 给显式构造）；更精细地 $\overline{\mathcal M}_{g,n}(X,\beta)$ 是 $\mathbb C$ 上的固有代数叠（[BM]），其底层空间即粗模空间。$g=0$、$X=\mathbb P^r$、$\beta=d\ell$ 时它是光滑叠，底层轨形维数 $dr+r+d+n-3$，不可约正规射影（p.193）。

**定义 C（预期维数；式 (7.6)，p.194）。**
$$\dim^{\mathrm{exp}}=(1-g)(\dim X-3)-\int_\beta\omega_X+n .$$
它的来源见 §6 的 D3：等于切空间与障碍空间维数之差 $\operatorname{Ext}^1-\operatorname{Ext}^0$（p.198）。

**定义 D（虚拟基本类；p.199–203）。** 取 $\mathfrak M_{g,n}$ 为满足定义 A 条件 1、2 的 $n$-标记亏格 $g$ 曲线（预稳定曲线）的叠；令 $F:\overline{\mathcal M}_{g,n}(X,\beta)\to\mathfrak M_{g,n}$ 忘掉映射（不作稳定化），$\pi_{n+1}:\overline{\mathcal M}_{g,n+1}\to\overline{\mathcal M}_{g,n}$ 忘最后一点并稳定化，$e_{n+1}$ 为该点的赋值映射，则
$$E^\bullet=\bigl(R\pi_{n+1*}\,e_{n+1}^{*}\Theta_X\bigr)^\vee$$
是相对完美障碍理论（p.202–203），相对虚拟基本类为
$$\bigl[\overline{\mathcal M}_{g,n}(X,\beta)/\mathfrak M_{g,n},\,E^\bullet\bigr]\in A^*\bigl(\overline{\mathcal M}_{g,n}(X,\beta)\to\mathfrak M_{g,n}\bigr),$$
绝对虚拟基本类为 $\xi:=[\overline M_{g,n}(X,\beta)]^{\mathrm{virt}}=[\mathfrak M_{g,n}]\cap(\text{相对类})\in A_*(\overline M_{g,n}(X,\beta))$（p.203）。等价的 Li–Tian 口径：$\xi=s^*[C^{E^\bullet}]$，其中 $E^1\to E^2$ 为切—障碍复形、$C^{E^\bullet}$ 为虚法锥、$s$ 为 $E^2$ 的零截面，$\deg\xi=\operatorname{rk}E^1-\operatorname{rk}E^2$（p.200、p.202）。对稳定映射可取 $T^i=\operatorname{Ext}^i_{\mathcal C/S}\bigl(f^*\Omega_X\to\Omega_{\mathcal C/S}(D),\mathcal O_{\mathcal C}\bigr)$，$i=1,2$，$D=\cup s_i(S)$（式 (7.17)，p.202）。

**本书用法。** Cox–Katz 在 p.195–207 采用「把叠上的类搬到粗模空间」的宽松记法：$\xi$ 严格活在叠与双变 Chow 群中，书中却把它当 $\overline M_{g,n}(X,\beta)$ 上的类使用，并在 p.204 明说全书沿用；与使用 $c_1(TX)$ 的文献对比时注意 $K_X$ 的符号（p.194、p.210）。

## 4. 最小例子（能算出）

**4.1 $\overline M_{0,3}(\mathbb P^1,1)$ 的 3 个点。** 取 $X=\mathbb P^1$、$\beta=\ell$（$d=1$）、$g=0$、$n=3$。$\mathbb P^1$ 光滑射影且凸（定义 7.1.7：对每个亏格 0 稳定映射有 $H^1(C,f^*T_{\mathbb P^1})=0$，因 $f^*T_{\mathbb P^1}\cong\mathcal O(2d)$ 在 $\mathbb P^1$ 上，$h^1=0$），故 $\overline{\mathcal M}_{0,3}(\mathbb P^1,1)$ 是预期维数轨形且 $\xi$ 就是普通基本类（p.203）。

**维数（两条路都算）。** 式 (7.6)：$\dim^{\mathrm{exp}}=(1-0)(1-3)-\int_\ell\omega_{\mathbb P^1}+3=-2-(-2)+3=3$（$\omega_{\mathbb P^1}=\mathcal O(-2)$，故 $\int_\ell\omega_{\mathbb P^1}=-2$）。定理 7.1.4 的公式：$dr+r+d+n-3=1\cdot1+1+1+3-3=3$。两式一致，且实际维数也是 3，故 3 个点条件恰好把它降到 0 维。

**点条件与数字。** 固定互异 $q_1,q_2,q_3\in\mathbb P^1$，条件 $f(p_i)=q_i$（$i=1,2,3$）给出 $\overline{\mathcal M}_{0,3}(\mathbb P^1,1)$ 上的 3 个除子，其交点数即
$$\int_{\xi}e_1^*[\mathrm{pt}]\,e_2^*[\mathrm{pt}]\,e_3^*[\mathrm{pt}]=\langle I_{0,3,\ell}\rangle([\mathrm{pt}],[\mathrm{pt}],[\mathrm{pt}])=1 .$$
唯一性：3 个像点互异 $\Rightarrow$ $f$ 不能在含标记点的分支上常值；$d=1$ 迫使主分支 $\cong\mathbb P^1$ 且 $f$ 在其上为同构（额外的常值 $\mathbb P^1$ 分支只能靠 $\ge3$ 个结点挂上，树状曲线做不到）。于是 $f$ 是 Möbius 变换，由 $f(0)=q_1$、$f(1)=q_2$、$f(\infty)=q_3$ 唯一确定；置 $a=q_1,b=q_2,c=q_3$，显式矩阵为
$$M=\begin{pmatrix}c(b-a) & a(c-b)\\ b-a & c-b\end{pmatrix},\qquad \det M=(b-a)(c-b)(c-a)\ne0,$$
即 $f(z)=\dfrac{c(b-a)z+a(c-b)}{(b-a)z+(c-b)}$。标记有次序，不除以 $3!$，所以答案是 $1$ 而不是 $1/6$。

**4.2 无标记对照。** 同一目标上 $g=0,n=0,d=1$：$\overline M_{0,0}(\mathbb P^1,1)$ 只有一个点（次数 1 的映射只差源曲线的重参数化，$\mathrm{PGL}_2$ 被 $\mathrm{Aut}(\mathbb P^1)$ 完全吃掉），式 (7.6) 也给 $(1)(-2)+2+0=0$；故 $\langle I_{0,0,\ell}\rangle=1$。这说明本例的 $3$ 个点条件与 $3$ 维模空间相抵，数字 1 来自「有序三点决定一个 Möbius 变换」。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | $\deg\xi=\dim^{\mathrm{exp}}=(1-g)(\dim X-3)-\int_\beta\omega_X+n$ | 式 (7.6) p.194；$\deg\xi=\operatorname{rk}E^1-\operatorname{rk}E^2$ p.200 | 实际维数可大于它（p.195） |
| 2 | $X$ 凸（$\forall$ 亏格 0 稳定映射 $H^1(C,f^*T_X)=0$）$\Rightarrow$ 模空间是预期维数轨形且 $\xi=[\overline M_{0,n}(X,\beta)]$ | 定义 7.1.7 p.203 | 射影空间、齐性空间都是凸的 |
| 3 | 法锥版本：$i_*(s^*[C_{Z/Y}])=c_r(E)\cap[Y]$，故 $s^*[C_{Z/Y}]$ 是 Euler 类的精细化 | 引理 7.1.5 p.196 | 有时可写成超额法丛的 Euler 类 |
| 4 | 相对/绝对相容：$\xi=[\mathfrak M_{g,n}]\cap[\overline{\mathcal M}_{g,n}(X,\beta)/\mathfrak M_{g,n},E^\bullet]$；且忘点相容 $[\overline M_{g,n}(X,\beta)]^{\mathrm{virt}}=\phi_n^*[\overline M_{g,n-1}(X,\beta)]^{\mathrm{virt}}$ | p.203；式 (7.20) p.205–206 | $\phi_n$ 不总存在：$n+2g\ge4$ 或 $\beta\ne0,n\ge1$ |
| 5 | 超额维数公式：若 $R^1\pi_{n+1*}e_{n+1}^*\Theta_X$ 局部自由且秩等于超额维数，则 $\xi=c_e(R^1\pi_{n+1*}e_{n+1}^*\Theta_X)\cap([\overline{\mathcal M}/\mathfrak M]\cap[\mathfrak M])$ | p.205（Behrend–Getzler） | 即使 $\overline M$ 光滑该假设也未必成立 |
| 6 | 两套构造（Li–Tian 切—障碍复形、Behrend–Fantechi 完美障碍理论）应一致，但一般等价性未见文献 | p.199（本书对同一论断常给两个证明） | 与 MS-05 §8 的等价性讨论一致 |

## 6. 推导流程（D1…Dn）

- **D1｜先有稳定映射。** 把「曲线 + 映射」的稳定性逐条写出：定义 7.1.1 的 (i)–(iv)，并证明它等价于自同构有限。依据：p.192。
- **D2｜再有模空间。** 函子 $\overline{\mathcal M}_{g,n}(X,\beta)$ 由族（定义 7.1.2）定义；$X$ 射影时粗模空间存在（定理 7.1.3），更精细地得到固有代数叠（定理 7.1.4）。依据：p.192–193。
- **D3｜算预期维数。** 对 $f$ 取切—障碍复形 $f^*\Omega_X\to\Omega_C(\sum p_i)$（式 (7.14) 的长正合列），稳定性使 $\operatorname{Ext}^0=0$，故
  $$\dim^{\mathrm{exp}}=\operatorname{Ext}^1-\operatorname{Ext}^0=\chi(f^*\Theta_X)+\dim\operatorname{Ext}^1(\Omega_C(\Sigma p))-\dim\operatorname{Ext}^0(\Omega_C(\Sigma p));$$
  由 Hirzebruch–Riemann–Roch，$\chi(f^*\Theta_X)=-\int_\beta\omega_X+(1-g)\dim X$，曲线项之差为 $3g-3+n$，合得式 (7.6)。依据：p.198。
- **D4｜发现一般情形会坏。** 模空间可能含有高于预期维数的分支，式 (7.10) 的推前不再合法，于是把式 (7.8) 改写为用类 $\xi$ 的式 (7.11)–(7.12)。依据：p.194–195。
- **D5｜先做最简单的 $\xi$：法锥。** 对 $Z=Z(s)\subset Y$ 定义法锥 $C_{Z/Y}=\operatorname{Spec}_Z\bigoplus I^k/I^{k+1}$（式 (7.13)），得 $s^*[C_{Z/Y}]\in A_{n-r}(Z)$；引理 7.1.5 把它与 Euler 类联系起来。依据：p.195–196。
- **D6｜Li–Tian：从切—障碍复形到虚法锥。** 局部取两项复形 $E^1\to E^2$ 与 Kuranishi 映射，定义虚法锥 $C^{E^\bullet}$，令 $\xi=s^*[C^{E^\bullet}]$，证明它与 $E^\bullet$、Kuranishi 映射的选取无关。依据：p.199–200；例题 7.1.4（p.200）说明它推广 D5。
- **D7｜Behrend–Fantechi：内蕴法锥 + 完美障碍理论。** DM 叠有内蕴法锥 $C_M\subset N_M$；障碍理论 $E^\bullet\to L^\bullet_M$ 在 $h^0$ 同构、$h^{-1}$ 满射；命题 7.1.6 把 $N_M$ 识别为 $h^1/h^0((L^\bullet_M)^\vee)$，$\xi$ 为 $C$ 与零截面的交。依据：p.201–202。
- **D8｜搬到稳定映射上。** 用泛稳定映射 $(\pi_{n+1},e_{n+1})$ 取 $E^\bullet=(R\pi_{n+1*}e_{n+1}^*\Theta_X)^\vee$（式 (7.17)），得相对与绝对 VFC；$\deg\xi$ 重现式 (7.6)。依据：p.202–203。
- **D9｜能算的三类情形。** 凸簇：$\xi=[\overline M]$（p.203）；五次簇：$\xi$ 是零圈 $c_{5d+1}(\mathcal V_d)\cap[\overline M_{0,0}(\mathbb P^4,d)]$ 的推前（式 (7.19)，p.205）；超额维数：命题 p.205。
- **D10｜最终定义 GW 类与不变量。** 把 $\xi$ 代入定义 7.1.9 的 (i)(ii)，得 $I_{g,n,\beta}$ 与 $\langle I_{g,n,\beta}\rangle$。依据：p.206–207。

## 7. 常见误解与反例（≥2）

- **误解 1：虚拟基本类就是模空间的普通基本类。** 反例：Fermat 五次 $V\subset\mathbb P^4$ 上 $\overline M_{0,0}(V,\ell)$ 由 50 个一维分支（平面 Fermat 五次曲线上的锥）与 375 条孤立直线组成，预期维数为 0；普通基本类连次数都不对，虚拟基本类给出零圈，贡献为 $20\cdot50+5\cdot375=2875$（p.196–197）。只有凸簇（$\mathbb P^r$、齐性空间）才有 $\xi=[\overline M]$（p.203）。
- **误解 2：模空间光滑则 $\xi$ 必是基本类、必可用 Euler 类算。** 错。超额维数命题要求 $R^1\pi_{n+1*}e_{n+1}^*\Theta_X$ 局部自由且秩恰等于超额维数，而障碍并不落在 $H^1(C,f^*\Theta_X)$ 本身，而在其商 $\operatorname{Ext}^2_{\mathcal C}(f^*\Omega_X\to\Omega_{\mathcal C}(\Sigma p_i),\mathcal O_{\mathcal C})$，所以即使 $\overline M_{g,n}(X,\beta)$ 光滑该假设也可能不成立（p.205）。
- **误解 3：只要曲线稳定，随便配一个映射都是稳定映射。** 错。定义 7.1.1 的第 3 条针对「像点退化的分量」：常值 $\mathbb P^1$ 分支必须自带 3 个特殊点；否则连续多个自同构。第 4 条排掉 $p_a=1,n=0$ 的常值映射。自同构有限这一条不能省，否则 $n+2g<3$ 时连 $\overline M_{g,n}$ 都不存在（p.192）。
- **误解 4：$n+2g<3$ 时 GW 不变量无定义。** 错。只有 GW **类**要求 $n+2g\ge3$，不变量对所有 $n,g\ge0$ 有定义（定义 7.1.9(ii)，p.206）；例如 4.2 的 $\langle I_{0,0,\ell}\rangle=1$。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999 | p.192–194（PDF p.192–194），定义 7.1.1–7.1.2、定理 7.1.3–7.1.4 | 本卡定义 A、B 与模空间的出处；$g=0,X=\mathbb P^r$ 的光滑性与维数 $dr+r+d+n-3$ 也在此 |
| Cox–Katz 1999 | p.194–207（PDF p.194–207），式 (7.6)、(7.11)–(7.12)、(7.13)、(7.17)–(7.19)、引理 7.1.5、命题 7.1.6、定义 7.1.7、定义 7.1.9 | 预期维数 → 法锥 → Li–Tian/Behrend–Fantechi → 三类可算情形 → GW 类的完整链条。**冲突：** 本书正文原写作「虚基本类」（`_冲突表.md` T4），本卡按裁定与 SY01-24 术语表用「虚拟基本类」；`glossary.tsv` 行 63 目前仍冻结为「虚基本类」，待解冻（见 §11） |
| SY01-24（Siebert 讲义） | 第 3 章 §3（稳定映射）：定义 3.1 以 $\#\operatorname{Aut}(C_s,\mathbf x_s,f_s)<\infty$ 定义稳定映射叠（术语表行 31，书 p.42）；定义 3.5 完美障碍理论；式 (3.102) $[X]^{\mathrm{virt},\phi^\bullet}=s_0^![C_{\phi^\bullet}]\in A_*(X)$（术语表行 32，书 p.46 附近）；定理 3.1（$\overline{\mathcal M}_{0,k}(\mathbb P^n)$ 光滑）= 本书 p.193 的 $g=0$ 情形 | 同一构造的讲义版，但走「完美障碍理论 + 内蕴法锥」一条线到底。**冲突：** 定义表述不同——其定义 3.1 直接要求自同构有限，本书定义 7.1.1 用 (i)–(iv) 四条并证明二者等价（p.192）；**冲突：** 取值范畴不同——式 (3.102) 落在 Chow 群 $A_*(X)$，本书定义 7.1.9 落在 $H^*(\overline M_{g,n},\mathbb Q)$，相对类在双变 Chow 群而常与同调类等同（p.203、p.206），两套表述是否只差记号未见证明；**冲突：** 术语「叠」与「代数叠」（`_冲突表.md` T3 裁定用「代数叠」，本卡从之，p.193） |
| SY01-25 资料卡 | `资料卡/04-术语文献勘误.md`：25 条核心术语表与 34 条文献表 | 主题是 HMS/SYZ，不处理稳定映射与 VFC：术语表 25 条中无 stable map、无 virtual fundamental class 条目；Fukaya 侧用 $A_\infty$-预范畴与 Morse 模型（表内 $[Fu1]$、$[Fu2]$、$[FuO]$、$[P1]$ 一条线）。**冲突：** 适用范围不同——本书把 VFC 放在代数几何框架（§7.1，p.190–207），§7.2（p.207–214）只概述辛侧；按 `_冲突表.md` U4，本卡注明「本书不覆盖 HMS 的辛侧细节」，不用 $A_\infty$/Morse 模型替代 $\operatorname{Ext}^1/\operatorname{Ext}^2$ 切—障碍复形 |
| Behrend–Fantechi 1997（[BF]） | The intrinsic normal cone, Invent. Math. 128；本书命题 7.1.6 引其 p.66–69 | 内蕴法锥与完美障碍理论的原文献，本书 p.201–202 的 D7 即其缩写（卷期页码待核，见 §11） |
| Li–Tian 1998（[LTi2]） | Virtual moduli cycles and Gromov–Witten invariants of algebraic varieties, J. Amer. Math. Soc. 11；本书式 (7.17) 与 p.199–200 | 切—障碍复形与虚法锥的原文献，$\xi=s^*[C^{E^\bullet}]$ 与「与选取无关」的证明出处（卷期页码待核） |
| Kontsevich 1995（[K2]） | §2.2；本书例题 7.1.6（p.207） | 首次给出五次簇公式 $\langle I_{0,0,d\ell}\rangle=\int_{\overline M_{0,0}(\mathbb P^4,d)}c_{5d+1}(\mathcal V_d)$，即 VFC 推前公式的第一次应用 |

## 9. 前置与后继

- **前置：MS-16 预稳定曲线与模空间**（$\overline M_{g,n}$、稳定化、结点曲线叠 $\mathfrak M_{g,n}$；没有它，定义 D 里的 $\pi_{n+1}$ 与 $[\mathfrak M_{g,n}]\cap$ 都写不出来）。另需法锥/Euler 类（Fulton 相交理论）与完美障碍理论的基本语言（`glossary.tsv` 行 65、66、121）。
- **后继：MS-05 GW 不变量**（定义 7.1.9 的 $\xi$ 就是本卡的 VFC）；MS-04 量子上同调（三点不变量给量子乘积）；MS-17 局部化与等变上同调（算 $\int c_{5d+1}(\mathcal V_d)$ 一类积分）；MS-19 量子超平面截面（相对 GW 不变量用相对 VFC）；MS-01 镜像对称（五次族的 A 模型预测）。
- **依赖方向：** MS-16 → MS-15 → MS-05 → MS-04/MS-17/MS-19。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- 只给签名与关键假设，允许 sorry
variable (X : Scheme) [IsSmoothProjective X] (g n : ℕ) (β : H₂ X ℤ)

structure StableMap (X : Scheme) (n : ℕ) where
  C : Scheme
  f : C ⟶ X
  mark : Fin n → C
  -- 定义 7.1.1 (i)-(iv)：普通二重点、标记互异光滑、常值 P¹ 分支 ≥3 特殊点、p_a = 1 且 n = 0 时非常值
  stable : Prop

axiom moduliStack  (g n : ℕ) (β : H₂ X ℤ) : AlgebraicStack     -- 定理 7.1.4（p.193）
axiom coarseSpace  (g n : ℕ) (β : H₂ X ℤ) : Scheme             -- 定理 7.1.3（p.192）
def expectedDim : ℤ := (1 - g) * (dim X - 3) - ∫ β ω_X + n       -- 式 (7.6)（p.194）
axiom obstructionTheory (g n : ℕ) (β : H₂ X ℤ) : TwoTermComplex  -- 式 (7.17)（p.202）
axiom virtualFundamentalClass : (g n : ℕ) (β : H₂ X ℤ) → A_* (moduliStack g n β)
theorem vfc_degree_eq_expected : deg (virtualFundamentalClass g n β) = expectedDim := by sorry
theorem vfc_eq_fundamental_of_convex [IsConvex X] :
    virtualFundamentalClass g n β = cycleOf (coarseSpace g n β) := by sorry  -- 定义 7.1.7（p.203）
```

## 11. 待核清单

- [ ] **冲突（T4 术语）：** `glossary.tsv` 行 63 冻结为「虚基本类」，与 `_冲突表.md` T4 的裁定「虚拟基本类」及 SY01-24 术语表行 32 不一致；本卡用「虚拟基本类」，需解冻并统一。
- [ ] **冲突（T3 术语）：** SY01-24 术语表行 30 作「叠」，本书作「代数叠」（p.193）；本卡从 `_冲突表.md` T3 裁定用「代数叠」，SY01-24 侧是否回改待定。
- [ ] **冲突（定义表述）：** SY01-24 定义 3.1 用 $\#\operatorname{Aut}<\infty$ 定义稳定映射，本书定义 7.1.1 用 (i)–(iv) 并证等价（p.192）；两者等价性是否需在译注中给出，待定。
- [ ] **冲突（取值范畴）：** SY01-24 式 (3.102) 的 VFC 落在 $A_*(X)$，本书定义 7.1.9 落在 $H^*(\overline M_{g,n},\mathbb Q)$、相对 VFC 在双变 Chow 而「常与同调类等同」（p.203、p.206）；两套表述的等价性本书未证，待核。
- [ ] **冲突（适用范围，U4）：** SY01-25 资料卡 04 走辛侧（$A_\infty$-预范畴、Morse 模型），本书只在 §7.1 给代数几何版 VFC、§7.2（p.207–214）仅概述；本卡按 U4 注明「本书不覆盖 HMS 的辛侧细节」，辛侧定义与本书定义是否对应待核。
- [ ] **原始文献卷期页码：** [BF] Invent. Math. 128 (1997)、[LTi2] JAMS 11 (1998)、[K2] Kontsevich 1995 §2.2 的卷期页码本书未给，需按原刊补齐（MS-05 §11 亦记此项）。
- [ ] **宽松记法：** p.195、p.204 混用 $[\overline M_{g,n}(X,\beta)]^{\mathrm{virt}}$ 与 $[\overline{\mathcal M}_{g,n}(X,\beta)]^{\mathrm{virt}}$；本卡统一写粗模空间记法，若 MS-05 改记号需同步。
- [ ] **例题编号：** 中译 \SourceExampleNumber{7.1.3}{1}–{7.1.6}{1} 与定理编号 7.1.3–7.1.4、引理 7.1.5、命题 7.1.6 重号，疑为排版沿用原书；本卡按「例题 7.1.x」引用，是否需改编号待核。
- [ ] **2875 的分解：** $20\cdot50+5\cdot375$ 中 20 与 5 来自法锥重数 2/5 与纤维维 5/6 的组合（p.197），需逐步复核该算术。
- [ ] **SY01-24 页码：** 其稳定映射、虚拟基本类正文（书 p.42、p.46）仅有术语表与源码 `ch03.tex` 可查，印刷页码未逐页对读，待核。
