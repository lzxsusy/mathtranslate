# 第 II 章校订日志（chap2.tex，681 行）

## 0. 核对概况

- 英文页范围：`en_pages/p061.txt`–`p082.txt`（PDF 页 = 印刷页 + 6，印刷 55–76）。
- 条目数核对：§1 十六条（1.1 Lem … 1.16 Prop）、§2 十五条（2.1 Lem … 2.15 Lem）、§3 七条（3.1 Lem / 3.2 Thm / 3.3 Lem / 3.4 Lem / 3.5 Prop / 3.6 Prop / 3.7 Thm）；与英文逐条对应，条目类型序列一致，**无缺条、无漏译整段**。译文 681 行 ↔ 英文 22 页，二十一页内容皆有着落（末页 p082 仅 3.7 证明的三行，对应 chap2.tex:678–680）。
- 全部条目的陈述与证明逐句对过；全部展示公式（含 §2 的正合列、Vandermonde/Cramer 推导、P'(g(x)) 计算、§3 的符号映射公式）逐符号对过。
- 术语全章扫描：`正像` 0 处（chap2.tex:589 已用「直像层 $\pi_*(\mathcal{O}_{T^*(X)})$」）；`holonomic` 0 处；切层/切丛/余切丛/象征/支集/凝聚/正则/光滑/闭子集 均合表；人名 Noether、Cramer 保留拉丁字母。无残留英文整句。
- 以下改动均为最小编辑，未改文风、未增补数学内容、未使用 `annote`。

## 1. 改动清单

| 位置 | 原文（英文，截 60 字内） | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| chap2.tex:80 / 印刷 p.57 | By 1.3, there exists a differential operator S ∈ D(n) of order ≤ p | 由上一定理存在阶数 $\le p$ 的微分算子 $S\in D(n)$ | 由上一条引理存在阶数 $\le p$ 的微分算子 $S\in D(n)$ | 英文指 1.3，1.3 是 Lemma（"1.3. Lemma."），译文误作「定理」 | P3 |
| chap2.tex:164 / 印刷 p.60 | By 9, this is a sheaf of O_X-modules for left multiplication | 由层论的结果，这是左乘 $\mathcal{O}_X$-模的层 | 由 1.9，这是左乘 $\mathcal{O}_X$-模的层 | "By 9" 指本节条目 1.9（$\beta_f:D(X)_f\to D(X_f)$ 同构，正是主开集上粘接的依据），不是「层论的一般结果」；同页 p066:29「as well as 10」证明本节裸数字即本节条目号 | P2 |
| chap2.tex:188 / 印刷 p.60 | This result, as well as 10, is a special case of the following lemma | 此结果以及前面的结果是如下引理的特例 | 此结果以及 1.10 是如下引理的特例 | 英文点名「10」（即 1.10 命题），译文泛化为「前面的结果」，丢失引用 | P2 |
| chap2.tex:229 / 印刷 p.61 | (i) follows from 8, (ii) from 3. and (iii) from (ii) | (ii) 由 1.14 得出 | (ii) 由 1.3 得出 | 1.14 是「滤过 $F\mathcal{D}_X(U)$ 穷尽」，与 $F_p\mathcal{D}_X$ 的凝聚性无关；英文作「3.」，按本节裸数字惯例即 1.3。数学上更直接的依据是 1.4（$D_p(X)$ 有限生成），见存疑 2 | P2 |
| chap2.tex:616 / 印刷 p.74 | Since F_1 D_X = O_X ⊕ T_X by 1.15.(ii) | 由 1.15.(ii) 有 $F_1\mathcal{D}_X=\mathcal{O}_X\oplus\mathcal{T}_X$ | 由 1.16.(ii) 有 $F_1\mathcal{D}_X=\mathcal{O}_X\oplus\mathcal{T}_X$ | $F_1\mathcal{D}_X=\mathcal{O}_X\oplus\mathcal{T}_X$ 是 **1.16.(ii)**（p068:20）；1.15 是拟凝聚/凝聚性定理，其 (ii) 是「$F_p\mathcal{D}_X$ 凝聚」，并不给出该分解。英文原文即误引 1.15.(ii)，见下「原文笔误」 | P2 |
| chap2.tex:582 / 印刷 p.73 | we can assume by 2.10. that U is sufficiently small so that there exists a coordinate system | 由于断言是局部的，由前面的定理可设 $U$ 充分小，使得 $U$ 上存在坐标系 | 由于断言是局部的，由 2.10 可设 $U$ 充分小，使得 $U$ 上存在坐标系 | 英文点名 2.10（Lemma），译文泛化作「前面的定理」且条目类型错 | P3 |
| chap2.tex:648 / 印刷 p.75 | a coordinate system on U as in 2.10 | $(f_1,\dots,f_n;D_1,\dots,D_n)$ 是如前面定理中 $U$ 上的坐标系 | 是如 2.10 中 $U$ 上的坐标系 | 英文作「as in 2.10」，2.10 为 Lemma，译文作「定理」且未指名 | P3 |

## 2. 原文笔误（按方案铁律 4：译文正确者不动，只登记）

| 位置 | 原文（英文） | 译文 | 处理 | 说明 |
|---|---|---|---|---|
| 印刷 p.58（p064:7） | Since f_1 ∈ R(X_f) | $f^{-1}\in R(X_f)$ | 不改 | 上下文为 $f^nh\in r_f(R(X))$ 推出 $f^nS(h)=S(f^nh)=0$，须用 $f^{-1}$ 可逆；原文把 $f^{-1}$ 印成 $f_1$。译文正确 |
| 印刷 p.67（p073:35） | we conclude that r(J)_x = I_x | $J_x=I_x$ | 不改 | 同段 p073:45 作 $J_x=I_x$，$r$ 为衍字。译文正确 |
| 印刷 p.74（p080:33） | Since F_1 D_X = O_X ⊕ T_X by 1.15.(ii) | 由 1.15.(ii)（已改） | 改为 1.16.(ii) | 原文引错条目，正确出处是 1.16.(ii)。此项同时计入 P2 |

## 3. 保留不改（方案 §3「—」行：文风、译者对原书笔误的正当修正、译者行文习惯）

| 位置 | 原文（英文） | 译文 | 处理 | 说明 |
|---|---|---|---|---|
| chap2.tex:355 / 印刷 p.65 | First we claim that we can assume that g ∈ R(X) | 先断言可设 $g\in R(X)$（原文本处疑有笔误） | 不改 | 原文 p071:6 已取 $g\in R(X)$，此断言确为原文冗余，译者括注是对原文的正当说明 |
| chap2.tex:355,359 / 印刷 p.65 | S⁻¹R(X) = R(X) | …（此处指分式域）…（分式域） | 不改 | 原文此处 $R(X)$ 兼指分式域，译者括注为必要澄清 |
| chap2.tex:377 / 印刷 p.66 | generate a B-submodule of R(X) which contains R(X) | 因此 $\frac{g^i}{D}$ … 生成 $R(X)$ 的一个含 $R(X)$ 的 $B$-子模（此处按原文） | 不改 | 译文与原文逐字对应，括注为译者说明 |
| chap2.tex:118,421 / 印刷 p.57,67 | imbedded in some k^n as a closed subset | 作为闭子集嵌入某 $k^n$ / 嵌入某 $k^m$ | 不改 | 术语表「closed immersion→闭浸入」针对浸入态射；此处原文为 imbedded as a closed subset 的日常用法，非术语 |

## 4. 存疑

1. **chap2.tex:229 / 印刷 p.61**：英文「(i) follows from 8」的「8」若指 1.8（$\rho_f$ 为滤过环同态），配合 1.9 可说明 $\mathcal{D}_X$ 拟凝聚，尚说得通；译文作「由前述结果得出」未指名，保留原样，仅在此登记。
2. **chap2.tex:229 / 印刷 p.61**：英文「(ii) from 3.」——数学上给出 $F_p\mathcal{D}_X$ 凝聚的直接依据是 1.4 推论（$D_p(X)$ 是有限生成 $R(X)$-模），疑英文「3.」为「4.」之误。译文已按印刷原文改为 1.3；若主控判定原文应作 4，此条需再改。
3. **chap2.tex:89,234,566,568 / 印刷 p.56,62,73**：`I.8.9`、`I.8.2.(iii)`、`I.8`、`I.8.3` 与中译本第一章分节对不上——`chap1.tex:645` 的 §5 才是「多项式系数微分算子环」，而 `chap1.tex:1135` 的 §8 是「Holonomic 模」，但 $D_1(U)=R(U)\oplus T_X(U)$、$\sigma_p$ 的对称多重线性等正是 §5/§6 的内容。英文原文确印作 I.8.x，故本章按铁律不动，请主控核查第一章节号是否需整体平移。
4. **chap2.tex:5,7 / 印刷 p.55**：译文「可如第一章 §5 那样定义」「如第一章所讨论」，对应英文原文为 `as in ??` 与 `As we discussed in ??`——原文此处就是未解析的交叉引用（`??`），无法核对所指，保留译文。

## 5. 统计

- **P1：0 条**（无公式错误、无证明断链、无术语致概念变化、无漏译）
- **P2：4 条**（chap2.tex:164、188、229、616）
- **P3：3 条**（chap2.tex:80、582、648）
- **原文笔误：3 条**（p064:7、p073:35、p080:33；其中 p080:33 与 P2 的 :616 为同一处）
- **存疑：4 条**
