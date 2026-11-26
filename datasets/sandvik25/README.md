# Sandvik《Arkhipov–Bezrukavnikov 等价》资料卡（sandvik25）

**一句话定位**：这是 Colton Sandvik《The Arkhipov–Bezrukavnikov Equivalence》（BunG 讨论班报告，2025-01-29，**13 页**）的中文资料卡。报告用五节、13 页把 Arkhipov–Bezrukavnikov 等价讲成一条完整的链：反球模的三条路线 → 中心层与 Wakimoto 层 → Springer 解消上的凝聚层与三造函子 $F_1,F_2,F$ → Iwahori–Whittaker 侧的最高权结构与平均函子 → 主等价 $F^{\mathrm{IW}}$。本包把它拆成 **27 张卡（21 概念 + 6 推导）**，与同目录配套的中译本（`08_source_code/SY02-40_...`）逐页对齐。

## 一张卡只回答一个问题

- **概念卡**三问：这是什么？为什么需要它？哪里容易讲错？
- **推导卡**两问：这条推导怎么走通？每一步凭什么（原文写了什么，哪里是我们补的）？

## 底本与规模

- **A** = Colton Sandvik, *The Arkhipov–Bezrukavnikov Equivalence*, BunG Seminar, 2025-01-29，**印刷页 1–13**（底本 PDF 页 = 印刷页，偏移 0）。引用一律写印刷页。
- **B** = 白名单二次文献（nLab、Stacks Project）与本库译注；**C** = 原始文献（[ArBe] Arkhipov–Bezrukavnikov, *Israel J. Math.* **170** (2009), 135–183；[AcRi] Achar–Riche, *Central Sheaves on Affine Flag Varieties*；[BNP] Ben-Zvi–Nadler–Preygel, *Compos. Math.* **153** (2017), 1908–1944；[Gai1] Gaitsgory, *Invent. Math.* **144** (2001), 253–280；[Gai2] Gaitsgory, *Pure Appl. Math. Q.* **16** (2020), 775–904）。
- 规模：**27 张 = 21 概念卡 + 6 推导卡**，全部 `status: "dev"`、`rights: "rewritten"`。
- 底本没有 LaTeX 源码；PDF 文本层可抽取（13 页、26,992 字符），全部引文均已对回原 PDF 页核对。

## 30 秒入口

| 想看什么 | 打开 |
| --- | --- |
| 全包骨架与三条阅读路径 | `MAP.md` |
| 按轨道浏览全部卡 | `md/index.md` |
| 机器可读轻量索引 | `index.jsonl` |
| 概念卡样例 | `cards/concepts/three-categorifications.json`、`central-affine-grassmannian.json`、`iw-highest-weight.json` |
| 推导卡样例 | `cards/derivations/nearby-cycles-to-central.json`、`fully-faithful-hom.json` |

## 三条阅读路径

1. **只想懂主定理在说什么**（约 12 分钟）：`three-categorifications` → `ab-equivalence-theorem` → `functor-fiw` → `five-categories`。
2. **想懂证明怎么走**：`antispherical-module` → `nearby-cycles` → `central-affine-grassmannian` → `gaitsgory-central-functor` → `wakimoto-filtration` → `springer-resolution` → `functor-f1` → `functor-f2` → `functor-f3` → `iw-category` → `iw-averaging` → `functor-fiw` → `fully-faithful-hom`。
3. **只关心「几何朗兰兹里为什么冒出凝聚层」**：`springer-resolution` → `hat-n-x` → `functor-f3` → `five-categories`。

## 术语

与 `08_source_code/SY02-40_.../工程文件/work/glossary.tsv` 同一份冻结表。三条硬约定：

- `antispherical` 一律译「反球」：球（spherical）情形取平凡表示、反球情形取符号表示，两者是 Hecke 模的对偶。不译「反对称」。
- `Iwahori–Whittaker` 保留原词，缩写 `IW`；`Wakimoto` 保留原词。
- 「中心层」专指 $Z(\mathcal F)$ 的像，不是「中心的层」；`tilting` 译「倾斜层」（不译「可倾斜」）。

## 生产与校验

```bash
python tools/lint_cards.py cards --strict   # 字段、id、related、anchor、页码范围
python tools/build_index.py                 # 重建 index.jsonl
python tools/render_md.py                   # 重建 md/
```

生成器在 `workflow/`：`gen_cards.py`（共用字段与写盘）、`cards_o.py`、`cards_a.py`、`cards_b.py`、`cards_c.py`、`cards_d.py`、`cards_deriv.py`。改卡请改生成器后重跑，不要手改 JSON。

## 权利

`rights: "rewritten"`：所有中文表述、定义重写、评注与 `why` 均为本库自撰；底本 PDF 不入库，卡内只引用页码与短句。底本为讨论班报告（作者个人网页可公开下载），中译注本另见 `08_source_code/SY02-40_...`，登记于 `RELEASE_REGISTER.csv`。
