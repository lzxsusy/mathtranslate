# 结构索引 · SY01-11

> 由 `tools/build_structure_index.py` 生成（D0，零 LLM，确定性抽取）。nodes 只是骨架，不含 role/difficulty；edges 的 method=rule、status=proposed。`uses`=节点内/证明内引用，`mentions`=正文提及（confidence 0.5，仅线索）。

## 总览

| 项 | 值 |
|---|---|
| 扫描 .tex 文件 | 13 |
| 环境实例（全部） | 253 |
| 已识别为节点 | 52（定理型 52，章/节结构 0；带 label 0） |
| 类型分布 | theorem 23、definition 11、lemma 8、proposition 4、remark 3、example 2、corollary 1 |
| 引用总数 | 0 |
| 去重后边 | 0（uses 0 / mentions 0） |
| 正文 mention 条数 | 0 |
| 解析失败引用 | 0（目标去重 0） |
| 重复 label | 0 |
| 带 proof 的节点 | 16 |

> ⚠️ 本工程所有节点都没有 `\label`：**无法建边**。这是翻译流程的缺口——任务书需要求「保留/补齐 label」。

## 未映射环境（Top 20）

这些环境没在 preamble/默认表里找到中文标题，暂不建节点；补 `KIND_BY_TITLE` 即可。

| env | 次数 |
|---|---|
| `center` | 54 |
| `aligned` | 38 |
| `enumerate` | 25 |
| `pmatrix` | 25 |
| `tikzcd` | 21 |
| `array` | 7 |
| `align*` | 5 |
| `itemize` | 4 |
| `quote` | 3 |
| `flushright` | 1 |
| `gathered` | 1 |

## PageRank Top 15（全文最承重的节点）

| # | node | kind | 入度 | PR | 位置 |
|---|---|---|---|---|---|

## 被引用最多 Top 15

| # | node | kind | 入度 | 位置 |
|---|---|---|---|---|

## 下一步

- 人工/LLM 只补 `role`、`difficulty`、`statement_zh`，不改边；
- 边进人工闸门：每类抽 50 条 precision ≥0.9 才允许扩书；
- 把本目录登记进 `index/README.md`。
