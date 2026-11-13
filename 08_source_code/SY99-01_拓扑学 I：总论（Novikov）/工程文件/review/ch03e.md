# 核验报告 · ch03e（原书 p.70–p.78）

- 核验人：译者甲（tr-jia）
- 作者：译者乙（tr-yi）
- 核验日期：2026-11-09
- 核验方式：逐页读 pages\p077.png–p085.png（原书 p.70–p.78），另读 p086.png 顶端一行以确认跨页句的后半，与 src\chunks\ch03e.tex（313 行）逐段、逐式对照；编号 (4.6)(5.1)–(5.22) 逐个核对；英译中逐句比对，跨页句归属与页标记位置按 STYLE_GUIDE（含 lead 的页标记规则）复核。

## 结论

需修改（1 条必须改：一处残句；数学内容、编号、体例全部正确，本块是乙四块中质量最高的一块）。

## 必须改（影响正确性）

1. **第 268 行句末残句：「……所诱导，该（即对应的轨道中各链的）有限和。」**
   - 原书 p.77 末—p.78 首："…the homomorphism $\mu_j$ is then induced by that associating each $c_G\in C_j(K/G)$ with $\sum_{g\in G}g(c)\in C_j(K)$, the (finite) sum of the chains in the corresponding orbit."
   - 现译把英文同位语 "the (finite) sum…" 用逗号硬接在「所诱导」后面，排成「该（即对应的轨道中各链的）有限和。」——这是一个没有谓语的名词短语，句子断了，读者读到这里会停顿。
   - 建议改为：「……对应到 $\sum_{g\in G}g(c)\in C_j(K)$ 所诱导；这里出现的和，是相应轨道中各链的（有限）和。」即把逗号改分号并补出「这里出现的和，是……」。→ src\chunks\ch03e.tex 第 268 行。

## 建议改（可读性/文风）

1. **第 6 行 Tutor Note 位置**：按 STYLE_GUIDE「批注写在需提醒段落之后」，这条讲原书 p.70 例 2 的 $\cF_3=\cF_1/\cF_2$ 笔误的注释应放在第 8 行（含该式的那段）之后，而不是 `\begin{example}{2}` 之前。**注释内容本身我已逐字核实正确**（lead 也确认过：这是原书笔误，照排 + 注的处理正确，不要改成「正确」的式子，只需挪位置）。
2. **第 311 行 Tutor Note 离被注段落太远**：它讲的是转移同态 $\mu_*$ 与 (5.18)–(5.20)，却排在整块最末（(5.22) 与 Smith 定理之后）。建议移到第 285 行（(5.20) 与「其中上标 $G$……」那句）之后。
3. **第 91 行**「特别令人感兴趣的是那些表示 $\rho\colon\pi\to\operatorname{Aut}V$，其相应的同调群 $H_q(K;\rho)$ 都平凡；」——逗号后接「其相应的」略松，可改「……的表示 $\rho\colon\pi\to\operatorname{Aut}V$，其相应的同调群 $H_q(K;\rho)$ 都平凡；」或「凡使相应的同调群 $H_q(K;\rho)$ 都平凡的表示」。两种都可，现文不算错。
4. **第 34 行页标记 `% [原文 p.71]`**：现落在 (5.1) 之后、「其成立条件为……」之前。严格说 (5.1) 显示式已属 p.71（原书 p.71 第一行就是该式），而按 lead 的「环境前后也算边界」这条，现在的位置是可接受的；若按「句界优先」，可把标记移到第 35 行之后。请 lead 定夺，不必单独返工。

## 抽查记录（逐页一句）

- **p.70**（PDF 77）：块首承接 ch03d 的例 1 末句（"(4.5) reduces to…" 起于 p.69）已由 ch03d 写完，本块不重复 ✓；§4 例 2（$\cF_1\subset\cF_2$ 常层、$\cF_3=\cF_1/\cF_2$ 照排 + 注 ✓）、(4.6) Bockstein 同态、其直接定义 $z=\tilde z\bmod p$、$\partial^*z=0,\partial^*\tilde z=pu,\partial^*u=0$、$\frac1p\partial^*\tilde z=\beta(z)$、□；Remark（非阿贝尔群层、$H^0$ 有群结构、$H^1$ 仅是集合、主 $G$-丛、截面群），全部一致。
- **p.71**（PDF 78）：(5.1) $H_n(K,L;\Z)\cong\pi_n(K,L)\otimes_{\Z[\pi]}\Z$ 及成立条件；张量积 (5.2) 与 $R=\Z$ 的退化；万有覆叠复形 $C_*(\tilde K)$ 为自由 $\Z[\pi]$-模、$p:\tilde K\to K$、$p^{-1}(\sigma^n_\alpha)=\bigcup_{\gamma\in\pi}\sigma^n_{\alpha\gamma}$、初始单形 $\sigma^n_{\alpha1}$ 与 $\gamma(\sigma^n_{\alpha1})=\sigma^n_{\alpha\gamma}$、$\partial$ 与 $\Z[\pi]$-作用交换、正规覆叠时 $\Gamma=\pi_1(K)/N$ 的 $\Gamma$-作用，全部一致。
- **p.72**（PDF 79）：表示 $\rho$ 与 $(V,\rho)$、(5.3) $C_*(K;\rho)=C_*(\tilde K)\otimes_{\Z[\Gamma]}(V,\rho)$、按商模构造同调/上同调；例 1（平凡表示 → $H_q(K;V)$，□）、例 2（不可定向流形、$\rho[\gamma]=\sgn\gamma$、$V=\Z$、Poincaré 对偶 (5.4) 两行，□）、例 3（$V=\Z[\pi]$ 右乘 → $H_j(K;\rho)\cong H_j(\tilde K;\Z)$，□）；$\rho$-零调定义与正合列 (5.5)；「特异基」段；Remark 开头（基变换的自由度），全部一致。
- **p.73**（PDF 80）：Remark 的 1) 定向改变 $\sigma^n_\alpha\mapsto-\sigma^n_\alpha$、2) 另选初始胞腔引起的 $\sigma^n_\alpha\mapsto\pm\gamma\sigma^n_\alpha$ 或 $\pm\rho(\gamma)\sigma^n_\alpha$、固定特异基的假设与 □；$V$ 为有限维向量空间、$\rho$-零调、两项正合列时 $\partial$ 为同构、$\det\partial=\det C_*(K;\rho)$；三项正合列时「行列式」的定义（$c_n,c_{n-1},c_{n-2}$、中间复形另取基 $(\partial c_n,\partial^{-1}(c_{n-2}))$、「三角形」性质）；一般情形的 $A_j$、$a_j$、$A_0=0,A_n=C_n,a_n=c_n$ 及五个阶梯式显示式，全部一致。
- **p.74**（PDF 81）：$\det C_*(K;\rho)$ 的分式定义（分子 $c_{n-1},c_{n-3},\dots$、分母 $c_{n-2},c_{n-4},\dots$，我逐项与页图比对，(5) 处符号无差）；Definition 5.1 用 `definition*{5.1}` 正确（原书无 □）；1930 年代末 Reidemeister–de Rham–Franz 的组合不变性、1970 年代拓扑不变性、括号内变动的来源；$R(K\times L,\rho)=R(K,\rho)\chi(L)$；透镜空间 $A$ 的定义 (5.6)、$S^{2n-1}$ 上的作用 (5.7)、$L^{2n-1}_{(q_1,\dots,q_n)}$ (5.8)、可设 $q_1=1$、$n=2$ 时的 $L^3_q$ 与同伦等价判据 (5.9)，全部一致。
- **p.75**（PDF 82）：Bockstein 同态给出的同余式 $(a\beta(a),\pm[L^3_q])\equiv\pm q\ \mathrm{mod}\ m$ 与「$a\mapsto\lambda a$ 则 $q\mapsto\lambda^2q$」；CW 分解与 (5.10) $\partial\sigma^{2j-1}=0,\ \partial\sigma^{2j}=m\sigma^{2j-1}$；$S^{2n-1}$ 上诱导覆叠胞腔分解 (5.11)；$s=0,1,2,3$ 的边缘算子 (5.12)（$\partial\sigma^3=(1-A^q)\sigma^2$、$\sigma^3_1=\sigma^3$、$\partial\sigma^2=(1+A+\cdots+A^{m-1})\sigma^1$、$\partial\sigma^1=(1-A)\sigma^0$）；表示 $\rho:\Z\to(\ee^{2\pi\ii/m})$ 下 $L^3_q$ 为 $\rho$-零调、(5.13) 与 (5.14) $R(L^3_q,\rho)=(1-\zeta^q)(1-\zeta)\ \mathrm{mod}\ (\pm\zeta^\alpha)$，全部一致。
- **p.76**（PDF 83）：$\zeta=\ee^{2\pi\ii/m}$、由 (5.14) 得同伦等价而不组合等价的透镜空间、Moise–Chapman–Edwards 的同胚反例、de Rham–Franz 的 $n>2$ 结论；Whitehead 的问题陈述；$L\subset K$、相对链复形 $C(K,L)$ 零调；初等运算 (i)（(5.15) $\sigma^k_j\mapsto\gamma\sigma^k_j+\sigma^k_j$）与 (ii) 稳定化（(5.16)(5.17)）；等价类构成 $K_1(R)$、行列式群、无穷矩阵群与换位子/初等矩阵取商，全部一致。
- **p.77**（PDF 84）：p.76 末句"To obtain $K_1(R)$ one factors this"的续文（正规子群、行列式公理化）✓；$\Wh(\pi)=K_1(\Z[\pi])/(\pm\pi)$（Whitehead 群）、$C(\tilde K,\tilde L)$ 的行列式、简单同伦型、$\rho:\pi\to\operatorname{GL}(n,\R)$ 给出 $K_1(\Z[\pi])\to\R^*$、单连通时 $K_1(\Z)=0$；Smith–Richardson 段、$G$ 作用保胞腔、$K^G$ 与 $K/G$、$i_*,\pi_*$；转移同态 $\mu_*$ 的定义（轨道链条数），全部一致（仅末句残句见上）。
- **p.78**（PDF 85）：(5.18) $\pi_*\mu_*$ 为乘以 $|G|$、(5.19) $\mu_*\pi_*$ 由 $\sum_{g\in G}g$ 决定、(5.20) 两条分解（特征为零或特征与 $|G|$ 互素）；$\rho C(K)$ 与 $H^\rho_*(K)$、$G=\Z/p,k=\Z/p$ 时 $H^\rho_*(K;\Z/p)$ 的理解方式；(5.21) $\sigma=1+T+\cdots+T^{p-1}$、$\tau=1-T$、$\sigma\tau=\tau\sigma=0$；Smith 正合列 (5.22) 与紧随的无编号 $\tau$ 版；「类似的上同调正合列」；末句（$\Z/p$ 作用在 $\Z/p$-同调 $n$-球面上，不动点集为某维数 $r$ 的 $\Z/p$-同调球面）为**跨页句**（起于 p.78 末、p.79 首 "likewise a $\Z/p$-homology sphere of some dimension $r$"），我读了 p086.png 顶端确认：乙把它整句写在 ch03e 内，与规则①一致，译法无误。

**总评**：ch03e 的数学内容零差错——23 个编号式（(4.6) 与 (5.1)–(5.22)）逐个与页图比对，无缺号、无错号、无符号错误；三个例子、两个 Remark、Definition 5.1 的星号体例全部正确；跨页句（p.77→78 的 μ_j 定义句、p.78→79 的不动点集句）归属都判对。唯一实质缺陷是第 268 行那个残句。

**跨块提醒（给 lead / tr-bing，不在本报告范围内）**：ch03f 应从 p.79 的 "Moreover if $p>2$, then $n-r$ is even." 起译——本块已把 p.78 末句整句写完，注意别重复；此外 src\figures\fig3_8.png 在 ch03e 里未被引用（本块 p.70–78 无插图），若它属于 ch03f 的图则请 tr-bing 核对编号与题注。
