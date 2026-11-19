# gaits04 —《几何朗兰兹的非正式导论》资料卡

D. Gaitsgory《几何朗兰兹的非正式导论》（Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281）的**概念卡**数据集，与译本工程 [SY02-13](../../08_source_code/) 同批产出。

- 底本：13 页（原书 269–281 = PDF 271–283），四节一附录。
- 卡片：**23 张概念卡**，六轨（O/A/B/C/D/E）。
- 批注：**每卡至少一条**，共 23 条，类型限「易错预警 / 含糊点拨 / 背景直觉」——对应译本里的 8 条译注，并补足逐卡的具体提醒。
- 锚点：每卡指向中译本 `源码/chapters/ch12_sec*.tex` 的确切行号区间；无锚点不入库。
- 状态：全部 `reviewed` + `verification: source-only`（只与底本页图逐条对照，未做外部独立核验）。按本库规则，`source-only` 不得标 `published`。

## 六轨

| 轨 | 名称 | 张数 | 内容 |
|---|---|---|---|
| O | 总览 | 1 | 全章论证地图：函数 → 向量丛 → 层 |
| A | 阿代尔与球表示 | 7 | 阿代尔环、光滑函数、整阿代尔、局部 Hecke 代数、球表示、Satake、整体 Hecke 代数 |
| B | 尖点与 Langlands 对应 | 4 | 尖点函数、多重度一定理、无分歧 ↔ lisse 层、Lafforgue 定理 |
| C | 向量丛与 Hecke | 4 | 双商 ↔ 向量丛、Hecke 对应与 Grassmann 纤维、Hecke 算子、常项算子 |
| D | 层化与猜想 | 5 | 模叠、局部 Hecke 函子、大 Hecke 叠、Hecke 本征层与猜想、为何限于球情形 |
| E | 附录：层-函数对应 | 2 | Grothendieck 层-函数对应、特征层与 Lang 同态 |

## 用法

```bash
cd datasets/gaits04
python tools/make_cards.py --check   # 只校验
python tools/make_cards.py           # 重写 cards/、md/、index.jsonl、verification.jsonl、taxonomy.md、MAP.md
```

产物：

- `cards/concepts/*.json` — 一卡一文件，字段见 [SCHEMA.md](SCHEMA.md)。
- `index.jsonl` — 逐卡一行：id / track / title / summary / question / status / verification / path。
- `verification.jsonl` — 逐卡核验台账（`basis` 说明依据）。
- `md/*.md` — 渲染版，供人直接读；`[[slug]]` 表示相关卡。
- `taxonomy.md`、`MAP.md` — 分类视图与卡片地图（含原书页）。

## 权利

全部卡片 `rights: "rewritten"`：用自己的话重写的事实与结构，不复制原书表达与图；术语与定义的中文表述取自已发布的译本。单处引文 ≤ 60 字并注出处。
底本为在版图书，**译本 PDF 不随仓发布**（见根目录 `RELEASE_REGISTER.csv` 中 SY02-13 行：成品不公开）。

## 出处

- 译本工程：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/`
- 原书：J. Bernstein, S. Gelbart (eds.), *An Introduction to the Langlands Program*, Birkhäuser, 2004, Chapter 12.
- 核验方式：逐卡对照 150 dpi 原书页图与译文源码；公式逐符号核对（见工程 `work/公式核对记录.md`）。
