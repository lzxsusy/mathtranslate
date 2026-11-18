# 资料卡 JSON 规范（seidel v1）

一本书的资料卡：Seidel《Fukaya categories and Picard–Lefschetz theory》（2008；公开 PDF 共 334 页）。  
中文译注本的校订材料（187 条译者注、修订总表 40 行）裁成可检索、可自测的卡片。

一张卡一个 JSON 文件，UTF-8，缩进 2 空格，`ensure_ascii=False`，文件名 = id 最后一段。

- 概念卡 `cards/concepts/`，id `seidel/concept/<slug>`
- 推导卡 `cards/derivations/`，id `seidel/deriv/<slug>`
- 勘误卡 `cards/corrections/`，id `seidel/correction/<slug>`

三类卡共用：`id` / `type` / `track` / `title` / `aliases` / `summary` / `question` / `pitfalls` / `related` / `sources` / `rights` / `status` / `provenance_note`。

`track`：`A` A∞ 代数与三角范畴；`B` Floer 理论与 Fukaya 范畴；`C` Picard–Lefschetz 理论；`O` 术语与总览。

`summary` ≤ 120 汉字（去掉公式与空白后计数）；`question` 以问号结尾；`rights` 一律 `rewritten`（自己的转述，不复制原书段落）；`status` 为 `draft` / `reviewed` / `published`。

---

## 概念卡

```json
{
  "id": "seidel/concept/twisted-complex",
  "type": "concept",
  "track": "A",
  "title": "扭曲复形",
  "aliases": ["twisted complex", "Tw A", "扭曲链复形"],
  "summary": "不超过 120 汉字的摘要",
  "question": "卡片正面的自测题，一句话，以问号结尾",
  "definition": {
    "text": "定义的完整陈述，可含 LaTeX 行内公式 $...$ 与行间公式 $$...$$",
    "notation": "符号约定；没有就写空字符串"
  },
  "key_points": ["要点 1", "要点 2", "要点 3"],
  "formulas": ["$$d_T = \\sum_i d_i + \\sum_k q_k$$"],
  "theorems": [
    {
      "name": "命题的名字",
      "statement": "完整陈述",
      "proof": {
        "status": "complete",
        "steps": [
          {"no": 1, "text": "推导的一步", "why": "为什么这一步成立 / 为什么需要它"}
        ],
        "gap_note": ""
      },
      "source": "原书 p.3 §1"
    }
  ],
  "pitfalls": ["真正的易错点，不是废话"],
  "related": ["seidel/concept/karoubi-envelope", "seidel/deriv/twisted-differential"],
  "sources": [
    {"book": "Seidel, Fukaya categories and Picard–Lefschetz theory", "section": "§1", "pages": [3, 4], "anchor": "原书 p.3–4 §1"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "原书 p.3；译者注 A01-02（nLab twisted complex，B 级）。"
}
```

## 推导卡

```json
{
  "id": "seidel/deriv/theorem-a-strategy",
  "type": "derivation",
  "track": "C",
  "title": "定理 A 的证明路线",
  "aliases": ["Theorem A", "PL 归纳计算"],
  "summary": "不超过 120 汉字的摘要",
  "question": "这条推导要回答的问题，以问号结尾",
  "goal": "要得到的结论（一句话）",
  "setup": ["前提 1", "前提 2"],
  "steps": [
    {
      "no": 1,
      "text": "这一步做什么",
      "why": "为什么必须这样 / 依据是什么",
      "locator": "原书 p.4 定理 A",
      "provenance": "A"
    }
  ],
  "result": "推导最终得到什么（可以带公式）",
  "gaps": ["原文只写「可以证明」、没有逐条验证的地方"],
  "pitfalls": ["易错点"],
  "related": ["seidel/concept/lefschetz-fibration", "seidel/concept/vanishing-cycle"],
  "sources": [
    {"book": "Seidel, Fukaya categories and Picard–Lefschetz theory", "section": "§19", "pages": [4, 5], "anchor": "原书 p.4–5"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "原书导言 pp.4–5；译者注 A01-04。"
}
```

`steps` 的 `provenance`：`A` 原文明写；`B` 由原文推出、我们补的中间步；`C` 我们的判断。每步必须有 `locator`（原书页码 + 公式/命题号），至少三步。

## 勘误卡

```json
{
  "id": "seidel/correction/h2-vs-h3",
  "type": "correction",
  "track": "B",
  "title": "协调化障碍类住在 H² 而非 H³",
  "aliases": ["H^3 → H^2", "典范类次数"],
  "summary": "不超过 120 汉字的摘要",
  "question": "初版这里为什么改？",
  "page": 138,
  "original": "初版的错误写法（完整保留，用 $...$ 包公式）",
  "corrected": "改后的写法",
  "why": "为什么改：原文/数学依据",
  "note": "补充说明，可空字符串",
  "pitfalls": ["只改这一处、不要推广到别的 H 上标"],
  "related": ["seidel/concept/fukaya-category", "seidel/correction/..."],
  "sources": [
    {"book": "Seidel, Fukaya categories and Picard–Lefschetz theory", "section": "§10", "pages": [138, 138], "anchor": "原书 p.138；src/chapters/section-10-cd.tex:41"}
  ],
  "rights": "rewritten",
  "status": "draft",
  "provenance_note": "修订总表第 7 条（A05）；已核对英文 p.138。"
}
```

裁稿规则：`original` 与 `corrected` 只留足以辨认差异的片段，不整段抄译文；`why` 必须给依据（英文原文、数学事实或术语表），不得写“更通顺”。

---

## 质检

```bash
python tools/lint_cards.py cards            # 全量
python tools/lint_cards.py cards --strict   # 有 error 退出码 1
python tools/build_index.py                 # 重建 index.jsonl
python tools/render_md.py                   # 重建 md/
```
