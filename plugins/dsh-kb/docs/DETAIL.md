# dsh-kb

**数译知识库** — 把带页码、带来源、带可信度的数学文献资料卡，接成 agent 可直接检索的工具。

## 它解决什么问题

翻译/精读一本新书时，最贵的不是查资料，而是**不知道我们自己已经知道什么**：
同一概念在别的书里已经做过卡、同一术语有过三种译法、同一个命题某处已经勘误过。
`dsh-kb` 把这些问题变成一次 `kb_brief` 调用。

## 为什么不是通用 RAG

| | 通用 RAG | dsh-kb |
|---|---|---|
| 检索单位 | 文本块 | 一张卡（概念/定理/证明骨架/论证链/勘误/对齐） |
| 出处 | 文件名 | 作品编号 + **原文页码** + 来源等级（A 一手 / B 讲义 / C 转述） |
| 可信度 | 无 | `verified` / `checked` / `disputed` / `draft`，默认只给已核 |
| 矛盾 | 揉成一个答案 | 成对返回，标 `disputed` |
| 回源 | 难 | `kb_card` 给页图路径，一步回原文核对 |

## 工具

- `kb_search(query, layer?, kind?, work?, level?, lang?, include_draft?, limit?)` — `layer=cards|source|both`
- `kb_source(pkg, page?, query?, around?)` — 读底本原文整页上下文
- `kb_card(id)`
- `kb_brief(work? | query?)` — 阅读前置包
- `kb_zh(pkg, para? | query?)` — 读中文译文某段及前后文
- `kb_stats()` — 库现状 + 三层覆盖度

## 三层数据

| 层 | 内容 | 规模 | 索引方式 |
|---|---|---|---|
| `cards` | 结构化资料卡（结论 + 出处 + 可信度） | 1,250 张 / 45 部 | 中文 bigram 倒排 + 拉丁词表，字段加权 |
| `zh` | 本库自己的中文译文（逐段） | 47,802 段 / 82 个工程 / 389.8 万汉字（8.1 MB gz） | 预计算小写文本，线性扫描（单查 5–30ms） |
| `source` | 底本原文抽文（逐字） | 7,644 段 / 33 个工程 / 5.2M 字符（2.2 MB gz） | 同上（2–60ms） |

`zh` / `source` 两层不建倒排是有意为之：几百万字符建 bigram 索引要吃几百 MB 内存，而线性扫描已经够快。
三层都只读仓库里**已经公开**的数据（卡片 JSON + 译文语料 + 已公开的原文抽文），不新做原文摘录。

## 配置

```yaml
repo:   "C:\\Users\\admin\\Desktop\\数译发布\\gitee_shuyi"
python: "C:\\Users\\admin\\.dsh\\dsh-runtimes\\dsh-primary-runtime\\dependencies\\python\\python.exe"
timeoutMs: 30000
```

数据在包内 `data/cards`（卡片）、`data/zh`（译文）与 `data/src`（原文抽文）。配了 `repo` 时优先读
`repo/kb/cards`、`repo/01_corpus_zh` 与 `repo/01_corpus_src`；`kb/shuyi.db`（由 `kb/ingest.py` + `kb/build_kb.py` 生成）
只是 Python 侧查询用的中间产物，插件不依赖它。
