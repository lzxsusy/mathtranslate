# 格拉斯曼精读资料卡

*Grassmannians, Moduli Spaces and Vector Bundles*（Clay Mathematics Proceedings 14，AMS/Clay 2011；9 篇独立论文，中译本 170 页）的**可检索、可自测、可打印**资料卡。

一张卡只回答一个问题：**概念卡**回答「这是什么、为什么需要、哪里会错」，**例子卡**回答「这条定义/公式具体怎么算」。

- 底本：中译本（9 篇论文，中文源 `source/chapters/ch01–09.tex`）；原文 Clay 14，英文 PDF 页 = 原书页 + 9。
- 规模：**90 张**——73 张概念卡 + 17 张例子卡；九条章轨（1–9）+ 一条跨章基础轨（A）。
- 权利：全部 `rights: "rewritten"`。文字是用自己的话改写的，公式照录，出处逐条标中译页 / 英文 PDF 页与 TeX 锚点；**不收录原文段落**。

## 30 秒入口

| 想做什么 | 打开 |
|---|---|
| 看全书骨架与三条阅读路线 | [MAP.md](MAP.md) |
| 按轨道浏览 | [md/INDEX.md](md/INDEX.md) |
| 按 id / 页码检索 | [index.jsonl](index.jsonl) |
| 看一张概念卡长什么样 | [md/concepts/gv-sheaf.md](md/concepts/gv-sheaf.md) |
| 看一张例子卡长什么样 | [md/examples/factorization-along-a-curve.md](md/examples/factorization-along-a-curve.md) |
| 字段规范 | [SCHEMA.md](SCHEMA.md) |
| 轨道划分与全量清单 | [taxonomy.md](taxonomy.md) |

## 十条轨道

| 轨道 | 主题 | 概念卡 | 例子卡 |
|---|---|---|---|
| A | 跨章基础：Koszul 上同调、仿射 Grassmannian、GV-层、凝聚系 | 3 | 0 |
| 1 | Hitchin 的射影平坦联络、Toeplitz 算子与 TQFT 曲线算子的渐近展开 | 8 | 2 |
| 2 | Koszul 上同调及其在模空间中的应用 | 11 | 3 |
| 3 | Reider 定理与 Thaddeus 对再探 | 7 | 2 |
| 4 | 丛的奇异模空间中的相交配对 | 6 | 1 |
| 5 | Beilinson–Drinfeld 格拉斯曼流形与辛纽结同调 | 7 | 2 |
| 6 | 曲线上层的模空间的算术方面 | 8 | 2 |
| 7 | 代数曲线上 $\alpha$-稳定凝聚系的存在性 | 9 | 2 |
| 8 | 阿贝尔簇上的正则性 III：与一般消没的关系及应用 | 8 | 2 |
| 9 | 可约曲线上的向量丛及应用 | 6 | 1 |

## 资料卡怎么用

### 概念卡：七步

1. **先自测**：遮住正文，只读卡片正面的 `question`，用 30 秒口述答案。
2. **读定义**：`definition.text` 是改写后的精确表述，`definition.notation` 固定记号；先确认每个符号指什么。
3. **过要点**：`key_points` 是 4–5 条「必须记住的句子」，不是证明。
4. **推公式**：`formulas` 里的式子自己推一遍，尤其是余维、次数、符号与 $\pm$ 的位置。
5. **读证明**：`theorems[].proof.steps` 每步都有 `why`；`sketch` 的卡在 `gap_note` 说明书中省了什么，`reference` 的卡只指出处。
6. **看坑**：`pitfalls` 是真正会错的地方（余维下界写成严格、把 $\mathbb{P}^1$ 接桥当成点对粘合、把 $E_\infty$ 写成 $E_p$ 之类），优先于背结论。
7. **跳相关卡**：`related` 指向同一条轨道的前后卡，也指跨章的工具卡；例子卡在 `concept_refs` 里反向指回。

### 例子卡：四步

1. 读 `setup`，自己先列已知量与目标量。
2. 遮住 `computation`，独立算一遍；再逐步对照，重点是每步凭什么。
3. 用同组概念卡复核（代回、特例、维数、$S$ 矩阵正交归一），不要只看结果。
4. 回到 `concept_refs` 指向的概念卡，把这道题挂回框架。

## 这些卡是怎么做出来的

1. **九章并行精读**：九个子读者各读一章（中译 + 英文 PDF 对读 + TeX 源定位），每章交付六件套——导读（≥1200 字）、批注（≥12 条，五类：数学-难点 / 数学-补证 / 译注-核对 / 译文-问题 / 联系-他章）、errata（10 列 TSV）、笔记（≥1500 字）、卡片候选（≥7 条，逐条给 `chapters/chNN.tex:行号`）、章报告（含存疑清单）。
2. **候选去重与分轨**：89 行候选 → 剔除与种子卡重复的 2 条 → 87 条，按「A 基础 + 章号」分轨，按甲（A+1+3）/乙（2+7）/丙（5+8）/丁（4+6+9）分四组。
3. **四组卡手并行成卡**：每张卡都回 `chNN.tex` 的 anchor ±60–120 行读原文，写定义、要点、公式、定理（complete 步骤带 `why`，sketch 必带 `gap_note`）、坑、关联卡与出处；跨组至少链一张。
4. **机器闸门**：`validate_cards.py --strict` 0 error（id/长度/anchor 行号真实存在/related 可解析/例子卡 `concept_refs`），`build_index.py` 生成 `index.jsonl` 与 `md/INDEX.md`。

整本书的精读与审校产物（9 章导读、159 条批注、58 条 errata、9 章笔记）在配套工程 `Grassmannians-精读/` 下；过程记录见发布仓库 `09_thinking/chains/GRASSMANN_2026-11-25_九章精读流水线.md`。

## 质检

```bash
python tools/validate_cards.py --strict   # 字段/长度/anchor 行号/related/例子卡，0 error 才算过
python tools/build_index.py               # 重建 index.jsonl 与 md/INDEX.md
python tools/render_md.py                 # 重建 md/concepts/*.md、md/examples/*.md
```

`validate_cards.py` 会真的去 `Grassmannians-精读/source/chapters/chNN.tex` 数行数，确认 anchor 的行号落在文件里且不是空行；换书或改行号后必须重跑。

## 目录结构

```
_cards_grassmann/
├── README.md                  # 本文件
├── MAP.md                     # 骨架图：三条路线 + 15 条跨章依赖
├── SCHEMA.md                  # 卡片 JSON 规范（含完整示例）
├── taxonomy.md                # 十轨划分与 90 张全量清单
├── cards/concepts/*.json      # 73 张概念卡
├── cards/examples/*.json      # 17 张例子卡
├── md/INDEX.md                # 按轨道的总索引（生成）
├── md/concepts/*.md           # 渲染版概念卡（生成）
├── md/examples/*.md           # 渲染版例子卡（生成）
├── index.jsonl                # 一行一张卡的检索索引（生成）
├── tools/                     # validate_cards / build_index / render_md
└── workflow/PRODUCTION.md     # 卡手的生产协议（每张卡读什么、写到什么程度）
```

## 约定

- `track`：`A` 是跨章基础；`1`–`9` 对应第 1–9 篇论文。
- `sources.pages_zh` 是中译页（`zh-译文.pdf` 页序），`pages_en` 是英文 PDF 页（= 原书页 + 9）；ch4 实测中译 = 原书 + 2，ch9 页脚印刷号 = 中译 PDF − 6，卡片一律用 PDF 页口径。
- 卡片内容以**中译本**为准；发现译文与英文原文不符时，结论不进卡片，记到工程的 `产出/批注/chNN-errata.tsv`（全书 58 条，high 2 条）。
- 新增或修改卡片后：先改 `cards/` 里的 JSON，再跑 `validate_cards.py --strict`、`build_index.py`、`render_md.py`，三者都过再提交。
