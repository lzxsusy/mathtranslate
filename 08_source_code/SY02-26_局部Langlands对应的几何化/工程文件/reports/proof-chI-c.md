# 块 C 校对报告（§I.10 尾–§I.13，原书 p.39–p.44）

- 校对对象：`源码/sections/s03-chI-3.tex`（90 行，UTF-8 无 BOM；校对前 94 行）
- 上接：`源码/sections/s02b-chI-10.tex`（§I.10 正文，Lead 补译；本报告只改其 1 处页锚点，见 §2 #9）
- 原文：`00_原文/fargues-scholze-2102.13459v4.pdf` p.39–p.44，逐页文本 `01_pages/p039.txt`–`p044.txt`，另以 150 dpi 渲染原页逐段核对分段、公式与脚注
- 依据：`工程文件/work/TASK-proofread.md`、`BRIEF.md` §4/§5、`SPEC.md`、`work/glossary.tsv`、`symbols.tsv`、`术语裁定.md`、译手报告 `reports/chI-c.md`、`work/trace-chI-c.md`

## 0 结论

**可交付。** 块 C 内发现 **8 处问题，全部已改**（分段 1、漏译 1、术语 2、空格 1、未译英文 1、译注来源 1、页锚点 1）；另有 **1 处任务书授权的跨文件页锚点修改**（`s02b-chI-10.tex` 的 p.38）。**§I.13 记号表 19 条逐条与原文 p.44 核对：不缺、不并、条目顺序与原文一致，页码引用全部正确。**

s03 与上节 s02b 的衔接正常：`注 I.10.3` 由计数器自动接续（原文件 Remark 不带可选参数），与 s02b 内 `定理 I.10.1`、`猜想 I.10.2` 构成 I.10.1–I.10.3，**无重复开节、无编号错位**。

编译：`_check_pc.pdf` 6 页 0 error；整书 `main.pdf` 42 页 0 error；两项页锚检查（单块 p.39–44、整书 p.7–44）均为两个 `[ok]`。

## 1 逐维度

| # | 维度 | 检查量 | 问题数 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | 漏段/并段 | p.39–p.44 共 6 页逐段比对 | 1 | p.39 §I.11 首段原文为**一整段**（"Finally, … correspondences. Fargues [Far04] has proved …" 同行续排、无缩进），译文拆成两段 → 已合并（§2 #2） |
| 2 | 漏译/多译 | 6 页逐句 | 1 | p.40 首句漏 "**on the Fargues–Fontaine curve**" → 已补（§2 #3）；其余无增删 |
| 3 | 术语 | 全篇 20+ 术语对 glossary/裁定 | 2 | `isocrystal` 译「同晶」2 处，glossary 第 16 条与本库 SY02-18 均为「**等晶体**」→ 已改（§2 #3、#4）；其余（完满空间、菱形、固体、游走算子、野惯性子群、G-主丛、Hecke 特征层、反常 t-结构）均一致 |
| 4 | 公式 | 全部显示式 5 个 + 行内式逐个回原页 | 0 | 译手报告的 6 处 txt 失真已在译文中正确处理：`\cO_X^n\to\cO_X(\frac1n)`（p.40）、`\wt{\mathbb{B}}^n_C`（p.42）、`\ol{\QQ}_\ell`×2（p.39）、p.42 有/无上划线并列、`D_{\text{ét}}` 的 é（p.41）、`\ul X`（p.44）；原页渲染逐一复核无误 |
| 5 | 编号 | 2 个编号对象 + s02b 衔接 | 0 | `注 I.10.3`（自动）、`问题 I.11.1`（question 环境自动编号，原文 Problem I.11.1 的 problem 环境 preamble 未定义，见 `reports/chI-c.md` §7）；与 s02b 无重号 |
| 6 | 译注 | 6 条全部审读 | 1 | 1 条来源把 §I.10 写成 §I.11 → 已改（§2 #8）；内容核对见 §4 |
| 7 | 中文 | 全篇 | 2 | 「评述。 [Sch17a]」多余半角空格 → 删（§2 #5）；记号表第 12 条「underlying 拓扑空间」英文未译 → 「底层拓扑空间」（§2 #7） |
| 8 | 体例 | 6 个页锚点 + 环境 | 2 | p.43 页锚全书编译后丢失（原为独立行 `\srcpage{43}`，已在段首无可再挪）→ 改 `\srcpageinl{43}` 嵌入段首（§2 #6）；p.39 页锚紧跟 `\begin{remark}` 时全书编译丢失 → 移入 remark 首句，现印成页边 `p.39`（§2 #1） |
| 9 | 编译 | xelatex 2 pass（check + 整书） | 0 | 0 error、0 Overfull；Underfull 单块 2 / 整书 3（均为 `\allowbreak` 处中文断行，见 §5） |
| 10 | 黑名单 | grep「显然/众所周知/不难/容易看出/自然」 | 0 | 共 5 处（L26「不难证明」、L35「容易看出」、L37「变得显然」、L39「非常不自然」、L48「最自然的结果」），均一一对应原文 "it is not hard to prove" / "It is easy to see" / "immediate" / "very unnatural" / "the most natural results"，非滥用，未改 |

## 2 改动清单

改动全部落在块 C 文件内，仅 #9 为任务书授权的跨文件页锚点。

| # | 位置（改后行号） | 原译/原稿 | 改后 | 依据 |
| --- | --- | --- | --- | --- |
| 1 | `s03:10` | `\srcpage{39}` 单独一行，位于 `\begin{remark}` 之前（全书编译此页锚丢失，页边空白） | 移入 remark 首句：「…中的猜想。`\srcpage{39}`理想地，…」 | 原书 p.39 页首即 Remark I.10.3；`\marginnote` 紧接 `\begin{remark}` 且处于页首垂直模式时被丢弃，移入首句（水平模式）后正常印出（实测页边 `p.39`，x=51.2pt） |
| 2 | `s03:15` | 原文 p.39 首段被拆成 L15、L17 两段（「…得到了实现。」／「此外，Fargues [Far08] 还证明了…」） | 合为一段 | 原页 "…correspondences. Fargues [Far04] has proved …" 同行续排、无缩进，是一整段（150 dpi 渲染确认） |
| 3 | `s03:17` | 「…不过就是极小修正 $\cO_X^n\to\cO_X(\frac{1}{n})$ 空间的两种对偶描述`\srcpageinl{40}`，取决于…」 | 「…不过就是 **Fargues--Fontaine 曲线上**极小`\srcpageinl{40}`修正 $\cO_X^n\to\cO_X(\frac{1}{n})$ 空间的两种对偶描述，取决于…」 | p.40 首句 "…the space of minuscule **(p.39 末行止于 minuscule)** / modifications O_X^n → O_X(1/n) **on the Fargues–Fontaine curve**, depending on which bundle is fixed…"：补漏译，并把 `\srcpageinl{40}` 移到原页断行处「极小｜修正」之间 |
| 4 | `s03:17`、`s03:21` | 「与某个**同晶**（isocrystal）相伴的向量丛」／「后者用基本的 $G$-**同晶**来精细研究 $L$-包」 | 「**等晶体**」×2 | glossary 第 16 条 isocrystal＝等晶体（本库 SY02-18）；s01 已用 23 次「等晶体」 |
| 5 | `s03:26` | 「我们将在下文评述**。 ** [Sch17a] 的一项中心技术」 | 「我们将在下文评述。[Sch17a] 的一项中心技术」 | 中文句号后不应有半角空格（SPEC 中文标点条） |
| 6 | `s03:44` | `\srcpage{43}` 单独一行（全书编译丢失） | 「在此期间，`\srcpageinl{43}`几何 Langlands 纲领中有…」 | 该段已是 p.43 起点的段首，无更早位置可挪；按任务书改 `\srcpageinl{N}`，实测印出〔p.43〕 |
| 7 | `s03:82` | 「空间 $S$ 的 **underlying** 拓扑空间」 | 「空间 $S$ 的**底层**拓扑空间」 | `symbols.tsv`：`\|X\|`＝底层拓扑空间；中文正文不留未译英文 |
| 8 | `s03:10`（译注来源） | `{A：原文 §I.11 p.39 脚注 7；Hansen [Han24]}` | `{A：原文 §I.10 p.39 脚注 7；Hansen [Han24]}` | 该脚注属 §I.10 末（Remark I.10.3），不属 §I.11 |
| 9 | `s02b:63` | `\srcpage{38}` 单独一行（全书编译丢失） | `\srcpageinl{38}证明的关键部分其实是上面定理 I.8.2 的最后一部分，…` | 任务书授权；该锚点已在段首无更早位置，改行内后实测印出 |

> 说明：任务书点名的另外两处丢失锚点中，**p.30 在我动手前已由并行进行的块 B 校对改为 `\srcpageinl{30}`**（`源码/sections/s02-chI-2.tex:244`，位于「…并且在其上，`\srcpageinl{30}`$\GG_m$-作用在 $t\to0$…」段中；该文件在我准备修改时被外部改写，我方 `\srcpage{30}` 的修改未落地）。我复核了其三处锚点（p.25/p.30/p.35）的可见性与顺序，`check_pagemarks` 与 `page_map` 均通过，未再改动该文件。

## 3 未改但存疑（留 Lead 裁定）

1. **「双射？3839」**：Remark I.10.3 末尾原文脚注（`\footnote`）与 hadal 译注（`\yizhu`）相邻，两个脚注上标连排，正文印成「典范地双射？^38^39」，读者易误读为页码。改法涉及全书译注体例（是否允许译注并入作者脚注），本块未动。
2. **`s03:10` 的 `\srcpage{39}` 现印在「…中的猜想。」与「理想地」之间**（行内位置在第 1—2 行）。若 Lead 希望全书页锚统一为「段首独立行」或统一为行内，此处需随全库一起调整；目前是「页边码 + 句中断点」的组合。
3. **原文 p.39 页首的环境边界**：`\srcpage{39}` 最符合语义的位置是 `\begin{remark}` 之前，但该位置全书编译必丢（`marginnote` 在页首垂直模式失效）。恢复到环境前需改 `preamble.tex`（未动，红线）。
4. **「极小〔p.40〕修正」**：页锚插在复合名词中间，阅读略打断；但这是原文 p.39/40 断行的唯一忠实位置（"-minuscule | modifications-"），若改为句末则失去「原页起点」意义，故保留。
5. **记号表第 12、17 条**（`|S|`、`*`）与第 1 条内嵌的 `\FF_q`：前者为原文正文隐含使用的记号、后者原文即在 $E$ 的条目内定义。当前 19 条与原文显式定义符号数一致，但若 Lead 要求「19 条＝原文 19 个分号条目」的严格口径，需重排第 1、12、17 条（译手报告 `chI-c.md` §3 已声明此处理）。

## 4 译注抽查（6 条，全数审读）

| # | 行 | 内容 | 来源 | 核对 |
| --- | --- | --- | --- | --- |
| 1 | `s03:10` | 「反常—凝聚」（perverse-coherent）$t$-结构：glossary 仅收 perverse t-structure；原文加引号说明未定名，译文保留英文 | A：p.39；glossary.tsv | ✓ 原文 p.39 作 "perverse-coherent"，带引号；glossary 确无该词条 |
| 2 | `s03:10` | hadal 指海洋「深渊带」，作者对 Hansen 所引入 $t$-结构的戏称；[Han24] 照录 | A：p.39 脚注 7（改动后） | ✓ 原文脚注 7："…by introducing the hadal t-structure on Bun_G"；hadal 词义准确 |
| 3 | `s03:24` | 原文作 "etc.pp."，为拉丁语套语 "et cetera perge perge" 的缩写，非笔误 | A：p.41 | ✓ 原文 p.41 确作 "etc.pp."（德语式套语写法），译按「等等」处理合理 |
| 4 | `s03:32` | 「完满球」即完满空间意义下的 $n$ 维球；glossary 仅收 perfectoid space | A：p.42；glossary.tsv | ✓ 原文 "where B̃^n is a perfectoid ball"；译名与「完满空间」同词根一致，已声明待并入术语表 |
| 5 | `s03:37` | 原文 "Our attacks on this failing, a third key idea comes in:" 疑脱 "In" | A：p.42 | ✓ 原页确作此（语法上缺 "In"），标为疑似笔误并按原意补足，符合 BRIEF §4 第三类 |
| 6 | `s03:62` | sifted colimit＝筛范畴为指标的余极限，未入 glossary，暂译「筛余极限」并保留英文 | A：p.44（应为 p.44，来源串现写 §I.13 p.44） | ✓ 原文 p.44 "freely generated under sifted colimits by polynomial algebras"；译法与正文一致 |

结论：6 条均属 BRIEF §4 规定的三类必注（术语首现 4、跳步/歧义 1、疑似笔误 1），来源可查，无凭空杜撰；仅第 2 条来源的节号已修（§2 #8）。

## 5 编译与检查统计

```
cd 源码 && build.bat check sections/s03-chI-3.tex pc
  → Output written on _check_pc.pdf (6 pages)
  → [OK] _check_pc.pdf
  → log：0 error（`!` 计数 0）、0 Overfull、2 Underfull

python ../工程文件/tools/check_pagemarks.py _check_pc --start 39 --end 44 --pdf
  → [info] _check_pc.pagemarks 共 6 个锚点
  → [ok] 6 个锚点全部在 PDF 中可见
  → [ok] p.39–p.44 锚点齐全

cd 源码 && build.bat
  → Output written on main.pdf (42 pages) → [OK] main.pdf
  → log：0 error、0 Overfull、3 Underfull

python ../工程文件/tools/check_pagemarks.py main --start 7 --end 44 --pdf
  → [info] main.pagemarks 共 38 个锚点
  → [ok] 38 个锚点全部在 PDF 中可见      ← 修复前为 [FAIL] 缺 [30, 38, 43]
  → [ok] p.7–p.44 锚点齐全

python ../工程文件/tools/page_map.py main --start 7 --end 44 --tsv ../工程文件/work/pagemap_chI.tsv
  → [info] 38 个原文页锚点
  → [ok] 原文页 7–p.44 全部有定义
  → [info] 原文页 7–44 → 译本页 1–36
  → [ok] 写入 ..\工程文件\work\pagemap_chI.tsv
```

Underfull 3 处均为 `\allowbreak` 附近的短行（致谢人名串、`[GKRV22]` 长标签），无 Overfull、无版面溢出；块 C 无 `\emergencystretch` 越界残留（`2.5em` 在 `s03:43` 置、`s03:46` 复位）。

## 6 给 Lead 的建议

1. **全书「定理/猜想」标题重复编号，建议一次性修**：所有手写可选参数都会在自动编号后重复打印，实际印成「定理I.6.5 (I.6.5).」。共 **43 处**（s01 21、s02 20、s02b 2；s03 的 remark/question 未带参数，正常）。最省事的修法是用脚本删除 `\begin{theorem}[I.x.y]` 的可选参数（或统一改成 `\begin{theorem}` 并保留 `\label`），属别人文件的批量改动，我没有动。
2. **术语「condensed」两套译法并存，请裁定后统一**：`术语裁定.md` 作「凝聚」，`glossary.tsv` 第 148 行作「凝聚态」；正文 s02/s03 用「凝聚数学／凝聚集」，**s02b 用「凝聚态 $\Lambda$-模」5 处**（`s02b:19` 及其译注）。另 glossary 第 8 行 `Langlands dual group` 仍写「Langlands 对偶群」，与裁定的「朗兰兹对偶群」不一致（块 B 校对报告亦已提出）。两处都属 glossary 侧，按规矩未改。
3. **前置件与缺件**：①`front-translator-note.tex` 仍是 `\chapter*{译者说明}` +「（待写）」占位；②目录（ii）之后有一张空白页 iv，页眉仍残留「目录」（`\tableofcontents` 章节标记未随 `\mainmatter` 清除）；③`工程文件/reports/chI-b.md`（B 块译手报告）不存在，B 块自报译注数无法核对（`proof-chI-b.md` 亦已指出）。三项均需 Lead 或 B 块译手补齐，建议交付前处理。

---

## 7 全书统稿检查（Chapter I，p.7–p.44）

本节为**只读**检查：除任务书授权的 3 个页锚点（p.30/p.38/p.43，其中 p.30 由并行进行的块 B 校对落地）外，未改动 A/B 两块的任何 tex，问题一律记在此处。

### 7.1 术语一致性（对照 `glossary.tsv` 与 `术语裁定.md` 逐条 grep）

| 术语 | 基准（glossary / 裁定） | s01 | s02 | s02b | s03 | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| isocrystal | 等晶体 | 23（+1 词源注「同晶」） | 0 | 0 | 2 | ✅ 一致（「同晶」仅出现在 s01 的词源译注里，非译法） |
| perfectoid space | 完满空间 | 15 | 2 | 0 | 8 | ✅ |
| diamond | 菱形 | 13 | 6 | 0 | 5 | ✅ |
| solid | 固体 | 0 | 5 | 0 | 4 | ✅ |
| excursion operator | 游走算子 | 0 | 6 | 0 | 2 | ✅ |
| G-torsor | G-主丛 | 26 | 2 | 1 | 1 | ✅（无「扭子/挠子」误译） |
| Langlands dual group | 朗兰兹对偶群（裁定） | 正文均作「朗兰兹对偶群」，仅 yizhu 记别名「Langlands 对偶群」 | — | — | — | ✅ 正文一致；glossary 第 8 行仍用旧名（见 §6.2） |
| L-parameter / L-packet / stack of L-parameters | L-参数 / L-包 / L-参数叠 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Hecke eigensheaf / wild inertia | Hecke 特征层 / 野惯性子群 | ✅ | ✅ | ✅ | ✅ | ✅ |
| perverse t-structure | 反常 $t$-结构 | 3 | 17 | 0 | 4 | ✅（s03 另用「反常—凝聚」译 perverse-coherent，已加译注） |
| **condensed** | **裁定＝凝聚；glossary＝凝聚态** | 2（凝聚信息） | 凝聚数学 1 | **凝聚态 $\Lambda$-模 5** | 凝聚数学 3、凝聚集 1 | ⚠️ **冲突**：s02b 用「凝聚态」，其余用「凝聚」；glossary 与裁定本身互相矛盾，按规矩报 Lead（见 §6.2），不自裁 |
| chI-b 报告缺失 | — | — | — | — | — | ⚠️ `reports/chI-b.md` 不存在，B 块术语自述无法核对（只能以正文实测为准，上表 s02 列即实测） |

### 7.2 `\section` 顺序（应 I.1…I.13 连续无缺）

| 编号 | 标题 | 文件:行 |
| --- | --- | --- |
| I.1 | 局部 Langlands 对应 | `s01-chI-1.tex:10` |
| I.2 | 总体图景 | `s01-chI-1.tex:37` |
| I.3 | Fargues–Fontaine 曲线 | `s01-chI-1.tex:408` |
| I.4 | $\Bun_G$ 的几何 | `s01-chI-1.tex:473` |
| I.5 | $\Bun_G$ 上的 $\ell$-进层 | `s02-chI-2.tex:41` |
| I.6 | 几何 Satake 等价 | `s02-chI-2.tex:129` |
| I.7 | shtuka 模空间的上同调 | `s02-chI-2.tex:267` |
| I.8 | L-参数叠 | `s02-chI-2.tex:358` |
| I.9 | L-参数的构造 | `s02-chI-2.tex:406` |
| I.10 | 谱作用 | `s02b-chI-10.tex:10` |
| I.11 | 思想的来源 | `s03-chI-3.tex:13` |
| I.12 | 致谢 | `s03-chI-3.tex:48` |
| I.13 | 记号 | `s03-chI-3.tex:54` |

**结论：I.1–I.13 共 13 节，连续、无缺、无重、无倒序**；跨文件接缝只有两处（I.4 在 s01→s02、I.10 在 s02→s02b、I.11 在 s02b→s03），接缝处没有重复开节（s02b 末尾无 `\section`，s03 开头直接是 Remark I.10.3）。

### 7.3 定理/定义编号（对照各块编号对齐表）

- 自动编号（`\newtheorem{theorem}{定理}[section]`，其余环境共用计数器）实测连续、无重无缺：
  I.2.1–I.2.15、I.3.1–I.3.5、I.4.1（s01）→I.4.2（s02）、I.5.1–I.5.2、I.6.1–I.6.5、I.7.1–I.7.3、I.8.1–I.8.3、I.9.1–I.9.6、I.10.1–I.10.3（s02b 前两个 + s03 的 remark 自动接续）、I.11.1（s03 的 question）。
- 与各块报告的对齐表逐条比对：A 块（`chI-a.md`）、B 块（`proof-chI-b.md` §1 #4「20 个编号对象」）、C 块（`chI-c.md` 编号表）**三方一致**。
- ⚠️ **但显示层重复**：所有手写 `\begin{theorem}[I.x.y]` 的可选参数都会在自动编号后再打印一次，实测印成「**定理I.6.5 (I.6.5).**」「**猜想I.10.2 (I.10.2).**」。共 43 处（s01 21、s02 20、s02b 2）。计数器本身无误，属排版缺陷，改法见 §6.1（未动别人文件）。
- ✅ s03 内 `注 I.10.3`、`问题 I.11.1` 不带可选参数，印出正常；与 s02b 的 I.10.1/I.10.2 衔接无错位。

### 7.4 `\yizhu` / `\yizhuw` 计数（与各块报告核对）

| 文件 | 实测 `\yizhu` | 实测 `\yizhuw` | 报告自述 | 结论 |
| --- | --- | --- | --- | --- |
| `s01-chI-1.tex` | 15（另有 1 处写在行首注释里，不计） | 0 | `chI-a.md` §4：共 15 条（术语 10、跳步/歧义 4、疑似笔误 1） | ✅ 吻合 |
| `s02-chI-2.tex` | 9 | 1 | `chI-b.md` **缺失**，无法核对；`proof-chI-b.md` §1 #5 记录「10 条全部审读」 | ⚠️ 实测 9+1；与 B 校对报告口径（10 条）一致 |
| `s02b-chI-10.tex` | 5 | 0 | 无译手报告（Lead 补译），`chI-c.md` §7 提及衔接 | ✅ 无异议 |
| `s03-chI-3.tex` | 6 | 0 | `chI-c.md` §4：共 6 条 | ✅ 吻合 |
| 合计 | **35** | **1** | — | — |

### 7.5 导言章与目录

- 整书 42 页：扉页 1（i）、目录 2（ii）、译者说明 3（iii）、空白 4（iv）、正文 5–40（译本页 1–36）、文献表与索引 41–42。
- **目录内容正确**：`译者说明 iii`、`I 导引 1`、`I.1–I.13` 页码 1/2/11/13/17/19/23/25/27/29/32/35/36，与正文实际页一致（已逐条核对渲染页）；`\subsection*{记号一览（译者整理）}` 为带星号小节，正确未入目录。
- ⚠️ **`译者说明` 仍是占位**：`front-translator-note.tex` 全文 3 行，正文只有「（待写）」。
- ⚠️ **目录后多出空白页 iv，页眉残留「目录」**：`\tableofcontents` 的章节标记未在 `\mainmatter` 处清除；修法在 `main.tex`/`preamble.tex`（红线，未动），建议 Lead 在 `\mainmatter` 前加 `\clearpage` 或对该页 `\thispagestyle{empty}`。
- ⚠️ 扉页作者栏印有「详参 `工程文件/README.md`」——书稿正文出现工程内部相对路径，建议交付前改为不带路径的说明（`main.tex` 内容，未动）。

### 7.6 锚点修复结果（任务书点名三处）

| 原页 | 原位置 | 处理 | 现状 |
| --- | --- | --- | --- |
| p.30 | `s02-chI-2.tex:270` 段首 `\srcpage{30}至此我们已经定义了…`（比原页起点晚 26 行） | 由并行进行的块 B 校对改为 `\srcpageinl{30}`，落在正确起点（`s02-chI-2.tex:244`「…并且在其上，$\GG_m$-作用…」段中） | ✅ 可见（pdfpage 27） |
| p.38 | `s02b-chI-10.tex:63` 段首独立行 | 本次改 `\srcpageinl{38}`（§2 #9） | ✅ 可见（pdfpage 35，段首缩进位） |
| p.43 | `s03-chI-3.tex` 段首独立行 | 本次改 `\srcpageinl{43}` 嵌入段首（§2 #6） | ✅ 可见（pdfpage 39） |

附带修好的：p.39 由独立行移入 Remark 首句后，页边码正常印出（pdfpage 36，x=51.2pt）。全书 38 个锚点现已全部可见，`check_pagemarks main` 与 `page_map main` 均两个/三个 `[ok]`。

> 误判更正（供后续校对参考）：译本页 23 页边出现的裸数字「25」「26」**不是**缺 `p.` 前缀的页边码，而是 `\yizhu` 脚注上标被挤到下一行行首（x≈95–113pt 即首行缩进位）。据此可以区分：真页边码在 x≈51.2pt，行内/行首锚点在 `〔p.N〕` 或缩进位。
