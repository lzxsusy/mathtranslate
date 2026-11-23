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

- `kb_search(query, kind?, work?, level?, include_draft?, limit?)`
- `kb_card(id)`
- `kb_brief(work? | query?)` — 阅读前置包
- `kb_stats()` — 库现状 + 风险队列

## 配置

```yaml
repo:   "C:\\Users\\admin\\Desktop\\数译发布\\gitee_shuyi"
python: "C:\\Users\\admin\\.dsh\\dsh-runtimes\\dsh-primary-runtime\\dependencies\\python\\python.exe"
timeoutMs: 30000
```

数据在 `repo/kb/shuyi.db`（由 `kb/ingest.py` + `kb/build_kb.py` 生成）。
