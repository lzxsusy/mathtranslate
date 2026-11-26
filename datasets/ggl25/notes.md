# 第 25 篇 · 平坦联络模空间的量子化与 Liouville 理论

Teschner, *Quantization of moduli spaces of flat connections and Liouville theory*,
arXiv:1405.0359（ICM 2014 proceedings 投稿，25 页，单版本 v1）。

## 0. 页码约定

- 本包所有 `pages`/`p.N` 一律用 **PDF 页序**。本篇已核：PDF 页序 = 印刷页序（p016 页脚印 "16"，p018 印 "18"，p020 印 "20"），p001 为标题页，正文 §1 自 p001 开始。
- **式号怪癖（重要）**：§2 用 (2.1)–(2.13)、§3 用 (3.1)–(3.18)，但从 §4 起编号没有在每节重置：§4 的第一式是 **(4.19)**、§5 的第一式是 **(5.33)**、§6 的第一式是 **(6.38)**、§7 的第一式是 **(7.43)**。也就是说式号的**小数第二位是整个文档的全局计数器**，第一位是所属节号。写 locator 时按印刷式号照抄，不要"修正"成 (4.1)/(5.1)/(6.1)/(7.1)。
- 图：Fig.1（p4，迹函数相乘的两种光滑化）、Fig.2（p5，F-move 的两个裤子分解）、Fig.3（p5，S-move）、Fig.4（p6，Poisson 括号的反对称光滑化）。

## 1. 一句话

这篇综述把三件事钉在同一个 Hilbert 空间上：Teichmüller 空间 $T(C)$ 的量子化（Fock–Goncharov 剪切坐标 + 量子簇变换）、平坦 $\mathrm{PSL}(2,\mathbb{R})$-联络模空间 $M_{\rm flat}(C)$ 的 Teichmüller 分支的量子化、以及 $c>1$ 的 Liouville 共形场论；钉法是把三者的 **Moore–Seiberg 群胚表示**逐字对上，参数对应为 $\beta_e=\tfrac{Q}{2}+\mathrm{i}\,l_e/(4\pi b)$，于是"共形场论不过是描述 $M^T_{\rm flat}(C)$ 量子化的另一种语言"。

## 2. 文章骨架（节 → 页 → 一句话）

| 节 | 页 | 一句话 |
| --- | --- | --- |
| 摘要 | p001 | 综述 CFT、平坦 $\mathrm{PSL}(2,\mathbb{R})$-联络模空间量子化、量子 Teichmüller 理论三者的已知关系。 |
| §1 Introduction | p001–002 | 用经典 uniformization 把 $T(C)$ 与平坦联络、把 $T(C)$ 的对偶与向量场 Lie 代数、把后者的量子化与 Virasoro 串起来，勾出全文路线与"钻石"图景。 |
| §2 Flat connections and the Teichmüller space | p002–007 | 在 $M_{\rm flat}(C)$ 上装三套坐标：剪切坐标（簇变换）、迹函数（Fricke 关系）、Fenchel–Nielsen（Darboux），并把 Poisson 结构写成 Fricke 多项式的导数。 |
| §2.1 | p002–003 | character variety 定义、实切片的分支、Teichmüller 分支 $\cong T(C)$。 |
| §2.2 | p003 | 三角剖分、水平截面、剪切坐标 $X^\tau_e$、Atiyah–Bott 辛形式给出的 Poisson 括号、换对角线的簇变换。 |
| §2.3 | p004–006 | 迹函数 $L_\gamma$、骨架代数 $A(C)$、裤子分解与 Dehn 参数、生成元、Fricke 关系。 |
| §2.4 | p006–007 | Poisson 括号的显式公式，以及它与 Fricke 多项式"同一个多项式"的相容性；Fenchel–Nielsen Darboux 坐标。 |
| §3 Quantization of $M^T_{\rm flat}(C)$ | p007–011 | 把 §2 的坐标逐条量子化：量子环面关系、量子簇变换、量子迹函数、量子 Fricke 关系、裤子分解上的表示、Moore–Seiberg 群胚。 |
| §3.1 | p007–008 | 每条边一个生成元 $X^t_e$，关系含 $e^{2\pi\mathrm{i}b^2 n_{ee'}}$；换三角剖分由酉算子 $T_{t_2t_1}$ 实现。 |
| §3.2 | p008–009 | 量子迹函数是 Laurent 多项式；两条二次、两条三次量子 Fricke 关系。 |
| §3.3 | p009–010 | 不相交曲线交换 ⇒ 可同时对角化；$R_{\sigma|t}$ 把 $\pi_t$ 搬到"乘法算子"表示，波函数是 $l_e\in\mathbb{R}_+$ 的函数。 |
| §3.4 | p010–011 | $F,S,B,Z$ 四类 move、Moore–Seiberg 群胚、投影酉表示、以及表示只依赖群胚同构类。 |
| §3.5 | p011 | 与模函子的类比：由 $C_{0,3},C_{0,4},C_{1,1}$ 局部生成，但不是严格模函子（向量空间无穷维）。 |
| §4 Conformal field theory | p011–016 | Virasoro 表示、共形块、Virasoro 单值化、粘接构造、以及把共形块组织成 $T(C)$ 上的投影局部系统的两套 move。 |
| §4.1 | p011–012 | $c>1$ 最高权表示、共形块是满足 $F(\rho_\chi v)=0$ 的线性泛函、$CB(C,\rho)$ 无穷维。 |
| §4.2 | p012–014 | 共形块的全纯依赖、Virasoro 单值化 $T(C)\cong V_{\rm out}\backslash\oplus_k\mathbb{C}((t_k))\partial_{t_k}/V_{\rm in}$、$T(z_0)F=F'(L_{-2}e_0\otimes\cdot)$。 |
| §4.3 | p014–016 | 粘接构造：三点函数 $N$、$q^{L_0}$ 传播、转移函数 $W$、$S$-move 的积分核。 |
| §5 Comparison | p016–019 | 主结论：参数按 (5.33) 对应后，量子 Teichmüller 的群胚表示与 CFT 的完全一致；Verlinde 线算子；$T(C)$ 的 Kähler 量子化给出同一个故事。 |
| §6 Outlook: relations | p019–021 | 三个方向：非紧量子群（模双重）、三维双曲几何（体积）、可积模型（等单值变形、Painlevé VI）。 |
| §7 Outlook: quantisation commutes with reduction | p022–023 | 把 (4.31) 看成 $\mathrm{Diff}^+(S^1)$ 的 Plancherel 公式，猜测这是"量子化与约化交换"。 |
| References | p023–025 | 52 条，绝大多数是 Teschner 自己及其合作者的工作。 |

## 3. 主命题清单

| 编号 | 位置 | 命题 |
| --- | --- | --- |
| S1 | p002, §2.1 | character variety $M^C_{\rm char}(C):=\mathrm{Hom}(\pi_1(C),\mathrm{PSL}(2,\mathbb{C}))/\mathrm{PSL}(2,\mathbb{C})$ 就是"平坦 $\mathrm{PSL}(2,\mathbb{C})$-联络模 gauge"的解析空间，见 (2.1)。 |
| S2 | p002, §2.1 | 实切片 $M^R_{\rm char}(C)$ 分解为有限个连通分支 [Hit, Go88]；其中 Fuchsian 群所在的分支 $M^{R,0}_{\rm char}$ 与 $M^T_{\rm flat}(C)$ 重合。 |
| S3 | p003, §2.2 | 剪切坐标 $X^\tau_e$ 只依赖四边形与截面、不依赖点 $P$，见 (2.2)–(2.3)。 |
| S4 | p003, (2.4) | $\{X^\tau_e,X^\tau_{e'}\}=n_{e,e'}X^\tau_{e'}X^\tau_e$，$n_{e,e'}\in\{-2,-1,0,1,2\}$ 是对偶肥图上两条边的总相交指数；该括号来自 Atiyah–Bott 辛形式。 |
| S5 | p003, (2.5) | 换对角线的变换是簇变换 $X^{\tilde\tau}_{e'}=X^\tau_{e'}(1+(X^\tau_e)^{-\mathrm{sgn}\,n_{e'e}})^{-n_{e'e}}$，$e'\neq e$；$X^{\tilde\tau}_e=(X^\tau_e)^{-1}$。 |
| S6 | p004, (2.6)–(2.7) | 迹函数 $L_\gamma=\nu_\gamma\mathrm{tr}\,\rho(\gamma)$ 取 $\nu_\gamma$ 使 Teichmüller 分支上为正且 $>2$；$L_\gamma=2\cosh(l_\gamma/2)$；乘积由 $L_{\gamma_1}L_{\gamma_2}=L_{S(\gamma_1,\gamma_2)}$ 闭合，$S$ 为对称光滑化（Fig.1）。 |
| S7 | p004–005, §2.3.2 | 裤子分解 $\sigma=(\gamma,\Gamma)$ 用 Dehn 参数 $(r_e,s_e)$ 分类，Dehn 定理给出 (2.8) 三条限制：$r_e\ge0$；$r_e=0\Rightarrow s_e\ge0$；同一 pair of pants 上 $r_{e_1}+r_{e_2}+r_{e_3}\in2\mathbb{Z}$。 |
| S8 | p005–006, §2.3.3 | 骨架代数 $A(C)$ 由 $3(3g-3+n)$ 个迹函数 $L^e_s,L^e_t,L^e_u$（$e$ 跑 $\Gamma$ 的边）生成。 |
| S9 | p006, (2.9)–(2.11) | Fricke 关系 $P_e(L^e_s,L^e_t,L^e_u)=0$：$C_{0,4}$ 型见 (2.10)，$C_{1,1}$ 型见 (2.11)；生成元加关系把 $M_{\rm flat}(C)$ 描述为代数簇。 |
| S10 | p006–007, (2.12)–(2.13) | $A(C)$ 上有 Poisson 括号 $\{L_{\gamma_1},L_{\gamma_2}\}=L_{A(\gamma_1,\gamma_2)}$，且 $\{L^e_s,L^e_t\}=\partial P_e/\partial L^e_u$——同一个多项式既是簇的方程又是辛结构的势。 |
| S11 | p007, (3.1) | 量子化：每条边给生成元 $X^t_e$，$X^t_eX^t_{e'}=e^{2\pi\mathrm{i}b^2n_{ee'}}X^t_{e'}X^t_e$；$b^2$ 就是通常的 $\hbar$。 |
| S12 | p007–008, (3.2)–(3.3) | 换三角剖分由代数自同构（量子簇变换，量子双对数型乘积）实现，并由酉算子 $T_{t_2t_1}$ 表示；故量子理论不依赖三角剖分。 |
| S13 | p008, (3.4)–(3.5) | 量子迹函数 $\pi_t(L_\gamma)$ 是 $(X^t_e)^{\nu_e/2}$ 的 Laurent 多项式；一般曲线由简单三角剖分上的 $T_{t't}$ 共轭得到；$\pi_t(L_\gamma)$ 正自伴、谱下界 2，不相交曲线交换。 |
| S14 | p008–009, (3.6)–(3.10) | 量子 Fricke 关系：二次关系 $P^{(2)}=0$ 是 Poisson 括号 (2.13) 的形变，三次关系 $P^{(3)}=0$ 是 (2.9) 的形变；$C_{0,4}$ 与 $C_{1,1}$ 两种，各含 $b^2/2$ 或 $b^2$ 的半相位。 |
| S15 | p009–010, (3.11)–(3.12) | $\pi_\sigma(L_\gamma):=R_{\sigma|t}\pi_t(L_\gamma)R_{\sigma|t}^{-1}$ 把迹函数写成 $l,k$ 的算子（$k=-4\pi\mathrm{i}b^2\partial_l$），即 Fenchel–Nielsen 坐标的量子对应；极大定义域给出 Gelfand 三元组 $S_\sigma\subset H_\sigma\subset D_\sigma$。 |
| S16 | p010–011, (3.13)–(3.18) | 裤子分解之间的酉同构 $U_{\sigma_2\sigma_1}$ 只依赖四类 move（$F,S,B,Z$），满足带相位 $\zeta$（$|\zeta|=1$）的三角关系；由此得 MCG 的**投影酉**表示 (3.18)。 |
| S17 | p011, §3.5 | 这套表示"局部地"是模函子（由 $C_{0,3},C_{0,4},C_{1,1}$ 生成），但因只对稳定曲面定义且纤维无穷维，只是模函子的类比。 |
| S18 | p011–012, (4.19)–(4.21) | $c=1+6Q^2$ 的 Virasoro 最高权表示 $V_\alpha$（$L_0$ 特征值 $\alpha(Q-\alpha)$）；共形块是满足 $F(\rho_\chi v)=0$（$\chi\in V_{\rm out}(C)$）的线性泛函，$\dim CB(C,\rho)=\infty$。 |
| S19 | p012–013, (4.22)–(4.26) | 手征配分函数 $Z(F)=F(e)$；Virasoro 单值化 (4.25) 把"对复结构模求导"实现为 $V_{\rm out}$ 的作用，于是 $T(z_0)F=F'(L_{-2}e_0\otimes\cdot)$。 |
| S20 | p014–016, (4.27)–(4.32) | 粘接构造给出 $Z_\sigma(\beta,q)$；它们在 $S$-move 下由积分核 $F_{\beta_1\beta_2}$ 联系（(4.31)），对四点情形该核化为 DOZZ 型模核（(4.32)）。 |
| S21 | p016, (5.33) + 主结论 | 取 $\beta_e=\tfrac{Q}{2}+\mathrm{i}l_e/(4\pi b)$、$\alpha_r=\tfrac{Q}{2}+\mathrm{i}l_r/(4\pi b)$、$N(\alpha_3,\alpha_2,\alpha_1)=(C(Q-\alpha_3,\alpha_2,\alpha_1))^{1/2}$，则第 3 节与第 4 节的 Moore–Seiberg 群胚表示**同构**；从而 $H_{\rm CFT}(C,\rho)$ 存在、MCG 作用酉。 |
| S22 | p017–018, (5.34)–(5.36) | 退化 puncture（$\alpha\in -b\mathbb{Z}_{\ge0}/2-\mathbb{Z}_{\ge0}/(2b)$）给出 BPZ 方程 (5.34)；$\alpha_0=\alpha_{-1}=-b/2$ 时两个二维表示张量积含一维表示，用嵌入 $\imath$ 与投影 $\wp$ 定义 Verlinde 线算子 $L_\gamma=\wp\circ M(\mu_\gamma)\circ\imath$。 |
| S23 | p018, §5.1.3 末 | [AGGTV, DGOT] 对 Verlinde 线算子的显式公式与 [TV13]（即本篇 §3.3）的 $\pi_\sigma(L_\gamma)$ 精确吻合 ⇒ $A_{b^2}(C)$ 作用在共形块上，$S_{\rm CFT}\subset H_{\rm CFT}\subset D_{\rm CFT}$ 与 $S(C)\subset H(C)\subset D(C)$ 作为 $A_{b^2}$-模同构。 |
| S24 | p018–019, (5.37) | 另有一条独立的量子化路线：$T(C)$ 的 Kähler 量子化（$\Omega_{\rm WP}=\Omega_{\rm AB}|_{T(C)}$，$H_r\mapsto b^2\partial_{q_r}$），其波函数 $\Psi^\sigma_l(q)$ 与粘接共形块 $Z_\sigma(\beta,q)$ 相等。 |
| S25 | p020, (6.38) | 三维双曲几何：Fenchel–Nielsen 坐标变换的生成函数 $W$（$\kappa_s=\partial W/\partial l_s$，$\kappa_t=-\partial W/\partial l_t$）就是边长 $(l_1,\dots,l_4,l_s,l_t)$ 的双曲四面体体积；$b\to0$ 时 $b^2\log F(l_s,l_t)\to \mathrm{Vol}_T(l)$。 |
| S26 | p020–021, (6.39)–(6.41) | 可积模型 I：$b\to0$ 的 BPZ 方程就是等单值变形；WKB 拟设给出 Hamilton–Jacobi 型方程 (6.41)。 |
| S27 | p021, (6.42) | 可积模型 II：Painlevé VI 与 Schlesinger 的 $\tau$ 函数是共形块在 $\beta\mapsto\beta+\mathbb{Z}^N$ 上的 Fourier 求和。 |
| S28 | p022–023, §7 | 把 (4.31) 读作 $\mathrm{Diff}^+(S^1)$ 上的 Plancherel/完备性陈述，最终解释为"量子化与约化交换"（§7 正文跨到 p023 上半页，参考文献自 p023 下半页起）。 |

## 4. 与库内已译文献的接口

本篇**参考文献里没有任何一篇**属于库内 01/02/06/11/16/23/28/36，接口全是概念性的。逐条列出可用之处与差别：

| 库内篇 | 接口点 | 差别（写卡片时必须交代） |
| --- | --- | --- |
| 01（KW06，扭化参数 $t$、$S$-对偶、brane 词典） | 本篇 §1 的"钻石"（CFT / Hitchin 模空间 / 几何 Langlands）正是 [T10] 的口径，而 [T10] 与 KW06 是同一张图的两侧；01 的 brane 词典里 $A$-brane/$B$-brane 与这里的"共形块 / 量子 Teichmüller 波函数"是同一对偶的两套语言。 | 01 用 $\Psi$（四维规范场）的语言，本篇完全不提四维；本篇的"模空间"是二维曲面上的平坦联络，不是 Hitchin 模空间本身，而是它的一个边界分量/Teichmüller 部分。 |
| 02（规范理论分歧与几何朗兰兹） | 都可作为"平坦联络模空间为什么与 Langlands 有关"的背景。 | 02 讲 $^L G$ 局部系统与 Hecke 特征层；本篇只到 $\mathrm{PSL}(2,\mathbb{R})$ 的 Teichmüller 分支，不提 Hecke 特征层。 |
| 06（镜像对称 Hitchin 与朗兰兹） | Hitchin 模空间的超对称量子化、$b\to0$ 的 WKB 与"体积"主题相接（本篇 (6.38)）。 | 06 是四维 $N=4$ 的镜像对称图景；本篇的 (6.38) 只是三维双曲体积，没有超对称。 |
| 11（量子力学路径积分） | §7 "量子化与约化交换"以及 §5.2 "Kähler 量子化 = 几何量子化"的语义背景。 | 11 的路径积分是有限维/量子力学的，本篇的量子化是形变量子化（$\hbar=b^2$），两条路线在本篇里被 (5.37) 对起来。 |
| 16（几何内窥与镜像对称） | 几何 Langlands 的"特征层"一侧；本篇 §1 明确把几何 Langlands 列为"钻石"的第三个角。 | 16 讲内窥与稳定化；本篇不涉及内窥。 |
| 23（四维规范场论纽结不变量） | **最实的接口**：23 的 Wilson/'t Hooft 圈与本篇 §5.1.3 的 Verlinde 线算子是同一种"沿曲线插入的算子"，本篇把 [AGGTV, DGOT] 的显式公式与量子 Teichmüller 的 $\pi_\sigma(L_\gamma)$ 做了逐字比对。 | 23 的圈是四维的（沿纽结），本篇的 $\gamma$ 是曲面上的简单闭曲线，算子作用在共形块上；且本篇明确指出这是**另一条**路线（Verlinde 圈 [Verlinde 90]）而非 't Hooft 算子本身。 |
| 28（bdh，Hitchin 可积系统量子化与 Hecke 特征层） | §5.2 的 Kähler 量子化与 28 的"Hitchin 可积系统的量子化"是同一套几何量子化技术的两个特例；$H_r$（Hamiltonian 截面）的角色也一致。 | 28 的模空间是 Hitchin 模空间（复维度 $2\dim$），本篇是 Teichmüller 空间（复维度 $3g-3+n$，即 Hitchin 模空间的"$SO(2)$ 部分"或 $b\to0$ 的极限），只保留 Abel 化后的 $H_r$。 |
| 36（朗兰兹与共形场论讲义） | 36 把共形块与 Hecke 特征层并置；本篇给出"共形块 = 量子 Teichmüller 波函数"这一更具体的等同。 | 36 的共形块是 WZW/仿射型，本篇是 Liouville（Virasoro, $c>1$）；两者通过 AGT 才相接（本篇只在 §1 提一句）。 |

库内可引用的既有卡（只作 related/对照，不属于本篇出处）：`csw/concept/flat-connection-moduli`（平坦联络模空间）、`csw/concept/conformal-blocks`（共形块）、`csw/concept/verlinde-formula`（Verlinde）、`csw/concept/wilson-line`（Wilson 圈）、`bdh/concept/hitchin-fibration`、`bdh/concept/hitchin-integrable-system`、`glc/concept/gl1-trace-character`（迹函数）。

## 5. 记号核对

| 记号 | 出现处 | 是否前后一致 | 处理 |
| --- | --- | --- | --- |
| $\rho$ | p002 单值表示 $\rho:\pi_1(C)\to\mathrm{PSL}(2,\mathbb{C})$；p012 起 $\rho$ 又是粘在 puncture 上的 Virasoro 表示数据，$CB(C,\rho)$ | **二义** | 卡片里显式区分"单值表示"与"共形块数据"；引用时写 $CB(C,\rho)$ 并注明 $\rho=(\alpha_r)$。 |
| $X^\tau_e$ / $X^t_e$ | §2 用三角剖分 $\tau$，§3 用 $t$ | 同物异号 | 卡片统一写 $X^t_e$，加注"§2 记作 $X^\tau_e$"。 |
| $\Delta_l$ | (3.15) $B=e^{\pi\mathrm{i}(\Delta_{l_3}-\Delta_{l_2}-\Delta_{l_1})}$，$\Delta_l=\frac{1+b^2}{4b}+(\frac{l}{4\pi b})^2$ | 与共形维数 $\Delta_\alpha=\alpha(Q-\alpha)$ **不是同一个量** | $\Delta_l-\Delta_\alpha=\frac{1+b^2}{4b}-\frac{Q^2}{4}=-\frac{Q(Q-1)}{4}$ 为常数；因 $B$ 算符只定义到一个相位，常数不改变 $B$。详见 errata 附近说明与 `quantum-teichmuller-algebra` 的 pitfall。 |
| $Q$ | p011 (4.19) 起就用（$c=1+6Q^2$、$\Delta=\alpha(Q-\alpha)$），但直到 p016 (5.33) 才写 $Q=b+b^{-1}$ | **先用后定义** | 不算笔误（$\mathbb{R}$ 上的标准记号），notes 记录；卡片在首次出现处补 $Q=b+b^{-1}$。 |
| $L_\gamma$ | p004 是经典迹函数（$\mathbb{C}$-值函数），p018 是 Verlinde 线算子（作用在共形块上的算子） | 同名不同物 | 卡片写 $L_\gamma$（经典）与 $\hat L_\gamma$ / "$L_\gamma$ 作为算子"两种，明确语境。 |
| $b,\hbar,q,\tilde q$ | p007 $b^2=\hbar$；p019 $q=e^{\pi\mathrm{i}b^2}$、$\tilde q=e^{\pi\mathrm{i}/b^2}$ | 一致 | 卡片注明 $q$ 不是模参数（§4.3 的 $q=e^{2\pi\mathrm{i}\tau}$ 是**另一个** $q$）。 |
| $n_{e,e'}$ | (2.4) 与 (3.1) 同一套整数 | 一致（(3.1) 明说"coincide with the structure constants of (2.4)"） | — |
| 维数 | $\dim M^C_{\rm char}=6g-6+2n$；$H_t\cong L^2(\mathbb{R}^{3g-3+n})$；$\Gamma$ 的边数 $=3g-3+n$；生成元 $3(3g-3+n)$；$CB$ 的变量数 $3g-3+n$ | 一致（除 E1） | 三角剖分的边数是 $6g-6+3n$，与 $3g-3+n$ 只差 $n$（puncture 的差别），见 errata E1。 |

## 6. 外部校正五项动作清单（按 XREF §4）

1. **主定理陈述与符号**：摘要（arXiv abs 页逐字与 p001 摘要一致）说"review known results on the relations between CFT, quantization of moduli spaces of flat PSL(2,R)-connections, and quantum Teichmüller theory"；正文主结论 p016 的弱化表述（"isomorphic as representations of the Moore–Seiberg groupoid"）与摘要一致，没有夸大。被引复述：nLab "quantum Teichmüller theory" 页把"量子 Teichmüller 的 Hilbert 空间 = Liouville 共形块空间"记为 Verlinde 1990 的**猜想**，本篇 p016 给的是群胚表示层面的定理（比猜想弱、比猜想精确），两者不冲突。库内互引：无（见 §4）。结论：**一致**。
2. **关键公式系数/符号/指数**（每条两个独立出处，详见「### 外部来源」表）：(2.1)、(2.4)、(3.7)–(3.10)、(3.15)、（4.19）、(5.33) 全部核过；(3.4) 的指数范围与另一处冲突（E1）。
3. **命题编号与交叉引用**：本篇编号自 (2.1) 起连续，p020 的"(3.14) reduces to (6.38)"指群胚关系 (3.14) 的经典极限，成立（(3.14) 的 intertwiner 在 $b\to0$ 变成生成函数）；脚注 6 引 [T01] 的 "(201)"，在 hep-th/0104158 的文本里确有单独编号 (201) 的式子；脚注 5 的"cubic relations"指对 $L_s,L_t,L_u$ 三次，成立。
4. **数值/维数一致性**：$H_t\cong L^2(\mathbb{R}^{3g-3+n})$ 与裤子图边数一致；$\dim M_{\rm char}=6g-6+2n$ 与 TV13 一致；仅 (3.4) 的 $\mathbb{Z}^{3g-3+2n}$ 与"components $\nu_e$"、与三角剖分边数 $6g-6+3n$ 不一致（E1）。
5. **记号前后定义是否同义**：见 §5 表；发现 $\rho$ 二义、$X^\tau/X^t$ 同物异号、$\Delta_l$ 与 $\Delta_\alpha$ 不同、$Q$ 先用后定义、$L_\gamma$ 同名不同物，均已在 notes 与相关卡片的 pitfall/provenance_note 里交代，未判为笔误。

## 7. 自己看不懂 / 未验算的地方

1. **(3.12) 的第二项**：$\sum_{\varepsilon=\pm1}\frac{1}{\sqrt{2\sinh(l/2)}}e^{\varepsilon k/2}\sqrt{c_{12}(L_s)c_{34}(L_s)}\frac{1}{\sqrt{2\sinh(l/2)}}e^{\varepsilon k/2}$ 里 $e^{\varepsilon k/2}$ 出现在两个因子的外侧、$k=-4\pi\mathrm{i}b^2\partial_l$ 又是微分算子，我没有逐项验算它确实满足 (3.9) 的 $C_{1,1}$ 型关系；只确认了它在 $b\to0$ 的经典极限给出 Fenchel–Nielsen 的生成函数（与 (6.38) 相容）。
2. **(3.2) 与 FG2 的量子簇变换**：本篇写的是 $\prod_{a=1}^{|n|}(1+e^{\pi\mathrm{i}(2a-1)b^2}X^{-\mathrm{sgn}\,n})^{-\mathrm{sgn}\,n}$，我核到它与 FG2 的量子双对数形式一致，但没有独立验算"酉算子 $T_{t_2t_1}$ 的存在性"（(3.3)）——原文只说"there exists"，未给构造。
3. **(4.20)–(4.21) 的 $V_{\rm out}(C)$ 与 $n=1$ 的 Weierstrass gap 例子**：原文用一句话带过（"one may use the Weierstrass gap theorem"），我没有把它与 $CB(C,\rho)$ 的具体维数对上。
4. **(4.31) ⇒ (4.32)**：原文说 [HJS] 证明；我没有核 [HJS] 的证明，只确认 (4.32) 的相位 $e^{\pi\mathrm{i}(c/12)(\tau+1/\tau)}$ 与 $S_{\beta_1\beta_2}(\alpha_0)$ 的形式与 Liouville 模核的文献一致。
5. **§6.3.1 的 $b\to0$ WKB**：从 $Z=e^{W/b^2}\psi$ 到 (6.40) 的 $v_k^2+t_{k,2}=0$，中间"$t_{k,1}=0$"这一步是原文的断言，我没有验算（它依赖 $Z$ 对 $u_k$ 的依赖只通过 $W$ 这一拟设）。
6. **§7 的环带半群 $An$ 与 $T(C)$ 开子集的等同**：原文只给了一个"can be identified with"的断言，我没有找到严格陈述。
7. **(3.4) 的 $F$ 有限集**：原文说 $F$ 是有限集，但没有给界；(3.5) 用 $T_{t't}$ 共轭来定义一般 $\gamma$，我没有验证这样定义的 $\pi_t(L_\gamma)$ 与三角剖分无关（这依赖 (3.17) 的相位 $\zeta$ 恰好在共轭中抵消）。

## 8. 核对与勘误

### 外部来源

每条都实际取到全文并逐处定位；抓取方式：arXiv PDF → `pdftotext`，再按式号/页码回定位。

| 来源 | 定位 | 核了什么 |
| --- | --- | --- |
| arXiv:1405.0359 摘要页与提交历史 | abs 页；v1 2014-05-02 08:22:30 UTC | 只有 v1 无修订；25 页；"contribution to the proceedings of the ICM 2014"；无 journal-ref；摘要逐字与本篇 p001 摘要同。 |
| Teschner–Vartanov, arXiv:1302.3778（[TV13]） | (6.3)(6.4)(6.5)(6.6)、(6.15b) 与 $\Delta(l)$ 定义、(6.21)(6.22)(6.23)、§6.2 | 本篇 (3.7)(3.8)(3.9)(3.10) 与 TV13 的对应式逐字相同（含 (3.9) 的 $b^2/2$ 半相位、(3.10) 的 $e^{\pi\mathrm{i}b^2}(L_s^2+e^{-2\pi\mathrm{i}b^2}L_t^2+L_u^2)$）；(3.15) 的 $\Delta_l=\frac{1+b^2}{4b}+(\frac{l}{4\pi b})^2$ 与 TV13 的 $\Delta(l)$ 全同；(5.33) 与 TV13 (6.21) 的 $\alpha_e=\frac{Q}{2}+\frac{\mathrm{i}l_e}{4\pi b}$ 全同；TV13 §6.2 每条三角剖分边一个 $X_e$。 |
| Fock–Goncharov, arXiv:math/0311149（[FG1]） | §1.2 的 (1.27)–(1.29)、Fig.1.6 附注、$X^{P+}_{GL2,S}=\mathbb{R}^{6g-6+3n}$ | 剪切坐标的 Poisson 括号 $\{X_{j_1},X_{j_2}\}=\varepsilon_{j_1j_2}X_{j_1}X_{j_2}$，$\varepsilon$ 为整数、反对称，与本篇 (2.4) 的 $n_{e,e'}\in\{-2,\dots,2\}$ 同型；$X$ 坐标的个数为内部边数 $6g-6+3n$。 |
| AGT, arXiv:0906.3219 | 摘要与正文（$c=1+6Q^2$，$Q=b+1/b$；$\Delta=\alpha(Q-\alpha)$） | (4.19) 的 $c=1+6Q^2$ 与 $L_0$ 特征值 $\alpha(Q-\alpha)$ 的约定；与 (5.33) 相容（此时 $\alpha(Q-\alpha)=\frac{Q^2}{4}+(\frac{l}{4\pi b})^2$）。 |
| nLab: *quantum Teichmüller theory*（2014-02-17 版） | Idea 段与 References | "According to a conjecture in (Verlinde 90) the corresponding Hilbert space may be identified with the space of conformal blocks of Liouville theory"——与本篇主线一致，但它是猜想形式；本篇 p016 给到群胚表示的层面。 |
| Teschner, arXiv:hep-th/0104158（[T01]） | 文末编号 (201) 的式子 | 本篇脚注 6 引 "[T01, eq (201)]"，该式在原文中确实存在（未逐条核内容）。 |

### 勘误

逐条结论（详见 `errata.tsv`）：

- **E1（medium）**：p008 (3.4) 的求和范围写作 $\nu\in\mathbb{Z}^{3g-3+2n}$，但同句说"with components $\nu_e$"，而 (3.4) 的乘积跑遍三角剖分 $t$ 的边 $e$，边数是 $6g-6+3n$（FG1 §1.2 给出 $X^{P+}_{GL2,S}=\mathbb{R}^{6g-6+3n}$；TV13 §6.2 每条边一个 $X_e$，而 $l_e$ 只有 $3g-3+n$ 个）。判为原文笔误，订正为 $\mathbb{Z}^{6g-6+3n}$。**依据1 + 依据2 齐全**，但只有一处与本篇内部的冲突（"components $\nu_e$"），故置信度记 **medium** 而不是 high；卡片里不写这个指数范围（只写"按边标号取 Laurent 多项式"），故"影响卡片 = -"。
- **未判为笔误的三处**（写在这里以免后来者重复怀疑）：
  1. (3.9) 的 $b^2/2$ 半相位看似给出 $\{L_s,L_t\}=\frac12(2L_u-L_sL_t)$（少一个 2），但 TV13 (6.5) 逐字相同，且这是 $C_{1,1}$ 的半相位约定 ⇒ 不是笔误；
  2. (3.15) 的 $\Delta_l=\frac{1+b^2}{4b}+\cdots$ 与 $\Delta_\alpha=\frac{Q^2}{4}+\cdots$ 差一个常数 $-\frac{Q(Q-1)}{4}$，因 $B$ 只定义到相位 ⇒ 不是笔误（TV13 同式）；
  3. (5.34) 的 $(\partial_{z_0}^2+b^{\pm2}T(z_0))Z=0$ 与 $\alpha=-b^{\pm1}/2$ 的配对：用 level-2 零向量系数 $\kappa=-(4\Delta+2)/3$ 验算得 $\kappa=b^{2}$（对应 $-b/2$）与 $\kappa=b^{-2}$（对应 $-1/(2b)$），配对正确 ⇒ 不是笔误。
- 其余（(2.1) character variety、(2.4) Poisson、(2.10)(2.11) Fricke、(3.1) 量子环面、(3.7)(3.8)(3.10) 量子 Fricke、(4.19) Virasoro、(5.33) 参数对应、(6.38) 体积）与至少一处独立出处一致，**本稿其余未发现笔误**。
