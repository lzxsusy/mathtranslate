# 《K 理论十八讲》中文译注本 —— 交付说明

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 底本：Ioannis P. Zois, *18 Lectures on K-Theory*, arXiv:1008.1346v1 [math.KT]，2010 年 8 月，137 页（Letter）。
> 本译注本由 DeepSeek Harness 多智能体流程完成：1 名 Lead + 10 名译者分块翻译（Lead 兼译 pp.4–7 引言与 pp.134–137 参考文献），
> 随后 8 名译者交叉互检（每人校别人的一块），全部改单由 Lead 以 exact-match patch 落改，
> 最后真编译 3 遍并回读成品 PDF 逐项验收。

## 1. 底本信息与页码映射

| 项目 | 实测值 |
|---|---|
| 标题 | 18 Lectures on K-Theory |
| 作者 | Ioannis P. Zois（Athens） |
| 日期 | arXiv v1：2010-08-07；PDF 由 arXiv 于 2024-11-26 重编译 |
| 来源 | `https://arxiv.org/abs/1008.1346`（arXiv 非独占许可） |
| 原 PDF | 588,443 bytes；`拓扑K理论讲义\pdfs\04_Zois_18_Lectures_on_K-Theory_2010.pdf`（同一文件） |
| 原 PDF 页数 | **137 页**（Letter，612×792 pt；dvips + Ghostscript） |
| **页码对应** | **PDF 页号 = 原文印刷页码（偏移 0）** |
| 结构 | 22 个 `\section`：拓扑 K 6 讲（§2–7）+ 解析 K 6 讲（§9–14）+ 高阶代数 K 6 讲（§16–21）+ 附录（§22）；§1/§8/§15 为三支总起 |
| 编号公式 | **0 条**（全文右栏 `(x.y)` 扫描为 0；原文展示式一律居中不编号） |
| 图 / 表 | **0 图 / 0 表**（位图 0 张；正文无 Figure/Table 引用） |
| 编号定理类 | 定义 55、命题 14、引理 19、定理 26、推论 12、注 3、断言 3（共 132 条，**每个 section 内从 1 重编号**，与原文一致） |
| 展示式 | 592 处，全部 LaTeX 重排；其中 30 个交换图用 Ti*k*Z 重画、31 个矩阵用 `pmatrix`、4 组分段式用 `cases`，**无一处截图** |
| 参考文献 | pp.134–137，共 **40 条**，保留英文原貌（学术惯例不译） |

译文在每一起始原文页处有注释 `% [原文 p.N]`（N = PDF 页号 = 印刷页号），便于逐页对照。
成品为 A4 纸（原文 Letter），故成品页数（86 页）与原文页数（137 页）不同：原文 137 页中 pp.1–3 为标题页与目录（不逐字翻译），
成品第 1–4 页依次是封面、译者说明、目录（罗马数字页码区），正文从成品第 5 页开始。

## 2. 结构清单

```
封面
译者说明
目录
引言与背景                                    （原文 pp.4–7）
 1  拓扑 K 理论                                （原文 p.8）
 2  第一讲（向量丛的拓扑预备）                  （原文 pp.8–27）
 3  第二讲（同伦、Bott 周期性与上同调性质）      （原文 pp.28–33）
 4  第三讲（乘积与 Bott 周期性的再审视）          （原文 pp.34–39）
 5  第四讲（Chern 特征与 Chern 类）              （原文 pp.40–45）
 6  第五讲（K 理论中的运算、对称积与 Adams 运算） （原文 pp.46–52）
 7  第六讲（Adams 运算的应用：Hopf 不变量为 1 的映射的不存在性）（原文 pp.53–55）
 8  解析 K 理论（K-同调）                        （原文 p.56）
 9  第一讲（泛函分析的一些预备，Fredholm 算子的指标）（原文 pp.56–62）
10  第二讲（Toeplitz 算子的指标、绕数与 K-同调）  （原文 pp.63–67）
11  第三讲（斜积与 K 理论和 K-同调之间的配对）    （原文 pp.68–71）
12  第四讲（Bott 周期性）                        （原文 pp.72–75）
13  第五讲（Banach 代数与 C*-代数的 K 理论）      （原文 pp.76–81）
14  第六讲（C*-代数扩张与 K-同调）                （原文 pp.82–86）
15  高阶代数 K 理论                              （原文 pp.87–88）
16  第一讲（代数预备与 Grothendieck 群）          （原文 pp.89–98）
17  第二讲（Whitehead 群与 Steinberg 群）         （原文 pp.99–103）
18  第三讲（群的中心扩张）                        （原文 pp.104–108）
19  第四讲（分类空间与群（上）同调）              （原文 pp.109–113）
20  第五讲（+ 构造与一般 K 群的定义）             （原文 pp.114–120）
21  第六讲（若干定理与例子）                      （原文 pp.121–126）
22  附录                                        （原文 pp.127–133）
参考文献                                        （原文 pp.134–137，英文原貌，40 条）
```

## 3. 编译方法

```powershell
powershell -ExecutionPolicy Bypass -File build.ps1
```

- 引擎：**LuaLaTeX ×3**（`ctex` 自动取系统中文字体，无需 fontconfig / `\setCJKmainfont`）。
- 本机实测两条硬约束（同《学术PDF翻译_标准作业手册 v2》M2）：**LuaTeX 不能写非 ASCII 路径与 Desktop**，
  故 `build.ps1` 先把 `src/*.tex`、`src/chunks/` 镜像到 ASCII 可写目录
  （默认 `<本地路径>`），把 `TMP`/`TEMP` 指向可写目录，
  编译成功后把 `main.pdf` 拷回 `src\main.pdf`，并打印 log 统计。
- 依赖宏包：`ctex`、`amsmath/amssymb/amsthm/mathtools`、`bm`、`graphicx`、`geometry`、`xcolor`、
  `enumitem`、`booktabs`、`array`、`multicol`、`fancyhdr`、`caption`、`tikz`（含 `cd` 库）、`hyperref`。
- 本次真编译结果（见 `compile.log`）：**LuaLaTeX ×3，0 error / 0 undefined / 0 missing character / 0 overfull**。

## 4. 译校体例

- **正文**：忠实逐段翻译，不增不减；原文笔误照译，仅在 `% [Tutor Note: …]` 批注中指出并给出正确形式。
- **定理类**：原文的编号定义/命题/引理/定理/推论/注/断言一律**手工给号**（`\begin{defn}{1}` 等），
  号数与原文逐条对应（**原文每个 section 内从 1 重新编号**，译文照此；原文的重号/异体号照排，不"统一"）。
  中文版正文用**直立体**（原文斜体是西文排版习惯，中文不用斜体）。
- **公式**：原文无编号公式，译本亦无（不使用 `\tag`）；全部展示式按 200 dpi 原页图逐符号重排，
  矩阵用 `pmatrix`、分段函数用 `cases`、交换图（30 处）用 `tikzcd`，**无一处截图**。
- **文献引用**：`[Atiyah]`、`[Bott]` 等照抄英文方括号，不改 `\cite`、不译键名。
- **参考文献**：保留英文原貌（学术惯例），按原文逐条转录 40 条。
- **批注**：`% [Tutor Note: …]` 为译者批注，**不进入排版**，全部汇总于随附《译注汇总.md》。
  内容为可验证的易错点、补出的省略论证、原文笔误与判断依据、术语首现英文原词。本次共 **206 条**。
- **术语**：`work/glossary.tsv` 冻结（约 150 条），全稿统一（如：vector bundle → 向量丛、clutching function → 粘合函数、
  Bott periodicity → Bott 周期性、Grothendieck group → Grothendieck 群、Adams operations → Adams 运算、
  K-homology → K-同调、C*-algebra → C\*-代数、Whitehead group → Whitehead 群）。
- **符号**：$K(X)$、$\wt K(X)$、$\Vect_k(X)$、$\mathrm{Gr}(M)$ 等按页图规范展开（原文的紧凑写法 `KX`、`˜KX` 等为排版压缩，不是不同记号）；算子名按原文大小写取正体（$\operatorname{Im},\operatorname{Ker},\operatorname{Ind},\operatorname{coker}$），原文的斜体是西文排版习惯。\n- **术语归一**：通稿时统一了「万有覆盖／万有中心扩张」（原文 universal covering / universal central extension），并把正文中的“K 理论”统一为直排（与节标题、glossary 一致）。
- **紧凑人名/术语**：`GLA`、`EA`、`StA` 等按页图展开为 $\GL(A)$、$E(A)$、$\mathrm{St}(A)$（见 TIMELINE 裁决）。

## 5. 原文笔误登记表

以下疑点均由译者在正文中**照原样翻译**、并在批注中指出；登记前均按纪律用 500–800 dpi 裁图复核原文。
（本表摘自各块回执，按页码排序；完整清单见《译注汇总.md》与各块批注。）

| 序号 | 页 | 原文（疑） | 说明 / 正确形式 |
|---|---|---|---|
| 1 | p.4 | "the the Grothendieck Group"（p.3 目录同） | "the" 重复 |
| 2 | p.5 | "Eilenberg-Steenroad" | → Eilenberg–Steenrod |
| 3 | p.5 | "Rordam, M. and Rrdam, M."（p.135） | 应为 Rørdam |
| 4 | p.6 | "Birckoﬀ" | 应为 Birckhoff（MacLane–Birkhoff《Algebra》） |
| 5 | p.8 | "the two most famous applications … is" | 主谓不一致，应为 are |
| 6 | p.8 | "clasic"；"Mobious" | → classic；Möbius |
| 7 | p.9 | "the field of real $\R$" | 漏 "numbers" |
| 8 | p.13 | "Clearly $s$ is continuous of all the $a_i$ functions are." | of → if |
| 9 | p.15 | "compelx" | → complex |
| 10 | p.16 | "isomorhisms" | → isomorphisms |
| 11 | p.18 | "Its customarily to denote $KX$ and $KOX$ and the complex and the real case respectively" | 语序与 Its→It is |
| 12 | p.19 | "honest real vector bundles" | 与本章"复向量丛"约定不符，疑沿用实情形说法 |
| 13 | p.21 | 引理 2 事实 (i) "on each slice $X\times\{x\}\times\C^n$" | 应为 $X\times\{c\}\times\C^n$ |
| 14 | p.22 | "grapf" | → graph |
| 15 | p.23 | "One can gine a topology"；"the $k$-tuples of of orthonormal" | → give；衍一 of |
| 16 | p.24 | "canonical $n$-dim vector bundles over $G_k(\C^n)$"；"condtition" | 应为 $k$ 维；condition |
| 17 | p.28 | "stably isomorphism classes"；定义 2 把约化 K 群说成"集合" | 表述不严谨 |
| 18 | p.28 | 维数映射写成 $X\to\Z$ | 应为 $K(X)\to\Z$ |
| 19 | p.31 | "because Grassmannians are contractible" | **数学错误**：$G_k(\C^n)$ 是紧复流形，正确理由是单连通（同页下文自己写 $\pi_2(G_k(\C^n))=\Z$） |
| 20 | p.34 | "Eilenberg-Steenroad" | → Eilenberg–Steenrod |
| 21 | p.39 | $\SO_N$ 同伦群表最后一行重复 $i\equiv1(8)$、漏 $i\equiv0(8)$ | 正确：$\pi_i(\SO)=\Z/2$ 当 $i\equiv0,1\pmod 8$ |
| 22 | p.39 | 公式末 ", $N>2n+2)$"、$\GL_N(\C))$ 多右括号；"onviously"、"orhtogonal" | 排印讹误 |
| 23 | p.40 | 定理 1 的 $H^{dd}(X;\Q)$ | 应为 $H^{odd}$（本讲开头与 p.46 复述均为 odd） |
| 24 | p.41 | $c_1(L_1\otimes L_2)=c_1L_1+c_2L_2$ | 应为 $c_1L_1+c_1L_2$（线丛高次 Chern 类为 0）；"duall"→dual |
| 25 | p.42 | "Kunneth"、"Mayer-Vietories"；引理 2 证明"$f_1$ is injective by Lemma 1" | → Künneth、Mayer–Vietoris；应为 $f_1^*$ 单射，依据是定理 2 |
| 26 | p.43 | "Chen character"、"ommit" | → Chern、omit |
| 27 | p.45 | "comutes" | → commutes |
| 28 | p.46 | 外幂置换项 $x\otimes_{\sigma(1)}x\otimes\ldots$ | 应为 $x_{\sigma(1)}\otimes x_{\sigma(2)}\otimes\ldots\otimes x_{\sigma(k)}$；$\Vect(\xi)$ 应为 $\Vect(X)$ |
| 29 | p.47 | $c_k:\Vect(X)\to H^{ev}(X;\Q)$ | 靶应为 $H^{2k}$ |
| 30 | p.49 | $\Psi_t$ 定义中的 $\wedge_t$ | 应为 $\wedge_{-t}$（与 p.51 的 $1+\frac{tL}{1-tL}$ 对照） |
| 31 | p.50 | "integral multiplets"；例中 $3\wedge^2$、一般式 $k\wedge^2$ | → multiples；应为 $3\wedge^3$、$k\wedge^k$（Newton 恒等式） |
| 32 | p.51 | $(\wedge_t(x)\wedge_{-t}(y))$ 第一因子；"propety" | 应为 $\wedge_{-t}(x)$；property |
| 33 | p.52 | "Then the map … where $S^4=S^2\wedge S^2$" | 原文为残句（缺主句），照译不补 |
| 34 | p.54 | "obtain taht"；p.55 "Caley numbers"、"there no other such maps"、"the group (U(1)" | → that；Cayley；缺 are；多左括号 |
| 35 | p.57 | "linear opearator" | → operator |
| 36 | p.59 | 证明中 $S:(\im T)\to(\im T)^\perp$ | 靶空间应为 $(\ker T)^\perp$ |
| 37 | p.60 | $\|Tx\|\ge\frac{1}{2\|S\|}x$；定义 5 "If $\in\mathrm{Fred}(H)$" | 漏 $\|x\|$；缺主语 $T$ |
| 38 | p.61 | $\ind(Q_nT_{t_0})=\ind T_{t_0}+m$ 的 $m$ | 原文未定义，照排 |
| 39 | p.68 | 定义 2 "A -cycle" | 短横线前缺 $K$，应为 A $K$-cycle |
| 40 | p.69 | "Degenerat"；"where $C(X)$ acts on ."；"$\mathrm{Fred}(P,H)$"；"codimesnion" | → Degenerate；漏 $H$；应为 $\mathrm{Fred}(H)$；codimension |
| 41 | p.69–70 | "$O\oplus\Ker$" 的 $O$ | 按上下文应为零空间 $0$ |
| 42 | p.70 | 定理 2 $[X,\mathrm{Fred}^S(H)]\to K^0(Y)$ | 定义域 $X$ 与值域 $Y$ 不一致，按证明应为 $[Y,\dots]$ |
| 43 | p.71 | "contratible"；"$GLH$" | → contractible；$\GL(H)$ |
| 44 | p.76 | 例 d 的 $g^*=\bar g$ | 与上一行 $\|f\|=\sup|f|$ 的 $f$ 记号不一致 |
| 45 | p.84 | 定理 1 署名 "Averson" | 应为 Arveson（W. B. Arveson, 1969） |
| 46 | p.86 | 末式 $K_1X=BDF(X)=\Ext(C(X))=\Hom(K^{-1}X;\Z)$ | 中间商位置的等号只在"$X$ 为多面体"时成立（p.85 已声明） |
| 47 | p.87 | "trully ingeneous"；"this later assumption" | → truly ingenious；latter |
| 48 | p.88 | "mudulo torsion" | → modulo（引号方向亦反） |
| 49 | p.89 | "the the Grothendieck Group"；"abreviated"；"projctive"；把 $\End_F(F^\infty)$ 称作 "a module" | 重复 the；→ abbreviated、projective；实为环（IBP 经典反例） |
| 50 | p.91–92 | "Iso($P_A$) )" 多右括号；"a+b=nd_0" | → $na_0$ |
| 51 | p.93 | "integral quotient"；"[F, Q]"；"excercise" | → integral closure；$[F:\Q]$；exercise |
| 52 | p.95 | "be to complex vector bundles"；"in an neighborhood" | → two；a |
| 53 | p.96–97 | "Propositon"；"thy" | → Proposition；they |
| 54 | p.98 | "Since $f^2=f$, then $E=\Ker f=\mathrm{Im}(1-f)$" | 与同段 $E=\mathrm{Im}f$ 矛盾：幂等有 $\mathrm{Im}f=\Ker(1-f)$，应为 $E=\Ker(1-f)$ |
| 55 | p.101 | diag 换位子式第三因子 $[\mathrm{diag}(a^{-1},a^{-1},1)]^{-1}$ | 应为 $[\mathrm{diag}(a,a^{-1},1)]^{-1}$ |
| 56 | p.105 | "$cy_2y'(cy_2)'y'^{-1}$" | $(cy_2)'$ 应为 $(cy_2)^{-1}$ |
| 57 | p.110 | $\mathrm{id}\in\Hom(H_2G,H_1G)$ | 应为 $\Hom(H_2G,H_2G)$（完美群时 $H_1G=0$） |
| 58 | p.113 | "Poincre duality"；$S_3\to\SO_3$；$\pi_0(O_3)=\SO_3$；$K^{-1}O(pt)$ | → Poincaré；$S^3$；$\pi_0(O_3)=\Z_2$；$KO^{-1}(\mathrm{pt})$ |
| 59 | p.117 | "Reacall"；"Eilenberg-McLane" | → Recall；Eilenberg–MacLane |
| 60 | p.123 | "shalll"；$\mu(x,x_0)=x_0$ | → shall；按 H-空间单位元公理应为 $=x$ |
| 61 | p.125 | $\dim_\Q[K_n\Z\otimes\Q]=\Z$ | 维数应为 1（$K_{4k+1}\Z\otimes\Q\cong\Q$） |
| 62 | p.126 | "the later groups" | → latter |
| 63 | p.127 | "background meterial" | → material |
| 64 | p.129 | 万有系数定理两处 $\Tor(H_{i-1}(X;A),A)$ | 标准形式应为 $\Tor(H_{i-1}(X;\Z),A)$ |
| 65 | p.131 | "to kill of the remaining homotopy"；"representations of homology with $G$ coefficients" | → kill off；表示的是**上**同调 $H^n(X;G)$ |
| 66 | p.132 | "seperates points"；Gelfand 定理 "arrows the homeomorphisms among them" | → separates；按 Gelfand 对偶应为**连续映射**（同胚对应 \*-同构） |
| 67 | p.84 | 定理 1 证明末式 $\phi_{11}(xx^*)=\phi_{11}(x)\phi_{11}(x^*)+\phi_{12}(x)\phi_{12}(x^*)$ | 按分块矩阵乘法的 $(1,1)$ 元应为 $\phi_{12}(x)\phi_{21}(x^*)$（页图确印作 $\phi_{12}\cdot\phi_{12}$） |
| 68 | p.119 | $i_*:H_*(X,i^*L)\to H_*(X,L)$ | 右端应为 $H_*(X^+,L)$（对照同页 $H_*(B\GL A,L)\simeq H_*(B\GL A^+,L)$） |
| 69 | p.128 | "(lader)" | 应为 ladder（梯子） |

**非笔误（已澄清，避免误登记）**：文字层中的 `ﬁ`/`ﬂ`/`ﬀ` 连字是抽取问题（`Deﬁnition` 实为 Definition），
`CW − complex` 是原文把 "CW-complex" 排成数学模式的排版习惯，均非错字；
原文多处 `Cardiﬀ`、`oﬀ` 之类只是连字字形，印刷无误。

## 6. 统计

| 项目 | 数值 |
|---|---|
| 原 PDF 页数 | 137（Letter） |
| 成品 PDF 页数 | **86**（A4；封面 + 译者说明 + 目录 + 正文 82 页） |
| 章节 | 22 个 `\section`（三支各 6 讲 + 附录），编号 1–22 与原文一致 |
| 编号定理类 | **132**：定义 55 + 命题 14 + 引理 19 + 定理 26 + 推论 12 + 注 3 + 断言 3；证明 55 处 |
| 编号公式 | **0**（原文亦 0；`check.py`：TAG 禁用扫描 0） |
| 图 / 表 / 脚注 | 0 / 0 / 0 |
| 展示式 | **592** 处（`\[ … \]`），全部 LaTeX 重排；tikzcd 30、pmatrix 31、cases 4，**无一处截图** |
| 参考文献 | 40 条（英文原貌，pp.134–137） |
| Tutor Note 批注 | **206 条**（见《译注汇总.md》；按文件：c-intro 1、c-refs 1、tr01a 29、tr02a 15、tr03a 35、tr04a 15、tr05a 19、tr06a 22、tr07a 20、tr08a 21、tr09a 16、tr10a 12） |
| 原文笔误登记 | **69 项**（见 §5） |
| 分工 | Lead pp.1–7（封面/目录/引言）+ pp.134–137；tr-01 pp.8–27；tr-02 28–39；tr-03 40–52；tr-04 53–62 与 114–126；tr-05 63–75；tr-06 76–86 与 127–133；tr-07 87–98；tr-08 99–113 |
| 交叉校对 | **8 轮**（tr-01 校 tr08a、tr-02 校 tr06a、tr-03 校 tr07a、tr-04 校 tr10a、tr-05 校 tr03a、tr-06 校 tr09a、tr-07 校 tr04a、tr-08 校 tr02a），报告见 `work/review/*.md`；共 **20 条「必须改」全部落改**（另取舍 30+ 条「可选改」），Lead 复跑 `check.py` + 真编译 + 成品回读 |
| 编译 | LuaLaTeX ×3：**0 error / 0 undefined / 0 missing character / 0 overfull** |
| 成品回读 | 22/22 节标题、参考文献、字体全部子集嵌入、无「??」/残留占位 —— 均通过（`verify_pdf.py`） |

## 7. 已知偏差与限制

1. **中文定理正文为直立体**：原文用斜体（西文排版惯例），中文无对等的斜体语义，故按中文习惯排直立体；
   定理编号、标题层级与原文一一对应。
2. **页码体系**：成品 A4、原文 Letter，页数不同（86 vs 137）。原文位置一律以源码 `% [原文 p.N]` 注释标记，
   成品页码与原文页码**不逐页对应**。
3. **参考文献**：40 条按原文逐条**手工转录**，保留英文原貌，未逐条校对（条目本身简短）；
   其中两处原文拼写已登记在 §5（[17] Rrdam、[16] "an Theory" 等）。
4. **图示**：原文 0 图 0 表；文中 30 处交换图用 Ti*k*Z 重画，箭头样式、标签位置与原图**略有差异**（不改变内容）。
5. **原文笔误照译**：§5 的 69 项一律按原样排，仅在批注中给出正确形式；不做"顺手修正"。
6. **符号展开**：原文的紧凑写法（`KX`、`˜KX`、`V ect`、`GLA`、`BGLA` 等）按页图规范化为 $K(X)$、$\wt K(X)$、$\Vect$、$\GL(A)$、$B\GL(A)$；这属于排版规范化，不是记号改动。
7. **定理类重号**：原文 §9 内有两个「定理 1」（p.56 与 p.59），§13 有「定义 1′、2′」；译文照原文保留，未重排。
8. **术语**：个别译名可能有更常见的替代（如 clutching function → 粘合函数，也有「过渡函数」的译法），全稿以 `work/glossary.tsv` 为准。
9. **未做**：原文 pp.1–3 的标题页与目录未逐字翻译（按惯例以译本封面/目录代替）；原文无习题、无脚注，译本亦无；未增补任何原文没有的内容。

## 8. 版权声明

原文 © Ioannis P. Zois，2010；arXiv:1008.1346（arXiv 非独占许可，仅供学术研究使用）。
本译注本为个人学习研究之用，**不用于商业用途**；原文版权归原作者所有，如需引用或再分发请以原文为准。
