# 第 21 篇通读笔记 · N=4 超 Yang–Mills 理论中的超对称边界条件

- 底本：Gaiotto–Witten, *Supersymmetric Boundary Conditions in N=4 Super Yang-Mills Theory*, arXiv:0804.2902**v2**（2008-07-16，89 页）。
- 页码约定：**一律 PDF 页序**。已抽验 p003 页脚 2、p045 页脚 44、p060 页脚 59、p083 页脚 82、p089 页脚 88，故 **PDF 页 = 印刷页 + 1**。
- 式号照原文；卡片里的 `anchor` 写成 `A p.NN eq (x.y)`。
- 注意：本文 §2 与 §4.2.1 的连续参数记 **γ**（不是 τ；τ 是 S-对偶用的复耦合）。v2 与 v1 在这一记号上一致。

---

## 1. 文章骨架（节标题 → 一句话）

| 节 | PDF 页 | 一句话 |
|---|---|---|
| §1 Introduction | 4 | 四维 N=4 的半 BPS 边界条件几乎没有系统研究，本文补这一课，并预告极点（Nahm 方程）会带来非平凡真空模空间。 |
| §2 Half-BPS Boundary Conditions | 6 | 十维 Majorana–Weyl 超对称出发，要求保留 OSp(4\|4)（32 个超荷留一半），并把 R-对称破到 SO(3)×SO(3)。 |
| 2.1 Basic Examples | 8 | 用 B0=Γ456789、B1=Γ3456、B2=Γ3789 的代数把超对称条件化成一族混合边界条件 (2.13)+(2.15)，由单个参数 a 标号。 |
| 2.1.1 Interpretation | 11 | a=0/∞ 是 NS5 型（Neumann 型），a=±1 是 D5 型（Dirichlet 型）；γ 与四维 θ 角成正比。 |
| 2.2 BCs That Reduce The Gauge Symmetry | 13 | 用「x3 反射 × 李代数自同构 × 标量反射」的对合构造破缺规范群的边界条件。 |
| 2.2.1 Generalization To Any H | 14 | 只需 g=g₊⊕g₋ 满足 [g₊,g₊]⊂g₊、[g₊,g₋]⊂g₋，不必是对称空间，就能对任意子群 H 定义边界条件。 |
| 2.2.2 Global Symmetries | 15 | 边界上的常规范变换给出与 H 交换的全局对称群 K。 |
| 2.2.3 Central Elements | 16 | 中心元可以把 Dirichlet 值平移（X₊(0)=v、Y₋(0)=w）。 |
| 2.3 Coupling The NS System To Matter | 17 | 把半空间看成 R^{1,2}×L 上规范群为映射群 Ĝ 的三维理论，耦合边界超多重态。 |
| 2.3.1 3d Theory With Infinite-Dimensional Gauge Group | 18 | Ĝ 的规范作用量与超凯勒度规/三形式显式写出 (2.26)–(2.28)。 |
| 2.3.2 Shifted BC of Y | 20 | 算超凯勒矩映射得 μ(y)=DX/Dy+X×X+δ(y)X(0)，故边界条件被边界物质移位成 X(0)+μ_Z=0。 |
| 2.3.3 Analog For General H | 21 | 换成 Ĝ_H={g(0)∈H}，条件变为 X₊(0)+μ_Z=0，X(0)∈h^⊥。 |
| 2.3.4 Coupling To A More General Boundary Theory | 22 | 任意带 H 对称的边界 CFT 都可用（Higgs 支的低能描述）。 |
| 2.3.5 Shifting The BCs | 22 | 加 FI 参数把条件进一步平移成 X₊(0)+μ_Z=v；Y 侧用「变形伴随表示」实现 Y₋(0)=w。 |
| 2.4 The D5 System And Nahm's Equations | 24 | 三维 Poincaré 真空（F=0、只依赖 y）的超对称条件给出 Nahm 方程。 |
| 2.4.1 Poles | 25 | 奇异解 X_i=t_i/y（ρ:su(2)→g）给出「Nahm 极点」边界条件，把 G 破到 ρ 的中心化子。 |
| 2.5 Combining The Constructions | 27 | 三种构造（极点、破缺规范群、边界物质）可以叠加：统一成 Ĝ_H + 极点 + 边界物质，由三元组 (ρ,H,B) 标号。 |
| 2.5.1 A Brane Construction | 28 | U(n) 的 n 张 D3 同时终止在 D5 与 NS5 上，参数 v、w 分别来自 NS5、D5 的横向位移。 |
| 2.6 Domain Walls | 30 | 折叠技巧把两个理论的域壁变成其中一个（或乘积）的半空间边界条件。 |
| 2.6.1 First Example | 30 | G\|G 域壁 ↔ G×G 里取对角 G 的边界条件。 |
| 2.6.2 Generalization | 31 | 任意 G、G′ 与共同子群 H（两个嵌入）都给一个域壁。 |
| §3 Moduli Spaces Of Solutions Of Nahm's Equations | 32 | 系统研究给定 X∞（和极点）时 Nahm 方程解的模空间 M，它是超凯勒流形，也是本文「反常」的来源。 |
| 3.1 The Hyper-Kahler Quotient | 32 | M = W///Ĝ：平坦超凯勒空间按矩映射零点商掉 Ĝ；G 作用的矩映射是 X(0)。 |
| 3.1.1 Including A Pole | 33 | 加极点后 Ĝ 换成保极点的子群，G 作用的矩映射变成 X_h(0)（正交投影到 h）。 |
| 3.2 The Complex Manifold | 34 | 取一个复结构，Nahm 方程变成全纯方程 DX/Dy=0，于是 M 同构于 X∞ 的共轭轨道。 |
| 3.2.1 Conjugacy Classes In Complex Lie Algebras | 35 | 复轨道维数 = d − s（中心化子维数），正则元 s=r，故维数 d−r。 |
| 3.2.2 Turning Off The Symmetry Breaking | 36 | SU(2) 例：X∞→0 时轨道不塌缩，闭包是幂零锥 C²/Z₂，实解族 X=g(t/y+f)g⁻¹ 给出整个锥。 |
| 3.2.3 Analog For Any G | 37 | 一般 G：M 是同 Casimir 的正则轨道闭包；X∞=0 时 M=幂零锥。 |
| 3.2.4 More On Nilpotent Orbits | 39 | 幂零轨道由分拆/Jordan 型标号，正则幂零轨道稠密，其余是奇点。 |
| 3.3 Solutions Of Nahm's Equations With Poles | 41 | 有极点时不能用复规范变换置 A=0，但可置 A=it₃/y；通解由最低权向量参数化。 |
| 3.3.1 Some Examples | 43 | t₊ 正则幂零 ⇒ Slodowy 切片与每个正则轨道交于一点 ⇒ M 是单点；次正则 ⇒ C²/Γ。 |
| 3.4 Nahm's Equations And Brane Constructions | 44 | D3-D5 系统：D5 上的双基本超多重态给 Nahm 方程加 δ(y) 源，X 在 y=0 跳变。 |
| 3.4.1 Uniqueness Of The Vacuum | 47 | 该系统的真空模空间是单点（用秩 1 矩映射与特征多项式算出来）。 |
| 3.4.2 One Extra Brane | 48 | n\|n+1 张 D3 的域壁也给出单点模空间，并与 D3-D5 的极限互相退化。 |
| 3.4.3 D3-Branes Ending On A D5-Brane | 53 | 「n 张 D3 终止于 D5」⟺「X 在 y=0 有不可约 su(2) 嵌入的极点」。 |
| 3.4.4 A More General Case | 54 | m\|n（n≥m+2）：块状极点 + 两个半直线模空间按 U(m) 做超凯勒商，维数相加为 0。 |
| 3.5 Pole Of General Type | 57 | 一般极点 n=n₁+…+n_k：模空间维数 (3.52)，且只有在「从体内到边界 D3 数非增」时才等于膜图参数。 |
| 3.5.1 Analysis Of M As A Complex Manifold | 61 | 用 n=3=2+1 逐参数对比三个复流形，确认只有非增排列的极限收敛到超共形边界条件。 |
| 3.6 Moduli Space Of Vacua With More General BCs | 63 | 再取 H⊂F 并商掉 H：M_{ρ,H}=M_ρ///H，加边界理论 B 后 M_{ρ,H,B}=(M_ρ×H_B)///H。 |
| 3.7 Including Y∞ | 64 | 打开 Y∞ 后 Y 只生成解的对称性，超凯勒商应按 stabilizer H_Y 做，模空间按共轭类分片。 |
| 3.8 Duality: First Steps | 67 | Neumann 的 S-对偶不是朴素 Dirichlet，而是主嵌入的 Nahm 极点（Slodowy 切片平凡的唯一一支）。 |
| 3.9 Other Moduli Spaces Of Solutions Of Nahm's Equations | 68 | 区间上的 Nahm 模空间：G_ℓ≅T*G_C、拼接律、两端有极点的 S^{ρ,ρ′}、NS5 的双基本源（v2 新增）。 |
| 3.9.1 Hyper-Kahler Analog Of A Lie Group | 68 | 区间 [0,ℓ] 两端规范变换取 1：G_ℓ 是超凯勒流形，G×G 作用，复结构下同构 T*G_C。 |
| 3.9.2 Hyper-Kahler Analog Of A Homogeneous Space | 70 | 一端加极点得 T^ρ_ℓ，拼接律 G_ℓ×_G T^ρ_{ℓ′}=T^ρ_{ℓ+ℓ′}，商掉两端极点得 S^{ρ,ρ′}。 |
| 3.9.3 Including An NS5-Brane | 71 | NS5 在中间、两侧 n 与 m 张 D3：两侧边界条件由同一对复矩映射 μ_L=AB、μ_R=−BA 联系。 |
| §4 Supersymmetry Without Lorentz Invariance | 73 | 放松 SO(1,2)：只要保 8 个超荷，边界条件由一个自对偶三形式 q 标号（10 参族）。 |
| 4.1 Deforming The D3-D5 System | 73 | D5 上加常通量 F，保半 BPS 的条件是 W²=1，即 B1wB1=w⁻¹（充分条件 B1F=−FB1）。 |
| 4.1.1 Field Theory Interpretation | 75 | 场论侧：极点与任何四平面里的自对偶 Yang–Mills 相容，故可对极点作 SO(1,5) 旋转；得 9 维族 Z̃9。 |
| 4.2 Rotating The D3-NS5 System | 77 | 对 D3-NS5 作 S 对偶并旋转极点，得三形式 q=(∗012+∗456)F/8，它是 F 的非线性函数。 |
| 4.2.1 Realization In Field Theory | 79 | 边界上加 CS 型项（系数 γ）与三标量项（系数 u）实现 (4.27)/(4.30)，一般化到任意三形式 q 的边界项 (4.31)。 |
| 4.2.2 Canonical Form Of q | 81 | 自对偶三形式有 10 参 = 1(u) + 9(SO(1,5)/SO(1,2)×SO(3))；提升到 6+1 维得族 Z10。 |
| 4.3 An Example | 82 | q=¼(dx0+dx4)∧(dx1∧dx5+dx2∧dx6) 不能化成 (4.33)，它正是几何 Langlands 中 c.c. 膜的边界条件。 |
| 4.4 General Formulation | 84 | 一般判据：ε 落在极大 8 维零子空间 T；保 SO(3)_Y 时 T=U⊗W₂，U 由自对偶三形式 q 给出（f 对称）。 |
| 致谢、参考文献 | 88–89 | [19] 是 Kapustin–Witten（= 库内 01 KW06）；[10] 是同期 Janus 文。 |

---

## 2. 主定理清单（编号 + 页码 + 一句话）

原文是物理文献，定理没有统一编号，下表用「§ + 式号 + PDF 页」。

1. **半 BPS 判据**（§2，p9，式 (2.9)）：十维超流变分 $\mathrm{Tr}\,\bar\varepsilon\Gamma^I\Gamma^{JK}F_{JK}\Gamma_3\Psi=0$ 对所有 $I$ 成立 ⟺ 边界条件保半超对称。
2. **混合边界条件族**（§2.1，p10–p11，式 (2.13)、(2.15)、(2.18)）：保完整规范群、保共形、保半 BPS 的条件必为
   $\epsilon^{\lambda\mu\nu}F_{3\lambda}+\gamma F_{\mu\nu}=0$ 加 $D_3X_a+\frac u2\epsilon_{abc}[X_b,X_c]=0$，
   且 $(\gamma,u)=\bigl(-\frac{2a}{1-a^2},-\frac{2a}{1+a^2}\bigr)$；分类上只允许「X 或 Y 恰有一组 Dirichlet」。
3. **γ 与 θ 成正比**（§2.1.1，p12，式 (2.20)）：加 $\frac{\theta}{8\pi^2}\int\mathrm{Tr}F\wedge F$ 后变分给出同一个 (2.13)，$\gamma=-\theta e^2/4\pi^2$。
4. **破缺规范群的构造**（§2.2.1，p14，式 (2.24)）：$[g_+,g_+]\subset g_+$、$[g_+,g_-]\subset g_-$ 即可，不需要 $[g_-,g_-]\subset g_+$；$H=1$ 回到 Dirichlet。
5. **边界物质移位**（§2.3.2，p21，式 (2.33)）：矩映射含 $\delta(y)(\vec X(0)+\vec\mu_Z)$，故 $X(0)+\mu_Z=0$；加 FI 参数后 $X_+(0)+\mu_Z=v$ (2.36)。
6. **BPS 真空 ⟺ Nahm 方程**（§2.4，p25，式 (2.40)）：$\varepsilon_0$ 取 $B_1$ 本征向量时，$\frac{DX_1}{Dy}=\pm[X_2,X_3]$ 及循环，且 $Y$ 只生成未破缺规范对称 (2.41)。
7. **Nahm 极点**（§2.4.1，p26，式 (2.43)）：$\vec X=\vec t/y$（$[t_1,t_2]=t_3$，即 $\rho:\mathfrak{su}(2)\to\mathfrak g$）给出每个非零 $\rho$ 的半 BPS 边界条件，$G$ 破到 $Z_\rho(G)$。
8. **(ρ,H,B) 三元组**（§2.5，p28）：极大超对称边界条件由极点 $\rho$、保持的规范群 $H$、带 $H$ 对称的边界理论 $B$ 三者标号。
9. **真空模空间是超凯勒商**（§3.1，p32–p33，式 (3.3)、(3.4)）：$M=W///\hat G$，$\mu_i=\frac{DX_i}{Dy}+[X_{i+1},X_{i-1}]$，$G$ 作用 $\vec\mu=\vec X(0)$；$X_\infty$ 正则时 $M$ 光滑。
10. **复结构下 M 是共轭轨道**（§3.2，p35，式 (3.7)）：$M\cong\{X_\infty$ 在 $\mathfrak g_{\mathbb C}$ 中的共轭轨道$\}$，复维 $d-r$；$X_\infty$ 非正则时 $M=\overline{O_x}$（$x$ 同 Casimir），例如幂零锥。
11. **Slodowy 切片公式**（§3.3，p42–p43，式 (3.23)、(3.24)）：$M_\rho\cong S_{t_+}\cap\overline O_{X_\infty}$，$\dim_{\mathbb C}M_\rho=s-r$；$\rho$ 正则幂零（$s=r$）时 $M_\rho$ 是单点。
12. **D3-D5 真空唯一**（§3.4.1，p47，式 (3.33)–(3.35)）：$X''=X'-M$（$M_{ij}=B_iC_j$ 秩 1）必为幂零、且 $\det(z-X'')=z^n$ 的系数是 $C$ 的线性函数 ⇒ 恰一解。
13. **D3 终止于 D5 ⟺ 不可约 su(2) 极点**（§3.4.3，p54，式 (3.44)–(3.45)）：半直线上趋于 0 且正则幂零的解必为 $\vec X=\vec t/y+c$，$c\to\infty$ 时 $\vec X=\vec t/y$。
14. **一般极点的维数与排序条件**（§3.5，p60，式 (3.52)）：$s=n+2\sum_{j}(j-1)n_j$，$\dim_{\mathbb C}M=s-n=2\sum(j-1)n_j$；此式成立**当且仅当** $n_i$ 按非增顺序排列（从体内到边界 D3 数非增）。
15. **一般 (ρ,H,B) 模空间**（§3.6，p63，式 (3.58)、(3.59)）：$M_{\rho,H}=M_\rho///H$，$M_{\rho,H,B}=(M_\rho(X_\infty)\times \mathcal H_B)///H$。
16. **Neumann 的对偶**（§3.8，p67）：Neumann 真空唯一，其 S-对偶必是 $S_{t_+}$ 平凡的那支，即主嵌入 $\rho$ 的 Nahm 极点；$U(N)$ 由 D3-NS5↔D3-D5 确认。
17. **区间上的拼接律**（§3.9，p68–p71，式 (3.69)、(3.71)、(3.74)、(3.78)）：$G_\ell\times_G G_{\ell'}=G_{\ell+\ell'}$，$G_\ell\cong T^*G_{\mathbb C}$，$S^{\rho,\rho'}_{\ell+\ell'}=(T^\rho_\ell\times T^{\rho'}_{\ell'})///G$。
18. **常通量保半 BPS 判据**（§4.1，p74，式 (4.4)）：$W=-B_0wB_0B_1\in\mathrm{Spin}(1,6)$，保半 BPS ⟺ $W^2=1$ ⟺ $B_1wB_1=w^{-1}$；充分条件 $B_1F=-FB_1$。
19. **自对偶三形式族**（§4.2.2，p81–p82，式 (4.33)、(4.34)）：$\varepsilon_-=\sum q_{IJK}\Gamma^{IJK}\Gamma^3\varepsilon_+$，$q$ 自对偶，10 参 = $u$（1）+ $SO(1,5)$ 轨道（9）；$\tilde Z_9\subset Z_{10}$。
20. **零子空间判据**（§4.4，p85–p87，式 (4.47)、(4.57)）：半 BPS ⟺ $\varepsilon$ 落在 $(\varepsilon,\tilde\varepsilon)=\varepsilon\Gamma^3\tilde\varepsilon$（号差 (8,8)）的极大 8 维零子空间；保 $SO(3)_Y$ 时 $\varepsilon_-=\sum q_{IJK}\Gamma^{IJK}\Gamma^3\varepsilon_+$，$q$ 自对偶。

---

## 3. 与已译文献的接口

按 XREF §3 给的八篇逐个判断（只写**确实有共用对象**的，其余如实说「无直接接口」）。

| 篇 | 接口 | 具体位置 |
|---|---|---|
| **01 KW06**（电磁对偶与几何朗兰兹） | **最强的一条** | 本文 [19] 即 KW06。§4.3 脚注 17（p83）明确说：(4.37) 的三形式边界条件正是 KW06 式 (12.31) 里「canonical coisotropic brane 的规范理论描述」；并给出记号换算——**本文的 $x^3$ 是 KW06 的 $x^1$，本文的 012456 是 KW06 的 023567**。库内 `datasets/kw06/cards/concepts/canonical-coisotropic-brane.json` 把 c.c. 膜定义为 $M_H(G,C)$ 上空间充满的 rank-1 A-膜、$F=(\mathrm{Im}\,\tau)\omega_J$；本篇给的是它在四维规范理论侧的边界条件（三形式微扰），两者是同一对象的两种语言。 |
| **06 SY05-25**（镜像对称、Hitchin 方程与朗兰兹对偶） | 间接 | 本篇 §4 的 $q$ 变形属于 A-膜/B-膜词典里的 B-膜侧边界条件；§4.3 的 c.c. 膜例子正是 06 里 A-膜 ↔ D-模那条词典的一端。**未逐式对照**（06 的中译在库内，但本轮没有逐条比对 $q$ 的坐标形式）。 |
| **23 SY05-01**（四维规范场论中的纽结不变量） | 共用对象 | 都用四维 N=4 的半 BPS 边界条件、't Hooft 算子与 $\mathbb R^3$ 上的三维理论（本篇 §2.3 的 $\hat G$ 就是 23 里边界三维理论的同款构造）。本篇 §4 的 $\gamma,u$ 与 23 的扭化参数不是同一参数，**未混用**。 |
| **28 bdh**（Hitchin 可积系统的量子化与 Hecke 特征层） | 间接 | c.c. 膜的开弦代数是微分算子（28 的核心对象），本篇 §4.3 的边界条件给出它的规范理论实现。 |
| **36 SY03-21**（朗兰兹纲领与共形场论讲义） | 术语层 | 「典范余各向同性膜」「特征膜」等定名以 36 与 SCHEMA 为准；本篇不引入新译名。 |
| **02 SY02-06**（规范理论、分歧与几何朗兰兹） | 无直接接口 | 本篇不讨论分歧（ramification）；只在「边界条件 → 算子」的大图景上相邻。 |
| **11 SY03-01**（量子力学路径积分的新视角） | 无直接接口 | 本篇不涉及路径积分定义问题。 |
| **16 SY01-07**（几何内窥与镜像对称） | 无直接接口 | 内窥（endoscopy）在本篇未出现。 |

---

## 4. 核对与勘误

### 4.1 XREF 五项动作逐条回填

| # | 核什么 | 怎么核 | 结论 |
|---|---|---|---|
| 1 | 主定理的陈述与符号 | 摘要 vs 正文；§2.4.1/§2.3/§2.2 与摘要三句话一一对；被引 2611.18118 的复述 | **一致**。摘要「Dirichlet 可加极点」「Neumann 可耦合边界场」「orientifold 也可推广」分别对应 §2.4.1、§2.3、§2.2；摘要说「Nahm 方程解的模空间」，正文 §3 正是它的系统研究。 |
| 2 | 关键公式的系数/符号/指数 | (2.18) 对 ggl12 旧卡；(2.15) 对 ggl12 旧卡；自算 (2.13) 代入 (2.18)；(3.52) 自算 $s$；(4.26) 与 (4.27)、(4.32) 自洽 | **一致**。见下文「外部来源」表第 1、2 行。(2.18) 代入 (2.15) 得 $D_3X_a-\frac{a}{1+a^2}\epsilon_{abc}[X_b,X_c]=0$，与 ggl12 卡逐字相同；(2.13) 与旧卡 $F_{3\mu}+\frac{a}{1-a^2}\epsilon_{\mu\nu\lambda}F^{\nu\lambda}=0$ 经 3d $\epsilon$ 缩并后只差符号，随 $\epsilon$ 与 $F$ 指标位置的约定而变，不算冲突；$s=n+2\sum_{i<j}n_j$ 用 $u(3)$ 按 $3=2+1$ 分解（不可约项数 $5=3+2$）验证。 |
| 3 | 命题编号与交叉引用 | 抽查 p10 引 (2.12)、p33 引 (3.4)、p56 引 (3.4)、p67 引 (3.66)、p80 引 (4.31)、p83 脚注 17 引 [19](12.31) | **全部指向正确条目**：(2.12) 六方程在 p10；(3.4) $\vec\mu=\vec X(0)$ 在 p33；(3.66) 在 p67；(4.31) 在 p80。 |
| 4 | 数值/维数一致性 | $\dim_{\mathbb C}M=s-r$；$s-n=2\sum(j-1)n_j$；$2n(k-1)$；$m^2+m$ 与 $m^2-m$ 加超凯勒商为 0 | **一致**。$2m^2+(m^2+m)+(m^2-m)-2m^2=0$ ✓；$k$ 张 D5 的 $2n(k-1)$ 与「$k-1$ 段 × 每段 $n$ 个双基本超多重态」✓。**中途的疑点已排除**：我一度以为 §3.4.4 的 $s-n=m^2+m$ 算不出来，原因是我把 $s$ 当成「不可约表示个数」却漏了 $s=n+2\sum(j-1)n_j$ 里的 $2\sum$ 项；用 $n=(n-m)+1^m$ 代 (3.52) 立即得 $m(m+1)$，原文无误。 |
| 5 | 记号与前后定义 | 通读全篇查同一符号 | **有三处需要注意，但都不是错**：①连续参数记 **γ**，不是 τ（τ 留给 S-对偶的复耦合）；②$X,Y$ 在 §2.1 与 §2.3 之间**互换**（§2.3 起固定 $\varepsilon_0$ 为 $B_1$ 本征向量，$X$ 属超多重态），§3 一律沿用 §2.3 的约定；③$H$ 既是「与 $\rho$ 交换的子群」（p33 明确定义）、又在 p34 第 11 行被误写成超凯勒流形——这是 E1。 |

### 外部来源

| 来源 | 位置 | 核了什么 | 结论 |
|---|---|---|---|
| 库内旧卡 `datasets/ggl12/cards/concepts/d3-ns5-boundary-condition.json` | formulas 栏与 notation 栏 | (2.13)、(2.15)、(2.18) 的系数与 $a\leftrightarrow\theta$ 对应 | **一致**。旧卡作 $F_{3\mu}+\frac{a}{1-a^2}\epsilon_{\mu\nu\lambda}F^{\nu\lambda}=0$、$D_3X_c-\frac{a}{1+a^2}\epsilon_{cde}[X_d,X_e]=0$、$\frac{\theta}{2\pi}=\frac{2a}{1-a^2}\frac{4\pi}{g_{\rm YM}^2}$；(2.18) 代入 (2.15) 与旧卡逐字相同（$u/2=-\frac{a}{1+a^2}$）；(2.13) 与旧卡经 3d $\epsilon$ 缩并后只差一个符号，属 $\epsilon$、$F$ 指标位置约定，判一致、不记 errata。 |
| 库内旧卡 `datasets/ggl22/cards/concepts/nahm-pole-bc.json` | definition 栏 | 极点 $\vec X\sim\rho(\vec t)/y$、(2.43) 的 $[t_1,t_2]=t_3$、$\rho$ 由分拆/Jordan 型决定、中心化子 $Z_\rho(G)$ | **一致**。旧卡 quote「Supersymmetry requires that the residue of the pole should be the images」与 (2.43) 的语义相同；旧卡的页号 [55] 属它自己底本的页序，不能当本篇页号用。 |
| 库内旧卡 `datasets/ggl22/cards/concepts/half-bps-bc-triple.json` | definition 栏 | (ρ,H,B) 三元组与 §2.5 p28 的表述 | **一致**。旧卡「G 显式破缺到 H、ρ 决定极点残数且与 h 对易、B 是带 H 对称的三维边界场论」正是 (2.45) 前后那段。 |
| 库内旧卡 `datasets/kw06/cards/concepts/canonical-coisotropic-brane.json` | definition 栏 | §4.3 脚注 17 说的 c.c. 膜边界条件 | **相容**。旧卡：$M_H(G,C)$ 上空间充满 rank-1 A-膜、$F=(\mathrm{Im}\,\tau)\omega_J$；本篇给的是它的四维规范理论侧描述（(4.37) 的三形式微扰）。脚注 17 的记号换算是本篇自述，未在 KW06 译本里逐式复核（库内 01 只有卡片、没有本篇可 grep 的 txt）。 |
| arXiv `0804.2902v1`（`external/v1.pdf`，83 页；抽文 `external/v1_pages/`） | v1 p060（印刷 59） | (3.52) 与非增排序条件是否 v2 才加 | **v1 同页同式号已有 (3.52) 与排序条件**，故这两条不是 v2 新增；v1 的节列表从 §3.8 直接到 §4，**没有 §3.9**，即 v2 comment 说的 "enhanced analysis of Nahm's equations" 主要是新增 §3.9（约 5 页）。 |
| arXiv `2611.18118`（`external/ref2611.xml`，摘要） | 摘要 | Nahm 极点是否以主嵌入 su(2) 标号；Nahm 极点与 Neumann 的对偶方向 | **一致**。摘要：「the boundary fugacities are specialized along the principal embedding of $\mathfrak{su}(2)$」，并提出 Nahm 极点边界条件与「Neumann + 边界费米多重态」的镜像对称——这正是本篇 §3.8「Neumann 的对偶是主嵌入极点」在 3d N=4 半指标层面的实现。 |

### 勘误

本稿共发现 2 处原文笔误，均为 **low**（只有内部证据、无第二处独立出处），卡片不改写、只登记：

- **E1**（p034 第 11 行）：「the most useful way to understand the hyper-Kähler manifold **H**」应为 **M**。依据：p033 明确定义 $H$ 是与 $\rho$ 交换的子群、其李代数为 $\mathfrak h$；p032/p033/p034 首段把该模空间一直叫 $M$；§3.1.1 的 $H$ 作用是群作用，不是流形。**v1 同页同句也作 H**（`external/v1_pages/p033.txt`），说明不是 v2 引入的排印事故，作者两版都没改；只有内部证据，故判 low，卡片不引用该句。
- **E2**（p080 第 16 行）：「a **dimenstion** three term」应为 **dimension**。拼写错误，只有内部证据，判 low，卡片不引用该句。
- 另有 **一处曾被怀疑、最终判为无误**：§3.4.4 的 $s-n=m^2+m$（见 §4.1 第 4 行）。我最初按「$u(n)$ 按 $n=(n-m)+1^m$ 分解的不可约项数」手算得 $m+1$，与 $m^2+m$ 不符；改用原文自己给的 $s=n+2\sum_{i<j}n_j$ 代入后得 $m(m+1)$，完全一致。**这是我自己漏项，不是原文笔误**，故不记 errata，只在此留痕。
- 一处**版本差异**（不是笔误）：v2 新增 §3.9（3.9.1–3.9.3，约 5 页）与若干参考文献，v1 无 §3.9。正文其余处 (3.52) 等在两版同页同式号，可用作稳定性证据。

---

## 5. 不懂

1. **§3.4.4 的 $M_-$ 维数 $m^2-m$ 的来历**：原文只说 $M_-$ 是 $y\le0$ 半直线上 $m\times m$、在 $y=0$ 正则的解，然后给出 $\dim M_-=m^2-m$。我按「正则轨道维数 $d-r$」算得 $U(m)$ 情形是 $m^2-1-(m-1)=m^2-m$，能对上，但原文没有说明为什么这里的解模空间恰好是正则轨道；如果 $X(0)$ 非正则，维数会不会变，文中没有讨论。
2. **§3.7 的 $M_{H,Y}=\bigcup_\alpha M^\alpha_Y(X_\infty)///H_Y$**：$Y$ 取常值且与 $X$ 对易，按 (3.60) 它生成解的对称性；但「固定一个共轭方式 $Y_\infty=w+h$」与「按 $H_Y$ 而不是按 $H$ 做商」这两步的严格性，文中只给了理由、没有证明。$Y\neq0$ 时原来的 $H$ 对称性被破坏，这一点我接受，但分片 $\alpha$ 的指标集是否有限、各片维数是否相同，我没能推出来。
3. **§4.2 里 $q$ 是 $F$ 的非线性函数**：文中说 (4.23) 精确等价于 (4.25)，且 $q$ 是 $F$ 的非线性函数（含 $\sinh/\cosh$ 型重求和），我只验证了一阶 $q=(*_{012}+*_{456})F/8$。高阶项的具体形式（尤其 $\theta$ 角如何进入）我没有独立复算，只接受了「10 参 = 9 参 $F$ + 1 参 $\theta$」的计数论证。
4. **§4.4 的极大零子空间分类**：文中说与 $W_4'$ 交为零的 4 维子空间恰好由对称 $f$（自对偶 $q$）给出，与 $W_4$ 交为零者由对称 $g$（反自对偶 $\tilde q$）给出；「恰好」这一完备性我只逐行读了论证，没有独立验证「所有极大零子空间都落在这两类之一」。
5. **$B_0,B_1,B_2$ 与 $\Gamma$ 矩阵的具体表示**：文中只在 (2.8) 给 $2\times2$ 表示，未给 $V_8$ 上的显式矩阵。我按 $B_0^2=-1$、$B_1^2=B_2^2=1$、$B_0B_1=-B_1B_0=B_2$ 的代数关系核对了 (2.13)–(2.18)，但没有把 $V_8$ 矩阵写出来逐项验 (2.11) 的六个方程。
