# 生产流程：gaits04

本目录的卡不是手写的散件，而是从**已完成的译注本**里裁出来的：先有逐句译文与源码行号，再有卡；卡的每条定义都能回到 `ch12_sec*.tex` 的某几行。

## 1. 前置

- 译本工程 `08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/` 已完成：`源码/`（TeX）、`成品/`（PDF，不随仓）、`工程文件/`（通读笔记、疑点清单、术语表、公式核对记录）。
- 读 `MEMORANDUM_01_论证精读与语料生产.md`，并按 `tools/check_memo_gate.py --role lead --record` 登记回执。

## 2. 切卡

1. **定骨架**：按原书 §1–§4 的实际论证单元切分（不是按页切），得到 23 个概念。
   §2.2（除子类）太薄，并入 `bun-bijection` 的要点，不单列。
2. **取锚点**：对每个概念，在 `ch12_sec{1,2,3}.tex` 里量出它占据的行号区间，写成
   `ch12_sec2.tex:24-50（§2.3–§2.4）`。锚点是行号，不是页码——页码会随重排而失效。
3. **定页**：原书页写进 `pages`，`pdf_pages` 由脚本统一 +2（底本 PDF 页 = 原书页 + 2）。
4. **写卡**：字段见 [../SCHEMA.md](../SCHEMA.md)。顺序固定为
   一句话 → 问题 → 定义（自足） → 记号 → 要点 → 公式 → 定理 → 易错点 → 批注 → 相关 → 来源。
5. **配批注**：每卡至少一条。译本里的 8 条译注按主题映射到 `satake`、`unramified-lisse`、
   `bun-bijection`、`hecke-correspondence`、`bun-stack`、`eigensheaf`、`sheaf-function`、
   `character-sheaf` 八卡；其余卡按「读者会错在哪」补写具体的一条。

## 3. 校验与产物

```bash
python tools/make_cards.py --check   # 只校验：字段、related 可解析、pages/pdf_pages 对齐、批注类型
python tools/make_cards.py           # 校验并重写 cards/ md/ index.jsonl verification.jsonl taxonomy.md MAP.md
```

校验器是同目录的 `make_cards.py`：数据在 `cards_1.py`（O/A/B，12 张）与 `cards_2.py`（C/D/E，11 张），
`make_cards.py` 只负责汇总与渲染，**不手改产物**——要改就改数据文件再重跑。

## 4. 核验状态

- 全部 `verification.status = source-only`：指「已与底本页图、译文源码逐条对照」，不等于外部确认。
- 升级到 `external-confirmed` 的做法：对每张卡的定义与公式，在 nLab / Stacks Project / 原始论文中找到对应陈述，
  把来源与结论写进 `verification.checks`，再改 `status`；只有 `external-confirmed` 才能标 `published`。

## 5. 已知缺口

- 定理卡只覆盖原书两个带证明的命题/引理（1.5、2.4）与两个陈述（2.6、3.4 后的猜想）；其余定理以要点形式散在概念卡里。
- 未做外部核验（见 §4）。
- 未收录 §2.7 插叙（模曲线上的 Hecke 对应）为独立卡：它只是类比，已在 `hecke-operator` 的批注里点出。
