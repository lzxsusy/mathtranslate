# ggl22 — Gaiotto–Witten, *S-Duality of Boundary Conditions in N=4 Super Yang-Mills Theory*

arXiv:0807.3720（hep-th），172 页（本地 PDF 页序），出版于 Adv. Theor. Math. Phys. **13** (2009) 721–896。
本笔记配合 `cards/concepts/` 14 张、`cards/derivations/` 6 张、`terms.tsv`、`excerpts.md`、`errata.tsv` 使用。

## 0. 页码约定

全部页码为 **PDF 页序**（本库统一约定）。本篇经三处核对：p005 页脚印「4」且正文是 §1 Introduction；p050 页脚印「49」；p076 页脚印「75」。即 **PDF 页 = 印刷页 + 1**。
arXiv 元数据标称 170 页，本地 PDF 却是 172 页（p001 是标题页，p168 致谢，p169–p172 是参考文献）。两页之差的原因我没查明（不是封面/印章页），但这不影响页序约定：一律以本地 PDF 页序为准，不做任何换算。

## 1. 一句话

本文把四维 N=4 规范理论的 S-对偶从「理论 ↔ 理论」推广到「边界条件 ↔ 边界条件」：把半 BPS 边界条件编码成五膜构型，证明 S-对偶在边界上就是三维 N=4 的 mirror symmetry，由此得到一类自镜的边界 SCFT $T(G)$ 及其极点推广 $T^\rho_{\rho'}(G)$，并把整个构造提升为作用在边界条件上的 $SL(2,\mathbb Z)$。

## 2. 文章骨架（节 → 一句话）

| 节 | PDF 页 | 一句话 |
|---|---|---|
| §1 Introduction | 005–006 | 边界条件由三元组 $(\rho,H,B)$ 分类；两条主线：S-对偶 ↔ 3d mirror、自镜的 $T(SU(n))$。 |
| §2.1 Brane Constructions | 007 | 半 BPS 边界条件 ↔ D3/D5/NS5 构型，R-对称性破到 $SO(3)\times SO(3)$。 |
| §2.2 Ordering | 011–015 | 五膜必须「良序」：净 D3 数非零的 D5 在 NS5 右侧，同类膜的 linking number 从左到右非降。 |
| §2.3 S-Duality | 016–018 | S-对偶 = 交换 NS5/D5 并交换 $\vec X\leftrightarrow\vec Y$；交换后次序错，移膜恢复次序，构型类封闭。 |
| §2.4 Quivers: Good, Bad, Ugly | 019–029 | monopole 的 R-荷公式 (2.15)；$n_f\ge 2n_c$ 为 good，$=2n_c$ 为 balanced，$2n_c-1$ 为 ugly，$\le 2n_c-2$ 为 bad。 |
| §3.1–3.2 U(1), U(2) | 031–049 | 最小例子：$U(1)$ 的 $T(U(1))$ 是两个 $U(1)$ 的 CS 耦合；$U(2)$ 展示一般机制。 |
| §3.3 U(n) | 050–069 | Dirichlet 的对偶是 Neumann $+T(SU(n))$（自镜）；Nahm 极点 ↔ 幂零共轭类 ↔ Young 图；$T_\rho$、$T^\rho$、$T^\rho_{\rho'}$。 |
| §3.4 A General Recipe | 070–075 | 任意边界条件 $B$：ungauging 给出的 mirror 是 $B_H\times_H T^\rho(SU(n))$（(3.13)，全篇最重要结论）。 |
| §3.5 Domain Walls | 076–081 | 把 $G_1\times G_2$ 边界条件折成 domain wall（folding trick），对偶可逐字读出。 |
| §4.1 $T(G)$ | 082–085 | 任意紧群 $G$ 的 $T(G)$：对称性 $G\times G^\vee$，Higgs/Coulomb 分支为 $\mathcal N,\mathcal N^\vee$，$T(G)\leftrightarrow T(G^\vee)$ 互为 mirror。 |
| §4.2 Nahm pole | 086–089 | 两端加极点得 $T^\rho_{\rho^\vee}(G)$，分支由 Slodowy slice 与幂零轨道的交给出（Table 1）。 |
| §4.3 General Duality Prescription | 090–096 | 一般处方 $B\mapsto \tilde B^\vee=B_H\times_H T^\rho(G)$；$S^2=1$（有 $S^2=C$ 的 subtlety）。 |
| §4.4 $T(U(1))$ | 097–100 | 用两形式场验证 §4.1 的抽象定义给同一个 $U(1)$ 理论。 |
| §4.5 Massive Deformations | 101–105 | 加质量形变后边界条件如何流动。 |
| §5 SO/Sp | 106–121 | 把 (2.15) 用到 $SO(k)$、$Sp(2t)$：good 条件为 $n_f\ge k-1$、$n_f\ge 2t+1$，excess 相应平移。 |
| §6.1–6.3 Orientifolds/Orbifolds | 122–130 | $U(n)$ 的三类 involution（Class I/II/III）↔ $O5^+/O5^-/I_4(-1)^{F_L}$ orbifold；Table 3 给出各自的 S-对偶。 |
| §6.4–6.6 | 131–140 | orthosymplectic quiver 的极点、中心荷与对称性增强。 |
| §7.1–7.2 O3 review | 141–155 | O3 四型与半 D5：$SO(2n),SO(2n+1),Sp(2n),Sp'(2n)$；单半 D5 只给奇数秩极点。 |
| §7.3–7.4 | 156–162 | 一般 SO/Sp 边界条件的 S-对偶、$O3+O5$ 组合。 |
| §8.1–8.3 Theta-Angle | 163–168 | 边界条件上的 $SL(2,\mathbb Z)$ 作用：$T$=CS 系数平移、$S$=复合 $T(G^\vee)$；$(ST)^3=1$；$(p,q)$ 五膜与分数 CS。 |
| References | 169–172 | 52 条。**全文没有结论节**，p168 致谢后直接进参考文献。 |

## 3. 主命题清单（原文有编号的式子给式号，无编号的命题编号 S1–S13 为本笔记所加）

- **S1（p005）**：半 BPS 边界条件由三元组 $(\rho,H,B)$ 分类：$G$ 在边界附近破缺到 $H$，$\rho:\mathfrak{su}(2)\to\mathfrak g$ 是嵌入，$B$ 是带 $H$ 对称性的边界场论。
- **S2（p012、p013–p014）**：五膜构型的两条约束——(i) 净 D3 数非零的 D5 全在 NS5 右侧；(ii) 对每类五膜，linking number 从左到右非降。满足约束的构型才能读出干净的 quiver。
- **S3（p018）**：S-对偶（NS5↔D5、$\vec X\leftrightarrow\vec Y$）交换两类 linking number；配合「移膜恢复次序」的唯一步骤，**满足约束的构型类在 S-对偶下封闭**；推论：每个每节点 $n_f\ge 2n_c$ 的线性 quiver 都有同类的 mirror。
- **S4（p024–p026）**：monopole 的 R-荷 $q_R=\frac12(\sum|h_i|-\sum|v_j|)$（2.15）；线性 quiver 上 $q_R=\sum_i(\Delta_i+A_i+B_i)$（2.22），$e_i=m_i+n_{i-1}+n_{i+1}-2n_i$（2.18）；good $\Leftrightarrow$ $e_i\ge0$。
- **S5（p050）**：Dirichlet 边界条件（$n$ 个 D3 各终止在一个 D5 上）的 S-对偶 = Neumann 耦合 $T(SU(n))$；$T(SU(n))$ 自镜。
- **S6（p055–p056）**：Nahm 极点的残数给出 $\rho$，$\rho$ 等价于幂零共轭类，也等价于分拆 $n=\sum d_i$ 与 Young 图；Young 图沿主对角线翻转给对偶 ${\rho^D}$；brane 上第 $i$ 个 D5 接 $d_i$ 个 D3，对应 $T_\rho(SU(n))$。
- **S7（p058–p060）**：$\mathcal H_{T_\rho}=\overline{\mathcal O_{\rho^D}}$；$\mathcal H_{T^\rho}=S_\rho\cap\mathcal N$（Slodowy slice 与幂零锥之交）；两极点情形 $\mathcal H=S_\rho\cap\overline{\mathcal O_{\rho'^D}}$、$\mathcal C=S_{\rho'}\cap\overline{\mathcal O_{\rho^D}}$，记 $T^\rho_{\rho'}(SU(n))$，mirror 为 $T^{\rho'}_\rho$。
- **S8（p073，(3.13)）**：$\tilde B^\vee=B_H\times_H T^\rho(SU(n))$。原文称 "the single most important conclusion of the present paper"。
- **S9（p074–p075）**：对偶边界条件 $B^\vee$ 何时降秩/带极点？当且仅当 ungauging 构型有 $q_R\le0$ 的手征算子；对偶地 composite 理论有 $q_R\le0$ 的 monopole。
- **S10（p082–p087）**：$T(G)$ 的对称性 $G\times G^\vee$，Higgs/Coulomb 分支为 $\mathcal N,\mathcal N^\vee$；$T(G)\leftrightarrow T(G^\vee)$ 互为 mirror；带极点时 Table 1 给出四个分支公式。
- **S11（p128–p130）**：Class I/II/III ↔ $O5^+/O5^-/$orbifold；orbifold 的 S-对偶是 $O5^-$ 加一个 D5；$I_4(-1)^{F_L}$ 的一般 Class III 与 $Sp(n)$ 只在 $p=q$ 时对偶；Table 3 与 Nadler [41] 完全一致（作者原话）。
- **S12（p141–p152）**：O3 四型（$O3^-,\tilde eO3^-,O3^+,\tilde eO3^+$）与其规范群；单半 D5 只给奇数秩 Nahm 极点，偶秩需 full D5 且会得到 bad quiver。
- **S13（p163–p168）**：$S$ 与 $T$ 提升为边界条件上的变换，生成 $SL(2,\mathbb Z)$；$(ST)^3=1$ 用 $N=3$ Janus 壁证；$(p,q)$ 五膜与分数 CS 的 (8.2)（(8.3) 是忽略通量求和的近似）。

## 4. 与库内已译文献的接口

**先说结论**：本篇是纯物理文章，全篇**不出现** geometric Langlands / ramification / Hecke / endoscopy 任何字样（对 172 页 txt 做过 grep，唯一命中是参考文献 [29] 的标题）。所以库内接口分两类：**引用**（只有 #02）与**概念相接**（其余）。

### 4.1 直接引用：只有 #02 Gukov–Witten

- p099（§4.4 $T(U(1))$ 的开头）原文：「We follow [28] and section 2.4 of [29]」——[29] 即 Gukov–Witten, *Gauge Theory, Ramification, and the Geometric Langlands Program*（hep-th/0612073 = 本库 #02），[28] 是 Witten 的 *On S-Duality in Abelian Gauge Theory*（hep-th/9505186）。也就是说：**本文 §4.4 的 $U(1)$ 电-磁对偶推导直接建立在 #02 的 §2.4 之上**。
- 概念上更强的一层：#02 把「带 Nahm 极点的边界条件」对应到「分歧（ramification）数据」，而本文的 $\rho$（幂零共轭类、Young 图、$T_\rho$ 与 $T^\rho$ 的对偶）就是同一套数据的物理侧。本文没有做这个翻译，但两张卡的 $\rho$ 可以逐字接上 #02 的分歧参数。
- 另有 [1] = Gaiotto–Witten, *Supersymmetric Boundary Conditions in N=4 SYM*（0804.2902，本文的前作，库内没有）与 [2] = 同作者 Janus 文（0804.2907）。本文大量引用 [1] 的 §3（Nahm 方程解模空间、Slodowy slice），读本篇前最好先有 [1] 的结论。

### 4.2 逐条对账表

| 库内 | 是否被本文引用 | 接口性质 |
|---|---|---|
| 01 Kapustin–Witten `kw06` | **否**（grep 不到 0604151） | 概念相接：同一条「S-对偶 ↔ 几何朗兰兹」主线；本文 §8.1 的 direct/twisted action 与 KW06 的 A/B 型 brane 语言可对译；本文的 $T(G)$ 是 KW06 边界条件语言的群论化。 |
| 02 Gukov–Witten `SY02-06` | **是**（[29]，p099） | 直接：§4.4 的 $U(1)$ 对偶沿用其 §2.4；$\rho$ ↔ 分歧数据。 |
| 06 Witten `SY05-25` | 否 | 概念相接：mirror symmetry 与 Hitchin 方程；本文 §4 的 $T(G)$ 分支（$\mathcal N$ 与 $\mathcal N^\vee$）与 3d mirror 的 Hitchin 图像同源。 |
| 11 Witten `SY03-01` | 否 | 弱：只有「把 $\tau$ 解析延拓、让耦合随位置变」的方法论关联（Janus 壁）。 |
| 16 Frenkel–Witten `SY01-07` | 否 | 概念相接：内窥（endoscopy）与外自同构。本文的 Class I/II 恰是**外**自同构 involution（$H=O(n),Sp(n)$），正是内窥的物理侧。 |
| 23 Gaiotto–Witten `SY05-01` | 否（晚于本篇） | 概念相接：同作者；domain wall / Janus 与 folding trick 是同一套技术，本文 §3.5 的 folding trick 在 23 里用来算纽结不变量。 |
| 28 Beilinson–Drinfeld `SY02-14` | 否 | 概念相接：Hecke 特征层 ↔ 本文的 $T(G)$ 与 §8 的 $SL(2,\mathbb Z)$ 轨道；本文给物理侧，BD 给几何侧。 |
| 36 Frenkel `SY03-21` | 否 | 背景：$L$-群 $G^\vee$ 的定义与「对偶群」的来历；本文把 $G^\vee$ 用作 mirror 伙伴的整体对称性。 |

### 4.3 概念相接的三处具体点

1. **Nahm 极点 = 分歧**：$\rho$ 的分拆数据 $\{d_i\}$（#02 的分歧指标）↔ 本文的 Young 图；$T_\rho$ 与 $T^\rho$ 的对偶 ↔ 分歧的「对偶分歧」。这一条是两篇之间最实在的桥。
2. **$SL(2,\mathbb Z)$ 与 Hecke 算子**：本文 §8 的 $S,T$ 作用与 §4 的 $T(G)$ 复合，正是几何朗兰兹里 Hecke 算子作用在 $\mathcal D$-模上的物理对应；#28 的 Hecke 特征层可以看成 $T(G)$ 型边界条件的对偶描述。
3. **外自同构 = 内窥**：Class I（$O(n)$）与 Class II（$Sp(n)$）来自 $\tau^2=\pm1$ 的外自同构，#16 的内窥正是处理外自同构诱导的 Langlands 函子性；本文 Table 3 的四种约化可以看成内窥的物理名单。

### 4.4 本文自己承认接不上的地方

- 全文没有结论节，也没有把结果翻译成朗兰兹语言——作者只在引论里说「与 3d mirror symmetry 密切相关」，此后不再提。
- p096 承认 $S^2=1$ 有 subtlety（复表示时可能 $S^2=C$），未展开。
- p130 用一整节把 Table 3 与 Nadler [41] 对照，明确说「perfect agreement」，但没有给出数学上的证明（只是逐项比对）。

## 5. 记号表

| 记号 | 含义 | 首见页 |
|---|---|---|
| $(\rho,H,B)$ | 边界条件的三元组 | 005 |
| $\vec X,\vec Y$ | 6 个伴随标量的两组，分别对应 456 与 789 方向 | 007 |
| $\ell$ | linking number：左侧异类五膜数 + 右侧终止于该膜的净 D3 数 | 011 |
| $q_R$ | monopole 算子的 R-荷 | 024 |
| $e_i$ | excess：$m_i+n_{i-1}+n_{i+1}-2n_i$ | 026 |
| $T(SU(n))$ | Dirichlet 的对偶边界 SCFT，自镜 | 050 |
| $\rho^D$ | Young 图转置对应的对偶嵌入 | 055 |
| $T_\rho(SU(n))$ | 带 Nahm 极点 $\rho$ 的边界 SCFT（Higgs 侧） | 056 |
| $T^\rho(SU(n))$ | 其对偶（Coulomb 侧） | 059 |
| $S_\rho$ | Slodowy slice（横截于 $\rho_+$） | 059 |
| $\mathcal N,\mathcal O_\rho$ | 幂零锥、幂零轨道 | 059 |
| $T^\rho_{\rho'}(SU(n))$ | 两端各带极点的最一般情形 | 060 |
| $T(G)$ | 任意紧群 $G$ 的对应物，对称性 $G\times G^\vee$ | 082 |
| $\tilde B^\vee$ | $B^\vee$ 的 mirror（不是 $B^\vee$ 本身） | 073 |
| Class I/II/III | $U(n)$ 的三类 involution | 123 |
| $O3^\pm,\tilde eO3^\pm$ | 四型 O3 平面 | 141 |
| $Sp'(2n)$ | theta 角差 $\pi$ 的 $Sp(2n)$ | 141 |
| $(p,q)$ 五膜 | NS 荷 $p$、D5 荷 $q$ 的五膜 | 166 |

## 6. 不懂的地方（诚实清单）

1. p074–p075 的 $q_R\le0$ 判据：$W(p)$ 的路径排序指数与正规化 $\hat W=\lim_{\epsilon\to0}\epsilon^{-it_3}W_\epsilon(p)$ 我只读了陈述，没有跟上「拉伸 Wilson 线给出 composite 理论 monopole」的构造。
2. §3.2（p040–p049）$U(2)$ 的逐例计算我只扫读，没建卡；若要用 $U(2)$ 交叉验证一般公式，需要重读。
3. §4.5 massive deformations（p101–p105）完全没读。
4. §5.2–5.4（p108–p121）的 orthosymplectic quiver 我只取了结论（good 条件、monopole 计数），排表过程没核。
5. §6.2 的弦论构造（p126–p127）与 §6.4–6.6（p131–p140）没读，Table 3 的 $\tilde EH$ 记号我按上下文理解为「与 $H$ 对偶的那一侧的群」，可能与原文定义有偏差。
6. §7.1.2 的 monopole/orientifold 讨论（p149–p150）没读；fig 65(b) 的半个 D3 账目我只有文字转述。
7. §7.3–7.4（p156–p162）只读结论。
8. $T_\rho=T^0_\rho$、$T^\rho=T^\rho_0$ 的下标约定是我从 p058 与 p059 的分支公式反推的（见 trace），原文没有明写；若这条错了，编号 9 的卡片要改。
9. p096 的 $S^2=C$ 只说了一句，$C$ 与 $SL(2,\mathbb Z)$ 中心元 $-1$ 的对应我未验证。
10. p167–p168 关于 FQH 里 (8.3) 合法的论证，我接受结论但没试算通量求和。
11. 「$q_R$ 是整数或半整数」的量子化（p024 引 [6]）未核原文。
12. Table 2 的 $I_4(-1)^{F_L}$ 与 O5 型的对应，我只按正文转述，没核 orbifold 投影的路径积分。

## 7. 卡片与原文的对应

| 卡片 | 页 |
|---|---|
| `concept/half-bps-bc-triple` | 005 |
| `concept/brane-construction-bc` | 007, 012, 014 |
| `concept/s-duality-brane-action` | 016, 018 |
| `concept/good-bad-ugly` | 024–026, 106–107 |
| `concept/t-su-n` | 050, 082 |
| `concept/nahm-pole-bc` | 055, 151 |
| `concept/nilpotent-young-duality` | 055, 058 |
| `concept/t-rho-su-n` | 056, 058 |
| `concept/t-rho-rhoprime` | 060 |
| `concept/t-g` | 082, 083, 086 |
| `concept/involution-bc` | 122, 123, 130 |
| `concept/o3-planes` | 141, 142, 152 |
| `concept/sl2z-action-bc` | 163, 165 |
| `concept/pq-fivebrane-fractional-cs` | 166–168 |
| `deriv/dirichlet-dual-t-su-n` | 050 |
| `deriv/nahm-pole-young-transpose` | 055–056 |
| `deriv/ungauging-general-recipe` | 070–073 |
| `deriv/monopole-r-charge` | 024–026 |
| `deriv/s-duality-mirror` | 005, 050, 082–086 |
| `deriv/st-cubed-janus` | 165–166 |

## 8. 枝节（写进笔记，不建卡）

- §3.1 $U(1)$ 的四维计算（p031–p039）：用两形式场与 gerbe 的显式做法，结论并进 $T(U(1))$ 的卡片，细节不建卡。
- §3.2 $U(2)$ 的逐步构造（p040–p049）：作者用它演示「先猜后证」的流程，技术细节重复，不建卡。
- §4.4 的 (4.7)–(4.9)（p097–p100）：两形式场 $k$、扩展规范对称性 $B\to B+b$、$k\to k+db$，是 $U(1)$ 对偶的标准做法，只在与 #02 的接口里提。
- §4.5 massive deformations（p101–p105）：不建卡。
- §5.2–5.4 orthosymplectic quiver 的枚举（p108–p121）：大量具体例子，不建卡。
- §6.2 弦论构造、§6.5–6.6（p126–p140）：不建卡。
- §7.3–7.4 的 $O3+O5$ 组合（p156–p162）：不建卡。
- §2.4 的 ugly 理论真空分支 $\mathbb C\times\mathcal H$（p025）：只进 good-bad-ugly 卡的一段。

## 9. 核对与勘误

本篇共 172 页、52 条参考文献、无编号定理，所以要核的不是定理陈述而是**公式系数、表格列序、记号约定**。下面五项按 XREF.md 的动作清单逐条回查。

### 外部来源

| 来源 | 定位 | 核了什么 |
|---|---|---|
| arXiv API + INSPIRE recid 791356 | 元数据 | 只有 v1（2008-07-23），标称 170 页而本地 PDF 172 页（差异未查明）；出版信息 Adv. Theor. Math. Phys. 13 (2009) 721–896、zbMATH Zbl 1206.81082 一致；页码一律按本地 PDF 序。 |
| Gaiotto, arXiv:1609.09030 §D.2 | 独立文献 | Nahm 极点边界条件 "labelled by an embedding ρ of su(2)"、破缺到 commutant $G_H=Z_\rho(G)$、BAA twist 下 Higgs 场落 Slodowy slice $S_\rho$——与本文 p055/p086 的 $\rho$、commutant、$S_\rho$ 表述逐项一致。 |
| Cremonesi–Hanany–Mekareeya, arXiv:1309.2657 (2.4) | 独立文献 | 其 $\Delta(m)=-\sum_{\alpha\in\Delta_+}|\alpha(m)|+\frac12\sum_i\sum_{\rho_i\in R_i}|\rho_i(m)|$ 与本文 (2.15) $q_R=\frac12(\sum|h_i|-\sum|v_j|)$ 同构（矢量侧 $\sum_{\text{all}}|v|=2\sum_{\alpha>0}|\alpha|$），**独立确认 (2.15) 的 $\frac12$ 与正负号**。 |
| Nadler, math/0202150 Table 1 | 独立文献 | 本文 p130 自述「our table is in perfect agreement with that of [41]」；我按 p130 的文字版 (1)′、(2)′ 与该文 A_{n−1} 前三行的结构对照，约化群与 pole 形状相符（未逐格核原表，只核了文字版）。 |
| Witten, hep-th/0307041（本文 [22]） | 本文自引 | $SL(2,\mathbb Z)$ 在三维 CFT 上的作用，是 §8.1 的 $S$ 作用的来源；与 (ST)³ 的论证一致。 |
| 内部恒等式复核 | 原文 p024/p026/p107 | (2.16)↔(2.17)、(5.3)↔(5.4)、(5.7)↔(5.8) 三对公式互为代数恒等（用 $\sum_{i<j}(|a_i|+|a_j|)=(N-1)\sum|a_i|$，$N=n_c,k,2t$）——**没有系数笔误**。 |

### 勘误

`errata.tsv` 里记两条，都是「同一份文件内部两处说法互相冲突」型，故最高只到 medium：

1. **E1（medium，open）p141 Table 4 的通量列序**。表的两列是 RR 与 NS 离散通量，表注按「RR and NS」的顺序描述；但按此读，$\tilde eO3^-$ 的 RR 通量为 0，与同页正文「Adding half a D3-brane changes the RR discrete flux to 1」直接矛盾；$O3^+$ 按此读带 RR 通量，而正文说它带 NS 通量。按 **(NS, RR)** 读则四处全通，且 $S$ 交换两类通量使四个 S-对偶关系全部正确。结论：表注/列序笔误（不是物理错误），卡片按正文写并在 pitfalls 里注明列序存疑。
2. **E2（low，open，存疑）p055 与 p056 的 $d_i$ 单调性方向**。p055 说 $d_i$ "arranged in nondecreasing order"，p056 说 "we take the $d_i$ to be non-increasing"，而 p056 又说 D5 的 linking number **等于** $d_i$、p014 的第二约束要求 linking number 从左到右**非降**。三处互相冲突，且只影响 Young 图画法（$\{d_i\}$ 是多重集，物理不变），无法判定哪一处是笔误，故只记 low 存疑、不改卡片。建议以 p056 + Young 图惯例（行长度非增）为准。

**本稿还记下三处「我们自己的」问题**（不改原文，只写在这里，免得以后分不清是谁的锅）：

1. E2 的判定我反复了三次：先判「p056 错」（因为它与 p014 的非降要求冲突），再判「p055 错」（因为 Young 图惯例是非增），最后才意识到两页说的是不同的东西（p055 说的是把分拆排成图的行序、p056 说的是 brane 的可分离性），且方向只影响画法——于是降为 low 存疑。这条完整写进 `trace.md`。
2. p025 的 balanced 情形我一度记成 $a_i=(\pm1,\mp1,0,\dots,0)$ 才有 $q_R=1$；按 (2.17) 核算，正确的是**单个** $\pm1$ 分量 $a_i=(\pm1,0,\dots,0)$（此时 $\sum|a_i|=1$、交叉项为 0）。已改正，也写进 `trace.md`。
3. $T_\rho$ 与 $T^\rho$ 的下标方向：原文 p060 只说 "$T_\rho$、$T^\rho$ 都是 $T^\rho_{\rho'}$ 的特例"，没有指明哪个下标是哪个。我按「$T_\rho$ 的 Higgs 分支 $=\overline{\mathcal O_{\rho^D}}$（p058）」与「$T^\rho$ 的 Higgs 分支 $=S_\rho\cap\mathcal N$（p059）」反推出 $T_\rho=T^0_\rho$、$T^\rho=T^\rho_0$ 才能在两个公式间自洽。这是本稿的**推断**（provenance B），已写在卡片里。
