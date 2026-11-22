# 数译 · 中文数学译注本语料与轨迹数据集

本目录是 `数译`（mathtranslations）工程的对外数据包：**122 部**数学文献的中文译注本、它们的 LaTeX 工程源码、
段落级中文语料、术语与记号规范、资料卡、自然语言↔Lean 4 对齐卡，以及 AI 辅助翻译的过程轨迹与会话原始流。
所有数字取自 `_meta/stats.json`（由 `python make_stats.py --write` 生成），定义与退役口径见 `_meta/口径.md`。

**本包的重心**：从「给出可读的译本」转到「**资料卡 + 自然语言与形式语言的对齐**」。
规范层在 `01_corpus_zh/数语规范/`，卡片层在 `datasets/`，路线见 `04_playbook/15_形式化与自然语言对齐_2026-11.md`。

| 目录 | 内容 | 说明 |
|---|---|---|
| `01_corpus_zh/` | 中文段落语料 `zh_paragraphs.jsonl`（**49,322 段**，唯一 47,756；**95 个工程**有正文）、术语表 `termbase.jsonl`（**1,820 条**）、**`数语规范/`**（术语 1,847 条 / 记号 76 条 / 冲突 76 组 / 宏 550 个，含三份规范：术语与记号、中文语体、对齐卡） | 从 95 部译本的 109 部 LaTeX 源码中抽出正文段落（已去 LaTeX 命令、保留公式）与人工冻结术语；数语规范由 `tools/build_norm.py` 从 termbase 与两张冻结表合并生成，`--check` 作提交闸门 |
| `02_trajectories/` | 精选 agent 任务轨迹 **402 条** | 任务意图 → 关键动作（工具调用序列）→ 验证证据 → 结论，四段式 |
| `03_translations_meta/` | **122 部**译本的元数据、投稿信息与术语索引；预印本类成品 PDF 清单见 `_PDF清单.tsv` | 源码与工程文档统一放在 `08_source_code/`，本目录不重复保存；**本目录不保存任何成品 PDF**：预印本类走 Release 外链，图书类按 `COMPLIANCE.md` §4 申请，公开讲义类按 R3 随仓公开（成品放在 `08_source_code/<编号>/成品/`，如 SY01-24、SY07-09） |
| `04_playbook/` | 翻译总纲、施工纪律（v2.1）、文献引进标准、待完成清单、环境改造、**形式化对齐路线** | 这套工程「怎么干」的规范 |
| `05_seminar_witten/` | 威腾（Witten）文章研讨班产出与文献索引 | 研讨班任务书、errata、notes、one-pager、253 篇索引 |
| `06_sessions_raw/` | 全量会话语料（脱敏、zst 压缩） | **4 个分片 / 144.6 MB**（Release 附件），仓库只留抽取脚本与分片说明；消息条数与字符数属当日快照，重构后不再在文档里手写 |
| `07_originals/` | 原文获取指引与书目信息（**不含原文 PDF**） | 本库不发布、不托管、不给原文直链；arXiv 原文请到 arXiv 按编号获取，图书请走出版社/图书馆 |
| `08_source_code/` | **122 部**译注工程的 LaTeX 源码与工程文档 | 109 部带 `源码/*.tex`；13 部无源码（`SY01-18/01-19/02-08/02-11/03-02/03-16/03-17/03-18/03-21/05-19/05-20/05-21/05-22`） |
| `datasets/` | 可训练数据集：**21 个集 / 1,095 张资料卡**——`leanstmt/`（39 条中文↔Lean 4 对齐卡）、`glc/` 154、`functoriality/` 83、`kshms/` 83、`gw06/` 75、`siebert/` 75、`seidel/` 70、`kw06/` 67、`dmod/` 61、`pathintegral/` 50、`geoq/` 48、`bdh/` 43、`csw/` 40、`gtgl15/` 40、`sy0117/` 36、`cdm14/` 35、`gaits04/` 23、`ggl19/` 12，另有 `math/`、`parallel/`、`deepread/`、`highlights/`、`traces/`、`kg/`、`bench/` 等工艺集 | 规则见 `datasets/README.md`；权利分 `self / arxiv / book / rewritten` **四层**，`book` 派生只进 `datasets/_internal/`，永不发布 |
| `MEMORANDUM_01_论证精读与语料生产.md` | **强制前置读本**：精读与语料生产的科学规程（七条铁律、七级证据、三席三轮协议、unit 八字段、八道闸门、十条红线） | 任何人/智能体开工前必须通读；与任务书冲突时以它为准；网页版 `site/memo.html` |
| `PLAYBOOK_02_AMS量子场与弦习题推理链_v1.md` | **任务规程**：AMS《量子场与弦》习题课——角色、L0–L5 提示阶梯、卡点冻结、C1–C8 归因、`exercise.jsonl` schema、每周 90 分钟时间盒 | 只用于习题课线；上游是 MEMORANDUM-01；网页版 `site/playbook-ams.html` |
| `09_thinking/` | AI 思考链的筛选、审计与上传：L0 raw → L1 候选卡 → L2 人工批准链 → L3 审计报告；硬纪律 R1–R12 | 2026-11-20 新建；工具 `tools/thinking_audit.py`；只上传人批准的链，raw reasoning 不入库 |
| `10_gmn_series/` | GMN 系列（Gaiotto–Moore–Neitzke：穿墙、BPS 态、WKB 谱网络、红外代数）的资料卡、阅读报告、术语与索引 | 2026-11-21 新建；译文源码在 `08_source_code/SY01-27_…`；GMW 两篇待地基文献齐备后启动 |
| `ASSESSMENT_2026-11-20_产出作用.md` | 按“有没有用”审计 33 天产出：页数、可验证判断、成本-作用对照 | **历史快照**（数字保留当日口径，不再回改）；与 `ASSESSMENT_2026-11-20_AI消耗.md`、`04_playbook/15_形式化与自然语言对齐_2026-11.md` 配套；现行统计以 `_meta/stats.json` 为准 |

## 大体积资产：Release 附件

为了让 `git clone` 不必下载近 900 MB 历史，以下二进制资产不再进入 Git 仓库，改为
[Release `v1.0.1`](https://atomgit.com/lzxSUSUY/mathtranslate/releases/tag/v1.0.1) 的附件：

| 资产 | 大小 | 说明 |
|---|---|---|
| `06_sessions_raw/` 的 4 个 `.zst` 分片 | 144.6 MB | 拼接与校验见 `06_sessions_raw/_分片说明.md` |
| `03_translations_meta/<编号>/成品/` 的 41 部预印本成品 PDF | 50.8 MB | 仅限 arXiv / 开放许可底本；逐部直链见 `03_translations_meta/_PDF清单.tsv` |

Git 仓库内保留全部源码、元数据、语料、轨迹与工程文档（11,739 个跟踪文件 / 406.6 MB）；需要整包离线数据时，先 clone 仓库再按清单下载附件即可。

## 合规

四级发布模型与 9 条红线见 [`COMPLIANCE.md`](./COMPLIANCE.md)：L1 自产全公开、L2 译文公开受限、L3 成品仅外链、L4 原本/扫描件/影印件禁入。每部底本的权利状态、成品去向登记在 [`RELEASE_REGISTER.csv`](./RELEASE_REGISTER.csv)（**116 行**，逐部有台账）；提交前的自动检查由 `tools/check_compliance.py` 与 `tools/check_numbers.py` 完成。2026-11-16 的独立评估与整改记录见 [`ASSESSMENT_2026-11-16.md`](./ASSESSMENT_2026-11-16.md)（历史快照）。

## 数据来源与生成方式

| 产物 | 脚本 | 说明 |
|---|---|---|
| 中文段落语料 | `01_corpus_zh/_build_corpus.py`（及 `_build_corpus_v3.py`、`_append_pkg*.py`） | 去 LaTeX 命令、保留公式、按 `para_id` 去重 |
| 术语与记号规范 | `tools/build_norm.py` | 合并 termbase + 冻结表 → `数语规范/` 四张表；`--check` 作闸门 |
| 精选轨迹 | `02_trajectories/_curate_traj.py` | 按评分与证据完整度筛选 |
| 会话抽取 | `06_sessions_raw/_extract_sessions.py` | 读 `session.v4.jsonl.zstd`，按 `callId` 配对 |
| 统计与站点 | `make_stats.py`、`tools/build_site.py` | 统计写 `_meta/stats.json`，站点只从统计与台账取数，不手写数字 |
| 清单 | `build_manifest.py`、`tools/check_manifest.py` | 从 `HEAD` blob 算字节数与 sha256 前缀 |

## 脱敏

所有文本在打包时统一脱敏：邮箱、口令、SSH 私钥/公钥、GitHub 令牌等一律替换为 `[已脱敏]`。
`MANIFEST.json` 记录每个文件的字节数与 sha256 前缀，可用于校验完整性。

## 许可

**分两层**，完整条款见仓库根 [`LICENSE`](./LICENSE) 与 [`COMPLIANCE.md`](./COMPLIANCE.md)。

- **自产层 → CC BY 4.0**：元数据、术语表、标注、轨迹、方法文档、工程文档、脚本、站点、资料卡、对齐卡；署名即可，欢迎训练、蒸馏与商用。
- **译文层 → 本库不另设限制**：译文、译注、语料正文、译文源码是第三方作品的演绎作品；本库不代原作者授权，也不附加“仅非商业”“禁止训练”一类限制——检索、研究、教学、模型训练、蒸馏都可以用。要出版发行请自行核实底本权利。
- 原文版权归原作者与出版方，本库不发布原文、不授予原文权利；权利方通知后 48 小时内撤下。
- 口径沿革见 `LICENSE` §7。

## 训练数据卫生

- **自产层可直接用于训练**（元数据、术语、方法、轨迹、站点、资料卡、对齐卡）；**译文与语料同样不设训练限制**，可用，但底本原文权利仍归原作者，出版发行须自行核实。
- 干净子集：`python tools/make_train_subset.py` 生成 `01_corpus_zh/zh_train.jsonl.gz`（实测 **44,372 段 / 366 万汉字 / 86% 含公式**；源 49,322 段保留不动，两个口径并存）。
- 本工程自采语料在入库前按 `04_playbook/01_数学文献翻译纪律.md` §2.5.9 执行来源黑名单
  （知乎、百度百科/知道、CSDN、简书、公众号、视频课笔记等一律不看、不引、不缓存），黑名单内容不得进入语料。
  这是**内部质检纪律，不是对使用者的限制**。
