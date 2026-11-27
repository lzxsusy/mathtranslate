---
case: D27-08
id: lbook04/concept/ch3-three-motives
set: lbook04
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 页覆盖不足 / 出处定位漂移
---

# 案例 D27-08 · 三个动机：定义正文超出所引页码

> **卡片**：`lbook04/concept/ch3-three-motives`  
> **路径**：`datasets/lbook04/cards/concepts/ch3-three-motives.json`  
> **判定**：minor；确认者 lead（当日核验）  
> **失效模式**：页覆盖不足 / 出处定位漂移  
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `['sources', 0, 'pages']`

**错误版本（卡上原文）**

```text
[
  39,
  40
]
```

**正确版本（已替换）**

```text
[
  39,
  43
]
```

改动理由：definition 含 §2.3（从印刷 41 起、Example 2.1 在 42、G_k 在 43），pages 只到 40。

### 1.2 字段 `['sources', 0, 'pdf_pages']`

**错误版本（卡上原文）**

```text
[
  46,
  47
]
```

**正确版本（已替换）**

```text
[
  46,
  50
]
```

改动理由：印刷 39–43 ↔ PDF 46–50（本章偏移 7）。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

`sources[0].pages` 写 [39,40]，但卡自己的 `definition` 正文包含 §2.3 的内容：
τ′ = γτ、g(z;γτ) = (cτ+d)^k g(z;τ)、例 2.1 的 ℘ 函数与 G_k——这些在印刷 42–43（PDF 49–50）。
按 §4.5，卡的定义正文落在 cited 页之外即算错。根因是只按节标题页（§2 起于 39）填范围，没有覆盖定义实际走到的页。

## 3. 怎么发现的

当日核验第 14 张。子代理发现定义里的模变换与 ℘ 例子在 42–43；lead 用原书 PDF 复核：
印刷 39=PDF 46、40=PDF 47、41=PDF 48、42=PDF 49、43=PDF 50，确认偏移 7。

## 4. 证据锚点

- `bernstein_gelbart_introduction.pdf` 印刷 p.42（PDF 49）：「Example 2.1. The Weierstrass p-function of the lattice Λ is …」
- 卡 `definition` 含 τ′ = γτ 与 g(z;γτ) 的变换式，位于 §2.3（印刷 42–43）。

## 5. 对形式化 / Lean 的提示

形式化这三个动机时，权 k 与 level 要显式；页号不影响陈述，但 §2.3 的模变换是定义的一部分。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
