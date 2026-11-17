# csw · Chern–Simons 理论与共形场论资料卡

把 **Witten 1989（CMP 121, 351–399）** 那篇文章里散落的定义、定理、推导与陷阱，拆成可检索、可校验、可复用的「资料卡」。它是 [`papers/WIT-1989-JONES`](../../papers/WIT-1989-JONES/README.md) 研讨班与讲义的**结构化副产品**：讲义负责连续叙事，资料卡负责“一个概念一张卡、一个定理一条链”。

- **40 张卡** = 31 张概念卡（`cards/concepts/`）+ 9 张例子卡（`cards/examples/`）
- **索引**：`index.jsonl`（一行一卡）；`md/` 是给人和检索引擎读的渲染版
- **证据**：每张卡都带 `sources`（书/节/印刷页/PDF 页/锚点）与 `proof.status`（complete / sketch + 缺口说明）
- **版权**：全部 `rewritten`——转述与重写，不复制原文；页码只是定位，引用请查原刊

## 怎么用

1. **查定义**：从 `index.jsonl` 或 `taxonomy.md` 找到 `csw/concept/<slug>`，读 `cards/concepts/<slug>.json` 或 `md/concepts/<slug>.md`。
2. **跟推导**：概念卡的 `theorems[].proof.steps` 是“起点→为什么→终点”的三段链，`sketch` 会标 `gap_note`（本文没证、谁补的）。
3. **做计算**：例子卡的 `computation` 步骤 + `check` 是可手算/可脚本复核的数值，例如 $Z(S^3)=S_{00}$、$SU(2)$、$k=2$ 的 $S$ 矩阵。
4. **写作引用**：把 `csw/concept/x` 的 id 当作稳定锚点写进讲义或笔记，比“某书某页”更可追。

## 目录结构

```
datasets/csw/
├── README.md                  # 本文件
├── SCHEMA.md                  # 卡片 JSON 规范（字段/约束/写作规则）
├── taxonomy.md                # 轨道（track）与卡片总表
├── MAP.md                     # 卡与卡之间的依赖图（mermaid）
├── index.jsonl                # 一行一卡的索引
├── cards/concepts/*.json      # 概念卡
├── cards/examples/*.json      # 例子卡
├── md/concepts/*.md           # 渲染版（给人读）
├── md/examples/*.md
├── tools/
│   ├── _data1..5.py           # 卡片源数据（Python 字面量，便于批量改）
│   ├── build_cards.py         # 数据 → cards/*.json + index.jsonl
│   ├── lint_csw.py            # 结构/内容 lint（0 error 才可入库）
│   └── render_md.py           # cards/*.json → md/
└── workflow/
    └── PRODUCTION.md          # 队伍怎么构造、怎么评审、怎么复现
```

## 复现命令（在 `datasets/csw` 下）

```bash
python tools/build_cards.py     # 生成 cards/ 与 index.jsonl
python tools/lint_csw.py        # 必须 0 error、0 warning
python tools/render_md.py       # 生成 md/
```

Windows 上如遇中文乱码，先 `set PYTHONIOENCODING=utf-8`。

## 轨道（track）

| track | 主题 | 卡数 |
| --- | --- | --- |
| O | 总览 | 1 |
| A | 三维理论：作用量、level、Wilson 线 | 3 |
| B | 相空间：约束、辛商、平坦联络模空间 | 4 |
| C | 几何量子化机器：预量子化、极化、全纯截面、半形式 | 6 |
| D | Wilson 线的穿刺点与 Borel–Weil–Bott | 4 |
| E | WZW 一侧：仿射代数、Sugawara、共形块、KZ、融合 | 6 |
| F | 对偶与映射类群 | 2 |
| G | 计算：手术、S 矩阵、Verlinde、Jones | 4 |
| H | 边界：CS/WZW 与 AdS₃/CFT₂ 的区别 | 1 |

明细见 [`taxonomy.md`](taxonomy.md)。

## 与其他产物的关系

- **讲义**（`papers/WIT-1989-JONES/deliverables/lecture/main.pdf`，49 页）：连续叙事，读者从 0 到能自己重述主线。
- **注疏本**（`papers/WIT-1989-JONES/deliverables/reading_note/main.pdf`，97 页）：逐节对照原文，带 G-x/D-x 编号。
- **研讨班记录**（`papers/WIT-1989-JONES/sessions/s1..s6`）：六场 claims/questions 与评分。
- **本资料卡**：把以上三者的“原子断言”抽成机器可读、可引用的卡。

## 队伍怎么构造（摘要）

详见 [`workflow/PRODUCTION.md`](workflow/PRODUCTION.md)：Lead（出题/裁决/集成）+ historian（语境与问题史）+ bibliographer（文献与交叉核对）+ archivist（证据官：锚点抽检）+ verifier（独立评分，读 claims 不读 reports）。每张卡走“起草 → 证据官抽检 → verifier 抽检 → 入库”四步，`proof.status=sketch` 必须写 `gap_note`。

## 贡献与许可

- 卡片内容为改写（`rewritten`），可自由引用，但请保留 `id` 与 `sources`。
- 发现错误请开 issue 或在 `workflow/PRODUCTION.md` 的“纠错”流程里登记；修卡必须同时改 `tools/_data*.py` 并重跑 build/lint。
