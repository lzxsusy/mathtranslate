# tr10a.tex 交叉校对报告

- **校对对象**：`work/src/chunks/tr10a.tex`（原文 Ioannis P. Zois, *18 Lectures on K-Theory*, arXiv:1008.1346v1，**pp.127–133**，§22 附录）
- **核对依据**：`work/pages/p127.png–p133.png`（200 dpi，公式唯一真值）+ 对关键处另做 **500–900 dpi** 裁图复核（`work/tmp/rev10a_*.png`）；`work/split/p127.txt–p133.txt`（仅用于定位）；`STYLE_GUIDE.md`、`BRIEF.md`、`TIMELINE.md`、`glossary.tsv`
- **校对方式**：只读 tr10a.tex，未修改任何文件；脚本做结构静态检查；tikzcd 写法用最小样例单独编译验证（未编译全书）
- **校对时间**：2026-11-06

---

## 一、结论摘要

**总体合格，可付编译**。7 页内容**无漏译**；原文 **12 个粗体小标题全部到位、无自造**；11 条批注、7 个页标记、2 个 tikzcd 图、全部展示式均逐符号核对通过；tr-06 自称的 **6 处原文笔误全部为真**（500–900 dpi 复核）。

需处理的问题共 **2 处必须改 + 6 项可选改**：

| 级别 | 数量 | 内容 |
|---|---|---|
| **必须改** | 2 | ① p.131 `Examples:` 原文**不是**粗体，tr10a 用 `\para` 排成了粗体小标题（使粗体标题变成 13 个）；② p.128 原文笔误 `lader`（=ladder）**未登记批注**（tr-06 的 6 处之外的第 7 处笔误） |
| **可选改** | 6 | 斜体强调遗漏 4 处、`\bigwedge` 字号、2 条批注措辞不准、首部注释措辞、`1-连通` 术语全书统一 |

**关键结论**：

1. 结构：原文粗体标题 12 个 → tr10a 全部覆盖（逐条对照见 §二）；tr10a 的 `\para` 共 13 处，多出的 1 处是 `例子：`（原文存在但非粗体）。
2. 公式：抽查 11 条（含 5-引理梯子图、蛇形引理图、UCT 的 Tor 项、Eilenberg–MacLane 定义、Gelfand 对偶）**全部与原文一致**，连 5-引理图中「q 的标签在箭头右侧」这一原文排版细节都照原样保留。
3. 笔误：`meterial`、`kill of`、`seperates`、`Tor(H_{i-1}(X;A),A)`、「homology vs H^n」、「homeomorphisms」 **6 处全部真实存在**，tr10a 的登记与判断皆正确；另有第 7 处 `lader` 漏登。
4. 排版硬指标：正文 **U+2013 = 0**、**`\tag` = 0**；U+2014 仅作中文破折号（2 处正文，正常）；环境/花括号/`$` 全部配对；UTF-8 无 BOM、LF、无乱码。
5. 边界：p.126（tr-09 末）→ p.127 起、p.133 末 → p.134（c-refs）**无重复、无缺口**。

---

## 二、结构核对表

### 2.1 原文粗体小标题（12 个）逐条核对

| # | 原文页 | 原文粗体小标题（页图核对） | tr10a 行号与写法 | 状态 |
|---|---|---|---|---|
| 1 | p.127 | **Van Kampen's Theorem.** | L18 `\para{Van Kampen 定理.}` | ✅ 在 |
| 2 | p.128 | **5-Lemma.** | L37 `\para{5-引理.}` | ✅ 在 |
| 3 | p.128 | **Serpent Lemma.** | L54 `\para{蛇形引理.}` | ✅ 在 |
| 4 | p.129 | **Universal Coefficient Theorem.** | L74 `\para{万有系数定理.}` | ✅ 在 |
| 5 | p.129 | **Hurewicz Theorem.** | L88 `\para{Hurewicz 定理.}` | ✅ 在 |
| 6 | p.130 | **Whitehead Theorem.** | L107 `\para{Whitehead 定理.}` | ✅ 在 |
| 7 | p.130 | **Definition of Eilenberg-MacLane spaces.** | L121 `\para{Eilenberg--MacLane 空间的定义.}` | ✅ 在 |
| 8 | p.131 | *Examples:*（**正文行首，非粗体**） | L129 `\para{例子：}` | ⚠️ **被粗体化**（见 §七-必须改 1） |
| 9 | p.131 | **Milnor-Moore Theorem.** | L144 `\para{Milnor--Moore 定理.}` | ✅ 在 |
| 10 | p.131 | **Group Completion Theorem (D. McDuff, G. Segal).** | L151 `\para{群完备化定理（D. McDuff, G. Segal）.}` | ✅ 在 |
| 11 | p.132 | **Closed Graph Theorem.** | L164 `\para{闭图像定理.}` | ✅ 在 |
| 12 | p.132 | **Stone-Weierstrass Theorem.** | L179 `\para{Stone--Weierstrass 定理.}` | ✅ 在 |
| 13 | p.132 | **Gelfand Theorem.** | L187 `\para{Gelfand 定理.}` | ✅ 在 |

**核对结论**：

- 原文 **12 个粗体小标题一个不缺、一个不多**（对象名逐字对应；`Serpent Lemma` → 蛇形引理、`Group Completion Theorem` → 群完备化定理 等译名均可接受）。
- **无自造标题**：13 个 `\para` 中 12 个对应原文粗体标题，第 13 个 `例子：` 在原文中确实存在（p.131 "Examples:"），只是**原文没有加粗**——属于排版层级误加，不是内容编造。
- 原文附录**无编号定理类**：逐页复核 pp.127–133，未出现 "Definition 1." / "Theorem 1." 之类编号标题，tr10a 全部用 `\para{…}`、未自造编号，**处理正确**。
- 另有若干**斜体引导句**（如 p.130 "Eilenberg-MacLane spaces are the building blocks of homotopy theory:"、p.131 "The Hurewicz Theorem is a central result…"），tr10a 用 `\emph{…}` 或普通段落处理，未误加粗体标题 ✅。

### 2.2 其他结构项

| 项目 | 检查结果 |
|---|---|
| `\section` | 仅 1 个：`\section{附录}`（L9），与 BRIEF §3 逐字一致 ✅ |
| 页标记 `% [原文 p.N]` | 7 个，p.127–p.133 全覆盖，位置正确（p.130 的标记落在 Hurewicz 句中断处，与原文跨页一致）✅ |
| 片段头 | `% ===== 原文 pp.127--133 =====` 存在（L7）✅ |
| 图表 | 2 个 tikzcd（5-引理梯子、蛇形引理），均包在 `\[ … \]` 内；已用最小样例验证 lualatex 可正常编译 ✅（与 tr04a/tr09a 的「裸 tikzcd」写法不同，但输出无碍，见 §七-可选 6） |
| 批注 | 11 条 `% [Tutor Note: …]`，密度 ≥3 条/节（本块仅 1 节）✅ |
| 禁止项 | `\documentclass`/`\usepackage`/`\begin{document}`/`\newcommand`/`**`/`$$` 均为 0 ✅ |

---

## 三、公式逐符号核对表

### 3.1 抽查（11 条，均对 200 dpi 页图 + 关键处 800–900 dpi 裁图）

| # | 页 | 公式/图表 | 原文（dpi 复核） | tr10a（行号） | 结论 |
|---|---|---|---|---|---|
| 1 | p.127 | van Kampen 融合自由积 | $\pi_1(X_1,*)\star_{\pi_1(X_0,*)}\pi_1(X_2,*)\to\pi_1(X,*)$，下标 $\pi_1(X_0,*)$ | L22–24 同式，$\star_{\pi_1(X_0,*)}$ | ✅ 一致 |
| 2 | p.128 | **5-引理「梯子」图** | 上行 $A\xra{f}B\xra{g}C\xra{h}D\xra{j}E$（字母在上）；下行 $A'\xra{r}B'\xra{s}C'\xra{t}D'\xra{u}E'$（字母在下）；竖箭头 $l,m,n,p$ 标签在箭头**左**侧，$q$ 在**右**侧 | L39–43 tikzcd：上行 `"f","g","h","j"`、下行 `"r"','"s"','"t"','"u"'`、竖箭头 `"l"','"m"','"n"','"p"'`，而 `"q"` 无撇（=右侧） | ✅ 一致（**连 q 在右侧这一原文排版特征都保留了**） |
| 3 | p.128 | **蛇形引理图** | 上行 $0\to A\xra{f}B\xra{g}C\to0$；下行 $0\to A'\xra{f'}B'\xra{g'}C'\to0$；竖箭头 $a,b$ 在左、$c$ 在右 | L56–59 tikzcd：`"a"','"b"'` 左，`"c"` 右（无撇） | ✅ 一致（同上，c 在右侧照原样） |
| 4 | p.128 | 蛇形引理正合列 | $0\to\ker a\to\ker b\to\ker c\xra{d}\coker a\to\coker b\to\coker c\to0$ | L62–65 同式 | ✅ 一致（`Ker`/`coker` 按标准正体归一） |
| 5 | p.129 | **UCT 的 Tor 项** | 正文：$\operatorname{Tor}(H_{i-1}(X;A),A)$；展示式同样写 $H_{i-1}(X;A)$（800 dpi 复核两处均为 **A**） | L76、L80 两处均写 `H_{i-1}(X; A)` | ✅ 一致（照原文的疑似笔误；批注已登记，见 3.2-④） |
| 6 | p.129 | Hurewicz 同态 | $h_*:\pi_k(X)\to H_k(X;\Z)$；$h_*:\pi_1(X)\to\pi_1(X)/[\pi_1(X),\pi_1(X)]$ | L89–90、L95–96 | ✅ 一致 |
| 7 | p.130 | Eilenberg–MacLane 定义 | 连通 $X$ 称为 $K(G,n)$ 型，若 $\pi_n(X)\cong G$ 且其余同伦群为零；$n>1$ 时 $G$ 交换 | L121–123、L125 | ✅ 一致 |
| 8 | p.131 | Milnor–Moore | $U(\pi_*(\Omega X)\otimes\Q)\to H_*(\Omega X;\Q)$ | L146–148 | ✅ 一致 |
| 9 | p.131 | 群完备化 | $H_*(M)\to H_*(\Omega BM)$；$H_*(M)[\pi_0(M)^{-1}]\to H_*(\Omega BM)$ | L153–159 | ✅ 一致 |
| 10 | p.132 | 闭图像定理 | 图像 $=\{(x,y)\in X\times Y:Tx=y\}$ | L166–168 | ✅ 一致 |
| 11 | p.132–133 | **Gelfand 对偶** | 两个范畴等价；函子 $C(-)$：紧 Hausdorff 空间 $X\mapsto C(X)$；$\operatorname{Spec}(-)$：$A\mapsto\operatorname{Spec}(A)$（谱） | L187–197 | ✅ 一致（`homeomorphisms` 照原文，见 3.2-⑥） |

> 另抽查：p.127 `K(\Z,1)=S^1`、`K(\Z,2)=\C P^\infty`、`K(\Z_2,1)=\R P^\infty`（p.131 例）均与原文一致 ✅；p.131 `K(G,1)=\bigwedge_{i=1}^{k}S^1` 语义正确，但 `\bigwedge` 比原文的 `\wedge^{k}_{i=1}` 偏大（见 §七-可选 2）。

### 3.2 tr-06 自称的 6 处原文笔误——逐条复核（500–900 dpi 裁图）

| # | 位置 | tr-06 的说法 | 实测复核 | 判定 |
|---|---|---|---|---|
| ① | p.127 | `background meterial` → material | 800 dpi 裁图：`books with background meterial in the introduction`，确为 **meterial** | ✅ **真笔误**，tr10a 处理正确（正文照译「背景材料」+ 批注） |
| ② | p.131 | `to kill of the remaining homotopy` → kill off | 800 dpi：`... of higher dimension to kill of the remaining homotopy.` | ✅ **真笔误**，tr10a 按「消去」译 + 批注 ✅ |
| ③ | p.132 | `seperates points` → separates | 800 dpi：`a subset which seperates points` | ✅ **真笔误**，tr10a 照译 + 批注 ✅ |
| ④ | p.129 | UCT 的 $\operatorname{Tor}(H_{i-1}(X;A),A)$ 应为 $H_{i-1}(X;\Z)$ | 800 dpi 复核**正文与展示式两处**均为 $H_{i-1}(X;A)$；标准 UCT 应为 $\operatorname{Tor}(H_{i-1}(X;\Z),A)$ | ✅ **真笔误**（且原文同一错误出现两次），tr10a 两处照抄 + 批注给正确形式 ✅ |
| ⑤ | p.131 | 说「representations of **homology** with G coefficients」，紧接的却是 $H^n(X;G)$（上同调） | 800 dpi：`give representations of homology with G coefficients: ... the set H^n(X;G) (the n-th singular cohomology group ...)` | ✅ **真笔误**（homology 应为 cohomology；$[X,K(G,n)]\cong H^n(X;G)$），tr10a 照译 + 批注 ✅ |
| ⑥ | p.132–133 | Gelfand 定理第 2 条「arrows the **homeomorphisms** among them」 | 800 dpi：p.132 末 `... and arrows the`，p.133 首 `homeomorphisms among them.` | ✅ **真笔误**（Gelfand 对偶的态射应为连续映射，同胚只对应 $\ast$-同构），tr10a 照译 + 批注 ✅ |

**小结**：6 处全部为真，tr10a 的登记、判断依据与正确形式**均正确**。

### 3.3 额外发现的第 7 处原文笔误（tr-06 未登记）

| 位置 | 原文 | 应为 | 证据 |
|---|---|---|---|
| **p.128** | `the following commutative diagram (lader) is given` | **(ladder)** | 800 dpi 裁图 `rev10a_b.png` 清晰显示 `(lader)`；5-引理插图通称「ladder（梯子）」，tr10a 正文虽译作「（梯子）」，但**没有批注登记笔误**，不符合 STYLE §5「原文笔误必须给正确形式 + 判断依据」 |

> 另有若干排版级小疵（**不必逐条登记**）：`Poincare`（缺重音，tr10a 已写作 Poincaré，属译名规范化，可接受）、`CW −complex`（减号代替连字符，tr10a 已有批注说明）、`Hausdorffspace`/`Hausdorﬀspace`（词间空格丢失，纯排版）。

---

## 四、漏译核查（逐页对 split p127–p133）

| 页 | 原文内容单元 | tr10a 对应 | 覆盖 |
|---|---|---|---|
| p.127 | 开篇说明（含 `meterial`）/ Seifert–van Kampen 引导段 / **Van Kampen's Theorem** 全文 / 证明思路段（含 push-out、groupoid、2-groups、J.P. May）/ 5-Lemma 引导段 | L11–34 | ✅ 全覆盖，无删减 |
| p.128 | **5-Lemma** 陈述 + 梯子图 + 结论 / "diagram chasing" / 两个 4-引理与短 5-引理 / **Serpent Lemma** 陈述 + 图 + 正合列 | L37–65 | ✅ 全覆盖 |
| p.129 | 蛇形引理补充断言（$f$ 单、$g'$ 满）/ **UCT** 引导段 + 陈述 + 展示式 + 分裂性说明 + 上同调对偶 / Hurewicz 引导段 + **Hurewicz 定理** + 相对/三元组版本 + $k=1$ 情形 | L68–101 | ✅ 全覆盖 |
| p.130 | Hurewicz 同构与完美群注记 / Whitehead 引导段 + **Whitehead 定理** + 弱同伦等价 + 形状理论 + Quillen 模型范畴 / **Eilenberg–MacLane 定义** + $n>1$ 说明 | L100–126 | ✅ 全覆盖（页首句由 p.129 起、tr10a 在 L98–101 完整接续） |
| p.131 | `Examples:` + 4 个例子 / $K(G,n)$ 的 CW 构造（smash 积、粘胞腔、`kill of`）/ 基本性质（$[X,K(G,n)]\cong H^n(X;G)$，`homology` 笔误）/ **Milnor–Moore** / **Group Completion** | L129–159 | ✅ 全覆盖 |
| p.132 | closed graph 引导 + **Closed Graph Theorem** + 图像 / Weierstrass 定理 / 1937 Stone 段（Tychonoff、$C(X)$）/ **Stone–Weierstrass**（`seperates`）/ 实版本注 / Gelfand 引导 / **Gelfand Theorem** + 第 1 条 | L162–193 | ✅ 全覆盖 |
| p.133 | 第 2 条尾句（`homeomorphisms among them.`）/ 函子 $C(-)$ 与 $\operatorname{Spec}(-)$ / 局部紧与非单位的推广 / Connes 非交换几何 | L191–202 | ✅ 全覆盖 |

**边界接缝**

| 交界 | 检查 | 结论 |
|---|---|---|
| tr-09（p.126 末）→ tr10a（p.127 起） | tr09a 末为 p.126 的 Vandiver 段与两条批注；tr10a 首行为 `% ===== 原文 pp.127--133 =====` + `% [原文 p.127]` + `\section{附录}`，对应原文 "22 Appendix" | ✅ 无重复、无缺口 |
| tr10a（p.133 末）→ c-refs（p.134） | tr10a 末为 p.133 Connes 段；`c-refs.tex` 以 `% ===== 原文 pp.134--137 =====` + `% [原文 p.134]` + `\section*{参考文献}` 起 | ✅ 无重复、无缺口 |
| 块内页标记 | 7/7 标记，p.130 标记落在 Hurewicz 句中（跨页处），与原文分页一致 | ✅ |

---

## 五、术语核查（对照 glossary.tsv）

**与 glossary 一致（抽查）**：正合列 exact sequence、挠 torsion→挠（挠群）、张量积 tensor product、分类空间 classifying space、环路空间 loop space、局部紧 locally compact、紧 compact、谱 spectrum（Gelfand 谱）、$C^*$-代数、Banach 空间、幺半群 monoid（拓扑幺半群）✅

**glossary 未收、本块新出现（建议 Lead 决定是否补入）**：

| 英文 | tr10a 译法 | 备注 |
|---|---|---|
| fundamental group | 基本群 | 全书通用 |
| abelian category | 阿贝尔范畴 | |
| universal coefficient theorem | 万有系数定理 | |
| 5-Lemma / serpent (snake) lemma | 5-引理 / 蛇形引理 | |
| short exact sequence | 短正合列 | glossary 有「长/六项正合列」，缺「短正合列」 |
| Eilenberg–MacLane space | Eilenberg–MacLane 空间 | |
| weak homotopy equivalence | 弱同伦等价 | |
| shape theory | 形状理论 | |
| model category；fibrant / cofibrant | 模型范畴；纤维性 / 余纤维性 | |
| Hopf algebra | Hopf 代数 | |
| universal enveloping algebra | 泛包络代数 | |
| group completion | 群完备化 | |
| smash product | smash 积（**中英混排**） | 建议统一为「smash 积」或「压缩积」，见 §七-可选 5 |
| closed graph theorem | 闭图像定理 | |
| Stone–Weierstrass / Gelfand | Stone–Weierstrass 定理 / Gelfand 定理 | |
| groupoid / free product / amalgamation / push-out | 群胚 / 自由积 / 合并 / 推出 | |
| abelianisation | 交换化 | 与 tr04a「交换化」一致 ✅ |
| 1-connected | 1-连通 | **与 tr04a 的「单连通」不一致**（跨块术语），见 §七-可选 5 |

**内部一致性**：同一概念在 tr10a 内部无自相矛盾；`CW-复形`、`Eilenberg–MacLane`、`Milnor–Moore` 等复合名统一用 `--`，与全书其余 chunk 的 `Eilenberg–Steenrod` 风格一致 ✅。

---

## 六、排版检查

| 项目 | 结果 |
|---|---|
| 正文 **U+2013**（en dash） | **0 个** ✅（全部写成 `--`） |
| **`\tag`** | **0 个** ✅ |
| U+2014（em dash） | 12 个字符，仅出现在中文破折号「——」（正文 L27、L115 两处 + 头部注释/批注），属中文正常用法 ✅ |
| 展示式 | 12 个 `\[` / 12 个 `\]`，配对 ✅ |
| tikzcd | 2/2，均包在 `\[ … \]` 内；已用最小样例 (`work/tmp/rev10a_tikzcdtest.tex`) 在 lualatex 下编译通过（exit 0，生成 1 页 PDF），**不会导致编译失败** ✅ |
| 环境配对 / 花括号 / `$` 成对 | 脚本核验：`\begin`/`\end` 全配对、花括号深度归零、无奇数 `$` 行 ✅ |
| 编码 | UTF-8 无 BOM、LF（CR=0）、无 U+FFFD ✅ |
| 其他 | 无 `\documentclass`/`\usepackage`/`\begin{document}`/`\newcommand`/`**`/`$$` ✅ |

---

## 七、必须改 / 可选改

### 🔴 必须改（2 项）

| # | 位置 | 问题 | 建议改法 |
|---|---|---|---|
| 1 | **L129（p.131）** | `\para{例子：}` 把原文的 `Examples:` 排成粗体小标题。原文 `Examples:` 是**正文行首、非粗体**（800 dpi 裁图 `rev10a_d.png` 与加粗的 `5-Lemma.` 对比可辨）。这违反 STYLE §7.6「不给原文没有的段落加粗体标题」，且使本块粗体小标题变成 13 个（原文 12 个） | 改为普通段落：`例子：`（去掉 `\para`）。itemize 内容不变 |
| 2 | **p.128（对应 L37 附近）** | 原文笔误 `(lader)`（=ladder）未登记批注。tr10a 只在正文译作「（梯子）」，没有按 STYLE §5「原文笔误：必须给正确形式 + 判断依据（500 dpi 复核）」登记。这是 tr-06 自称的 6 处之外**第 7 处**笔误（800 dpi 裁图 `rev10a_b.png` 确认原文印作 `(lader)`） | 在 §5-引理段附近补一条批注，例如：`% [Tutor Note: p.128 原文把 "ladder"（梯子）误排作 "lader"，500/800 dpi 复核确认；正文按原意译作「梯子」，此处给出正确拼写。]` |

### 🟡 可选改（6 项，不影响数学内容）

| # | 位置 | 问题 | 建议 |
|---|---|---|---|
| 1 | L134（p.131） | `\bigwedge_{i=1}^{k}` 比原文的 `\wedge^{k}_{i=1}` 偏大（原图 ∧ 仅约大写字母高，非大运算符） | 改为 `\wedge_{i=1}^{k}`（与页图逐符号一致） |
| 2 | L104（p.130）、L185（p.132）、L199 / L201–202（p.133） | 原文斜体强调未译出：`weak homotopy equivalence`、`noncommutative geometry`、`locally compact`、`non-unital`、`topological extension`、`noncommutative algebras`（均已在 800 dpi 裁图确认斜体） | 按 TIMELINE §2 给相应中文加 `\emph{}`（属风格统一，非内容错误） |
| 3 | L210（p.131 批注） | 批注称「原文用 $\bigwedge_{i=1}^{k}S^1$（大楔积记号）」，但原文实际是普通 `\wedge`（见上） | 措辞改为「原文用 $\wedge^{k}_{i=1}$（楔号）」，避免给读者错误印象 |
| 4 | L212（p.132 批注） | 批注称 Stone–Weierstrass「另需 $S$ 对共轭封闭，原文未提，属省略」，但定理说的是「$S$ 生成的复单位 $\ast$-代数」，`\ast`-代数已含共轭封闭，无需额外假设 | 删去该半句或改为「『$\ast$-代数』一词已包含对共轭封闭的要求」 |
| 5 | 全文术语 | `smash 积` 中英混排；`1-连通`（p.131）与 tr04a 的「单连通」跨块不一致（glossary 未收） | 由 Lead 统一：`smash 积`（或「压缩积」）；`1-连通`/「单连通」择一 |
| 6 | 全块写法 | 2 个 tikzcd 用 `\[ \begin{tikzcd}…\end{tikzcd} \]` 包裹，与 tr04a/tr09a 的「裸 tikzcd」写法不一致（**已实测可正常编译**） | 无需修改；若追求全书源码风格统一，可去掉外层 `\[ … \]`（不影响输出） |

> 附：首部注释 L4「原文附录未使用任何编号定理类，**全部为粗体小标题**」与实测略有出入（`Examples:` 非粗体，另有若干斜体引导句），可顺手微调措辞，属可选。

---

### 附：本次校对用到的裁图（均在 `work/tmp/`，可复核）

`rev10a_ladder.png`（p.128 梯子图 900 dpi）、`rev10a_snake.png`（p.128 蛇形图 900 dpi）、`rev10a_a.png`/`rev10a_meterial.png`（p.127 meterial）、`rev10a_b.png`（p.128 lader）、`rev10a_c.png`/`rev10a_uctdisp.png`（p.129 UCT Tor 两处）、`rev10a_d.png`（p.131 Examples 非粗体）、`rev10a_e.png`（p.131 楔号）、`rev10a_f.png`（p.131 kill of / homology）、`rev10a_g.png`（p.132 seperates）、`rev10a_h.png`/`rev10a_gelfnum.png`（p.132 Gelfand 定理与列表）、`rev10a_133.png`（p.133 homeomorphisms 与斜体）。
