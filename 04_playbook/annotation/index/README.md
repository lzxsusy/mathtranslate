# 结构索引 v0（D0）· 三本书的实测结果

> 2026-11-14。零 LLM、只从 LaTeX 源码抽 `\begin{definition/theorem/...}` + `\label` + `\ref`。
> 用途：给「论证精读」提供骨架——先知道一篇论文里有哪些陈述、谁引用谁，再让 LLM 补「为什么难」。
> **这不是最终图谱**：它只有 statement 级依赖，没有步骤、没有 warrant、没有概念合并。

## 一、三本书横向对比

| 指标 | SY07-08 代数几何（第二版） | SY01-11 Kontsevich–Witten | SY01-23 Dirichlet 膜与镜像对称 |
|---|---|---|---|
| 源码文件 | 21 | 13 | 14 |
| 环境实例 | 1,089 | — | — |
| 定理型节点 | **210** | 52 | **455** |
| 章/节结构节点 | 13 | 0 | 375 |
| 带 label | 223 / 223 | **0 / 52** | 798 / 830 |
| 边（uses / mentions） | 256（198 / 58） | **0** | 801（162 / 639） |
| 解析失败引用 | 18（目标去重 15） | 0 | 974（目标去重 535） |
| 带 proof 的节点 | 187 | 16 | 77 |
| 重复 label | 0 | 0 | 0 |
| 结论 | **可直接用** | **不可用：译本丢了 label** | 可用，但需补 equation/section 节点 |

类型分布：SY07-08 = proposition 125 / lemma 37 / corollary 35 / theorem 13；SY01-23 以 definition / theorem / proposition / remark 为主（详见各目录 `SUMMARY.md`）。

## 二、每本书说明什么

### SY07-08：结构完整，是 D1 的基准书
- 21 个 chunk 全部有 `\label`，198 条 `uses` 边能落到具体 `\ref`。
- 187 个节点带 proof，适合做「步骤级精读」的第一篇。
- 未解析 18 条：多为指向图/表/公式的引用，不是定理依赖，可忽略。

### SY01-11：反面样本，暴露工作流缺口
- 52 个定义/定理**一个 label 都没有**，所以 0 条边。
- 这不是脚本问题，是译本生产时把 `\label` 删了（或从未加）。
- **结论：任务书必须写死「保留并回填 `\label`」，否则精读只能靠 LLM 从纯文本猜依赖。**

### SY01-23：量大、结构层次多，但 974 条未解析
- 830 个节点（455 定理型 + 375 章/节），801 条边；`\BookRef` 宏已能解析。
- 未解析主要是 `eq:*`（公式）与 `sec:*`（节）——公式/节没有建成节点。章级 `chap:*` 已通过结构节点解决。
- 下一步优先级：先补 `section` 节点（成本低），`equation` 节点只在做「公式依赖」时再加。

## 三、怎么复跑

```powershell
$py = "C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
$ann = "C:\Users\admin\Desktop\数译发布\gitee_shuyi\04_playbook\annotation"

& $py "$ann\tools\build_structure_index.py" `
  --root "C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY07-08_代数几何（第二版）\源码" `
  --paper-id SY07-08 --out "$ann\index"
```

三本书都跑一遍后，`index/<paper_id>/` 下会有 `nodes.jsonl`、`edges.jsonl`、`SUMMARY.md`。

## 四、字段说明（nodes / edges）

- `node_id`：`<paper_id>:<label>`；无 label 的节点用 `<paper_id>:auto-<file>-<line>`。
- `kind`：由 preamble 的 `\newtheorem{env}{中文标题}` 推断；星号环境自动去 `*`。
- `locator.tex_file / tex_lines`：可直接跳回源码行。
- `body_sha1`：节点体哈希，用于查重与增量更新。
- `has_proof`：节点后是否紧跟 `\begin{proof}`。
- `pagerank / in_degree / out_degree`：结构重要性，只作排序线索，**不是难度**。
- `edges.rel`：`uses`（定理体/proof 内的 `\ref`）或 `mentions`（正文顺带提到，confidence 0.5，只作线索）。
- `edges.evidence`：原文 quote + 行号，满足「无证据不入库」的下限要求。

## 五、已知边界

1. 只读 LaTeX 源码；PDF-only 的书（21 部未入语料中的 14 部）这条路径走不通。
2. 译本若丢 `\label`，索引直接失效（SY01-11 是实例）。
3. `equation` / `figure` / `tikzcd` 不建节点，所以公式级依赖暂缺。
4. 章/节节点会把 PageRank 抬高；`SUMMARY.md` 的 Top 表已排除结构节点。
5. 这里的边只是「引用」，不是「论证」；`warrant`、步骤切分、难度分要由 L1/L2 标注补。

## 六、下一步（D1）

1. 以 SY07-08 为基准书，人工标 5 个 unit（含 1 个 gap）+ 3 条 inference + 1 条 chain。
2. 用 `tools/check_gate.py` 过 G2.5。
3. 把 SY07-08 的 198 条 `uses` 边抽样 30 条，人工判 precision；< 0.9 就先修解析器，不扩量。
