# Dataset Card · 数译中文数学译注语料

> 版本 `v1.3.0`（2026-11-21；统计改为从 `_meta/stats.json` 单一来源取数，新增「数语规范」与「对齐卡」两层）· 维护者：超对称梦想家（chaoduicheng）
> 仓库：<https://atomgit.com/lzxSUSUY/mathtranslate> · 镜像：<https://gitee.com/supersymmetry-dream-home/shuyi>

## 1. 这是什么

一批**中文数学译注本**（镜像对称、几何朗兰兹、量子场论、辛几何与拓扑等方向）连同它们的
**LaTeX 工程源码**、**段落级中文语料**、**术语与记号规范**、**资料卡**、**自然语言↔Lean 4 对齐卡**、
**AI 辅助翻译的过程轨迹**与**会话原始流**。

五层资产：

| 层 | 目录 | 说明 |
|---|---|---|
| 权威层 | `08_source_code/` | **118 部工程**的 LaTeX 源码 + 工程文档（其中 **105 部带 LaTeX 源码**；13 部无源码，只有成品 PDF 或译本正文） |
| 衍生层 | `01_corpus_zh/`、`02_trajectories/`、`06_sessions_raw/`（分片在 Release 附件）、`03_translations_meta/` | 语料、轨迹、会话、元数据与术语 |
| 规范层 | `01_corpus_zh/数语规范/` | **术语 1,847 条 / 记号 76 条 / 冲突 76 组 / 宏 405 个**；三份规范（术语+记号、中文语体、对齐卡） |
| 卡片层 | `datasets/` | **18 个集 / 1,034 张资料卡**；其中 `leanstmt/` 是 **39 条自然语言↔Lean 4 对齐卡**（21 certified + 18 gap） |
| 过程层 | `04_playbook/`、`05_seminar_witten/`、`10_gmn_series/` | 翻译纪律、审校报告、研讨班与 GMN 系列的研究笔记 |
| 参考层 | `07_refs_nlab/` | nLab 条目摘要 120 条 + 替代来源卡 37 份 + 110 条来源真实性抽查；几何 Langlands 线的术语与引文底账 |

**方向说明**：本库重心已从「给出可读译本」移到「**资料卡 + 自然语言与形式语言的对齐**」——
术语、记号、陈述三层都要能被机器引用、被编译器检查。规范见
[`01_corpus_zh/数语规范/`](01_corpus_zh/数语规范/README.md)，路线见
[`04_playbook/15_形式化与自然语言对齐_2026-11.md`](04_playbook/15_形式化与自然语言对齐_2026-11.md)。

## 2. 来源与授权

- 底本分布（`RELEASE_REGISTER.csv` 台账，逐部登记，合计 **118 部**）：**arXiv 预印本 49 部、讲义 25 部、图书 23 部、待复核 9 部、学位论文 6 部、在版图书 1 部、会议论文集 1 部、作者手稿（会议报告手写笔记 + 报告幻灯片；未刊）1 部、作者自印本 1 部、研讨会内部笔记 1 部、出版社排版 PDF 1 部**。
- 发布物**不含任何原文**；不发布原文 PDF，不提供原文下载直链，不托管扫描件或页面图。
- **许可分两层**（完整条款见 [`LICENSE`](./LICENSE)）：
  - **自产层**（元数据、术语、工程文档、方法、轨迹、站点、脚本、资料卡与对齐卡）：**CC BY 4.0**，署名即可，欢迎训练、研究与商用。
  - **译文层**（译文、译注、语料正文、译文源码）：第三方作品的演绎作品，本库**不代原作者授权，也不另设限制**（不标 CC BY，不写"仅非商业/禁止训练"）；检索、研究、教学、模型训练与蒸馏均可用；权利方通知后 48 小时内撤下。
- 原文的权利不在本许可之内：版权归原作者与出版方，本库不授予原文权利。
- 逐部底本信息与发布级别见 `03_translations_meta/<编号>/投稿信息.md` 与 [`RELEASE_REGISTER.csv`](./RELEASE_REGISTER.csv)。
- **口径历史**：2026-11-15 全库统一 CC BY 4.0；2026-11-16 v1.1 把译文层改为"保留权利、仅非商业"；2026-11-20 v1.2 收回该限制——
  译文层既不作授权声明，也不附加限制。以 `LICENSE` v1.2 为准。目录级说明见 `04_playbook/README.md`，欠账修复排期见 `04_playbook/12_质量欠账台账_v1.md`。

## 3. 语料规格（`01_corpus_zh/zh_paragraphs.jsonl`）

| 字段 | 类型 | 含义 |
|---|---|---|
| `pkg` | str | 工程编号（如 `SY01-08`） |
| `file` | str | 来源 `.tex` 相对路径 |
| `para` | int | 段序 |
| `para_id` | str | 内容 sha1 前 16 位，**全库唯一稳定**，可做去重键 / 引用键 / 增量更新的锚点 |
| `page_orig` | int\|null | 原书页码（解析 TeX 里 `% ===== PDF p.NNN (原书 p.N) =====` 或 `\SourceParagraph{id}{PDF页}`；共 4,023 段带此锚点，SY01-23 一次贡献 2,950 段，SY01-08 692、SY02-09 381） |
| `env` | str | `text` / `theorem` / `definition` / `proof` / `remark` / `example` |
| `tier` | str | 工程评级 A/B/C |
| `text` | str | **保真文本**：`$...$`、`\[...\]`、`equation/align` 等数学环境原样保留 |
| `dup_of` / `dup_pkg` | str\|null | 与前面某段文本完全重复时指向首次出现（重复段保留，便于下游按需过滤） |

统计（2026-11-21 实测，`python make_stats.py` 写 `_meta/stats.json`，为唯一事实源）：
**49,322 段 / 95 个工程有语料 / 唯一 47,756（96.8%）/ 含公式 42,396（86.0%）/ 汉字 4,055,500 字**。
另标 `near_dup_of`（MinHash-LSH，Jaccard≥0.8，1,418 段，保留不删；SY01-23 之后未重算，为下界）。
`flags` 记录质检动作与已知缺陷（见 §5）：`orphan_number`（独占一行的公式号/页码 2,620 段）、
`empty_ref`（引用编号被吞，只剩空括号 481 段）、`junk_trimmed`（清除残渣 212 段）、
`layout_residue`（字号/行距残渣 90 段）、`l0_fixed`（L0 修正留痕 44 段）、`overlong`（>3,000 汉字未切段 12 段）、
`meta_block`（目次/索引类非正文块 7 段）、`unbalanced_math`（7 段）、`placeholder_in_math`（4 段）。
2026-11-15 增量：`_append_pkg_generic.py` 把此前漏入库的工程补进语料
（每行带 `seg="blank"` 标明是空行切分口径、`tier="B"` 标明未人工评级）。
schema 已统一（`_normalize_schema.py`）：`flags` 恒为数组（可为空数组），`seg` 恒存在
（`"blank"`＝2026-11-15 追加的空行切分包，`""`＝旧口径），因此下游不必再判键是否存在。
去重策略与理由见 `01_corpus_zh/DEDUP_REPORT.md`，质检记录见 `01_corpus_zh/QA_REPORT.md`。

## 4. 清洗管线（精确到脚本）

| 步骤 | 脚本 | 说明 |
|---|---|---|
| 段落抽取 | `01_corpus_zh/_build_corpus_v3.py` | 去 LaTeX 命令但**保留公式**；只删 `\cite/\ref/\label` 等引用类参数；unwrap 仅格式命令 |
| 增量入库 | `01_corpus_zh/_append_pkg.py` + `_tex_clean.py` | 按 `\SourceParagraph{id}{页}` 锚点切段（一段一个 `page_orig`）；花括号平衡的宏展开器把 `\BookCite/\BookEqRef/\BookSectionRef/\BookChapterRef/\BookRef/\footnote/\emph` 转纯文本，`\Book*` 残留验收为 0 |
| 术语抽取 | 同上 | 三种来源：`术语表_*.csv`、`deliverable/*.md`、`.tex` 里的术语对照；合并成 `termbase.jsonl` |
| 术语/记号规范 | `tools/build_norm.py` | 合并 termbase + 两张冻结表 + 记号表，生成 `01_corpus_zh/数语规范/` 四张表；`--check` 作闸门 |
| 脱敏 | `tools/scrub_publish.py` | **JSON 感知**：先 `json.loads` 再清洗字符串值，最后重新序列化（早版直接在字节上跑正则会写坏 JSON） |
| 清单 | `build_manifest.py` + `tools/check_manifest.py` | 从 `HEAD:<path>` 的 blob 计算字节数与 sha256 前 16 位；`check_manifest.py` 单进程流式复算（万级文件，十几秒） |
| 统计 | `make_stats.py` | 生成 README 统计块与 `_meta/stats.json`，杜绝手写数字漂移；`--check` 作闸门 |
| 数字闸门 | `tools/check_numbers.py` | 扫描文档里的退役数字（旧工程数、旧语料段数、旧资料卡数等），防止旧口径复活 |
| 会话抽取 | `06_sessions_raw/_extract_sessions.py` | 读 `session.v4.jsonl.zstd`，按 `callId` 配对 tool/call 与 tool/result；分片从 Release `v1.0.1` 附件下载，拼接与校验见同目录 `_分片说明.md` |

## 5. 已知缺陷（诚实清单）

| 缺陷 | 现状 | 影响 |
|---|---|---|
| 2 张插图在库中缺失（`SY01-08/fig1-1.png`、`SY05-08/fig_p012_a.png`） | 已补 342 张，这两张本机与各源目录均无 | 这两部整书编译会缺这 2 张图，其余可编 |
| 13 部工程无 LaTeX 源码 | `SY01-18 / 01-19 / 02-08 / 02-11 / 03-02 / 03-16 / 03-17 / 03-18 / 03-21 / 05-19 / 05-20 / 05-21 / 05-22` | 无法从源码重建，只能读成品或语料 |
| `SY02-11` 的 `源码/` 是空目录 | 该包只有成品 PDF、`README.md` 与 12 个 `.md` 工作稿，**没有 `.tex`** | 语料无法收录此书（是唯一「有译文却进不了语料」的工程） |
| 9 部工程没有 `工程文件/` | `SY01-18 / 01-19 / 02-08 / 02-11 / 03-16 / 03-18 / 05-20 / 05-21 / 05-22` | 缺 BRIEF 与校对记录，复用流水线时无过程文档 |
| 语料重复 3.55% | 保留并标注 `dup_of`，不静默删除 | 训练前建议按 `para_id` 去重 |
| `near_dup_of` 未覆盖 SY01-23 | 该包按页锚点增量入库、未跑 MinHash | 近重复统计（1,418）是下界 |
| 2026-11-15 补入的工程未跑 MinHash | `_append_pkg_generic.py` 只追加、不重新聚类 | 近重复统计仍为下界（现覆盖 82 包） |
| 页码覆盖 4,023 段 | 仅部分工程的 TeX 带页锚点；SY01-23 用 `\SourceParagraph` 全量覆盖 | 其余段落无原书页码锚点 |
| 术语 1,847 条中 **D 级（未标级）1,411 条** | 多为抓取时自动抽出的候选，未逐条查证 | D 级不得进对齐卡；需分批提级或删除 |
| 术语冲突 76 组未裁定 | 一外多中 12（高 9）、一中多外 28、等级不一致 33、空格/连字符 3 | 跨工程合稿时仍需人工二选一 |
| 记号表只覆盖 1 部工程 | `symbols_frozen_FUNCTORIALITY.tsv` 76 条 | 其余 115 部的记号无登记，对齐卡只能依赖 `preamble.tex` |
| 宏跨工程同名不同义 405 个 | `\R` 一个名字 6 种定义，`\C` 4 种 | 跨工程搬运陈述前必须按目标导言区重映射 |
| 原文对齐（EN↔ZH）尚未发布 | 需原文与分页 OCR 文本，本次未做 | 尚无 `align.jsonl` |
| 对齐卡 39 条中 18 条是 gap | 陈述已写出，依赖或证明未完成；22 处 `sorry`（18 条声明）已记账 | 不能当「已验证定理」使用 |
| 会话包未做第三方审计 | 只有自述数字与脱敏脚本 | 建议使用者自行抽样审计 |
| ~~03 与 08 有 1337 个同名 `.tex`~~ | 已于 2026-11-14 删除 `03_translations_meta` 下的重复 `源码/` 与 `工程文件/`（约 45 MB，与 08 逐字节相同）；统一以 `08_source_code/` 为唯一来源 | 已消除 |

## 6. 推荐用途

- **模型训练（自产层）**：`04_playbook` 的方法与工作流、`02_trajectories` 的工具调用示范、`03_translations_meta` 的元数据与术语；这些是 CC BY 4.0。
- **学术研究**：术语一致性研究、数学文本抽取、翻译流水线复现（`04_playbook` + `08_source_code`）。
- **教学与精读**：译文可用于教学与精读；成品 PDF 只对 arXiv/开放许可底本以 Release 外链提供，图书底本成品需申请获取（见 `COMPLIANCE.md`）。
- **Agent 训练**：`02_trajectories` 的四段式（意图→动作→证据→结论 + 评分 6.07–9.99）+ `06_sessions_raw` 的未截断 I/O（Release 附件），属自产层。
- **形式化研究**：`datasets/leanstmt/` 的 39 条自然语言↔Lean 对照（含 21 条 certified 与盲验回译）可直接用于「中文陈述 → Lean 命题」的评测与训练；schema 与验收规则见 [`01_corpus_zh/数语规范/STYLE_FORMAL.md`](01_corpus_zh/数语规范/STYLE_FORMAL.md)。

- **模型训练（译文与语料）**：`01_corpus_zh/zh_paragraphs.jsonl`（49,322 段中文数学段落）与 `datasets/` 资料卡可直接用于训练与蒸馏，本库不设限制；出版发行请自行核实底本权利。
- **干净训练子集**：`python tools/make_train_subset.py` 会按固定口径（丢 `empty_ref` / `orphan_number` / `layout_residue` / 重复 `para_id` 等标注段、丢 <8 汉字碎片）生成 `01_corpus_zh/zh_train.jsonl.gz`——当前实测 **44,372 段 / 366 万汉字 / 86% 含公式**（源 49,322 段保留不动，两个口径并存）。

## 7. 引用

```bibtex
@misc{shuyi2026,
  author       = {超对称梦想家 (chaoduicheng)},
  title        = {数译：中文数学译注文献库（v1.3.0）},
  year         = {2026},
  howpublished = {\url{https://atomgit.com/lzxSUSUY/mathtranslate}},
  note         = {118 部译注 / 49{,}322 段中文数学语料 / 1{,}847 条术语 / 1{,}034 张资料卡 / 39 条中文↔Lean 对齐卡 / 402 条 agent 轨迹}
}
```

版本记录见 `CHANGELOG.md`；每版语料可凭 tag 与 `MANIFEST.json` 复现。统计口径定义与退役数字清单见 [`_meta/口径.md`](_meta/口径.md)。
