# 核验报告 · ch04c（原书 p.165–175）

核验人：译者己　　作者：译者戊　　日期：2026-11-09

## 结论
通过（无影响正确性的错误；4 条建议改，其中第 1 条是跨页句归属的体例项，可与 lead 商量后再定）

## 必须改（影响正确性）
无。

## 建议改（可读性/版式/体例）
1. **p.175 末到 p.176 首的跨页句**（第 304 行末「可定向（即」）。原句自 p.175 起、到 p.176 的「…结构群约化到群 $SO_{\lambda_\alpha}$），则有不等式 (2.13)」才结束，现由 ch04d 第 2 行接完。按 STYLE_GUIDE 跨页句归起始页块的规则，严格说应把这半句收进本块。但这样会连带把 (2.13) 的 display 也拉进本块、且要同步改 ch04d 与 p.176 页标记的位置，收益不大。**建议维持现状，由 lead 裁定**；若裁定必须搬，注意两文件要一起改。
2. **图 4.14 内嵌英文未译**（第 294–298 行）。原书 p.175 的图里印着 `Line of degenerate singularities` 与 `f`，裁出的 fig4_14.png 原样保留了这段英文，图题却是空的。建议把图题补成 `\figtitle{4.14}{$f$ 的退化奇点线（原图内标签）}`，或重裁时避开该标签、在图注里说明。
3. **p.169「（均始于 20 世纪 50 年代初）」**（第 135 行）。原书 `(dating from the early 1950s)` 紧跟 Wu 的显式公式，只修饰它；译作「均」把 Thom 定理也纳入了（史实上 Thomas 的模 2 结论也是 50 年代初，但原书没这么说）。建议改为「（后者始于 20 世纪 50 年代初）」。
4. **§2 标题过长**（第 26 行，5 个分句共 40 余字）。运行页眉会挤。建议与 ch03f/h/i/j 的做法一致，加短标题：`\section[光滑流形的同调论. 复流形]{…全标题…}`。

## 抽查记录（逐页）
- **p.165**（`pages\p172.png`）：开头承接 ch04b 末段（复流形的定义、维数 $2n$），起点正确；紧复流形的两个基本例子 $\CP^n$、$T^{2n}=\C^n/\Gamma$；射影代数簇；Hermitian 度量 $ds^2=g_{ij}dz^i_\alpha d\bar z^j_\alpha$、$g_{ij}=\bar g_{ji}$；相配 2-形式 $\Omega=\frac{\ii}{2}g_{ij}dz\wedge d\bar z$；$d\Omega=0$ 与 Kähler 流形；Hodge 流形（$\Omega$ 表示整上同调类）、Siegel 与 Kodaira 的定理、复环面成为射影代数簇的 Riemann 条件；$\C^n$ 中无边界、维数 $>0$ 的复子流形非紧——逐句一致。§2 长标题四句齐全。
- **p.166**（`p173.png`）：图 4.6；光滑三角剖分 $M^n=\bigcup f_{k,\alpha}(\sigma^k)$ 与「PL 流形」的条件（组合等价于 $\sigma^n$）；Cairns–Whitehead 唯一性；单纯同调机器经三角剖分搬到光滑流形；一般位置下 $W^k\cap V^j$ 的相交；$k+j<n$ 时为空的说明；(2.1) $W^k\circ V^j\equiv m\ (\mathrm{mod}\ 2)$——一致。
- **p.167**（`p174.png`）：(2.2) 两个式子（定向符号与 $V^j\circ W^k=(-1)^{kj}(W^k\circ V^j)$，标签挂第二行，符合「一编号跨行贴末行」）；(2.3) 对偶基 $z_j^{\alpha_j}\circ\tilde z_{n-j}^{\alpha_{n-j}}=\delta$、$z_0=\tilde z_0=1$、$z_n=\tilde z_n=[M^n]$；$n=2m$ 时 $H^m$ 的对偶基；不可定向情形的模 2 版本；Example（Δ 与 Δ_f）——一致。
- **p.168**（`p175.png`）：非退化条件 $\det(\delta_{pq}-\partial f^p/\partial x^q)\ne0$；(2.4)、(2.5) Lefschetz 公式；零同伦推出 $\Delta\circ\Delta_f=1$、Brouwer 定理；图 4.8 与图题；$k+j>n$ 时 (2.6) $V^j\circ W^k=N^{j+k-n}$；闭链未必能由闭流形像代表——一致。原书 Example 末有 □，本块用无星 `example` 正确。
- **p.169**（`p176.png`）：Steenrod 问题与 Thom 的模 2 肯定解；$w_1$、$Dw_1\in H_{n-1}(M^n;\Z/2)$、Bockstein $\beta_*$ 与 (2.7)；第 3 章 §4 的 Bockstein 定义（$\beta_*(\tilde z)=\partial z/2$）；$w_1$ 的同伦不变性、Thom 与 Wu；不可定向流形的定向满射 $\sigma:\pi_1\to\Z/2$、Möbius 带、局部系数同调 $H_i(M^n;\sigma)$ 与 $H^{n-j}$ 的对偶；Morse 函数的两个条件——一致。**Möbius 带例句原书引「图 4.6」有误，译文照排并在 Tutor Note 说明，处理正确。**
- **p.170**（`p177.png`）：$\det(\partial^2f/\partial x^i_\alpha\partial x^k_\alpha)\ne0$；Morse 函数、图 4.9、Morse 指标；$M^n_{c\pm\eps}$ 与边界 $N^{n-1}_{c\pm\eps}$；把手 $H^n_\lambda=D^{n-\lambda}\times D^\lambda$、$\partial H^n_\lambda$；用微分同胚 $\psi$ 等同 $D^{n-\lambda}\times S^{\lambda-1}$ 与小管状邻域——一致。
- **p.171**（`p178.png`）：贴把手与磨光；$M^n_{c+\eps}\cong M^n_{c-\eps}\cup_\psi(D^{n-\lambda}\times D^\lambda)$；Morse 手术与 $N^{n-1}_{c+\eps}$ 的表达式、$\tilde D^{n-\lambda}$ 为内部；图 4.10；把手分解、图 4.11、4.12 与 Smale 函数——一致。
- **p.172**（`p179.png`）：图 4.11、4.12；(2.8) $m_\lambda(f)\ge b_\lambda,\ b_\lambda^{(p)}$；(2.9) $m_\lambda(f)\ge b_\lambda+q_\lambda+q_{\lambda-1}$；「这些就是 Morse 不等式」——一致。
- **p.173**（`p180.png`）：维数 $\ge6$ 单连通时不等式可取等号（Smale，60 年代初）；与 $M^n$ 同伦等价的 CW 复形构造；(2.10) 梯度流 $\frac{dx^i_\alpha}{dt}=-g^{ij}\frac{\partial f}{\partial x^j_\alpha}$、$g^{ij}g_{jq}=\delta^i_q$；Morse 坐标；$\lambda$-圆盘嵌入 $\phi$；图 4.13；(i)(ii)——一致。
- **p.174**（`p181.png`）：(iii) $\phi(\partial D^\lambda)\subset\partial M^n_{c-\eps}$；同伦 $\varphi_\tau$ 的定义与要点；逐临界点的 CW 构造与一般位置论证；(2.11)、(2.12)；Lyusternik–Shnirelman 范畴 $\mathrm{cat}(X)$ 的定义与 $m(f)\ge\mathrm{cat}(M^n)$——一致。
- **p.175**（`p182.png`）：上同调长度 $l(M^n)$ 与 $\mathrm{cat}(M^n)>l(M^n)$；$\mathrm{cat}(M^n)\le n+1$、$\mathrm{cat}(S^n)=2$、$\mathrm{cat}(M^2)=3$（$M^2\ne S^2$）、$\mathrm{cat}(\RP^n)=\mathrm{cat}(\CP^n)=n+1$；临界子流形（critical submanifold）的定义、非退化与指标、Hessian 在法向二次型、Pontryagin（30 年代末）与 Bott（50 年代）；法丛 $\nu^{\lambda_\alpha}\to W^k_\alpha$ 与最速下降方向；末句断在「可定向（即」——一致（跨页处理见建议改 1）。

## 体例抽查
- 页标记：`% [原文 p.165]`…`p.175]` 共 11 条，递增无重复。p.170、p.172 的标记落在句/段边界之后（该句起于上一页），符合 lead 的「页标记须落句界」补充规则 ✓。
- 编号公式：(2.1)–(2.12) 共 12 个，连续、无自造、无重号；正文引用「式 (2.3)」「式 (2.4)」「式 (2.7)」均为纯文本 ✓。
- 陈述环境：仅 1 处 `example{}`（原书 p.167 末有 □，故用无星版，正确）；check_chunk 提示「编号为空」是原书无编号所致，无需改 ✓。
- 图：fig4_6 至 fig4_14 共 9 幅，文件全部存在；`\figtitle` 齐（4.8 有中文题、其余原书只有「Fig. 4.x」故留空）✓；图 4.6、4.7、4.14 内嵌原书英文/符号，其中 4.14 的英文标签见建议改 2。
- Tutor Note：4 条（11 页，要求 ≥3）✓；均属三类允许内容（易错预警、省略论证点拨、背景直觉），无空话 ✓。
- 末行 `% CHUNK ch04c DONE` ✓；`check_chunk.py` 复跑 → OK，0 error。
