# log_ch16 —— 第 16 章《（导出）几何 Langlands 中的缺陷》校订记录

- 对象：`src/chapters/ch16.tex`（校前 632 行 / 44904 字节，校后 633 行 / 46028 字节）；英文 `en/ch16_en.txt`（868 行，`<<< p.NNN >>>` 为 PDF 页码）；页面图 `pages/p-265.png` … `pages/p-279.png`。
- 范围：原 PDF pp.265–279（15 页，印刷页 264–278），3 节 8 小节，101 个编号公式（16.1–16.101），1 幅图（Figure 16.1），英文脚注 2 条，既存 `[Tutor Note]` 10 条。
- 方式：EN 全文与 CN 全文各通读一遍、逐段逐句对齐；101 式全部对照英文文本层，其中上下标易走形的公式（16.1）(16.15)–(16.18) (16.23)–(16.24) (16.32)–(16.38) (16.43)–(16.47) (16.57)–(16.67) (16.70)–(16.74) (16.80)–(16.96) (16.98)–(16.101) 另开页面图逐字核对；重点复查任务说明所列跨章风险（endomorphism/自同构、abelian/紧、skyscraper、monodromy/单值化）。

## 一、结构与编号核对

- 公式编号：CN 共 101 个 `\tag{16.k}`，序列 16.1–16.101 完整、连续、无缺号无重号，与 EN 的 101 式一一对应。
- 节结构：16.1（16.1.1 导出版本 / 16.1.2 几何 Langlands 中的移位辛空间 / 16.1.3 源于何处）、16.2（16.2.1 $A$-侧 / 16.2.2 $B$-侧）、16.3（16.3.1 Langlands 函子性 / 16.3.2 畴壁与边界条件 / 16.3.3 哈密顿作用），与 EN 完全对应。
- 图：Figure 16.1（原 PDF p.275）1 幅，图题与 EN「By "folding" along the domain wall…」一致，`\label{fig:16-1}` 无重复；图题末尾「（原文 p.~275，Figure 16.1）」按 `src/main.tex:58` 的约定指**原 PDF 页码**（非印刷页 274），正确，不必改。
- 脚注：EN 2 条（脚注 1「It does require some thought…」挂 (16.24) 前的 "We can rewrite¹ this as:"；脚注 2「It is important to keep track of notation and context…」挂 (16.25) 的 "based loop space"）。校前 CN 只有脚注 1，且单独成行落在 `\end{align}` 之后（原 149 行），脚注号会印到下一段段首；脚注 2 整条缺失。本次各作处理，见 §二-2、§三-1。
- 逐段核对：EN 每一段均能在 CN 找到对应句，**未发现整段漏译或增译**；only / never / any / exactly / at least / always 一类限定词逐处比对（en:175 only→CN 159「只依赖」；en:223 the only objects→CN 187「仅有的对象」；en:365 only had trivial→CN 284「只有平凡的」；en:384 exactly→CN 300「正是」；en:764/779 only→CN 583/592「只看了」「只有」），均已译出；否定句「does NOT give any kind of map」→ CN 430「并不给出任何形式的映射」，无译反。
- 对象/侧别核对：(16.3) $\cM^1_B=\cM^1_A=\mathrm{pt}/G^\vee$、(16.16) $T^*[3](\mathrm{pt}/G^\vee)$、(16.17)(16.18) $T=\fg^\vee[1]$、$T^*=\fg^\vee[-1]$、(16.19)–(16.24) 粘合、(16.51)–(16.55) $\fg^{\vee*}[2]/G^\vee\rightsquigarrow\mathfrak h^{\vee*}[2]/W$、(16.62) 纤维积方阵、(16.70) 右端 $(\mathrm{Sym}(\fg^\vee[-2])\text{-mod})^{G^\vee}$、(16.97) $\cM^1\to\cM^0$、(16.99)–(16.101) 均与印本一致，无 $A$/$B$ 侧错位、无 $\vee$ 错配。

## 二、P1 必改（3 处）

| 位置 | 类别 | 原文 | 原译 | 改为 | 理由 | 依据 |
| --- | --- | --- | --- | --- | --- | --- |
| ch16.tex:162（(16.27) 之后，原 PDF p.268） | P1 漏译限定语（丢 derived） | I.e. we are computing the derived self-intersection of a point in a vector space. | 也就是说，我们是在计算向量空间中一点的自交。 | 也就是说，我们是在计算向量空间中一点的**导出**自交。 | 「derived」是限定语，删去后与同章 164 行「考虑 $0\in V$ 的**导出**自交」、(16.27) 的导出纤维积自相矛盾；本段整段都在讲「不取导出就只剩对角」 | `en/ch16_en.txt:181`；对照 `ch16.tex:164`、`ch16.tex:165`（(16.28)） |
| ch16.tex:150（(16.25) 之前，原 PDF p.268） | P1 整句漏译（脚注 2 全条缺失） | 2 It is important to keep track of notation and context. This is based loops in the world of derived algebraic geometry, not in homotopy theory. | （无。全章校前只有 1 条 `\footnote`，即脚注 1） | 在 `\term{基于一点的环路空间}{based loop space}` 之后补 `\footnote{要注意记号与语境：这是导出代数几何意义下的基于一点的环路，而不是同伦论中的环路空间。}` | EN 有 2 条脚注，脚注 2 未译；而 (16.36)(16.37) 紧接着就把 $\wedge^\bullet V^*$ 认作**同伦论**里的 $H_*(S^1)$，这条脚注正是防止读者把两种「环路空间」混为一谈的 | `en/ch16_en.txt:214–216`；全仓 grep 无对应译文；`ch16.tex:144` 为唯一既存脚注 |
| ch16.tex:426（(16.74) 阵列底行，原 PDF p.274） | P1 符号缺失（图式） | (16.74) 底行虚线箭头上方印有「?」 | `\mathcal{A}_H & \dashrightarrow & \mathcal{A}_G` | `\mathcal{A}_H & \stackrel{?}{\dashrightarrow} & \mathcal{A}_G` | 「?」标出该函子既未构造、也未必存在；漏掉后图式读作「函子存在」，与紧随的正文「$H^\vee\to G^\vee$ 并不给出任何形式的映射 $H\to G$」相反 | `pages/p-274.png`（放大核对）；同类处 (16.67) 译本已用 `\stackrel{?}{\simeq}`（`ch16.tex:365`） |

改后核验（grep 均可命中）：`导出自交。`（162）、`\footnote{要注意记号与语境`（150）、`\stackrel{?}{\dashrightarrow}`（426）。

## 三、P2 必改（1 处）

| 位置 | 类别 | 原文 | 原译 | 改为 | 理由 | 依据 |
| --- | --- | --- | --- | --- | --- | --- |
| ch16.tex:144（原 149 行，原 PDF p.266） | P2 排版/脚注挂点 | 印本 "We can rewrite¹ this as:"，脚注号紧挂 "rewrite" | `\end{align}` 之后单独一行 `\footnote{确实需要想一下为什么商与交可以交换。}`（内容本身无误） | 把该 `\footnote` 移到「我们可以把它改写成」之后同一行，`\end{align}` 后不再有脚注 | 竖直模式下的 `\footnote` 会把脚注号印到**下一个段落**（「也就是说，$S^2$ 上的局部系统…」）的开头，读者会把这条关于 (16.23)(16.24) 的注记错挂到后一段的论断上 | `pages/p-267.png`（印本脚注号在 "rewrite" 上）；`en/ch16_en.txt` 同位；改后 §九 自检无环境/`$` 失衡 |

其余术语项逐条排查，均无问题：
- endomorphism：全章 0 处「自同构」误译。`ch16.tex:124` 的「自同构」对应印本 automorphisms（圆盘上唯一局部系统的自同构群由 $G^\vee$ 给出），正确，**不是** ch09 那类错误。
- automorphic forms：全章 3 处均作「自守形式」，无 ch09 式串味；原文两处 "automorphism forms" 笔误已有注（`ch16.tex:432`）覆盖。
- abelian/紧：`ch16.tex:244/252` 的「紧」对应 compact object（与 Perf 相对），用法正确，**不是** ch08 的「丢 abelian 换紧」。
- monodromy：全章作「单值性」（`ch16.tex:128`），**0 处**「单值化」。
- skyscraper：全章 4 处一律「摩天楼层」，与 ch06/ch11/ch15 一致（仅 ch08 作「天穹层」），属跨章不统一，见 §五-3，不在本章擅改。

## 四、新增注释（1 条）与补译脚注（1 条）

1. **ch16.tex:429（(16.74) 之后，原 PDF p.274）**——新注说明图式中「≀」与「?」的含义：中间一行两个 ≀ 表示上下两行对象在几何 Langlands 对偶下相互对应，底行虚线加「?」表示该函子未构造、未必存在。理由：印本的 ≀/「?」是全文唯一用图式表达「尚未存在的函子性」的地方，译文只保留字形而不解释，读者易误读为已建立的对应。来源：`[译者按（无外部依据）：依 (16.71)–(16.73) 与下一句推得]`。
2. **ch16.tex:150 补脚注**（内容见 §二-2）：忠实照译英文脚注 2，未增删语义。

现有 `[Tutor Note]` 10 条（CN 61、120、162、208、299、391、432、513、538、607）一字未动；新增 429 一条，全章共 11 条。

## 五、P3（只记录，不改）

1. **ch16.tex:393（原 PDF p.273）**："the derived version of line operators spectrally composes over $T^*[1]\Loc_{G^\vee}$" 译作「在谱意义上**分解**于 $T^*[1]\Loc_{G^\vee}$ 之上」。composes 字面是「复合」，与「分解」相反；但原文用词本身可疑（疑为 decomposes 之笔误，或作者就「谱」字玩的戏称），中文「分解于……之上」符合上下文意图，故不改，按 §八 GAP 处理。
2. **ch16.tex:479（原 PDF p.275）**："and we're just alternatively thinking of it as an element of $A\otimes B^{\mathrm{op}}$-mod" 译作「并**等价地**把它看成 $A\otimes B^{\mathrm{op}}$-mod 的元素」。「just alternatively」是「换一种说法」，不是「等价地」；建议改为「只是换一种说法，把它看成……」，语义未错，不改。
3. **跨章术语**：skyscraper sheaf 本章 4 处（192、204、269、311）一律「摩天楼层」，与 ch06（18/130/170/178）、ch11（1091/1105）、ch15（353/486/490）一致；仅 ch08（701/719/734/738/775/796/806/847）作「天穹层」。`src/appendix_glossary.tex` 无此条。本章不动，建议 lead 全书统一为「摩天楼层」并回改 ch08。
4. **ch16.tex:61**：「这就是 $\mathbb{E}_n$ 与 $\mathbb{E}_m$ 之间的**可加关系**」（additive relationship）。措辞略生硬，既有注已解释，不改。
5. **ch16.tex:559**：「想法是做同样的**谱废话**」（the same spectral nonsense）。作者自嘲语，口语，可接受。
6. **ch16.tex:607**：「Chern--Simons **在道德上**就是 $BG$ 的 RW」（morally）。物理惯用语，既有注已覆盖，不改。
7. **(16.41)（ch16.tex:234）**：印本用 $\approx$（`Coh_S ≈ Perf_S`），译本用 `\simeq`；纯排版差异（同页 (16.44)(16.47) 印本亦混用 ≈/≃），不记错。
8. **图号硬编码**：图题「Figure 16.1」与正文均未用 `\ref{fig:16-1}`，目前图序唯一，无风险。

## 六、原书笔误（照译，不改，仅记录）

1. **(16.38)（ch16.tex:220，原 PDF p.270）**：印本 $S=H_{S^1}(\mathrm{pt})=H^*(BS^1\simeq\C\PP^\infty)\simeq k[u]$。左端按上下文（(16.58)(16.59) 均为 $H^*_G$）应为 $H^*_{S^1}(\mathrm{pt})$，印本脱上标 `*`。译文照印本，不擅改。
2. **(16.55)（ch16.tex:305，原 PDF p.271）**：印本 $\mathfrak h^{\vee*}[2]/W=\mathfrak h[2]/W$，右端脱 $\vee$（对照 (16.53) $\cM^0=\mathfrak h^{\vee*}[2]/W$）。译文照印本。
3. **(16.34)(16.35)（ch16.tex:202/206）**：印本 (16.35) 作 $\End_{\wedge^\bullet}(k)$，比 (16.34) 的 $\End_{\wedge^\bullet V^*}(k)$ 少下标 $V^*$。译文照印本。
4. **"automorphism forms"（p.274 两处，CN 432）**：应为 automorphic forms，既有 Tutor Note 已说明，未动。

## 七、存疑待裁定

1. **ind-coherent sheaves →「导出凝聚层」（ch16.tex:244、337、355、391；另 `src/appendix_notes.tex:1000` 同）**。Gaitsgory 的 IndCoh 是 ind-（归纳）完备化构造，与「导出凝聚层」（derived coherent）不是同一概念；而 `appendix_glossary.tex:65` 已把「凝聚层」定为 coherent sheaf，读者极易把「导出凝聚层」误读为 derived coherent。译者首次出现处（244）以「导出凝聚层（ind-coherent sheaves）」夹注英文，读者尚可辨认。因改动需同时覆盖 ch16 与附录注（跨文件），本章不擅改，建议 lead 统一改为「ind-凝聚层」或「归纳凝聚层」。影响：术语层面，数学内容不受影响。
2. **图 16.1 图片文件**：`figure16-1.png` 为原文 p.275 手绘图的重绘/截取，图题已注明出处；未逐像素比对，若 lead 要求图与印本完全一致需另行核图。此项不影响文字校对。

## 八、GAP（1 处）

| 位置 | 原文片段 | 问题 | 已查范围 | 影响 |
| --- | --- | --- | --- | --- |
| ch16.tex:393（原 PDF p.273；正文 `% [GAP:` 提示在 394 行） | the derived version of line operators **spectrally composes over** $T^*[1]\Loc_{G^\vee}$ | composes 一词含义不确定：字面「复合」，疑为 decomposes（「分解于……之上」）之笔误，也可能是作者就「spectral」玩的戏称；两种读法对应不同的数学断言（前者强调「组装/复合」，后者强调「按奇异支撑分层」） | 英文文本层 `en/ch16_en.txt:513–514`；作者本章他处无同样的 compose/decompose 用法；未查到他处讲义原话 | 译文暂按「分解于……之上」处理（与「奇异支撑在 $T^*[1]\Loc$ 上分层」的上下文一致），正文已加 `% [GAP: …]` 提示读者 |

## 九、自检（规程 §7）

- 行数：632 → 633（+1 行 (16.74) 新注释、+1 行 GAP、−1 行脚注 1 由独立成行移入正文行）；字节 44904 → 46028。文件行尾全为 CRLF（633 行 CRLF、0 行裸 LF），无混用。
- `\begin{` 126 = `\end{` 126，逐环境计数一致（equation 99、array 10、srcrem 5、sectionkey 3、srcthm 2、srcex 2、srcclaim 1、keytakeaways 1、figure 1、align 1、flushright 1）；无未闭合环境。
- `$` 共 872 个（偶数）；逐行检查（先剔除注释）奇数个 `$` 的行数 = 0。
- `\label` 2 个（`ch:16`、`fig:16-1`），无重复。
- `\ref`/`\eqref`：本章 0 处，无失效引用；正文「图 15.1/15.2」（引用 ch15 图）、「(16.k)」编号均为硬编码，已抽查与目标一致。
- `\tag{16.k}`：101 个，16.1–16.101 连续无缺号。
- 注释闭合：`% [Tutor Note:` 11 条（原 10 + 新 1）、`% [GAP:` 1 条，逐条检查 `]` 闭合、内部 `$` 成对，无半截注释。
- 未改动：`keytakeaways`、3 个 `sectionkey`、既有 10 条 `[Tutor Note`、图文件、`src/preamble.tex`、`src/main.tex`、附录、他章；未编译（按约定由 lead 统一编译）。
- 工作区：本次只写 `src/chapters/ch16.tex`（4 次 `edit`，无 `write` 整章覆盖）与新建本日志；校对用的临时放大图/脚本目录已删除。
