# kshms · Kontsevich–Soibelman《同调镜像对称与环面纤维化》资料卡

一篇论文的**可检索知识库**：把 66 页原文里每一个编号条款（定义、定理、命题、引理、推论、猜想、注）
拆成一张独立的卡，附主旨、公式、易错点、原文页码与译本锚点，供人检索、供模型取用。

- 底本：M. Kontsevich, Y. Soibelman, *Homological mirror symmetry and torus fibrations*,
  arXiv:math/0011041v2 [math.SG], 4 Jun 2001, 66 页，无摘要。
- 译本：数译工程 **SY01-25** 中文译注本（58 页，译注 47 条，术语表 213 条），
  源码见 [`08_source_code/SY01-25_同调镜像对称与环面纤维化/`](../../08_source_code/SY01-25_同调镜像对称与环面纤维化/)。
- 规模：**83 张卡** = 条款卡 73（定义 23、定理 4、命题 15、引理 3、推论 1、猜想 5、注 22）
  + 原文勘误卡 10。

## 怎么用

| 想做的事 | 打开 |
| --- | --- |
| 先看这篇论文说了什么 | [`md/README.md`](md/README.md)（按 8 条轨道分组的总表） |
| 查某条定理的陈述与证明 | [`index.jsonl`](index.jsonl) 搜 `thm-`；或直接看 `md/<slug>.md` |
| 确认某条是「已证」还是「猜想」 | 卡的 `proof.status`（`complete` / `sketch` / `none`）；`00-速览` 有对照表 |
| 看原文与译本怎么对位 | [`MAP.md`](MAP.md) |
| 了解分轨与编号规则 | [`taxonomy.md`](taxonomy.md) |
| 引用文献 | [`SOURCES.md`](SOURCES.md) |
| 自己再造一个这样的数据集 | [`workflow/PRODUCTION.md`](workflow/PRODUCTION.md) |

## 卡片规格

一卡一 JSON，放在 `cards/{concepts,remarks,corrections}/`。字段见 [`SCHEMA.md`](SCHEMA.md)，要点：

- `id` 形如 `kshms/concept/dfn-07-nonunital-a-inf-pre-category`；`kind_no` **照抄原文编号**，
  原文每类环境各自连续编号、不带节号，本库不重排、不重编号。
- `statement` 是可独立阅读的完整陈述，公式用 `\mathbb` / `\mathcal` / `\operatorname` 展开，
  **不使用任何译本自定义宏**——这样卡片粘到别处也能编译。
- `proof.status` 三值：`complete`（原文给了完整证明）、`sketch`（只给思路，`gap_note` 指出缺口）、
  `none`（定义/注/猜想，本不该有证明）。猜想卡必须是 `none`。
- `pitfalls` 至少一条，写**真会错的地方**，不是套话。
- `sources[].pages` 是**原文页码**；`sources[].anchor` 指向译本 LaTeX 源码的行区间，可回查措辞。
- `rights` 一律 `rewritten`：卡里的陈述是按原文重写的，不是逐句翻译。

## 三条轨道之外的说明

- 原文的**注**单独成卡，不并入相邻定理：注 19（$\mathcal{O}'_Y$ 的分类）、注 21（截断 theta 级数）
  都承载独立技术约定。
- **原文勘误不写进陈述**：10 条笔误单列在 `cards/corrections/`，陈述里用更正后的形式，
  并在卡的 `statement`/`pitfalls` 中注明原文拼法。
- 论文体裁的处理：本库不写「章节导读」式的长文，只写卡；论文的**纲领性**（大量「我们猜想」）
  由 `00-速览` 的「已证 vs 猜想」表与每张猜想卡的 `pitfalls` 双重标出，避免把纲领读成定理。

## 校验

```bash
python tools/lint_cards.py cards --strict   # 当前 83 张：0 error / 0 warning
python tools/build_index.py                 # 重建 index.jsonl
python tools/render_md.py                   # 重建 md/
```

`lint_cards.py` 会回查每个 `anchor` 指向的真实文件与行区间，防止卡与文本脱钩。
