# 数译 · 中文数学译注文献库（数据集与语料）

> 让散落的数学资料得以保存，让数学术语形成共识。

> **施工标准（硬性）**：本库全部译注工程一律按 [`04_playbook/01_数学文献翻译纪律.md`](04_playbook/01_数学文献翻译纪律.md) **v2.0** 执行——
> 先通读后落笔（§1.0）、译注必须有来源并可追溯（§2.5）、来源黑名单与语料卫生（§2.5.9）。
> **每次开工前、每次接手别人的稿、每次交付前都要重读对应章节**；文件库总入口见 [`04_playbook/README.md`](04_playbook/README.md)。

本仓库是「数译」工程的**数据与语料发布仓**：把一批中文数学译注本、工程原件、术语资产、
AI 辅助翻译的过程轨迹、以及威腾文章研讨班的组织资料整理成**可以被别人直接拿去用**的数据。

- 译者/整理者：超对称梦想家（chaoduicheng）
- 用途：欢迎用于学术研究、教学、以及**模型训练与蒸馏**（见「使用许可」）

<!-- STATS:BEGIN -->

| 指标 | 数值 |
|---|---|
| 译注工程 | **86** 部（其中 **72** 部带完整 LaTeX 源码） |
| 仓库文件 | 6910 个 / **483.0 MB** |
| LaTeX 源文件 / 插图 | 1338 个 `.tex` / 1845 张图 |
| 成品 PDF（预印本类） | 41 部 / **50.8 MB** |
| 中文段落语料 | **41186** 段（唯一 39619），其中 **35468** 段含公式（86%）；汉字 3,354,874 字 |
| 近重复标注 | 1418 段（保留，标 `near_dup_of`） |
| 术语基 | 657 条 |
| 精选轨迹 | 400 条 |
| 原始会话分片 | 4 片 / **144.6 MB** |

<!-- STATS:END -->

## 内容结构

| 目录 | 内容 |
|---|---|
| `00_README.md` | 资产说明、脱敏说明、使用许可 |
| `MANIFEST.json` | 全部文件的路径 / 字节数 / sha256 前 16 位（提交后重算，见「校验」） |
| `01_corpus_zh/` | **中文段落语料**（保真保留 LaTeX 公式）+ 术语基 `termbase.jsonl` + 去重报告 |
| `02_trajectories/` | AI 辅助工作的精选工具调用轨迹（意图→动作→证据→结论，含评分） |
| `03_translations_meta/` | 每部书的元数据、投稿信息、术语表、交付文档；41 部预印本类另有**成品 PDF**（`<编号>/成品/`） |
| `04_playbook/` | 翻译总纲、施工纪律（v2.0）、文献引进标准、待完成清单、环境备忘 |
| `05_seminar_witten/` | 威腾（Witten）文章研讨班的索引、阅读路线、经验教训 |
| `06_sessions_raw/` | 原始对话事件流（已脱敏、zstd 压缩、按 45MB 分片） |
| `papers/WIT-1989-JONES/` | **威腾 1989 CS/Jones 论文研讨班**（第二轮解经试点）：六场研讨记录、claims/questions 数据、教材核查，以及最终交付的 21 页读书笔记（LaTeX 源码 + PDF）与一键构建工程 |
| `08_source_code/` | **每部译本的完整工程**：`工程文件/`（BRIEF、构建脚本、交付清单、术语表、校对记录、逐章报告）+ `源码/`（LaTeX 源与插图） |
| `site/` | 静态站点（`site/index.html` 双击即开，无需服务器） |

## `01_corpus_zh/`：语料的形态

`zh_paragraphs.jsonl` 每行一段，字段：

| 字段 | 含义 |
|---|---|
| `pkg` / `file` / `para` | 所属工程、源文件、段序 |
| `para_id` | 内容哈希（sha1 前 16 位），全库唯一稳定标识，便于下游去重 / 增量更新 / 引用 |
| `page_orig` | 原书页码（解析 TeX 里的 `% ===== PDF p.NNN (原书 p.N) =====` 标记；仅 14 个工程带此标记） |
| `env` | 段落所在环境：`text` / `theorem` / `definition` / `proof` / `remark` / `example` |
| `tier` | 该工程的评级 A/B/C（来自工程元数据） |
| `text` | **保真文本**：行内/行间公式原样保留 `$...$`、`\begin{equation}...\end{equation}`，不再被洗成 ASCII 骨架 |
| `dup_of` / `dup_pkg` | 若与前面某段文本完全相同，指向首个出现位置；重复段**不删除**，便于按需过滤 |

去重统计与理由见 `01_corpus_zh/DEDUP_REPORT.md`；术语基 `termbase.jsonl` 字段为
`foreign / lang(en|ja|other) / zh / status / pkg / src_format`。

## `08_source_code/`：工程源码

- 放的是**翻译工程本身**：`工程文件/` + `源码/`（LaTeX + figures）。
- 装 TeX Live / MiKTeX 后进 `源码/` 跑 `xelatex main.tex` 即可重建中文译注本；
  少数工程的根文件叫 `main.tex` 之外的名称，见该工程 `工程文件/编译说明.md`。
- **14 部当初只留了成品 PDF、没有 LaTeX 工程**（`SY01-18 / 01-19 / 02-08 / 03-02 / 03-16 / 03-17 / 03-18 / 03-20 / 03-21 / 05-10 / 05-19 / 05-20 / 05-21 / 05-22`），
  这些目录只有 `投稿信息.md`；其余 **72 部**有完整可编译源码。
- 用途：学习、研究、复用翻译流水线。

## 成品 PDF 与原文 PDF（给不使用 LaTeX 的读者）

- **成品 PDF（中文译注本）**：41 部以 arXiv 预印本为底本的译本，成品 PDF 放在 `03_translations_meta/<编号>/成品/`，点开即读；逐部清单（页数、字节、arXiv 号、文件名、下载直链）见 [`03_translations_meta/_PDF清单.tsv`](03_translations_meta/_PDF清单.tsv)。
- **原文 PDF 不发布**：本库只发布译文、工程源码、元数据与自建语料；原文（无论 arXiv 版还是出版书）请按书目信息自行获取。
- **直链怎么用**：清单里的直链形如 `https://raw.gitcode.com/lzxSUSUY/mathtranslate/blobs/<blob>/<URL 编码的文件名>`，浏览器打开即下载文件本体。AtomGit 网页的 `/raw/<分支>/<路径>` 对 PDF 只返回预览壳，所以清单给的是 blob 直链；链接失效时用 `git clone` 取文件。
- **为什么只有 41 部**：其余 45 部以正式出版的书籍（日文/英文专著、Springer 丛书等）为底本，成品 PDF 不发布；它们的元数据、工程文档与源码照常公开。

## 校验（`MANIFEST.json`）

- `MANIFEST.json` 记录每个文件的 **路径 / 字节数 / sha256 前 16 位**，在**提交后**按仓库内容重算（`.gitattributes` 已固定 `eol=lf`，因此清单位节数 = 仓库内 blob 字节数，不会因换行归一化而集体失配）。
- 自查：`python tools/check_manifest.py`（仓库自带）会重算并报告不一致项。
- 已知例外：`MANIFEST.json` 自身与 `_build_summary.json` 不计入清单（它们是生成物）。

## 分片还原

`06_sessions_raw/` 里两个 `.zst` 因超过平台单文件上限被切成多片，
拼接与校验命令写在 `06_sessions_raw/_分片说明.md`（含整包 sha256）。

## 脱敏

已发布文本资产统一过一遍脱敏（脚本 `tools/scrub_publish.py`）：

- 邮箱 → `[邮箱隐去]`
- Windows 本机绝对路径 / UNC 路径 → `<本地路径>`
- `ghp_ / github_pat_ / sk- / AKIA / ssh-ed25519` 等凭据与密钥模式 → `[已脱敏]`
- 真实密码、账号名等由 `package_upload.py` 在打包阶段剔除

`06_sessions_raw/` 的 zstd 分片是用同一套规则（含新增两类模式）重新脱敏后压缩的。

## 使用许可

- **语料与轨迹数据（`01_corpus_zh/`、`02_trajectories/`、`06_sessions_raw/`）**：**CC BY 4.0**——
  欢迎用于学术研究、教学、**模型预训练 / 微调 / 蒸馏**，请注明来源「数译（chaoduicheng）」。
- **译文与工程文档（`03_translations_meta/`、`08_source_code/`、`04_playbook/`）**：CC BY-NC-SA 4.0（署名—非商业性使用—相同方式共享）。
- **成品 PDF**：与译文同许可（CC BY-NC-SA 4.0），可直接下载阅读。
- **原文 PDF**：仅发布 41 部 arXiv 预印本的 arXiv 版本，版权归原作者，按 arXiv 许可用于对照研究；正式出版的书籍类原本不发布。原作者要求撤下时随时移除。
- **原始文献版权**归原作者与出版方所有；本仓库发布的是译文、工程源码、元数据与自建语料。

## 相关

- 站点：`site/index.html`
- 术语表：`03_translations_meta/*/工程文件/deliverable/术语表_*.csv`，汇总见 `01_corpus_zh/termbase.jsonl`
- 统计与一致性：`make_stats.py`（生成上面的统计块）、`tools/check_manifest.py`
