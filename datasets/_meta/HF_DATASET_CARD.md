---
pretty_name: "数译 Shuyi — 中文数学译注语料与资料卡"
language:
  - zh
license: cc-by-4.0
task_categories:
  - text-generation
  - question-answering
  - text-classification
tags:
  - mathematics
  - chinese
  - corpus
  - lean4
  - formalization
  - langlands-program
  - dataset
size_categories:
  - 100K<n<1M
configs:
  - config_name: paragraphs
    data_files: zh_paragraphs.jsonl
  - config_name: terms
    data_files: termbase.jsonl
  - config_name: cards
    data_files: cards/**/*.json
---

# 数译 Shuyi — 中文数学译注语料与资料卡

本数据集把数学讲义与专著逐段译成中文，并把译文、术语、资料卡与 Lean 4 对齐卡整理成机器可读格式。
当前快照（2026-11-27）：**147 部译注工程**、**51,009 段**段落级中文语料（86% 含公式）、
**2,214 条**中英日术语、**1,858 张**资料卡。

## 文件

| 文件 | 规模 | 说明 |
|---|---|---|
| `zh_paragraphs.jsonl` | 51,009 行 | 段落级中文语料；按 `para_id` 去重，按 `flags` 过滤 |
| `termbase.jsonl` | 2,214 行 | 术语基：外文 / 中文 / 语种 / 状态 / 来源工程 |
| `cards/**/*.json` | 1,858 个 | 资料卡：定义、定理、证明思路、校正、例子、陈述、注记 |
| `catalog.json` | 147 行 | 工程目录：编号、底本、作者、段落数、源码数 |

## Schema

### `zh_paragraphs.jsonl`

```json
{"pkg": "SY02-33", "para_id": "…", "env": "text", "tier": "B",
 "flags": [], "text": "……"}
```

- `pkg`：工程编号；`para_id`：段落在仓库中的稳定 id（去重键）。
- `env`：LaTeX 环境类型（`text` / `theorem` / `definition` / `equation` 等）。
- `tier`：译注等级（A / B / I，见 `DATASHEET.md`）。
- `flags`：质量标志；建议训练前过滤 `orphan_number`、`empty_ref`。
- `text`：去掉 LaTeX 命令、保留行内公式的中文正文。

### `cards/**/*.json`

关键字段：`id`、`type`（`concept` / `derivation` / `correction` / `example` / `statement` / `remark` / `conjecture`）、
`title`、`summary`、`definition{text,notation}`、`key_points`、`formulas`、
`theorems{name,statement,proof{status,steps,gap_note},source}`、`pitfalls`、`related`、
`sources{book,section,pages,pdf_pages,anchor}`、`rights`、`status`。
含义与制作标准见仓库 `04_playbook/23_资料卡制作规范_v1.md`。

## 用法

```python
from datasets import load_dataset

paras = load_dataset("json", data_files="zh_paragraphs.jsonl", split="train")
terms = load_dataset("json", data_files="termbase.jsonl", split="train")
```

训练前建议：

1. 按 `para_id` 去重（全库唯一段 49,443）；
2. 过滤 `flags` 中的 `orphan_number`、`empty_ref`；
3. 语料含公式，分词/切块时不要按 `$` 硬切。

## 许可（三层，别混）

- **自产层**（元数据、术语、方法、脚本、文档）：CC BY 4.0。
- **译文层**（译文、译注、语料正文、LaTeX 源码）：第三方底本的演绎作品；
  本库不代原作者授权，也不另设限制（检索、研究、教学、训练、蒸馏均可）；权利人通知即撤。
- **原文本体**（底本 PDF、扫描件、页面图、OCR 全文）：**不在本数据集中**。

## 已知偏差

- 语料以几何、拓扑、量子场论、镜像对称、几何朗兰兹为主，分析/概率/数论覆盖少。
- 译文由 AI 辅助生产，经术语冻结与人工抽检，但**未逐段人工校对**；`tier` 与 `flags` 是质量线索，不是保证。
- 公式保留 LaTeX 记号，未统一成 MathML 或 Lean 语法。

## 引用

```bibtex
@misc{shuyi2026,
  title  = {数译 Shuyi: 中文数学译注语料、术语基与资料卡},
  author = {数译 Shuyi contributors},
  year   = {2026},
  url    = {https://github.com/lzxsusy/mathtranslate}
}
```

有 DOI 后请改用 `CITATION.cff` 中的版本。
