# ch03b 译校报告

块：ch03b（原书 §3.3）｜书页 p.549–555（p.555 仅取到命题 3.3.5 为止，3.4 标题归 ch03c）
产出：`src/chunks/ch03b.tex`（276 行）｜`work/proposals/ch03b.tsv`

## 1 内容与结构

覆盖小节：仅 §3.3“代表全忠实函子的对象之构造”。本块不含 `\chapter`，起首为
`\section{代表全忠实函子的对象之构造}` + 一条 `\takeaway`（构造路线：极丰富线丛 → 闭嵌入 → $\PP^{N}\times X$ 上的 $\cE'$ → 切回 $M\times X$ 上的 $\cE$）。

页标记 7 处，与书页一一对应、单调递增：p.549、550、551、552、553、554、555。
段落：与原书逐段对应，段序段数一致；跨页段落按原书换页处硬插页标记，不另起段
（如 p.550/551 交界“……再取它在第二个因子上的∥投影下的直接像”，p.552/553 交界“……典范态射
$B_{m}\otimes\cO_{M}\to B_{m-1}\otimes\cL$∥的核，该态射由自然嵌入……”，p.554/555 交界“……但有特异三角∥同上可以证明”）。

陈述 5 条（编号照抄原书，无 `\label`/`\ref`，末尾不加符号）：

| 编号 | 环境 | 内容 |
| --- | --- | --- |
| 3.3.1 | lemma | 对一切 $k\in\Z$ 有典范同构 $f_k:F'(\cO(k))\iso\Phi_{\cE'}(\cO(k))$，且函子性（对 $\alpha:\cO(k)\to\cO(l)$ 的方块交换） |
| 3.3.2 | remark | 由 $F$ 构造的 $\cE'\in\Db(\PP^{N}\times X)$ 唯一确定 |
| 3.3.3 | definition | $n$-Koszul 代数与 Koszul 代数（右 $A$-模序列正合） |
| 3.3.4 | proposition | 对任一 $n$ 可选 $\cL$ 使 1) $A$ 为 $n$-Koszul；2) $A_{k-n}\otimes R_n\to\cdots\to\cL^k\to0$ 正合；3) $\cL^{-n}\boxtimes R_n\to\cdots\to\cO_\Delta$ 给出对角的 $n$-消解 |
| 3.3.5 | proposition | 存在 $\cE\in\Db(M\times X)$ 使 $\Rf J_*\cE\cong\cE'$，且同构意义下唯一 |

证明环境 1 个（引理 3.3.1 的证明，原书 5 段，本译本同 5 段）。

## 2 公式与图

编号公式 7 条，全部 `\tag{原编号}`、逐条核过页图：

- (31) $0\to\cO(-N)\boxtimes\Omega^{N}(N)\xrightarrow{d_{-N}}\cO(-N+1)\boxtimes\Omega^{N-1}(N-1)\to\cdots\to\cO(-1)\boxtimes\Omega^{1}(1)\xrightarrow{d_{-1}}\cO\boxtimes\cO.$（原书排两行，末有句点；译本用 `aligned` 两行，句点保留）
- (32) $C^{\bullet}:=\{\cO(-N)\boxtimes F'(\Omega^{N}(N))\xrightarrow{d'_{-N}}\cdots\to\cO(-1)\boxtimes F'(\Omega^{1}(1))\xrightarrow{d'_{-1}}\cO\boxtimes F'(\cO)\}.$
- (33) $B_m=\Ker(B_{m-1}\otimes A_1\xrightarrow{u_{m-1}}B_{m-2}\otimes A_2),$（原书末尾为**逗号**，照录，因同句续“其中 $u_{m-1}$ …”）
- (34) $0\to R_m\to B_m\otimes\cO_M\to B_{m-1}\otimes\cL\to\cdots\to B_1\otimes\cL^{m-1}\to\cL^m\to0.$
- (35) $0\to\Omega^m(m)\to\bigwedge^{m}A_1\otimes\cO\to\bigwedge^{m-1}A_1\otimes\cO(1)\to\cdots\to\cO(m)\to0.$（$m$、$m-1$ 排在 $\bigwedge$ 顶点上方；末句点）
- (36) $\cL^{-n}\boxtimes F(R_n)\to\cdots\to\cL^{-1}\boxtimes F(R_1)\to\cO_M\boxtimes F(R_0).$
- (37) $A_{k-n}\otimes F(R_n)\to A_{k-n+1}\otimes F(R_{n-1})\to\cdots\to A_k\otimes F(R_0).$

无编号 display 共 20 余处，均按页图逐符号核（$d'_{-i}$ 的定义与 6 行复合映射链；$\Hom^{l}$ 三行链；$k\ge0$ 时 $\cO(k)$ 的消解→$\delta_k$→$\cO(k)$；$D^{\bullet}_k$ 复形；$\Hom^{i}(F'(\cG),F'(\cH))=\Hom^{i}(j^*\cG,j^*\cH)=0$；引理 3.3.1 内的 $f_k$；p.552 两行等式与 $h\circ F'(\delta_k)$；$\cO(k)\iso\{V^k_0\otimes\cO\to\cdots\}$；定义 3.3.3 的模序列；$B_m\otimes\cO_M\to B_{m-1}\otimes\cL$；命题 3.3.4 的三个式子；$A_{k-n}\otimes R_n\to\cdots\to A_k\otimes R_0$；$\cL^{-k}\boxtimes F(R_k)\to\cL^{-k+1}\boxtimes F(R_{k-1})$；p.554 两行 $\Hom$ 同构；特异三角 $S\to K\to\cE'\to S[1]$；p.555 三式）。

交换图 9 个，全部以 TikZ 重绘（`\diag{…}`；552a、554a、555b 三图较宽，改用同款 tikzcd 环境并局部收紧 `column sep`／放宽 `row sep`）。已按 Lead 要求删除全部 `\figdiag`、不再引用任何位图裁切；节点与箭头逐条对页图核过：

| 编号 | 位置 | 节点与箭头 | 标注 |
| --- | --- | --- | --- |
| 549a | p.549 末（“并考虑投影构成的图”） | $\PP^N\times X\xrightarrow{\pi'}X$，左竖 $q$ 指向 $\PP^N$ | 无 $\cong$、无 $\eta$；图右侧印孤立句点 |
| 550a | 引理 3.3.1 内 | 上 $F'(\cO(k))\xrightarrow{F'(\alpha)}F'(\cO(l))$；左竖 $f_k$、右竖 $f_l$；下 $\Phi_{\cE'}(\cO(k))\xrightarrow{\Phi_{\cE'}(\alpha)}\Phi_{\cE'}(\cO(l))$ | 无 |
| 551a | 证明第 3 段末（“使下图交换”） | 上 $H^0(\cO(k))\otimes F'(\cO)\xrightarrow{F'(\delta_k)}F'(\cO(k))$；左竖 $\id$、右竖 $f_k$；下横 $\Rf\pi'_*(\gamma_k)$ 至 $\Phi_{\cE'}(\cO(k))$ | 右侧孤立句点 |
| 551b | 证明第 4 段（“对任一 $\alpha$”） | 同形；左竖 $H^0(\alpha)\otimes\id$、右竖 $F'(\alpha)$；下横 $F'(\delta_l)$ | 无 |
| 551c | 同上（“以及”） | 左竖 $H^0(\alpha)\otimes\id$、右竖 $\Phi_{\cE'}(\alpha)$；下横 $\Rf\pi'_*(\gamma_l)$ | 右侧孤立句点 |
| 552a | $k<0$ 情形（“可见复形映射”） | 上行 $V^k_0\otimes F'(\cO)\to\cdots\to V^k_N\otimes F'(\cO(N))$；下行 $V^k_0\otimes\Phi_{\cE'}(\cO)\to\cdots\to V^k_N\otimes\Phi_{\cE'}(\cO(N))$；左竖 $\id\otimes f_0$、右竖 $\id\otimes f_N$ | 两竖箭头旁**各带 $\wr$** |
| 554a | p.554（“考虑 $\Db(\PP^N\times X)$ 上的复形映射”） | 上行 $\cO(-n)\boxtimes F'(\Omega^n(n))\to\cdots\to\cO\boxtimes F'(\cO)$；下行 $\Rf j_*\cL^{-n}\boxtimes F(R_n)\to\cdots\to\Rf j_*\cO_M\boxtimes F(R_0)$；左竖 $\mathrm{can}\boxtimes F(f_n)$、右竖 $\mathrm{can}\boxtimes F(f_0)$ | 页图此处印**小写 $j$**（见 §5、Tutor Note）；右侧孤立句点 |
| 555a | p.555（“使下图交换”） | 上 $K\xrightarrow{\varphi}\Rf J_*G$；下 $\cE'\xrightarrow{\psi}\Rf J_*\cE$ | 两竖箭头**无标号**；右侧孤立句点 |
| 555b | p.555（“这些 $\psi_k$ 装进交换图”） | 上 $S^kA_1\otimes F(\cO)\xrightarrow{\mathrm{can}}F(\cL^k)\xrightarrow{\sim}\Rf\pi'_*(\cE'\otimes q^*(\cO(k)))$；下 $A_k\otimes F(\cO)\xrightarrow{\mathrm{can}}F(\cL^k)\xrightarrow{\sim}\Rf\pi_*(\cE\otimes p^*(\cL^k))$；左竖 $\mathrm{can}$、右竖 $\psi_k$ | 见 §5、Tutor Note |

页图与文字层出入（逐条：页码＋文字层抽出＋页图实际＋处理）：

1. p.549 文字层“$RE'=RJ_*E$” → 页图确为 $\cE'=\Rf J_*\cE$（大写 $J$）→ 照录，非笔误。
2. p.552 文字层“$RJ_*E\simeq E'$” → 页图为 $\cong$ → 译作“$\cong$”。
3. p.553 文字层“$\wedge^{i}A_1\subset B_i$”“$\wedge^m$” → 页图为 $\bigwedge$，且 $m$、$m-1$ 在顶点上方 → 用 `\bigwedge^{m}`。
4. p.550–554 文字层多处丢 $\boxtimes$、上下标（“$d'_{-i}$”抽成“d′−i”、“$C^{\bullet}$”抽成“C·”）→ 一律以页图为准。
5. p.551 文字层“$\pi'_*(C^{\bullet}_k)$”无粗体 $\mathbf R$，页图亦然（与同句后半的 $\Rf\pi'_*$ 不一致）→ 照录 + Tutor Note。
6. p.552 文字层“an object in the category $E\in\Db(M\times X)$”→ 页图语序相同（非抽字错误）→ 按原意译 + Tutor Note。
7. p.554 图内两处竖箭头写作 $\Rf j_*$（小写），而 p.549/552/555 同函子作 $\Rf J_*$ → 照录 + Tutor Note。
8. p.555 图左上 $S^kA_1\otimes F(\cO)$、左下 $A_k\otimes F(\cO)$ → 页图放大核实为原样，非 OCR 误识 → 照录 + Tutor Note。
9. 命题 3.3.5 末尾页图无句点 → 中文按习惯以句号收尾 + Tutor Note。
10. p.551 证明第 1 段以**小写**“since”起句（紧跟花括号复形的冒号）→ 译本按中文断句处理，不另加批注。

## 3 译注

`\yizhu` 4 条（均 60–200 字，均以【来源：…】收尾，来源限 A 级）：

1. 式 (31) 后：说明它就是 Beilinson 为 $\PP^N\times\PP^N$ 对角所造的 Koszul 型消解，第 $-i$ 项 $\cO(-i)\boxtimes\Omega^{i}(i)$，微分由外积与缩并配对给出，并与 (35) 的代数版对应。【来源：原书 p.549 式 (31) 及 p.553 式 (35)。】
2. (32) 后：解“卷积”这一操作（$\bigoplus_i C^i[-i]$ 配符号微分），指出其唯一性即引理 3.1.2 的内容，说明后文“同一复形的卷积⇒同构”的用法。【来源：原书 p.550 对引理 3.1.2 的援引，及 p.551、p.553 的同类论证。】
3. 定义 3.3.3 后：$n$-Koszul 是 Koszul 性的有限截断；$B_m$ 为 Koszul 复形各项；$\bigwedge^iA_1\subset B_i$ 是交换情形的线性部分。【来源：原书 p.552 定义 3.3.3、p.553 的嵌入，及文献 [1]（Backelin）。】
4. 命题 3.3.5 后：全节路线“先放大、再切掉”，并说明 $S$ 的上同调区间 $[-n-a,-n]$ 与 $\Rf J_*\cE$ 的 $[-a,0]$ 不相交。【来源：原书 p.549–555 全节结构及 p.555 末的论证。】

`% [Tutor Note: …]` 5 条：① p.551 $\pi'_*$ 无粗体 $\mathbf R$ 而前后作 $\Rf\pi'_*$；② p.552 “object in the category $E\in\Db$”语序错位；③ p.554 图内 $\Rf j_*$ 与全篇 $\Rf J_*$ 不一致；④ p.555 图内 $S^kA_1$ 与 $A_k$ 并置（$A$ 由 $A_1$ 生成时二者相同）；⑤ 命题 3.3.5 末尾页图无句点。

## 4 术语

沿用冻结表：closed embedding 闭嵌入、very ample 极丰富／ample 丰富、line bundle 线丛、graded algebra 分次代数、homogeneous coordinate algebra 齐次坐标代数、resolution of the diagonal 对角的消解、coherent sheaf 凝聚层、perfect complex 完美复形、distinguished triangle 特异三角、convolution 卷积、canonical isomorphism 典范同构、structure sheaf 结构层、diagonal 对角、cohomology 上同调、Koszul complex Koszul 复形、n-Koszul 保留。

新定（已写入 `work/proposals/ch03b.tsv`，6 条）：Veronese 代数、上同调层、$n$-消解、局部自由层、射影空间、Koszul 代数。
其中 **homological dimension（同调维数）**与 **right resolution（右消解）** 已于 ch03a 的提案中出现，本块沿用同一译法（同调维数／右消解），建议 glossary 合并为一条。

提请复核：`n-Koszul` 按 glossary 保留拉丁，故本块未把“$n$-Koszul 代数”改成中文；“Koszul 代数”与之同族，命名策略一致。`$\bigwedge^{i}A_{1}\subset B_{i}$` 中的 $\bigwedge$ 属外代数，未另立术语。

## 5 存疑

1. **图资产问题（已由 Lead 处置）**：`src/figures/` 于 00:43 生成的那批裁图在成品 PDF 中显示异常——`dg_549_a`（MediaBox 69.9×19.2pt）裁切框偏右偏上，左缘只剩“$\times X$”，$\PP^N$ 被切，再经 `width=0.92\linewidth` 放大 5 倍后成品只剩一根大竖箭头与字母“$N$”；`dg_554_a` 右端被切（“can⊠”、“$F(i”）；`dg_518_a`（ch03a 用）框到原书英文正文。**现处置**：`src/figures/` 已清空、`\figdiag` 只印占位框，本块 9 图全部改为 TikZ 重绘，不再依赖位图；成书渲染已逐图核对（p.551、p.553、p.554 三处宽图另调整了间距）。
2. **p.555 的 $S^kA_1$**：页图确实是 $S^kA_1$，而左下是 $A_k$。本译本照录并批注（$A$ 由 $A_1$ 生成时二者相同）。
3. **命题 3.3.5 的“$\cE'$ 是 §3.3 中构造的”**：原书在 §3.3 内部回指 §3.3，读来像笔误（应为 §3.1 或“上面”），但页图如此，译本照录，未改。
4. **编译状态**：本块私有构建（驱动文件 `work/build03b/main03b.tex`，含 ch00a–ch03d，避开他人正在改动的 ch04）
   `file:line=chunks/ch03b.tex:1-276 fatal=0 undefined=0 missingchar=0 overfull=0`，68 页，LuaHBTeX 1.25.7 两遍通过；本块成品位于 pp.48–52（页眉“3.3”）。
   全量 `main.tex` 当前编译被 **ch04.tex 未闭合的 `\begin{proof}`**（`! LaTeX Error: \begin{proof} on input line 192 ended by \end{document}`）阻断，与本块无关；
   另全量构建有 3 处 `Missing character: There is no α (U+03B1)`，来源为 `appendix_b.tex:15309` 与 `ch03a.tex:3369` 的裸希腊字母（非本块）。

## 6 与邻块的边界

- 本块**首句**（原书 p.549）：“In this section, starting from an exact fully faithful functor $F$, we construct an object $\cE$ of $\Db(M\times X)$; in the next section we shall prove that the functors $F$ and $\Phi_{\cE}$ are isomorphic.” → 译本第二段起句。§3.3 标题之前的内容（§3.2 末“这完成定理的证明”等）未收入本块。
- 本块**末句**（原书 p.555，命题 3.3.5）：“…and this $E$ is unique up to isomorphism.” → 译本以句号收尾。其后紧接 “3.4. Proof of the main theorem.”，本块止于该标题之前，未越界一句；`ch03c` 亦从该标题起译（已核）。
- 与 ch03a 的接缝：ch03a 末为 §3.2 的注 3.2.4（约定 $H^{i}(F(\cF))$ 仅在 $i\in[-a,0]$ 非零，$a$ 为正整数），本块直接从 §3.3 标题起，无重复译、无漏译。
- 页标记衔接：本块首标记 p.549（§3.3 标题所在的页），末标记 p.555；ch03b.txt 与 ch03a.txt 在 p.549、与 ch03c.txt 在 p.555 各有整页重叠，本块按句子锚点切（起于 §3.3 标题、止于命题 3.3.5 末句），故与两邻块不重复译、不缺页。
