---
case: D27-11
id: glc/concept/fundamental-local-equivalence
set: glc
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 页覆盖不足
---

# 案例 D27-11 · 基本局部等价：相对构造在 p.72

> **卡片**：`glc/concept/fundamental-local-equivalence`  
> **路径**：`datasets/glc/cards/concepts/fundamental-local-equivalence.json`  
> **判定**：minor；确认者 lead（当日核验）  
> **失效模式**：页覆盖不足  
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `['sources', 0, 'pages']`

**错误版本（卡上原文）**

```text
[
  71
]
```

**正确版本（已替换）**

```text
[
  71,
  72
]
```

改动理由：definition 末句的相对构造与 Op(X\{x})^unr 定义在印刷 p.72，pages 只有 [71]。

### 1.2 字段 `['sources', 0, 'pdf_pages']`

**错误版本（卡上原文）**

```text
[
  71
]
```

**正确版本（已替换）**

```text
[
  71,
  72
]
```

改动理由：本集 PDF = 印刷（偏移 0）。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

`definition.text` 末句与 `formulas[2]` 给出相对构造
`KL ⊗_{QCoh(Op^unr)} QCoh(Op^unr_{Ǧ}(X\{x})) → DMod_crit(Bun_G)` 及 `Op(X\{x})^unr` 的定义，
这些在印刷 **72**（PDF 72）；p.71 只到 `KL ≃ IndCoh(Op^unr)` 与 ∗/! 约定。`pages` 与 `pdf_pages` 都只有 [71]，
按 §4.5 属 cited 页覆盖不足。

## 3. 怎么发现的

当日核验第 20 张。子代理比对 definition 末句与 p.71 末行，发现相对构造落在 p.72；lead 复核 `glc.txt`
p.72「Localization should enhance to a relative construction of the form」与 p.71「up to the usual ∗- versus !-IndCoh convention」。

## 4. 证据锚点

- `glc.pdf` p.72 §14.6：「Localization should enhance to a relative construction of the form …」
- p.71 §14.6 末：「up to the usual ∗- versus !-IndCoh convention」

## 5. 对形式化 / Lean 的提示

形式化该等价时要区分 `IndCoh` 与 `QCoh`、∗ 与 ! 的拉回方向；这是卡 pitfalls 里已强调的约定。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
