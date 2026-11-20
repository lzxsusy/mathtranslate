---
id: MS-18
zh: Frobenius 流形与 Dubrovin 联络
en: Frobenius manifold and Dubrovin connection
aliases: [Dubrovin 形式体系, Dubrovin formalism, 形式 Dubrovin 联络]
layer: L1
prereqs: [MS-04, MS-11]
sources:
  - "A 级：Cox–Katz 1999, §8.4, PDF p.262–265（印刷 p.239–242）：式 (8.35)–(8.36)、二元运算 $*$ 与 Dubrovin 联络 $\\nabla^\\lambda$（p.262）；命题 8.4.1（p.263）；$\\nabla^\\lambda_{\\partial/\\partial t_i}(T_j)=\\lambda T_i*T_j$、Euler 场、Frobenius 流形的例子（p.264）；形式 Dubrovin 联络（p.265）"
  - "A 级：Cox–Katz 1999, §8.5.2–8.5.3, PDF p.266–269（印刷 p.243–246）：A 模型联络（p.266–267）；命题 8.5.2（p.267–268）；命题 8.5.3（p.269）"
  - "A 级：Cox–Katz 1999, §8.5, PDF p.277（印刷 p.254）：定理 8.5.11（A 型极化 Hodge 结构变分）"
  - "A 级：Cox–Katz 1999, §8.6, PDF p.280–282（印刷 p.257–259）：定义 8.6.1、定理 8.6.2"
  - "A 级：Dubrovin 1992, Nuclear Phys. B379, 627–689（本书 [Dubrovin1]）；Dubrovin 1996, LNM 1620, 120–348（[Dubrovin2]）；Kontsevich–Manin 1994, Comm. Math. Phys. 164, 525–562（[KoM1]）"
  - "B 级：本书 §8.4 节；Manin 1999, Frobenius Manifolds, Quantum Cohomology, and Moduli Spaces, AMS Colloq. Publ. 47（与本书 [Manin3] 预印本同源的标准综述）"
status: draft
review:
  drafter: agent-232
  reviewer: lead
  blindtest: pending
glossary_refs: ["SY01-24 #5 Yukawa 耦合", "SY01-24 #17 Gauss–Manin 联络", "SY01-24 #18 单值变换（本书作「单值性」）"]
symbols_refs: ["$A_{ijk}$", "$A_{ij}^{\\,k}$", "$\\nabla^\\lambda$", "$\\lambda$", "$\\Phi$", "$E$"]
updated: 2026-11-20
---

# MS-18 Frobenius 流形与 Dubrovin 联络

## 1. 一句话
量子乘法给出的平坦联络使上同调成为 Frobenius 流形。

## 2. 为什么需要它
- 镜像猜想要说清「两边同构」，必须给 A 模型一侧一个可比较的几何对象：定义 8.6.1（PDF p.280–281）要求镜像映射提升为保持两个**极化 Hodge 结构变分**的丛同构，而 A 模型那一侧的变分正是用 Dubrovin 联络构造的（定理 8.5.11, PDF p.277）。
- 把结合律升级为几何：$\nabla^\lambda$ 平坦 ⟺ $F$ 满足 WDVV ⟺ $*$ 结合（PDF p.263）。于是平坦联络、单值性、极限混合 Hodge 结构这一整套工具可用（§8.5, PDF p.265–277），不必停在「环是否结合」的代数验证上。
- §8.4 不只对 $\Phi$ 定义，而依 [Dubrovin1] 对任意偶势 $F$ 发展一般理论（PDF p.262）；凡满足 WDVV 的偶 $F$ 都给出与 GW 类相似的 CohFT 结构（PDF p.264），这是 Givental 联络 $\nabla^g$（PDF p.268）与 MS-19 量子超平面截面原理的入口。
- 计算上：五次族的 3 点函数 $\Phi_{111}=5+2875q+\cdots$ 与 B 模型归一化 Yukawa 耦合，只在 Frobenius 流形框架里才能逐项对齐（定理 8.6.2, PDF p.282）。

## 3. 定义（全假设）
（背景）设 $X$ 为光滑射影簇；$H^*(X,\mathbb{C})$ 有限维，Poincaré 配对 $g(a,b)=\int_Xa\cup b$ 非退化对称（命题 8.1.6, PDF p.244）；取齐次基 $T_0=1,\dots,T_m$，对应**超交换**变量 $t_0,\dots,t_m$，$(g_{kl})$ 为配对矩阵、$(g^{kl})$ 为其逆。

（定义，PDF p.262）设 $F$ 是 $t_i$ 的**偶形式幂级数**（好情形下在超流形 $H^*(X,\mathbb{C})$ 的某开集收敛）。定义：
1. $A_{ijk}=\dfrac{\partial^3F}{\partial t_i\partial t_j\partial t_k}$（式 (8.35)）；$A_{ij}^{\,k}=\sum_lA_{ijl}g^{lk}$（式 (8.36)，升指标）。
2. 二元运算 $T_i*T_j=\sum_kA_{ij}^{\,k}T_k$。
3. **Dubrovin 联络** $\nabla^\lambda_{\partial/\partial t_i}\big(\partial/\partial t_j\big)=\lambda\sum_kA_{ij}^{\,k}\partial/\partial t_k$，其中 $\lambda\in\mathbb{C}^\times$。
4. **全部假设**：$F$ 满足 **WDVV 方程** $\sum_aA_{ij}^{\,a}A_{ak}^{\,l}=(-1)^{\deg t_i(\deg t_j+\deg t_k)}\sum_aA_{jk}^{\,a}A_{ai}^{\,l}$（PDF p.263；对 $F=\Phi$ 即定理 8.2.4，PDF p.255–256），且 $A_{0ij}=g_{ij}$ 对所有 $i,j$。
5. 上述假设下：$\nabla^\lambda$ 平坦且无挠，$\nabla^\lambda_{\partial/\partial t_0}=\lambda\,\mathrm{id}$，且 $(H^*(X,\mathbb{C}),*,g)$ 逐点是 Frobenius 代数（命题 8.4.1, PDF p.263）。
6. **Frobenius 流形的本书用法**（PDF p.264）：超流形 $H^*(X,\mathbb{C})$ 连同度量 $g$、满足 WDVV 的偶势 $F$，以及「由量子乘法给出的联络」$\nabla^\lambda_{\partial/\partial t_i}(T_j)=\lambda\,T_i*T_j$，合起来是 Frobenius 流形的一个例子；$\Phi$ 的齐次性在联络语言中表现为存在偶 **Euler 向量场 $E$**（与 $\nabla^\lambda$ 相容）；把 $\lambda$ 看作 $\mathbb{P}^1$ 的仿射坐标时 $\nabla^\lambda$ 延拓为 $\widehat\nabla$，在 $\lambda=0,\infty$ 有奇点（PDF p.264）。
- 对照物：**Frobenius 代数** = 有限维、有单位 $1$ 的交换结合代数 + 非退化对称双线性型 $\langle\,,\rangle$，满足 $\langle a*b,c\rangle=\langle a,b*c\rangle$（附录 B, PDF p.455；本书 §8 只引用该定义）。
**本书用法（与标准定义的出入）**：Cox–Katz **没有**给 Frobenius 流形编号定义，p.264 仅以「一个例子」引入；形式公理化（平坦度量、Euler 场、$\mathbb{P}^1$ 延拓、形式情形）须回 [Dubrovin1,2]、[Manin3]。另注意本书版本是**带次数的**：$t_i$ 有 $\deg$、$F$ 偶、$E$ 齐次，所以不等于「一族 Frobenius 代数」。

## 4. 最小例子（能算出）
### 4.1 $\mathbb{P}^2$：从 GW 势算 $*$、$\nabla^\lambda$ 与 WDVV 的一个分量
书内数据（§8.3.2, PDF p.259–260）：$T_0=[\mathbb{P}^2]$、$T_1=[\ell]$、$T_2=[\mathrm{pt}]$，$\deg t_0=-2,\deg t_1=0,\deg t_2=2$，$q=q^\ell$，$N_d$ = 过 $3d-1$ 个一般位置点的 $d$ 次有理曲线数，
$$\Phi=\frac12(t_0^2t_2+t_0t_1^2)+\sum_{d\ge1}N_d\,e^{dt_1}\frac{t_2^{3d-1}}{(3d-1)!}q^d .$$
(1) 配对：$g_{ij}=\int_{\mathbb{P}^2}T_i\cup T_j$，唯一非零的是 $g_{02}=g_{20}=g_{11}=1$，故 $g=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}=g^{-1}$。
(2) 单位元条件：$A_{002}=\partial_0^2\partial_2\Phi=1=g_{02}$，$A_{011}=\partial_0\partial_1^2\Phi=1=g_{11}$，$A_{012}=0=g_{12}$，即 $A_{0ij}=g_{ij}$（PDF p.263 的假设）。
(3) 取 $t_0=t_1=t_2=0$（即小量子乘积），由 $\Phi$ 的三阶导得 $A_{110}=1$、$A_{111}=A_{112}=A_{222}=0$、$A_{122}=N_1q=q$（$A$ 对指标全对称，故 $A_{221}=A_{122}=q$）；升指标（$g^{-1}=g$）得
$$T_1*T_1=T_2,\qquad T_1*T_2=qT_0,\qquad T_2*T_2=qT_1,$$
于是 $T_1*T_1*T_1=qT_0$，即 Frobenius 代数 $\mathbb{C}[T_1]/(T_1^3-q)$；结合律可直接验算：$(T_1*T_1)*T_1=T_2*T_1=qT_0=T_1*(T_1*T_1)$。书中对照：大量子乘积 $T_1*T_1=T_2+\Phi_{111}T_1+\Phi_{112}T_0\ne T_2$（PDF p.259），故大 $\ne$ 小。
(4) A 模型（=Dubrovin）联络矩阵：以 $u=u_1$、$q=e^{2\pi iu}$，$\nabla_{\partial/\partial u}(T_j)=T_1*T_j$ 的矩阵（列 $=$ $T_1*T_j$ 的坐标）为
$$M(u)=\begin{pmatrix}0&0&q\\1&0&0\\0&1&0\end{pmatrix},\qquad M^3=q\,I .$$
$M^3=qI$ 正是 $T_1^3=qT_0$ 的矩阵形式（一维 Kähler 基上 $\nabla^2=0$ 自动成立；非平凡的平坦性检验见 (5)）。
(5) WDVV 数值核验：取 $(i,j,k,l)=(1,1,2,2)$（PDF p.259）$\Phi_{222}+\Phi_{111}\Phi_{122}=\Phi_{112}^2$，比较 $q^2t_2^2$ 系数。由 $\Phi$ 得
$\Phi_{111}=\sum_dN_dd^3e^{dt_1}\frac{t_2^{3d-1}}{(3d-1)!}q^d$，$\Phi_{112}=\sum_dN_dd^2e^{dt_1}\frac{t_2^{3d-2}}{(3d-2)!}q^d$，$\Phi_{122}=\sum_dN_dde^{dt_1}\frac{t_2^{3d-3}}{(3d-3)!}q^d$，$\Phi_{222}=\sum_dN_de^{dt_1}\frac{t_2^{3d-4}}{(3d-4)!}q^d$（$\Phi_{222}$ 的 $d=1$ 项含因子 $3d-3=0$），故
$$\Phi_{222}\big|_{q^2t_2^2}=\tfrac12N_2e^{2t_1}t_2^2,\quad \Phi_{111}\Phi_{122}\big|_{q^2t_2^2}=\tfrac12N_1^2e^{2t_1}t_2^2,\quad \Phi_{112}^2\big|_{q^2t_2^2}=N_1^2e^{2t_1}t_2^2 .$$
方程化为 $\tfrac12N_2+\tfrac12N_1^2=N_1^2$，即 **$N_2=N_1^2$**；取 $N_1=1$ 得 $N_2=1$。再用书中递推（PDF p.260）：$d=3$ 时 $(d_1,d_2)=(1,2)$ 项为 $1\cdot4\cdot\binom51-1\cdot2\cdot\binom52=0$，$(2,1)$ 项为 $4\cdot1\cdot\binom54-8\cdot1\cdot\binom55=12$，故 $N_3=12$。

### 4.2 五次三维簇（队列指定的例子）
书内（§8.3.3, PDF p.260–262）：$V\subset\mathbb{P}^4$ 光滑五次，基 $T_0=[V],T_1=[H],T_2=[\ell],T_3=[\mathrm{pt}]$（$[\ell]$ 为直线类，$\int_VH\cup\ell=1$）及 $H^3$ 的基 $\gamma_1,\dots,\gamma_{204}$，
$$\Phi=\frac12t_0^2t_3+t_0t_1t_2+\frac56t_1^3-\sum_{i<j}q_{ij}t_0u_iu_j+\sum_{d\ge1}\langle I_{0,0,d}\rangle(e^{t_1}q)^d .$$
- 经典项给出 $\int_VT_1^3=\Phi_{111}\big|_{q=0}=5$；量子项给出 $T_1*T_1=\Phi_{111}T_2$，且 $\Phi_{111}=5+\sum_{d\ge1}\langle I_{0,0,d}\rangle d^3q^d=5+2875q+\cdots$（$n_1=2875$，第 2 章 PDF p.46；PDF p.261）。
- 因此 $\langle T_1,T_1,T_1\rangle=\int_VT_1*T_1*T_1=\Phi_{111}=5+2875q+\cdots$（PDF p.261），A 模型联络系数 $\nabla_{\partial/\partial u}(T_1)=(5+2875q+\cdots)T_2$ 就是三点函数；它与 B 模型归一化 Yukawa 耦合 $Y=5+2875q+\cdots$ 逐项相等，正是定理 8.6.2 的断言（PDF p.282）。

## 5. 关键性质（3–6 条，带出处）
| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | $\nabla^\lambda$ 挠率为零 ⟺ $A_{ij}^{\,k}=(-1)^{\deg t_i\deg t_j}A_{ji}^{\,k}$ ⟺ $*$ 超交换 | PDF p.262–263 | 由式 (8.35)(8.36) 直接算 |
| 2 | $\nabla^\lambda$ 平坦 ⟺ $F$ 满足 WDVV ⟺ $*$ 结合 | PDF p.263 | 曲率第一项由 $\partial_lA_{ij}^{\,k}=(-1)^{\deg t_i\deg t_l}\partial_iA_{lj}^{\,k}$ 消去 |
| 3 | $T_0$ 是 $*$ 单位元 ⟺ $A_{0ij}=g_{ij}$ ⟺ $\nabla^\lambda_{\partial/\partial t_0}(\partial/\partial t_i)=\lambda\partial/\partial t_i$ | PDF p.263 | 三者等价 |
| 4 | WDVV + $A_{0ij}=g_{ij}$ ⟹ $(H^*(X,\mathbb{C}),*,g)$ 是 Frobenius 代数（命题 8.4.1） | PDF p.263 | $\Phi$、$\Phi_{\mathrm{small}}$ 都满足 |
| 5 | $\nabla^\lambda_{\partial/\partial t_i}(T_j)=\lambda T_i*T_j$；把 $\lambda$ 看成 $\mathbb{P}^1$ 仿射坐标时延拓为 $\widehat\nabla$，$\lambda=0,\infty$ 有奇点 | PDF p.264–265 | 联络由量子乘法决定；$\mathbb{P}^2$ 时 $\widehat\nabla$ 的 Laplace 变换联系第六 Painlevé 方程；$F$ 为形式幂级数时称形式 Dubrovin 联络（p.265），收敛性未定（p.267） |
| 6 | A 模型联络 $=$ $\nabla^\lambda\big\vert_{\lambda=1/(2\pi i)}$；沿 $\Delta^r-D_\sigma$ 正则奇点、单值性幺幂，$N_j\sim-T_j\cup$；给出权 $d$ 极化 VHS | 命题 8.5.2（PDF p.267–268）；命题 8.5.3（PDF p.269）；定理 8.5.11（PDF p.277） | 镜像对的 A 侧对象（$\nabla^{\mathrm{middle}}$） |

## 6. 推导流程（D1…Dn）
- **D1（配对与基）** 取基 $T_0=1,\dots,T_m$ 与非退化配对 $g$；依据：命题 8.1.6（PDF p.244）。
- **D2（三阶张量）** $A_{ijk}=\partial^3F/\partial t_i\partial t_j\partial t_k$（式 (8.35), PDF p.262）；对 $F=\Phi$，$A_{ijk}=\langle I_{0,3}\rangle$ 类关联函数（引理 8.2.3）。
- **D3（乘法）** 升指标 $A_{ij}^{\,k}$（式 (8.36)），$T_i*T_j=\sum_kA_{ij}^{\,k}T_k$；依据：PDF p.262。
- **D4（Dubrovin 联络）** $\nabla^\lambda_{\partial/\partial t_i}(\partial/\partial t_j)=\lambda\sum_kA_{ij}^{\,k}\partial/\partial t_k$，$\lambda\ne0$；依据：PDF p.262。
- **D5（挠率与交换律）** 由 $A_{ij}^{\,k}=(-1)^{\deg t_i\deg t_j}A_{ji}^{\,k}$ 得挠率为零、$*$ 超交换；依据：PDF p.262–263。
- **D6（曲率与 WDVV）** 第一项为零（偏导恒等式）；第二项为零 ⟺ WDVV；WDVV ⟺ $*$ 结合（定理 8.2.4–8.2.5, PDF p.255–257；等价链见 PDF p.263）。
- **D7（单位元与 Frobenius 代数）** $A_{0ij}=g_{ij}$ ⟺ $T_0$ 单位元；命题 8.4.1 给出逐点 Frobenius 代数；依据：PDF p.263。
- **D8（联络即量子乘法）** 等同 $\partial/\partial t_i\leftrightarrow T_i$ 后 $\nabla^\lambda_{\partial/\partial t_i}(T_j)=\lambda T_i*T_j$；由 $F$ 偶 + WDVV + 单位元得 Frobenius 流形，齐次性 $\leftrightarrow$ Euler 场 $E$；依据：PDF p.264。
- **D9（限制到 $H^2$ 得 A 模型联络）** 引理 8.5.1（PDF p.265）把大量子乘积限制到 $H^2$；令 $u_j=t_j/(2\pi i)$、$q^\beta=e^{2\pi i\int_\beta\omega}$，命题 8.5.2（PDF p.267–268）证明 $\nabla=\nabla^\lambda\big|_{\lambda=1/(2\pi i)}$。
- **D10（单值性 → VHS → 镜像对）** 命题 8.5.3（PDF p.269）给正则奇点与幺幂单值性；定理 8.5.11（PDF p.277）得权 $d$ 极化 VHS；定义 8.6.1（PDF p.280–281）把它作为镜像映射提升要保的结构，定理 8.6.2（PDF p.282）化为 $Y_{ijk}=\langle T_i,T_j,T_k\rangle$。

## 7. 常见误解与反例（≥2）
1. **误解：「Frobenius 流形」就是「Frobenius 代数」的别名。** 错。Frobenius 代数（附录 B, PDF p.455）只是有限维代数 + 配对；Frobenius 流形要求在整族上 $F$ 满足 WDVV（$\Leftrightarrow\nabla^\lambda$ 平坦）、带 Euler 场，且 $\nabla^\lambda$ 由量子乘法给出（PDF p.263–264），命题 8.4.1 只断言「每一点上是 Frobenius 代数」。边界情形：任取一个 Frobenius 代数 $A$ 配三次型 $F$ 都得到系数为常数的「常值」Frobenius 流形（$\nabla^\lambda$ 平凡但合法）；而 $\mathbb{P}^2$ 的真实 $\Phi$ 的三阶导 $\Phi_{111}=\sum_dN_dd^3e^{dt_1}t_2^{3d-1}/(3d-1)!q^d$ 随 $t$ 变化（PDF p.259），$N_d$（$d\ge2$）只藏在 $t$ 的高阶导里，单个 Frobenius 代数（即 $t=0$ 处的 $A_{ijk}$）看不到它们。
2. **误解：任意偶势 $F$ 都能定义 Frobenius 流形；WDVV 是额外公理。** 错。取 $\mathbb{P}^2$ 的配对 $g_{02}=g_{11}=1$，令 $F=\frac12(t_0^2t_2+t_0t_1^2)+\frac{c}{2}t_1^2t_2$（$c\ne0$）。除经典项外唯一非零的三阶导是 $A_{112}=A_{121}=c$；升指标得 $T_1*T_1=T_2+cT_0$、$T_1*T_2=cT_1$、$T_2*T_2=0$，于是 $(T_1*T_1)*T_2=cT_2$ 而 $T_1*(T_1*T_2)=cT_2+c^2T_0$，$c\ne0$ 时不结合；由 D6，$\nabla^\lambda$ 不可能平坦，$F$ 不满足 WDVV。正确说法：对 $F=\Phi$，WDVV 由 $\overline M_{0,n+4}$ 上两个边界除子的线性等价证明（定理 8.2.4, PDF p.255–256），并与结合律等价（定理 8.2.5, PDF p.256–257）。
3. **误解：$A$ 模型联络与 Dubrovin 联络是两套独立理论；或 CY 三维簇上「大 $=$ 小」所以 Frobenius 流形结构是平凡的。** 错。命题 8.5.2（PDF p.267–268）证明 $\nabla=\nabla^\lambda\big|_{\lambda=1/(2\pi i)}$，二者是同一对象在坐标 $u_j=t_j/(2\pi i)$ 下的写法；CY 三维簇上「大 $=$ 小」只指环结构（PDF p.262：$\Phi$ 的三阶导 $=$ 量子关联函数，WDVV 归结为杯积的结合律），但 $\Phi_{111}=5+2875q+\cdots$ 仍含全部亏格 0 数据，A 模型 VHS（定理 8.5.11）依赖它，非平凡。
4. **误解：Frobenius 流形的定义要求 $F$ 收敛、模空间是真正的流形。** 错。本书明确允许 $F$ 是形式幂级数，此时称**形式 Dubrovin 联络**（PDF p.265）；A 模型联络的收敛性仍是猜想，故书中「严格说只是形式联络」（PDF p.267）。

## 8. 在文献中的坐标
| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999 | §8.4, PDF p.262–265（印刷 p.239–242） | 定义 $A_{ijk}$、$*$、$\nabla^\lambda$（式 (8.35)–(8.36), p.262）；证 $\nabla^\lambda$ 平坦 ⟺ WDVV ⟺ 结合（p.263）；命题 8.4.1（p.263）；$\nabla^\lambda_{\partial/\partial t_i}(T_j)=\lambda T_i*T_j$、Frobenius 流形例、Euler 场、$\widehat\nabla$（p.264）；形式 Dubrovin 联络（p.265） |
| Cox–Katz 1999 | §8.5.2–8.5.3, PDF p.266–269（印刷 p.243–246） | A 模型联络（p.266–267）；命题 8.5.2：$\nabla=\nabla^\lambda$，$\lambda=1/(2\pi i)$（p.267–268）；命题 8.5.3：正则奇点 + 幺幂单值性 $N_j\sim-T_j\cup$（p.269） |
| Cox–Katz 1999 | §8.5, PDF p.277（印刷 p.254） | 定理 8.5.11：$(H,\nabla,H_{\mathbb{Z}},F^\bullet)$ 是权 $d$ 极化 Hodge 结构变分（$d\ge3$ CY） |
| Cox–Katz 1999 | §8.6, PDF p.280–282（印刷 p.257–259） | 定义 8.6.1 数学镜像对（镜像映射提升为保持两侧极化 VHS 的丛同构）；定理 8.6.2：等价于 $Y_{ijk}=\langle T_i,T_j,T_k\rangle$ |
| SY01-24 术语表 | 70 条中与本卡相关的仅 #5 Yukawa 耦合（首现 p.8，概览）、#17 Gauss–Manin 联络（p.19，第 1 章）、#18 单值变换（p.21，第 1 章） | 只覆盖 B 模型/Gauss–Manin 侧译名；**全表无 Frobenius 流形、Dubrovin 联络、WDVV、量子上同调、三点函数条目**（术语对照缺口）。**冲突**：monodromy 作「单值变换」（#18），本书 §8.5.3（PDF p.269）作「单值性」；`_冲突表` T1 已裁定「单值性」，本卡照用。另：#5 的 Yukawa 耦合是 B 模型/SCFT 语境（首现 p.8），与本书 §8.6 的 A 模型三点函数 $\langle T_i,T_j,T_k\rangle$ 经镜像映射相等但非同一对象（C4） |
| SY01-25 资料卡 | `04-术语文献勘误.md` §一（25 条核心术语）、§二（34 条文献）、§三（10 条勘误）、§四（7 条存疑） | 以 HMS/SYZ、$A_\infty$-预范畴、Morse–Smale 复形为主线；**无 Frobenius 流形/Dubrovin 联络/WDVV 条目**，文献表也无 Dubrovin/Manin。**冲突**：大复结构极限作 $q\to0$（§一），本书用 $q=e^{2\pi iu}$、大半径极限点为 $0\in\Delta^r$（PDF p.268），坐标约定不同（U3, C2）；「极大单值」（[LTY] maximal unipotent monodromy）与本书「最大幺幂」（定义 8.6.1, PDF p.280）用词不同（C3）；其 $A_\infty$/Fukaya 侧与本书 §8 的稳定映射 + GW 路线不重叠（U4） |
| Dubrovin 1992（[Dubrovin1]） | Nuclear Phys. B379, 627–689 | §8.4 的 Frobenius 流形/Dubrovin 联络理论的原始文献（PDF p.262 引：$\nabla^\lambda$ 三组等价关系的证明见 [Dubrovin1,KoM1,Manin3]） |
| Dubrovin 1996（[Dubrovin2]） | LNM 1620, 120–348 | Frobenius 流形的标准综述；PDF p.264 把「$H^*(X,\mathbb{C})$ + $g$ + WDVV 势」称作 Frobenius 流形的例子时引此文（定理号/页码待核，见 §11） |
| Kontsevich–Manin 1994（[KoM1]） | Comm. Math. Phys. 164, 525–562 | GW 类公理化、WDVV 证明；$\nabla^\lambda$ 在 $\mathbb{P}^1$ 上的延拓 $\widehat\nabla$ 引此文（PDF p.263–264） |

## 9. 前置与后继
- 前置：**MS-04**（小/大量子乘积、三点函数、GW 势 $\Phi$、定理 8.2.4–8.2.5）；**MS-11**（Hodge 结构变分 $F^\bullet$ 与 Gauss–Manin 联络 $\nabla^{\mathrm{GM}}$，§8.5 用它陈述镜像对）。
- 后继：**MS-19**（量子超平面截面原理；用 $\nabla^\lambda$ 与量子微分方程推相对 GW，PDF p.268 起）；**MS-12/MS-13**（单值性与极限混合 Hodge 结构：命题 8.5.3、定理 8.5.11 的细化）；**MS-01/MS-02**（定义 8.6.1 里的 $\nabla^{\mathrm{middle}}$ 即本卡的 A 模型联络）。
- 外部补充：Frobenius 流形的公理化定义读 Dubrovin 1996 或 Manin 1999（本卡的「本书用法」只有例子式引入）。

## 10. 形式化接口（Lean 可 sorry）
```lean
-- 只给签名与关键假设；证明允许 sorry。
variable {H : Type*} [AddCommGroup H] [Module ℂ H]

structure FrobeniusManifoldData (H : Type*) [AddCommGroup H] [Module ℂ H] where
  g : H → H → ℂ                       -- 非退化对称配对（Poincaré 配对）
  g_symm : ∀ a b, g a b = g b a
  g_nondegen : Prop                    -- Function.Bijective g 的抽象化
  A : H → H → H → ℂ                    -- A_{ijk} = ∂³F（式 (8.35)）
  star : H → H → H                     -- T_i * T_j = Σ_k A_{ij}^{\,k} T_k
  unit : H                             -- T_0 = 1
  unit_star : ∀ a, star unit a = a
  star_comm : ∀ a b, star a b = star b a
  star_assoc : ∀ a b c, star (star a b) c = star a (star b c)
  frobenius_inv : ∀ a b c, g (star a b) c = g a (star b c)
  wdvv : Prop                          -- F 满足 WDVV（PDF p.263 的等价形式）
  nabla : ℂ → H → H → H                -- ∇^λ：∇^λ_{∂i}(∂j) = λ Σ A_{ij}^{\,k} ∂_k
  flat : Prop                          -- (∇^λ)² = 0 对所有 λ ≠ 0（示意）
  torsion_free : Prop                  -- 挠率为零（示意）
  euler : H                            -- Euler 向量场 E（齐次性）

-- 命题 8.4.1：WDVV + A_{0ij}=g_{ij} ⟹ 逐点 Frobenius 代数
theorem frobenius_algebra_of_wdvv (M : FrobeniusManifoldData H) (h : M.wdvv) : Prop := sorry
-- 命题 8.5.2：A 模型联络 = ∇^λ，λ = 1/(2πi)
theorem a_model_connection_eq_dubrovin (M : FrobeniusManifoldData H) : Prop := sorry
-- 定理 8.5.11：由 A 模型联络得到权 d 极化 Hodge 结构变分
theorem a_model_vhs (M : FrobeniusManifoldData H) : Prop := sorry
```

## 11. 待核清单
- [ ] **C1（术语级）** monodromy：SY01-24 #18 作「单值变换」，本书 §8.5.3（PDF p.269）作「单值性变换」/「单值性」；`_冲突表` T1 已裁定用「单值性」，本卡照用，不重判。
- [ ] **C2（理解级）** 大复结构极限：SY01-24 #14 只立译名「大复结构极限」（p.18，说明栏未记坐标约定），SY01-25 §一 记其对应 $q\to0$；本书取 $q=e^{2\pi iu}$、大半径极限点为 $0\in\Delta^r$（$t\to i\infty$），PDF p.268。坐标换算见 `_冲突表` U3、MS-06/MS-19。
- [ ] **C3（术语级）** SY01-25 用「极大单值」（maximal unipotent monodromy, [LTY]），本书定义 8.6.1（PDF p.280）用「最大幺幂」；本卡按「最大幺幂」。
- [ ] **C4（口径级）** SY01-24 #5「Yukawa 耦合」首现 p.8，是 B 模型/SCFT 语境；本书 §8.6 定理 8.6.2（PDF p.282）的 A 模型关联函数是 $\langle T_i,T_j,T_k\rangle=\int T_i*T_j*T_k$。两者经镜像映射相等但非同一对象，不能互作译名依据。
- [ ] **T1（待核）** [Dubrovin2] LNM 1620 中 Frobenius 流形定义的具体编号与页码（本卡只给 PDF p.264 的用法）。
- [ ] **T2（待核）** 定理 8.5.11 的完整假设（整性猜想、最大幺幂点等）——本卡只引其「VHS 存在」结论。
- [ ] **T3（待核）** 本书是否另有 Frobenius 流形的编号定义：全章 grep 未见 definition 环境，p.264 段为唯一正式引入；待另一轮全文复核。
- [ ] **T4（待核）** §4.1(5) 的 $N_2=N_1^2$、$N_3=12$ 为按书中 $\Phi$ 与递推（PDF p.259–260）推出的核验值，非书中原文数字；如书内另有直接陈述，补页码。
- [ ] **T5（待核）** SY01-24/SY01-25 均无 Frobenius 流形/Dubrovin 联络/WDVV 条目，术语对照无法闭环；需在两书下一轮补条目或在本项目术语表加「本书口径」注。
