---
case: D27-04
id: functoriality/concept/strip-shrinking
set: functoriality
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 出处定位漂移
---

# 案例 D27-04 · 带收缩：定理页码整体后移两页

> **卡片**：`functoriality/concept/strip-shrinking`  
> **路径**：`datasets/functoriality/cards/concepts/strip-shrinking.json`  
> **判定**：minor；确认者 lead（当日核验）  
> **失效模式**：出处定位漂移  
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `['theorems', 0, 'source']`

**错误版本（卡上原文）**

```text
原书 p.25 §3.5.2
```

**正确版本（已替换）**

```text
原书 p.27 §3.5.2
```

改动理由：§3.5.2 与 eq (62) 在印刷/PDF p.27（页脚 27），p.25 是 §3.5 的开头（(58) 附近）。

### 1.2 字段 `['theorems', 1, 'source']`

**错误版本（卡上原文）**

```text
原书 p.26 §3.5.2
```

**正确版本（已替换）**

```text
原书 p.28 §3.5.2
```

改动理由：[WW15, Theorem 5.1] 的推广段落在 p.28（页脚 28）。

### 1.3 字段 `['provenance_note']`

**错误版本（卡上原文）**

```text
原书 p.25–26 §3.5.2（定理 1.0.1、定理 5.1 的转述）；公式 (62) 逐字取自中译本 chapter3.tex。
```

**正确版本（已替换）**

```text
原书 p.27–28 §3.5.2（定理 1.0.1 在 p.27、定理 5.1 的转述在 p.28）；公式 (62) 逐字取自中译本 chapter3.tex。
```

改动理由：provenance_note 重复了同一处 p.25–26；按已核实的 p.27/p.28 同步。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

两处 `source` 与一处 `provenance_note` 都按 §3.5 的**起始页**（p.25–26）填，而两个定理分别在 p.27（定理 1.0.1 / eq (62)）
和 p.28（[WW15, Theorem 5.1] 的转述）。作者很可能只看了节标题页就概括整节，没有翻到定理正文。
`provenance_note` 又原样复制了同一个错范围，属「同一错误在多个字段重复」——修的时候必须一起改，否则两个版本并存。

## 3. 怎么发现的

当日核验第 5 张。子代理逐条比对 arXiv:2210.11159v1 的 §3.5.2，发现 eq (62) 在 p.27；
lead 复核 p.28 的 [WW15, Theorem 5.1] 段，并发现 `provenance_note` 仍写 p.25–26（子代理只报了 theorems[].source）。

## 4. 证据锚点

- arXiv:2210.11159v1 p.27：「3.5.2. Categorification commutes with composition.」
- 同文 p.28：「Woodward showed in [WW15, Theorem 5.1] that under the same hypotheses of (62), and assuming …」

## 5. 对形式化 / Lean 的提示

形式化带收缩时要显式「复合嵌入」前提（卡 pitfalls 已述）；定理本身的页号不影响陈述。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
