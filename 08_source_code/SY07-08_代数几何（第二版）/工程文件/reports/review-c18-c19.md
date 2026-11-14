# 校勘报告：c18 + c19（§2.7 Grothendieck 存在定理，原书 p.223–246）

- 校对块：`源码/chunks/c18.tex`（p.223–235，条目 2.7.1–2.7.13）、`源码/chunks/c19.tex`（p.236–246，条目 2.7.14–2.7.21 + 2.7.10 的证明）。
- 依据：页面图像 `工程文件/pages/p230.png`–`p253.png`（24 页，逐页对照）；条目类型/页码另与 `工程文件/work/items.tsv` 交叉核对。
- 结论：**未发现实质数学错误**。全部 21 个条目的编号、环境类型、`\label` 与原书一致；9 个交换图（c18 三个、c19 六个）与原图逐个节点/箭头一致；核过 40 余条关键公式，无一错符号。发现 **6 处非数学性瑕疵**（2 处建议修，4 处轻微），其中 1 处是原书自身的笔误被 c19 静默改正但未加译注。

---

## 一、条目编号 / 环境类型 / label（全部一致）

| 编号 | 原书页(PDF) | 原书类型 | c18/c19 环境 | label |
|---|---|---|---|---|
| 2.7.1 | 223 (230) | Lemma | `lemma` | `it:2.7.1` ✓ |
| 2.7.2 | 224 (231) | Lemma | `lemma` | `it:2.7.2` ✓ |
| 2.7.3 | 225 (232) | Lemma | `lemma` | `it:2.7.3` ✓ |
| 2.7.4 | 227 (234) | Theorem | `theorem` | `it:2.7.4` ✓ |
| 2.7.5 | 228 (235) | Corollary | `corollary` | `it:2.7.5` ✓ |
| 2.7.6 | 229 (236) | Corollary | `corollary` | `it:2.7.6` ✓ |
| 2.7.7 | 230 (237) | Lemma | `lemma` | `it:2.7.7` ✓ |
| 2.7.8 | 231 (238) | Proposition | `proposition` | `it:2.7.8` ✓ |
| 2.7.9 | 233 (240) | Corollary | `corollary` | `it:2.7.9` ✓ |
| **2.7.10** | 234 (241) | **Theorem**（Grothendieck Existence Theorem） | `theorem[Grothendieck 存在定理]` | **`it:2.7.10` ✓** |
| 2.7.11 | 234 (241) | **Theorem**（原书同样标题为 Grothendieck Existence Theorem） | `theorem[Grothendieck 存在定理]` | `it:2.7.11` ✓ |
| 2.7.12 | 235 (242) | Lemma | `lemma` | `it:2.7.12` ✓ |
| 2.7.13 | 235 (242) | Lemma | `lemma` | `it:2.7.13` ✓ |
| 2.7.14 | 236 (243) | Lemma | `lemma` | `it:2.7.14` ✓ |
| 2.7.15 | 236 (243) | Lemma | `lemma` | `it:2.7.15` ✓ |
| 2.7.16 | 237 (244) | Lemma | `lemma` | `it:2.7.16` ✓ |
| 2.7.17 | 238 (245) | Lemma | `lemma` | `it:2.7.17` ✓ |
| 2.7.18 | 241 (248) | Corollary | `corollary` | `it:2.7.18` ✓ |
| 2.7.19 | 241 (248) | Corollary | `corollary` | `it:2.7.19` ✓ |
| 2.7.20 | 243 (250) | Theorem | `theorem` | `it:2.7.20` ✓ |
| 2.7.21 | 245 (252) | Lemma | `lemma` | `it:2.7.21` ✓ |

统计：**lemma 11 / theorem 4 / corollary 5 / proposition 1 = 21**，与 lead 的预估一致。
- **2.7.10 确为 Grothendieck 存在定理**，label `it:2.7.10` 正确（c09 的引用可解析）。
- 注意：**2.7.11 在原书里也冠以同名标题 "Theorem 2.7.11 (Grothendieck Existence Theorem)"**（p.234），c18 照录同名，不是笔误；它是 2.7.10 的"不涉及形式完全化"的等价形式。

## 二、发现的 6 处瑕疵（按严重度）

格式：`位置（原书页 + 文件行号）| 原书 | 译文 | 建议`

### A. 建议修（2 条）

**A1. 静默改正原书笔误，未加译注（1）：$\Gamma(X,\cF_1(n))$ → $\Gamma(X_1,\cF_1(n))$**

| 位置 | 原书 | 译文 | 建议 |
|---|---|---|---|
| 原书 p.241（PDF 248）；`c19.tex:192` | `Γ(X̂,𝔉(n)) → Γ(X,𝓕₁(n))` 是满射 | `\Gamma(\widehat{X},\fF(n))\to\Gamma(X_1,\cF_1(n))` 是满射 | **改得对，但请补一条译注** |

理由（回答 lead 的问题："c19 按 $X_1$ 处理是否合理"）：**完全合理，且是必须的**。$\cF_1=\hat i_1^*\mathfrak F$ 是 $X_1$ 上的模，$\Gamma(X,\cF_1(n))$ 无意义；紧接的下一句原书自己就写"它们在 $\Gamma(X,\cF_1(n))$ 中的像"，而 2.7.17 给出的正是 $H^0(\widehat X,\mathfrak F(n))\to H^0(X_k,\cF_k(n))$（$k=1$）的满射性。所以这是原书排印时把 $X_1$ 漏了下标 1。建议照 c19 的处理保留 $X_1$，并在该段后加一行：`\begin{tnote}...同一页原书把 $\Gamma(X_1,\cF_1(n))$ 印作 $\Gamma(X,\cF_1(n))$，据 2.7.17（$k=1$）与下文自证，此处应为 $X_1$。[依据：原书 p.241]`。

**A2. 静默改正原书笔误，未加译注（2）：2.7.21 陈述中的 $f$ → $p$**

| 位置 | 原书 | 译文 | 建议 |
|---|---|---|---|
| 原书 p.245（PDF 252）；`c19.tex:372` | "…the morphism $p_k:Z_k\to X_k$ induced by $p$ … is an isomorphism for each $k$. If $A$ is $I$-adically complete, then **$f$** is also an isomorphism." | "…$p_k\colon Z_k\to X_k$ 是同构。若 $A$ 是 $I$-进完备的，则 $p$ 也是同构。" | **译得对（$f$ 无定义，必为 $p$），但请补译注** |

2.7.21 通篇只有 $p:Z\to X$，没有 $f$；其证明也是从 $p$ 出发证 $p$ 是同构。这是原书笔误。建议同 A1 的处理方式加一行 `[依据：原书 p.245]` 的译注；若 Lead 更倾向"改而不注"，则至少在两块报告的存疑点里登记。

### B. 轻微（2 条）

**B1. 漏译 "unique up to unique isomorphism" 的第二个 unique**

| 位置 | 原书 | 译文 | 建议 |
|---|---|---|---|
| 原书 p.234（PDF 241）；`c18.tex:528` | "there exists a coherent $\cO_X$-module $\cF$ **unique up to unique isomorphism** such that $\mathfrak F\cong\widehat\cF$" | "存在凝聚 $\cO_X$-模 $\cF$，**它在同构意义下唯一**，使得…" | 改为"**它在至多差一个唯一同构的意义下唯一**"或"**它在唯一同构意义下唯一**" |

"unique up to unique isomorphism" 是比 "unique up to isomorphism" 强的陈述（唯一性本身是唯一的），Grothendieck 存在定理的标准表述就要这个强度；2.7.11 用了同样的措辞（c18.tex:549 写"它在同构意义下唯一"）。两处宜同样改。

**B2. 译注措辞失实："沿固有满射下降"**

| 位置 | 原书 | 译文 | 建议 |
|---|---|---|---|
| 原书 p.235–242；`c19.tex:230` | 2.7.15 假设"Suppose $g$ is a **proper** morphism"；2.7.16 亦只设 $g$ **proper** | 译注写"2.7.15、2.7.16 允许沿**固有满射**（由 Chow 引理给出的射影覆盖）下降" | 删"满射"，改为"沿**固有态射**下降" |

原书 2.7.15/2.7.16 都没有 surjective 假设；"由 Chow 引理给出的射影覆盖"是 2.7.10 证明里的用法，不在这两条引理的假设中。事实性小错，但译注是可被读者当依据的文字，建议改。

### C. 可选（2 条，可不改）

**C1.** `c18.tex:524`（原书 p.234）2.7.9 的证明直接用"由于 $f$ 是固有的"而没有定义 $f$ —— **原书也是如此**（$f$ 指结构态射 $X\to\Spec A$，承 2.7.8 的 $X$ proper over $\Spec A$）。译文照录不算错；若求读者友好，可在该处加半句"（$f$ 指结构态射 $X\to\Spec A$）"。

**C2.** `c18.tex:392`（原书 p.230–231）译注把"$i^*$ 正合 ⟺ 茎 $\cO_{\widehat X,P}$ 是 $\cO_{X,P}$ 的平坦代数"称作"形式函数定理的平坦版本"。可辩护，但严格说形式函数定理是关于 $H^n(\widehat X,\widehat\cF)\cong\plim H^n(X,\cF/I^k\cF)$ 的（2.7.4），这里只是它的"平坦性基石"。若要严谨，改为"这正是形式函数定理（2.7.4）证明中反复用到的平坦性"。

## 三、译注所指"原书笔误"是否属实（逐条判定）

| 译注 | 位置 | 所指 | 判定 |
|---|---|---|---|
| c18 tnote 1 | `c18.tex:44`，[依据 p.223–226] | 2.7.1 的 ML 交换性是 2.7.2–2.7.4 的骨架 | **属实**。2.7.1 用 ML 交换 $H^n$ 与 $\plim$（p.223–224）；2.7.2 借松弛层把它搬到层（p.224–225）；2.7.3 搬到一般基（p.225–226）；2.7.4 用 2.7.3 收尾（p.228）。未声称笔误，仅导读，内容无误。 |
| c18 tnote 2 | `c18.tex:392`，[依据 p.230–231] | $i^*$ 正合＝茎平坦，是"形式函数定理的平坦版本" | **不涉笔误**；解释性措辞偏松，见 C2。 |
| c18 tnote 3 | `c18.tex:556`，[依据 p.234、p.242] | "原书随后实际证明的是 2.7.10（见 p.242 'Finally, we are ready to prove 2.7.10'）" | **页码正确**：该句确在原书 p.242 首段之后（PDF 249）。内容也正确（原书只证 2.7.10，2.7.11 经 1.5.13/1.5.18 的字典等价）。唯一含糊处："2.7.11 的存在性部分由**唯一性论证**与…字典得到"——存在性来自字典与 2.7.10，与"唯一性论证"无关，建议把"唯一性论证与"删掉。 |
| c19 tnote 1 | `c19.tex:230`，[依据 p.235–242] | 2.7.12–2.7.19 是下降链条 | 页范围属实（2.7.12 在 p.235，2.7.19 在 p.242）；"固有满射"失实，见 B2。 |
| c19 tnote 2 | `c19.tex:268`，[依据 p.242–243] | 2.7.10 的证明取 Noether 归纳、用 Chow 引理换射影覆盖 | **属实**。$\mathcal S$ 取极小元→Chow 引理 1.4.18（p.242）→2.7.19 得可代数化→2.7.15/2.7.16 造 $\mathcal R$→2.7.14 反推矛盾（p.243）。 |
| c19 tnote 3 | `c19.tex:404`，[依据 p.246] | 全书正文止于 p.246，§2.7 无习题 | **属实**。p.246 在 2.7.21 证明的 □ 之后整页留白。 |

## 四、接缝与漏译

- **c18 → c19**：原书 p.235 末行是 2.7.13 证明的中间句（"$(\Ext^1_{\cO_X}(\cH,\cF))^\wedge\cong\Ext^1_{\cO_X}(\cH,\cF)$"），该证明的收尾（"于是 $\Ext^1\cong\Ext^1$… By 2.1.15 … By 2.4.7 … □"）排在 p.236 顶部。c18 按"段落归起始页"规则把 p.236 顶部这段收在自己末尾（`c18.tex:590–599`），c19 从 `\begin{lemma}\label{it:2.7.14}` 直接起头 → **无重复、无漏译**，符合 BRIEF 接缝规则。lead 说的"c18 收在 p.235"严格讲应是"c18 收在 p.236 顶部 2.7.13 证明的收尾"。
- **c19 之后**：原书 p.246 之后无 §2.7 的任何内容（p.247–248 起是参考文献/索引，p.249–251 为 Index）。**无漏译**。
- c19 不写 `\subsection` ✓（符合分工）。

## 五、交换图核对（9 个全部一致）

| # | 位置 | 内容 | 判定 |
|---|---|---|---|
| 1 | `c18.tex:25–28`（p.223） | $0\to B^n(C_l)\to Z^n(C_l)\to H^n(C_l)\to0$ 的两行竖箭头 | 一致 ✓ |
| 2 | `c18.tex:231–234`（p.228） | $H^n(X,\cF)\to H^n(X,\cF/I^l\cF)\to Q_l\to0$ 对 $Q_k$ 行，左端 equal、第三竖箭头 | 一致 ✓ |
| 3 | `c18.tex:537–540`（p.234） | 2.7.11 的五对象图：$(X_k)\xrightarrow{i_k}(X)$、左竖 $i_{kl}$、底行 $(X_l)\xrightarrow{\hat i_l}(\widehat X)$、斜 $(X_l)\xrightarrow{i_l}(X)$、右竖 $(\widehat X)\xrightarrow{i}(X)$ | 一致 ✓ |
| 4 | `c19.tex:17–20`（p.236） | 2.7.15：$Y\xrightarrow{g}Z$，$Y$ 斜向 $\Spec A$、$Z$ 竖直向 $\Spec A$ | 一致 ✓ |
| 5 | `c19.tex:44–48`（p.237） | 2.7.16：$\widehat Y\to\widehat Z$ / $Y'=Y\times_ZZ'\xrightarrow{g'}Z'$ / $Y\xrightarrow{g}Z$ 三层竖箭头 | 一致 ✓ |
| 6 | `c19.tex:102–105`（p.238） | 2.7.17：笛卡尔方块 $X'=X\times_S\Spec B\xrightarrow{g'}X_1$、$f'\downarrow,\ f_1\downarrow$、底行 $\Spec B\xrightarrow{g}\Spec A/I$ | 一致 ✓ |
| 7 | `c19.tex:302–306`（p.244） | 2.7.20 菱形图（左列两对象 equal、右列两对象 ≅、四箭头汇聚到 $\cO_{X_k\times Y_k}\cong i_k^*\cO_{X\times Y}$） | 一致 ✓（原书在指向中心的两条斜箭头上标了 ≅，译文省略了这两个标签，纯装饰差异） |
| 8 | `c19.tex:314–317`（p.244） | $\cO_{X\times_S Y}\to\cO/\sJ_f$，斜向 $\cO/\sJ_g$，右竖 ≅ | 一致 ✓ |
| 9 | `c19.tex:350–353`（p.245） | 三列两行：$\cO_{X_k\times Y_k}\cong i_k^*\cO_{X\times Y}\cong i_k^*\cO_{X\times Y}$ 对上 $\cO/\sJ_k\cong i_k^*\cF\cong i_k^*\cO/\sJ$ | 一致 ✓ |

## 六、已逐符号核过的关键公式（≥20 条）

| # | 原书页 | 公式 | 文件位置 | 判定 |
|---|---|---|---|---|
| 1 | 223 | $H^n(\plim_k C_k^\bullet)\cong\plim_k H^n(C_k^\bullet)$ | c18:13 | ✓ |
| 2 | 223 | $\Image(H^n(C_l)\to H^n(C_k))=\Image(H^n(C_{k+k_0})\to H^n(C_k))$，$l\ge k+k_0$ | c18:20 | ✓ |
| 3 | 223 | $0\to\plim Z^n\to\plim C^n\to\plim B^{n+1}\to0$；$0\to\plim B^n\to\plim Z^n\to\plim H^n\to0$ | c18:37–38 | ✓ |
| 4 | 225 | $\check H^n(\mathfrak U,\plim\cF_k)\cong\plim\check H^n(\mathfrak U,\cF_k)$ | c18:89 | ✓ |
| 5 | 227 | $\widehat X=\Supp(\cO_X/\cI)$，$\cO_{\widehat X}=\plim(\cO_X/\cI^k)|_{\widehat X}$，$\widehat\cF=\plim(\cF/\cI^k\cF)|_{\widehat X}$ | c18:182–187 | ✓ |
| 6 | 227 | $i_*\widehat\cF=\plim\cF/I^k\cF$ | c18:205 | ✓ |
| 7 | 227 | $Q_k=\Image(H^n(X,\cF/I^k\cF)\to H^{n+1}(X,I^k\cF))$ | c18:219 | ✓ |
| 8 | 228 | $\Image(H^n(X,\cF/I^l\cF)\to H^n(X,\cF/I^k\cF))=\Image(H^n(X,\cF)\to H^n(X,\cF/I^k\cF))$ | c18:247 | ✓ |
| 9 | 229 | $R^n\hat f_*\widehat\cF\cong\plim R^nf_{k*}\cF_k\cong\widehat{R^nf_*\cF}$ | c18:282 | ✓（原书 $\widehat{R^nf_*}\cF$，帽子范围不同，等义） |
| 10 | 229 | $R^n(i_{Y_k}f_k)_*\cF_k\cong i_{Y_k*}R^nf_{k*}\cF_k$ | c18:331 | ✓ |
| 11 | 230 | $\plim R^nf_*\cF/I^kR^nf_*\cF\cong\plim R^nf_*(\cF/I^k\cF)$（用 2.5.9） | c18:339 | ✓ |
| 12 | 231 | $(i^*\cF)_P\cong\cO_{\widehat X,P}\otimes_{\cO_{X,P}}\cF_P$ | c18:362 | ✓ |
| 13 | 233 | $(\Ext^n_{\cO_X}(\cF,\cG))^\wedge=i^*\Ext^n_{\cO_X}(\cF,\cG)$ | c18:442 | ✓ |
| 14 | 233 | 五段复合 $(\Ext^n)^\wedge\cong i^*\Ext^n\cong H^n(i^*\Hom)\to H^n(\Hom(i^*\cF,i^*\cI))\to H^n(\Hom(i^*\cF,\cJ))\cong\Ext^n_{\widehat X}$ | c18:449–455 | ✓ |
| 15 | 233 | 谱序列 $(H^p(X,\Ext^q))^\wedge\Rightarrow(\Ext^{p+q})^\wedge$ 与 $H^p(\widehat X,\Ext^q_{\widehat X})\Rightarrow\Ext^{p+q}_{\widehat X}$，tag (1)(2) | c18:486–492 | ✓ |
| 16 | 234 | $I\subset\operatorname{rad}(A)$、$V(\mathfrak a)\cap V(I)=\varnothing\Rightarrow\mathfrak a=A$ | c18:524 | ✓ |
| 17 | 234 | 2.7.11 的 $\phi_{kk}=\id$、$i_{lm*}(\phi_{lk})\circ\phi_{ml}=\phi_{mk}$、$i_{kl}^*F_l\cong F_k$ 即 $F_l\otimes_{\cO_{X_l}}\cO_{X_k}\cong F_k$ | c18:546–547 | ✓ |
| 18 | 234 | $\psi_{lk}:i_l^*\cF\to i_{kl*}i_{kl}^*i_l^*\cF\cong i_{kl*}i_k^*\cF$ | c18:551 | ✓ |
| 19 | 235 | $(\Ext^1_{\cO_X}(\cH,\cF))^\wedge\cong\Ext^1_{\cO_{\widehat X}}(\fH,\fF)$ 及 2.1.15 的对应 | c18:580–594 | ✓ |
| 20 | 237 | $\widehat{(J'^n)^\sim}\cong(J'^n)^\sim\cO_{\widehat Z}=(J^n)^\sim\cO_{\widehat Z}\cong\widehat{(J^n)^\sim}$ | c19:52 | ✓ |
| 21 | 237 | $\hat g^*\mathfrak G\cong\hat g^*((M^\sim)^\wedge)\cong\hat g^*i_Z^*M^\sim\cong i_Y^*g^*M^\sim\cong(g^*M^\sim)^\wedge$ | c19:60 | ✓ |
| 22 | 237 | $\hat g_*\hat g^*\mathfrak G\cong(g_*g^*M^\sim)^\wedge$，$\ker(M^\sim\to g_*g^*M^\sim)\cong K^\sim$，$(J^n)^\sim K^\sim=0$ | c19:64,76,78 | ✓ |
| 23 | 238 | $\cO_X(n)=\cO_X(1)^{\otimes n}$，$\cF_k=\hat i_k^*\mathfrak F$，$\cF_k(n)=\cF_k\otimes i_k^*\cO_X(n)$，$\mathfrak F(n)=\mathfrak F\otimes i^*\cO_X(n)$ | c19:84–87 | ✓ |
| 24 | 239 | $g'_*\cO_{X'}\cong f_1^*B^\sim\cong\bigoplus_k f_1^*(I^k/I^{k+1})^\sim$ | c19:113 | ✓ |
| 25 | 239 | $g'_*(\fF'(n))\cong\bigoplus_k I^k\mathfrak F(n)/I^{k+1}\mathfrak F(n)$（1.4.26）；$\bigoplus_k H^p(X_1,I^k\mathfrak F(n)/I^{k+1}\mathfrak F(n))\cong H^p(X',\fF'(n))$ | c19:125,137 | ✓ |
| 26 | 240 | $H^p(\widehat X,\mathfrak F(n)/I^k\mathfrak F(n))=0$ 即 $H^p(X_k,\cF_k(n))=0$；$H^p(\widehat X,\mathfrak F(n))\cong\plim_k H^p(X_k,\cF_k(n))$ | c19:145–149,173 | ✓ |
| 27 | 241 | $((B^m)^\sim)^\wedge\to(M^\sim)^\wedge$ 满（1.4.2 (iii) + 1.5.13 (i) + 中山引理） | c19:212 | ✓ |
| 28 | 242 | $\cO_{\widehat X}(n')^{m'}\to\cO_{\widehat X}(n)^m\to\mathfrak F\to0$ | c19:224 | ✓ |
| 29 | 242 | $0\to\widehat\cJ^n\to\cO_{\widehat Z}\to(h_*\cO_{Z-U})^\wedge\to0$，$(h_*\cO_{Z-U})^\wedge\cong\hat h_*\cO_{\widehat{Z-U}}$ | c19:246,250 | ✓ |
| 30 | 243 | $\cO_{\widehat{Z-U}}\cong(\cO_{\widehat Z}/\widehat\cJ^n)|_{\widehat{Z-U}}$；$\mathcal R\cong\hat h_*\hat h^*\mathcal R$ | c19:258,262 | ✓ |
| 31 | 243 | $\sJ_f\cO_{X_k\times_{S_k}Y_k}=\sJ_g\cO_{X_k\times_{S_k}Y_k}$ 及其商相等 | c19:290,294 | ✓ |
| 32 | 244 | $i_k^*(\cO/\sJ_f)\cong i_k^*(\cO/\sJ_g)$，两图交换 ⇒ $\cO/\sJ_f=\cO/\sJ_g$ | c19:298,321 | ✓ |
| 33 | 245 | $i_k^*(\cO/\sJ)\cong i_k^*\cF\cong\cO_{X_k\times Y_k}/\sJ_k$ | c19:346 | ✓ |
| 34 | 246 | $i_k^*p_*\cO_Z\cong p_{k*}\cO_{Z_k}$，故 $i_k^*\cO_X\to i_k^*p_*\cO_Z$ 等同 $p_k^\sharp$ | c19:390,398 | ✓ |

补充核过但未列式的：2.7.4 证明中 $k_0$ 的取法（$Q_{k+k_0}\to Q_k=0$ 及三段分解 $Q_l\to Q_{k+2k_0}\to Q_{k+k_0}\to Q_k$）、2.7.6 证明中 $i_{X_k*}\cF_k=\cF/I^k\cF$ 与 $fi_{X_k}=i_{Y_k}f_k$、2.7.17 中 $K=\bigoplus_k I^k\mathfrak F/I^{k+1}\mathfrak F$ 视为 $\cO_{X_1}$-模的三步论证、2.7.18 中 $(B/IB)^m\to M/IM$ 满⇒$B^m\to M$ 满。——均与原书一致。

## 七、给 Lead 的处理建议

1. **必须做**：给 A1、A2 各补一条 `[依据：原书 p.N]` 译注（两处都是原书笔误，译文改对了但没留痕；本工程惯例是"照录+译注"，静默改正会让后续校对者以为是译文错）。若 Lead 认可"静默改正"这一新惯例，也请在 STYLE_GUIDE 里写明，否则各块标准不一。
2. **建议做**：B1（unique up to unique isomorphism，两处）、B2（删"满射"）。
3. **可不做**：C1、C2、c18 tnote 3 的"唯一性论证"三字。
4. 无需改动的：21 个条目的编号/类型/label、9 个交换图、接缝、以及全部 34 条主公式 —— 均可放行。
