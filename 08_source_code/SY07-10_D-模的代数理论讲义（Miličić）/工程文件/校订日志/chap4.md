# 第 IV 章 校订日志（D-模的直像与逆像）

- 译文：`src/D-modules-zh/chapters/chap4.tex`（1521 行，10 节）
- 原文：`en_pages/p103.txt`–`p138.txt`（PDF 页 = 印刷页 + 6，印刷 97–132 页）
- 核对方式：逐条对英文原页；公式逐符号比对（上下标、系数、指标范围、$\operatorname{Tor}/\operatorname{Ext}$ 上下标、$\otimes$ 下标、移位、双模两侧作用、维数加减）。
- 条目对应：本章 10 节共 74 条（4.1.1–4.10.3），条目的类型与先后顺序与英文 4.x.y 一一吻合。

## 一、漏译与残留英文

- **无整条/整段漏译**：74 条编号条目、全部证明与说明段落均有对应；36 页原文对应 1521 行译文，密度正常。
- **无残留英文整句**：仅两处夹用英文短语「long exact」，已改（见 P2-12、P2-13）。术语首现的夹注（「有限振幅（amplitude）」「松的（flabby）」「完整亏格（holonomic defect）」）按体例保留。

## 二、P1（数学含义 / 公式 / 证明）

| 位置 | 原文 | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| chap4.tex:272（Lemma 4.2.3 证明末） | "which implies that Ext1R(Y)(Γ(X,V),N) = 0" | $\operatorname{Ext}^1_{R(Y)}(\Gamma(X,V),N)=0$ | $\operatorname{Ext}^1_{R(X)}(\Gamma(X,V),N)=0$ | 原文笔误：同句前半即 $\operatorname{Ext}^1_{R(X)}(\cdots)_x=0$，结论为「$\Gamma(X,V)$ 是投射 $R(X)$-模」，指标只能是 $R(X)$。译文原有括注「（原文误写为 $x\in R(X)$）」保留 | P1 |
| chap4.tex:747（Cor 4.5.7） | "the functor H0 ◦i+ ◦D = i• … is exact" | $H^0\circ i_+\circ\mathcal{D}=\varphi_\bullet$ | $H^0\circ i_+\circ\mathcal{D}=i_\bullet$ | 符号错：该函子从右 $\mathcal{D}_U$-模到右 $\mathcal{D}_X$-模，是 $i_\bullet$（原文 i•），非 $\varphi_\bullet$ | P1 |
| chap4.tex:1005（§7 Bernstein 证明末） | "Now, ?? implies that Ch(i+(V\|U)) ≥ n" | $\operatorname{Ch}(i_+(\mathcal{V}\|_U))\ge n$ | $\dim\operatorname{Ch}(i_+(\mathcal{V}\|_U))\ge n$ | 原文漏 $\dim$：上一式 $\operatorname{holdef}=\dim\operatorname{Ch}-n\ge 0$ 只能推出维数 $\ge n$，不是链的包含关系 | P1（原文笔误，径改） |
| chap4.tex:1434（Thm 4.10.2 证明，闭浸入特殊情形） | "where ψ0 is the restriction of ψ and i0 the natural inclusion" | 「其中 $\psi'$ 是 $\psi$ 的限制」 | 「其中 $\varphi'$ 是 $\varphi$ 的限制」 | 该图箭头为 $\varphi':\varphi^{-1}(Y)\to Y$ 与 $i'$（自然包含），$\psi'$ 不在图中；$\varphi'$ 才是 $\varphi$ 的限制。原文 $\psi/\psi_0$ 系 $\varphi/\varphi_0$ 之误 | P1 |

## 三、P2（术语、符号、交叉引用、一致性）

| 位置 | 原文 | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| 全章 14 处（行 1、216、224、261、619、625、642、676、760、762、1009、1019 等） | "direct image" | 正像 | 直像 | 术语表：direct image→直像；含章标题、§2/§5/§6 节标题及正文各处，改后「正像」全章为 0 | P2 |
| chap4.tex:456、462、464、466（Prop 4.3.8 及证明） | "Lp φ+" | $L^p\varphi^+$ | $L_p\varphi^+$ | 原文全作 $L_p$，且与本章其余（326、380、383、388 行）一致；$L^p$ 会被读成上同调 | P2 |
| chap4.tex:441（Thm 4.3.6 证明） | "by applying 4" | 引理 \ref{lem:4.3.5} | 引理 \ref{lem:4.3.4} | 原文「4」=同节 Lemma 3.4（$L\varphi^+=\mathcal{D}_{X\to Y}\otimes^L\varphi^{-1}$），非 3.5 | P2 |
| chap4.tex:498（Thm 4.3.10 证明，第一处） | "Because of the preceding discussion and 1" | 注记 \ref{rem:4.1.6} | 注记 \ref{rem:4.3.1} | 原文「1」=同节第 1 条（§3 的 Rem 3.1）；4.1.6 是 §1 的注记，不对 | P2 |
| chap4.tex:498（同句，第二处） | "This follows from 4. and the preceding discussion" | 引理 \ref{lem:4.3.5} | 引理 \ref{lem:4.3.4} | 同节「4」=Lemma 3.4 | P2 |
| chap4.tex:503 | "by 1" | 注记 \ref{rem:4.1.6} | 注记 \ref{rem:4.3.1} | 同上（语义见「五、存疑」第 5 条） | P2 |
| chap4.tex:757（Thm 4.5.8 证明） | "φ+(i+(D(W))) = (φ◦i)+(D(W)) is a complex with quasicoherent cohomology by 5.6" | 「由推论 \ref{cor:4.5.6}，后者是…」（缺等式） | 补「由定理 \ref{thm:4.5.3} 有 $\varphi_+(i_+(\mathcal{D}(\mathcal{W})))=(\varphi\circ i)_+(\mathcal{D}(\mathcal{W}))$，而由推论 \ref{cor:4.5.6}，后者是…」 | 原文有此等式，原译跳过中间一步，证明断链 | P2 |
| chap4.tex:842 | "exact by 1" | 引理 \ref{lem:4.4.5} | 命题 \ref{prop:4.6.1} | 原文「1」=本节 Prop 6.1（$\mathcal{D}_{Y\to X}$ 局部自由 ⇒ $\otimes$ 正合），非 4.4.5 | P2 |
| chap4.tex:865 | "exact by 1" | 引理 \ref{lem:4.4.5} | 命题 \ref{prop:4.6.1} | 同上 | P2 |
| chap4.tex:1064（Prop 4.8.3 证明） | "by 2, we can reduce … to the case of codimension one" | 「由前述可把证明归结为…」 | 「由引理 \ref{lem:4.8.2} 可把证明归结为…」 | 原文「2」=Lemma 8.2（$(i\circ j)^!\cong j^!\circ i^!$），正是逐层归结的依据 | P2 |
| chap4.tex:1216（Thm 4.8.13 证明 (i)） | "(i) follows immediately from 3, 10 and 12" | 引理 \ref{lem:4.8.6}、定理 \ref{thm:4.8.10} 与命题 \ref{prop:4.8.12} | 命题 \ref{prop:4.8.3}、定理 \ref{thm:4.8.10} 与命题 \ref{prop:4.8.12} | 原文「3」=Prop 8.3（$i^!$ 保持拟凝聚）；8.6 与本条无关 | P2 |
| chap4.tex:1235 | "the long exact sequence attached to …" | 附带 long exact 序列 | 附带的长正合序列 | 残留英文 | P2 |
| chap4.tex:1276 | "the long exact sequence" | 附带的 long exact 序列 | 附带的长正合序列 | 同上 | P2 |
| chap4.tex:1315（Thm 4.9.7 证明） | "From 3. and 6. …" | 「由前述可知」 | 「由定理 \ref{thm:4.9.3} 与命题 \ref{prop:4.9.6} 可知」 | 原文两处引用（3=Thm 9.3 三角等价；6=Prop 9.6）未译出 | P2 |
| chap4.tex:1354（Thm 4.9.9 证明） | "… has property (ii) by 8" | 由引理 \ref{lem:4.8.2} | 由定理 \ref{thm:4.9.8} | 原文「8」=Thm 9.8（$Ri^!$ 对复合），引理 8.2 讲的是 $i^!$，指错条 | P2 |
| chap4.tex:1378 | "Hence, by 7, …" | 再由前述 | 再由定理 \ref{thm:4.9.7} | 原文引用未译出 | P2 |
| chap4.tex:1436（Thm 4.10.2 证明，投影情形） | "Hence, by 1, (Z×S)×S X = Z×X" | 故由前述 | 故由引理 \ref{lem:4.10.1} | 原文「1」=Lemma 10.1（纤维积的基变换） | P2 |
| chap4.tex:1444 | "Hence, by 1, every fiber product …" | 故由前述 | 故由引理 \ref{lem:4.10.1} | 同上 | P2 |

## 四、P3（错别字 / 语病 / 排版）

| 位置 | 原文 | 原译 | 改为 | 理由 | 级别 |
|---|---|---|---|---|---|
| chap4.tex:1045 | "0 −→ Hom_{i−1(OX)}(OY, i−1(W))" | $\mathcal{O}\longrightarrow\operatorname{Hom}_{i^{-1}(\mathcal{O}_X)}(\cdots)$ | $0\longrightarrow\operatorname{Hom}_{i^{-1}(\mathcal{O}_X)}(\cdots)$ | pdftotext 把正合列首项 0 印成字母 O；照原文会读成层 $\mathcal{O}$ | P3 |

## 五、存疑（未改，记录备查）

1. **chap4.tex:168** — 原文 p107「by 3.7.(ii)」：指向不明（第 I 章 §3.7？本章 §3 无「7.(ii)」），译文照录「由 3.7.(ii)」，未改。
2. **chap4.tex:819** — 原文 p121「By 3.5. and 8.」：「8」无法确证（§6 的第 8 条是 Thm 6.8，讲紧化支撑，与本处「小邻域」的构造无直接关系），保留。
3. **chap4.tex:920** — 原文 p123 作 $\dim_Y X=\sup_{x\in Z}(\dim_x X)$，其中 $Z$ 应为 $Y$；译文已加译注「（原文如此，应为 $x\in Y$）」，保留。
4. **chap4.tex:93** — 原文 p105「by 4」；按内容（阶 $\le 0$ 的 $S$ 为函数）实为 Lemma 1.3（Lemma 1.4 是切映射 $\Phi$ 的存在唯一性），译文取 1.3，正确，仅记原文笔误。
5. **chap4.tex:498 / 503** — 原文两处「1」按同节编号即 4.3.1（Rem 3.1），已改指 4.3.1；但 3.1 讲的是开浸入 $i^+$ 为限制函子，作为「上述讨论」的引用略牵强，标存疑。
6. **chap4.tex:747（同句）** — 「设 $\mathcal{V}$ 是拟凝聚右 $\mathcal{D}_U$-模。则对任意拟凝聚右 $\mathcal{D}_U$-模 $\mathcal{V}$」重复一次；原文 p119 同样重复（"Let V be … for any quasicoherent right DU-module V"），据实保留。

另记（原文笔误/省略，译文处理正确，未改）：

- Thm 4.2.7(ii)：原文 p111 收敛对象印作 "(M)"，按谱序列应为 $(N)$，译文作 $(N)$，正确。
- chap4.tex:1489：原文 p137「By ...,」省略引用，译文补作「由引理 \ref{lem:4.9.10}」（$Ri^!\circ Rj_\bullet=0$），正确。
- p119 Thm 5.8 证明「generate … by [2, ??]」引用残缺，译文按「生成 $D^b_{qc}$」叙述，未补编号。
- chap4.tex:839「$(D^I;I\in\mathbb{Z}_+^n)$ 是自由 $R(Y)$-模 $\mathcal{D}_{Y\to X}$ 的一组基」：此处 §6 为闭浸入 $Y\subset X$，$\mathcal{D}_{Y\to X}=R(Y)\otimes_{R(X)}\mathcal{D}_X$，确为自由 $R(Y)$-模，**不是**笔误，无需改。

## 六、已核对无误的主要公式（抽样记录）

- $\mathcal{D}_{X\to Y}=\varphi^*\mathcal{D}_Y=\mathcal{O}_X\oplus\varphi^*\mathcal{J}_Y$、$\gamma_U(S)(f)=\alpha(S(f\otimes1))$、Lemma 1.1/1.3/1.4/1.5 的构造与证明。
- $\varphi_+=R\varphi_\bullet(\mathcal{V}^\cdot\otimes^L_{\mathcal{D}_X}\mathcal{D}_{X\to Y})$；投影公式 $\varphi_+(\mathcal{V}^\cdot\otimes^L_{\mathcal{D}_X}\mathcal{D}_{X\to Y})$、$L_p\varphi^+$、$\operatorname{Tor}^{-\!p}_{\mathcal{D}_Y}(\mathcal{D}_{X\to Y},\cdot)$ 的上下标。
- §3：同调维数 $\le 2\dim Y$、§3.6 交换图、§3.8 $\operatorname{Tor}^{\mathcal{D}_Y}_{-p}$、§3.11 $\mathcal{D}(D_{X\to Z})=\mathcal{D}(D_{X\to Y})\otimes^L_{\mathcal{D}_Y}\mathcal{D}(D_{Y\to Z})$。
- §6：$\mathcal{D}_{Y\to X}=R(Y)\otimes_{R(X)}\mathcal{D}_X$ 的基 $(D^I;I\in\{0\}\times\mathbb{Z}_+^{n-m})$、$i_+=Ri_\bullet(\mathcal{V}^\cdot\otimes_{\mathcal{D}_Y}\mathcal{D}_{Y\to X})$、$\operatorname{Ch}(i_+(\mathcal{V}))$ 与 $\dim_{p^{-1}(x)}$ 的维数公式。
- §8：$[E,f_j]=f_j$、$[E,D^I]=-|I|D^I$、$vE=\sum vf_jD^j$、$\operatorname{ord}$ 递减、$\Gamma_{[Y]}=i_+i^!$、$i^!\circ i_+\cong\operatorname{id}$、$i_+\circ i^!\cong\Gamma_{[Y]}$。
- §9：$\operatorname{cd}\Gamma_Y\le\dim X+1$、$R^pi^!=i^!H^p_Y$、$R\Gamma_Y\cong i_+\circ Ri^!$、$\operatorname{cd}\Gamma_Y\le\dim X-\dim Y$、§9.10 交换图。
- §10：$\omega$ 同构 $\mathcal{D}_{X\to Z}\cong\mathcal{D}_{X\to Y}\otimes_{\mathcal{D}_Y}\mathcal{D}_{Y\to Z}$、$p^!=Lp_+[-\dim S]$、$\varphi(X)\cap\psi(Y)=\varnothing\Rightarrow\psi^!\circ\varphi_+=0$。

## 七、统计

| 级别 | 条数 | 说明 |
|---|---|---|
| P1 | 4 | 272 Ext 下标、747 $\varphi_\bullet\to i_\bullet$、1005 补 $\dim$、1434 $\psi\to\varphi$ |
| P2 | 18 | 术语「正像→直像」（14 处计 1 条）、$L^p\to L_p$（4 处计 1 条）、交叉引用 13 条、残留英文 2 条、补等式 1 条、证明中引用补全 2 条 |
| P3 | 1 | 1045 正合列首项 $O\to 0$ |
| 存疑 | 6 | 168、819、920、93、498/503、747 重复句 |

- 改动均落在 `chap4.tex` 内（未动 `main.tex`，未改编号、未加 label、未用 annote）。
- 未编译（由主控统一编译）。
