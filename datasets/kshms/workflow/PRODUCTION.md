# kshms · 制作流程（workflow v1）

本数据集由「中译注本」反向索引而来：先有逐页核对过的中文译本，再从译本的条款顺序与原文页码，
一条一条抽成卡。流程刻意保持可重跑——所有卡片的 `kind_no`、原文页码、`anchor` 都由机器对齐，
人只负责写内容。

## 0. 前置产物

| 产物 | 位置 | 作用 |
| --- | --- | --- |
| 底本 PDF | arXiv:math/0011041v2（66 页） | 页码基准；`pages` 字段一律指它的页脚数字 |
| 中译注本 | `08_source_code/SY01-25_…/源码/` | `anchor` 指向这里的 `chunks/chNN.tex` 行区间 |
| 逐页文字 | 译注本工程 `工程文件/work/pages/pNNN.txt` | 抽原文页码、核对题头 |
| 条款清单 | 译注本工程 `工程文件/work/items.tsv` | 73 条（定义/定理/命题/引理/推论/猜想/注）+ 节 + 原文页 + chunk |

## 1. 定轨道

按原文节切 8 条 track（见 `taxonomy.md`），不按环境类型切：
定义 1（§3）与命题 1（§3）同属几何退化这一条论证线，拆开反而看不到依赖。
§1 是纲领，无条款卡，只留 `00-速览` 里的一句话定位与「已证 vs 猜想」表。

## 2. 一条编号一张卡

- 定义 23、定理 4、命题 15、引理 3、推论 1、猜想 5、注 22 → 73 张 `concept` / `remark` 卡。
- **注不并入相邻定理**：注 19（$\mathcal{O}'_Y$）、注 21（截断 theta 级数）都承载独立技术约定，
  并进去会让「陈述」变成两件事。
- 卡片 id 用 `kind-slug`：`dfn-07-nonunital-a-inf-pre-category`、`thm-02-morse-de-rham-equivalence`，
  slug 描述**内容**不描述编号，编号在 `kind_no` 里。

## 3. 写卡顺序（每张卡）

1. 读 `源码/chunks/chNN.tex` 对应行区间 → 得到译本措辞（已核对过原文图版）。
2. 用 `pages/pNNN.png`（160 dpi 图像）**再看一眼公式**：译本可能已把原文笔误改对，
   卡片要写「现在正确的形式」，并在 `pitfalls` 里提原文拼法。
3. `statement` 用 LaTeX 重排，**禁用译注本自定义宏**，一律 `\mathbb` / `\mathcal` / `\operatorname`。
4. `proof.status`：原文给了完整证明 → `complete`；只给思路 → `sketch` + `gap_note`；
   定义/注/猜想 → `none`。
5. `pitfalls` 至少一条，写**真会错的地方**（缺失的假设、容易误读的下标、跨页截断的条件）。
6. `sources.pages` 写真页码；跨页时在 `provenance_note` 注明续页。

## 4. 校验

```bash
python tools/lint_cards.py cards --strict   # 0 error 才能提交
python tools/build_index.py                 # 重建 index.jsonl
python tools/render_md.py                   # 重建 md/
```

`lint_cards.py` 会回查 `anchor` 指向的真实文件与行区间——锚点写错、文件改名、行号漂移都会报错，
这是本库防止「卡与文本脱钩」的主要手段。

## 5. 已知的坑（制作时踩过）

- **原文页码不是译本页码**：`items.tsv` 早期版本列序是「译本页 / 原文页」，处理时踩过一次，
  凡看到页码先确认是哪一侧。
- **原文题头无句点**：`Theorem 1 There exists …`，正则若要求 `Theorem 1.` 会漏掉全部定理页。
- **注 18 在文字层被打散**：原文 p46 处 OCR 层是 `RemarkP 18`，只能从图像确认；
  卡片照常建，`provenance_note` 说明来源为图像。
- **定义 13 的 $k/n$**：原文写 $\mathcal{C}_0=\mathcal{D}$、$0\le i\le k-1$，与上下文不合；
  译本已按数学意义改为 $\mathcal{C}_n=\mathcal{D}$、$0\le i\le n-1$，卡片写改后形式并记原文拼法。
- **pandoc 等宽字体缺制表符字形**：ASCII 图可以，▼│├ 会掉字。
