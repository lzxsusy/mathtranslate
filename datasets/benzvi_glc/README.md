# benzvi_glc · Ben-Zvi 几何 Langlands 综述资料卡

底本：David Ben-Zvi, *What is the Geometric Langlands Correspondence about?*
AMS Current Events Bulletin, arXiv:[2605.23167v1](https://arxiv.org/abs/2605.23167)（2026-05-22，34 页，CC BY 4.0，Elliot Kienzle 插图）。

本目录把这篇综述拆成 **42 张中文概念卡**，用来回答“几何 Langlands 到底在说什么、证明卡在哪、哪些部分今天能形式化”。卡片是中文重写（`rights: rewritten`），不是原文翻译，也不替代五篇 GLC 论文与两卷专著。

## 规模

| 轨道 | 名称 | 数量 |
| --- | --- | ---: |
| O | 总览：主定理与证明地图 | 4 |
| A | 谱定理、Fourier 与 Mellin（Abel 玩具模型） | 8 |
| B | Bun_G、Hecke 与几何 Satake | 8 |
| C | 谱侧、Hitchin 与谱作用 | 8 |
| D | 因子化、相对 Langlands 与证明架构 | 8 |
| E | 分歧、局部/函数域与物理 | 6 |
| **合计** | | **42** |

## 核验状态

| 状态 | 数量 | 含义 |
| --- | ---: | --- |
| `external-confirmed` | 0 | 尚未逐条对照 nLab / Stacks Project / GLC 五篇论文 |
| `source-only` | 42 | 已逐节对齐 Ben-Zvi 原文，锚到节与页 |
| `rejected` | 0 | — |

全部卡片 `status: reviewed`。**这是“读懂综述”的卡，不是“已核验定理”的卡**。Ben-Zvi 在文中自述 *“I consistently err on the side of intuition over precision”*；需要严格陈述时，回到：

- GLC I：Gaitsgory–Raskin, *A stacky approach to crystals* / GLC 系列
- GLC II–V：arXiv 五篇（GR24a、ABC+24b、CCF+24、ABC+24a、GR24b）
- 两卷专著 *Geometric Langlands*（Gaitsgory–Raskin 等）

## 目录

```text
benzvi_glc/
├── README.md
├── SCHEMA.md
├── index.jsonl              # 一行一卡（id/type/track/title/summary/path）
├── verification.jsonl       # 42 条来源对齐记录
├── taxonomy.md              # 按轨道分组的卡片总表
├── MAP.md                   # related 依赖图（mermaid）
├── cards/concepts/*.json    # 42 张卡
└── tools/
    ├── build_cards.py       # 卡片源（改内容改这里）
    ├── normalize_cards.py   # 折叠过度转义
    ├── build_index.py
    ├── gen_docs.py
    └── lint_benzvi.py
```

## 复现

在本目录下：

```bash
python tools/build_cards.py
python tools/normalize_cards.py
python tools/build_index.py
python tools/gen_docs.py
python tools/lint_benzvi.py
```

当前结果：`cards=42 errors=0 warnings=0`。

## 怎么用

- 想快速知道 GLC 的陈述：先读 `O` 轨的 `glc-overview`、`glc-statement`、`proof-map`。
- 想理解“为什么是 Fourier–Mukai 的范畴化”：读 `A` 轨，从 `spectral-theorem` 到 `gl1-derham-glc`。
- 想理解几何侧与谱侧：读 `B`、`C` 两轨；`D` 轨解释五篇论文的分工。
- 想找形式化切口：优先看 `E` 轨与 `C` 轨的 `indicoh-nilpotent-support`、`D` 轨的 `relative-langlands`；但注意这些只是语义地图，不是 Lean 声明。

## 与 `datasets/glc` 的区别

- `datasets/glc`：陈麟《几何 Langlands 讲义》154 张卡，66 张有外部核验，是“教材级”资料。
- 本目录：Ben-Zvi 2026 综述 42 张卡，全部 `source-only`，是“研究地图级”资料，适合定位问题与证明架构，不适合直接引用为定理来源。
