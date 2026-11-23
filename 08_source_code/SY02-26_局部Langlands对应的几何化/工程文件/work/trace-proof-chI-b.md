# 块 B · 校对决策记录（trace-proof-chI-b）

四栏：判断点 / 依据 / 结论与理由 / 事后确认。记号：`A:` 有原文或工程依据，`B:` 有外部文献依据，`I:` 本人推理，`J:` 本人判断。范围 §I.5–§I.9（p.23–36），对象 `源码/sections/s02-chI-2.tex`（529 行），产出 `工程文件/reports/proof-chI-b.md`。

## 一、校对顺序与范围

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| 先通读还是边读边改 | TASK「跳步与公式是重点」 | **先通读整块 529 行 + 原文 14 页**，再回头逐条定夺。跳步错（如 q^- 方向）单看一句看不出来，要看图表与前后函子定义 | A: 通读后一次列出 8 类疑点，逐条回图核销 |
| 是否把 A 块末句「对于」一并改掉 | 红线「不动他人 sections」 | **不改**。A 块 `s01-chI-1.tex` 末尾的「对于」只能由 A 块删；我只删本节多余的「对」与省略号，把跨文件接缝写进报告 §6-1 | A: `s01-chI-1.tex` 末行；报告 §0-1、§6-1 |
| 页锚点只信 `check_pagemarks` 吗 | 该脚本只查「锚点是否印出」，不查位置 | **不信**。按原文每页首行人工定位，发现 p.25/p.30/p.35 三个锚点晚 5–26 行，p.29 锚点落在一个词中间 | A: 脚本两 `[ok]` 之后仍改 3 处；`_check_pb.pagemarks` 仍 14 个 |

## 二、真实弯路（走过又退回）

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| ① 编译直接调 `build.bat` | TASK 规定 `cd 源码 && build.bat check sections/s02-chI-2.tex pb` | MSYS bash 下 `cmd //c "build.bat …"` 只打印 cmd 标题就返回 0，`cmd //c "echo hi"` 也不回显；加 `MSYS_NO_PATHCONV=1` 仍无效。**改为复刻其 `:check` 分支**：手写 `_check_pb.tex` + 直接调 MiKTeX 的 `xelatex -jobname=_check_pb`，判据与产物名同 build.bat。build.bat 未动 | A: 两次 `cmd //c` 输出仅版本横幅；复刻后 EXIT=0、14 页 |
| ② p.32 括号位置 | 译手译注称「右括号错位，应包住整个积」 | 首轮信了译注，把「右括号在 $\Lambda$ 前」写进备查。**回 400 dpi 图后发现**原文是 `D([*/G_b(E))]`：多的 `)` 在 `[*/G_b(E)]` 的右方括号**之前**，使 `D(` 提前闭合。译注引文与描述都要改，正文排印反而本来是对的 | A: `_chkb/p32_zoom3.png`；译注 L347 重写；报告 §2-14 |
| ③ p.24 极限方向 | `01_pages/p024.txt` 抽成 `lim ←− n`（折行） | 抽取文本里箭头与 `n` 分行，先按「可能是行内 lim」搁置。**回图**见 `lim` 正下方一个左向箭头、`n` 在其下，确定为逆向极限 `\varprojlim`。教训：极限/上下标一律回图，不信 txt | A: `_chkb/p24_lim.png`；`\varinjlim_n` → `\varprojlim_n`；报告 §2-2 |
| ④ 想把 glossary 一起改 | glossary 第 8 行「Langlands 对偶群」与裁定「朗兰兹对偶群」冲突 | 一度想顺手改 glossary 对齐。**红线禁止**，且裁定优先于 glossary。改为：正文按裁定（已是「朗兰兹对偶群」），glossary 的冲突写进报告 §0-3、§3-5 | A: 裁定第 3 条；`grep 朗兰兹对偶群` 命中正文 |

## 三、公式与交换图

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| p.29 / p.30 两个 tikzcd 的 `q^-` 挂哪个节点 | 原页箭头的**落点**（箭头头部画在 Gr_G / X 上），配合 CT^- = R(p^-)_*R(q^-)^! 与 L^- 的定义 | `\arrow[dr,"q^-"']` 把源点写成 Gr_G / X，方向反了。改为在 Gr_{P^-} / X^- 上 `\arrow[ul,"q^-"]`。**判据是箭头落点，不是标签位置**；标签左右侧是排版细节，不动 | A: `_chkb/p29_bottom.png`、`p30_diag.png`；改后重编译 0 error |
| 另外 3 个图要不要动 | p.25 三点图、p.26 卷积图、p.30 Hecke 图 | 逐个回图：`[*/G_b(E)] ←q_b— M_b —π_b→ Bun_G`、`Hck×Hck ←(p1,p2)— L^+G\LG×_{L^+G}LG/L^+G —m→ Hck`、`Hck 上、q→ℋck、h_1→Bun_G、h_2→Bun_G×(Div¹)^I` 均与原页一致，**不动** | A: `_chkb/p26_bot.png`、`p30_heck.png`；报告 §1-3 |
| 「态射空间是有限维的」 | 原文 “the morphism spaces between constructible sheaves are finite” | 有限 vs 有限维是两回事（前者是集合有限，后者是 $\Lambda$-模有限生成）。改「有限的」 | A: p.24 第二段；报告 §2-3 |
| 「自同态代数 Hecke 代数」 | 原文 “are Hecke algebras, which are infinite-dimensional” | 原句缺谓语、读不通，且 `which` 的先行词是 Hecke 代数。最小修：补「是」+「而后者」 | A: p.24 同段；报告 §2-4 |

## 四、术语与译注

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| `congredients` 怎么处理 | 原页 p.36 第 41 行、p.319 同；书目 [AV16] = Adams–Vogan, *Contragredient representations and characterizing the local Langlands correspondence* | 原文印 **congradients**，是 contragredients 的拼写笔误，不可能是「配料」之类的术语。译「反变（contragredient）表示」，`\yizhuw` 保留原拼写并说明笔误。**不**擅自写进 glossary，译名报 Lead 冻结 | B: p.351 书目；A: 两处原页同形；报告 §4-10 |
| 3 条「见报告 §6 未解项」的译注 | 书稿是独立成品；`工程文件/reports/chI-b.md` 根本不存在 | **一律改写成自足表述**，不删译注（译注承载译手的核查工作，删了信息就没了）。dim. trg 补 §IV 三种维数；「出奇地形式化」补归纳骨架；congradients 补书目依据 | A: 报告 §2-12/13/15 |
| 「出奇地形式化」补到哪一步 | 原文只有 “One reduces to $I=\{*\}$ by an inductive argument” | 补两层：① 对 $\lvert I\rvert$ 归纳，用融合积把算子分解为外积；② 单因子情形 $\Div^1=\Spd\dot E/\varphi^\ZZ$ 在 v-拓扑下是点，故 $\Bun_G\times\Spd\dot E\to\Bun_G$ 为同构、$\varphi$ 作用给局部系统。**明确标 `I:推理`**，不冒充原文 | I: 由原书 p.28 融合积同构与 p.31 该句推出；报告 §4-8 |
| 黑名单词要不要清 | grep 得 p.28「不难证明」、p.31「显然」 | 分别对译 “It is easy to deduce”“clearly”，是原文语气，不是译手偷懒。**不改**，写进报告 §3-3 | A: 两处英文原句；报告 §1-10 |

## 五、编译与交付

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| 编译验收用哪个入口 | TASK 指定 build.bat；红线「不动 build.bat」 | 因 `cmd //c` 在本机不执行，**等价复刻 check 分支**（同 `\documentclass`、同 preamble、同 jobname 规则、同 halt-on-error），未改任何构建脚本 | A: EXIT=0、`Output written on _check_pb.pdf (14 pages)`、log 无 `!` |
| 锚点验收 | TASK 要求两个 `[ok]` | 跑 `check_pagemarks.py _check_pb --start 23 --end 36 --pdf`，得 `[ok] 14 个锚点全部在 PDF 中可见`、`[ok] p.23、p.36 锚点齐全` | A: 脚本原文输出；`_check_pb.pagemarks` = 23…36 |
| 临时裁图脚本与产物 | 工程整洁 | 校对期间用 `工程文件/work/crop_chI_b.py` + `_chkb/`，交付前**删除**，不在工程里留临时文件 | A: 交付清单只有三文件 |
