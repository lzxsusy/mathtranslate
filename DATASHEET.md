# Dataset Card · 数译中文数学译注语料

> 版本 `v1.0.0`（2026-11-13）· 维护者：超对称梦想家（chaoduicheng）
> 仓库：<https://atomgit.com/lzxSUSUY/mathtranslate> · 镜像：<https://gitee.com/supersymmetry-dream-home/shuyi>

## 1. 这是什么

一批**中文数学译注本**（镜像对称、几何朗兰兹、量子场论、辛几何与拓扑等方向）连同它们的
**LaTeX 工程源码**、**段落级中文语料**、**术语基**、**AI 辅助翻译的过程轨迹**与**会话原始流**。

三层资产：

| 层 | 目录 | 说明 |
|---|---|---|
| 权威层 | `08_source_code/` | 89 部工程的 LaTeX 源码 + 工程文档（其中 72 部带完整可编译源码） |
| 衍生层 | `01_corpus_zh/`、`02_trajectories/`、`06_sessions_raw/`、`03_translations_meta/` | 语料、轨迹、会话、元数据与术语 |
| 过程层 | `04_playbook/`、`05_seminar_witten/` | 翻译纪律、审校报告、研讨班组织资料 |

## 2. 来源与授权

- 底本分两类：**arXiv 预印本**（41 部，可公开引用与对照）与**正式出版书籍**（45 部，日文/英文专著、Springer/AMS 丛书）。
- 发布物**不含任何原文**（不发布原文 PDF）；只发布译文、工程源码、元数据与自建语料。
- 译文与工程文档：CC BY-NC-SA 4.0。语料、轨迹、会话：CC BY 4.0。
- 逐部底本信息（书名、作者、出版年、arXiv 号）见 `03_translations_meta/<编号>/投稿信息.md`。

## 3. 语料规格（`01_corpus_zh/zh_paragraphs.jsonl`）

| 字段 | 类型 | 含义 |
|---|---|---|
| `pkg` | str | 工程编号（如 `SY01-08`） |
| `file` | str | 来源 `.tex` 相对路径 |
| `para` | int | 段序 |
| `para_id` | str | 内容 sha1 前 16 位，**全库唯一稳定**，可做去重键 / 引用键 / 增量更新的锚点 |
| `page_orig` | int\|null | 原书页码（解析 TeX 里 `% ===== PDF p.NNN (原书 p.N) =====`；仅 89 个工程带此标记，覆盖 694 段） |
| `env` | str | `text` / `theorem` / `definition` / `proof` / `remark` / `example` |
| `tier` | str | 工程评级 A/B/C |
| `text` | str | **保真文本**：`$...$`、`\[...\]`、`equation/align` 等数学环境原样保留 |
| `dup_of` / `dup_pkg` | str\|null | 与前面某段文本完全重复时指向首次出现（重复段保留，便于下游按需过滤） |

统计：**41,186 段 / 89 个工程 / 唯一 39,619（96.2%）/ 含公式 35,468（86.1%）/ 汉字 3,354,874 字**。
另标 `near_dup_of`（MinHash-LSH，Jaccard≥0.8，1,421 段，保留不删）。
`flags` 记录质检动作：`junk_trimmed`（440 段切掉目录/图注残渣）、`placeholder_in_math`（4 段）、`unbalanced_math`（5 段）。
去重策略与理由见 `01_corpus_zh/DEDUP_REPORT.md`。

## 4. 清洗管线（精确到脚本）

| 步骤 | 脚本 | 说明 |
|---|---|---|
| 段落抽取 | `01_corpus_zh/_build_corpus_v3.py` | 去 LaTeX 命令但**保留公式**；只删 `\cite/\ref/\label` 等引用类参数；unwrap 仅格式命令 |
| 术语抽取 | 同上 | 三种来源：`术语表_*.csv`、`deliverable/*.md`、`.tex` 里的术语对照；合并成 `termbase.jsonl` |
| 脱敏 | `tools/scrub_publish.py` | **JSON 感知**：先 `json.loads` 再清洗字符串值，最后重新序列化（早版直接在字节上跑正则会写坏 JSON） |
| 清单 | `build_manifest.py` + `tools/check_manifest.py` | 从 `HEAD:<path>` 的 blob 计算字节数与 sha256 前 16 位；`check_manifest.py` 单进程流式复算（6818 文件约 10 秒） |
| 统计 | `make_stats.py` | 生成 README 的规模表，杜绝手写数字漂移 |
| 会话抽取 | `06_sessions_raw/_extract_sessions.py` | 读 `session.v4.jsonl.zstd`，按 `callId` 配对 tool/call 与 tool/result |

## 5. 已知缺陷（诚实清单）

| 缺陷 | 现状 | 影响 |
|---|---|---|
| 2 张插图在库中缺失（`SY01-08/fig1-1.png`、`SY05-08/fig_p012_a.png`） | 已补 342 张，这两张本机与各源目录均无 | 这两部整书编译会缺这 2 张图，其余可编 |
| 14 部工程只有成品 PDF、无 LaTeX 源码 | `SY01-18 / 01-19 / 02-08 / 03-02 / 03-16 / 03-17 / 03-18 / 03-20 / 03-21 / 05-10 / 05-19 / 05-20 / 05-21 / 05-22` | 无法从源码重建，只能读成品 |
| 语料重复 3.85% | 保留并标注 `dup_of`，不静默删除 | 训练前建议按 `para_id` 去重 |
| 页码覆盖仅 694 段 | 仅 89 个工程的 TeX 带页码标记 | 其余段落无原书页码锚点 |
| 术语基 657 条，覆盖 89 个工程 | 其余 89 个工程未产出机器可读术语表 | 术语一致性只能局部校验 |
| 原文对齐（EN↔ZH）尚未发布 | 需原文与分页 OCR 文本，本次未做 | 尚无 `align.jsonl` |
| 会话包未做第三方审计 | 只有自述数字与脱敏脚本 | 建议使用者自行抽样审计 |
| 03 与 08 有 1337 个同名 `.tex` | blob 级 100% 一致（已验），但属人工同步 | 约定「08 为源、03 为派生」 |

## 6. 推荐用途

- **模型预训练 / 微调 / 蒸馏**：`01_corpus_zh`（中文数学文本 + 保真 LaTeX 公式）、`02_trajectories`（工具调用示范）、`06_sessions_raw`（长会话与 agent 轨迹）。
- **学术研究**：术语一致性研究、数学文本抽取、翻译流水线复现（`04_playbook` + `08_source_code`）。
- **教学与精读**：`03_translations_meta/*/成品/` 的 41 部成品 PDF；`site/index.html` 是离线可开的检索站点。
- **Agent 训练**：`02_trajectories` 的四段式（意图→动作→证据→结论 + 评分 6.07–9.99）+ `06_sessions_raw` 的未截断 I/O。

我们不主张对使用方式设额外限制：**把这份语料用于训练是它的目标之一**。唯一要求是遵守第 2 节的署名与非商业条款（译文层）。

## 7. 引用

```bibtex
@misc{shuyi2026,
  author       = {超对称梦想家 (chaoduicheng)},
  title        = {数译：中文数学译注文献库（v1.0.0）},
  year         = {2026},
  howpublished = {\url{https://atomgit.com/lzxSUSUY/mathtranslate}},
  note         = {83 部译注 / 89 个工程 / 41{,}186 段中文数学语料 / 400 条 agent 轨迹}
}
```

版本记录见 `CHANGELOG.md`；每版语料可凭 tag 与 `MANIFEST.json` 复现。
