# kb/ — 数译知识库（KB）

把仓库里的资料卡变成**可检索、可回溯、可互链**的单文件库。配套 DSH 插件 `dsh-kb`（见仓库外 `..\dsh-kb\`）。

> 一句话原则：**知识库只给带证据的线索，不给没有出处的结论。**

## 1. 三种卡源 → 一种卡

| 来源 | 位置 | 现状 |
|---|---|---|
| YAML frontmatter 单卡 | `08_source_code/*/资料卡/*.md` | 25 张（SY01-26），有 `layer/prereqs/sources/status/review` |
| JSON 结构化卡 | `datasets/*/cards/**/*.json` | 1,232 张（glc/bdh/cdm14/ggl…），带 `status` 与 `verification` |
| 五件套叙述体报告 | `08_source_code/*/资料卡/00-速览…04-术语文献勘误.md` | 18 部，**不切段**，只建 `kind=work` 书级条目（draft） |

`kb/ingest.py` 把前两种直接迁入，第三种只建书级条目——叙述体报告切段会产出「像结论但没核对」的卡，正是要避免的东西。

## 2. 流水线

```bash
PY="C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
export PYTHONIOENCODING=utf-8

"$PY" kb/ingest.py all     # 1) 三种卡源 → kb/cards/<work>.jsonl
"$PY" kb/build_kb.py       # 2) → kb/shuyi.db（cards + fts_uni + fts_tri + query_log）
"$PY" kb/q.py stats        # 3) 看现状
```

`kb/shuyi.db` 是**生成物**，不进 git（见 `.gitignore`）；重建只需两步。

### 2.1 原文层（v0.3.0 起）

插件除了资料卡，还能直接检索**底本原文抽文**。它不经过 `kb/`，由单独的脚本生成：

```bash
"$PY" tools/build_src_corpus.py            # → 01_corpus_src/src_paragraphs.jsonl + plugins/dsh-kb/data/src/*.gz
```

扫的是仓库里**已经公开**的原文文本（`08_source_code/*/工程文件/work/full.txt`、
`work/split/pNNN.txt`、`05_seminar_witten/**/source/text/pNNN.txt`），按页标记切页、
去页眉页脚与页码行、按空行切段；不新做任何原文摘录。当前 **7,644 段 / 33 个工程 / 5.2M 字符**。
同一工程若已有 `full.txt`，就不再扫它的 `split/`（同一份内容的不同切法），按文本哈希去重。

## 3. 查询

```bash
"$PY" kb/q.py search "Hecke 特征层" [--kind concept] [--work SY02-14] [--level L2] [--include-draft] [--json]
"$PY" kb/q.py card SY01-26.MS-05
"$PY" kb/q.py brief --work SY02-14        # 已入库作品：本作品卡 + 跨书线索
"$PY" kb/q.py brief --query "顶点代数 仿射 Kac-Moody"   # 未入库新书：动笔前的阅读前置包
"$PY" kb/q.py gaps --min-works 3          # 跨书锚点：多部作品都提到、却没有术语卡
"$PY" kb/q.py verify SY01-26.MS-05        # 回源：页码 / 来源 / 证据引文 / 页图路径
```

中文检索用 **trigram** 分词（SQLite ≥3.34），拉丁词用 `unicode61`；连字符 `–—‐−` 统一归一成 `-`，
所以 `Gromov–Witten`（en dash）与 `Gromov-Witten` 能互相命中。

## 4. 可信度模型（防止“知识库帮倒忙”）

| status | 含义 | 默认是否返回 |
|---|---|---|
| `verified` | ≥2 轮独立核对（其中一轮回原文页图） | ✅ |
| `checked` | 一轮核对，引文可核到原文页 | ✅ |
| `disputed` | 有未决矛盾（`rel=contradicts` 成对存在） | ✅（成对显示） |
| `draft` | 机生未复核 | ❌ 需 `--include-draft` |

- **每张卡必须带** `pages`（原文 PDF 页序）+ `sources`（A/B/C 级）+ 可选 `evidence_quote`；没有页码的卡不进入“可回溯”统计。
- 检索结果**永远**附 `caveat`：页码是启发式抽取的、只有单轮校对的、书级条目只是指针——这些都会明说。
- `query_log` 记录每次命中 → `q.py stats` 输出**风险队列**：「被查得多 × 未复核」的卡优先复核。

## 5. 配置页图根目录（可选，用于 verify）

`kb/page_roots.json`：

```json
{ "SY02-08": "C:/Users/admin/Documents/deepseek-harness/default-workspace/frenkel-loop/pages" }
```

`verify` 会在该目录下找 `pNNN.png` 并告诉你文件是否存在，方便 `read_image` 一步回源。

## 6. 已知欠账

- frontmatter 的 25 张卡目前全是 `draft`（复审后应升 `checked`）；页码从 `sources` 文本启发式抽取。
- JSON 卡的页码多数是从卡内文本（`locator: "A p.47"` 等）抽的，`caveat` 已标注「引用前回源核对」。
- 术语锚点目前只有 1 条跨 4 部作品（`hecke eigensheaf`）；补术语卡是 P2 的活。
- 语义检索（向量）暂不做：1–3 万卡规模下，FTS5 + 术语归一足够；等卡量上去再考虑 `sqlite-vec`。
