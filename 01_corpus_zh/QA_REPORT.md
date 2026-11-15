# 语料质检报告（v3 + 增量）

| 指标 | 数值（2026-11-15 复核） |
|---|---|
| 总段数 | 49038 |
| 含公式 | 42153（85.96%） |
| 唯一 para_id | 47471 |
| 精确重复（保留 + 标 `dup_of`） | 1567 |
| 近重复（Jaccard≥0.8，保留 + 标 `near_dup_of`） | 1418（未对新增包重算，为下界） |
| 带原书页锚点 `page_orig` | 4023 |
| 汉字总数 | 4035712 |
| 包（pkg）数 | 81 |

> 上表由 `zh_paragraphs_stats.json` 实测值回填（`_build_corpus_v3.py` 写 stats 时同步刷新本表）。
> 更早的两版数字（44,138 / 38,027 / 42,571 / 3,625,154 / 70 与 44,522 / 42,955 / 3,668,359 / 71）
> 分别对应 SY01-23 增量前与 2026-11-14 增量后，保留在下方各节的历史记录里，不再作为对外口径。

## 2026-11-15 复核与修复（第三方评审后的整改）

评审报告见仓库根 `AUDIT_2026-11-15.md` / 站点 `site/audit-2026-11-15.html`。本次改了四处管道 + 一次数据修复：

1. **路径误伤**（`tools/scrub_publish.py`）：脱敏正则曾把 TeX 换行 `\\` 当成 UNC 路径删掉/替换成 `<本地路径>`。
   改为先保 TeX 元字符（`_keep_tex()`）、只认真正的盘符/UNC 路径；并回填已损坏的 36 个 `.tex`（99 处，全部是矩阵与对齐换行）
   与语料 22 行（并重算 `para_id`）。
2. **数学语义**（`01_corpus_zh/_tex_clean.py`）：`UNWRAP` 不再吞 `\mathrm` / `\operatorname` / `\hbox`；
   新增 `transnote` 等内容类命令进白名单。
3. **宏展开**（`01_corpus_zh/_append_pkg.py`）：`unwrap_all()` 改用配平展开器，不再用裸正则
   （裸正则会把 `\mathrm{e}^{2\pi i}` 剥成 `e}^{2\pi i}`）。
4. **可移植**（`_append_pkg.py` / `_build_corpus_v3.py`）：硬编码的绝对路径改成基于 `__file__`。
5. **补包**（新增 `_append_pkg_generic.py`）：把此前有译文却没进语料的 10 个工程补入库，
   **+4,516 段 / +367,525 汉字**（`seg="blank"` 标明切分口径，`tier="B"` 标明未经人工评级）；
   `SY02-11` 无可用 `.tex`，仍缺。
6. **缺陷可见**（新增 `_repair_2026-11-15.py`）：只加 `flags`、不改正文，把已知问题标出来供下游过滤 ——
   `empty_ref` 481、`layout_residue` 90、`orphan_number` 2,621、`meta_block` 10、`overlong` 12、
   `junk_trimmed` 214、`placeholder_in_math` 4、`unbalanced_math` 7。

仍未修（需要重跑抽取器或有版权归属问题，见评审报告 P1/P2）：工程自定义宏（`\R`、`\C`、`\Z` 等 7,816 段）
未展开；`\mathbb/\mathcal` 被历史清洗吞掉的段落无法还原；近重复未对新增 10 包重算；EN↔ZH 对齐仍缺。

## 历史记录：2026-11-14 增量后（44,522 段 / 71 包）

## 增量入库（2026-11-14，SY01-23《Dirichlet 膜与镜像对称》）

- 入口：`01_corpus_zh/_append_pkg.py`（切段器 `_tex_clean.py`），数据源是发布仓 `08_source_code/SY01-23_…/源码`。
- 切段单位 = `\SourceParagraph{id}{原书PDF页}` 锚点，一段带一个 `page_orig`；新增 **2952 段**（含公式 2559，带页锚点 2950）。
- 清洗：宏展开后再落文本——`\BookCite{ref393,ref461}`→`[393, 461]`、`\BookEqRef`→`(2.1)`、`\BookSectionRef`→`第 3.1 节`、`\BookChapterRef`→`第 2 章`、`\BookRef`→显示串、`\footnote{…}`→`（…）`、`\emph` 类只留内容；`\BookStatementNumber`/`\label`/`\BookImage` 等连同参数删除；`figure`/`table` 环境整块丢弃。
- 验收：`leftover_macro = 0`（无 `\Book*`、`\cite`、`\ref` 残留）、孤立花括号 0、精确重复 0；`para_id = sha1(text)[:16]`。
- 术语：`glossary.csv`（762 行）合并进 `termbase.jsonl`，新增 **755** 条（`status=candidate`，`pkg=SY01-23`，去重键 `(foreign, zh)`）。
- 边界：本包的 `near_dup_of` 未计算（未跑 MinHash）；`with_page_orig` 的大幅提升来自本包（其余 69 包基本以空行切段）。

## 本次清掉的排版残渣（230 段，v3 阶段）


判定规则：出现 `tocsection`/`figures/*.png`/环境名表；或汉字 ≤6 且整段几乎是数字与点线；或整段无汉字。

抽样（最多 20 条）：

- `SY01-03` p1：plain
- `SY01-06` p12：引言 引言引言
- `SY01-08` p1：编者介绍
- `SY01-08` p1：底本要项
- `SY01-08` p19：N=2 共形场论
- `SY01-08` p49：镜像对称的今后
- `SY01-08` p1：初出一览
- `SY01-08` p1：译校说明
- `SY01-08` p8：前言
- `SY01-09` p2：[2] #1m o #2 ##1 ##2（##2）
- `SY01-09` p1：参考文献
- `SY01-09` p1：参考文献
- `SY01-09` p1：参考文献
- `SY01-09` p1：参考文献
- `SY01-09` p1：参考文献
- `SY01-09` p1：参考文献
- `SY01-09` p1：编者说明
- `SY01-10` p2：
- `SY01-17` p2：前言 前言前言
- `SY02-01` p1：术语译名对照表

## 公式修复

- 占位符落进公式内部（`$<本地路径>` 之类）：修复 **4** 段，改用 `\text{[略]}`
- 公式定界符不配平：修复 **5** 段（去掉孤立 `$`），并在段落上标 `flags:["unbalanced_math"]`

## 字段变化（相对 v2）

- 新增 `zh_chars`（汉字数，可用于按语言纯度过滤或配比采样）
- 新增 `near_dup_of`（近重复指向首个出现，**不删除**）
- 新增 `flags`（`placeholder_in_math` / `unbalanced_math`，仅在有修复时出现）
