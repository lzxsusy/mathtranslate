---
id: MS-07
zh: 环面簇
en: toric variety
aliases: [环面代数簇, toric variety, 环面簇 X_Σ]
layer: L0
prereqs: [MS-08]
sources:
  - "A 级：Cox–Katz 1999, PDF p.55（印刷 p.32）§3.1——X_σ=Spec C[M∩σ̌] 与粘合、式 (3.1)、Chow 列 (3.2)、完备/光滑/单纯三判据、Cartier 判据与支撑函数"
  - "A 级：Cox–Katz 1999, PDF p.56–60（印刷 p.33–37）§3.2——Δ_D 式 (3.3)、H^0 同构 (3.4) 与 (3.7)、P_Δ 与法扇、定义 3.2.2 齐次坐标环、定理 3.2.3 范畴商"
  - "A 级：Cox–Katz 1999, PDF p.61–68（印刷 p.38–45）§3.3–3.4——命题 3.3.1 Kähler 锥、引理 3.3.2 与推论 3.3.3、式 (3.16) 与定理 3.3.4 矩映射、定理 3.4.1/3.4.2"
  - "A 级：Cox–Katz 1999, PDF p.72–75（印刷 p.49–52）例 3.7.1–3.7.3——P^n、P(1,1,2,2,2)、P^1×P^1×P^1"
  - "A 级：Batyrev 1994, J. Algebraic Geom. 3 (1994), 493–535（法扇与 P_Δ=Proj S_Δ，书 PDF p.57–58 引 Batyrev4）"
  - "A 级：Cox 1995, J. Algebraic Geom. 4 (1995), 17–50（齐次坐标环，书 PDF p.59–60 采用）"
  - "B 级：Fulton 1993, Introduction to Toric Varieties, Princeton Univ. Press（书 PDF p.62 引「Fulton 书 p.99」）"
  - "B 级：Oda 1988, Convex Bodies and Algebraic Geometry, Springer（书 PDF p.58、p.66 引）"
  - "B 级：SY01-24 术语表第 18/44/50/51 条；SY01-25 资料卡 04（对照，见 §8）"
status: draft
review:
  drafter: agent-218
  reviewer: lead
  blindtest: pending
glossary_refs: [toric variety, toric geometry, affine toric variety, fan, cone, Chow group, Picard group, ample divisor, polytope]
symbols_refs: ["$M$", "$N$", "$T_N$", "$\\Sigma$", "$\\Sigma(1)$", "$X_\\Sigma$", "$D_\\rho$", "$A_{n-1}(X)$", "$\\Delta_D$", "$S$", "$\\operatorname{cpl}(\\Sigma)$"]
updated: 2026-11-20
---

# MS-07 环面簇

## 1. 一句话

环面簇由格中扇的锥对应的仿射片粘合而成、含稠密开环面，是镜像对称的可计算模型。

## 2. 为什么需要它

- **第 4 章 Batyrev 构造的几何舞台。** 自反多胞形 $\Delta$ 先给出环面簇 $\mathbb P_\Delta=\operatorname{Proj}S_\Delta$，其扇是 $\Delta$ 的法扇，这一步即「$\mathbb P$ 正是由该法扇确定的环面簇」（PDF p.57–58，引 Batyrev4）；Batyrev 镜像对 $(\mathbb P_\Delta,\mathbb P_{\Delta^\circ})$ 与 MPCP 消解都在两个环面簇里进行（MS-23）。缺了 §3.1–3.2 的扇–簇词典，第 4 章无法陈述。
- **GKZ 分解／多重镜像的相图。** 固定一维锥集 $\Xi$ 后，所有射影单纯 $X_\Sigma$（$\Sigma(1)\subset\Xi$）都是同一辛商 $\mu_\Xi^{-1}(a)/G(\Xi)_{\mathbb R}$ 的纤维（定理 3.4.2，PDF p.68）：$a$ 落在不同锥 $\operatorname{cpl}(\Sigma)$ 内部就得到不同 $X_\Sigma$，落在 $A^+(\Xi)$ 外得到 Landau–Ginzburg 相（PDF p.69）。这是附录 B.5 的 GLSM 相图的数学版本，也是 MS-21 的前置。
- **齐次坐标环是计算引擎。** 第 5 章的 Yukawa 耦合靠 $S=\mathbb C[x_\rho:\rho\in\Sigma(1)]$ 与 $H^0(X,\mathcal O(D))\cong S_\alpha$（定义 3.2.2、式 (3.8)，PDF p.59–60）把周期积分写成多项式环里的显式积分；书中明言可用齐次坐标描述微分形式。没有 $X_\Sigma$，$S$ 无从定义。
- **Fano 与自反多胞形之间的翻译器。** 定义 3.5.1 与命题 3.5.5（PDF p.69）把「Fano 环面簇」等价于「自反多胞形」；例 3.7.3（PDF p.74–75）的立方体与八面体是一对最小样例（MS-09）。

## 3. 定义（全假设）

**定义 3.1（格、锥；PDF p.54–55）.** 取自由 Abel 群 $M\cong\mathbb Z^n$ 与对偶 $N=\operatorname{Hom}(M,\mathbb Z)\cong\mathbb Z^n$，配对 $\langle\cdot,\cdot\rangle:M\times N\to\mathbb Z$；$M_{\mathbb R}=M\otimes\mathbb R$，$N_{\mathbb R}=N\otimes\mathbb R$。由 $u_1,\dots,u_s\in N$ 生成的有理多面锥 $\sigma=\operatorname{cone}(u_1,\dots,u_s)=\{\sum\lambda_iu_i:\lambda_i\ge0\}$；若 $\sigma\cap(-\sigma)=\{0\}$ 称强凸，$\dim\sigma=\dim_{\mathbb R}\operatorname{span}(\sigma)$。对偶锥 $\check\sigma=\{m\in M_{\mathbb R}:\langle m,v\rangle\ge0,\ \forall v\in\sigma\}$；$\sigma$ 的面是 $\tau=\{v\in\sigma:\langle m,v\rangle=0\}$（某 $m\in\check\sigma$）。

**定义 3.2（扇；PDF p.55）.** 扇 $\Sigma$ 是 $N_{\mathbb R}$ 中有限个强凸有理多面锥的集合，满足：(i) 若 $\sigma\in\Sigma$，其每个面也属于 $\Sigma$；(ii) 任两 $\sigma,\sigma'\in\Sigma$ 之交 $\sigma\cap\sigma'$ 是二者的公共面（从而属于 $\Sigma$）。支集 $|\Sigma|=\bigcup_{\sigma\in\Sigma}\sigma$；$\Sigma(d)$ 记 $d$ 维锥之集。**本书始终假设一维锥 $\rho\in\Sigma(1)$ 张成 $N_{\mathbb R}$**（PDF p.55）。$\rho\cap N$ 的唯一本原整生成元记 $v_\rho$，并常把 $\rho$ 与 $v_\rho$ 等同。

**定义 3.3（环面簇；PDF p.55）.** 对 $\sigma\in\Sigma$ 令 $X_\sigma=\operatorname{Spec}\mathbb C[M\cap\check\sigma]$：$\mathbb C$-代数由 $\chi^m$（$m\in M\cap\check\sigma$）生成，乘法 $\chi^m\chi^{m'}=\chi^{m+m'}$。若 $\tau=\sigma\cap\sigma'$ 是公共面，则按定义 3.2(i) $X_\tau$ 同时开嵌入 $X_\sigma$、$X_{\sigma'}$；沿这些开嵌入粘合得 $X_\Sigma$。$T_N=N\otimes\mathbb C^*=\operatorname{Spec}\mathbb C[M]$ 对应锥 $\{0\}$，是 $X_\Sigma$ 的稠密开子集；$T_N$ 在自身上的乘法作用唯一延拓为 $X_\Sigma$ 上的代数作用（此即「环面簇」得名之由）。$X_\Sigma$ 是 $n$ 维 Cohen–Macaulay 代数簇，其 $T_N$-轨道只有有限个。

**定义 3.4（三条判据；PDF p.55）.** (a) $X_\Sigma$ 完备（即紧）$\iff|\Sigma|=N_{\mathbb R}$；(b) $X_\Sigma$ 光滑 $\iff$ 每个 $\sigma\in\Sigma$ 的生成元都可扩充为 $N$ 的 $\mathbb Z$-基；(c) $X_\Sigma$ 是轨形（$V$-流形）$\iff$ 每个 $\sigma$ 的生成元在 $\mathbb R$ 上线性无关，此时称 $\Sigma$ 与 $X_\Sigma$ 单纯。

**定义 3.5（除子与 Chow 群；PDF p.55）.** $\rho\in\Sigma(1)$ 对应不可约 $T_N$-不变除子 $D_\rho$；把 $\chi^m$ 看作有理函数，$\operatorname{div}(\chi^m)=\sum_\rho\langle m,v_\rho\rangle D_\rho$（式 (3.1)）。由此得正合列
$$0\longrightarrow M\longrightarrow\mathbb Z^{\Sigma(1)}\longrightarrow A_{n-1}(X)\longrightarrow0\qquad(3.2)$$
其中 $m\mapsto(\langle m,v_\rho\rangle)$，$(a_\rho)\mapsto$ 除子 $\sum a_\rho D_\rho$ 的类；故 $\operatorname{rank}A_{n-1}(X)=r-n$，$r=|\Sigma(1)|$。$D=\sum a_\rho D_\rho$ 是 Cartier 除子 $\iff$ 对每个 $\sigma\in\Sigma$ 存在 $m_\sigma\in M$，使 $\rho\subset\sigma$ 时 $\langle m_\sigma,v_\rho\rangle=-a_\rho$；此时支撑函数 $\varphi_D$ 由 $\varphi_D(v)=\langle m_\sigma,v\rangle$（$v\in\sigma$）定义。$\operatorname{Pic}(X_\Sigma)\subset A_{n-1}(X_\Sigma)$：$X$ 光滑时 $\operatorname{Pic}=A$；单纯时 $\operatorname{Pic}$ 在 $A$ 中指数有限；$X$ 完备时 $\operatorname{Pic}$ 无挠，而 $A$ 即使单纯也可有挠。

**定义 3.6（丰沛判据与多胞形；PDF p.56–59）.** $D$ 由整体截面生成 $\iff\langle m_\sigma,v_\rho\rangle\ge-a_\rho$ 对一切 $\rho\not\subset\sigma$；丰沛 $\iff$ 严格不等式。令 $\Delta_D=\{m\in M_{\mathbb R}:\langle m,v_\rho\rangle\ge-a_\rho,\ \forall\rho\}$（式 (3.3)），则 $H^0(X,\mathcal O(D))\cong\bigoplus_{m\in\Delta_D\cap M}\mathbb C\chi^m$（式 (3.4)，PDF p.57）。齐次坐标环 $S=\mathbb C[x_\rho:\rho\in\Sigma(1)]$，$\deg x_\rho=[D_\rho]\in A_{n-1}(X)$，按 Chow 群分次（定义 3.2.2，PDF p.59）。

**本书用法.** 本书不给编号的「环面簇」定义：PDF p.54 章首说明假定读者熟悉 [Danilov, Fulton3, Oda] 的锥–扇语言，p.55 以「回顾经典定义」的口吻写出 $X_\sigma$ 与 $X_\Sigma$，§3.2 起才切换到多胞形（$\mathbb P_\Delta=\operatorname{Proj}S_\Delta$）与齐次坐标两种新表述。术语上「环面几何」是第 3 章章名（Toric Geometry），单数对象「环面簇」始终指 $X_\Sigma$（连同选定的扇）。第 3 章不出现 monodromy，故 §8 的 T1 术语冲突只作登记、不在正文使用。

## 4. 最小例子（能算出）

取 $\mathbb P^2$：$N=\mathbb Z^2$，$M=\mathbb Z^2$，射线 $v_0=(1,0)$、$v_1=(0,1)$、$v_2=(-1,-1)$，扇 $\Sigma$ 由 $0$、三条射线与三个 2 维锥 $\sigma_{01}=\operatorname{cone}(v_0,v_1)$、$\sigma_{12}=\operatorname{cone}(v_1,v_2)$、$\sigma_{20}=\operatorname{cone}(v_2,v_0)$ 连同其面组成（例 3.7.1 的 $n=2$ 情形，PDF p.72；SY01-24 例 4.10 用同一扇）。

1. **扇的判据。** $\det(v_0,v_1)=\det(v_1,v_2)=\det(v_2,v_0)=1$，三个 2 维锥的生成元都是 $\mathbb Z^2$ 的 $\mathbb Z$-基，故 $X_\Sigma$ 光滑（定义 3.4(b)）。又 $-v_2=v_0+v_1$（系数皆正），$0$ 落在 $\operatorname{conv}(v_0,v_1,v_2)$ 内部，三条射线正张成 $\mathbb R^2$，$|\Sigma|=\mathbb R^2$，故 $X_\Sigma$ 完备（定义 3.4(a)）。
2. **Chow 群。** $r=3,n=2$，式 (3.2) 为 $0\to\mathbb Z^2\to\mathbb Z^3\to A_1(\mathbb P^2)\to0$，其中 $(m_1,m_2)\mapsto(m_1,m_2,-m_1-m_2)$，$(a_0,a_1,a_2)\mapsto a_0D_0+a_1D_1+a_2D_2$。$M$ 的像 $=\{(a_0,a_1,a_2):a_0+a_1+a_2=0\}$（秩 2），故 $A_1(\mathbb P^2)\cong\mathbb Z^3/\text{像}\cong\mathbb Z$，同构由 $(a_0,a_1,a_2)\mapsto a_0+a_1+a_2$ 给出，$\operatorname{rank}=r-n=1$：三条直线 $D_0,D_1,D_2$ 同类 $=H$，且无 $3H=0$ 的关系（Chow 群自由）。
3. **Cartier 与丰沛。** 取 $D=D_0$（$a=(1,0,0)$）：在 $\sigma_{12}$ 上取 $m=(0,0)$，得 $\langle m,v_1\rangle=0$、$\langle m,v_2\rangle=0$；在 $\sigma_{20}$ 上取 $m=(-1,1)$，得 $\langle m,v_0\rangle=-1$、$\langle m,v_2\rangle=0$；在 $\sigma_{01}$ 上取 $m=(-1,0)$，得 $\langle m,v_0\rangle=-1$、$\langle m,v_1\rangle=0$。每个锥上 $\rho\subset\sigma$ 处的等式都成立，故 $D_0$ 是 Cartier（即 $\mathcal O(1)$）；且这些锥外的不等式全为严格 $>$，故 $D_0$ 丰沛（PDF p.56）。
4. **多胞形与 $h^0$。** $\Delta_{D_0}=\{m:m_1\ge-1,\ m_2\ge0,\ m_1+m_2\le0\}$（式 (3.3)），是顶点 $(-1,0),(0,0),(-1,1)$ 的三角形；平移 $(1,0)$ 后恰为例 3.7.1 的 $\{c_i\ge0,\ c_1+c_2\le1\}$（平移正对应 $\Delta_{D+\operatorname{div}\chi^m}=\Delta_D-m$，PDF p.56）。数整点：$|\Delta_{D_0}\cap M|=3$、$|2\Delta_{D_0}\cap M|=6$、$|3\Delta_{D_0}\cap M|=10$（Ehrhart：面积 $=1/2$、边界整点数 $=3$，故 $|k\Delta\cap M|=(k^2+3k+2)/2$）。由式 (3.4)(3.7) 得 $h^0(\mathcal O(kH))=3,6,10$，而 $\dim S_k=\dim\mathbb C[x_0,x_1,x_2]_k=(k+2)(k+1)/2=3,6,10$，逐一相符。
5. **边界对照（挠）。** 取 $\sigma=\operatorname{cone}((1,0),(1,2))\subset N_{\mathbb R}=\mathbb R^2$：强凸、单纯，但 $\det((1,0),(1,2))=2\ne1$ 故不光滑（定义 3.4(b)）。式 (3.2) 给 $0\to\mathbb Z^2\to\mathbb Z^2\to A_1(X_\sigma)\to0$，$(x,y)\mapsto(x,x+2y)$，行列式 $2$，故 $A_1(X_\sigma)\cong\mathbb Z/2=\operatorname{Cl}(X_\sigma)$。又 $\check\sigma\cap M$ 的 Hilbert 基为 $(0,1),(2,-1),(1,0)$，关系 $2(1,0)=(0,1)+(2,-1)$，故 $\mathbb C[\check\sigma\cap M]\cong\mathbb C[x,y,z]/(z^2-xy)$，即 $A_1$ 奇点。这说明定义 3.5 末句「$A$ 可有挠」并非空话。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | $T_N$-轨道闭包与锥反序一一对应；$\rho\in\Sigma(1)$ 恰对应不可约 $T_N$-不变除子 $D_\rho$ | PDF p.55 | 轨道有限，故 $X_\Sigma$ 是「几乎齐性」的紧化 |
| 2 | $\operatorname{div}(\chi^m)=\sum_\rho\langle m,v_\rho\rangle D_\rho$，由此得正合列 (3.2)，$\operatorname{rank}A_{n-1}=r-n$ | PDF p.55 式 (3.1)(3.2) | 依赖「一维锥张成 $N_{\mathbb R}$」假设 |
| 3 | 完备 $\iff\lvert\Sigma\rvert=N_{\mathbb R}$；光滑 $\iff$ 每锥生成元可补成 $\mathbb Z$-基；轨形 $\iff$ 单纯 | PDF p.55 | 几何性质完全由扇的组合数据决定 |
| 4 | Cartier $\iff$ 每锥存在 $m_\sigma$；丰沛 $\iff$ 严格不等式；此时 $\Delta_D$ 以 $\{m_\sigma\}$ 为顶点集，非空面 ↔ 锥、刻面 ↔ $\Sigma(1)$ | PDF p.55–56 式 (3.3) | 单纯不能替代光滑（见 §7-2） |
| 5 | $H^0(X,\mathcal O(D))\cong\bigoplus_{\Delta_D\cap M}\mathbb C\chi^m$；$S$ 按 Chow 群分次且 $S_{\Delta_D}\cong\bigoplus_kS_{k\alpha}$ | PDF p.57 式 (3.4)；p.59–60 式 (3.7)(3.8) | 第 5 章 Yukawa 耦合的计算入口 |
| 6 | $1\to G\to(\mathbb C^*)^{\Sigma(1)}\to T_N\to1$，$X$ 为范畴商、单纯时几何商；Kähler 锥 $=\operatorname{cpl}(\Sigma)$ 内部；矩映射 $\mu_\Sigma^{-1}(a)/G_{\mathbb R}\cong X_\Sigma$ | PDF p.60 式 (3.9)、定理 3.2.3；p.62 命题 3.3.1；p.64–65 定理 3.3.4 | $G\cong(\mathbb C^*)^{r-n}\times$（有限群，$A$ 有挠时） |

## 6. 推导流程（D1…Dn）

- **D1（锥 $\to$ 仿射片）.** $\sigma\mapsto X_\sigma=\operatorname{Spec}\mathbb C[M\cap\check\sigma]$：$\chi^m$ 的乘法在 $\check\sigma\cap M$ 上封闭，故这是幺半群代数。依据：PDF p.55。
- **D2（粘合 $\to$ 整体）.** 公共面 $\tau=\sigma\cap\sigma'$ 使 $X_\tau$ 同时开嵌入 $X_\sigma$、$X_{\sigma'}$（局部化 $M\cap\check\tau\supset M\cap\check\sigma$），沿之粘合得 $X_\Sigma$；$T_N$ 的作用自动相容。依据：PDF p.55；SY01-24 式 (4.49)（p.66）用 $\varinjlim$ 表述同一构造。
- **D3（扇 $\to$ 除子与 Chow）.** 每个 $\rho$ 给出 $D_\rho$，$\operatorname{div}(\chi^m)$ 由配对给出式 (3.1)，核–像得正合列 (3.2)。依据：PDF p.55。
- **D4（Cartier $\to$ 支撑函数 $\to$ 多胞形）.** 每锥的 $m_\sigma$ 拼出 $\varphi_D$；整体生成/丰沛的不等式一致给出 $\Delta_D$（式 (3.3)）及其顶点集条件。依据：PDF p.55–56。
- **D5（多胞形 $\to$ 上同调）.** $H^0$ 由 $\Delta_D\cap M$ 整点给出（式 (3.4)）；$k$ 倍多胞形给出式 (3.7)。依据：PDF p.57–59。
- **D6（齐次坐标）.** 对偶 $A_{n-1}$ 得 $G$，式 (3.9) 与 $Z(\Sigma)=V(B(\Sigma))$（式 (3.10)）使 $X_\Sigma$ 成为 $\mathbb C^{\Sigma(1)}-Z(\Sigma)$ 的范畴商。依据：PDF p.59–61，定理 3.2.3。
- **D7（辛侧）.** $G_{\mathbb R}=\operatorname{Hom}(A_{n-1},U(1))$ 的矩映射 $\mu_\Sigma$（式 (3.16)）给轨形微分同胚 $\mu_\Sigma^{-1}(a)/G_{\mathbb R}\cong X_\Sigma$（$a$ 为 Kähler 类）。依据：PDF p.61–65，定理 3.3.4。
- **D8（同一 $\Xi$ 下的相分解）.** 固定 $\Xi$ 时各 $\operatorname{cpl}(\Sigma)$ 拼成 GKZ 扇（定理 3.4.1），次级扇由 Gale 变换给出，全部 $X_\Sigma$（$\Sigma(1)\subset\Xi$）由同一个 $\mu_\Xi$ 商得到（定理 3.4.2）。依据：PDF p.65–68。

## 7. 常见误解与反例（≥2）

- **误解 1：环面簇就是环面 $(\mathbb C^*)^n$。** 错：$T_N$ 只是 $X_\Sigma$ 的稠密开子集（PDF p.55），$X_\Sigma$ 是它的紧化。$n=1$ 时取 $\Sigma=\{0,\mathbb R_{\ge0},\mathbb R_{\le0}\}$，得 $X_\Sigma=\mathbb P^1$：式 (3.2) 为 $0\to\mathbb Z\to\mathbb Z^2\to A_0(\mathbb P^1)\to0$，故 $A_0(\mathbb P^1)\cong\mathbb Z$；两个边界除子 $D_+,D_-$ 是两个点，正是 $T_N=\mathbb C^*$ 之外的部分。
- **误解 2：扇单纯（simplicial）就自动光滑、$\operatorname{Pic}=A$。** 错：单纯只给轨形与「$\operatorname{Pic}$ 在 $A$ 中指数有限」（PDF p.55）；光滑要求生成元补成 $\mathbb Z$-基。反例即 §4-5 的 $A_1$ 锥 $\operatorname{cone}((1,0),(1,2))$（$\det=2$，不光滑，$\operatorname{Cl}\cong\mathbb Z/2$）；例 3.7.2 的 $\mathbb P(1,1,2,2,2)$（PDF p.72–74）是同一现象在加权射影空间的样板。
- **误解 3：$A_{n-1}(X_\Sigma)$ 总是自由 Abel 群，挠只出现在非单纯情形。** 错：PDF p.55 明说「$X$ 完备时 $\operatorname{Pic}$ 无挠，而 $A_{n-1}(X)$ 即使 $X$ 单纯也可有挠」；反例见 §4-5（$A_1(X_\sigma)\cong\mathbb Z/2$）。注意方向：完备性只保证 $\operatorname{Pic}$ 无挠，不保证 $A$ 无挠。
- **误解 4：任意 Weil 除子 $D=\sum a_\rho D_\rho$ 都能配一个 $\Delta_D$ 并用式 (3.4) 算 $h^0$。** 错：$\varphi_D$ 与 $\Delta_D$ 只在 $D$ 为 Cartier 时才有定义（PDF p.55–56），一般 $D$ 只有类 $[D]\in A_{n-1}$；单纯情形下 $\operatorname{Pic}$ 可能真小于 $A$（有限指数），故 $A$ 中的类未必有 Cartier 代表。书上例 3.7.1 的 $D_0$ 恰是 Cartier 且丰沛，才可直接套 (3.4)。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999（本译本） | PDF p.54–56（§3.1，印刷 p.31–33） | 锥–扇–簇的经典定义：$X_\sigma$ 与粘合、$T_N$ 作用、式 (3.1)、Chow 列 (3.2)、完备/光滑/单纯三判据、Cartier 判据与支撑函数。本卡 §3 的出处 |
| Cox–Katz 1999 | PDF p.56–61（§3.2，印刷 p.33–38） | $\Delta_D$ 式 (3.3)、$H^0$ 同构 (3.4)、$S_\Delta$ 与 $\mathbb P_\Delta$、法扇（引理 3.2.1）、齐次坐标环（定义 3.2.2）、$Z(\Sigma)$ 式 (3.10) 与定理 3.2.3 |
| Cox–Katz 1999 | PDF p.61–68（§3.3–3.4，印刷 p.38–45） | Kähler 锥 $=\operatorname{cpl}(\Sigma)$（命题 3.3.1）、Mori 锥（引理 3.3.2、推论 3.3.3）、矩映射（式 (3.16)、定理 3.3.4）、GKZ 分解（定理 3.4.1）、次级扇与 Gale 变换、定理 3.4.2 |
| Cox–Katz 1999 | PDF p.72–75（例 3.7.1–3.7.3，印刷 p.49–52） | 三个基础例子：$\mathbb P^n$ 的扇与 Chow 群、$\mathbb P(1,1,2,2,2)$ 的消解、立方体/八面体（$\mathbb P^1\times\mathbb P^1\times\mathbb P^1$ 及其 Fano 对偶 $\mathbb P_{\Delta^\circ}$） |
| Batyrev 1994, J. Algebraic Geom. 3 (1994), 493–535 | 全篇；本书 PDF p.57–58、p.69 引 Batyrev4 | A 级原始文献：由整多胞形 $\Delta$ 的法扇定义 $\mathbb P_\Delta=\operatorname{Proj}S_\Delta$（「$\mathbb P$ 正是由该法扇确定的环面簇」）、自反多胞形与镜像对的来源 |
| Cox 1995, J. Algebraic Geom. 4 (1995), 17–50 | 全篇；本书 PDF p.59–60 | A 级原始文献：齐次坐标环 $S$ 与定理 3.2.3 的商结构（定义 3.2.2 的直接出处） |
| Fulton 1993, Introduction to Toric Varieties, Princeton Univ. Press | 本书 PDF p.62 引「Fulton 书 p.99」；p.54 列为经典参考 | B 级教材：引理 3.3.2 中光滑邻域时 $c_\sigma=1$ 的出处；标准扇–簇语言的参考 |
| Oda 1988, Convex Bodies and Algebraic Geometry, Springer | 全篇；本书 PDF p.58、p.66 引 Oda | B 级教材：凸体/多胞形与环面几何的对照，$\varphi_\Delta$ 与 $\Delta_{D_\Delta}=\Delta$ 的依据之一 |
| SY01-24 术语表第 18/44/50/51 条（原书印刷 p.21/59/61/65） | 术语表 | **冲突（术语）**：① monodromy 译「单值变换」（第 18 条，说明栏并称「全书统一为『单值变换』」），本书与 _冲突表 T1 用「单值性」；② 术语表只收「环面几何」（#44）、「仿射环面簇」（#50）、「环面分层」（#51），无「环面簇」伞形条目，而本书基本对象恰是整体 $X_\Sigma$（PDF p.55）。孰对不判，见 §11-1 |
| SY01-24 第 4 章（定义 4.4 p.61、命题 4.6 p.63、定义 4.7 p.65、式 (4.49) p.66） | 第 4 章「环面几何」 | **冲突（假设）**：定义 4.4 的 $X_\sigma=\operatorname{Spec}k[\sigma^\vee\cap M]$ 与本书 $X_\sigma$ 逐字同构（其「尖锥」= 本书「强凸」）；但定义 4.7 的扇定义未列「一维锥张成 $N_{\mathbb R}$」，本书 PDF p.55 将其列为始终假设——少了它，式 (3.2) 的 $\operatorname{rank}=r-n$ 不再成立。另：命题 4.6 断言「每个仿射环面簇都是正规的」，本书 p.55 只断言 Cohen–Macaulay（正规 $\Rightarrow$ CM，强弱不同，非矛盾） |
| SY01-25 资料卡 04（第 8/9/19/30 行） | 一、核心术语（25 条速查） | **冲突（同词根异对象）**：卡 04 的 torus fibration=「环面纤维化」指 SYZ 的 $T^n$ 纤维，其「环面」不是环面簇的开环面 $T_N$；卡 04 未设「环面簇」条目、未说明二者关系，读者易把本卡 §7-1 的 $T_N$ 与 SYZ 纤维混同。不判对错，见 §11-3 |

## 9. 前置与后继

- 前置：MS-08（扇与多胞形：多胞形、极多胞形、法扇；队列登记 `prereqs: MS-08`）。读本卡 §5-4 与 §6-D5 前建议先过 MS-08 的极多胞形与法扇。
- 后继：MS-09（自反多胞形，T6）；MS-21（GLSM 与相，队列 `prereqs` 含 MS-07，本卡 §2 第 2 条是其入口）；MS-22（极端跃迁，用到 §3.3.2 的曲线 $C_\sigma$ 与 Mori 锥）；MS-23（nef 分拆与 Batyrev 构造，用到 §2 第 1 条）；MS-12/13（单值性，仅术语交叉，T1）。

## 10. 形式化接口（Lean 可 sorry）

```lean
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.LinearAlgebra.Finsupp

-- 接口草案；Mathlib 现有 toric 定义与下列名称待核（§11-8）
variable (n : ℕ)

/-- 格 M ≅ ℤ^n 与对偶 N = Hom(M,ℤ)（§3 定义 3.1） -/
abbrev Lattice := Fin n → ℤ

/-- 强凸有理多面锥：由有限生成元给出的尖锥 -/
structure Cone where
  gens : Finset Lattice
  pointed : Prop
  pointed_ok : pointed

/-- 扇：面封闭 + 两锥交为公共面（§3 定义 3.2） -/
structure Fan where
  cones : Finset Cone
  face_closed : Prop
  intersection_is_face : Prop
  ok : face_closed ∧ intersection_is_face

/-- 仿射片 X_σ = Spec C[M ∩ σ̌]（定义 3.3）；以幺半群代数占位 -/
noncomputable def affineChart (σ : Cone) : Type := MonoidAlgebra ℂ (σ.dual ∩ Lattice)

/-- 环面簇 X_Σ：沿 X_{σ∩τ} 粘合（粘合数据与 T_N 作用待补） -/
noncomputable def toricVariety (Σ : Fan) : Type := sorry

/-- X_Σ 为 n 维 Cohen–Macaulay（PDF p.55） -/
theorem cohenMacaulay (Σ : Fan) : IsCohenMacaulayRing (toricVariety Σ) := sorry

/-- Chow 正合列 (3.2)：0 → M → ℤ^{Σ(1)} → A_{n−1}(X) → 0（PDF p.55） -/
theorem chowSequence (Σ : Fan) (hspan : Prop) :
    ∃ r : ℕ, r = Σ.cones.card ∧ True := sorry
```

## 11. 待核清单

- [ ] **冲突 C1（术语）**：SY01-24 术语表第 18 条 monodromy 译「单值变换」并称全书统一（术语表 p.21 说明栏），本书口径「单值性」(_冲突表 T1；T1 的涉及卡明确含 MS-07)。本卡正文未使用 monodromy，仅登记；第 3 章是否真有单值性语境、T1 是否需把 MS-07 移出，待 lead 核。
- [ ] **冲突 C2（假设）**：SY01-24 定义 4.7（p.65）的扇定义未列「一维锥张成 $N_{\mathbb R}$」；需核 SY01-24 是否在 §4.6 或别处默认该假设——若默认，则属表述差异而非假设冲突。
- [ ] **冲突 C3（同词根）**：SY01-25 资料卡 04「环面纤维化」与「环面簇」的对象区分；建议在卡 04 或 213 条术语全表加交叉索引（本轮禁止改写既有文件，需 lead 处理）。
- [ ] 页码：本卡统一用 PDF 物理页（$=\SourcePage{N}=$ 印刷页 $+23$）。已核 p.55 页眉 32、p.59 印 36、p.60 印 37、p.64 印 41；p.54 无页眉数字，p.66/68 的印刷页待逐页复核。
- [ ] 式号：矩映射公式已核为式 (3.16)（PDF p.64）；原存疑的 (3.11)=$\operatorname{cpl}(\Sigma)$、(3.12)=$\lambda$ 线性关系、(3.13)=$\Lambda_{\mathbb Q}$ 均在 PDF p.62，(3.15)=$M_{\mathbb R}\to(\mathbb R^r)^*\to A\otimes\mathbb R$ 在 p.64。
- [ ] §4-4 未使用 $\deg D=n!\cdot\operatorname{vol}(\Delta_D)$（§3.2 未见该表述原文），改用整点计数 $3,6,10$ 交叉核对式 (3.4)(3.7)，以免依赖未核实的换算。
- [ ] 例 3.7.2 的 OCR 细节（$v_5=(0,-1,-1,-1)$、权重 $\lambda^{-2}\mu$）需对照印刷本复核；本卡只引用其「单纯而非光滑」的定性结论。
- [ ] §10 的 Mathlib 名称（`IsCohenMacaulayRing`、`MonoidAlgebra`）与上游是否已有 `Fan`/`Cone` 定义待核；本卡仅为接口草案。
- [ ] _冲突表 第三节需同步登记本卡 3 条（C1–C3）；本轮禁止改写既有文件，需 lead 同步。登记后本卡 `status` 继续保持 draft。
- **核验（2026-11-20）**：本卡经 `_核验记录.md` 核验，修正 1 处（详见该文件 ✗ 清单与证据链接）；其余待核条目保留。
