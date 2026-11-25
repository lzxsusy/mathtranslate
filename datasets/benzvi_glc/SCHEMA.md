# benzvi_glc 卡片规范（SCHEMA）

本数据集是 Ben-Zvi 2026 年几何 Langlands 综述的**中文概念卡**。一卡一 JSON，UTF-8，缩进 2 空格，放在 `cards/concepts/<slug>.json`。

## 1. 标识

- `id`：`bzg/concept/<slug>`，slug 用小写字母、数字、连字符，全局唯一。
- `type`：固定 `concept`。
- `track`：`O` / `A` / `B` / `C` / `D` / `E`。
  - O 总览：主定理与证明地图
  - A 谱定理、Fourier 与 Mellin（Abel 玩具模型）
  - B Bun_G、Hecke 与几何 Satake
  - C 谱侧、Hitchin 与谱作用
  - D 因子化、相对 Langlands 与证明架构
  - E 分歧、局部/函数域与物理
- `title`：中文短标题，可夹数学记号。
- `aliases`：至少 1 个别名（英文名、常用记号或旧译名）。
- `summary`：≤ 120 字；超过只 warn，但应尽量压缩。索引与卡片总表直接使用。
- `question`：本卡要回答的问题，以全角 `？` 结尾。

## 2. 正文

- `definition.text`：定义/解释，用 `$...$` 写行内公式。
- `definition.notation`：记号约定；无特别记号可写空串。
- `key_points`：至少 3 条，每条一个独立事实或机制。
- `formulas`：至少 1 条，LaTeX 字符串；JSON 中反斜杠需写成 `\\`。
- `theorems`：数组，可为空。每条：
  - `name`、`statement`、`source`
  - `proof.status`：`complete` / `sketch`
  - `proof.steps`：数组，元素 `{no, text, why}`
  - `proof.gap_note`：`sketch` 必填；说明缺什么，不能写“显然”。
- `pitfalls`：至少 1 条，写易错点、常见误读或记号陷阱。
- `related`：至少 2 个库内 `id`，必须能解析，不能指向自身。
- `sources`：至少 1 条：
  - `book`：统一为 `David Ben-Zvi, What is the Geometric Langlands Correspondence about? (arXiv:2605.23167v1, 2026-05-22, 34 pp., CC BY 4.0)`
  - `section`：如 `§2.5`
  - `pages` 与 `pdf_pages`：等长整数列表；本 PDF 印刷页 = PDF 页
  - `anchor`：`arXiv:2605.23167 §X, p.N`

## 3. 权利与状态

- `rights`：固定 `rewritten`。卡片是中文重写，不复制原文长段；单处引文 ≤ 60 字并注出处。
- `status`：`draft` / `reviewed` / `published`。
  - `reviewed`：内容已逐节对齐原文，但未做外部逐条核验。
  - `published`：还要求 `verification.status != source-only`。
- `verification.status`：`external-confirmed` / `source-only` / `rejected`。
  - 本数据集当前全部 `source-only`：Ben-Zvi 是综述，卡片只对齐该文；外部核验（nLab / Stacks / 五篇 GLC 论文）尚未逐条完成。
- `verification.checked_on`：最近一次对齐日期，`YYYY-MM-DD`。
- `verification.checks`：至少 1 条，记录来源、URL、最后修订日、断言与结论。

## 4. 质量闸门

`tools/lint_benzvi.py` 检查：必填字段、id 前缀、track 枚举、summary 长度（warn）、question 全角问号（warn）、key_points ≥ 3、formulas ≥ 1、pitfalls ≥ 1、theorem 的 proof 字段、related 可解析且非自身、sources 完整、`pages` 与 `pdf_pages` 等长、`published` 的 verification。退出码 0 才入库。

## 5. 生产流程

```bash
python tools/build_cards.py      # 从脚本生成 cards/concepts/*.json 与 verification.jsonl
python tools/normalize_cards.py  # 折叠过度转义的反斜杠（必须在上一步之后）
python tools/build_index.py      # index.jsonl
python tools/gen_docs.py         # taxonomy.md / MAP.md
python tools/lint_benzvi.py      # 0 error 才提交
```

## 6. 与 `datasets/glc` 的关系

`glc` 是陈麟《几何 Langlands 讲义》的 154 张卡（有外部核验）；本数据集是 Ben-Zvi 2026 综述的 42 张卡（source-only）。两者可互链，但**不要**把本数据集的 `source-only` 卡当成已核验事实；Ben-Zvi 明确说自己“err on the side of intuition over precision”，严格陈述应回到 GLC 五篇论文与两卷专著。
