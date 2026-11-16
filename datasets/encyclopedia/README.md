# 数译百科：按词条组织的数学语料

这里不是某本书的电子版，也不是译本的搬运。它是**按概念词条**组织的语料库：一个词条吸收多本书、多篇文章、多个来源的内容，用自己的话重写成一个自足的知识单元。分类轴是概念（流形、纤维丛、示性类、反常……），不是书或章节。

第一本供料是立川裕二《物理学家用代数拓扑》（Tachikawa, *Algebraic Topology for Physicists*, 2024 notes）。之后会接入更多教材、讲义、带答案的习题集与人工精选的例子。

## 为什么这样做

- **中文研究级数学语料稀缺**。英文有 Mathlib、NumPy 文档、arXiv 全文；中文的系统性数学说明很少，超对称场论方向尤其少。
- **词条比章节更适合训练**：一个词条自带定义、定理、证明、例子、物理联系和常见错误，可以独立检验，不必依赖上下文。
- **组织方式是原创的**：选哪些概念、如何串联、举什么例子、怎么讲清楚——这些是我们的工作；原书的思想与事实属于公共知识。

## 词条格式

每个词条是一个 JSON 文件，路径 `entries/<category>/<slug>.json`，完整规范见 [`ENCYCLOPEDIA.md`](ENCYCLOPEDIA.md)。核心字段：

| 字段 | 内容 |
|---|---|
| `id` / `title` / `aliases` | `category/slug`、中文名、别名 |
| `category` | `topology` / `geometry` / `algebra` / `qft` / `susy` / `condensed` / `math-phys` |
| `summary` | 一句话（≤160 字） |
| `definition` | 自足定义 + 符号表 |
| `theorems[]` | 陈述 + 证明（`complete` 逐步给 `why`；`sketch` 必须写 `gap_note`）+ 出处 |
| `examples[]` | 可复算的例子：`computation` 步骤 + `result` |
| `physics` | 物理联系（规范场、反常、拓扑相……） |
| `pitfalls` | 常见误解 |
| `related` | 相关词条与理由 |
| `sources` | 书目/页码 |
| `rights` / `status` | `rewritten`；`draft` / `reviewed` |

## 写作纪律

1. **自足**：读者只看这一条就能懂，符号先交代。
2. **证明要完整**：原书有证明的写成 `complete`，每步给理由；原书没证或只有轮廓的，写 `sketch` 并在 `gap_note` 里说清缺什么。不许把"显然"当证明。
3. **例子要算**：给出具体步骤和结果（同调群、π_n、陈数、χ、系数），不是"例如可以证明"。
4. **改写，不复制**：不连续照抄原文或任何译本（引用 ≤60 字并注出处）；不复制原书图，需要图时用文字描述或重画。
5. **页码真实**：`sources.pages` 用 PDF 页（印刷页 = PDF − 5），能在原书里对上。
6. **诚实**：拿不准的标 `draft` 或写进 `pitfalls`，不冒充已证。

## 权利

- 词条的**中文表述与组织结构**由数译撰写，按 `rights: rewritten` 处理：可 CC BY 4.0 引用与训练。
- 原书的思想、定义、定理本身是公共知识；**原书的表达、选目、图与译本**仍受版权保护，本库不复製。
- 词条中若引用原文，单处 ≤60 字并注出处；累计引用不超过词条的 10%。
- 权利人如认为某条越界，按 [`../COMPLIANCE.md`](../COMPLIANCE.md) §8 撤下。

## 生产流程

1. 从总表 [`taxonomy.md`](taxonomy.md) 取一个词条（含出处页码）；
2. 读对应章节（`chapters/` 的页标记用于定位），列出定义、定理、证明、例子；
3. 用自己的话写 JSON，证明补全，例子算一遍；
4. `python tools/entry_lint.py datasets/encyclopedia/entries` 校验；
5. 人工复核后标 `reviewed`。

## 现状

- 类目与词条总表：`taxonomy.md`（约 45 条，SUSY 类目先占位）。
- 第一批 **17 个词条**：74 条定理、50 个例子，其中 59 条证明为 `complete`、15 条为 `sketch`（均写 `gap_note`）。
  - 几何：流形（示范，已复核）、定向、连通和、李群；
  - 丛论：纤维丛、主丛、向量丛、切丛、自旋结构；
  - 同伦：同伦群、同伦长正合列、Hopf 纤维化、覆盖空间；
  - 上同调：微分形式、de Rham 上同调、Stokes 定理、Mayer–Vietoris。
- 状态：`manifold` 为 `reviewed`，其余 16 条为 `draft`，等独立复核后逐条升级；复核重点是「补证」部分（标【补】的步骤）与页码。
- 后续：同调与示性类、Chern–Simons、K 理论与十重分类、指标定理；超对称场论词条（用户指定的长期重点）。

## 校验

```bash
python tools/entry_lint.py datasets/encyclopedia/entries --index
```

检查：id/路径一致、类目合法、summary 长度、定理与证明完整性、例子是否有计算与结果、页码范围、与译稿的 12 字重合告警；`--index` 生成 `index.jsonl`。
