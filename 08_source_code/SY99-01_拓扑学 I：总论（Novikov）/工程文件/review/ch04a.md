# 核验报告 · ch04a（原书 p.142–152）

核验人：译者丙　　作者：译者丁　　日期：2026-11-09

## 结论
小改（公式与内容全对：逐页核对 11 页，编号 (1.1)–(1.17) 连续无缺、与原书逐个对应；例 1、两张图、Lie 群表、Stiefel/Grassmann 流形与分类空间、联络与曲率形式均无实质错误。必须改 4 条集中在体例：3 处页标记插在句子中间、1 处衍字。建议改若干为符号大小写与个别漏译。）

## 必须改（影响正确性）
1. **第 66 行**：页标记插在句中——「……对光滑性类充分高的任意映射 $f:M^n\to N^k$（$k\le n$），其`% [原文 p.145]`」后紧接「集合 $f(Z)$ 在 $N^k$ 中测度为零」。按 lead 新规（页标记必须独占一行、且只落在段落或句子边界），须把该句补完（「其集合 $f(Z)$……测度为零。」）后再放 `% [原文 p.145]`。
2. **第 134 行**：页标记插在句中——「……它是非退化的对称`% [原文 p.147]`」后紧接「$(0,2)$ 型张量（场）……」，把一个词（「对称 $(0,2)$ 型张量」）劈成两半。同样须移到句末。
3. **第 258 行**：页标记插在句中——「……并考察 $B\subset E$ 的每一点处的平面`% [原文 p.151]`」后紧接「（该平面在 $\R^N$ 中……）」。须移到句末。
4. **第 302 行**：衍字——「而曲率形式 $\Omega$ **局部地形如**」应为「局部形如」（原文 and the curvature form Ω has locally the form），「地」为衍字。

## 建议改（可读性/文风/排版）
1. **第 259 行（p.151）**：原书印「parallel-translating these planes to the origin in $\R^N$」，译文作「平行移动到 $\R^n$ 的原点」——与 p.150 的原书印法（那里确为 $\R^n$）混同了。建议 p.151 处照印 $\R^N$（p.150 处保留 $\R^n$，两页原书本来就印法不同）。
2. **第 146、150、152 行（p.147）**：Lie 群的二元运算原书印作大写 $\Psi$（`Ψ:M^n×M^n→M^n; Ψ(x,y)=x·y`，已放大核对），译文通篇用小写 `\psi`。建议改为 `\Psi`，并核对分量式 $z^j=\Psi^j(\ldots)$ 的大小写。
3. **第 12 行（p.142）**：「closely linked with analysis and, particularly in recent times, with contemporary mathematical physics」中的「particularly in recent times」（尤在近年）漏译，建议补「尤其近年来与当代数学物理紧密相连」。
4. **图 4.1 的图题**（第 38 行）：图内英文标注有 `Disk D(√b)`、`Disk D^n(√a)`、`R^n` 轴，图题只讲了 $W_\alpha$/$W'_\alpha$。建议在图题里补半句「图中横轴为 $\R^n$，两个盘 $D(\sqrt b)$、$D^n(\sqrt a)$ 示意 $W_\alpha\subset W'_\alpha$ 的嵌套」，便于读者对上英文标注。
5. 图 4.2 的裁图（第 57 行）只含原图 (i)(ii) 两段说明与图形、未含 `Fig. 4.2` 行，符合补充规则⑦；图题中译文完整，无需改。

## 抽查记录（逐页）
- **p.142**（`pages\p149.png`）：「Chapter 4 / Smooth Manifolds」与 `\section`、`\takeaway` 由本块写（正确，章、节标题都在 p.142）；Whitney 1930 年代的初等理论；可微流形的内蕴定义（拓扑流形、坐标卡、转移函数 $C^k$、$C^\infty$、实解析）；Jacobi 行列式非零；单位分解存在性与 $\psi_\alpha$ 的四条性质——逐句一致。
- **p.143**（`p150.png`）：图 4.1 与例 1（紧流形的单位分解、$\psi_\alpha x_\alpha^j=y_\alpha^j$、嵌入 $\{y_\alpha^j\}:M^n\to\R^{nN}$、$k\ge2n+1$ 时嵌入稠密、$k\ge2n$ 时浸入稠密、$n=1$ 见图 4.2）；光滑映射与秩的定义——一致（例 1 原书带 □，用无星 example，正确）。
- **p.144**（`p151.png`）：图 4.2；浸入/淹没/嵌入/微分同胚的定义；Whitney 的 $C^k$ 与 $C^\infty$（实解析）唯一性、Morrey 的实解析嵌入；一般位置引理（Sard：临界点集像测度零）——一致。
- **p.145**（`p152.png`）：一般位置（$f(Z)$ 测度零、$k>n$ 时 $f(M^n)$ 测度零）；切向量与切空间；(1.1) $\eta_\beta^k=\eta_\alpha^j\partial x_\beta^k/\partial x_\alpha^j$、(1.2) $\eta_{i\beta}=\eta_{k\alpha}\partial x_\alpha^k/\partial x_\beta^i$；$(m,k)$ 型张量与标准基——逐符号一致。
- **p.146**（`p153.png`）：张量的分量表示、$\partial/\partial x_\alpha^j$ 与 $dx_\alpha^j$ 的对偶；张量场；Einstein 求和约定；(1.3) $\Omega_k=\frac1{k!}T_{i_1\cdots i_k}dx^{i_1}\wedge\cdots\wedge dx^{i_k}$；外积的反对称性与 (1.4)；$d$ 的三条定义与 $d\circ d=0$、Leibniz 律——一致。
- **p.147**（`p154.png`）：Riemann/伪 Riemann 度量 $(0,2)$ 型张量、$g_{ij}=g_{ji}$、$\det(g_{ij})\ne0$、内积公式与 $g^{ij}g_{jk}=\delta_k^i$；Lie 群定义、$\Psi$ 的 Taylor 展开 (1.5)、Lie 代数 (1.6)(1.7) 与 Jacobi 恒等式；$O_{p,q}$——一致（符号大小写见建议改 2）。
- **p.148**（`p155.png`）：$O_n=O_{n,0}$、$U_{p,q}$、$U_n$、$SO_{p,q}$、$SU_{p,q}$、$SL_n$；$Sp_n$ 为 $n\times n$ 四元数正交矩阵子群；Cartan–Killing 定理（6 个紧单连通单 Lie 群）与 $(T^n\times G_1\times\cdots\times G_k)/D$；光滑纤维丛、光滑向量丛（实/复）；切丛 $\tau$、$T(M^n)$、截面即向量场、Riemann 度量使结构群约化为 $O_n$；余切丛 $\tau^*$ 与 $(m,k)$ 型张量丛——一致。
- **p.149**（`p156.png`）：外幂 $\Lambda^k(\tau^*)$ 的截面即微分形式、$S^2\tau$ 的截面即 Riemann 度量；$k$-标架丛；Stiefel 流形 $V^{\R}_{n,k}$、$V^{\C}_{n,k}$ 与 (1.8)；Grassmann 流形 $G^{\R}_{n,k}$、$G^{\C}_{n,k}$ 与 (1.9)；可定向 Grassmann 流形 $\widehat G^{\R}_{n,k}$ 及其二重覆叠、嵌入与正向极限、$\widehat G^{\R}_1$ 可缩、$G^{\R}_1=\RP^\infty$、$G^{\C}_1=\CP^\infty$——逐符号一致。
- **p.150**（`p157.png`）：(1.10) $\pi_j(V^{\R}_{n,k})=0$（$j<n-k$）、$\pi_j(V^{\C}_{n,k})=0$（$j<2(n-k)$）；主丛 (1.11) 与极限 $E^{\R}_\infty$ 等可缩；(1.12) $BO_k=G^{\R}_k$、$BSO_k=\widehat G^{\R}_k$、$BU_k=G^{\C}_k$；分类对应 $[M^n,BG]$；Gauss 映射 $f:M^n\to G^{\R}_{N,n}$（可定向时到 $\widehat G^{\R}_{N,n}$）；原书此处印 $M^n\to BO_k$（$k$ 非 $n$，是原书印法），译文照印，正确——一致。
- **p.151**（`p158.png`）：向量丛全空间可缩到零截面、嵌入 $\R^N$、Gauss 映射 $B\to G^{\R}_{N,n}$；任意有限 CW 复形有同伦等价的光滑流形；一般 $G\subset\Diff F$ 的万有丛 $E_N(F)$、$E_\infty(F)$、Milnor 构造；同伦正合列 $SO_{n-1}\to SO_n\to S^{n-1}$、$U_{n-1}\to U_n\to S^{2n-1}$、(1.13)、稳定同伦群与 Bott——一致（$\R^N$ 见建议改 1）。
- **p.152**（`p159.png`）：右不变 1-形式 $\omega_0$ 与 (1.14) $-\frac12[\omega_0,\omega_0]=d\omega_0$、$g^*\omega_0=(\mathrm{Ad}\,g)\omega_0$；主丛 $(E,B,G,\cG,p)$ 上的联络 1-形式 $\omega$ 与 (1.15) $g^*\omega=(\mathrm{Ad}\,g)\omega$、$\omega|F=\omega_0$；曲率形式 (1.16) $\Omega=d\omega+\frac12[\omega,\omega]$、「纯水平」；局部形式 $\omega_{\phi_U}=A_adx^a$、$\Omega_{\phi_U}=F_{ab}dx^a\wedge dx^b$ 与 (1.17) $F_{ab}=\partial_aA_b-\partial_bA_a+[A_a,A_b]$——逐符号一致（衍字见必须改 4）。

## 体例抽查
- 页标记：`% [原文 p.142]` … `% [原文 p.152]` 共 11 个，递增、无重复 ✓；但 3 处落在句中（见必须改 1–3）。跨页句 1 处。
- 编号：`\tag` (1.1)–(1.17) 共 17 个，连续无缺、无自造 ✓；多行公式 (1.5)(1.8)(1.9)(1.10)(1.11)(1.13) 用 `gathered` 单 tag，与原书右侧单编号一致 ✓。
- 陈述：例 1 用 `example{}`（原书带 □，无编号）✓；check_chunk 的「空编号」WARN 属预期。
- 结构：第 4 章章标题、§1 节标题与 `\takeaway` 均在本块（p.142）写，且只写一次 ✓。
- 图：图 4.1、4.2 均为原页裁图（不含 `Fig.` 行），`\figtitle{4.1}`、`\figtitle{4.2}` 用中文另写 ✓。
- Tutor Note：5 条（要求 ≥ 11/3 = 3.7）✓；单行、无 `%` 字符。
- `% CHUNK ch04a DONE` 在末行 ✓。
- check_chunk：`python work\check_chunk.py src\chunks\ch04a.tex` 复跑 **0 error**（1 条空编号 WARN 属预期）。
