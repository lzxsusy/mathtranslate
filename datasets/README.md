# 数译数据集（datasets/）

> 本目录把「译本」升级为「可训练、可评测、可追溯的学术翻译数据集」。
> 规则自 2026-11-16 起生效；与 [../COMPLIANCE.md](../COMPLIANCE.md) 冲突时以 COMPLIANCE 为准。

## 0. 一句话

一段原文、一段译文、一条「为什么这么译」的理由，三样齐了才算数据；缺了理由，就只是文本。

**2026-11-16 方向调整**：训练价值的主体从「翻译对齐」转向「数学与推理」——模型缺的不是译法，而是数学理解、证明能力和**中文推理链**。因此：

- `math/`（数学推理条目）成为主力：命题、自足上下文、证明步骤、缺口、难度、校验状态；
- `parallel/` 保留但降为术语与表达的小样本，不再扩量；
- `deepread/`、`highlights/` 继续作为 `math/` 的素材池；
- `traces/` 记录「怎么想、怎么验」，不是「怎么译」。

设计依据见 [math/README.md](math/README.md)（北大 AI4Math 的命题级检索、层级展开、形式化反馈三条经验）。

## 1. 数据集类型

| 目录 | 内容 | 一条记录 = 什么 | 单条上限 |
|---|---|---|---|
| `math/` | 定义/定理/断言 + 自足上下文 + 证明步骤 + 依赖 + 校验状态 | 一个可独立检验的数学单元（中文优先） | 陈述 4,000 字、证明 12,000 字 |
| `parallel/` | 原文片段 ↔ 译文片段 ↔ 译法理由 | 一个句群/公式块的对齐单元 | 原文 600 字、译文 600 字 |
| `deepread/` | 精读卡：命题、证明骨架、补步、易错点、前置知识 | 一个可独立复述的数学单元 | 正文 4,000 字 |
| `highlights/` | 高光标注：哪段论述精彩、哪段证明难、难在哪、怎么破 | 一处「值得单独讲」的位置 | 正文 1,500 字 |
| `traces/` | 事件级工作流：读→写→编译→报错→改→验 | 一次可重放的完整对话流 | 事件 500 条 |
| `kg/` | 概念/定理/证明/人物/文献节点与带证据的边 | 一个节点或一条边 | 正文 500 字 |
| `bench/` | 带评分细则的 held-out 评测题 | 一道题 | 题目 800 字 |
| `encyclopedia/` | 按概念词条组织的自足数学单元：定义+定理+完整证明+可算例子+物理联系+坑 | 一个可独立阅读的词条（JSON） | 正文 20,000 字 |
| `geoq/` | 单章资料卡：概念卡 + 例子卡 + 框架地图 + 使用说明 + 生产工作流 | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `pathintegral/` | 单章资料卡（第 2 章路径积分）：概念卡 + 例子卡 + 框架地图 + 使用说明 + 生产工作流 | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `kw06/` | 单篇论文资料卡（Kapustin–Witten 2006）：概念卡 + 推导卡 + 骨架图 + 渲染 Markdown | 一张可独立使用的卡（JSON） | 单卡 3,000 字 |
| `csw/` | 单篇论文资料卡（Witten 1989，Chern–Simons / Jones 多项式）：31 张概念卡 + 9 张例子卡 + 依赖图 + 生产工作流 | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `glc/` | 整本讲义资料卡（陈麟《几何 Langlands 讲义》，16 章）：154 张概念卡，逐卡经外部核验（`verification.jsonl` 记对齐结论与核验页面） | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `seidel/` | 专著资料卡（Seidel《Fukaya categories and Picard–Lefschetz theory》）：32 张概念卡 + 8 张推导卡 + 30 张校订卡（初版错译→改译→理由），三轨 A/B/C | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `siebert/` | 讲义资料卡（Siebert《镜像对称》讲义译本裁切卡，2019 年秋课程）：概念卡 + 推导卡 + 勘误卡，七轨 A–F + O | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `dmod/` | 整本讲义资料卡（Miličić《D-模的代数理论讲义》，5 章 35 节 283 条）：61 张卡（59 概念 + 2 例子），九轨 O–H，逐卡对齐校订批注本源码行号并在 nLab / Stacks Project 找依据（`verification.jsonl` 记 `alignment` 与核验页面） | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `functoriality/` | 单篇论文资料卡（Abouzaid–Bottman《范畴辛几何中的函子性》，arXiv:2210.11159v1）：56 张概念卡 + 14 张推导卡 + 13 张勘误卡，四轨 A/B/C/D；每卡带英文原文印刷页锚，公式逐字对中译本源码校验；其中 42 张交换图以 tikz-cd 源码存于卡内、渲染 PNG 在 `md/diagrams/` | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `gtgl15/` | 单篇论文资料卡（Witten《More On Gauge Theory And Geometric Langlands》，arXiv:1506.04293v3，79 页，与 SY03-20 校订译注版同批）：30 张概念卡 + 10 张推导卡，六轨 A（Hitchin 几何与谱曲线）/B（对偶环面与 T-对偶）/C（膜、线算符与本征膜）/D（'t Hooft 算符与赫克修正）/E（行列式线丛与本征值）/O（总览）；每卡带 arXiv 印刷页锚（印刷页 = PDF 页 − 1） | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `cdm14/` | 单篇论文资料卡（Gaitsgory–Rozenblyum《晶体与 D-模》，arXiv:1111.2087v4，65 页，与 SY02-12 译注本同批）：27 张概念卡 + 8 张推导卡，八轨 A（de Rham 预栈）/B（左/右晶体与 Kashiwara）/C（下降与归纳函子）/D（$t$-结构）/E（与 D-模的关系）/F（扭化）/G（扭晶体）/O（总览）；每卡带 arXiv 印刷页锚（印刷页 = PDF 页）与 A/B/C 来源标注 | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `gaits04/` | 单章资料卡（Gaitsgory《几何朗兰兹的非正式导论》，《朗兰兹纲领导论》第 12 章，13 页，与 SY02-13 译注本同批）：23 张概念卡，六轨 O/A/B/C/D/E；**每卡携带批注**（易错预警 / 含糊点拨 / 背景直觉，共 23 条）；每卡带原书页锚与中译本源码行号锚（`ch12_sec*.tex:A-B`）；全部 `reviewed` + `source-only` | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `sy0117/` | 整本专著资料卡（Bocklandt《同调镜像对称性浅入门》中译二轮校订本，CUP 2021，LMS Student Texts 99）：20 张概念卡 + 12 张勘误卡；**每张概念卡至少 1 条批注**（易错预警 / 含糊点拨 / 背景直觉）；锚到中译本源码行号（`chapters/chNN.tex:A-B`）；全部 `reviewed` + `source-only`，不发布 PDF | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `gw06/` | 单篇论文资料卡（Gukov–Witten《规范理论、分歧与几何朗兰兹纲领》中译校订本，arXiv:hep-th/0612073v2，160 页）：57 张概念卡 + 18 张勘误卡，覆盖 §1–§6 与附录 A；**每卡 3 条批注**（易错预警 / 含糊点拨 / 背景直觉）；锚到中译本源码行号（`源码/sections/sNN-*.tex:A-B`），印刷页 = PDF 页 − 1；全部 `reviewed` + `source-only`，不发布 PDF | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `bdh/` | 整本专著资料卡（Beilinson–Drinfeld《Hitchin 可积系统的量子化与 Hecke 特征层》中译校订本，作者自印 To appear，386 页，与 SY02-14 同批）：29 张概念卡 + 14 张勘误卡，覆盖 §0–§10 与参考文献；**每张概念卡至少 2 条批注**（易错预警 / 含糊点拨 / 背景直觉）；锚到中译本源码行号（`源码/chapters/chNN.tex:A-B`），`pages` = `pdf_pages`（本书 PDF 页 = 印刷页，偏移 0）；全部 `reviewed` + `source-only`，不发布 PDF | 一张可独立使用的卡（JSON，附渲染版 Markdown） | 单卡 3,000 字 |
| `leanstmt/` | 自然语言 ↔ Lean 陈述对照语料：39 张陈述卡（21 certified + 18 gap；Witten 2015 ×12 + Witten 2008 ×14 + GNO 1977 ×13），每卡含原文页/式锚、规范化中英陈述、Lean 4 语句、mathlib 依赖、假设、盲验回译、`verification.jsonl` 机器可复算；`lean/` 存源码快照，`tools/` 可一键复跑 | 一条可编译、可复算的陈述 | 单卡 3,000 字 |

`bench/` 与训练集严格隔离：出题时不得使用 `parallel/`、`deepread/` 中已出现的同一段落。

## 2. 权利分层（写进每条记录）

- `rights: "self"` — 自产（导读、术语裁决、精读卡、图谱边、评测题、中文证明与结构化）。可 CC BY 4.0，可商用训练。数学事实本身不受版权保护；`math/` 记录的版权只涉及其中的中文表述与结构。
- `rights: "arxiv:<id>"` — 原文来自 arXiv。**逐篇**核对 arXiv 许可（`https://arxiv.org/abs/<id>` 页脚）；只有 CC BY / CC0 的原文片段可随数据集公开，其余只存 `src_ref` 链接与不超过 300 字的引用。
- `rights: "book"` — 在版图书（含扫描件、出版社 PDF）。**只进 `_internal/`，不发布、不进公开数据集、不随权重发布**；片段引用 ≤ 200 字，且只用于本机训练与人工研读。
- `rights: "rewritten"` — `encyclopedia/` 的词条、`geoq/` 与 `pathintegral/` 的资料卡：用自己的话重写的事实与结构，不复制原书表达与图；可 CC BY 4.0。单处引文 ≤ 60 字并注出处，累计不超过单条 10%。

发布前用 `tools/ds_publish.py --check` 过滤：`rights: "book"` 与未确认许可的 `arxiv:*` 记录一律不出现在公开目录。

## 3. 目录结构

```
datasets/
├── README.md                  # 本文件
├── schema/                    # 数据集的 JSON Schema
├── encyclopedia/              # 词条库（entries/<category>/<slug>.json + taxonomy.md）
├── geoq/                      # 单章资料卡（cards/ + md/ + map.png/svg + workflow/ + tools/）
├── pathintegral/              # 单章资料卡：第 2 章路径积分（同 geoq 结构）
├── kw06/                      # 单篇论文资料卡：Kapustin–Witten 2006（概念卡 + 推导卡）
├── seidel/                    # 专著资料卡：Seidel《Fukaya categories and P–L theory》（概念/推导/校订）
├── siebert/                   # 讲义资料卡：Siebert《镜像对称》（概念/推导/勘误，七轨 A–F+O）
├── sy0117/                    # 整本专著资料卡：Bocklandt《同调镜像对称性浅入门》中译二轮校订本（20 概念 + 12 勘误，每卡带批注）
├── gw06/                      # 单篇论文资料卡：Gukov–Witten《规范理论、分歧与几何朗兰兹纲领》（57 概念 + 18 勘误，每卡 3 条批注）
├── functoriality/             # 单篇论文资料卡：Abouzaid–Bottman《范畴辛几何中的函子性》（概念/推导/勘误，四轨 A–D，42 张交换图）
├── gtgl15/                    # 单篇论文资料卡：Witten 2015《More On Gauge Theory And Geometric Langlands》（概念/推导，六轨 A–E+O）
├── leanstmt/                  # 自然语言 ↔ Lean 陈述对照语料（Witten 2015 ×12 + 2008 ×14 + GNO 1977 ×13；21 certified + 18 gap）
├── cdm14/                     # 单篇论文资料卡：Gaitsgory–Rozenblyum《晶体与 D-模》（概念/推导，八轨 A–G+O）
├── bdh/                       # 整本专著资料卡：Beilinson–Drinfeld《Hitchin 可积系统的量子化与 Hecke 特征层》（29 概念 + 14 勘误）
├── math/<pkg>.<split>.jsonl   # 数学推理条目（主力）
├── parallel/<pkg>.<split>.jsonl
├── deepread/<pkg>.<split>.jsonl
├── highlights/<pkg>.<split>.jsonl
├── traces/<pkg>.<topic>.jsonl
├── kg/<pkg>.<split>.jsonl
├── bench/<pkg>.<split>.jsonl
├── _internal/                 # book 权利，永不发布（.gitignore）
└── workflow/                  # 生产协议、提示词、审校清单
```

`<pkg>` 用 `08_source_code/` 里的工程名（如 `SY05-25`）；`<split>` 取 `train|dev|test`，`bench` 固定 `test`。

## 4. 生产协议（每类数据都走这五步）

1. **选段**：从 `08_source_code/<pkg>/源码/` 取 TeX 段落；原文取 `originals_pkg/07_originals/` 或 arXiv `/e-print/` 的 LaTeX 源，**不入库**。
2. **对齐**：句群级对齐，公式块整体对齐；跨页/跨节处标 `alignment: "block"` 并给上下文。
3. **写理由**：至少一条 `why`，说明「为什么这样断句/选词/补主语/保留语序」；术语选择必须给 `alternatives` 与取舍。
4. **自检**：`python tools/ds_lint.py datasets/` 零错误；引用行号必须存在。
5. **双人复核**：`reviewed_by` 至少两人（生产 + 审校），`status` 从 `draft` → `reviewed` → `published`。

生产提示词与审校清单一律放 `workflow/`，不散落在会话里。`math/` 的专门流程（选点、自足化、证明步骤、依赖、形式化校验）见 [math/README.md](math/README.md)。

**存量回收（2026-11-16 起）**：除了生产新单元，还要把库里已有的翻译"余料"榨出来——`tools/ds_harvest.py` 按 flags、未展开宏、悬空引用、超长/碎片段、尚无精读卡等规则给段落打分，生成 `datasets/candidates/harvest_queue.jsonl`；五级标注（L0 修正 / L1 术语裁决 / L2 精读卡 / L3 数学条目 / L4 对话流与评测）与抽检比例见 [workflow/余料回收.md](workflow/余料回收.md)。

**第一批 L0（2026-11-16）**：取队列前 50 条，44 条修正（按工程导言逐工程展开 `\R`、`\C`、`\id` 等宏，去尺寸残渣，合并空白）、3 条删除（`meta_block`）、3 条无改动；改动留档 `datasets/fixes/l0_batch01.jsonl`，语料从 49,038 段变为 49,035 段。同日补 3 张跨工程 L2 卡：`SY01-01` 谱流、`SY01-09` SYZ 启发式、`SY03-08` Chern–Simons 形式的规范变换。成本：L0 约 0.5 人时/50 条（AI 起草 + 抽检），L2 单卡 AI 起草 2–3 分钟、人工复核 8–12 分钟。


**首批 event-level trace（2026-11-16）**：`traces/KW06-04.lead.jsonl`（52 条决策流）与
`traces/KW06-04.units.jsonl`（17 条单元回执）来自 SEM-0604151 讲义工程；配套协议
[`workflow/KW06-04_讲义生产协议.md`](workflow/KW06-04_讲义生产协议.md)。这类 trace 的训练价值在
「报错 → 修法」与验收判定，不在成品文字，故保留 `error` 与 `outcome=partial` 的记录。

## 5. 质量门禁

`tools/ds_lint.py` 强制：

- `id` 全局唯一；必填字段齐全；
- 引文字数上限（见 §1）与 `rights` 一致；`book` 记录不得出现在 `_internal/` 之外；
- `src_ref` 的 arXiv 号能被 `^[a-z-]+(\.[A-Z]{2})?/\d{7}$|^\d{4}\.\d{4,5}$` 解析；
- `evidence[].file` 必须存在于仓库且行号不超过文件行数；
- 文本中不得出现本机绝对路径（`C:\Users\...`）、口令、邮箱；
- 记录不得是整章/整节全文粘贴（单条 ≤ 6,000 字，`math/` ≤ 24,000 字）；
- `math/` 的 `verification.kind` ∈ {`lean`,`human`,`none`}、`verification.status` ∈ {`checked`,`sketch`,`unchecked`}；标 `lean` 必须给 `artifact`（编译过的文件路径）。

`tools/ds_publish.py` 是发布过滤器：`book` 一律拦；`arxiv:*` 未确认 CC BY 的整条拦、只留 ≤300 字引用；`self` 需 `status=reviewed/published`。

## 6. 引用与署名

数据条目引用格式：

```
数译数据集 v0.1（2026-11-16），<pkg> <split> <id>，
https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/datasets/<...>.jsonl
```

原文权利归原作者与出版方；数学事实本身不受版权保护；数据集只主张自产部分（中文表述、译法理由、精读、证明整理、图谱、评测题）的 CC BY 4.0。

## 7. 版本

- `v0.1`（2026-11-16）：五类 schema + SY05-25 试点 + 校验器。
- `v0.2`（2026-11-16）：新增 `math/`（数学推理条目）与 `math.schema.json`，SY05-25 6 条；`parallel/` 降为术语样本；发布过滤器与门禁支持 `math/`。
- `v0.6`（2026-11-16）：新增 `encyclopedia/`（按概念组织的词条库，17 条、74 定理、50 例）与 `tools/entry_lint.py`；`datasets/README.md` 升为八类。
- `v0.7`（2026-11-16）：第一本书拆完——`encyclopedia/` 扩到 43 条、187 定理、130 例（128 complete / 59 sketch），覆盖拓扑、几何、数学物理、凝聚态、QFT。
- `v0.8`（2026-11-16）：新增 `geoq/`——李思《量子力学与几何》第 5 章「几何量子化」的 48 张资料卡（1 总览 + 27 概念 + 20 例），附框架地图、读者版总表、渲染版 Markdown 与六路并行生产协议；`lint_geoq.py` / `audit_pages.py` 0 错。
- `v0.10`（2026-11-17）：新增 `kw06/`——Kapustin–Witten 2006 的资料卡 67 张（40 概念 + 27 推导，约 100 步），
  每卡带印刷页锚、常见误解与相关卡；`lint_cards.py --strict` 0 error、`audit_pages.py` 134 条 anchor 0 issue。
- `v0.9`（2026-11-16）：新增 `pathintegral/`——同书第 2 章「路径积分形式」的 50 张资料卡（1 总览 + 29 概念 + 20 例），65 条定理、219 个证明步骤、109 个例子步骤；附五轨框架地图、读者版总表、渲染版 Markdown 与七路并行生产协议；`lint_pi.py` / `audit_pages.py` 0 错。
- `v0.11`（2026-11-19）：新增 `seidel/`——Seidel《Fukaya categories and Picard–Lefschetz theory》的 70 张资料卡（32 概念 + 8 推导 + 30 校订，2026-11-19 复核后），
  三轨 A（A∞/三角范畴）/B（Floer/Fukaya）/C（Picard–Lefschetz），每卡带印刷页锚与 nLab/原书来源；`lint_cards.py --strict` 0 error、`render_md.py` 54 卡。
- `v0.12`（2026-11-19）：新增 `siebert/`——Siebert 讲授、Van Dyke 记录《Mirror Symmetry》（2019 年秋课程讲义）中文译本《镜像对称：代数几何专题讲义》的 75 张资料卡
  （46 概念 + 14 推导 + 15 勘误），七轨 A（数值镜像）/B（叠）/C（GW 与虚技术）/D（环面几何）/E（环面退化）/F（HMS）/O（术语）；
  印刷页 7–106 覆盖 84 页，每卡带「原书 p.N」锚与 nLab / Stacks Project / 原文依据，324 条 pitfalls、61 条 gaps；
  `lint_cards.py --strict` 0 error、`index.jsonl` 75 条、`render_md.py` 75 卡。同批入库 SY01-24 中译注本（103 页，讲义类，L2 公开·受限，随仓公开）。
- `v0.13`（2026-11-19）：新增 `functoriality/`——Abouzaid–Bottman《Functoriality in categorical symplectic geometry》（arXiv:2210.11159v1，68 页）的 83 张资料卡（56 概念 + 14 推导 + 13 勘误），四轨 A（第 1–2 章 Floer/Fukaya/操作子）/B（第 3 章 拼接 Floer 与函子）/C（第 4 章 辛 (A∞,2)-范畴）/D（第 5 章 应用）；
  页码锚由英文 PDF 逐页抽文定出（35 条节→页映射），73 个推导步骤、266 条 pitfalls；`lint_cards.py --strict` 0 error、`audit_pages.py` 0 issue、`check_formulas.py` 232/232 逐字命中、`index.jsonl` 83 条、`render_md.py` 83 卡。
- `v0.14`（2026-11-19）：`functoriality/` 补 **42 张交换图**（tikz-cd，编译校验通过、PNG 渲染入 `md/diagrams/`），并把该论文的**术语表（209 条）与记号表（76 条）**冻结进 `01_corpus_zh/`（`terms_frozen_FUNCTORIALITY.tsv`、`symbols_frozen_FUNCTORIALITY.tsv`），术语基追加 190 行（`pkg=FUNCTORIALITY`）；
  术语表 209 条（A 124/B 77/I 8）、记号表 76 条（5 组）；`check_diagrams.py --png` 42/42 编译通过。
- `v0.15`（2026-11-19）：新增 `gtgl15/`——Witten《More On Gauge Theory And Geometric Langlands》（arXiv:1506.04293v3，79 页）的 40 张资料卡（30 概念 + 10 推导），六轨 A（Hitchin 几何与谱曲线）/B（对偶环面与 T-对偶）/C（膜、线算符与本征膜）/D（'t Hooft 算符与赫克修正）/E（行列式线丛与本征值）/O（总览）；每卡带 arXiv 印刷页锚（印刷页 = PDF 页 − 1）、来源定位与 pitfalls；`lint_cards.py --strict` 0 error、`index.jsonl` 40 条、`render_md.py` 40 卡；维数类断言按原文 eq (2.6) 复核（$\dim_{\mathbb C}M_H=2(g-1)\dim G$）并记入 `workflow/PRODUCTION.md` 修订记录。同批入库 SY03-20 校订译注本（77 页、57 条译注，讲义类，L2 公开·受限，随仓公开）。
- `v0.16`（2026-11-19）：**既有资料卡修复**——按独立核验结论直接修入 `kw06/`（10 张卡、22 个文本点：A 类 4 条 = *simply-laced*「单连通」误译 3 卡 6 处 + `geometric-langlands` 把 $M(G,C)$ 误作稳定 Higgs 丛；C 类 6 条 = 一般纤维/$Ξ$ 归一化/$B,C$ 族 $n_g$/lacing number 等），`glc/` 两张 Hitchin 卡互注 $d_i$ 指数 vs 次数约定（非错误）并同步 `verification.jsonl` 的 note；修后 `lint_cards.py --strict` 0 error（kw06 67 卡）、`lint_glc.py` 0 error 0 warning（glc 154 卡），index/md 全部重生成。同批：SY03-20 中文字体由 Fandol 换成 SimSun/SimHei/KaiTi（`\IfFontExistsTF` 回退链），PDF 中文与「译注｜」脚注可复制可检索（290 KB 文本、0 处 Missing character），页数仍 77。核验与修复全记录见 `08_source_code/SY03-20…/工程文件/校对记录/既有资料卡问题上报.md`。
- `v0.17`（2026-11-19）：新增 `leanstmt/`——**自然语言 ↔ Lean 陈述对照语料**（首批 Witten 2015 试点 12 条：10 `certified` + 2 `gap`）。钉死验证环境：`leanprover/lean4:v4.36.0`、mathlib `d33c49ca43873d3746194325da62640cc893c9d9`；`lake env lean` 两文件均 exit 0（Statements 0 sorry、Gaps 2 sorry），`verification.jsonl` 12 行机器可复算；`lint_cards.py --strict` 0 error 0 warning；附 `SCHEMA.md` 五条硬性纪律（不虚标/不掺沙/不越界/盲验回译/缺口照登）、`workflow/PRODUCTION.md`（含 18:31 内存耗尽事故记录与复现教训）、`ROADMAP.md`（先做/缓做/暂不做三分与下一批选题）。同批：lean 源码快照 `lean/ShuyiFormal/Witten2015/{Statements,Gaps}.lean`，工具链 `tools/{make_cards,lint_cards,build_index,render_md,check_lean}.py`。
- `v0.18`（2026-11-19）：新增 `cdm14/`——Gaitsgory–Rozenblyum《Crystals and D-modules》（arXiv:1111.2087v4，65 页）的 **35 张资料卡**（27 概念 + 8 推导），八轨 A（de Rham 预栈）/B（左/右晶体与 Kashiwara）/C（下降与归纳函子）/D（$t$-结构）/E（与 D-模的关系）/F（扭化）/G（扭晶体）/O（总览）；每卡带印刷页锚（印刷页 = PDF 页）、来源定位与 pitfalls，推导卡逐步标 locator 与 A/B/C 可信度；`lint_cards.py --strict` 0 error、`index.jsonl` 35 条、`render_md.py` 35 卡。与 SY02-12 译注本（73 页）同批，卡内术语与译注本一致。
- `v0.19`（2026-11-19）：`leanstmt/` 加入 **B 批 Witten 2008**（*Mirror Symmetry, Hitchin's Equations, and Langlands Duality*，arXiv:0802.0999v1，15 页）14 张陈述卡（5 `certified` + 9 `gap`），两批合计 **26 卡 = 15 certified + 11 gap**；轨道拆为 `W15`/`W08`，SCHEMA 升 v0.2（`source.pages` 分两批约定：2015 印刷页 = PDF 页 − 1、2008 印刷页 = PDF 页）。`lake env lean` 四个 Lean 文件全部 exit 0（Witten2015/Statements 0 sorry、Gaps 2；Witten2008/Statements 0 sorry、Gaps 9），`verification.jsonl` 26 行重跑核验；`lint_cards.py --strict` 0 error 0 warning；`lint_cards.py` 的 sorry 计数改为先剥注释（避免文档提到 sorry 被误判）。B 批的 5 条 certified 只是离散/代数影子（SL(N,ℂ) 中心 = μ_N、有限 Pontryagin 对偶的两条、非正则奇点系数伸缩律、函数空间 currying），本文主定理（Hitchin 纤维化上的镜像对称）如实记为 G06 gap。
- `v0.20`（2026-11-19）：`leanstmt/` 加入 **C 批 GNO 1977**（Goddard–Nuyts–Olive, *Gauge Theories and Magnetic Charge*, Nucl. Phys. B125 (1977) 1–28；CERN-TH-2255 影印本 38 页）13 张陈述卡（6 `certified` + 7 `gap`），三批合计 **39 卡 = 21 certified + 18 gap**；轨道加 `GNO77`，SCHEMA 升 v0.3（`source.pages` 记 CERN 影印 PDF 页、注明页脚数字不可靠故引用以节/式号为准；`source.arxiv` 放宽为 arXiv 号或 `Nucl. Phys. …` 起头）。原文为无文字层扫描件，经 `mutool` 渲图 + PIL 合成 300 dpi PDF + tesseract.js OCR（`workflow/PRODUCTION.md` §七 有完整管线）；`lake env lean` 六个 Lean 文件全部 exit 0（GNO1977/Statements 0 sorry、Gaps 7；其余不变），`verification.jsonl` **39 行**重跑核验；`lint_cards.py --strict` 0 error 0 warning。C 批 certified 只是群论/单变量骨架（权整性、式 (1.3) 的 U(1) 特例、中心元幂、有限对偶同阶、式 (1.6) 有限群双对偶、Weyl 反射 p↦−p 不变），GNO 的主定理（磁权 = H^∨ 的权）如实记为 G02 gap。
- `v0.21`（2026-11-20）：新增 `sy0117/`——Bocklandt《同调镜像对称性浅入门》中译二轮校订本的 **32 张资料卡**（20 概念 + 12 勘误）；每张概念卡携带至少 1 条批注（易错预警 / 含糊点拨 / 背景直觉），勘误卡记录二轮实际改动（原文片段→改为→依据）；锚点全部指向修订后 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/chNN.tex:A-B`；`tools/make_cards.py --check` 输出 `OK 32 cards`，全部 `reviewed` + `source-only`，不发布 PDF；同批 SY01-17 二轮校订 89 处，报告覆盖首轮原件（本地 `_v1_archive/`，不随仓）。
- `v0.22`（2026-11-20）：新增 `gw06/`——Gukov–Witten *Gauge Theory, Ramification, And The Geometric Langlands Program*（arXiv:hep-th/0612073v2，160 页）中译校订本的 **75 张资料卡**（57 概念 + 18 勘误）；每卡携带 3 条批注（易错预警 / 含糊点拨 / 背景直觉），勘误卡记录校订实际改动（原文片段→改为→依据）；锚点指向修订后 `08_source_code/SY02-06_…/源码/sections/sNN-*.tex:A-B`，`pages` 用印刷页、`pdf_pages = pages + 1`；`tools/make_cards.py --strict` 输出 `OK`（75 卡 0 error 0 warning），全部 `reviewed` + `source-only`，不发布 PDF。同批 SY02-06 全文对照校订：14 个分片、764 段、262 个编号公式，P1 4 处 / P2 34 处，新增译注 156 条（78→234），xelatex 重编译 133 页（初版 111 页）。
- `v0.23`（2026-11-21）：新增 `bdh/`——Beilinson–Drinfeld《Quantization of Hitchin's Integrable System and Hecke Eigensheaves》（作者自印 To appear，386 页）中译校订本（SY02-14）的 **43 张资料卡**（29 概念 + 14 勘误）；覆盖 §0 引论、§1 栈上的微分算子、§2 Hitchin 哈密顿量的量子化、§3 oper、§4 Pfaffian 与 c-格、§5–§6 Hecke 特征层、§7 栈上 D-模附录、§8–§10 补充材料；每张概念卡至少 2 条批注，公式逐条对中译本源码校验；`pages` = `pdf_pages`（本书 PDF 页 = 印刷页）；`make_cards.py --strict` 无 error 无 warning。
- 后续见 [CHANGELOG.md](../CHANGELOG.md)。
