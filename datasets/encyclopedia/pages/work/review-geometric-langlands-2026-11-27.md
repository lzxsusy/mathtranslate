# 综述页独立审校报告（2026-11-27）

审校对象：

- 主文件 `pages/geometric-langlands.md`（399 行，v0.3，status draft）
- 配套页 `pages/kapustin-witten.md`（274 行）

路径约定（下文引用均按此缩写）：

- `PAGE` = `C:\Users\admin\Desktop\数译发布\gitee_shuyi\datasets\encyclopedia\pages`
- `L906` = `C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应`（法文逐页文本在 `工程文件\work\src\pNN.txt`，页眉 `906-NN` 为原文印刷页；中译注本 PDF 在 `成品\`）
- `FGV` = `C:\Users\admin\Downloads\t09_arxiv\math_0012255_pages.txt`（`<<<<< PAGE n >>>>>` 标 PDF 页，PDF 页 1 为标题页）
- `GA` = `C:\Users\admin\Downloads\t09_arxiv\math_0204081_pages.txt`（同上）
- `KW` = `C:\Users\admin\Downloads\_kw_audit`（逐页文本 `pages\pNNN.txt`，`p{印刷页+1}.txt`；全文 `full.txt`）
- `S1252` = `C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-45_Scholze布尔巴基1252几何Langlands的证明`（源码在 `源码\`）

## 结论（一句话 + 计数：critical/major/minor）

页面结构、逐字引文与主要归属（Drinfeld / FGV 猜想 / Gaitsgory 消没 / Laumon 合并）大体可靠，但物理侧有一处会误导读者的复结构错误，另有 2 处定义错误、1 处中译页码错误、1 处五部曲编年/归属错误；香蕉空间全程 403，未能对照。

**计数：critical 2 / major 3 / minor 9（共 14 条）。**

## 错误清单

| # | 位置（行号） | 原文摘录 | 问题 | 依据（文件:行 或 URL#page） | 建议改法 | 严重度 |
|---|---|---|---|---|---|---|
| 1 | `pages/geometric-langlands.md:332`；`pages/kapustin-witten.md:115,124` | 「$\Psi=\infty$ 时是复结构 $I$ 下的 B-模型」；配套页 115「二维理论是复结构 $I$ 下的 B-模型」、124「Wilson 算子在 $\Psi=\infty$（B-模型，$I$）」 | KW 原文：$\Psi=\infty$ 时是复结构 **$J$** 下的 B-模型。复结构 $I$ 的 B-模型是 KW 另一处（$q=0$ 轨道）的说法，不是 $\Psi=\infty$。配套页 130–132 自引又写 $J$，前后矛盾 | `KW/pages/p071.txt:28–38`（印刷 p.70）：「To get Ψ = ∞, we take t = i … The resulting model is the B-model in complex structure J. … a mirror pair in complex structure J」；`KW/full.txt:2686–2694`（印刷 p.62）的 $I$ 属 $q=0$ 轨道 | 主文件 332 的 $I$ 改 $J$；配套 115、124 同步改（124 的「B-模型，$I$」改「B-模型，$J$」）；保留 130–132 的正确引文 | critical |
| 2 | `pages/kapustin-witten.md:222`（并 273） | 「一般约化群、特征 $0$ 与特征 $p$ 的完整等价 … 由 Gaitsgory–Raskin 五部曲（2025a/b）证明」 | 五部曲是 I (2025b)、II–IV (2024)、V (2026)；2025a 是独立的正特征论文（2508.02237），不属五部曲。句中把「五部曲」与「2025a/b 两篇」混为一谈，读者会以为 char $p$ 由五部曲证明 | `S1252/源码/sections/s13-refs.tex:33`（2025a，2508.02237）、`:34`（2025b，2405.03599v3）、`:6,7,21`（2024 三篇）、`:35`（2026，2409.09856v3）；`S1252/源码/sections/s02-glc.tex:170` 只列五篇 | 改为「char $0$ 由五部曲（2024–2026）证明；char $p$ 由 Gaitsgory–Raskin 2025a（2508.02237）在 $p\gg0$、$p$ 非 $G$ 的挠素数的条件下证明」；273 行的年份同改 | critical |
| 3 | `pages/geometric-langlands.md:250` | 「$E^{(d)}$ 是 $X^{(d)}$ 上秩 $n^d$ 的局部系统（式 (1.3)）」 | 纤维秩随 $D$ 变化；$E^{(d)}$ 整体是可构造复形，只有限制到正则半单轨迹 $X^{(d)}_{\mathrm{rss}}$ 上才是秩 $n^d$ 的局部系统。照现文读会以为 $X^{(d)}$ 上处处有秩 $n^d$ 的局部系统 | `L906/工程文件/work/src/p09.txt:15–18`：「le rang de cette fibre varie avec D, mais que, au-dessus de l'ouvert X^{(d)}_rss, ce rang est constant et la restriction de E^{(d)} est un système local de rang n^d」；同页 20–23 行（引理 3.1） | 改为「$E^{(d)}$ 是可构造复形；它在 $X^{(d)}_{\mathrm{rss}}$ 上的限制才是秩 $n^d$ 的局部系统（式 (1.3) 给的是该限制的纤维）」 | major |
| 4 | `pages/geometric-langlands.md:395` | 「它成为反常层，是 $E^{(d)}$ 到 $\operatorname{Coh}^d_0$ 的中间延拓」 | 到 $\operatorname{Coh}^d_0$ 的中间延拓是 $\mathcal L^d_E=\det^*E^{(d)}$（定义 3.2）；$E^{(d)}[d]$ 是从 $X^{(d)}_{\mathrm{rss}}$ 到 $X^{(d)}$ 的中间延拓（引理 3.1）。两种延拓的靶不同 | `L906/工程文件/work/src/p09.txt:20–23`（引理 3.1）、`:26–33`（定义 3.2）、`:35–37`（$d$-平移拉回 $=E^{(d)}[d]$）；本页 253、255 行自述 | 改为「$E^{(d)}[d]$ 是 $E^{(d)}$ 从 $X^{(d)}_{\mathrm{rss}}$ 到 $X^{(d)}$ 的中间延拓；到 $\operatorname{Coh}^d_0$ 的中间延拓是 $\mathcal L^d_E=\det^*E^{(d)}$」 | major |
| 5 | `pages/geometric-langlands.md:172` | 「（Laumon 中译 p7 = 原文 p7）」 | 该段（定义 2.1 与 $S_2$-等变条件）在中译注本 PDF 第 6 页（页边 `906--7`），不在第 7 页；且与 146 行同一内容的「中译 p6 = 原文 p7」自相矛盾 | `SY02-46_..._中译注本.pdf` 第 6 页（pdftotext：第 6 页含 `906--7`、`S2 -等变的`、`定义 2.1`）；`L906/源码/main.tex:25` 说明边注 `906--NN` 对应原文页 | 改为「中译 p6 = 原文 p7」 | major |
| 6 | `pages/geometric-langlands.md:81` | 「弱形式（集合/双射）… 经典的类域论与 Drinfeld 的 $\operatorname{GL}(2)$ 工作大体处在这一层」 | 与本页 82 行（中形式 = 定理 2.2 的强度，而定理 2.2 含 $n=2$ 的 Drinfeld）及 314 行（$n=2$ 由 Drinfeld）矛盾：Drinfeld 1983 构造的是具体的 Hecke 特征层，属中形式；几何弱形式是存在性，不是集合间双射 | `pages/geometric-langlands.md:82,314`；`L906/工程文件/work/src/p08.txt:4–8`（定理 2.2 的归属句） | 把 Drinfeld 从中删去（或移到中形式）；弱形式改为「每个谱侧对象至少对应一个自守侧对象（存在性）」，不写「双射」 | minor |
| 7 | `pages/geometric-langlands.md:94` | 引文止于「…théorie cohomologique à coefficients dans $C$」 | 原文在 $C$ 后还有「pour la catégorie des schémas de type fini sur $k$」；截断处未加省略号，与页首「引文逐字」的说明不符 | `L906/工程文件/work/src/p02.txt:6–9` | 句末加「…」，或补全后半句 | minor |
| 8 | `pages/geometric-langlands.md:156` | 「Satake 是局部的（球面 Hecke 代数与 $\operatorname{Rep}(\hat G)$ 的等价）」 | 这是经典 Satake 同构；几何 Satake 是 $\mathrm{DMod}(\mathrm{Gr}_G)^{L^+G}\simeq\operatorname{Rep}({}^LG)$ 的幺半等价。用经典版本给「几何 Satake」下定义，读者会以为二者是同一句话 | `07_refs_nlab/pages/geometric_Satake_equivalence.md`（「$\mathrm{DMod}(\mathrm{Gr}_G)^{L^+G}\simeq\operatorname{Rep}({}^LG)$」）；本页 156 行同句已出现「几何 Satake」 | 改为「几何 Satake：$\mathrm{DMod}(\mathrm{Gr}_G)^{L^+G}\simeq\operatorname{Rep}({}^LG)$（其 Grothendieck 群给出经典 Satake 同构）」 | minor |
| 9 | `pages/geometric-langlands.md:235` | 「一般特征 $p>0$ 由 Gaitsgory 证明（[Ga]）」 | 底域正特征他确实处理；但他自限系数：特征 $0$，或 $\mathbb F_\ell$ 且 $\ell>d$。照现文读会以为任意系数均可 | `GA` PDF p.1（引言）：「we will be able to treat only the case of characteristic 0 coefficients, or … $\mathbb F_\ell$-coefficients when $\ell>d$」；`GA:119`（正特征底域） | 补「（系数特征 $0$，或 $\mathbb F_\ell$ 且 $\ell>d$）」 | minor |
| 10 | `pages/geometric-langlands.md:291` | 「推论 6.4 由此得到 $\operatorname{Aut}'_E$ 在各分支上不可约」 | Cor 6.4 的主语是 $K_{E,n}$，不是 $\operatorname{Aut}'_E$；二者只在开集上一致（引理 5.2） | `L906/工程文件/work/src/p15.txt`（COROLLAIRE 6.4：「La restriction de K_{E,n} à chaque composante connexe de V_n^∘ est un faisceau pervers irréductible」）；本页 282 行（引理 5.2） | 改为「$K_{E,n}$ 在各分支上不可约，从而 $\operatorname{Aut}'_E$ 在相应开集上不可约」 | minor |
| 11 | `pages/geometric-langlands.md:346`（并 332；`pages/kapustin-witten.md:186,188`） | 「$\Psi=h$ 时扭化为零，恰好是普通微分算子」 | $h$ 未定义；KW 原文 $h$ 是 $G$ 的对偶 Coxeter 数（典范线丛为 $\mathcal L^{-2h}$，$\Psi=h$ 时开弦代数是普通微分算子）。同页 332 的 $n_g$ 也未定义（配套页 70–74 才定义） | `KW/pages/p207.txt:32–36`（印刷 p.206）；`pages/kapustin-witten.md:70–74`（$n_g$ 的定义） | 首次出现处补「$h$ 为 $G$ 的对偶 Coxeter 数；$n_g$ 为 $S$-对偶的标度因子（见配套页 70–74）」 | minor |
| 12 | `pages/geometric-langlands.md:383` | 「正文 14 个 `{{entry:…}}` 链接」 | 实际真链接 **10** 个（64 行 2、156 行 2、197、218、308、364、365、367 行各 1）；383 行自身的 `{{entry:…}}` 是字面示例 | `grep -o "{{entry:" pages/geometric-langlands.md | wc -l` = 11（含 383 行示例），11 − 1 = 10 | 改为「10 个」 | minor |
| 13 | `pages/geometric-langlands.md:385` | 「第 7 节的『一般约化群 char 0』只给 Scholze 1252 的页码」 | §7（316 行）只给定理编号「Scholze 1252 定理 2.11/2.12」，未给页码；全文 grep「p.18」无命中 | `pages/geometric-langlands.md:316` | 改为「只给定理编号」，或补页码 p.18 | minor |
| 14 | `pages/kapustin-witten.md:273` | 「D. Gaitsgory, D. Kazhdan, et al.（GR 五部曲，2025a/b）」 | Kazhdan 不在五部曲作者之列（他是 2020a/b、2021 三篇前作的作者）；年份问题同第 2 条 | `S1252/源码/sections/s13-refs.tex:9,11,12`（Kazhdan 的三篇前作）、`:6,7,21,33,34,35`（五部曲与 2025a） | 删去 Kazhdan，或改注「含前作 Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky (2020–21)」 | minor |

## 需要作者决定的问题（不是错，但有歧义）

1. **$\hat G$ 与 ${}^LG$ 记号**：58、60、102 行用 $\hat G$，328、350、356 行用 ${}^LG$。在 $G=\operatorname{GL}(n)$ 时二者相同，但一般 $G$ 不同；建议全页统一为 ${}^LG$，只在 $G=\operatorname{GL}(n)$ 处注明 $\hat G={}^LG$。
2. **强形式的适用条件**：83 行把 $D(\operatorname{Bun}_G)\simeq\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{{}^LG})$ 说成「Gaitsgory–Raskin 工作的强度」，未写 char $0$；316 行已正确写出 char $p$ 需换成 $\operatorname{LocSys}'$。建议在 83 行加一句限定，避免与 316 行冲突。
3. **「Whittaker」术语**：308 行说「Whittaker 范畴」「特征层 = 特征函子的像」，而 Scholze 1252 用的是「谱投影子」「Whittaker 层」（`S1252/源码/sections/s07*.tex`、`s09*.tex`）。这两个说法是否等同、是否需要在页内定义，建议作者定夺。
4. **「中译 pN」的约定**：本页的「中译 pN」实际指中译 PDF 第 N 页，但中译注本同页常横跨 2–3 个原文页（如第 6 页含 906--6/7/8）。建议统一写成「中译 p6（原文 p7）」双标，或明确「中译 pN = PDF 第 N 页」。
5. **proper 反常层的定义位置**：定义在 §10（393 行），但 §6（291 行）已使用。是否前移到 §2 或 §6 首次出现处，或加词条链接（前 matter 已列 `geometry/perverse-sheaf`，但正文未链）。
6. **$C=\bar{\mathbb Q}_\ell$**：91 行写 $\ell$-进设定 $C=\bar{\mathbb Q}_\ell$，Laumon 原文（`p02.txt:20–22`）写 $C=\mathbb Q_\ell$。这是系数域约定差异，建议注明「Laumon 记 $C=\mathbb Q_\ell$，本文取代数闭包 $\bar{\mathbb Q}_\ell$」。

## nLab / 香蕉空间 对齐表

说明：香蕉空间两次抓取（`https://www.bananaspace.org/wiki/几何朗兰兹` 与站内搜索 URL）均返回 **HTTP 403**（Cloudflare），下表「香蕉空间」列一律记「未能核实（403）」，不作判断。nLab 用本地转储 `07_refs_nlab/pages/`（2026-04 至 2026-10 抓取，共 8 页）。

| 术语 | 本页 | nLab | 香蕉空间 | 判断 |
|---|---|---|---|---|
| 反常层 / perverse sheaf | 用「反常层」，§3 起直接使用，未在页内定义 | `perverse_sheaf.md`：「abelian subcategory of the constructible derived category」，标准定义 | 未能核实（403） | 本页用法与 nLab 一致；建议首次出现处给一句定义或链 `geometry/perverse-sheaf` |
| proper 反常层 | §10:393 定义为 $j_!L\to j_*L$ 同构，保留英文 proper | 本地 nLab 无「proper perverse sheaf」条目 | 未能核实（403） | 本页定义与 Laumon (0.2)（`p04.txt`）一致；nLab 无对应条目，不能据 nLab 判错 |
| Hecke 特征层 | 168–174 行：$E$ 不可约、$K$ 不可约、$H(K)\cong E\boxtimes K$、$S_2$-等变 | `Hecke_eigensheaf.md`：「taken to a tensor-multiple of itself under the integral transform induced by a Hecke correspondence」，无不可约要求 | 未能核实（403） | 本页采 Laumon 窄定义；180–183 行已辨明 FGV 宽定义，与 nLab 的宽泛表述不冲突（nLab 未含 $S_2$/不可约） |
| Hecke 对应 / Hecke 叠 | 121–142 行：三元组 $(x,L,L'\subset L)$ 的叠，两投影相对维数 $n-1$ 与 $n$ | `Hecke_correspondence.md`：参数化「pairs of bundles with a modification」，两投影 | 未能核实（403） | 一致 |
| 局部系统 | 102 行：基本群的表示 / 局部常值层 | `local_system.md`：局部常值层、基本群胚、Riemann–Hilbert 对应平坦联络 | 未能核实（403） | 一致 |
| 对偶群 | 58、60、328、350 行：$\hat G$ 与 ${}^LG$ 混用 | `Langlands_dual_group.md`：仅 13 行参考文献，无定义 | 未能核实（403） | 本页内部记号不统一（见「待作者决定」1）；nLab 无可比定义 |
| 几何 Satake | 156 行：「球面 Hecke 代数与 $\operatorname{Rep}(\hat G)$ 的等价」 | `geometric_Satake_equivalence.md`：$\mathrm{DMod}(\mathrm{Gr}_G)^{L^+G}\simeq\operatorname{Rep}({}^LG)$ 的对称幺半等价 | 未能核实（403） | **不一致**：本页写的是经典 Satake 同构（见错误 8） |
| $\operatorname{Bun}_G$ / $\operatorname{LocSys}$ | 55–60 行；83 行强形式 | `geometric_Langlands_correspondence.md`：$\operatorname{QCoh}(\operatorname{Loc}_{{}^LG})\simeq\operatorname{DMod}(\operatorname{Bun}_G)$（BD–Frenkel），Arinkin–Gaitsgory 精化为 $\operatorname{IndCoh}_{\mathrm{Nilp}}$ | 未能核实（403） | 一致（本页 83 行即此精化形式） |
| $\Psi$ 与复结构 | 332 行：$\Psi=\infty$ → 复结构 $I$ 的 B-模型 | `Kapustin-Witten_TQFT.md`：$I$ = Higgs 丛，$J,K$ = 局部系统；$S$-对偶把 $M_H({}^LG)$ 上 $J$ 的 B-膜与 $M_H(G)$ 上 $K$ 的 A-膜互换 | 未能核实（403） | **不一致**：nLab 与 KW 原文一致（$J$），本页 332 行错（见错误 1） |
| c.c. 膜 | 346 行：$(A,B,A)$ 型，c.c. 膜 | `Kapustin-Witten_TQFT.md` 称「canonical **isotropic** brane」（KW 原文 coisotropic） | 未能核实（403） | 本页正确（$(A,B,A)$、coisotropic）；nLab 用词有误，不能据 nLab 改本页 |

## 未能核实的项

1. **香蕉空间全部术语**：两个 URL 均 HTTP 403（Cloudflare 拦截），无法核对任何中文用法；对齐表该列只能记「未能核实（403）」。是否有对应词条本身也未知。
2. **nLab 线上全集**：本地转储只有 8 页（geometric Langlands、Hecke eigensheaf、Hecke correspondence、perverse sheaf、local system、Langlands dual group、geometric Satake、KW TQFT），未核对线上是否另有「proper perverse sheaf」「Whittaker」等条目。
3. **Scholze 1252 定理 2.11 的 Betti/étale 覆盖**：`s02-glc.tex:172–174` 只说三种设定均成立，未逐篇追到原始论文的证明来源。
4. **Raskin 讲义定理 3.3.1 的英文原稿页码**：中译注本边注 p.10 已核，未对英文 PDF 逐页复核（若需可补）。
