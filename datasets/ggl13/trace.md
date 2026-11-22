# trace · 第 13 篇 Witten（arXiv:1108.3103v2，18 页）

决策记录。每条四栏：判断点 / 依据 / 结论与理由 / 事后确认。
「弯路」指先做错、后来自己发现并改正的判断。

## 1. 纳姆极点要不要单独立一张卡

- 判断点：p012 的 φᵢ=tᵢ/y、[t₁,t₂]=t₃ 是全文唯一一个能写出闭式解的地方，值不值得单独立卡？
- 依据：p012「We define an elliptic boundary condition by declaring that we will allow only solutions that are …」；同页把 tᵢ 说成「in the sense of Kostant」的主 𝔰𝔲(2) 子代数。
- 结论与理由：不单独立卡。库内 `gw06/concept/nahm-pole` 已经把「一阶极点 + 留数 [t₁,t₂]=t₃」讲完了，再立一张只会重复旧卡。改成把它放进 `nahm-pole-boundary-condition`，重点写本篇独有的两件事：它为什么是**四维方程的椭圆边界条件**，以及推广到一般 W 时为什么要 ad(E)≅TW 协变常值。
- 事后确认：维持。写完发现这张卡真正的信息量在「一般 W 的扭转」，极点本身只占一小节。

## 2. 页码一律用 PDF 页序

- 判断点：§2 该标 p.1–p.4 还是 p.2–p.5？草稿里先按纸面读到的印刷页码写，后来发现 `txt/13/` 的文件名是 p001–p018。
- 依据：`txt/13/p002.txt` 开头就是 §1/§2 的正文，而每页最后一行印着 1、2、3…；即 PDF 页 = 印刷页 + 1。
- 结论与理由：**这是弯路**。题目书和库里都规定用 PDF 页序，我第一版按印刷页写，全部 12 张卡的 `pages`、`anchor`、`locator` 都偏了一页。改法：anchor 一律写 `A p.5–6 §2`（PDF 页），不写印刷页；术语表的「首见页」同样用 PDF 页。
- 事后确认：已全量改正，并用 `verify_pages.py` 机器回查（它只认 `txt/pNNN.txt`，写错页会直接报「页码不符」）。

## 3. (2.14) 与 KW06 式 (3.29) 差一个 t 的符号

- 判断点：KW06 的推广 Bogomolny 方程是 (F−φ∧φ+tDφ)⁺=0、(F−φ∧φ−t⁻¹Dφ)⁻=0；本篇 (2.14) 写成 (F−φ∧φ)⁺=t(d_Aφ)⁺、(F−φ∧φ)⁻=−t⁻¹(d_Aφ)⁻，两边 t 的位置不同。是不是抄错了？
- 依据：p004 式 (2.14) 原文；`datasets/kw06/cards/derivations/one-parameter-family.json` 所引的 (3.29)。
- 结论与理由：不是笔误。把本篇的 φ 换成 −φ 就得到 KW06 的形式，二者只差一个约定；p013 也明说本篇在 t=1 时与 [4] 的方程一致，若真是符号错误这句话就不成立。因此**不登 errata**，改在 `t-family-elliptic-equations` 的 pitfalls 与推导卡第 5 步的 `provenance: C` 里写明「与 KW06 差 φ→−φ 的约定」。
- 事后确认：维持。最初已拟好一条 errata，核对 kw06 卡后撤回——这是本次最容易误伤原文的一处。

## 4. 概念卡从 9 张砍到 8 张

- 判断点：原计划给「Casson 不变量 / 平坦联络计数」单独立一张概念卡，再给「半稳定性」立一张。
- 依据：p008「we will categorify the Casson invariant」「In three dimensions, this is not an elliptic equation, but is part of a nonlinear elliptic complex」；p006 对半稳定性只有一句话（「requiring semistability」）。
- 结论与理由：两张都砍。Casson 这条线是推导卡 `casson-to-khovanov` 的主干，单独立卡会把同一条论证讲两遍；半稳定性在原文只有一句、没有定义也没有条件，立卡就是空话。半稳定性降为 `solution-count-jones` 的一条 pitfall。
- 事后确认：维持。8 张概念卡里没有一张是「只有定义 + 三条空话」的。

## 5. 「Bogomoly」是不是 OCR 假象

- 判断点：p015 印的是 extended Bogomoly equations，而 p008 同一概念作 Bogomolny。第一反应是 txt 抽取把 n 弄丢了，不该登 errata。
- 依据：p015 原文句；p008「Bogomolny equation」；p018 所引 [4] 即 Kapustin–Witten。
- 结论与理由：**这是弯路**。用 PyMuPDF 把 p015 那一行按 4 倍渲染裁出来（`external/p015_bogomoly.png`），字形清楚是 Bogomoly，没有 n——是原文排印错误，不是抽取错误。于是登 `errata.tsv` e3，置信度 high（同篇 p008 的反证 + 所引 [4] 的术语），并在 `reduced-equations-oper` 里挂 correction。
- 事后确认：维持。教训：牵涉单个字母的判断，先渲染再说话；txt 只能当索引用。

## 6. XREF.md 的「版本数 1」能不能直接用

- 判断点：`tools/xref.py` 生成的 XREF.md 写「版本数 1、初版 2011-08-15」，但 PDF 首页明明写 `arXiv:1108.3103v2 [math.GT] 2 Oct 2012`。
- 依据：p001 页眉；arXiv abs 页（v1 2011-08-15 / v2 2012-10-02，两版都是 52 KB，Comments 仍写 16 pp）。
- 结论与理由：工具抓漏了一个版本，不能照抄。notes 的「核对与勘误」里把它记为外部来源 X1 的一条**工具局限**（不是原文笔误，故不入 errata）：本篇 txt 是 v2、18 页；Comments 的「16 pp」是 v1 遗留，v1 与 v2 未逐页 diff。所有卡片按 v2 写。
- 事后确认：维持。这条也解释了为什么页数会与 arXiv 注释不一致。

## 7. excerpts 从 4 段砍到 3 段

- 判断点：初稿四段，第四段准备写 §4 前半「Casson 不变量 → Bogomolny 折叠」。
- 依据：p008–p009 的折叠论证；对照已写好的 `casson-to-khovanov` 推导卡。
- 结论与理由：砍。那段与推导卡 8 步里的前 4 步几乎逐句重合，摘录的价值是「给没读原文的人一条完整思路」，不是把卡片再讲一遍。保留三段：纲领（p2）、范畴化机制（p10）、投影内建（p17），正好覆盖「为什么—怎么做—最后到哪」。
- 事后确认：维持，三段汉字数 239 / 246 / 269，都在 150–400 区间。

## 8. p008 的逗号大写要不要登 errata

- 判断点：p008 有一句「not the Jones polynomial, This means」，逗号后误作大写 T。
- 依据：p008 该句原文；errata 的定位是「影响理解的笔误」。
- 结论与理由：不登。它不影响任何公式、术语或论证，登了会把 errata 变成校对清单；但也不能装作没看见，所以在 notes 的「核对与勘误」末尾用一句话记下「已知未登表」。
- 事后确认：维持。errata 最终 5 条，全部是会误导读者的拼写/编号错误。

## 9. 卡片 summary 里不放公式

- 判断点：summary 限 120 字符，最初想把 (2.14) 整式塞进去，觉得那样最准确。
- 依据：`lint_cards.py` 的 `text_len`（去 `$...$`、去空白后计字符数）；(2.14) 三条式子光字符就 60+。
- 结论与理由：不塞。summary 只写「是什么 + 为什么重要」，公式全部下沉到 `formulas` 数组（裸 LaTeX、不带 `$`，与 ggl19 范例一致）。理由：summary 是检索时第一眼看到的东西，塞公式既超限又难读。
- 事后确认：维持。12 张卡的 summary 全部 ≤120，无一条需要 lint 回退。

## 10. 卡标题怎么避开撞名

- 判断点：第 4 张卡想叫「Khovanov 同调」，但库内 `functoriality/concept/khovanov-homology` 已经占了这个名字。
- 依据：`tools/term_index.py check out/13_ggl13/cards` 报撞名；旧卡讲的是一般定义（Z×Z 双分级、Euler 特征=Jones），本篇讲的是「用五维方程的解造出来的候选链复形」。
- 结论与理由：标题改「候选 Khovanov 同调」（candidate 是原文自己的用词，p010「the candidate for Khovanov homology」），既避开撞名又没改变概念。术语表里仍沿用旧译名「Khovanov 同调」，并注明本文的 candidate 用法。
- 事后确认：维持。撞名检查最终 0 命中。

## 11. 推导卡 `casson-to-khovanov` 从 5 步加到 8 步

- 判断点：这条推导按「Casson → 折叠成 Bogomolny → φ₀→D/Ds → Floer」四步就写完了，最初只列 5 步。
- 依据：p008–p011；同一套「范畴化 = 加一维 + 把 φ₀ 换成 D/Ds」在 §4 里用了两次（先 Casson 后 Jones）。
- 结论与理由：加到 8 步，把两次使用分开写：第 1–4 步是 Casson 线（终点 Floer 上同调），第 5–8 步是对 Jones 重复同一手法（终点候选 Khovanov 同调）。理由：只写一次会让读者以为 Khovanov 那边是另一个构造，而原文的重点恰恰是「同一个手法用两次」。
- 事后确认：维持。8 步里第 5 步标 `provenance: B`（原文只说「同样地」，未逐句重述）。

## 12. 那条「large than」的置信度先写错了

- 判断点：p017「On a length scale large than 1/|c|」，显然应为 larger than，最初按 medium 登记。
- 依据：PDF p017 渲染图（`external/p017_large_than.png`）确为 large；除此之外只有语法判断（比较级），没有第二处独立的拼写依据。
- 结论与理由：**这是弯路**。BRIEF §9 的口径是「两处独立出处才 high，只有一处冲突记 low 存疑、卡片不改」；medium 是给「两处依据但其中一处较弱」的，这里不成立。已把 e4 降为 low，卡片 `knot-projection-coulomb` 的 correction 措辞本来就是「低置信存疑、正文不引用该句」，现在两边一致。
- 事后确认：维持。改完后 errata 的置信度分布是 high 4 / low 1。

## 13. 五维方程的椭圆性和等变 Euler 特征都只有断言

- 判断点：§4 说五维方程「是椭圆的」、说等变欧拉特征「等于 J(q;K,R)」，都没给证明。卡片要不要替作者补？
- 依据：p010–p011 原文只有断言与「the definition of the instanton number is subtle」这类限定；p011 明说这是 candidate。
- 结论与理由：不补。卡片 `khovanov-complex-candidate` 的定理条目用 `proof.status: "sketch"` + `gap_note`，写明「椭圆性与等变 Euler 的良定义在原文中只有断言」；notes 的「不懂/存疑」另列一条。理由：替作者补证明会把「候选」写成「已证」，这正是本库最该防的事。
- 事后确认：维持。这是我对本篇「诚实度」最在意的一处。

## 14. aₙ 的大 n 消失只是猜想

- 判断点：p007 说 aₙ 在 |n| 大时应当为 0（因为只有有限个瞬子数），但原文用了「presumably」。
- 依据：p007「the claim is that this function is the Jones polynomial」前后文；同页只给了解数为孤立非退化解时带符号计数的说明。
- 结论与理由：卡片里一律写「猜想/未证」，pitfalls 第一条就是「aₙ 的有限支撑没有证明，J(q;K,R) 作为幂级数的良定义依赖它」。不写成「已知有限支撑」。
- 事后确认：维持。

## 15. 一条 quote 是我「顺」出来的，不是原文

- 判断点：`knot-boundary-condition` 的第二条出处想说明「R 是 K 进入构造的唯一通道」，我凭记忆写成「it depends on the knot K and on the choice of a representation R of the Langlands」。
- 依据：p006 原文实际是「it depends on the choice of a knot (or link) K, and on the choice of a representation R of the Langlands or GNO dual group G∨ of G. In this description, this is the only way that K (or R) enters.」——我漏掉了「on the choice of a」，把两个分句缝成了一句。
- 结论与理由：**这是弯路**。`verify_pages.py --strict` 直接报「原文里搜不到这段 quote」，我改成逐字的「In this description, this is the only way that K (or R) enters」。理由：quote 必须是能在该页 txt 里检索到的连续片段，凭记忆缝句子看着通顺、机器一查就穿。
- 事后确认：改正后 40 条 A 类出处全部命中，问题 0 条。教训：quote 只能用「复制 + 截断」，不能手打。
