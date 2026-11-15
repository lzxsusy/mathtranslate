# 数译 · 中文数学译注本语料与轨迹数据集

本目录是 `数译`（mathtranslations）工程的对外数据包，包含四类资产：

| 目录 | 内容 | 说明 |
|---|---|---|
| `01_corpus_zh/` | 中文段落语料 `zh_paragraphs.jsonl`（49,038 段，92 个工程）、术语表 `termbase.jsonl`（1,627 条） | 从 92 部译本的 TeX 源码抽出的正文段落（已去 LaTeX 命令）与人工冻结术语 |
| `02_trajectories/` | 精选 agent 任务轨迹 402 条 | 任务意图 → 关键动作（工具调用序列）→ 验证证据 → 结论，四段式 |
| `03_translations_meta/` | 92 部译本的元数据、投稿信息与术语索引；预印本类成品 PDF 清单见 `_PDF清单.tsv` | 源码与工程文档统一放在 `08_source_code/`，本目录不重复保存；成品 PDF 已移到 Release 附件 |
| `04_playbook/` | 翻译总纲、施工纪律、文献引进标准、待完成清单、环境改造 | 这套工程「怎么干」的规范 |
| `05_seminar_witten/` | 威腾（Witten）文章研讨班产出与文献索引 | 研讨班任务书、errata、notes、one-pager、253 篇索引 |
| `06_sessions_raw/` | 全量会话语料（脱敏、zst 压缩） | 118,278 条消息 / 2.61 亿字符 ≈ 1.7 亿 token；工具轨迹 17 万条。145 MB 分片已移到 Release `v1.0.1` 附件，仓库只留抽取脚本与分片说明 |
| `07_originals/` | 41 部预印本类译本的 arXiv 原文 PDF（42.1 MB） | 存放在 AtomGit 的 `originals` 分支（Gitee 单仓上限，放不下）；下载直链见 `03_translations_meta/_PDF清单.tsv` |

## 大体积资产：Release 附件

为了让 `git clone` 不必下载近 900 MB 历史，以下二进制资产不再进入 Git 仓库，改为
[Release `v1.0.1`](https://atomgit.com/lzxSUSUY/mathtranslate/releases/tag/v1.0.1) 的附件：

| 资产 | 大小 | 说明 |
|---|---|---|
| `06_sessions_raw/` 的 4 个 `.zst` 分片 | 145 MB | 拼接与校验见 `06_sessions_raw/_分片说明.md` |
| `03_translations_meta/<编号>/成品/` 的 41 部成品 PDF | 50.8 MB | 逐部直链见 `03_translations_meta/_PDF清单.tsv` |

Git 仓库内保留全部源码、元数据、语料、轨迹与工程文档；需要整包离线数据时，先 clone 仓库再按清单下载附件即可。

## 数据来源与生成方式

- 语料抽取：`01_corpus_zh/_build_corpus.py`
- 轨迹筛选：`02_trajectories/_curate_traj.py`
- 会话抽取：`06_sessions_raw/_extract_sessions.py`

## 脱敏

所有文本在打包时统一脱敏：邮箱、口令、SSH 私钥/公钥、GitHub 令牌等一律替换为 `[已脱敏]`。
`MANIFEST.json` 记录每个文件的字节数与 sha256 前缀，可用于校验完整性。

## 许可

**全库统一 CC BY 4.0**（署名即可），完整条款见仓库根 [`LICENSE`](./LICENSE)。

译文、译注、术语表、语料、轨迹、会话、工程文档与研讨班产出由作者（本工程）创作，按 CC BY 4.0 授权，
**明确欢迎用于模型训练、微调、蒸馏、评测与商业用途**。原始外文文献版权归原作者与出版方，本许可不授予原文的任何权利；
正式出版的书籍类原本不随包发布，arXiv 预印本按 arXiv 各自许可使用，权利方通知后 48 小时内撤下。

## 训练数据卫生

我们**鼓励**把这份语料用于训练——不需要申请许可、不需要等我们的审计（见 `LICENSE` §1）。

上面这条是给使用者的。下面这条是给我们**自己**的：本工程自采语料在入库前按 `04_playbook/01_数学文献翻译纪律.md` §2.5.9
执行来源黑名单（知乎、百度百科/知道、CSDN、简书、公众号、视频课笔记等一律不看、不引、不缓存），
黑名单内容不得进入语料。这是**内部质检纪律，不是对使用者的限制**。
