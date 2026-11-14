# 结构索引 · SY01-23

> 由 `tools/build_structure_index.py` 生成（D0，零 LLM，确定性抽取）。nodes 只是骨架，不含 role/difficulty；edges 的 method=rule、status=proposed。`uses`=节点内/证明内引用，`mentions`=正文提及（confidence 0.5，仅线索）。

## 总览

| 项 | 值 |
|---|---|
| 扫描 .tex 文件 | 14 |
| 环境实例（全部） | 1727 |
| 已识别为节点 | 830（定理型 455，章/节结构 375；带 label 798） |
| 类型分布 | subsection 185、definition 138、subsubsection 136、example 107、theorem 56、section 45、proposition 43、exercise 30、remark 27、lemma 14、assumption 12、chapter 9、conjecture 9、construction 7、problem 5、corollary 5、claim 2 |
| 引用总数 | 1861 |
| 去重后边 | 801（uses 162 / mentions 639） |
| 正文 mention 条数 | 708 |
| 解析失败引用 | 974（目标去重 535） |
| 重复 label | 0 |
| 带 proof 的节点 | 77 |

## 未映射环境（Top 20）

这些环境没在 preamble/默认表里找到中文标题，暂不建节点；补 `KIND_BY_TITLE` 即可。

| env | 次数 |
|---|---|
| `equation` | 570 |
| `aligned` | 254 |
| `figure` | 142 |
| `enumerate` | 89 |
| `pmatrix` | 57 |
| `cases` | 20 |
| `itemize` | 14 |
| `gathered` | 11 |
| `table` | 6 |
| `tabular` | 6 |
| `array` | 4 |
| `split` | 3 |
| `lettertheorem` | 2 |
| `align` | 2 |
| `property` | 2 |
| `equation*` | 2 |
| `solution` | 1 |
| `smallmatrix` | 1 |
| `principle` | 1 |
| `matrix` | 1 |

## PageRank Top 15（全文最承重的节点）

| # | node | kind | 入度 | PR | 位置 |
|---|---|---|---|---|---|
| 1 | `SY01-23:prop:4.36` | proposition | 2 | 0.0172 | chapters/ch04.tex:811 |
| 2 | `SY01-23:ex:7.10` | example | 5 | 0.0071 | chapters/ch07.tex:845 |
| 3 | `SY01-23:lem:5.39` | lemma | 2 | 0.0059 | chapters/ch05.tex:3687 |
| 4 | `SY01-23:ex:4.35` | example | 6 | 0.0047 | chapters/ch04.tex:800 |
| 5 | `SY01-23:lem:4.51` | lemma | 2 | 0.0046 | chapters/ch04.tex:1476 |
| 6 | `SY01-23:constr:6.92` | construction | 4 | 0.0045 | chapters/ch06.tex:3321 |
| 7 | `SY01-23:def:1.2` | definition | 1 | 0.0041 | chapters/ch01.tex:149 |
| 8 | `SY01-23:ex:4.13` | example | 1 | 0.0041 | chapters/ch04.tex:191 |
| 9 | `SY01-23:ex:5.3` | example | 1 | 0.0041 | chapters/ch05.tex:159 |
| 10 | `SY01-23:thm:5.41` | theorem | 1 | 0.0041 | chapters/ch05.tex:3828 |
| 11 | `SY01-23:lem:7.26` | lemma | 1 | 0.0041 | chapters/ch07.tex:1786 |
| 12 | `SY01-23:constr:6.86` | construction | 6 | 0.0040 | chapters/ch06.tex:3148 |
| 13 | `SY01-23:ex:7.7` | example | 3 | 0.0039 | chapters/ch07.tex:549 |
| 14 | `SY01-23:prop:5.35` | proposition | 3 | 0.0036 | chapters/ch05.tex:3586 |
| 15 | `SY01-23:prop:6.24` | proposition | 5 | 0.0035 | chapters/ch06.tex:939 |

## 被引用最多 Top 15

| # | node | kind | 入度 | 位置 |
|---|---|---|---|---|
| 1 | `SY01-23:ex:4.35` | example | 6 | chapters/ch04.tex:800 |
| 2 | `SY01-23:constr:6.86` | construction | 6 | chapters/ch06.tex:3148 |
| 3 | `SY01-23:thm:4.76` | theorem | 5 | chapters/ch04.tex:2305 |
| 4 | `SY01-23:thm:5.37` | theorem | 5 | chapters/ch05.tex:3665 |
| 5 | `SY01-23:prop:6.24` | proposition | 5 | chapters/ch06.tex:939 |
| 6 | `SY01-23:constr:6.90` | construction | 5 | chapters/ch06.tex:3263 |
| 7 | `SY01-23:ex:7.10` | example | 5 | chapters/ch07.tex:845 |
| 8 | `SY01-23:ex:5.22` | example | 4 | chapters/ch05.tex:1600 |
| 9 | `SY01-23:ex:6.74` | example | 4 | chapters/ch06.tex:2823 |
| 10 | `SY01-23:constr:6.92` | construction | 4 | chapters/ch06.tex:3321 |
| 11 | `SY01-23:eq:3.44` | example | 3 | chapters/ch03.tex:1033 |
| 12 | `SY01-23:ex:4.39` | example | 3 | chapters/ch04.tex:849 |
| 13 | `SY01-23:ex:4.52` | example | 3 | chapters/ch04.tex:1527 |
| 14 | `SY01-23:ex:4.65` | example | 3 | chapters/ch04.tex:1981 |
| 15 | `SY01-23:cor:4.73` | corollary | 3 | chapters/ch04.tex:2253 |

## 解析失败的引用目标（Top 20）

常见原因：label 在未扫描的附录/别册、拼写差异、`\cref` 多目标拆分、章级引用无节点。

| target | 次数 |
|---|---|
| `chap:4` | 12 |
| `chap:5` | 11 |
| `chap:3` | 10 |
| `eq:5.41` | 10 |
| `eq:5.71` | 10 |
| `chap:8` | 9 |
| `eq:7.1` | 9 |
| `eq:7.2` | 9 |
| `eq:3.1` | 8 |
| `eq:5.17` | 8 |
| `chap:2` | 6 |
| `chap:6` | 6 |
| `eq:3.59` | 6 |
| `eq:3.181` | 6 |
| `eq:3.79` | 6 |
| `chap:7` | 5 |
| `eq:3.14` | 5 |
| `eq:3.75` | 5 |
| `eq:3.87` | 5 |
| `eq:3.70` | 5 |

## 下一步

- 人工/LLM 只补 `role`、`difficulty`、`statement_zh`，不改边；
- 边进人工闸门：每类抽 50 条 precision ≥0.9 才允许扩书；
- 把本目录登记进 `index/README.md`。
