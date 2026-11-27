# goresky04 —— 为物理学家讲述的朗兰兹猜想（Goresky，IAS 2004）

> 一句话：这是一包「从零到一」的导读卡。它不假设你知道朗兰兹猜想是什么，只假设你会算矩阵的特征值。

Mark Goresky 于 2004 年 3 月 8 日在 I.A.S. 给一批物理学家讲了几次课，会后扩写成这份 **20 页的讲义体综述**。
本文的正文停在 §8.2–8.7 的六个标题上（作者自述 work in progress），§8.5 正是「几何 Langlands」。
这包卡把这篇讲义拆成 22 张可独立使用的卡，让「两侧分别是什么、为什么需要平代环、$n=2$ 为什么能做成」
这三件事可以一张一张地读。

## 一卡一问

- **概念卡**回答三件事：它是什么（定义）、为什么需要它（要点）、它把哪一步往前推了（定理与陷阱）。
- **推导卡**回答两件事：这一步怎么算（steps，每步带 why）、算完得到什么（result）。
- 每张卡都带原文页码锚（`A p.N` 或 `B p.N`），一个人可以在 10 分钟内核对卡与原文是否一致。

## 底本与规模

| 项 | 内容 |
| --- | --- |
| 底本 | Mark Goresky, *Langlands' Conjectures for Physicists*, I.A.S. 讲座（2004-03-08）扩写稿，20 页，dvips 排版 |
| 来源级别 | **B**：作者自印讲义（work in progress），非正式出版物；PDF 不入库，只留书目与出处 |
| 译本 | `08_source_code/SY02-42_为物理学家讲述的朗兰兹猜想（Goresky 2004 IAS 讲义）/`（23 页，译注 11 条） |
| 卡数 | **22 张**：概念 18 + 推导 4，五轨 O/A/B/C/D |
| 页码 | 印本页 1–20，PDF 页 = 印本页（偏移 0） |
| 状态 | 全部 `draft` + `rewritten`（本库重写的译注卡，不复制原文） |

## 30 秒入口

| 你想知道 | 读这张 |
| --- | --- |
| 猜想本身到底说什么 | `concept/langlands-conjecture-statement` |
| 左右两侧各是什么 | `concept/two-sides-map` |
| $n=2$ 为什么能证 | `concept/eichler-shimura-theorem` |
| $n\ge3$ 卡在哪 | `concept/obstruction-n-ge-3` |
| 几何朗兰兹换掉了什么 | `concept/geometric-langlands` |

## 三条阅读路径

**路径 1（给物理学家，40 分钟）**
`langlands-conjecture-statement` → `two-sides-map` → `zeta-function-of-variety` → `hecke-eigenform` → `eichler-shimura-theorem`。
跳过 §3 的域分类，直接从「左边是特征值、右边是特征值」入手。

**路径 2（给代数几何背景，90 分钟）**
`global-and-local-fields` → `etale-cohomology` → `frobenius-element` → `satake-parameter` → `eichler-shimura-theorem` → `geometric-langlands`。
这条路径把「为什么需要平展上同调」讲透。

**路径 3（给做朗兰兹的人，查缺）**
直接看 `obstruction-n-ge-3`（$n\ge3$ 的障碍）与 `geometric-langlands`（换域之后），
再回看 `deriv/hecke-to-frobenius`（两侧特征值如何逐素数对齐）。

## 术语三条硬约定

1. **adele → 平代环**（不是「阿代尔」）。限制直积条件不能省。
2. **cuspidal → 尖点的**；尖点形式 = cusp form。「尖点」指的是模曲线在无穷远处的尖点。
3. **étale → 平展**。平展上同调必须 $\\ell\\neq p$，否则会退化。

## 生产与校验

```bash
cd datasets/goresky04
python workflow/cards_oa.py && python workflow/cards_b.py && python workflow/cards_cd.py
python tools/lint_cards.py cards --strict      # 必须 OK: 0 error
python tools/build_index.py                     # 生成 index.jsonl
python tools/render_md.py                       # 生成 md/
```

## 与其它包的关系

| 包 | 关系 |
| --- | --- |
| `sandvik25`（SY02-40） | 几何 Langlands 的现代化版本：反球模的三造函子 |
| `lafforgue02`（SY02-39） | 函数域情形的朗兰兹（Drinfeld 的 $\GL(2)$ 情形） |
| `raskin_lcft`（SY99-04） | 上同调类域论：几何 Langlands 的「$\GL(1)$ 影子」 |

**建议顺序**：先读本包（从零到一）→ 再读 `raskin_lcft`（几何的入口）→ 最后读 `sandvik25`（现代构造）。

## 权利

卡片是本库重写的译注卡（`rights: rewritten`），不是原文复制。底本为作者自印讲义，
本库只收录书目信息与页码锚点，**不收录 PDF**。
