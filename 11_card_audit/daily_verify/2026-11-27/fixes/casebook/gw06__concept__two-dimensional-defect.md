---
case: D27-10
id: gw06/concept/two-dimensional-defect
set: gw06
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 页覆盖不足 / 出处定位漂移
---

# 案例 D27-10 · 二维缺陷：离散 α,η 的互换在下一页

> **卡片**：`gw06/concept/two-dimensional-defect`<br>
> **路径**：`datasets/gw06/cards/concepts/two-dimensional-defect.json`<br>
> **判定**：minor；确认者 lead（当日核验）<br>
> **失效模式**：页覆盖不足 / 出处定位漂移<br>
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `sources[0].pages`

**错误版本（卡上原文）**

```text
[
  29,
  30
]
```

**正确版本（已替换）**

```text
[
  29,
  31
]
```

改动理由：α 与 η 在对偶下互换的句子在印刷 p.31（PDF 32），pages 少一页。

### 1.2 字段 `sources[0].pdf_pages`

**错误版本（卡上原文）**

```text
[
  30,
  31
]
```

**正确版本（已替换）**

```text
[
  30,
  32
]
```

改动理由：同上（本集 PDF = 印刷 + 1）。

### 1.3 字段 `sources[0].page_note`

**错误版本（卡上原文）**

```text
抛物子群、博雷尔子群与幂幺根（式 (2.57)–(2.63)），以及极大列维情形的离散 $\alpha,\eta$；印刷页 29–30，原文 PDF 第 30–31 页。
```

**正确版本（已替换）**

```text
抛物子群、博雷尔子群与幂幺根（式 (2.57)–(2.63)），以及极大列维情形的离散 $\alpha,\eta$；印刷页 29–31，原文 PDF 第 30–32 页。
```

改动理由：互换句在印刷 p.31，页码区间要覆盖到它。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

`page_note` 声称「印刷页 29–30」覆盖「极大列维情形的离散 α, η」，但 core 陈述
「𝒵(G) 与 Hom(π₁(G),U(1)) 在对偶下互换」在印刷 **31**（PDF 32）；29–30 只到 (2.63) 与「If α=0 … L=G, P=G_C, N=1」。
`pages`/`pdf_pages` 因此各少一页。根因同其他页覆盖问题：按「主要公式结束页」而不是「最后一句定义所在页」填。

## 3. 怎么发现的

当日核验第 19 张。子代理报 page_note 与 definition 末句不一致；lead 用 `gw06.txt` 复核 PDF 31（印刷 30）
的 `L = G` 句与 PDF 32（印刷 31）的 `are exchanged by` 句，并把 `index.jsonl` 里派生的 pdf_pages 一并更新。

## 4. 证据锚点

- `gw06.pdf` 印刷 31（PDF 32）：「The finite groups Z(G) and Hom(π1 (G), U (1)) are exchanged by …」
- 印刷 30（PDF 31）：「If α = 0, we get a special case … L = G, P = G_C, N = 1」

## 5. 对形式化 / Lean 的提示

符号约定 L=G、P=G_C、N=1（卡已述）是形式化时要对齐的；页号不影响陈述。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
