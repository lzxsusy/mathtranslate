# R2 独立审校报告：§5–§7、附录 A/B/C、front matter

审校对象：`datasets/encyclopedia/pages/geometric-langlands.md`（745 行，只读未改）
审校范围：front matter（1–115）、§5 证明地图（441–546）、§6 证明细节（547–586）、§7 已知/未知（587–641）、附录 A/B/C（642–744）。
证据源与页码约定：

- SCH26 = Scholze, Bourbaki 1252 中译，`===== PAGE n =====` 的 n 即引用页码（页边 `1252--N` 是原版页，未混用）。
- CL23 = 陈麟讲义中译，**书页 = PDF 页 − 5**（用译注「书p.N」与目录互证）。
- LAU02 = Laumon 906 中译，引用 `906--N`（页边原书页）。
- BZ26 = 底本 `full.txt`，`===== PAGE n =====` 的 n 即页码。
- 资料卡、百科词条、形式化卡按任务给的路径逐个读；`sha256` 前 16 位用 Python 比对。
- 机械检查复跑：`check_survey.py geometric-langlands.md` → `cards: 60 unique / 95 refs; missing 0`；`local links checked: 73; dead 0`；`citation markers: 196`；`OK`（entries 一项该脚本报 0，见 P2-21）。

## 结论摘要

1. 主干引文质量高：68 条〔…〕里 51 条页码与节号完全对得上；char p 的两个条件（p.14 定理 2.12+脚注 15、p.16 定理 3.4）都落在正确页码，§7 的表述与原文一致。
2. 五篇论文的 arXiv 号**已获双证**：SCH26 p.41–44 书目与 CL23 书目同时给出 I–V 五个号，页面「II/III/IV 待核」可以撤掉（见「已证」条）。
3. 两处实质内容与底本相反：行 571 把 Beilinson–Drinfeld 1996 说成「目前最一般的构造」（原文强调 opers 只是半维子簇，一般参数要 [FG09a]）；行 602 把 Dolbeault 的 `generically`（通有）读成「一般情形」。
4. 附录 C 有两处依赖方向与 §5 正文相反（II→I、char p→char 0 主定理），且缺 4 类边（I→II、II→III、II→IV 及 DG16/FR/BKS22 三条工具边）。
5. front matter 的 `compiled_from` 只有 39 条（任务预期 60）；正文引用的 22 张卡未登记，另 1 张登记卡从未在正文出现。附录 B 与正文的集合也差一张（多 relative-langlands、漏 sy0246/vanishing-theorem）。

## 一、总表

| 项目 | 核对量 | 正确/一致 | 错页或错节 | 内容不符 | 无依据 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 〔…〕引文（441–745） | 68 | 51 | 14 | 2 | 1 | 错节多为 BZ26 p.26 §6→§5.5；错页 4 处 |
| §5.2 十二节页范围 | 12 | 9 | 3（§2/§3/§4 各少一页） | 0 | 0 | 与页面自身「边界重叠」惯例不一致 |
| 资料卡 `{{card:}}`（全页 60 unique） | 60 | 59 | — | 2 处集合不一致 | — | 见 P1-6/P1-7 |
| 本地链接 | 73（§5 起 65） | 73 | 0 dead | — | — | 附录 A 的 PDF#page=15 已开 PDF 验证 |
| `compiled_from` | 39（应 60） | hash 39/39 对 | — | 缺 22、多 1 | — | 见 P1-6 |
| 附录 A 年表 | 11 行 | 10 | 0 | 1（列举顺序） | 0 | 行 650 |
| 附录 B 卡表 | 60 行 | 59 | 0 | 1 未引用 / 漏 1 | — | 行 712、649 |
| 附录 C 依赖边 | 13 | 11 | 2 方向反 | 缺 4 类 | — | 行 735、740 |
| front matter related/parents | 3 | 3 存在 | — | — | — | page/kapustin-witten、page/langlands-program |

计数口径：一条〔…〕若同时含两段（如 499 行「p.21–22 §5.1；p.26 §6」）按一条计，其中后半错节不计入「错页」单列，已并入该条判定。

## 二、P1（须改，影响事实或结构）

**[P1] 571 · 「这是目前最一般的构造」 · 内容与底本相反 · 证据：BZ26 p.26 §5.5「opers themselves only form a half-dimensional subvariety of Loc_Ĝ … a broader class … provided by [FG09a]」；同页 [ABC+24b] 才是把临界水平表示装成机器的那一步。 · 建议：改为「BD 1996 对 oper 型参数造出 Hecke 特征层；一般局部系统还要 [FG09a]/五部曲的机器」，并删「最一般」。**

这条是 §6 构造线的定性句，读者会据此以为 BD 已覆盖全部参数，与原文「opers 只是半维」直接冲突，属 P1。

**[P1] 602 · 「Dolbeault 已有一般情形的工作」 · 内容不符（generically 误读）· 证据：BZ26 p.27 §6.0.4「the Dolbeault conjecture was proven **generically** in [DP12] … See [PT25] for progress on a new form of the Dolbeault conjecture over the entire Hitchin base」；同句开头已说 Dolbeault/quantum「remain open even in the unramified setting」。 · 建议：改「Dolbeault 在通有（generically）情形已由 [DP12] 证明；全 Hitchin 基上仍开，[PT25] 有新进展」。**

「一般情形」在中文里读作「无条件的普遍情形」，与「通有位置」差一个量级；且漏掉「仍开」这一层，§7 的「已知/未知」表会把一个开问题写成已解决。

**[P1] 735 · `KM["II · Kac–Moody + opers…"] --> I` · 依赖方向反 · 证据：行 495「II 与 III 都要用 I 的 L_G」；§5 思路图 511–534 只有 I→III、II→III，没有 I→II。 · 建议：改 `I --> KM`（与 §5.3 表「II 的输出依赖 I 的 L_G」一致），并补 II→III、II→IV。**

附录 C 是全文唯一的总图，方向反了会让读者把 II 读成 I 的前提；而 §5.1 明说 I 定稿 2025b、II 是 2024（时间上也支持 I 在后被 II 引用，而不是反过来）。

**[P1] 740 · `CP["char p（独立 2025a）…"] --> TH["char 0 主定理"]` · 方向与正文相反 · 证据：§5 图 530 为 `GLC --> CP`（char p 由主定理的框架推出），行 651/657 也说 char p「独立成篇」「不计入五部曲」。 · 建议：改为并列节点，或 `TH -.-> CP`（虚线表示「同一框架下的独立论文」），不要用实线 CP→TH。**

**[P1] 567 · 「两者接缝处的重数必须是一」 · 无依据 · 证据：BZ26 p.26 §5.5 对该论文的全部表述是「[GR24b] … leading to … all eigenspaces have multiplicity one and the unramified GLC holds」；无「接缝」「必须」的论证。 · 建议：标为「编者推断」，或改「V 把重数一与无分歧 GLC 一起收口」。**

**[P1] front matter 37–114 · `compiled_from` 只有 39 条（预期 60）· 元数据不一致 · 证据：正文 60 个 unique 卡 id；39 条 hash 与卡文件 sha256 前 16 位 39/39 一致（脚本验），但以下 22 张被正文引用却未登记：bzg/abelianization、algebraic-spectral-theorem、betti-mellin、bun-g、categorical-fourier、categorical-harmonic-analysis、dolbeault-glc、dual-group、factorization、fourier-transform、glc-overview、glc-statement、higgs-bundles、hitchin-fibration、indicoh-nilpotent-support、loc-g-betti、loc-g-derham、low-genus、spectral-action、spectral-theorem、glc/geometric-class-field-theory、sy0246/vanishing-theorem；另有 1 条 `bzg/concept/relative-langlands` 登记了却从未在正文出现。 · 建议：以正文实际引用重生成 `compiled_from`（60 条，补 hash），删 relative-langlands 或把它真正用进 §5/§7。**

任务要求「60 个 id+hash 与 sha256 前 16 位一致」目前无法满足；39 条本身全部对，说明校验流程是好的，只是清单没跟正文同步。

**[P1] 附录 B 665–724 · 与正文/附录 A 的卡集合不一致 · 证据：行 649 用 `{{card:sy0246/concept/vanishing-theorem}}`，B 表 60 行里没有它；B 表 712 行 `bzg/concept/relative-langlands` 标「§5/§7」，但该卡只出现在 front matter 89 行与 712 行本身。 · 建议：B 表补 sy0246/vanishing-theorem（节列记「附录 A」，或表头改「按节 + 附录」），删/换 relative-langlands。**

## 三、P2（建议改，不影响主结论但会被读者抓到）

**[P2] 445（两处）、495、503、507、549 · 「BZ26 p.26 §6」· 错节（系统性）· 证据：五篇清单与「more subtle functional analysis」都在 p.26 **§5.5 末尾**，紧接「6. What is this good for, and what's next?」标题之前；§6 里没有这份清单。 · 建议：全部改 §5.5；§5.3 表 V 行的「p.26 §6」同改。**

**[P2] 445 · 「编年照 §6」· 来源无依据 · 证据：BZ26 §6 无年份编年（标签是 24a/24b/24）；「I 2025b、II–IV 2024、V 2026」的真正出处是 SCH26 p.14 五篇列表与 p.42–43 书目。 · 建议：改「编年见 SCH26 p.14 与书目 p.42–43」。**

**[P2] 461 · 「四步战略」引〔SCH26 p.7 §1〕· 错页 · 证据：四步逐条在 p8（「1. 把几何Langlands 对应表述为范畴等价…4. 对特征0 的域上的曲线…」）；p7 是定理 1.7 与注 1.8。 · 建议：改 p.8。**

**[P2] 463 · 「§2 等价陈述（p.9–14）」· 页范围少一页 · 证据：注 2.13 从 p14 续到 p15，§3 标题也在 p15。 · 建议：改 p.9–15（与 §9/§10 行「边界重叠」的写法一致）。**

**[P2] 465 · 「§3 Bun_G 上的层（p.15–16）」· 页范围少一页 · 证据：p17 仍是 §3 末段（Betti 用 D(S)=D(S(C),e)、de Rham 用完整导出 D(Bun_G)），§4 标题「4 局部系统的叠」也在 p17。 · 建议：改 p.15–17。**

**[P2] 467 · 「§4 局部系统的叠（p.17–18）」· 页范围少一页 + 内容错位 · 证据：§4 延到 p19（p19 顶部「LocSys^et_X 在文献中记作 LocSys^restr_X」，即 Ind Lisse 的 pro-代数完备化）；「Betti 用 e-向量空间层、étale 用 Ind D^b_c」实际是 §3 末 p17 的句子。 · 建议：页范围改 p.17–19；把「restricted 完备化」一句移到 §3 行或注明「§4 末 p19」。**

**[P2] 469 · 「Betti/étale 用 Nadler–Yun 的 1-affineness」· 归属不精确 · 证据：定理 5.1（p19）归 Nadler–Yun；1-affineness 是 p20–21 的 Gestalt 论证（∗/Ĝ 是 1-affine，故映射 Gestalt 1-affine），p19 定理本身没有这个词。 · 建议：改「Nadler–Yun 的谱作用；1-affineness 由 Gestalt 论证（p.20–21）」。**

**[P2] 471 · `G_m^{2g}×(∗×^L∗)×∗/G_m` · 记号漏下标 · 证据：SCH26 p.26「LocSys^Betti_{G_m}=G_m^{2g}×(∗×^L_{G_m}∗)×∗/G_m」。 · 建议：补 `^L_{G_m}`。**

**[P2] 473 · 「D_qc(∗/Ĝ)-线性」· 记号漏 `_Ran` · 证据：SCH26 p.27「P 是 D_qc(∗/Ĝ)_Ran-线性」。 · 建议：补 `_Ran`（这是 Ran 空间上范畴层的关键限定）。**

**[P2] 477 · 「定理 9.6 给 Whittaker 系数的完全描述」引〔p.33 §9〕· 错页 + 措辞过强 · 证据：定理 9.6 在 p35（几何 Casselman–Shalika：D_qc(∗/Ĝ)→D_!(LU^Θ\_ψ Gr^Θ_G) 的等价；推论 9.7 Whit(G)≅D_qc(∗/Ĝ)_Ran）；p33 是定理 9.3。 · 建议：页码改 p.35，措辞改「把 Whittaker 侧识别为 D_qc(∗/Ĝ)」。**

**[P2] 563 · CT_{P!} 与「沿尖点取 Fourier 展开的常数项」引〔p.35–36 §10〕· 错页 · 证据：Eis_{P!}=q_!p^* 在 p36；CT_{P!}=p_!q^* 及「Fourier 展开中的常数项」在 p37（定理 10.1 同页）。 · 建议：拆成〔p.36〕〔p.37〕。**

**[P2] 585 · 消没定理引〔LAU02 906--13〕· 错页（边界）· 证据：定理 6.1（Gaitsgory）在 906--14；906--13 只是「6 消没定理」节首。 · 建议：改 906--14。**

**[P2] 559 · 「AGKRV 2021」· 作者缩写漏字 · 证据：SCH26 p.30 定理 8.2 作者为 Arinkin、Gaitsgory、Kazhdan、Raskin、Rozenblyum、Varshavsky（六人）= AGKRRV。 · 建议：改 AGKRRV。**

**[P2] 571 · 「到 Ȗ^Θ 的约化」· 符号错 · 证据：SCH26 p.38「把其底层的 Ĝ-丛约化到 ˇU^Θ 的约化」（对偶群记号用 ˇ）。 · 建议：改 ˇU^Θ（与全文 Ĝ/ˇT 记号统一）。**

**[P2] 543 · 「整个 enterprise 的致谢」· 措辞过强 · 证据：SCH26 p.2 原句「该定理依赖许多其他论文，作者包括……」——是依赖声明，不是致谢。 · 建议：改「依赖声明里列出的十一人」。**

**[P2] 650 · 「Kac–Moody 局部化、ambidexterity、Eisenstein」· 列举顺序与 II–III–IV 不对应 · 证据：II=Kac–Moody 局部化+FLE、III=Eisenstein 归纳步、IV=ambidexterity（BZ26 p.26 清单、SCH26 书目标题）。 · 建议：按 II/III/IV 顺序写「Kac–Moody 局部化、Eisenstein、ambidexterity」。**

**[P2] 720 · `function-field-langlands` 节列记「§7」· 与正文不符 · 证据：该卡只出现在附录 A 651 行（char p 条目）与 B 表 720 行，§7 正文没有它。 · 建议：节列改「附录 A」，或把它真正引到 §7 正特征一段。**

**[P2] 712 · `relative-langlands` 节列「§5/§7」· 同上 · 证据：仅 front matter 89 行与 712 行。 · 建议：见 P1-7。**

**[P2] 599 · 「这一步是否已被框架覆盖，见待核」· 占位符遗留 · 证据：正文出现「见待核」；同类 arXiv 待核已可由 SCH26 书目撤掉。 · 建议：给出「SCH26 p.40 §11 的交换图已覆盖/未覆盖」的判定，或删掉该分句。**

**[P2] 591、592、598、600 · 「§2.11」「§2.12」· 伪节号（系统性）· 证据：SCH26 只有 §2，其内是定理 2.11/2.12，没有 §2.11 这样的节。 · 建议：统一写「p.14 §2 定理2.11/2.12」。**

**[P2] check_survey.py 对 entries 报 0 · 工具与页面格式不对齐 · 证据：本页 entries 是标准 YAML 列表（`- geometry/…`，18–31 行），14 个目标文件都存在，但脚本输出 `entries: 0 unique`。 · 建议：校对脚本的 entries 解析（或确认发布流水线读的是同一键），否则词条反链会漏。**

## 四、未覆盖清单（行号 + 一句话）

- 599：「高秩函子性是否被框架覆盖」——SCH26 没有对应论断，无法判定，只报了占位符。
- 601：「完全分歧需局部 GLC」的 [Gai25] 具体出处——BZ26 p.26 只给引用，未展开核对 Gai 的原文。
- 601：「精细形式仍在研究」的时态——属编者概括，未找到逐字对应句。
- 附录 B「节」列：只验了每行**首项**与该卡正文首现节一致；`§0/§2`、`§5/§6` 这类多节声明未逐节验证。
- BZ26 p.29–34 书目：只核了 [BKS22]、[GR24b]、[GR25]、[BD] 四条，其余未逐条对。
- SCH26 §8–§12：抽查了定理 8.2、9.3、9.6、10.1、11.4 与 §12 全链，其余段落（如 §9 的 Θ-丰沛细节）未逐句核。
- 附录 C：只做文本级依赖核对，未跑 mermaid 渲染（语法是否成图未验）。
- front matter entries：14 个目标文件存在性已验，但未逐个打开确认语义与页面主题匹配（如 geometry/perverse-sheaf 的卡内容是否覆盖本页用法）。

## 五、已证与可撤的「待核」

- **五篇 arXiv 号已获双证，可撤「待核」**：SCH26 p.41–44 书目给出 II=2405.03648、III=2409.07051、IV=2409.08670、I=2405.03599v3、V=2409.09856v3、char p=2508.02237；CL23 书目独立给出同样的五个号。页面 447–457、651–653 全部正确，只有 445 的「待核」措辞需要跟进（属编者状态，不是错误）。
- **char p 条件写法正确，且页码精确**：592 行「p 大于由 G 决定的常数、且 p 不是 G 的挠素数」= SCH26 p.14 定理 2.12 + 脚注 15（「特别地，p = char(k) 不应是 G 的挠素数」）；593 行「p 相对 G 充分大」= p.16 定理 3.4（「特别地，它对 G 是非挠的素数。17」）。两处不混。
- **附录 A 646 的 PDF 锚点已开页验证**：`…中译注本.pdf#page=15` 第 15 页正是参考文献页，首条为 [Dr 1] Drinfeld, ICM Helsinki 1978, 565–574。
- **附录 A 647/648/649 的 arXiv 号与书目互证**：math/0207078（Laumon 906，gap 卡 source）、math/0012255（FGV，RAS23 书目「Math. Soc. 15 (2002), 367–417」）、math/0204081（Gaitsgory, Annals 160.2 (2004) 617–682，CL23 书目）。

## 六、查过但没问题的要害条目（18 条）

1. 457 · char p 一段的条件、LocSys′ 开闭子叠、Witt 提升与一般纤维退化，全部对得上 SCH26 p.14。
2. 592 · 定理 2.12 的「常数 + 非挠素数」两条件与开闭子集 LocSys′，逐字对 p.14。
3. 593 · 定理 1.7（p.7）与「取 Frobenius 迹推出」（p.14–15）两处引文都对。
4. 447 · I 的 L_G 与定理 9.3（p.33）一致；「唯一保余极限、紧对象→最终余连通」与原文同。
5. 449 · II 主输出「定理 11.4 交换图：上排 L_G、下排 FLE」与 p.40 一致。
6. 451 · III 的 Eis_{P!}、CT_{P!}、第二伴随（p.37）与 CCF 方块（p.38）分工正确。
7. 463 · 猜想 2.10（p.13）的归一化「结构层 ↦ Whittaker 层」与原文一致。
8. 465 · 定理 3.4（p.16）三条件与脚注 17（良好幂零锥）无误。
9. 475 · 定理 8.2（p.30）、Xue 2025（p.31）、注 8.3（p.31）三处页码全对。
10. 481 · 定理 11.4 的九人名单与「2024」与 p.40 一致。
11. 501 · 旧 FGV 链与 CL23 p.36–37 §5.7–§6.2 对得上；`d > nk(2g−2)` 与 CL23 原句一致。
12. 553 · 白光/Whittaker period 的归一化引 BZ26 p.23–24 §5.4 正确。
13. 557 · 「微茎（Nadler–Taylor）」在 SCH26 p.41、FR 不消失/单射在 BZ26 p.25，两处都对。
14. 565 · CCF 差扭、注 10.2、CT 方块用 Kac–Moody（p.38）与 BZ26 p.23 §5.3 都对。
15. 573 · BB 局部化（BZ26 p.25 §5.5）与 FLE 交换图（SCH26 p.40）都对。
16. 575 · opers 半维子簇、[Ari16]/Deligne、BKS22 可缩（BZ26 p.26 §5.5）都对。
17. 606 · gap 卡描述（scope gap、sorry_count 1、定理 1.2、五个 opaque 占位、未编译）与 JSON 完全一致。
18. 附录 B 的机械项：60 行路径全部存在、卡内 id 一致、底本页与 `sources[0].pages` 一致（脚本 60/60）。

## 七、建议的最小改动集（按性价比）

1. 改行 571、602 两句定性（P1）——只动两句话，风险最高。
2. 改附录 C 735/740 的箭头方向，补 I→II、II→III、II→IV 三条边（P1）。
3. 重生成 `compiled_from`（60 条）与附录 B（补 sy0246/vanishing-theorem、删 relative-langlands）（P1）。
4. 批量替换「BZ26 p.26 §6」→「p.26 §5.5」（6 处）与「§2.11/§2.12」→「§2 定理2.11/2.12」（4 处）（P2，机械）。
5. 修四页范围（§2 p.9–15、§3 p.15–17、§4 p.17–19）与四处错页（461→p.8、477→p.35、563→p.37、585→906--14）（P2）。
6. 记号：471 补 `^L_{G_m}`、473 补 `_Ran`、571 改 `ˇU^Θ`、559 改 AGKRRV（P2）。

## 八、核对明细（证据表）

### 8.1 §5.2 十二节页范围逐条

| 节 | 页面写 | 实际（SCH26 PAGE） | 判定 |
| --- | --- | --- | --- |
| §1 引言 | p.2–8 | p.2–8（§2 标题在 p9） | ✓ |
| §2 等价陈述 | p.9–14 | p.9–15（注 2.13 续到 p15） | 少一页 |
| §3 Bun_G 上的层 | p.15–16 | p.15–17（Betti/de Rham 层范畴段在 p17） | 少一页 |
| §4 局部系统的叠 | p.17–18 | p.17–19（LocSys^restr 在 p19） | 少一页 |
| §5 谱作用 | p.19–25 | p.19–25 | ✓ |
| §6 G=G_m | p.26–27 | p.26–27 | ✓ |
| §7 Beilinson 谱投影子 | p.27–28 | p.27–28 | ✓ |
| §8 Frobenius 的迹 | p.29–31 | p.29–31 | ✓ |
| §9 Whittaker 系数 | p.32–35 | p.32–35（定理 9.6 在 p35） | ✓ |
| §10 Eisenstein 级数 | p.35–38 | p.35–38 | ✓ |
| §11 Kac–Moody 局部化 | p.38–40 | p.38–40 | ✓ |
| §12 尖点形式 | p.40–41 | p.40–41（书目 p42 起） | ✓ |

### 8.2 错页/错节/内容不符/无依据的 17 条

| # | 行 | 原句（截） | 判定 | 证据 |
| --- | --- | --- | --- | --- |
| 1 | 445 | 五篇…收口〔BZ26 p.26 §6〕 | 错节 | 清单在 §5.5 末，§6 标题前 |
| 2 | 445 | 编年照 §6〔BZ26 p.26 §6〕 | 错节+无编年 | SCH26 p.14/p.42–43 才有年份 |
| 3 | 461 | 四步战略〔SCH26 p.7 §1〕 | 错页 | 四步逐条在 p8 |
| 4 | 477 | 定理 9.6…〔SCH26 p.33 §9〕 | 错页 | 定理 9.6 在 p35 |
| 5 | 495 | 这条链不线性…〔BZ26 p.26 §6〕 | 错节 | 应为 §5.5 |
| 6 | 499 | …故 §6 称它「更精细的泛函分析」 | 错节 | 该语在 p26 §5.5 列表 |
| 7 | 503 | （§5.4 段）〔BZ26 p.26 §6〕 | 错节 | 应为 §5.5 |
| 8 | 549 | 三条互锁的输入…〔BZ26 p.26 §6〕 | 错节 | 输入分见 §5.3/§5.4/§5.5 |
| 9 | 563 | CT_{P!}…〔SCH26 p.35–36 §10〕 | 错页 | CT 定义与常数项在 p37 |
| 10 | 585 | 消没定理〔LAU02 906--13〕 | 错页 | 定理 6.1 在 906--14 |
| 11 | 591 | 定理 2.11〔SCH26 p.14 §2.11〕 | 伪节号 | 原文只有 §2 |
| 12 | 592 | 定理 2.12〔SCH26 p.14 §2.12〕 | 伪节号 | 同上（p 数对） |
| 13 | 598 | 仅 SL_n 已知〔SCH26 p.14 §2.12〕 | 伪节号 | 同上（p 数对） |
| 14 | 600 | 条件未去掉〔SCH26 p.14 §2.12〕 | 伪节号 | 同上（p 数对） |
| 15 | 571 | 这是目前最一般的构造 | 内容不符 | BZ26 p.26：opers 只是半维 |
| 16 | 602 | Dolbeault 已有一般情形的工作 | 内容不符 | p.27：proven generically |
| 17 | 567 | 两者接缝处的重数必须是一 | 无依据 | 原文只说 multiplicity one 成立 |

### 8.3 附录 A 逐行

| 行 | 内容 | 判定 |
| --- | --- | --- |
| 646 | 1978 Drinfeld ICM Helsinki GL(2) | ✓（PDF p15 见 [Dr 1]，页码 565–574） |
| 647 | 2002 Laumon 906，arXiv:math/0207078 | ✓（gap 卡 source 同号） |
| 648 | 2002 FGV，arXiv:math/0012255 | ✓（RAS23 书目：JAMS 15 (2002) 367–417） |
| 649 | 2002 Gaitsgory，arXiv:math/0204081，消没定理 | ✓（CL23 书目 [Gai04] Annals 160.2） |
| 650 | 2024 GLC II–III–IV「三篇」 | 数目 ✓；列举顺序 ✗（应 Kac–Moody、Eisenstein、ambidexterity） |
| 651 | 2025a char p，2508.02237 | ✓（SCH26 书目） |
| 652 | 2025b I，2405.03599v3 | ✓ |
| 653 | 2026 V，2409.09856v3 | ✓ |
| 654 | 2026 Scholze，Bourbaki 1252 | ✓（SCH26 p1：第 78 年，第 1252 期，2026 年 3 月） |
| 655 | 2026 Ben-Zvi，arXiv:2605.23167v1 | ✓（底本自身，单证可接受） |
| 656 | leanstmt 卡 laumon906-g01 | ✓（文件存在，scope gap） |

### 8.4 附录 C 逐边

| 行 | 边 | 判定 |
| --- | --- | --- |
| 732 | S0→S1（代数谱定理/Fourier → 几何 Satake） | ✓ |
| 733 | S1→S2（Satake → 谱作用） | ✓ |
| 734 | S2→I | ✓（§5 图 513–516 一致） |
| 735 | II→I | ✗ 方向反（应 I→II） |
| 736 | I→III | ✓（§5 图 517） |
| 737 | III→IV | ✓（§5 图 522） |
| 738 | IV→V | ✓（§5 图 527） |
| 739 | V→TH（char 0 主定理） | ✓（§5 图 529） |
| 740 | char p→TH | ✗ 方向反（§5 图 530 为 GLC→CP） |
| 741 | TH→FQ（迹 ⇒ Thm 1.7） | ✓（§5 图 531、533） |
| 742 | S2⇢BE（Beilinson 投影子） | ✓ |
| 743 | BE⇢I | ✓（BE 是 I 的工具） |
| — | 缺 I→II、II→III、II→IV | 与 §5 正文 495 行不符 |
| — | 缺 DG16→III、FR→IV、BKS22→V | 与 §5 图 519/523/528 不一致（工具边可省，但宜补虚线） |

### 8.5 front matter 逐项

| 字段 | 值 | 判定 |
| --- | --- | --- |
| id/title/kind/status | page/geometric-langlands；几何 Langlands 对应是什么…；topic；draft | ✓ |
| version/reviewed_by/reviewed_on | 1.0；[]；2026-11-27 | ✓（未审状态与 draft 一致） |
| related | page/kapustin-witten、page/langlands-program | ✓ 2/2 存在 |
| parents | page/langlands-program | ✓ 存在 |
| order | 20 | ✓ |
| entries | 14 条 | ✓ 14/14 文件存在；但 check_survey 报 0（工具解析问题） |
| note | 底本 BZ26、主线 SCH26、细节 CL23/LAU02 | ✓ 与正文与附录 A 一致 |
| compiled_from | 39 条（hash 39/39 对） | ✗ 应 60：缺 22、多 1 |

### 8.6 附录 B 分组与控制项

| work | 行数 | 备注 |
| --- | --- | --- |
| benzvi_glc（bzg） | 40 | 含 712 relative-langlands（正文未引用） |
| glc | 7 | 714 vanishing-theorem（glc）在 501 用过 |
| glc1 | 11 | 10 concept + 1 conjecture（702 glc-conjecture） |
| raskin_glc | 1 | 717 cuspidal-sheaf，§6 首现 579 ✓ |
| sy0246 | 1 | 716 main-theorem-fgv ✓ |
| 合计 | 60 | 与 B 表行数一致 |
| 漏项 | 1 | sy0246/concept/vanishing-theorem（649 行用过）未列 |
| 机械项 | 60/60 | 路径存在、id 一致、底本页 = sources[0].pages |

### 8.7 复跑记录

- `check_survey.py`：`cards: 60 unique / 95 refs; missing 0`；`local links checked: 73; dead 0`；`citation markers: 196`；`OK`。
- 自定义脚本：`〔〕` 68 条（51/14/2/1）；`{{card:}}` 45 次（§5 起）/60 unique（全页）；链接 65 条（§5 起）。
- PDF 抽页：LAU02 中译注本第 15 页 = 参考文献页，含 [Dr 1] Helsinki 1978。
