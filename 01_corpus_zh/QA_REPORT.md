# 语料质检报告（v3 + 2026-11-14 增量）

| 指标 | 数值 |
|---|---|
| 总段数 | 44138 |
| 含公式 | 38027（86.15%） |
| 唯一 para_id | 42571 |
| 精确重复（保留 + 标 `dup_of`） | 1567 |
| 近重复（Jaccard≥0.8，保留 + 标 `near_dup_of`） | 1418（未对新增包重算，为下界） |
| 带原书页锚点 `page_orig` | 3642 |
| 汉字总数 | 3625154 |
| 包（pkg）数 | 70 |

> 上表是 2026-11-14 追加 SY01-23 之后的**实测值**；下文 v3 一节保留首次生成时的记录。

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
