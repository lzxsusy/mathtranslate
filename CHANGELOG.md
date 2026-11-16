# CHANGELOG

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
