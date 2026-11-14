# 学术审校报告（REVIEW NOTES）

项目：Niklas Garner & Natalie M. Paquette,
*TASI Lectures on the Mathematics of String Dualities*（TASI 2021 讲座），
arXiv:2204.01914v2 [hep-th]，PoS 会议文集，原文 85 页。
中译本：`asi2204-zh/`，正文 21 个分片，可编译 PDF 66 页。

---

## 0. 首先要说清楚的一件事：作者不是 Witten

所给 PDF 的标题页、页眉与版权页均写明作者为 **Niklas Garner** 与
**Natalie M. Paquette**（University of Washington），文章是 TASI 2021 的会议讲义，
由第二作者在 2021 年 6 月 7 日–7 月 2 日（University of Colorado, Boulder）讲授，
2022 年 4 月 12 日提交 arXiv。它不是 Edward Witten 的论文。
Witten 的工作在文中作为文献被大量引用（如 [17] Donaldson–Witten 扭变、
[47] Morse 理论、[96] Jones 多项式等），但本文本身是综述性讲义。
译本一律以实际作者为准，未在任何位置冒称 Witten。

如果任务是「翻译 Witten 的文章」，那么这份 PDF 不是目标文件；本译本仍按原 PDF
完整翻译，并在 `main.tex` 的译者说明中如实声明。

---

## 1. 全文内容与学术定位

这是一篇**教学性综述**，而不是包含新定理的研究论文。它由 TASI 2021 系列讲座的
最后两讲整理而来，主题是：**扭变（twisting）、镜像对称、下降（descent）与高阶代数**，
并把它们串成一条主线：

> 对偶是精确等价 → 超对称的受保护量可以用扭变分离出来 → 扭变后的理论由某个
> 幂零超荷 $Q$ 的上同调刻画 → 上同调（链层面）上的代数结构由 $A_\infty/L_\infty$
> 等高阶代数描述 → 在二维情形这些结构分别实现为手征环、量子上同调、
> Hochschild 上同调与（同伦）顶点代数。

各章内容与本报告的技术评述如下。

### §1 引言

作者把对偶类比为「傅里叶变换」：弱–强对偶交换 $g\leftrightarrow 1/g$，
等价于交换量子涨落的强与弱；数学上对应 Fourier–Mukai 变换、Koszul 对偶等。
镜像对称被定位为**微扰对偶**（不是弦耦合 $g_s$ 的强–弱对偶，而是在
$\alpha'/R^2$ 意义上的 T 对偶型对偶）。这一节的定位是准确且克制的，
没有把镜像对称混同为非微扰对偶。

### §2 扭变与镜像对称（全篇主体，原文 30 页）

**(a) 扭变的现代语言（2.1）。** 取平方为零的超荷 $Q$，只保留 $Q$-闭算子并对
$Q$-恰当算子作等价，即取 $Q$-上同调；若把 $Q$ 并进 BRST 微分 $d_Q=d+Q$，
则得到扭变理论的算子代数。这里有一个易被略过的前提：$d_Q^2=\{d,Q\}$，
只有在 $d$ 与 $Q$ 反对易时 $d_Q$ 才幂零（译本已在此加注）。
「幂零簇」（nilpotence variety）是本节最有价值的组织性概念：所有平方为零的超荷
构成一个代数簇，2d $\mathcal{N}=(2,2)$ 情形为四个两两相切的 $\mathbb{P}^1$；
秩 1 分支给出全纯（半）扭变，秩 2 分支给出拓扑的 $A/B$ 扭变。
把「有哪些 twist」转化为「幂零簇的分层」，是近年数学物理中非常有效的视角。

**(b) 从世界面看镜像对称（2.2）。** 镜像对称被实现为 2d $\mathcal{N}=(2,2)$
超代数的外自同构：交换左移超荷 $Q_-\leftrightarrow\bar Q_-$（相应地
$R_A\leftrightarrow R_V$、复质量 $Z\leftrightarrow\tilde Z$），
从而交换手征多重态与扭手征多重态、$A$ 模型与 $B$ 模型。
Landau–Ginzburg 模型作为「手征超场 + 全纯超势」的显式例子给出，
并说明超势的 $R$ 荷必须为 2。

**(c) 扭变世界面与两个环（2.3）。** 这是全篇技术核心之一：
$B$ 扭变的手征环同构于 Dolbeault 上同调
$H^{0,\bullet}(X,\wedge^\bullet T^{1,0}X)$（多重矢量场），初级乘积即楔积；
$A$ 扭变的扭手征环同构于量子上同调，乘积含世界面瞬子修正。
两个 Table 把 $B/A$ 扭变下各分量的自旋、$R$ 荷与分次逐项列出，
是读者实际动手时最常查的表（译本已逐格核对）。

**(d) 同调镜像对称（2.4）。** $B$ 膜 ↔ 凝聚层的导出范畴
$D^b\mathrm{Coh}(X)$，$A$ 膜 ↔（包裹）Fukaya 范畴；$\mathrm{Hom}$ 对应
$\mathrm{Ext}$ 与 Floer 上同调，复合对应开弦粘合，高阶乘积 $\mu_n$ 对应
全纯圆盘计数。Kontsevich 的同调镜像对称猜想在此被表述为范畴等价。
这一节的物理图像清楚，但数学陈述是「猜想/预期」层面的，译文保留了原文的
推测语气（「据信」「预期」），没有拔高为定理。

### §3 同伦与若干后续发展（原文 28 页）

**(a) 拓扑下降与次级乘积（3.1）。** 下降给出后代 $O^{(k)}$ 与
$QO^{(k)}=dO^{(k-1)}$；在 $k$-链上积分得到延展算子。
次级乘积（secondary product）由「把一个后代沿环绕另一个算子的球面积分」定义，
在 $d\ge2$ 时是分次反对称括号，在 $d=1$ 时给出通常对易子。
$B$ 模型里它实现为多重矢量场的 Schouten–Nijenhuis 括号（Gerstenhaber 括号）。
**这是全篇推导最容易出符号错误的地方**：$Q$ 穿过积分映射产生的 $(-1)^n$、
Stokes 定理给出的边界项、以及 Koszul 符号约定，三者叠加。
译本已在 (3.11)、(3.13)–(3.16) 等处以 Tutor Note 逐项标注。

**(b) $A_\infty$ 代数与 Hochschild 上同调（3.2）。** 从拓扑量子力学的
碰撞（collision）出发，把局域算子的 $n$ 元运算 $\mu_n$ 组织成 $A_\infty$ 关系；
重点在于「链层面」而非上同调层面：$H^\bullet(A)$ 上的高阶运算
（$A_\infty$–Massey 积）是链层面运算的提升。作者随后论证
**体局域算子代数 ≅ 边界条件范畴的 Hochschild 上同调**，
并用自由手征多重态与 Landau–Ginzburg 模型作显式计算。
这里有一个技术要点值得读者注意：与拓扑引力耦合时严格相关的是**循环**上同调，
而非普通 Hochschild 上同调（原文脚注 23 已作说明，译本保留）。
原文 (3.55) 的归一化与「直接计算」相差一个因子 2，译本按原文照录并加注，
读者自行核对时以 Hochschild 微分的归一化为准。

**(c) 全纯扭变与顶点代数（3.3）。** 本讲义最新颖也最前沿的部分：
全纯扭变只要求一个标量超荷平方为零（不要求把自旋群完全拓扑化），
所得理论在二维是全纯理论、在三维是「全纯–拓扑混合」理论；
其局域算子的 $Q$-上同调带有 $L_\infty$ 共形代数 / Poisson 顶点代数结构，
并期望提升为同伦顶点代数。这里的许多陈述是「应当」「预期」，
属于当前研究前沿；译文保留不确定语气，未擅自补全证明。

### 附录 A–C

- **附录 A**：等变上同调的 Cartan 模型（$d_\sigma=d_M+\sigma\iota_V$）、
  Atiyah–Bott/Duistermaat–Heckman 型局域化，以及超对称路径积分的局域化
  （BPS 轨迹 + 单圈行列式）。这是理解正文「受保护量可精确计算」的技术基础。
- **附录 B**：$A$ 型量子力学与 Morse 理论。$Q^2=2H$ 的超对称量子力学中，
  基态 = $\bar Q$-上同调类；Morse 函数临界点、梯度流与
  Morse–Smale–Witten 复形给出基态计数。这是 Witten 1982 年文章的现代讲义版。
- **附录 C**：Landau–Ginzburg $B$ 模型与矩阵分解。$B$ 膜由矩阵分解
  $(E,J)$（$EJ=W\cdot\mathrm{id}$、$JE=W\cdot\mathrm{id}$）描述，
  超势 $W$ 的因子化为边界条件提供代数数据；这是 Orlov 型矩阵分解范畴的物理实现。

---

## 2. 翻译与审校方法

1. **以页面图像为准。** 所有公式、上下标、花体、正负号均对照 `pages/page-NN.png`
   与 500–1600 dpi 局部放大图逐符号核对；文字层（`text/`）只用于定位与英文措辞，
   不用于公式。
2. **编号锁定。** 全文 182 个带号公式全部用 `\tag{}` 锁定为原文编号：
   (2.1)–(2.54)、(3.1)–(3.76)、(A.1)–(A.9)、(B.1)–(B.27)、(C.1)–(C.16)，
   由 `tools/verify.py` 逐项校验「182/182，无缺号、无重号」。
3. **图表剥离。** 原文 14 幅矢量插图（Figure 1–14）按矢量边界 + 图注定位逐幅裁切，
   以 300 dpi 渲染保存为 `figures/fig01–14.png`，并在正文对应段落以 `figure` 环境插入；
   图注逐条译为中文并标注「（原文第 N 页，Figure K）」。
   2 张表（Table 1/2，第 19、21 页）用 `booktabs` 忠实重建，数值逐格核对。
   另有 5 处「公式内的矢量示意图」（第 42 页两处树图、第 43 页、第 44 页、
   第 69 页 (B.18) 阶梯图），按原图矢量裁切嵌入，避免用 TikZ 重画引入失真。
4. **脚注。** 原文 63 条脚注全部译为 `\footnote{}`；编号由 LaTeX 重排，
   与原编号整体偏移属正常现象。
5. **批注。** 全书共 **161 条 Tutor Note、24 条原文疑误、24 条存疑、19 条背景补充**，
   均为源码中的 `%` 注释，不影响排版输出，可在 `.tex` 中直接阅读；
   全部批注的分类索引见 `notes/annotations-index.md`。
6. **连续性。** 21 个分片按原文页序拼接，20 处页界/分片边界逐句核对，
   无重复句、无漏句；跨页断句处均有 `% [跨页接续]` 注释。

---

## 3. 原文疑误与存疑（摘录）

以下为正文中已加注的主要问题。均**照原文排版**，仅在注释中给出判断依据；
读者若要引用，请回到原文核对。

### 3.1 明确的拼写/语法笔误

| 原文位置 | 原文 | 应为 |
|---|---|---|
| p4 | "can be though of as" | "can be thought of as" |
| p5 | "a topological supercharges" | 冠词/单复数不一致 |
| p29 | "Our hope here it to provide" | "is to provide" |
| p30 | "the Morse index $\mu(p)$ equal to" | 缺 is |
| p32 | "of the the intersection point" | 重复 the |
| p35 | "one can can integrate" | 重复 can |
| p37 脚注 34 | "leads to a mixed holomorphic-topological," | 缺中心名词 twist |
| p38 脚注 | "is a simply pair of points" | "is simply a pair of points" |
| p43 正文与 Figure 9 图注 | "Sashtev polytope" | "Stasheff polytope"（原文两处均拼错） |
| p56 | "are holomorphically twisted of 2d … theories" | 缺 versions of |
| p59 | "is naturally have this structure" | "naturally has" |
| p66 | "as discussed in at the beginning of Section 2.1" | 多一个 in |

### 3.2 符号/指标/数值上可疑之处（均照录）

- **p32 (2.52) 之前**：正文说 $|q_{23}\rangle$，但同段交点写作
  $q_{13}\in\mathcal{L}_1\cap\mathcal{L}_3$，式 (2.52) 也对 $q_{13}$ 求和，
  Figure 7 图注为 $|q_{13}\rangle$；疑应为 $q_{13}$。
- **p46 (3.29)**：$\psi_3$ 括号内印作 $\phi^2\partial_{\bar\gamma_3}+\phi^3\partial_{\bar\gamma_2}$
  （与 $\psi_1$ 相同），按 $S_3$ 对称性应为 $\phi^1\partial_{\bar\gamma_2}+\phi^2\partial_{\bar\gamma_1}$；
  且与 (3.30) 的 $\{\psi_1,\psi_3\}=-\frac23\phi^2$ 相差因子 2。
- **p48 (3.36)**：第二项印作 $\phi(Q_\partial Q_1,\dots,O_n)$，疑应为
  $\phi(Q_\partial O_1,\dots,O_n)$，且行末多一个右括号。
- **p51 vs p50/Figure 13**：构型空间一处作 $C_{\mathbb{H}}(1;n)$、一处作
  $C_{\mathbb{H}^2}(1;3)$（原文自身不一致，译本照录并加注）。
- **p52**：导子条件印作 $f(ab)=f(a)b\pm af(b)$，一般应为含分次符号的 Leibniz 法则。
- **p53/54**：$N=4$ 用普通斜体，与全文 $\mathcal{N}$ 的写法不一致。
- **p56 (3.61) 下方**：$d z^{\bar a}\partial_{\bar a}$ 漏掉 $\bar z$ 的横线，
  按 Dolbeault 微分应为 $d\bar z^{\bar a}\partial_{\bar a}$。
- **p69**：Betti 数写作 $b_p(M)=\dim H^p(\Omega^p(M),d)$，按上下文应为 $\Omega^\bullet(M)$。
- **p72 (C.7)**：$\bar Q=\bar\psi_n\bar\partial^a+\cdots$ 的上标 $a$ 疑应为 $n$。
- **p74 (C.8)**：$\{\bar D,D'\}\Phi^a$ 的 $a$ 疑应为 $n$。
- **p74 附近**："其平方等于 $2W$ 乘单位矩阵"与同页前句「平方是 $W(\phi|)$」
  及 (C.15) 矛盾（$2W$ 疑应为 $W$）。
- **p77 [127]**：原文 PDF 本身把 $\mathbb{A}^2$ 印成了 HTML 源码字面
  `<strong>A</strong> <sup>2</sup>`（源文件标记泄漏），译本按原貌保留并加注。

### 3.3 译者层面的订正（仅此一处，已注明）

- 初稿曾把 (3.28) 的生成元按文字层误录为 $\gamma_n$；终校据页面图订正为
  $\bar\gamma_n$（与 (3.29) 一致），并在源码中加 `% [校订: ...]`。
  这是**翻译过程**的订正，不是原文笔误。

---

## 4. 编译与完整性

- 编译：XeLaTeX（`tectonic -X compile main.tex`），ctex + fandol 字体；
  **0 error、0 overfull hbox**，正文 66 页（含目录）。
- 完整性校验（`tools/verify.py`）：
  - 分片：21/21；
  - 带号公式：182/182，无缺号、无重号；
  - 页码锚点：原文第 1–85 页全部覆盖（第 3、22、66 页因跨页/分片重叠各出现两次，
    属有意设计，均有注释）；
  - 插图：14 幅 + 5 个内嵌图全部被引用且文件存在；
  - 批注：161 + 24 + 24 + 19 条。
- 参考文献：[1]–[151] 连续无缺号，保留英文原貌；每条按原文编号字面排版，
  不使用 BibTeX 重编号。

---

## 5. 使用建议

1. **作为讲义读**：第 2 章可作为「扭变 → 镜像对称 → 两个环」的入门；
   第 3 章适合已熟悉 $A_\infty$ 代数的读者；附录 A/B/C 是三个独立的技术补充，
   建议按需查阅。
2. **作为研究地图读**：文中的「应当/预期/据信」是作者对前沿的诚实标注，
   不宜当作定理引用；需要严格陈述时应追溯所引文献（参考文献 [1]–[151]）。
3. **作为翻译对照读**：源码中每页都有页码锚点，`% [Tutor Note]` 与
   `% [原文疑误]` 注释直接给出该处的技术要点与疑点，适合与原文并排阅读。
4. **若要用源码继续写作**：导言区在 `main.tex`，正文分片在 `sections/`，
   每个分片自足、可单独抽取；公式编号用 `\tag`，不依赖全局计数器，
   增删内容不会破坏编号。
