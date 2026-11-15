# 推导链语料产出报告

工程：WIT-0604151-EMDGL（Kapustin–Witten 2006 分层解经本）
角色：语料工程子代理 corpus
日期：2026-11-15

## 1. 产出清单

| 文件 | 条数 | 目标区间 | 大小 | 状态 |
| --- | ---: | --- | ---: | --- |
| `derivation/skeleton.jsonl` | 119 | 90–120 | ~126 KB | 校验通过 |
| `derivation/qa.jsonl` | 66 | 60–70 | ~32 KB | 校验通过 |
| `derivation/concepts.jsonl` | 85 | 70–85 | ~50 KB | 校验通过 |
| `derivation/branches.jsonl` | 38 | 30–40 | ~20 KB | 校验通过 |
| `manuscript/sections/51_appendix_corpus.tex` | 4 页 | 3–5 页 | ~12 KB | 编译通过 |
| `reports/corpus_report.md` | — | — | — | 本文件 |

另：`tools/check_jsonl.py`（自检脚本，新增）、`build/check_corpus/check.tex` 与编译产物（编译自检用）。

## 2. 校验方法与结果

### 2.1 JSONL

`tools/check_jsonl.py` 的检查项：

1. 每个文件逐行 `json.loads`，统计非法行；
2. 四类文件的必填字段是否齐全（skeleton 14 字段、qa 9 字段、concepts 11 字段、branches 8 字段）；
3. `id` 唯一、`anchor` 非空；
4. skeleton 的 `anchor` 页号必须落在 `section` 对应的页码区间（区间表照 `source/meta.md`）；
5. 原始行不得匹配绝对路径正则 `[A-Za-z]:\\\\`（匹配 JSON 转义后的盘符路径）；
6. 长度限制：skeleton 的 `idea`/`claim` ≤300 字，qa 的 `answer` ≤400 字，concepts 的 `definition_our` ≤200 字；
7. concepts 的 `edges` 类型必须在 9 种允许值内、目标 id 存在、无重复边；`nlab` 要么为 null 要么是 `https://ncatlab.org/nlab/show/...`；
8. `provenance` 只允许 A/B/C。

最终结果：**0 issue(s)**（首次跑出 34 个问题，逐条修完：4 行坏 JSON、8 处 section/anchor 越界、
2 处正则误报、1 处 idea 超长、1 处非法转义）。

### 2.2 LaTeX 编译

`build/check_corpus/check.tex`（照 `build/check_layer0/check.tex` 写法，只 input `51_appendix_corpus`），
`xelatex -interaction=nonstopmode` 连跑两遍：**exit 0，0 error，0 undefined reference，Output written 4 pages**。
未使用 `\begin{caveat}`（会报错，`\caveat` 是带参命令），警示框用 `\begin{warn}`。

## 3. 统计

### 3.1 provenance（skeleton + qa）

| 文件 | A（原文明确） | B（我们重建） | C（我们判断） |
| --- | ---: | ---: | ---: |
| skeleton | 89 | 21 | 9 |
| qa | 55 | 9 | 2 |
| 合计 | 144（77.8%） | 30（16.2%） | 11（5.9%） |

设计要求 A 约 55%、B 30%、C 15%。**实际 A 明显偏高**，见 §5 薄弱处第 1 条。

### 3.2 skeleton

- 节点分布：S1 13、S2 18、S3 15、S4 15、S5 15、S6 13、S7 15、S8 15（每节点 13–18，满足 8–20）；
- 覆盖 37 个小节、98 个不同锚点；
- 依赖边 154 条；119/119 条填写 `failure_mode`。

### 3.3 qa

- 类型：概念 26、推导 20、动机 10、陷阱 10；
- 层级：核心 29、细节 25、进阶 12；
- 覆盖 29 个小节。

### 3.4 concepts

- kind：物理 31、几何 25、代数 19、工具 10；
- 边 103 条：`depends_on` 93、`specializes_to` 8、`dual_to` 1、`categorifies` 1（9 种允许类型只实现 4 种）；
- 84/85 个节点至少有一条边（唯一孤立点 `C-COHOM`，因它只作背景概念）；
- nLab：79 个非空（78 个去重 URL）、6 个 null；`stacks` 全部 null。

### 3.5 branches

- 类型：常见误解 25、技术陷阱 10、死路 2、未被采用的路线 1；
- 覆盖 21 处正文位置；38/38 `recoverable: true`；
- 任务书点名的 8 个题材全部覆盖：Ψ 当耦合常数、普通 N=4 直接紧化、跳过 §12、't Hooft 当 Wilson、
  eigenbrane 当 Hecke 特征层本身、镜像当另一组对偶、忽略 π₁(G) 相位、M_H 的 J 与 K 混用。

## 4. nLab 链接核验

策略：**全量 HTTP 探测 + 关键页逐页核验**。

1. 用临时脚本（`build/nlab_probe.py`，urllib + 12 线程、15 s 超时）对 123 个候选 slug 做 GET：
   - 104 个返回 HTTP 200 且页面标题与概念匹配 → 采用；
   - 19 个 404/不一致 → 弃用，相关概念写 `null`（GNO 对偶群、$\mathcal N=4$ SYM、超凯勒商、
     Hecke modification、N=4 表示、谱曲线、SYZ、opers、monopole bubbling 等）。
2. 再用 `web_fetch` 对 4 个核心页逐页确认（HTTP 200、标题、正文确实讲该概念）：
   - `https://ncatlab.org/nlab/show/D-module`
   - `https://ncatlab.org/nlab/show/Langlands+dual+group`
   - `https://ncatlab.org/nlab/show/Hecke+eigensheaf`（页面正文含 KW 的 S-对偶/特征膜对照表）
   - `https://ncatlab.org/nlab/show/affine+Grassmannian`
3. 未采用的 19 个候选**没有**写进语料，因此语料中不存在编造的 nLab URL；
4. Stacks Project：未能稳定核验 tag，按任务要求全部写 null，不做猜测。

## 5. 已知薄弱处

1. **A 级偏高**（77.8% vs 目标 55%）：第一批优先写原文明确的步骤，B/C 类判断（尤其 §10–§12）
   写得偏少；若要达标，需把部分「原文一句话、重建一大段」的步骤降级为 B。
2. **锚点为页级/节级**：98 个不同锚点支撑 119 条，存在同页多步；不是逐句对齐，不能当精确引用。
3. **概念边稀疏**：只实现 4/9 种边类型，且有 1 个孤立节点；缺少 `generalizes`/`acts_on`/`obstruction_to` 等。
4. **外部参考不完整**：`stacks` 全为 null；6 个概念 nLab 为 null。
5. **§12 之后语料较薄**：四维边界条件部分多为 B 级重建（原文自陈「实现不唯一」），
   且 §10.4/§10.5 的 OPE 与扩展 Bogomolny 只给了 2 条骨架步。
6. **未做人审**：按 witten-exegesis 闸门只能标 `dev`，不得标 `train`；附录 B 已写明此限制。

## 6. 复现命令

```powershell
$py = 'C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe'
& $py -X utf8 tools\check_jsonl.py        # 期望 0 issue(s)
cd build\check_corpus
xelatex -interaction=nonstopmode check.tex
xelatex -interaction=nonstopmode check.tex # 期望 0 error
```

## 7. 清理说明

生成过程中的临时文件已删除：`derivation/_tmp_*.jsonl`、`build/_merge_corpus.py`、`build/_stats.py`、
`build/nlab_probe.py`、`build/nlab_probe.txt`、`build/tmp_fix*.py`、`build/tmp_show_abs.py`、
`build/probe_corpus_urls.ps1/.txt`。保留 `build/check_corpus/`（编译证据）与 `tools/check_jsonl.py`（校验脚本）。
未改动 `manuscript/main.tex`、`preamble.tex` 及其他 sections 文件。
