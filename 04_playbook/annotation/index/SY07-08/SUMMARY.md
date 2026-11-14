# 结构索引 · SY07-08

> 由 `tools/build_structure_index.py` 生成（D0，零 LLM，确定性抽取）。nodes 只是骨架，不含 role/difficulty；edges 的 method=rule、status=proposed。`uses`=节点内/证明内引用，`mentions`=正文提及（confidence 0.5，仅线索）。

## 总览

| 项 | 值 |
|---|---|
| 扫描 .tex 文件 | 21 |
| 环境实例（全部） | 1089 |
| 已识别为节点 | 223（定理型 210，章/节结构 13；带 label 223） |
| 类型分布 | proposition 125、lemma 37、corollary 35、theorem 13、subsection 12、section 1 |
| 引用总数 | 338 |
| 去重后边 | 256（uses 198 / mentions 58） |
| 正文 mention 条数 | 77 |
| 解析失败引用 | 18（目标去重 15） |
| 重复 label | 0 |
| 带 proof 的节点 | 187 |

## 未映射环境（Top 20）

这些环境没在 preamble/默认表里找到中文标题，暂不建节点；补 `KIND_BY_TITLE` 即可。

| env | 次数 |
|---|---|
| `equation*` | 186 |
| `tikzcd` | 148 |
| `enumerate` | 107 |
| `center` | 83 |
| `tnote` | 76 |
| `aligned` | 41 |
| `align*` | 20 |
| `cases` | 15 |
| `exercises` | 9 |
| `pmatrix` | 3 |
| `flushright` | 2 |
| `equation` | 1 |

## PageRank Top 15（全文最承重的节点）

| # | node | kind | 入度 | PR | 位置 |
|---|---|---|---|---|---|
| 1 | `SY07-08:it:1.1.2` | proposition | 2 | 0.0372 | chunks/c01b.tex:39 |
| 2 | `SY07-08:it:1.2.2` | proposition | 9 | 0.0361 | chunks/c03.tex:24 |
| 3 | `SY07-08:it:2.1.1` | proposition | 3 | 0.0267 | chunks/c10.tex:114 |
| 4 | `SY07-08:it:1.2.5` | proposition | 4 | 0.0267 | chunks/c03.tex:169 |
| 5 | `SY07-08:it:1.2.4` | proposition | 3 | 0.0235 | chunks/c03.tex:89 |
| 6 | `SY07-08:it:1.3.13` | proposition | 3 | 0.0222 | chunks/c04.tex:249 |
| 7 | `SY07-08:it:1.5.1` | proposition | 5 | 0.0193 | chunks/c08.tex:29 |
| 8 | `SY07-08:it:1.3.16` | proposition | 4 | 0.0184 | chunks/c04.tex:412 |
| 9 | `SY07-08:it:1.5.3` | corollary | 4 | 0.0181 | chunks/c08.tex:91 |
| 10 | `SY07-08:it:1.5.2` | proposition | 1 | 0.0172 | chunks/c08.tex:73 |
| 11 | `SY07-08:it:1.2.1` | proposition | 1 | 0.0172 | chunks/c03.tex:13 |
| 12 | `SY07-08:it:1.5.4` | proposition | 5 | 0.0169 | chunks/c08.tex:140 |
| 13 | `SY07-08:it:1.3.9` | proposition | 4 | 0.0140 | chunks/c04.tex:165 |
| 14 | `SY07-08:it:1.3.10` | proposition | 3 | 0.0138 | chunks/c04.tex:196 |
| 15 | `SY07-08:it:1.2.10` | proposition | 1 | 0.0125 | chunks/c03.tex:344 |

## 被引用最多 Top 15

| # | node | kind | 入度 | 位置 |
|---|---|---|---|---|
| 1 | `SY07-08:it:1.2.2` | proposition | 9 | chunks/c03.tex:24 |
| 2 | `SY07-08:it:2.4.9` | proposition | 7 | chunks/c15.tex:337 |
| 3 | `SY07-08:it:1.4.2` | proposition | 6 | chunks/c06.tex:138 |
| 4 | `SY07-08:it:2.4.5` | corollary | 6 | chunks/c15.tex:272 |
| 5 | `SY07-08:it:1.4.1` | proposition | 5 | chunks/c06.tex:75 |
| 6 | `SY07-08:it:1.5.1` | proposition | 5 | chunks/c08.tex:29 |
| 7 | `SY07-08:it:1.5.4` | proposition | 5 | chunks/c08.tex:140 |
| 8 | `SY07-08:it:1.5.13` | proposition | 5 | chunks/c09.tex:54 |
| 9 | `SY07-08:it:1.2.5` | proposition | 4 | chunks/c03.tex:169 |
| 10 | `SY07-08:it:1.2.8` | proposition | 4 | chunks/c03.tex:270 |
| 11 | `SY07-08:it:1.3.9` | proposition | 4 | chunks/c04.tex:165 |
| 12 | `SY07-08:it:1.3.16` | proposition | 4 | chunks/c04.tex:412 |
| 13 | `SY07-08:it:1.3.25` | proposition | 4 | chunks/c05.tex:248 |
| 14 | `SY07-08:it:1.3.26` | proposition | 4 | chunks/c05.tex:277 |
| 15 | `SY07-08:it:1.4.3` | proposition | 4 | chunks/c06.tex:253 |

## 解析失败的引用目标（Top 20）

常见原因：label 在未扫描的附录/别册、拼写差异、`\cref` 多目标拆分、章级引用无节点。

| target | 次数 |
|---|---|
| `it:2.7.10` | 2 |
| `eq:2.3.1` | 2 |
| `it:2.6.7` | 2 |
| `it:1.1.6` | 1 |
| `ex:1.1.1` | 1 |
| `it:1.3.17` | 1 |
| `it:1.3.19` | 1 |
| `it:1.3.28` | 1 |
| `it:1.3.30` | 1 |
| `it:1.4.8` | 1 |
| `it:1.5.13` | 1 |
| `it:1.5.12` | 1 |
| `it:2.5.2` | 1 |
| `it:2.5.7` | 1 |
| `it:2.5.8` | 1 |

## 下一步

- 人工/LLM 只补 `role`、`difficulty`、`statement_zh`，不改边；
- 边进人工闸门：每类抽 50 条 precision ≥0.9 才允许扩书；
- 把本目录登记进 `index/README.md`。
