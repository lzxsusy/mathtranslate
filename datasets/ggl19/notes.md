# 19 · Kapustin《量子几何朗兰兹对偶、规范理论与平坦联络模空间的量子化》通读笔记

| 项 | 值 |
|---|---|
| 英文题名 | A Note on Quantum Geometric Langlands Duality, Gauge Theory, and Quantization of the Moduli Space of Flat Connections |
| 作者 / 机构 | Anton Kapustin / California Institute of Technology |
| arXiv | 0811.3264v1 [hep-th], 20 Nov 2008 |
| 篇幅 | 18 页（`txt/19/p001.txt` … `p018.txt`） |
| 体裁 | Note（非正式论文），**全文没有一个编号定理**，结论一律以「论证 + 断言」给出 |
| 引用文献 | 18 条 |

## 0. 页码约定

卡片 `sources.pages` 与所有 `anchor`（含推导步 `locator`）里的 **`p.N` 一律指 PDF 页序**，即
`txt/19/pNNN.txt` 的 N，便于逐页回查。

印刷页码 = PDF 页 − 1：`p001` 是标题+摘要页（页脚印 `0`），`p002` 起印 `1`，`p018` 印 `17`。
凡本笔记正文说「印刷页 x」，指的是页脚数字；说 `p.x` 指 PDF 页。

## 1. 一句话

把 Kapustin–Witten 的 GL 扭化取在 **t = 0** 这个「手征」端点上，Montonen–Olive 对偶就变成
「平坦联络模空间 $M_{\mathrm{flat}}(G_{\mathbb C},C)$ 与 $M_{\mathrm{flat}}({}^LG_{\mathbb C},C)$
的量子化导出 Morita 等价」，量子化参数 $\hbar=(\mathrm{Im}\,\tau)^{-1}$；翻译成 D-模语言就是
**量子几何朗兰兹对偶在纯虚量子参数 $q=-i\,\mathrm{Im}\,\tau$ 处的陈述**。

## 2. 文章骨架（节 → 一句话）

| 节 | PDF 页 | 一句话 |
|---|---|---|
| Title + Abstract | p001 | MO 对偶给出 $M_H(G)$ 与 $M_H({}^LG)$ 上 A-膜范畴等价；本文把它改写为量子化平坦联络模空间上 B-膜范畴的等价，从而推出纯虚量子参数的 QGL；分歧版本一并处理。 |
| §1 Introduction | p002–p005 | 三条 Langlands 物理化身（数域/函数域、几何、量子几何）的谱系；Atiyah 的 MO 猜想；KW 用扭化推出几何 Langlands；指出 KW 推导的两个不足（$q$ 只能实、$\theta$ 与 $\hbar$ 无关），宣布本文的修法。 |
| §2 GL-twisted theory at t=0 | p005–p006 | 写出场内容、手征 BRST 算子 $Q_0$ 的变换、作用量 $S=\{Q,V\}+\frac{i\bar\tau}{4\pi}\int\mathrm{Tr}\,F\wedge F$ 与定域方程；论证配分函数与 $\tau$ 无关、局域可观测全为零。 |
| §3 Reduction to two dimensions | p006–p007 | $C\times\Sigma$ 上约化得到靶为 $M_H(G,C)$ 的 A-模型，其 Kähler 形式与 B-场由 $B+i\omega=-\bar\tau\,\omega_I$ 决定；给出 $\omega_I,\omega_J,\omega_K$ 的归一化与 $\omega_I$ 的上同调类（即 $L_0$）。 |
| §4 From A-branes to noncommutative B-branes | p007–p011 | 构造 **d.c. 膜**（$F=\mathrm{Im}\,\tau\,\omega_K$）；边界可观测代数 = $(M_{\mathrm{flat}},J)$ 上全纯函数的量子化，$\mathrm{Im}\,\tau$ 就是 $1/\hbar$；讨论 $\mathrm{Re}\,\tau\neq0$ 的 B-场、Azumaya 推广、若干 A-膜例子及其对偶像。 |
| §5 From noncommutative B-branes to twisted D-modules | p011–p013 | $M_{\mathrm{flat}}\cong$ 扭化余切丛 $A_{L_0^{-1}}(\mathrm{Bun}_G)$；扭化余切丛的量子化 = $K^{1/2}\otimes L^{i\lambda/\hbar}$ 上的全纯微分算子；代入得 $\mathcal O(L_0^{-h^\vee-i\,\mathrm{Im}\,\tau})$，故 $q=-i\,\mathrm{Im}\,\tau$。 |
| §6.1 Line operators | p014 | 只剩 descent 型线算子 $\int\mathrm{Tr}\,\psi\sigma$；Wilson 型不存在，'t Hooft 型被 BPS 方程 + 球对称定标不变性排除。 |
| §6.2 Surface operators | p015 | 曲面算子由四元组 $(\alpha,\beta,\gamma,\eta)$ 参数化；$t=0$ 时只有 $\alpha$（控 Kähler 类）与 $\eta$（控 B-场）要紧；MO 作用为 $(\alpha,\eta)\mapsto(\eta,-\alpha)$。 |
| §6.3 Ramified QGL | p015–p017 | 插曲面算子 ⇒ 抛物 Higgs 丛模空间；写出 $[\omega_I/2\pi]$、$[B/2\pi]$、$c_1(L_\hbar)$ 的分解，得到分歧版 QGL：$\mathrm{Im}\,{}^L\tau=1/(n_g\,\mathrm{Im}\,\tau)$。 |
| References | p016–p018 | 18 条。 |

## 3. 主命题清单（原文无编号，编号 S1–S9 为本笔记所加）

| 编号 | 页 | 一句话 |
|---|---|---|
| **S1** | p001（摘要）、p003 | MO 对偶 ⇒ $M_H(G,C)$ 与 $M_H({}^LG,C)$ 上 A-膜范畴等价；本文把它改写为「量子化 $M_{\mathrm{flat}}(G_{\mathbb C},C)$ 与 $M_{\mathrm{flat}}({}^LG_{\mathbb C},C)$ 上 B-膜范畴等价」，并由此推出纯虚量子参数的 QGL。 |
| **S2** | p003 eq (1) | QGL 的参数关系 ${}^Lq=-\dfrac{1}{n_g q}$（$n_g=1,2,3$ 依 Dynkin 图最大边重数）；把 $q$ 读作 $1/\hbar$ 时，$q\to\infty$ 与 ${}^Lq\to0$ 互为对偶极限，此极限下 QGL 退化为经典几何 Langlands。 |
| **S3** | p004 | GL 扭化有一族 BRST 算子 $Q_t$（$t\in\mathbb C\cup\{\infty\}$），MO 对偶在参数上作用 $t\mapsto{}^Lt=t|\tau|/\tau$；经典几何 Langlands 是 $\theta=0,\,t=i,\,{}^Lt=1$，本文取 $t={}^Lt=0$。 |
| **S4** | p006 eq (6) | MO 对偶 ⇒ 靶为 $M_H(G,C)$ 与 $M_H({}^LG,C)$ 的两个 A-模型等价，当且仅当复化 Kähler 类满足 ${}^L\tau=-\dfrac{1}{n_g\tau}$。 |
| **S5** | p007–p008 | 存在 **d.c. 膜**：$\mathrm{Re}\,\tau=0$ 时 $M_H(G,C)$ 上曲率 $F=\mathrm{Im}\,\tau\,\omega_K$ 的秩一线丛；其边界可观测代数是 $(M_{\mathrm{flat}}(G_{\mathbb C},C),J)$ 上全纯函数环的量子化，$\mathrm{Im}\,\tau$ 充当 $1/\hbar$，一阶交换子为 $[f,g]=-i(\mathrm{Im}\,\tau)^{-1}\Omega_J^{-1}(df,dg)$。 |
| **S6** | p009 | 由「极大维数余各向同性 A-膜存在 ⇒ A-膜范畴 ≅ 非交换形变上的 B-膜范畴」，MO 对偶等价于：两个量子化平坦联络模空间上凝聚层的导出范畴等价，即两个量子化函数代数是**导出 Morita 等价**的（由乘积空间上的一个对象/双模实现）。 |
| **S7** | p012–p013 | 扭化余切丛 $A_{L^\lambda}(M)$ 的量子化是 $K^{1/2}\otimes L^{i\lambda/\hbar}$ 上的全纯微分算子；取 $M=\mathrm{Bun}_G$、$L=L_0$、$\lambda=-1$、$\hbar=(\mathrm{Im}\,\tau)^{-1}$ 得 $L_0^{-h^\vee-i\,\mathrm{Im}\,\tau}$，故 $q=-i\,\mathrm{Im}\,\tau$，纯虚。 |
| **S8** | p014 §6.1 | $t=0$ 时没有 Wilson 型线算子，也没有 't Hooft 型（disorder）线算子；后者之不存在由「BPS 方程 + 球对称 + 标度不变 + GNO 量子化条件」给出，因为所得「电场」对应的电荷是纯虚的。 |
| **S9** | p015–p017 §6.3 | 分歧 QGL：在 $C$ 上 $s$ 个点插曲面算子后，等价的是 $\mathrm{Bun}_G(C;p_1,\dots,p_s)$ 与 $\mathrm{Bun}_{{}^LG}(C;p_1,\dots,p_s)$ 上的扭化 D-模导出范畴，条件为 eq (8) 与 $\mathrm{Im}\,{}^L\tau=\dfrac{1}{n_g\,\mathrm{Im}\,\tau}$（$\mathrm{Re}\,\tau=0$ 时）。 |

## 4. 与几何朗兰兹既有文献的接口

### 4.1 直接命中语料库「已译」清单的三条

本文参考文献 18 条，落在 `BRIEF.md §7` 已完成清单里的只有三条：

| 本文编号 | 文献 | 语料库序号 / 工程 | 本文用它的什么 |
|---|---|---|---|
| [12] | Kapustin–Witten, *Electric-Magnetic Duality and the Geometric Langlands Program*, hep-th/0604151 | **#01 / `kw06`（67 卡）** | 整个 GL 扭化机器（见 §4.2）；本文是它的一个「端点补充」 |
| [7] | Gukov–Witten, *Gauge Theory, Ramification, and the GL Program*, hep-th/0612073 | **#02 / `SY02-06`（全译）** | 曲面算子的定义与 $[\omega_I/2\pi]$、$[B/2\pi]$、$[\omega_K/2\pi]$ 的分解；分歧故事的骨架 |
| [3] | Frenkel, *Lectures on the Langlands Program and CFT*, hep-th/0512172 | **#36 / `SY03-21`（全译）** | QGL 的数学陈述与它和共形场论的关系（本文只作背景引用） |

另有两条落在**待译**清单：`[8]` = #03 刚性曲面算子（`ggl03`），`[9]` = #04 膜与量子化（`ggl04`）；
`[10]` Kapustin *A-branes and noncommutative geometry*（hep-th/0502212）与 `[15]` Pestun 不在 46 篇列表内。

### 4.2 本文引用了 KW 2006 的哪些构造（逐条对账）

| KW06 的构造 | 本文怎么用 | 本文改了什么 |
|---|---|---|
| GL 扭化的场内容：$A,\varphi,\sigma,\psi,\tilde\psi,\eta,\tilde\eta,\chi$，协变导数 $d+A$、幺正平凡化下 $A,\varphi$ 反 Hermite | §2 原样沿用，连符号约定都声明「use the notation of [12]」 | 无 |
| 一族超交换 BRST 算子 $Q_t=Q_\ell+tQ_r$，$t\in\mathbb C\cup\{\infty\}$ | 把 $t$ 当连续参数，研究端点 $t=0$（纯左手，「手征」） | KW 主要用 $t=i$（对应 $\theta=0$ 的几何 Langlands）与 $t=1$；本文取 $t=0$ |
| MO 对偶在 $t$ 上的作用 $t\mapsto{}^Lt=t|\tau|/\tau$ | §1 直接引用，用来说明「$t=0$ 是 MO 不变的端点」 | 无（这是本文能取 $t={}^Lt=0$ 的依据） |
| 三复结构 $I,J,K$（$IJ=K$）与 $\omega_I,\omega_J,\omega_K$ 的归一化（$\omega_I$ 周期为 $2\pi$ 整数倍，$H^2(M_H)=\mathbb Z$ 由其生成） | §3 全部照搬，并补上 $\omega_J,\omega_K$ 恰当而 $\omega_I$ 不恰当的对比 | 无 |
| A-模型只由 $(B,\omega)$ 决定，且 $B+i\omega=-\bar\tau\,\omega_I$ | §3、§4 的出发点 | 无 |
| **c.c. 膜**（canonical coisotropic brane）：$F=\mathrm{Im}\,\tau\,\omega_J$，$K$ 中 A-膜、$J$ 中 B-膜 | §4 的对照物；$t=0$ 时它是 $(A,B,A)$ 型 | 本文另造 **d.c. 膜**（$F=\mathrm{Im}\,\tau\,\omega_K$，$(A,A,B)$ 型），二者由超凯勒旋转相连 |
| 「最自然的量子化配方」带来 $K^{1/2}$ 修正（$\hbar^0$ 阶的 $c_1$ 修正） | §5 直接引用，作为把 $L^{i\lambda/\hbar}$ 提升为 $K^{1/2}\otimes L^{i\lambda/\hbar}$ 的理由 | 无（本文明确说这是「as explained in [12]」） |
| Hitchin 纤维化的 T-对偶解释「为什么 MO ⇒ A-膜范畴等价」 | §4 开头一句带过 | 无 |
| Wilson / 't Hooft 线算子 | §6.1 讨论它们在 $t=0$ 的命运：都不存在 | KW 在 $t=i$ 有 Wilson 与 't Hooft 的交换；本文在 $t=0$ 得到空集 |
| 扭化 D-模 ↔ A-膜的字典：$M_H(G,C)_K$ 上 A-膜 ↔ $\mathrm{Bun}_G$ 上扭化 D-模，$q=\theta/2\pi$ | §1、§5 沿用字典 | **改参数化**：$q$ 从实变复，本文取 $q=\bar\tau=-i\,\mathrm{Im}\,\tau$；并把 $q$ 与规范理论 $\hbar$ 挂钩（KW 中 $\theta$ 与 $\hbar$ 无关） |
| 「严格说是稳定丛/稳定联络的开子集，不是真正的余切丛」这一技术保留 | §5 脚注 3 重复同样的 gloss | 无（本文也 gloss over） |

**一句话概括接口**：本文 = KW06 的机器 + (a) 把端点从 $t=i$ 换到 $t=0$，(b) 把 c.c. 膜换成 d.c. 膜，
(c) 把 $q$ 从 $\theta/2\pi$ 换成 $\bar\tau$。三步都只是「换个端点/换张膜」，但结果把 $q$ 从实变纯虚，
并且第一次让 $q$ 等于规范理论普朗克常数的倒数。

### 4.3 与其余已译文献的关系（本文**没有**引用，但概念上相接）

- **#06 Witten, *Mirror Symmetry, Hitchin's Equations, and Langlands Duality***：本文用到的
  「Hitchin 纤维化 T-对偶 ⇒ A-膜等价」正是 #06 的主题；本文没有引它，是因为把这件事全部归给 [12]。
  若要补一条链，应在 #06 的 Hitchin 纤维化卡与本文的 `hitchin-moduli-hyperkahler` 卡之间建立 `related`。
- **#28 Beilinson–Drinfeld, *Quantization of Hitchin's Integrable System and Hecke Eigensheaves***：
  本文 §5 的「量子化 = 微分算子层」与 BD 的 $\mathcal D$-模/Hecke 特征层图像是同一件事的两个方向；
  本文走的是「从 $M_{\mathrm{flat}}$ 的辛几何出发」，BD 走的是「从 Hitchin 可积系统出发」。本文未引 BD。
- **#16 Frenkel–Witten, #23 Gaiotto–Witten, #11 Witten 路径积分**：与本文无直接接口，不赘。
- **#02 Gukov–Witten** 是本文 §6.2–§6.3 的唯一来源，见 §4.1。

### 4.4 本文自己承认接不上的地方

p004 明说：Fock–Goncharov [5] 也讨论过与平坦联络模空间相关的模空间的量子化并看到 Langlands 对偶的迹象，
但「the details of their set-up are rather different from ours and we do not understand the precise relationship」。
这条要原样保留，别在卡片里假装接上了。

## 5. 记号表

| 记号 | 含义 | 首次出现 |
|---|---|---|
| $G$, ${}^LG$ | 紧单连通单 Lie 群与其 Langlands 对偶（特征格 ↔ 余特征格互换） | p002 |
| $G_{\mathbb C}$, ${}^LG_{\mathbb C}$ | 对应的复化群 | p002 |
| $\mathrm{Bun}_G(C)$ | $C$ 上主 $G$-丛的模空间（实为模栈） | p002 |
| $L_0$ | $\mathrm{Bun}_G(C)$ 上由 $c_1$ 生成 $H^2$ 的全纯线丛；$G=SU(N)$ 时为行列式线丛 | p002 脚注 2 |
| $h^\vee$ | $G$ 的对偶 Coxeter 数 | p003 |
| $q$, ${}^Lq$ | 扭化 D-模的扭化参数（"quantum parameter"）；$q=0$ 对应**临界扭化** $L_0^{-h^\vee}$ | p002–p003 |
| $n_g$ | $1,2,3$，依 $G$ 的 Dynkin 图最大边重数 | p003 |
| $\tau=\frac{\theta}{2\pi}+\frac{4\pi i}{e^2}$ | 复化规范耦合 | p004 |
| $t$ | GL 扭化的 BRST 参数，$Q_t=Q_\ell+tQ_r$ | p004 |
| $M_H(G,C)$ | $C$ 上 $G$-Higgs 丛模空间（超凯勒） | p001 |
| $M_{\mathrm{flat}}(G_{\mathbb C},C)$ | 稳定平坦 $G_{\mathbb C}$-联络模空间 | p007 |
| $\omega_I,\omega_J,\omega_K$ | 三个 Kähler 形式 | p006–p007 |
| $\Omega_J=\omega_K+i\omega_I$ | $J$ 下的全纯辛形式 | p008 |
| $\mathcal A_{L^\lambda}(M)$ | 以 $T^*M$ 为模型、扭化为 $L^\lambda$ 的扭化余切丛 | p011 |
| d.c. / c.c. 膜 | distinguished / canonical coisotropic A-brane | p007 / p004 |
| $\hbar$ | 规范理论普朗克常数；本文 $\hbar=(\mathrm{Im}\,\tau)^{-1}$ | p008 |

## 6. 不懂的地方（诚实清单）

1. **仿射丛 $\leftrightarrow H^1(\Omega^1)$ 的翻译**。p010 用 Čech 1-上闭链 $\alpha_{U,\tilde U}$ 定义
   $\alpha(\mathcal A)\in H^1(\Omega^1_M)$，并说「$\alpha$ 是 $\bar\partial$-闭 ⇒ $dp_i dq_i$ 良定义」。
   我只验证了「转移函数差一个全纯 1-形式 ⇒ $dp\wedge dq$ 在重叠处一致」这一步，
   **没有**验证「$\bar\partial$-闭」与「$dp\,dq$ 闭/非退化」的等价，也没做 Čech 计算。
2. **$K^{1/2}$ 修正的必然性**。p012–p013 说：平凡的 $L$ 时「最自然」取 $L_\hbar=K^{1/2}$，
   理由是「这保证扭化微分算子代数同构于它的反代数，而 $p\to-p$ 的离散对称要求如此」。
   为什么这条要求**恰好**挑出 $K^{1/2}$（而不是 $K^{1/2}$ 乘一个 $n$-挠丛），以及为什么没有
   $\hbar^{-1}$ 或 $\hbar^{-2}$ 阶的更高修正，原文只有一句 "Asssuming that there are no higher-order corrections"。
   我照抄了结论，没有独立理解。
3. **$K^{1/2}=L_0^{-h^\vee}$ 这一步**。p013 直接写 $K^{1/2}\otimes L_0^{-i\,\mathrm{Im}\,\tau}=L_0^{-h^\vee-i\,\mathrm{Im}\,\tau}$，
   即把 $K^{1/2}$ 认成 $L_0^{-h^\vee}$。这与「临界扭化 = $L_0^{-h^\vee}$」的平移是同一件事，
   但我没有从 $\mathrm{Bun}_G$ 的典范丛算出这个指数；$h^\vee$ 从哪来（对偶 Coxeter 数）我只知道结论。
4. **d.c. 膜确实是 A-膜**。p008 说 $F=\mathrm{Im}\,\tau\,\omega_K$ 是 $K$ 型的 $(1,1)$ 形式，故为 $(A,A,B)$ 型。
   余各向同性 A-膜需要对 $(\omega_I^{-1}F)^2=-1$ 之类的条件；我没有逐项验证 $\omega_I^{-1}\omega_K$ 在 $M_H$ 上
   满足这个代数关系（在 Hitchin 模空间上这是「超凯勒旋转」的标准事实，但本文没证）。
5. **「极大维数余各向同性膜存在 ⇒ A-膜 ≅ 非交换形变上的 B-膜」这条定理的适用范围**。
   p009 引 [10]（并注 [15,12,9]），但没说 d.c. 膜是否满足「极大维数」。若 d.c. 膜支撑是整个 $M_H$，
   则维数够；这一点我是从「$F$ 非退化 ⇒ 支撑开」推的，属于我自己的补足（provenance B）。
6. **$\mathrm{Re}\,\tau=n\in\mathbb Z$ 时「边界可观测代数与 $\mathrm{Re}\,\tau=0$ 相同」**。
   p009 的理由是 "the gauge theory for $\mathrm{Re}\,\tau=n$ is isomorphic to the gauge theory for $\mathrm{Re}\,\tau=0$"。
   这是什么同构（大规范变换？$\theta$ 角的 $2\pi$ 周期性 + 某个伴变换？）原文没说，我不清楚。
7. **高秩（Azumaya）膜的曲率方程可解性**。p009 说 $F=\mathrm{Im}\,\tau\,\omega_K\cdot1+\mathrm{Re}\,\tau\,\omega_I\cdot1$
   在 $r\,\mathrm{Re}\,\tau\in\mathbb Z$ 时「may admit solutions」。这是 DUY 型存在性问题，本文只给必要条件，
   我没看到充分性论证，也没看到 $r$ 如何被 $\mathrm{Re}\,\tau$ 的分母决定。
8. **§6.1 的「无 Wilson 型」只有一句话**（"At $t=0$ there are no observables of this kind"），
   没有像 't Hooft 型那样给论证；我只能接受。
9. **$t\mapsto t|\tau|/\tau$ 的推导**。这是 [12] 的结果，本文直接引用；我没有回查 KW06 的对应节，
   所以卡片里这条标 provenance A（本文引用）而不是「我验证过」。
10. **分歧情形 $c_1(L_\hbar)$ 的「全纯依赖于 $\alpha_k^*+i(\mathrm{Im}\,\tau)^{-1}\eta_k$」**。
    p016 说这「as expected for the A-model in complex structure $I$」，但没解释为什么这个组合是全纯的；
    我理解为「A-模型的复化 Kähler 参数 $B+i\omega$ 必须以全纯方式出现」，但这只是我的解读（provenance C）。
11. **「导出 Morita 等价」的精确含义**。p009 只说「由乘积空间上一个对象实现，其截面给出双模」。
    这是 dg-范畴层的等价还是 $A_\infty$-层的？本文不区分，我也没深究。
12. **$n_g$ 的来源**。p003 说 $n_g=1,2,3$ 依 Dynkin 图最大边重数，但没说为什么是「最大重数」而不是别的
    （对 $A_n$ 是 1、$D_n$ 是 2、$E_6,E_7,E_8$ 是 3？$G_2$ 呢？）我没有独立核对这张表。

## 7. 卡片与原文的对应

| 卡 id | 类型 | 主要出处 |
|---|---|---|
| `ggl19/concept/gl-twist-at-t-zero` | 概念 | §2, p005–p006 |
| `ggl19/concept/hitchin-moduli-hyperkahler` | 概念 | §3, p006–p007 |
| `ggl19/concept/twisted-cotangent-bundle` | 概念 | §5, p010–p011 |
| `ggl19/concept/distinguished-coisotropic-brane` | 概念 | §4, p007–p010 |
| `ggl19/concept/azumaya-algebra` | 概念 | §4, p009 |
| `ggl19/concept/twisted-d-module` | 概念 | §1, §5, p002–p003, p012–p013 |
| `ggl19/concept/quantum-geometric-langlands` | 概念 | §1, p003; §4–§5 |
| `ggl19/concept/ramified-qgl` | 概念 | §6.2–§6.3, p015–p017 |
| `ggl19/deriv/dc-brane-to-noncommutative-algebra` | 推导 | §4, p007–p009 |
| `ggl19/deriv/quantize-twisted-cotangent` | 推导 | §5, p010–p013 |
| `ggl19/deriv/montonen-olive-parameter-map` | 推导 | §1, p003–p004 |
| `ggl19/deriv/no-t-hooft-at-t-zero` | 推导 | §6.1, p014 |

## 8. 枝节（写进笔记，不建卡）

- **A-膜的三个例子与它们的对偶像**（p010）：固定 $(0,1)$ 部分 / 固定 $(1,0)$ 部分给出 $J$ 全纯的
  Lagrange 子流形（$(A,B,A)$ 型）；由 3-流形 $N$（$\partial N=C$）的平坦联络限制定义的 $\alpha_N$
  也是复 Lagrange 子流形，但**在 $C$ 上非局域**，因而不能来自 4d 局域边界条件。
  对偶方面：c.c. 膜 ↔ oper 膜（猜测），d.c. 膜 ↔ oper 膜的超凯勒旋转像。这些都只是「plausible」，不建卡。
- **flat 线丛扭化 d.c. 膜**（p010）：得到更一般的 $(A,A,B)$ 膜；属技术细节。
- **曲面算子上的线算子**（p015）：当 $(\alpha,\eta)$ 不正则（被 Weyl 群某非平凡元素固定）时，
  $(\beta,\gamma)$ 参数空间有非平凡环路，对应曲面算子上的线算子。这是 §6.1 与 §6.2 的桥，但只一句。
- **$\mathrm{Re}\,\tau=n$ 时 d.c. 膜的推广**（p009）：$F=\mathrm{Im}\,\tau\,\omega_I+\mathrm{Re}\,\tau\,\omega_I$
  不恰当，上同调类为 $n\,c_1(\det)$；已并入 `distinguished-coisotropic-brane` 卡的一个要点。
- **Fock–Goncharov 的关系**：作者自己说不懂（见 §4.4），不建卡。
- **致谢、资助号**：与数学无关，略。

## 9. 核对与勘误

本篇的尺寸很小（18 页）但**没有任何编号定理**——全文 grep 不到 theorem/proposition/lemma/corollary，
结论一律以「论证 + 断言」给出。所以校正的重点不在定理陈述，而在**公式与参数的约定**。
以下逐条回查，凡涉及与他篇约定的地方都写明出处。

### 外部来源

| 来源 | 定位 | 核了什么 |
|---|---|---|
| `datasets/kw06` 卡 `kw06/deriv/table1-and-ng` | B p.3–12（KW06 §11 附近） | $n_g$ 的取值表：simply-laced 为 1，$F_4$ 为 2，$G_2$ 为 3，$\mathrm{Spin}(2k+1)$ 与 $\mathrm{Sp}(k)$ 为 2——与本篇「$n_g$ 由 Dynkin 图最大边重数决定（1,2,3）」**逐项一致** |
| `datasets/kw06` 卡 `kw06/concept/langlands-dual-group` | B p.11 | $S$ 变换在非单边群上为 $\tau\mapsto-1/(n_g\tau)$，与本篇式 (6) 同形；本篇的式 (1) 只是把同一关系搬到扭化参数 $q$ 上 |
| arXiv:0811.3264 摘要（arXiv API / INSPIRE recid 803143） | p.0 | 摘要说量子参数「purely imaginary … proportional to the inverse of the Planck constant」；正文 p.13 给出 $q=-i\,\mathrm{Im}\,\tau$ 且 $\hbar=(\mathrm{Im}\,\tau)^{-1}$，**摘要与正文一致** |
| 原文 p.3 式 (1) 与 p.7 式 (6) 互校 | p.3 / p.7 | 两式**不是**同一个式子：式 (1) 是扭化参数 $q$ 的关系（$^Lq=-1/(n_g q)$），式 (6) 是复化 Kähler 类 $\tau$ 的关系（$^L\tau=-1/(n_g\tau)$）。此前有卡片把两者混称，已改（见「勘误」第 2 条） |
| 原文全文式号交叉引用 | p.21 | 全文唯一一处式号引用是 p.21 的「…are related as in (6)…」，式 (6) 确实存在且就是 MO 条件——**没有串号** |

### 勘误

**本稿未在原文中发现笔误**（`errata.tsv` 只有表头）。但这次回查抓到了三处**我们自己的**问题，
都已直接改进卡片，不记入 errata（errata 只记原文的错误，免得以后分不清谁的锅）：

1. `montonen-olive-parameter-map` 的 `pitfalls[2]` 原写「把 $q=\bar\tau$ 直接代入 (1) 会得到
   $^Lq=1/(n_g i\,\mathrm{Im}\,\tau)$ 之类，须先算 $^L\tau$ 再取虚部」。这条**自相矛盾**：
   $\theta=0$ 时 $\tau=i\,\mathrm{Im}\,\tau$，故 $\bar\tau=-i\,\mathrm{Im}\,\tau=q$ 确实成立，
   而 $1/(n_g i\,\mathrm{Im}\,\tau)=-i/(n_g\,\mathrm{Im}\,\tau)$ 正是正确答案。
   真正的坑是 **$\theta\neq0$ 时 $q=-i\,\mathrm{Im}\,\tau\neq\bar\tau$**，直接代入会得到带实部的 $^Lq$，
   违反 QGL 对纯虚性的要求。已改写。
2. 两张卡把式 (6)（$\tau$ 的关系，位于 §4、PDF p.7）写成「§3、p.6」，把 $B$-场那段（PDF p.9）
   写成「p.6–7」。**按印刷页抄了，违反本库 PDF 页序约定**。已全部回查改正，并给每条 A 类出处
   补上 `quote`（英文原句），以后 `tools/verify_pages.py` 可机器回查。
   同类问题还有一处：`quantize-twisted-cotangent` 的 `pages` 写 `[10,13]` 却与自身 `anchor`
   的「p.12–13」矛盾（§5 起于 p.11，配方与代入都在 p.12–13），已改为 `[12,13]`。
   另有 6 处推导步 `locator` 指向了错误的页/节（`montonen-olive` 4 处、`quantize-twisted-cotangent`
   1 处、`dc-brane-to-noncommutative-algebra` 1 处），逐条对着原文改过——其中 `montonen-olive`
   第 4 步的式 (6) 是「印刷页 6 vs PDF p.7」那个坑的第二次冒头，说明这个错误是**系统性**的：
   抄的人在心里做了「印刷页 = PDF 页 − 1」的换算，而本库要求一律写 PDF 页序。
3. 结论性的一条：$\theta=0$ 时 $q=\bar\tau=-i\,\mathrm{Im}\,\tau$，所以「$q$ 是规范耦合的共轭」
   ——这句话比「$q$ 是纯虚的」信息量更大，已补进 `quantum-geometric-langlands` 卡的关键点。
