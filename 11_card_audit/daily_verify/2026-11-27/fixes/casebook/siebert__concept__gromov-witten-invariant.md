---
case: D27-06
id: siebert/concept/gromov-witten-invariant
set: siebert
group: daily-2026-11-27
severity: major
confirmed_by: lead（2026-11-27 当日核验）
modes: 适用范围遗漏 / 条件替换
---

# 案例 D27-06 · GW 不变量的形变不变性：lci 被换成了「连通」

> **卡片**：`siebert/concept/gromov-witten-invariant`<br>
> **路径**：`datasets/siebert/cards/concepts/gromov-witten-invariant.json`<br>
> **判定**：major；确认者 lead（当日核验）<br>
> **失效模式**：适用范围遗漏 / 条件替换<br>
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `pitfalls[4]`

**错误版本（卡上原文）**

```text
GW 不变量的形变不变性只在『连通基底 + 代数等价』的意义下成立（Prop 3.12），不是任意同调类扰动下不变。
```

**正确版本（已替换）**

```text
GW 不变量的形变不变性只在『lci 基底 + 代数等价』的意义下成立（Prop 3.12），不是任意同调类扰动下不变；原文并不要求基底连通。
```

改动理由：Prop 3.12 的假设是「If S is lci」；卡删掉 lci、换成「连通」，与卡 1 勘误「讲义原文也没有『同一连通分支』这一条」直接冲突。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

Prop 3.12 的假设是「S is lci」，结论是对**所有** s, s′ 有代数等价——不要求 S 连通。
`pitfalls[4]` 写成「只在『连通基底 + 代数等价』下成立」：删掉了 lci，加入了源里没有的连通。
更要命的是同批第 1 张卡（prop-3-12-lci 勘误）明确写「讲义原文也没有『同一连通分支』这一条」，
两卡对同一命题给出相反读法——这是跨卡一致性检查能抓到的典型冲突。

## 3. 怎么发现的

当日核验第 12 张。子代理报 major 后，lead 用 `siebert.txt` p.58 逐字复核 Prop 3.12 原文，
并把它与第 1 张勘误卡的陈述对照，确认「连通」是新增条件、lci 是丢失条件。

## 4. 证据锚点

- `siebert.pdf` p.58：「Proposition 3.12. If S is lci, then for all s, s′ we get an algebraic equivalence (3.121) [Ms]virt ∼ [Ms′]virt in A∗(M).」
- 同批 `siebert/correction/prop-3-12-lci` 的 corrected 文本亦写「讲义原文也没有『同一连通分支』这一条」。

## 5. 对形式化 / Lean 的提示

形式化 Prop 3.12 需要 `IsLci`（或 `Smooth ⇒ IsLci`）假设；连通性不在假设里，不要为了「同分支」再加 `ConnectedSpace`。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
