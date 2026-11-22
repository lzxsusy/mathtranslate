# 第 11 章 通读笔记：Cogdell, *Dual Groups and Langlands Functoriality*

底本 pp. 251–268（PDF 253–270），页图 `work/pages/c11_p253.png`–`c11_p270.png`。

## 三句话主旨

1. 对一般连通约化群 $G$，Galois 侧该用什么代替 $\GL_n(\mathbb{C})$？答案是 Langlands 对偶群 ${}^{L}G$：把根数据对偶化，再让 $\mathcal{G}_k$ 通过外自同构作用上去。
2. 有了 ${}^{L}G$，局部与整体 Langlands 猜想就可统一写成「容许同态 $W'_k\to{}^{L}G$（或 $\mathcal{L}_k\to{}^{L}G$）参数化容许/自守表示」，而函子性原则断言每个 L 同态 ${}^{L}H\to{}^{L}G$ 都给出表示层面的提升。
3. 例子分两类：Galois 理论的（基变换、自守诱导、内型）多用迹公式；群论的（张量积、对称幂、典型群）近来全靠 $\GL_n$ 逆定理，而逆定理的解析输入来自 Langlands–Shahidi 方法。

## 逐节内容地图

- **导言（pp. 251–252）**：从 $\GL_n$ 的猜想讲到一般 $G$ 的两个未知：自守侧换成 $G(k)$/$G(\mathbb{A})$ 的表示（已知），Galois 侧的目标换成 ${}^{L}G$（本章主题）。动机有二：Satake 参数化 [33] 与代数环面表示的分类 [24]。列出已由迹公式得到的例子（循环基变换、循环自守诱导、内型间提升）与用逆定理新得的到 $\GL_n$ 的提升（Ramakrishnan $\GL_2\times\GL_2\to\GL_4$；Kim–Shahidi $\GL_2\times\GL_3\to\GL_6$、$\mathrm{sym}^3,\mathrm{sym}^4$；CKPS 典型群 $\to\GL_N$）。末段交代全文结构与致谢。

- **§1 对偶群（pp. 252–253）**
  - 记号：$X=\mathcal{X}^*(T)$、$\Phi=\Phi(G,T)$、$\Delta$；对偶三元组 $(X^{\vee},\Phi^{\vee},\Delta^{\vee})$，$X^{\vee}=\mathcal{X}_*(T)$。
  - 根数据 $\Psi(G)=(X,\Phi,X^{\vee},\Phi^{\vee})$；带基根数据 $\Psi_0(G)=(X,\Delta,X^{\vee},\Delta^{\vee})$。
  - **定理 1.1**：$\Psi(G)$ 在不计 $\bar k$-同构下决定 $G$（Chevalley）。
  - 分裂正合列 $1\to\operatorname{Int}(G)\to\operatorname{Aut}(G)\to\operatorname{Aut}(\Psi_0(G))\to 1$；选根向量 $x_\alpha$（$\alpha\in\Delta$）给出分裂（pinning）与典范同构 $\operatorname{Aut}(\Psi_0(G))\to\operatorname{Aut}(G,B,T,\{x_\alpha\})$。
  - $\mathcal{G}_k\to\operatorname{Aut}(G_{/\bar k})\to\operatorname{Aut}(\Psi_0(G))$。
  - 对偶化：$\Psi_0(G)^{\vee}=(X^{\vee},\Delta^{\vee},X,\Delta)$ 定义 $\mathbb{C}$ 上连通约化群 ${}^{L}G^{0}$；$\operatorname{Aut}(\Psi_0({}^{L}G^{0}))=\operatorname{Aut}(\Psi_0(G))$ 使 Galois 作用可搬过来，得 $\mu:\mathcal{G}_k\to\operatorname{Aut}({}^{L}G^{0})$ 固定分裂 $({}^{L}G^{0},{}^{L}B^{0},{}^{L}T^{0},\{x_{\alpha^{\vee}}\})$。
  - **定义 1.1**：${}^{L}(G_{/k})={}^{L}G={}^{L}G^{0}\rtimes\mathcal{G}_k$（原书排作 $\times$）。
  - **注 1**：Weil 形式 ${}^{L}G^{0}\rtimes W_k$、Weil–Deligne 形式。**注 2**：$G,G'$ 在 $\bar k$ 上同构时，互为内型 $\iff$ ${}^{L}G\cong{}^{L}G'$ 于 $\mathcal{G}_k$ 上；故对偶群只分辨到内型，但完全决定准分裂型。
  - 型：$A_n,D_n$ 保持，$B_n\leftrightarrow C_n$；伴随型 $\leftrightarrow$ 单连通型。**表**（$G$ 对 ${}^{L}G^{0}$）：$\GL_n\mapsto\GL_n(\mathbb{C})$；$\mathrm{SO}_{2n+1}\mapsto\mathrm{Sp}_{2n}(\mathbb{C})$；$\mathrm{Sp}_{2n}\mapsto\mathrm{SO}_{2n+1}(\mathbb{C})$；$\mathrm{SO}_{2n}\mapsto\mathrm{SO}_{2n}(\mathbb{C})$；伴随型 $\mapsto$ 单连通型；单连通型 $\mapsto$ 伴随型。
  - 局部–整体相容：$\iota_v:{}^{L}G_v\to{}^{L}G$。

- **§2.1 局部 Langlands 猜想（pp. 254–256）**
  - $W'_k$（Weil–Deligne 群；阿基米德时取 $W'_k=W_k$）。
  - 容许同态三条件：(i) 在 $\mathcal{G}_k$ 上（方块交换）；(ii) 连续、$\phi(\mathbb{G}_a)$ 在 ${}^{L}G^{0}$ 中幂幺、半单映半单；(iii) $\phi(W'_k)$ 落在真抛物 $P$ 的 Levi 中 $\Rightarrow P$ 相干（relevant）。
  - $\Phi(G)$ = 容许同态模 ${}^{L}G^{0}$ 内自同构。内型未必给出同一 $\Phi$，因 (iii) 看见 $k$-结构；$G$ 准分裂时 $\Phi(G')\subset\Phi(G)$。
  - 两个补充构造：$\omega_\phi$（$C(G)$ 的特征）；$\alpha\in H^1(W'_k;C({}^{L}G^{0}))\mapsto\chi_\alpha$（$G(k)$ 的特征）。$\phi=(\phi_1,\phi_2)$，$\phi\mapsto\phi_1$ 给出 $\Phi(G)\hookrightarrow H^1(W'_k;{}^{L}G^{0})$，$H^1(W'_k;C({}^{L}G^{0}))$ 作用保持 $\Phi(G)$。
  - **局部 Langlands 猜想**：满射 $\mathcal{A}(G)\to\Phi(G)$，纤维有限，纤维 $\mathcal{A}_\phi$；五条性质 (i) 中心特征、(ii) 与扭相容、(iii) 模中心平方可积 $\iff$ $\phi(W'_k)$ 不在真 Levi 中、(iv) 缓增 $\iff$ $\phi(W_k)$ 有界、(v) 与 $\eta:H(k)\to G(k)$（核余核均交换）相容，$\pi$ 限制到 $H(k)$ 分解为有限多个 $\mathcal{A}_{{}^{L}\eta\circ\phi}(H)$ 中的表示之直和。
  - L 包；文献 [4] 的版本 I 即 $\GL_n$ 情形（L 包为单点，双射）。
  - 已知：1. 阿基米德（Langlands [26]，完全）；2. 无分歧（Satake [33] 的重述）；3. Iwahori 不动向量（Kazhdan–Lusztig [19]）；4. 分裂 $\mathrm{SO}_{2n+1}$ 的 generic 表示（Jiang–Soudry [16,17]，由 $\GL_{2n}$ 拉回）。
  - L 函数：需 $r:{}^{L}G\to\GL_n(\mathbb{C})$（连续，限制到 ${}^{L}G^{0}$ 为复 Lie 群态射）。**定义 2.1** $L(s,\pi,r)=L(s,r\circ\phi)$、$\varepsilon(s,\pi,r,\psi)=\varepsilon(s,r\circ\phi,\psi)$。故同一 L 包内无法用 L/$\varepsilon$ 因子区分。只有参数化已知时才有定义（如无分歧）。
  - 版本 II：解析定义的 L/$\varepsilon$ 因子与此处定义者匹配（[3] 中 $\GL_n$ 情形）；一般约化群未见此表述，Jiang–Soudry 实际做到：$r:\mathrm{Sp}_{2n}(\mathbb{C})\hookrightarrow\GL_{2n}(\mathbb{C})$，$L(s,\pi\times\pi')=L(s,\pi\times\pi',r\otimes\mathrm{id})=L(s,(r\circ\phi_\pi)\otimes\rho_{\pi'})$。

- **§2.2 整体 Langlands 猜想（pp. 256–257）**
  - $\mathcal{L}_k$ 替代 $W'_k$，$\phi:\mathcal{L}_k\to{}^{L}G$；形式「相当猜想性」。
  - 局部–整体相容：$\pi=\bigotimes'\pi_v\mapsto\{\phi_v\}$，复合 $\iota_v$ 得 $\{\iota_v\circ\phi_v\}$；这组局部数据足以定义整体 L/$\varepsilon$ 因子。
  - **定义 2.2**：$L(s,\pi,r)=\prod_v L(s,\pi_v,r_v)=\prod_v L(s,r\circ\iota_v\circ\phi_v)$，$\varepsilon$ 同理；$\psi=\bigotimes\psi_v$ 在 $k$ 上平凡。
  - 部分 L 函数 $L^S(s,\pi,r)=\prod_{v\notin S}L(s,\pi_v,r_v)$ 总有定义，绝对收敛于右半平面（Langlands [25]）。

- **§3 函子性（pp. 257–259）**
  - L 同态 $u:{}^{L}H\to{}^{L}G$ 三条件（在 $\mathcal{G}_k$ 上、连续、限制到 ${}^{L}H^{0}$ 为复解析）。
  - $G$ 准分裂时 $u\circ\phi\in\Phi(G)$，得 $\Phi(u)$；局部 $u_v$ 由限制得到。
  - **函子性原则**（原文以斜体陈述）：$k$ 局部（或整体），$H,G$ 连通约化、$G$ 准分裂，则每个 L 同态对应一个转移/提升。
  - §3.1 局部：$\phi'=u\circ\phi$ 参数化 L 包 $\mathcal{A}_{\phi'}(G)$，即提升。三种已理解情形：阿基米德；$\GL_m\to\GL_n$；无分歧（有 $\mathcal{O}$ 结构、特殊极大紧子群 $H(\mathcal{O})$、$G(\mathcal{O})$，唯一无分歧 $\Pi$，称自然无分歧提升）。
  - §3.2 整体：绕过 $\mathcal{L}_k$，用局部–整体相容逐位点提升。**定义 3.1** 弱/强提升。推论：$L^S(s,\pi,r\circ u)=L^S(s,\Pi,r)$、$\varepsilon^S$ 同理。须在 L 包层面理解，歧义常存。

- **§4 例子（pp. 260–265）**
  - $H=\{1\}$：${}^{L}H=W'_k$（Weil–Deligne 形式的 L 群），$u$ 即容许同态，函子性 $=$ 局部 Langlands；整体用 Galois 形式即得 $\GL_n$ 整体猜想。这是 Langlands 视函子性为「包含猜想」的理由。
  - 两类：Galois 理论（基变换、自守诱导、内型）与群论（张量积、对称幂、典型群）。明确不涉及内视（endoscopy）：内视是 $u$ 把 ${}^{L}H^{0}$ 实现为 ${}^{L}G^{0}$ 中某对合的不动点者，其重要性在于理解迹公式。
  - §4.1：基变换（$G=R_{K/k}H$，$u$ 把 ${}^{L}H^{0}\times\mathcal{G}_k$ 对角嵌入 $\prod_{\mathcal{G}_K\backslash\mathcal{G}_k}{}^{L}H^{0}\rtimes\mathcal{G}_k$；$n=2$ Langlands，可解扩张 Arthur–Clozel，非正规三次 JPSS）；自守诱导（$H=R_{K/k}\GL_n$、$G=\GL_{dn}$，分块对角 + $\mathfrak{S}_d$ 置换矩阵；Arthur–Clozel，$n=2$ Jacquet–Langlands，Henniart–Herb，$n=1$ Kazhdan）；内型（${}^{L}H={}^{L}G$，恒等映射；Jacquet–Langlands $D^{\times}\to\GL_2$；Rogawski $m=1$；Deligne–Kazhdan–Vignéras）。
  - §4.2：张量积（$\GL_m\times\GL_n\to\GL_{mn}$，$u_\otimes$）；对称幂（$\mathrm{sym}^n:\GL_2(\mathbb{C})\to\GL_{n+1}(\mathbb{C})$，Gelbart–Jacquet $n=2$，Kim–Shahidi $n=3$，Kim $n=4$，全 $n$ $\Rightarrow$ Ramanujan）；典型群（表：$H$、${}^{L}H^{0}$、$u^{0}$、${}^{L}G^{0}$、$G$；CKPS 弱提升 $\mathrm{SO}_{2n+1}\to\GL_{2n}$，GRS 强化并刻画像，Jiang–Soudry 局部推论）。
  - 逆定理方法总述：逐位点局部提升 $\Pi_v$ $\to$ 局部 L 因子等式 $\to$ 整体 $L(s,\pi,r)=L(s,\Pi,\iota)$ $\to$ 扭 $L(s,\pi\times\pi',r\otimes\iota)$ 的解析控制（Langlands–Shahidi）$\to$ 逆定理得 $\Pi$ 自守。
  - 重访三例：Ramakrishnan 需 $\pi'$ 在 $\GL_1,\GL_2$ 上（Rankin 三重积，Garrett / Rallis–PS 积分表示）；Kim–Shahidi 需 $m=1,2,3,4$（$\GL_5$、$\mathrm{Spin}_{10}$、$E_6$、$E_7$ 上 Eisenstein 级数）；对称幂（$\GL_3$ 逆定理、Shimura 积分；$\mathrm{sym}^3,\mathrm{sym}^4$ 由 $\GL_2\times\GL_3$ 与外平方推出）。
  - 典型群的次生问题：有限位点集 $S$ 上参数化未知 $\Rightarrow$ 取任意（平凡中心特征）局部提升，用高度分歧伊代尔类特征 $\eta$ 的扭补偿；$\eta$ 的两个作用（控制整体极点；经 $\gamma$ 因子稳定性匹配局部因子）；得弱提升 $\Pi'$。$\gamma$ 因子稳定性：原仅 $\mathrm{SO}_{2n+1}$ [8,5]，借 Shahidi 局部系数 $=$ Bessel 函数 Mellin 变换 [35] 推广到其他分裂典型群 [6]。$\mathrm{SO}_{2n+1}$ 情形由 GRS 得强提升与像的刻画，Jiang–Soudry 据此拉回 $\GL_N$ 的参数得 ${}^{L}H$ 的参数。
  - 参考文献 36 条（pp. 265–268），本译本不迻录。

## 体裁

综述（survey）。第一人称单数出现数次（"I would like to thank the referee"、"I have not seen a formulation"、"The other examples of functoriality I wish to discuss"），译文保留「我」。技术层级：定义—猜想—原理—例子，几乎无证明；编号段仅定理 1.1、定义 1.1、定义 2.1、定义 2.2、定义 3.1、函子性原则、局部 Langlands 猜想。两处表格、两处交换方块、若干独立公式。文风偏 Borel 学派，句子长、从句多，须拆句。

## 风险点（落笔时逐条核对页图）

1. **${}^{L}G$ 的排版**：原书用左上标 $L$；定义 1.1 中印作 $\times$，但语义是半直积（$\mathcal{G}_k$ 经 $\mu$ 作用），译文用 $\rtimes$ 并在译注说明。
2. **$\Phi$ 一号两用**：§1 的 $\Phi=\Phi(G,T)$ 是根系，§2 起 $\Phi(G)$ 是容许同态集；原书自己在 p. 254 提醒勿与 [4] 的几何 Frobenius 混淆。译文保留字母，译注点明。
3. **$\Psi_0(G)^{\vee}$ 的次序**：$(X^{\vee},\Delta^{\vee},X,\Delta)$，不是 $(X,\Delta,X^{\vee},\Delta^{\vee})$ 的逐项对偶写法以外的顺序；页图 p. 253 首行可核。
4. **表 1 的 `SO_{2n}` 行**：原书给 ${}^{L}G^{0}=\mathrm{SO}_{2n}(\mathbb{C})$，与「伴随型 $\leftrightarrow$ 单连通型」的规则看似冲突（$\mathrm{SO}_{2n}$ 既非单连通也非伴随，是 $\mathrm{Spin}_{2n}$ 的中间商），须译注解释。
5. **条件 (iii) 的 `relevant`**：原书不定义，只指向 Borel [2]；译文用「相干的」并加括注，不擅造定义细节。
6. **$W'_k$ 与 $W_k$**：条件 (ii) 中 $\phi(\mathbb{G}_a)$ 幂幺、条件 (iii)(iv) 中分别用 $W'_k$ 与 $W_k$（(iii) 用 $W'_k$，(iv) 用 $W_k$），页图 p. 255 可核，不可统一。
7. **Def 3.1 前一句的笔误**：原文 "Now let $\pi\in\mathcal{A}(G)$, $\pi=\bigotimes'\pi_v$, be an irreducible automorphic representation of $H(\mathbb{A})$" —— 应为 $\mathcal{A}(H)$；译文改正并在译注说明。
8. **p. 265 的 $\Pi$ 与 $\Pi'$**：弱提升记 $\Pi'$，正文先说 "$\Pi_v=\Pi'_v$ for all $v\notin S$"；译文照原书，但在译注说明弱提升唯一性来自 $\GL_N$ 的强重数一。
9. **基变换公式的指标集**：$\mathcal{G}_K\backslash\mathcal{G}_k$ 是双陪集，等于 $\operatorname{Hom}_k(K,\bar k)$；$\mathcal{G}_k$ 的置换作用与 ${}^{L}H^{0}$ 上的对角映射要分清（原书说得简略）。
10. **公式回页图**：定理 1.1 的正合列、$\operatorname{Aut}$ 的典范同构、定义 1.1、表 1、条件 (i)–(v)、定义 2.1–2.2、函子性原则、定义 3.1 后的 L 因子等式、基变换与自守诱导的嵌入、表 2、p. 263 的四条 L 因子等式、p. 265 的四重等式，均已逐页核对（p. 254、255、256、257、258、259、260、262、263、265、267）。
11. **禁止 overfull**：表 2 五列、$\prod_{\mathcal{G}_K\backslash\mathcal{G}_k}$ 的公式、p. 263 的四重等式最长，须拆行或缩字号。
