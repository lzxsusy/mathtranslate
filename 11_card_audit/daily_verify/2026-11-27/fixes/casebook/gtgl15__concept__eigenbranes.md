---
case: D27-02
id: gtgl15/concept/eigenbranes
set: gtgl15
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 定理 / 猜想层级混淆
---

# 案例 D27-02 · 本征膜：把定义登记成了定理

> **卡片**：`gtgl15/concept/eigenbranes`<br>
> **路径**：`datasets/gtgl15/cards/concepts/eigenbranes.json`<br>
> **判定**：minor；确认者 lead（当日核验）<br>
> **失效模式**：定理 / 猜想层级混淆<br>
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `theorems[0]`

**错误版本（卡上原文）**

```text
{
  "name": "本征值空间的来源",
  "statement": "对线算符本征的膜，其“本征值”取值为有限维向量空间（Chan–Paton 空间）。",
  "proof": {
    "status": "gap",
    "steps": [],
    "gap_note": "原文 $\\S4.1$ 直接以定义形式给出 eq (4.3)，并说明“术语不好但物理上合理”；未从第一原理证明本征值必为向量空间。"
  },
  "source": "A p.37"
}
```

**正确版本（已替换）**

```text
（整段删除）
```

改动理由：层级错误：eq (4.3) 是定义（原文 §4.1），卡却把它放进 theorems 并标 proof.status=gap；内容与卡内 definition.text 重复。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

eq (4.3)「LB ≅ B⊗V for some vector space V」在原文 §4.1 是**定义**，卡却把它单独列成 `theorems[0]`，
还标 `proof.status = "gap"`、gap_note 自认「未从第一原理证明本征值必为向量空间」。
这是把「定义的一部分」升级成「待证命题」：读者/形式化系统会去找证明，而原文根本没有这条定理。
同时 `definition.text` 说「固定向量空间」、theorem 说「有限维向量空间」，两处措辞也不一致。
本批按最小改动删除 `theorems[0]`（内容已被 `definition.text` 与 `key_points[1]` 覆盖），保留定义原样。

## 3. 怎么发现的

当日核验第 3 张（lead 亲自核）。核对 §4.1 时发现 eq (4.3) 紧跟在「We say that…」之后，是定义句式；
再读 `theorems[0]`，其 statement 与 `definition.text` 同义，且 gap_note 自述「原文直接以定义形式给出」。

## 4. 证据锚点

- `gtgl15.pdf` 印刷/PDF p.37：「We say that the brane B is an eigenbrane of the line operator L if LB = B ⊗ V (4.3) for some vector space V.」
- 卡内 `theorems[0].proof.gap_note`：「原文 §4.1 直接以定义形式给出 eq (4.3)…未从第一原理证明本征值必为向量空间。」

## 5. 对形式化 / Lean 的提示

Lean 里应写成 `def IsEigenbrane (L : LineOp) (B : Brane) : Prop := ∃ V : Type, …`；不要 `theorem … := by sorry`，否则定义被误当开放问题。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
