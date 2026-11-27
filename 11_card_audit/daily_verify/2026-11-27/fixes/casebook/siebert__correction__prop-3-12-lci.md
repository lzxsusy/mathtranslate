---
case: D27-01
id: siebert/correction/prop-3-12-lci
set: siebert
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 出处定位漂移
---

# 案例 D27-01 · 命题 3.12：Gysin 拉回定义的起始页

> **卡片**：`siebert/correction/prop-3-12-lci`  
> **路径**：`datasets/siebert/cards/corrections/prop-3-12-lci.json`  
> **判定**：minor；确认者 lead（当日核验）  
> **失效模式**：出处定位漂移  
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `['pitfalls', 1]`

**错误版本（卡上原文）**

```text
别把 lci 与光滑互换着用：讲义 p.51 起只为 lci 嵌入定义 Gysin 拉回 (3.58)(3.64)，而 Prop 3.12 的 $j_s^!$ 正需要这个工具；光滑只是充分条件。
```

**正确版本（已替换）**

```text
别把 lci 与光滑互换着用：讲义 p.50–51 只为 lci 嵌入定义 Gysin 拉回（(3.58) 在 p.50，(3.64) 在 p.51），而 Prop 3.12 的 $j_s^!$ 正需要这个工具；光滑只是充分条件。
```

改动理由：sources 页码错误：(3.58) 是 Definition 3.4，在讲义 p.50；p.51 只有 (3.64)。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

`pitfalls[1]` 想提醒读者「Gysin 拉回只为 lci 嵌入定义」，却把统一定义的起点写成「p.51 起」。
讲义里 (3.58) 是 Definition 3.4，在 **p.50**；p.51 才出现 (3.64)。作者大概率是按 (3.64) 所在页概括了整组公式，
没有逐页核对 (3.58)——这是「按最后一个公式的页概括整段」的典型漂移。
另按本卡自己的要求，写成「p.50–51 + 两个编号各自页码」比只给起点更抗回查。

## 3. 怎么发现的

当日核验第 1 张（lead 亲自核）。用 `siebert.txt` 按 `\f` 定位 Prop 3.12 时顺手核了 pitfalls 里的 (3.58)(3.64)，
发现 (3.58) 在 PDF 58 页之前的 p.50，与「p.51 起」矛盾。

## 4. 证据锚点

- `datasets/_audit/third_party_2026-11-26/tmp/sources/siebert.pdf` p.50：「Definition 3.4.」及 (3.58) `\iota^![V]:=s_0^*[C_{W/V}]`；PDF p.51 为 (3.64)。
- 卡内 `provenance_note` 写「原书 p.58…对照片 p.50–52 的 Gysin 拉回 (3.58)(3.64)」，本来就承认 50–52，与 pitfalls 的「p.51 起」自相矛盾。

## 5. 对形式化 / Lean 的提示

不涉及定理形式化。若以后把 Gysin 拉回写成 Lean 定义，假设应是 `IsLci`（局部完全交态射），并在 docstring 引 (3.58) 的定义而不是页码。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
