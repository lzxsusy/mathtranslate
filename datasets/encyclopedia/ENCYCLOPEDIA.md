# 数译百科：词条化语料规范（v0.1）

## 为什么按词条，不按书

按书/按章切，产出的还是「书的压缩版」：读者（和人）拿到的是某本书的目录，训练数据也带着原书的选目与顺序。按**词条**切，每个词条是围绕一个概念的自足单元，可以吸收多本书、多篇论文、多个例子，最终长成一部可检索、可增补、可训练的数学百科。

规则：

- 一个词条 = 一个概念/对象（如「纤维丛」「陈类」「同伦群」「拓扑孤子」），不是一章。
- 词条内部再分层：定义 → 定理（含证明）→ 例子 → 计算 → 物理中的用法 → 坑 → 关联词条 → 出处。
- 同一词条可以由多本书喂养；出处逐条记，不合并成一句「见某书」。
- 词条之间用 `related` 连成网；不复制正文，只给 id 与一句关系说明。

## 目录与文件

```
encyclopedia/
  README.md                 本规范
  taxonomy.md               分类表（顶层类目与词条清单）
  entries/<category>/<slug>.json   一个词条一个文件
  index.jsonl               自动生成的索引（id/title/category/summary）
```

`category` 用两层：`topology/fiber-bundle`、`geometry/manifold`、`qft/anomaly`、`susy/none` 之类，顶层限定为：

`topology`、`geometry`、`algebra`、`qft`、`susy`、`condensed`、`math-phys`。

## 词条 JSON 结构

```json
{
  "id": "topology/fiber-bundle",
  "title": "纤维丛",
  "aliases": ["fiber bundle", "fibration"],
  "category": "topology",
  "summary": "一句话：底空间上局部平凡、纤维为 F 的空间，转移函数给出扭曲。",
  "definition": {
    "text": "自足的定义（中文，首次给英文名）……",
    "notation": "E, B, F, π, U_i, g_ij"
  },
  "theorems": [
    {
      "name": "定理名",
      "statement": "……",
      "proof": {
        "status": "complete | sketch | omitted",
        "steps": [
          {"no": 1, "text": "……", "why": "这一步用的假设/引理"},
          {"no": 2, "text": "……", "why": "……"}
        ],
        "gap_note": "若 status=sketch，写清缺哪一步"
      },
      "sources": [{"book": "Tachikawa", "section": "3.1", "pages": [28, 30]}]
    }
  ],
  "examples": [
    {
      "name": "Hopf 纤维化",
      "setup": "……",
      "computation": [
        {"no": 1, "text": "……", "why": "……"}
      ],
      "result": "S^1 → S^3 → S^2，π_3(S^2)=Z 由此可见。",
      "sources": [{"book": "Tachikawa", "section": "3.2", "pages": [31, 32]}]
    }
  ],
  "physics": [
    {"claim": "规范场是主丛上的联络", "why": "……", "sources": [{"book": "Tachikawa", "section": "3.7", "pages": [44, 44]}]}
  ],
  "pitfalls": ["……"],
  "related": [{"id": "topology/principal-bundle", "why": "主丛是纤维丛的特例"}],
  "sources": [{"book": "Tachikawa, Algebraic Topology for Physicists", "edition": "2024 notes", "url": ""}],
  "rights": "rewritten",
  "status": "draft",
  "reviewed_by": []
}
```

## 写作纪律

1. **自足**：不假设读者读过原书；定义里的每个符号先在 `notation` 或定义正文中交代。
2. **证明要完整**：原书给了完整证明的，按步骤重写并保留每一步的理由；原书只给 sketch 的，补成 `complete` 并标 `补`，或如实写 `sketch` + `gap_note`。
3. **例子要算**：能算出具体数字的例子（同调群、陈数、π_n、配分函数）必须给出计算步骤与结果；能用 sympy/mpmath 复核的，在 `why` 里写复核方式。
4. **改写，不复制**：语句自己组织，连续引用不超过一句（≤60 字），且必须注明出处；不复制原书图、表。
5. **出处到节与页**：`book/section/pages`；页码用 PDF 页码（书内印刷页 = PDF 页 − 5）。
6. **诚实**：没把握的标 `sketch`/`uncertain`，不编造页码与定理编号。
7. **物理联系**只写书里或标准文献支持的，不硬凑。

## 质量门槛（lint 会查）

- id 唯一、category 在允许集合内、title 非空、summary ≤ 120 字；
- 至少 1 个 definition 或 2 个 theorems；
- 每个 theorem 有 `statement`，`proof.status=complete` 时 `steps` ≥ 2；
- 每个 example 有 `computation` ≥ 1 且 `result` 非空；
- 所有 `sources.pages` 为两个整数且落在书的页范围内；
- 连续中文引用与译稿的重合 ≤ 阈值（由 `tools/entry_lint.py` 检查）。
