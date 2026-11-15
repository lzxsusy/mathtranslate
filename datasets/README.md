# 数译数据集（datasets/）

> 本目录把「译本」升级为「可训练、可评测、可追溯的学术翻译数据集」。
> 规则自 2026-11-16 起生效；与 [../COMPLIANCE.md](../COMPLIANCE.md) 冲突时以 COMPLIANCE 为准。

## 0. 一句话

一段原文、一段译文、一条「为什么这么译」的理由，三样齐了才算数据；缺了理由，就只是文本。

## 1. 五类数据

| 目录 | 内容 | 一条记录 = 什么 | 单条上限 |
|---|---|---|---|
| `parallel/` | 原文片段 ↔ 译文片段 ↔ 译法理由 | 一个句群/公式块的对齐单元 | 原文 600 字、译文 600 字 |
| `deepread/` | 精读卡：命题、证明骨架、补步、易错点、前置知识 | 一个可独立复述的数学单元 | 正文 4,000 字 |
| `highlights/` | 高光标注：哪段论述精彩、哪段证明难、难在哪、怎么破 | 一处「值得单独讲」的位置 | 正文 1,500 字 |
| `traces/` | 事件级工作流：读→写→编译→报错→改→验 | 一次可重放的完整对话流 | 事件 500 条 |
| `kg/` | 概念/定理/证明/人物/文献节点与带证据的边 | 一个节点或一条边 | 正文 500 字 |
| `bench/` | 带评分细则的 held-out 评测题 | 一道题 | 题目 800 字 |

`bench/` 与训练集严格隔离：出题时不得使用 `parallel/`、`deepread/` 中已出现的同一段落。

## 2. 权利分层（写进每条记录）

- `rights: "self"` — 自产（导读、术语裁决、精读卡、图谱边、评测题）。可 CC BY 4.0，可商用训练。
- `rights: "arxiv:<id>"` — 原文来自 arXiv。**逐篇**核对 arXiv 许可（`https://arxiv.org/abs/<id>` 页脚）；只有 CC BY / CC0 的原文片段可随数据集公开，其余只存 `src_ref` 链接与不超过 300 字的引用。
- `rights: "book"` — 在版图书（含扫描件、出版社 PDF）。**只进 `_internal/`，不发布、不进公开数据集、不随权重发布**；片段引用 ≤ 200 字，且只用于本机训练与人工研读。

发布前用 `tools/ds_publish.py --check` 过滤：`rights: "book"` 与未确认许可的 `arxiv:*` 记录一律不出现在公开目录。

## 3. 目录结构

```
datasets/
├── README.md                  # 本文件
├── schema/                    # 五类记录的 JSON Schema
├── parallel/<pkg>.<split>.jsonl
├── deepread/<pkg>.<split>.jsonl
├── highlights/<pkg>.<split>.jsonl
├── traces/<pkg>.<topic>.jsonl
├── kg/<pkg>.<split>.jsonl
├── bench/<pkg>.<split>.jsonl
├── _internal/                 # book 权利，永不发布（.gitignore）
└── workflow/                  # 生产协议、提示词、审校清单
```

`<pkg>` 用 `08_source_code/` 里的工程名（如 `SY05-25`）；`<split>` 取 `train|dev|test`，`bench` 固定 `test`。

## 4. 生产协议（每类数据都走这五步）

1. **选段**：从 `08_source_code/<pkg>/源码/` 取 TeX 段落；原文取 `originals_pkg/07_originals/` 或 arXiv `/e-print/` 的 LaTeX 源，**不入库**。
2. **对齐**：句群级对齐，公式块整体对齐；跨页/跨节处标 `alignment: "block"` 并给上下文。
3. **写理由**：至少一条 `why`，说明「为什么这样断句/选词/补主语/保留语序」；术语选择必须给 `alternatives` 与取舍。
4. **自检**：`python tools/ds_lint.py datasets/` 零错误；引用行号必须存在。
5. **双人复核**：`reviewed_by` 至少两人（生产 + 审校），`status` 从 `draft` → `reviewed` → `published`。

生产提示词与审校清单一律放 `workflow/`，不散落在会话里。

## 5. 质量门禁

`tools/ds_lint.py` 强制：

- `id` 全局唯一；必填字段齐全；
- 引文字数上限（见 §1）与 `rights` 一致；`book` 记录不得出现在 `_internal/` 之外；
- `src_ref` 的 arXiv 号能被 `^[a-z-]+(\.[A-Z]{2})?/\d{7}$|^\d{4}\.\d{4,5}$` 解析；
- `evidence[].file` 必须存在于仓库且行号不超过文件行数；
- 文本中不得出现本机绝对路径（`C:\Users\...`）、口令、邮箱；
- 记录不得是整章/整节全文粘贴（单条 ≤ 6,000 字）。

## 6. 引用与署名

数据条目引用格式：

```
数译数据集 v0.1（2026-11-16），<pkg> <split> <id>，
https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/datasets/<...>.jsonl
```

原文权利归原作者与出版方；数据集只主张自产部分（理由、精读、图谱、评测题）的 CC BY 4.0。

## 7. 版本

- `v0.1`（2026-11-16）：五类 schema + SY05-25 试点 + 校验器。
- 后续见 [CHANGELOG.md](../CHANGELOG.md)。
