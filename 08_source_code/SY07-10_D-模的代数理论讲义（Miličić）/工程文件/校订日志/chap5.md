# 第 V 章校订日志（chap5.tex，309 行）

## 0. 核对概况

- 英文页范围：`en_pages/p139.txt`–`p147.txt`（PDF 页 = 印刷页 + 6，即印刷 **133–141**）。任务书给到 `p148.txt`，但 **`p148.txt` 为 0 字节空文件**，第 V 章正文止于印刷 p.141（§6 末尾 6.3 定理），参考文献自 `p149.txt`（印刷 142）起，不属于本章。故 **309 行覆盖整章，无整段漏译**。
- 覆盖度检查：把 p139–p147 逐段与译文逐段对齐（章引言、§1–§6 每段、每条陈述与证明），无缺段、无跳过整页；节标题与原文一一对应（1 Holonomic D-modules / 2 Connections / 3 Preservation of holonomicity under direct images / 4 Classification of irreducible holonomic modules / 5 Local cohomology of holonomic modules / 6 Preservation under inverse images）。
- 条目数核对（与英文逐条对应，类型序列一致，共 17 条编号环境）：§1 三条（1.1 Thm / 1.2 Lem / 1.3 Thm）；§2 两条（2.1 Thm / 2.2 Cor）；§3 四条（3.1 Thm / 3.2 Prop / 3.3 Prop / 3.4 Thm）；§4 四条（4.1 Lem / 4.2 Cor / 4.3 Prop / 4.4 Thm）；§5 一条（5.1 Lem）；§6 三条（6.1 Lem / 6.2 Lem / 6.3 Thm）。环境计数自检：theorem 7、lemma 5、proposition 3、corollary 2、proof 11、tikzcd 3、enumerate 7，`\begin`/`\end` 各 38，全部配对；`\label` 17 个，与编号环境数一致。
- 公式逐符号核对：引理 1.2 的 $\operatorname{holdef}_x(\mathcal{V})=\operatorname{holdef}_x(i_+(\mathcal{V}))$；定理 2.1 证明中 $T s_i=\sum_j a^i_js_j$ 与 $0=\sum_i(T(g_i)+\sum_j a_i^jg_j)s_i$ 的指标约定（$a^i_j$ 上标=输入、下标=输出，全段自洽）；矩阵 $A_i$、$D_is_j=\sum_kA^i_{kj}s_k$、$\Psi^{-1}D_i\Psi=D_i+A_i$、曲率方程 $D_j(A_i)-D_i(A_j)=[A_i,A_j]$；$L^p\Phi_+\circ i_{X,+}=i_{Y,+}\circ L^p\varphi_+$（$p\in-\mathbb{Z}_+$）；$H^p(\varphi_+(\mathcal{D}(\mathcal{V})))$；$\operatorname{supp}(I/L)\subset\bar V-V$；三角 $R\Gamma_Y\to\mathcal{V}^\cdot\to Rj_\bullet(\mathcal{V}^\cdot|_U)\to[1]$；$p_+(\mathcal{V}^\cdot)=\mathcal{O}_X\boxtimes\mathcal{V}^\cdot$。除下表所列外，上下标、系数、指标范围、$\mathcal{D}$ 与 $D$、维数加减均与原文一致。
- 术语全章扫描：`holonomic`/`Holonomic` 原 75 处 → 全部改「完整」（现全章仅 L7 括注保留拉丁词）；`正像` 原 7 处 → 0 处（全改「直像」，`直像` 现 7 处）；`完整性`、`特征簇`、`好滤过`、`闭浸入`、`局部上同调`、`凝聚`、`不可约`、`联络` 均合表；人名（Kashiwara、Hilbert、Nakayama、Čech）保留拉丁字母。无一字未译的英文整句，无 `\footnote`。
- 以下改动均为最小编辑：只改 `chap5.tex`，未改文风、未增补原文没有的数学内容、未用 `annote`、未新增 `\label`/`\ref`、未动 `main.tex`。备份在 `chap5.tex.bak`。

## 1. 改动清单

| 位置 | 原文（英文，截 60 字内） | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| chap5.tex:1 / 印刷 p.133 | Holonomic D-modules（章题） | `\chapter{Holonomic D-模}` | `\chapter{完整 D-模}` | 术语表：holonomic → 完整 | P2 |
| chap5.tex:7 / 印刷 p.133 | we call a coherent DX-module holonomic if | 是\emph{holonomic 的}（或\emph{完整}的） | 是\emph{完整（holonomic）的} | 术语表要求每章首次出现作「完整（holonomic）」；原译以「或」并列两名，等于给出两个术语，与统一后的用法冲突 | P2 |
| chap5.tex:10,12,19,20,38,39,53,57(×4),62,115,141,163(×4),166,168,172,175(×3),176,179,184,191,192,198(×2),202,205,207,210,218,221,224,228,238(×2),250,254,265,270,274,279,284,291,296,302,308 等（共 75 处） | holonomic / Holonomic | 完整（原为英文原词或「完整」混用） | 完整 | 术语表：holonomic → 完整；同章内不得混用拉丁词 | P2 |
| chap5.tex:133,135,137,146,148,234,238 / 印刷 p.135–139 | preservation of holonomicity under direct images；the direct image functor | §3 标题「完整性与正像」；「正像」「相应正像函子」 | 「完整性与直像」；「直像」 | 术语表：direct image → 直像（本章「正像」全部改「直像」） | P2 |
| chap5.tex:57 / 印刷 p.134 | Since by II.2.8 being of finite length is a local property | 由于由 II.2.8，为有限长度是局部性质 | 由于由 III.2.8，为有限长度是局部性质 | 引用指错：II.2.8（印刷 p.73）是「光滑代数簇的不可约分支即连通分支」的命题；「有限长度是局部性质」是**章 III §2 的 2.8 Lemma**（印刷 p.82：(i)(ii)(iii) 等价）。原文亦误作 II.2.8，见 §2 第 2 条 | P2 |
| chap5.tex:83 / 印刷 p.134 | Since, by 3.8, it projects onto supp(V) | 由于由 3.8 它投射到 $\operatorname{supp}(\mathcal{V})$ 上 | 由于由 III.3.9 它投射到… | 引用指错：本章无 3.8（原文缺章号）；「$\operatorname{Ch}$ 投射到 $\operatorname{supp}$ 上」是**章 III §3 的 3.9 Theorem**（$\pi(\operatorname{Ch}(V))=\operatorname{supp}(V)$，印刷 p.86）；III.3.8 是「特征簇是锥形子簇」，不足以得出该句 | P2 |
| chap5.tex:119 / 印刷 p.136 | there exist q×q-matrices Ai = (Aijk), … such that Di sj = Σk Aikj sk | 则存在 $q\times q$ 矩阵 $A_i=(A^i_{jk})$ | $A_i=(A^i_{kj})$ | 指标自相矛盾：紧随的定义式与下两行末式都要求 $A_i$ 的元素为 $A^i_{kj}$（行=输出 $k$、列=输入 $j$），否则 $\Psi^{-1}D_i\Psi=D_i+A_i$ 不成立。原文声明的 $(A^i_{jk})$ 系笔误，见 §2 第 3 条 | P1 |
| chap5.tex:123 / 印刷 p.136 | = Σj Di(fj)sj + Σk (Σj fj Aikj) sk | $$=\sum_{j=1}^qD_i(f_j)s_j+\sum_{j=1}^qf_jA^i_{kj}s_k | $$=\sum_{j=1}^qD_i(f_j)s_j+\sum_{j,k=1}^qf_jA^i_{kj}s_k | 原文只对 $j$ 求和，而被加项 $f_jA^i_{kj}s_k$ 中 $k$ 是自由的，等式两边不合法；须对 $j,k$ 双重求和才能化到下一行的单项和 | P1 |
| chap5.tex:148 / 印刷 p.135 | between MR(DX) (resp MR(DY)) and MR(D(n)) (resp MR(D(m))) | 与 $\mathcal{M}_R(D^{(n)})$（相应地 $\mathcal{M}_R(D^{(n)})$） | （相应地 $\mathcal{M}_R(D^{(m)})$） | 第二个对应的是 $D_Y$，而 $i_Y:Y\to k^m$，应为 $D^{(m)}$；原译复制了第一个 | P1 |
| chap5.tex:184–185 / 印刷 p.144 | Let V be a holonomic module on X, C·(U,V) its Čech resolution | 设 $\mathcal{U}$ 是 $X$ 上 holonomic 模，$C^\cdot(\mathcal{U},\mathcal{U})$ 是其 Čech 分解 | 设 $\mathcal{V}$ 是 $X$ 上完整模，$C^\cdot(\mathcal{U},\mathcal{V})$ 是其 Čech 分解 | 原文 $U$ 兼表仿射开覆盖与模（同处冲突），照译使「$C^\cdot(\mathcal{U},\mathcal{U})$」无意义；据 3.2 证明首句（$X$ 上完整模 $\mathcal{V}$）与 3.3 陈述恢复为 $\mathcal{V}$ | P1 |
| chap5.tex:218 / 印刷 p.146 | i.e. W is the unique irreducible DX-submodule of V | 即 $\mathcal{W}$ 是 $\mathcal{V}$ 的唯一不可约 $\mathcal{D}_X$-子模 | 即 $\mathcal{W}$ 是 $i_\bullet(\mathcal{V})$ 的唯一不可约 $\mathcal{D}_X$-子模 | 本段讨论的对象自始至终是 $i_\bullet(\mathcal{V})$ 的不可约子模；照原文写成「$\mathcal{V}$ 的唯一不可约子模」则与上句「$\mathcal{W}$ 是 $i_\bullet(\mathcal{V})$ 的不可约子模」矛盾，也使 4.1(ii) 中「$\mathcal{W}$ 在 $U$ 上的限制等于 $\mathcal{V}$」这一结论失去对象。原文笔误，见 §2 第 4 条 | P1 |
| chap5.tex:234,236,237,238,241,245,246,247,254,255,257,258,265,266 / 印刷 p.138–139 | Let V be a connected smooth subvariety of X, j : V → X …（子簇 V 与模 V 在原文以正体/花体区分） | 子簇与模都写作 $\mathcal{V}$：如「存在 $\mathcal{V}$ 的支集中的不可约开光滑仿射子簇 $\mathcal{V}$ 及 $\mathcal{V}$ 上不可约联络 $\tau$」、「使得 $\mathcal{V}=\operatorname{supp}(\mathcal{V})\cap U$ 是 $U$ 的闭光滑子簇」 | 子簇统一作 $V$、$V'$、$V''$、$\bar V$、$j_V$、$\mathcal{D}_V$、$I(V,\tau)$、$L(V,\tau)$；模仍作 $\mathcal{V}$、$i_\bullet(\mathcal{V})$、$\mathcal{W}$。如「存在 $\mathcal{V}$ 的支集中的不可约开光滑仿射子簇 $V$ 及 $V$ 上不可约联络 $\tau$」、「使得 $V=\operatorname{supp}(\mathcal{V})\cap U$ 是 $U$ 的闭光滑子簇」 | 原译把斜体 $V$（子簇）与花体 $\mathcal{V}$（模）并作一个符号，§4 的核心对象因此串味：$V=\operatorname{supp}(\mathcal{V})\cap U$ 一式中「模等于自身支集与开集之交」，4.4(i)(ii) 的陈述与证明随之失去可读性；$j_V$、$\mathcal{D}_V$ 更无从表意 | P1 |
| chap5.tex:299 / 印刷 p.141 | Hence, + : Mqc(DY) → Mqc(DX×Y) is an exact functor | 因此，$+:\mathcal{M}_{qc}(\mathcal{D}_Y)\to\dots$ | 因此，$p_+:\mathcal{M}_{qc}(\mathcal{D}_Y)\to\dots$ | 上一句正说 $p_+$；pdftotext 丢了字母 $p$，函数名悬空 | P1 |
| chap5.tex:308 / 印刷 p.141 | Let F : X −→ Y be a morphism … the inverse image functor Lf + | 设 $F:X\to Y$ 是光滑代数簇的态射。则逆像函子 $Lf^+$ | 设 $f:X\to Y$ 是… | 原文同一句内 $F$ 与 $f$ 不一致（$Lf^+$ 只能配 $f$）；统一为 $f$ | P2 |
| chap5.tex:多处（L10、53、62、115、163×3、168、172、191、192、198、207、210、218、224、228、238、254、265、274、284、291、296、302、308 等及 L266 的 $\cap V'$） | — | 术语替换后「完整$\mathcal{D}_X$」「完整$D^{(n)}$」「\capV」等 | 「完整 $\mathcal{D}_X$」「完整 $D^{(n)}$」「\cap V」 | 术语统一时被替换词与行内公式/控制序列粘连，补空格（纯排版） | P3 |

## 2. 原文笔误（按方案铁律：译文正确者不动，只登记；译文照抄笔误者另注处理）

| # | 位置 | 原文（英文） | 译文 / 处理 | 说明 |
|---|---|---|---|---|
| 1 | 印刷 p.133（p139 1.1(ii)） | if V1 and V2 are holonomic, V2 is holonomic | 译文作「若 $\mathcal{V}_1$ 与 $\mathcal{V}_3$ 是完整的，则 $\mathcal{V}_2$ 是完整的」，正确，不改 | 正合列 $0\to V_1\to V_2\to V_3\to0$ 中，「两端完整 ⇒ 中间完整」的第二端只能是 $V_3$；同条 (i) 亦作 $V_1$、$V_3$ |
| 2 | 印刷 p.134（p140 1.3 证明） | Since by II.2.8 being of finite length is a local property | 已按 III.2.8 改（§1 第 5 行） | II.2.8 是「不可约分支=连通分支」；「有限长度是局部性质」是 III.2.8 Lemma |
| 3 | 印刷 p.134（p140 2.1 证明） | Since, by 3.8, it projects onto supp(V) | 已按 III.3.9 改（§1 第 6 行） | 缺章号且编号有误；所需结论是 III.3.9 |
| 4 | 印刷 p.136（p142） | Ai = (Aijk) 与 Di sj = Σk Aikj sk 并存 | 已按 $A_i=(A^i_{kj})$ 统一（§1 第 7 行） | 两式指标不自洽：$(A^i_{jk})$ 与下两行末式的 $A^i_{jk}$ 是同一约定，则 $D_is_j$ 应作 $\sum_kA^i_{jk}s_k$；反之亦然。取与 $\Psi^{-1}D_i\Psi=D_i+A_i$ 相容的一种 |
| 5 | 印刷 p.138（p145 4.3） | the support of I(Q, τ )/L(Q, τ ) is contained in V̄ − V | 译文作 $I(V,\tau)/L(V,\tau)$，正确，不改 | 本段对象是附属于 $(V,\tau)$ 的标准模 $I(V,\tau)$ 与其不可约子模 $L(V,\tau)$，$Q$ 系 $V$ 之误 |
| 6 | 印刷 p.141（p147 6.2 前） | Hence, + : Mqc (DY ) −→ Mqc (DX×Y ) is an exact functor | 已按 $p_+$ 改（§1 第 13 行） | 缺 $p$ |
| 7 | 印刷 p.141（p147 6.3） | Let F : X −→ Y … the inverse image functor Lf + | 已按 $f:X\to Y$ 改（§1 第 14 行） | 同句 $F$/$f$ 不一致 |
| 8 | 印刷 p.141（p147 6.3） | generailzes ?? | 译文作「推广前述结论」，不改 | 拼写错误 + 引用空缺 |
| 9 | 印刷 p.141（p147 6.1 前后） | Li_+(V · ) is a bounded complex of holonomic DY-modules | 译文照译「$Li_+(\mathcal{V}^\cdot)$ 是 $\mathcal{D}_Y$-模的有界完整复形」，不改 | $Li_+:D_Y\to D_X$，作用在 $X$ 上的 $\mathcal{V}^\cdot$ 得不出 $D_Y$-复形；原文疑脱 $Ri^!$（应为 $Li_+(Ri^!(\mathcal{V}^\cdot))$ 或纯属笔误）。照译，另见 §4 第 5 条 |

## 3. 保留不改

| 位置 | 原文（英文） | 译文 | 处理 | 说明 |
|---|---|---|---|---|
| chap5.tex:184 / 印刷 p.144 | its Čech resolution | 「Čech 分解」 | 不改 | 全书统一用「分解」表 resolution（chap3.tex:364、chap4 同），改「消解」会与既有译法冲突 |
| chap5.tex:274 / 印刷 p.140 | distinguished triangle | 「可区别三角」 | 不改 | chap4 同一译法（chap4.tex:1222），保持全书一致 |
| chap5.tex:148 / 印刷 p.135 | By abuse of notation | 「借由记号上的滥用」 | 不改 | 译者的行文处理，语义无误，属文风问题 |
| chap5.tex:124 / 印刷 p.136 | = Σj (Di(fj) + Σk fk Aijk) sj | 同（$\sum_k f_kA^i_{jk}$） | 不改 | 与 L119 起的约定（$A^i_{kj}$：行=输出、列=输入）自洽：系数 $s_j$ 为 $\sum_k f_kA^i_{jk}$。校订中曾误改为 $A^i_{kj}$，已回退 |
| chap5.tex:33 / 印刷 p.133 | Hol(DX) is an abelian thick subcategory | 「$\operatorname{Hol}(\mathcal{D}_X)$ 是 Abel 的且是厚的」 | 不改 | 与原文一致；全章 abelian、thick 的处理同 |

## 4. 存疑

1. **chap5.tex:5 / 印刷 p.133**：原文 "We proved in ?? that for any point x in supp(V), dim..."，引用编号被 pdftotext 吞掉；译文作「我们已证明」，无法核对所指，保留。
2. **chap5.tex:8 / 印刷 p.133**：原文 "This generalizes the definition from ??"（指第 I 章特征簇/完整性的旧定义）；译文作「这推广了前述定义」，空缺无法核对。
3. **chap5.tex:50 / 印刷 p.133**：原文 "The next result generalizes ??"；译文作「下一个结果推广了前述结论」，保留。
4. **chap5.tex:169,185,202 / 印刷 p.143–144 与 L305 / p.141**：原文 "[2, ??]"、"Čech resolution [3, ?]"、"by ?? results"、"using ??" 等参考文献编号与交叉引用空缺；译文分别作「[2]」「称其为 Čech 分解」「由相关结果」「使用前述」「推广前述结论」，均无法核对，保留待主控统一处理。
5. **chap5.tex:291 / 印刷 p.141**：「这进而蕴含 $Li_+(\mathcal{V}^\cdot)$ 是 $\mathcal{D}_Y$-模的有界完整复形」照原文译出，但 $Li_+:D_Y\to D_X$ 与结论中的 $\mathcal{D}_Y$ 不相容（见 §2 第 9 条）。若主控确认原文脱漏，可改为 $Li_+(Ri^!(\mathcal{V}^\cdot))$；本轮不动。
6. **chap5.tex:166 / 印刷 p.143**：原文 "By localizing ??"（定理 3.1 的局部化），编号空缺；译文作「对定理 \ref{thm:5.3.1} 局部化可见」，所指明确，保留。

## 5. 统计

- **P1：7 条**（chap5.tex:119、123、148、184–185、218、234–266 的 $V$／$\mathcal{V}$ 符号分流、299）
- **P2：7 条**（chap5.tex:1、7、57、83、308；另两项为全章术语统一：75 处 holonomic→完整、7 处正像→直像）
- **P3：1 条**（术语替换后的空格粘连，纯排版）
- **存疑：6 条**（原书/pdftotext 的引用编号空缺 5 条，$Li_+$ 与 $\mathcal{D}_Y$ 不相容 1 条）
- **原文笔误：9 条**（已登记，其中 5 条按正确数学内容改，4 条照译不改）
