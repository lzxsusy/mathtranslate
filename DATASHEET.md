# Dataset Card · 数译中文数学译注语料

> 版本 `v1.1.0`（2026-11-14；v1.0.1 瘦身版之后新增 SY01-23）· 维护者：超对称梦想家（chaoduicheng）
> 仓库：<https://atomgit.com/lzxSUSUY/mathtranslate> · 镜像：<https://gitee.com/supersymmetry-dream-home/shuyi>

## 1. 这是什么

一批**中文数学译注本**（镜像对称、几何朗兰兹、量子场论、辛几何与拓扑等方向）连同它们的
**LaTeX 工程源码**、**段落级中文语料**、**术语基**、**AI 辅助翻译的过程轨迹**与**会话原始流**。

三层资产：

| 层 | 目录 | 说明 |
|---|---|---|
| 权威层 | `08_source_code/` | 92 部工程的 LaTeX 源码 + 工程文档（其中 80 部带完整可编译源码） |
| 衍生层 | `01_corpus_zh/`、`02_trajectories/`、`06_sessions_raw/`（分片在 Release 附件）、`03_translations_meta/` | 语料、轨迹、会话、元数据与术语 |
| 过程层 | `04_playbook/`、`05_seminar_witten/` | 翻译纪律、审校报告、研讨班组织资料 |
| 参考层 | `07_refs_nlab/` | nLab 条目摘要 120 条 + 替代来源卡 37 份 + 110 条来源真实性抽查；几何 Langlands 线的术语与引文底账 |

## 2. 来源与授权

- 底本分两类：**arXiv 预印本**（42 部，可公开引用与对照）与**正式出版书籍**（45 部，日文/英文专著、Springer/AMS 丛书）。
- 发布物**不含任何原文**（不发布原文 PDF）；只发布译文、工程源码、元数据与自建语料。
- **许可：全库统一 CC BY 4.0**（署名即可）。语料、术语、标注、轨迹、会话、译文、译注、工程文档一律同一许可，
  **明确欢迎用于模型训练、微调、蒸馏、评测与商业用途**。完整条款见仓库根 [`LICENSE`](./LICENSE)。
- 原文的权利不在本许可之内：原文版权归原作者与出版方，本库不授予原文权利；权利方通知后 48 小时内撤下。
- 逐部底本信息（书名、作者、出版年、arXiv 号）见 `03_translations_meta/<编号>/投稿信息.md`。
- **口径历史**：v2.0 之前各工程模板写着「本项目语料默认不用于训练」；2026-11-14 改为「语料 CC BY 4.0 + 译文 CC BY-NC-SA 4.0」；
  **2026-11-15 起取消分层，统一 CC BY 4.0**（「非商业」与「欢迎训练」自相矛盾，第三方评审 P2 指出后由作者拍板）。
  旧表述一律作废，以本节与 `LICENSE` 为准。目录级说明见 `04_playbook/README.md`，欠账修复排期见 `04_playbook/12_质量欠账台账_v1.md`。

## 3. 语料规格（`01_corpus_zh/zh_paragraphs.jsonl`）

| 字段 | 类型 | 含义 |
|---|---|---|
| `pkg` | str | 工程编号（如 `SY01-08`） |
| `file` | str | 来源 `.tex` 相对路径 |
| `para` | int | 段序 |
| `para_id` | str | 内容 sha1 前 16 位，**全库唯一稳定**，可做去重键 / 引用键 / 增量更新的锚点 |
| `page_orig` | int\|null | 原书页码（解析 TeX 里 `% ===== PDF p.NNN (原书 p.N) =====` 或 `\SourceParagraph{id}{PDF页}`；共 3,642 段带此锚点，SY01-23 一次贡献 2,950 段） |
| `env` | str | `text` / `theorem` / `definition` / `proof` / `remark` / `example` |
| `tier` | str | 工程评级 A/B/C |
| `text` | str | **保真文本**：`$...$`、`\[...\]`、`equation/align` 等数学环境原样保留 |
| `dup_of` / `dup_pkg` | str\|null | 与前面某段文本完全重复时指向首次出现（重复段保留，便于下游按需过滤） |

统计（2026-11-15 复核后）：**49,038 段 / 92 个工程有语料 / 唯一 47,471（96.8%）/ 含公式 42,153（85.96%）/ 汉字 4,035,712 字**。
另标 `near_dup_of`（MinHash-LSH，Jaccard≥0.8，1,418 段，保留不删；SY01-23 之后未重算，为下界）。
`flags` 记录质检动作与已知缺陷（见 §5）：`junk_trimmed`、`placeholder_in_math`、`unbalanced_math`、
`empty_ref`（引用编号被吞，只剩空括号 481 段）、`layout_residue`（字号/行距残渣 90 段）、
`orphan_number`（独占一行的公式号/页码 2,621 段）、`meta_block`（目次/索引类非正文块 10 段）、
`overlong`（>3,000 汉字未切段 12 段）。
2026-11-15 增量：`_append_pkg_generic.py` 把此前漏入库的 92 个工程补进语料（+4,516 段 / +367,525 汉字，
每行带 `seg="blank"` 标明是空行切分口径、`tier="B"` 标明未人工评级）。
schema 已统一（`_normalize_schema.py`）：`flags` 恒为数组（可为空数组），`seg` 恒存在
（`"blank"`＝2026-11-15 追加的空行切分包，`""`＝旧口径），因此下游不必再判键是否存在。
去重策略与理由见 `01_corpus_zh/DEDUP_REPORT.md`，质检记录见 `01_corpus_zh/QA_REPORT.md`。

## 4. 清洗管线（精确到脚本）

| 步骤 | 脚本 | 说明 |
|---|---|---|
| 段落抽取 | `01_corpus_zh/_build_corpus_v3.py` | 去 LaTeX 命令但**保留公式**；只删 `\cite/\ref/\label` 等引用类参数；unwrap 仅格式命令 |
| 增量入库 | `01_corpus_zh/_append_pkg.py` + `_tex_clean.py` | 按 `\SourceParagraph{id}{页}` 锚点切段（一段一个 `page_orig`）；花括号平衡的宏展开器把 `\BookCite/\BookEqRef/\BookSectionRef/\BookChapterRef/\BookRef/\footnote/\emph` 转纯文本，`\Book*` 残留验收为 0 |
| 术语抽取 | 同上 | 三种来源：`术语表_*.csv`、`deliverable/*.md`、`.tex` 里的术语对照；合并成 `termbase.jsonl` |
| 脱敏 | `tools/scrub_publish.py` | **JSON 感知**：先 `json.loads` 再清洗字符串值，最后重新序列化（早版直接在字节上跑正则会写坏 JSON） |
| 清单 | `build_manifest.py` + `tools/check_manifest.py` | 从 `HEAD:<path>` 的 blob 计算字节数与 sha256 前 16 位；`check_manifest.py` 单进程流式复算（6818 文件约 10 秒） |
| 统计 | `make_stats.py` | 生成 README 的规模表，杜绝手写数字漂移 |
| 会话抽取 | `06_sessions_raw/_extract_sessions.py` | 读 `session.v4.jsonl.zstd`，按 `callId` 配对 tool/call 与 tool/result；分片从 Release `v1.0.1` 附件下载，拼接与校验见同目录 `_分片说明.md` |

## 5. 已知缺陷（诚实清单）

| 缺陷 | 现状 | 影响 |
|---|---|---|
| 2 张插图在库中缺失（`SY01-08/fig1-1.png`、`SY05-08/fig_p012_a.png`） | 已补 342 张，这两张本机与各源目录均无 | 这两部整书编译会缺这 2 张图，其余可编 |
| 14 部工程只有成品 PDF、无 LaTeX 源码 | `SY01-18 / 01-19 / 02-08 / 03-02 / 03-16 / 03-17 / 03-18 / 03-20 / 03-21 / 05-10 / 05-19 / 05-20 / 05-21 / 05-22` | 无法从源码重建，只能读成品 |
| `SY02-11` 的 `源码/` 是空目录 | 该包只有成品 PDF、`README.md` 与 12 个 `.md` 工作稿，**没有 `.tex`** | 语料无法收录此书（是唯一「有译文却进不了语料」的工程） |
| 语料重复 3.55% | 保留并标注 `dup_of`，不静默删除 | 训练前建议按 `para_id` 去重 |
| `near_dup_of` 未覆盖 SY01-23 | 该包按页锚点增量入库、未跑 MinHash | 近重复统计（1,418）是下界 |
| 2026-11-15 补入的 92 个工程未跑 MinHash | `_append_pkg_generic.py` 只追加、不重新聚类 | 近重复统计仍为下界（现覆盖 81 包） |
| 页码覆盖 4,023 段 | 仅部分工程的 TeX 带页锚点；SY01-23 用 `\SourceParagraph` 全量覆盖 | 其余段落无原书页码锚点 |
| 术语基 1,627 条，非全部工程产出 | 其余工程未产出机器可读术语表；仅 SY02-09 的 215 行带 `level/source/lecture` 并 `status=confirmed` | 其余工程术语一致性只能局部校验 |
| 只有一部有「术语定案表」 | `01_corpus_zh/terms_frozen_SY02-09.tsv`（223 条，A/B/I 分级 + 首次出现讲次） | 跨工程术语冻结仍靠人工核对 |
| 原文对齐（EN↔ZH）尚未发布 | 需原文与分页 OCR 文本，本次未做 | 尚无 `align.jsonl` |
| 会话包未做第三方审计 | 只有自述数字与脱敏脚本 | 建议使用者自行抽样审计 |
| ~~03 与 08 有 1337 个同名 `.tex`~~ | 已于 2026-11-14 删除 `03_translations_meta` 下的重复 `源码/` 与 `工程文件/`（约 45 MB，与 08 逐字节相同）；统一以 `08_source_code/` 为唯一来源 | 已消除 |

## 6. 推荐用途

- **模型预训练 / 微调 / 蒸馏**：`01_corpus_zh`（中文数学文本 + 保真 LaTeX 公式）、`02_trajectories`（工具调用示范）、`06_sessions_raw`（长会话与 agent 轨迹，Release 附件）。
- **学术研究**：术语一致性研究、数学文本抽取、翻译流水线复现（`04_playbook` + `08_source_code`）。
- **教学与精读**：Release `v1.0.1` 附件里的 42 部成品 PDF（逐部直链见 `03_translations_meta/_PDF清单.tsv`）；`site/index.html` 是离线可开的检索站点。
- **Agent 训练**：`02_trajectories` 的四段式（意图→动作→证据→结论 + 评分 6.07–9.99）+ `06_sessions_raw` 的未截断 I/O（Release 附件）。

我们不主张对使用方式设额外限制：**把这份语料用于训练、蒸馏、商用都是欢迎的**，唯一要求是署名（CC BY 4.0，见 `LICENSE`）。

## 7. 引用

```bibtex
@misc{shuyi2026,
  author       = {超对称梦想家 (chaoduicheng)},
  title        = {数译：中文数学译注文献库（v1.2.0）},
  year         = {2026},
  howpublished = {\url{https://atomgit.com/lzxSUSUY/mathtranslate}},
  note         = {93 部译注 / 44{,}522 段中文数学语料 / 1{,}627 条术语 / 120 条 nLab 参考条目 / 402 条 agent 轨迹}
}
```

版本记录见 `CHANGELOG.md`；每版语料可凭 tag 与 `MANIFEST.json` 复现。
