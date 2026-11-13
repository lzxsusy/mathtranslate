# PATCH_LOG —— Lead 的单点修复记录（R3/M6：每条修改都可追溯）

> 原则：不做正则批量改写正文；每条 exact-match、命中数必须 == 1，否则跳过并记录。
> 脚本：`work/tools/patch_c01.py`（markdown 粗体）、`patch_format.py`（图/公式）、`patch_circled.py`（圈码）。
> 每次落改后都重跑 `check.py` + `build.ps1` + `verify_pdf.py`。

## 第一轮（Lead 自己的译块 c01）

| # | 文件 | 位置 | 问题 | 处理 | 依据 |
|---|---|---|---|---|---|
| 1 | c01.tex | 7 处 | 残留 markdown `**…**`（PDF 会印出星号） | `**…**` → `\textbf{…}`（7 处，exact-match 各 1 次） | Gate 1 `MD_BOLD`；PDF 回读出现 14 个 `**` |
| 2 | c01.tex | 表 1 | 表格宽 69pt 超出版心 | `\footnotesize` + `\tabcolsep=3pt` + 内容列 `p{4.7cm}`、参考文献列 `p{4.0cm}` | log `Overfull \hbox (69.25pt)` |
| 3 | c-refs.tex | 生成器 | 参考文献 17pt/6pt Overfull（长 DOI/URL） | `gen_refs.py` 输出 \\begingroup 内加 `\sloppy`，重新生成 | log Overfull |

## 第二轮（跨文件排版修复，均为 exact-match）

| # | 文件 | 位置 | 问题 | 处理 | 依据 |
|---|---|---|---|---|---|
| 4 | tr05a.tex | B157 列表 | 圈码 ①②（U+2460/2461）在正文字体缺字 | `\item[①]`→`\item[（i）]`、`\item[②]`→`\item[（ii）]`；批注同步改述 | log `Missing character: There is no ①` ×7 |
| 5 | tr05a.tex | B167 后 | 底本 canvas 图「Orbits of $H_1$」被降级为一行题注 | 按 canvas 绘制指令（原点、`|p|`/`|q|` 两轴、一条双曲轨道）用 tikz 重画 + `\figtitle{2}{…}` | probe：`<canvas id="image-H1">` 及内联 JS 指令 |
| 6 | tr03a.tex | B112 开头 | 底本 canvas 图「Moment polytope for P^2」（三点三角形）被降级为例题标题 | 用 tikz 重画三点三角形 + `\figtitle{1}{…}`；例题标题收回为 `\begin{example*}` | probe：`<canvas id="fig:P2">` + JS 三点 (25,25)-(25,125)-(125,125) |
| 7 | preamble.tex | 图注宏 | 缺 `\figtitle` | 新增 `\newcommand{\figtitle}[2]{\caption*{…}}`（与 `\tabtitle` 同风格） | 图 1/图 2 需要手工编号图注 |
| 8 | tr03a.tex | B112 后批注 | 原批注说「不重绘 canvas」已与现状不符 | 改为「按 canvas 绘制指令用 tikz 重画为图 1，未改数学」 | #6 |
| 9 | tr02a.tex | B065 | 一行内公式 27pt 超出版心（无法断行） | 该行内公式改为独立公式 `\[…\]`（数学内容逐字不变）；独立公式数因此由 2 变 3（全工程 38→39，已在 README 说明） | log `Overfull 27.71pt`；`_disp.py` 比对 |
| 10 | tr03b.tex | B126 | 长公式 101pt 超出版心 | 外层包 `\resizebox{0.985\textwidth}{!}{$\displaystyle …$}`（数学内容逐字不变） | log `Overfull 100.98pt` |

## 第三轮（交叉校对报告落改，2026-11-04 11:20 前后）

> 6 位译者交叉校对（每人校一块），6 份报告见 `work/review/tr01.md`～`tr06.md`。全部落改为 exact-match。
> 「可选改」的取舍：采纳有实质收益者（结构类型、语义、指代、批注矛盾），纯文风/分段建议不采纳（记录如下）。

### 3.1 采纳的「必须改」

| # | 文件 | 来源 | 处理 |
|---|---|---|---|
| 11 | tr01a.tex ×2、tr01b.tex ×1 | review-tr01 M1 | 底本三组 `<ol type="i">` 列表由 `itemize` 改 `enumerate[label=\roman*.]`（i./ii./iii.），与底本类型一致 |
| 12 | tr01a.tex | review-tr01 M2 | B022 `resconstruction` 补批注（原先漏登记） |
| 13 | tr04b.tex | review-tr04 M1/M2 | B146/B145 两条批注把 `\{w_i\}_{i=1}^w` 的上限误判为 $N$，改为 $n$（$(\C^\ast)^n$ 的基有 $n$ 个；$N$ 是射线/求和项数），并消除与 B147 批注的矛盾 |
| 14 | tr04b.tex | review-tr04 M3 | B152 「associate product」原文笔误补批注（原文照录） |
| 15 | tr04a.tex | review-tr04 M4 | B138 `\mu_i\in\mathbb{Z}_{>0}` 与 B142 分类矛盾的补注；引用处改 Z_{\ge 0}（正文仍照录原文） |
| 16 | tr05b.tex | review-tr05 M1 | B182 「toric base」由误挂 $\mathcal{S}$ 改为「三元组 $(B,\mathcal{A},\mathcal{S})$ 称为环面底」（语义错误） |
| 17 | tr05a.tex | review-tr05 M2 | B167 批注仍写「未自造插图」，与 Lead 后加的图 2 矛盾 → 改述为「图 2 为按 canvas 重画的 TikZ」 |
| 18 | tr05a.tex | review-tr05 M3 | B158/B161/B162 的 `% [源 …]` 标记行首缩进 → 顶格（与其余 31 个标记一致；check.py 本已容忍缩进） |
| 19 | tr03a.tex | review-tr03 M1 | B112 批注的「补正方案」算错（取 λ² 仍得 λ²）→ 改为正确推导：$t_i=\frac12|x_i|^2$ 时要直角边 $\sqrt\lambda$ 须约化层取 $\sqrt\lambda$；正文照录不动 |
| 20 | tr02a.tex | review-tr02 M1 | B065 被 Lead 改成独立公式（第 9 条）后违反「行内公式原样保留」→ 回退为行内，改用局部 `{\sloppy … \par}` 消除 27.7pt Overfull；独立公式数恢复 38/38 |

### 3.2 采纳的「可选改」

| # | 文件 | 处理 |
|---|---|---|
| 21 | tr03a.tex | 图 1 的 figure 由 `example*` 内移到 `example*` 之前（保持底本「图 → Examples. → 正文」顺序，避免浮动体落在定理环境内） |
| 22 | tr01a.tex | 「辛簇」→「辛流形」（全书 15 处均为「辛流形」） |
| 23 | tr02a.tex | B051「其余维数 $\ge 1$」→「余维数 $\ge 1$」 |
| 24 | tr01b.tex | B034「这一层」→「这个分层」 |
| 25 | tr06a.tex | B206 补批注：源文 (2) 的 $\supseteq$ 方向疑误（按 B204 应为 $\subseteq$），照译 + 登记 |
| 26 | tr06a.tex | B212 带引号 "Definition" 的「原文加引号，表示非严格定义」从定理标题移入 Tutor Note（译注不进入排版，符合 R1） |
| 27 | tr06a.tex | B213 批注「上边缘算子」→「边缘算子」（$\partial$ 降次）；B214「考虑对」→「考虑配对」；B207「其对偶基」→「取其生成元的对偶基」；B193 的 `<ol class="bracketed-list">` 改 `enumerate[label=\arabic*)]`（1) 2)） |
| 28 | tr02a.tex | 更正「`\espan` 是笔误」的说法：底本 HTML 的 MathJax `tex.macros` 明确定义 `espan:"{\\operatorname{span}}"`，故是**页面自定义宏**而非笔误（README 登记表同步修正） |

### 3.3 未采纳（记录取舍）

| 来源 | 建议 | 不采纳理由 |
|---|---|---|
| review-tr01 O2/O3/O4/O5/O6/O8/O9 | 按底本 `<br/>` 分段、若干语序调整 | 纯行文风格；不改变信息与正确性，改动会引入新的排版波动，且底本 `<br/>` 本属网页排版手段 |
| review-tr02 O1/O3/O5 | 定理名重复「定理」、术语改写、条件句显式化 | 均为风格项；O1 保留底本重复（不擅改） |
| review-tr03 O2/O3/O4/O6/O7 | 若干措辞与原文语法瑕疵登记 | 不影响理解；语法瑕疵已由其他批注覆盖 |
| review-tr04 O1–O9 | 批注措辞、display 结尾逗号、`\left/\right` 源码计数、U+2014 | Gate 层已 0 问题；批注措辞不致误；不改已确认无误的转写 |
| review-tr05 O1–O9 | 图 2 题注/曲线范围、B155 语序等 | 图 2 题注为解释性扩展（已在 README 声明重画）；曲线域微调无实质收益 |
| review-tr06 O1/O2/O6 | 生成元表述、语序、align 列结构 | 风格项；O6 源文 `array{rcl}` 与 `align*` 数学内容等价 |


## 复跑记录

| 时间 | check.py | build.ps1 | verify_pdf.py |
|---|---|---|---|
| 修 #1–#3 后 | Gate0 214/214（当时缺 tr 块，后补齐） | 0 error / 0 overfull | 图表/文献 OK |
| 修 #4–#10 后 | Gate 0 214/214 全覆盖；Gate 1 无问题；`\tag`=0；Tutor Note 117 条 | **0 file:line error / 0 undefined / 0 missing char / 0 overfull** | 8 章标题全 OK、表 1–3 OK、32 条文献全在、0 未嵌字体、无 `??`/`**`/`Undefined` |
