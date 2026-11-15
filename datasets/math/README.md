# `datasets/math/`：数学推理语料（不是翻译语料）

> 这一层回答的问题不是「这句话怎么译」，而是「这个数学断言为什么成立、证明的哪一步是真正难的、缺了哪块砖」。

## 为什么转向数学与推理

2026-11-16 与仓主讨论后调整方向：翻译数据教的是「语言转换」，而模型缺的是**数学理解与推理**，尤其是**中文的推理链**——现有数学语料以英文为主（NuminaMath 86 万条英文 CoT、MATH/GSM8K 均为英文），中文数学数据集中在 K-12 题库（CMATH、AMPSD24K、FineMath 等），研究级中文推理几乎空白。模型在 MoE 里「用英文想」不是提示词问题，是训练分布问题。

北大 AI4Math（董彬团队）的经验给了三条可直接借用的做法：

1. **把数学数字化**：自然语言 ↔ Lean 4 的形式化对，能给出可机器校验的反馈信号，是「高质量数据」的硬标准（[AI4M 学习指南](http://faculty.bicmr.pku.edu.cn/~dongbin/Data/AI4M2025.pdf)、[Rethlas/Archon 论文](https://ar5iv.labs.arxiv.org/html/2604.03789)）。
2. **检索是推理的一部分**：Matlas 把论文拆成**命题级**条目（旧版 arXiv 语料 1,360 万条；新版 851 万条，来自 43.5 万篇论文、180 种期刊、1,900 余本教材），并抽取陈述间的依赖、做**层级展开**让每条自成上下文；LeanSearch 在 Mathlib（26.7 万定理 / 12.7 万定义）上做语义检索。数据单位是「一条自足的数学陈述」，不是「一篇论文」。
3. **推理原语要显式记录**：构造玩具例子、构造反例、检索相关结果、拆子目标、直接证明、递归证明、归纳失败模式——这些动作比最终证明更能教会模型「怎么做数学」。

## 一条记录是什么

本目录只收**数学内容**，语言以中文为主（`lang=zh`），英文原句只作为 `source.quote` 短引用。

| 字段 | 含义 |
|---|---|
| `kind` | `definition` / `theorem` / `claim` / `construction` / `example` / `counterexample` / `gap` |
| `statement` | 中文陈述，自足：不依赖上一段也能读懂 |
| `context` | 让陈述自足所需的定义展开（对应 Matlas 的 hierarchical unfolding） |
| `proof` | 中文证明/论证；`kind=definition` 时可空 |
| `proof_steps` | 结构化步骤：`claim` / `justification` / `gap`（哪一步作者跳过了） |
| `dependencies` | 这条陈述用到的前置结果，`name` + `why` + `ref`（行号或外部编号） |
| `difficulty` | 1–5（3=研究生教材习题，4=论文技术引理，5=研究级） |
| `verification` | `kind`: `lean` / `human` / `none`；`status`: `checked` / `sketch` / `unchecked`；`artifact` 指向 Lean 文件或审校记录 |
| `rights` | 数学事实本身不受版权保护；本条的中文表述与结构化是自产，记 `self` |

## 与 `parallel/` 的分工

- `parallel/`：保留，但降为「术语与表达」小样本，用于术语一致性，不再扩量。
- `math/`：主力。目标不是「多」，而是**每条都能被检查**：要么 Lean 编译过，要么有人逐行审过并写明 `status=sketch` 与缺口。

## 生产流程

1. **选点**：从 `datasets/deepread/` 的精读卡或论文的技术引理里挑「真正难的一步」，不要挑定义复述。
2. **自足化**：把陈述需要的定义、记号、前置换写成 `context`，使读者不需要翻原文。
3. **写证明**：先写 `proof_steps`，每步只放一个断言 + 一句理由；作者跳过的地方标 `gap`，不要替它补完还假装是原文。
4. **挂依赖**：`dependencies` 指向本目录其他条目或外部编号；没有出处的依赖不写。
5. **校验**：以人工复核为主（`verification.kind=human`），写清审校人与缺口；只有已有形式化产物的条目才标 `lean`，不把形式化当主线——那是专门团队的基础设施。
6. **过门禁**：`python tools/ds_lint.py` 与 `python tools/ds_publish.py --check`。

## 扩量顺序

1. 先把 `SY05-25`（Witten, arXiv:0802.0999）第 1 节的 6 条做成模板；
2. 每部 arXiv 工程挑 3–5 个「技术引理/关键跳步」，目标 37 部 × 4 ≈ 150 条；
3. 讲义类（22 部）做定义链与证明骨架；
4. 图书类只做 `_internal/`，不发布；
5. 形式化对（NL↔Lean）**不是我们的主线**：有现成产物才收录，没有就不做；我们优先把自然语言推理写扎实。

## 反面清单

- 不收「把英文证明逐句译成中文」的条目——那是 `parallel/`，不是推理数据。
- 不收没有 `proof_steps` 的「结论 + 一段话」，那只是摘要。
- 不收 `status=unchecked` 还标 `difficulty>=4` 的条目：难题的错答案比没有更糟。
- 不用模型生成的证明冒充人工审校；`verification.kind` 必须诚实。
