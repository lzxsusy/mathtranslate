# gw06 资料卡：Gukov–Witten《规范理论、分歧与几何朗兰兹纲领》中译校订

> 语言：中文。底本：Sergei Gukov, Edward Witten, *Gauge Theory, Ramification, And The Geometric Langlands Program*,
> arXiv:hep-th/0612073v2（160 页，2006）。中译校订本：`08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/`。
> 本数据集只发布改写后的卡片，不发布原书、译文全文或 PDF。

## 1. 规模

- **73 张卡**：55 张概念卡（覆盖 §1–§6 与附录 A 全部小节）+ 18 张勘误卡。
- 每张卡至少 3 条批注（`易错预警` / `含糊点拨` / `背景直觉` 各一），全部带锚点。
- 中译校订新增译注 156 条（库内 `\begin{yizhu}` 由 78 条增至 234 条），其中 [原文疑误] 条目由 14 条增至 24 条；
  18 张勘误卡是其中可独立成卡的代表，`original` / `corrected` 只保留差异片段。

## 2. 文件

```
datasets/gw06/
├── cards/concepts/*.json       # 55 张概念卡
├── cards/corrections/*.json    # 18 张勘误卡
├── index.jsonl                 # 逐卡摘要索引
├── verification.jsonl          # 核验台账
├── md/*.md                     # 人读渲染
├── taxonomy.md                 # 按节分类
├── MAP.md                      # 卡片地图（节 | 类型 | 标题 | 锚点）
├── SCHEMA.md                   # 字段规范
├── README.md
├── workflow/PRODUCTION.md      # 校订与写卡流水线
└── tools/
    ├── make_cards.py           # 校验与生成（--check / --strict / --allow-missing-related）
    ├── check_pages.py          # 页码与锚点硬查
    └── section_index.json      # 各节标题行号（写卡锚点基线）
```

## 3. 复跑

```bash
cd datasets/gw06/tools
python make_cards.py --check                     # 只校验
python make_cards.py --strict                    # 警告也算失败
python make_cards.py                             # 校验并重写 index.jsonl、verification.jsonl、md/、MAP.md、taxonomy.md
python check_pages.py                            # pdf_pages == pages + 1、anchor 存在性
```

校验覆盖：id 唯一与前缀、必填字段、track 匹配 `§N[.M]` / `附录A|B`、summary ≤ 120 汉字、
question 问号结尾、annotations 三型且带 title、text ≥ 40 汉字、related ≥ 2 且可解析、自指禁止、
rights/status/verification 取值、`pdf_pages == pages + 1`、anchor 文件存在且行号在文件内、
勘误卡 `corrected` 片段必须落在 anchor 行区间内。

## 4. 权利与核验

- `rights: "rewritten"`：所有定义、解释与批注均为校订时重写，不复制原文或译文长句；单处引文仅保留必要的差异片段。
- `verification.status: "source-only"`：逐段对照 arXiv:hep-th/0612073v2 的 `pdftotext` 文本、按数学自洽复核并用 xelatex 重编译；
  **未取得 Curr. Dev. Math. 2006 印刷本页面图像**，故一律不标 `published`。
- `sources.pages` 用**印刷页码**，`pdf_pages = pages + 1`（arXiv 版 PDF 第 1 页是封面）。
- 锚点指向 `08_source_code/SY02-06_…/源码/sections/sNN*.tex:A-B`；若后续再改分片，须重跑 `make_cards.py` 与 `check_pages.py` 并更新锚点。

## 5. 与本轮校订的关系

- 14 个中文分片逐一对照 16 个英文切片（`ramified.tex` 的节界切分）复核，日志随校订记录存放（不入数据集）：
  764 段、262 个编号公式、P1 改动 4 处、P2 改动 34 处、存疑 29 条。
- P1 四处：`real codimension` 吞词（§3.1）、`sec:2.4` 误引（实为 §2.5）、`more than one point` 的量词、
  `semi-simple` 译作「单」（§4.6）。
- 18 张勘误卡是上述改动的可独立条目，不替代逐片日志；概念卡锚到校订后的分片行号。

## 6. 已知边界

- `two-dimensional-defect` 卡对极大列维情形的 $\xi\in H^2(D,\pi_1(G))$ 解释是标准图景补全，原文只一句，建议第三轮复核。
- `cameral-cover` 卡的一般 $G$ 部分（$|W|$ 重覆盖、Prym）依外部标准结果写入，可逐字核验的只有 $SL(2)$ 谱曲线与 (3.107)–(3.109)。
- §5.3 的 (5.10)–(5.14) 目前无专属卡；如需补齐可加一张推导卡。
