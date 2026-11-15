# 数译 · 中文数学译注本语料与轨迹数据集

本目录是 `数译`（mathtranslations）工程的对外数据包，包含四类资产：

| 目录 | 内容 | 说明 |
|---|---|---|
| `01_corpus_zh/` | 中文段落语料 `zh_paragraphs.jsonl`（49,038 段，81 个工程有正文）、术语表 `termbase.jsonl`（1,627 条） | 从 92 部译本中 81 部的 TeX 源码抽出的正文段落（已去 LaTeX 命令）与人工冻结术语 |
| `02_trajectories/` | 精选 agent 任务轨迹 402 条 | 任务意图 → 关键动作（工具调用序列）→ 验证证据 → 结论，四段式 |
| `03_translations_meta/` | 92 部译本的元数据、投稿信息与术语索引；预印本类成品 PDF 清单见 `_PDF清单.tsv` | 源码与工程文档统一放在 `08_source_code/`，本目录不重复保存；**仓库内不保存任何成品 PDF**，预印本类成品走 Release 外链，图书类成品按 `COMPLIANCE.md` §4 申请 |
| `04_playbook/` | 翻译总纲、施工纪律、文献引进标准、待完成清单、环境改造 | 这套工程「怎么干」的规范 |
| `05_seminar_witten/` | 威腾（Witten）文章研讨班产出与文献索引 | 研讨班任务书、errata、notes、one-pager、253 篇索引 |
| `06_sessions_raw/` | 全量会话语料（脱敏、zst 压缩） | 118,278 条消息 / 2.61 亿字符 ≈ 1.7 亿 token；工具轨迹 17 万条。145 MB 分片已移到 Release `v1.0.1` 附件，仓库只留抽取脚本与分片说明 |
| `07_originals/` | 原文获取指引与书目信息（**不含原文 PDF**） | 本库不发布、不托管、不给原文直链；arXiv 原文请到 arXiv 按编号获取，图书请走出版社/图书馆 |

## 大体积资产：Release 附件

为了让 `git clone` 不必下载近 900 MB 历史，以下二进制资产不再进入 Git 仓库，改为
[Release `v1.0.1`](https://atomgit.com/lzxSUSUY/mathtranslate/releases/tag/v1.0.1) 的附件：

| 资产 | 大小 | 说明 |
|---|---|---|
| `06_sessions_raw/` 的 4 个 `.zst` 分片 | 145 MB | 拼接与校验见 `06_sessions_raw/_分片说明.md` |
| `03_translations_meta/<编号>/成品/` 的 41 部预印本成品 PDF | 50.8 MB | 仅限 arXiv / 开放许可底本；逐部直链见 `03_translations_meta/_PDF清单.tsv` |

Git 仓库内保留全部源码、元数据、语料、轨迹与工程文档；需要整包离线数据时，先 clone 仓库再按清单下载附件即可。

## 合规

四级发布模型与 9 条红线见 [`COMPLIANCE.md`](./COMPLIANCE.md)：L1 自产全公开、L2 译文公开受限、L3 成品仅外链、L4 原本/扫描件/影印件禁入。每部底本的权利状态、成品去向登记在 [`RELEASE_REGISTER.csv`](./RELEASE_REGISTER.csv)；提交前的自动检查由 `tools/check_compliance.py` 完成。2026-11-16 的独立评估与整改记录见 [`ASSESSMENT_2026-11-16.md`](./ASSESSMENT_2026-11-16.md)。

## 数据来源与生成方式

- 语料抽取：`01_corpus_zh/_build_corpus.py`
- 轨迹筛选：`02_trajectories/_curate_traj.py`
- 会话抽取：`06_sessions_raw/_extract_sessions.py`

## 脱敏

所有文本在打包时统一脱敏：邮箱、口令、SSH 私钥/公钥、GitHub 令牌等一律替换为 `[已脱敏]`。
`MANIFEST.json` 记录每个文件的字节数与 sha256 前缀，可用于校验完整性。

## 许可

**分两层**，完整条款见仓库根 [`LICENSE`](./LICENSE) 与 [`COMPLIANCE.md`](./COMPLIANCE.md)。

- **自产层 → CC BY 4.0**：元数据、术语表、标注、轨迹、方法文档、工程文档、脚本、站点；署名即可，欢迎训练、蒸馏与商用。
- **译文层 → 保留权利**：译文、译注、语料正文、译文源码是第三方作品的演绎作品，仅限非商业学术研读，不得整本转载或用于商业训练；其他用途须先取得底本权利人授权。
- 原文版权归原作者与出版方，本库不发布原文、不授予原文权利；权利方通知后 48 小时内撤下。

## 训练数据卫生

- **可用于训练的只有自产层**（元数据、术语、方法、轨迹、站点）。译文层不授予训练权利。
- 本工程自采语料在入库前按 `04_playbook/01_数学文献翻译纪律.md` §2.5.9 执行来源黑名单
  （知乎、百度百科/知道、CSDN、简书、公众号、视频课笔记等一律不看、不引、不缓存），黑名单内容不得进入语料。
  这是**内部质检纪律，不是对使用者的限制**。
