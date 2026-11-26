# Raskin《上同调类域论》资料卡

Sam Raskin 讲授、Oron Propp 整理的 *Lectures on Cohomological Class Field Theory*（MIT 18.786，2016 年春课程讲义，119 页 / 23 讲，公开讲义、未正式出版）中文译本《上同调类域论讲义》（91 页）的**可检索、可自测**资料卡。

一张卡只回答一个问题：**概念卡**回答「这是什么、为什么需要、哪里会错」，**推导卡**回答「这条论证怎么一步步走通、每步凭什么」，**勘误卡**回答「底本哪里印错、为什么必须改、译文怎么处理」。

- 底本：公开课程讲义原 PDF（MIT OCW 版），印刷页 **1–115**；卡中的「原书 p.N」一律指印刷页，不是中文译本的页序（物理页 = 印刷页 + 4）。
- 材料：91 页中文译注本（2026-11-26 校对轮后的版本）。译稿正文**不入库**，只把其中的数学结论与校订结论裁成卡。
- 规模：**27 张卡**——概念 12、推导 5、勘误 10；五轨 A 7 / B 8 / C 5 / D 1 / E 6；印刷页 1–107 中覆盖 81 页；27 个推导步骤、22 条定理陈述、70 条 pitfalls、13 条 gaps。
- 权利：全部 `rights: "rewritten"`，自产部分 CC BY 4.0；不收录讲义原文；单处引文 ≤ 60 字并注出处。

## 30 秒入口

| 想做什么 | 打开 |
|---|---|
| 看全书骨架与每讲要覆盖什么 | [MAP.md](MAP.md) |
| 按类型、轨道浏览 | [md/index.md](md/index.md) |
| 按 id / 页码检索 | [index.jsonl](index.jsonl) |
| 字段规范与两个可抄的样例 | [SCHEMA.md](SCHEMA.md) |
| 写卡前先看流程与禁区 | [workflow/PRODUCTION.md](workflow/PRODUCTION.md) |

## 五条轨道

| 轨道 | 主题 | 讲 |
|---|---|---|
| `A` | 局部类域论与希尔伯特符号（`n=2` 的完整图景） | 第 1–5 讲 |
| `B` | 同调代数工具（长正合列、Tate 上同调、Herbrand 商、Hilbert 90） | 第 6–12 讲 |
| `C` | 无界复形的 Tate 上同调与消没定理 | 第 13–17 讲 |
| `D` | 范数群、Kummer 理论与存在定理 | 第 18 讲 |
| `E` | 布劳尔群、两个不等式与 gcft 主定理 | 第 19–23 讲 |

轨道只是检索维度：一张卡只落一个 track，跨讲的内容放进 `related`，不重复落卡。
`D` 本版只落 1 张（`kummer-duality`）：第 18 讲的存在定理已并入 `norm-group` 概念卡，其余内容分散在 B/C 两轨。

## 目录结构

```
raskin_lcft/
├── SCHEMA.md                     # 卡片字段规范
├── README.md                     # 本文件
├── MAP.md                        # 讲次 → 覆盖矩阵
├── index.jsonl                   # 机器索引（build_index.py 生成）
├── cards/
│   ├── concepts/                 # 概念卡 12
│   ├── derivations/              # 推导卡 5
│   └── corrections/              # 勘误卡 10
├── md/                           # 渲染版（render_md.py 生成）
│   ├── concepts/ derivations/ corrections/
│   └── index.md
├── tools/
│   ├── lint_cards.py             # 字段 / 长度 / id / 页码 / 路径检查
│   ├── build_index.py            # 重建 index.jsonl
│   └── render_md.py              # 重建 md/
└── workflow/
    └── PRODUCTION.md             # 生产流程、取材原则、禁止事项
```

## 版权与合规

- **底本**：Raskin 讲授、Propp 记录的 MIT 18.786 课程讲义（2016 年春），经 MIT OCW 公开，未正式出版。讲义著作权归作者；本数据集不主张讲义原文的任何权利。
- **卡片是转述**：定义、证明、要点一律用**自己的话**重写，`rights: "rewritten"`；不复制讲义段落，也不整段搬用译稿正文。
- **引用上限**：确需引用时单处 ≤ 60 字，注明页码；累计不超过单卡正文的 10%。
- **数学事实**不受版权保护；数据集只主张自产部分（中文转述、推导整理、术语裁决、勘误记录）的 CC BY 4.0。
- 权利人如有异议，撤下对应卡片即可，不影响其余部分。
- 底本 PDF、页面图与 OCR 中间产物**一律不入库**（库规 L4）。

## 质检

```bash
python tools/lint_cards.py cards --strict     # 0 error 才算过
python tools/build_index.py                   # 重建 index.jsonl
python tools/render_md.py                     # 重建 md/
```

三条命令都用标准库，不需要额外依赖；空 `cards/` 下 lint 返回 0 error，`index.jsonl` 为空文件。

## 如何贡献

1. **一卡一文件**：新建 `cards/<类型>/<slug>.json`，文件名与 id 末段一致；字段照 [SCHEMA.md](SCHEMA.md)。
2. **先定轨再写**：看 [MAP.md](MAP.md) 里该讲归哪个 track，别把第 6 讲的长正合列写成第 20 讲的伊代尔卡。
3. **`related` 不许悬空**：新卡引用的 id 必须已经存在，或同批一起提交；分批写卡时用 `--allow-missing` 做中途检查。
4. **勘误卡要给依据**：`why` 写讲义原句、数学推导或标准文献的结论，不写「更通顺」。本数据集的勘误都经过与原 PDF 逐页核对。
5. **提交前跑三道门禁**，并把 `status` 保持 `draft`，直到有人逐卡复核。

## 统计

| 项 | 数值 |
|---|---|
| 卡片总数 | 27（概念 12 / 推导 5 / 勘误 10） |
| track 分布 | A 7、B 8、C 5、D 1、E 6 |
| 页码覆盖 | 印刷页 1–107 中 81 页（未落卡为过渡段、图示页与习题引用页） |
| 推导步骤 | 27 步（每步带 `locator` 与 `provenance` A/B/C），另有 13 条 `gaps` |
| 定理陈述 | 22 条（`proof.status` 为 complete / sketch / none，sketch 均带 `gap_note`） |
| 踩坑记录 | 70 条 `pitfalls` |
| 质检 | `lint_cards.py cards --strict`：**0 error，0 warn**；`index.jsonl` 27 条；`md/` 27 张卡 + index.md |

（本节的数字由 `index.jsonl` 与卡片文件统计而来，改动卡片后请重跑三道门禁并同步本节。）

## 与工程目录的关系

卡片只裁数学与校订结论；底本信息、编译记录、术语表（109 条）、22 条原文疑误的逐条出处见
`08_source_code/SY99-04_上同调类域论（Raskin 讲义）/`：

- `工程文件/REPORT.md`：交付记录、校对轮方法与统计
- `工程文件/ERRATA.md`：29 条校订（22 疑误 + 4 图复原 + 2 原注 + 1 已核），带讲次与译稿行号
- `资料卡/01-结果清单.md`：按 23 讲列出全部 208 条陈述与印刷页
- `资料卡/02-证明骨架.md`：八个主论证的骨架与四处图复原对照
