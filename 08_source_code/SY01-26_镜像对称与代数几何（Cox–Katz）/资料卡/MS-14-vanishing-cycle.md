---
id: MS-14
zh: 消失圈
en: vanishing cycle
aliases:
  - 消失球
  - 极小整消失圈
  - 极小整圈
layer: L1
prereqs: [MS-12, MS-06, MS-10]
sources:
  - A 级：Cox–Katz 1999, §2.3, 印刷 p.19（PDF p.42，`\SourcePage{42}`），式 (2.6)
  - A 级：Cox–Katz 1999, §5.1.3, 印刷 p.75（PDF p.98），单值性定理 [Landman]：(T^m−I)^{n+1}=0
  - A 级：Morrison 1993, JAMS 6, 223–247（本书 p.42 的引用来源：极小整消失圈与 m=1）
  - A 级：Landman 1973, Trans. AMS 181, 89–126（Picard–Lefschetz 变换与单值性定理）
  - B 级：Cox–Katz 1999, 第 5 章 §5.2（最大幺幂）、§5.6.1（镜像映射周期比）节号索引
  - B 级：nLab, "vanishing cycle" 与 "Picard–Lefschetz formula"（索引级；版本与条目号待核）
status: draft
review:
  drafter: agent-229
  reviewer: lead
  blindtest: pending
glossary_refs: [vanishing cycle（消失圈，frozen）, cycle（圈，frozen）, monodromy（单值性）, maximally unipotent（最大幺幂）]
symbols_refs: [γ0, γ1, T, N, m, t, q]
updated: 2026-11-20
---

# MS-14 消失圈

## 1. 一句话

随参数趋于边界点而收缩为一点的整同调圈；本书用它定义镜像映射。

## 2. 为什么需要它

- **把周期比变成良定义的函数。** 镜像映射取 $t=\int_{\gamma_1}\Omega/\int_{\gamma_0}\Omega$；分母与分子都是一个圈上的周期，$\gamma_0$ 是其中在单值性下不变的那个，于是比值的单值性只剩 $t\mapsto t+1$，$q=e^{2\pi it}$ 才单值（印刷 p.19／PDF p.42，式 (2.6)）。
- **给单值性算子一个几何载体。** 第 5 章把单值性写成 $T=\exp N$、$N=\log T$（PDF p.98）；消失圈是 $N$ 作用最简的向量：$N\gamma_0=0$、$N\gamma_1=m\gamma_0$（PDF p.42），并与对偶基 $g_i$ 满足 $N(g_1)=g_0$（PDF p.101–102、p.132）。
- **决定 $q$ 的归一化常数。** $\gamma_1$ 只能定到「加 $\gamma_0$ 的整数倍」，故 $q$ 只定到常数 $c_1$：$q=c_1(x-770x^2+\cdots)$；$c_1=-1$ 需另外证明（印刷 p.20–21／PDF p.43–44）。
- **几何退化与物理的交叉口。** 单结点锥形奇点处单值性幺幂但非最大幺幂，$N^2=0$（PDF p.104），几何上恰有一个 $S^3$ 收缩；锥形奇点跃迁中该圈对应变无质量的 D3 膜／带电黑洞（PDF p.167、p.427–428）。
- **通向权滤过与高维情形。** $g_0\in W_0$、$g_1\in W_2$，故 $\hat q=\exp(2\pi i\langle g_1,\Omega\rangle)$（PDF p.132）；$r>1$ 时这一构造以整性猜想 $(m_{jk})$ 在 $\mathbb Z$ 上可逆为代价（PDF p.104–105）。

## 3. 定义（全假设）

设 $\pi:X\to\Delta$ 是 $\Delta=\{t:|t|<\varepsilon\}$ 上的光滑族，$X_t$ 为紧 Kähler 流形，$\dim_{\mathbb C}X_t=n$（本书主用 $n=3$）；记 $\Delta^*=\Delta\setminus\{0\}$，固定 $t\in\Delta^*$。

1. **局部单值性。** 取 $\Delta^*$ 中以 0 为圆心、逆时针定向的小回路，沿其解析延拓得到**单值性变换** $T\in \mathrm{GL}\big(H_n(X_t,\mathbb Z)\big)$；$T$ 与回路的选取（同伦类内）无关，且不依赖 $t$（PDF p.98）。这是本书「单值性」的唯一含义（术语裁定见冲突表 T1）。
2. **光滑性假设。** 只要求 $\pi$ 在 $\Delta^*$ 上光滑；$X_0$ 允许有奇点——消失圈正是描述 $X_0$ 奇点「在 $X_t$ 里剩下什么」的对象。
3. **结点情形（几何标准版）。** 设 $X_0$ 有孤立结点（ordinary double point，三维时即**锥形奇点**／conifold），局部解析模型为 $z_0^2+\cdots+z_n^2=0$。取 $0<|t|\ll\varepsilon$，令
   $$\Delta_t=\Big\{\sqrt t\,u:\ u\in\mathbb R^{n+1},\ u_0^2+\cdots+u_n^2=1\Big\}\cong S^n$$
   （$\sqrt t$ 任取一支；$t>0$ 时 $\Delta_t$ 就是 $X_t$ 的实点集）。其整同调类 $\delta=[\Delta_t]\in H_n(X_t,\mathbb Z)$ 称为该结点的**消失圈**（$n=3$ 时叫消失球）。$\delta$ 在 $T$ 下不变：$T\delta=\delta$；若 $X_0$ 有 $\kappa$ 个结点，则得到 $\kappa$ 个可取得彼此不交的消失圈。
4. **Picard–Lefschetz 公式。** 结点情形下对一切 $\gamma\in H_n(X_t,\mathbb Z)$，
   $$T\gamma=\gamma+(-1)^{n(n+1)/2}(\gamma\cdot\delta)\,\delta .$$
   本书没有显式写出这条一般公式（只把它命名为「Picard–Lefschetz 变换」，PDF p.98）；$n=3$ 时符号为 $+$。
5. **最大幺幂情形（本书 p.42 实际使用的版本）。** 设 0 是**最大幺幂边界点**（定义见 MS-12：$T_i$ 全幺幂、$\dim W_0=1$、$\dim W_2=1+r$ 且 $(m_{ij})$ 可逆，PDF p.104）。令 $N=\log T$，则 $N^n\ne0$、$N^{n+1}=0$。称 $\gamma_0\in H_n(X_t,\mathbb Z)$ 为**极小整消失圈**，若它是本原整类且 $N\gamma_0=0$（等价于 $T\gamma_0=\gamma_0$），即 $\gamma_0$ 生成 $W_0\cap H_n(X_t,\mathbb Z)$；称 $\gamma_1\in H_n(X_t,\mathbb Z)$ 为**极小整圈**，若 $N\gamma_1=m\gamma_0$，$m\in\mathbb Z$（等价于 $T\gamma_1=\gamma_1+m\gamma_0$）。此时 $\gamma_0$ 除符号外唯一，$\gamma_1$ 除符号与「加 $\gamma_0$ 的整数倍」外唯一；五次三维簇 $m=1$ [Morrison2]（PDF p.42）。
6. **锥形奇点处的计数版本。** 若边界点处 $X_0$ 恰有 $\kappa$ 个结点，则消失同调由 $\kappa$ 个 $S^n$ 张成；单参数三维族在锥形点处可证 $N^2=0$，但它一般**不是**最大幺幂点（PDF p.104；判别式主分支的一般点恰有一个结点，PDF p.145）。
7. **术语。** 本书用「消失圈」；「消失球」指第 3 条中的 $S^n$ 本身（标准用法，本书 p.42 未用）；「单值性变换即 Picard–Lefschetz 变换」（PDF p.98）。

**本书用法。** Cox–Katz 在 PDF p.42（印刷 p.19）用的是第 5 条的 MUM 版本，而不是教材中最常见的第 3 条结点版本：$x=0$ 处是最大幺幂边界点，那里没有球面收缩，只有 $W_0$ 中的极小整类；真正的单结点锥形奇点在另一边界点 $x=-5^{-5}$（PDF p.104、p.145），那里才是收缩 $S^3$ 的几何情形。本书没有写出第 3、4 条的一般陈述，只有第 5 条的 $n=3$、$m=1$ 实例与第 4 条的命名（PDF p.98），故第 3、4 条按标准理论补足并计入 A 级来源（[Landman]、[Morrison2]，见 §8）。

## 4. 最小例子（能算出）

### 4.1 局部模型：$A_1$ 结点的消失球

取 $n=3$，$X_t=\{z_0^2+z_1^2+z_2^2+z_3^2=t\}\subset\mathbb C^4$。

- **球面。** $\Delta_t=\{\sqrt t\,u:\ u\in\mathbb R^4,\ u_0^2+u_1^2+u_2^2+u_3^2=1\}$：取实解（$t>0$ 时它就是 $X_t$ 的实点集），$\sum u_i^2=1$ 是 $\mathbb R^4$ 中的单位球面，乘 $\sqrt t$ 后仍微分同胚于 $S^3$，并在 $t\to0$ 时缩为结点。
- **自交。** $n=3$ 为奇数，$H_3$ 上相交形式斜对称，故 $\delta\cdot\delta=0$（与 $T\delta=\delta$ 相容）。
- **单值性。** 沿 $t\mapsto e^{2\pi i\theta}t$（$\theta\in[0,1]$）延拓有 $z_i\mapsto e^{\pi i\theta}z_i$；其一阶效应即第 4 条的 Picard–Lefschetz 公式，$n=3$ 时
  $$T\gamma=\gamma+(\gamma\cdot\delta)\delta,\qquad N\gamma=(\gamma\cdot\delta)\delta,\qquad N^2=0 .$$
- **与本书的接口。** 取 $\gamma_1$ 使 $\gamma_1\cdot\delta=1$，得 $T\gamma_1=\gamma_1+\delta$，即 $m=1$：第 5 条中 $m=1$ 的几何来源就是 $m=\gamma_1\cdot\gamma_0$（符号随定向，见 §11）。在基 $(\gamma_0,\gamma_1)$ 下
  $$T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad N^2=0 .$$

### 4.2 全局模型：五次镜像族的锥形点只收缩一个 $S^3$

取 PDF p.39–40 的五次族 $f_\psi=x_1^5+x_2^5+x_3^5+x_4^5+x_5^5+\psi x_1x_2x_3x_4x_5=0$，镜像模坐标为 $x=\psi^{-5}$（PDF p.41）。

1. 临界点条件：$\partial f_\psi/\partial x_i=5x_i^4+\psi\prod_{j\ne i}x_j=0$。两边乘 $x_i$，记 $e=\prod_j x_j$，得 $5x_i^5+\psi e=0$（对每个 $i$）。
2. 若 $e=0$，则一切 $x_i=0$，不是 $\mathbb P^4$ 的点；故 $e\ne0$、一切 $x_i\ne0$，且所有 $x_i^5=-\psi e/5$ 相等。写 $x_i=\zeta_i x_1$，$\zeta_i\in\mu_5$，$\zeta_1=1$。
3. 代入 $f_\psi=0$：$e=x_1^5\prod\zeta_i$，故 $x_1^5=-\psi e/5$ 给出 $1=-\psi\prod\zeta_i/5$，即 $\psi=-5/\prod\zeta_i$；此时 $f_\psi=x_1^5(5+\psi\prod\zeta_i)=0$ ✓。
4. 取 $\psi=-5$（即 $x=(-5)^{-5}=-5^{-5}$）：条件化为 $\prod_i\zeta_i=1$，于是临界点为 $[1:\zeta_2:\zeta_3:\zeta_4:\zeta_5]$，$\zeta_i^5=1$、$\zeta_2\zeta_3\zeta_4\zeta_5=1$，共 $5^3=125$ 个（均非退化，即结点；结点性本卡未逐项验证，见 §11）。
5. $G=\{a\in(\mathbb Z/5)^5:\sum a_i\equiv0\bmod 5\}/\mathbb Z_5\cong(\mathbb Z/5)^3$ 阶为 125，按 $(x_i)\mapsto(\zeta^{a_i}x_i)$ 作用。它在 125 个结点上**自由且传递**（坐标全非零 ⇒ 稳定子平凡；给定目标 $(\eta_i)$，取 $g_1\in\mu_5$、$g_i=g_1\eta_i/\zeta_i$，则 $\prod g_i=g_1^5\prod\eta_i/\prod\zeta_i=1$）。故商族 $V_\psi/G$（即镜像族）在 $x=-5^{-5}$ 处**恰有 1 个结点**，其邻近光滑纤维恰有一个消失 $S^3$——与 PDF p.104「此时 $N^2=0$」、PDF p.145「判别式主分支一般点有一个结点」互检；数值上 $h^{2,1}=1$、$b_3=204=2+2\cdot101$，与 MS-22 的锥形奇点跃迁 $b_3:204\to202$ 一致。

### 4.3 数值链（本书 p.42–44）

- $m=1$ ⇒ $\dfrac{\int_{\gamma_1}\Omega}{\int_{\gamma_0}\Omega}\mapsto$ 自身 $+1$，故 $t=y_1/y_0$、$q=e^{2\pi it}$ 单值（式 (2.6)）。
- $y_0,y_1$ 满足式 (2.8)（PDF p.43）；$y_0=\sum_{n\ge0}\frac{(5n)!}{(n!)^5}(-1)^nx^n=1-120x+\frac{10!}{(2!)^5}x^2-\cdots$，其中 $\frac{10!}{2^5}=\frac{3628800}{32}=113400$，即 $y_0=1-120x+113400x^2-\cdots$（式 (2.11)）。
- $q=c_1(x-770x^2+\cdots)$（式 (2.9)）；取 $c_1=-1$（PDF p.43–44 由镜像对称定出），$x=10^{-4}$ 时 $q\approx-10^{-4}+770\cdot10^{-8}=-9.23\times10^{-5}$。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页／文献） | 备注 |
|---|---|---|---|
| 1 | $\gamma_0$ 在单值性下不变；$\gamma_1\mapsto\gamma_1+m\gamma_0$，五次三维簇 $m=1$ | 印刷 p.19（PDF p.42），[Morrison2] | 本书唯一系统用法 |
| 2 | $\gamma_0$ 除符号外唯一；$\gamma_1$ 除符号与 $\gamma_0$ 整数倍外唯一；故比值与 $\Omega$ 无关 | 印刷 p.19（PDF p.42） | 于是 $q$ 只差常数 $c_1$ |
| 3 | 绕 $x=0$ 一周 $\int_{\gamma_1}\Omega/\int_{\gamma_0}\Omega$ 增加 1，$q=\exp(2\pi i t)$ 单值 | 印刷 p.19（PDF p.42）；p.109（PDF p.132） | 镜像映射的基石 |
| 4 | 单值性定理：存在整数 $m\ge0$ 使 $(T^m-I)^{n+1}=0$ | 印刷 p.75（PDF p.98），[Landman] | 中译本作 $m>0$，已登冲突表 MS-13 |
| 5 | 最大幺幂点：$N^d\ne0$、$N^{d+1}=0$；三维单参数族 $N^3\ne0$ | 印刷 p.81–82（PDF p.104–105），[Morrison2] | $h^{2,1}=1\Rightarrow h^3=4$ |
| 6 | 单结点锥形点：单值性幺幂但非最大幺幂，$N^2=0$ | 印刷 p.81（PDF p.104）；p.122（PDF p.145） | 恰一个消失 $S^3$ |

## 6. 推导流程（D1…D8）

- **D1 族与两个边界点。** 五次族 $f_\psi$ 在 $\psi=-5\mu^i$ 处奇异；取 $x=\psi^{-5}$，复模边界点为 $x=0$ 与 $x=-5^{-5}$（PDF p.39–41，印刷 p.16–18）。
- **D2 判定最大幺幂。** 只有 $x=0$ 具最大幺幂单值性，理由是 $\star H$ 最大幂零：$(\star H)^3\ne0$、$(\star H)^4=0$（PDF p.41，印刷 p.18）；一般地由指标方程 $(\lambda-\ell)^4=0$ 判定（PDF p.102 命题，印刷 p.79）。
- **D3 消失圈的存在与唯一性。** 在 $x=0$ 附近取极小整消失圈 $\gamma_0$（单值性不变）与极小整圈 $\gamma_1$（$T\gamma_1=\gamma_1+m\gamma_0$），五次 $m=1$，并断言 $\gamma_0$ 除符号、$\gamma_1$ 除符号与整数倍外唯一 [Morrison2]（PDF p.42，印刷 p.19）。
- **D4 周期比的单值性。** 由 D3，$t=y_1/y_0$ 在单值性下 $t\mapsto t+1$，故 $q=e^{2\pi it}$ 是 $x=0$ 邻域上的良定义函数（PDF p.42，式 (2.6)）。
- **D5 用 Picard–Fuchs 方程算级数。** $y_0,y_1$ 满足式 (2.8)；用超几何解法得 $y_0=1-120x+113400x^2-\cdots$、$q=c_1(x-770x^2+\cdots)$（PDF p.43，印刷 p.20，式 (2.9)、(2.11)）；$c_1$ 的整数格丢失即由 $\gamma_1$ 的整数倍歧义造成（同页）。
- **D6 归一化 $c_1=-1$。** 用镜像对称（Yukawa 耦合的匹配）证明 $c_1=-1$，从而 $q=-x\exp\big(\frac{5}{y_0}\sum_{n\ge1}\cdots\big)$（PDF p.43–44，印刷 p.20–21，式 (2.12)）。
- **D7 权滤过与对偶表述。** $g_i$ 与 $\gamma_i$ 庞加莱对偶，$g_0\in W_0$、$g_1\in W_2$、$N(g_1)=g_0$，归一化后 $\hat q=\exp(2\pi i\langle g_1,\Omega\rangle)$（PDF p.101–102、p.132，印刷 p.78–79、p.109）；$r$ 维情形要求 $(m_{jk})$ 整可逆（PDF p.104–105 的整性猜想 [Morrison6]）。
- **D8 锥形点与几何解释。** 在 $x=-5^{-5}$ 处 $N^2=0$（PDF p.104，印刷 p.81），恰一个结点（PDF p.145，印刷 p.122）；锥形奇点跃迁中该圈对应变无质量的 D3 膜／黑洞（PDF p.167、p.427–428，印刷 p.144、p.404–405）。

## 7. 常见误解与反例（≥2）

1. **误解：消失圈就是收缩为一点的球面。** 反例：本书 p.42 的 $\gamma_0$ 位于最大幺幂点 $x=0$，那里没有任何球面收缩；SY01-24 原书 p.18–19 把大复结构极限处的消失循环显式写成 SYZ 的 $T^3$ 环面 $\beta_0$，不是 $S^3$。球面情形出现在锥形点 $x=-5^{-5}$（PDF p.104、p.145），即 §4.1、§4.2。
2. **误解：消失圈就是被单值性移动的那个圈。** 反例：按 PDF p.42，不变的是 $\gamma_0$，被移动的是 $\gamma_1$（$\gamma_1\mapsto\gamma_1+m\gamma_0$）。若把两者互换，$t$ 的变换方向随之改变，$q=e^{2\pi it}$ 将不再单值，式 (2.6) 失效。
3. **误解：消失圈唯一确定，故 $q$ 没有常数歧义。** 反例：$\gamma_0$ 只定到符号，$\gamma_1$ 还差 $\gamma_0$ 的整数倍，故 $q$ 只定到常数 $c_1$（式 (2.9)，PDF p.43）；$c_1=-1$ 必须靠镜像对称另证（PDF p.43–44），这正是 MS-02 的内容。
4. **误解：单参数族之外也能直接取同一消失圈。** 反例：$r$ 维最大幺幂点处一般用 $g_0\in W_0$ 与矩阵 $(m_{jk})$ 描述，后者在 $\mathbb Z$ 上可逆仅是猜想（PDF p.104–105，[Morrison6]）；本书对一般簇的镜像映射建立在该猜想上，$m_{jk}$ 的整性只在五次族等例子中验证（[Morrison2]）。
5. **误解：锥形奇点跃迁的 16 个结点与镜像族的 1 个结点是同一件事。** 反例：PDF p.167 例题 6.2.4(1) 是 $\overline V\subset\mathbb P^4$ 中含平面的五次超曲面，有 16 个结点；PDF p.145 的「一个结点」是判别式主分支一般点（环面超曲面模空间）的奇点类型。两者构造不同，本卡 §4.2 的 125→1 属于后者（见 §11）。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999（本书） | §2.3，印刷 p.19（PDF p.42），式 (2.6)；索引「vanishing cycle, 19」 | 唯一系统定义：极小整消失圈 $\gamma_0$、极小整圈 $\gamma_1$、$m=1$、$q$ 公式 |
| 同上 | §5.1.3，印刷 p.75（PDF p.98） | 单值性变换「也称 Picard–Lefschetz 变换」；单值性定理 [Landman] |
| 同上 | §5.2.1，印刷 p.78–79（PDF p.101–102），指标方程命题 | 最大幺幂的 Jordan 形、$N=\log T$、$g_i\leftrightarrow\gamma_i$ 对偶 |
| 同上 | §5.2.1 末，印刷 p.81（PDF p.104） | 锥形点 $x=-5^{-5}$：幺幂但非最大幺幂，$N^2=0$ |
| 同上 | §5.6.1，印刷 p.109（PDF p.132） | $\hat q=\exp(2\pi i\int_{\gamma_1}\Omega/\int_{\gamma_0}\Omega)$；$N(g_1)=g_0$ |
| 同上 | §6.1，印刷 p.122（PDF p.145） | 判别式主分支一般点 = 一个结点的超曲面（三维结点即锥形奇点） |
| 同上 | §6.2.3，印刷 p.144（PDF p.167），例 6.2.4(1) | 五次锥形奇点跃迁：16 个结点、$H^3=5\ne0$、光顺化为五次三维簇 |
| 同上 | §12，印刷 p.404–405（PDF p.427–428） | 消失圈（三维膜／D3 膜）↔ 带电黑洞在簇变奇异时质量变为零 |
| SY01-24（Siebert 讲义中译本） | 第 1 章，原书 p.18–19；术语表 #15 | 消失循环 $=\beta_0=T^3$ 的显式 SYZ 模型（大复结构极限）。**冲突**：术语「消失循环」与本书「消失圈」不一致（冲突表 T2 已裁定「消失圈」）→ §11 C1。**冲突**：它把消失循环显式认成 SYZ 的 $T^3$ 环面并给辛基 $\beta_0,\beta_1,\alpha_1,\alpha_0$，本书 p.42 只用抽象极小整类、未给环面模型 → §11 C2 |
| SY01-25（Kontsevich–Soibel'man 中译本资料卡 04） | §二 文献表 [Se]「消没圈与变异」；其 25 条术语表无 vanishing cycle 条目 | 第三种译法「消没圈」，语境为 Fukaya／$A_\infty$ 辛侧。**冲突**：术语与语境都与本书不同，本书不展开辛侧（冲突表 U4）→ §11 C3 |
| Morrison 1993（原始文献，本书 p.42 引用） | JAMS 6, 223–247 | $h^{2,1}=1$ 情形的极小整消失圈与 $m=1$，本书 p.42 的直接来源 |
| Landman 1973（原始文献，本书 p.98 引用） | Trans. AMS 181, 89–126 | $(T^m-I)^{n+1}=0$ 的单值性定理 |
| Greene–Morrison–Strominger 1995（原始文献，本书 p.167 引用） | Nucl. Phys. B451, 109 | 锥形奇点跃迁与无质量黑洞 |

## 9. 前置与后继

- **前置。** MS-12（单值性与最大幺幂）：本卡第 5 条的 MUM 定义、$N=\log T$、权滤过 $W_\bullet$ 直接借用（PDF p.98–105）；MS-10（Hodge 结构与滤过）；MS-06（Picard–Fuchs 方程：$y_0,y_1$ 满足式 (2.8)）。书内阅读顺序：§2.2–2.3（PDF p.39–42）→ §5.1.3（PDF p.98）→ §5.2.1（PDF p.101–104）→ §5.6.1（PDF p.132）。
- **后继。** MS-02（镜像映射：用 $\gamma_0,\gamma_1$ 得 $t,q$，PDF p.42–44）；MS-13（单值性定理的定量版）；MS-22（极端跃迁与锥形奇点跃迁：锥形点的几何侧，PDF p.145、p.167、p.427–428）；MS-18（Frobenius 流形：$t$ 坐标下 Yukawa 耦合）。
- **不覆盖。** 辛侧 Fukaya 范畴里的 vanishing cycle（SY01-25 语境，冲突表 U4）本书不展开，本卡亦不展开。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- Mathlib 无 Picard–Lefschetz 理论；本块只给陈述级接口，证明一律 sorry。
namespace MirrorSymmetry

/-- 整同调上的局部单值性：T 为绕边界点一周的自同构，N 为 T − I 的幺幂线性化。 -/
structure LocalMonodromy (H : Type) [AddCommGroup H] where
  T : H ≃+ H
  N : H →+ H
  unipotent : ∀ v, T v = v + N v

/-- 结点（三维锥形奇点）的消失圈：δ 在 T 下不变，(T−I)² = 0，
    且 T 是单次 Picard–Lefschetz 变换（n = 3 时符号为 +）。 -/
structure VanishingCycle (H : Type) [AddCommGroup H] where
  mono : LocalMonodromy H
  delta : H
  intersection : H → ℤ
  fixed : mono.T delta = delta
  nilpotent_sq : ∀ v, mono.N (mono.N v) = 0
  picard_lefschetz : ∀ v, mono.T v = v + (intersection v) • delta

/-- 最大幺幂点处的极小整消失圈 γ₀ 与极小整圈 γ₁（Cox–Katz, 印刷 p.19）。 -/
structure MUMVanishingPair (H : Type) [AddCommGroup H] where
  mono : LocalMonodromy H
  gamma0 : H
  gamma1 : H
  m : ℤ
  invariant_gamma0 : mono.N gamma0 = 0
  shifted_gamma1 : mono.N gamma1 = m • gamma0
  quintic_m : m = 1 -- 五次三维簇，[Morrison2]

/-- 周期比 t = ∫_{γ₁}Ω / ∫_{γ₀}Ω 在单值性下满足 t ↦ t + 1，故 q = exp(2πit) 单值。 -/
theorem period_ratio_shift (H : Type) [AddCommGroup H] (P : MUMVanishingPair H) :
    True := by sorry

end MirrorSymmetry
```

## 11. 待核清单

- [ ] **C1（术语）** SY01-24 作「消失循环」、SY01-25 资料卡 04 作「消没圈」，本书与 glossary 裁定作「消失圈」（冲突表 T2）→ §8 第 9、10 行。只登记差异、不判定对错；SY01-24 原书 p.18 的定义原文未逐字核对。
- [ ] **C2（表述粒度）** SY01-24 p.18–19 把消失循环显式写成 SYZ 的 $T^3=\beta_0$ 并给辛基 $\beta_0,\beta_1,\alpha_1,\alpha_0$、$N=T-I$；本书 p.42 只用抽象极小整类，未给环面模型 → §8 第 9 行。两者是否同一对象待核：同样的极限（$x=0$／$\psi=\infty$）但坐标换算 $x=\psi^{-5}$ 与 SY01-24 的 $z=(1/(5\psi))^5$ 未逐项验证。
- [ ] **C3（语境）** SY01-25 的「消没圈」出现在 Fukaya／$A_\infty$ 辛侧（[Se] 消没圈与变异）；本书不展开辛侧（冲突表 U4）→ §8 第 10 行。是否需在本卡补辛侧对应关系，待项目裁定。
- [ ] **队列定位不符**：`_queue.md` 写 MS-14 位于「第 5 章 §5.1.2；第 3 章 §3.5」，实际定义在 §2.3（PDF p.42），第 5 章仅在 §5.1.3／§5.2.1（PDF p.98–104）作框架，第 3 章无消失圈内容 → 需维护者更正（本卡不改既有文件）。
- [ ] **Picard–Lefschetz 公式符号**：一般形式 $T(\gamma)=\gamma+(-1)^{n(n+1)/2}(\gamma\cdot\delta)\delta$ 本书未显式陈述（只有 PDF p.42 的 $n=3$、$m=1$ 实例与 p.98 的命名）；$n=3$ 时取 $+$，故 $m=\gamma_1\cdot\gamma_0$。定向与符号约定需对 [Landman] 定理号核一次。
- [ ] **§4.2 的 125→1 推导**：临界点计数 125 由方程直接解出，可信；但结点性（Hessian 非退化）与 $G$ 在结点集上传递性的逐项验证本卡未做，仅与 PDF p.104「$N^2=0$」、p.145「一个结点」互检 → 需补标准文献页码。
- [ ] **p.167 的 16 结点例题**与本卡 §4.2 的「1 个结点」是不同构造（前者是 $\overline V\subset\mathbb P^4\times\mathbb P^1$ 的跃迁，后者是判别式主分支一般点），§7 误解 5 已注明；二者关系待核（转 MS-22）。
- [ ] **式编号**：式 (2.6)、(2.9)、(2.11) 由 `chapter02.tex` 中 `\label` 顺序推定（与 MS-06 卡「式 (2.8)=PF 方程」一致），印刷版定稿前需核一次。
- [ ] **B 级来源**：nLab 的 "vanishing cycle"／"Picard–Lefschetz formula" 条目号与版本未取；Stacks Project 是否有对应条目待核，当前 B 级主要靠书内节号索引。
