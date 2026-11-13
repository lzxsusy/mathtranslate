# ENGINEERING.md — 工程文档（便于后续优化迭代）

> 工程代号：`cft_gauge`　｜　版本：v1.0　｜　底本：Kenji Ueno, *Conformal Field Theory with Gauge Symmetry*, Fields Institute Monographs 24, AMS, 2008。
> 本文件面向"下一个接手的人/模型"：读完它应当能**不看对话历史**就接手、复现、修补、扩译。

---

## 1. 交付物

| 交付物 | 路径 | 说明 |
|-----|----------------|----------------|
| 中文译注本 PDF | `deliverable/共形场论与规范对称性-中文译注本.pdf` | 全文 6 章 + 附录 + 参考文献，可编译 |
| LaTeX 源码 | `deliverable/src/` + `main.tex` | xelatex 两遍出 PDF |
| 译注汇总 | `deliverable/译注汇总.md` / `.pdf` | 全部 `% [Tutor Note: …]` 批注汇总（不进正文排版） |
| 脉络梳理 | `deliverable/脉络梳理.md` / `.pdf` | 精读路线图、重点清单、难点/跳步标注（★/★★/★★★） |
| 工程文档 | `deliverable/ENGINEERING.md` | 本文件 |
| 反馈报告 | `deliverable/反馈-模型协作问题与改进建议.md` | 本次多智能体协作遇到的工具/流程问题与建议 |
| ERRATA | `deliverable/ERRATA.md` | 原文笔误与译者更正清单 |
| 术语表 | `deliverable/glossary.tsv` | 英中术语冻结表（约 100 条） |

## 2. 底本与坐标

- 原书 PDF 178 页；**印刷页 = PDF 页 $-$ 9**（印刷 p.1 = PDF p.10）。
- 正文印刷 p.1–168；附录 p.161–162；参考文献 p.163–166；索引 p.167–168（未译）。
- 原书目录结构见 `TIMELINE.md`。
- 原书排版特征：每页约 270 词 + 若干显示公式 + 少量插图（全书 17 幅）；公式按**章**连续编号 `(章.序)`；定义/定理/引理/命题/推论/例/注**共用章内一个计数器**（所以会出现 `Definition 1.1, Example 1.2, Theorem 1.3` 这样的连号）；Figure 也按章编号。

## 3. 目录结构与文件职责

```
cft_gauge/
├── BRIEF.md            项目总览（给人和新 agent 的第一份材料）
├── STYLE_GUIDE.md      硬性写作规范（冲突时优先级最高）
├── BLOCK_TASKS.md      译手任务书（素材、写法、自检、报告格式、块表）
├── TIMELINE.md         分块表：章/节 $\leftrightarrow$ 印刷页 $\leftrightarrow$ PDF 页 $\leftrightarrow$ 负责块/译手；小节标准译名表
├── glossary.tsv        术语冻结表（en / zh / note），全队唯一术语来源
├── ENGINEERING.md      本文件
├── ROADMAP_SPEC.md     《脉络梳理》写作规格（结构、篇幅、素材来源）
├── make_stubs.py       生成空的 src/bNN.tex 与 refs.tex（新工程初始化用）
├── crop.py             从底本 PDF 裁剪放大任一矩形区域（看公式用，400dpi）
├── check_block.py      单块静态自检（编码/括号/环境/禁用命令/Unicode/批注数/页标记/\tag）
├── aggregate.py        汇总：译注汇总.md、\tag 章内连续性报告、ERRATA.md
├── pages/pNNN.png      原文 200dpi 页面渲染（公式唯一真值），NNN = PDF 页码
├── split/pNNN.txt      文字层 OCR（仅用于定位段落，不可用于抄公式）
├── full.txt            全书文字层（同上）
├── main.tex            主文件（封面/译者说明/目录/章节骨架/\input 各块）
├── src/preamble.tex    导言区：版式、字体、宏表、定理环境（Lead 独占）
├── src/b00_preface.tex 前言译文
├── src/b00_notation.tex 记号表译文
├── src/b01..b17.tex    17 个正文块（每块一个译手，互不重叠）
├── src/refs.tex        参考文献（`thebibliography`，由 main.tex \input）
├── block-reports/bNN.md 每块交件报告（DONE/BOUNDARY/TERM/ISSUES/ERRATA/DIFFICULT）
├── 译注汇总.md / ERRATA.md 由 aggregate.py 生成，勿手改
├── tmp/                编译临时文件、裁剪图、测试稿（可清空）
└── deliverable/        最终交付（PDF + src + 四份说明文档）
```

## 4. 工作流（七阶段）

1. **底本勘察**：PyMuPDF 取页数、内嵌 TOC、逐页渲染 200dpi、导出文字层；确定页码偏移与 OCR 质量。→ 结论：文字层是劣质 OCR，**公式只能看图抄**。
2. **规范冻结**：写 `STYLE_GUIDE.md`（写作硬规范）、`glossary.tsv`（术语）、`src/preamble.tex`（版式与宏）、`main.tex`（骨架），并用 stub 编译一次，确认工具链可用（这一步在本工程中曾暴露 `\AA` 与 `\subsection` 两处规范冲突，见 §7）。
3. **分块**：以**小节边界**切块，块大小 6–17 印刷页；每块一个文件、一个译手，写域完全不相交。块表与页边界写死进 `TIMELINE.md` / `BLOCK_TASKS.md`。
4. **并行翻译**：译手按"读页图 → 逐段译 → 每 2–3 页落盘 → 写译注 → 自检 → 写报告 → 报告 Lead"的循环推进；块内小节标题由块自己写（自动编号即与原文一致）。
5. **汇总与编译**：Lead 用 `aggregate.py` 查 `\tag` 章内连续性、汇总批注与 ERRATA；xelatex 两遍编译；按编译告警清单逐条处理（未定义宏、缺字形、Overfull > 20pt、环境未闭合）。
6. **复核**：逐块抽查（数字/编号/公式符号与原文对照）、跨块边界句、术语一致性、目录页码。
7. **交付**：`deliverable/` 目录 + 说明文档 + 反馈报告。

## 5. 角色与分工（团队上限 8 名成员，含 Lead）

| 角色 | 职责 | 写域 |
|--------|------------------|------------------------|
| Lead | 规范、骨架、块划分、编译、复核、文档、对外汇报 | `main.tex`、`src/preamble.tex`、`BRIEF/STYLE/TIMELINE/BLOCK_TASKS/ENGINEERING/ROADMAP_SPEC`、`deliverable/` |
| tr-ch1a…tr-ch5b（8 人） | 每人 1–2 块正文翻译 + 译注 + 报告 | 各自的 `src/bNN.tex`、`block-reports/bNN.md` |
| 收尾轮派 | 先完工的译手接后续块（B14–B17），最后一名接《脉络梳理》 | 对应块 / `脉络梳理.md` |

**并发约束**：团队成员上限 8（含 Lead）→ 最多 7–8 名译手并行；17 块必须**轮派**（先完工者接新块），不能一次性派完。这是本工程最重要的调度事实（见 §7 问题 3）。

## 6. 关键决策记录（ADR）

- **ADR-1 用 LaTeX 译注本，而不是 Markdown 直译。** 理由：底本含 600+ 编号公式与 200+ 定理类环境，只有 LaTeX 能在"编号与原文逐一对应"的同时保证排版；纯 Markdown 无法稳定复现 `(5.17)` 这类编号与定理环境样式。
- **ADR-2 公式一律看页面图，不看文字层。** 文字层 OCR 把 `∈` 变 `G`、`m` 变 `ra`、公式碎成单字符；用它抄公式必然错。文字层只用于快速定位段落起点。
- **ADR-3 编号手工写，不用自动计数器。** 原书环境共用一个章内计数器且与公式编号交织；自动编号在缺页/跨块时会漂移，手工 `[1.1]` + 静态自检更可靠（`check_block.py` 校重复与递增）。
- **ADR-4 小节标题由块自己写。** 块按小节切分，若标题由 Lead 写在 `main.tex`，则"块文件 $\leftrightarrow$ 标题位置"耦合过紧；让块写 `\subsection`、用字由 `TIMELINE.md` 冻结，既能自动编号又与原文一致。代价：`check_block.py` 的禁用命令表必须放行 `\subsection`（早期版本误禁，导致全队被自己判 PROBLEM，见 §7 问题 1）。
- **ADR-5 图一律不复刻。** 复刻 17 幅示意图（连接、配边、节点消解）成本高、易失真；改为原位留 `\figomit{编号}{图注译文}`，精读时对照原文 PDF。
- **ADR-6 译注写进 `%` 注释，不进排版。** 批注是"给人看的"，混排会破坏"编号与原文一致"的对照性；同时用 `aggregate.py` 抽出独立《译注汇总》，便于阅读。
- **ADR-7 每块交 `block-reports/*.md`，其中 `DIFFICULT:` 字段强制详细。** 它是《脉络梳理》难点标注的**唯一原始素材**，把"读的时候哪里卡住"变成工程数据，而不是靠事后回忆。
- **ADR-8 《脉络梳理》用 Markdown 写、pandoc 转 PDF。** 理由：内容是提纲/清单/表格，Markdown 迭代最快；`pandoc --pdf-engine=xelatex -V CJKmainfont=SimSun` 在本机已验证可出中文 PDF。

## 7. 质量控制体系

**a) `check_block.py`（每块交付前必须 OK）**：UTF-8 无 BOM / 无 CR / 花括号平衡 / `\begin-\end` 环境配对 / `$` 奇偶 / 禁用命令（`\usepackage`、`\newcommand`、`\input`、`\section`、`\label`、`\eqref` 等）/ Unicode 数学符号 / 数学中中文 / `\tag` 格式与片内重复 / Tutor Note 数量（<5 报 PROBLEM）/ `% [原文 p.N]` 页标记存在性。

**b) `aggregate.py`（全局）**：跨块检查每章 `\tag{ch.n}` 连续性（缺号/重号/乱序）、汇编《译注汇总》、汇总 `ERRATA.md`。

**c) 编译检查**：xelatex 两遍；关注 `! LaTeX Error`、`Undefined control sequence`、`Missing character`（曾出现 `★` 无字形）、`Overfull \hbox > 20pt`、`Empty thebibliography`。

**d) 人工复核**：逐块对照页图抽查 3–5 处（重点抽查：定理陈述、公式首项、编号、边界句）。

**e) 术语一致性**：`glossary.tsv` 冻结 + 各块 `TERM:` 回报 → Lead 合并回表；终检用 grep 找同词异译。

## 8. 已知问题与未完成项

**交付版的编译状态（`tmp/final/book.pdf`，xelatex ×2）**：157 页 / **0 error** / **0 Overfull** / **0 Missing character**。历史告警均已处理：19 处 Overfull、42 个 `Missing character ^^C`（`\mathbf{大写希腊}` 在 TU 编码下无字形）、`\cC`/`\Res` 未定义、b14 的 `\end{corollary}` 嵌进 `\[…\]`。

**有意为之、不算缺陷的项**：

| 项 | 现状 | 原因 |
|------|-----------|------------------------|
| 索引（原书 p.167） | 未译 | 原书索引按英文条目排；译文条目对不上，保留原书页码指向，见译者说明第 6 条 |
| 插图 23 张 | 未复刻，仅留图注译文 | 14 张有编号用 `\figomit{}{}`、9 张无编号用 `\figomitn{}`；原图多为示意图，重绘有引入错误风险（见 ADR-5） |
| 原书笔误 147 条 | 正文**照排原文**，批注指出正确形式 | 铁律「不改正文」；条目集中登记在 `ERRATA.md`（含公式抽查 5 条、QA 追加 3 条） |
| 交叉引用 | 纯文本「式 (1.41)」「定理 1.33」 | 为了与原文编号逐字对齐，不用 `\ref`；因此 `xref.py` 是必要工具（3 条原书自身错引照排：p.18「引理 1.22」应为定理、p.86/p.89「推论 4.8」应为定理 4.8） |
| 脚注 | 全书无编号脚注 | 原书用「Remark」而非脚注，译文同样处理 |

**已知的轻微体例偏差（可选修）**：

1. 人名体例统一为「黎曼保留中文、其余一律拉丁（Cartan/Killing/Verlinde/Hitchin/Wenzl/Kanie）」，但 **Kodaira–Spencer 映射在正文里多用「小平–Spencer 映射」（34 处）**，仅少数译注写英文 `Kodaira–Spencer`（8 处）。若要彻底统一，用 `小平–Spencer` → `Kodaira–Spencer` 全局替换即可。
2. 术语首现附英文（「中文（English）」）覆盖不全（22 处抽查中缺 12 处），不影响阅读。
4. md 文档出 PDF 时，表格列宽由 pandoc 按分隔行「短横线个数」等比分配，默认 `|---|` 会让长文本列被压成一字一行；`finalize.py` 前的处理脚本按「各列内容最大显示宽度」重算短横线（下限 8、上限 26），并把 `类型` 列的值从「引用外部」缩成「外部」。另在 wrapper 里加了 `\setcounter{secnumdepth}{0}`，因为 md 标题自带编号（`## 1. …`），否则会渲染成「1.1 1. 一句话定位」这样的双编号。
3. `\begin{sloppypar}` 用于 3 处无断点长段（b05 证明段、b12 证明段、b16 Wenzl 段），排版上首行缩进略异于普通段，属可接受的取舍。

**工具链遗留**：

- `tmp/`（约 200+ 文件：页图、日志、body_*.tex、doc_*.pdf）保留供复核，可整体删除；重跑 `finalize.py` 会重建所需部分。
- `aggregate.py` 的 ERRATA 抽取依赖 `block-reports/*.md` 里 `ERRATA` 段的写法（`ERRATA:` 或 `ERRATA（…）:`，条目按 `-`/`1.`/空行分段）；新增报告请沿用现有格式。
- `crop.py` 的 y 坐标只能目测给出（无 OCR 辅助定位），同页常需 2–4 轮；这是本项目最耗时的单点操作。

## 9. 复用指南（下一本书 / 下一版怎么做）

1. 复制本目录骨架，删 `pages/`、`split/`、`src/b*.tex`、`block-reports/`、旧 PDF。
2. 改 `crop.py` 顶部 `SRC` 为新的底本路径；重跑页面渲染（200dpi）与文字层导出；重新确定**页码偏移**并在 `TIMELINE.md` 首行写死。
3. 重写 `TIMELINE.md` 的章/节/页表与块表（块按小节切，6–17 页/块），重写 `BLOCK_TASKS.md` §9 块表；重写 `glossary.tsv`（新书术语）。
4. 保留 `check_block.py`、`aggregate.py`、`make_stubs.py`、`finalize.py`、`main.tex` 骨架、`preamble.tex`（多数宏可复用）。
5. 按 §5 派工；**记住团队上限 8**，块数 > 8 时必须轮派。
6. 编译顺序：stub 编译验证工具链 → 首批 1–2 块到位后编译验证样式 → 每完成 3–4 块编译一次，早发现系统性错误（比全齐再编译省时得多）。

**续译缺失块**：`src/bNN.tex` 若只有 `% STUB` 头，即该块未完成；按 `BLOCK_TASKS.md` 派给任一空闲译手即可，无需改动其它文件。**改版式/宏**：只改 `src/preamble.tex`，全库生效；改后必须重编译全本并检查 `\tag` 与目录。

**md 文档出 PDF（`finalize.py` 的 `md_pdf()`）**：不要用 `pandoc --pdf-engine=xelatex` 直出——pandoc 3.13 的模板无条件加载 `unicode-math`，与本项目的 `\mathcal`/`\C` 宏冲突（`! Missing { inserted.`），且 `-M unicode-math=false` 无效。正确管线：`pandoc -t latex --wrap=none --syntax-highlighting=none` 出正文 → 把 `\def\LTcaptype{none}` 改成 `{table}` → 套自建 `ctexart` + `\input{src/preamble.tex}` wrapper（主字体 SimSun、等宽 SimSun）→ xelatex ×2。

## 10. 度量（交付版实测）

| 指标 | 数值 |
|-----------|------------------------|
| 翻译印刷页数 | 168（正文 p.1–168，含附录；索引未译） |
| 块数 / 译手数 | 17 / 8（团队上限 8，含 Lead → 轮派三批） |
| `src/*.tex` 总行数 | 11,275（21 个文件） |
| 编号公式条数（`\tag`） | 274（Ch1 70 / Ch2 27 / Ch3 38 / Ch4 29 / Ch5 64 / Ch6 38 / 附录 A.39–A.46 = 8） |
| 定理类环境数 | 165（定义/定理/引理/命题/推论/例/注，章内共用计数器，编号连续） |
| 译注（Tutor Note）条数 | 332 |
| 插图从略（`\figomit`/`\figomitn`） | 23（14 有编号 + 9 无编号） |
| 页标记（`% [原文 p.N]`） | 174 |
| ERRATA 条数 | 147（`ERRATA.md`） |
| 编译告警（交付版） | 0 error / 0 Overfull / 0 Missing character |
| 交付 PDF 页数 / 大小 | 157 页 / 0.9 MB |
| 四份派生文档 | 脉络梳理 26 页、译注汇总 34 页、工程文档 7 页、官方反馈 17 页（均 0 error / 0 Missing） |
| 全程耗时 | 约 2 小时（21:52–23:57），8 名 agent 并行 |

## 11. 经验教训（供下一版 / 下一代工具改进）

1. **静态检查器不等于可编译**：`check_block.py` 能查括号、环境、`\tag`、禁用字符，但查不出 `\cC` 未定义、`\end{corollary}` 嵌进数学环境、Overfull、`\tr` vs `\Tr`。必须每 3–4 块做一次**全本编译**，把编译当 lint 用。
2. **规范自伤是最贵的坑**：`check_block.py` 曾把 `\subsection` 列为 BANNED，而规范要求块自己写小节标题；`\tag` 校验曾用 `float()` 把 `1.10` 判成 `1.1`。工具与规范必须同源评审（本次共修 3 处自伤冲突）。
3. **「照排原文」需要显式的判定口径**：笔误是「照排 + 批注」，还是「直接订正」？本次在 112 条公式抽查里形成口径：**只影响排版/无数学后果 → 照排 + 批注；明确数学错误且有独立证据（裁图/上下文）→ 订正并记 ERRATA**。口径要写进规范，否则不同译手处理不一致（曾出现同类错误两种处理）。
4. **共享临时目录的命名与并发**：`tmp/` 下脚本曾与标准库同名（`struct.py`）导致 `import pymupdf` 崩溃；两名译手同时改同一文件曾造成 40 分钟返工。约定：`tmp/` 只放 `tmp_` 前缀文件、写权限归 Lead。
5. **md 侧字符归一必须成表**：`$\hat{g}$`、`$\check{C}$`、`$\leftrightarrow$`、`$\mapsto$`、`$\Longrightarrow$`、`$\checkmark$` 这类字符在 LaTeX/字体里是缺字源头；出 PDF 前统一替换成数学命令（见 §9）。这类问题在 34 页文档里表现为「几百个 Missing character」，不致命但显眼。
