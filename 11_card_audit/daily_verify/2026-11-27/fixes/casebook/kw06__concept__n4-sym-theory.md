---
case: D27-03
id: kw/concept/n4-sym-theory
set: kw06
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 出处定位漂移
---

# 案例 D27-03 · N=4 超杨–米尔斯：(2.14) 的页号（第二次修改）

> **卡片**：`kw/concept/n4-sym-theory`<br>
> **路径**：`datasets/kw06/cards/concepts/n4-sym-theory.json`<br>
> **判定**：minor；确认者 lead（当日核验）<br>
> **失效模式**：出处定位漂移<br>
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `theorems[0].source`

**错误版本（卡上原文）**

```text
B p.7–11（eq (2.14) 在 p.11）
```

**正确版本（已替换）**

```text
B p.7–10（eq (2.14) 在 p.10）
```

改动理由：eq (2.14) 在 PDF 11（页脚「10」），即印刷 p.10；p.11 是 (2.15)。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

`theorems[0].source` 原写「B p.7–11（eq (2.14) 在 p.11）」，但 (2.14) 在 PDF 第 11 页、页脚印的是 **10**；
p.11（PDF 12）才是 (2.15)。这是 PDF/印刷页偏移（+1）导致的 off-by-one。
需要说明：2026-11-26 批次已把该字段从 `B p.6` 改成 `B p.7–11（…p.11）`，当时把 (2.14) 记到了 p.11；
本批核对页脚后改为 p.10。按 WORKFLOW §9，这属于同一张卡的第二次修改，历史 fix_log 不改，
`datasets/_audit/third_party_2026-11-26/tools/verify_final.py` 因此会对本条报 1 个 STALE（预期，见施工说明）。

## 3. 怎么发现的

当日核验第 4 张。子代理报「定理 source 疑似 off-by-one」，lead 用 `kw06.txt` 抽 PDF 10/11/12 三页页脚与
(2.14)(2.15) 位置复核：PDF 11 页脚 10 且 (2.14) 在该页，PDF 12 页脚 11 且 (2.15) 在该页。

## 4. 证据锚点

- `kw06.pdf` PDF p.11（页脚 10）：`(2, 1, 4) ⊕ (1, 2, 4). (2.14)`；PDF p.12（页脚 11）：`(2.15)`。
- 卡内 `theorems[1].source` 写「B p.11 eq (2.15)」，与本条修正后自洽。

## 5. 对形式化 / Lean 的提示

与 Lean 无关；若把 (2.14) 写成表示分解，注意源是 (2,1,4̄)⊕(1,2,4)（本卡 11-26 已修 statement）。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
