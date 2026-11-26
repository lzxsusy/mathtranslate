# 几何 Langlands 猜想 I 资料卡规范（glc1 SCHEMA v1）

一卡一 JSON，UTF-8，缩进 2，`ensure_ascii=False`。本规范沿用 [`../glc/SCHEMA.md`](../glc/SCHEMA.md) v1 的字段体系，只改三处：`id` 前缀、`track` 枚举、以及 `sources` 的定位方式（本集底本是 arXiv 预印本，**印刷页 = PDF 页**，且每卡必须锚到仓内译文 `源码/chunks/chNN.tex`）。

## 1. 概念卡必填字段

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | `glc1/concept/<slug>`，slug 小写连字符 |
| `type` | string | `"concept"` |
| `track` | string | `A B C D E F` 之一（见 §2） |
| `title` | string | 中文标题，可含公式 |
| `aliases` | string[] | ≥1，含英文名与常见译名 |
| `summary` | string | ≤120 汉字，一句话说清"是什么/为什么重要" |
| `question` | string | 以问号结尾，这张卡要回答的问题 |
| `definition.text` | string | 定义正文；数学用 `$...$` / `$$...$$` |
| `definition.notation` | string | 记号说明（归一化、符号约定） |
| `key_points` | string[] | ≥3，每条一个独立断言 |
| `formulas` | string[] | ≥1，关键公式 |
| `theorems` | object[] | 结构见下；纯定义卡可为空数组 |
| `pitfalls` | string[] | ≥1，常见错误 |
| `related` | string[] | ≥2，必须是本集内可解析的 `id` |
| `sources` | object[] | ≥1，见 §3 |
| `rights` | string | 固定 `"rewritten"` |
| `status` | string | `draft` / `reviewed` / `published` |
| `verification` | object | 见 §4；`published` 必填 |

`theorems[]`：`name`、`statement`、`proof{status, steps[], gap_note}`、`source`。
- `proof.status` 只能是 `complete` 或 `sketch`；`sketch` 必须给 `gap_note`（原文把证明推给了谁、哪一句说明没证）；
- `steps[]` 每条 `{no, text, why}`：`text` 这一步做什么，`why` 为什么可以这样做；
- 原文把证明整条交给引文的（如"这是 [AGKRRV, Cor. 14.4.10]"），`status` 记 `sketch`，`gap_note` 写明引用出处。

## 2. track 划分（本集专用）

| track | 含义 | 覆盖内容 |
| --- | --- | --- |
| A | 自守侧 | $\mathrm{Bun}_G$、$\det_{\mathrm{Bun}_G}$、半步扭曲 D 模、Betti 层 $\mathrm{Shv}^{\mathrm{Betti}}_{1/2,\mathrm{Nilp}}$、$i^L$ |
| B | 谱侧 | $\mathrm{IndCoh}_{\mathrm{Nilp}}$、$\mathrm{LS}_{{}^LG}$、奇异支撑、幂零锥、谱作用与 $\mathrm{Loc}^{\mathrm{spec}}$ |
| C | Langlands 函子 | 真空 Poincaré 层、$\mathrm{coeff}^{\mathrm{Vac}}$、$L_{G,\mathrm{coarse}}$、$L_G$、GLC 猜想、唯一性刻画 |
| D | 有界性与 $t$-结构 | 振幅界、可截断栈、Cousin 滤过、受限变形 $\mathrm{LS}^{\mathrm{restr}}$、$t$-正合性 |
| E | 版本比较与缓增 | Betti 函子与 Betti GLC、de Rham ⟹ Betti、四版本等价、缓增子范畴、奇迹函子 |
| F | Hecke 特征层 | 特征层范畴与 $F_\sigma$、特征闭链 $\mathrm{CC}$、半单性、微局部茎 |

## 3. sources[] 字段

`book`（文献名，固定写 `Gaitsgory–Raskin, GLC I (arXiv:2405.03599v3)`）、`section`（节号或条目号）、
`pages`（印刷页）、`pdf_pages`（PDF 页；本底本印刷页 = PDF 页，两者应相同）、
`anchor`（锚点，如 `源码/chunks/ch03.tex（定理 1.6.2）`）。
`pages` 与 `pdf_pages` 为 list 时长度必须一致。

## 4. verification（本集口径）

```json
"verification": {
  "status": "source-only | external-confirmed",
  "checked_on": "2026-11-25",
  "checks": [
    {"source": "原文", "entry": "§1.6", "asserts": "卡内哪条断言", "verdict": "match"}
  ]
}
```

- 本集**以原文为准**，默认 `source-only`：卡片与原文逐句对齐，但不声称外部权威已确认。
- 只有当某条断言能在 A 级文献的公开页面（如作者的后续论文、会议论文集）逐字找到时，才记 `external-confirmed`，并写出"哪句支持哪条"。
- `published` 的卡必须 `external-confirmed`；本集首批一律 `reviewed` + `source-only`。

## 5. 数学写作规则

1. 行内 `$...$`、行间 `$$...$$`；**只用 MathJax 标准宏**，不得出现译本的 LaTeX 宏（`\Bun`、`\LG`、`\Dmodh`、`\IndCoh` 等一律展开成 `\operatorname{...}`）。
2. 原文的 $\check G$ 在卡内统一写作 ${}^LG$（`{}^LG`）。
3. 引用原文编号写「定理 1.6.2」「注 2.3.5」，页码写「p.16」。
4. 记号必须显式：$\mathrm{D\!-\!mod}^{1/2}$ 的 $1/2$ 是半步 twist；$\mathrm{LS}^{\mathrm{restr}}$ 是受限变形；$\heartsuit$ 指 $t$-结构的心。
5. 中文全角标点；公式内英文标点。
6. 不写"显然""易见"；每一步为什么成立写进 `why`。
7. **不做超出原文的推广**：卡片陈述必须与原文该条一致，不加条件、不加等价、不举原文没有的例子。原文明确标为"新结果"的（定理 6.1.3 (5)）必须在 `key_points` 里保留这一标注。

## 6. 校验

`tools/lint_glc1.py` 检查：必填字段、id 前缀、track 枚举、summary 长度、`key_points`/`formulas`/`pitfalls` 下限、
证明步骤字段、`related` 可解析、sources 完整性、pages/pdf_pages 对齐、verification 合法性、以及**禁用宏扫描**。
**0 error 才允许入库**。
