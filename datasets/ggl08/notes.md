# 第 08 篇笔记 · 六维视角下的几何朗兰兹

Witten, *Geometric Langlands from Six Dimensions*, arXiv:0905.2720（30 页，仅 v1，2009-05-17）。
本笔记页码 = PDF 页序 = 印刷页（p001 页脚印 1、p003 页头印 3、p020 页头印 20，均已核）。

## 一、文章骨架

| 节 | 页 | 一句话 |
| --- | --- | --- |
| §1 Introduction | 1 | $d$ 维 QFT 是 $d$-流形→配分函数、$(d-1)$-流形→态空间、$(d-2)$-流形→范畴的逐层结构。 |
| §1.1 Categories And Physics | 2 | 二维：范畴=边界条件/D-膜；三维 Chern–Simons：范畴=loop group 正能量表示。 |
| §1.2 Geometric Langlands | 3 | 四维 $\mathcal N=4$ 的第三种扭化下 $G\leftrightarrow G^\vee$ + 耦合取逆，即 $\mathrm{Coh}(Y_{G^\vee})\simeq\mathrm{D\text{-}mod}(Z_G)$。 |
| §2 Defects Of Various Dimension | 4 | $p$ 维算子：0 维局域、2 维曲面（分歧）、3 维壁（$G\to H$ 跳跃）。 |
| §3 Selfdual Gerbe Theory | 6 | 六维自对偶三形式 $H=\star H$ 没有作用量但有量子理论；$M_4\times T^2$ 上给出四维 $U(1)$ 电磁对偶。 |
| §4 The Nonabelian Case | 9 | 每个单链 $G$ 有六维 $(0,2)$ 理论；两个微扰极限（阿贝尔 gerbe / 五维规范理论）给出非阿贝尔对偶。 |
| §4.1 Space Of Conformal Blocks | 11 | 共形块空间 = $H^3(M_6,\mathbb Z)$ 的 Heisenberg 群的不可约模；与 level 1 WZW 平行。 |
| §4.2 What Is Next? | 14 | 固定 $T^2$ 只变 $M_4$，六维是理解几何 Langlands 的框架；六维是超共形场论的最高维数。 |
| §5 GL Duality For Surfaces | 15 | 研究 $(0,2)$ 在更一般的六维流形上，尤其是圆丛与超凯勒流形。 |
| §5.1 Circle Fibrations | 15 | 圆丛的扭转给五维有效作用量加 $\Delta I=\frac{i}{2\pi}\int_{M_5}f\wedge CS(A)$。 |
| §5.2 Allowing Singularities | 15 | 允许 $U(1)$ 作用有不动点：余维 3 轨迹 $W$ 上 $df=2\pi\delta_W$。 |
| §5.2.1 Role Of W | 17 | $\Delta I$ 沿 $W$ 有反常 ⇒ $W$ 上必须有 level 1 全纯 WZW。 |
| §5.2.2 More Concrete Argument | 18 | 用 M5-膜/D4-D6 的弦论构造具体实现 $W$ 上的 current algebra（只对经典型群）。 |
| §5.3 Compactification On A Hyper-Kähler Manifold | 18 | $M_6=\mathbb R\times S^1\times X$，未破缺 SUSY 给 $\{Q_\alpha,Q_\beta\}=2\delta_{\alpha\beta}(H-P)$，BPS 态空间 $\mathcal V$。 |
| §5.4 Taub-NUT Spaces | 20 | 带 triholomorphic $U(1)$ 的超凯勒四维流形由 $\mathbb R^3$ 上调和函数 $U$ 决定；$TN_k$ 是 $A_{k-1}$ 消解。 |
| §5.4.1 A Note On The Second Cohomology | 21 | 非紧使 $H^2$ 换成 $\Gamma_k\cong\mathbb Z^k$，二次型 $\sum y_i^2$。 |
| §5.4.2 Basis Of $\Gamma_k$ | 22 | $\tilde H^3(W\times TN_k)=\oplus_jH^1_{(j)}(W,\mathbb Z)$ ⇒ 共形块是 $k$ 个 level 1 WZW 块的张量积。 |
| §5.5 Two Ways To Compute The Space Of BPS States | 23 | 小 $S$（Description I）与小 $R$（Description II）两种算法必须给出同一个 $\mathcal V$。 |
| §5.5.1 Description I | 23 | $\mathcal V=\oplus_nH^*_{L^2\,\mathrm{harm}}(\mathcal M_n)$；电/磁分级。 |
| §5.5.2 Description II | 25 | $\mathcal V=\otimes_{j=1}^kW_j$；$P=L_0$，电核扮演 Description I 中磁荷的角色。 |
| §5.5.3 A Note On The Dual Group | 27 | 非单链情形沿 $S^1$ 用外自同构扭曲，得到 $H\leftrightarrow H^\vee$ 的对偶。 |
| §5.5.4 Points With Multiplicity | 28 | 重数 $r$ 的点 ⇔ $A_{r-1}$ 奇点处的 $\varphi:\mathbb Z_r\to G$ ⇔ level $r$ 可积表示。 |

## 二、主定理清单

1. **几何 Langlands 的基本断言**（p.3，引 [7]）：$\mathrm{Coh}(Y_{G^\vee}(C))\simeq\mathrm{D\text{-}mod}(Z_G(C))$，$Y_{G^\vee}(C)=\mathrm{Hom}(\pi_1(C),G^\vee)$、$Z_G(C)$ 为全纯 $G$-丛模栈。
2. **式 (1.2)**（p.4）：$\tau^\vee=-1/(n_g\tau)$，$n_g$ 为长短根长度平方比；单链时 $n_g=1$。
3. **式 (1.3)**（p.4）：半经典等价 $\tau\to\tau+1$、$\tau^\vee\to\tau^\vee+1$，因为瞬子数取整。
4. **式 (3.2)(3.3)**（p.8）：$H=F\wedge dx+\star F\wedge dy$ 时 $dH=0\iff dF=d\star F=0$（Maxwell）。
5. **式 (3.4)(3.5)**（p.8）：四维作用量与 $\tau=\theta/2\pi+4\pi i/e^2$；**式 (3.4) 的 $\theta$ 项原文缺 $i$**（见勘误 E1）。
6. **红外极限**（p.8）：$g_6(t)=t^2g_4\oplus g_2$、$t\to\infty$ 时六维理论收敛到四维 $U(1)$ 规范理论。
7. **式 (4.1)**（p.10）：$I_5=\frac{1}{8\pi R}\int_{M_5}\mathrm{Tr}\,F\wedge\star F$；系数 $R^{-1}$ 由六维共形不变性定出，不是 KK 的 $R$。
8. **式 (4.5)**（p.11）：$I_4=\frac{S}{8\pi R}\int_{M_4}\mathrm{Tr}\,F\wedge\star F$；对 $S,R$ 不对称。
9. **式 (4.12)**（p.14）：$Z_b(-1/\tau)=C\sum_a\exp(2\pi i(b,a))Z_a(\tau)$；特例给 $G$ 与 $G^\vee$ 的对偶（$G^\vee=G_{\rm ad}$）。
10. **式 (5.2)(5.4)**（p.15、p.17）：$\Delta I=\frac{i}{2\pi}\int f\wedge CS(A)$、$df=2\pi\delta_W$。
11. **式 (5.5)**（p.17）：$\Delta I\to\Delta I-i\int_WX_2$ ⇒ $\exp(-\Delta I)$ 是行列式线丛的截面 ⇒ $W$ 上 level 1 全纯 WZW。
12. **式 (5.6)=(5.15)**（p.19、p.23）：$\{Q_\alpha,Q_\beta\}=2\delta_{\alpha\beta}(H-P)$，$H-P$ 湮灭的态为 BPS 态。
13. **式 (5.12)(5.13)**（p.22）：$\tilde H^3(W\times TN_k,\mathbb Z)=H^1(W,\mathbb Z)\otimes\Gamma_k=\oplus_{j=1}^kH^1_{(j)}(W,\mathbb Z)$。
14. **式 (5.16)**（p.25）：$\mathcal V=\oplus_nH^*_{L^2\,\mathrm{harm}}(\mathcal M_n)$。
15. **式 (5.17)**（p.26）：$\otimes_{j=1}^kW_j=\oplus_nH^*_{L^2\,\mathrm{harm}}(\mathcal M_n)$；两侧分别按 $(L_0,\text{电核})$ 与 $(P,\text{磁荷})$ 分级。

## 三、与已译文献的接口

本篇的文献编号 [n] 是它自己的书目，与库内篇号无关；下表按内容对应。

| 库内篇 | 本篇引用 | 位置 | 内容 |
| --- | --- | --- | --- |
| 01 KW06 (hep-th/0604151) | [9] | p.4、p.5–6 | 第三种扭化 ↔ 几何 Langlands；Wilson/'t Hooft 算子与 Hecke 算子/特征层的词典；本篇 §5.5 的 BPS 分析与 KW06 的 brane 词典同源。 |
| 02 Gukov–Witten (hep-th/0612073) | [12] | p.6 | 二维（曲面）算子要成为电磁对偶不变的类，必须补量子参数，由此得到分歧的 QFT 框架。 |
| 06 0802.0999 | [10] | p.4 Remark 1.1 | 四维是几何 Langlands 自然起点的另一种解释：模栈上的二维 sigma 模型实为四维规范理论（Atiyah–Bott [11]）。 |
| 07 0902.0948 | [36] | p.22 §5.4.2 | $\Gamma_k$ 的基 $L_r$ 的显式构造（本篇只说 "described explicitly in [36]"）。 |
| 21 0804.2902 / 22 0807.3720 | [13, 14] | p.6 | 三维（余维 1）算子的丰富结构；$G\to H$ 跳跃与 functoriality 相关。 |
| 28 bdh 量子化 | [7] | p.3 | 几何 Langlands 基本断言 $\mathrm{Coh}(Y_{G^\vee})\simeq\mathrm{D\text{-}mod}(Z_G)$ 的出处（Beilinson–Drinfeld）。 |
| 11 1009.6032 / 16 0710.5939 / 23 1106.4789 / 36 hep-th/0512172 | 未引用 | — | 11、23 晚于本篇（2010、2011），16、36 主题相关但本篇未引；只能作概念对照，不能当作本篇的出处。 |

另：本篇 [24] = Braverman–Finkelberg 0711.2083（库内无卡，§5.5.4 的对应关系的数学来源）、[26] = Nakajima 0809.2605、[23] = Vafa–Witten、[39] = Vafa hep-th/9707131。

## 核对与勘误

### XREF 五项动作清单（逐条回填）

| # | 动作 | 核了什么 | 结论 |
| --- | --- | --- | --- |
| 1 | 主定理陈述与符号 | 摘要 + §1.2 + [7]/[9] 的复述 | 一致：四维第三种扭化下 $G\leftrightarrow G^\vee$ 且 $\tau\to-1/\tau$，范畴层面即几何 Langlands。nLab 与 KW06 的陈述同形，无出入。 |
| 2 | 关键公式系数/符号/指数 | (1.2)(3.4)(3.5)(4.1)(4.5)(4.12)(5.2)(5.4)(5.5)(5.12)(5.13)(5.16)(5.17) | 只有 (3.4) 的 $\theta$ 项缺 $i$ 是笔误（E1）；其余符号/系数与本篇内部及外部一致。(4.5) 与 (3.4) 的因子 2 属 $\mathrm{Tr}$ 归一化约定，不记勘误。 |
| 3 | 命题编号与交叉引用 | (5.2)→(5.4)→(5.5) 的引用链；§5.5 对 (4.12) 的回引 | 自洽；但 (5.4)(5.5) 在 p.17 而非 p.16（我最初记错，靠 grep 式号纠正），(5.3) 在 p.16。 |
| 4 | 数值/维数一致性 | $\dim R=(\#Z)^g$；(5.12) 两侧秩 $2gk$；$\Gamma_k$ 秩 $k$；$H^3(M_6)=H^2+H^3$ | 一致。$\mathrm{rank}(H^1(W)\otimes\Gamma_k)=2g\cdot k$，与 $H^3(W\times TN_k)$ 的 Künneth 秩相同（$H^3(TN_k)=0$）。 |
| 5 | 记号与前后定义 | $\tau$（六维环面模 vs 四维耦合）、$Z$（中心）、$\mathcal V$、$P/P'$、$U$ | $\tau$ 一词双关是本篇的关键（也是正确性所在）；$Z$ 始终指中心；$P$ 在两侧分别指瞬子数与 $L_0$，原文有明说，不算混淆。 |

### 外部来源

| 来源 | 定位 | 核了什么 | 结论 |
| --- | --- | --- | --- |
| KW06, hep-th/0604151（库内 `pdf/01`） | p.10–11 式 (2.11)(2.12)；p.48 式 (4.16) | $\theta$ 项的号差约定：洛伦兹 (2.11) 无 $i$，欧氏 (4.16) 明写 $i\theta/8\pi^2\int\mathrm{Tr}F\wedge F$；$\tau=\theta/2\pi+4\pi i/e^2$ | 支持 E1：本篇 (3.4) 在四维欧氏语境下缺 $i$。 |
| Gukov–Witten, hep-th/0612073（库内 `pdf/02`） | p.13；p.17 式 (2.26)；p.21 式 (2.38)(2.39) | $\theta$ 以 $e^{i\theta d}$ 进入路径积分；欧氏作用量 $I_\theta=-i\theta N$，$N=-\frac{1}{8\pi^2}\int\mathrm{Tr}F\wedge F$ | 支持 E1（第二处独立出处）。 |
| Witten, 0902.0948（库内 `pdf/07`） | p.6 式 (2.1)–(2.2) | Taub-NUT 度量形式与本篇 (5.7) 同形；其 $U=\frac{1}{|\vec X-\vec x|}+\frac{1}{\lambda^2}$ | 形式一致；系数 1 vs 本篇 $1/2$ 判为 $\theta$ 周期/荷归一约定，不记勘误。 |
| nLab: geometric Langlands correspondence | 词条正文（web） | 猜想陈述 $\mathcal OMod(Loc_{{}^L G}(\Sigma))\simeq\mathcal DMod(Bun_G(\Sigma))$；Hecke 变换 ↔ 't Hooft 算子、Hecke 特征层 ↔ magnetic eigenbrane | 与本篇 §1.2、§2 的陈述一致；译名 eigenbrane=特征膜、Hecke eigensheaf=Hecke 特征层得到确认。 |
| arXiv:0711.2083（Braverman–Finkelberg） | abs 页（web） | 用 $A_{k-1}$ 奇点上的 Uhlenbeck 瞬子空间构造仿射 Grassmannian 的切片奇点，猜想其相交上同调由对偶仿射 Kac–Moody 群的可积表示描述 | 与本篇 §5.5.4「level $r$ 可积模 ↔ $\varphi:\mathbb Z_r\to G$」的对应对应，支持 (5.17) 与 [24] 平行的说法。 |
| Witten, 0802.0999（库内 `pdf/06`） | p.5 | 「Wilson 与 't Hooft 线算子的基本事实给出 Hecke 特征层的陈述，详见 KW06 §9–10」 | 支持 't Hooft 算子卡的算子词典；并确认 KW06 的相关段落在其 p.40 以后（超出本包 30 页上限）。 |

### 勘误

**E1（high，fixed）**：p.8 式 (3.4) 的 $\theta$ 项缺因子 $i$。原文作
$$I=\frac{1}{4e^2}\int_{M_4}F\wedge\star F+\frac{\theta}{8\pi^2}\int F\wedge F,$$
欧氏号差下应为
$$I=\frac{1}{4e^2}\int_{M_4}F\wedge\star F+\frac{i\theta}{8\pi^2}\int F\wedge F.$$
判级理由：(i) 两处独立外部出处都带 $i$（KW06 式 (4.16) 欧氏、Gukov–Witten 式 (2.26)/(2.38)）；(ii) 本篇内部不自洽——p.4 说 $\tau\to\tau+1$（$\theta\to\theta+2\pi$）是半经典对称，理由是「瞬子数取整」，而没有 $i$ 时 $e^{-I}$ 在 $\theta\to\theta+2\pi$ 下改变 $e^{-\theta\,\mathrm{const}}$，不成立；(iii) 只有配上 $i$ 后 (3.5) 的 $\tau$ 才在 (4.12) 里给出正确的模变换。影响卡片：`ggl08/deriv/abelian-duality-from-selfdual-gerbe`（已按订正写并加 `corrections`）、`ggl08/concept/abelian-duality-from-six-dimensions`。

### 不计入勘误的约定差异（写在 notes，不进 errata.tsv）

1. **(4.5) 与 (3.4) 的因子 2**：$I_4=\frac{S}{8\pi R}\int\mathrm{Tr}F\wedge\star F$ 与 $\frac{1}{4e^2}\int F\wedge\star F$ 差因子 2，取决于非阿贝尔 $\mathrm{Tr}$ 的归一化（KW06 p.9 把 $\mathrm{Tr}$ 归一化为 $\frac{1}{8\pi^2}\int\mathrm{Tr}F\wedge F$ 取遍整数）。原文在 (4.1) 处未定义 $\mathrm{Tr}$，不构成自相矛盾。
2. **Taub-NUT 的 $1/2$**：本篇 (5.9)(5.11) 用 $U=\frac{1}{R^2}+\frac{1}{2|\vec x|}$，0902.0948 式 (2.2) 用系数 1。差异等价于 $\theta$ 的周期（$2\pi$ vs $4\pi$）与荷的归一，物理内容相同。
3. **$G^\vee=G_{\rm ad}$**：本篇 p.14 明说「单链且单连通」时成立；对 $E_8$ 则 $G=G^\vee$。这不是笔误而是条件。

## 五、不懂

1. **$\tilde H^3$ 的确切定义**（p.22）：原文只说它是 $H^3$ 的「appropriate substitute」，用 $\Gamma_k$ 替换 $H^2(TN_k)$。我不知道这里该用相对上同调 $H^3(M,\text{无穷远})$、还是紧支撑上同调、还是某种 $L^2$ 上同调；(5.13) 的分解我按 Künneth 能验算秩，但验不了「无穷远平凡化」这一条。
2. **$\Gamma_k$ 的二次型为什么是 $\sum y_i^2$**（p.22）：原文说 "It turns out that"。我知道 $TN_k$ 的 $L^2$ 反自对偶线丛与 $A_{k-1}$ 的根格有关，但为什么取 $U(k)$ 权格而不是根格配对，我没算出来。
3. **§5.2.2 的 M-理论论证**（p.18）：$Q_7\times TN$ 上的 M-理论 ↔ $Q_7\times\mathbb R^3$ 上的 IIA 加 D6，我接受这个对偶，但没有核 D4–D6 相交给出 level 1 current algebra 的系数。
4. **为什么 $Sp(4)$ 在 $\mathcal V$ 上平凡作用**（p.25）：原文说「很可能」，等价于 $L^2$ 调和形式只在中间维且对每个复结构是 $(p,p)$ 型。这是 Hitchin 的 $L^2$ 上同调结果 [38]，我没读原文。
5. **(5.17) 的严格性**：两侧用的上同调不同（$L^2$ 调和形式 vs 数学文献的相交上同调），原文 p.27 承认这一点。等式究竟是定理、猜想还是「物理上必须相等」，我判断不了。
6. **一般环面（非矩形）的 (5.2) 分析**：脚注 6 说可以用 (5.2) 处理一般环面，但 (5.2) 需要圆丛结构，一般 $T^2$ 上的 $\tau$ 与 $f$ 的关系我没推。

## 六、术语撞名处理（term_index）

`tools/term_index.py check out/08_ggl08/cards` 初跑报 2 处撞名、改别名后又各引出 2 处，逐条判断如下（原则：译名以旧卡为准，同概念不重复造卡，只改我这边的别名）：

| 我的卡 | 撞名项 | 撞到的旧卡 | 判断 |
|---|---|---|---|
| `ggl08/concept/defects-of-various-dimension` | surface operator / codimension-two defect | `gw06/concept/sigma-model-ramified`、`gw06/concept/surface-operator` | 我这张卡讲的是 $p$-流形算子的整条维度层级，不是曲面算子本身；旧卡已占「surface operator = 曲面算子/余维二缺陷」这两个英文别名，故删去它们，只保留中文「余维二缺陷」（归一化后不撞）与「p-流形算子」 |
| `ggl08/concept/thooft-operator-to-hecke-operator` | 't Hooft operator / disorder operator / Hecke 算子 / Hecke 对应 | `gtgl15/concept/thooft-operator`、`kw06/concept/thooft-operator`、`bdh/concept/hecke-stack-and-functor`、`glc/concept/global-hecke-stack` | 't Hooft 算子与 Hecke 算子的**定义**分别由 gtgl15/kw06 与 bdh 的卡承担；我这边的卡只负责「两者相等」这条词典，故别名改成 `'t Hooft–Hecke 词典`、`geometric Hecke operator`、`算子–层对应`、`算子词典（'t Hooft 与 Hecke）`；标题保留「't Hooft 算子与几何 Hecke 算子」因为它描述的是对应关系 |

结果：`[done] 检查 14 张卡，与既有语料撞名 0 处`。terms.tsv 里的中译仍按旧卡：`'t Hooft 算子`（kw06 用「算子」，gtgl15 用「算符」，以 kw06 为准）、`surface operator` 记为「曲面算子（余维二缺陷）」。
