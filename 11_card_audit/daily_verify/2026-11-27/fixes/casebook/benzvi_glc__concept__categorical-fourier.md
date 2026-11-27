---
case: D27-09
id: bzg/concept/categorical-fourier
set: benzvi_glc
group: daily-2026-11-27
severity: major
confirmed_by: lead（2026-11-27 当日核验）
modes: 出处无法定位 / 证据强度夸大
---

# 案例 D27-09 · 范畴化 Fourier：被引 §2.1 里没有这条核公式

> **卡片**：`bzg/concept/categorical-fourier`  
> **路径**：`datasets/benzvi_glc/cards/concepts/categorical-fourier.json`  
> **判定**：major；确认者 lead（当日核验）  
> **失效模式**：出处无法定位 / 证据强度夸大  
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `['sources', 0, 'section']`

**错误版本（卡上原文）**

```text
§2.1
```

**正确版本（已替换）**

```text
§1.3
```

改动理由：§2.1（p.8）是「范畴 ≈ Hilbert 空间」的类比，没有 FM 核公式；categorical Fourier 只在 §1.3（p.6）作 general theme 出现。

### 1.2 字段 `['sources', 0, 'pages']`

**错误版本（卡上原文）**

```text
[
  8
]
```

**正确版本（已替换）**

```text
[
  6
]
```

改动理由：同上，locator 改到 p.6。

### 1.3 字段 `['sources', 0, 'pdf_pages']`

**错误版本（卡上原文）**

```text
[
  8
]
```

**正确版本（已替换）**

```text
[
  6
]
```

改动理由：p.6 为 PDF 第 6 页（偏移 0）。

### 1.4 字段 `['sources', 0, 'anchor']`

**错误版本（卡上原文）**

```text
arXiv:2605.23167 §2.1, p.8
```

**正确版本（已替换）**

```text
arXiv:2605.23167 §1.3, p.6
```

改动理由：同上。

### 1.5 字段 `['sources', 0, 'page_note']`

**错误版本（卡上原文）**

```text
（整段存在）
```

**正确版本（已替换）**

```text
原文只在 §1.3（p.6）以「general theme of categorical Fourier transforms」提到此类等价，未写出核公式 $FM_{\mathcal K}(F)=p_{Y!}(p_X^*F\otimes\mathcal K)$；该公式按标准 Fourier–Mukai 变换给出。
```

改动理由：让读者知道核公式不是原文逐字给的，避免把「出处」当成「逐字定义」。

### 1.6 字段 `['verification', 'checks', 0, 'entry']`

**错误版本（卡上原文）**

```text
Ben-Zvi 2026, §2.1
```

**正确版本（已替换）**

```text
Ben-Zvi 2026, §1.3
```

改动理由：section 改 §1.3 后，verification 内同一出处的旧定位必须同步，否则读者仍被指到 §2.1。

### 1.7 字段 `['verification', 'checks', 0, 'asserts']`

**错误版本（卡上原文）**

```text
本卡内容逐句对齐该节；尚未在 nLab / Stacks Project 找到逐字对应的外部核验页。
```

**正确版本（已替换）**

```text
本卡内容依据 §1.3（p.6）的 general theme 整理；核公式为标准的 Fourier–Mukai 变换，该节未逐字写出。
```

改动理由：原 asserts 声称「逐句对齐」，与「该节无核公式」的事实冲突，属证据强度夸大。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

卡把 `FM_𝒦(F) = p_{Y!}(p_X^*F ⊗ 𝒦)` 记在 Ben-Zvi 2026 的 §2.1（p.8）名下。
但 p.8 的 §2.1 是「范畴 / Hilbert 空间」类比（brave new harmonic analysis），既没有这条公式，也没有 Poincaré 丛给出核的说法；
Fourier–Mukai 只在 §1.3（p.6）作为 categorical Fourier transforms 的 general theme 被提到，**不给核公式**（p.13/p.19 的 Mukai transform 是特例）。
这是把「标准定义」挂到了「只谈主题」的节上。修法：section 改 §1.3，加 `page_note` 说明公式按标准 Fourier–Mukai 变换整理，
并把 `verification` 里「逐句对齐该节」的断言改成「依据该节 general theme 整理」。

## 3. 怎么发现的

当日核验第 17 张。子代理在 benzvi.txt 里搜 FM 公式无果，定位到 §1.3 p.6 的主题句与 §2.1 p.8 的类比段；
lead 复核原文两段，并检查 `verification.checks[0]` 仍写着 §2.1，一并改掉（否则旧定位还留在卡里）。

## 4. 证据锚点

- `benzvi.pdf` p.6 §1.3：「This fits in a general theme of categorical Fourier transforms – these are equivalences of (derived) …」
- 同文 p.8 §2.1：「2.1. The language: brave new harmonic and functional analysis.」

## 5. 对形式化 / Lean 的提示

FM 函子形式化需要 `p_{Y!}` 的 proper 性（或取 `p_{Y*}` 并加额外假设）；核 𝒦 应作为参数，不要硬编码 Poincaré 丛。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
