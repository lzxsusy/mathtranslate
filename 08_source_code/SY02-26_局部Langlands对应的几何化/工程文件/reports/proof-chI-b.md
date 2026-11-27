# 块 B 校对报告（§I.5–§I.9，原书 p.23–p.36）

- 校对对象：`源码/sections/s02-chI-2.tex`（529 行，UTF-8 无 BOM）
- 原文：`00_原文/fargues-scholze-2102.13459v4.pdf` p.23–36，逐页文本 `01_pages/p023.txt`–`p036.txt`，公式与交换图回 400 dpi 渲染图核对
- 依据：`工程文件/work/TASK-proofread.md`、`工程文件/BRIEF.md` §4/§5、`工程文件/SPEC.md`、`工程文件/work/glossary.tsv`、`symbols.tsv`、`术语裁定.md`、译手 `work/trace-chI-b.md`

## 0 结论

**可交付。** 共 15 处改动，全部落在本节文件内：公式/交换图 4 处（其中 2 处是 tikzcd 箭头方向反了）、页锚点错位 3 处、译注重写 4 条、中文 3 处、接缝 1 处。编译 0 error，页锚点两项 `[ok]`。

**需上游处理（本块无权改）：**

1. `源码/sections/s01-chI-1.tex` 末尾停在「对于」，与本节首句构成重复；本节已删去自己这一侧多余的「对」，A 块末尾那个「对于」须由 A 块删（§3-4）。
2. 任务书要求参考的译手报告 `工程文件/reports/chI-b.md` **不存在**（该目录只有 `chI-a.md`、`chI-c.md`、`lead-log.md`）。译手的 5 条自述只能从 `work/trace-chI-b.md` 与 `work/疑点清单.tsv` 间接核对，结论见 §4 末。
3. `work/glossary.tsv` 第 8 行仍作「Langlands 对偶群」，与 `术语裁定.md` 的「朗兰兹对偶群」不一致；正文已按裁定用「朗兰兹对偶群」，glossary 需 Lead 统一。

## 1 逐维度

| # | 维度 | 检查量 | 问题数 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | 漏段/并段 | p.23–p.36 共 14 页逐段比对 | 1 | p.23 接缝重复「对」，且正文出现省略号「……」 |
| 2 | 术语 | 全篇 20+ 术语对 glossary/裁定 | 1 | `congredients` 系误读（原文 congradients，本意 contragredient）；其余（完满/菱形/固体/凝聚/巡游算子/ULA/shtuka/局部 Hecke 叠/谱 Bernstein 中心/好滤过/Weil 限制）均合裁定 |
| 3 | 公式 | 约 60 个显示式 + 5 个 tikzcd 逐图回原页 | 4 | 2 处数学陈述（`\varinjlim` 应为 `\varprojlim`；`有限维` 应为 `有限`）、2 处交换图箭头方向（q^- 挂在错误的源点） |
| 4 | 编号 | 20 个编号对象 + 全部 `\ref` | 0 | Thm I.4.2、I.5.1、I.5.2、Rem I.6.1、Def I.6.2、Thm I.6.3、Prop I.6.4、Thm I.6.5、Rem I.7.1、Thm I.7.2、Cor I.7.3、Thm I.8.1、I.8.2、I.8.3、Prop I.9.1、Def I.9.2、Prop I.9.3、Rem I.9.4、Conj I.9.5、Thm I.9.6，与原文页一一对应，无缺无重 |
| 5 | 译注 | 10 条全部审读，重点 4 条 | 4 | 3 条以「见报告 §6 未解项」结尾（书稿里指向不存在的内部报告）、1 条原文引述位置错、1 条未答「补了哪一步」 |
| 6 | 过度翻译 | 60+ 文献标签、专名、数学缩写 | 0 | [Far16]/[SW20]/[Sch17a] 等标签原样保留，未改；`dim.\ trg`、`i^{b*}`、GL_n、PGL_2 等按原样 |
| 7 | 中文 | 全篇 | 3 | 缺谓语（p.24）、「于是是」（p.28）、「这从其中容易得到」（p.28–29） |
| 8 | 体例 | 14 个页锚点 + 环境 | 3 | p.25 / p.30 / p.35 三个锚点比原页起点晚 5–26 行；另 1 处锚点随句子调整（计入改动 8） |
| 9 | 编译 | xelatex 2 pass | 0 | EXIT=0，`Output written on _check_pb.pdf (14 pages)`，log 无 `!` |
| 10 | 黑名单 | grep「显然/众所周知/不难」 | 2 处 | p.28「不难证明」（原文 It is easy to deduce）、p.31「显然」（原文 clearly），均为忠实对译，非滥用，未改 |

## 2 改动清单

| # | 位置 | 原译 | 改后 | 依据 | 类型 |
| --- | --- | --- | --- | --- | --- |
| 1 | p.23 / L24 | `\srcpageinl{23}……对每个这样的截面` | `\srcpageinl{23}每个这样的截面` | p.23 首行 “For each such section…”，A 块末已有「对于」 | 漏段/接缝 |
| 2 | p.24 / L50 | `\operatorname{Ind}\Bigl(\varinjlim_n D^b_c(...)\Bigr)` | `\varprojlim_n` | 原页印 `lim` 下带左向箭头（`lim ←− n`）= 逆向极限 | 公式 |
| 3 | p.24 / L52 | 构造层之间的态射空间是有限**维**的 | ……是有限**的** | 原文 “the morphism spaces between constructible sheaves are finite” | 公式（数学陈述） |
| 4 | p.24 / L52 | 但它们的自同态代数 Hecke 代数，是无限维的 | 但它们的自同态代数**是** Hecke 代数，**而后者**是无限维的 | 原文 “are Hecke algebras, which are infinite-dimensional”；原句缺谓语 | 中文 |
| 5 | p.29 / L230–233 | `\Gr^I_G \arrow[dr,"q^-"']`；`\Gr^I_{P^-} \arrow[ur,"p^-"']` | `\Gr^I_G`（去掉该箭头）；`\Gr^I_{P^-} \arrow[ul,"q^-"] \arrow[ur,"p^-"]` | 原页箭头的**落点**在 $\mathrm{Gr}^I_G$，即 $q^-:\mathrm{Gr}^I_{P^-}\to\mathrm{Gr}^I_G$；原译码把源点写成 $\mathrm{Gr}^I_G$，方向反了 | 公式/交换图 |
| 6 | p.30 / L248–251 | `X \arrow[dr,"q^-"']`；`X^- \arrow[ur,"p^-"']` | `X`；`X^- \arrow[ul,"q^-"] \arrow[ur,"p^-"]` | 同上，原页 $q^-:X^-\to X$ | 公式/交换图 |
| 7 | p.28 / L218 | 这一定理**于是是** Mirković–Vilonen 的定理 | 这一定理**因而是** | 「于是是」不成词 | 中文 |
| 8 | p.28–29 / L218 | `$\wt{M}\to\wt{G}$。这从\srcpageinl{29}其中容易得到……` | `$\wt{M}\to\wt{G}$。\srcpageinl{29}由此容易得到……` | 原文 “from which it is easy to get…”；顺带把 p.29 锚点回到句界 | 中文+体例 |
| 9 | p.25 / L87 | 锚点置于 L97「这一定理把表示论中的…」 | `\srcpageinl{25}` 前移至 L87「其中 $B\in D(\Bun_G,\Lambda)$…」 | p.25 首行 “for $B\in D(\Bun_G,\Lambda)$, where $\pi$…” | 体例 |
| 10 | p.30 / L244 | 锚点置于 L270「至此我们已经定义了…」 | `\srcpageinl{30}` 前移至「…并且在其上，$\GG_m$-作用在 $t\to0$…」 | p.30 首行 “$t\in\GG_m$-action admits a limit as $t\to0$” | 体例 |
| 11 | p.35 / L448 | 锚点置于 L457「包含 $D(G(E),\Lambda)\hookrightarrow…」 | `\srcpageinl{35}` 移至 `\item[(iii)]` 之后 | p.35 首行 “(iii) The spectral Bernstein center…” | 体例 |
| 12 | p.23 / L34 | 译注末「它指 [Sch17a] 中引入的维数概念，细节见报告 §6 未解项。」 | 改为「……它指 [Sch17a] 中引入的维数概念——原文 §IV 把它与 Krull 维数、上同调维数并列为三种维数——其精确定义见 [Sch17a]，本译本未作改动。」 | p.41 第 50 行；书稿不能引用内部报告 | 译注 |
| 13 | p.31 / L292 | 只说「由 $\Div^1$ 是单点……再逐步剥离 $(Div^1)^I$」 | 补出：对 $\lvert I\rvert$ 归纳 + 融合积分解为外积；单因子用 $\Spd\dot E$ 是点 ⇒ $D(\Bun_G,\Lambda)\cong D(\Bun_G\times\Spd\dot E,\Lambda)$，$\varphi$ 作用给 $\Div^1$ 方向局部系统 | 原文 “One reduces to $I=\{*\}$ by an inductive argument” 未展开的步骤；证据标 `I:推理` | 译注 |
| 14 | p.32 / L347 | 引文作 `$D([*/G_b(E)])\times\prod\cdots,\Lambda)$`，称「右括号错位」 | 引文改为 `$D([*/G_b(E))]$`：多的 `)` 在 `[*/G_b(E)]` 的**右方括号之前**，使 `D(` 提前闭合 | 400 dpi 回图（原页 p.32 第 3 行） | 译注 |
| 15 | p.36 / L519 | 与取 **congredients** 相容（保留英文） | 与取**反变（contragredient）表示**相容；`\yizhuw` 说明原文印 congradients、应为 contragredients | 原页 p.36 第 41 行、p.319 同；书目 [AV16] 标题 “Contragredient representations…” | 术语+译注 |

合计 15 条：公式/交换图 4、体例 3（+1 条并入第 8 条）、译注 4、中文 3、漏段 1；术语 1 条与第 15 条重合。

**编译方式说明**：`build.bat check sections/s02-chI-2.tex pb` 在本机 MSYS bash 下经 `cmd //c` 调用时只弹 cmd 标题、不执行（`cmd //c "echo hi"` 同样无输出；加 `MSYS_NO_PATHCONV=1` 亦无效）。为不改 `build.bat`，改为等价复刻其 `:check` 分支：本目录写 `_check_pb.tex`（`\documentclass[11pt,openany]{book}` + `\input{preamble}` + `\input{"sections/s02-chI-2.tex"}`），再以 `xelatex -interaction=nonstopmode -halt-on-error -jobname=_check_pb _check_pb.tex` 跑两遍。命令与产物名、失败判据（`errorlevel 1` ⇒ `[FAIL]`）与 build.bat 一致。

## 3 未改动但存疑

1. **译注 L111 后半**（p.25「部分 (v) 本质上是形式推论」）：注文写「由 (iii) 中 $i^{b*}$ 的左伴随保持紧性……逐项验证」，但这只解释了 (iii) 的紧性判据，没有说明 (v) 的「ULA ⇔ 容许」为何由此形式推出。我无法给出比原文更可靠的补证，保持原样。
2. **译注 L180**（p.27「在 $\Lambda$ 上平坦」）：注文把定义 I.6.2 的条件解释成「等价于 $A$ 的每一阶上同调层在 $\Lambda$ 上平坦」。这与原文括注「for all $\Lambda$-modules $M$, also $A\otimes^{\fsL}_\Lambda M$ is perverse」是否严格等价，我未能确证（涉及反常 $t$-结构与 $\Lambda$-平坦性的交换），故不改，留待 Chapter VII 校对时定。
3. **黑名单词 2 处**（p.28「不难证明」、p.31「显然」）：分别对译 “It is easy to deduce”“clearly”，语义忠实，删去反而损失原文语气，按「只改错不改风格」保留。
4. **A 块末尾悬空「对于」**：`s01-chI-1.tex` 最后一句停在「对于」，本节首句原为「……对每个这样的截面」。我已删本节多余的「对」，但 A 块那个「对于」仍在，成书后会是「……对于每个这样的截面」——这其实读得通，但 A 块若另有收尾句被漏掉则问题更大，须 A 块校对者确认。
5. **glossary 第 8 行**「Langlands 对偶群」与裁定「朗兰兹对偶群」不一致：正文（p.28 定理 I.6.3 等）已按裁定，未动 glossary。
6. **原文自身的 3 处笔误**（均已用译注处理，未改原文语义）：p.29 末 “etc.\ .” 双句点；p.32 显示式 `D([*/G_b(E))]` 括号提前闭合；p.36 (iv) “congradients”（应为 contragredients）。
7. **译手报告缺失**：`工程文件/reports/chI-b.md` 不存在，故任务书要求的「译手 5 条疑点」只能从译手 trace 与疑点清单反推，逐条结论见 §4 末。

## 4 译注抽查

10 条 `\yizhu` 全读，判定如下（「合格」= 依据真实、答其所问；「补强」= 依据对但没答到点子上；「重写」= 已改）：

| # | 行 | 主题 | 判定 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | L34 | `dim.\ trg` 不译 | 重写 | 原注以「见报告 §6 未解项」收尾，书稿中无此物；改为引原文 §IV 三种维数并列（p.41），并说明本译本不改 |
| 2 | L54 | 固体模（Clausen–Scholze） | 合格 | 引 [CS] 与第七章，说明为何要换掉 $\ell$-进完备化 |
| 3 | L111 | 「容易」与「形式推论」 | 补强 | 前半（挠系数下 (i)(ii)）合格；后半未答 (v) 何以形式，见 §3-1 |
| 4 | L180 | $\Lambda$-平坦 | 补强 | 把 i.e. 展开成显式条件，方向对，但「等价于逐阶上同调平坦」待确证，见 §3-2 |
| 5 | L206 | 「必然与 $\star$ 一致」（Eckmann–Hilton） | 合格 | 论证正确：两幺半结构互相交换 ⇒ 交换性约束给出自然同构 |
| 6 | L242 | p.29 末 “etc.\ .” | 合格 | 判为排版笔误，处理得当 |
| 7 | L262 | Thm I.6.5「本质像上」 | 合格 | 把「限制到本质像」解释为 $L^-\to L^+$ 在 $\pi$ 的像上同构，与 Braden 型陈述吻合 |
| 8 | L292 | 「出奇地形式化」的归纳 | 重写 | 原注只说「由 $\Div^1$ 是单点……逐步剥离」，没有回答「补了哪一步」；新注给出归纳骨架与「一个点」的确切含义（$D(\Bun_G)\cong D(\Bun_G\times\Spd\dot E)$），并明确标 `I:推理` |
| 9 | L347 | p.32 显示式括号 | 重写 | 原注把原文引错（说右括号在 $\Lambda$ 前）；回图后改为「多的 `)` 在 `[*/G_b(E)]` 的右方括号前」 |
| 10 | L519 | congradients | 重写 | 原注保留英文并称「疑为 [AV16] 专门术语」；实为 contragredient 的拼写笔误，已译出并注明 |

**译手 5 条疑点复核结论**

1. **`dim.\ trg`**：结论——不译是对的（symbols.tsv 与原文 p.23/25/29 一致，指 [Sch17a] 的维数），注文已补依据。**已结**。
2. **congredients**：结论——原文印的是 **congradients**（p.36、p.319 两处一致），据 [AV16] 标题与文意应为 contragredients，属原文拼写笔误；译文改「反变（contragredient）表示」。**已结**（并建议 Lead 把该书原文笔误记入勘误表）。
3. **定理编号括注**：结论——20 个编号对象与原书页逐一对应，`\ref` 全部解析（编译无 undefined reference），括注格式「定理 0.5.x (I.9.6)」由 preamble 决定、成书为「1.9.6 (I.9.6)」，非本节问题。**已结**。
4. **p.31「出奇地形式化」的归纳**：结论——原文只有一句 “One reduces to $I=\{*\}$ by an inductive argument”，归纳与「一个点」两步都没写；已按融合积 + $\Spd\dot E$ 是点补出，标为推理。**已结（推理，非引文）**。
5. **p.28 PGL₂ 细节**：结论——译文与原文一致（“everything reduces to $G=\mathrm{PGL}_2$, which is easily analyzed by means of the minimal Schubert cell…the minimal Schubert cell $\PP^1$ of $\Gr_{\mathrm{PGL}_2}$”），原文确实未给计算；译注 L262 区域未涉及此点，未加注也不算漏（属「作者留给读者的 easy」）。**已结，不改**。

## 5 编译与统计

- 编译：xelatex 两遍，`EXIT=0`，`Output written on _check_pb.pdf (14 pages)`，log 中 `!` 错误 0 条，无 undefined reference。
- 页锚点：`python ../工程文件/tools/check_pagemarks.py _check_pb --start 23 --end 36 --pdf`
  - `[ok] 14 个锚点全部在 PDF 中可见`
  - `[ok] p.23、p.36 锚点齐全`
  - `_check_pb.pagemarks` 内容：23 24 25 26 27 28 29 30 31 32 33 34 35 36
- 文件：529 行，UTF-8 无 BOM，无绝对路径。
- 改动：15 处（公式/图 4、体例 3、译注 4、中文 3、接缝 1；术语 1 与第 15 条重合）。
- 核对方式：5 个 tikzcd 全部按原页 300–400 dpi 渲染图逐个核对箭头落点与标签；3 个重点公式（p.24 极限、p.32 括号、p.36 单词）单独放大确认。

## 6 给 Lead 的建议

1. **A 块 p.23 收尾必须处理**：`s01-chI-1.tex` 末尾的「对于」要么删，要么补全被截断的句子。这是全书唯一跨文件的句子接缝，成书前请 A 块校对者确认（我已把本节一侧的多余「对」与省略号删掉，现在读作「……对于每个这样的截面」尚可，但 A 块若丢了半句就看不出来）。
2. **原文笔误建一张勘误表**：本块就发现 3 处（p.29 “etc. .”、p.32 括号提前闭合、p.36 “congradients”），另有 p.22 “is a also consequence”。建议 Lead 统一登记，译注里只写「原文如此」，勘误表集中说明，避免每条译注各写一套。
3. **tikzcd 的 q^±/p^± 必须按原页箭头的落点核对，不能只看标签**：本块 p.29、p.30 两个图的 `q^-` 都挂在错误源点上（源点应是 $X^-$/$\mathrm{Gr}_{P^-}$，不是 $X$/$\mathrm{Gr}_G$），编译与「标签齐全」都查不出来。建议其他块凡有 Braden/双曲局部化型四节点图的，一律回原页看箭头头部落在哪个节点。
