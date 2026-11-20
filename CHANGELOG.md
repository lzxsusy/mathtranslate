# CHANGELOG

## SY03-22《广义 Argyres–Douglas 理论》中译注本（45 页）+ 新工序「译中验算」 — 2026-11-21

- **新增工程** `08_source_code/SY03-22_广义 Argyres-Douglas 理论/`：Dan Xie《General Argyres–Douglas Theory》（arXiv:1204.2270v2 [hep-th]，2016-07-12，Prepared for submission to JHEP）全文译注，8 节 + 致谢 + 67 条参考文献，**45 页**；**20 幅插图**按原 PDF 的 1:1 pt 坐标重绘为 TikZ 黑白线稿（每个文件只含一个 `tikzpicture`，标注保留原文 ASCII），4 张表、151 条编号公式；xelatex 两遍 **0 error / 0 Missing character / 0 Overfull hbox**；`translate_kit.py gate` 与 `check` 全过（黑名单 0、译注来源 0 缺失、引用闭合、无残留标记）。
- **术语**：45 条候选由两名术语译手独立出提案，逐条裁定后冻结 **132 条**（`工程文件/work/glossary.tsv`）。abelianization / spray / class S / magical / lamination space 一律**保留英文**；非正则奇点（irregular singularity）、完备理论（complete theory）、箭图支链（quiver leg/tail）、驯顺/野分歧（tame/wild ramification，§8 刻意换用的几何 Langlands 词汇，不可回译为「正则/非正则奇点」）等定名与理由记入 `工程文件/STYLE_GUIDE.md`。
- **疑点**：**32 条**全部有结论（未解 0），15 处标【原文如此】并给出正确形式或判定依据；原则是正文照录、不动数字，改正版只进译注。
- **新工序** `04_playbook/16_译中验算与原文缺陷发现.md`（v1.0）：把「译注＝对原文的一次独立复算」固化成工序——五条复算手法（反算幂次或分母、双路记账、边界代入、维数检查、图数格点）、判定三分（排印瑕疵 → 径行订正不出注／笔误 → 照录 +【原文如此】+ 译注且须算出正确形式／论证缺口 → 必须指出哪一步不成立，标【译者按（无外部依据）】，不许替作者改论证）、四条红线。本次首次实战即撞出 **§6.1 式 (6.6) 的论证缺口**：由 $j_1/k_1\le j_2/(k_2-1)$ 推不出与 $j_1/k_1>j_2/k_2$ 的矛盾（$k_2>1$ 时二者可并存），结论本身仍由后文（只剩两 block 且 $k_2=1$）支撑，故原样保留并注记；另 5 处笔误：(5.23) 的 $\omega$ 项幂次应为 $z^{3n-1}$、(5.24) 的 $[u_{3n+1}]$ 分母应为 $3n+3$、表 4 的 Base dimension 列与 (5.19) 自相矛盾、(6.8)(6.9) 的 $\omega$ 指数应为 $k$ 而非 $n$、§6.3.1 两处把 $Y_3$ 写了两遍。
- **台账**：`RELEASE_REGISTER.csv` 增 SY03-22 行（随仓公开·状态合规），`03_translations_meta/SY03-22/投稿信息.md` 同步。

## SY01-26 Cox–Katz 收尾：官方勘误 99 条逐条比对 + 命题 5.5.4 依作者更正重写 — 2026-11-20

- **勘误比对（主任务）**：AMS 2020-01-29 版 `typos.pdf` 98 条逐条定位译本（`\SourcePage{N}`，PDF 页 = 印刷页 + 23）并判定，另补入原表漏收的 page 54 line 12（编号 9a），共 **99 条**：已修 43、已吸收 49、不适用 7、**无未判定**。改动落在 `chapters/chapter03/04/05/06/07/08/09/10/11/12.tex`、`preface.tex`、`appendixA.tex`、`references.tex`；每条依据（`chapters/chapterXX.tex:行号`）写入 `工程文件/校对/官方勘误2020/官方勘误2020对照表.md` 的「备注」列。
- **命题 5.5.4 重写**：作者 2001-10-14 的 *Correction to Proposition 5.5.4*（`554.pdf`）指出原书 p98 命题 as stated 有误；AMS 勘误表的处理是把 p98–p101 整段从列表里抽掉，本译本改为**照更正版重写正文**：(5.43) 符号写法加一句等价性说明、命题改为 $Q\widetilde I$ 满足 $\mathcal A$ 方程组且 $\widehat\beta=(0,\ldots,0,-1,\ldots,-1)$、(5.47) 化单项式、$\Box'_\beta=A-q^\beta B$ 与 (5.51)(5.52) 重写、引入 $C,S,T,U$ 四记号完成逐项相消、删去 p100 末三行括注、p101 补 $q_1=-z$ 的变量替换。`译注.md` 末节「据作者 2020 更正重写 · 命题 5.5.4」记全过程。
- **(5.43) 复核（E5）**：正文仍作 $(-1)^{\sum_ic_1\cdot\beta_j}\prod\lambda_\rho^{D_\rho\cdot\beta_j}/\prod\lambda_{r+i}^{c_1\cdot\beta_j}$，与勘误的 $(-\lambda_{r+i})$ 写法等价；重写未改动该因子，`原文笔误表` E5 补注说明。
- **编译**：`latexmk -xelatex` 三遍 + biber，**412 页**（原 410，+2），0 未定义引用、0 未定义 citation、2 处 Overfull；成品同步覆盖到 `成品/`。遗留：`chapters/appendixC.tex` 若干行正文模式内含字面 Unicode 数学符号（ℏ、∏、∫ 等），xelatex 报 90+ 条 "Missing character"（前任遗留，未在本轮处理）。
- **一致性**：`audit_terms.py` 与 `pdftotext | grep` 的「单值化/虚基本类/通用族/线性束」计数均为 0；`RELEASE_REGISTER.csv`、`03_translations_meta/SY01-26/`、项目 `README.md`、`CHANGELOG.md`、`交付报告` 五处页数与条目数已同步。

## 产出作用审计 + 思考链纪律与工具 + 形式化路线 — 2026-11-20

- 新增 `ASSESSMENT_2026-11-20_产出作用.md`：按“有没有用”审计 33 天产出（95 部/11,404 页、200,366 次调用、¥2,437.38；结论：页数已过拐点，稀缺的是 240 条核验断言、153 个校对 JSON、402 条轨迹）。
- 新增 `ASSESSMENT_2026-11-20_AI消耗.md`：成本侧报告（输出 token 45.6%、缓存命中 98.61%、¥0.21/页）。
- 新增 `09_thinking/`：L0 raw → L1 候选卡 → L2 人工批准链 → L3 审计；硬纪律 R1–R12；一条链七段（任务/关键片段/决策与替代方案/自纠与回退/验证证据/逆转条件/交付物）；`_TEMPLATE.md` + `index.csv`。
- 新增 `tools/thinking_audit.py`：`scan / rank / extract / approve / check / coverage / report`；272 个子会话试跑得到 12 张候选卡（3,952 万字符 reasoning 压到 9KB/张）。
- 新增 `04_playbook/15_形式化与自然语言对齐_2026-11.md`：Lean 陈述层做验证器，T1–T4 课程，2026-Q1 1,000 条 NL↔Lean 对齐。
- 更新 `README.md`、`00_README.md`、`04_playbook/README.md`、`04_playbook/11_资源受限路线_v1.md`：统计口径统一到 105 部/92 部源码/10,043 文件/442.9MB/49,035 段/95 部 11,404 页；补入 `09_thinking`、审计报告与形式化路线入口；修正主题分布表（含 SY08-01）。

## SY05-26 Gaiotto–Witten《通过膜探测量子化》中译注本（69 页）— 2026-11-20

- 新增 `08_source_code/SY05-26_通过膜探测量子化/`：D. Gaiotto、E. Witten, *Probing Quantization Via Branes*（arXiv:2107.12251v2，2021-08-11，101 页；原文日期 2020-05）全文中译注本，`ctex` + XeLaTeX，成品 **69 页**（书名页、译序、目录、§1–§5、附录 A–D、致谢、文献），正文约 **5.57 万字**。
- 底本策略：不用 PDF 重排，改用作者 arXiv LaTeX 源码（`Draft_D.tex`，4335 行）。公式、编号、图位置、参考文献（**55 条**）全部原样沿用，译文只改文字与章节标题；源码中注释掉的旧节（Gauged quantization、More On Cotangent Bundles 等）不在 PDF 成文中，未译。PDF 仅用于核对与页面图。
- 工序：源码 4335 行通读 → `work/通读笔记.md`（行号→印刷页结构表、逐节论证骨架）与 `疑点清单.tsv`（Q01–Q22，**未解 0**）→ 术语冻结约 100 条（`work/glossary.tsv`）→ 按小节切 31 个 tex 分块翻译 → 两遍 xelatex。
- 质量：`main.log` 0 error / 0 undefined / 0 overfull（4 处 underfull，badness 1043–2134）；逐页目检书名页、§3.1、附录 C/D 与目录；图 10 幅全部加载（`6.pdf` 经 `pdftocairo` 重新蒸馏，`Correspondence.pdf` 统一改小写）。
- 批注：译注 **4 条**（Groenewold–Van Hove 障碍、亚辛校正与 $\mathrm{Spin}^c$、线丛的复幂、与几何 Langlands 的关系；来源分别 A/I/I/A）、校勘 **2 条**（§3.7 联络共轭方向、附录 A $[\hat z^3,\hat{\bar z}^3]$ 的 $\bar z^2$ 笔误）、概念卡片 **1 张**；另汇总 12 条原文笔误（Stiefel–Whitney、ultraviolet、Eguchi–Hanson、$v_s\to c_s$ 等）。
- 交付：`BRIEF.md`、`STYLE_GUIDE.md`、`build.ps1`（编译 + 质量门，PowerShell 5.1 下已验证）、`work/{通读笔记,疑点清单,glossary}`、`deliverable/{术语对照表,译注汇总,工程总结,阅读参考指南,统计数据}`、`投稿信息.md`（工程内与 `03_translations_meta/SY05-26/` 各一份）。
- 合规：底本为 arXiv 预印本，按 `RELEASE_REGISTER.csv` 登记（源码 L2 公开·受限，成品 Release 外链，原文 L4 禁入，`auto`，合规）；底本 PDF、页面图（`work/pages/`，30 MB）、作者源码（`work/原文/`）与成品 `源码/main.pdf` 均不入库，项目内 `.gitignore` 兜底。**未做资料卡**（按用户要求，待正文稳定后补）。
- 已知遗留：译注偏少、无 B 级来源交叉、§2.8 一处 $\alpha$ 方向按约定改而未加校勘框；详见 `deliverable/工程总结.md` 第六节。

## SY01-17 Bocklandt《同调镜像对称性浅入门》中译二轮校订 + sy0117 32 张资料卡 — 2026-11-20

- 二轮独立校订：12 章各由一名审稿人通读，主校逐条复核；共 **89 处**修订（ch01 8、ch02 6、ch03 4、ch04 9、ch05 11、ch06 8、ch07 9、ch08 14、ch09 7、ch10 3、ch11 6、ch12 4），只改确定的误译/漏译、数学错误、记号错误与体例错误，纯风格问题不改。用二轮结果覆盖 `reports/ch01.md`–`ch12.md`、`审校报告.md`、`审校批注索引.md`、`reports/notes_index.md`、`appendix_notes.tex`；首轮原件仅本地备份于 `reports/_v1_archive/`，不随仓。
- 代表修正：ch01 `Top_*` 态射补“连续”；ch02 面映射补回 $x_0$；ch05 辛形式补 $i$ 与 $dz\wedge d\bar z$；ch07 统一“反 Fano/一般型”术语并修例 7.90 矩阵阶数；ch08 三维 LG 模型统一为 $UV=W_t$；ch10 三穿孔球面改 $\mathbb C\setminus\{0,1\}$；ch11 删除定理中未使用的 $A$；ch12 $\Lambda_Z\to E_Z^{\pm}$。
- 90 条校订批注保留，仅 ch10 批注 $2-k\to k-2$；本轮未新增或删除批注。本机无英文原书与页面图像，二轮以中译内部数学一致性、记号、术语、交叉引用与体例自洽为主，**未逐页对照英文原文**，报告如实说明。
- 新增 `datasets/sy0117/`：**20 张概念卡 + 12 张勘误卡 = 32 卡**；每张概念卡至少 1 条批注（易错预警/含糊点拨/背景直觉），勘误卡记 `location/original/corrected/why/note`；anchor 全部指向 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/chNN.tex:A-B`；`tools/make_cards.py --check` 输出 `OK 32 cards (20 concepts, 12 corrections)`；全部 `reviewed` + `source-only`。
- 更新 `08_source_code/SY01-17_同调镜像对称性浅入门/` 的源码与工程文件；`README.md` 升 v3.0（89 处修订、90 条批注、32 张卡）。重编译 **365 页**，`undefined_refs=0 duplicate_dest=0 overfull=0 missing_glyph=0`。
- 合规：底本为在版图书，按 `RELEASE_REGISTER.csv` 的 SY01-17 条目（成品不公开、L4 禁入）执行；仓库只收源码、工程文件与资料卡，不收 PDF、不收原书扫描件。

## SY01-26 Cox–Katz《镜像对称与代数几何》中译校订本 + 逐页对照全校订 + 24 张资料卡 — 2026-11-20

- 新增 `08_source_code/SY01-26_镜像对称与代数几何（Cox–Katz）/`：David A. Cox、Sheldon Katz *Mirror Symmetry and Algebraic Geometry*（AMS Mathematical Surveys and Monographs **66**, 1999；ISBN 978-0-8218-1059-0，xx + 469 页）全书中译本的校订版。底本扫描件 495 页、纯图像无文本层；译本原 403 页，校订后 **410 页**（新增附录 C 译注汇编 7 页），XeLaTeX 三遍 + biber，0 Overfull。
- 原文数字化：第一轮 RapidOCR 200 dpi 有整行丢失（如 p14 丢一整行），弃用；第二轮 300 dpi、`det_limit_side_len=1600`、8 进程 OCR 全部 483 页（PDF p13–495），正文完整，公式仍不可辨处逐条记 `skipped`（632 条），不臆断。
- 切块与对照：按 `\SourcePage{N}`（N = PDF 物理页 = 印刷页 + 23）每 3 页一单元，共 **153 个单元**；子智能体每批 8 个并行逐句对照中英，产出 **209 条**问题（术语 89、错译 34、增译 28、记号 24、病句 14、漏译 13、数学 3、指代 1），机械替换 **136 条**（0 条失配），其余并入术语归一。
- 术语裁决（与库内 27 个 SY01 工程对照）：monodromy 全书旧译「单值化」**149 处**改「单值性」（单值化专指 uniformization）；「虚基本类」**140 处**改「虚拟基本类」（库内主流 75:5）；通用族→万有族 2 处、线性束→线性系 1 处。保留并说明理由：消失圈、代数叠、多胞形、自反多胞形（本书内部一致，改动 138 处收益不抵风险）。裁决表见 `工程文件/校对/术语对照与冲突.md`。
- 高风险复核：对记号/同调/公式类问题用第二份高分辨率印刷扫描逐页渲染核对——u47 的 `Δ∩M`（原书写 Δ∩M，译本误作 Δ°∩N）、u81 的 homology class（译本误作上同调）、u94 漏掉的 `1/(2πi)^d` 三项抽查全部属实；并顺带核出原书 3 处笔误。
- 译注：**92 条**编为「附录 C 译注汇编」，按原书 PDF 页排序，内容为 OCR 不可辨处的处理、术语与记号歧义、作者跳步说明；正文不加脚注，避免破坏与原书页码的对位。另有 `工程文件/校对/译注.md`（全文，含被筛除项）与 `原文笔误表.md`（5 条勘误 + 3 条存疑，含 AMS 官方勘误 p16 `d=0`、p99 (5.47)→(5.48) 与 (5.51) 补 `(-1)^{s_β}`）。
- 术语表：`成品/SY01-26_术语表.md` **133 条**（中文/英文/首现页/章/说明），首现页用 PDF 物理页。
- 资料卡：`资料卡/` **24 张**（MS-01…MS-24；L0 5 / L1 12 / L2 7），按 playbook 13 号十一节硬模板；每张要求最小例子能算出具体数字（如五次三维簇 `h^{2,1}=101` 的 Jacobian 环计数、`n_2=609250` 的级数系数核对），并与 SY01-24 术语表、SY01-25 资料卡逐条对照，冲突登记 `资料卡/_冲突表.md`；状态一律 `draft`（冷启动盲测未做）。
- 工作流：`工程文件/工作流/` 收录 12 步流水线的 README、14 个脚本（OCR、切块、套用、术语归一、报告、页渲染、术语审计）与两份 workflow 脚本（校对 153 单元、资料卡 24 张），可复现。
- 合规：底本为在版图书，按 `COMPLIANCE.md` §4 **R3 成品不公开**——校订版 PDF 只在本地 `成品/`，不入 git、不发布、不给直链；原书扫描件与 OCR 全文 L4 禁入。台账 `RELEASE_REGISTER.csv` 已追加 SY01-26；`03_translations_meta/SY01-26/投稿信息.md` 与工程内同名文件一致。

## SY08-03 Thomas《给数学家的导出范畴》中译注本（28 页）+ 校勘 10 条 + 精读指南 — 2026-11-20

- 新增 `08_source_code/SY08-03_给数学家的导出范畴/`：R. P. Thomas, *Derived categories for the working mathematician*（arXiv:math/0001045，v1 2000-01-07 / v2 2001-10-17，13 页；会议版 Winter School on Mirror Symmetry, Harvard 1999，AMS/IP Stud. Adv. Math. 23 (2001) 349–361，Zbl 1008.18011）全文中译，`ctex` + XeLaTeX，成品 **28 页**（书名页、译序、目录、正文 6 节、附录 A–D、文献）。
- 选篇理由：这是“导出范畴”最常被引用的一篇讲稿，作者是 Donaldson 的学生；全文 13 页却把链复形、拟同构、局部化、锥与三角、导出函子五件事串成一条线，适合作为进入导出范畴的第一篇精读材料，也与既有 SY08-02（Orlov《凝聚层的导出范畴》）互补。
- 工序：原文两遍通读 → `工程文件/work/通读笔记.md`（六节论证地图）与 `疑点清单.tsv`（D01–D15，`未解`=0）→ 术语冻结 76 条（`work/glossary.tsv`，与 SY08-02 译法对齐）→ 分块落盘 `sections/01_intro … 06_derived` → 三遍 xelatex。
- 质量：0 error / 0 undefined / 0 overfull / 0 缺字；逐页 110 dpi 目检书名页、译序、§4、§5 两图、附录 A/B/D。自查脚本 `work/check.py`：黑名单来源 0 处、译注与概念卡片来源标记 100%、标签全部有定义、禁用句式 0 处、术语均有表。
- 译注 20 条（橙框，每条末句带 `[来源：…]`）、概念卡片 3 张、本节重点 6 段、“校勘”红框 7 个；附录 B 逐条校勘记 **K1–K8 + S1–S2**：K1 引言节号错位（实为 §2–§6）；K2 “末三个箭头”应为“末三项”；K3 §3 的“同调相同却不同构”例子不成立（给正确反例 $A=\C[\epsilon]/\epsilon^2$）；K4 全纯 de Rham 复形被误称 Dolbeault、Hodge 指标互换；K5 “内射层 $\subset$ 拟凝聚层”应为拟凝聚层中的内射对象；K6 Leray 与 local-to-global 谱序列记号残缺；K7 对偶公式 $\R\mathcal Hom(A,B)\cong B\Ltimes A^\vee$ 缺“$A$ 完美”条件（反例：光滑曲线上 $A=B=k_x$，左边 $k\oplus k[1]$，右边 $k[1]\oplus k[2]$）；K8 “rather then”拼写。S1 $\R\Gamma=\R H^\bullet$ 记号、S2 同调/上同调指标混用，标“存疑”保留原文。
- 精读：附录 D 给论证地图、逐节导读、五个关键论证拆解（Whitehead 用锥证明、锥的两种上同调、分数演算、阿贝尔范畴为何无核余核、de Rham 即导出函子）、后续三条线（dg 范畴、稳定 $\infty$-范畴、导出代数几何）与五道带提示的习题。
- 图：原文两张 EPS（fig2dev）转 PNG 目检后，用 TikZ 重绘（X—f→Y→C_f 的锥、以及 Dold–Puppe 序列的悬挂双锥），不携带原始 EPS。
- 合规：底本为 arXiv 预印本，按 COMPLIANCE R3 登记 `RELEASE_REGISTER.csv`（源码 L2 公开·受限，成品 Release 外链，原文 L4 禁入，`auto` 判定，合规）；`03_translations_meta/SY08-03/投稿信息.md` 与 `_PDF清单.tsv` 已登记；成品 PDF 不随仓（`源码/` 内已清编译产物）。`tools/check_compliance.py` 通过（仅 3 条既有/预期 WARN）。

## leanstmt C 批：GNO 1977 陈述对照语料 13 卡 + 扫描件 OCR 管线 — 2026-11-19

- 底本：R. Goddard, J. Nuyts, B. S. Olive, *Gauge Theories and Magnetic Charge*, Nucl. Phys. **B125** (1977) 1–28（DOI 10.1016/0550-3213(77)90221-8；报告号 CERN-TH-2255）。原文无公开 arXiv 号；从 CERN CDS record 422230 取影印 PDF（38 页、600 dpi 1-bit 扫描、无文字层），自解 Anubis v1.27 challenge 后下载。
- OCR：`mutool draw -r 300` 渲 38 页 → PIL 合 300 dpi PDF（15.9 MB）→ `convert_file(ocr:true)`（tesseract.js/eng）；另用 node+tesseract.js 逐页 OCR 带 `[[PDF p.N]]` 标记。页脚数字不可靠，语料一律按节号+式号定位。
- 新增 `datasets/leanstmt/cards/statements/gno1977-*.json` **13 张**（`s01`–`s06` certified、`g01`–`g07` gap），三批合计 **39 卡 = 21 certified + 18 gap**；轨道 `GNO77`；SCHEMA v0.3。
- certified 6 条均为群论/单变量骨架：权的整性 `exp(2πiz)=1 ↔ z∈ℤ`；狄拉克量子化式 (1.3) 的 U(1) 特例 `exp(4πiz)=1 ↔ 2z∈ℤ`；中心元 `ζ^N=1`；有限对偶同阶 `|Hom(H,U(1))|=|H|`；式 (1.6) 有限群双对偶 `(ℤ_N)^∨∨≅ℤ_N`；Weyl 反射 `p↦−p` 保持量子化条件。
- gap 7 条：根格/权格构造 H^∨（`dual_group_construction`）、磁权=H^∨ 的权（`magnetic_weights_are_weights`，GNO 主定理）、磁荷共轭到 Cartan 组合（式 (1.5)）、拓扑量子数 π₂(G/H)≅π₁(H)、单极解渐近行为（式 (1.1)(1.2)）、非半单 H 推广（§6）、附录 D 磁权表。
- Lean：`formal/ShuyiFormal/GNO1977/{Statements,Gaps}.lean`；`check_lean.py --run` 六个文件全部 exit 0（GNO1977/Statements 0 sorry、Gaps 7），`verification.jsonl` 39 行；`lint_cards.py --strict` 0 error 0 warning；`build_index` 39 行、`render_md` 39 篇。
- 工程：`make_cards.py` 扩为三批生成器（`tools/gno77_data.py` 数据表）；`lint_cards.py` 的 `source.arxiv` 规则放宽为「arXiv 形式或 `Nucl. Phys.` 起头」；`workflow/PRODUCTION.md` 增 §七（含 CDS/Anubis、OCR 管线、页映射、编译备注）；`ROADMAP.md` 记 C 批已落地并修 DOI；`datasets/README.md` 记 v0.20。

## SY02-13 Gaitsgory《几何朗兰兹的非正式导论》中译注本（15 页）+ dataset gaits04（23 卡） — 2026-11-19

- 新增 `08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/`：D. Gaitsgory, *Informal Introduction to Geometric Langlands*（Bernstein–Gelbart 编 *An Introduction to the Langlands Program* 第 12 章，Birkhäuser 2004，原书 pp. 269–281 = PDF 271–283，13 页）全章中译，`ctexbook` + XeLaTeX，成品 **15 页**（题页、译者说明、目录、正文 9 页、文献）。
- 选篇理由：全书 12 章中唯此章从「函数域自守形式 → 向量丛 → 层」走完几何化，且作者自称是「进入几何朗兰兹的一张地图」。
- 工序按 v2.1：原文两遍通读 → `工程文件/通读笔记.md`（三句话主旨、逐节论证地图、体裁清单）与 `工程文件/疑点清单.tsv`（17 条，8 列，`未解`=0）→ 术语冻结（`工程文件/术语表.tsv` 109 条）与 `符号表.tsv` 44 条 → 150 dpi 页图逐符号核公式（`工程文件/公式核对记录.md`；pdftotext 提取件公式全乱码，一律不采信）→ 分节落盘 → 三遍 xelatex。
- 质量：0 error / 0 undefined / 0 overfull / 0 缺字，7 处 Underfull（中文-数学混排）；逐页 110–130 dpi 目检，TOC 6 项、节号 1–4 与原书一致。
- 两条术语决定：① Hecke eigen-sheaf 作「Hecke 本征层」而非「Hecke 特征层」，因 §4.3 的 character sheaf 必须作「特征层」（SY02-11 旧译已在译者说明里交代改译理由）；② 原书「小节号与命题共用一套编号」照原书保留，`\ob` 与 `othm` 共用计数器。
- 排版取舍：不作页边码（右边界 2.6 cm 易 overfull），改在译者说明里给 13 行「原书页 ↔ 内容」对照表；8 条译注的来源统一 `\raggedleft` 独占一行，避免满行时被挤到行首。
- 同批新增 `datasets/gaits04/`：**23 张概念卡**，六轨 O（总览 1）/A（阿代尔与球表示 7）/B（尖点与 Langlands 对应 4）/C（向量丛与 Hecke 4）/D（层化与猜想 5）/E（附录 2）。每卡**至少一条批注**（共 23 条，类型限易错预警 / 含糊点拨 / 背景直觉），8 条译注按主题落入 `satake`、`unramified-lisse`、`bun-bijection`、`hecke-correspondence`、`bun-stack`、`eigensheaf`、`sheaf-function`、`character-sheaf` 八卡。每卡带原书页与 `ch12_sec*.tex:A-B` 行号锚；`python tools/make_cards.py --check` → 23 卡、0 错误、0 警告；全部 `reviewed` + `source-only`，按规则不标 `published`。
- 合规：底本为**在版图书**，按 COMPLIANCE R3 与 SY02-08 先例登记为「成品不公开」——译本 PDF 不随仓（`成品/说明.md` 给出本地编译方式）；原书文本层抽取、`work/pages/` 页面图均未入仓。`RELEASE_REGISTER.csv` 新增 SY02-13 行（图书、风险高、源码 L2 公开·受限、成品不公开、原文 L4 禁入、人工判定、合规）。
- 遗留：`site/catalog.json` 与 `site/p/` 仍停在 SY01 批次（SY02-11/12/13 均未登记），站点未重生成；gaits04 尚未做外部核验（`source-only`）。

## leanstmt B 批：Witten 2008 陈述层形式化（14 卡） — 2026-11-19

- 新增 `datasets/leanstmt/cards/statements/witten2008-{s01..s05,g01..g09}.json`：据 Witten, *Mirror Symmetry, Hitchin's Equations, and Langlands Duality*（arXiv:0802.0999v1，15 页；**印刷页 = PDF 页**）裁出 **14 张陈述卡**（5 `certified` + 9 `gap`），轨道 `W08`；与 A 批合计 26 卡（15 certified + 11 gap）。
- certified 5 条（都真编译、0 sorry）：① SL(N,ℂ) 的中心 = μ_N（`center_sl`，原文 §2：SU(N) 的对偶 PSU(N) 的离散核）；② 有限字符群基数 `|Hom(ℤ_N,U(1))| = N`（`card_dual_zmod`）；③ 典范同构 `ℤ_N ≃+ Hom(ℤ_N,U(1))`（`dual_zmod_equiv`）；④ 非正则奇点系数在 z = λw 下的伸缩律 `λ·(c/λ^{m+1}) = c/λ^m`（`coefficient_scaling`，§5 式 (5.1) 的重标度）；⑤ `Maps(Σ, Maps(C,G)) ≃ Maps(Σ×C, G)`（`gauge_maps_curry`，§6.1）。
- gap 9 条（各带中文 docstring 说明缺什么）：Y(G,C) 复辛与维数、A/B 模型、Hitchin 方程 (2.1)、解 ↔ 平坦联络 ↔ 希格斯丛、Hitchin 纤维化、**主定理镜像对称**、tame ramification 单值、wild/辫群、四维提升与 `Bun_G` 无整体商。
- 环境与复核：`leanprover/lean4:v4.36.0`、mathlib `d33c49ca43873d3746194325da62640cc893c9d9`；`lake env lean` 四个文件全部 exit 0（Statements 0 sorry、Gaps 2 / 9），`verification.jsonl` 26 行机器可复算；`lint_cards.py --strict` → `cards=26 ids=26 errors=0 warnings=0`；`build_index.py` 26 行、`render_md.py` 26 篇。
- 工程改动：轨道拆为 `W15`/`W08`，`SCHEMA.md` 升 v0.2（`source.pages` 两批约定：2015 印刷页 = PDF 页 − 1、2008 印刷页 = PDF 页；`leanstmt/witten2008-<key>` id 前缀），`README.md`/`MAP.md`/`ROADMAP.md`/`workflow/PRODUCTION.md` §六 同步；`tools/make_cards.py` 重写为两批生成、2008 批数据内联，A 批数据抽到 `tools/cards15_data.py`；`tools/lint_cards.py` 的 sorry 计数改为先剥注释（避免注释里提到 "sorry" 被判成 certified 卡所在文件含 sorry）。同批更新 `datasets/README.md` v0.19。

## dataset cdm14《晶体与 D-模》资料卡（35 张） — 2026-11-19

- 新增 `datasets/cdm14/`：据 SY02-12 译注本裁出 **35 张**资料卡（27 概念 + 8 推导），八轨 A（de Rham 预栈与晶体定义 4）/B（左/右晶体、$\Upsilon$、Kashiwara 6）/C（下降与归纳函子 6）/D（$t$-结构 8）/E（与 D-模的关系 4）/F（扭化 4）/G（扭晶体 2）/O（总览 1）。每卡一 JSON，字段与 gtgl15 同规范（`SCHEMA.md` 已改写为 cdm14 版：id 前缀 `cdm14`、页 1–65、来源 A/B/C/D）。
- 内容主线：$Y_{\mathrm{dR}}$ 的定义与保极限 → 左右晶体与 $\Upsilon$ 等价 → Kashiwara 引理 → h/fppf 下降与 $\ind^r$ 的单子性 → 两个 $t$-结构（含 $[-n]$ 平移、左完备、Gorenstein、$D(\heartsuit)\simeq\Crys^r$）→ 积分变换与 $D^l_X\simeq\mathrm{Diff}_X$ → 晶体 $\simeq$ D-模 → gerbe/扭化 $\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}\times_H*)[2]$ → 扭晶体。
- 质量门禁：`python tools/lint_cards.py cards --strict` → `cards=35 ids=35 dup=0 errors=0`；`build_index.py` 35 条；`render_md.py` 35 卡。推导卡逐步带 `locator`（印刷页）与 `provenance` A/B/C，非 A 步一律在 `gaps` 登记；每卡 `provenance_note` 点名「最没把握处」。
- 同批更新：`datasets/README.md` 十类表、目录树与版本记录 `v0.18`；`RELEASE_REGISTER.csv` 的 SY02-12 备注补「另附 cdm14 资料卡 35 张」；SY02-12 的 CHANGELOG 条目「遗留」改为「资料卡已裁，见 datasets/cdm14」。

## SY02-12 Gaitsgory–Rozenblyum《晶体与 D-模》中译注本（73 页） — 2026-11-19

- 新增 `08_source_code/SY02-12_晶体与D-模（Gaitsgory–Rozenblyum）/`：Dennis Gaitsgory, Nick Rozenblyum, *Crystals and D-modules*（arXiv:1111.2087v4，2014-10-02，65 页，未正式出版预印本）全书中译，`ctexbook` + XeLaTeX，成品 **73 页 A4**（正文 67 页 + 前置 4 页 + 参考文献 2 页），含译注 10 条、重画交换图 33 幅。
- 底本是导出代数几何里「晶体 = de Rham 预栈上的（归纳）凝聚层」这一路线的纲领性文本：§1 定义 de Rham 预栈 $Y_{\mathrm{dR}}$ 并证 laft 保持性；§2 左/右晶体与 $\Upsilon:\mathrm{Crys}^l\to\mathrm{Crys}^r$ 的等价、Kashiwara 引理；§3 h/fppf 下降与归纳函子；§4 两个 t-结构、$\mathrm{Crys}^r\simeq D(\mathrm{Crys}^r)^\heartsuit$；§5 与 D-模的等价；§6 扭化的 Picard 群胚 $\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}(Y)\times_{H(Y)}*)[2]$；§7 扭晶体。全书编号 277 条（编号段 174 + 定理类 103），中译本逐条沿用原编号，`\ref` 回指原书。
- 工序按 v2.1：先通读并交 `工程文件/work/通读笔记.md`（论证地图 + 20 条卡点）与 `工程文件/work/疑点清单.tsv`（58 条，8 列，`未解`=0）；术语先冻结（`工程文件/work/术语表.tsv`，133 条，列 en/zh/依据/备注）；每章对照 `工程文件/work/pages/` 的 65 页 150 dpi 页面图逐符号核公式，`pdftotext` 文本只作索引；交换图全部 `tikz-cd` 重画，不截图。
- 译注 10 条，全部带来源：9 条 A 级（原书节号、[GR1]、[IndCoh]、[GL:Stacks]、[BB]），1 条「译者按（上下文推断）」解释 §3.4.5 的 $k[\alpha]$（$\deg\alpha=-2$）反例机制；B 级来源 0 条、黑名单来源 0 条。主题覆盖：为何需要导出环、右晶体为何必须用 $\mathrm{IndCoh}$、形式邻域与形式完备化技巧、「那个」t-结构与反常 t-结构、Gorenstein 的「分次线丛」、晶体对 D-模的推广、扭化群胚与 TDO。
- 原文笔误 **13 处**只登记不改（`comaptible` p.9、`aribitrary` p.12、`th n-coconnective` p.14、`duaizing` p.21、`Corollaty` p.31、`indices` p.33、`functior` p.35、`ket(j` p.36、`Expilcitly` p.42、`amplidude` p.62、`forgeftul` p.63、`an an equivalence` p.63、脚注 12 `footnone`），译文按原意处理；另有一处 `transpoistion` 经检索确认原文并无此词，早先记录撤回。
- 成品：`成品/晶体与D-模（Gaitsgory–Rozenblyum）-译注本.pdf`（73 页，随仓入库）；`成品/SY02-12_交付报告.md`（交付物、关键数字、六道工序、译注表、笔误表、校订层次、遗留问题）；`工程文件/build.sh`（干净目录三遍 xelatex + 页数/Overfull/未定义引用检查，当前 **Overfull 0 / 未定义引用 0**）。
- 台账与元数据：`RELEASE_REGISTER.csv` 新增 SY02-12（arXiv 预印本，风险低，源码 L2 公开·受限，**随仓公开 / 成品在仓=是**，原文 L4 禁入，人工判定，合规，2026-11-19）；`03_translations_meta/SY02-12/投稿信息.md` 与工程根同名文件一致；README 主题分布表更新为 84 部 / 10,376 页（SY02 9 部 / 1,078 页）。`tools/check_compliance.py` 通过（2 条既有提示）。
- 合规：底本 PDF、`en_full.txt`/`en_raw.txt` 文本层抽取与 `work/pages/` 页面图均属 L4，未入仓；`.gitignore` 新增 `08_source_code/**/工程文件/work/en_*.txt` 与 `*_raw.txt` 两条排除规则，并为 SY02-12 成品 PDF 增加随仓例外（与 SY03-20 同属未正式发表 arXiv 预印本，台账登记「随仓公开」）。
- 遗留：术语索引与资料卡按约定等主人验收后再裁；本工程未做 index，未附预览 PNG。（2026-11-19 补：主人验收后已裁出 `datasets/cdm14/` 35 张资料卡。）

## SY03-20 Witten《规范理论与几何朗兰兹续谈》校订译注本 + dataset gtgl15（40 卡） — 2026-11-19

- 新增 `08_source_code/SY03-20_规范理论与几何朗兰兹续谈/`：Edward Witten, *More On Gauge Theory And Geometric Langlands*（arXiv:1506.04293v3，2017-07-28，79 页，未正式出版预印本）既有中译（62 页）→ **校订译注版 77 页**（源码 50 项 / 工程文件 / 成品）。正文 62 页 + 参考文献 2 页 + 附录 A 译注汇总 8 页 + 附录 B 术语对照表 3 页 + 中文概念索引 2 页。
- 校订：四位校订译手一人一章（§1–2.6.3 / §2.6.4–3.4.1 / §4–5 / §6–7）逐段对照 79 页原文，正文改动 **12 行**（P1 1 行：essentially 漏限定词；P2 11 行 7 组：术语统一 7 行、记号 2 行、专名 1 行、句义精度 1 行）。最重的是 §3 开头 "which was essentially described" 的限定词 essentially 原译漏（「实际上」→「实质上」）、"one-form" 原译「单形式」2 处；另有宏与记号统一、Stiefel–Whitney 专名、其余 5 处「一形式」统一为「1-形式」。逐条见 `工程文件/reports/ch0N_issues.md`。
- 译注 **57 条**（part1 15 / part2 13 / part3 17 / part4 12），每条带 `[来源：…]`：A 级原始文献为主（Witten 1988/1998/2008、KW 2006、Hitchin 1987×2、GNO 1977、Deligne 1987、Quillen 1985、RSW 1989、Donagi–Gaitsgory、Frenkel–Witten、Hausel–Thaddeus 等），B 级 nLab/Stacks 少量且均 web_fetch 实测 200、记 Last revised 与 2026-11-19 访问日期并与 A 级互证；黑名单来源 0 命中、「译者按（无外部依据）」0 条。附录 A 按节重列，编号「节号-序号」；附录 B 92 条中英对照（中文/英文/首见节），由 `\index{english@中文}` 机械生成。
- 原文疑误 **27 处**只登记不改（保留译文原样），其中特别影响阅读的 3 处加译注说明：$q'$/$q''$ 重复、§2.6.5 偶 $N$ 的 $K^{1/2}$ 依赖、§3.4.1 脚注曲率 $2\pi i\Sigma$ 与式 (3.38) 的 $i\pi$ 归一化差因子 2。
- 工程工具：`工程文件/tools/` 新增 `check_part.py`（UTF-8/LF/括号/$/环境配对/未转义 %）、`gen_appendix.py`（由 part 文件机械生成附录 A/B 与 `译注清单.tsv`）、`wrap_urls.py`（译注内裸 URL 包 `\url{}`）、`build.sh`（xelatex→makeindex→xelatex→xelatex + 日志审计 + 预览 PNG）。最终编译 **0 error / 0 undefined / 0 overfull**（109 条 warning 全为既有 hyperref PDF 字符串与 `\large` in math mode 字体警告，已登记疑点清单）。
- 字体：源码不随包字体；中文字体换装为**可检索方案**——`preamble.tex` 用 `\IfFontExistsTF` 链选 SimSun（宋体，正文）+ SimHei（黑体，粗体与标题）+ KaiTi（楷体），无 SimSun 时退 Noto Serif SC，再退 Fandol 并警告。原因：Fandol 的 OTF 缺 post 字形名，xdvipdfmx 写不出 ToUnicode CMap，旧成品 `pdftotext` 抽出 101 KB 却 0 个汉字、0 个「译注｜」；换装后 `pdffonts` 各字体 `uni=yes`、`pdftotext` 抽出 290 KB 中文（含 57 条译注与中文索引）、0 处 Missing character，页数仍 77、0 error / 0 undefined / 0 overfull；成品约 760 KB，源码 768 KB。`compile.py` 的字体清单校验改为 `fonts/` 存在时才执行，`build.sh` 的 ROOT 改为按脚本位置自动推导（两处均可移植）。
- 新增 `datasets/gtgl15/`：据本文裁切的 **40 张**资料卡（30 概念 + 10 推导），六轨 A（Hitchin 几何与谱曲线 17）/B（对偶环面与 T-对偶 4）/C（膜、线算符与本征膜 10）/D（'t Hooft 算符与赫克修正 3）/E（行列式线丛与本征值 4）/O（总览 2）；每卡带 arXiv 印刷页锚（印刷页 = PDF 页 − 1）、来源定位、pitfalls 与 provenance A/B/C；`lint_cards.py --strict` 0 error、`index.jsonl` 40 条、`render_md.py` 40 卡。维数类断言经复核按原文 eq (2.6) 更正（$\dim_{\mathbb C}M_H=2(g-1)\dim G$、$\dim_{\mathbb R}M_H=4(g-1)\dim G$；$\mathcal M\subset M_H$ 为复 Lagrangian、复维是环境的一半），修订记录见其 `workflow/PRODUCTION.md`。
- 既有资料卡核验并**直接修复**（仓主要求保证正确性）：独立核验员交叉核对 `datasets/kw06/`（67 卡）与 `datasets/glc/`（154 卡，重点 53 张），随后按核验结论把问题**直接修入数据集**，不再只上报。kw06 共改 **10 张卡、22 个文本点**：A 类 4 条 = (1) 把 *simply-laced*（单边）系统性误译为「单连通」——`mirror-symmetry.json`、`table1-and-ng.json`（含 title/步骤/标题）、`sdual-sl2z.json` 共 3 卡 6 处，反证 KW2006 印刷 pp.11–12（$F_4,G_2,\mathrm{Spin}(2k+1),\mathrm{Sp}(k)$ 单连通却 $n_g\ne1$）；(2) `geometric-langlands.json` 把 $M(G,C)$ 误注为「稳定 Higgs 丛」（KW2006 p.5 为全纯 $G$-丛模空间）；C 类 6 条（「一般纤维」×3、$\Xi$ 恒等加归一化说明与出处、$n_g$ 补 $B/C$ 族、术语「花边数」改直陈 `lacing number`、残留 simply-laced 统一）。glc **未见数学错误**，唯一实质问题是同一符号 $d_i$ 在 `hitchin-base`（指数）与 `hitchin-fibration`（次数）含义差 1，属约定差异，已在两卡互注并同步 `verification.jsonl` 的 note（不改 verdict/alignment）；另 kw06 `hitchin-fibration` 也补了 $d_i$ 约定说明。修后 kw06 `lint_cards.py cards --strict` → 67 卡 0 error、glc `lint_glc.py` → 154 卡 0 error 0 warning，两包 `index.jsonl`/`md/` 全部重生成。ch14.tex 第 23 行译注「次数」经核确属口误（英文原书 p.67 作 exponents），该文件属另一工程、不在本仓写作用域，仅记录。逐条反证与修复清单见 `工程文件/校对记录/既有资料卡问题上报.md`（30 KB、150 行）。
- 台账 `RELEASE_REGISTER.csv`：SY03-20 由「成品不公开/成品在仓=否」改为 **随仓公开、成品在仓=是**、复核日期 2026-11-19（底本为未正式出版 arXiv 预印本，依 COMPLIANCE R3 第二款）；`tools/build_release_register.py` 的 SY03-20 人工判定同步更新，并修正「随仓公开」工程的成品在仓状态判定（原先一律标「违规待清」）。
- 同步更新：`03_translations_meta/SY03-20/投稿信息.md`（与工程内同名文件一致，补齐 arXiv 编号与版本、译者署名、版本号、术语索引、分类）；`datasets/README.md` 十类表、目录树与版本记录 `v0.15`。
- 同日补记：成品 PDF 按新字体重出并核验（`pdftotext` 中文/公式/脚注/索引均可抽取，`pdffonts` 全字体 `uni=yes`）；两份 `投稿信息.md` 同步成品体积（约 760 KB）与字体策略；`datasets/README.md` 记 `v0.16`（资料卡修复 + 字体换装）。

## dataset functoriality 补交换图（42 张）+ 术语/记号冻结表入库 — 2026-11-19

- **交换图**：仓主要求「复杂交换图不画出来就没用」。资料卡 schema 新增可选字段 `diagrams`（tikz-cd 自足源码，≤4 张/卡，禁 `%`/`$$`/equation，标题 ≤40 字），并在 `SCHEMA.md` 写死原则「凡是原文用交换图讲清的一步，卡里必须把图也画出来，只写文字的『复合满足结合律』读者无法复核」。本轮给 **14 张推导卡**（26 图）与 **14 张概念卡**（16 图）补图：其中 18 张直取原文/中译本的交换图（式 (20)(54)(76)(80)(93)(95)(107)(111)(112)(113)(133)(135)(136)(140)(144) 等），其余按定义/定理重排为论证骨架并在 `note` 注明「原文未画」，不改箭头方向、标号与同伦标记。
- **工具**：新增 `tools/check_diagrams.py`——每图 `standalone` + tikz-cd 单独编译，失败回报首条 TeX 错误，`--png` 用 mutool 渲染 `md/diagrams/<slug>-<n>.png`，`--only` 过滤；`lint_cards.py` 增 `diagrams` 结构校验；`render_md.py` 增「交换图」节（PNG 链接 + tikz 源码块）。实测 **42/42 图编译通过**，PNG 逐张目检无乱码/断箭头。
- **术语冻结**：新增 `01_corpus_zh/terms_frozen_FUNCTORIALITY.tsv`（**209 条**：A 124 / B 77 / I 8，列同 SY02-09：英文/中文/等级/依据/首次出现/备注，备注含拼音索引键 `key=…` 与 D07 辛同胚裁决等）与 `01_corpus_zh/symbols_frozen_FUNCTORIALITY.tsv`（**76 条**记号：记号 / LaTeX 源码 / 读法 / 含义 / 首次出现 / 依据，按「导言区宏—辛拓扑与基本几何—Floer 与 A∞ 范畴—拼接 Floer 与对应—组合模型与应用」五组）。术语基 `01_corpus_zh/termbase.jsonl` 追加 **190 行**（`pkg=FUNCTORIALITY`、`status=confirmed`、`src_format=tsv`，19 条与既有全局条目重复者已跳过；旧 1630 行逐字节未动）。
- **复核**：术语表与译文的一致性抽查（`grep` 全书）——「干净」4 处、0 处「洁净」；「拼片」11 处、0 处「补片」；「哈密顿」28 处、0 处拉丁 Hamilton；唯一真冲突是 grading 旧注作「分级」而正文 19 处作「分次」，已把冻结表与 termbase 统一为**分次**。B 级依据只用已核 HTTP 200 的 nLab 页面（77 条，页面名与 URL 全记），无编造页码。
- **同步更新**：`datasets/functoriality/README.md`（规模行加 42 图、入口加交换图、质检命令加 `check_diagrams.py`）、`datasets/README.md`（十类表加交换图说明、版本记录 `v0.14`）、根 `README.md` 的 `01_corpus_zh/` 节（两张冻结表与新 pkg 说明）、`index.jsonl` / `md/`（83 卡重渲染，含图）/ `MAP.md`。
- 说明：全部卡仍为 `status: "draft"`、`rights: "rewritten"`；图为自绘/重排，不复制原文整图。

## dataset functoriality —— Abouzaid–Bottman《范畴辛几何中的函子性》资料卡（83 张）— 2026-11-19

- 新增 `datasets/functoriality/`：Abouzaid & Bottman, *Functoriality in categorical symplectic geometry*（arXiv:2210.11159v1，2022-10-20，68 页、43 图）中文译注本的资料卡 **83 张**——概念 56 / 推导 14 / 勘误 13，四轨 A（第 1–2 章 Floer、Fukaya、操作子原理、带曲率 A∞ 与边界上链）/ B（第 3 章 凝聚层与拉格朗日对应、拼接 Floer、Φ#、A∞-双模、伴随、辛约化）/ C（第 4 章 巫曲线与巫球、(A∞,2)-范畴 Symp、相对 2-操作子）/ D（第 5 章 Dehn 扭转、Khovanov、Floer 场论、HMS、形式群、Barr–Beck）。
- 页码锚：以 `pdftotext -layout` 逐页抽英文原文，按作者 LaTeX 的 `\section/\subsection` 顺序建 35 条「节号 → 印刷页区间」映射（PDF 页 = 印刷页），卡内 `sources.pages` 与 anchor 全部照该表；页锚覆盖 p.2–65 共 41 个印刷页。勘误卡 13 张对应译注登记的原文笔误（p.3、p.9、p.24、p.26、p.31、p.39、p.40、p.52、p.56×2、p.61、p.64、p.65），每张给「原文—应作—依据」三层。
- 质量：`lint_cards.py cards --strict` **0 error / 0 warn**（字段、长度、id 与文件名一致、related 可解析、页码 1–68、anchor 以「原书 p.」开头、禁本机绝对路径）；`audit_pages.py` 0 issue（页码落在所属节区间、跨度 ≤3 页、anchor 页码自洽）；`check_formulas.py --corpus book/` **232/232** 条公式在中译本 5 个章节源码中逐字命中；73 个推导步骤、266 条 pitfalls，推导卡每步带 `provenance`（A 原文明写 / B 补出 / C 判断）与 `locator`。
- 生成物：`index.jsonl` 83 行、`md/` 83 张 Markdown + `md/index.md`、`MAP.md`（mermaid 骨架 + 逐节卡表，由 `tools/gen_map.py` 生成）；`tools/` 另含 `lint_cards.py`、`audit_pages.py`、`build_index.py`、`render_md.py`、`check_formulas.py`；`workflow/PRODUCTION.md` 记来源三级、硬性规则与终审标准，`workflow/cards_plan.tsv` 为 70 条写作清单。
- 同步更新：`datasets/README.md` 的十类数据表、目录树与版本记录加 `v0.13`。
- 说明：全部卡 `status: "draft"`、`rights: "rewritten"`；第 5 节的 expectation 5.14/5.15 与 conjecture 5.6 按「预期」「猜想」措辞，未升格为定理。

## SY01-24 Siebert《镜像对称：代数几何专题讲义》中译注本（三校）+ dataset siebert — 2026-11-19

- 新增 `08_source_code/SY01-24_镜像对称（Siebert 讲义中译本）/`：Siebert 讲授、Van Dyke 记录 *Mirror Symmetry*（Fall 2019 课程讲义，108 页，未出版）→ 中译注本 **103 页**（源码 50 项 / 工程文件 / 成品）。
- 三校：正文改动 **32 行**（概览 1、ch01 4、ch02 6、ch03 4、ch04 5、ch05 3、ch06 9），类别为数学陈述 12 / 术语 11 / 表述 8 / 漏译 1。最重的是把数学条件译错的四处：ch02「阶为 $a$」应为「满足 $\varphi^a=\mathrm{id}$」、ch02 étale locally 误作「平坦局部」、ch03 命题 3.12 把局部完全交收窄成光滑、ch05 定理 5.3 自加光滑性假设且结论缺 $h$；另有 ch06「完美复形↔紧对象」方向说反、Polishchuk 刚性定理引成命题 3.1（应 3.7）。
- 依据：逐句对英文原文 + **nLab 与 Stacks Project** 相关条目 30 余条（条目名与 Last revised 日期全部记在 `工程文件/校对/三校汇总.md` 第 6 节；nLab 取不到的 13 条已如实列出）+ 回查上一轮术语表。
- 术语改定：单值化→**单值变换**（库内用量 272:78 支持）、退行锥→**回收锥**、向法锥变形→**形变到法锥**、上边界→**上边缘**；保留并说明理由：吹起、可表态射、丰/甚丰、接合部。新增 `成品/SY01-24_术语表.md`（70 条：中文/英文/原书首现页/本轮裁决）。
- 新增 `datasets/siebert/`：按原书分节裁出的 **75 张**数学资料卡（概念 46 / 推导 14 / 勘误 15；track A 概览与第 1 章 15、B 叠 11、C GW 与虚技术 11、D 环面几何 12、E 环面退化 12、F 同调镜像对称 12、O 术语 2），印刷页 7–106 覆盖 84 页，97 个推导步骤、84 条定理陈述、324 条 pitfalls、61 条 gaps；schema 与 `datasets/seidel` 同构，`lint_cards.py --strict` 0 error 0 warn，`index.jsonl` 75 条、`render_md.py` 75 卡 + index.md。
- 说明文件同步更新：`工程文件/使用说明.txt` 按三校重写（编译链、源码 50 项清单、本轮改动、原文问题 10 条）；`03_translations_meta/SY01-24/投稿信息.md`（与工程内同名文件一致）；`README.md` 统计块经 `make_stats.py --write` 重算（100 部工程 / 8696 文件 / 372.6 MB / 1662 个 .tex / 2125 张图 / 术语 1630 条）；`00_README.md` 的语料与工程数（49,035 段、100 部、1,630 条术语）与「成品 PDF 去向」表述按 R3 更正；`datasets/README.md` 版本记录加 `v0.12`。
- 台账 `RELEASE_REGISTER.csv` 追加 SY01-24（讲义、L2 公开·受限、**成品随仓公开**、原文 L4 禁入）；原文 PDF 不随仓、不发布、不给直链。
- 编译：XeLaTeX → Biber → XeLaTeX×2 → makeindex → XeLaTeX；103 页、0 Overfull、`main.ind` 70 条唯一词条；`工程文件/使用说明.txt` 已按本轮改定重写。

## SY07-10 Miličić《D-模的代数理论讲义》中文校订批注本 — 2026-11-19

- 新增 `08_source_code/SY07-10_D-模的代数理论讲义（Miličić）/`：英文讲义 150 页 → 中译本校订批注本 **153 页**（源码 / 工程文件 / 成品）。
- 校订：283 条编号条目与原文**逐条对齐（37 节零差异）**；改动 **79 处**（P1 25 / P2 44 / P3 10）。最重的是第 I 章 §10 整段漏译 6 条（10.5–10.10，已补译）与 §12–§13 把逆像 $i^+$ 全按直像 $i_+$ 录入 33 处（Kashiwara 定理陈述因此失真）。
- 体系：定理编号由 `[chapter]`（显示 1.1…1.79、与正文「节.序号」引用全盘错位）改为节内编号，恢复原书体系；术语统一（holonomic→完整、正像→直像）。
- 校注 **17 条**（I8/II2/III2/IV3/V2），每条末句标来源：Stacks Tag 00IN/00IP/00KE/0055/00LA/07BK/01BD/01BU/0A6Y 与 8 个 nLab 条目（附 Last revised）。
- 新增 `datasets/dmod/`：**61 张** D-模资料卡（59 概念 + 2 例子，九轨 O–H）；lint 0 错、原文对齐 `match 61 ／ broken 0`、`external-confirmed` 17 ／ `source-only` 44 ／ `rejected` 0。
- 台账 `RELEASE_REGISTER.csv` 追加 SY07-10（随仓公开，成品在仓=是）；`tools/check_compliance.py` 通过。

## dataset seidel 复核与扩卡 — 2026-11-19（70 张）

- 规模：54 → **70 张**（32 概念 + 8 推导 + 30 校订），补 operad、HPT、Kadeishvili、Yoneda、映射锥、拟同构、例外对象、directed A∞、Maslov 类、谱序列、Pin、Serre 函子、Dehn 扭转、PL 公式、LF 的 Fukaya 范畴、A_m 奇点 16 张概念卡。
- 复核：24 张旧概念/推导卡对照原书页图与 nLab/arXiv 逐条重审，**全部查出错误并改正**（含 theorem-b-construction 的包含方向、split-generation 的分裂闭包、matching-cycle 的构造、A∞ 符号约定）。
- 校订卡：30 张覆盖 `修订总表.tsv` 40/40 行，逐张回页图；12 张页码修正；新增 p183 `\subset`→`\in` 原书排印笔误登记。
- 两处拟修订经核不成立，正文已回退、卡改为“复核否决”记录：`section-6.tex:7`（p87 作 In fact）、`section-14-a.tex:44`（p199 作 explains）。有效修订 31 → **29**。
- 证据：`work/review/verification*.jsonl`、`report-verify-*.md`、`correction-coverage.tsv`；`lint_cards.py --strict` 0 error。

## dataset seidel — 2026-11-19（Seidel《Fukaya categories and Picard–Lefschetz theory》资料卡 54 张）

新增 `datasets/seidel/`：把全书校订工程（301 页译注本、187 条译者注、31 处译文修订 + 9 条术语统一）
裁成 **54 张资料卡**，按三条轨道组织（A：A∞ 与三角范畴；B：Floer 与 Fukaya 范畴；C：Picard–Lefschetz 理论）：

- 概念卡 16（A 6 / B 6 / C 4）：A∞ 代数与范畴、扭曲复形、Karoubi 完备化、分裂生成、正合三角；正合 Lagrangian、
  Floer 复形、Maslov 指标、行列式线、膜结构、Fukaya 范畴；Lefschetz 纤维化、消失圈、匹配圈、顶针。
- 推导卡 8（A 6 / C 2）：μ^d 分次、扭曲微分、映射锥、分裂生成、PL 归纳、定理 B 构造、变异、directed dg。
  每步带 `text/why/locator/provenance`，provenance 分 A（原书）/B（由原文推出）/C（上下文推断）。
- 校订卡 30（A 5 / B 12 / C 13）：一卡记一处初版错译，字段 `page/original/corrected/why/note`；
  由 `精选数据/修订总表.tsv` 的 40 行机械聚合（operad 2 条并 1、thimble 9 条并 1），页码取修订理由中的印刷页或
  `page_map.csv`，不手填。已知缺口：`section-10-cd.tex:41` 两条 H³→H² 因同 slug 合并为 1 卡。
- 结构：`SCHEMA.md`（csw 体系的 seidel 版，三卡型 + 三轨）、`cards/{concepts,derivations,corrections}/`、
  `index.jsonl`（54 行）、`md/`（54 卡 + index.md，按类型分目录）、`MAP.md`（三章骨架图）、
  `workflow/PRODUCTION.md`（输入、写卡规则、G0–G5 门禁）、`tools/{lint_cards,build_index,render_md}.py`。
- 工具链自检：`lint_cards.py --strict` **54 卡 0 error / 0 warn**；`render_md.py` 54 卡 + 索引。
- 权利：全部 `rewritten`；单处引文 ≤60 字（超长截断并在 `note` 注明），不复制原文段落；底本为 EMS 在版图书，
  译文与 PDF 不入公开仓库，只有卡片以 CC BY 4.0 发布。
- 材料来源：校订工程的 12 份分章报告、`译者注总表.tsv`（187 行）、`修订总表.tsv`（40 行）、`errata.md`；
  卡片与注文共享同一页码锚（印刷页 = PDF 页 − 8）。

## dataset glc — 2026-11-18（陈麟《几何 Langlands 讲义》资料卡 154 张，逐卡外部核验）

新增 `datasets/glc/`：把陈麟《Introduction to Geometric Langlands Theory》（清华 2023 秋讲义，
2025-08-08 修订，85 页、16 章 119 节）逐条裁成 **154 张概念卡**，按九条轨道组织
（O 总览 4 / A 整体类域论 4 / B Hecke 与 Satake 9 / C Whittaker 与 Laumon 20 / D Fourier 与洁净性 19 /
E 因子化与 Ran 空间 18 / F 消失与范畴猜想 30 / G 谱侧与 Hitchin 20 / H 局部等价与证明架构 30）。

- 硬要求「不能有错」的落地：**8 名 drafter 起草 + 16 名 verifier 一章一人独立核验**（两拨人不相交）。
  verifier 逐句与译本锚点对齐，再去 nLab / Stacks Project / 讲义参考文献逐字找依据，记录「哪句支持哪条断言」。
  结果：**external-confirmed 66 / source-only 88 / rejected 0**；`alignment=error` 9 条，已全部改正并复验。
- 抓到的 9 处实质错误包括：量子局部 GL 的「水平 $\kappa$」与「临界水平」混用、Whittaker 特征函数的指数符号、
  $\operatorname{QLisse}$ 的定义（应为 $\operatorname{IndLisse}$ 的左完备化）、范畴迹的单位/余单位对调、
  Fourier–Deligne 变换的 $t$-正合性、平均函子的基础情形、消失定理的秩条件 $k<\operatorname{rank}E$、
  $P=G$ 的归属、整体函子的提升方向。明细见 `datasets/glc/README.md` 修订表与 `verification.jsonl`。
- 结构：`SCHEMA.md`（csw v1 + `verification` 扩展）、`cards/concepts/*.json`、`verification.jsonl`（154 行台账）、
  `index.jsonl`、`md/`（154 个）、`taxonomy.md`、`MAP.md`、`workflow/PRODUCTION.md`（四闸 + 本批执行记录）。
- 工具链：`tools/lint_glc.py`（含 verification 交叉校验，`published` 不得是 source-only）、`build_index.py`、
  `render_md.py`、`gen_docs.py`，全部随仓；lint **154 卡 0 error / 0 warning**。
- 权利：全部 `rewritten`，不复制原文；`sources` 标章、节、条目号与印刷页。
- 根 `README.md` 新增「资料卡试点：几何 Langlands（`datasets/glc/`）」小节。

## dataset csw — 2026-11-17（Witten 1989 资料卡 40 张）

新增 `datasets/csw/`：把 Witten 1989（*Quantum Field Theory and the Jones Polynomial*，CMP 121, 351–399）
拆成 **31 张概念卡 + 9 张例子卡**，九条轨道（O 总览 / A 三维理论 / B 相空间 / C 几何量子化 / D 穿刺点与 BWB /
E WZW / F 对偶 / G 计算 / H 边界），与 `papers/WIT-1989-JONES/` 的 49 页讲义、97 页注疏本、六场研讨班记录配套。

- 结构：一卡一 JSON（`cards/`），渲染版 `md/`，索引 `index.jsonl`，依赖图 `MAP.md`，总表 `taxonomy.md`；
  规范 `SCHEMA.md`（概念卡 17 个必填字段、例子卡 16 个，`proof.status=sketch` 必须写 `gap_note`）。
- 工具链：`tools/_data1..5.py`（源数据）→ `build_cards.py` → `lint_csw.py` → `render_md.py` → `gen_docs.py`，
  全部随仓，`lint` 结果 **40 卡 0 error / 0 warning**。
- 队伍与流程：`workflow/PRODUCTION.md` 记录 Lead + historian/bibliographer/archivist/verifier 五角色、
  四道闸（结构 / 证据 / 内容 / 入库）与纠错流程；卡片的“原子断言”来自研讨班 `sessions/s1..s6` 的 claims。
- 权利：全部 `rewritten`，不复制原文；`sources` 逐条标印刷页与 tex 锚点。
- 根 `README.md` 新增「资料卡试点：Chern–Simons 与共形场论」小节，`datasets/README.md` 十类数据表增 `csw/` 一行。

## translation SY02-09 — 2026-11-17（成品 PDF 随仓公开）

袁瑶（Yao YUAN）*Langlands 纲领导论*（2020 年春季课程讲义，未出版，原稿 198 页）中译注本随仓发布：
`成品/Langlands纲领导论_中译注本.pdf`（162 页，11.3 MB）+ 两张预览图。

- 由仓内 `源码/` 原样重编：`xelatex → makeindex → xelatex ×2`，0 error / 0 Overfull / 0 未定义引用。
- 底本为公开课程讲义（未出版），台账 `成品级别=随仓公开`、`成品在仓=是`；R3 对在版图书仍不放行。
- `.gitignore` 增该工程 `成品/*.pdf` 反向规则；`投稿信息.md` 的成品说明同步。

## translation SY07-09 — 2026-11-17（陈麟《代数几何讲义 I》中译注本 + 定义与定理资料卡 366 张）

新增工程 `08_source_code/SY07-09_代数几何讲义I（陈麟）/`：Lin Chen（陈麟）*Notes for Algebraic Geometry 1*
（2025 年秋季课程讲义，英文，原书 171 页）的整本中译注本，以及从译注本逐条裁出的资料卡。

- 译注本 195 页：31 节（§0–§30）+ 附录 A（阿贝尔范畴）+ 附录 B（术语英中对照）+ 参考文献；
  定理类编号与原书逐条对应（「节.小节.序号」），205 条译注，引用 Stacks Project 123 个不同 Tag、nLab 15 条
  （均记 Last revised），术语 226 条；编译 xelatex ×2，0 error / 0 Overfull / 0 未定义引用 / 0 缺字。
- 资料卡 64 页 366 张：定义、定理、命题、引理、推论、断言、预备定义、命题—定义 8 类；
  每张标「§小节 · 原书页」，卡内交叉引用全部换成字面编号（全文无 `??`），书末附条目索引。
  生成链为 `工程文件/tools/extract_cards.py`（讲义源码 → cards.json）与 `gen_deck.py`（→ tex → pdf），两脚本随仓。
- 两份成品 PDF 随仓（`成品/`，共 1.7 MB）：底本为公开课程讲义、未出版，台账记
  `成品级别=随仓公开`、`成品在仓=是`；`check_compliance.py` 新增「台账驱动的成品放行」——
  登记为随仓公开的工程，其 `成品/*.pdf` 才通过 R3，其余工程仍按原红线拦截。
- 原书笔误 50 余处（Algbera/Algera、Haussdorff、Principle open subschemes、$f_*$ 与 $i_*$ 互换等）
  一律不改编号与结构，正文按正字排印并在译注或《疑点清单》说明；疑点 55 条全「已解」。

## translation SY07-08 v1.1 — 2026-11-17（术语更正：presheaf 前层 → 预层）

仓主指出 presheaf 的标准中文译名是**预层**（本库术语基原本就有 `前層 → 预层` 一条），
而 SY07-08 初稿误作「前层」。本次全量改正，并把判据写进术语基与工程纪要：

- 术语基 `01_corpus_zh/termbase.jsonl`：`前層 → 预层` 由 `candidate` 升级为 `confirmed`（等级 A、记裁决来源）；
  新增 `presheaf 预层`、`constant presheaf 常预层`、`morphism of presheaves 预层态射` 三条英文条（1627 → 1630 行）。
- SY07-08 正文：32 个文件「前层 → 预层」（21 个块共 72 处含索引项），索引键 `qianceng → yuceng`、
  `changqianceng → changyuceng`；重编译 **209 页 / 0 未定义引用 / 0 Overfull / 0 缺字**，条目编号仍 12 节全连续（210 条）。
- 审计方向翻转：`check.py` 禁用术语由「预层」改为「前层」，`normalize.py` 规则改为「前层 → 预层」，防止回退。
- 交付报告新增「术语更正记录」一节；`工程文件/工作流与决策纪要.md` §3 记录决策链与教训
  （**开译前先 grep 术语基，库里有条目者不得自行「通行译法」式新造**）。
- 成品 PDF 依 COMPLIANCE v1.0 不随仓；仓内只更新交付报告、术语表与三张预览图。

## datasets v0.10 — 2026-11-17（kw06：Kapustin–Witten 资料卡 67 张）

`datasets/kw06/`：把 K–W 2006 的三份工作底稿（219 页解经本、46 页导读讲义、第二期研讨班八轮报告）
压成**概念卡 + 推导卡**：40 张概念卡、27 张推导卡、约 100 个推导步骤。

- 每张卡都带印刷页锚（`B p.N`，必要时带式号）、常见误解（≥2）、相关卡；概念卡另有核心公式与
  「定理 + 证明或缺口」（complete / sketch / gap 三态诚实标注）。
- 推导卡每步四栏：`text`（做了什么）/ `why`（为什么必须这样）/ `locator`（原文页）/ `provenance`
  （A 原文写了 / B 原文暗示我们补的 / C 我们的判断）。
- 工具链：`tools/draft_cards.py`（从解经本 JSONL 起草）、`tools/lint_cards.py`（--strict 0 error）、
  `tools/audit_pages.py`（134 条 B 底本 anchor 逐条回页文本核，0 issue）、`tools/build_index.py`、
  `tools/render_md.py`（67 份可读 Markdown + 索引）。
- 骨架图 `MAP.md`（mermaid，四维→扭化→紧化→二维→Langlands→回到四维）、分类 `taxonomy.md`、
  规范 `SCHEMA.md`；全部 `rights: rewritten`、`status: dev`（机器自检 + 抽核，未人类逐卡认证）。

## lecture-notes v1.0 — 2026-11-17（Kapustin–Witten 十讲导读讲义）

`05_seminar_witten/seminars/SEM-0604151/lecture_notes/`：46 页 TeX 讲义，
把 231 页原文压成十讲，供第一次读原文的人用（形态上区别于 219 页解经本与研讨班报告）。

- 结构：写在前面（三条读法 / 前置 / 记号 / 十讲地图 / 三条诚实提醒）+ 八讲正文 + 附录 A 术语 90 条、
  B 习题 30 题（均带提示）、C 参考文献与阅读路线。
- 每讲统一五件：本讲目标 → 正文（2,200–3,200 汉字）→ 本讲核心 → 跟读提示（原文页段）→ 自检问题；
  断言带 `\src{B p.N}` 页锚，可回原文逐条核对。
- 质量：两遍 xelatex 0 error、0 overfull、0 missing character；`tools/check_lectures.py --strict` 0 issue。
- 附带：第 3 讲把 (3.52) 的正确形式与「OCR 把倒数读反」的坑写进正文（对应解经本 v1.2 勘误）。
- 已知薄弱：§1.4 可解性依赖 T-对偶直觉、§2.3 GNO↔^L G 只给一行、§8.1 三类膜四维推导未展开。

## seminar v1.0 — 2026-11-17（SEM-GL2 第二期八轮 + 合册）

`05_seminar_witten/seminars/SEM-GL2/`：威腾讨论班第二期结项（draft-v1.0）。

- **组织**：三文本轮读。B = Kapustin–Witten 2006（hep-th/0604151，231 页）切八节 U01–U08，
  D = Frenkel《Gauge Theory and Langlands Duality》（arXiv:0906.2747，32 页）与
  C = Witten《Mirror Symmetry, Hitchin's Equations, and Langlands Duality》（arXiv:0802.0999，15 页）
  为全员通读的前置导读。每轮五拍：报告 → 三席质询 → 修订（before/after diff）→ 证据核验 → 独立复算 → 语料入库。
- **产出**：8 份定稿报告（合计约 10 万汉字、约 2,100 处 `B p.N` 页锚）、8 份讲义、
  112 条七类语料（reasoning 24 / concept 24 / challenge 16 / misconception 16 / qcard 16 / meta 8 / crosswalk 8）、
  8 份 verify + 8 份 recalc（复算脚本可重跑）、合册 198 页 PDF、三文对读表 20 主题、盲区清单 40 条、训练价值终评。
- **质量门**：每轮 `check_round.py` 0 error / 0 warn；语料 `check_package.py` 112 条 0 error；
  合规 `--compliance` 0 error（无原文、页图、逐页文本、整节译文、本机路径）。
- **副产物（真收获）**：讨论班抓出已发布解经本 SEM-0604151 的 **6 处实质错误**并回原页图核对后重编：
  (3.52) 共轭位置写反（v1.2，5 处）；§4.2 (4.11)(4.20)、§10.5 (10.36)(10.41)(10.42)、§12.3 复 Hitchin
  的下标 bar 丢失一族（v1.3，5 文件 8 式）。教训：locator 对得上不等于公式对，文本层抽取会系统性丢上划线。
- **局限**：单次讨论水平；语料未经人类认证，只能标 dev；证据抽核是抽样；B 的严格化路线未展开。

## datasets v0.9 — 2026-11-16（路径积分资料卡：50 张）

新增 `datasets/pathintegral/`：把李思《量子力学与几何》第 2 章「路径积分形式」拆成
**1 张总览 + 29 张概念卡 + 20 张例子卡**。五条轨道：A 定义与时间切片 → B 高斯与谐振子
（精确答案）→ C 渐近方法与半经典 → D 格林函数、WKB 与隧穿 → E 威克图、Moyal 与量子 HKR。

- 概念卡：定义、要点、公式、定理与逐步证明（每步有 `why`）、易错点、相关卡、逐条出处；
  例子卡：设定 → 计算 → 结果 → 可独立复核的 `check`。共 65 条定理、219 个证明步骤、
  109 个例子计算步骤、145 条公式、207 条易错点。
- 配套：`README.md`（概念卡/例子卡用法、三条推荐路线、页码约定）、`taxonomy.md`（50 张总表）、
  `MAP.md` + `map.svg/png`（五轨脉络图）、`SCHEMA.md`、`index.jsonl`、`md/`（50 张渲染版）、
  `tools/`（lint、页码审计、索引、Markdown、地图、总表）、`workflow/`（生产协议与提示词）。
- 质量门：`lint_pi.py` 50 卡 0 错 0 警告；`audit_pages.py` 0 问题；中文散文与底本比对
  无连续 20 字相同片段（最长 14 字）。独立审校修掉：伽马函数拉普拉斯推导漏 `λ^s`、
  拉普拉斯端点半高斯误用、斯托克斯射线与反斯托克斯射线混淆、位置完备性循环论证、
  虚时间记号冲突、预解核 `iε` 跳步、WKB 前因子的方向分支与 `m/ℏ` 因子、自由格林函数
  符号解释等。
- 书中存疑（未擅改底本，在对应卡 `pitfalls` 注明）：p.83 动量本征态归一约定；p.90
  §2.3.1/§2.3.2 页码边界；p.120 例 2.7.3 的 `A` 应为 `A²`；p.123 起格林函数端点次序；
  p.144 例 2.8.8 的 `Aut(Γ)` 应为 `D4` 而非 `Z2³`；命题 2.8.11 证明漏 `i/(2πn)`；
  ch02a.tex:1451 斯托克斯射线判据与上文矛盾；§2.5.2 与 §2.5.3 的指数符号约定不一致。
- 权利：全部 `rights: "rewritten"`；公式照录，出处逐条标原书印刷页（80–160）。
- 文档：`datasets/README.md` 升为十类并加 `pathintegral/` 行；根 README 增加「资料卡试点：
  路径积分」入口与框架地图。

## datasets v0.8 — 2026-11-16（几何量子化资料卡：48 张）

新增 `datasets/geoq/`：把李思《量子力学与几何》第 5 章「几何量子化」拆成
**1 张总览 + 27 张概念卡 + 20 张例子卡**，每张卡可单独抽出使用。

- 概念卡：定义、要点、公式、定理与逐步证明（每步有 `why`）、易错点、相关卡、逐条出处；
  例子卡：设定 → 计算 → 结果 → 可独立复核的 `check`。共 55 条定理、214 个证明步骤、
  97 个例子计算步骤、163 条易错点。
- 配套：`README.md`（概念卡/例子卡用法、复习与教学、三条推荐路线、页码约定）、`taxonomy.md`（48 张总表，逐卡标
  印刷页与源码行）、`MAP.md` + `map.svg/png`（四轨脉络图）、`SCHEMA.md`、`index.jsonl`、
  `md/`（48 张渲染版，供阅读/打印/Anki）、`tools/`（lint、页码审计、索引、Markdown、
  地图）、`workflow/`（生产协议与可复用提示词）。
- 质量门：`lint_geoq.py` 48 卡 0 错 0 警告；`audit_pages.py` 0 问题；中文散文与底本
  比对无连续 20 字相同片段。两轮独立审校修掉 18 处数学/记号问题（星交换子 ℏ 因子、
  极化局部解空间维数、马斯洛夫计数、哈密顿向量场符号、$G_0/G_1$ 次序等）。
- 书中三处存疑：p.276 归一化系数、p.280 Segal–Bargmann 变换指数、ch05b.tex:1426
  特例符号；均未擅改底本，在对应卡 `pitfalls` 注明。
- 权利：全部 `rights: "rewritten"`；公式照录，出处逐条标原书印刷页（250–296）。
- 文档：`datasets/README.md` 升为九类并加 `geoq/` 行；根 README 增加「资料卡试点」
  入口与框架地图。

## datasets v0.7 — 2026-11-16（第一本书拆完：43 个词条）

在 v0.6 的 17 条基础上补齐 Tachikawa 全书：**43 个词条、187 条定理、130 个例子**；
128 条证明为 `complete`（原书没证的标【补】），59 条为 `sketch` 并写 `gap_note`。

- 新增词条（26）：奇异同调、CW 复形、上同调环、Hurewicz；示性类、陈类、Stiefel–Whitney、
  Euler 类、Pontryagin 类；分类空间、Thom 同构、Chern–Simons；Čech 上同调、群上同调、反常；
  旋量、Clifford 代数、Bott 周期；K 理论、十重分类；eta 不变量、配边、广义上同调、指标定理；
  toric code、瞬子。
- 代表性补证：∂²=0、cup 积 Leibniz 法则、Euler–Poincaré 公式、Poincaré 引理、Stokes 广义定理、
  Hurewicz（S^n 特例）、dCS=tr F²、大规范变换量子化、BPST 自对偶与 8π²/g²、2^{2g} 简并。
- 代表性计算：CP^n 的 c(TCP^n)=(1+c)^{n+1} 与陈数、RP² 的 w1/w2、S² 的 e 积分=χ=2、
  K(S²)=Z⊕Z、KO(S^n) 表、十重分类读数、S³ 上 CS 作用量 −2π、Landau 能级 η̃、K3 的 Â=2。
- `datasets/encyclopedia/README.md` 更新为「第一本已拆完」，列出全部 43 条；README/目录树/统计同步。
- 状态：1 条 reviewed、42 条 draft；独立复核后升级（复核重点：标【补】的证明与页码）。

下一步：复核已写词条并升级；接入用户提供的带答案习题集与人工精选例子；超对称场论词条（长期重点）。

## datasets v0.6 — 2026-11-16（词条库：按概念而不是按书组织）

新增 `datasets/encyclopedia/`：第一本供料是立川裕二《物理学家用代数拓扑》，但分类轴是**概念词条**，
不是书或章节。17 个词条、74 条定理、50 个例子；59 条证明为 complete（原书没证的标【补】），
15 条为 sketch 并写 gap_note。

- `datasets/encyclopedia/README.md`：定位（改写而非搬运）、词条字段、六条写作纪律（自足、证明完整、
  例子要算、改写不复制、页码真实、诚实标注）、权利边界（`rights: rewritten`；单处引文 ≤60 字，
  累计 ≤10%；不复制图）。
- `datasets/encyclopedia/ENCYCLOPEDIA.md`：词条 JSON 规范（definition / theorems[proof.steps] /
  examples / physics / pitfalls / related / sources）。
- `datasets/encyclopedia/taxonomy.md`：约 45 个词条的总表与出处页码，SUSY 类目先占位。
- `datasets/encyclopedia/entries/`：17 个 JSON。几何（流形、定向、连通和、李群）、丛论（纤维丛、
  主丛、向量丛、切丛、自旋结构）、同伦（同伦群、长正合列、Hopf 纤维化、覆盖空间）、上同调
  （微分形式、de Rham、Stokes、Mayer–Vietoris）。demo 词条流形为 reviewed，其余 draft。
- `tools/entry_lint.py`：id/路径一致、类目白名单、summary 长度、complete 证明 ≥2 步且每步有 why、
  sketch 必须有 gap_note、例子必须有 computation/result、页码 1–207、与译稿 12 字重合告警
  （按符号断句，避免公式把句子拼成假重合）、`--index` 生成 index.jsonl。
- 合规：`COMPLIANCE.md` §11 增第 9 条——只收改写词条，不收原书/译本章节；单处引文 ≤60 字、
  累计 ≤10%；不复制原图；pages 必须真实；有异议按 §8 撤下。
- `datasets/README.md` 升为「八类数据」，加 `encyclopedia/` 行与 `rights: rewritten`。

后续：第二批 ch6–ch8（同调、示性类、Chern–Simons）、第三批 ch9–ch13（群上同调、旋量、K 理论、
指标定理）；用户将提供带答案的习题集与人工精选例子；超对称场论词条是长期重点。

## datasets v0.5 — 2026-11-16（SEM-0604151 讲义生产的数据流）

把「K–W 2006 分层解经本」的制作过程本身作为数据发布：不只是成品，还有**怎么一步步做出来的**。

- 新增 `datasets/traces/KW06-04.lead.jsonl`（52 条）：决策流。清点 421 份材料 → 确认底本无中文全译本 →
  定四层结构与 S1–S8 编号 → 派 12 个写作单元（并发上限 8，4 个被拒后补派）→ 整合修（重复 label、
  私有宏、伪引用）→ 机器审计 → 首版 207 页 → 用户反馈 → 四张交换图 + 附录 D 60 条 → v1.1 219 页。
  每条带 `action`（read/tool/write/check/fix/decide/think/report）、`observation`、`decision`、`error`；
  `fidelity="reconstructed"` 标明是从会话摘要重建，不是原始事件导出。
- 新增 `datasets/traces/KW06-04.units.jsonl`（17 条）：15 个写作单元（lead + 2 结构层 + 4 骨血 + 2 细度 +
  1 对照 + 1 语料 + 1 讨论班 + 3 问答录）的回执：交付统计（页数/锚点/A-B-C/图表）、自编译结果、
  **最弱两处**。弱项不是装饰：它们被原样写进书的前言「已知薄弱处」。
- 新增 `datasets/workflow/KW06-04_讲义生产协议.md`：可复用协议——分层产品定义、并发分工模型、
  writer 提示词模板、共享约定（页码映射 / 公式号核对 / A-B-C 三级标注）、5 道验收门、
  **13 条环境坑与对策**（Windows PowerShell 无 pwsh、.ps1 无 BOM、xeCJK `\colorbox` 崩溃、
  tikz-cd 文本模式、`\shortstack`、圈号缺字、Poppler 缺 Adobe-GB1、CRLF 文件、Select-String 忽略大小写等）。
- 语料侧：该工程 `derivation/dialogue.jsonl` 60 条（附录 D 的机器可读版，A 级、带原文短引与页锚）
  与既有 308 条推导链一并发布在 `05_seminar_witten/seminars/SEM-0604151/`。
- `ds_publish --write`：12 个可发布文件、0 条被阻（trace 记录无 rights 字段，按规则视为可发布）。
- 训练视角：这批数据的价值在「错误 → 修复」的配对（报错文本 + 修法）与「验收门」的判定过程，
  不是成品文字的又一次誊写；因此 trace 保留 `error`/`outcome=partial` 的记录，不做美化。

## datasets v0.4 — 2026-11-16（第一批 L0 修正与三张跨工程精读卡）

按"先修余料、再补理解"的顺序做了第一批实活，并把成本记下来，作为是否上量的依据。

- 新增 `tools/ds_fix_l0.py`：读 `harvest_queue.jsonl`，按 `para_id` 回改 `01_corpus_zh/zh_paragraphs.jsonl`；
  默认只 `--dry-run`，`--apply` 才落盘；删除 `meta_block`/`template` 段，去尺寸残渣、合并空白、展开未定义宏；
  改动留档 `datasets/fixes/l0_batch01.jsonl`（before/after 各截 2,000 字）。
- 关键实现：宏**不能全局展开**。`SY01-17` 的导言把 `\R`、`\C` 定义为 `\mathcal{R}`、`\mathcal{C}`，全局换成
  `\mathbb{R}` 会改错语义；改为按工程扫 `源码/**/*.tex|sty` 的 `\newcommand`/`\DeclareMathOperator` 建表，逐工程展开。
- 第一批（队列前 50 条）：44 条修正、3 条删除、3 条无改动；语料 49,038 → 49,035 段，4,035,712 → 4,035,682 汉字。
- 新增 3 张跨工程 L2 精读卡：`SY01-01` 谱流（分次自同构的显式作用，补原文一句带过的构造）、
  `SY01-09` SYZ 猜想的启发式推导（A-膜模空间 = X̌、逐纤维 T 对偶、两处 resp. 的交叉对应）、
  `SY03-08` Chern–Simons 形式在规范变换下的全导数项（符号与左右作用约定绑定）。
- `datasets/PUBLISH.json` 重生成：10 个可发布文件、0 条被阻；`candidates/` 与 `fixes/` 属内部台账，不参与发布清单。
- 成本：L0 约 0.5 人时/50 条；L2 单卡 AI 起草 2–3 分钟、人工复核 8–12 分钟。

## datasets v0.3 — 2026-11-16（存量回收：`ds_harvest.py` 与五级标注）

不追 Lean，不追"再译几篇"；把库里已经译过、但价值没榨干的"余料"找出来，补成可训练的中文数学推理数据。

- 新增 `tools/ds_harvest.py`：确定性打分（不调用模型），规则为 `flags`（meta_block / orphan_number / empty_ref /
  overlong / junk_trimmed / layout_residue）、未展开宏（`\R \C \Z \Hom \dd \mathrm \ref` 等）、悬空引用、碎片/超长段、
  本机路径残留、工程尚无精读卡；输出 `datasets/candidates/harvest_queue.jsonl`（每工程上限 25 条 + 术语候选 200 条）。
- 首跑：2,009 个段落候选、1,412 条 `status=candidate` 术语；选定 700 条入队。最高频信号是"工程尚无精读卡"（1,985 段），
  其次是未展开宏（374）、碎片段（321）——说明存量里最大的一块价值是"还没被理解"，不是"还要再译"。
- 新增 `datasets/workflow/余料回收.md`：三种采样（审计/主动/覆盖）、五级标注（L0 修正→L1 术语→L2 精读→L3 数学条目→L4 对话流）、
  "AI 提议 + 规则校验 + 人工抽检"流程、质量指标；明确不做 Lean 形式化，校验靠可复核的证明步骤与依赖。
- `datasets/README.md`、`README.md`、`datasets/math/README.md` 同步：`math/` 的校验以人工复核为主，形式化有现成产物才收录。

## datasets v0.2 — 2026-11-16（转向数学与推理：`datasets/math/`）

方向调整：模型缺的不是「译法」，而是数学理解、证明能力与**中文推理链**——研究级中文数学语料近乎空白，
现有数学语料以英文为主（NuminaMath 86 万条英文 CoT），中文数据集中在 K-12 题库。据此把数据集主力从
`parallel/`（翻译对齐）转到 `math/`（数学推理条目），`parallel/` 降为术语与表达的小样本。

- 新增 `datasets/math/README.md`：记录定义（`kind/statement/context/proof/proof_steps/dependencies/
  difficulty/verification/rights`）、生产流程（选点→自足化→写证明→挂依赖→校验→门禁）、扩量顺序、
  反面清单；设计参照北大 AI4Math 的三条经验（命题级检索、层级展开、形式化反馈）。
- 新增 `datasets/schema/math.schema.json`（draft-07）；`verification.kind ∈ {lean,human,none}`，
  `status ∈ {checked,sketch,unchecked}`，标 `lean` 必须给编译过的 `artifact`。
- 试点 `datasets/math/SY05-25.sec1.jsonl`：6 条中文数学记录——复辛流形定义、Riemann–Hilbert 对应、
  Y(G,C) 的复辛结构（含非退化性的 gap）、A/B 模型的几何前提、广义复结构形变、量子几何 Langlands；
  每条带 `proof_steps`（含 `gap`）与 `dependencies`，难题标 `sketch` 而非 `checked`。
- `tools/ds_lint.py` 支持 `math/`：字段、id、`kind/lang` 枚举、`verification` 结构、字数上限
  （陈述 ≤4,000 / 证明 ≤12,000 / 单条 ≤24,000）；`ds_lint` 47 条 0 错，`ds_publish --check` 7 文件 0 blocked。
- `COMPLIANCE.md` §11 增第 8 条「数学校验诚实」；`datasets/README.md` 改为七类数据并写明方向调整；
  `README.md` 的 `datasets/` 小节与结构表同步。
- 下一步（P1）：每部 arXiv 工程挑 3–5 个技术引理，目标 150 条；形式化对（NL↔Lean）先做 20 条能编译的。

## datasets v0.1 — 2026-11-16（P0 试点：把译本变成可训练数据）

v1.5.0 解决了"什么能发"，这一轮解决"发了以后怎么让模型真的学到东西"：只给译文不够，训练缺的是
**原文片段、译法理由、工作过程**。新增与译本并列的第五类资产 `datasets/`，先以 SY05-25（Witten,
arXiv:0802.0999）第 1 节为试点跑通全链路。

- 新增 `datasets/README.md` 与 `datasets/schema/*.schema.json`（6 个 draft-07 schema）：平行片段、
  精读卡、高光、工作流事件、概念图谱、评测题；id 形如 `SY05-25.p0001`。
- 试点 41 条记录：`parallel/` 7 条（原文↔译文↔为什么这样译）、`deepread/` 4 张（含证明骨架与跳步补全）、
  `highlights/` 3 条（C* 作用论证、Im Ω 上同调平凡、形变枢纽）、`bench/` 3 题（带 rubric 与 must_not_include）、
  `kg/` 6 节点 6 边、`traces/` 12 事件（含一次 lint 报错→修复的真实过程）。
- 权利三分：`self` CC BY 4.0 可训练；`arxiv:<id>` 逐篇核许可、未确认只留 ≤300 字引用；`book` 只进
  `datasets/_internal/`（`.gitignore` 已忽略），永不发布、不进公开训练集。
- 新增 `tools/ds_lint.py`（结构、id、行号、字数、权利、敏感路径）与 `tools/ds_publish.py`
  （发布前过滤，生成 `datasets/PUBLISH.json`）；`ds_lint` 41 条 0 错，`ds_publish --check` 6 文件 0 blocked。
- `COMPLIANCE.md` 新增 §11：引用上限（原文 ≤600 字/条、单条 ≤1,400 字；精读卡 ≤6,000 字）、
  不得新增 L4、行号可追溯、发布过滤、trace 脱敏。
- `.githooks/pre-commit` 同时跑 `check_compliance.py` 与 `ds_lint.py`；`README.md`、`00_README.md` 增
  `datasets/` 说明。
- 下一步（P1）：把同一协议推到其余 36 部 arXiv 工程，再做 22 部讲义；图书底本只做 `_internal/`。

## v1.4.3 — 2026-11-15（《纪律》v2.1：社区类来源白名单扩为 nLab / Stacks Project / ProofWiki）

作者决定：**社区类来源不再只认 nLab**。Stacks Project 与 ProofWiki 与 nLab 并列进入 B 级白名单，
可作译注依据（须与 A 级交叉验证，正文一律不缓存）。理由是各专业的实际查证路径不同：
代数几何核定理用 Stacks（带 `Tag` 编号与完整证明），标准定理拆"显然"跳步用 ProofWiki，
概念网络与文献线索用 nLab。

- `04_playbook/01_数学文献翻译纪律.md` 升 **v2.1**：
  - §2.5.2 来源分级 B 级行改为「社区类来源白名单：nLab、Stacks Project、ProofWiki」；
  - §2.5.2 末尾 callout（原「nLab 是社区类来源的底线」）改写为白名单制，并说明白名单之外仍是线索级；
  - §2.5.3 改为「社区类来源三家分工」，新增 **Stacks Project**、**ProofWiki** 两节的强项／局限／引用写法／许可注意；
  - §2.5.3 首选入口表新增 ProofWiki 行，Stacks 行的定位说明改写；
  - §2.5.4 查证六步第 3 步按语义分派（概念→nLab、定理与证明→Stacks 并记 `Tag`、跳步→ProofWiki）；
  - §2.5.9 新增「白名单（可作 B 级依据，只存链接与短引用）」与「线索级（可看、不可引）」两段，
    白名单为**穷举制**，新增一家须 Lead 书面批准；
  - §10 铁律 12／13 同步；版本日志新增 v2.1 行。
- `04_playbook/00_学术翻译总纲.md` §8「来源红线」、`04_playbook/README.md` 动笔小节同步为本白名单口径。
- `README.md` 施工标准的版本号 v2.0 → **v2.1**；93 份 `03_translations_meta/*/投稿信息.md` 的版本引用同步。
- `08_source_code/SY01-17_同调镜像对称性浅入门/工程文件/数学文献翻译纪律.md`（v2.0 旧副本）**整体覆盖为 v2.1**，
  仓库内不再并存两个版本。
- 许可注意：ProofWiki 正文 CC BY-SA、Stacks 正文 GFDL、nLab 无正式许可——三者均只存「条目名 + 链接 + 修订日期 + ≤200 字短引用」，
  正文不落库，避免把 SA／GFDL 的传染性带进 CC BY 4.0 的语料库。

## v1.5.0 — 2026-11-16（合规整改：下架、两层许可、台账与提交门禁）

外部第三方评估发现仓库存在四类合规风险，本轮全部处置。**v1.4.2 的「全库统一 CC BY 4.0」作废**——
译文是第三方作品的演绎作品，仓主无权对全库发 CC BY，更无权许可商业训练。详见 `ASSESSMENT_2026-11-16.md`。

- **下架 8 个文件 / 12.6 MB**：SY02-09 的他人讲义原本（198 页 PDF + README）、6 个随仓成品 PDF
  （SY02-11、SY05-25、SY07-08、SY08-02、SY02-10，及 SY05-25 源码下的 `main.pdf`）。
  文件移入仓外私有归档 `_private/2026-11-16_合规下架/`（含 sha256 清单），Git 索引删除。
- **新增 `COMPLIANCE.md`**：四级发布模型（L1 自产全公开 / L2 译文公开受限 / L3 成品仅外链 / L4 原本与扫描件禁入）、
  9 条红线、内容处置表、撤下流程、历史与镜像说明、grandfather 条款。
- **新增 `RELEASE_REGISTER.csv`（96 行）** 与 `tools/build_release_register.py`：逐部登记底本类型、权利状态、
  成品去向；当前 96/96「合规」，41 部走 Release 外链、52 部成品不公开、3 部暂无外链。
- **新增 `tools/check_compliance.py` 与 `.githooks/pre-commit`**：提交前自动拦截原本/扫描件/成品 PDF、
  原文直链、越权许可措辞、未登记工程；当前 6,763 个文件 0 违规。
- **许可改为两层（`LICENSE` v1.1）**：自产层（元数据、术语、标注、轨迹、方法、脚本、站点）CC BY 4.0；
  译文层（译文、译注、语料正文、译文源码）保留权利、仅非商业学术研读、可撤下，其他用途须底本权利人授权；
  明确「未获任何出版社或作者商业授权，也不声称已获授权」。280 处模板句、101 个站点页脚、6 份总纲/说明同步改写。
- **`_PDF清单.tsv`**：41 条 `raw.gitcode.com` 原文 PDF 直链删除，换成 arXiv 摘要页；成品直链仅保留 Release 附件；
  SY02-11 的本地路径、SY02-09 的原本行清空。
- **隐私清理**：`site/catalog.json` 删除 264 处本机绝对路径字段（`proj`/`pkg`/`pdf`），
  trajectory 与日志共 323 处路径替换为 `<HOME>`；13 个 UTF-16 临时输出与 2 个过期迁移脚本删除。
- **`.gitignore`** 增加合规章节：`原本/`、`07_originals/`、`**/pages/`、成品 PDF、编译产物、`_private/` 等一律不入库。
- 统计口径修正：成品只按「有 Release 外链」计数（41 部 / 50.8 MB）；语料 49,038 段 / 81 个工程有正文。

## v1.4.2 — 2026-11-15（许可统一：全库 CC BY 4.0，欢迎训练与蒸馏）

作者决定：**不再区分语料层与译文层，全库统一 CC BY 4.0，公开声明欢迎训练、蒸馏与商用（署名即可）**。
起因是第三方评审的 P2——「语料 CC BY 4.0 明确允许训练」与「译文 CC BY-NC-SA 4.0（非商业）」自相矛盾，
而 `00_README.md` 还留着「默认不用于任何模型训练」。

- 新增仓库根 **`LICENSE`**：CC BY 4.0 全文口径 + 原文权利声明（不授予原文权利、原文 PDF 不随库发布、48 小时内响应撤下）
  + 「语料卫生是内部纪律，不构成对使用者的限制」+ 历史口径（旧表述作废）。
- `README.md` / `DATASHEET.md` / `00_README.md` / `04_playbook/README.md` 许可段全部改写为单一来源，指向 `LICENSE`。
- `00_README.md` 的「训练数据卫生：默认不用于任何模型训练/微调/蒸馏」删除，改为「我们鼓励用于训练，无需申请许可」。
- **285 个工程模板**（`03_translations_meta/*/投稿信息.md` 等）里的
  「语料 CC BY 4.0 + 译文与工程文档 CC BY-NC-SA 4.0」双轨句，统一改为「全库统一 CC BY 4.0，欢迎训练、蒸馏与商用」；
  另有 5 个写「本项目语料默认不用于训练，须经 Lead 书面批准」的模板同步改正。
- 逐部译本的「译注部分 CC BY-NC-SA / CC BY-NC」表述改为按 `LICENSE` 的 CC BY 4.0；
  底本为 NC/ND 的书仍保留「对外分发受原文许可约束」的说明（原文权利不因本许可转移）。
- `site/audit-2026-11-15.html`、`AUDIT_2026-11-15.md` 的整改验收表：该 P2 行由「未改」改为「已修」。

## v1.4.1 — 2026-11-15（语料整改，第三方评审后）

首次由外部第三方对本库做质量评审（报告：`AUDIT_2026-11-15.md` / `site/audit-2026-11-15.html`，
判定 **B+ 有条件通过**），并按评审结论修掉可修项。**语料口径因此全部更新**，旧数字（44,522 段 / 71 包 / 3,668,359 汉字）作废。

### 修了什么

- **补包**：此前有译文却没进语料的 10 个工程入库（新增 `01_corpus_zh/_append_pkg_generic.py`）——
  SY01-20、SY01-21、SY01-22、SY02-10、SY05-23、SY05-24、SY05-25、SY07-08、SY08-01、SY08-02，
  **+4,516 段 / +367,525 汉字**（原语料 +10.0%）。语料现为 **49,038 段 / 81 个工程 / 4,035,712 汉字**。
  每行新增 `seg="blank"`（切分口径）与 `tier="B"`（未经人工评级）。`SY02-11` 无可用 `.tex`，仍缺。
- **路径误伤**（`tools/scrub_publish.py`）：脱敏正则曾把 TeX 换行 `\\` 当成 UNC 路径吞掉/替换成 `<本地路径>`；
  改为保 TeX 元字符、只认真盘符/UNC 路径，并回填 **36 个 `.tex` 的 99 处**与语料 22 行（重算 `para_id`）。
- **数学语义**（`01_corpus_zh/_tex_clean.py`）：`UNWRAP` 不再吞 `\mathrm` / `\operatorname` / `\hbox`。
- **宏展开**（`01_corpus_zh/_append_pkg.py`）：`unwrap_all()` 改用配平展开器，不再用裸正则（会把 `\mathrm{e}^{2\pi i}` 剥成 `e}^{2\pi i}`）。
- **可移植**：`_append_pkg.py` / `_build_corpus_v3.py` 里硬编码的绝对路径改为基于 `__file__`。
- **缺陷可见**（新增 `_repair_2026-11-15.py`，只加 `flags` 不改正文）：`empty_ref` 481、`layout_residue` 90、
  `orphan_number` 2,621、`meta_block` 10、`overlong` 12、`junk_trimmed` 214、`placeholder_in_math` 4、`unbalanced_math` 7。
- **统计口径**：`make_stats.py` 新增「语料覆盖」行；README / DATASHEET / QA_REPORT / `00_README.md` / 欠账台账全部回填实测值。

### 没修（已写进诚实缺陷表）

工程自定义宏未展开（7,816 段 / 21,923 处，需重跑抽取器并喂 `\newcommand` 表）；历史清洗吞掉的
`\mathbb/\mathcal` 参数无法还原；近重复未对新增 10 包重算（1,418 仍是下界）；EN↔ZH 对齐仍缺。

## v1.4.0 — 2026-11-15

新增 Elliott 2016 年西北大学博士论文《几何朗兰兹对应的规范场论面向》（228 页）的**全本重译注本**，
并**撤下 2026-11-12 的初版（v1）**，以 v2 覆盖同名路径。

### 为什么撤下 v1

v1 的框架（章节、定理体例、页锚、术语表）可用，但逐句对照底本后，问题在句层而不是个别笔误：

- **数学内容译反**：p.16 把 BPS 界的「下界」写成「上界」，与紧邻的不等式 $E\ge\alpha|m|$ 自相矛盾；
  p.95 费曼积分漏负号；p.82 两因子次序对调；p.180「the second supercharge」误作「第二个直和项」；
  p.202 主从颠倒。
- **术语不一**：root datum 作「根系数据」（与 root system 混）、holonomy 作「完整」、
  divergence 作「全导数」、vanishing/nearby cycles 作「消没闭链／邻近闭链」。
- **公式图表错位**：表 1.2 以「版面」为由删去 $SL(mn;\mathbb{C})/C_m$、$Spin(8n)$、$Spin(8n+4)$ 数行；
  p.94、p.135 交换图错位；p.159 图漏一条竖箭头。
- **页锚错乱**：第 1 章缺 p.10/p.11/p.25/p.26/p.47 五处；附录自 p.216 起整体滞后一页。
- **漏译**：**定理 B.8（p.228）整条未译**、致谢全节未译、p.37–38 与 p.163 各缺一整句。

读 v1 有可能读到与原文相反的数学陈述，因此整包撤下，不做「打补丁式」维护。

### v2 交付（`08_source_code/SY02-11_Elliott2016几何朗兰兹对应的规范场论面向/`、`03_translations_meta/SY02-11/`）

- **113 页**译注本（1,236,270 B）：正文汉字 71,675 → 73,927（+3%），前置件 575 → 1,215（补译摘要与致谢）。
- **206 个页锚**（第 1 章 46 / 第 1 部分 49 / 第 2 部分 84 / 第 3 部分 13 / 附录 14），逐页连续、无缺无重。
- **补全漏译**：定理 B.8、致谢全节、p.37–38 奇异支撑句、p.163 截面配对句。
- **参考文献 137 条重建**（136 个唯一 key；原书自身两条同用 `[BD04]`，照录），修折行碎条、连字、分解音标 30 余处。
- **四幅 Feynman 图矢量化**：按底本 PDF 的矢量路径逐条转写为 TikZ（宽图 9.5 pt 虚线、小图 1.8 pt 点线），
  PDF 内无位图；同时输出 600 dpi PNG 供 Markdown 阅读。
- **nLab 校定**：15 个词条、16 条对照译注（geometric Langlands correspondence、singular support、
  factorization algebra、BV formalism、twistor space、L∞-algebra 等）。
- **术语统一 16 组**：root datum→根数据、超 Yang–Mills、全纯–拓扑扭转、proper→真（proper）、
  on-shell→在壳（on-shell）等，并入 `00_术语表.md`。
- 原文疑似笔误 10 条一律**照录另加译注**，不擅改正文；清单见 `08_校订说明.md` 第八节。

## v1.3.0 — 2026-11-15

新增 Witten《镜像对称、Hitchin 方程与朗兰兹对偶》（arXiv:0802.0999v1，15 页）的**译注本**。
这是本库第一次把「nLab 词条级批注」与「篇末框架梳理」同时作为一级交付物：正文一字未增，
全部补充移入 46 条【译注】与一篇《译者后记》。

### 新工程（`08_source_code/SY05-25_镜像对称、Hitchin 方程与朗兰兹对偶/`、`03_translations_meta/SY05-25/`）
- **41 页**译注本（ctexart + xelatex）：正文六节语义级忠实翻译，节号、公式号（(2.1)–(5.1)）、
  脚注位置与 22 条参考文献一律保留原位；作者原注 5 条以【原注】标记，与【译注 x.y】混排、全文连续编号。
- **译注 46 条**（§1 6、§2 8、§3 8、§4 7、§5 7、§6 10）：来源分三级 A（原文/经典原始文献）、
  B（nLab，60 余个候选 slug 先探 HTTP 200 再取 `Last revised`，与 A 级交叉核对，标访问日）、
  I（纯由原文推得，标「译者按」）。404 词条（`SYZ conjecture`、`hyperkähler quotient` 等）一律不引。
- **《译者后记》**（5 节 + 图 2）：一句话论点、六节依赖链、三条主线、文献导读、读法建议；
  图 2 用 TikZ 画出 §1→§5 的推导依赖与 §6 对 §1 的「模空间应读作叠」反向修正。
- **两张图均以 TikZ 重排**：图 1 是原文第 4 页以文字排出的 Hitchin 纤维化示意图（caption 注明「内容未变」），
  图 2 为译者新增依赖图（caption 注明「为译者所加」）。
- **附录 A** 术语表 38 条 + 记号表 18 条；**附录 B** 46 条译注汇编——两者与正文脚注同源，
  由 `工程文件/tools/gen_tables.py` 从 `notes_data.py`（译注单一真源）一次生成。
- `工程文件/`：README（可复现工作流）、SPEC（体例与判据）、精选片段 10 条、校核记录（编译 7 处修复、
  逐页目视、46=46=46 数据一致性）、`译注清单.tsv`、tools 三脚本（`notes_data.py`、`gen_tables.py`、
  `build.ps1` 一键重建）。
- 排印处理：前置页 roman ii–iv 与正文 arabic 1–37 分离、目录点线统一；日志只剩 Underfull，
  **无 Overfull / 无缺字 / 无 undefined / 无 TeX 错误**；PDF 元数据（标题、作者、主题、关键词）已写入。
- `_PDF清单.tsv` 增一行（成品 41 页 / 489,675 B；原本 15 页 / 216,398 B，直链待 Release 上传后回填）。

## v1.2.0 — 2026-11-14

新增一部**课程讲义**（Yao YUAN 2020 年春季课程《Langlands Program: an introduction》，23 讲、原稿 198 页）的
中文**译注本**工程。与前几部不同，本工程的主交付不是「重译」，而是按 v2.0 施工标准对既有译本做**逐页复核校订**，
并把「学生向译注」做成可追溯的独立附录——这是本库第一次把「译注」当作一级交付物来管理。

### 新工程（`08_source_code/SY02-09_Langlands纲领导论/`、`03_translations_meta/SY02-09/`）
- **162 页**译注本（ElegantBook 重排），覆盖原稿 198/198 页、23 讲 87 节、299 个原书编号对象。
- 23 讲**逐页对照**原稿校订（正文可信、公式一律回页面图像逐符号核对）：A 类数学错误改正文、B 类漏译补回、
  C 类语言病灶清理；原稿笔误不改正文而留痕。
- **译注 144 条**（126 条 `\znote` 带来源 + 18 条 `\znoteplain` 仅上下文推断），**原稿笔误登记 147 条**；
  正文脚注 + 附录 A《译注来源总表》+ 附录 B《原书笔误与存疑登记》，两份附录由脚本从 `notes/notes_*.tsv` 全量重生成。
- 来源分级按 v2.0 §2.5：A 级本讲参考文献教材/原始论文、B 级 nLab / Stacks / MathWorld / DLMF、I 级本库译注；
  无依据者只能写「译者按（上下文推断，无外部依据）」。nLab 覆盖不到的概念建 `nlab/alt/` 来源库（37 份），
  并对两批共 110 条译注做了 URL/修订日期/内容真实性抽查（PASS 98 / WARN 11 / FAIL 1，全部整改）。
- 08 带完整可编译源码（26 个 tex + 62 幅原书矢量图 + 224 项术语表 + 前两轮的 `audit/` 记录）。
- `工程文件/`：通读笔记（v2.0 §1.0）、疑点清单 TSV（8 列 9 条全结案）、施工细则、分章报告 23 份、
  译注登记 TSV 23 份、来源库与抽查记录、15 个流水线脚本（nLab 抓取/索引、单章编译自检、附录生成、审计）。
- 另附**读书笔记**（`成品/Langlands纲领导论_读书笔记.pdf`，7 页）：三句话主旨、四层地图、三条主线、
  核心概念对照表、十个最容易读错的地方、阅读路线——由 `work/build_note.py` 从 md 经 pandoc + ctexart 排版。
- **原本随仓**：`08_source_code/SY02-09_Langlands纲领导论/原本/`（讲义合并本，23 讲 / 198 页 / 4,936,559 B，
  附 SHA256 与「原稿页 = 印刷页」的页映射说明）。这是本库唯一随仓保存的原文——作者公开授课、未正式出版，
  经仓主指定发布，供逐页对照与读者核对；`_PDF清单.tsv` 增一行指向该文件（成品列仍留空，本库不发布书籍/讲义类成品）。

### 术语与参考资源入库（新增 `07_refs_nlab/`、`01_corpus_zh/terms_frozen_SY02-09.tsv`）
- **术语定案表** `01_corpus_zh/terms_frozen_SY02-09.tsv`（223 条）：英文 / 中文 / 等级 A·B·I / 依据 / 首次出现讲次 /
  本轮校订备注。这是第一份**冻结**术语表——23 讲逐页校订后的统一口径（含「分圆域」替换「圆分域」、
  「射有限」替换「投有限」、「零调消解」「忠实平坦有限表现」「阿基米德素位」「范映射」等定名），
  以后翻几何 Langlands 的文献先查它，避免同词异译。
- **术语基升级**：`termbase.jsonl` 中 `pkg=SY02-09` 的 215 行由 `candidate` 升为 `confirmed`，
  并补 `level`（A/B/I）/`source`（依据，nLab URL 或教材版次章节）/`lecture`（首次出现讲次）三字段。
- **nLab 参考资料库** `07_refs_nlab/`：`pages/` 120 条 nLab 条目摘要（抓 Instiki 源码，保留 `last_revised`，
  可直接写进译注来源行）；`alt/` 37 份替代来源卡（nLab 只有存根/404 的经典数论与表示论概念改引 A 级教材、
  MathWorld、Stacks）+ 书目底账 `_BIB.tsv` + 110 条来源真实性抽查记录；`tools/` 抓取与索引脚本 + 示例清单，
  并附 `README.md` 说明「先查缓存 → 补抓 → 降级到 A 级教材 → 才写译者按」的取源顺序与红线。
### 语料（`01_corpus_zh/`）
- 新增入库脚本 `_append_pkg_sy0209.py` + 预清洗器 `_tex_clean_sy0209.py`：本工程用 `\sourcepage{原书页}`
  做页锚点（无段落 id），故按页锚点切段；`\znote/\znoteplain/\idx/\lref/\refitem` 等自有宏在清洗阶段剥除。
- **+384 段**（含公式 366；带页锚点 381），全库 → **44,522 段 / 唯一 42,955 / 含公式 38,393（86.23%）/ 汉字 3,668,359**；
  `with_page_orig` 3,642 → **4,023**。验收 `leftover_macro = 0`、精确重复 0。
- 术语基 1,412 → **1,627**（+215，`status=candidate`，去重键 `(foreign, zh)`）。
- 本轮两个术语裁决记录在案：**cyclotomic field → 分圆域**（旧译「圆分域」11 处，库内无先例，按学界惯例定案）；
  **profinite → 射有限**（旧译「投有限」12 处，库内有先例，直接沿用）。

### 过程层（`02_trajectories/`）
- `02_trajectories/SY02-09_精选片段.md`：10 条判定链，含四条「改正文 vs 只加注」的分界判例
  （算得清的错误改正文、缺假设不可替作者判的只加注）、t-结构左右正合的「定义无对错」裁决、
  nLab 张冠李戴（polarization）、书目不许加版次，以及跨章符号 grep 一致性。

## v1.1.0 — 2026-11-14

新增一部**正式出版专著**的完整工程（Clay 数学研究所《Dirichlet Branes and Mirror Symmetry》中文校订版），
首次用「原书页锚点」做语料增量入库，并把整书对照校订的流水线沉淀成 playbook 与一条精选轨迹。
本版基于 v1.0.1 的**瘦身后**仓库（03 不再重复存源码、会话分片与成品 PDF 在 Release 附件）。

### 新工程（`08_source_code/SY01-23_Dirichlet 膜与镜像对称（Clay 专著）/`、`03_translations_meta/SY01-23/`）
- 530 页译本，逐段对照 Clay 官方 PDF（697 页，底本与成品 SHA256 均已钉死）校订：**正文 201 处 + 术语/记号 90 处 + 文献 18 条**。
- 08 带完整可编译源码（250 文件：main.tex / book-adapt.sty / elegantbook.cls / 15 个章节 tex / 222 张矢量图 / references.bib 476 条 / index-zh.tex）。
- `工程文件/`：BRIEF、README、编译说明、build.ps1、校对标准、14 个流水线脚本、`reports/`（11 份分章日志 + 术语审计 + 落地回查 201/201 + 完整性审计）、`deliverable/`（校订报告 + 术语对照表）。
- 按「正式出版书籍底本不发布成品 PDF」的约定，本工程**不含成品 PDF**；03 只留 `投稿信息.md`（瘦身后规矩）。

### 语料（`01_corpus_zh/`）
- 新增入库脚本 `_append_pkg.py` + 宏展开器 `_tex_clean.py`：按 `\SourceParagraph{id}{PDF页}` 锚点切段，**一段一个 `page_orig`**。
- **+2,952 段**（含公式 2,559；带页锚点 2,950），全库 → **44,138 段 / 唯一 42,570 / 含公式 38,027（86.15%）/ 汉字 3,625,154**；`with_page_orig` 692 → **3,642**。
- 验收 `leftover_macro = 0`（`\BookCite/\BookEqRef/\BookSectionRef/\BookChapterRef/\BookRef/\footnote` 全部转纯文本）、孤立花括号 0、精确重复 0。
- 术语基 657 → **1,412**（+755，`status=candidate`，去重键 `(foreign, zh)`）。
- `DEDUP_REPORT.md` / `QA_REPORT.md` 更新为增量后实测值；SY01-23 未跑 MinHash，近重复 1,418 记为下界。

### 过程层（`04_playbook/`、`02_trajectories/`）
- 新增 `04_playbook/07_整书对照校订流水线.md`（11 节：锚点对齐 → 分块 → 判据 → 断言式批改 → 落地回查 → 完整性审计 → 合并重建 → 交付装配，附七个坑），必读顺序表加第 6、7 行。
- `04_playbook/tools/review_pipeline/` 收录本次 14 个脚本；`02_trajectories/SY01-23_精选片段.md` 记录 11 条判定链。
- 轨迹 401 → **402 条**（新增 score 9.90）；`traj_stats.json` 同步（扫描 1007 / 候选 952 / 入选 402 / 均分 7.32）。

### 统计
- `make_stats.py --write` 刷新 README：**91 部（77 部带完整源码）/ 5,819 文件 294.1 MB / 1,505 tex + 2,115 图 / 41 部成品 PDF 50.8 MB（Release）/ 语料 44,138 段 / 术语 1,412 / 轨迹 402**。

## v1.0.1 — 2026-11-13

语料质检版：v1.0.0 的语料虽然保住了公式，但仍混有大量**排版残渣**（目录条目、环境名表、
`figures/*.png` 图注、`0pt 3.2pt` 尺寸残渣）和**近似重复段**。本版逐段清洗并标注。

### 语料（`01_corpus_zh/`）
- **残渣清理**：440 段在第一个目录/图注标记处**截断保留正文前缀**（不再整段丢弃），
  230 段清洗后确认为空壳而删除。旧版被误杀的真内容（如 SY01-02 的译校说明）已回补。
- **新增 `near_dup_of`**：MinHash-LSH（4 band × 2 row，Jaccard ≥ 0.8）标注 **1,421 段**近重复，保留不删。
- **新增 `zh_chars`** 字段；全库汉字 **3,354,874** 字。
- **公式内占位符修复** 4 段（`<本地路径>` → `\text{[略]}`）、**定界符修复** 5 段（孤立 `$`）。
- 最终：**41,186 段 / 唯一 39,619 / 含公式 35,468（86.1%）**；新增 `QA_REPORT.md` 质检报告。
- 重建脚本升级为 `_build_corpus_v3.py`（v2 已删）。

### 仓库瘦身（2026-11-14）
- **消除 03/08 重复**：删除 `03_translations_meta/<编号>/源码/` 与 `工程文件/`（1511 + 518 个文件，约 45 MB）——
  与 `08_source_code/` 逐字节相同；源码与工程文档统一以 08 为唯一来源。两份 03 独有小文件（`smoke/o.txt`、`_tmp_rules.txt`）
  已转存到 08 对应目录并加 `-from-03meta` 后缀。
- **大体积资产外置**：`06_sessions_raw/` 的 4 个 `.zst` 分片（145 MB）与 41 部成品 PDF（50.8 MB）移到
  Release `v1.0.1` 附件；仓库内保留 `06_sessions_raw/_分片说明.md`、`_attachments.json` 与
  `03_translations_meta/_PDF清单.tsv`（含附件直链）。
- **历史重写**：被移出的文件已从全部历史清除并 force push；检出体积 524 MB → 约 280 MB，clone 不再下载这些二进制。
- **文档同步**：README、`00_README.md`、`DATASHEET.md`、`_PDF清单.tsv`、`MANIFEST.json` 全部重算。

### 说明
- 本版**历史已压缩为单提交**：v1.0.0 中带残渣的语料不再能从本仓库历 clone 到，避免下游误用。

## v1.0.0 — 2026-11-13

首个语义化版本。基于外部评审（19 条建议）逐条核实后的修复版。

### 语料（`01_corpus_zh/`）
- **公式保真重建**：旧版把 `\Sigma`、`\mathcal{N}`、`\oplus` 等剥成 ASCII 骨架（41,202 段中 **0 段**含公式），
  现改为保留 `$...$` / `\[...\]` / 数学环境原样：**41,416 段，其中 35,562 段（85.9%）含公式**。
- 新增 `para_id`（内容哈希，全库唯一）、`page_orig`（694 段有原书页码）、`env`（定理/定义/证明/正文）、
  `tier`（工程评级）、`dup_of`/`dup_pkg`（重复指向首个出现）。
- 术语基升级为 `termbase.jsonl`（657 条，含 `lang` 标注：en 104 / ja 325 / other 228；冲突 0），
  取代旧的 `terms.tsv`（`source_kind` 列语义错位、混入日文词条）。
- 新增 `DEDUP_REPORT.md`：重复 1,594 段（3.85%），保留并标注而非静默删除。

### 工程源码（`08_source_code/`）
- 新增该目录：86 个工程、`工程文件/` + `源码/`（LaTeX + figures），**不含任何 PDF**。
- **补回 342 张插图**（`figures/` 下的 PDF 型图此前被「跳过所有 PDF」的规则误伤），
  现仅 2 张在库中缺失（`SY01-08/fig1-1.png`、`SY05-08/fig_p012_a.png`，源目录亦无）。
- 04 与 08 的 1337 对同名 `.tex` 在 blob 级 100% 一致（已验），约定「08 为源、03 为派生」。

### 卫生
- 删除 25 个空文件（`chunks/_src/*_pages.txt`、`work/dbg_style.txt` 等中间产物）。
- 脱敏改为 **JSON 感知**（`tools/scrub_publish.py`）：先解析再清洗字符串值。
  此次 **13 个文件 / 65,701 处** 替换。顺带修复了上一版脱敏**写坏 JSON** 的问题
  （`zh_paragraphs.jsonl` 446 行、`traj_selected.jsonl` 全部行解析失败），两文件已从源数据重建。
- 不发布原文：删除 `originals` 分支（原文 PDF 不再出现在任何分支）。

### 校验
- 新增 `.gitattributes`（`* text=auto eol=lf`，二进制例外）。
- `MANIFEST.json` 改为按 **提交后的 blob 重算**（`build_manifest.py`），
  并在仓库内提供 `tools/check_manifest.py` 单进程复算（6818 文件 10 秒，0 不一致）。
- `_build_summary.json` 由脚本生成，不再手写（旧值声明 6256 文件，实际 6818）。

### 文档
- `README.md` 规模表改为 `make_stats.py` 自动生成（统计块 `<!-- STATS:BEGIN/END -->`），
  修掉「86 部译注本 / 20 部只有成品 PDF」等漂移表述（实际 86 个工程、14 部无源码）。
- **许可表述调整**：语料、轨迹、会话为 CC BY 4.0，并明确写明**欢迎用于模型预训练 / 微调 / 蒸馏**；
  译文与工程文档为 CC BY-NC-SA 4.0。去掉了旧版「默认不用于任何模型训练」的表述。
- 新增本文件与 `DATASHEET.md`。
- `06_sessions_raw/_分片说明.md` 重写为 UTF-8（旧文件是乱码），补**整包 sha256**、双平台拼接命令、解压与读取说明。

### 计数（v1.0.0）
- 仓库：6,819 文件 / 479.7 MB（按 blob 计，不含 `MANIFEST.json` 自身）
- 工程 86 部（72 部有完整源码）· `.tex` 1,338 · 插图 1,845 · 成品 PDF 41 部 50.8 MB
- 语料 41,416 段 · 术语 657 条 · 轨迹 400 条 · 会话分片 4 片 144.6 MB

## v0.x — 2026-11 之前

非版本化的迭代期：83 部译注本（10,303 页）陆续完成，工程源码、元数据、术语表、轨迹与会话逐步入库；
无 tag、无 CHANGELOG，`MANIFEST` 与 README 数字存在漂移（本版已修）。
