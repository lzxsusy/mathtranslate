# c16 / c17 校勘报告（原书 p.195–223 = PDF p.202–230）

校勘者：tr-ch2c　日期：2026-11-14
范围：`源码/chunks/c16.tex`（§2.5，15 条 2.5.1–2.5.15）、`源码/chunks/c17.tex`（§2.6，10 条 2.6.1–2.6.10）
方法：页面图像 `工程文件/pages/p202.png`–`p230.png` 为唯一依据（局部放大 3–4 倍核符号），OCR 仅用于定位。只查数学，未改动他人文件。

## 结论

**未发现实质数学错误**（0 处）。条文编号、编号类型、关键证明链、交换图、接缝均与原书一致；6 条译注所指的原书排印问题**全部属实**（已回图放大核实）。

但发现 **2 处需要修正的非数学问题**（1 条译注与正文自相矛盾；2 个文件头页范围少写一页），另有 3 条可选改进建议。逐条见下。

## 一、问题清单

格式：位置（原书页 + 文件行号）｜原书｜译文｜建议

### P1（建议修）译注与正文自相矛盾 —— `c17.tex:443` 与 `c17.tex:468–470`（原书 p.220 = PDF p.227）

- 原书（p.227，已放大核实）：`This implies that $H^i(X,\mathcal F\otimes M)\to H^i(X,\mathcal F\otimes_A M')$ is surjective.`（第一处 $\otimes$ 无下标 $A$，目标为 $M'$，与上一行交换图不符，应为 $M''$。）
- 译文正文（c17.tex:443）：`这说明 $H^i(X,\cF\tensor_A M)\to H^i(X,\cF\tensor_A M'')$ 是满射。` —— **已按正确数学写作 $M''$**。
- 但译注（c17.tex:468–470）写：「…按上下文应为 …$M''$…；**译文保留原书排印**。」——与正文实际写法不符。
- 建议：二选一。① 按 STYLE_GUIDE 第 9 条「照译＋译注指出」，把正文改回 `\cF\tensor_A M'`（第一处 $\otimes$ 亦按原书作 `\tensor`）；② 保留正文的正确写法，把译注末句改为「译文此处按上下文写作 $M''$，原书作 $M'$」。**本条不影响数学正确性，属一致性问题。**

### P2（建议修）文件头页范围各少一页 —— `c16.tex:1`、`c17.tex:1`

- 原书实际：2.5.15 的证明从 p.209 跨到 **p.210 顶部**（PDF p.217，OCR/图像均确认「…and hence $f$ is injective. □」在 p.217），其后同页紧接 §2.6 标题。
- `c16.tex:1` 写 `% c16 原书 p.195–209（PDF p.202–216）`，实际含 p.210 顶部约 20 行 → 应为 `p.195–210（PDF p.202–217）`。
- `c17.tex:1` 写 `% c17 原书 p.210–222（PDF p.217–229）`，实际 2.6.10 的证明（(ii)(iii)）延续到 **p.223 顶部**（PDF p.230，□ 在其上），其后同页接 §2.7 → 应为 `p.210–223（PDF p.217–230）`。
- 建议：只改注释，正文不动（正文内容与页边界完全正确，见「三、接缝」）。

### P3（可选）原书笔误照录但未加译注 —— `c16.tex:119`（原书 p.199 = PDF p.206）

- 原书（p.206，图像核实）：`So $j^*\mathcal G' = \mathcal G|_U$.` —— 此处 $\mathcal G$ 尚未定义（$\mathcal G$ 是本引理要构造的整体子模，下段才出现），按上下文应为 $j^*\mathcal G'=\mathcal G_U$。
- 译文照录 `$j^*\cG'=\cG|_U$`（忠实，无错），但未加译注，读者易误以为 $\cG$ 已定义。
- 建议：可加半句译注（本条不计入 3 条译注亦可；若加，建议并入现有 p.197 译注或另立一条并注明「原书 p.199」）。

### P4（措辞建议）`c16.tex:38`（原书 p.197）

- 原书：`Let $\mathcal O_{Z'}(1)$ be an invertible $\mathcal O_{Z'}$-module very ample over $Z$.`
- 译文：「令 $\cO_{Z'}(1)$ 为 **$Z$ 上**极丰沛的可逆 $\cO_{Z'}$-模。」
- 译法正确（`over Z` 指相对 $Z$ 极丰沛 / $g\colon Z'\to Z$ 的丰沛），只是「$Z$ 上」易被读成「$Z$ 上的层」。建议改「**关于 $Z$ 极丰沛**」。

### P5（可选）`c17.tex:120`（原书 p.213 = PDF p.220）

- 原书（p.220，图像核实）：`$H^i(X\times_Y\Spec B,\mathcal F\otimes_A B)\cong H^i(K\otimes_A B)$` —— 原书即印 $K$（无上标 $\cdot$），译文照录 `$H^i(K\tensor_A B)$`（忠实，无错），但同一命题上一行写 $K^\cdot$，读者可能停顿。
- 建议：不改（照录原书）；若求统一可加极短译注。

> 附：`c16.tex:302` 的 `$\alpha_{k_0}(S_{k_0})Q=0$` 中 $Q$ 未定义，**原书 p.203 亦如此排印**（已回图核实），译文忠实，不必改。`c16.tex:60` 的 $\cO_{Z'}(n)$ 确系原书 p.197 排印（译注 1 属实）。

## 二、编号与类型核对（25 条，全部一致）

依据：页面图像 + `_check_c16.aux`/`_check_c17.aux` 的 `\newlabel`（编号由计数器自动生成，无手写）。

| 原书 | 类型（原书/译文） | 页（原书） | label |
|---|---|---|---|
| 2.5.1 | Theorem / theorem | 195 | it:2.5.1 |
| 2.5.2 | Lemma / lemma | 198 | it:2.5.2 |
| 2.5.3 | Corollary (Finiteness Theorem) / corollary[有限性定理] | 199 | it:2.5.3 |
| 2.5.4 | Corollary / corollary | 199 | it:2.5.4 |
| 2.5.5 | Lemma / lemma | 200 | it:2.5.5 |
| 2.5.6 | Theorem / theorem | 201 | it:2.5.6 |
| 2.5.7 | Lemma / lemma | 202 | it:2.5.7 |
| 2.5.8 | Lemma / lemma | 203 | it:2.5.8 |
| 2.5.9 | Corollary / corollary | 203 | it:2.5.9 |
| 2.5.10 | Theorem (Theorem of Connectedness) / theorem[连通性定理] | 204 | it:2.5.10 |
| 2.5.11 | Lemma / lemma | 206 | it:2.5.11 |
| 2.5.12 | Proposition / proposition | 206 | it:2.5.12 |
| 2.5.13 | Proposition / proposition | 207 | it:2.5.13 |
| 2.5.14 | Theorem (Zariski Main Theorem) / theorem[Zariski 主定理] | 208 | it:2.5.14 |
| 2.5.15 | Corollary / corollary | 208 | it:2.5.15 |
| 2.6.1 | Lemma / lemma | 211 | it:2.6.1 |
| 2.6.2 | Lemma / lemma | 212 | it:2.6.2 |
| 2.6.3 | Lemma / lemma | 212 | it:2.6.3 |
| 2.6.4 | Proposition / proposition | 213 | it:2.6.4 |
| 2.6.5 | Theorem (Semicontinuity Theorem) / theorem[上半连续性定理] | 214 | it:2.6.5 |
| 2.6.6 | Theorem / theorem | 215 | it:2.6.6 |
| 2.6.7 | Lemma / lemma | 217 | it:2.6.7 |
| 2.6.8 | Proposition / proposition | 218 | it:2.6.8 |
| 2.6.9 | Theorem / theorem | 221 | it:2.6.9 |
| 2.6.10 | Corollary / corollary | 222 | it:2.6.10 |

- 原书 p.195–223 区间内**没有** Definition / Example / Remark / Construction 类编号条目（OCR 全量 grep `Definition 2.` 无命中），无漏译条目。
- 小标题：原书 2.5.14「Zariski Main Theorem」、2.5.10「Theorem of Connectedness」、2.6.5「Semicontinuity Theorem」、2.5.3「Finiteness Theorem」的括注均已保留。
- 习题：§2.5、§2.6 原书**无习题**（§2.4 的习题止于 p.195 顶部，属 c15/c16 接缝，已由 c16 注释说明跳过）。

## 三、接缝核对（p.209/p.210，PDF p.216/p.217）

- c16 末尾：2.5.15 证明的后半（从「设 $U_i$（$i=1,2$）是 $x_i$ 的仿射开邻域…」到 `...故 $x_1=x_2=x$，从而 $f$ 是单射。` + □），与 p.216 末行、p.217 整页文字**逐句对应，无遗漏、无重复**。
- c17 开头：`\subsection{高阶直接像的局部自由性}` + 引言段（flat over Y 定义、X_y、F_y、本节目标），与 p.217 下半页 §2.6 标题及正文**逐句对应**。
- 两文件之间**没有**同一句被写两遍，也**没有**整句丢失。c16 的 `% 起始页 p.202 顶部为 §2.4 习题…按接缝规则跳过` 注释与 c15 报告所述一致（p.195 顶部习题 (1)–(4) 归 c15）。

## 四、关键证明链逐符号核对（回图核实，共 30 条）

「图」= 已放大核对页面图像；「文」= 与原文逐句比对（同一页已整体核对）。

**c16**

1.（图 p202）2.5.1 陈述：`R^nf_*\cF` 凝聚，对每个凝聚 $\cO_X$-模与每个 $n$。
2.（图 p203）2.5.1 证：$R^p(fi)_*R^qg_*\cO_{Z'}(k)\Rightarrow R^{p+q}(fig)_*\cO_{Z'}(k)$（双正则谱序列退化）。
3.（图 p203）$R^n(fi)_*(g_*\cO_{Z'}(k))\cong R^n(fig)_*\cO_{Z'}(k)$。
4.（图 p203）$R^nf_*(i_*g_*\cO_{Z'}(k))\cong R^n(fi)_*(g_*\cO_{Z'}(k))$。
5.（图 p204）$\phi_z\colon(g_*\cO_{Z'}(k))_z^m\cong\cG_z$；$\phi_V\colon(i_*g_*\cO_{Z'}(k))^m|_V\cong i_*\cG|_V$。
6.（图 p204）图态射 $(i_*g_*\cO_{Z'}(n))^m|_V\to\bigl((i_*g_*\cO_{Z'}(k))^m\oplus i_*\cG\bigr)|_V,\ s\mapsto(s,\phi_V(s))$ —— **原书确实印 $n$**（译注 1 属实）。
7.（图 p206）2.5.2 证：$j^*\cG'$ 是 $j^*j_*\cG_U=\cG_U$ 在 $j^*\cF\to j^*(j_*j^*\cF)=j^*\cF$ 下的原像；$j^*\cG'=\cG|_U$（原书如此，见 P3）。
8.（图 p208）2.5.5：$\bigoplus_k I^k\cF$ 是 $\bigoplus_k f^*((I^k)^\sim)$-模；$g'_*\cF'\cong\bigoplus_k I^k\cF$；$\HH^n(X',\cF')\cong\HH^n(X,g'_*\cF')\cong\bigoplus_k\HH^n(X,I^k\cF)$。
9.（图 p208）2.5.6 陈述：$(\HH^n(X,\cF))^{\wedge}\cong\dlim_k\HH^n(X,\cF/I^k\cF)$。
10.（图 p208）2.5.6 证：$I^k\HH^n(X,\cF/I^k\cF)=0$；长正合列 $\HH^n(X,I^k\cF)\to\HH^n(X,\cF)\to\HH^n(X,\cF/I^k\cF)\to\HH^{n+1}(X,I^k\cF)$。
11.（图 p208）$R_k=\operatorname{im}(\HH^n(X,I^k\cF)\to\HH^n(X,\cF))$，$Q_k=\ker(\HH^{n+1}(X,I^k\cF)\to\HH^{n+1}(X,\cF))=\operatorname{im}(\HH^n(X,\cF/I^k\cF)\to\HH^{n+1}(X,I^k\cF))$。
12.（图 p209）$0\to\HH^n(X,\cF)/R_k\to\HH^n(X,\cF/I^k\cF)\to Q_k\to0$；取逆向极限后 $\dlim\HH^n/R_k\cong(\HH^n)^{\wedge}$、$\dlim Q_k=0$。
13.（图 p209）2.5.7：交换图 $I^k\cF\xrightarrow{a}I^{k+l}\cF$ 与 $\cF\xrightarrow{a}\cF$；$I^lR_k\subset R_{k+l}$；$R_k=I^{k-k_0}R_{k_0}\subset I^{k-k_0}\HH^n(X,\cF)$；$I^k\HH^n(X,\cF)=I^kR_0\subset R_k$。
14.（图 p210）2.5.8：$\alpha_k(S_k)Q_k=0$；$\alpha_{k_0}(S_{k_0})x_i=0$；$\alpha_{k_0}(S_{k_0})Q=0$（原书亦印 $Q$）；$Q_{k+k_0}=S_{k_0}Q_k$；三列交换图。
15.（图 p210）2.5.9 陈述：$\dlim_k R^nf_*\cF/\mathcal I^kR^nf_*\cF\cong\dlim_k R^nf_*(\cF/\mathcal I^k\cF)$。
16.（图 p211）2.5.10 笛卡尔图 $X_k=X\times_Y\Spec\cO_{Y,y}/\fm_y^k\xrightarrow{i_k}X'=X\times_Y\Spec\cO_{Y,y}\xrightarrow{i}X$（下排 $\Spec\cO_{Y,y}/\fm_y^k\to\Spec\cO_{Y,y}\xrightarrow{j}Y$）；$f'_*\cO_{X'}\cong j^*\cO_Y\cong\cO_{\Spec\cO_{Y,y}}$。
17.（图 p212）$\dlim_k\HH^0(X_k,\cO_{X_k})\cong\hat\cO_{Y,y}$；$(1,0)+(0,1)=1$ 而两者均非单位的矛盾论证。
18.（图 p212）Stein 分解段：$g_*\cO_{Y'}\cong f_*\cO_X$；$f'^\sharp$ 同构 ⇒ $f'$ 纤维连通；拟有限定义。
19.（图 p216）2.5.15 证：$A[x_0,\dots,x_m]_{(x_0)}\to A[x_1,\dots,x_m],\ x_i/x_0\mapsto x_i$；$\Spec A[x_1,\dots,x_m]\cong D_+(x_0)\to\bP^m_A$（译注 3 属实）。
20.（图 p216）$\cO_{X,x_i}=\dlim_{x_i\in U}\cO_X(U)\to\cO_{X,\xi}$ 单射；交换图 $\cO_{Y,y}\to\cO_{Y,\eta}$、$\cO_{X,x_i}\to\cO_{X,\xi}$。
21.（图 p217）$\cO_X(U_1\cap U_2)\subset\cO_{X,x_1}=\cO_{X,x_2}$ 与两张菱形交换图；$\fm_x\cap\cO_X(U_1\cap U_2)$ 对应点 $x$，$\fm_x\cap\cO_X(U_i)$ 对应 $x_i$ ⇒ $x_1=x_2$。

**c17**

22.（图 p219）2.6.2 证：$\cdots\to K^{-1}\to K^0\to K^0/B^0(K^\cdot)\to0$；$\Tor_i^A(K^0/B^0(K^\cdot),M)\cong H^{-i}(K^\cdot\tensor_AM)$；$H^{-i}(K^\cdot\tensor M)\cong H^{-i}(C^\cdot\tensor M)$。
23.（图 p219）2.6.3 证：$A=\{(c,k)\in C^p\oplus Z^{p+1}(K^\cdot)\mid c,k\ \text{在}\ Z^{p+1}(C^\cdot)\ \text{中同像}\}$；$\coker\alpha\to H^{p+1}(C^\cdot)$ 单且满 ⇒ 同构；$\ker\alpha\cong Z^p(C^\cdot)$；$H^{p+1}(K^\cdot)\cong\coker(\alpha\gamma)\cong\coker\alpha\cong H^{p+1}(C^\cdot)$。
24.（图 p220）2.6.4 陈述：$\HH^i(X,\cF\tensor_AM)\cong\HH^i(K^\cdot\tensor_AM)$；$\HH^i(X\times_Y\Spec B,\cF\tensor_AB)\cong\HH^i(K\tensor_AB)$（原书印 $K$）；$\HH^i(X_y,\cF_y)\cong\HH^i(K^\cdot\tensor_Ak(y))$。
25.（图 p221）$C'^i(\fU,\cF\tensor_AM)=C^i\tensor_AM$；$C'^\cdot(\fU',\cF\tensor_AB)=C^\cdot\tensor_AB$；$\HH^i(X\times_Y\Spec B,\cF\tensor_AB)\cong\HH^i(C^\cdot\tensor_AM)$（**原书印 $M$，译注“原书 p.214”属实**）。
26.（图 p222）$\chi(X_y,\cF_y)=\sum_i(-1)^i\dim_{k(y)}(K^i\tensor_Ak(y))$；$\{y\mid\dim_{k(y)}\operatorname{im}(d^i\tensor\id_{k(y)})\le r\}=V(\fa)$，$\fa$ 由 $(r+1)\times(r+1)$ 阶子式生成。
27.（图 p222）2.6.6 陈述与证明开头；$\dim\HH^i+\dim\operatorname{im}(d^{i-1})=\dim(K^i\tensor k(y))-\dim\operatorname{im}(d^i\tensor k(y))$。
28.（图 p227）2.6.8 (ii)⇒(iii) 交换图（两行 $M',M,M''$ 全同）；「两行正合、三竖箭头满射」⇒ 右正合。
29.（图 p229）2.6.9 证：$(R^if_*\cF)_y\cong\HH^i(X\times_Y\Spec\cO_{Y,y},p^*\cF)$；两函子右正合 ⇔ 两个标准同态满射；结论「$R^if_*\cF$ 局部自由 ⇔ $(R^{i-1})$ 那条满射」。
30.（图 p229–p230）2.6.10 陈述 (i)(ii)(iii) 与 (i) 证：$(\coker d^i)\tensor_Ak(y)$ 维数局部常值 ⇒ $\coker d^i$ 投射 ⇒ 短正合列分裂 ⇒ $(\ker d^i)\tensor_Ak(y)\cong\ker(d^i\tensor\id)$ ⇒ $\HH^i(K^\cdot)\tensor_Ak(y)\cong\HH^i(K^\cdot\tensor_Ak(y))$；$R^{-1}f_*\cF$ 平凡满射（译注 3 属实）。

## 五、交换图核对

- **c16 共 9 个 tikzcd**：2.5.5 笛卡尔图（p207）、2.5.7 两张方图（p209）、2.5.8 两张（p209–210，含 $\alpha_k(a)$ 那条）、2.5.10 双行笛卡尔图（p211）、2.5.15 三张（p216 一张、p217 两张）。形状、箭头方向、上下标与原书一致；2.5.8 原书用「弯箭头」标 $\alpha_k(a)$，译文排成第二段直箭头并加下标 $k$，**语义等价**，可接受。
- **c17 共 6 个 tikzcd**：2.6.2 复形态射图（p218）、2.6.3 $\alpha$ 图（p219）、2.6.6 $\HH^i(K^\cdot)\tensor k(y)$ 图（p223）、2.6.8 两张（p226、p227）、2.6.8 (iii)⇒(iv) 图（p227）。形状与箭头均与原书一致。
- 编译后目检（latex_look）：c16 p11（2.5.14/2.5.15 的分解箭头）、c17 p9（2.6.8 两张交换图 + 2.6.9）渲染正常，无溢出、无箭头错位。

## 六、译注核实（6 条全部属实）

| 文件 | 位置 | 主张 | 核实 |
|---|---|---|---|
| c16 | p.197（p204） | 图态射的 $\cO_{Z'}(n)$ 应为 $\cO_{Z'}(k)$ | 属实（放大见 $n$） |
| c16 | p.207（p214） | 原书 “The ring $A$ must an artinian…” 脱漏 be | 属实（原文即缺 be） |
| c16 | p.209（p215–216） | $D_+(x_0)$ 坐标简记为 $x_i$，右端应为 $A[x_i/x_0]$ | 属实（原书 $x_i/x_0\mapsto x_i$，$D_+(x_0)$ 写在下一行） |
| c17 | p.214（p221） | $\HH^i(X\times_Y\Spec B,\cF\tensor_AB)$ 右端应作 $C^\cdot\tensor_AB$，原书印 $M$ | 属实 |
| c17 | p.220（p227） | 原书 $M'$ 应为 $M''$；第一处 $\otimes$ 无下标 $A$ | 主张属实，**但“译文保留原书排印”与正文不符，见 P1** |
| c17 | p.222–223（p229–230） | $R^{-1}f_*\cF$ 取 $-1$ 阶直接像为 0，故平凡满射 | 属实（原文用 $R^{-1}$，未另解释） |

## 七、编译与排版

- `_check_c16.tex`：xelatex 3 遍，**0 error，12 页，0 Overfull/Underfull**。
- `_check_c17.tex`：xelatex 3 遍，**0 error，11 页，0 Overfull/Underfull**。
- 单块自检中 `??`（`it:2.4.9`、`it:1.4.14`、`it:2.1.19` 等）为跨块引用，主文件可解析，属预期。
- `_check_c16.tex`/`_check_c17.tex` 的 `\setcounter{subsection}{4}`/`{5}` 使自检 PDF 印「2.5/2.6」正确。

## 八、改动建议汇总（供 Lead 决定，我未改他人文件）

1. c17.tex:443 或 468–470 二者择一统一（P1）。
2. c16.tex:1、c17.tex:1 页范围注释各补一页（P2）。
3. 可选：c16.tex:119 加半句译注（P3）；c16.tex:38 改「关于 $Z$ 极丰沛」（P4）；c17.tex:120 加极短译注（P5）。

数学上**无需改动任何公式、编号或证明**。
